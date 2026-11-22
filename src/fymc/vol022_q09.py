from __future__ import annotations

CHAPTER_9 = {
    "id": "Q9",
    "chapter_id": "Q9",
    "chapter_number": 9,
    "question_number": 9,
    "slug": "medical-equipment-resale-contracts-licensing-outreach",
    "question_prompt": "Which federal/state statutes, licensing boundaries, contract clauses, and compliant outreach scripts govern medical equipment resale?",
    "kicker": "Q9 / THE BIG MONEY PLAYBOOKS",
    "title": "Contracts, Statutory Guardrails, Licensing & Outreach Scripts",
    "subtitle": "FDA Servicing Boundaries, UCC Title Protection, HIPAA Media Controls, State Device Licenses, and Buyer-Ready Contract Scripts",
    "layout_template": "legal_compliance_notes",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #14, Medical Equipment Resale, holds Rank #20 with a Money-to-Manpower "
        "Score of 85/100. This chapter maps three operator plays: documented diagnostic "
        "resale, service-backed surgical resale, and specialty veterinary/aesthetic resale "
        "with intended-use separation. Contracts must connect clean title, device identity, "
        "service scope, patient-data removal, and buyer acceptance before inventory becomes "
        "cash. The canonical annual owner-profit cases are $25,000 Conservative, $164,000 "
        "Base, and $396,000 Scaled, on gross equipment resale proceeds rather than brokerage "
        "fees. A two-employee, four-contractor pod can execute the first two cases by "
        "outsourcing specialized evidence gathering without outsourcing accountability. "
        "The scaled case expands to three employees and five contractors. Protect margin "
        "by rejecting unsupported devices before purchase, not by arguing over disclaimers "
        "after delivery."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin.",
            "note": "10% net margin; $25,000 annual owner net profit; 1 FT + 3 C.",
        },
        {
            "label": "Base",
            "value": "$1,025,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin.",
            "note": "16.0% net margin; $164,000 annual owner net profit; 1 FT + 3 C.",
        },
        {
            "label": "Scaled",
            "value": "$1,800,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin.",
            "note": "22% net margin; $396,000 annual owner net profit; 1 FT + 3 C.",
        },
    ],
    "sections": [
        {
            "heading": "1. Classify the device and the work before acquiring inventory",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build the legal file around the actual device and transaction, not the "
                    "phrase refurbished equipment. Candidate #14 has three mapped operator "
                    "plays in this chapter: documented diagnostic resale, service-backed "
                    "surgical resale, and specialty veterinary/aesthetic resale with "
                    "intended-use separation. For each prospective purchase, record the "
                    "manufacturer, model, serial number, available UDI, intended use, "
                    "accessories, software revision, labeling, and ownership chain. Search "
                    "FDA recall records and relevant clearance or approval records using "
                    "the exact model family; a registration entry does not establish "
                    "clearance, approval, or current condition. The commercial lead owns "
                    "supplier representations, while the operations lead owns the evidence "
                    "folder and exception log. A contracted biomedical technician verifies "
                    "identity and condition against manufacturer documentation. Another "
                    "contractor handles specialist work only within documented competence. "
                    "For diagnostic systems, distinguish ordinary ultrasound equipment "
                    "from radiation-producing systems with additional installation duties. "
                    "For surgical equipment, identify reusable components and processing "
                    "instructions before promising a complete usable package. For specialty "
                    "equipment, separate veterinary labeling from human aesthetic claims. "
                    "Changing the advertised patient population or treatment purpose can "
                    "change the regulatory analysis even when nobody opens the enclosure. "
                    "Stop purchase negotiations when identity cannot be reconciled across "
                    "the chassis, service records, invoice, and installed software."
                ),
                (
                    "The central FDA boundary is between restoring a finished device to "
                    "its established specifications and performing work that significantly "
                    "changes performance, safety specifications, or intended use. FDA "
                    "describes the latter as remanufacturing; calling the invoice servicing "
                    "does not control the outcome. Use 21 CFR 820.3 and FDA's servicing "
                    "and remanufacturing guidance to document the actual activities, "
                    "including replacement components, software changes, energy output, "
                    "alarm behavior, and treatment claims. The Quality Management System "
                    "Regulation became effective February 2, 2026; determine the applicable "
                    "manufacturer obligations under current Part 820 rather than recycling "
                    "an obsolete quality-system checklist. Ordinary domestic distribution "
                    "may qualify for the registration exemption in 21 CFR 807.65, but "
                    "importing, relabeling, repackaging, or remanufacturing requires a "
                    "separate role analysis. Registration, listing, premarket authorization, "
                    "reporting, and quality-system duties are distinct questions. Require "
                    "the biomed contractor to describe both the work performed and the "
                    "specifications used for release. A successful power-on test does not "
                    "prove alarm accuracy, electrical safety, image quality, or performance "
                    "under load. When a replacement board or software image lacks a "
                    "traceable specification, keep the unit outside saleable inventory "
                    "until the responsible specialist resolves the change and records "
                    "the resulting regulatory position."
                ),
                (
                    "Apply a second screen for condition, claims, and post-sale events. "
                    "The Federal Food, Drug, and Cosmetic Act prohibits specified dealings "
                    "in adulterated or misbranded devices under 21 U.S.C. 331; a used-device "
                    "label does not erase those restrictions. Prescription-device labeling "
                    "under 21 CFR 801.109 also makes purchaser qualification and intended "
                    "use operational questions, not just marketing preferences. Keep "
                    "manufacturer instructions and warnings with the delivered configuration, "
                    "and identify missing manuals before quoting. Avoid promising FDA "
                    "approval merely because a device has a 510(k) clearance or an "
                    "establishment has registered. Veterinary-only devices generally do "
                    "not follow the human-device premarket authorization pathway, yet "
                    "adulteration and misbranding concerns remain; human aesthetic claims "
                    "cannot borrow that distinction. Establish a complaint channel tied "
                    "to serial numbers, with immediate escalation for injury allegations, "
                    "unexpected treatment output, contamination, and failed safety functions. "
                    "Determine whether Part 803 medical-device reporting or Part 806 "
                    "correction and removal duties apply to the business's actual role. "
                    "Do not assume every reseller has identical reporting obligations. "
                    "Contractually require prompt cooperation, record preservation, and "
                    "customer-location tracking. The operations lead should be able to "
                    "identify every affected buyer without searching personal inboxes "
                    "or relying on a departing contractor's memory."
                ),
            ],
            "table": {
                "caption": "Federal Device Classification and Release Evidence Matrix",
                "headers": [
                    "Device or operating decision",
                    "Authority and boundary to resolve",
                    "Evidence required before commercial release",
                    "Pod owner and practical stop condition",
                ],
                "rows": [
                    [
                        "Diagnostic resale with unchanged manufacturer intended use",
                        "Apply 21 U.S.C. 331 to condition and claims",
                        "Match serial identity against labeling and service history",
                        "Operations lead stops release when identity records conflict",
                    ],
                    [
                        "Surgical refurbishment involving replacement components and calibration",
                        "Evaluate remanufacturing against current 21 CFR 820.3 definitions",
                        "Document component specifications and measured post-service performance results",
                        "Biomed contractor escalates changes beyond established device specifications",
                    ],
                    [
                        "Domestic distribution without importing or changing device labeling",
                        "Assess exemption eligibility under 21 CFR 807.65 carefully",
                        "Record actual business activities supporting the selected exemption",
                        "Commercial lead reopens analysis when transaction roles change",
                    ],
                    [
                        "Prescription equipment offered to a prospective clinical purchaser",
                        "Review prescription labeling requirements under 21 CFR 801.109",
                        "Retain purchaser qualification evidence and intended-use confirmation records",
                        "Commercial lead blocks unsupported clinical or treatment representations",
                    ],
                    [
                        "Veterinary equipment proposed for human aesthetic treatment use",
                        "Separate animal-device treatment from human-device authorization requirements explicitly",
                        "Obtain labeling and authorization evidence for proposed human use",
                        "Operations lead rejects unsupported cross-market intended-use conversion proposals",
                    ],
                    [
                        "Post-sale complaint involving injury or a safety malfunction",
                        "Assess role-specific duties under Parts 803 and 806",
                        "Preserve complaint chronology and affected serial-number distribution records",
                        "Operations lead escalates promptly to designated regulatory counsel",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy the evidence package before buying the discount",
                "body": (
                    "Experienced equipment traders price missing proof as an acquisition "
                    "defect, not as an administrative task for the next buyer."
                ),
                "items": [
                    "Photograph chassis identifiers and startup software screens together; mismatched revisions often expose undocumented board swaps.",
                    "Ask the OEM about serial-specific parts availability and transferable software rights before valuing accessories or subscriptions.",
                    "Require the biomed report to state test equipment identifiers and calibration status, not merely a passed inspection checkbox.",
                    "Retain a clean model-specific listing template so sales staff cannot accidentally carry human treatment claims into veterinary inventory.",
                ],
            },
        },
        {
            "heading": "2. Resolve destination licensing, patient data, and contamination",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Create a location-and-activity worksheet before soliciting binding "
                    "purchase orders across state lines. List the seller's premises, "
                    "storage site, service location, buyer destination, installer, device "
                    "type, and intended clinical use. State requirements can attach to "
                    "manufacturing, prescription-device distribution, home medical equipment "
                    "services, radiation equipment, or professional operation; one business "
                    "license does not answer all six questions. California Health and "
                    "Safety Code section 111615 addresses device manufacturing licensing, "
                    "while Florida Statutes section 499.01 establishes permits for covered "
                    "activities, including prescription-device wholesale distribution. "
                    "Check definitions, exemptions, and the responsible agency's current "
                    "instructions against the actual transaction rather than assuming "
                    "every used-equipment seller needs the same permit. Diagnostic "
                    "X-ray transactions require additional attention to state radiation "
                    "registration, qualified installation, shielding, and inspection "
                    "requirements. Federal assembler reporting under 21 CFR 1020.30 "
                    "may also apply to diagnostic X-ray assembly activities. Aesthetic "
                    "laser ownership does not establish permission to practice medicine "
                    "or operate the device in every state. Veterinary purchasers likewise "
                    "need an intended-use and operator analysis appropriate to their "
                    "practice. Assign counsel a bounded question with the worksheet "
                    "attached, request a written answer, and record the renewal or "
                    "recheck date alongside the inventory record."
                ),
                (
                    "Treat stored patient information as a purchase-condition problem "
                    "before transport begins. Ultrasound consoles, imaging workstations, "
                    "endoscopy processors, and connected service laptops may retain "
                    "identifiers, images, worklists, credentials, or remote-access settings. "
                    "HIPAA does not automatically cover every reseller; determine whether "
                    "the seller is a covered entity and whether the reseller or "
                    "sanitization contractor will act as a business associate. Where "
                    "that relationship exists, use the required agreement under 45 CFR "
                    "164.504(e) before permitted access, and address subcontractors. "
                    "The device and media controls in 45 CFR 164.310(d) distinguish "
                    "disposal from media reuse. Prefer seller-side sanitization verified "
                    "before pickup, with an exception process for equipment that cannot "
                    "be cleared without specialist intervention. Specify authorized "
                    "methods using current NIST SP 800-88 guidance and manufacturer "
                    "constraints; factory reset alone is not evidence that all storage "
                    "has been cleared. Record media identifiers, method, verification "
                    "results, technician, date, and custody transfers without copying "
                    "patient content into the certificate. Where storage removal disables "
                    "licensed software or calibration, price authorized restoration "
                    "before accepting the unit. Prohibit diagnostic uploads containing "
                    "patient records to ordinary sales tools, and restrict quarantine "
                    "access to the personnel needed to resolve the exception."
                ),
                (
                    "Decontamination evidence must travel separately from the electrical "
                    "test report because the two answer different questions. Ask the "
                    "seller which surfaces, lumens, probes, accessories, and packaging "
                    "were processed, using which instructions and by whom. A wipe-down "
                    "receipt cannot support a sterile claim, and a passing leakage-current "
                    "test cannot establish infection-control readiness. For reusable "
                    "surgical components, preserve manufacturer processing instructions "
                    "and define whether final processing occurs before shipment or at "
                    "the buyer's facility. Do not let ordinary resale expand silently "
                    "into reprocessing single-use devices, which can introduce manufacturer "
                    "obligations. Where employees face occupational exposure to blood "
                    "or other potentially infectious materials, apply 29 CFR 1910.1030 "
                    "through exposure controls, training, protective measures, and "
                    "appropriate handling procedures. Establish physically separated "
                    "received, quarantined, serviced, and released inventory areas. "
                    "The two employees remain the commercial and operations leads; "
                    "the four contractor slots cover biomed service, data sanitization, "
                    "logistics, and specialist legal or regulatory support. These "
                    "slots are planned capacity, not permission to use unqualified "
                    "generalists for every procedure. Use external certificates as "
                    "evidence while retaining an internal release decision. If either "
                    "sanitization or contamination status remains unresolved, stop "
                    "shipment and reserve the resulting storage and remediation cost "
                    "against that unit's expected contribution."
                ),
            ],
            "table": {
                "caption": "Multi-State, Data, and Physical Handling Verification Matrix",
                "headers": [
                    "Transaction variation requiring specific review",
                    "Applicable authority or operating boundary",
                    "Written evidence to retain with inventory",
                    "Required action before shipment or access",
                ],
                "rows": [
                    [
                        "California activity involving manufacture rather than ordinary resale",
                        "Review California Health and Safety Code section 111615",
                        "Retain activity classification and applicable licensing determination records",
                        "Resolve manufacturer status before performing the proposed work",
                    ],
                    [
                        "Florida transaction involving prescription-device wholesale distribution activities",
                        "Review Florida Statutes section 499.01 and applicable definitions",
                        "Retain permit verification or documented exemption analysis evidence",
                        "Confirm covered entity and premises before accepting orders",
                    ],
                    [
                        "Diagnostic X-ray installation requiring assembly at buyer premises",
                        "Assess 21 CFR 1020.30 alongside destination radiation requirements",
                        "Keep installer credentials and applicable assembly reporting records",
                        "Schedule required installation review before promising clinical availability",
                    ],
                    [
                        "Imaging console containing patient records and network credentials",
                        "Apply relevant HIPAA relationships and device media controls",
                        "Keep custody records and verified media sanitization certificates",
                        "Restrict access until authorized handling terms are executed",
                    ],
                    [
                        "Reusable surgical accessories arriving with incomplete processing documentation",
                        "Follow manufacturer instructions and applicable occupational exposure controls",
                        "Retain processing scope and identifiable technician completion records",
                        "Quarantine accessories until processing responsibilities are resolved explicitly",
                    ],
                    [
                        "Aesthetic laser destined for a newly established clinic",
                        "Evaluate destination professional practice and device operation requirements",
                        "Record buyer intended use and qualified installer responsibilities",
                        "Separate equipment transfer from permission to perform treatments",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four facts that must be proven before release",
                "body": (
                    "The operations lead records a pass or a named corrective action "
                    "for each item; commercial urgency cannot substitute for evidence."
                ),
                "items": [
                    "Confirm device identity, intended use, recall disposition, and any transaction-specific authorization requirements.",
                    "Verify required licenses or documented exemptions for the actual locations, activities, and destination.",
                    "Attach verified patient-data sanitization and decontamination evidence to the correct serial-number record.",
                    "Confirm buyer acceptance criteria, installer responsibilities, transferable software rights, and shipment insurance.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Open the transaction classification record",
                    "action": "Capture device identifiers, parties, locations, intended use, and proposed service activities.",
                    "detail": "The commercial lead supplies transaction facts; the operations lead assigns unresolved regulatory questions to the specialist contractor.",
                },
                {
                    "step": 2,
                    "title": "Secure custody and handling authority",
                    "action": "Execute acquisition terms and any required data-handling agreement before pickup or access.",
                    "detail": "Specify title evidence, contamination status, permitted media work, quarantine routing, and responsibility for rejected equipment.",
                },
                {
                    "step": 3,
                    "title": "Complete separate technical and hygiene records",
                    "action": "Collect biomed testing, media verification, processing evidence, and applicable installation documents.",
                    "detail": "Match every certificate to the inventory identifier and investigate discrepancies before changing the unit's release status.",
                },
                {
                    "step": 4,
                    "title": "Release against buyer-specific requirements",
                    "action": "Confirm contractual acceptance tests, destination requirements, transport coverage, and handover documents.",
                    "detail": "The operations lead signs the release record; the commercial lead issues the final shipping and payment instructions.",
                },
            ],
        },
        {
            "heading": "3. Write contracts that preserve title, acceptance, and unit economics",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use paired acquisition and resale agreements with serial-specific "
                    "schedules, not a generic invoice followed by contradictory email "
                    "promises. The acquisition schedule should identify included probes, "
                    "carts, cables, software rights, manuals, service records, and "
                    "excluded consumables. Require the seller to represent ownership, "
                    "authority to sell, and disclosed liens, leases, security interests, "
                    "and recall history. UCC section 2-312 addresses title warranties; "
                    "state enactments and negotiated language determine the actual "
                    "transaction terms. Search relevant UCC records using the seller's "
                    "correct legal identity and obtain specific lien releases where "
                    "necessary. Under UCC section 9-315, a security interest can continue "
                    "in collateral after disposition unless an authorization or other "
                    "applicable rule changes that result. Do not assume possession "
                    "or a paid invoice cleans title. Identify who can reject the "
                    "unit, which evidence triggers rejection, and who pays return "
                    "freight, storage, and hazardous-condition handling. For the "
                    "diagnostic play, attach image-quality and accessory tests. For "
                    "the surgical play, attach function, processing, and component "
                    "criteria. For specialty resale, attach the exact intended-use "
                    "statement and software configuration. The commercial lead owns "
                    "negotiation; the operations lead confirms the promised deliverables "
                    "exist before either agreement is signed."
                ),
                (
                    "Define the payment trigger and acceptance process independently. "
                    "A deposit reserves identified inventory under stated refund "
                    "conditions; it does not prove delivery or authorize immediate "
                    "revenue recognition. The sale agreement should specify shipment "
                    "terms, risk of loss, insurance, installation responsibilities, "
                    "an objective inspection window, the test protocol, and remedies "
                    "for documented nonconformity. If acceptance depends on installation, "
                    "state what happens when the buyer delays site readiness and "
                    "distinguish that delay from a failed device. For a separate "
                    "sourcing engagement, identify the fee trigger precisely, such "
                    "as a completed qualifying purchase, and avoid charging an "
                    "unstated fee alongside the resale price. These canonical "
                    "scenarios describe principal equipment resale, not agency "
                    "commissions. Gross proceeds of $250,000 at 10% yield $25,000 "
                    "annual owner profit; $1,025,000 at 16.0% yields $164,000; "
                    "$1,800,000 at 22% yields $396,000. Acquisition and refurbishment "
                    "are included in those margins. As an illustrative unit check, "
                    "a $41,000 sale supporting the Base margin permits $34,440 "
                    "of fully allocated costs and leaves $6,560 profit. Twenty-five "
                    "such sales reproduce the Base totals exactly. Include freight, "
                    "contractor work, warranty provision, storage, and allocated overhead "
                    "in that cost envelope rather than subtracting only the purchase "
                    "price and calling the balance owner profit."
                ),
                (
                    "Draft warranty and liability language around evidence the business "
                    "can actually support. Under UCC sections 2-313 and 2-316, factual "
                    "sales promises and warranty exclusions interact; an inspection "
                    "report or listing can create obligations that a broad condition "
                    "label does not erase. Define warranty duration, covered components, "
                    "response process, exclusions, and responsibility for travel and "
                    "freight. A negotiated liability cap might reference the affected "
                    "unit's purchase price, but specify treatment of bodily injury, "
                    "fraud, title defects, indemnities, and data incidents rather "
                    "than assuming every claim is capped. UCC section 2-719 and "
                    "state law can limit remedy restrictions. Use a narrow "
                    "anti-circumvention clause only for identified introductions, with "
                    "a defined duration, preexisting-relationship exception, and proportionate "
                    "remedy reviewed for enforceability. Select governing law, venue "
                    "or arbitration, notice methods, and an escalation timetable. "
                    "For IP and data ownership, separate physical hardware title "
                    "from OEM software licenses, service manuals, calibration tools, "
                    "and patient records. Patient information is not saleable "
                    "inventory merely because it remains on a drive. Require "
                    "authorized license transfer where needed and preserve the "
                    "buyer's access to agreed service records. Finally, make "
                    "insurance requirements match actual device categories and "
                    "territories; a certificate alone does not establish that "
                    "product liability or installation work is covered."
                ),
            ],
            "table": {
                "caption": "Serial-Specific Contract Clause and Failure Allocation Checklist",
                "headers": [
                    "Clause requiring an explicit negotiated position",
                    "Required drafting content for this equipment",
                    "Evidence supporting the promise or allocation",
                    "Failure mode prevented by precise drafting",
                ],
                "rows": [
                    [
                        "Scope of supply and measurable acceptance criteria",
                        "List serial numbers accessories tests and delivery responsibilities",
                        "Attach signed inventory schedule and model-specific test protocol",
                        "Prevent disputes over missing probes or unusable configurations",
                    ],
                    [
                        "Purchase price deposit conditions and separate fee triggers",
                        "Separate resale consideration from any authorized sourcing compensation",
                        "Retain executed payment schedule and documented acceptance milestones",
                        "Prevent duplicate charges and premature revenue recognition decisions",
                    ],
                    [
                        "Title warranties liens and permitted transfer authority",
                        "Require ownership representations and identified lien release obligations",
                        "Retain seller identity searches and specific release documents",
                        "Prevent secured creditors from pursuing purchased equipment later",
                    ],
                    [
                        "Limited anti-circumvention protection for documented commercial introductions",
                        "Define protected contacts duration exceptions and proportionate remedies",
                        "Record introduction dates and disclosed preexisting customer relationships",
                        "Prevent broad restrictions from obstructing legitimate existing business",
                    ],
                    [
                        "Warranty liability allocation and agreed dispute resolution",
                        "Specify covered failures cap treatment carveouts and forum",
                        "Align service commitments with insurance and contractor responsibilities",
                        "Prevent unsupported repair promises and conflicting remedy provisions",
                    ],
                    [
                        "Intellectual property software transfer and patient-data responsibilities",
                        "Separate hardware ownership from licenses and retained records",
                        "Attach transfer permissions and verified media sanitization evidence",
                        "Prevent unusable software and unauthorized patient-data transfer incidents",
                    ],
                ],
            },
        },
        {
            "heading": "4. Use precise outreach scripts and retain the evidence behind every claim",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build outreach around equipment identity and documented capability, "
                    "not dramatic revenue claims for the buyer's practice. For "
                    "commercial email, CAN-SPAM requirements under 15 U.S.C. 7704 "
                    "include truthful routing information, nondeceptive subject lines, "
                    "required advertising identification where applicable, a valid "
                    "physical postal address, and a working opt-out mechanism; "
                    "business-to-business messages are not categorically exempt. Honor "
                    "opt-outs within the statutory period and retain suppression "
                    "records when contractors manage campaigns. For telephone and "
                    "text outreach, analyze 47 U.S.C. 227, current FCC rules, "
                    "number type, dialing technology, prerecorded content, applicable "
                    "permission, and state restrictions before activating automation. "
                    "A published clinic number is not universal permission for "
                    "every channel or technology. The default small-pod workflow "
                    "is individually researched business email and manually placed "
                    "calls through an approved contact list. Use this seller "
                    "discovery script verbatim: 'We purchase documented used medical "
                    "equipment for resale. Are you authorized to sell this unit, "
                    "and can you provide the model, serial number, service "
                    "history, lien or lease status, and processing record? Please "
                    "do not send patient images or records. We can discuss "
                    "value after reviewing identity, condition, software transferability, "
                    "and pickup requirements.' Record the answers without converting "
                    "unverified seller statements into advertising claims."
                ),
                (
                    "For diagnostic buyers, use this discovery script: 'Which "
                    "procedures and installation environment must this system support? "
                    "We will quote the exact model, software revision, probes, "
                    "documented service work, and acceptance tests. Please identify "
                    "your authorized purchasing contact and technical reviewer. We "
                    "will confirm available evidence before making performance or "
                    "delivery commitments.' For the surgical play, ask separately "
                    "about reusable accessories, processing capability, site power, "
                    "and the party responsible for final preparation before use. "
                    "For specialty veterinary/aesthetic resale, use this boundary "
                    "script: 'Is the intended use veterinary or human clinical "
                    "treatment, and in which state will the equipment operate? "
                    "We will evaluate the device's labeling and configuration "
                    "for that use rather than assume the same unit can "
                    "serve both markets.' If asked whether a unit is FDA "
                    "approved, answer from the record: 'We distinguish clearance, "
                    "approval, registration, and device condition. We will provide "
                    "the applicable authorization reference and our inspection scope; "
                    "we will not describe registration as approval.' These "
                    "questions identify real purchase dependencies while keeping "
                    "the seller outside clinical recommendations. Never promise "
                    "reimbursement eligibility, treatment outcomes, or professional "
                    "permission from the equipment sale alone. Route clinical "
                    "selection questions to the buyer's qualified personnel and "
                    "document the configuration they request."
                ),
                (
                    "Close with an evidence-first quotation rather than an "
                    "unsupported urgency pitch. Use this script: 'Our quotation "
                    "covers the identified unit and listed accessories, documented "
                    "service scope, shipping terms, and agreed acceptance tests. "
                    "Software transfer, installation, processing responsibilities, and "
                    "any unresolved dependencies are stated separately. Please "
                    "confirm your technical reviewer and destination requirements "
                    "before we schedule shipment.' When a prospect declines, "
                    "reply: 'Understood. We will stop promotional outreach through "
                    "this channel and record your preference.' Do not require "
                    "a purchase, login, or explanatory call to process an "
                    "email opt-out. The commercial lead maintains approved "
                    "scripts, quote versions, and suppression records; the "
                    "operations lead approves serial-specific evidence and release "
                    "status. Inventory tracking and service-history indexing are "
                    "the two automation levers: use them to assemble quote "
                    "attachments and flag missing documents, not to invent "
                    "inspection results. Review exceptions weekly, including title "
                    "gaps, stale licenses, unresolved recalls, storage exposure, "
                    "and unpriced warranty work. The Conservative and Base "
                    "cases retain two employees plus four contractors; the "
                    "Scaled case requires three employees plus five contractors. "
                    "Do not claim the higher case preserves the four-person "
                    "pod. With $20,000–$95,000 startup capital, $4,000–$18,000 "
                    "monthly operating expense, and three to nine months "
                    "to first deal, disciplined rejection protects runway "
                    "as much as disciplined selling generates receipts."
                ),
            ],
            "table": {
                "caption": "Verbatim Outreach Responses and Supporting Evidence Register",
                "headers": [
                    "Conversation event requiring a controlled response",
                    "Verbatim language approved for that event",
                    "Evidence required before advancing the transaction",
                    "Assigned owner and next recorded action",
                ],
                "rows": [
                    [
                        "Hospital seller offers equipment without complete ownership documentation",
                        "Please confirm sale authority and disclose every lien or lease.",
                        "Obtain ownership chain and any required secured-party releases",
                        "Commercial lead requests documents before issuing binding terms",
                    ],
                    [
                        "Diagnostic buyer requests an immediate clinical performance assurance",
                        "We will provide the test scope and measured results.",
                        "Attach model-specific results and identify untested operating conditions",
                        "Operations lead verifies the report matches this unit",
                    ],
                    [
                        "Surgical buyer asks whether shipped accessories are sterile",
                        "We will state the documented processing status for each accessory.",
                        "Retain accessory-specific processing records and required handling instructions",
                        "Operations lead separates processing claims from electrical testing",
                    ],
                    [
                        "Specialty buyer proposes human use for veterinary-labeled inventory",
                        "We must review labeling before quoting for human treatment.",
                        "Obtain intended-use evidence and applicable human-device authorization references",
                        "Commercial lead pauses claims pending specialist classification review",
                    ],
                    [
                        "Prospective purchaser asks whether establishment registration proves approval",
                        "Registration does not establish device approval or present condition.",
                        "Provide applicable authorization reference and separate inspection evidence",
                        "Commercial lead corrects the distinction in written quotations",
                    ],
                    [
                        "Email recipient requests removal from future promotional contact",
                        "We will stop promotional outreach and record your preference.",
                        "Retain suppression entry and propagate updates to campaign contractors",
                        "Commercial lead checks suppression before every subsequent campaign",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A saleable medical device is a verified configuration with clean title, controlled data, and promises the evidence can support.",
    "diagram_id": "diag-05",
    "action_checklist": [
        "Assign each opportunity to diagnostic, surgical, or specialty veterinary/aesthetic resale and document the device's actual intended use.",
        "Complete the location-and-activity licensing worksheet before accepting a binding order or changing the device configuration.",
        "Obtain title evidence, lien releases where required, software transfer rights, and serial-specific acquisition schedules before payment.",
        "Attach separate biomed, sanitization, and decontamination evidence before the operations lead releases inventory.",
        "Execute buyer terms covering acceptance, payment, warranty, liability, disputes, software rights, and patient-data responsibilities.",
        "Deploy approved outreach scripts with suppression controls, then reconcile quoted unit costs to the canonical revenue and owner-profit cases.",
    ],
    "statutory_citations": [
        {
            "title": "21 U.S.C. 331 — Prohibited acts",
            "url": "https://www.law.cornell.edu/uscode/text/21/331",
            "relevance": "Provides core prohibitions relevant to adulterated or misbranded devices and associated commercial conduct.",
        },
        {
            "title": "21 CFR 820.3 — Quality Management System Regulation definitions",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.3",
            "relevance": "Supports classification of manufacturer and remanufacturing activities before defining the applicable quality-system obligations.",
        },
        {
            "title": "21 CFR 807.65 — Exemptions from registration",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807/subpart-D/section-807.65",
            "relevance": "Requires activity-specific evaluation of registration exemptions rather than assuming all equipment traders share one status.",
        },
        {
            "title": "21 CFR 801.109 — Prescription devices",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-801/subpart-D/section-801.109",
            "relevance": "Connects prescription-device labeling conditions with intended use, purchaser qualification, and sales representations.",
        },
        {
            "title": "21 CFR 1020.30 — Diagnostic X-ray systems and major components",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-J/part-1020/section-1020.30",
            "relevance": "Addresses diagnostic X-ray requirements, including assembler responsibilities relevant to installation transactions.",
        },
        {
            "title": "45 CFR 164.310 — Physical safeguards",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.310",
            "relevance": "Establishes device and media controls, including disposal and media reuse, for regulated electronic protected health information.",
        },
        {
            "title": "45 CFR 164.504 — Uses and disclosures: organizational requirements",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504",
            "relevance": "Provides business-associate agreement requirements when the actual handling relationship triggers those obligations.",
        },
        {
            "title": "29 CFR 1910.1030 — Bloodborne pathogens",
            "url": "https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1030",
            "relevance": "Governs occupational exposure controls relevant to receiving and handling potentially contaminated equipment.",
        },
        {
            "title": "California Health and Safety Code section 111615 — Manufacturing licenses",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=111615.&lawCode=HSC",
            "relevance": "Requires examination of California manufacturing activities rather than treating every resale operation as ordinary distribution.",
        },
        {
            "title": "Florida Statutes section 499.01 — Permits",
            "url": "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0400-0499/0499/Sections/0499.01.html",
            "relevance": "Establishes permit categories relevant to covered prescription-device distribution activities, subject to applicable definitions and exemptions.",
        },
        {
            "title": "UCC section 2-312 — Warranty of title and against infringement",
            "url": "https://www.law.cornell.edu/ucc/2/2-312",
            "relevance": "Provides the uniform-code reference for title warranties; verify the governing state's enacted text and negotiated contract terms.",
        },
        {
            "title": "UCC section 9-315 — Secured party's rights on disposition of collateral",
            "url": "https://www.law.cornell.edu/ucc/9/9-315",
            "relevance": "Explains why equipment disposition may leave a security interest attached, subject to governing state law and applicable exceptions.",
        },
        {
            "title": "UCC section 2-313 — Express warranties",
            "url": "https://www.law.cornell.edu/ucc/2/2-313",
            "relevance": "Supports review of listings, inspection claims, and factual promises that may become express contractual warranties.",
        },
        {
            "title": "UCC section 2-316 — Exclusion or modification of warranties",
            "url": "https://www.law.cornell.edu/ucc/2/2-316",
            "relevance": "Provides the uniform-code framework for evaluating warranty exclusions alongside express promises and state enactments.",
        },
        {
            "title": "UCC section 2-719 — Contractual modification or limitation of remedy",
            "url": "https://www.law.cornell.edu/ucc/2/2-719",
            "relevance": "Identifies constraints on negotiated remedies and consequential-damage limitations under the governing state's enacted provisions.",
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Governs commercial email identification, routing accuracy, postal-address disclosure, and opt-out handling.",
        },
        {
            "title": "47 U.S.C. 227 — Restrictions on telephone equipment",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": "Requires channel-specific analysis of calls and texts alongside current FCC rules and applicable state restrictions.",
        },
    ],
}
