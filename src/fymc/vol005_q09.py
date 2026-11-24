from __future__ import annotations

CHAPTER_9 = {
    "id": "Q9",
    "chapter_id": "Q9",
    "chapter_number": 9,
    "question_number": 9,
    "slug": "track-referrals-sold-leads-and-conversion-events",
    "question_prompt": "How do I create tracking links, configure and test postbacks, and connect advertiser, lead-sale, CRM, and Meta conversion events?",
    "kicker": "Q9 / THE BIG MONEY PLAYBOOKS",
    "title": "Track Referrals, Sold Leads, and Conversion Events",
    "subtitle": "FirstPromoter and Everflow walkthroughs, S2S postbacks, tracking domains, ClickFlare and RedTrack, LeadByte sold-lead events, CRM quality signals, and Cloudflare with GTM and Meta CAPI.",
    "layout_template": "tool_resource_directory",
    "reading_time_minutes": 15,
    "executive_summary": (
        "Everflow's trainers and RedTrack's Paulina converge on the same mechanism: "
        "store the click identifier and return it when the conversion happens. "
        "Daniel connects FirstPromoter commissions to subscription billing, demonstrating "
        "20% monthly until cancellation. LeadByte reports buyer-accepted leads back "
        "with revenue, while Isaac's CRM playbook rejects disconnected numbers and "
        "duplicates before payouts. Donald connects Everflow, ClickFlare, Meta conversion "
        "signals, and advertising costs; Carlos shares Everflow's direct Facebook "
        "integration instead. The alternatives differ in setup burden, attribution "
        "method, and reporting scope. Pixel Setup GTM Expert demonstrates a Cloudflare "
        "purchase worth 1450 Taka, while AffiliateStrat emphasizes Everflow's training "
        "and granular reporting. The recurring operational checks are identifier "
        "round trips, exact macro formatting, event selection, and visible postback results."
    ),
    "key_metrics": [
        {
            "label": "Task Flow recurring commission",
            "metric": "Task Flow recurring commission",
            "value": "20% monthly until customer cancels",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Daniel configures this recurring reward for the Task Flow SaaS "
                "example, rather than presenting it as a market-wide commission rate."
            ),
            "source": "Daniel | Tech & Data ([SWQet1wMMyA @ 00:03:03])",
        },
        {
            "label": "Everflow-managed random tracking domain",
            "metric": "Everflow-managed random tracking domain",
            "value": "$40 per domain per month",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Isaac quotes this charge when Everflow purchases and manages a "
                "random domain for tracking links."
            ),
            "source": "Everflow - Partner Marketing Platform ([Ni95PXMEMzE @ 00:03:00])",
        },
        {
            "label": "CRM milestone payout example",
            "metric": "CRM milestone payout example",
            "value": "$50 for the lead; $200 when the retainer is signed",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Isaac proposes staged rewards, followed by a bonus when the case "
                "settles, as an example of paying through the customer life cycle."
            ),
            "source": "Everflow - Partner Marketing Platform ([kLc_7B0eexA @ 00:02:24])",
        },
        {
            "label": "Cloudflare dashboard purchase demonstration",
            "metric": "Cloudflare dashboard purchase demonstration",
            "value": "One total sale worth 1450 Taka",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Pixel Setup GTM Expert shows this purchase value and total sale "
                "after completing the demonstrated customer journey."
            ),
            "source": "Pixel Setup GTM Expert ([HBs0vkiWarc @ 00:06:11])",
        },
    ],
    "sections": [
        {
            "id": "practitioner-consensus",
            "title": "The Practitioner Consensus",
            "paragraphs": [
                (
                    "The common mechanism is a click identifier that survives until the business "
                    "event can be reported. Everflow's S2S trainer starts with a partner tracking "
                    "link: a click generates a transaction ID, the advertiser stores it in a "
                    "website or CRM, and the advertiser sends it back when the desired action "
                    "occurs. That returned identifier credits the original partner rather than "
                    "merely counting an isolated action [2Q-xY6ABqXE @ 00:00:36]. RedTrack's Paulina "
                    "describes the same backend connection between a merchant and an advertising "
                    "channel, using a generated unique identifier to connect the click and "
                    "conversion. Their emphasis is on transferring conversion information between "
                    "systems, including campaigns running across multiple advertising channels "
                    "[oZcc_4NfA3g @ 00:02:43]. Isaac makes the return journey more explicit: the "
                    "advertiser postback brings conversion information into Everflow, and the "
                    "partner postback sends that information onward to the partner's own system. "
                    "The partner supplies their receiving URL; Everflow supplies the advertiser's "
                    "receiving URL. Isaac's workflow captures the click, creates the transaction "
                    "ID, directs the visitor to the advertiser, and returns the conversion through "
                    "both systems. Partners then receive credit and can track the sale inside "
                    "their own reporting environment [NSernIgs5XQ @ 00:03:03]."
                ),
                (
                    "The speakers also connect attribution to the event that actually changes "
                    "the commercial relationship. Daniel's FirstPromoter walkthrough ties commissions "
                    "directly to subscription billing activity rather than repeatedly recalculating "
                    "them in spreadsheets. Their Task Flow setup combines referral links with "
                    "promo codes, installs the initialization script in the website header, and "
                    "adds lead tracking after signup so customer emails connect to the referral "
                    "source. The recurring reward then follows the subscription life cycle "
                    "[SWQet1wMMyA @ 00:01:59]. LeadByte demonstrates a different commercial event: "
                    "a form submission enters LeadByte, goes to a buyer, and is accepted or "
                    "rejected. Acceptance records revenue, and the sold-lead event returns to "
                    "Everflow with the revenue carried as the postback amount. The demonstration "
                    "therefore follows the lead beyond the initial form submission to the buyer's "
                    "decision [NYSR6kFlcI8 @ 00:00:17]. Isaac's CRM example follows the same "
                    "outcome-oriented direction. A precious-metals client had been paying for "
                    "leads that sales staff quickly marked disconnected or bad. Connecting the "
                    "CRM changed that feedback loop: disconnected numbers were rejected immediately "
                    "and duplicates were blocked before payout. Isaac describes the shift as "
                    "paying for outcomes instead of activity, with affiliates receiving feedback "
                    "that lets them correct the traffic they send [kLc_7B0eexA @ 00:00:03]."
                ),
                (
                    "The baseline setup is an identified offer, an identified partner, and a "
                    "link whose extra information can be inspected later. Everflow's link-generation "
                    "trainer selects an offer and partner first, then exposes creative-specific "
                    "links, direct linking when enabled, and traffic-source parameters. A partner's "
                    "assigned traffic source is automatically selected and cannot be changed in "
                    "that generator. Additional parameters accept macros or static values, including "
                    "the demonstrated test marker in sub five [_VC3Wol9b0c @ 00:00:24]. Isaac's "
                    "domain walkthrough separates two jobs that sit behind those links: tracking "
                    "domains carry partner clicks, while conversion domains appear in the "
                    "advertiser's conversion postback or pixel. The primary tracking domain is "
                    "the default for partner links, and the primary conversion domain supplies "
                    "the default for conversion and event postbacks. These are distinct settings "
                    "in the platform's domain management [Ni95PXMEMzE @ 00:01:48]. AffiliateStrat "
                    "then demonstrates what the operator sees after traffic arrives: detailed "
                    "click data, conversion information, and a transaction flowchart showing "
                    "conversion events and partner postbacks. Their reporting walkthrough opens "
                    "and closes sections to keep the data navigable, rather than treating the "
                    "dashboard as one undifferentiated total. The flowchart connects the reporting "
                    "view back to the transaction's actual sequence [Z_YllaXsWGA @ 00:12:33]."
                ),
            ],
            "table": {
                "caption": "The shared operating model, from the referring partner to the commercial event.",
                "headers": ["Operating component", "Practitioner mechanism", "Expert Source"],
                "rows": [
                    [
                        "A stored identifier connects the original click with the eventual conversion",
                        "Everflow generates the transaction ID and the advertiser returns it when the action occurs.",
                        "Everflow - Partner Marketing Platform ([2Q-xY6ABqXE @ 00:00:36])",
                    ],
                    [
                        "Backend communication connects merchant activity with advertising channel reporting",
                        "Paulina describes servers communicating through a generated unique identifier that connects clicks and conversions.",
                        "RedTrack.io ([oZcc_4NfA3g @ 00:02:43])",
                    ],
                    [
                        "Advertiser and partner postbacks carry information in different directions",
                        "The advertiser reports into Everflow, which uses the partner's postback to report onward.",
                        "Everflow - Partner Marketing Platform ([NSernIgs5XQ @ 00:03:03])",
                    ],
                    [
                        "Subscription commissions remain connected to the customer's actual billing activity",
                        "Daniel describes FirstPromoter recalculating commissions automatically when subscription events happen in the billing system.",
                        "Daniel | Tech & Data ([SWQet1wMMyA @ 00:01:40])",
                    ],
                    [
                        "The sold lead becomes the event sent back with revenue",
                        "LeadByte records buyer acceptance and sends the sold event with revenue as the Everflow amount.",
                        "LeadByte ([NYSR6kFlcI8 @ 00:00:39])",
                    ],
                    [
                        "Lead quality feedback changes which referrals reach the payout stage",
                        "Isaac's client rejects disconnected numbers immediately and blocks duplicate leads before a payout is triggered.",
                        "Everflow - Partner Marketing Platform ([kLc_7B0eexA @ 00:00:33])",
                    ],
                ],
            },
        },
        {
            "id": "exact-street-mechanics",
            "title": "Exact Street Mechanics, Tools & Numbers",
            "paragraphs": [
                (
                    "Build the link with the generator instead of guessing the offer-partner "
                    "combination. Everflow's trainer selects both, unfolds additional parameters, "
                    "and enters a macro or static value into supported fields such as Source "
                    "ID and sub one. Their test example uses sub five equal to everflow test. "
                    "The generator also offers parameter encryption and exports through clipboard, "
                    "QR code, or sharing with offer details [_VC3Wol9b0c @ 00:01:30]. Next, the "
                    "advertiser-postback trainer checks two connections: the tracking link must "
                    "pass the transaction ID macro into the advertiser's landing page or system, "
                    "and the advertiser must configure the receiving postback URL to return "
                    "that ID upon conversion. Their validation tool is the advertiser postback "
                    "report, which records attempted conversion signals, acceptance or rejection, "
                    "and rejection reasons. Testing also checks values such as sale amount and "
                    "the resulting conversion status [qXMBHCgI3Wk @ 00:00:36]. AffiliateStrat's "
                    "walkthrough shows the reporting side of this work in the detailed click "
                    "report and transaction flowchart. They change the reporting interval, inspect "
                    "offers and partners, and open the flowchart to see transactions, conversion "
                    "events, and partner postbacks together. That is the demonstrated route from "
                    "a generated link to an inspectable event sequence [Z_YllaXsWGA @ 00:12:33]."
                ),
                (
                    "Donald builds the Meta connection in ClickFlare with two integrations: "
                    "conversion API delivery and cost tracking. The conversion integration takes "
                    "the Meta dataset ID as the pixel ID plus an access token, then maps "
                    "ClickFlare events to Facebook events. The cost integration connects the "
                    "Facebook account and selected advertising account. Donald next creates a "
                    "Facebook traffic source, attaches both integrations, creates an Everflow "
                    "affiliate-network entry and offer, and appends the ClickFlare click ID "
                    "to the Everflow offer URL. Their campaign combines those elements, uses "
                    "the integration for costs, and selects the pixel integration at campaign "
                    "level [cSLdoNWYxfE @ 00:04:57]. For event-specific reporting, Donald creates "
                    "a custom conversion and places its parameter after ct in the returning "
                    "postback. They explicitly warn that the value is case-sensitive and must "
                    "contain no spaces [cSLdoNWYxfE @ 00:13:03]. Carlos shares an Everflow "
                    "demonstration that sends conversions directly through the Facebook delivery "
                    "method instead. That setup selects the saved integration, pixel ID, and "
                    "Facebook event. The presenter suggests transaction ID as the event identifier "
                    "to help Facebook ignore duplicate conversions, then selects the action "
                    "source and supplies event-source information. Purchase value and currency "
                    "can be passed when that information reached Everflow from the advertiser "
                    "[zOQZw8jApe0 @ 00:20:22]."
                ),
                (
                    "LeadByte's implementation puts the Everflow transaction ID into the landing "
                    "form's source field. Submitting the form carries that source value into "
                    "LeadByte; the demonstrated record then shows the identifier alongside the "
                    "lead. After buyer acceptance, the sold event and its revenue return to "
                    "Everflow. The presenter shows a lead that generated 20 worth of revenue "
                    "and describes Everflow as configured in dollars, with conversion occurring "
                    "automatically [NYSR6kFlcI8 @ 00:00:58]. Isaac offers three CRM connection "
                    "routes: Zapier for smaller businesses using HubSpot or Salesforce, webhooks "
                    "for proprietary systems, and the direct API for larger deployments. Their "
                    "timing examples are an afternoon for the Zapier loop and a couple of "
                    "developer days to map a custom webhook connection. The proposed milestone "
                    "economics are $50 for a lead, $200 when a retainer is signed, and a "
                    "bonus when the case settles [kLc_7B0eexA @ 00:01:38]. Daniel demonstrates "
                    "the subscription alternative with a recurring 20% monthly commission, "
                    "lasting until the customer cancels. FirstPromoter also supports up to "
                    "three sub-affiliate layers in their walkthrough. Daniel connects Stripe "
                    "with test API keys and uses test mode to explore the workflow without "
                    "touching real customer payments [SWQet1wMMyA @ 00:03:03]."
                ),
            ],
            "table": {
                "caption": "Exact fields, settings, and commercial figures shown or proposed by the practitioners.",
                "headers": ["Execution point", "Demonstrated setting or operation", "Expert Source"],
                "rows": [
                    [
                        "Mark a generated test click with a static additional parameter",
                        "Use the demonstrated sub five value everflow test when generating a link for testing.",
                        "Everflow - Partner Marketing Platform ([_VC3Wol9b0c @ 00:01:52])",
                    ],
                    [
                        "Verify that the advertiser received and returned the transaction identifier",
                        "Inspect the advertiser postback report for attempted signals, acceptance, rejection, and the recorded reason.",
                        "Everflow - Partner Marketing Platform ([qXMBHCgI3Wk @ 00:01:12])",
                    ],
                    [
                        "Attach both Meta integrations to the Facebook traffic source",
                        "Donald selects the pixel and cost integrations, warning that costs will not be pulled otherwise.",
                        "ClickFlare ([cSLdoNWYxfE @ 00:05:44])",
                    ],
                    [
                        "Carry the tracker identifier into the Everflow affiliate offer",
                        "Append the ClickFlare click ID to the offer URL so Everflow can return it upon conversion.",
                        "ClickFlare ([cSLdoNWYxfE @ 00:07:39])",
                    ],
                    [
                        "Return an accepted lead's commercial result rather than only its form submission",
                        "Send the sold-lead event back from LeadByte with the respective revenue represented by Everflow's amount.",
                        "LeadByte ([NYSR6kFlcI8 @ 00:00:39])",
                    ],
                    [
                        "Keep the demonstrated recurring reward connected to an active subscription",
                        "Daniel selects a 20% monthly commission with duration set to until customer cancels.",
                        "Daniel | Tech & Data ([SWQet1wMMyA @ 00:03:03])",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Small settings that carry the attribution",
                "body": "The practitioners identify these specific configuration details in their walkthroughs.",
                "items": [
                    (
                        "Use advertiser-level events for an action shared across that advertiser's "
                        "offers; the general setup trainer demonstrates one add-to-cart event "
                        "postback working across offers. "
                        "[Everflow - Partner Marketing Platform — FMpj69YFsHA @ 00:10:48]"
                    ),
                    (
                        "Select the pixel integration again at ClickFlare campaign level; "
                        "Donald warns that leaving it unselected means it will not work. "
                        "[ClickFlare — cSLdoNWYxfE @ 00:09:07]"
                    ),
                    (
                        "For a custom conversion, make ct equal the custom conversion's "
                        "parameter, preserving case and removing spaces. "
                        "[ClickFlare — cSLdoNWYxfE @ 00:13:26]"
                    ),
                    (
                        "In the Facebook setup Carlos shares, use transaction ID as the "
                        "suggested event identifier to help Facebook ignore duplicate conversions. "
                        "[Carlos Corona — zOQZw8jApe0 @ 00:23:02]"
                    ),
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Generate the offer-partner link",
                    "action": "Select the offer and partner, then configure the available additional parameters.",
                    "detail": (
                        "Use the tracking link generator, select the offer and partner, and "
                        "choose direct or redirect linking when that option is available. "
                        "Add the demonstrated test marker through the additional-parameters "
                        "fields and copy the resulting link. "
                        "[Everflow - Partner Marketing Platform — _VC3Wol9b0c @ 00:00:24] "
                        "[Everflow - Partner Marketing Platform — _VC3Wol9b0c @ 00:01:30]"
                    ),
                },
                {
                    "step": 2,
                    "title": "Connect the incoming and outgoing postbacks",
                    "action": "Enter the partner-provided postback and obtain the global advertiser postback.",
                    "detail": (
                        "Under Partners and postbacks, add an active postback with the chosen "
                        "type, level, partner, and delivery method. Obtain the global advertiser "
                        "postback from Control Center and platform configurations, then pass it "
                        "to the advertiser for their implementation. "
                        "[Everflow - Partner Marketing Platform — q6vkJhEncx0 @ 00:05:59] "
                        "[Everflow - Partner Marketing Platform — q6vkJhEncx0 @ 00:09:07]"
                    ),
                },
                {
                    "step": 3,
                    "title": "Attach the commercial event",
                    "action": "Configure the sold-lead, CRM milestone, or subscription workflow being used.",
                    "detail": (
                        "For LeadByte, carry the transaction ID into the form's source field "
                        "and return the sold event with revenue after buyer acceptance. For "
                        "CRM milestones, Isaac describes Zapier, webhooks, and the direct API. "
                        "For Daniel's subscription example, configure 20% monthly until cancellation. "
                        "[LeadByte — NYSR6kFlcI8 @ 00:00:39] "
                        "[Everflow - Partner Marketing Platform — kLc_7B0eexA @ 00:01:38] "
                        "[Daniel | Tech & Data — SWQet1wMMyA @ 00:03:03]"
                    ),
                },
                {
                    "step": 4,
                    "title": "Complete and inspect a test conversion",
                    "action": "Inspect advertiser postback results and, for Facebook, the returning event payload.",
                    "detail": (
                        "Use the advertiser postback report to inspect acceptance, rejection, "
                        "and the values processed. For the Facebook flow Carlos shares, create "
                        "the ad, click it as a user, complete the advertiser conversion, and "
                        "inspect Events Manager and the Everflow postback payload for the "
                        "Facebook click ID. "
                        "[Everflow - Partner Marketing Platform — qXMBHCgI3Wk @ 00:00:55] "
                        "[Carlos Corona — zOQZw8jApe0 @ 00:26:36] "
                        "[Carlos Corona — zOQZw8jApe0 @ 00:27:55]"
                    ),
                },
            ],
        },
        {
            "id": "alternative-playbooks",
            "title": "Where Practitioners Disagree & Alternative Playbooks",
            "paragraphs": [
                (
                    "Daniel and AffiliateStrat emphasize different operating footprints. Daniel "
                    "positions FirstPromoter as specialized subscription infrastructure: billing "
                    "integration, recurring commissions, partner tracking, and payout automation "
                    "without the heavier enterprise setup they associate with PartnerStack. Their "
                    "comparison says PartnerStack brings an enterprise ecosystem and marketplace, "
                    "but also larger budgets, implementation work, and operational overhead. "
                    "FirstPromoter is their lighter route for SaaS founders and growth teams "
                    "[SWQet1wMMyA @ 00:05:53]. AffiliateStrat's Everflow review values a broader "
                    "partner-management environment, including marketplace access and detailed "
                    "reporting, but describes a mandatory four-week onboarding process with "
                    "tutorials before launch. They present that training and support as a "
                    "strength, especially for someone new to managing a partner network "
                    "[Z_YllaXsWGA @ 00:03:23]. Their drawbacks are equally concrete: Everflow's "
                    "pricing is a contact-and-quote arrangement rather than a clear public "
                    "ladder, and its marketplace is smaller than some major affiliate networks. "
                    "They also describe Everflow Plus as an option for hands-on setup assistance. "
                    "These are different product priorities rather than competing measurements "
                    "of one campaign: Daniel stresses subscription-specific simplicity, while "
                    "AffiliateStrat stresses partner breadth, reporting depth, and supported "
                    "onboarding. AffiliateStrat repeatedly ties fit to the business type and "
                    "size rather than declaring every platform interchangeable [Z_YllaXsWGA @ 00:21:15]."
                ),
                (
                    "Paulina takes the strongest position against pixel-led tracking, describing "
                    "S2S as the method for accurate attribution and emphasizing backend exchanges "
                    "rather than third-party cookies. Their argument also includes flexibility "
                    "over when a conversion counts: shipment or the end of a refund period "
                    "can define the successful event instead of an immediate thank-you-page "
                    "purchase signal [oZcc_4NfA3g @ 00:04:39]. Everflow's Pete and Bonnie offer "
                    "a more mixed technical menu. Bonnie demonstrates direct linking through "
                    "JavaScript, with a transaction ID created on the click, stored locally, "
                    "and passed into conversion code. They also demonstrate coupon-code "
                    "attribution that identifies the partner and offer without a tracking-link "
                    "click [BzxID19IQnM @ 00:10:25]. In the closing questions, Pete says an "
                    "iframe request containing the transaction ID can still report when "
                    "cookies are blocked, provided the request actually reaches the tracking "
                    "code. Pete nevertheless recommends moving to server-side tracking where "
                    "possible [BzxID19IQnM @ 00:22:41]. Pixel Setup GTM Expert demonstrates another "
                    "combination: Facebook browser-side and server-side tracking together, plus "
                    "a client dashboard showing event flow. Their implementation uses Cloudflare "
                    "and shows Meta activity specifically. That is a working demonstration "
                    "of their chosen setup, not Paulina's argument for abandoning pixel-led "
                    "measurement across channels [HBs0vkiWarc @ 00:00:17]."
                ),
                (
                    "The Meta playbooks also take different routes through the stack. Donald "
                    "puts ClickFlare between Everflow and Meta so the same dashboard can show "
                    "advertising costs, revenue, and conversion information. Their setup connects "
                    "the conversion API separately from cost tracking, then maps the events "
                    "that should be delivered to the pixel. The purpose they state is to "
                    "identify profitable campaigns, ad sets, and creatives while sending richer "
                    "conversion signals back to Meta [cSLdoNWYxfE @ 00:00:36]. Carlos instead "
                    "shares Everflow's direct Facebook integration. That presentation creates "
                    "an app, obtains the app ID and app secret, creates a system-user token, "
                    "and stores those three values in the partner integration. Once created, "
                    "the integration can serve other postbacks for the same Facebook business "
                    "account [zOQZw8jApe0 @ 00:12:05]. Isaac's later postback walkthrough explains "
                    "the broader delivery choices: HTML for image or iframe pixels, dedicated "
                    "Meta and TikTok options, and traditional server-to-server postbacks. Their "
                    "S2S option can delay delivery to the partner by up to five minutes. "
                    "They also distinguish a global partner postback from a specific "
                    "offer-partner configuration and a global-offer configuration. The operator "
                    "therefore chooses both the delivery route and the scope of events "
                    "that route will receive [q6vkJhEncx0 @ 00:07:27]."
                ),
            ],
            "table": {
                "caption": "Different priorities and implementation routes, without turning them into invented head-to-head results.",
                "headers": ["Playbook or contrast", "What the practitioner actually emphasizes", "Expert Source"],
                "rows": [
                    [
                        "Subscription-specific infrastructure instead of a heavier enterprise partner ecosystem",
                        "Daniel favors FirstPromoter's lighter launch and billing-linked workflow while describing PartnerStack's greater implementation overhead.",
                        "Daniel | Tech & Data ([SWQet1wMMyA @ 00:05:53])",
                    ],
                    [
                        "Supported onboarding and broad partner management instead of immediate simplicity",
                        "AffiliateStrat describes mandatory four-week onboarding and presents tutorials and support as important strengths.",
                        "AffiliateStrat ([Z_YllaXsWGA @ 00:03:23])",
                    ],
                    [
                        "Delayed commercial confirmation instead of firing immediately on a purchase page",
                        "Paulina says the conversion timeline can wait until shipment or until the refund period expires.",
                        "RedTrack.io ([oZcc_4NfA3g @ 00:04:39])",
                    ],
                    [
                        "Coupon attribution instead of requiring the customer to click a tracking link",
                        "Bonnie associates the coupon with an offer and partner, then attributes the returning coupon conversion.",
                        "Everflow - Partner Marketing Platform ([BzxID19IQnM @ 00:12:12])",
                    ],
                    [
                        "Tracker-mediated Meta delivery with advertising cost and revenue in one dashboard",
                        "Donald connects conversion API delivery and cost tracking as separate integrations within ClickFlare.",
                        "ClickFlare ([cSLdoNWYxfE @ 00:01:28])",
                    ],
                    [
                        "Direct Facebook delivery from the partner's existing Everflow integration",
                        "The demonstration Carlos shares selects Facebook delivery, the saved integration, and the receiving pixel ID.",
                        "Carlos Corona ([zOQZw8jApe0 @ 00:20:22])",
                    ],
                ],
            },
        },
        {
            "id": "failure-modes",
            "title": "Firsthand Failure Modes, Traps & Economics Checks",
            "paragraphs": [
                (
                    "Isaac's support experience puts formatting near the front of the "
                    "troubleshooting queue. They report seeing partner postbacks missing the "
                    "question mark after the domain, and demonstrate how an extra space "
                    "can be difficult to spot while still breaking the URL. A misspelled "
                    "transaction parameter is another example. Their sequence is to check "
                    "formatting, check the correct parameter and macro vocabulary, and verify "
                    "that the advertiser receives and returns the transaction ID "
                    "[NSernIgs5XQ @ 00:11:25]. In the later Postbacks 101 session, Isaac "
                    "identifies wrong platform-specific formats as a recurring customer-success "
                    "problem. Everflow's transaction ID label is not automatically the label "
                    "another platform expects for its click ID. They also recommend having "
                    "the advertiser implement their side because macro brackets differ between "
                    "platforms [q6vkJhEncx0 @ 00:12:27]. Donald demonstrates a separate operational "
                    "snag when their Facebook cost connection needs reconnecting, and then "
                    "warns that the traffic source must actually select the cost integration "
                    "or costs will not be pulled. Their custom-conversion warning is similarly "
                    "literal: ct must match the configured parameter, with the right case "
                    "and no spaces. These are demonstrated reconnects and practitioner-reported "
                    "configuration failures, not unexplained changes in traffic performance "
                    "[cSLdoNWYxfE @ 00:04:32] [cSLdoNWYxfE @ 00:13:03]."
                ),
                (
                    "A conversion visible to the advertiser can still be rejected inside "
                    "Everflow. The general advertiser setup trainer opens the advertiser "
                    "postback report, inspects status, and demonstrates a rejection because "
                    "the event ID does not belong to the offer. The same report distinguishes "
                    "approved, rejected, and pending results and exposes the conversion method "
                    "[FMpj69YFsHA @ 00:22:39]. Their duplicate-conversion answer points to the "
                    "offer's revenue-and-payout settings: when duplicates are not allowed, "
                    "later conversions with the same transaction ID are automatically rejected, "
                    "although the trainer says they can be approved manually "
                    "[FMpj69YFsHA @ 00:26:09]. Isaac's precious-metals client shows the economic "
                    "cost of a different missing connection. Sales staff identified disconnected "
                    "numbers and bad information within minutes, while affiliate commissions "
                    "had already been paid and had to be clawed back weeks later. The CRM "
                    "connection replaced that delayed reconciliation with immediate quality "
                    "feedback and duplicate blocking [kLc_7B0eexA @ 00:00:03]. LeadByte's buyer "
                    "acceptance workflow supplies another concrete checkpoint: the buyer can "
                    "accept or reject the lead, and acceptance is what records the revenue "
                    "and causes the sold event to return with an amount. The demonstrated "
                    "commercial signal is therefore the buyer's result, not merely the "
                    "presence of a submitted form [NYSR6kFlcI8 @ 00:00:17]."
                ),
                (
                    "The demonstrations expose reporting and implementation limits as well as "
                    "successful events. Pixel Setup GTM Expert's dashboard shows Meta events "
                    "but no TikTok or GA4 activity because those destinations were not "
                    "configured. After the purchase, the presenter shows one sale worth "
                    "1450 Taka; selecting yesterday produces zeros because the implementation "
                    "had only just gone live. Their dashboard's visible scope follows the "
                    "setup they actually performed [HBs0vkiWarc @ 00:02:03] "
                    "[HBs0vkiWarc @ 00:06:11]. AffiliateStrat encounters a permissions block "
                    "when opening traffic health in the demo account and skips that "
                    "screen. Their detailed click report also displays only the first "
                    "thousand rows, with the remainder available through an asynchronous "
                    "report request [Z_YllaXsWGA @ 00:12:33]. Pete supplies the implementation "
                    "bottleneck behind the server-side recommendation: engineering time is "
                    "required on the advertiser's side or the operator's side, and Pete "
                    "calls that a major reason people have not switched. Conversely, "
                    "Pete reports situations where getting tracking code into a website "
                    "release slowed deployment. Their comparison therefore includes both "
                    "the engineering work needed for S2S and the release process that "
                    "can obstruct browser-side code. Neither path is described as requiring "
                    "no implementation effort [BzxID19IQnM @ 00:20:01]."
                ),
            ],
            "table": {
                "caption": "Observed snags and explicit practitioner checks before trusting the reporting.",
                "headers": ["Failure or economics check", "Reported symptom and inspection route", "Expert Source"],
                "rows": [
                    [
                        "Invisible spaces or missing punctuation break the partner's postback URL",
                        "Isaac reports missing question marks and demonstrates an extra space that prevents the postback working.",
                        "Everflow - Partner Marketing Platform ([NSernIgs5XQ @ 00:11:25])",
                    ],
                    [
                        "A receiving platform expects its own parameter and macro vocabulary",
                        "Isaac identifies wrong postback formats as a recurring customer-success issue and checks the platform-specific guide.",
                        "Everflow - Partner Marketing Platform ([q6vkJhEncx0 @ 00:12:27])",
                    ],
                    [
                        "An advertiser's event can arrive but fail the offer association check",
                        "The trainer opens conversion details and shows rejection because the event ID does not belong to the offer.",
                        "Everflow - Partner Marketing Platform ([FMpj69YFsHA @ 00:23:47])",
                    ],
                    [
                        "Lead commissions were paid before sales feedback exposed disconnected numbers",
                        "Isaac's precious-metals client had been manually clawing back commissions weeks later before connecting the CRM.",
                        "Everflow - Partner Marketing Platform ([kLc_7B0eexA @ 00:00:03])",
                    ],
                    [
                        "Facebook cannot recognize the demonstrated conversion without the returned click identifier",
                        "The presenter Carlos shares inspects the payload and warns that the actual Facebook click ID must replace the macro.",
                        "Carlos Corona ([zOQZw8jApe0 @ 00:28:16])",
                    ],
                    [
                        "A configured Meta dashboard does not imply other destinations were connected",
                        "Pixel Setup GTM Expert explicitly attributes missing TikTok and GA4 events to not configuring those destinations.",
                        "Pixel Setup GTM Expert ([HBs0vkiWarc @ 00:02:03])",
                    ],
                    [
                        "Tracking-domain selection changes generated links rather than blocking other active domains",
                        "Isaac says selecting a specific domain does not block traffic arriving through links using other active domains.",
                        "Everflow - Partner Marketing Platform ([Ni95PXMEMzE @ 00:06:13])",
                    ],
                    [
                        "Detailed click reporting has a displayed-row limit in the walkthrough",
                        "AffiliateStrat shows the first thousand rows and explains that remaining data requires an asynchronous report request.",
                        "AffiliateStrat ([Z_YllaXsWGA @ 00:12:33])",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "The practitioners' final tracking checks",
                "body": "Use the actual rejection reason, payload, and event result shown by the reporting tools.",
                "items": [
                    (
                        "Check that the transaction ID is passed in the base destination "
                        "URL and correctly returned by the advertiser; Isaac names both "
                        "directions as essential troubleshooting checks. "
                        "[Everflow - Partner Marketing Platform — NSernIgs5XQ @ 00:14:26]"
                    ),
                    (
                        "Read the advertiser postback's conversion details instead of stopping "
                        "at a missing total; the demonstrated rejection identifies an event "
                        "ID that does not belong to the offer. "
                        "[Everflow - Partner Marketing Platform — FMpj69YFsHA @ 00:23:47]"
                    ),
                    (
                        "For the Facebook flow Carlos shares, inspect the payload for the "
                        "actual Facebook click ID; the presenter says Facebook will not "
                        "recognize the successful conversion when it is absent. "
                        "[Carlos Corona — zOQZw8jApe0 @ 00:28:16]"
                    ),
                    (
                        "Follow the purchase through the live dashboard: Pixel Setup GTM "
                        "Expert checks the purchase event and then the one-sale total "
                        "worth 1450 Taka after completing the purchase. "
                        "[Pixel Setup GTM Expert — HBs0vkiWarc @ 00:05:49] "
                        "[Pixel Setup GTM Expert — HBs0vkiWarc @ 00:06:11]"
                    ),
                ],
            },
        },
    ],
    "pull_quote": (
        '"They stopped paying for activity and started paying for outcomes." '
        "— Everflow - Partner Marketing Platform (kLc_7B0eexA @ 00:00:33)."
    ),
    "diagram_id": "diag-05",
    "action_checklist": [
        (
            "Generate the offer-partner tracking link and use additional parameters "
            "for the demonstrated test marker before copying the link. "
            "[Everflow - Partner Marketing Platform — _VC3Wol9b0c @ 00:01:30]"
        ),
        (
            "Inspect tracking and conversion domains in platform configurations; "
            "distinguish the partner-click domain from the conversion-postback domain. "
            "[Everflow - Partner Marketing Platform — Ni95PXMEMzE @ 00:01:48]"
        ),
        (
            "Add the partner's receiving postback and pass the global advertiser "
            "postback to the advertiser, preserving the transaction-ID round trip. "
            "[Everflow - Partner Marketing Platform — q6vkJhEncx0 @ 00:05:05] "
            "[Everflow - Partner Marketing Platform — q6vkJhEncx0 @ 00:14:32]"
        ),
        (
            "Connect the chosen commercial result: LeadByte buyer acceptance, CRM "
            "milestones, or FirstPromoter's billing-linked recurring commission. "
            "[LeadByte — NYSR6kFlcI8 @ 00:00:39] "
            "[Everflow - Partner Marketing Platform — kLc_7B0eexA @ 00:02:24] "
            "[Daniel | Tech & Data — SWQet1wMMyA @ 00:03:03]"
        ),
        (
            "For Donald's Meta route, connect conversion API and cost tracking, "
            "append the ClickFlare click ID, and select the campaign integration. "
            "[ClickFlare — cSLdoNWYxfE @ 00:01:28] "
            "[ClickFlare — cSLdoNWYxfE @ 00:07:39] "
            "[ClickFlare — cSLdoNWYxfE @ 00:09:07]"
        ),
        (
            "Run the conversion journey and inspect accepted or rejected advertiser "
            "postbacks; for the Facebook workflow, inspect Events Manager and the "
            "Everflow payload containing the Facebook click ID. "
            "[Everflow - Partner Marketing Platform — qXMBHCgI3Wk @ 00:00:55] "
            "[Carlos Corona — zOQZw8jApe0 @ 00:26:36] "
            "[Carlos Corona — zOQZw8jApe0 @ 00:27:55]"
        ),
    ],
    "statutory_citations": [
        {
            "title": "Everflow - Partner Marketing Platform — What is a Server-to-Server (S2S) Postback? | Everflow Mini Webinars [00:00:36]",
            "url": "https://www.youtube.com/watch?v=2Q-xY6ABqXE&t=36s",
            "relevance": "Primary practitioner testimony on generating, storing, and returning the transaction ID.",
        },
        {
            "title": "Everflow - Partner Marketing Platform — How to Set Up & Test Your Advertiser Postback | Everflow Mini Webinars [00:00:55]",
            "url": "https://www.youtube.com/watch?v=qXMBHCgI3Wk&t=55s",
            "relevance": "Primary practitioner testimony on validating conversion values, statuses, and advertiser postback results.",
        },
        {
            "title": "LeadByte — Tracking Leads Sold in Everflow [00:00:39]",
            "url": "https://www.youtube.com/watch?v=NYSR6kFlcI8&t=39s",
            "relevance": "Primary practitioner testimony on returning buyer-accepted sold leads with revenue.",
        },
        {
            "title": "Everflow - Partner Marketing Platform — Connect Everflow to Your CRM: Pay on Quality, Not Just Quantity | Everflow Mini Webinars [00:00:33]",
            "url": "https://www.youtube.com/watch?v=kLc_7B0eexA&t=33s",
            "relevance": "Primary practitioner testimony on disconnected-number rejection and duplicate blocking before payout.",
        },
    ],
    "source_citations": [
        {
            "source_type": "video_pro_tip",
            "video_id": "SWQet1wMMyA",
            "title": "FirstPromoter Review - 2026 | The Easiest Way to Run a SaaS Affiliate Program?",
            "channel": "Daniel | Tech & Data",
            "author": "Daniel | Tech & Data",
            "text": "For our Task Flow example, we'll configure a recurring 20% monthly commission, and for the duration parameter, we'll select until customer cancels.",
            "tip": "For our Task Flow example, we'll configure a recurring 20% monthly commission, and for the duration parameter, we'll select until customer cancels.",
            "timestamp": 183,
            "timestamp_seconds": 183,
            "timestamp_label": "[00:03:03]",
            "url": "https://www.youtube.com/watch?v=SWQet1wMMyA&t=183s",
            "markdown": "[00:03:03](https://www.youtube.com/watch?v=SWQet1wMMyA&t=183s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q9.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "2Q-xY6ABqXE",
            "title": "What is a Server-to-Server (S2S) Postback? | Everflow Mini Webinars",
            "channel": "Everflow - Partner Marketing Platform",
            "author": "Everflow - Partner Marketing Platform",
            "text": "The process starts the moment a user clicks a partner's tracking link, prompting Everflow to immediately generate and store a unique identifier called the transaction ID.",
            "tip": "The process starts the moment a user clicks a partner's tracking link, prompting Everflow to immediately generate and store a unique identifier called the transaction ID.",
            "timestamp": 36,
            "timestamp_seconds": 36,
            "timestamp_label": "[00:00:36]",
            "url": "https://www.youtube.com/watch?v=2Q-xY6ABqXE&t=36s",
            "markdown": "[00:00:36](https://www.youtube.com/watch?v=2Q-xY6ABqXE&t=36s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q9.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "qXMBHCgI3Wk",
            "title": "How to Set Up & Test Your Advertiser Postback | Everflow Mini Webinars",
            "channel": "Everflow - Partner Marketing Platform",
            "author": "Everflow - Partner Marketing Platform",
            "text": "This report helps identify if conversions were accepted or rejected and the reason why.",
            "tip": "This report helps identify if conversions were accepted or rejected and the reason why.",
            "timestamp": 72,
            "timestamp_seconds": 72,
            "timestamp_label": "[00:01:12]",
            "url": "https://www.youtube.com/watch?v=qXMBHCgI3Wk&t=72s",
            "markdown": "[00:01:12](https://www.youtube.com/watch?v=qXMBHCgI3Wk&t=72s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q9.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "cSLdoNWYxfE",
            "title": "How To Track Everflow and Meta For Advanced Affiliate Marketing",
            "channel": "ClickFlare",
            "author": "ClickFlare",
            "text": "We need to append the ClickFlare click ID to that Everflow link.",
            "tip": "We need to append the ClickFlare click ID to that Everflow link.",
            "timestamp": 459,
            "timestamp_seconds": 459,
            "timestamp_label": "[00:07:39]",
            "url": "https://www.youtube.com/watch?v=cSLdoNWYxfE&t=459s",
            "markdown": "[00:07:39](https://www.youtube.com/watch?v=cSLdoNWYxfE&t=459s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q9.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "oZcc_4NfA3g",
            "title": "S2S Tracking Explained: How to Track Conversions Server-to-server",
            "channel": "RedTrack.io",
            "author": "RedTrack.io",
            "text": "You want to establish that conversion happens only after the delivery was shipped or after the refund period has expired.",
            "tip": "You want to establish that conversion happens only after the delivery was shipped or after the refund period has expired.",
            "timestamp": 295,
            "timestamp_seconds": 295,
            "timestamp_label": "[00:04:55]",
            "url": "https://www.youtube.com/watch?v=oZcc_4NfA3g&t=295s",
            "markdown": "[00:04:55](https://www.youtube.com/watch?v=oZcc_4NfA3g&t=295s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q9.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "zOQZw8jApe0",
            "title": "Pay Per Call: How to configure your Everflow postback to track FB conversion pixels",
            "channel": "Carlos Corona",
            "author": "Carlos Corona",
            "text": "You click on it as a user would, and this is important because only then the Facebook click ID will be created and added to the Everflow tracking link.",
            "tip": "You click on it as a user would, and this is important because only then the Facebook click ID will be created and added to the Everflow tracking link.",
            "timestamp": 1618,
            "timestamp_seconds": 1618,
            "timestamp_label": "[00:26:58]",
            "url": "https://www.youtube.com/watch?v=zOQZw8jApe0&t=1618s",
            "markdown": "[00:26:58](https://www.youtube.com/watch?v=zOQZw8jApe0&t=1618s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony from the Everflow demonstration shared by Carlos in Chapter Q9.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "BzxID19IQnM",
            "title": "Everflow Connect 2020 - Tracking Methods: Past, Present, and Future",
            "channel": "Everflow - Partner Marketing Platform",
            "author": "Everflow - Partner Marketing Platform",
            "text": "Another thing that is a con of server-side tracking is it actually requires engineering time and effort from either the advertiser's end or your end to actually get it up and working.",
            "tip": "Another thing that is a con of server-side tracking is it actually requires engineering time and effort from either the advertiser's end or your end to actually get it up and working.",
            "timestamp": 1255,
            "timestamp_seconds": 1255,
            "timestamp_label": "[00:20:55]",
            "url": "https://www.youtube.com/watch?v=BzxID19IQnM&t=1255s",
            "markdown": "[00:20:55](https://www.youtube.com/watch?v=BzxID19IQnM&t=1255s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q9.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "FMpj69YFsHA",
            "title": "General Advertiser & Postback set up",
            "channel": "Everflow - Partner Marketing Platform",
            "author": "Everflow - Partner Marketing Platform",
            "text": "If it's rejected, you can also view the conversion details and you can see why this postback or this conversion has been rejected.",
            "tip": "If it's rejected, you can also view the conversion details and you can see why this postback or this conversion has been rejected.",
            "timestamp": 1427,
            "timestamp_seconds": 1427,
            "timestamp_label": "[00:23:47]",
            "url": "https://www.youtube.com/watch?v=FMpj69YFsHA&t=1427s",
            "markdown": "[00:23:47](https://www.youtube.com/watch?v=FMpj69YFsHA&t=1427s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q9.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Ni95PXMEMzE",
            "title": "Tracking & Conversion Domain Management | Webinars",
            "channel": "Everflow - Partner Marketing Platform",
            "author": "Everflow - Partner Marketing Platform",
            "text": "Selecting a specific tracking domain here does not block traffic from tracking links with other active domains.",
            "tip": "Selecting a specific tracking domain here does not block traffic from tracking links with other active domains.",
            "timestamp": 373,
            "timestamp_seconds": 373,
            "timestamp_label": "[00:06:13]",
            "url": "https://www.youtube.com/watch?v=Ni95PXMEMzE&t=373s",
            "markdown": "[00:06:13](https://www.youtube.com/watch?v=Ni95PXMEMzE&t=373s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q9.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "NYSR6kFlcI8",
            "title": "Tracking Leads Sold in Everflow",
            "channel": "LeadByte",
            "author": "LeadByte",
            "text": "If they accept the lead, a revenue will be recorded and that sold event will be sent back to Everflow with the respective revenue amount.",
            "tip": "If they accept the lead, a revenue will be recorded and that sold event will be sent back to Everflow with the respective revenue amount.",
            "timestamp": 39,
            "timestamp_seconds": 39,
            "timestamp_label": "[00:00:39]",
            "url": "https://www.youtube.com/watch?v=NYSR6kFlcI8&t=39s",
            "markdown": "[00:00:39](https://www.youtube.com/watch?v=NYSR6kFlcI8&t=39s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q9.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Z_YllaXsWGA",
            "title": "Everflow Review & Guide: Full Platform Walkthrough, Pros, Cons, and Real Demos",
            "channel": "AffiliateStrat",
            "author": "AffiliateStrat",
            "text": "Only the first thousand rows can be displayed. The remaining data can be retrieved by requesting the report asynchronously.",
            "tip": "Only the first thousand rows can be displayed. The remaining data can be retrieved by requesting the report asynchronously.",
            "timestamp": 753,
            "timestamp_seconds": 753,
            "timestamp_label": "[00:12:33]",
            "url": "https://www.youtube.com/watch?v=Z_YllaXsWGA&t=753s",
            "markdown": "[00:12:33](https://www.youtube.com/watch?v=Z_YllaXsWGA&t=753s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q9.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "NSernIgs5XQ",
            "title": "Partner and Advertiser Postback 101",
            "channel": "Everflow - Partner Marketing Platform",
            "author": "Everflow - Partner Marketing Platform",
            "text": "One thing that I see sometimes is a lack of a question mark.",
            "tip": "One thing that I see sometimes is a lack of a question mark.",
            "timestamp": 685,
            "timestamp_seconds": 685,
            "timestamp_label": "[00:11:25]",
            "url": "https://www.youtube.com/watch?v=NSernIgs5XQ&t=685s",
            "markdown": "[00:11:25](https://www.youtube.com/watch?v=NSernIgs5XQ&t=685s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q9.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "q6vkJhEncx0",
            "title": "Postbacks 101 With Everflow",
            "channel": "Everflow - Partner Marketing Platform",
            "author": "Everflow - Partner Marketing Platform",
            "text": "One of the big issues that I've seen in customer success with why someone's postbacks might be failing is because they're using the wrong format for their postback.",
            "tip": "One of the big issues that I've seen in customer success with why someone's postbacks might be failing is because they're using the wrong format for their postback.",
            "timestamp": 747,
            "timestamp_seconds": 747,
            "timestamp_label": "[00:12:27]",
            "url": "https://www.youtube.com/watch?v=q6vkJhEncx0&t=747s",
            "markdown": "[00:12:27](https://www.youtube.com/watch?v=q6vkJhEncx0&t=747s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q9.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "_VC3Wol9b0c",
            "title": "How To Generate Tracking Links | Everflow Mini Webinars",
            "channel": "Everflow - Partner Marketing Platform",
            "author": "Everflow - Partner Marketing Platform",
            "text": "First you must select an offer and a partner that the tracking link is for.",
            "tip": "First you must select an offer and a partner that the tracking link is for.",
            "timestamp": 24,
            "timestamp_seconds": 24,
            "timestamp_label": "[00:00:24]",
            "url": "https://www.youtube.com/watch?v=_VC3Wol9b0c&t=24s",
            "markdown": "[00:00:24](https://www.youtube.com/watch?v=_VC3Wol9b0c&t=24s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q9.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "kLc_7B0eexA",
            "title": "Connect Everflow to Your CRM: Pay on Quality, Not Just Quantity | Everflow Mini Webinars",
            "channel": "Everflow - Partner Marketing Platform",
            "author": "Everflow - Partner Marketing Platform",
            "text": "If it's a duplicate, it's blocked before a payout is ever triggered. And they stopped paying for activity and started paying for outcomes.",
            "tip": "If it's a duplicate, it's blocked before a payout is ever triggered. And they stopped paying for activity and started paying for outcomes.",
            "timestamp": 33,
            "timestamp_seconds": 33,
            "timestamp_label": "[00:00:33]",
            "url": "https://www.youtube.com/watch?v=kLc_7B0eexA&t=33s",
            "markdown": "[00:00:33](https://www.youtube.com/watch?v=kLc_7B0eexA&t=33s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q9.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "HBs0vkiWarc",
            "title": "Cloudflare Server Side Tracking Setup | GTM + Meta CAPI | Cloudflare pixel | Live Tracking Dashboard",
            "channel": "Pixel Setup GTM Expert",
            "author": "Pixel Setup GTM Expert",
            "text": "There is one total sale, whose value is 1450 Taka.",
            "tip": "There is one total sale, whose value is 1450 Taka.",
            "timestamp": 371,
            "timestamp_seconds": 371,
            "timestamp_label": "[00:06:11]",
            "url": "https://www.youtube.com/watch?v=HBs0vkiWarc&t=371s",
            "markdown": "[00:06:11](https://www.youtube.com/watch?v=HBs0vkiWarc&t=371s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q9.",
        },
    ],
}
