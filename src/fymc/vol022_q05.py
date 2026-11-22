from __future__ import annotations

CHAPTER_5 = {
    "id": "Q5",
    "chapter_id": "Q5",
    "chapter_number": 5,
    "question_number": 5,
    "slug": "beginner-traps-clawbacks-asymmetric-failure-modes",
    "question_prompt": "What kills 80% of newcomers in medical equipment resale, and what forensic metrics detect margin leaks, regulatory landmines, or platform bans before they wipe out capital?",
    "kicker": "Q5 / THE BIG MONEY PLAYBOOKS",
    "title": "Beginner Traps, Clawbacks & Asymmetric Failure Modes",
    "subtitle": "Serial-Level Cost Forensics, Biomed Acceptance, FDA Servicing Boundaries, HIPAA Media Controls, and Payment-Reversal Containment",
    "layout_template": "expert_insights",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #14, Medical Equipment Resale, ranks #20 with a 85/100 "
        "Money-to-Manpower Score: attractive spreads conceal capital-intensive, "
        "labor-intensive failure paths. This chapter maps three operator plays: "
        "diagnostic-system refurbishment, surgical-equipment resale, and "
        "veterinary/aesthetic specialty resale. The canonical annual owner profits "
        "are $25,000 Conservative, $164,000 Base, and $396,000 Scaled, on gross "
        "equipment resale proceeds rather than customer treatment revenue. A "
        "1 FT + 3 C pod must defend those outcomes through serial-specific "
        "ownership evidence, biomed release records, supportability checks, and "
        "cash reserves for reversals. The question's 80% framing is not a measured "
        "failure rate. The actionable issue is loss concentration: one contaminated "
        "shipment, locked software entitlement, concealed lien, or unrecoverable "
        "refund can erase many successful trades."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin",
            "note": "10% net margin; $25,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$1,025,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin",
            "note": "16.0% net margin; $164,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,800,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin",
            "note": "22% net margin; $396,000 annual owner net profit; 1 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Reject the Cheap Serial That Cannot Become a Deliverable Device",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Treat the three mapped plays as different inspection businesses, "
                    "not interchangeable inventory categories. Play one, diagnostic-system "
                    "refurbishment, depends on probe integrity, image quality, software "
                    "entitlements, and compatible workstations. Play two, surgical-equipment "
                    "resale, depends on electrical safety, accessories, sterilization "
                    "compatibility, and documented functional performance. Play three, "
                    "veterinary/aesthetic specialty resale, depends on intended use, "
                    "consumable availability, operator requirements, and the actual "
                    "configuration being offered. Assign the two full-time staff to "
                    "commercial ownership and operations ownership; retain four contractors "
                    "for biomed testing, device-specific service, controlled logistics, "
                    "and bookkeeping with records administration. These are capacity "
                    "assignments, not six interchangeable repair technicians. Obtain "
                    "specialist counsel or privacy support when a case requires it, "
                    "and count that external expense inside operating costs. Before "
                    "bidding, the commercial lead must identify a plausible buyer "
                    "and the operations lead must identify a supportable release "
                    "path. A low auction price without those two facts is a "
                    "speculative parts position. The stated $20,000–$95,000 startup "
                    "capital range does not make every lot affordable: quarantine, "
                    "freight, repairs, and refunds compete for the same cash. "
                    "An acquisition that consumes both purchasing liquidity and "
                    "the refund reserve must be declined regardless of apparent spread."
                ),
                (
                    "The first cluster of fatal traps is documentary: buying leased "
                    "equipment from someone without disposition authority, accepting a "
                    "serial number that differs from the invoice, overlooking a "
                    "secured creditor, and assuming possession conveys transferable "
                    "software. Request the seller's legal identity, equipment schedule, "
                    "serial photographs, ownership representation, and any required "
                    "lender or lessor release. UCC searches are jurisdiction-dependent "
                    "and do not independently prove clean ownership; counsel should "
                    "resolve conflicting records before funds leave escrow. Under "
                    "UCC section 9-315, security interests can continue in collateral "
                    "after disposition, subject to authorization and applicable "
                    "exceptions. A marketplace receipt does not resolve that issue. "
                    "Next, send the exact model, serial, software version, options "
                    "list, and destination country to the manufacturer or authorized "
                    "service organization. Obtain written answers about license "
                    "transfer, parts access, installation, and support expiration. "
                    "An ultrasound system with disabled options is not equivalent "
                    "to the demonstration configuration. A laser console without "
                    "usable handpieces can have negative recovery value after "
                    "removal costs. Record unresolved ownership or entitlement "
                    "questions as a purchase hold, not a discount negotiation. "
                    "The four-person pod cannot economically litigate title while "
                    "simultaneously rebuilding a service ecosystem for orphaned equipment."
                ),
                (
                    "The next traps hide inside apparently functional hardware: a "
                    "probe passes a brief scan but fails intermittently, a battery "
                    "holds charge only during the demonstration, a surgical unit "
                    "lacks the correct return-electrode accessories, or an aesthetic "
                    "handpiece reaches its usage limit immediately after delivery. "
                    "Replace the seller's generic demonstration with an agreed "
                    "acceptance protocol tied to model-specific service documentation. "
                    "For diagnostic systems, capture phantom images, probe-channel "
                    "findings, error logs, storage behavior, and installed options. "
                    "For surgical systems, retain measured outputs and electrical "
                    "safety results using appropriate calibrated analyzers, such "
                    "as a Fluke Biomedical platform selected by the technician. "
                    "For specialty systems, establish consumable authentication, "
                    "remaining supported life, cooling performance, and applicable "
                    "laser controls. Never infer test adequacy from a calibration "
                    "sticker alone. Search FDA recalls by manufacturer, model, "
                    "and affected serial range, then obtain evidence that applicable "
                    "corrections were completed. Set an internal circuit-breaker: "
                    "any unresolved safety defect, altered identification plate, "
                    "or missing critical accessory blocks listing. Require an "
                    "independent service quotation when expected repairs exceed "
                    "15% of expected selling price. That threshold is a purchasing "
                    "policy, not a statutory tolerance or permission to sell "
                    "a device with a known defect."
                ),
            ],
            "table": {
                "caption": "Acquisition Traps and Serial-Specific Evidence Across the Three Plays",
                "headers": [
                    "Trap and exposed operator play",
                    "Evidence required before committing acquisition cash",
                    "Early warning that overrides apparent discount",
                    "Named owner and immediate containment action",
                ],
                "rows": [
                    [
                        "Diagnostic systems offered with borrowed demonstration software options",
                        "Written entitlement transfer terms tied to exact device serial",
                        "Seller refuses manufacturer confirmation or excludes installed options",
                        "Commercial lead pauses bidding until transferable configuration is priced",
                    ],
                    [
                        "Surgical equipment removed from facilities under active lease",
                        "Lessor disposition authorization and serial-specific release of ownership",
                        "Invoice seller differs from documented equipment owner",
                        "Commercial lead requires ownership resolution before releasing purchase funds",
                    ],
                    [
                        "Diagnostic probes hide intermittent cable and element failures",
                        "Recorded phantom tests and qualified technician inspection findings",
                        "Image artifacts recur after cable movement or warmup",
                        "Biomed contractor quarantines probe and prices documented replacement",
                    ],
                    [
                        "Surgical generators arrive without compatible safety-critical accessory sets",
                        "Model-specific accessory inventory with functional and safety results",
                        "Supplier substitutes connectors without documented compatibility evidence",
                        "Operations lead blocks release until tested configuration is complete",
                    ],
                    [
                        "Aesthetic handpieces exhaust supported pulses immediately after delivery",
                        "Authenticated usage counters and written consumable replacement availability",
                        "Counter history conflicts with service records or wear",
                        "Device specialist calculates replacement economics before purchase authorization",
                    ],
                    [
                        "Veterinary conversions assume human-device support transfers without restrictions",
                        "Written support scope for intended species and configuration",
                        "Manufacturer declines service for the proposed changed application",
                        "Commercial lead rejects unsupported claims and revises sale scope",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy the Evidence Package Before Buying the Machine",
                "body": (
                    "Veteran buyers price the supportable configuration, not the "
                    "most flattering demonstration or the seller's original invoice."
                ),
                "items": [
                    "Ask the service provider to quote against the actual serial before auction day; an attractive model family can contain unsupported revisions.",
                    "Photograph every probe, handpiece, footswitch, and license screen during inspection, then attach that configuration schedule to the purchase agreement.",
                    "Reserve qualified biomed bench time before arranging removal; idle inventory often begins with an unavailable technician rather than a difficult repair.",
                    "Request both a repair quotation and an evidenced parts-recovery quotation so the downside case includes disposal, handling, and time to cash.",
                ],
            },
        },
        {
            "heading": "2. Separate Routine Servicing from Product, Privacy, and Contamination Exposure",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The most expensive regulatory trap is describing a material "
                    "device change as routine refurbishment. FDA distinguishes "
                    "servicing from remanufacturing based on the activities performed "
                    "and their effects, not the invoice label. Under 21 CFR "
                    "820.3, a remanufacturer includes a person whose work significantly "
                    "changes a finished device's performance or safety specifications "
                    "or intended use. Changing energy output, substituting critical "
                    "components, rewriting control software, or marketing a new "
                    "clinical application requires a documented assessment before "
                    "work proceeds. The Quality Management System Regulation became "
                    "effective February 2, 2026; determine applicable manufacturer "
                    "requirements, registration, listing, premarket obligations, and "
                    "quality-system duties for the actual role and device. Do "
                    "not assume ordinary resale itself creates every manufacturer "
                    "obligation, and do not assume a reseller label removes "
                    "obligations created by the work. The biomed contractor records "
                    "the proposed change; the operations lead holds the serial "
                    "until qualified regulatory review establishes the path. "
                    "This boundary matters particularly for surgical output stages "
                    "and aesthetic energy devices. Veterinary-only devices require "
                    "their own intended-use analysis rather than automatic import "
                    "of every human-device rule. A conversion between applications "
                    "must never be justified solely by a buyer's willingness "
                    "to accept the hardware."
                ),
                (
                    "A second asymmetric loss begins when used equipment arrives "
                    "with patient data. Ultrasound archives, DICOM workstations, "
                    "service logs, removable media, and network settings can retain "
                    "identifiers even after the visible patient list is deleted. "
                    "Establish whether the reseller receives protected health "
                    "information as a business associate, whether an agreement "
                    "is required, and which party performs sanitization before "
                    "transfer. HIPAA applicability depends on the entities and "
                    "activities involved; possession of any used device does "
                    "not automatically establish covered-entity status. For regulated "
                    "electronic information, 45 CFR 164.310(d) addresses device "
                    "and media controls, including disposal and media reuse. "
                    "Use a documented sanitization method appropriate to the "
                    "media and device, informed by NIST SP 800-88, then "
                    "verify the result without browsing clinical records unnecessarily. "
                    "Factory reset is evidence only when its scope and "
                    "effectiveness are established. If storage cannot be sanitized "
                    "without disabling licensed functions, obtain manufacturer-supported "
                    "replacement or another validated route. Isolate the device "
                    "from production networks, restrict access, and retain a "
                    "media disposition record linked to the equipment serial. "
                    "Any suspected disclosure triggers containment and the applicable "
                    "incident process, not deletion of logs or quiet forwarding "
                    "of the device to the next buyer."
                ),
                (
                    "Contamination and labeling failures can convert a profitable "
                    "trade into an injury claim long after payment clears. "
                    "Require a device-specific decontamination record from the "
                    "releasing facility, then verify the process is appropriate "
                    "for the surfaces, channels, and accessories present. A "
                    "wiped exterior does not establish that an internal fluid "
                    "path is safe. Used invasive accessories, single-use components, "
                    "and instruments needing specialized reprocessing demand separate "
                    "assessment; FDA requirements applicable to reprocessors are "
                    "not bypassed by calling an item refurbished. Worker "
                    "exposure to blood or other potentially infectious materials "
                    "also invokes the applicable OSHA controls under 29 CFR "
                    "1910.1030. Keep dirty intake physically separated from cleared "
                    "inventory and use trained contractors for work outside "
                    "the pod's demonstrated capability. Prescription-device distribution "
                    "requires attention to 21 CFR 801.109 and applicable "
                    "state requirements; aesthetic buyers are not interchangeable "
                    "with authorized clinical purchasers. X-ray equipment additionally "
                    "requires device-specific radiation and destination-state review. "
                    "For every play, verify state dealer, installer, facility, "
                    "or operator requirements where relevant rather than searching "
                    "for one universal resale license. A missing decontamination "
                    "record, contradictory intended-use label, or unresolved recall "
                    "removes the serial from sale until documented resolution, "
                    "even when the buyer requests immediate shipment."
                ),
            ],
            "table": {
                "caption": "Device, Data, and Worker-Safety Holds with Concrete Release Evidence",
                "headers": [
                    "Exposure requiring a separate operating decision",
                    "Applicable authority or technical evidence source",
                    "Release evidence retained against the equipment serial",
                    "Circuit-breaker applied by the operations lead",
                ],
                "rows": [
                    [
                        "Refurbishment changes energy output or intended clinical application",
                        "21 CFR 820.3 definitions and applicable manufacturer requirements",
                        "Documented activity assessment and completed applicable regulatory pathway",
                        "Stop modification and listing until role obligations are resolved",
                    ],
                    [
                        "Diagnostic storage retains patient studies after superficial reset",
                        "45 CFR 164.310(d) device and media control requirements",
                        "Verified sanitization record covering internal and removable storage",
                        "Isolate equipment and restrict access pending validated sanitization",
                    ],
                    [
                        "Surgical accessories contain inaccessible residues from prior procedures",
                        "Manufacturer reprocessing instructions and applicable FDA reprocessor requirements",
                        "Qualified cleaning verification and accessory-specific disposition records",
                        "Separate contaminated intake from every cleared shipping area",
                    ],
                    [
                        "Workers handle equipment with foreseeable blood exposure risks",
                        "29 CFR 1910.1030 bloodborne pathogens exposure control requirements",
                        "Training records and task-specific protective handling procedures",
                        "Suspend exposed handling until required controls are available",
                    ],
                    [
                        "Prescription equipment is marketed to an unsuitable purchaser",
                        "21 CFR 801.109 and destination-specific professional practice requirements",
                        "Buyer qualification evidence and appropriate prescription-device sale documentation",
                        "Reject unsupported consumer claims and pause buyer fulfillment",
                    ],
                    [
                        "Affected recalled serial lacks evidence of completed correction",
                        "FDA recall records and manufacturer serial-specific correction instructions",
                        "Completed correction record matching affected model and serial",
                        "Block publication and shipment until safety disposition is documented",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Independent Checks Before a Serial Becomes Saleable",
                "body": (
                    "The operations lead records each result separately. A clean "
                    "commercial file cannot substitute for a clean technical file."
                ),
                "items": [
                    "Verify seller authority, serial identity, applicable creditor releases, and transferable software rights before committing acquisition funds.",
                    "Verify calibrated test evidence, required accessories, recall disposition, and manufacturer-supported configuration before making performance claims.",
                    "Verify decontamination, media sanitization, controlled custody, and any required information-handling agreement before releasing equipment from quarantine.",
                    "Verify activity classification, device-specific distribution requirements, buyer qualifications, and destination-state obligations before accepting a binding delivery commitment.",
                ],
            },
        },
        {
            "heading": "3. Reconstruct True Unit Economics Before Refunds Consume the Pod",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The canonical scorecard recognizes gross equipment resale proceeds, "
                    "not customer procedure revenue, treatment volume, or auction "
                    "catalog value. Conservative revenue of $250,000 at 10% "
                    "produces $25,000 annual owner net profit and implies "
                    "$225,000 total costs. Base revenue of $1,025,000 at "
                    "16.0% produces $164,000 and implies $861,000 total costs. "
                    "Scaled revenue of $1,800,000 at 22% produces $396,000 "
                    "and implies $1,404,000 total costs. The first two "
                    "cases use 1 FT + 3 C; Scaled uses "
                    "1 FT + 3 C, eight people. These are "
                    "scenario targets, not evidence that actual wages, throughput, "
                    "or warranty experience already fit. Build a serial-level "
                    "cost ledger in QuickBooks Online or Xero, with an "
                    "inventory register linking each posting to the physical "
                    "asset. Include buyer premiums, removal labor, freight, storage, "
                    "repair parts, contractor testing, sales fees, and expected "
                    "return exposure. Reconcile inventory accounting with the "
                    "bookkeeper so purchasing cash outflow is not confused "
                    "with immediate cost of goods sold. The stated "
                    "$4,000–$18,000 monthly operating-expense range is planning "
                    "context, not a second deduction from published net "
                    "profit; actual recurring expenses must fit inside the "
                    "total-cost envelope for the selected case."
                ),
                (
                    "Consider an illustrative $40,000 diagnostic-system sale, separate "
                    "from the canonical annual cases. An $18,000 hammer "
                    "price plus $2,700 buyer premium, $1,600 removal and "
                    "inbound transport, $3,200 refurbishment, $600 testing and "
                    "sanitization, $1,400 outbound crating and freight, $1,200 "
                    "selling and payment costs, and $1,500 expected warranty "
                    "and return allowance totals $30,200. The resulting "
                    "$9,800 contribution is 24.5% before allocated recurring "
                    "overhead, not the owner's annual net margin. An "
                    "incremental $6,000 probe failure outside that allowance "
                    "reduces contribution to $3,800. At the unchanged "
                    "$164,000 Base profit target, an additional unrecovered "
                    "$16,400 loss consumes 10% of annual owner profit; "
                    "that sensitivity does not replace the canonical scenario. "
                    "Other leaks include nonrefundable auction premiums after "
                    "rescission, undisclosed loading charges, storage while a "
                    "site awaits installation, payment processing retained after "
                    "a refund, and missing accessories discovered during "
                    "commissioning. Obtain actual vendor terms rather than "
                    "assuming every processor keeps the same fees. Quote "
                    "installation separately when necessary, but track it "
                    "within the agreed revenue and cost treatment. A "
                    "shipping charge collected from the buyer does not "
                    "eliminate freight risk or establish delivery acceptance."
                ),
                (
                    "Clawback exposure begins before a refund appears in "
                    "the bank feed. Card disputes, marketplace buyer "
                    "protection, negotiated returns, warranty repairs, and "
                    "secured-creditor recovery follow different rules and "
                    "can overlap. Stripe or PayPal dispute deadlines "
                    "come from the actual account notice; eBay "
                    "return obligations come from the listing, transaction, "
                    "and current platform terms. Capture the serial, "
                    "tested configuration, condition disclosures, delivery evidence, "
                    "and acceptance record without assuming a signature "
                    "eliminates every remedy. A contract cannot make "
                    "a materially misleading listing accurate. Maintain "
                    "separate cash and expense views: an estimated "
                    "warranty provision is not cash reserved for "
                    "a full refund. As an internal liquidity "
                    "policy, retain enough immediately available cash "
                    "for the largest open refundable transaction, "
                    "estimated recovery transport, and eight weeks "
                    "of fixed operating costs; avoid double-counting "
                    "restricted processor balances as available money. "
                    "If that reserve falls short, stop new "
                    "purchases before seeking more sales. For "
                    "the four-person pod, inspect every first "
                    "return from a new model family. "
                    "Two same-cause failures within ten deliveries "
                    "trigger a model-family hold and root-cause "
                    "review. Small samples require investigation, "
                    "not comforting portfolio averages that conceal "
                    "one defective batch or one weak contractor."
                ),
            ],
            "table": {
                "caption": "Internal Forensic Thresholds for Margin, Cash, and Inventory Deterioration",
                "headers": [
                    "Metric calculated from serial-level operating records",
                    "Explicit internal threshold requiring immediate owner review",
                    "Likely mechanism behind the observed deterioration",
                    "Circuit-breaker and responsible pod role assignment",
                ],
                "rows": [
                    [
                        "Forecast contribution less latest fully costed contribution",
                        "Deterioration exceeds five percentage points on any serial",
                        "Repair scope expanded while selling price remained fixed",
                        "Bookkeeping contractor refreshes estimate before further purchase commitments",
                    ],
                    [
                        "Actual repair cost divided by expected selling price",
                        "Expected repairs exceed fifteen percent before acquisition commitment",
                        "Hidden subsystem failures undermine the original refurbishment budget",
                        "Device specialist obtains independent quotation and revised recovery case",
                    ],
                    [
                        "Days since receipt without a completed release package",
                        "Any serial remains unreleased after thirty calendar days",
                        "Parts delays or missing records consume scarce working cash",
                        "Operations lead assigns resolution date or initiates controlled exit",
                    ],
                    [
                        "Days since release without credible buyer inspection activity",
                        "Sixty days without inspection triggers documented pricing review",
                        "Unsupported options or weak demand prevent inventory conversion",
                        "Commercial lead compares evidenced bids and reduces purchase exposure",
                    ],
                    [
                        "Repeated failure count within each model-family delivery cohort",
                        "Two matching failures appear within ten completed deliveries",
                        "Shared component defect or deficient contractor testing escapes detection",
                        "Biomed contractor stops family releases pending documented corrective work",
                    ],
                    [
                        "Available unrestricted cash against defined refund reserve requirement",
                        "Cash falls below largest refund plus recovery and overhead",
                        "Processor holds and inventory purchases conceal near-term repayment exposure",
                        "Commercial lead freezes purchasing while bookkeeper rebuilds cash coverage",
                    ],
                ],
            },
        },
        {
            "heading": "4. Stop Platform Shortcuts and Turn Every Exception into a Controlled Decision",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Naive shortcuts destroy marketplace access because they "
                    "replace verifiable condition with an invented story. "
                    "Relabeling a prescription device as a consumer "
                    "wellness accessory, presenting servicing as FDA "
                    "approval, concealing serial labels in photographs, "
                    "reusing another seller's test certificate, or "
                    "claiming a factory warranty without transfer "
                    "confirmation creates a mismatch that complaints "
                    "and document reviews can expose. Shipping "
                    "a different serial than the invoiced "
                    "unit makes otherwise valid testing records "
                    "irrelevant. Review eBay's current medical-device "
                    "policy and each payment provider's current "
                    "restricted-business rules before listing a new "
                    "category. Keep the review date, relevant "
                    "policy excerpt, and account correspondence in "
                    "the listing file. A listing accepted "
                    "by software is not evidence that "
                    "the category or claim is permitted. "
                    "If a restriction arrives, stop affected "
                    "listings, preserve records, resolve open "
                    "customer obligations, and use the documented "
                    "appeal process. Do not create substitute "
                    "accounts, borrow identities, split restricted "
                    "transactions, or disguise product descriptions "
                    "to bypass review. Platform suspension can "
                    "freeze both distribution and settlement "
                    "cash, which is why the reserve "
                    "calculation excludes balances the operator "
                    "cannot immediately withdraw and why "
                    "the commercial lead owns policy monitoring."
                ),
                (
                    "Design telemetry around scarce attention rather "
                    "than dashboard decoration. Use Airtable or "
                    "a controlled spreadsheet for inventory states: "
                    "received, quarantined, testing, released, listed, "
                    "reserved, shipped, accepted, and returned. "
                    "Each transition requires a named owner, "
                    "timestamp, and linked evidence; inventory "
                    "tracking is the first automation lever. "
                    "Service-history indexing is the second: "
                    "store repair reports, recall checks, "
                    "configuration photographs, and test outputs "
                    "under the serial, then extract dates "
                    "and model identifiers for search. "
                    "OCR can suggest fields but cannot "
                    "certify a test or resolve conflicting "
                    "serials. Alert immediately on duplicate "
                    "serials, missing release documents, changed "
                    "bank instructions, and mismatched shipping "
                    "labels. Require an independently verified "
                    "callback for seller payment changes. "
                    "Route seven-day stagnant test queues "
                    "to the operations lead and "
                    "unanswered buyer defects after one "
                    "business day to the commercial "
                    "lead. These are internal service "
                    "targets, not statutory response periods. "
                    "Hold a weekly thirty-minute exception "
                    "review covering only blocked cash, "
                    "safety holds, disputed transactions, and "
                    "aging inventory. Contractors update evidence "
                    "before the meeting so the two "
                    "full-time staff make decisions rather "
                    "than reconstructing six separate inboxes "
                    "while another shipment misses its "
                    "promised installation window."
                ),
                (
                    "When a serious complaint arrives, protect "
                    "the customer and the evidence simultaneously. "
                    "Record the serial, event description, "
                    "configuration, delivery date, and immediate "
                    "risk; communicate appropriate isolation or "
                    "cessation instructions through qualified personnel "
                    "when safety may be affected. "
                    "Do not diagnose an injury "
                    "through a sales chat or "
                    "promise that resetting an alarm "
                    "makes the device safe. Preserve "
                    "the listing, communications, service files, "
                    "and applicable logs, and notify "
                    "the insurer under the actual "
                    "policy's timing requirements. Determine whether "
                    "the business's role creates reporting "
                    "duties under 21 CFR Part "
                    "803 or correction/removal duties under "
                    "Part 806; those duties are "
                    "not identical for ordinary distributors, "
                    "importers, manufacturers, and user facilities. "
                    "Use a qualified reviewer and "
                    "the applicable deadlines, not the "
                    "weekly meeting schedule. Expand the "
                    "hold to related serials when "
                    "a shared component or procedure "
                    "is implicated. Resume sales only "
                    "after documented disposition and corrective "
                    "work establish a supportable release "
                    "basis. Scaling to 3 FT "
                    "+ 5 C should add "
                    "measurable inspection and service capacity, "
                    "not merely more inventory. The "
                    "durable advantage across all three "
                    "plays is reliable evidence per "
                    "serial, collected before cash and "
                    "custody become difficult to reverse."
                ),
            ],
            "table": {
                "caption": "Platform, Fraud, and Incident Signals That Require Immediate Containment",
                "headers": [
                    "Observable signal in the commercial operating system",
                    "Evidence reviewed before taking any corrective action",
                    "Immediate containment assigned to a named owner",
                    "Documented condition required before normal work resumes",
                ],
                "rows": [
                    [
                        "Marketplace requests documents supporting a restricted medical-device listing",
                        "Current category policy and original serial-specific listing evidence",
                        "Commercial lead pauses affected listings and preserves correspondence",
                        "Platform review resolved and listing claims independently substantiated",
                    ],
                    [
                        "Seller changes receiving bank shortly before scheduled payment",
                        "Existing verified contact records and independently confirmed instructions",
                        "Commercial lead stops transfer pending trusted-channel callback verification",
                        "Verified payee details match documented seller authority records",
                    ],
                    [
                        "Shipping serial differs from invoice or release certificate",
                        "Physical label photographs and linked biomed release package",
                        "Operations lead stops carrier handoff and corrects allocation",
                        "Invoice shipment and test evidence identify identical equipment",
                    ],
                    [
                        "Buyer reports injury or potentially dangerous device behavior",
                        "Event account device configuration and relevant service history",
                        "Operations lead initiates safety containment and qualified reporting assessment",
                        "Documented safety disposition supports any further equipment release",
                    ],
                    [
                        "Processor places settlement funds into a restricted reserve",
                        "Account notice balance availability and open refund exposure",
                        "Bookkeeping contractor removes restricted funds from available cash",
                        "Purchasing resumes only after unrestricted reserve coverage is restored",
                    ],
                    [
                        "Two contractors submit conflicting results for identical serial",
                        "Original measurements analyzer calibration and test configuration records",
                        "Biomed contractor repeats disputed tests under controlled conditions",
                        "Operations lead accepts reconciled evidence and closes discrepancy",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Open the exception against the physical serial",
                    "action": "Record the issue, affected buyer or seller, responsible owner, and immediate cash or safety exposure.",
                    "detail": "Link original photographs, payment records, service reports, and communications; preserve originals and record later corrections separately.",
                },
                {
                    "step": 2,
                    "title": "Contain custody, claims, and new commitments",
                    "action": "Pause affected listings, shipments, modifications, or payments according to the actual failure mechanism.",
                    "detail": "Keep unrelated supported inventory moving, but extend the hold when shared components, contractors, or procedures create a credible common cause.",
                },
                {
                    "step": 3,
                    "title": "Quantify recovery and fulfill applicable duties",
                    "action": "Price repair, refund, recovery freight, parts recovery, and disposal while assigning required notices and reporting reviews.",
                    "detail": "The bookkeeping contractor updates cash coverage; the appropriate technical or regulatory specialist determines evidence and timing requirements.",
                },
                {
                    "step": 4,
                    "title": "Close with evidence and revise the purchasing rule",
                    "action": "Document final disposition, realized loss, root cause, and the specific control preventing recurrence.",
                    "detail": "The operations lead authorizes technical release and the commercial lead confirms accurate listing terms; neither replaces required external determinations.",
                },
            ],
        },
    ],
    "pull_quote": "A cheap device becomes valuable only when its ownership, performance, support, and refund exposure are all provable.",
    "diagram_id": "diag-05",
    "action_checklist": [
        "Map every active serial to diagnostic refurbishment, surgical resale, or veterinary/aesthetic specialty resale, with separate technical acceptance criteria.",
        "Create one evidence package per serial covering ownership, software rights, recall disposition, decontamination, sanitization, and biomed release.",
        "Reconcile serial-level costs to the canonical $25,000, $164,000, and $396,000 annual owner-profit cases without deducting operating expenses twice.",
        "Calculate unrestricted refund coverage weekly and stop acquisitions whenever available cash falls below the documented reserve requirement.",
        "Configure inventory alerts for duplicate serials, missing release records, seven-day test stagnation, thirty-day unreleased stock, and repeated model-family defects.",
        "Run a simulated platform restriction and serious-device-complaint exercise, assigning evidence preservation, customer communication, reporting assessment, and purchasing containment.",
    ],
    "statutory_citations": [
        {
            "title": "21 CFR 820.3 — Definitions under the Quality Management System Regulation",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.3",
            "relevance": "Supports assessment of when changes to finished devices constitute remanufacturing rather than ordinary servicing.",
        },
        {
            "title": "21 CFR Part 807 — Establishment Registration and Device Listing",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807",
            "relevance": "Determine registration, listing, exemption, and premarket notification requirements from actual activities and device circumstances.",
        },
        {
            "title": "45 CFR 164.310(d) — Device and Media Controls",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.310",
            "relevance": "For entities subject to the HIPAA Security Rule, governs handling of hardware and electronic media, including disposal and reuse controls.",
        },
        {
            "title": "45 CFR 164.504(e) — Business Associate Contracts",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504",
            "relevance": "Assess required business associate arrangements when services involve protected health information on acquired or serviced equipment.",
        },
        {
            "title": "29 CFR 1910.1030 — Bloodborne Pathogens",
            "url": "https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1910/subpart-Z/section-1910.1030",
            "relevance": "Requires applicable exposure controls for workers with occupational exposure to blood or other potentially infectious materials.",
        },
        {
            "title": "21 CFR 801.109 — Prescription Devices",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-801/subpart-D/section-801.109",
            "relevance": "Provides prescription-device labeling exemption conditions relevant to distribution, labeling, and purchaser qualification workflows.",
        },
        {
            "title": "21 CFR Part 803 — Medical Device Reporting",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803",
            "relevance": "Determine event reporting and recordkeeping duties according to the entity's actual role, including manufacturer, importer, or user facility.",
        },
        {
            "title": "21 CFR Part 806 — Medical Devices; Reports of Corrections and Removals",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-806",
            "relevance": "Assess applicable manufacturer and importer reporting and recordkeeping duties when correcting or removing distributed devices.",
        },
        {
            "title": "UCC Section 9-315 — Secured Party's Rights on Disposition of Collateral",
            "url": "https://www.law.cornell.edu/ucc/9/9-315",
            "relevance": "Explains continued security interests after disposition, subject to exceptions; verify the governing state's enacted text and transaction-specific releases.",
        },
        {
            "title": "21 U.S.C. 331 — Prohibited Acts",
            "url": "https://www.law.cornell.edu/uscode/text/21/331",
            "relevance": "Addresses prohibited acts involving adulterated or misbranded devices, supporting accurate labeling and controlled distribution practices.",
        },
    ],
}
