from __future__ import annotations

CHAPTER_6 = {
    "id": "Q6",
    "chapter_id": "Q6",
    "chapter_number": 6,
    "question_number": 6,
    "slug": "build-the-order-bump-and-upsell-sequence",
    "question_prompt": "How do I implement order bumps, one-click upsells, downsells, and product delivery to increase the value of each purchase?",
    "kicker": "Q6 / THE BIG MONEY PLAYBOOKS",
    "title": "Build the Order Bump and Upsell Sequence",
    "subtitle": "GoHighLevel, Systeme.io, ClickFunnels, Shopify, SamCart, WPFunnels, and WooCommerce implementations, plus DM automation and post-purchase delivery",
    "layout_template": "step_by_step_blueprint",
    "reading_time_minutes": 15,
    "executive_summary": (
        "The common play is a related checkout add-on, a post-payment offer, and delivery tied to what the buyer actually purchased. "
        "Marketing Mark demonstrates a $27 checkout becoming $44 with a $17 bump; Maik Kleinert reports a $7 product producing a $57 order. "
        "The builders connect products, prices, page elements, acceptance buttons, and access workflows rather than stopping at persuasive copy. "
        "Their alternatives matter: Zero to Launch starts with a bump, Knola builds the upsell first, and SamCart distinguishes additive offers from prorated upgrades. "
        "Default selection, downsell structure, and funnel length also differ. "
        "Social Nest Marketing encounters oversized files, broken routing, and mismatched prices; Prompt On Fire warns that a purchase tag does not book a call."
    ),
    "key_metrics": [
        {
            "label": "GoHighLevel checkout with bump",
            "metric": "GoHighLevel checkout with bump",
            "value": "$27 + $17 = $44",
            "confidence": "attributed_practitioner_claim",
            "context": "Marketing Mark toggles the $17 bump on a $27 main offer and shows the checkout charging $44 for both products.",
            "source": "Marketing Mark ([qUqLPLYblBI @ 00:03:11])",
        },
        {
            "label": "DM-connected product bundle",
            "metric": "DM-connected product bundle",
            "value": "$7 entry product; $57 three-product order",
            "confidence": "attributed_practitioner_claim",
            "context": "Maik Kleinert describes the $7 product with a mini course reduced from $27 to $20 and another product reduced from $47 to $30.",
            "source": "Maik Kleinert | Content-to-Conversion Systems ([pE2Z7vTYfSw @ 00:03:27])",
        },
        {
            "label": "SamCart bump acceptance benchmark",
            "metric": "SamCart bump acceptance benchmark",
            "value": "30 to 40%",
            "confidence": "attributed_practitioner_claim",
            "context": "Scott Moran describes this as a good order-bump acceptance rate, while saying upsell acceptance varies with the offer's price.",
            "source": "SamCart ([UxhtBuVj4gY @ 00:25:13])",
        },
        {
            "label": "Watercolor downsell payment schedule",
            "metric": "Watercolor downsell payment schedule",
            "value": "$10 each month; three payments; zero trial period",
            "confidence": "attributed_practitioner_claim",
            "context": "Zero to Launch configures the same landscapes course as a payment-plan downsell after presenting it as a $29 one-time upsell.",
            "source": "Zero to Launch ([PX4xnrhsmpM @ 00:11:46])",
        },
    ],
    "sections": [
        {
            "id": "practitioner-consensus",
            "title": "The Practitioner Consensus",
            "paragraphs": [
                (
                    "The shared move is to stop treating the first purchase as the only purchase the customer can make. "
                    "Scott Moran of SamCart calls the additional spending expansion revenue: give customers add-ons, upgrades, and upsells instead of leaving them with one product at one price. "
                    "His baseball-training business began with a roughly $50 mini course, producing about $5,000 from 100 customers. "
                    "An inexpensive bonus-content bump brought another $750 when 30 customers accepted; a $100 course upsell brought another $2,000 when one in five accepted. "
                    "Moran says that changed what the business could spend on advertising while remaining profitable. "
                    "Marketing Mark demonstrates the same purchase structure at a smaller ticket: a $27 main offer, a $17 checkout bump, and a $97 one-on-one-call offer after payment. "
                    "The upsell appears whether or not the customer bought the bump. "
                    "Knola links a $197 YouTube course to a related scripts product and a PDF extra rather than leaving the original course as the maximum available purchase. "
                    "These operators all put additional products into the buying sequence; they do not describe the bump as a replacement for selling the initial offer. "
                    "The main sale opens the sequence, and the related extras give the buyer something else to accept. "
                    "[SamCart — UxhtBuVj4gY @ 00:01:27] "
                    "[Marketing Mark — qUqLPLYblBI @ 00:04:52] "
                    "[Knola — IOF1VzMEcKI @ 00:06:10]"
                ),
                (
                    "Relevance is the repeated offer-selection rule. Funnel Building Secrets describes a ClickFunnels bump as a low-cost add-on that complements the main offer, presented through a catchy headline and short description. "
                    "Sultan at WPFunnels makes that relationship concrete with a microphone and pop filter: the buyer is already purchasing the microphone, and the filter is something used with it. "
                    "He explicitly rejects dropping a random offer into checkout and favors a modest additional expense rather than another $100 or $150 purchase in that example. "
                    "Knola makes the same argument with digital products. A course about creating a YouTube channel fits a PDF containing ten YouTube script ideas for small businesses; a puppy-toilet-training product does not fit that purchase. "
                    "SamCart gives the broader formulation: the best bumps and upsells help customers reach their existing destination faster and with less work. "
                    "Its examples include a downloadable sleep tracker, a bonus module, personalized coaching, and community access around a newborn sleep-training course. "
                    "The agreement is about helping with the purchase already underway, not about forcing every platform into one price ladder. "
                    "Short checkout copy sells the simple extra; a dedicated upsell page gives the larger offer room for a headline, explanation, images, or video. "
                    "[Funnel Building Secrets — BZ4rml1tc1U @ 00:00:32] "
                    "[WPFunnels - Drag And Drop Sales Funnel Builder — 7SOm-x6R5nE @ 00:05:25] "
                    "[Knola — IOF1VzMEcKI @ 00:10:29] "
                    "[SamCart — UxhtBuVj4gY @ 00:19:31]"
                ),
                (
                    "The baseline build begins with products and a working purchase path. Marketing Mark requires multiple products and corresponding offers before adding the GoHighLevel bump. "
                    "The checkout needs an order-form element, the main product, and a separately configured bump product. "
                    "Zero to Launch starts the watercolor funnel with three existing courses and a connected payment gateway; without that gateway, none of the offers can be paid for. "
                    "The main course receives its resource, full-access setting, and price plan before the checkout bump or post-purchase steps are added. "
                    "GROUNDTECHY distinguishes the two purchase surfaces clearly: the bump sits on the order form and is added with a checkbox, while the upsell comes after the customer has supplied payment information. "
                    "That upsell page has acceptance and refusal buttons rather than another payment form. "
                    "Delivery is another explicit part of the setup, not merely a thank-you headline. "
                    "Prompt On Fire attaches a strategy-call tag to a $49 offer, then warns that the tag identifies the buyer but does not book the call. "
                    "The booking link still needs an automation email. Across these builds, the operator connects the offer, the payment action, and the resource or follow-up the purchaser should receive. "
                    "A visible button and a named product are only part of that connection. "
                    "[Marketing Mark — qUqLPLYblBI @ 00:00:01] "
                    "[Zero to Launch — PX4xnrhsmpM @ 00:00:34] "
                    "[GROUNDTECHY — F73hzfI-XsE @ 00:01:19] "
                    "[Prompt On Fire — 2V0NDEQHG0I @ 00:03:18]"
                ),
            ],
            "table": {
                "caption": "The shared purchase structure, with each operator's concrete implementation.",
                "headers": ["Purchase Component", "Practitioner Implementation", "Expert Source"],
                "rows": [
                    [
                        "Create the additional products before configuring checkout offers.",
                        "Marketing Mark requires products and corresponding offers before building the GoHighLevel bump.",
                        "Marketing Mark ([qUqLPLYblBI @ 00:00:01])",
                    ],
                    [
                        "Make the checkout extra complement the original purchase.",
                        "ClickFunnels bump copy uses a catchy headline, short description, and low-cost complementary offer.",
                        "Funnel Building Secrets ([BZ4rml1tc1U @ 00:00:32])",
                    ],
                    [
                        "Put the one-click offer after payment details are captured.",
                        "GROUNDTECHY uses acceptance and refusal buttons without another payment form on the upsell page.",
                        "GROUNDTECHY ([F73hzfI-XsE @ 00:02:08])",
                    ],
                    [
                        "Attach a payment gateway before expecting offers to sell.",
                        "The watercolor funnel begins with existing courses and Stripe connected under payment gateways.",
                        "Zero to Launch ([PX4xnrhsmpM @ 00:00:34])",
                    ],
                    [
                        "Choose extras that help with the buyer's existing objective.",
                        "SamCart describes faster results and less work as the common thread connecting its strongest offers.",
                        "SamCart ([UxhtBuVj4gY @ 00:19:31])",
                    ],
                    [
                        "Connect the purchase identifier to the promised next action.",
                        "A strategy-call tag identifies acceptance; an automation rule must email the booking link.",
                        "Prompt On Fire ([2V0NDEQHG0I @ 00:03:18])",
                    ],
                ],
            },
        },
        {
            "id": "street-mechanics-tools-numbers",
            "title": "Exact Street Mechanics, Tools & Numbers",
            "paragraphs": [
                (
                    "Marketing Mark's GoHighLevel sequence starts in the checkout step's Products tab. Add the main offer, choose its price, and save; add the second product and change Additional Options from main product to bump product. "
                    "In the page editor, select the order form, enable the order bump, select the linked product, and enter the title, subheadline, sales copy, and optional image. "
                    "His live checkout moves from $27 to $44 when the $17 bump is selected. "
                    "For the post-payment offer, his separate one-click tutorial places a new upsell step immediately after checkout, sets checkout to send traffic to the next step, and adds the upsell product to that page. "
                    "The button's Link To action becomes the one-click upsell or downsell product action, with the correct product selected. "
                    "GHLGrowthGarage follows the same product-to-page-to-button pattern and shows payment integrations under the Payments menu. "
                    "Funnel Building Secrets gives the ClickFunnels counterpart: enable the order-form bump, save its copy and price, create a one-click upsell step, choose a template, and link the product through product settings. "
                    "Its final instruction is to place a test order so both offers can be checked in the purchase flow, rather than stopping after editing the pages. "
                    "[Marketing Mark — qUqLPLYblBI @ 00:01:25] "
                    "[Marketing Mark — 0u4Tmd6BlWA @ 00:00:29] "
                    "[GHLGrowthGarage — caMKGGphSZA @ 00:01:02] "
                    "[Funnel Building Secrets — BZ4rml1tc1U @ 00:01:30]"
                ),
                (
                    "Zero to Launch builds the Systeme.io watercolor sequence with a $9 beginners course, a $5 flowers bump, a $29 landscapes upsell, and the same landscapes course offered as three monthly $10 payments after refusal. "
                    "Each offer gets a product, course resource, access mode, and price plan. "
                    "The bump also needs its order-bump element dragged onto the payment page; configuring the product alone does not display it. "
                    "The finished order is order form, upsell, downsell, and thank-you page. "
                    "The upsell's acceptance button buys landscapes, while its decline button sends the buyer to the payment-plan alternative. "
                    "LAUNCHTIP's Shopify route uses SellUp Add Ons and Cart Upsell: install the app, enable its theme embed, enable post-purchase upsells, and choose the product or collection that triggers the offer. "
                    "The example then edits the title, description, and link text before saving. "
                    "WP Simple Hacks builds the WooCommerce equivalent with FunnelKit Pro, creating checkout, a bump, upsell offers, and a thank-you page. "
                    "Its denim-jacket offer receives a 20% discount and a setting to skip the offer when that product already exists in the parent order. "
                    "The later T-shirt offer gets a separate dynamic path: acceptance ends at thank-you; refusal opens the discounted downsell. "
                    "[Zero to Launch — PX4xnrhsmpM @ 00:05:39] "
                    "[Zero to Launch — PX4xnrhsmpM @ 00:11:46] "
                    "[LAUNCHTIP — k8mwfZ9Nq_c @ 00:00:25] "
                    "[WP Simple Hacks - Wordpress tips and tricks — XHgk_luxaUU @ 00:07:02]"
                ),
                (
                    "Maik Kleinert connects the offer stack to Instagram comments rather than sending a link and stopping. "
                    "The automation checks whether the person already received the message or owns the product, applies interest tags, responds to the comment, and asks whether they want the guide before sending the product link. "
                    "After the second message, a 16-hour wait precedes another ownership check and a free-product route for people who have not already received it. "
                    "That route collects an email address and starts a separate email workflow. "
                    "At checkout, the $7 product can become a $57 order through a $20 mini-course offer and a $30 additional workbook offer. "
                    "Marketing Mark handles GoHighLevel access with separate workflows: sale for the main checkout purchase, Bump for the bump purchase, and upsell for the one-time offer, followed by the relevant tags and offer grants. "
                    "Social Nest Marketing delivers downloadable upsells through a workflow email using a Google Drive link stored as a custom value. "
                    "The operator adds the tag, inserts the custom value through the email editor's selector, saves, and publishes the workflow. "
                    "The DM tags, purchase triggers, and delivery links are all visible working parts of these operators' sequences, alongside the prices and sales pages. "
                    "[Maik Kleinert | Content-to-Conversion Systems — pE2Z7vTYfSw @ 00:05:33] "
                    "[Maik Kleinert | Content-to-Conversion Systems — pE2Z7vTYfSw @ 00:07:28] "
                    "[Marketing Mark — qUqLPLYblBI @ 00:03:31] "
                    "[Social Nest Marketing — -xCVVPZu48k @ 00:20:05]"
                ),
            ],
            "table": {
                "caption": "Exact controls and offer settings demonstrated across the implementation routes.",
                "headers": ["Build Operation", "Exact Setting or Sequence", "Expert Source"],
                "rows": [
                    [
                        "Configure the GoHighLevel bump as a separate checkout product.",
                        "Under Additional Options select bump product, save, then enable the bump on the order-form element.",
                        "Marketing Mark ([qUqLPLYblBI @ 00:01:25])",
                    ],
                    [
                        "Attach the GoHighLevel upsell product to its purchase button.",
                        "Select the one-click upsell product button action and choose the product already attached to the page.",
                        "GHLGrowthGarage ([caMKGGphSZA @ 00:01:23])",
                    ],
                    [
                        "Show the Systeme.io bump after saving its product configuration.",
                        "Drag the order-bump payment element onto the page and write the checkbox line and offer description.",
                        "Zero to Launch ([PX4xnrhsmpM @ 00:06:02])",
                    ],
                    [
                        "Choose which Shopify purchases should trigger the post-purchase offer.",
                        "Enable SellUp post-purchase upsells and select either a specific product or a collection.",
                        "LAUNCHTIP ([k8mwfZ9Nq_c @ 00:01:07])",
                    ],
                    [
                        "Configure an affordable WPFunnels accessory with an explicit discount.",
                        "The pop filter moves from $39.99 to $35.99 when Sultan applies the demonstrated 10% discount.",
                        "WPFunnels - Drag And Drop Sales Funnel Builder ([7SOm-x6R5nE @ 00:03:54])",
                    ],
                    [
                        "Build reusable SamCart bump groups before attaching the funnel.",
                        "Create the products, open Offers and Order Bumps, then group offers for reuse across products.",
                        "SamCart ([UxhtBuVj4gY @ 00:08:03])",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Small implementation details the builders actually use",
                "body": "These are specific editor, workflow, and purchase-button moves demonstrated by the operators.",
                "items": [
                    "Marketing Mark inserts a space before the first letter of the GoHighLevel bump sales-copy field because otherwise the displayed text runs into the preceding text. [Marketing Mark — qUqLPLYblBI @ 00:02:20]",
                    "Marketing Mark puts wording near the upsell button explaining that the buyer will be charged upon clicking, and adds a separate refusal button. [Marketing Mark — 0u4Tmd6BlWA @ 00:02:08]",
                    "Maik Kleinert checks whether the DM was already sent and whether the person already bought the product before continuing the promotional sequence. [Maik Kleinert | Content-to-Conversion Systems — pE2Z7vTYfSw @ 00:05:33]",
                    "WP Simple Hacks activates the FunnelKit option to skip an upsell when its product already exists in the parent order; the separate prior-purchase skip option remains off in the example. [WP Simple Hacks - Wordpress tips and tricks — XHgk_luxaUU @ 00:07:02]",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Create the products and connect payment",
                    "action": "Prepare the main offer and each additional offer before linking the pages.",
                    "detail": "SamCart creates a product for every front-end offer, bump, and upsell. Zero to Launch begins with existing courses and a connected Stripe gateway before building the watercolor sequence. [SamCart — UxhtBuVj4gY @ 00:06:15] [Zero to Launch — PX4xnrhsmpM @ 00:00:34]",
                },
                {
                    "step": 2,
                    "title": "Add and display the checkout bump",
                    "action": "Set the bump product and price, then configure its visible checkout element.",
                    "detail": "Marketing Mark selects bump product under Additional Options and enables the order bump inside the order-form editor. Zero to Launch separately drags the order-bump element onto the Systeme.io payment page. [Marketing Mark — qUqLPLYblBI @ 00:01:25] [Zero to Launch — PX4xnrhsmpM @ 00:06:02]",
                },
                {
                    "step": 3,
                    "title": "Connect acceptance and refusal paths",
                    "action": "Place the upsell after checkout and give the buyer both purchase and refusal actions.",
                    "detail": "Marketing Mark links the GoHighLevel button to its one-click product. GROUNDTECHY shows upsell acceptance bypassing the downsell, while refusal opens it; either downsell decision then reaches thank-you. [Marketing Mark — 0u4Tmd6BlWA @ 00:01:49] [GROUNDTECHY — F73hzfI-XsE @ 00:03:15]",
                },
                {
                    "step": 4,
                    "title": "Connect delivery and exercise the purchase flow",
                    "action": "Attach the correct access workflow and place a test order.",
                    "detail": "Marketing Mark separates sale and Bump submission triggers for the relevant offer grants. Funnel Building Secrets finishes by placing a test order to confirm that the checkout bump and upsell work together. [Marketing Mark — qUqLPLYblBI @ 00:03:31] [Funnel Building Secrets — BZ4rml1tc1U @ 00:01:49]",
                },
            ],
        },
        {
            "id": "disagreements-alternative-playbooks",
            "title": "Where Practitioners Disagree & Alternative Playbooks",
            "paragraphs": [
                (
                    "Default selection is a direct split. Marketing Mark shows that GoHighLevel can enable the bump by default but says that is not the practice he follows. "
                    "Maik Kleinert does the opposite: one bump is already selected, so the $7 buyer also gets the course unless they untick it. "
                    "His checkout presents original and discounted prices, with the complete three-product selection reaching $57. "
                    "Knola's PDF extra is off by default, and the buyer checks it to move the displayed checkout from $197 to $224. "
                    "The speakers also differ over which extra to build first. Zero to Launch's answer is the order bump: it uses an existing checkout rather than requiring another page, and every buyer sees it before paying. "
                    "An upsell needs its own product, page, headline, acceptance button, refusal action, and supporting explanation. "
                    "Knola demonstrates the opposite build order by adding the related scripts upsell before returning to checkout to add the PDF. "
                    "These are distinct operating approaches, not a single agreed configuration. "
                    "Mark's unselected bump, Kleinert's preselected course, and Knola's off-by-default extra all appear in working offer designs, while Zero to Launch emphasizes the smaller construction job as the reason to start with the bump. "
                    "[Marketing Mark — qUqLPLYblBI @ 00:02:37] "
                    "[Maik Kleinert | Content-to-Conversion Systems — pE2Z7vTYfSw @ 00:03:10] "
                    "[Knola — IOF1VzMEcKI @ 00:06:28] "
                    "[Zero to Launch — u9nHXAMBUe4 @ 00:02:05]"
                ),
                (
                    "Downsell does not mean the same offer structure in every build. CRM Tutorials Library presents a lower-priced or simplified fallback, using basic webpage design after the fuller webpage-design upsell. "
                    "The channel also warns that overusing downsells can train customers to wait for cheaper offers. "
                    "Zero to Launch keeps the watercolor landscapes course intact and changes how it is paid for: the $29 one-time upsell becomes three monthly payments of $10 after refusal, with full course access attached to both products. "
                    "WP Simple Hacks keeps the same T-shirt but changes the discount. The first offer takes 10% off; declining it opens a duplicated offer with 20% off and a last-chance headline. "
                    "The dynamic offer path sends an accepted first offer directly to thank-you instead. "
                    "Knola discusses another alternative without building it in that demonstration: a $1 trial for the scripts course, followed by the remaining $46 in seven days. "
                    "The speaker then chooses to add an order bump rather than implement that downsell. "
                    "The practical contrast is therefore explicit in the offers themselves: reduced features, smaller scheduled payments, a deeper discount, or a trial followed by the balance. "
                    "Each practitioner names the actual change instead of treating the downsell label as a complete offer. "
                    "[CRM Tutorials Library — pz33EMSEtfY @ 00:02:09] "
                    "[Zero to Launch — PX4xnrhsmpM @ 00:10:37] "
                    "[WP Simple Hacks - Wordpress tips and tricks — XHgk_luxaUU @ 00:15:11] "
                    "[Knola — IOF1VzMEcKI @ 00:08:51]"
                ),
                (
                    "An extra product, a replacement product, and a prorated upgrade are separate playbooks. Sultan initially uses WPFunnels bumps to add accessories, then changes the example to a better microphone. "
                    "Because he does not want both microphones purchased together, he enables Replace Product and replaces the whole cart, which contains one product. "
                    "SamCart's upgrade mechanism instead applies previous spending toward the upgraded offer's total; Moran demonstrates a post-checkout upgrade showing an additional $400. "
                    "His smart funnels can branch on acceptance or refusal, but his built example stays with two upsells and no downsells. "
                    "GROUNDTECHY demonstrates more extensive sequencing in Systeme.io: another upsell can follow the first upsell or come after its downsell, changing which offers customers encounter after each decision. "
                    "The platform demonstration permits as many upsells as the operator wants. "
                    "Moran's operating advice is narrower: start with one bump and one upsell, then add complexity; he says fourth and fifth steps have not helped much in the funnels he has seen. "
                    "The availability of another step and the speaker's experience of its usefulness are different claims. "
                    "The builders show how to extend the sequence, while Moran argues for keeping the initial sequence short and using offer analytics to compare what earns more. "
                    "[WPFunnels - Drag And Drop Sales Funnel Builder — 7SOm-x6R5nE @ 00:08:01] "
                    "[SamCart — UxhtBuVj4gY @ 00:18:21] "
                    "[GROUNDTECHY — F73hzfI-XsE @ 00:03:32] "
                    "[SamCart — UxhtBuVj4gY @ 00:23:58]"
                ),
            ],
            "table": {
                "caption": "Contrasting choices, attributed to the operators who actually present them.",
                "headers": ["Decision", "Contrasting Practitioner Approaches", "Expert Source"],
                "rows": [
                    [
                        "Choose whether the bump begins selected or unselected.",
                        "Marketing Mark avoids default selection; Maik Kleinert demonstrates an already-selected course that buyers can untick.",
                        "Marketing Mark ([qUqLPLYblBI @ 00:02:37]); Maik Kleinert | Content-to-Conversion Systems ([pE2Z7vTYfSw @ 00:03:10])",
                    ],
                    [
                        "Decide which additional offer to construct before the other.",
                        "Zero to Launch recommends the smaller bump build first; Knola builds the scripts upsell before adding the PDF.",
                        "Zero to Launch ([u9nHXAMBUe4 @ 00:00:00]); Knola ([IOF1VzMEcKI @ 00:06:28])",
                    ],
                    [
                        "Change the product scope or change the payment schedule.",
                        "CRM Tutorials Library offers basic webpage design; Zero to Launch retains the landscapes course with three payments.",
                        "CRM Tutorials Library ([pz33EMSEtfY @ 00:02:28]); Zero to Launch ([PX4xnrhsmpM @ 00:10:37])",
                    ],
                    [
                        "Use a deeper discount or a trial-based alternative.",
                        "WP Simple Hacks builds a 20% T-shirt downsell; Knola proposes, but does not build, a $1 trial.",
                        "WP Simple Hacks - Wordpress tips and tricks ([XHgk_luxaUU @ 00:15:11]); Knola ([IOF1VzMEcKI @ 00:08:51])",
                    ],
                    [
                        "Replace the checkout product or credit previous spending.",
                        "WPFunnels replaces the microphone through its bump setting; SamCart prorates the post-purchase upgrade using prior spending.",
                        "WPFunnels - Drag And Drop Sales Funnel Builder ([7SOm-x6R5nE @ 00:08:18]); SamCart ([UxhtBuVj4gY @ 00:15:30])",
                    ],
                    [
                        "Extend the sequence or keep the initial funnel short.",
                        "GROUNDTECHY demonstrates additional upsell placement; Moran says later fourth and fifth steps have not helped much.",
                        "GROUNDTECHY ([F73hzfI-XsE @ 00:03:32]); SamCart ([UxhtBuVj4gY @ 00:24:44])",
                    ],
                ],
            },
        },
        {
            "id": "failure-modes-economics-checks",
            "title": "Firsthand Failure Modes, Traps & Economics Checks",
            "paragraphs": [
                (
                    "Social Nest Marketing's build runs into delivery problems before the purchase flow is finished. "
                    "The upsell files arrive as folders, which the operator says cannot be sent that way, so each upsell becomes a ZIP file. "
                    "An upload then fails at the reported 100-megabyte limit; the operator uploads both files to Google Drive and uses those links in the workflows instead. "
                    "The purchase button also fails to behave as expected. With no cart attached in that setup, the operator creates a payment link and sends its completed checkout to the next upsell. "
                    "The test then exposes conflicting page prices, with $27 in one place and $97 farther down. "
                    "The operator explicitly wonders whether the setup is being done incorrectly. "
                    "That experience differs from Marketing Mark's direct GoHighLevel demonstration, where the linked upsell button charges the stored payment method without another card-entry step. "
                    "Funnel Building Secrets ends its ClickFunnels build by placing a test order to check the bump and upsell together. "
                    "Social Nest's walkthrough shows concrete reasons for doing that: the clickable page, the payment destination, the displayed price, and the downloadable product each needed attention during the build, and the delivery workflow was not yet configured when the first payment-link test ran. "
                    "[Social Nest Marketing — -xCVVPZu48k @ 00:03:02] "
                    "[Social Nest Marketing — -xCVVPZu48k @ 00:09:33] "
                    "[Marketing Mark — 0u4Tmd6BlWA @ 00:00:49] "
                    "[Funnel Building Secrets — BZ4rml1tc1U @ 00:01:49]"
                ),
                (
                    "Page placement and unfinished templates produce another set of visible traps. Prompt On Fire adds a strategy-call upsell and finds that the new step lands after the thank-you page. "
                    "The operator drags it between the order form and thank-you, explaining that customers encounter the steps in that order. "
                    "The chosen template already contains accept and decline buttons, but its lower section still has filler text that needs replacing before sharing the page. "
                    "Zero to Launch encounters the same placement issue in the watercolor build and manually moves both upsell and downsell into their intended positions. "
                    "The operator also removes unrelated sample copy and thank-you-page menu items, buttons, and footer elements that go nowhere useful. "
                    "The buyer walkthrough stops before payment; the later upsell previews show the pages, but their buttons do not execute purchases in preview. "
                    "GROUNDTECHY explains why a direct upsell address is not an ordinary landing-page test: without the prior checkout, visiting that link redirects to the order form. "
                    "The customer must first supply payment information. "
                    "These practitioners distinguish editing a page, previewing its appearance, and reaching it as a purchaser. "
                    "Their demonstrations also separate a tag that records a strategy-call purchase from the automation email that actually supplies the booking link. "
                    "[Prompt On Fire — 2V0NDEQHG0I @ 00:01:15] "
                    "[Zero to Launch — PX4xnrhsmpM @ 00:07:21] "
                    "[Zero to Launch — PX4xnrhsmpM @ 00:15:24] "
                    "[GROUNDTECHY — F73hzfI-XsE @ 00:01:52]"
                ),
                (
                    "The economics claims and headline totals are not uniform even within individual demonstrations. SamCart opens by saying sellers using the features make seven times more, then later describes the database average as six times more. "
                    "Moran separately recounts the baseball business moving from about $5,000 to almost $8,000 for the same customer count, and gives offer-specific acceptance targets rather than one universal upsell rate. "
                    "He calls 30 to 40% good for bumps, says 5% can be good for a very expensive upsell, and suggests around 20% for an upsell priced at two to three times the initial product. "
                    "Knola repeatedly presents the scripts upgrade as $47, but one description of accepting it says an extra $37 before the following explanation returns to $47. "
                    "Maik Kleinert calls the $7 sale almost zero profit on its own and reports a $57 bundle order, while also describing the combined discount as mostly 25%. "
                    "His automation commentary first calls the messaging window 24 hours and later calls it 20 hours; the demonstrated follow-up wait is 16 hours. "
                    "The reported order amounts, suggested acceptance targets, and shifting spoken figures therefore remain attached to the named operator and the particular example rather than becoming one blended forecast for every funnel. "
                    "[SamCart — UxhtBuVj4gY @ 00:00:12] "
                    "[SamCart — UxhtBuVj4gY @ 00:25:13] "
                    "[Knola — IOF1VzMEcKI @ 00:07:49] "
                    "[Maik Kleinert | Content-to-Conversion Systems — pE2Z7vTYfSw @ 00:08:00]"
                ),
            ],
            "table": {
                "caption": "Observed build problems, operator warnings, and the specific responses shown.",
                "headers": ["Observed Problem or Warning", "Practitioner Response or Limitation", "Expert Source"],
                "rows": [
                    [
                        "The downloadable upsell upload fails because the file is too large.",
                        "Social Nest Marketing reports a 100-megabyte limit and moves both upsell files to Google Drive.",
                        "Social Nest Marketing ([-xCVVPZu48k @ 00:03:02])",
                    ],
                    [
                        "The next upsell page displays two conflicting offer prices.",
                        "After the payment-link test, the operator spots $27 near the top and $97 farther down.",
                        "Social Nest Marketing ([-xCVVPZu48k @ 00:14:49])",
                    ],
                    [
                        "The new upsell appears after the funnel's thank-you page.",
                        "Prompt On Fire drags the step between order form and thank-you before configuring the offer.",
                        "Prompt On Fire ([2V0NDEQHG0I @ 00:01:15])",
                    ],
                    [
                        "The product exists but the checkout bump remains invisible.",
                        "Zero to Launch adds the order-bump element to the page after saving the offer configuration.",
                        "Zero to Launch ([PX4xnrhsmpM @ 00:06:02])",
                    ],
                    [
                        "The preview shows the offer without executing purchase-button actions.",
                        "Zero to Launch stops before payment and explicitly says the buttons do nothing in preview.",
                        "Zero to Launch ([PX4xnrhsmpM @ 00:16:03])",
                    ],
                    [
                        "Repeated cheaper fallback offers can shape future buying behavior.",
                        "CRM Tutorials Library warns that overusing downsells can train customers to wait for cheaper offers.",
                        "CRM Tutorials Library ([pz33EMSEtfY @ 00:02:09])",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Checks the practitioners put in front of a finished sequence",
                "body": "Use the actual build failures and purchase-path checks shown by the operators.",
                "items": [
                    "Check the physical step order after creating a Systeme.io upsell: Prompt On Fire finds it below thank-you and moves it directly after the order form. [Prompt On Fire — 2V0NDEQHG0I @ 00:01:15]",
                    "Check the price copy throughout the next offer page: Social Nest Marketing's test reveals $27 in one place and $97 in another. [Social Nest Marketing — -xCVVPZu48k @ 00:14:49]",
                    "Check that the strategy-call tag triggers an email with the booking link; the tag alone does not book the call. [Prompt On Fire — 2V0NDEQHG0I @ 00:03:18]",
                    "Place the test order through checkout and the additional offers, as Funnel Building Secrets instructs; Zero to Launch explicitly says Systeme.io preview buttons do not perform the purchase actions. [Funnel Building Secrets — BZ4rml1tc1U @ 00:01:49] [Zero to Launch — PX4xnrhsmpM @ 00:16:03]",
                ],
            },
        },
    ],
    "pull_quote": (
        "\"The best bumps and upsells are always going to help someone get where they're trying to go faster and with less work.\" "
        "— Scott Moran, SamCart (UxhtBuVj4gY @ 00:19:31)."
    ),
    "diagram_id": "diag-02",
    "action_checklist": [
        "Create the products for the main offer, each bump, and each upsell before assembling the offer sequence. [SamCart — UxhtBuVj4gY @ 00:06:15]",
        "Connect the payment gateway and attach each Systeme.io course resource with its intended access mode and price plan. [Zero to Launch — PX4xnrhsmpM @ 00:00:34] [Zero to Launch — PX4xnrhsmpM @ 00:03:13]",
        "Add the bump to checkout and inspect the selected and unselected totals, as Marketing Mark does with the $27 offer and $17 extra. [Marketing Mark — qUqLPLYblBI @ 00:03:11]",
        "Place the upsell after checkout, link its product to the purchase button, and add a refusal route to the downsell or confirmation page. [Marketing Mark — 0u4Tmd6BlWA @ 00:01:49]",
        "Connect separate sale and bump workflows to the correct access grants; for a strategy call, email the booking link when the purchase tag is added. [Marketing Mark — qUqLPLYblBI @ 00:03:31] [Prompt On Fire — 2V0NDEQHG0I @ 00:03:18]",
        "Place a test order through the sequence, then use offer analytics to compare how the bumps and upsells contribute to order value. [Funnel Building Secrets — BZ4rml1tc1U @ 00:01:49] [SamCart — UxhtBuVj4gY @ 00:25:43]",
    ],
    "statutory_citations": [
        {
            "title": "Marketing Mark — How to Add Order Bumps in GoHighLevel (Plus Easy One-Click Upsells) [00:03:31]",
            "url": "https://www.youtube.com/watch?v=qUqLPLYblBI&t=211s",
            "relevance": "Primary practitioner testimony on separate sale and bump workflows, tags, and product-access grants.",
        },
        {
            "title": "Zero to Launch — How to Build a Systeme.io Funnel with Order Bump, Upsell & Downsell [00:11:46]",
            "url": "https://www.youtube.com/watch?v=PX4xnrhsmpM&t=706s",
            "relevance": "Primary practitioner testimony on the three-payment downsell and its exact billing schedule.",
        },
        {
            "title": "SamCart — The Complete Guide to Upsells ($8 Billion in Data) [00:25:13]",
            "url": "https://www.youtube.com/watch?v=UxhtBuVj4gY&t=1513s",
            "relevance": "Primary practitioner testimony on bump acceptance benchmarks and price-dependent upsell expectations.",
        },
        {
            "title": "Social Nest Marketing — GoHighLevel One-Click Upsell Setup: Payment Link Redirect + Auto-Delivery Workflow (Part 6) [00:03:02]",
            "url": "https://www.youtube.com/watch?v=-xCVVPZu48k&t=182s",
            "relevance": "Primary practitioner testimony on a failed large-file upload and the Google Drive delivery alternative.",
        },
    ],
    "source_citations": [
        {
            "source_type": "video_pro_tip",
            "video_id": "qUqLPLYblBI",
            "title": "How to Add Order Bumps in GoHighLevel (Plus Easy One-Click Upsells)",
            "channel": "Marketing Mark",
            "author": "Marketing Mark",
            "text": "If I toggle on my $17 order bump, now we can see I'm being charged for both products for a total of 44.",
            "tip": "If I toggle on my $17 order bump, now we can see I'm being charged for both products for a total of 44.",
            "timestamp": 191,
            "timestamp_seconds": 191,
            "timestamp_label": "[00:03:11]",
            "url": "https://www.youtube.com/watch?v=qUqLPLYblBI&t=191s",
            "markdown": "[00:03:11](https://www.youtube.com/watch?v=qUqLPLYblBI&t=191s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "pE2Z7vTYfSw",
            "title": "I Upsold A $7 Product To $57  With DM Automation + Order Bump Setup ( Full System Explained )",
            "channel": "Maik Kleinert | Content-to-Conversion Systems",
            "author": "Maik Kleinert | Content-to-Conversion Systems",
            "text": "Instead of $7, they pay $57.",
            "tip": "Instead of $7, they pay $57.",
            "timestamp": 207,
            "timestamp_seconds": 207,
            "timestamp_label": "[00:03:27]",
            "url": "https://www.youtube.com/watch?v=pE2Z7vTYfSw&t=207s",
            "markdown": "[00:03:27](https://www.youtube.com/watch?v=pE2Z7vTYfSw&t=207s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "BZ4rml1tc1U",
            "title": "How to Set Up an Order Bump and Upsell",
            "channel": "Funnel Building Secrets",
            "author": "Funnel Building Secrets",
            "text": "Place a test order to confirm that both are working correctly.",
            "tip": "Place a test order to confirm that both are working correctly.",
            "timestamp": 109,
            "timestamp_seconds": 109,
            "timestamp_label": "[00:01:49]",
            "url": "https://www.youtube.com/watch?v=BZ4rml1tc1U&t=109s",
            "markdown": "[00:01:49](https://www.youtube.com/watch?v=BZ4rml1tc1U&t=109s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "0u4Tmd6BlWA",
            "title": "How to Build 1 Click Upsells in GoHighLevel",
            "channel": "Marketing Mark",
            "author": "Marketing Mark",
            "text": "This upsell page should go right after your checkout page.",
            "tip": "This upsell page should go right after your checkout page.",
            "timestamp": 29,
            "timestamp_seconds": 29,
            "timestamp_label": "[00:00:29]",
            "url": "https://www.youtube.com/watch?v=0u4Tmd6BlWA&t=29s",
            "markdown": "[00:00:29](https://www.youtube.com/watch?v=0u4Tmd6BlWA&t=29s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "F73hzfI-XsE",
            "title": "How to Setup Sell funnel Upsells, downsells, order bumps on Systemeio",
            "channel": "GROUNDTECHY",
            "author": "GROUNDTECHY",
            "text": "They only need to check this checkbox and the second offer will be added to their order.",
            "tip": "They only need to check this checkbox and the second offer will be added to their order.",
            "timestamp": 79,
            "timestamp_seconds": 79,
            "timestamp_label": "[00:01:19]",
            "url": "https://www.youtube.com/watch?v=F73hzfI-XsE&t=79s",
            "markdown": "[00:01:19](https://www.youtube.com/watch?v=F73hzfI-XsE&t=79s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "-xCVVPZu48k",
            "title": "GoHighLevel One-Click Upsell Setup: Payment Link Redirect + Auto-Delivery Workflow (Part 6)",
            "channel": "Social Nest Marketing",
            "author": "Social Nest Marketing",
            "text": "For some reason you can't go over 100 megabytes.",
            "tip": "For some reason you can't go over 100 megabytes.",
            "timestamp": 182,
            "timestamp_seconds": 182,
            "timestamp_label": "[00:03:02]",
            "url": "https://www.youtube.com/watch?v=-xCVVPZu48k&t=182s",
            "markdown": "[00:03:02](https://www.youtube.com/watch?v=-xCVVPZu48k&t=182s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "k8mwfZ9Nq_c",
            "title": "How to Create a One-Click Upsell Funnel for your Shopify store in 2026",
            "channel": "LAUNCHTIP",
            "author": "LAUNCHTIP",
            "text": "For a true one-click funnel, post-purchase upsells usually work best.",
            "tip": "For a true one-click funnel, post-purchase upsells usually work best.",
            "timestamp": 67,
            "timestamp_seconds": 67,
            "timestamp_label": "[00:01:07]",
            "url": "https://www.youtube.com/watch?v=k8mwfZ9Nq_c&t=67s",
            "markdown": "[00:01:07](https://www.youtube.com/watch?v=k8mwfZ9Nq_c&t=67s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "u9nHXAMBUe4",
            "title": "Order Bump or Upsell in Systeme.io: Which Should You Add First?",
            "channel": "Zero to Launch",
            "author": "Zero to Launch",
            "text": "An order bump takes one price and only one.",
            "tip": "An order bump takes one price and only one.",
            "timestamp": 248,
            "timestamp_seconds": 248,
            "timestamp_label": "[00:04:08]",
            "url": "https://www.youtube.com/watch?v=u9nHXAMBUe4&t=248s",
            "markdown": "[00:04:08](https://www.youtube.com/watch?v=u9nHXAMBUe4&t=248s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "pz33EMSEtfY",
            "title": "How to Set Up Main Product, Order Bump, Upsell & Downsell in GoHighLevel | Step-by-Step",
            "channel": "CRM Tutorials Library",
            "author": "CRM Tutorials Library",
            "text": "Overusing it can train customers to wait for cheaper offers.",
            "tip": "Overusing it can train customers to wait for cheaper offers.",
            "timestamp": 129,
            "timestamp_seconds": 129,
            "timestamp_label": "[00:02:09]",
            "url": "https://www.youtube.com/watch?v=pz33EMSEtfY&t=129s",
            "markdown": "[00:02:09](https://www.youtube.com/watch?v=pz33EMSEtfY&t=129s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "UxhtBuVj4gY",
            "title": "The Complete Guide to Upsells ($8 Billion in Data)",
            "channel": "SamCart",
            "author": "SamCart",
            "text": "A good order bump is going to be something like 30 to 40% of people accept it and put it in their cart.",
            "tip": "A good order bump is going to be something like 30 to 40% of people accept it and put it in their cart.",
            "timestamp": 1513,
            "timestamp_seconds": 1513,
            "timestamp_label": "[00:25:13]",
            "url": "https://www.youtube.com/watch?v=UxhtBuVj4gY&t=1513s",
            "markdown": "[00:25:13](https://www.youtube.com/watch?v=UxhtBuVj4gY&t=1513s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "2V0NDEQHG0I",
            "title": "I Added a 1-Click Upsell to My Systeme.io Funnel. Here’s What Happened",
            "channel": "Prompt On Fire",
            "author": "Prompt On Fire",
            "text": "The tag tells you who said yes, but it doesn't book the call by itself.",
            "tip": "The tag tells you who said yes, but it doesn't book the call by itself.",
            "timestamp": 198,
            "timestamp_seconds": 198,
            "timestamp_label": "[00:03:18]",
            "url": "https://www.youtube.com/watch?v=2V0NDEQHG0I&t=198s",
            "markdown": "[00:03:18](https://www.youtube.com/watch?v=2V0NDEQHG0I&t=198s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "IOF1VzMEcKI",
            "title": "How to Sell an Online Course With a Sales Funnel (Upsell + Order Bump)",
            "channel": "Knola",
            "author": "Knola",
            "text": "Immediately that 197 is now 224 for the same checkout, the same customer.",
            "tip": "Immediately that 197 is now 224 for the same checkout, the same customer.",
            "timestamp": 612,
            "timestamp_seconds": 612,
            "timestamp_label": "[00:10:12]",
            "url": "https://www.youtube.com/watch?v=IOF1VzMEcKI&t=612s",
            "markdown": "[00:10:12](https://www.youtube.com/watch?v=IOF1VzMEcKI&t=612s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "caMKGGphSZA",
            "title": "How To Set Up a GoHighLevel Upsell (Boost Funnel Sales Fast)",
            "channel": "GHLGrowthGarage",
            "author": "GHLGrowthGarage",
            "text": "Choose the one-click upsell product option and make sure to select your upsell product.",
            "tip": "Choose the one-click upsell product option and make sure to select your upsell product.",
            "timestamp": 83,
            "timestamp_seconds": 83,
            "timestamp_label": "[00:01:23]",
            "url": "https://www.youtube.com/watch?v=caMKGGphSZA&t=83s",
            "markdown": "[00:01:23](https://www.youtube.com/watch?v=caMKGGphSZA&t=83s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "PX4xnrhsmpM",
            "title": "How to Build a Systeme.io Funnel with Order Bump, Upsell & Downsell",
            "channel": "Zero to Launch",
            "author": "Zero to Launch",
            "text": "The buyer pays $10 a month three times. Trial period stays at zero.",
            "tip": "The buyer pays $10 a month three times. Trial period stays at zero.",
            "timestamp": 706,
            "timestamp_seconds": 706,
            "timestamp_label": "[00:11:46]",
            "url": "https://www.youtube.com/watch?v=PX4xnrhsmpM&t=706s",
            "markdown": "[00:11:46](https://www.youtube.com/watch?v=PX4xnrhsmpM&t=706s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "7SOm-x6R5nE",
            "title": "How To Use Order Bumps In Your Funnels To Increase AOV (New WPFunnels Tutorial)",
            "channel": "WPFunnels - Drag And Drop Sales Funnel Builder",
            "author": "WPFunnels - Drag And Drop Sales Funnel Builder",
            "text": "If you enable this option it will ask you, do you want to replace all the products or any specific selected products from the cart.",
            "tip": "If you enable this option it will ask you, do you want to replace all the products or any specific selected products from the cart.",
            "timestamp": 498,
            "timestamp_seconds": 498,
            "timestamp_label": "[00:08:18]",
            "url": "https://www.youtube.com/watch?v=7SOm-x6R5nE&t=498s",
            "markdown": "[00:08:18](https://www.youtube.com/watch?v=7SOm-x6R5nE&t=498s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "XHgk_luxaUU",
            "title": "How to Build a High-Converting WooCommerce Sales Funnel with Upsells & Order Bumps",
            "channel": "WP Simple Hacks - Wordpress tips and tricks",
            "author": "WP Simple Hacks - Wordpress tips and tricks",
            "text": "If the offer has been accepted, it goes straight to the thank you page, but when rejected, then display the downsell offer.",
            "tip": "If the offer has been accepted, it goes straight to the thank you page, but when rejected, then display the downsell offer.",
            "timestamp": 975,
            "timestamp_seconds": 975,
            "timestamp_label": "[00:16:15]",
            "url": "https://www.youtube.com/watch?v=XHgk_luxaUU&t=975s",
            "markdown": "[00:16:15](https://www.youtube.com/watch?v=XHgk_luxaUU&t=975s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
    ],
}
