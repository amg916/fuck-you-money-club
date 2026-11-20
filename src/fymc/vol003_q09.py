CHAPTER_9 = {
    "id": "Q9", "chapter_id": "Q9", "chapter_number": 9, "question_number": 9,
    "slug": "outreach-billing-compliance-tax-and-ip-enforcement",
    "question_prompt": "How do we sell, bill, collect tax, and defend digital products without destroying margin?",
    "kicker": "Q9 / THE BIG MONEY PLAYBOOKS",
    "title": "Outreach, Billing Rules, Global Digital Tax & Anti-Piracy Enforcement",
    "subtitle": "Comment-to-DM Scripts, FTC ROSCA Click-to-Cancel Rules, EU/UK VAT vs. US Economic Nexus, Affiliate Disclosures & DMCA Takedowns",
    "layout_template": "legal_compliance_notes", "reading_time_minutes": 14,
    "executive_summary": "Build the sale around proof of permission, clear price terms, correct tax treatment, and owned assets. These are operating controls, not paperwork theater. A small team can sell globally only when each order leaves a usable record: what the buyer requested, what they accepted, who collected tax, and which rights were licensed. This chapter supplies outreach scripts, recurring billing checks, tax routing, affiliate controls, and a takedown notice. Model contribution after real delivery and selling costs; neither gross receipts nor a large damages demand is spendable profit. Keep cancellation easy and enforcement specific.",
    "key_metrics": [
        {"label": "Conservative", "value": "$10,000 net", "context": "$50,000 gross / 20%", "note": "Modeled contribution; before income tax."},
        {"label": "Base", "value": "$159,375 net", "context": "$425,000 gross / 37.5%", "note": "Modeled contribution; 1 FT + 3 C."},
        {"label": "Scaled", "value": "$440,000 net", "context": "$800,000 gross / 55%", "note": "Modeled contribution; not a forecast."}
    ],
    "sections": [
        {
            "heading": "1. Earn the DM before pitching the product",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Run high_velocity_dm_outbound_systems as a permission queue, not a scraped inbox list. Publish this trigger: 'Comment MAP and I will DM the free product launch map. No mailing list signup required.' A keyword requests that asset; it does not authorize an endless sales sequence or email subscription. Save the post, request time, handle, and asset sent. Use approved platform tools and stop when platform limits or buyer objections require it. Assign one contractor to requests and one to replies, with the full time operator owning exceptions. Count qualified replies per delivered asset, not messages sent. Remove duplicate requests before sending anything. A person who asks for a map should receive the map first, without being forced into a call or a paid trial.",
                "Use three messages, advancing only when the buyer replies. Message one: 'Here is the map you asked for: [link]. Which is the main blocker today: choosing an offer, building it, or finding buyers?' Message two: 'You said [blocker]. What have you tried, and what would a useful result look like this month? I can suggest a free next step or explain our paid kit.' Message three: 'Based on [need], the kit fits because [specific feature]. It costs $149 once, with no renewal. It includes [files] and excludes coaching. Refund terms: [link]. Want the checkout link?' Replace price and scope with actual terms. If the fit is poor, give the free step and close the thread. Silence is not a reason to send all three messages.",
                "For a warm email, use: 'Subject: The launch checklist we discussed. Hi [name], you asked about [need] at [event]. Here is the checklist: [link]. If [specific problem] is still live, reply with your current setup and I will point you to the relevant page. Our paid kit is optional. To stop sales emails, reply stop. [Sender name, business, postal address].' A prior meeting is context, not universal marketing permission. Check the recipient jurisdiction and your permission record before sending; UK and EU rules differ from US rules. Honor opt outs across every sending tool, not just one inbox. Review complaints and negative replies each Monday. Pause the source with rising objections rather than hiding the problem by rotating accounts or changing domains."
            ],
            "table": {
                "caption": "Forensic checks before increasing volume",
                "headers": ["Naive Trap", "Detection Metric", "Durable Operator Fallback"],
                "rows": [
                    ["Mass cold DMs", "Complaints per delivered DM", "Requested keyword assets only"],
                    ["Silent renewal", "Renewal disputes per charge", "Clear terms and easy exit"],
                    ["Tax assumed handled", "Orders without tax owner", "Verify seller contract"],
                    ["Automated piracy threats", "False matches per review", "Human rights review"]
                ]
            }
        },
        {
            "heading": "2. Make recurring charges explicit and exit simple",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "ROSCA, 15 U.S.C. section 8403, governs online negative option charges: disclose all material terms clearly before obtaining billing information, obtain express informed consent before charging, and provide simple mechanisms to stop recurring charges. Put the price, cadence, trial conversion, term, and cancellation method next to the purchase action. Use real copy: '$29 today, then $29 each month until canceled. Cancel online in Account > Billing. Cancellation stops future charges; access lasts through the paid period. Refund policy: [link].' Adapt this wording if access or refunds work differently. A receipt cannot repair a checkout that hid renewal terms. Store the displayed terms version, acceptance event, price, currency, and timestamp. Keep payment credentials with the processor; your evidence record does not need full card numbers or security codes.",
                "Do not describe 16 CFR Part 425 as a currently enforceable universal federal one click mandate. The Eighth Circuit vacated the FTC's 2024 negative option amendment in July 2025. The older rule concerns prenotification negative option plans, not every online subscription. ROSCA and applicable state renewal laws remain separate obligations; check current rule and litigation status before publishing legal claims. Adopt one click cancellation parity as your own service standard: make leaving no harder than joining. Do not require a phone call to end a plan bought online. This reduces avoidable disputes but cannot prevent every bank chargeback. Show the effective cancellation date immediately and email a record. Keep optional retention offers separate from the action that stops the next charge, with no forced survey or sales chat.",
                "Test billing with a real low value account and a controlled refund each month. Start a trial, inspect the conversion notice where required, cancel before renewal, and confirm that the next invoice is suppressed. Replay the cancellation webhook to prove duplicate events cannot restart a plan. Test cancellation during a failed payment retry as well as during an active term. A support agent should be able to stop future charges without asking engineering to edit a database. Keep renewal reminders where law or your promise requires them, and show a recognizable card statement descriptor. Track disputes by reason, product, and sales source. When 'subscription not recognized' rises, fix checkout wording and receipts first. Fighting each dispute with a generic terms PDF is slower than removing the underlying ambiguity."
            ]
        },
        {
            "heading": "3. Route digital tax by buyer, product, and seller",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "For electronically supplied B2C products, EU VAT generally follows the consumer's location. A seller established outside the EU generally has no small turnover exemption for these supplies; a qualifying EU established seller may have a limited cross border threshold exception. Non Union OSS can simplify reporting for eligible non EU suppliers. UK consumer digital supplies have separate rules: a non established seller generally must register from the first taxable supply, while domestic registration rules differ. 'Instant VAT' means determine liability on the sale, not that every creator worldwide owes VAT on every download. Classify prerecorded courses, live teaching, templates, and mixed bundles separately. Capture adequate location evidence and resolve contradictions before choosing a rate. See Council Directive 2006/112/EC, Articles 44, 58, and 196, and HMRC's VAT Notice 741A for the underlying place of supply framework.",
                "B2B is not a checkbox labeled company. Collect the legal business name, establishment location, and tax identifier, then validate an EU VAT ID through VIES and a UK VAT number through HMRC's checking service. Save the result and date with the invoice. For qualifying cross border B2B services, place of supply and reverse charge rules commonly shift accounting to the business customer; domestic supplies and exceptions need separate treatment. A failed validation is a review item, not automatic proof of fraud or automatic permission to remove tax. Request alternative business evidence where appropriate and document the decision. Use 'reverse charge' invoice wording only when that treatment actually applies. Never substitute a US employer identification number for a European VAT registration or assume every business purchase qualifies for zero collection.",
                "US sales tax needs two independent answers: is this product taxable here, and does this seller have a collection obligation here? South Dakota v. Wayfair removed the physical presence restriction, not state variation. Washington broadly taxes digital products, while California generally treats electronically delivered products differently from tangible deliveries; courses, subscriptions, and service bundles can change the result. Check each state's revenue department rather than copying a marketplace competitor. Track physical nexus separately from economic thresholds, measurement periods, included sales, and marketplace rules. A payment processor is not automatically a merchant of record. Read the contract to identify the legal seller and exactly which taxes the provider handles. Reconcile tax collected, credits, and remittances monthly. Sales tax and VAT held for authorities are liabilities, not product margin or marketing funds."
            ],
            "sop_steps": [
                {"step": 1, "title": "Identify the seller", "action": "Read the checkout contract.", "detail": "Record direct seller versus merchant of record responsibilities."},
                {"step": 2, "title": "Classify the supply", "action": "Map each SKU and bundle.", "detail": "Separate downloads, live services, and subscriptions."},
                {"step": 3, "title": "Validate the buyer", "action": "Store location and business evidence.", "detail": "Resolve inconsistent evidence and retain validation dates."},
                {"step": 4, "title": "Reconcile obligations", "action": "Compare sales with registrations and filings.", "detail": "Review state thresholds, VAT returns, refunds, and provider remittances monthly."}
            ]
        },
        {
            "heading": "4. Substantiate affiliates before paying for reach",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Treat 16 CFR Part 255 as FTC interpretive guidance on endorsements and testimonials under deception law, not a certification program. Require this affiliate wording beside the recommendation: 'I earn a commission if you buy through this link.' For a gifted product, say: 'The seller gave me free access to review this course.' Put the disclosure where people encounter the endorsement, not behind a profile link or beneath a collapsed caption. Video endorsements need disclosure in the video; consider both spoken and visible presentation so the audience actually receives it. A platform disclosure tool can help but does not excuse an unclear message. Give affiliates approved factual claims, prohibited unsupported claims, and a contact for checking new copy. Pay for valid referred sales, not invented testimonials or concealed relationships.",
                "A screenshot of one exceptional seller's revenue is not evidence of typical buyer earnings. Before using a testimonial, retain the original statement, permission, dates, relevant product version, and support for every objective claim you adopt. If an endorsement implies buyers generally achieve a result, substantiate that implication or clearly disclose the generally expected performance when the guides require it. A vague 'results vary' line does not solve an unsupported earnings message. Separate gross billings from refunds, advertising, labor, fees, and tax liabilities in every published example. Use this replacement script: 'This is one customer's documented experience, not our expected buyer outcome. We do not have evidence supporting an earnings prediction, so our offer describes the files and support provided rather than promising income.' Remove the earnings headline too.",
                "Give the third contractor a weekly sample of active affiliate posts and landing pages, selected by sales volume plus random coverage. Save dated captures, test disclosures on mobile, and compare claims against the evidence register. When a problem appears, send: 'Please remove [claim] and place [disclosure] beside the link by [time]. Reply with the updated URL. We have paused this creative while we check the correction.' Escalate repeated deception to suspension under the affiliate contract. Keep payout disputes separate from consumer refunds so buyers are not stranded between parties. Measure unsupported claims found per review and corrections completed, not just affiliate revenue. The operator should own final claim wording because outsourced promotion still affects the seller's reputation, refund load, and exposure to deceptive marketing allegations."
            ],
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Evidence before amplification",
                "body": "Scale only the exact creative whose price, claims, and relationship disclosures you checked.",
                "items": ["Archive the published version.", "Match objective claims to evidence.", "Remove misleading earnings implications.", "Recheck edits before resuming promotion."]
            }
        },
        {
            "heading": "5. Enforce owned rights and count recovered margin",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                "Run copyright_phash_reverse_image_statutory_settlement as an evidence workflow, not an automatic demand engine. Perceptual hashes and reverse image matches identify leads; they do not establish ownership, infringement, or damages. Preserve your original files, publication dates, contributor assignments, license terms, suspected URLs, and dated captures. Compare actual protected expression, then consider permission, fair use, public domain material, and mistaken identity before sending anything. A similar teaching idea or spreadsheet function is not necessarily copied expression. Route a specific hosting notice to the provider's designated DMCA agent, not unrelated advertisers or the uploader's employer. Separate removal requests from settlement proposals. Statutory damages under section 504 depend on eligibility, with registration timing under section 412 often decisive; neither a match nor a takedown creates an automatic cash entitlement or establishes an infringement award.",
                "Use this notice after completing the ownership review: 'To [designated agent]: I am [owner or authorized agent]. The copyrighted work is [course/template title, description, original URL; representative list if applicable]. Infringing material appears at [each exact URL and sufficient location details]. Please remove or disable access to that material under 17 U.S.C. section 512(c). Contact me at [name, postal address, telephone, email]. I have a good faith belief that use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law. The information in this notification is accurate, and under penalty of perjury, I am authorized to act on behalf of the owner of an exclusive right that is allegedly infringed. Electronic signature: [name]. Date: [date].' Replace every bracket, identify specific files, and retain the submitted notice and delivery record.",
                "A valid counter notification can lead to restoration after ten to fourteen business days under section 512(g), unless the provider receives notice of a qualifying court action. Know that timetable before filing; material misrepresentation can create section 512(f) liability. Budget enforcement by recoverable contribution, not retail price multiplied by alleged downloads. In the model below, gross billings exclude separately collected indirect tax; net means contribution after refunds, delivery, marketing, allocated team labor, software, fees, and enforcement, before income tax. Each annual scenario uses one full time operator plus three contractors, written as 1 FT + 3 C; hours and compensation must fit the budget, and the conservative case cannot fund four ordinary full time salaries. The higher scaled margin assumes efficiency and must be earned. Unpaid settlements and speculative prevented losses never enter realized revenue."
            ],
            "table": {
                "caption": "Annual illustrative economics; total cost includes labor and enforcement, not collected tax",
                "headers": ["Scenario / route", "Gross billings", "Costs / fee assumption", "Net contribution / decision"],
                "rows": [
                    ["Conservative / 1 FT + 3 C", "$50,000", "$40,000 total costs", "$10,000 / 20%"],
                    ["Base / 1 FT + 3 C", "$425,000", "$265,625 total costs", "$159,375 / 37.5%"],
                    ["Scaled / 1 FT + 3 C", "$800,000", "$360,000 total costs", "$440,000 / 55%"],
                    ["Direct / illustrative $100 order", "$100 excluding tax", "3% + $0.30 = $3.30", "$96.70 before other costs; seller manages tax"],
                    ["Merchant of record / same order", "$100 excluding tax", "5% + $0.50 = $5.50", "$94.50 before other costs; verify contractual coverage"],
                    ["Route comparison", "1,000 identical orders", "$2,200 incremental provider fee", "Compare with actual tax administration savings; not a provider quote"]
                ]
            }
        },
    ],
    "pull_quote": "The durable digital product business keeps proof of permission, proof of price, and proof of ownership before it spends another dollar acquiring demand.",
    "diagram_id": "diag-04-mor-vs-direct-fee-bars",
    "action_checklist": [
        "Publish one keyword trigger and save request evidence.",
        "Load the three diagnostic messages into saved replies.",
        "Test checkout consent, cancellation, and retry suppression.",
        "Map seller identity, VAT treatment, and state nexus.",
        "Audit affiliate disclosures and supporting claim evidence.",
        "Archive source files and prepare one reviewed takedown."
    ],
    "statutory_citations": [
        {"title": "15 U.S.C. section 8403", "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section8403&num=0&edition=prelim", "relevance": "Online negative option disclosures, consent, and cancellation."},
        {"title": "17 U.S.C. section 512(c)", "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title17-section512&num=0&edition=prelim", "relevance": "Hosting safe harbor and notice elements."},
        {"title": "16 CFR Part 255", "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255", "relevance": "FTC endorsement and testimonial guidance."}
    ]
}
