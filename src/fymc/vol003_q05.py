from __future__ import annotations

CHAPTER_5 = {
    "id": "Q5",
    "chapter_id": "Q5",
    "chapter_number": 5,
    "question_number": 5,
    "slug": "payments-sales-tax-and-merchant-of-record-choices",
    "question_prompt": "How do I compare payment processors and merchants of record, configure tax collection, and assess the migration risks discussed in these videos?",
    "kicker": "Q5 / THE BIG MONEY PLAYBOOKS",
    "title": "Payments, Sales Tax, and Merchant-of-Record Choices",
    "subtitle": "Stripe Checkout and Managed Payments, Stripe Tax activation, Paddle and FastSpring comparisons, Lemon Squeezy reviews, and reported migration and license-key gaps",
    "layout_template": "case_study",
    "reading_time_minutes": 15,
    "executive_summary": (
        "The practitioners agree on the central trade: standard Stripe buys control, while a merchant of record takes over tax work for a higher fee. "
        "HelperMan values the administrative relief after using both Lemon Squeezy and Paddle; SoloBuild compares their 5% plus 50-cent base pricing with Stripe's layered charges. "
        "OCH Platform demonstrates separate Stripe Tax activation, and Stephen S. demonstrates Managed Payments checkout setup with a tax-classification requirement. "
        "The disagreements concern coverage, total fees, product fit, and migration timing. "
        "TechWealth Hub champions selective Managed Payments, while Captain Vova identifies coverage limits in the version they discuss. "
        "Folioquest, heyymilian, and Gaurav Tiwari report Lemon Squeezy's March 31, 2027 shutdown; Gaurav prioritizes license keys, eligibility, and replacement links over promotional pricing."
    ),
    "key_metrics": [
        {
            "label": "Paddle pay-as-you-go base fee",
            "metric": "Paddle pay-as-you-go base fee",
            "value": "5% plus $0.50 per checkout transaction",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "SoloBuild says this plan has no monthly fee and includes tax handling, "
                "fraud protection, subscriptions, and customer billing support."
            ),
            "source": "SoloBuild ([i05UCC3UvNY @ 00:05:19])",
        },
        {
            "label": "Managed Payments domestic-card estimate",
            "metric": "Managed Payments domestic-card estimate",
            "value": "6.4% plus $0.30",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "heyymilian adds the stated standard domestic-card processing fee "
                "and Managed Payments surcharge, explicitly describing the result as their arithmetic."
            ),
            "source": "heyymilian ([0R3CB1EcgKA @ 00:05:11])",
        },
        {
            "label": "Paddle payout minimum",
            "metric": "Paddle payout minimum",
            "value": "$100 minimum; monthly payout sent by the fifteenth",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "SoloBuild says the balance converts on the first and Paddle sends payment "
                "by the fifteenth when the minimum has been reached."
            ),
            "source": "SoloBuild ([i05UCC3UvNY @ 00:05:36])",
        },
        {
            "label": "Reported Lemon Squeezy processing cutoff",
            "metric": "Reported Lemon Squeezy processing cutoff",
            "value": "March 31, 2027, including subscription renewals",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "heyymilian reports that Lemon Squeezy's migration page gives this final "
                "processing date and says extensions will not be offered."
            ),
            "source": "heyymilian ([0R3CB1EcgKA @ 00:00:00])",
        },
    ],
    "sections": [
        {
            "id": "practitioner-consensus",
            "title": "The Practitioner Consensus",
            "paragraphs": [
                (
                    "Choose who carries the tax work before choosing the checkout skin. Tutorly separates standard Stripe Checkout from Paddle and Lemon Squeezy: "
                    "Stripe processes the payment, while the other two become the legal seller and manage the associated tax responsibilities. The distinction matters "
                    "because Tutorly's list of payment operations includes subscriptions, refunds, invoices, and obligations across countries, not merely a successful card charge. "
                    "Their pitch for Stripe is customization and control; their pitch for a merchant of record is removing the administrative work that grows with international "
                    "customers [IfaCBBIoVK0 @ 00:00:32]. SoloBuild makes the same distinction but adds a specific boundary around Stripe Tax: calculation and collection do not "
                    "automatically include registration and filing. They place those services in Tax Complete, starting at $90 a month, and describe Managed Payments as Stripe's "
                    "handled-for-you alternative [i05UCC3UvNY @ 00:01:53]. Hayes Tutorials lands on the same operational split: Stripe fits developers with tax handling already "
                    "in place, Paddle fits B2B companies, and Lemon Squeezy fits independent creators. Their recommendation is not that every seller needs the same platform. "
                    "It is that existing tax capability, customer type, and the desire to delegate determine which platform removes useful work. Across these comparisons, "
                    "the cheapest processing headline and the smallest administrative workload are different purchasing decisions [mEXMrWuZFRQ @ 00:01:11]."
                ),
                (
                    "The appeal of delegation is concrete in HelperMan's accounts of using both platforms for around six months. With Lemon Squeezy, they describe quick "
                    "setup for digital products, subscriptions, and software without a complicated back end. The interface makes products, customers, subscriptions, and "
                    "payouts straightforward to manage, while the merchant-of-record arrangement removes tax and payment administration. Their enthusiasm is specifically "
                    "for solo founders and small creators who want to start selling rather than build payment infrastructure [IA4eosnOzIE @ 00:00:17]. With Paddle, HelperMan "
                    "highlights recurring billing, upgrades, downgrades, and customer payment handling. They also describe the checkout as designed for online software "
                    "rather than general retail. These are working conveniences, not a claim that outsourcing produces unlimited control: the same review says the additional "
                    "services cost more than traditional processing and leave the seller with less direct control over payment and customer processes [o3KRrFnoAgM @ 00:00:48]. "
                    "Calderon Bridger frames the choice as time versus money and, more sharply, one frustration versus another. Running the tax side yourself creates one "
                    "kind of stress; accepting another platform's limits creates a different kind. Their conclusion is to match the tool to technical patience and the "
                    "freedom the business actually wants. That matches HelperMan's experience: simplicity is valuable precisely because someone else controls part of "
                    "the operation [k-wa2TZefr4 @ 00:02:30]."
                ),
                (
                    "The bundled features explain why equal base fees do not make two platforms interchangeable. How2Genius describes Paddle as a combined checkout, "
                    "payment, subscription, and tax system: it calculates sales tax, collects payment, and remits taxes for sales in the US, Canada, and other countries. "
                    "Their practical attraction is a single platform instead of several tools, with one-time purchases, subscriptions, trials, and coupon codes supporting "
                    "different product models [Y5VXhUB7aNM @ 00:00:18]. houdztech emphasizes the software-business side of that bundle: revenue recovery, subscription analytics "
                    "through ProfitWell, dunning, and hybrid models combining self-served subscriptions with sales-led invoicing. In the same comparison, Lemon Squeezy is "
                    "positioned around a simpler interface, email marketing, affiliates, and a no-code storefront rather than the same enterprise-oriented depth "
                    "[Qq-EyvVj7IM @ 00:02:30]. Hayes Tutorials identifies license keys, affiliate networks, and email marketing as Lemon Squeezy's creator-oriented tools "
                    "[mEXMrWuZFRQ @ 00:00:52]. Tutorly explains the operational benefit: an independent developer selling apps, plugins, or templates can manage sales, "
                    "licensing, and basic marketing together instead of connecting multiple services. Their recommendation distinguishes established B2B software from "
                    "smaller creator businesses. The shared baseline is therefore not merely outsourced tax. It is a payment arrangement whose billing, delivery, and "
                    "marketing features fit the product being sold and the customers buying it [IfaCBBIoVK0 @ 00:03:01]."
                ),
            ],
            "table": {
                "caption": "The shared decision framework: responsibility first, then the work each bundle removes.",
                "headers": [
                    "Operating situation",
                    "Practitioner-described fit",
                    "Expert Source",
                ],
                "rows": [
                    [
                        "A developer already handles taxes and wants a customizable payment experience.",
                        "Hayes positions standard Stripe Checkout around lower starting fees and developer control.",
                        "Hayes Tutorials ([mEXMrWuZFRQ @ 00:00:14])",
                    ],
                    [
                        "A solo creator wants products and subscriptions running without a complicated backend.",
                        "HelperMan describes Lemon Squeezy setup and administration as straightforward during their use.",
                        "HelperMan ([IA4eosnOzIE @ 00:00:17])",
                    ],
                    [
                        "A software seller wants recurring billing changes handled within the payment platform.",
                        "HelperMan praises Paddle's management of recurring charges, upgrades, downgrades, and customer payments.",
                        "HelperMan ([o3KRrFnoAgM @ 00:00:48])",
                    ],
                    [
                        "A B2B software business needs enterprise contracts and more complex billing arrangements.",
                        "Tutorly identifies Paddle's enterprise contracts, subscription adjustments, and wire transfers as useful.",
                        "Tutorly ([IfaCBBIoVK0 @ 00:02:28])",
                    ],
                    [
                        "A creator wants licensing and basic marketing alongside the payment collection system.",
                        "Hayes identifies Lemon Squeezy's built-in license keys, affiliate networks, and email marketing.",
                        "Hayes Tutorials ([mEXMrWuZFRQ @ 00:00:52])",
                    ],
                    [
                        "A founder must choose between tax administration and another platform's operational limits.",
                        "Calderon describes distinct frustrations from personal tax responsibility and restricted platform control.",
                        "Calderon Bridger ([k-wa2TZefr4 @ 00:02:30])",
                    ],
                ],
            },
        },
        {
            "id": "street-mechanics",
            "title": "Exact Street Mechanics, Tools & Numbers",
            "paragraphs": [
                (
                    "Build the price comparison from the layers the speakers actually name. SoloBuild quotes standard Stripe domestic US cards at 2.9% plus 30 cents, "
                    "with 1.5% added for international cards and another 1% for currency conversion. They also name a $15 dispute charge and free standard payouts. "
                    "Their subscription comparison adds the no-code Stripe Tax charge of 0.5% where registered and Stripe Billing at 0.7% of billing volume, producing "
                    "their rough 4.1% plus 30-cent US subscription estimate [i05UCC3UvNY @ 00:02:42]. Tutorly quotes Paddle's base at 5% plus 50 cents and presents it "
                    "as payment for the merchant-of-record arrangement, not just another card-processing rate [IfaCBBIoVK0 @ 00:02:12]. SoloBuild then models forty monthly "
                    "sales of a $50 product on US cards: approximately $80 for standard Stripe with Stripe Tax, $120 for Lemon Squeezy or Paddle, and $140 for Managed "
                    "Payments. They call the approximately $40 monthly handoff gap worth comparing with filing time and accountant costs [i05UCC3UvNY @ 00:06:42]. "
                    "heyymilian separately calculates 6.4% plus 30 cents for Managed Payments and 3.4% plus 30 cents for a build using Tax Basic. Those figures concern "
                    "their stated domestic-card comparison; SoloBuild's subscription stack includes the separately named Billing layer [0R3CB1EcgKA @ 00:05:11]."
                ),
                (
                    "OCH Platform's activation sequence is specific: first have a connected, active Stripe account, then activate Stripe Tax in the Stripe dashboard. "
                    "Activating Stripe itself is not enough. Inside the course platform, open the admin section, choose integrations, find Stripe Tax, and toggle it on. "
                    "Next choose tax behavior: inclusive puts tax inside the displayed price, while exclusive adds it on top at checkout. The speaker also describes "
                    "tax ID collection for business buyers, allowing the checkout to request a business name and tax ID. After configuring those options, hit activate "
                    "and inspect the checkout page [H8_HQ-GZOwc @ 00:00:17]. The operational boundary appears in the same walkthrough: customers must enter an address "
                    "so tax can be calculated, and tax will not appear on checkout pages or invoices unless the seller is registered in the specific tax jurisdiction. "
                    "The visible checkout result therefore depends on more than finding the toggle in the integrations screen [H8_HQ-GZOwc @ 00:01:26]. SoloBuild's "
                    "distinction completes this workflow without turning the switch into a different service: Stripe Tax can calculate and collect while the standard "
                    "Stripe seller remains responsible for the tax side. Their Tax Complete discussion separately names registration and filing and its $90 monthly "
                    "starting price. The activation demonstration and the responsibility comparison describe different parts of the same operating choice [i05UCC3UvNY @ 00:01:53]."
                ),
                (
                    "Stephen S. demonstrates Managed Payments from an existing Astro application rather than an empty product catalog. Their site already has pricing, "
                    "but its buttons do not yet open checkout. They install the Stripe Payments power in the IDE, authenticate the Stripe MCP against their sandbox "
                    "account, and ask the tool to create products and pricing matching the website. Their prompt also adds Managed Payments requirements because the "
                    "feature is newer. The resulting setup contains free, pro, and enterprise prices [F-WZgXuQIuQ @ 00:00:29]. The checkout uses a Managed Payments "
                    "preview API version, subscription mode, and Managed Payments enabled. After setting the environment variable, Stephen opens the pro checkout. "
                    "The first attempt also requires account setup and the correct product tax classification; their example is software as a service for personal "
                    "use. Stephen explicitly says backend webhooks are not connected yet and describes associating a user object with checkout so subscription webhook "
                    "records can later be linked [F-WZgXuQIuQ @ 00:03:38]. TechWealth Hub gives the short version: enable Managed Payments in the checkout session "
                    "and Stripe takes the merchant-of-record role. Their demonstration shows a $29 monthly checkout marked sold through Link. Stephen's account "
                    "supplies the setup work and unfinished backend boundary behind that compact enablement pitch [KRdWGDk-GkY @ 00:01:33]."
                ),
            ],
            "table": {
                "caption": "Quoted pricing layers and demonstrated configuration steps, kept in their stated contexts.",
                "headers": [
                    "Layer or operation",
                    "Exact reported number or execution detail",
                    "Expert Source",
                ],
                "rows": [
                    [
                        "Standard Stripe processing for the domestic US card case SoloBuild describes.",
                        "The stated base is 2.9% plus 30 cents before the separately named additions.",
                        "SoloBuild ([i05UCC3UvNY @ 00:02:42])",
                    ],
                    [
                        "Tax and recurring-billing additions in SoloBuild's standard Stripe subscription comparison.",
                        "No-code Tax adds 0.5%; Billing adds 0.7% of the stated billing volume.",
                        "SoloBuild ([i05UCC3UvNY @ 00:03:08])",
                    ],
                    [
                        "Managed Payments surcharge rather than the complete underlying Stripe processing charge.",
                        "SoloBuild reports an additional 3.5% per successful transaction on top of standard fees.",
                        "SoloBuild ([i05UCC3UvNY @ 00:05:58])",
                    ],
                    [
                        "Course-platform configuration after connecting and activating the seller's existing Stripe account.",
                        "Activate Stripe Tax in Stripe, then enable its integration inside the course platform.",
                        "OCH Platform ([H8_HQ-GZOwc @ 00:00:17])",
                    ],
                    [
                        "Customer information and registration conditions for the demonstrated course checkout tax display.",
                        "Buyers provide addresses, and tax display depends on registration in that specific jurisdiction.",
                        "OCH Platform ([H8_HQ-GZOwc @ 00:01:26])",
                    ],
                    [
                        "The first Managed Payments checkout attempt in Stephen's existing application demonstration.",
                        "Account setup required the correct tax classification before the checkout API would work.",
                        "Stephen S. ([F-WZgXuQIuQ @ 00:03:38])",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Use the details hidden behind the headline rate",
                "body": (
                    "The speakers' useful shortcuts concern the work included, the setup "
                    "that remains, and the dependencies that survive a platform change."
                ),
                "items": [
                    (
                        "Price your own filing time and accountant costs against the handoff premium: "
                        "SoloBuild's forty-sales example puts the Stripe-with-Tax versus Lemon Squeezy/Paddle "
                        "gap at about $40 monthly, or $480 yearly. "
                        "[SoloBuild — i05UCC3UvNY @ 00:07:02]"
                    ),
                    (
                        "For products under $10, use Paddle's custom-pricing conversation rather than "
                        "assuming its quoted pay-as-you-go rate is the only arrangement. "
                        "[SoloBuild — i05UCC3UvNY @ 00:05:19]"
                    ),
                    (
                        "Do not treat an active Stripe connection as Stripe Tax activation: turn on "
                        "Stripe Tax in the dashboard and then its course-platform integration. "
                        "[OCH Platform — H8_HQ-GZOwc @ 00:00:17]"
                    ),
                    (
                        "Let existing license keys drive the migration decision before fees, and keep "
                        "the customer list, license server, and checkout links in your own hands. "
                        "[Gaurav Tiwari — cNc29NtuCYU @ 00:04:07]"
                    ),
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Choose the responsibility model",
                    "action": "Start with buyer geography, tax workload, and the extras the business needs.",
                    "detail": (
                        "SoloBuild orders the decision around where buyers live, how much tax paperwork "
                        "the seller will own, and whether storefront, affiliate, or billing-support features "
                        "matter. Their standard Stripe recommendation differs from their international "
                        "merchant-of-record recommendation. [SoloBuild — i05UCC3UvNY @ 00:07:44]"
                    ),
                },
                {
                    "step": 2,
                    "title": "Activate the demonstrated Stripe Tax path",
                    "action": "Enable Stripe Tax and configure the course-platform integration.",
                    "detail": (
                        "With Stripe connected and active, enable Stripe Tax in its dashboard; open course "
                        "admin integrations, choose inclusive or exclusive behavior, enable tax ID collection "
                        "if needed, activate, and inspect checkout. OCH also says tax display requires registration "
                        "in the applicable jurisdiction. [OCH Platform — H8_HQ-GZOwc @ 00:01:26] "
                        "[OCH Platform — H8_HQ-GZOwc @ 00:01:44]"
                    ),
                },
                {
                    "step": 3,
                    "title": "Wire the demonstrated Managed Payments checkout",
                    "action": "Use existing application pricing to create products, prices, and checkout.",
                    "detail": (
                        "Stephen installs the Stripe power, authenticates its MCP connection to their account, "
                        "and asks the IDE to build the pricing and subscription structure already displayed "
                        "on the website. Their demonstration requires product tax classification and leaves "
                        "backend webhook connections unfinished. [Stephen S. — F-WZgXuQIuQ @ 00:04:20] "
                        "[Stephen S. — F-WZgXuQIuQ @ 00:03:38]"
                    ),
                },
                {
                    "step": 4,
                    "title": "Execute Gaurav's migration order",
                    "action": "Export, stop new PayPal subscriptions, test the replacement, replace links, and notify buyers.",
                    "detail": (
                        "Gaurav's sequence is to export customers, orders, subscriptions, and license keys; "
                        "turn PayPal off at checkout so new subscribers can migrate; set up the new provider "
                        "in test mode; replace every link; and email customers about the new card-statement name. "
                        "[Gaurav Tiwari — cNc29NtuCYU @ 00:03:50]"
                    ),
                },
            ],
        },
        {
            "id": "disagreements-alternatives",
            "title": "Where Practitioners Disagree & Alternative Playbooks",
            "paragraphs": [
                (
                    "Managed Payments receives very different verdicts because the speakers describe different availability and coverage claims. TechWealth Hub presents it "
                    "as available in public preview, with full merchant-of-record support and selective use by transaction. Their recommendation is enthusiastic: an existing "
                    "Stripe user can add the role without moving to another platform, while a new software business can start with Stripe and enable it where needed "
                    "[KRdWGDk-GkY @ 00:04:13]. Captain Vova describes a narrower offering: Europe, the US, Canada, and the UK are covered in the documentation they discuss, "
                    "while Australia, India, and other locations remain outside that tax coverage. They explicitly reject treating that version as full global sales-tax "
                    "coverage [5zGuxRrg_O0 @ 00:00:45]. heyymilian discusses another boundary: the seller must be based in a supported location, and the supported product "
                    "categories are digital products rather than physical goods, professional services, or live in-person events. That is a business-eligibility question, "
                    "not the same question as where buyers are taxed [0R3CB1EcgKA @ 00:02:54]. Tutorly's alternative framework stays centered on business fit: standard "
                    "Stripe for control and existing tax handling, Paddle for B2B, and Lemon Squeezy for creators. These accounts do not support treating a broad launch "
                    "pitch as a universal answer about every seller, product, and market [IfaCBBIoVK0 @ 00:03:32]."
                ),
                (
                    "The fee accounts also disagree, and the disagreement changes what a comparison means. Yumi Kato Reviews first quotes Lemon Squeezy at 5% plus "
                    "50 cents, then says adding Stripe processing puts a referenced table near 7.9% plus a flat charge. They additionally report that Lemon Squeezy "
                    "refunds its platform fee when a buyer receives a refund [jwFYqAi_nQY @ 00:00:47]. SoloBuild describes a different structure: the 5% plus 50-cent "
                    "transaction rate, with named extras of 1.5% for international transactions, 1.5% for PayPal, and 0.5% for subscription payments. They also distinguish "
                    "payout costs, describing free US bank payouts and 1% for bank accounts outside the US [i05UCC3UvNY @ 00:03:53]. heyymilian's November 23, 2026 "
                    "price capture likewise starts Lemon Squeezy at 5% plus 50 cents with small additional fees in edge cases, while explicitly describing Managed "
                    "Payments as a surcharge in addition to processing. Their migration promotion is another separate price, not the permanent standard rate "
                    "[0R3CB1EcgKA @ 00:04:18]. HelperMan offers the useful business test without settling those conflicting totals: decide whether simpler administration "
                    "and tax handling are worth the extra fees for the actual business model. Their positive six-month verdict still leaves growing businesses wanting "
                    "more advanced control. A favorable simplicity review and an attractive headline rate are not the same evaluation [IA4eosnOzIE @ 00:01:52]."
                ),
                (
                    "Alternative playbooks turn on the feature that cannot disappear during the move. How2Genius prefers Paddle for quick setup and easy subscriptions, "
                    "but describes FastSpring as the stronger customization route: branded storefronts and checkout, upsells, bundles, localized pricing, flexible billing, "
                    "and international payment support. Their comparison does not reduce international selling to a tax toggle; it includes the selling experience and "
                    "the tools around it [Y5VXhUB7aNM @ 00:02:11]. Gaurav Tiwari starts elsewhere when existing customers already hold license keys. They put Dodo "
                    "Payments first for importing active Lemon Squeezy keys alongside products, customers, and coupons, quoting 4% plus 40 cents, PayPal support, and "
                    "acceptance of businesses in India. The tradeoff is explicit: imported keys lose their activations, and the migration tool is still in beta. "
                    "Their lower-flat-fee alternative is Creem at 3.9% plus 40 cents without an international-card extra [cNc29NtuCYU @ 00:02:14]. Gaurav then attaches "
                    "the missing pieces: Creem has no PayPal and does not move active subscriptions; Polar's free plan matches Lemon Squeezy's rate, while its $20 "
                    "plan drops to 3.8% plus 40 cents; Paddle supports PayPal but has no license keys. For WordPress products they name Freemius for licensing and "
                    "updates, while explicitly saying they have not sold through it themselves [cNc29NtuCYU @ 00:02:50]."
                ),
            ],
            "table": {
                "caption": "Keep conflicting claims and alternative feature bundles separate rather than merging them.",
                "headers": [
                    "Position or alternative",
                    "Contrasting claim or attached limitation",
                    "Expert Source",
                ],
                "rows": [
                    [
                        "TechWealth Hub promotes selective Managed Payments with broad merchant-of-record support in public preview.",
                        "Captain Vova describes limited geographic tax coverage in the version they discuss.",
                        "TechWealth Hub ([KRdWGDk-GkY @ 00:04:13]); Captain Vova (Vova Feldman) ([5zGuxRrg_O0 @ 00:00:45])",
                    ],
                    [
                        "Yumi adds Stripe processing and describes a Lemon Squeezy total near 7.9%.",
                        "SoloBuild instead quotes the base and explicitly named international, PayPal, and subscription additions.",
                        "Yumi Kato Reviews ([jwFYqAi_nQY @ 00:00:47]); SoloBuild ([i05UCC3UvNY @ 00:03:53])",
                    ],
                    [
                        "How2Genius favors Paddle for quick setup and straightforward subscription and tax administration.",
                        "FastSpring receives their recommendation for greater checkout control, pricing flexibility, and international expansion.",
                        "How2Genius ([Y5VXhUB7aNM @ 00:03:07])",
                    ],
                    [
                        "Gaurav prioritizes Dodo when customers already possess active Lemon Squeezy license keys.",
                        "They report imported keys lose activations and the migration tool remains in beta.",
                        "Gaurav Tiwari ([cNc29NtuCYU @ 00:02:14]); Gaurav Tiwari ([cNc29NtuCYU @ 00:02:30])",
                    ],
                    [
                        "Gaurav quotes Creem at 3.9% plus 40 cents without an international-card extra.",
                        "Their comparison also says Creem lacks PayPal and cannot move active subscriptions.",
                        "Gaurav Tiwari ([cNc29NtuCYU @ 00:02:30]); Gaurav Tiwari ([cNc29NtuCYU @ 00:02:50])",
                    ],
                    [
                        "Tutorly presents Paddle's enterprise contracts and wire transfers as useful B2B capabilities.",
                        "How2Genius emphasizes FastSpring's branded storefronts, bundles, upsells, and localized pricing capabilities instead.",
                        "Tutorly ([IfaCBBIoVK0 @ 00:02:28]); How2Genius ([Y5VXhUB7aNM @ 00:02:11])",
                    ],
                ],
            },
        },
        {
            "id": "failure-modes",
            "title": "Firsthand Failure Modes, Traps & Economics Checks",
            "paragraphs": [
                (
                    "The strongest firsthand constraints concern access and operating control, not a reported windfall. HelperMan says Paddle account approvals and reviews "
                    "can take time, particularly for new businesses or unusual models. Their advice after using it is to understand how the merchant-of-record model "
                    "changes payments, taxes, and customer billing before choosing it. They still value the service, but their experience does not describe immediate "
                    "entry or unrestricted control [o3KRrFnoAgM @ 00:01:38]. Gaurav Tiwari identifies a direct migration blocker: they sell plugins from India, and say "
                    "the Managed Payments replacement is not available to their business there. Their $99-sale comparison also reverses the initial price advantage: "
                    "they quote $5.45 for Lemon Squeezy, $4.66 on Stripe's migration rate, and $6.64 after that rate expires on December 1, 2027 "
                    "[cNc29NtuCYU @ 00:01:33]. Gaurav's own checkout experience is different: they sell plugins through FluentCart and also name Easy Digital Downloads "
                    "and their own Core Forms. None of those, they say, imports from Lemon Squeezy, leaving a manual move [cNc29NtuCYU @ 00:03:31]. Yumi's "
                    "suspension example is not their own operating loss: they recount another seller's sudden high-risk suspension after a month and slow support. "
                    "That distinction keeps a reported customer complaint separate from HelperMan's use and Gaurav's business situation [jwFYqAi_nQY @ 00:01:39]."
                ),
                (
                    "The shutdown reports agree on the hard endpoint but disagree on one tooling date. Folioquest reports March 31, 2027 as the shutdown date, with "
                    "new signups closed and no deadline extensions. Their account makes active subscriptions part of the cutoff rather than an exception that can "
                    "continue indefinitely [M61DsgB51BI @ 00:00:18]. heyymilian reports November 16, 2026 for the end of new users and stores, December 6 for eligible "
                    "Managed Payments migration tooling, and mid-January 2027 as the recommended latest start because the process can take up to eight weeks "
                    "[0R3CB1EcgKA @ 00:01:28]. Gaurav gives December 2 for that tooling opening and the same mid-January start recommendation. Their operational "
                    "argument is that a February start leaves no time to fix a failed import; this is a planning warning, not a claim that they personally suffered "
                    "that failed import [cNc29NtuCYU @ 00:00:19]. Folioquest also gives December 2 and describes moving catalogs, webhooks, and live subscriptions "
                    "as a four-to-eight-week process. The useful agreement is the size of the migration job and the need to begin well before the final processing "
                    "date. The disagreement remains December 2 versus December 6; neither date changes these speakers' shared mid-January recommendation or their "
                    "reported March endpoint [M61DsgB51BI @ 00:01:36]."
                ),
                (
                    "The handoff fails as a like-for-like replacement wherever payment migration is mistaken for product delivery. Gaurav says the official tooling "
                    "moves products, customers, and card subscriptions, with customers receiving at least fourteen days' notice. They also say Managed Payments "
                    "does not provide license keys, file delivery, or affiliates; PayPal subscriptions cannot move, affected subscribers must buy again, and checkout "
                    "links, buttons, and webhooks require manual replacement rather than automatic redirects [cNc29NtuCYU @ 00:00:55]. heyymilian independently "
                    "identifies missing storefronts, digital fulfillment, license keys, download links, and affiliates. Their conclusion is that sellers of files or "
                    "license keys still need a fulfillment tool even when choosing Managed Payments rather than taking tax responsibility themselves "
                    "[0R3CB1EcgKA @ 00:02:37]. Gaurav's execution order responds directly: export customers, orders, subscriptions, and keys; turn off PayPal for "
                    "new checkout subscriptions; configure the new provider in test mode; replace every link; then tell customers the new name that will appear "
                    "on card statements [cNc29NtuCYU @ 00:03:50]. Stephen's demonstration supplies a smaller version of the same unfinished-work problem: "
                    "opening checkout did not mean backend webhooks were connected. They explicitly left those connections out and described linking a user object "
                    "to later subscription records. A working payment page was the demonstrated result, not a completed subscription backend [F-WZgXuQIuQ @ 00:03:53]."
                ),
            ],
            "table": {
                "caption": "Firsthand constraints, reported complaints, and migration dependencies with their attribution intact.",
                "headers": [
                    "Failure mode or economic trap",
                    "Practitioner experience or specific reported boundary",
                    "Expert Source",
                ],
                "rows": [
                    [
                        "A newer business expects Paddle account access without waiting for its reviews.",
                        "HelperMan says approvals and reviews can take time, especially for unusual business models.",
                        "HelperMan ([o3KRrFnoAgM @ 00:01:38])",
                    ],
                    [
                        "A seller assumes the recommended Stripe replacement accepts their business registration location.",
                        "Gaurav says their India-based plugin business cannot use that Managed Payments migration path.",
                        "Gaurav Tiwari ([cNc29NtuCYU @ 00:01:33])",
                    ],
                    [
                        "A favorable migration promotion is treated as the permanent cost of each sale.",
                        "Gaurav quotes $4.66 initially and $6.64 afterward on the same $99 sale.",
                        "Gaurav Tiwari ([cNc29NtuCYU @ 00:01:33])",
                    ],
                    [
                        "A seller relies on one uncontested date for the opening of migration tooling.",
                        "Folioquest reports December 2, while heyymilian reports December 6 for eligible stores.",
                        "Folioquest ([M61DsgB51BI @ 00:01:36]); heyymilian ([0R3CB1EcgKA @ 00:01:28])",
                    ],
                    [
                        "A business expects existing PayPal subscribers and checkout links to transfer automatically.",
                        "Gaurav says PayPal subscribers must buy again and links require manual replacement.",
                        "Gaurav Tiwari ([cNc29NtuCYU @ 00:00:55])",
                    ],
                    [
                        "A successful checkout demonstration is mistaken for completed backend subscription record handling.",
                        "Stephen explicitly says webhooks are not connected and discusses later user-record association.",
                        "Stephen S. ([F-WZgXuQIuQ @ 00:03:53]); Stephen S. ([F-WZgXuQIuQ @ 00:04:38])",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Check the dependencies the practitioners say can break the move",
                "body": (
                    "These checks follow the reported eligibility, timing, fulfillment, "
                    "and payout constraints rather than the appearance of the checkout page."
                ),
                "items": [
                    (
                        "Check seller-location eligibility before treating Managed Payments as the destination: "
                        "Gaurav says their India-based plugin business is excluded from that path. "
                        "[Gaurav Tiwari — cNc29NtuCYU @ 00:01:33]"
                    ),
                    (
                        "Plan around the recommended mid-January migration start rather than the last processing "
                        "day: Gaurav warns that starting in February leaves no time to fix a failed import. "
                        "[Gaurav Tiwari — cNc29NtuCYU @ 00:00:19]"
                    ),
                    (
                        "Account for file delivery, license keys, download links, storefronts, and affiliates "
                        "separately; heyymilian says Managed Payments does not include those Lemon Squeezy functions. "
                        "[heyymilian — 0R3CB1EcgKA @ 00:02:21] "
                        "[heyymilian — 0R3CB1EcgKA @ 00:02:37]"
                    ),
                    (
                        "Include payout timing and minimum balance in the platform comparison: SoloBuild describes "
                        "Paddle's monthly schedule, payment by the fifteenth, and $100 minimum. "
                        "[SoloBuild — i05UCC3UvNY @ 00:05:36]"
                    ),
                ],
            },
        },
    ],
    "pull_quote": (
        "\"The real question isn't who renders the form, it's who carries the tax.\" "
        "— heyymilian (0R3CB1EcgKA @ 00:06:01)."
    ),
    "diagram_id": "diag-05",
    "action_checklist": [
        (
            "Begin with buyer geography, decide how much tax paperwork to own, and then compare "
            "the storefront, affiliate, and billing-support extras. "
            "[SoloBuild — i05UCC3UvNY @ 00:07:44]"
        ),
        (
            "Compare the handoff premium with accountant costs and personal registration and filing time, "
            "rather than comparing processing percentages alone. "
            "[SoloBuild — i05UCC3UvNY @ 00:07:25]"
        ),
        (
            "For the demonstrated course setup, activate Stripe Tax in Stripe and the course platform, "
            "choose tax behavior, enable tax ID collection if needed, and inspect checkout. "
            "[OCH Platform — H8_HQ-GZOwc @ 00:01:44]"
        ),
        (
            "Complete the product tax classification required by the Managed Payments setup, and keep "
            "Stephen's unfinished backend webhook connection separate from the working checkout demonstration. "
            "[Stephen S. — F-WZgXuQIuQ @ 00:03:38] "
            "[Stephen S. — F-WZgXuQIuQ @ 00:03:53]"
        ),
        (
            "Export customers, orders, subscriptions, and license keys; stop new PayPal subscriptions; "
            "set the replacement up in test mode; replace links; and notify buyers about the statement name. "
            "[Gaurav Tiwari — cNc29NtuCYU @ 00:03:50]"
        ),
        (
            "Choose the migration path around existing license keys before fees, and retain control "
            "of the customer list, license server, and checkout links. "
            "[Gaurav Tiwari — cNc29NtuCYU @ 00:04:07]"
        ),
    ],
    "statutory_citations": [
        {
            "title": "SoloBuild — Stripe vs Lemon Squeezy vs Paddle (2026): Which Should You Use? [00:01:53]",
            "url": "https://www.youtube.com/watch?v=i05UCC3UvNY&t=113s",
            "relevance": (
                "Primary practitioner testimony distinguishing standard Stripe tax responsibility, "
                "Stripe Tax calculation and collection, and Tax Complete registration and filing."
            ),
        },
        {
            "title": "OCH Platform — How to Enable Stripe Tax to Handle Sales Tax Automatically [00:01:26]",
            "url": "https://www.youtube.com/watch?v=H8_HQ-GZOwc&t=86s",
            "relevance": (
                "Primary practitioner testimony on address collection and the registration condition "
                "for tax appearing on checkout pages and invoices."
            ),
        },
        {
            "title": "Stephen S. — Stripe's Merchant of Record (MoR) Solution: Adding Managed Payments to an Existing App  #mcp [00:03:38]",
            "url": "https://www.youtube.com/watch?v=F-WZgXuQIuQ&t=218s",
            "relevance": (
                "Primary practitioner testimony from the checkout demonstration about account setup "
                "and the product tax classification needed for Managed Payments."
            ),
        },
        {
            "title": "Gaurav Tiwari — Lemon Squeezy Is Shutting Down, and Stripe's Fix Leaves Out License Keys [00:03:50]",
            "url": "https://www.youtube.com/watch?v=cNc29NtuCYU&t=230s",
            "relevance": (
                "Primary practitioner testimony giving the export, PayPal, test-mode, replacement-link, "
                "and customer-notification migration sequence."
            ),
        },
    ],
    "source_citations": [
        {
            "source_type": "video_pro_tip",
            "video_id": "IA4eosnOzIE",
            "title": "Lemon Squeezy for Merchant of Record Honest Review - Watch Before Using",
            "channel": "HelperMan",
            "author": "HelperMan",
            "text": "One thing I'd strongly recommend is making sure the simplicity and tax handling are actually worth the extra fees for your business model.",
            "tip": "One thing I'd strongly recommend is making sure the simplicity and tax handling are actually worth the extra fees for your business model.",
            "timestamp": 112,
            "timestamp_seconds": 112,
            "timestamp_label": "[00:01:52]",
            "url": "https://www.youtube.com/watch?v=IA4eosnOzIE&t=112s",
            "markdown": "[00:01:52](https://www.youtube.com/watch?v=IA4eosnOzIE&t=112s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on comparing administrative simplicity with the additional merchant-of-record fee.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "M61DsgB51BI",
            "title": "Lemon Squeezy Winds Down After Stripe Acquisition",
            "channel": "Folioquest",
            "author": "Folioquest",
            "text": "Automated data exports and migration tools open on December 2nd, 2026. Because moving catalogs, webhooks, and live subscriptions can take four to eight weeks, Lemon Squeezy urges sellers to begin by mid-January.",
            "tip": "Automated data exports and migration tools open on December 2nd, 2026. Because moving catalogs, webhooks, and live subscriptions can take four to eight weeks, Lemon Squeezy urges sellers to begin by mid-January.",
            "timestamp": 96,
            "timestamp_seconds": 96,
            "timestamp_label": "[00:01:36]",
            "url": "https://www.youtube.com/watch?v=M61DsgB51BI&t=96s",
            "markdown": "[00:01:36](https://www.youtube.com/watch?v=M61DsgB51BI&t=96s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner report of migration timing, with a tooling date that differs from heyymilian's account.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "o3KRrFnoAgM",
            "title": "Paddle for Merchant of Record Honest Review - Watch Before Using",
            "channel": "HelperMan",
            "author": "HelperMan",
            "text": "I also noticed that account approvals and compliance reviews can sometimes take time, especially for newer businesses or unusual business models.",
            "tip": "I also noticed that account approvals and compliance reviews can sometimes take time, especially for newer businesses or unusual business models.",
            "timestamp": 98,
            "timestamp_seconds": 98,
            "timestamp_label": "[00:01:38]",
            "url": "https://www.youtube.com/watch?v=o3KRrFnoAgM&t=98s",
            "markdown": "[00:01:38](https://www.youtube.com/watch?v=o3KRrFnoAgM&t=98s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Firsthand practitioner observation about Paddle review timing and the importance of understanding its operating model.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "5zGuxRrg_O0",
            "title": "Stripe Managed Payments: The Threat to Paddle and the Future of MoR",
            "channel": "Captain Vova (Vova Feldman)",
            "author": "Captain Vova (Vova Feldman)",
            "text": "The current downside in comparing Managed Payments to other Merchant of Records is there's no full global tax compliance yet.",
            "tip": "The current downside in comparing Managed Payments to other Merchant of Records is there's no full global tax compliance yet.",
            "timestamp": 45,
            "timestamp_seconds": 45,
            "timestamp_label": "[00:00:45]",
            "url": "https://www.youtube.com/watch?v=5zGuxRrg_O0&t=45s",
            "markdown": "[00:00:45](https://www.youtube.com/watch?v=5zGuxRrg_O0&t=45s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner description of geographic tax-coverage limits in the Managed Payments offering they discuss.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "KRdWGDk-GkY",
            "title": "Stripe Just KILLED Paddle and Gumroad (Managed Payments)",
            "channel": "TechWealth Hub",
            "author": "TechWealth Hub",
            "text": "Stripe managed payments can be applied selectively by transaction, by market, or by product line.",
            "tip": "Stripe managed payments can be applied selectively by transaction, by market, or by product line.",
            "timestamp": 163,
            "timestamp_seconds": 163,
            "timestamp_label": "[00:02:43]",
            "url": "https://www.youtube.com/watch?v=KRdWGDk-GkY&t=163s",
            "markdown": "[00:02:43](https://www.youtube.com/watch?v=KRdWGDk-GkY&t=163s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner description of selective Managed Payments use rather than a platform-wide all-or-nothing switch.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "i05UCC3UvNY",
            "title": "Stripe vs Lemon Squeezy vs Paddle (2026): Which Should You Use?",
            "channel": "SoloBuild",
            "author": "SoloBuild",
            "text": "Count your accountant fees and your own time for registering and filing. If they add up to more than that, the handed-off option is the cheaper one.",
            "tip": "Count your accountant fees and your own time for registering and filing. If they add up to more than that, the handed-off option is the cheaper one.",
            "timestamp": 445,
            "timestamp_seconds": 445,
            "timestamp_label": "[00:07:25]",
            "url": "https://www.youtube.com/watch?v=i05UCC3UvNY&t=445s",
            "markdown": "[00:07:25](https://www.youtube.com/watch?v=i05UCC3UvNY&t=445s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner economic comparison including tax-administration time rather than processing fees alone.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "IfaCBBIoVK0",
            "title": "Lemon Squeezy Vs Stripe Checkout Vs Paddle (2026) Which One Is Better?",
            "channel": "Tutorly",
            "author": "Tutorly",
            "text": "Stripe Checkout is a standard payment processor, while Paddle and Lemon Squeezy act as a merchant of record. A merchant of record means the platform becomes the legal seller of your product.",
            "tip": "Stripe Checkout is a standard payment processor, while Paddle and Lemon Squeezy act as a merchant of record. A merchant of record means the platform becomes the legal seller of your product.",
            "timestamp": 32,
            "timestamp_seconds": 32,
            "timestamp_label": "[00:00:32]",
            "url": "https://www.youtube.com/watch?v=IfaCBBIoVK0&t=32s",
            "markdown": "[00:00:32](https://www.youtube.com/watch?v=IfaCBBIoVK0&t=32s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner explanation of the legal-seller distinction underlying the checkout comparison.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Y5VXhUB7aNM",
            "title": "NEW* Paddle vs FastSpring — Best Checkout & Tax for Digital Products",
            "channel": "How2Genius",
            "author": "How2Genius",
            "text": "FastSpring stands out for its robust customization. You can create fully branded storefronts and checkout experiences, including upsells, bundles, and localized pricing.",
            "tip": "FastSpring stands out for its robust customization. You can create fully branded storefronts and checkout experiences, including upsells, bundles, and localized pricing.",
            "timestamp": 131,
            "timestamp_seconds": 131,
            "timestamp_label": "[00:02:11]",
            "url": "https://www.youtube.com/watch?v=Y5VXhUB7aNM&t=131s",
            "markdown": "[00:02:11](https://www.youtube.com/watch?v=Y5VXhUB7aNM&t=131s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner comparison of FastSpring's customization features with Paddle's simpler setup positioning.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Qq-EyvVj7IM",
            "title": "Paddle vs LemonSqueezy (2026) | Which One is Better?",
            "channel": "houdztech",
            "author": "houdztech",
            "text": "Lemon Squeezy is designed for simplicity. The UI is clean, modern, and genuinely easy to navigate. Setup takes 15 to 30 minutes.",
            "tip": "Lemon Squeezy is designed for simplicity. The UI is clean, modern, and genuinely easy to navigate. Setup takes 15 to 30 minutes.",
            "timestamp": 164,
            "timestamp_seconds": 164,
            "timestamp_label": "[00:02:44]",
            "url": "https://www.youtube.com/watch?v=Qq-EyvVj7IM&t=164s",
            "markdown": "[00:02:44](https://www.youtube.com/watch?v=Qq-EyvVj7IM&t=164s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner positioning of Lemon Squeezy's setup and interface for independent makers and small teams.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "F-WZgXuQIuQ",
            "title": "Stripe's Merchant of Record (MoR) Solution: Adding Managed Payments to an Existing App  #mcp",
            "channel": "Stephen S.",
            "author": "Stephen S.",
            "text": "I had to go in and specify the correct tax classification. So in this case, software as a service personal use for these products.",
            "tip": "I had to go in and specify the correct tax classification. So in this case, software as a service personal use for these products.",
            "timestamp": 218,
            "timestamp_seconds": 218,
            "timestamp_label": "[00:03:38]",
            "url": "https://www.youtube.com/watch?v=F-WZgXuQIuQ&t=218s",
            "markdown": "[00:03:38](https://www.youtube.com/watch?v=F-WZgXuQIuQ&t=218s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Firsthand setup requirement encountered while opening Managed Payments checkout in an existing application.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "mEXMrWuZFRQ",
            "title": "Stripe Checkout vs Paddle vs Lemon Squeezy: Payment Platform Comparison",
            "channel": "Hayes Tutorials",
            "author": "Hayes Tutorials",
            "text": "Choose Stripe if you already handle taxes or sell locally. Choose Paddle if you sell to businesses. Choose Lemon Squeezy if you sell to consumers.",
            "tip": "Choose Stripe if you already handle taxes or sell locally. Choose Paddle if you sell to businesses. Choose Lemon Squeezy if you sell to consumers.",
            "timestamp": 90,
            "timestamp_seconds": 90,
            "timestamp_label": "[00:01:30]",
            "url": "https://www.youtube.com/watch?v=mEXMrWuZFRQ&t=90s",
            "markdown": "[00:01:30](https://www.youtube.com/watch?v=mEXMrWuZFRQ&t=90s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner recommendation organized around tax capability and business-versus-consumer customers.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "jwFYqAi_nQY",
            "title": "Lemon Squeezy Review: Is the Merchant of Record Deal Worth It? (2026)",
            "channel": "Yumi Kato Reviews",
            "author": "Yumi Kato Reviews",
            "text": "Add Stripe's processing, and that table puts the total near 7.9% plus a flat charge per transaction.",
            "tip": "Add Stripe's processing, and that table puts the total near 7.9% plus a flat charge per transaction.",
            "timestamp": 47,
            "timestamp_seconds": 47,
            "timestamp_label": "[00:00:47]",
            "url": "https://www.youtube.com/watch?v=jwFYqAi_nQY&t=47s",
            "markdown": "[00:00:47](https://www.youtube.com/watch?v=jwFYqAi_nQY&t=47s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner fee claim contrasted with SoloBuild's and heyymilian's base-plus-specific-additions descriptions.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "k-wa2TZefr4",
            "title": "Lemon Squeezy vs Stripe Merchant Platform Review 2026: Payouts & Features",
            "channel": "Calderon Bridger",
            "author": "Calderon Bridger",
            "text": "There is a specific kind of stress that comes with managing your own tax liability. There is also a specific kind of frustration that comes with being limited by someone else's platform.",
            "tip": "There is a specific kind of stress that comes with managing your own tax liability. There is also a specific kind of frustration that comes with being limited by someone else's platform.",
            "timestamp": 150,
            "timestamp_seconds": 150,
            "timestamp_label": "[00:02:30]",
            "url": "https://www.youtube.com/watch?v=k-wa2TZefr4&t=150s",
            "markdown": "[00:02:30](https://www.youtube.com/watch?v=k-wa2TZefr4&t=150s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner framing of the trade between tax responsibility and platform restrictions.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "H8_HQ-GZOwc",
            "title": "How to Enable Stripe Tax to Handle Sales Tax Automatically",
            "channel": "OCH Platform",
            "author": "OCH Platform",
            "text": "Tax won't show up on checkout pages or invoices unless you're registered in that specific tax jurisdiction.",
            "tip": "Tax won't show up on checkout pages or invoices unless you're registered in that specific tax jurisdiction.",
            "timestamp": 86,
            "timestamp_seconds": 86,
            "timestamp_label": "[00:01:26]",
            "url": "https://www.youtube.com/watch?v=H8_HQ-GZOwc&t=86s",
            "markdown": "[00:01:26](https://www.youtube.com/watch?v=H8_HQ-GZOwc&t=86s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner-stated registration condition in the Stripe Tax activation walkthrough.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "0R3CB1EcgKA",
            "title": "Lemon Squeezy is closing. Can you just run your own checkout?",
            "channel": "heyymilian",
            "author": "heyymilian",
            "text": "Digital fulfillment not included. Managed payments doesn't deliver files, license keys, or download links. Affiliates not included either.",
            "tip": "Digital fulfillment not included. Managed payments doesn't deliver files, license keys, or download links. Affiliates not included either.",
            "timestamp": 157,
            "timestamp_seconds": 157,
            "timestamp_label": "[00:02:37]",
            "url": "https://www.youtube.com/watch?v=0R3CB1EcgKA&t=157s",
            "markdown": "[00:02:37](https://www.youtube.com/watch?v=0R3CB1EcgKA&t=157s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner identification of fulfillment and affiliate gaps in the Managed Payments replacement.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "cNc29NtuCYU",
            "title": "Lemon Squeezy Is Shutting Down, and Stripe's Fix Leaves Out License Keys",
            "channel": "Gaurav Tiwari",
            "author": "Gaurav Tiwari",
            "text": "Export everything now: customers, orders, subscriptions, and license keys. Turn PayPal off at checkout so new subscribers can migrate. Set up the new provider in test mode. Replace every link. Then email your customers and tell them the new name on their card statement.",
            "tip": "Export everything now: customers, orders, subscriptions, and license keys. Turn PayPal off at checkout so new subscribers can migrate. Set up the new provider in test mode. Replace every link. Then email your customers and tell them the new name on their card statement.",
            "timestamp": 230,
            "timestamp_seconds": 230,
            "timestamp_label": "[00:03:50]",
            "url": "https://www.youtube.com/watch?v=cNc29NtuCYU&t=230s",
            "markdown": "[00:03:50](https://www.youtube.com/watch?v=cNc29NtuCYU&t=230s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner migration sequence covering exports, payment-method handling, testing, replacement links, and customer communication.",
        },
    ],
}
