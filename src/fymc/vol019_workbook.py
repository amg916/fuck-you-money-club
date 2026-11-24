from __future__ import annotations

def build_volume_019_workbook() -> dict:
    return {'workbook_id': 'wb-019-enterprise-software-reselling',
 'volume_id': 'vol-019-enterprise-software-reselling',
 'title': 'Enterprise Software Reselling — Practitioner Testimony Operator Workbook',
 'subtitle': 'A Field Workbook for Building VAR Margin Stacks, Funding Reseller Channel Programs, Working '
             'Distributors and Marketplaces, Closing Channel Partner Private Offers, and Operating as a '
             'Microsoft CSP',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Margin Stack and Channel Readiness Audit',
                 'purpose': 'Prove the product sells direct, expose where the real margin sits above the '
                            'thin license, define markups and fee stacks in writing, and design a narrow, '
                            'funded reseller program with tiers, payouts priced against direct acquisition '
                            'cost, separate partner CRM fields, and claimed market development money.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Start with the direct sales proof field and stop if direct conversion '
                                  'is not yet repeatable, because no partner will outsell a vendor that '
                                  'cannot sell its own product.',
                                  'Break every customer account into license, implementation, training, '
                                  'customization and support lines so the thin license entry ticket is '
                                  'separated from the services that carry the profit.',
                                  'Write markup definitions, tax lines and implementation ballparks as if '
                                  'a skeptical VAR will read every quote, since hidden fees and unpriced '
                                  'surprises kill partner trust fast.',
                                  'Price partner tiers and payouts against your own funnel cost by stage, '
                                  'and recruit only the partners you can realistically activate instead of '
                                  'collecting hundreds of idle logos.',
                                  'Finish with a dated market development fund claim plan so every '
                                  'approved activity carries evidence and a filing deadline, turning '
                                  'approved budget into an actual payment.'],
                 'fields': [{'name': 'direct_sales_proof',
                             'type': 'textarea',
                             'prompt': 'Document the evidence that your product already sells direct '
                                       'before you recruit any reseller. List closed direct deals, average '
                                       'cycle length, and win rate, and state plainly whether a partner '
                                       'could realistically outsell what your own team achieves today.',
                             'example': 'Phil Morettini warns that no one can sell your product if you '
                                        'cannot [Phil Morettini — L1YsH5QkIus @ 00:02:18], and Willingness '
                                        'to Pay adds that a partner is never going to be better at selling '
                                        'it than you are [Willingness to Pay — _pp2kmBgn7s @ 00:47:03]. '
                                        'Entry: direct closes logged by quarter, win rate tracked, and '
                                        'channel launch held until direct conversion repeats.'},
                            {'name': 'margin_stack',
                             'type': 'textarea',
                             'prompt': 'Break your revenue per customer into the license and every service '
                                       'layered on top: implementation, training, customization, and '
                                       'support. Identify which layer carries the real margin and which '
                                       'layer is merely the thin entry ticket that opens the account.',
                             'example': 'Model the XAPT pattern: a Hungarian VAR that customized Navision '
                                        'for Caterpillar and heavy-equipment dealers posted $14 million '
                                        'pre-tax profit on $24 million revenue, almost 60 percent [Steve '
                                        'Preda — 5n6g3xVFV88 @ 00:04:18]. Record the license line as entry '
                                        'ticket, then price vertical customization as the profit engine, '
                                        'not a discount concession.'},
                            {'name': 'vertical_price_lift',
                             'type': 'text',
                             'prompt': 'Name the vertical where your customization turns a commodity '
                                       'product into a specialist package. State the generic seat price, '
                                       'the customized price you will charge, and the specific industry '
                                       'workflows that justify the multiple to a buyer in that niche.',
                             'example': 'Steve Preda, shopping for an investment-banking CRM around 2010, '
                                        'noticed a firm that customized Salesforce for investment banks '
                                        'and charged 250 per month against 25 per seat for the vanilla '
                                        'package, a tenfold lift [Steve Preda — 5n6g3xVFV88 @ 00:05:29]. '
                                        'Entry: vertical named, generic and customized price recorded, '
                                        'banking workflows listed as justification.'},
                            {'name': 'markup_definition',
                             'type': 'textarea',
                             'prompt': 'Write the exact markup definition you will demand in every quote '
                                       'you receive or issue. Specify whether markup is a percentage over '
                                       'net cost of goods or a shaved OEM discount, and require a '
                                       'broken-out tax line on each quote.',
                             'example': 'Ben Fox of TC2 describes VARs passing a 60 percent OEM discount '
                                        'through as 58 percent, taking the fee by shaving a point or two '
                                        '[Staying Connected — BJPNVL1CIiM @ 00:04:10]. He has seen '
                                        'importation and customs fees disguised as taxes [Staying '
                                        'Connected — BJPNVL1CIiM @ 00:08:17]. Entry: markup stated over '
                                        'net cost, tax and customs listed separately.'},
                            {'name': 'license_fee_stack',
                             'type': 'textarea',
                             'prompt': 'Lay out your complete license stack: setup fee, monthly minimum, '
                                       'usage pricing, and hourly customization rate. Explain how the '
                                       'monthly minimum protects you when a low-usage subscriber would '
                                       'otherwise cost more to invoice than it actually pays you.',
                             'example': 'Stuart Sutton lays out a full stack of setup fees, monthly '
                                        'minimums, usage pricing and per-hour customization, and charges a '
                                        'minimum monthly amount so a subscriber whose usage fees fall '
                                        'below the cost of cutting an invoice still pays its way [Stuart '
                                        'Sutton — yasPH-UlTQo @ 00:08:10]. Entry: setup fee, monthly '
                                        'floor, usage rate and hourly customization rate each listed.'},
                            {'name': 'implementation_ballparks',
                             'type': 'text',
                             'prompt': 'Publish entry, medium, and heavy implementation ballparks with '
                                       'durations and budgetary price ranges your partners can quote '
                                       'before the vendor meets the client. Note how you will avoid a '
                                       'large surprise number landing on a small buyer.',
                             'example': 'Channel Marketing Academy recommends ballparks such as a month '
                                        'and a half, six months and two years, or VARs will not put you in '
                                        'front of clients [Channel Marketing Academy — vLO0gA3TgxE @ '
                                        '00:01:38]. A $50,000 surprise on a $5,000 buyer embarrasses the '
                                        'VAR [Channel Marketing Academy — vLO0gA3TgxE @ 00:02:14]. Entry: '
                                        'three tiers published with ranges.'},
                            {'name': 'partner_tiers',
                             'type': 'textarea',
                             'prompt': 'Define your partner tiers, the margin attached to each tier, the '
                                       'annual quota for the top tier, and any bonus tied to deal '
                                       'registration. Confirm that training is free and that partners face '
                                       'no joining fee or upfront commitment.',
                             'example': "Ted Finch's template runs authorized, gold and platinum tiers at "
                                        '10, 20 and 30 percent margins with a $250K platinum quota and '
                                        "deal-registration bonuses. Iron Software states there's no "
                                        'joining fee and no upfront commitment [Iron Software — '
                                        'lCobx44k0Tw @ 00:00:47]. Entry: three tiers, margins, platinum '
                                        'quota and registration bonus recorded.'},
                            {'name': 'payout_vs_cac',
                             'type': 'textarea',
                             'prompt': 'Price your partner payout against your direct customer acquisition '
                                       'cost. Map which funnel stages the partner covers, from leads '
                                       'through close, and show the commission structure, whether '
                                       'recurring monthly, majority upfront, or margin-based, that matches '
                                       'those stages.',
                             'example': 'Willingness to Pay builds a $21,500 direct CAC from 100 leads, 20 '
                                        'qualified, 4 demos, 2 evaluations and 1 close, paying partners by '
                                        'stages covered [Willingness to Pay — _pp2kmBgn7s @ 00:13:06]. TAP '
                                        'Innovations pays $2,500 per month for 12 months per sale [TAP '
                                        'Innovations — 6_xruMdmmjM @ 00:02:23]. Entry: stages mapped, '
                                        'payout model chosen.'},
                            {'name': 'recruitment_and_crm',
                             'type': 'textarea',
                             'prompt': 'List the narrow set of partners you can actually activate, the '
                                       'source you used to find them inside your existing user base, and '
                                       'the separate CRM fields where partner-submitted deal registrations '
                                       'will live instead of your core records.',
                             'example': 'Luasai warns that 200 signed partners with 195 idle sinks '
                                        "programs [Luasai — 9ijiF4Aas8o @ 00:25:51]. Viktor's guest ran "
                                        'Clearbit enrichment and surfaced about 700 agencies already using '
                                        'the product [Viktor from Sales — 6Z4v3jibmMw @ 00:07:14]. '
                                        'Channeltivity keeps partner data in its own fields [Channeltivity '
                                        '- Channel Partner Portal — 5iuG2nYpJ0U @ 00:00:55]. Entry: '
                                        'activation list capped and fields separated.'},
                            {'name': 'mdf_claim_plan',
                             'type': 'textarea',
                             'prompt': 'Inventory every Market Development Fund and co-op budget available '
                                       'to you this quarter. For each, record the pre-approval status, the '
                                       'evidence you will attach to the claim, and the filing deadline so '
                                       'approved money actually becomes a payment.',
                             'example': 'ZINFI data shows as much as 60% of market development funds go '
                                        'unused each quarter [ZINFI Technologies, Inc. — lET3Wc2a74o @ '
                                        '00:00:35]. Marketing Business Network warns an approved budget is '
                                        'not automatically a payment [Marketing Business Network — '
                                        'gPoVTzxEwPw @ 00:00:44]. Entry: each activity pre-approved, '
                                        'evidence filed, deadline logged, nonprofit adds counted toward '
                                        'Microsoft designation.'}],
                 'completion_gate': 'Do not move to Worksheet 2 until direct sales conversion is '
                                    'documented as repeatable, every quote template carries a written '
                                    'markup definition and broken-out tax line, entry, medium and heavy '
                                    'implementation ballparks are published, partner payouts are priced '
                                    'against direct CAC, and every open MDF activity has pre-approval, '
                                    'evidence and a filing deadline.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Distribution, Marketplace Readiness, and Private Offer Build Sheet',
                 'purpose': 'Shift the revenue mix from boxes toward services, decide what to deliver '
                            'in-house versus through distributors, automate billing sync, lock down cloud '
                            'fraud exposure, and stand up a findable AWS Marketplace presence with private '
                            'offers whose economics, buyer targeting, expiration and renewal mechanics are '
                            'worked out before the first send.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Record your current hardware, software and services mix first, then '
                                  'name the next service you will add and whether a distributor will '
                                  'deliver it white label in your name.',
                                  'Wire billing connectors one function at a time and assign a named owner '
                                  'to trigger updates after every provisioning change, so agreements never '
                                  'drift from marketplace counts.',
                                  'Treat cloud fraud controls as a provisioning prerequisite: enforce '
                                  'strong MFA, verify the business exists, and set budget alerts before '
                                  'any new customer receives access.',
                                  'Confirm every AWS Marketplace seller prerequisite and split listings '
                                  'into separate product or industry SKUs before you build the first '
                                  'private offer.',
                                  'Work the private offer math, buyer account IDs, expiration date in UTC '
                                  'and renewal path on paper, then confirm the offer status reads Active '
                                  'before telling the buyer.'],
                 'fields': [{'name': 'revenue_mix_shift',
                             'type': 'textarea',
                             'prompt': 'Record your current revenue and profit split between hardware, '
                                       'software, and services. Identify which services you will add next, '
                                       'and state whether you plan to deliver them in-house, through a '
                                       'distributor, or under a white-label arrangement in your own name.',
                             'example': 'Jay McBain reports hardware down to 16% of partner revenue and '
                                        '13% of profit [Channel Partners Events — SwebwmaZR2I @ 00:02:55]. '
                                        "Distributors offer white label services in the partner's name, "
                                        'whether technical support or managed service [CRN — ULy4t5kvUt0 @ '
                                        '00:14:10]. Entry: current mix logged, next service named, '
                                        'delivery route chosen.'},
                            {'name': 'in_house_vs_outsourced',
                             'type': 'textarea',
                             'prompt': 'Decide what share of services you will deliver yourself versus '
                                       'outsource to providers. List the systems, processes, and maturity '
                                       'you actually have for round-the-clock coverage, and name what you '
                                       'will outsource so your experts stay in front of customers.',
                             'example': 'A large UK partner, roughly 85% services-led, outsources 60% to '
                                        '300-plus UK providers and delivers 40% itself [TD SYNNEX — '
                                        '2qmTwyQCa_o @ 00:02:45]. TD SYNNEX warns against promising 24/7 '
                                        'managed services without the systems beneath the iceberg [TD '
                                        'SYNNEX — K3d3674aDZ8 @ 00:03:03]. Entry: in-house share set, '
                                        'after-hours coverage outsourced, gaps listed.'},
                            {'name': 'billing_connector_setup',
                             'type': 'textarea',
                             'prompt': 'Map how marketplace subscription counts will flow into your PSA '
                                       'agreements and accounting without manual spreadsheets. Name the '
                                       'connector, the one-time linking step, the specific sync functions '
                                       'you will activate first, and who triggers updates after '
                                       'provisioning changes.',
                             'example': 'Complete the one-time ConnectWise agreement linking in ID Sync, '
                                        'then press force update after every provisioning change [Ingram '
                                        'Micro Cloud — ynfBBQclUKU @ 00:03:03]. With Digital Bridge, '
                                        'activate only the connectors you need, such as order status or '
                                        'invoice details [TD SYNNEX — 1Rg0jWCs65Y @ 00:05:34]. Entry: '
                                        'connector named, linking done, two sync functions enabled, owner '
                                        'assigned.'},
                            {'name': 'cloud_fraud_controls',
                             'type': 'textarea',
                             'prompt': 'Write the identity and consumption controls you enforce before '
                                       'provisioning any cloud customer. Cover strong MFA on administrator '
                                       'and console accounts, verification that the business actually '
                                       'exists, budget alert thresholds, anomaly detection, and the daily '
                                       'consumption review routine.',
                             'example': 'Hijacked accounts almost always lacked strong MFA [TD SYNNEX — '
                                        '8xAn9TMt7Ew @ 00:05:54]. A fake company onboarded with AI-forged '
                                        'IDs leaves nobody to pursue but the reseller [TD SYNNEX — '
                                        '8xAn9TMt7Ew @ 00:08:28]. Set budgets with alerts at 50, 90 and '
                                        '100%, review daily and call on any spike [TD SYNNEX — 8xAn9TMt7Ew '
                                        '@ 00:11:49].'},
                            {'name': 'expansion_path',
                             'type': 'textarea',
                             'prompt': 'Describe the small first engagement you will use to test a '
                                       "distributor's delivery capability, and the expansion path from "
                                       'that first project toward managed and security services. Include '
                                       'the attach questions you will ask on every inbound single-line '
                                       'order.',
                             'example': 'A five-person reseller tested capability with a five-day '
                                        'Microsoft migration before adding managed and security managed '
                                        'services [TD SYNNEX — 2qmTwyQCa_o @ 00:06:47]. On inbound Copilot '
                                        'orders, ask about data governance, cloud consumption readiness, '
                                        'adoption services and device capability before closing the single '
                                        'line [TD SYNNEX — 4NI20Et258M @ 00:02:37]. Entry: pilot project '
                                        'and four attach questions listed.'},
                            {'name': 'seller_registration',
                             'type': 'textarea',
                             'prompt': 'Confirm each prerequisite for selling through AWS Marketplace: an '
                                       'eligible jurisdiction for paid listings, a paid listing, '
                                       'Management Portal access, and a dedicated seller of record '
                                       'account. Note the owner and completion date for every item on the '
                                       'list.',
                             'example': 'Clazar notes private offers suit enterprise customers requiring '
                                        'tailored pricing, multi-year or volume deals, or CPPO channel '
                                        'motions [Clazar — h7liwzzA_-I @ 00:01:15]. AWS does not provision '
                                        "SaaS products, so buyers must register on the seller's website "
                                        '[Amazon Web Services — PVL4069oqC0 @ 00:02:32]. Entry: '
                                        'jurisdiction, paid listing, portal access, registration page '
                                        'confirmed.'},
                            {'name': 'listing_structure',
                             'type': 'text',
                             'prompt': 'List the separate product or industry SKUs you will publish '
                                       'instead of one company-name listing. For each SKU, note the buyer '
                                       'it targets and how AWS field sellers would find it when searching '
                                       'for a solution to a customer problem.',
                             'example': 'PartnerCloud argues against bucketing every deal under one '
                                        'company-name listing and recommends breaking offerings into '
                                        'separate SKUs by product or industry so buyers and AWS field '
                                        'sellers can actually find them [PartnerCloud — qXei9F9hLNU @ '
                                        '00:20:18]. Entry: one SKU per core product, one per regulated '
                                        'industry, each with target buyer and search terms recorded.'},
                            {'name': 'private_offer_economics',
                             'type': 'textarea',
                             'prompt': 'Calculate the net revenue on your first private offer. Record the '
                                       'list price, the private offer discount, the discounted customer '
                                       'price, the listing fee percentage, and the net disbursement you '
                                       'will actually receive after AWS invoices and collects from the '
                                       'buyer.',
                             'example': 'AWS works a $100 list price with a 20 percent private offer '
                                        'discount to $80; AWS charges the customer $80 and disburses to '
                                        'the ISV minus a 10 percent listing fee, netting $72 [Amazon Web '
                                        'Services — qWl-wamuA-Q @ 00:10:25]. Entry: list, discount, '
                                        'customer price, fee and net disbursement recorded line by line '
                                        'for the first offer.'},
                            {'name': 'offer_build_checklist',
                             'type': 'textarea',
                             'prompt': 'Build the checklist for each private offer: buyer AWS account IDs, '
                                       'invoicing terms for scheduled payments, contract duration, '
                                       'installment schedule, expiration date, and status check. Note the '
                                       'time zone used for dates and who confirms that the offer reads '
                                       'Active.',
                             'example': 'Add up to 23 buyer account IDs per SaaS contract offer [Amazon '
                                        'Web Services — 2qDBJ9lxIdQ @ 00:03:53]. Set expiration at least '
                                        'two weeks out, remembering AWS runs in UTC [Amazon Web Services — '
                                        'MlboB3rLbvE @ 00:02:38]. Verify the buyer is on invoicing terms '
                                        'before scheduling payments [Amazon Web Services — XvBBSBimMn4 @ '
                                        '00:05:47]. Entry: status confirmed Active.'},
                            {'name': 'renewal_and_scale_plan',
                             'type': 'textarea',
                             'prompt': 'Plan how renewals and upgrades will run through agreement-based '
                                       'offers and future dated agreements. Note when you will move offer '
                                       'creation into your CRM through the Marketplace API, and how you '
                                       'will reuse past offers instead of rebuilding them.',
                             'example': 'Allow up to 45 minutes for an agreement-based offer to generate '
                                        '[Amazon Web Services — KzcE0ZWyjzk @ 00:02:52]. Partners using '
                                        'future dated agreements at scale saw renewal rates rise [Amazon '
                                        'Web Services — gNv2wvhYkzA @ 00:03:43]. Use clone to new for '
                                        'revisions and export extended offers to PDF [AWS Events — '
                                        'K-GonrtXvKA @ 00:09:10]. Entry: renewal calendar built.'}],
                 'completion_gate': 'Do not move to Worksheet 3 until strong MFA, business verification '
                                    'and 50, 90 and 100% budget alerts are enforced on every cloud '
                                    'customer, billing sync runs without a spreadsheet, listings are split '
                                    'into findable SKUs, and at least one private offer has worked net '
                                    'economics, verified buyer account IDs, a UTC expiration two weeks out '
                                    'and an Active status.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Channel Partner Private Offer and CSP Operating Plan',
                 'purpose': 'Qualify every channel partner private offer before quoting, work the '
                            'wholesale and markup math, secure recurring resale authorizations, hand '
                            'buyers a clean acceptance path, forecast cash with realistic payment lag, '
                            'bundle multi-vendor solutions, and choose between direct-bill and indirect '
                            'CSP operation with compliance and services attach locked in.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Check paid listing, seller registration, product type and resale '
                                  'authorization validity before quoting any channel partner private '
                                  'offer, because BYOL and free products are excluded.',
                                  'Work the wholesale, markup and disbursement math for each pending deal, '
                                  'and ask each ISV for a recurring authorization so offers can be spun '
                                  'without renegotiation.',
                                  'Send every buyer the offer link together with the targeted account ID '
                                  'and the required permission level, then pad cash forecasts for payment '
                                  'lag and negotiated terms.',
                                  'Audit trailing twelve-month CSP revenue, support plan cost and '
                                  'designation status against the direct-bill bar well before renewal, not '
                                  'on the day the rules change.',
                                  'Close by stacking services on every license, locking headcount before '
                                  'annual new commerce orders, and claiming referral leads and capability '
                                  'points before they slip away.'],
                 'fields': [{'name': 'cppo_eligibility',
                             'type': 'textarea',
                             'prompt': 'Confirm eligibility before quoting a channel partner private '
                                       'offer. Record whether the ISV has a paid listing, whether you are '
                                       'a registered marketplace seller, whether the product is BYOL or '
                                       'free, and whether the resale authorization remains valid.',
                             'example': 'The ISV must have a paid listing; BYOL and free products are not '
                                        'supported by CPPO [Amazon Web Services — PkznZxwv3eg @ 00:01:43]. '
                                        'You must accept the reseller agreement the seller associated with '
                                        'the resell authorization before creating an offer [Amazon Web '
                                        'Services — pOUxsKDRzvM @ 00:02:26]. Entry: paid listing verified, '
                                        'seller registration confirmed, authorization window checked.'},
                            {'name': 'cppo_margin_math',
                             'type': 'textarea',
                             'prompt': 'Work the margin on one channel partner private offer. Record the '
                                       'ISV list price, the wholesale discount the ISV authorizes, your '
                                       'markup percentage, the final customer price, and the amount '
                                       'disbursed to you after the marketplace deducts the wholesale '
                                       'price.',
                             'example': 'AWS turns a $100 list into a $70 wholesale price with a 30% ISV '
                                        'discount; a 30% partner markup yields a $91 customer price, and '
                                        'after AWS deducts the $70, the channel partner receives $21 '
                                        '[Amazon Web Services — PkznZxwv3eg @ 00:11:04]. Entry: list, '
                                        'wholesale, markup, customer price and partner disbursement '
                                        'recorded for each pending deal.'},
                            {'name': 'authorization_terms',
                             'type': 'text',
                             'prompt': 'Specify the authorization terms you will request from each ISV. '
                                       'State whether you want a recurring authorization or a one-time '
                                       'discount, how many customers it should cover, and how long the '
                                       'discount must stay active for your pipeline.',
                             'example': 'Push the ISV for a recurring authorization rather than a one-time '
                                        'discount so you can spin multiple private offers for multiple '
                                        'customers without renegotiating while the discount stays active '
                                        '[Amazon Web Services — PkznZxwv3eg @ 00:03:41]. Entry: recurring '
                                        'authorization requested from each ISV, customer coverage stated, '
                                        'discount validity window matched to the next two quarters of '
                                        'pipeline.'},
                            {'name': 'buyer_handoff',
                             'type': 'textarea',
                             'prompt': 'Draft the buyer hand-off message for every private offer. Include '
                                       'the offer link, the targeted account ID, a reminder about the '
                                       'logged-in account, and the permission level required for whoever '
                                       'completes the purchase on the customer side.',
                             'example': 'Put the targeted AWS account ID in the offer email next to the '
                                        'link, because the buyer must be logged into that exact account to '
                                        'see the offer [Amazon Web Services — PkznZxwv3eg @ 00:08:13]. On '
                                        'Microsoft, the purchase must be completed by someone with '
                                        "appropriate permissions on the customer's Azure account "
                                        '[Microsoft Cloud — REkZmdc2hYE @ 00:02:42].'},
                            {'name': 'cash_forecast',
                             'type': 'textarea',
                             'prompt': 'Build your cash forecast for marketplace resale revenue. Record '
                                       'when disbursements typically land after invoicing, the average '
                                       'buyer payment lag, and the extra buffer for customers on net 30, '
                                       'net 45, or net 60 negotiated terms.',
                             'example': 'AWS cash lands between the 7th and 10th of the month after '
                                        'invoicing, and buyers pay within an average of 25 days, so add '
                                        'that buffer when forecasting [Amazon Web Services — PkznZxwv3eg @ '
                                        '00:12:57]. Pad further for buyers on net 30, plus those who '
                                        'negotiated 45 or 60 days [Amazon Web Services — vKzo7FINzss @ '
                                        '00:02:42].'},
                            {'name': 'solution_bundle',
                             'type': 'textarea',
                             'prompt': "Design one solution bundle that combines several vendors' products "
                                       'with your own professional services on top. List each component, '
                                       'the vendor behind it, and how you will transact the bundle as one '
                                       'offer instead of many separate private offers.',
                             'example': 'One solution combined three CrowdStrike products, two Zscaler '
                                        "products and the partner's own professional services; transacting "
                                        'it would have required six different private offers transacted '
                                        'one by one [AWS Events — cOyZpsRxxE4 @ 00:38:10]. Customers '
                                        'expect a one-stop trusted source of cloud services [Amazon Web '
                                        'Services — GMejbloTwGE @ 00:03:02]. Entry: components, vendors '
                                        'and single-offer route listed.'},
                            {'name': 'reseller_recruitment_pitch',
                             'type': 'textarea',
                             'prompt': 'Write the opening pitch you will use to recruit resellers into '
                                       'your marketplace offer. Lead with the recurring money each '
                                       'reseller earns for introducing customers versus closing alone, '
                                       'then explain when product training begins and who handles sales '
                                       'support.',
                             'example': 'WeTransact pitches the money before the product: 20% for '
                                        'introducing customers or 30% for closing alone, recurring year '
                                        'over year, teaching the product only after the reseller sees the '
                                        "revenue [WeTransact — jJAskh3xNOM @ 00:35:03]. Microsoft's CSP "
                                        'example leaves the reseller $70 on a $120 sale [Microsoft Cloud — '
                                        'yC9d52PsuOg @ 00:02:38]. Entry: margin pitch drafted.'},
                            {'name': 'direct_vs_indirect',
                             'type': 'textarea',
                             'prompt': 'Decide whether you will operate as a direct-bill or indirect CSP. '
                                       'Record trailing twelve-month CSP revenue, support plan cost, '
                                       'designation status, and billing platform investment, then state '
                                       'which model your numbers actually support before your next renewal '
                                       'date.',
                             'example': 'Direct bill now demands $1,000,000 a year in CSP revenue, up from '
                                        '$300,000 [Stratos Cloud Alliance — rV-Q2IVur6I @ 00:03:12], plus '
                                        'a support plan of at least 15k or premier at about 50,000 '
                                        'annually [Stratos Cloud Alliance — rV-Q2IVur6I @ 00:12:14]. '
                                        'Indirect resellers need only $1,000 USD per rolling 12 months '
                                        '[Manage Protect — Je2jbg9tm0Q @ 00:09:37].'},
                            {'name': 'partner_center_compliance',
                             'type': 'textarea',
                             'prompt': 'List the Partner Center compliance items you will verify this '
                                       'quarter: legal entity name, primary business address, current '
                                       'employee contact, MPA acceptance by a global admin, multi-factor '
                                       'authentication across partner tenants, and secure application '
                                       'model for integrations.',
                             'example': 'Confirm the Partner Center legal entity name, primary business '
                                        'address and a current employee contact, then have a global admin '
                                        'accept the MPA [Manage Protect — Je2jbg9tm0Q @ 00:10:39]. Enforce '
                                        'multi-factor authentication for all users in all partner tenants '
                                        'and implement the secure application model for API integrations '
                                        '[Microsoft Americas Partner Community — ybzVv-GZvMc @ 00:09:59].'},
                            {'name': 'services_attach_and_nce',
                             'type': 'textarea',
                             'prompt': 'Map the services you will stack on top of each license, the New '
                                       'Commerce term each customer will sign, and how you will lock '
                                       'headcount before annual orders. Note the designation points and '
                                       'referral leads you will pursue this quarter.',
                             'example': 'Monthly terms carry a 20% premium, so $100 becomes $120 [m365 '
                                        'Show — LGgw20GtaDQ @ 00:05:11], and the 7-day window is the only '
                                        'exit from annual orders [m365 Show | M365, Azure Cloud, Power '
                                        'Platform & AI — LGgw20GtaDQ @ 00:05:42]. Two staff earning '
                                        'intermediate certifications yield 10 of 25 capability points '
                                        '[Manage Protect — Je2jbg9tm0Q @ 00:15:57].'}],
                 'completion_gate': 'Part 1 is complete only when every pending channel partner private '
                                    'offer has verified eligibility, worked margin math and a buyer '
                                    'hand-off carrying the targeted account ID, the cash forecast includes '
                                    'the 25-day payment lag, the direct-bill versus indirect decision is '
                                    'backed by trailing twelve-month CSP revenue, and Partner Center '
                                    'compliance items are confirmed.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'SaaS Spend Control and Revenue Recognition Ledger',
                 'purpose': 'Turn SaaS and licensing spend into a controlled, evidence-backed ledger, then '
                            'make sure every resold dollar is recognized correctly as gross or net, '
                            'ratably or on delivery, so margin reports and revenue statements hold up '
                            'under review.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Pull the last twelve months of SaaS invoices, corporate-card '
                                  'statements, and identity provider sign-in exports before filling any '
                                  'field.',
                                  'Rank vendors by annual spend and concentrate effort on the top 20 to 25 '
                                  'contracts, where most recoverable waste sits.',
                                  'Record every number with its source system and date so finance and '
                                  'auditors can trace each figure back.',
                                  'Run the principal-versus-agent control test on every resold element '
                                  'before any revenue is booked gross.',
                                  'Have the controller review the revenue fields and sign off before the '
                                  'next month-end close begins.'],
                 'fields': [{'name': 'central_vendor_list',
                             'type': 'textarea',
                             'prompt': 'List every SaaS and licensing vendor your resale practice or '
                                       'client pays, ranked by annual spend. Identify the top 20 to 25 '
                                       'vendors that deserve focused review, and note who owns each '
                                       'contract centrally versus inside a business unit.',
                             'example': 'Danske Bank discovered 3,000 applications over two years against '
                                        'a target estate of 600 to 800, with about 100 new apps appearing '
                                        'monthly [FinOps Foundation — F-5GIklN_Ps @ 00:04:28]. Our list '
                                        'ranks Microsoft, Salesforce and ServiceNow first, flags 41 shadow '
                                        'apps found on corporate cards, and assigns the top 22 vendors to '
                                        'the central procurement desk for review.'},
                            {'name': 'waste_baseline',
                             'type': 'textarea',
                             'prompt': 'Estimate the share of current SaaS spend that is waste, using seat '
                                       'activity, corporate-card charges, and departed-employee licenses. '
                                       'Record the evidence source for every number so the baseline '
                                       'survives challenge from finance, business-unit owners, and the '
                                       'vendor account team.',
                             'example': "Priceline's Chris Reed cites Gartner's up-to-30% waste figure for "
                                        'SaaS spend [FinOps Foundation — hQDjTANIaTo @ 00:04:01], and '
                                        'recurring corporate-card charges kept billing after employees '
                                        'left at $5,000 a month, or 60k a year [FinOps Foundation — '
                                        'hQDjTANIaTo @ 00:09:23]. Our working baseline: 18% waste '
                                        'confirmed from SSO login logs, plus $3,400 monthly in orphaned '
                                        'card subscriptions awaiting cancellation.'},
                            {'name': 'seat_reclaim_rule',
                             'type': 'text',
                             'prompt': 'Define the inactivity threshold that triggers a seat reclaim, the '
                                       'identity or SSO source that proves inactivity, and the owner who '
                                       'confirms before removal. State whether you start at 30 days or 90 '
                                       'days and why that choice fits.',
                             'example': 'The ServiceNow playbook creates a reclaim rule with a 30-day '
                                        'inactivity threshold and suggests reviewing it and considering 90 '
                                        'days [ServiceNow Community — 8mJc7j3DW28 @ 00:03:48]. Our rule: '
                                        'identity-provider sign-in data flags seats idle 90 days, the '
                                        'department head confirms within five business days, and reclaimed '
                                        'Microsoft 365 licenses return to the shared pool before any new '
                                        'purchase.'},
                            {'name': 'concurrent_license_heatmap',
                             'type': 'textarea',
                             'prompt': 'For each concurrent or shared license pool, record contracted '
                                       'seats, observed peak simultaneous use, and the proposed '
                                       'right-sized count. Describe how the heat map was built, over what '
                                       'period, and what buffer above peak you will keep.',
                             'example': 'Peter Greenshaw built a heat map manually, found peak use of 15 '
                                        'out of 50 concurrent seats, and cut the contract to 20 [FinOps '
                                        'Weekly — sqpO85TKjEI @ 00:11:09]. Our engineering CAD pool: 40 '
                                        'contracted seats, peak of 22 over a 90-day window, renewal target '
                                        'set at 26 to keep a modest buffer above observed peak demand.'},
                            {'name': 'commitment_shortfall_model',
                             'type': 'textarea',
                             'prompt': 'Model every spend commitment against realistic consumption. Record '
                                       'the committed amount, projected actual spend, the resulting '
                                       'shortfall, and whether a larger mini business case could get the '
                                       'shortfall forgiven before you sign or renew the commitment.',
                             'example': 'Derer Mason of Roku shows that a $1M 12-month commit with $900K '
                                        'spent still owes $100K, unless a mini business case committing '
                                        '$1.2M gets the shortfall forgiven [FinOps Foundation — '
                                        'LF1AK1WypX0 @ 00:14:06]. Our Datadog commit: $600K committed, '
                                        '$510K projected, $90K exposure; we will propose a $720K renewal '
                                        "case before the vendor's April fiscal year-end."},
                            {'name': 'effective_rate_check',
                             'type': 'text',
                             'prompt': 'Recompute the effective rate for each committed contract as '
                                       'contract cost divided by actual usage. Compare it with the '
                                       'on-demand rate and note whether the savings procurement recorded '
                                       'are real or should be reversed in reporting.',
                             'example': 'The effective rate is contract cost divided by actual usage, and '
                                        'if it meets or exceeds on-demand, procurement must be told the '
                                        'recorded savings are not real [FinOps Foundation — iIwpcQbBkmM @ '
                                        '00:11:03]. Our analytics contract costs $240K for usage that '
                                        'would run $228K on-demand, so the logged 22% saving is reversed '
                                        'and flagged for renegotiation.'},
                            {'name': 'principal_agent_test',
                             'type': 'textarea',
                             'prompt': 'For each resold software or hardware element, run the control '
                                       'test: integration into a combined solution, control of the hosted '
                                       'software before transfer, or a pure arrange-for-the-vendor '
                                       'promise. Record the conclusion as gross principal or net agent.',
                             'example': "ECC's $500,000 GPU resale books gross with upfront inventory risk "
                                        'and physical custody, but if the vendor bills the customer '
                                        'directly it collapses to a $75,000 commission [Jobank CPA — '
                                        'KjWijHo8iMI @ 00:06:58]. Our Snowflake resale: vendor bills the '
                                        'client, we never host or integrate it, so we record net agent '
                                        'revenue only, even though we carry the credit risk.'},
                            {'name': 'side_letter_controls',
                             'type': 'textarea',
                             'prompt': 'Document every non-standard discount, performance guarantee, '
                                       'refund promise, or cancellation clause on open deals, including '
                                       'promises made by email or chat. Name the hard-stop controller '
                                       'review point and the customers who receive side letter '
                                       'confirmations each quarter or year.',
                             'example': 'A sales VP email promising a 100% refund if latency exceeded 200 '
                                        'milliseconds in Q1 turned a $900,000 TCV deal into $0 recognized '
                                        'for the quarter, with a $75,000 catch-up on April 1 [Jobank CPA — '
                                        'WeV8GbQwaPE @ 00:05:30]. Our control: Salesforce CPQ blocks '
                                        'signature until the controller approves, and our top 15 accounts '
                                        'confirm no side letters quarterly.'},
                            {'name': 'bundle_ssp_allocation',
                             'type': 'textarea',
                             'prompt': 'List each bundled contract with its invoice price per element and '
                                       'the standalone selling price for each element. Reallocate the '
                                       'transaction price on standalone value, and fold any non-distinct '
                                       'setup or onboarding fee into the subscription allocation.',
                             'example': 'Accounting and Auditing Hub reallocates a $600,000 bundle across '
                                        '$700,000 of standalone value and buries the non-distinct setup '
                                        'fee inside the SaaS allocation [Accounting and Auditing Hub — '
                                        '-5y55BOFAKA @ 00:05:48]. Our deal: $180,000 total, SaaS '
                                        'standalone $150,000, training $30,000, setup $20,000 '
                                        'non-distinct; allocation yields roughly $150,000 SaaS ratable and '
                                        '$30,000 training recognized on delivery.'},
                            {'name': 'month_end_deferred_close',
                             'type': 'textarea',
                             'prompt': 'Write the month-end revenue close sequence for resold '
                                       'subscriptions: journal entry generation, deferred revenue '
                                       'reclassification, and reconciliation. Name the report you '
                                       'reconcile against, the person who signs off, and how upfront cash '
                                       'lands in deferred revenue.',
                             'example': "Generate the month's revenue journal entries first, only then run "
                                        'the deferred revenue reclassification, and reconcile against the '
                                        'deferred revenue waterfall report [CFO AI — MAsF2w47iew @ '
                                        '00:04:55]. Our close: a $12,000 annual prepayment books to '
                                        'deferred revenue, $1,000 releases monthly in NetSuite ARM, and '
                                        'the controller signs the waterfall tie-out by business day '
                                        'three.'}],
                 'completion_gate': 'Do not advance to Worksheet 5 until the top 20 vendors carry a '
                                    'verified spend figure, every commitment has a modeled shortfall, and '
                                    'every resold element has a documented gross-or-net conclusion signed '
                                    'by the controller.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Renewal Calendar and Vendor Onboarding Control Sheet',
                 'purpose': 'Convert renewals from calendar surprises into planned financial decisions, '
                            'and harden the vendor onboarding and payment process so bad bank data, '
                            'expired documents, and invoice errors never reach accounts payable.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Collect the latest signed order form or amendment for every contract '
                                  'renewing in the next twelve months.',
                                  'Compute each notice deadline as renewal date minus notice period and '
                                  'enter it in a shared calendar with a named owner.',
                                  'Clean license counts and gather owner confirmations before any pricing '
                                  'conversation with the vendor.',
                                  'Treat payment terms and vendor onboarding as financial controls, not '
                                  'administrative tasks.',
                                  'Review the completed sheet with procurement, finance, and accounts '
                                  'payable together before the first deadline arrives.'],
                 'fields': [{'name': 'notice_deadline_register',
                             'type': 'textarea',
                             'prompt': 'For every contract renewing in the next twelve months, record the '
                                       'renewal date, notice period, and computed notice deadline. Pull '
                                       'each date from the latest signed order form or amendment, never '
                                       "from an invoice or anyone's memory.",
                             'example': "A CRM renewing on March 1st with 90 days' notice has to be "
                                        'decided by December 1st [Venduris — 0W4a6u1-zMQ @ 00:01:04]. Our '
                                        "register: ServiceNow renews July 15 with 60 days' notice, "
                                        'deadline May 16, sourced from Amendment 3; Atlassian renews '
                                        "October 1 with 30 days' notice, deadline September 1, sourced "
                                        'from the 2025 order form.'},
                            {'name': 'renewal_timeline_120',
                             'type': 'textarea',
                             'prompt': 'Lay out the 120-day renewal runway for your largest upcoming '
                                       'renewal: kickoff at 120 days, usage pull at 90, benchmarking at '
                                       '60, and notice or signature at 30. Name the owner and deliverable '
                                       'attached to each checkpoint.',
                             'example': 'SPK and Associates warns that companies treat software renewals '
                                        'as an admin task instead of a financial decision [SPK and '
                                        'Associates — Y8SGLxkUJd8 @ 00:02:59]. Our Salesforce runway: day '
                                        '120 the IT finance lead opens the file, day 90 the admin exports '
                                        'login data, day 60 procurement benchmarks pricing, day 30 the CFO '
                                        'signs or sends notice.'},
                            {'name': 'true_count_cleanup',
                             'type': 'textarea',
                             'prompt': 'Before negotiating price, establish the true license quantity. '
                                       'Strip inactive, blocked, stale, and contractor accounts, audit '
                                       'supposedly decommissioned servers still on the network, and state '
                                       "your data confidence percentage compared with the vendor's likely "
                                       'confidence level.',
                             'example': 'MetrixData 360 found a client holding 10,000 E3 seats but needing '
                                        '6,800; the 15% discount saved about $570,000 while 3,200 inactive '
                                        'licenses cost roughly $1.9 million [MetrixData 360 — ViSmcebdPlM '
                                        '@ 00:13:36]. Our cleanup removed 410 stale accounts and 60 '
                                        'misclassified contractor seats before negotiation, lifting our '
                                        "data confidence from 55% toward the vendor's 95%."},
                            {'name': 'seat_change_evidence',
                             'type': 'text',
                             'prompt': 'For every seat reduction you propose, attach the usage log excerpt '
                                       "and the business owner's written confirmation. Note any seat that "
                                       'is reserved for a pending hire, protected by a contractual '
                                       'minimum, or tied to a seasonal workload.',
                             'example': "Vektorindex requires usage logs plus an owner's confirmation "
                                        'before anyone touches seat counts, since an unused seat may be a '
                                        'hire starting Monday or a contractual minimum [Vektorindex — '
                                        'lR3RrM_hqMg @ 00:03:49]. Our design-suite reduction of 35 seats '
                                        'carries login exports and marketing director sign-off; eight '
                                        'seats stay for summer interns starting in June.'},
                            {'name': 'price_cap_and_term_levers',
                             'type': 'textarea',
                             'prompt': 'List every price-protection lever you will request: annual '
                                       'increase caps, multi-year price locks, longer terms, reference '
                                       'programs, and payment timing. For each cap, check spend-profile, '
                                       'product-lock, changed-metric, and renamed-product conditions that '
                                       'could void the capped percentage.',
                             'example': "Zylo's senior SaaS services manager negotiated Salesforce's 9% "
                                        'yearly price cap down to 3% on a live renewal [Zylo — 8wZiGBXdOBo '
                                        '@ 00:23:30]. Our ask: 3% cap holding even if the vendor renames '
                                        'editions or changes the user metric, a 36-month term for another '
                                        '5 to 10% off, and roughly 20% for joining the reference program.'},
                            {'name': 'auto_renewal_position',
                             'type': 'text',
                             'prompt': 'Decide for each contract whether auto-renewal stays or gets '
                                       'stripped. Justify the choice with price competitiveness, '
                                       'utilization, and contract-owner continuity, and record which '
                                       'internal person the vendor must contact if the current owner '
                                       'leaves without a handover.',
                             'example': 'Vistack strips auto-renewal so nothing triggers from the vendor '
                                        'side and the rep has to chase you, which also protects you when a '
                                        'contract owner leaves without handover [Vistack — 0I4GdLiHF5Y @ '
                                        '00:05:54]. Our decision: strip auto-renewal on the CRM and data '
                                        'warehouse; let a fully used, well-priced password manager roll '
                                        'annually, as one Zylo speaker allows.'},
                            {'name': 'payment_terms_ladder',
                             'type': 'textarea',
                             'prompt': 'Map how supplier payment terms will progress from upfront payment '
                                       'toward Net 60 in phases. For each step, record the monthly spend, '
                                       'the cash-flow benefit, and any price increase or discount removal '
                                       'the supplier demands in exchange.',
                             'example': 'On a simplified steady-state assumption, $50,000 of monthly '
                                        'purchases times two months equals roughly $100,000 of supplier '
                                        'financing at Net 60 [10 Min For Supply Chain — vdxHe8A6Tkk @ '
                                        '00:02:11]. Our ladder with the hosting supplier: 100% upfront '
                                        'now, Net 30 after two clean quarters, Net 60 next year, provided '
                                        'their existing 2% early-payment discount survives the change.'},
                            {'name': 'vendor_intake_validation',
                             'type': 'textarea',
                             'prompt': 'Describe the digital vendor intake form that replaces emailed '
                                       'spreadsheets. List required fields, bank-detail validation steps, '
                                       'document uploads, and duplicate checks, and explain how approved '
                                       'records write directly into the ERP vendor master without manual '
                                       'rekeying.',
                             'example': 'Hold ACH release until routing and account numbers pass '
                                        'validation and submitted changes are reviewed, because one '
                                        'fat-fingered digit returns and delays the payment [Charted '
                                        '(formerly SquareWorks) — 1wlmLTmDAfc @ 00:07:23]. Our intake: '
                                        'legal name, tax ID, tax form upload, insurance certificate, bank '
                                        'letter, and an automated duplicate check against the NetSuite '
                                        'vendor list before approval.'},
                            {'name': 'invoice_error_rules',
                             'type': 'text',
                             'prompt': 'List the invoice validation rules that must pass before a supplier '
                                       'invoice reaches accounts payable, including quantity, unit value, '
                                       'and purchase order matching. State how errors are pushed back to '
                                       'the supplier instead of corrected internally.',
                             'example': 'SAP Business Network runs 120-plus business rules that check '
                                        'supplier invoices before they hit accounts payable and can block '
                                        'altered quantities or values even when the total is unchanged '
                                        '[Spend And Procurement with Mike — xPYn_cF6f1E @ 00:00:58]. Our '
                                        'rules: PO flip required, three-way match within 2%, and rejected '
                                        'invoices returned to the supplier portal with reasons.'},
                            {'name': 'compliance_document_tracker',
                             'type': 'textarea',
                             'prompt': 'Track expiring insurance, tax, and compliance documents for every '
                                       'active vendor. Record the expiration date, the automated reminder '
                                       'schedule, the owner who chases renewals, and the action taken when '
                                       'coverage lapses before a scheduled payment run.',
                             'example': 'PROKURIA advises automating reminders for expiring insurance, '
                                        'tax, and compliance documents so expired coverage never becomes a '
                                        'compliance blind spot [PROKURIA — _R1e9FCXKyI @ 00:03:00]. Our '
                                        'tracker: reminders at 60, 30, and 7 days before expiry; the '
                                        'vendor manager owns follow-up; any lapsed certificate places the '
                                        'vendor on payment hold until a valid replacement is uploaded.'}],
                 'completion_gate': 'Do not open any renewal negotiation until its notice deadline is '
                                    'logged from a signed document, the license count is cleaned with '
                                    "owner evidence, and the vendor's bank details have passed "
                                    'validation.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Public Sector Vehicles, Vendor Risk, and Audit Defense Plan',
                 'purpose': 'Build the public sector contract discipline and vendor risk controls that '
                            'protect schedule pricing and cash, then prepare negotiation and audit '
                            'defenses that preserve leverage before signature and margin after it.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['List every public sector vehicle and multi-year commercial agreement, '
                                  'with current sales and expiration data.',
                                  'Check every commercial quote against schedule pricing before it leaves '
                                  'the building.',
                                  'Verify any bank-detail change by calling a known number taken from the '
                                  'vendor master, never from the request.',
                                  'Build your walk-away alternative and cost it before entering any major '
                                  'vendor negotiation.',
                                  'Prepare the audit protocol now, before any notice arrives, and assign '
                                  'named owners to every deadline.'],
                 'fields': [{'name': 'contract_vehicle_inventory',
                             'type': 'textarea',
                             'prompt': 'List every public sector contract vehicle you hold or plan to '
                                       'pursue, including GSA MAS schedules, cooperative contracts, and '
                                       'marketplace private offers. Record sales logged through each '
                                       'vehicle last year and whether it meets its annual sales minimum.',
                             'example': 'More than 60% of roughly 18,000 to 20,000 GSA schedule holders '
                                        'log zero sales through their schedule [How To Sell To & Win '
                                        'Federal Government Contracts — p3DsAuDE32c @ 00:10:31]. Our '
                                        'inventory: GSA MAS schedule with $41,000 in sales, above the '
                                        '$25,000 annual minimum; one university systemwide contract; and '
                                        'AWS Marketplace private offers for state agencies using bid terms '
                                        'instead of commercial terms.'},
                            {'name': 'iff_reporting_check',
                             'type': 'textarea',
                             'prompt': 'Describe how you calculate and report the Industrial Funding Fee '
                                       'each period. Confirm the fee is embedded in contract pricing, that '
                                       'open-market items and travel are excluded, and that every sale is '
                                       'reported under the correct SIN.',
                             'example': 'The 0.75% Industrial Funding Fee is paid by the customer, '
                                        'embedded in contract pricing rather than shown as a line item, '
                                        'and remitted by the vendor [GSA (General Services Administration) '
                                        '— NVfgGOTkm4Q @ 00:02:34]. Our quarter: $212,000 in schedule '
                                        'sales, $9,500 of travel and open-market items stripped out, '
                                        'leaving $1,519 in IFF remitted under the correct SIN.'},
                            {'name': 'price_reduction_guard',
                             'type': 'text',
                             'prompt': 'Before issuing any commercial quote, compare the proposed rate '
                                       'against your GSA rate for the same item or labor category. Record '
                                       'who checks, how the comparison is documented, and what happens '
                                       'when a commercial discount would undercut the schedule.',
                             'example': 'Confirm the commercial rate does not sit below your GSA rate, '
                                        'because the price reduction rule forces the GSA rate down [How To '
                                        'Sell To & Win Federal Government Contracts — p3DsAuDE32c @ '
                                        '00:12:11]. Our guard: the contracts manager compares every '
                                        'commercial quote against the schedule price list, and any '
                                        'discount deeper than the GSA rate needs written approval first.'},
                            {'name': 'public_sector_private_offer',
                             'type': 'textarea',
                             'prompt': 'Design the payment schedule and terms for your next public sector '
                                       'marketplace private offer. Record the term length, number and '
                                       "timing of payments relative to the buyer's fiscal-year change, and "
                                       'which contract terms replace standard commercial terms.',
                             'example': 'AWS private partner offers allow 1 to 60 month terms and up to 60 '
                                        'payments, so a small payment now can precede a larger remainder '
                                        'after the fiscal-year change [AWS Public Sector — F4gkR0s1Blw @ '
                                        '00:02:49]. Our state university offer: 36 months, $15,000 in '
                                        'June, $135,000 in July, with the systemwide contract replacing '
                                        'commercial terms.'},
                            {'name': 'bank_change_verification',
                             'type': 'text',
                             'prompt': 'Write the procedure for any vendor request to change bank details. '
                                       'Name who places the confirmation call, where the known phone '
                                       'number comes from, what evidence is logged, and how long payments '
                                       'stay on hold during verification.',
                             'example': 'Pause and call your vendor using a known number before acting on '
                                        'any bank detail change request [SecureOps with Ayden Connor — '
                                        'fOUGaSjlTBY @ 00:00:00]. Our procedure: the AP lead calls the '
                                        'phone number stored on the original vendor master record, never '
                                        'one from the request, logs the call time and contact name, and '
                                        'holds payments for up to five business days.'},
                            {'name': 'obligation_tracker',
                             'type': 'textarea',
                             'prompt': 'Load every cancellation window, auto-renewal date, and notice '
                                       'obligation from public sector and commercial contracts into one '
                                       'owned tracker. Record, for each contract, the owner, the reminder '
                                       'cadence, and the financial exposure if a window is missed.',
                             'example': 'One company missed a cancellation window, the agreement '
                                        'auto-renewed, and it was held liable for 75% of the cost of the '
                                        'remaining contract [Leegality — DeATzRK3azc @ 00:03:22]. Our '
                                        'tracker lists 38 obligations, each with a named owner and '
                                        'reminders at 90, 45, and 15 days; the largest exposure is a '
                                        '$480,000 security platform renewal.'},
                            {'name': 'walk_away_position',
                             'type': 'textarea',
                             'prompt': 'Define your walk-away alternative before negotiating with a major '
                                       'vendor. Describe the costed exit pilot, the baseline metrics '
                                       'gathered, the sequence of levers you will pull, and why the '
                                       'discount request comes last in that sequence.',
                             'example': "If the vendor senses you won't walk away, there's absolutely no "
                                        'way it drops the price [Virtualization Options LLC Free Learning '
                                        'Portal — fTqBORy9ePo @ 00:03:00]. Our sequence: baseline hardware '
                                        'metrics, consolidation, per-cluster bundle scoping, a costed exit '
                                        'pilot moving two clusters to an alternative platform for $85,000, '
                                        "and only then the discount request, timed to the vendor's "
                                        'year-end.'},
                            {'name': 'escalator_and_lock_terms',
                             'type': 'text',
                             'prompt': 'Record the annual price escalator in each multi-year agreement and '
                                       'the cap you will demand. Show the cumulative drift over the full '
                                       'term if uncapped, and note any multi-year price lock or ROI '
                                       'realization haircut you will apply.',
                             'example': 'Uncapped annual increases compound to 15 to 25% over a three-year '
                                        'term, and the prescribed counter is a 3 to 5% annual cap '
                                        '[Virtualization Options LLC Free Learning Portal — xP4R2F8hbBw @ '
                                        '00:06:54]. Our virtualization renewal: vendor proposed 8% yearly, '
                                        'roughly 26% cumulative; we demand a hard 3% cap and apply a 50% '
                                        "haircut to the vendor's ROI claim."},
                            {'name': 'audit_defense_protocol',
                             'type': 'textarea',
                             'prompt': 'Write your response protocol for a software publisher audit '
                                       'notice. Cover the NDA signed directly with the auditor, what data '
                                       'is withheld at kickoff, how disagreements are recorded in writing, '
                                       'and who owns the 30-day respond and settle deadlines.',
                             'example': 'Microsoft audits that find 5% or more non-compliance price '
                                        'shortfall licenses at 125% of your discounted price list, plus '
                                        'audit fee reimbursement [SAMexpert TV – Microsoft Licensing and '
                                        'Cloud — 7shzxv1SUFc @ 00:10:22]. Our protocol: direct NDA with '
                                        'the auditor at kickoff, no org structure shared, a running '
                                        'written protocol of disagreement, and the licensing manager '
                                        'owning every deadline.'},
                            {'name': 'spla_and_services_margin',
                             'type': 'textarea',
                             'prompt': 'For hosting and services lines, record current SPLA cost, margin, '
                                       'and per-user counts including everyone authorized through remote '
                                       'desktop tools. Add professional services margin and billable '
                                       'utilization targets, and note where sales has been discounting '
                                       'services to protect ARR.',
                             'example': 'Hosting providers cutting inbound SPLA costs by 30% moved margin '
                                        'from about 5% to 35% [SAMexpert TV – Microsoft Licensing and '
                                        'Cloud — S-D4c7b8-94 @ 00:10:53]. Our numbers: 310 per-user SPLA '
                                        'licenses after adding 22 TeamViewer users, 9% hosting margin, '
                                        'services margin at 31%, and utilization at 74%, inside The SaaS '
                                        "CFO's 70 to 80% billable target."}],
                 'completion_gate': 'Do not sign a multi-year agreement or respond to an audit notice '
                                    'until escalator caps are documented, the exit pilot is costed, the '
                                    'NDA protocol is assigned, and every cancellation window sits in the '
                                    'owned tracker.'}]}
