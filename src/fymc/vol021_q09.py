from __future__ import annotations

CHAPTER_9 = {
    "id": "Q9",
    "chapter_id": "Q9",
    "chapter_number": 9,
    "question_number": 9,
    "slug": "contracts-statutory-guardrails-licensing-outreach-scripts",
    "question_prompt": "Which federal/state statutes, licensing boundaries, contract clauses, and compliant outreach scripts govern automated e-commerce?",
    "kicker": "Q9 / THE BIG MONEY PLAYBOOKS",
    "title": "Contracts, Statutory Guardrails, Licensing & Outreach Scripts",
    "subtitle": "Authorized-Dealer Agreements, 3PL Custody, CPSC Reporting, Customs Entry, Sales-Tax Nexus, and Permissioned Coupon Attribution",
    "layout_template": "legal_compliance_notes",
    "reading_time_minutes": 14,
    "executive_summary": "Candidate #28, Automated E-Commerce, ranks #21 with a 85/100 Money-to-Manpower Score across 18 mapped plays. This chapter translates product safety, import duties, sales taxes, privacy, consumer protection, and partner attribution into executable contracts and operating records. The model recognizes retail sales net of refunds, with goods, fulfillment, and advertising included in margin. Annual owner net profit is $12,500 Conservative, $129,375 Base, and $360,000 Scaled. Protect those outcomes through authorized inventory, documented shipment promises, jurisdiction-specific registrations, defensible outreach, and recoverable supplier obligations. The checkout-promo interception play earns attribution through real merchant offers and deliberate shopper clicks, never hidden redirects. Use the matrices, scripts, and verification steps before releasing inventory, campaigns, or partner payouts.",
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": "Annual retail revenue net of refunds; goods, fulfillment, and advertising included in margin",
            "note": "5% net margin; $12,500 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$1,125,000",
            "context": "Annual retail revenue net of refunds; goods, fulfillment, and advertising included in margin",
            "note": "11.5% net margin; $129,375 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$2,000,000",
            "context": "Annual retail revenue net of refunds; goods, fulfillment, and advertising included in margin",
            "note": "18% net margin; $360,000 annual owner net profit; 3 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Establish product, importer, and state-level operating authority",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Start with a sellable-SKU dossier, not a supplier assurance that everything is certified. For each SKU, record the legal manufacturer, importer, country of origin, intended user, materials, claims, applicable standards, test reports, warnings, and lot identifiers. Under 15 U.S.C. § 2063, products subject to applicable consumer product safety rules require the relevant certification; children's products generally require testing by a CPSC-accepted third-party laboratory, subject to applicable exceptions. A CE marking alone does not establish satisfaction of United States requirements. Under 15 U.S.C. § 2064(b), manufacturers, importers, distributors, and retailers have immediate reporting duties when specified information reasonably supports a reportable product problem. Configure returns tracking to surface overheating, choking, injury, and repeated structural failures separately from ordinary buyer remorse. Customer support must escalate those signals without waiting for a monthly refund dashboard. Quarantine affected lots in the 3PL warehouse management system, preserve complaints and photographs, and obtain a documented reporting assessment. Supplier indemnity can fund recovery later, but it does not transfer the retailer's own statutory responsibilities. Maintain purchaser traceability sufficient to execute a targeted recall without exporting the entire customer database to every vendor.",
                "Treat importation as a distinct operating function even when a supplier offers delivered pricing. Under 19 U.S.C. § 1484, the importer of record carries reasonable-care responsibilities for entry information, classification, and valuation; a customs broker does not absorb those duties merely by filing paperwork. Name the importer in the purchase order, align Incoterms with the actual transaction, and identify who pays duties, brokerage, examinations, storage, and corrective entries. Obtain a classification rationale and origin support before approving landed-cost assumptions. Prefer a CBP binding ruling under 19 CFR Part 177 when material classification uncertainty would change the business case. Do not build contribution margin around an assumed low-value entry exemption: eligibility, country treatment, and current tariff measures require transaction-specific verification. A $4 unexpected landed-cost increase across 5,000 units removes $20,000 of contribution before overhead. Require documentary origin evidence rather than relabeling instructions, and reject supplier requests to understate value. FDA-regulated foods, cosmetics, supplements, and medical devices need separate product and establishment analyses; FCC equipment authorization can apply to radio-frequency devices. Keep those categories outside the initial assortment until the relevant specialist has resolved each SKU's actual requirements.",
                "Build a state matrix around physical inventory, employees, direct sales, marketplace sales, and product category. Inventory stored by a 3PL can create physical nexus independently of a state's remote-seller economic threshold. Marketplace collection does not automatically resolve direct-store obligations, registration questions, income-based taxes, or every filing requirement. For California, analyze Revenue and Taxation Code § 6203 and the applicable marketplace-facilitator provisions rather than copying another state's threshold. Track economic thresholds using each jurisdiction's prescribed measurement period and inclusions; some states have removed transaction-count tests while others retain different tests. Shopify Tax, Avalara, or TaxJar can assist calculation, but someone must own registration, exemption evidence, filing calendars, and reconciliation. A resale certificate supports qualifying inventory purchases; it is neither a universal business license nor permission to sell restricted products. Check local business licensing, assumed-name filings, and state seller permits separately. California Proposition 65 requires an exposure-based assessment where applicable, not automatic warnings on every imported item. Food, alcohol, tobacco, batteries, and other regulated categories can add permits, shipping restrictions, or stewardship duties. Record the source, review date, responsible person, and approved selling geography so order routing can block unsupported destinations before payment capture.",
            ],
            "table": {
                "caption": "SKU, Importer, and Jurisdiction Evidence Matrix",
                "headers": [
                    "Operating boundary",
                    "Primary authority or requirement",
                    "Required operating evidence",
                    "Failure response and accountable owner",
                ],
                "rows": [
                    [
                        "Children's merchandise entering the authorized online retail assortment",
                        "15 U.S.C. § 2063 establishes applicable testing and certification requirements",
                        "Retain applicable certificates, accepted laboratory reports, and identifiable production lots",
                        "Merchandising blocks affected SKUs until product specialists resolve missing evidence",
                    ],
                    [
                        "Injury complaints and recurring defects across fulfilled product lots",
                        "15 U.S.C. § 2064(b) imposes reporting duties on covered businesses",
                        "Preserve complaint chronology, lot identifiers, photographs, and documented escalation decisions",
                        "Safety lead quarantines inventory and promptly evaluates required CPSC reporting",
                    ],
                    [
                        "Imported inventory purchased through brokers or overseas trading companies",
                        "19 U.S.C. § 1484 assigns importer reasonable-care responsibilities for entries",
                        "Keep classification rationale, valuation support, origin records, and entry documentation",
                        "Import owner resolves discrepancies before releasing affected purchase commitments",
                    ],
                    [
                        "California inventory placement and direct sales into customer destinations",
                        "California Revenue and Taxation Code § 6203 addresses retailer collection nexus",
                        "Maintain warehouse locations, sales measurements, registrations, and direct-channel tax reconciliation",
                        "Tax owner corrects collection settings and addresses historical filing exposure",
                    ],
                    [
                        "Products creating potentially regulated California chemical exposure during use",
                        "California Health and Safety Code § 25249.6 governs covered exposure warnings",
                        "Retain exposure assessment, applicable exemption analysis, and warning placement decisions",
                        "Product owner restricts California sales while unresolved exposure questions remain",
                    ],
                    [
                        "Specialized categories expanding beyond ordinary unregulated general merchandise inventory",
                        "FDA statutes, FCC rules, and state category laws require separate assessment",
                        "Document category-specific permits, labeling analysis, testing evidence, and shipping limitations",
                        "Assortment owner excludes unsupported categories until required operating capability exists",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four verifications before a SKU becomes purchasable",
                "body": "A storefront toggle must reflect completed evidence, not a vendor's confidence or an approaching advertising launch.",
                "items": [
                    "Match the exact SKU and production lot to applicable certificates, laboratory reports, warnings, and authorized-dealer evidence.",
                    "Identify the importer of record and verify classification, origin, current duties, and landed-cost sensitivity with the customs specialist.",
                    "Confirm selling jurisdictions, 3PL inventory locations, required registrations, tax configuration, and category-specific shipping restrictions.",
                    "Run a test order, delayed-shipment notice, refund, lot quarantine, and purchaser export using restricted staff access.",
                ],
            },
        },
        {
            "heading": "2. Contract for recoverable failures across suppliers, warehouses, and partners",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Use a contract stack that follows custody and responsibility: supplier purchase terms, authorized-dealer permission, 3PL services agreement, customer-facing terms, and separate marketing-partner terms. Define scope through named SKUs, permitted channels, territories, service hours, integration responsibilities, and measurable exceptions. An authorized-dealer letter should state whether Amazon, Walmart Marketplace, Google Shopping, and independent storefront sales are permitted; purchasing genuine stock does not itself grant access to every brand program, image library, or marketplace entitlement. Specify when title and risk of loss pass rather than treating those concepts as interchangeable. UCC §§ 2-313, 2-314, and 2-316 provide a framework for express warranties, merchantability, and warranty exclusions, subject to the governing state's enacted text and applicable consumer rules. If offering written consumer warranties, assess the Magnuson-Moss Warranty Act and FTC warranty disclosure rules, including pre-sale availability. Require the supplier to preserve traceable lots, notify the retailer of safety developments, support recall execution, and provide relevant insurance evidence. Set inspection periods that accommodate latent defects instead of accepting a two-day window as the exclusive remedy. Document authorized substitutes explicitly; an automated reorder must never silently replace a tested product with a visually similar variant.",
                "Turn the 3PL agreement into an auditable event ledger. Define receipt at carton and unit level, inventory accuracy measurement, cutoff times, carrier handoff evidence, return grading, quarantine handling, and the treatment of inventory discrepancies. A shipping label is not proof of carrier acceptance. Tie storage, pick-pack, packaging, postage, returns, and project fees to enumerated events with accessible source records. If the warehouse assesses $3 per return on 600 monthly returns, the invoice should expose the 600 return identifiers supporting $1,800, with duplicate events contestable. Require advance notice for fee changes and specify how peak surcharges interact with quoted service rates. UCC Article 7, as enacted locally, can affect warehouse receipts, liens, and limitations of liability; obtain a realistic exit process before inventory is locked behind a payment dispute. A cap based on warehouse fees may be far below the replacement value of destroyed inventory. Negotiate separately for physical loss, data incidents, confidentiality breaches, and deliberate misconduct, with insurance aligned to the actual exposures. Define claims deadlines, valuation methodology, salvage rights, and evidence access. Preserve alternate fulfillment capability for high-contribution SKUs rather than relying solely on service credits after repeated missed shipments.",
                "Marketing and affiliate contracts need the same precision as custody agreements. Define a payable conversion as an approved, attributable order after the agreed refund and fraud review period, with an explicit adjustment process for later returns. List approved codes, eligible products, excluded purchasers, attribution window, deduplication hierarchy, brand-bidding restrictions, cashback rules, and required disclosures. A narrowly drafted anti-circumvention clause can protect documented introductions or agreed attribution; it should not claim unrelated future revenue or prevent customers from exercising ordinary choice. Specify duration, covered counterparties, evidence standards, and proportionate remedies. State which party owns product copy, commissioned photography, audience lists, event schemas, and exported performance reports. Grant only the data access required for reconciliation and prohibit repurposing customer records for an independent advertising audience without an appropriate basis. Include incident notification, subprocessors, retention, deletion, and migration assistance. Select governing law, venue, escalation procedures, and dispute mechanisms after reviewing enforceability in relevant jurisdictions; consumer arbitration and class-action terms require separate scrutiny from business-to-business terms. Maintain affirmative acceptance and version records for customer terms. A supplier contract cannot erase consumer remedies, and a liability cap should never be presented internally as permission to ignore a known safety defect.",
            ],
            "table": {
                "caption": "Six-Clause Contract Checklist for a Lean 3PL-Backed Retailer",
                "headers": [
                    "Clause to negotiate",
                    "Concrete drafting instruction",
                    "Evidence supporting enforcement",
                    "Fallback when agreement remains incomplete",
                ],
                "rows": [
                    [
                        "Scope covering authorized products, channels, territories, and service responsibilities",
                        "List permitted marketplaces, exact deliverables, excluded tasks, and change procedures",
                        "Attach dealer authorization, SKU schedule, integration map, and signed service exhibits",
                        "Restrict trading to documented permissions and exclude unsupported marketplace listings",
                    ],
                    [
                        "Fee trigger tied to independently verifiable fulfillment or conversion events",
                        "Define billable events, reversal periods, duplicate handling, and dispute deadlines",
                        "Retain warehouse scans, approved orders, refund events, and versioned rate schedules",
                        "Hold disputed amounts under agreed procedures while paying undisputed balances",
                    ],
                    [
                        "Anti-circumvention protecting documented introductions without claiming unrelated future transactions",
                        "Limit covered counterparties, protected activities, contractual duration, and proportionate remedies",
                        "Preserve introduction records, attribution logs, partner approvals, and dated correspondence",
                        "Use transparent referral reporting rather than expansive restrictions on ordinary commerce",
                    ],
                    [
                        "Liability allocation reflecting inventory value, safety exposure, and customer information",
                        "Negotiate meaningful caps, appropriate exceptions, indemnity procedures, and insurance requirements",
                        "Compare policy terms, inventory valuations, claim scenarios, and insurer endorsements",
                        "Reduce inventory concentration or select counterparties offering recoverable risk allocation",
                    ],
                    [
                        "Dispute resolution providing usable remedies before operational disruption becomes irreversible",
                        "Specify governing law, escalation owners, forum, deadlines, and continuity obligations",
                        "Maintain signed versions, acceptance records, notices, and event-level dispute evidence",
                        "Preserve alternate fulfillment and agreed inventory release rights during contested invoices",
                    ],
                    [
                        "Intellectual property and data ownership surviving termination and platform migration",
                        "Allocate content rights, permitted processing, export formats, deletion, and transition assistance",
                        "Keep asset licenses, processing schedules, access logs, and successful export tests",
                        "Avoid exclusive dependencies where customer records or essential creative cannot migrate",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Negotiate against the failure invoice, not the sales presentation",
                "body": "Experienced operators attach real transaction samples to contract discussions so vague promises become measurable obligations.",
                "items": [
                    "Give competing 3PLs the same thirty-order basket, including oversized parcels and returns, then reconcile every quoted surcharge.",
                    "Request a warehouse inventory-release drill before committing the full assortment; measure export usability and transfer lead time.",
                    "Attach an approved coupon landing-page screenshot and attribution sequence to the partner agreement, then version subsequent changes.",
                    "Model a lost pallet and a small recall against contract caps and insurance deductibles before accepting supplier pricing.",
                ],
            },
        },
        {
            "heading": "3. Earn outreach permission and checkout attribution without manufactured claims",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Design automated retention around the message's actual purpose and channel. Commercial email, including business-to-business prospecting, falls within CAN-SPAM requirements under 15 U.S.C. § 7704: accurate routing information, nondeceptive subjects, required identification, a valid postal address, and a functioning opt-out mechanism. Honor opt-outs within ten business days and preserve suppression through CRM migrations; do not mistake a purchased list for proof that every address is usable. Separate genuinely transactional messages from promotional content according to the primary-purpose rules. SMS marketing requires a different analysis under the TCPA and 47 CFR § 64.1200, including the technology used, message content, applicable consent standards, revocation, and federal and state restrictions. For automated marketing texts, use a separately documented opt-in with clear seller identification rather than assuming an email signup authorizes texting. Retain the exact language presented, timestamp, number, source, and withdrawal events. Configure Klaviyo or an equivalent system to prevent promotional sends to suppressed contacts, and test that a Shopify customer update cannot reactivate them. State mini-TCPA statutes and quiet-hour requirements can be stricter than the federal baseline. Launch only where the channel's jurisdictional rules and consent evidence are operationally supported, with email as a separate channel rather than a workaround for SMS refusal.",
                "Underwrite the mapped TRACK_2 play coupon_checkout_tab_under_injection as earned deal-page attribution, not permission to manipulate a shopper's browser. Its usable mechanism is a real merchant-approved discount, a clearly described cashback incentive where applicable, and a deliberate click that initiates the disclosed partner link. Never use tab-unders, forced redirects, hidden tracking requests, or fake coupon buttons; those mechanisms can violate network terms and destroy partner access. Show eligible products, exclusions, expiration, and whether cashback depends on order approval. Put a plain-language commission disclosure near the recommendation and link, applying FTC Act § 5 and the Endorsement Guides in 16 CFR Part 255. For an illustrative independent affiliate transaction, an eligible $72 merchant sale at 8% commission produces $5.76 of affiliate revenue. Subtract $2 cashback, $1.50 acquisition expense, and a $0.26 reversal reserve to leave $2 contribution before overhead. The $72 merchant sale is not affiliate revenue, and this illustration does not supplement the canonical retail scorecard. If the merchant denies paid search or exclusive codes, stop that placement and negotiate an approved offer. Query demand alone never creates trademark permission, an attribution entitlement, or authority to advertise an unavailable discount.",
                "Build privacy controls around actual data movement: storefront, analytics, advertising pixels, help desk, email platform, 3PL, payment provider, and affiliate network. Identify the information each recipient receives, the purpose, retention period, contract role, and downstream uses. California Civil Code § 1798.100 and related provisions impose duties on covered businesses; assess applicability rather than declaring every small retailer covered or exempt. Where sale or sharing rules apply, implement the required opt-out mechanisms and recognize applicable opt-out preference signals under California regulations. A server-side advertising integration does not remove these obligations. Other state privacy laws differ in thresholds, exemptions, sensitive-data treatment, and universal opt-out requirements, so keep a jurisdiction-specific configuration register. Minimize fulfillment exports to information actually needed to deliver orders and resolve returns. Do not send full payment details or broad browsing histories to a warehouse. Review chat-session recording, precise location, children's data, and health-related purchase inferences separately because additional rules may apply. Require role-based access, multifactor authentication, vendor offboarding, and tested deletion propagation. Privacy promises must match the event stream in production: compare browser network requests and server logs against the published notice after every material marketing change, not merely at initial launch.",
            ],
            "table": {
                "caption": "Outreach, Coupon Attribution, and Privacy Control Matrix",
                "headers": [
                    "Channel or mechanism",
                    "Required operator behavior",
                    "Proof retained for review",
                    "Specific failure fallback",
                ],
                "rows": [
                    [
                        "Commercial email prospecting directed toward authorized merchants and existing customers",
                        "Use truthful subjects, postal identification, functional unsubscribe, and timely suppression",
                        "Retain message versions, audience origin, suppression events, and send-provider records",
                        "Pause the affected audience when opt-out propagation or identity checks fail",
                    ],
                    [
                        "Automated promotional text messages supporting repeat purchases and replenishment reminders",
                        "Evaluate TCPA coverage and state rules; capture appropriate separate marketing permission",
                        "Preserve displayed opt-in language, recipient number, timestamp, source, and revocations",
                        "Disable promotional texts where permission evidence or jurisdictional support is deficient",
                    ],
                    [
                        "Merchant-approved coupon pages attracting shoppers searching for checkout discount codes",
                        "Publish genuine eligible offers and require deliberate user-initiated partner link activation",
                        "Keep merchant approval, offer terms, landing-page versions, and attributable click records",
                        "Remove expired offers and negotiate authentic exclusive discounts before resuming promotion",
                    ],
                    [
                        "Cashback incentives attached to approved affiliate purchases and refund review periods",
                        "Disclose eligibility, payout timing, commission relationship, exclusions, and reversal treatment",
                        "Reconcile approved commissions, cashback obligations, refunds, and actual customer payouts",
                        "Suspend new incentives when expected commission no longer funds promised customer payments",
                    ],
                    [
                        "Advertising integrations receiving customer identifiers through browser and server-side events",
                        "Assess covered data uses and enforce applicable opt-out and contractual restrictions",
                        "Maintain destination inventory, preference tests, processor terms, and event payload samples",
                        "Disable unsupported destinations until preference handling and permitted processing are verified",
                    ],
                    [
                        "Customer reviews and creator endorsements used inside acquisition or retention campaigns",
                        "Disclose material relationships and avoid fabricated reviews or misleading testimonial claims",
                        "Preserve authentic submissions, compensation records, permissions, and claim substantiation files",
                        "Remove unsupported endorsements without conditioning refunds on removal of honest criticism",
                    ],
                ],
            },
        },
        {
            "heading": "4. Deploy exact scripts and reconcile every promise to the scorecard",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Use this merchant discovery script verbatim: 'We operate a 3PL-backed online store and publish merchant-approved offers. Before discussing volume, which products, territories, and sales channels can you authorize in writing? Who owns the product certificates, recall communications, and importer records? Can we review a sample order, refund, and inventory feed together? For any coupon partnership, we require a genuine offer, visible eligibility terms, a disclosed commission relationship, and attribution initiated by the shopper's own click. We do not use hidden redirects, automatic tracking activation, or invented discounts. How do you define an approved conversion, handle returned orders, and resolve overlapping partner claims? Please send your dealer requirements and proposed commercial terms before we publish anything.' Follow with this warehouse discovery script: 'Please price receiving, storage, pick-pack, packaging, postage, returns, quarantine, and inventory removal separately. Show the source event behind each charge and a carrier acceptance record. What happens to our inventory and customer export if we dispute an invoice or terminate?' These questions expose authorization, custody, billing, and exit weaknesses before integration work creates switching costs. Record the counterparty's answers in the contract schedule rather than treating a sales-call recording as a substitute for negotiated obligations.",
                "For warm partner outreach, use this message only from an account whose signature supplies the actual sender identity and valid postal address: 'Subject: Authorized dealer and genuine coupon partnership inquiry. We are exploring an authorized retail relationship for your products. We would like to confirm channel permissions, product documentation, fulfillment expectations, and whether you offer a genuine exclusive code. Any partner link would be clearly disclosed and activated by the shopper. If you handle dealer partnerships, may we send our proposed operating terms? If another team owns this, a referral would help. To stop partnership messages from us, reply unsubscribe or use the unsubscribe link below.' Configure the working link and business identification before sending; the script alone does not satisfy channel requirements. For checkout-facing disclosure, use: 'We may earn a commission if you buy through this link. Review the displayed offer terms before continuing to the merchant.' Add the actual discount, exclusions, expiration, and cashback terms beside it. For a shipment problem, use: 'Your order will miss the promised shipping date. Please review the revised date shown here. You may cancel for a full refund using the cancellation link.' Configure the accompanying notice, customer-choice process, and refund timing to the specific delay under 16 CFR Part 435; one generic message cannot replace the rule's consent requirements.",
                "Reconcile contract promises to the canonical retail model before increasing acquisition spend. Conservative revenue of $250,000 at 5% yields $12,500 annual owner net profit and an implied $237,500 total cost envelope with 2 FT + 3 C. Base revenue of $1,125,000 at 11.5% yields $129,375 profit and $995,625 costs with 2 FT + 3 C. Scaled revenue of $2,000,000 at 18% yields $360,000 profit and $1,640,000 costs with 3 FT + 4 C. Those revenue figures represent retail sales net of refunds; do not add marketplace transaction volume, collected sales tax, or affiliate merchant sales. As a separate order-level illustration, $100 sales less $5 expected refunds gives $95 recognized revenue; subtract $32 goods, $10 fulfillment, $3 processing, $20 advertising, and $4 return handling for $26 contribution before overhead. Avoid subtracting the same refund twice, and validate the simplified cost assumptions against actual returned-stock recovery. Startup capital of $15,000–$80,000 and monthly opex of $4,000–$25,000 describe planning ranges, not replacements for the scenario cost envelopes. Order routing, inventory alerts, and returns tracking protect these economics only when exception owners resolve stockouts, ad-cost inflation, product liability, and broken customer promises before automation multiplies them.",
            ],
            "table": {
                "caption": "Pre-Launch Evidence and Scenario Reconciliation Register",
                "headers": [
                    "Control or financial case",
                    "Required calculation or operating proof",
                    "Named ownership and review cadence",
                    "Release condition or corrective action",
                ],
                "rows": [
                    [
                        "Conservative retail case with two full-time staff and three contractors",
                        "$250,000 revenue minus $237,500 costs equals $12,500 profit at 5%",
                        "Owner reviews monthly results against the complete annual cost envelope",
                        "Reduce discretionary spending when realized contribution cannot fund planned operating costs",
                    ],
                    [
                        "Base retail case with two full-time staff and three contractors",
                        "$1,125,000 revenue minus $995,625 costs equals $129,375 profit at 11.5%",
                        "Owner reconciles goods, fulfillment, advertising, and remaining costs every month",
                        "Scale acquisition only after refund-adjusted contribution supports the planned margin",
                    ],
                    [
                        "Scaled retail case with three full-time staff and four contractors",
                        "$2,000,000 revenue minus $1,640,000 costs equals $360,000 profit at 18%",
                        "Owner reviews concentration, capacity, claims, and margin before volume increases",
                        "Reprice or remove products whose complete costs break portfolio economics",
                    ],
                    [
                        "Shipment promises displayed across storefront, confirmation, and warehouse routing systems",
                        "Test promised dates against available stock and actual carrier acceptance evidence",
                        "Operations lead reviews aging orders daily and escalating exceptions immediately",
                        "Send required delay notices and process cancellations within applicable rule deadlines",
                    ],
                    [
                        "Marketing launch covering merchant codes, attribution, disclosures, and suppression controls",
                        "Verify genuine offers, deliberate click activation, message identity, and working opt-outs",
                        "Growth lead records campaign evidence before launch and after material changes",
                        "Stop affected campaigns when permission, offer validity, or suppression tests fail",
                    ],
                    [
                        "Customer data access spanning storefront, warehouse, support, and marketing vendors",
                        "Complete least-privilege review, destination inventory, deletion test, and export recovery exercise",
                        "Data owner reviews access changes and validates recurring vendor control checks",
                        "Remove excess permissions and disable unverified destinations before restoring integrations",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Assemble the operating evidence packet",
                    "action": "Create one versioned packet per supplier, SKU family, and selling jurisdiction.",
                    "detail": "Include dealer permissions, applicable product evidence, importer records, tax analysis, insurance documents, and assigned exception owners.",
                },
                {
                    "step": 2,
                    "title": "Execute contracts against sample transactions",
                    "action": "Walk a purchase, fulfillment event, return, inventory loss, and partner conversion through the proposed terms.",
                    "detail": "Confirm custody, billable triggers, liability allocation, data rights, dispute handling, and usable termination procedures before committing inventory.",
                },
                {
                    "step": 3,
                    "title": "Test the customer and partner journeys",
                    "action": "Run real sandbox workflows for order promises, delays, refunds, coupon clicks, marketing opt-outs, and privacy preferences.",
                    "detail": "Save screenshots and event records; disable any integration that creates undisclosed attribution, unsupported data transfers, or failed suppression.",
                },
                {
                    "step": 4,
                    "title": "Reconcile outcomes and retire broken automation",
                    "action": "Match sales, refunds, fees, advertising, fulfillment, and partner obligations to the selected canonical scenario.",
                    "detail": "Review exception trends weekly, assign corrective dates, and stop affected SKUs or campaigns when evidence or contribution deteriorates.",
                },
            ],
        },
    ],
    "pull_quote": "Automate the evidence behind the promise before you automate the volume of promises.",
    "diagram_id": "diag-05",
    "action_checklist": [
        "Build a SKU dossier linking dealer authorization, applicable safety evidence, lot traceability, warnings, and recall escalation ownership.",
        "Document importer responsibility, current landed costs, warehouse-state nexus, seller registrations, and category-specific selling restrictions.",
        "Negotiate supplier, 3PL, and partner terms covering scope, billable events, anti-circumvention, liability, disputes, and IP/data ownership.",
        "Publish only genuine merchant-approved coupon offers with nearby disclosures, explicit shopper click attribution, and reconciled cashback obligations.",
        "Test shipment-delay choices, refunds, email suppression, SMS permission records, privacy preferences, and vendor access before campaign activation.",
        "Reconcile retail revenue net of refunds to the exact Conservative, Base, or Scaled profit and staffing case without importing affiliate merchant sales.",
    ],
    "statutory_citations": [
        {
            "title": "15 U.S.C. § 2063 — Product safety certification and testing",
            "url": "https://www.law.cornell.edu/uscode/text/15/2063",
            "relevance": "Determine applicable certification, testing, and supporting evidence requirements for regulated consumer products.",
        },
        {
            "title": "15 U.S.C. § 2064 — Substantial product hazards",
            "url": "https://www.law.cornell.edu/uscode/text/15/2064",
            "relevance": "Establish prompt escalation and reporting assessment for information indicating potentially reportable product problems.",
        },
        {
            "title": "19 U.S.C. § 1484 — Entry of merchandise",
            "url": "https://www.law.cornell.edu/uscode/text/19/1484",
            "relevance": "Assign importer-of-record ownership for reasonable care in classification, valuation, and entry information.",
        },
        {
            "title": "19 CFR Part 177 — Administrative rulings",
            "url": "https://www.ecfr.gov/current/title-19/chapter-I/part-177",
            "relevance": "Use CBP ruling procedures where material classification or other customs uncertainty requires an authoritative determination.",
        },
        {
            "title": "California Revenue and Taxation Code § 6203 — Retailer collection obligations",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=6203.",
            "relevance": "Evaluate California collection duties using actual inventory, business activity, and applicable economic nexus rules.",
        },
        {
            "title": "California Health and Safety Code § 25249.6 — Exposure warning requirement",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=25249.6.",
            "relevance": "Assess covered exposures and applicable warning requirements rather than applying unsupported generic product warnings.",
        },
        {
            "title": "15 U.S.C. § 2302 — Consumer product warranty disclosure",
            "url": "https://www.law.cornell.edu/uscode/text/15/2302",
            "relevance": "Review disclosure duties when providing written consumer product warranties.",
        },
        {
            "title": "16 CFR Part 702 — Pre-sale availability of written warranty terms",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-G/part-702",
            "relevance": "Make applicable written warranty information available to prospective purchasers before sale.",
        },
        {
            "title": "15 U.S.C. § 7704 — Commercial electronic mail requirements",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Configure commercial outreach for accurate identification, postal information, functional opt-outs, and timely suppression.",
        },
        {
            "title": "47 U.S.C. § 227 — Restrictions on specified telephone communications",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": "Evaluate marketing-call and text practices against applicable technology, consent, and other statutory restrictions.",
        },
        {
            "title": "47 CFR § 64.1200 — Telephone solicitation and related restrictions",
            "url": "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200",
            "relevance": "Implement applicable consent, revocation, identification, and solicitation controls for supported messaging channels.",
        },
        {
            "title": "15 U.S.C. § 45 — Unfair or deceptive acts or practices",
            "url": "https://www.law.cornell.edu/uscode/text/15/45",
            "relevance": "Substantiate offers, customer promises, endorsements, and representations about data handling.",
        },
        {
            "title": "16 CFR Part 255 — FTC Endorsement Guides",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255",
            "relevance": "Apply FTC interpretive guidance to material-connection disclosures and truthful affiliate or creator endorsements.",
        },
        {
            "title": "16 CFR Part 465 — Consumer reviews and testimonials",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465",
            "relevance": "Prevent prohibited fake reviews, specified undisclosed insider reviews, and other deceptive review practices.",
        },
        {
            "title": "California Civil Code § 1798.100 — Consumer privacy obligations",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.100.",
            "relevance": "Assess covered-business notice, processing, contractual, and related duties against actual customer-data flows.",
        },
        {
            "title": "California Civil Code § 1798.135 — Sale and sharing opt-out mechanisms",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.135.",
            "relevance": "Design applicable consumer opt-out methods and connect them to advertising destinations and processing controls.",
        },
        {
            "title": "16 CFR Part 435 — Mail, Internet, or Telephone Order Merchandise Rule",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-435",
            "relevance": "Support shipment representations and implement required delay notices, cancellation choices, consent procedures, and refunds.",
        },
    ],
}
