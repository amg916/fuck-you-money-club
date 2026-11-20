CHAPTER_2 = {
    "id": "Q2", "chapter_id": "Q2", "chapter_number": 2, "question_number": 2,
    "slug": "who-pays-checkout-and-merchant-of-record",
    "question_prompt": "Who pays, why do they pay, and where does checkout capital sit?",
    "kicker": "Q2 / THE BIG MONEY PLAYBOOKS",
    "title": "Who Pays, Why They Pay & Where Checkout Capital Sits",
    "subtitle": "B2B Expense-Account Buyers vs. Prosumers, Merchant-of-Record (Paddle / Lemon Squeezy) vs. Direct Stripe Settlement & Reserve Mechanics",
    "layout_template": "executive_summary", "reading_time_minutes": 14,
    "executive_summary": "Sell saved work before selling inspiration. An expense-account buyer needs a usable output, an invoice, and a defensible reason to buy; an impulse buyer often needs only a persuasive promise. Those differences shape refunds, support, and acquisition cost. Checkout then decides who owes tax, who controls refunds, and when cash reaches payroll. Compare rails on contribution and available cash, not headline fees. This chapter connects buyer qualification, merchant-of-record economics, external web subscriptions, and genuine cohort scarcity to a small-team operating model with explicit costs and reserve assumptions.",
    "key_metrics": [
        {"label": "Conservative", "value": "$10,000 net", "context": "$50,000 gross; 20%", "note": "Modeled annual contribution"},
        {"label": "Base", "value": "$159,375 net", "context": "$425,000 gross; 37.5%", "note": "Modeled annual contribution"},
        {"label": "Scaled", "value": "$440,000 net", "context": "$800,000 gross; 55%", "note": "1 FT + 3 C; modeled, not observed"},
    ],
    "sections": [
        {
            "heading": "1. Sell an expense the buyer can defend",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Start with the person who owns a recurring task, not the broadest audience that clicks an advertisement. An operations lead buying a hiring SOP or reporting template can justify a purchase against hours saved this week. Ask which task repeats, who signs off on expenses, and what file must exist at the end. A $100 product that removes two hours of work valued at $75 per hour has a concrete buying story, although the customer must validate that saving. Provide a preview, supported file formats, license scope, and an invoice with the correct business details. Reimbursement is not automatic: distinguish someone buying on a company card from someone hoping their manager will repay a personal purchase after the work is complete.",
                "Treat lower refunds among qualified business buyers as a hypothesis to test, not a property bestowed by a business email address. These buyers may tolerate a higher price when the asset fits their workflow, yet demand more support when deployment is unclear. Track refunds by acquisition source, buyer role, product version, and reason over a fixed thirty day window. Separate an invoice correction from dissatisfaction and a duplicate charge from product failure. Prosumers occupy the middle: they buy tools for serious personal work but often spend their own money. Offer a focused sample rather than a sprawling bundle. Impulse consumer traffic may convert quickly and reverse quickly; compare retained contribution per visitor after refunds mature, not checkout conversion on launch day.",
                "Use discovery calls to turn vague interest into a measurable use case. Ask what the buyer did last time, how long it took, and which existing document they can safely describe without sharing confidential material. Then show the closest finished output and ask what would prevent adoption. Record objections about accuracy, editing effort, licensing, and internal review separately. A buyer who needs custom integration belongs in a service offer, not a download funnel whose margins assume self service. Price the template around a repeatable outcome and state what implementation remains with the customer. Build a refund reason ledger before scaling ads. Ten enthusiastic interviews are useful design evidence, but they are not a substitute for paid use and observed renewal behavior."
            ],
            "table": {
                "caption": "Buyer and scarcity failure detection",
                "headers": ["Naive Trap", "Detection Metric", "Durable Operator Fallback"],
                "rows": [
                    ["Business email means low refunds", "30-day refunds by buyer cohort", "Qualify task and preview output"],
                    ["Resetting countdown creates demand", "Timer resets while capacity is unchanged", "Publish actual seats and release dates"]
                ]
            }
        },
        {
            "heading": "2. Separate the seller, processor, and cash owner",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "A merchant of record is the contractual seller on covered transactions, not merely a nicer payment form. Paddle, Lemon Squeezy, and FastSpring can take responsibility for collecting and remitting applicable transaction taxes within their service scope. That does not move your corporate income tax, product promises, or every local obligation to the platform. Read the seller agreement for supported countries, restricted products, refund authority, dispute charges, and termination provisions. The customer pays the merchant of record, which later pays your business under its payout rules. With direct Stripe processing, your business generally remains the seller. Stripe Tax calculation does not by itself register your business everywhere or file every return. Assign each obligation to a named party before comparing the quoted percentages.",
                "Use 5% plus $0.50 as a standard merchant-of-record comparison assumption, not a universal contractual quote. Paddle and Lemon Squeezy advertise that starting structure, subject to product terms and possible additions; FastSpring pricing requires a commercial quote rather than an asserted identical public tariff. A direct domestic card model uses Stripe at 2.9% plus $0.30 and an assumed eligible Stripe Tax calculation charge of 0.5%. International cards, currency conversion, subscriptions, tax filing services, and negotiated rates can alter the bill. Gumroad direct sales use a 10% plus $0.50 platform fee with payment processing potentially additional; Discover uses 30% under its applicable terms. Apple and Google commonly fall within a 15% to 30% commission range, with program, territory, and transaction exceptions requiring review.",
                "Payment success is not spendable cash. Settlement first creates a platform balance; payout eligibility, a payout schedule, bank transit, and any reserve determine availability. A first payout can take longer than later payouts. A rolling reserve holds a percentage of eligible receipts for a stated period, while a fixed reserve or account review can restrict a different amount. Refund spikes, disputes, sudden volume growth, unusual ticket sizes, and delayed delivery can prompt review; no single trigger guarantees a particular hold. Maintain separate ledger balances for tax, unsettled proceeds, reserved funds, and available cash. Obtain the actual schedule from the account agreement and dashboard rather than relying on a generic comparison article. Fund payroll only from available cash after expected refunds and near-term operating commitments."
            ]
        },
        {
            "heading": "3. Acquire on the web without hiding the subscription",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "The mapped play web2app_quiz_subscription_billing_bypass describes mobile acquisition through a web diagnostic quiz followed by external Stripe or merchant-of-record checkout. Its durable version is a web purchase journey, not a trick that conceals charges or defeats app review. Advertise a specific diagnostic outcome, ask only questions needed to produce it, and show a useful result before offering the paid implementation asset. Tie the paid offer to the diagnosed task rather than manufacturing a frightening score to force conversion. Measure quiz completion, qualified checkout starts, paid activation, and retained subscriptions as separate events. A cheap quiz lead has no economic value until the buyer uses the product and stays. Preserve a clear distinction between an educational assessment and a professional diagnosis that the product cannot substantiate.",
                "A $100 order on the modeled 5% plus $0.50 merchant-of-record rail leaves $94.50 after that fee alone. That is the narrow meaning of retaining 94%+ net revenue in this play: payment-fee retention before refunds, advertising, support, tax effects, and additional charges. It is not a 94% contribution margin. Direct Stripe plus the modeled tax calculation leaves $96.30 before those other costs. Mobile app distribution remains a separate contract question. External links, alternative billing, entitlements, and applicable fees vary by storefront, territory, app category, and program. Check the rules for the actual distribution path rather than assuming a web purchase exempts every app transaction from store economics. If the permitted path is unclear, sell a complete browser product while evaluating a supported app implementation.",
                "For recurring offers, put the price, billing interval, trial conversion terms, and cancellation method where the buyer makes the purchase decision. A quiz completion is not permission to charge a card. Section 8403 of title 15 requires clear material disclosures before obtaining billing information, express informed consent before charging, and a simple mechanism to stop recurring charges for covered internet negative-option sales. Implement cancellation in the account flow and test it on mobile as carefully as checkout. Record the offer version and purchase event without collecting unnecessary sensitive data. Distinguish cancellation of future renewals from a refund of an earlier charge. Track first renewal failures and immediate cancellations by creative; a misleading advertisement can look efficient until the first billing cycle exposes the mismatch."
            ],
            "sop_steps": [
                {"step": 1, "title": "Define the result", "action": "Write one useful quiz outcome.", "detail": "Connect each question to an actual product decision."},
                {"step": 2, "title": "Map the purchase path", "action": "Document web and app entry points.", "detail": "Check storefront and territory terms for each path."},
                {"step": 3, "title": "Test the lifecycle", "action": "Exercise purchase, renewal, refund, and cancellation.", "detail": "Confirm receipts and entitlement changes match payment events."},
                {"step": 4, "title": "Reconcile a cohort", "action": "Compare mature receipts with acquisition and support costs.", "detail": "Expand only when contribution and available cash both support spending."}
            ]
        },
        {
            "heading": "4. Allocate real capacity instead of manufacturing urgency",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "The mapped play verified_fan_ticketing_and_drop_allocation_farming belongs here as a lesson in legitimate allocation mechanics, not automated hoarding or evasion of another platform's purchase limits. Apply it to your own product cohort: define how many customers the team can actually onboard, establish eligibility, and allocate seats through a documented waitlist. Do not create duplicate identities, misrepresent fan status, or promise third-party tickets you do not control. For a template workshop, capacity may be the number of files an expert can review, not the number of downloads a server can deliver. A download is usually abundant; individualized attention is scarce. State which component is capped so buyers understand what expires and what remains available after a cohort fills. That distinction protects both trust and staffing economics.",
                "Calculate capacity from service minutes before writing a launch email. Suppose three contractors can each devote four hours per week to reviews, giving twelve hours in total. At thirty minutes per review, theoretical capacity is twenty-four reviews; reserve four for rework and sell twenty weekly review seats. Those are illustrative allocations, not a staffing benchmark. Keep the download available separately if its marginal delivery cost is low. Order the waitlist by a published timestamp rule or use a disclosed lottery when fairness matters more than speed. Give selected buyers a real acceptance deadline and release unused seats to the next eligible person. Maintain an allocation log showing offered, accepted, expired, and refunded seats so support can resolve disputes without inventing exceptions or quietly overselling capacity.",
                "A countdown is truthful only when the stated consequence happens. If a cohort closes Friday because onboarding starts Monday, close it Friday and publish the next intake rather than resetting the clock for every visitor. If a seat is reserved for fifteen minutes during checkout, release it when the reservation expires and avoid counting abandoned carts as completed sales. Show availability from the same inventory record used to accept orders. A waitlist should not silently become a paid subscription, and an allocation email should distinguish an invitation from a confirmed purchase. Watch complaints about urgency alongside conversion metrics. The operational test is simple: could a support person explain the deadline and capacity number using staffing records and order history? If not, remove the claim and sell the actual benefit.",
            ],
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Capacity must survive reconciliation",
                "body": "Open the next cohort only when delivery time and collected cash support the seats offered.",
                "items": ["Name the scarce service component.", "Publish the allocation and expiry rules.", "Reconcile seat inventory with paid orders.", "Keep an accurate next-intake date."]
            }
        },
        {
            "heading": "5. Price the rail, then fund the cash cycle",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                "Read the rail table as a controlled $100 tax-exclusive order comparison, not a live quote. Assume a domestic card, no currency conversion, no refund, no dispute, and no separately priced subscription tooling. For direct Stripe, assume the entire $100 is eligible for the 0.5% tax calculation charge. For Gumroad direct, show both the platform fee and an illustrative 2.9% plus $0.30 processing layer rather than hiding processing inside the headline rate. Store commissions are simplified percentages; taxes and contractual commission bases can change the actual settlement. Taxes collected from the buyer are liabilities, not revenue. Wayfair removed the physical-presence requirement for state sales-tax nexus, but it did not establish one nationwide threshold. EU VAT analysis likewise depends on customer status, location, and the applicable supply rules.",
                "Model reserves as restricted cash rather than an additional processing expense. On the direct Stripe illustration, $100 less $3.70 in modeled fees leaves $96.30 before other deductions. An illustrative 10% reserve applied to gross receipts restricts another $10, leaving $86.30 initially available before payout timing and other liabilities. The $10 remains an asset subject to release or application against obligations; it is not lost margin merely because access is delayed. If eligible monthly billings are $40,000 and that reserve retains three monthly cohorts, approximately $12,000 can remain tied up at steady volume. This is a stress case, not a stated Stripe policy. Build a weekly cash forecast that includes opening available cash, scheduled releases, refunds, contractor invoices, advertising, and taxes payable, with no borrowing from customer tax balances.",
                "The annual scenarios use gross product billings excluding transaction taxes and modeled costs that include refund leakage. Conservative means $50,000 gross less $40,000 costs, yielding $10,000 net at 20%. Base means $425,000 less $265,625, yielding $159,375 at 37.5%. Scaled means $800,000 less $360,000, yielding $440,000 at 55%. These are planning cases, not observed results or inevitable scale economies. The operating shape is 1 FT + 3 C: one full-time founder and three contractors with variable hours. The cost bridge includes contractor spend but excludes founder compensation and income taxes, so net here means modeled operating contribution before those items, not personal take-home profit. At conservative revenue, a fully paid full-time role is not funded. Insert the founder's required salary before deciding whether this business supports their livelihood."
            ],
            "table": {
                "caption": "$100 order: modeled take rate, fee retention, and payout exposure; verify account terms",
                "headers": ["Rail", "Fee assumptions", "Fee / retained", "Reserve and payout mechanics"],
                "rows": [
                    ["Paddle MoR", "5% + $0.50 baseline", "$5.50 / $94.50", "Contractual payout schedule; risk holds possible; additions excluded"],
                    ["Lemon Squeezy MoR", "5% + $0.50 baseline", "$5.50 / $94.50", "Holding period and payout cycle; additions and payout fees excluded"],
                    ["FastSpring MoR", "5% + $0.50 comparison assumption only", "$5.50 / $94.50 modeled", "Obtain actual quote, payout cycle, and reserve terms"],
                    ["Stripe direct + Stripe Tax", "2.9% + $0.30 + 0.5%", "$3.70 / $96.30", "Account-specific settlement; rolling or fixed reserves possible, not universal"],
                    ["Gumroad direct", "10% + $0.50; assumed processing $3.20 extra", "$13.70 / $86.30", "Eligibility, holding period, review, and payout method govern availability"],
                    ["Gumroad Discover", "30% inclusive platform comparison", "$30.00 / $70.00", "Marketplace payout eligibility and account review still apply"],
                    ["Apple in-app", "15% to 30% scenario range", "$15-$30 / $85-$70", "Program-specific fiscal payout cycle and adjustments; exceptions apply"],
                    ["Google in-app", "15% to 30% scenario range", "$15-$30 / $85-$70", "Program-specific payment cycle and adjustments; exceptions apply"]
                ]
            },
        },
    ],
    "pull_quote": "A cheaper checkout is not a better business when the savings disappear into refunds, tax administration, or cash you cannot yet withdraw.",
    "diagram_id": "diag-04-mor-vs-direct-fee-bars",
    "action_checklist": [
        "Interview five buyers about their last recurring task.",
        "Tag orders by buyer role and acquisition source.",
        "Obtain written rail pricing and payout terms.",
        "Reconcile available, pending, and reserved balances.",
        "Test cancellation and renewal disclosures end to end.",
        "Publish cohort capacity and build the annual cost bridge."
    ],
    "statutory_citations": [
        {"title": "South Dakota v. Wayfair, 585 U.S. 162 (2018)", "url": "https://www.supremecourt.gov/opinions/17pdf/17-494_j4el.pdf", "relevance": "Physical presence is not required for state sales-tax nexus; state rules still govern."},
        {"title": "EU Council Directive 2006/112/EC", "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0112", "relevance": "EU VAT framework; customer status and place-of-supply rules matter for digital sales."},
        {"title": "15 U.S.C. section 8403", "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section8403&num=0&edition=prelim", "relevance": "Online negative-option sales require material disclosures, express informed consent, and simple stopping mechanisms."}
    ]
}
