from __future__ import annotations

CHAPTER_1 = {
    "id": "Q1",
    "chapter_id": "Q1",
    "chapter_number": 1,
    "question_number": 1,
    "slug": "what-exactly-is-medical-equipment-resale",
    "question_prompt": "What exactly is medical equipment resale, how is real operator revenue recognized vs underlying asset/client GMV, and what separates durable small-team moats from fragile beginner hype?",
    "kicker": "Q1 / THE BIG MONEY PLAYBOOKS",
    "title": "What Exactly Is Medical Equipment Resale?",
    "subtitle": "Serial-Level Trading, Biomed Acceptance, FDA Servicing Boundaries, HIPAA Data Hygiene, and CON-Sensitive Imaging Exits",
    "layout_template": "opportunity_overview",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Medical equipment resale converts documented, serviceable assets into buyer-ready clinical capacity, "
        "not merely inexpensive auction inventory. Candidate #14, Pipeline Rank #22 of 29, scores 64/100 "
        "because capital exposure and specialist labor constrain otherwise attractive spreads. This chapter "
        "maps three operating plays: CON-sensitive decommissioned imaging arbitrage, diagnostic equipment "
        "refurbishment, and veterinary equipment redeployment; the latter two are chapter-level applications, "
        "not additional canonical play identifiers. Principal-owned equipment sales generate gross resale "
        "revenue, with acquisition and refurbishment inside costs; agency transactions generate only earned "
        "fees. Canonical annual owner profits are $25,000 Conservative, $164,000 Base, and $396,000 Scaled. "
        "Durability comes from verified title, model-specific testing, service-history indexing, controlled "
        "patient-data handling, and buyers whose installation requirements are understood before inventory is purchased."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin",
            "note": "10% net margin; $25,000 annual owner net profit; 2 FT + 4 C",
        },
        {
            "label": "Base",
            "value": "$1,025,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin",
            "note": "16.0% net margin; $164,000 annual owner net profit; 2 FT + 4 C",
        },
        {
            "label": "Scaled",
            "value": "$1,800,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin",
            "note": "22% net margin; $396,000 annual owner net profit; 3 FT + 5 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Define the asset, the customer promise, and the revenue boundary",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Medical equipment resale is the purchase, preparation, and sale of identifiable devices whose "
                    "remaining utility exceeds the cost of restoring buyer confidence. The operator acquires title "
                    "or a clearly defined selling mandate, documents condition, arranges appropriate servicing, and "
                    "delivers an agreed configuration to an identified buyer. Diagnostic ultrasound, surgical tables, "
                    "veterinary monitors, and aesthetic lasers are different businesses because their accessories, "
                    "technical support, installation requirements, and failure liabilities differ. A listing marked "
                    "working does not establish measurement accuracy, software rights, electrical safety, or clinical "
                    "suitability. The actual product is a serial-numbered asset plus evidence that its promised "
                    "functions survive transport and acceptance testing. Five useful archetypes are diagnostic "
                    "refurbisher, surgical package assembler, veterinary redeployer, aesthetic specialist, and imaging "
                    "project trader. Each earns a spread by resolving a specific uncertainty rather than simply "
                    "finding a cheaper seller. Bimedis, DOTmed, eBay, and hospital auctions expose opportunities, "
                    "but none substitutes for a title review or a model-specific inspection. Start with a narrow "
                    "supported model family, a qualified service partner, and buyers willing to specify acceptance "
                    "criteria before the purchase order. The first competitive advantage is knowing which apparently "
                    "cheap assets cannot economically become saleable inventory."
                ),
                (
                    "Revenue follows the contractual role and transfer of control, not the largest number passing "
                    "through a transaction. When the business controls equipment before transfer, bears inventory "
                    "risk, and is responsible for delivering the promised asset, gross equipment resale proceeds "
                    "are the relevant principal revenue basis. Acquisition, refurbishment, contractor labor, freight "
                    "obligations, and warranty exposure then reduce earnings. A $25,000 sale of an owned ultrasound "
                    "system is not merely the difference between its selling price and its purchase price. Conversely, "
                    "an agent arranging a $100,000 hospital asset sale for an earned 8% commission ordinarily records "
                    "$8,000 of fee revenue, not $100,000 of equipment revenue. Labels such as broker or consignment "
                    "are insufficient; assess control and the actual promises using ASC 606 principal-versus-agent "
                    "guidance. Deposits received before performance are generally liabilities, and purchased devices "
                    "held for resale are inventory rather than immediate revenue offsets. Separately assess freight, "
                    "installation, taxes collected for authorities, returns, and warranty terms. A buyer's future "
                    "patient-service receipts are outside the reseller's revenue boundary. Keep agency fees in a "
                    "separate ledger so brokerage volume cannot inflate the canonical gross-resale scorecard or make "
                    "an inventory-light operation appear comparable to a principal-owned trading business."
                ),
                (
                    "The durable moat is an evidence chain that competitors cannot recreate by copying photographs. "
                    "For every serial number, retain acquisition authority, lien-release evidence where applicable, "
                    "incoming condition images, configuration details, service findings, decontamination records, "
                    "data-sanitization evidence, and signed acceptance results. Use Odoo or Zoho Inventory to track "
                    "status and landed cost, with access-controlled document storage for supporting records. Service-history "
                    "indexing should expose recurring fault codes, unsupported software releases, probe failures, "
                    "and parts consumption across the same model family. It should not accumulate patient identifiers "
                    "inside a general sales database. A contractor's reputation helps, but a reproducible test protocol "
                    "and traceable instruments matter more than a reassuring verbal assessment. UCC Sections 2-312 "
                    "and 2-313 explain why title promises and specific descriptions deserve operational discipline: "
                    "a listing can create obligations that survive a casually worded as-is label. Describe tested "
                    "functions precisely and distinguish cosmetic restoration from verified performance. A beginner "
                    "sells an attractive photograph and hopes the buyer discovers no expensive defect. An established "
                    "operator prices a documented configuration, budgets the residual defect risk, and knows which "
                    "service organization can resolve a failure after delivery without consuming the entire deal spread."
                ),
            ],
            "table": {
                "caption": "Five Sub-Niche Operator Archetypes and Their Actual Deliverables",
                "headers": [
                    "Operator archetype and customer",
                    "Saleable asset and evidence package",
                    "Economic engine and staffing requirement",
                    "Failure boundary and practical fallback",
                ],
                "rows": [
                    [
                        "Diagnostic refurbisher serving independent outpatient imaging practices",
                        "Supported ultrasound systems with probe tests and configuration records",
                        "Own inventory spread funds specialist inspection and documented repairs",
                        "Reject damaged probes unless replacement economics preserve target contribution",
                    ],
                    [
                        "Surgical package assembler serving procedure rooms and ambulatory centers",
                        "Matched tables, lights, and accessories with installation specifications",
                        "Bundle compatibility reduces buyer coordination and supports package pricing",
                        "Separate incompatible components rather than promising an unvalidated room",
                    ],
                    [
                        "Veterinary redeployer serving established companion animal clinical practices",
                        "Appropriate monitors and imaging equipment with species-relevant application review",
                        "Lower acquisition basis rewards careful accessory and workflow matching",
                        "Do not assume human equipment automatically suits veterinary applications",
                    ],
                    [
                        "Aesthetic specialist serving properly credentialed treatment facility buyers",
                        "Verified laser platforms with transferable rights and tested handpieces",
                        "Service access and consumable availability determine achievable resale spread",
                        "Walk away when software transfer or service support fails",
                    ],
                    [
                        "Imaging project trader coordinating hospital decommissioning and replacement",
                        "Inspected imaging assets with rigging plans and site boundaries",
                        "Project execution earns spread while equipment and authority remain separate",
                        "Exit under contingencies or sell equipment without operating authority claims",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy the evidence before buying the apparent bargain",
                "body": (
                    "Veteran traders reduce uncertainty before committing scarce working capital. These tactics "
                    "create a repeatable advantage without pretending that every used device deserves refurbishment."
                ),
                "items": [
                    "Request the exact software version, enabled options, accessory serials, and service-access terms before negotiating the headline price.",
                    "Ask the biomed contractor to quote a model-specific incoming inspection separately from repair labor so rejection remains economically possible.",
                    "Photograph accessory layouts and connector condition before packing; these images resolve missing-part disputes faster than generic condition statements.",
                    "Maintain model-family defect histories and quote a stressed exit price before bidding, including the cost of a second freight movement.",
                ],
            },
        },
        {
            "heading": "2. Select sub-verticals by supportability rather than auction discount",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "A sub-vertical is attractive when customers can define the required configuration, service partners "
                    "can measure performance, and enough comparable transactions support disciplined pricing. Asking "
                    "prices on DOTmed or Bimedis are discovery signals, not completed-sale evidence. Auction catalogs "
                    "from GovDeals or AllSurplus often make removal deadlines and buyer premiums explicit, but those "
                    "terms vary by seller and lot. Read the actual auction conditions instead of borrowing a fee "
                    "percentage from another transaction. Direct hospital purchases may avoid a marketplace charge "
                    "while introducing procurement coordination, lien questions, and difficult deinstallation. eBay "
                    "adds category-specific selling costs, payment timing, and return exposure; verify current terms "
                    "before setting a bid ceiling. Establish a landed-cost worksheet that includes acquisition, "
                    "premium, unrecoverable taxes, removal, packing, transport, inspection, parts, software transfer, "
                    "and expected support costs. The bid ceiling is the conservative net selling price minus every "
                    "remaining cost and the required contribution. Refuse inventory whose price works only if a "
                    "missing accessory appears free, a password becomes available, or a hospital extends removal "
                    "time. Those are unresolved costs, not entrepreneurial upside. A six-figure original purchase "
                    "price means little when the manufacturer no longer supports the installed configuration or "
                    "replacement parts consume the achievable resale price."
                ),
                (
                    "Map the mandatory play con_decommissioned_medical_imaging_arbitrage to equipment and site diligence "
                    "as two separate workstreams. A hospital's approved capacity can influence a buyer's interest, "
                    "but a used scanner does not carry portable permission to operate an imaging service. State "
                    "Certificate-of-Need rules can address projects, services, facilities, ownership changes, and "
                    "replacement equipment differently. North Carolina General Statutes Section 131E-178 illustrates "
                    "the requirement to establish whether a proposed new institutional health service requires a "
                    "certificate before undertaking it. Never infer transferable authority from a seller's historic "
                    "utilization or an existing room. Consider an illustrative $125,000 equipment acquisition, "
                    "$22,000 deinstallation and transport budget, $12,000 inspection and servicing budget, $6,000 "
                    "holding allowance, and $10,000 transaction overhead allocation. A $190,000 principal resale "
                    "leaves $15,000 after those $175,000 of specified costs. A $10,000 option credited against the "
                    "purchase price is part of the $125,000 acquisition, not an extra profit source. This is "
                    "deal arithmetic, not an annual forecast. Contract for inspection and required authorization "
                    "contingencies, cap the option exposure, and verify refund terms. If the intended site transaction "
                    "cannot proceed, exercise an available termination right or sell inspected equipment separately "
                    "without representing transferable operating authority."
                ),
                (
                    "The two complementary chapter-level plays are diagnostic refurbishment and veterinary redeployment. "
                    "For a diagnostic example, a $14,000 ultrasound purchase plus $3,000 of probe and system testing, "
                    "$1,500 freight, and a $1,000 warranty allowance creates a $19,500 specified cost basis. A "
                    "$25,000 sale provides $5,500 contribution before remaining business overhead, not $5,500 of "
                    "assured owner profit. If inspection reveals an additional $6,000 probe replacement, that spread "
                    "turns negative before overhead; reject the acquisition under negotiated inspection terms or "
                    "reprice the device for a clearly described alternative sale. For veterinary redeployment, "
                    "a $4,000 monitor package, $1,200 service and accessory budget, and $600 shipping cost against "
                    "an $8,000 sale yield $2,200 before overhead and residual support exposure. Species-appropriate "
                    "accessories, intended application, and buyer training needs remain explicit diligence items. "
                    "A failed compatibility check means returning the asset when contractually allowed or selling "
                    "it into a supported use, not improvising undocumented adaptations. Both examples reward "
                    "standardization across repeatable configurations. Neither example changes the canonical annual "
                    "profit cases. Keep these contribution calculations beside the inventory record so acquisition "
                    "staff can distinguish a repairable exception from an asset whose eventual sale merely hides "
                    "a loss behind impressive transaction volume."
                ),
            ],
            "table": {
                "caption": "Sixteen Sub-Verticals: Named Channels, Fee Bases, Defensible Moats, and Reversal Triggers",
                "headers": [
                    "Sub-vertical and named sourcing channel",
                    "Fee structure and purchase economics",
                    "Small-team moat and verification work",
                    "Refund, clawback, or failure trigger",
                ],
                "rows": [
                    [
                        "Cart ultrasound systems sourced through DOTmed and hospital relationships",
                        "Quote channel charges separately from negotiated equipment purchase consideration",
                        "Index probe condition, enabled options, and model-specific service histories",
                        "Undisclosed probe defects trigger negotiated remedies and consume warranty reserves",
                    ],
                    [
                        "Portable ultrasound platforms located through Bimedis and direct sellers",
                        "Confirm any subscription or promotion charges before evaluating contribution",
                        "Verify battery health, charger originality, and software entitlement continuity",
                        "Missing licensed functions undermine acceptance despite successful basic startup",
                    ],
                    [
                        "CT systems offered through DOTmed and decommissioning project relationships",
                        "Budget equipment price plus rigging, freight, and project contractor charges",
                        "Document tube usage, service access, and buyer installation dependencies",
                        "Tube failure or missing service access destroys projected resale spread",
                    ],
                    [
                        "MRI systems sourced through hospital tenders and DOTmed listings",
                        "Price specialist deinstallation and transport independently from equipment consideration",
                        "Use qualified magnet specialists and documented site-specific removal plans",
                        "Magnet condition or access constraints can exceed the asset spread",
                    ],
                    [
                        "Mobile C-arms discovered through Bimedis and surgical center replacements",
                        "Include negotiated marketplace costs and qualified imaging inspection charges",
                        "Confirm detector performance, mechanical motion, and destination radiation requirements",
                        "Image artifacts or registration deficiencies prevent contracted buyer acceptance",
                    ],
                    [
                        "Digital radiography packages sourced through AllSurplus and hospital disposals",
                        "Apply lot-specific buyer premiums and collection costs before setting bids",
                        "Match detectors, workstations, interfaces, and transferable software rights",
                        "Missing detector pairing or software rights strands otherwise functional hardware",
                    ],
                    [
                        "Mammography systems identified through DOTmed and specialist service networks",
                        "Separate asset pricing from installation, testing, and specialist transport quotes",
                        "Coordinate buyer facility requirements under applicable mammography quality standards",
                        "Facility certification assumptions or detector defects invalidate installation economics",
                    ],
                    [
                        "Flexible endoscopy systems located through Bimedis and endoscopy center replacements",
                        "Include specialist inspection and validated reprocessing costs within acquisition underwriting",
                        "Document leak testing, image quality, compatibility, and reprocessing evidence",
                        "Channel damage or inadequate reprocessing records creates serious return exposure",
                    ],
                    [
                        "Surgical tables purchased through GovDeals and direct hospital asset sales",
                        "Read lot premiums, removal deadlines, and loading responsibility before purchase",
                        "Verify load specifications, articulation, batteries, and accessory mounting compatibility",
                        "Missing specialty attachments or unstable movement defeats procedure-specific acceptance",
                    ],
                    [
                        "Surgical lighting systems sourced through AllSurplus and operating room renovations",
                        "Budget removal crews, mounting hardware, freight protection, and installation coordination",
                        "Preserve complete arm assemblies and confirm buyer structural mounting requirements",
                        "Incomplete ceiling components create expensive substitutions and installation delays",
                    ],
                    [
                        "Anesthesia workstations identified through DOTmed and specialist refurbishment sellers",
                        "Add qualified testing, approved replacement parts, and support allowances",
                        "Require model-specific safety checks and documented service capability before trading",
                        "Leaks, unsupported components, or failed safety tests require withholding delivery",
                    ],
                    [
                        "Multiparameter monitors sourced through eBay and hospital replacement programs",
                        "Check current category selling fees and applicable payment charges",
                        "Standardize modules, accessories, batteries, and measurement verification across repeat purchases",
                        "Accessory incompatibility or inaccurate readings triggers contractual correction obligations",
                    ],
                    [
                        "Electrosurgical generators offered through Bimedis and surgical equipment liquidations",
                        "Include analyzer testing and complete accessory costs in landed basis",
                        "Document output verification through qualified technicians using suitable test equipment",
                        "Failed output tests or damaged insulation require repair before resale",
                    ],
                    [
                        "Veterinary imaging packages found through DOTmed and established clinic referrals",
                        "Price species-relevant accessories and specialist application review alongside freight",
                        "Match actual clinic workflows rather than assuming universal cross-use suitability",
                        "Unsupported application or inaccessible service creates preventable buyer disputes",
                    ],
                    [
                        "Aesthetic laser platforms sourced through Bimedis and direct practice replacements",
                        "Verify handpiece replacement charges and license transfer costs before bidding",
                        "Authenticate usage records, service eligibility, and supported treatment configurations",
                        "Locked software or exhausted consumables eliminates the apparent purchase discount",
                    ],
                    [
                        "Tabletop sterilizers located through GovDeals and authorized service relationships",
                        "Budget auction premiums, transport, servicing, and appropriate cycle verification",
                        "Match chamber capacity and manufacturer instructions to the buyer workflow",
                        "Failed cycle performance or pressure-system defects blocks promised operational delivery",
                    ],
                ],
            },
        },
        {
            "heading": "3. Reconcile the scorecard with inventory turns and fully counted costs",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The canonical Conservative case is $250,000 gross equipment resale revenue at a 10% net margin, "
                    "producing $25,000 annual owner net profit with two full-time staff and four contractors. The "
                    "Base case is $1,025,000 at 16.0%, producing $164,000 with the same staffing counts. The Scaled "
                    "case is $1,800,000 at 22%, producing $396,000 with three full-time staff and five contractors, "
                    "eight people in total. These imply total annual expenses of $225,000, $861,000, and $1,404,000 "
                    "respectively. Contractor counts describe people engaged, not full-time-equivalent workloads. "
                    "For an illustrative volume bridge, ten sales averaging $25,000 reproduce Conservative revenue; "
                    "forty-one sales averaging $25,000 reproduce Base revenue; sixty sales averaging $30,000 reproduce "
                    "Scaled revenue. These are arithmetic decompositions rather than promised deal frequencies or "
                    "a required product mix. The corresponding fully allocated expense per sale is $22,500, $21,000, "
                    "and $23,400, respectively. A higher absolute cost per Scaled transaction is compatible with "
                    "a stronger margin because its average selling price is higher. Acquisition, refurbishment, "
                    "paid labor, ordinary support, and operating expenses must fit within each total expense envelope. "
                    "Do not append contractor invoices after calling the residual owner profit, and do not count "
                    "inventory purchases twice when translating earnings into cash requirements."
                ),
                (
                    "Working capital explains why a profitable spreadsheet can still produce a failed trading "
                    "business. The startup capital range is $75,000 to $400,000, monthly operating expenditure ranges "
                    "from $5,000 to $22,000, and time to first deal is three to nine months. Those are planning "
                    "ranges, not additional deductions layered onto already complete annual cases. Classify recurring "
                    "operating costs separately from inventory acquisition cash flows and reconcile both to the "
                    "expense model. Three months at the upper operating range consumes $66,000 before any equipment "
                    "purchase, so the lowest capital starting point cannot support every inventory strategy. A "
                    "hospital purchase paid immediately, followed by six weeks of servicing and thirty-day customer "
                    "terms, can tie up cash far longer than the visible repair duration. Customer deposits help "
                    "fund the cycle but remain obligations until the promised performance occurs. Maintain a rolling "
                    "thirteen-week cash forecast with serial-level expected completion dates, committed contractor "
                    "payments, removal deadlines, tax payments, and realistic collection timing. Set purchase limits "
                    "against the stressed forecast rather than bank balance alone. Track aged inventory at thirty, "
                    "sixty, and ninety days, then reprice, return where permitted, or liquidate under a documented "
                    "plan instead of allowing yesterday's purchase decision to dictate today's valuation."
                ),
                (
                    "Sensitivity work should attack the assumptions most likely to break, not add attractive revenue "
                    "categories. In the Base decomposition, a $1,000 average increase in unrecovered costs across "
                    "forty-one sales reduces annual profit by $41,000, from $164,000 to $123,000, assuming revenue "
                    "and other costs remain unchanged. A single $20,000 unrecovered warranty loss consumes roughly "
                    "12.2% of the canonical Base profit. In the imaging illustration, an additional $18,000 repair "
                    "changes the specified $15,000 deal remainder into a $3,000 loss. These are sensitivities, not "
                    "replacement scorecard cases. Use them to set purchase contingencies, maximum repair authorizations, "
                    "and model-family concentration limits. Avoid booking speculative service subscriptions or buyer "
                    "procedure income as a rescue. If a separate maintenance agreement is actually sold, evaluate "
                    "its performance obligations and costs separately rather than recognizing the entire contract "
                    "with the equipment shipment. Track contribution by model, realized warranty cost, days to cash, "
                    "and repeat-buyer rate alongside gross sales. A business with fewer sales and cleaner acceptance "
                    "can outperform one carrying impressive but disputed invoices. Inventory automation earns its "
                    "place when it prevents duplicate purchases, catches missing accessories, and identifies "
                    "unsupported configurations early; it does not make technician judgment or field service "
                    "capacity disappear from the labor model."
                ),
            ],
            "table": {
                "caption": "Canonical Annual Economics and Explicitly Separate Transaction Boundaries",
                "headers": [
                    "Case or transaction being measured",
                    "Recognized revenue and applicable economic basis",
                    "Cost reconciliation and resulting operator earnings",
                    "Staffing interpretation or recognition control required",
                ],
                "rows": [
                    [
                        "Conservative annual case using ten illustrative equipment sales",
                        "$250,000 gross resale proceeds from ten $25,000 transactions",
                        "$225,000 total expenses leave $25,000 profit at 10%",
                        "Two full-time staff plus four contractors within total expenses",
                    ],
                    [
                        "Base annual case using forty-one illustrative equipment sales",
                        "$1,025,000 gross resale proceeds from forty-one $25,000 transactions",
                        "$861,000 total expenses leave $164,000 profit at 16.0%",
                        "Two full-time staff plus four contractors within total expenses",
                    ],
                    [
                        "Scaled annual case using sixty illustrative equipment sales",
                        "$1,800,000 gross resale proceeds from sixty $30,000 transactions",
                        "$1,404,000 total expenses leave $396,000 profit at 22%",
                        "Three full-time staff plus five contractors, eight people total",
                    ],
                    [
                        "Agency illustration kept outside the canonical principal-resale cases",
                        "$8,000 earned commission on a $100,000 underlying asset sale",
                        "Subtract agency operating costs before determining actual agency profit",
                        "Document control assessment rather than relying on broker labels",
                    ],
                    [
                        "Imaging principal transaction with separately evaluated site authority",
                        "$190,000 equipment proceeds exclude any claimed transferable CON value",
                        "$175,000 specified costs leave $15,000 before additional unmodeled costs",
                        "Option credit belongs inside acquisition cost, without double counting",
                    ],
                    [
                        "Customer deposit collected before promised equipment performance occurs",
                        "Cash receipt generally creates liability rather than immediate revenue",
                        "Release liability as applicable contractual performance obligations are satisfied",
                        "Track deposits separately from available unrestricted operating cash balances",
                    ],
                ],
            },
        },
        {
            "heading": "4. Make technical evidence and bounded obligations the operating system",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Regulatory diligence begins with the device and the activity, not the reseller's preferred "
                    "business label. FDA establishment registration and listing obligations under 21 CFR Part 807 "
                    "depend on the role performed; buying and reselling used equipment does not automatically make "
                    "every domestic trader a manufacturer. Importing, relabeling, repackaging, or remanufacturing can "
                    "change the analysis. FDA distinguishes servicing intended to return a device to its original "
                    "safety and performance specifications and intended use from remanufacturing that significantly "
                    "changes performance, safety specifications, or intended use. Document the scope before modifying "
                    "hardware or software, and obtain specialist review when a proposed change crosses that boundary. "
                    "The Quality Management System Regulation in 21 CFR Part 820 became effective February 2, 2026; "
                    "determine applicability rather than assuming a technician's invoice satisfies manufacturer "
                    "obligations. Search FDA recall records using model, catalog number, and serial range, then "
                    "resolve applicable corrective actions before shipment. Radiation-producing equipment adds "
                    "device-specific federal and destination-state requirements; mammography facilities also face "
                    "21 CFR Part 900 requirements. State licensing, prescription-device restrictions, and installation "
                    "rules require a destination-specific check. Neither veterinary placement nor export should "
                    "serve as a casual escape route for a device whose actual condition and permitted use remain "
                    "unresolved after inspection."
                ),
                (
                    "Patient-data control and physical decontamination are separate acceptance tracks. Ultrasound "
                    "consoles, imaging workstations, printers, and removable storage may retain patient names, images, "
                    "worklists, network credentials, and exported reports. Ask the transferring institution to "
                    "identify storage and its authorized sanitization process before collection. Where the reseller "
                    "acts as a business associate and handles protected health information, address the applicable "
                    "contract and safeguard requirements under 45 CFR Sections 164.502(e), 164.504(e), and 164.308. "
                    "HIPAA does not automatically apply to every reseller merely because equipment once sat in a "
                    "hospital, but that distinction is no reason to accept uncontrolled patient records. The media "
                    "disposal and reuse provisions in 45 CFR Section 164.310(d)(2) provide concrete requirements "
                    "for regulated parties. Use an authorized, validated process consistent with current NIST "
                    "media-sanitization guidance and manufacturer constraints; a factory reset alone may not erase "
                    "all storage. Preserve necessary software entitlements while recording what was sanitized, by "
                    "whom, when, and how completion was verified. Separately require model-appropriate cleaning "
                    "or reprocessing evidence before technician handling. A generic clean sticker cannot establish "
                    "that a flexible endoscope was properly reprocessed or that inaccessible contaminated components "
                    "are safe to handle. Unresolved assets stay isolated from saleable inventory."
                ),
                (
                    "Build a small-team workflow around explicit custody changes and signed evidence, not verbal "
                    "assurances between independent contractors. One full-time role can own sourcing, contracts, "
                    "and buyer qualification while another owns inventory records, scheduling, and acceptance "
                    "coordination; specialist testing, rigging, freight, and field service remain assigned to "
                    "qualified contractors. That division fits the canonical staffing structure without pretending "
                    "every contractor works a full week. Before acquisition, confirm seller authority, exact "
                    "configuration, inspection rights, removal obligations, and the downside exit. At intake, record "
                    "condition and isolate the asset until decontamination, data handling, and technical checks "
                    "are complete. Before listing, reconcile the advertised functions against the test report, "
                    "software rights, included accessories, warranty scope, and destination requirements. Before "
                    "delivery, obtain buyer agreement on installation responsibilities and measurable acceptance "
                    "criteria. Preserve the packed-condition photographs and freight handoff record, then close "
                    "the sale against actual contractual performance rather than a convenient invoice date. Schedule "
                    "a post-delivery check while the service evidence is fresh and track every claim against the "
                    "specific model family. The commercial objective is not eliminating all returns. It is making "
                    "defects discoverable early, responsibilities legible, and recovery costs small enough that "
                    "repeat transactions compound operating knowledge instead of repeatedly financing the same "
                    "avoidable mistake."
                ),
            ],
            "table": {
                "caption": "Serial-Level Evidence Controls Before Purchase, Listing, and Delivery",
                "headers": [
                    "Control and responsible operating role",
                    "Evidence required in the asset record",
                    "Concrete authority or technical reference point",
                    "Stop condition and bounded recovery action",
                ],
                "rows": [
                    [
                        "Acquisition lead confirms authority to sell and convey title",
                        "Executed purchase terms, serial schedule, and relevant lien releases",
                        "UCC Section 2-312 addresses title and related warranty obligations",
                        "Suspend purchase until disputed ownership or encumbrances are resolved",
                    ],
                    [
                        "Qualified technical lead classifies proposed servicing and device changes",
                        "Written repair scope, intended-use comparison, and performance verification plan",
                        "21 CFR Parts 807 and 820 apply according to role",
                        "Escalate material changes before performing work or making claims",
                    ],
                    [
                        "Data custodian controls retained records and storage media disposition",
                        "Storage inventory, authorized sanitization record, and verification completion evidence",
                        "45 CFR Section 164.310 addresses regulated media disposal and reuse",
                        "Isolate equipment until authorized handling and verification are complete",
                    ],
                    [
                        "Intake coordinator verifies appropriate cleaning before technician handling",
                        "Model-specific decontamination evidence and documented handling requirements for staff",
                        "29 CFR Section 1910.1030 applies where occupational exposure exists",
                        "Withhold routine handling until exposure controls and cleaning are resolved",
                    ],
                    [
                        "Project lead separates imaging assets from site operating permissions",
                        "Equipment contract, destination analysis, and documented authorization contingencies",
                        "North Carolina General Statutes Section 131E-178 illustrates CON obligations",
                        "Terminate when permitted or pursue equipment-only sale without authority claims",
                    ],
                    [
                        "Delivery coordinator aligns advertised functions with contractual acceptance tests",
                        "Signed configuration schedule, test results, packing images, and acceptance record",
                        "UCC Section 2-313 addresses express warranties created by descriptions",
                        "Correct unsupported claims before shipment and document any agreed substitutions",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight verifications before money becomes stranded inventory",
                "body": (
                    "Advance the asset only when the responsible person can produce the evidence. An attractive "
                    "purchase price cannot compensate for an unresolved ownership, safety, or resale restriction."
                ),
                "items": [
                    "Verify seller authority, serial identity, relevant liens, inspection rights, and enforceable removal terms before releasing acquisition funds.",
                    "Verify a qualified technician's test plan, supported parts supply, software rights, and a capped repair budget before accepting the asset.",
                    "Verify documented decontamination and authorized data sanitization before moving equipment into unrestricted handling or saleable stock.",
                    "Verify buyer destination requirements, installation responsibility, measurable acceptance terms, and a contingency exit for any CON-sensitive project.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Underwrite the exact configuration",
                    "action": "Create the serial-level asset record and calculate a stressed acquisition ceiling.",
                    "detail": "Attach seller authority, accessories, software terms, channel charges, removal quotes, and an equipment-only fallback value.",
                },
                {
                    "step": 2,
                    "title": "Receive into controlled inventory",
                    "action": "Record custody and condition while restricting access until handling requirements are resolved.",
                    "detail": "Keep decontamination, storage-media disposition, and technical inspection as separate documented workstreams with named owners.",
                },
                {
                    "step": 3,
                    "title": "Release a defensible sale package",
                    "action": "Match every advertised functional claim to test evidence and the agreed device configuration.",
                    "detail": "Confirm service scope, destination obligations, licensed options, warranty terms, accessories, and buyer installation dependencies.",
                },
                {
                    "step": 4,
                    "title": "Close against performance and learn",
                    "action": "Document delivery and acceptance, apply the correct revenue treatment, and monitor claims.",
                    "detail": "Reconcile serial-level costs, release applicable deposit liabilities, update warranty exposure, and index defects for future purchase decisions.",
                },
            ],
        },
    ],
    "pull_quote": "The spread belongs to the operator who resolves the device's uncertainty before the buyer inherits it.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Choose one supported model family and interview five credible buyers about required configurations, acceptance tests, and installation constraints.",
        "Build a serial-level landed-cost worksheet that includes auction charges, servicing, software rights, transport, warranty exposure, and downside liquidation value.",
        "Separate principal equipment sales, earned agency fees, customer deposits, and buyer clinical receipts in the accounting design.",
        "Contract with qualified biomed, decontamination, data-sanitization, and logistics providers before committing to inventory that requires their services.",
        "For an imaging opportunity, document equipment economics separately from site authority and negotiate inspection, authorization, and exit contingencies.",
        "Reconcile the thirteen-week cash forecast and annual expense envelopes to $25,000, $164,000, and $396,000 canonical owner profit cases.",
    ],
    "statutory_citations": [
        {
            "title": "21 CFR Part 807 — Establishment Registration and Device Listing",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807",
            "relevance": "Determine role-specific registration and listing obligations, including activities beyond ordinary domestic resale.",
        },
        {
            "title": "21 CFR Part 820 — Quality Management System Regulation",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820",
            "relevance": "Assess manufacturer and remanufacturing obligations rather than treating every repair activity as ordinary servicing.",
        },
        {
            "title": "45 CFR 164.310 — Physical Safeguards",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.310",
            "relevance": "Paragraph (d)(2) addresses disposal and media reuse controls for electronic protected health information handled by regulated parties.",
        },
        {
            "title": "45 CFR 164.504 — Uses and Disclosures: Organizational Requirements",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504",
            "relevance": "Paragraph (e) sets requirements relevant to business associate contracts when the reseller performs covered data-handling functions.",
        },
        {
            "title": "North Carolina General Statutes 131E-178 — Activities Requiring Certificate",
            "url": "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_131E/GS_131E-178.html",
            "relevance": "Illustrates why an imaging project requires state-specific analysis separate from ownership of the equipment being resold.",
        },
        {
            "title": "21 CFR Part 900 — Mammography",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-I/part-900",
            "relevance": "Mammography facility certification and quality requirements affect buyer readiness and installation planning without attaching automatically to an equipment listing.",
        },
        {
            "title": "29 CFR 1910.1030 — Bloodborne Pathogens",
            "url": "https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1910/subpart-Z/section-1910.1030",
            "relevance": "Establishes workplace controls when equipment handling creates occupational exposure to blood or other potentially infectious materials.",
        },
        {
            "title": "UCC 2-312 — Warranty of Title and Against Infringement",
            "url": "https://www.law.cornell.edu/ucc/2/2-312",
            "relevance": "Model-code title warranty provisions support seller-authority and encumbrance checks; confirm the governing state's enacted text.",
        },
        {
            "title": "UCC 2-313 — Express Warranties",
            "url": "https://www.law.cornell.edu/ucc/2/2-313",
            "relevance": "Model-code provisions explain how descriptions and factual promises can create express warranties; confirm the governing state's enacted text.",
        },
    ],
}
