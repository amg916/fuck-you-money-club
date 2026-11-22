from __future__ import annotations

CHAPTER_9 = {
    "id": "Q9",
    "chapter_id": "Q9",
    "chapter_number": 9,
    "question_number": 9,
    "slug": "contracts-statutory-guardrails-licensing-outreach-scripts",
    "question_prompt": "Which federal/state statutes, licensing boundaries, contract clauses, and compliant outreach scripts govern productized ai agencies?",
    "kicker": "Q9 / THE BIG MONEY PLAYBOOKS",
    "title": "Contracts, Statutory Guardrails, Licensing & Outreach Scripts",
    "subtitle": "CFAA Access Boundaries, FTC Review Rules, TCPA Outreach, Carrier Duties, and Fixed-Scope AI Delivery Contracts",
    "layout_template": "legal_compliance_notes",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #29, Productized AI Agencies, holds Rank #08 with an 89/100 "
        "Money-to-Manpower Score across 23 mapped plays. The operating advantage "
        "comes from selling bounded implementation outcomes, not assuming clients' "
        "regulatory duties or treating their transaction volume as agency revenue. "
        "This chapter connects written access authority, data-processing terms, "
        "intellectual-property allocation, consequential-decision review, and "
        "substantiated outreach to fixed-scope sprints and support retainers. Annual "
        "owner profit remains $20,000 Conservative, $165,000 Base, and $400,000 "
        "Scaled. Two hazardous mapped plays receive explicit boundaries: reputation "
        "monitoring must not become review suppression, and telecom utilities must "
        "not depend on artificial traffic or jurisdiction shopping. Use the clause "
        "matrix, scripts, and evidence checkpoints to sell repeatable services "
        "without inheriting unbounded operational exposure."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$100,000",
            "context": "Annual implementation fees and support retainers; client automation revenue excluded",
            "note": "20% net margin; $20,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$550,000",
            "context": "Annual implementation fees and support retainers; client automation revenue excluded",
            "note": "30.0% net margin; $165,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,000,000",
            "context": "Annual implementation fees and support retainers; client automation revenue excluded",
            "note": "40% net margin; $400,000 annual owner net profit; 3 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Establish access authority before connecting client systems",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start every sprint with an authority schedule, not a shared password. "
                    "Name the client entity, authorized signer, system owner, permitted "
                    "datasets, allowed operations, production window, and expiration date. "
                    "The Computer Fraud and Abuse Act, 18 U.S.C. § 1030, makes access "
                    "boundaries material; possession of credentials does not establish "
                    "permission to enter every connected account. Separate client "
                    "authorization from platform permission: a merchant can authorize "
                    "work on its Salesforce tenant but cannot authorize bypassing "
                    "Google, Yelp, or another provider's access restrictions. Use "
                    "OAuth scopes, dedicated service accounts, and an access register "
                    "that records who can read, modify, export, or delete each object. "
                    "For Zapier, Make, n8n, and model APIs, document which service "
                    "receives the payload and whether logs retain content. Prefer "
                    "synthetic fixtures during development and minimized fields during "
                    "production. Require a named client reviewer before consequential "
                    "employment, credit, health, or eligibility decisions are released. "
                    "That reviewer needs source evidence, correction authority, and "
                    "enough time to disagree; a checkbox after an automatic rejection "
                    "does not create meaningful review. End access promptly when the "
                    "engagement ends, and retain revocation evidence without retaining "
                    "the client's underlying sensitive records."
                ),
                (
                    "Translate privacy obligations into a data-processing schedule "
                    "with concrete fields: purpose, categories, retention, subprocessors, "
                    "security controls, deletion method, incident contacts, and permitted "
                    "secondary uses. California Civil Code § 1798.100(d) requires "
                    "specified contractual protections when a covered business discloses "
                    "personal information to service providers, contractors, or third "
                    "parties. Classification depends on actual conduct and contract "
                    "terms, not the label printed above a signature. Colorado Revised "
                    "Statutes § 6-1-1305 separately specifies controller-processor "
                    "duties and contractual requirements. Assess each state's coverage, "
                    "exemptions, sensitive-data rules, and consumer-request duties "
                    "before reusing a national template. A dental workflow involving "
                    "protected health information can require a business associate "
                    "agreement under 45 CFR §§ 164.502(e) and 164.504(e), plus "
                    "appropriate downstream arrangements. A public medspa review does "
                    "not authorize confirming that the reviewer received treatment. "
                    "Recording discovery calls also needs a state-specific analysis; "
                    "California Penal Code § 632 protects confidential communications "
                    "and can require every party's consent. Record the participants' "
                    "locations, announce recording, and offer an unrecorded alternative. "
                    "Avoid storing raw call transcripts merely because transcription "
                    "is inexpensive; assign a deletion deadline and identify the "
                    "person responsible for carrying it out."
                ),
                (
                    "There is no general federal license simply to implement a "
                    "business automation workflow, but the underlying activity may "
                    "cross a licensed boundary. An agency configuring appointment "
                    "reminders is different from diagnosing patients, advising on "
                    "securities, adjusting insurance claims, or providing legal "
                    "representation. Describe the deliverable as software "
                    "configuration and documented operating support when that is "
                    "what the team actually supplies. Do not rename regulated "
                    "professional judgment as an AI recommendation to avoid the "
                    "applicable rule. Employment deployments need particular care: "
                    "Title VII, 42 U.S.C. § 2000e-2, remains relevant when a tool "
                    "screens applicants, and New York City Administrative Code "
                    "§§ 20-870 through 20-874 imposes additional requirements on "
                    "covered automated employment decision tools. Human involvement "
                    "does not automatically remove a tool from local coverage. "
                    "Build a jurisdiction-and-use register covering the client's "
                    "locations, affected people, data flows, and decision categories. "
                    "Route clinical or other licensed judgments to the client's "
                    "qualified professional rather than agency contractors. When "
                    "the intended use changes from summarizing documents to "
                    "ranking people, pause that function and reprice the assessment. "
                    "The original discovery budget should not silently absorb a "
                    "new regulated product category."
                ),
            ],
            "table": {
                "caption": "Access, Privacy, and Sector Requirements Translated into Delivery Evidence",
                "headers": [
                    "Operating boundary and primary authority",
                    "Required implementation decision",
                    "Evidence retained for the engagement",
                    "Failure response and scope consequence",
                ],
                "rows": [
                    [
                        "Client system access under 18 U.S.C. § 1030",
                        "Limit service accounts to expressly authorized objects and operations",
                        "Signed authority schedule plus dated OAuth permission export",
                        "Suspend the affected connector when authority expires or changes",
                    ],
                    [
                        "California disclosures under Civil Code § 1798.100(d)",
                        "Determine recipient role and prohibit incompatible secondary data uses",
                        "Executed processing terms and versioned subprocessor disclosure register",
                        "Remove unapproved data flows before resuming production processing",
                    ],
                    [
                        "Colorado processing contracts under Revised Statutes § 6-1-1305",
                        "Specify processing instructions, confidentiality, assistance, deletion, and audit arrangements",
                        "Controller instructions linked to each deployed automation workflow",
                        "Reassess changed purposes before adding new datasets or destinations",
                    ],
                    [
                        "Health information under 45 CFR § 164.504(e)",
                        "Execute applicable business associate arrangements before processing protected information",
                        "Signed agreements and documented downstream service eligibility checks",
                        "Use synthetic records until the protected workflow is ready",
                    ],
                    [
                        "Confidential recording under California Penal Code § 632",
                        "Assess participant locations and obtain required recording permissions",
                        "Dated recording notice with documented participant permission evidence",
                        "Continue discovery without recording when permission is withheld",
                    ],
                    [
                        "Employment automation under NYC Administrative Code §§ 20-870–20-874",
                        "Assess covered use and required audit and notice obligations",
                        "Use classification, responsible employer, and current audit evidence",
                        "Keep the covered screening function disabled until requirements are met",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before production access",
                "body": (
                    "The delivery lead records these checks against the specific "
                    "workflow version, rather than relying on a generic client signature."
                ),
                "items": [
                    "Verify the signer controls the named tenant and has authorized every requested read, write, export, and deletion operation.",
                    "Trace one synthetic record through every connector, model endpoint, log destination, and backup location before admitting client records.",
                    "Confirm applicable processing agreements, sector restrictions, retention settings, and a reachable incident-response contact.",
                    "Test reviewer override, connector revocation, and rollback using an intentionally incorrect output before enabling consequential actions.",
                ],
            },
        },
        {
            "heading": "2. Price bounded obligations and allocate ownership explicitly",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Use a master services agreement for recurring commercial "
                    "terms and a statement of work for each bounded sprint. "
                    "The statement should name inputs, connectors, output formats, "
                    "volume limits, supported environments, acceptance tests, and "
                    "exclusions. Replace 'automate customer support' with 'classify "
                    "up to 2,000 monthly tickets into twelve agreed categories, "
                    "draft responses, and route every draft to a client reviewer.' "
                    "Define a measurable quality test using a client-approved "
                    "evaluation set, including ambiguous examples and prohibited "
                    "disclosures. Specify that changes to categories, source "
                    "systems, languages, or autonomous actions require a priced "
                    "change order. A fee trigger can be 50% at booking, 30% "
                    "when the sandbox passes named tests, and 20% at production "
                    "handoff; payment milestones and accounting recognition are "
                    "separate questions. Give the client a defined acceptance "
                    "window and a written method for identifying reproducible "
                    "defects. Do not make silence waive hidden security defects "
                    "or mandatory statutory rights. Support terms must distinguish "
                    "response time from restoration time and identify excluded "
                    "third-party outages. Document client dependencies, especially "
                    "credential delivery and reviewer availability, so their delay "
                    "moves the schedule rather than creating unpaid standby work."
                ),
                (
                    "Allocate intellectual property by category rather than writing "
                    "'client owns everything.' List preexisting agency libraries, "
                    "reusable templates, client-specific configuration, client source "
                    "data, third-party components, and generated outputs separately. "
                    "Under 17 U.S.C. § 204(a), transfers of copyright ownership "
                    "generally require a signed writing; contractor work should "
                    "not be assumed to qualify automatically as work made for "
                    "hire. Obtain contractor assignments where appropriate and "
                    "give the client a durable license to embedded reusable "
                    "components. Do not promise exclusive copyright in purely "
                    "machine-generated material or rights the model provider "
                    "cannot convey. Data terms should prohibit using client "
                    "records to train unrelated products without a separate, "
                    "specific agreement. Address subprocessors, export formats, "
                    "deletion, and transition support at termination. Negotiate "
                    "a liability cap tied to a defined fee period, with "
                    "express treatment of confidentiality, intellectual-property "
                    "claims, fraud, and liabilities that applicable law will "
                    "not allow parties to limit. A dispute clause should "
                    "identify governing law, forum, escalation timing, and "
                    "whether arbitration applies. Narrow any anti-circumvention "
                    "term to identified introductions and deliberate fee "
                    "avoidance; exclude preexisting relationships and independent "
                    "inbound contacts instead of claiming ownership over the "
                    "client's entire market."
                ),
                (
                    "Keep scenario economics tied to implementation fees and "
                    "support retainers. An illustrative Conservative mix is ten "
                    "$6,000 sprints plus five $8,000 annual support packages: "
                    "$60,000 + $40,000 = $100,000 revenue. At 20% net "
                    "margin, annual costs total $80,000 and owner profit "
                    "equals $20,000. Base can comprise twenty-five $14,000 "
                    "sprints plus ten $20,000 annual retainers: $350,000 + "
                    "$200,000 = $550,000 revenue, with $385,000 costs and "
                    "$165,000 owner profit at 30.0%. Scaled can comprise "
                    "forty $15,000 sprints plus twenty $20,000 annual "
                    "retainers: $600,000 + $400,000 = $1,000,000 revenue, "
                    "with $600,000 costs and $400,000 owner profit at 40%. "
                    "The canonical teams remain 2 FT + 3 C for "
                    "Conservative and Base, and 3 FT + 4 C for "
                    "Scaled. Contractor counts describe roster size, not "
                    "automatically full-time commitments. These are annualized "
                    "illustrations, not evidence that five market-rate salaries "
                    "fit the Conservative budget. Reconcile actual compensation, "
                    "API charges, insurance, acquisition, rework, and support "
                    "against the cost envelope before hiring. Client sales "
                    "influenced by automation, carrier settlement receipts, "
                    "and customer transaction principal never become agency "
                    "revenue merely because the agency dashboard displays them."
                ),
            ],
            "table": {
                "caption": "Six Commercial Clauses That Protect a Fixed-Scope Implementation Margin",
                "headers": [
                    "Clause and commercial purpose",
                    "Specific language elements to negotiate",
                    "Supporting delivery record",
                    "Boundary that prevents expensive disputes",
                ],
                "rows": [
                    [
                        "Scope and acceptance for one bounded workflow sprint",
                        "Name connectors, volume ceilings, tests, exclusions, and acceptance timing",
                        "Versioned statement of work with client-approved evaluation fixtures",
                        "Treat additional autonomous actions as separately priced scope changes",
                    ],
                    [
                        "Fee triggers and collection for staged implementation work",
                        "Tie each installment to an observable contractual delivery milestone",
                        "Invoice references linked to booking, sandbox tests, and handoff",
                        "Separate cash collection timing from recognized service revenue",
                    ],
                    [
                        "Narrow anti-circumvention protection for documented commercial introductions",
                        "Identify protected contacts, reasonable duration, and deliberate avoidance conduct",
                        "Dated introduction register excluding established and independently sourced relationships",
                        "Avoid broad restraints that prevent ordinary unrelated client purchasing",
                    ],
                    [
                        "Liability allocation for bounded services and identifiable risks",
                        "Specify cap period, exclusions, insurance, and defense responsibilities",
                        "Negotiated agreement aligned with actual coverage and operational controls",
                        "Reject obligations exceeding available protection without deliberate commercial repricing",
                    ],
                    [
                        "Dispute resolution and orderly continuity during disagreements",
                        "State governing law, venue, escalation deadlines, and arbitration election",
                        "Signed agreement with named commercial and technical escalation contacts",
                        "Preserve client data export while handling contested payment obligations",
                    ],
                    [
                        "Ownership and licensing across client and agency assets",
                        "Separate source data, custom work, reusable libraries, and generated outputs",
                        "Asset schedule supported by contractor assignments and license inventory",
                        "Promise only rights the agency actually controls and can transfer",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Translate discovery into measurable scope",
                    "action": "List each input, connector, output, volume ceiling, and excluded action.",
                    "detail": "Attach a small evaluation dataset with expected routing and failure behavior before quoting the sprint.",
                },
                {
                    "step": 2,
                    "title": "Price dependencies and exception work",
                    "action": "Estimate delivery hours, API use, reviewer effort, support load, and rework.",
                    "detail": "Compare total engagement costs with the applicable annual scenario envelope and price additional obligations explicitly.",
                },
                {
                    "step": 3,
                    "title": "Execute rights and processing schedules",
                    "action": "Obtain signatures covering access, data handling, asset ownership, fees, and acceptance.",
                    "detail": "Confirm contractor assignments and applicable downstream agreements before deploying client-specific assets.",
                },
                {
                    "step": 4,
                    "title": "Handoff with revocable access",
                    "action": "Deliver test evidence, operating instructions, escalation contacts, and termination procedures.",
                    "detail": "Demonstrate rollback, credential revocation, data export, and deletion using the actual supported environment.",
                },
            ],
        },
        {
            "heading": "3. Turn reputation monitoring into a defensible service, not suppression",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The mapped play review_gating_reputation_extortion_funnels "
                    "requires a firm redesign around legitimate monitoring. "
                    "For medspas, dental implant practices, roofers, and auto "
                    "dealers, monitor new one-star reviews on Google Business "
                    "Profiles, Trustpilot, and Yelp only through permitted "
                    "interfaces, licensed feeds, or authorized manual review. "
                    "Do not evade rate limits or assume public visibility "
                    "creates permission for unrestricted extraction. Offer "
                    "timestamped alerts, review-velocity reporting, response "
                    "drafts, and evidence-based platform-policy assessments. "
                    "An alert within minutes is a measured service objective "
                    "only where the authorized feed supports that latency; "
                    "otherwise state the actual polling interval. The "
                    "Federal Trade Commission Act, 15 U.S.C. § 45, "
                    "prohibits deceptive practices, while 16 CFR Part 465 "
                    "addresses fake reviews, specified incentive practices, "
                    "and review suppression. Never condition a refund, "
                    "service recovery, or payment on removing an honest "
                    "negative review. Never threaten exposure, fabricate "
                    "policy violations, or claim a special platform "
                    "relationship. The Consumer Review Fairness Act, "
                    "15 U.S.C. § 45b, also restricts covered form-contract "
                    "terms that prohibit or penalize honest consumer "
                    "reviews. A B2B agency contract should require "
                    "client cooperation with these operating boundaries "
                    "rather than quietly funding prohibited tactics."
                ),
                (
                    "Apply the fallback precisely: provide equal post-service "
                    "review invitations to all eligible customers, without "
                    "filtering by satisfaction, and flag only genuine "
                    "platform-policy-violating spam or other documented "
                    "violations. Equal treatment alone is insufficient if "
                    "the solicitation violates the destination platform's "
                    "rules. Google prohibits incentivized reviews, and "
                    "Yelp discourages businesses from soliciting reviews; "
                    "use a neutral private-feedback channel where direct "
                    "solicitation is unsuitable. Recheck current platform "
                    "rules before activating each destination. A Google "
                    "invitation can read: 'Thank you for choosing our "
                    "team. If you would like to share your experience, "
                    "you can leave an honest review using the review "
                    "link in this message. Positive, mixed, and critical "
                    "feedback are equally welcome. Participation is "
                    "optional and does not affect your service.' The "
                    "system supplies the verified business link and "
                    "uses an authorized communication channel. Do not "
                    "send happy customers to a public review page "
                    "while diverting unhappy customers into a private "
                    "form. For a disputed review, preserve the original "
                    "text, URL, timestamp, policy provision, and "
                    "supporting evidence. Request platform review "
                    "without promising removal. A healthcare response "
                    "should invite private contact without confirming "
                    "patient status or discussing treatment details."
                ),
                (
                    "Make the unit economics support patient, evidence-led "
                    "work rather than coercive urgency. An illustrative "
                    "$500 monthly monitoring package across twenty "
                    "locations produces $10,000 monthly service billings, "
                    "or $120,000 annualized if retained for twelve "
                    "months. Budget $80 per location for authorized "
                    "data and messaging, $100 for human review, "
                    "and $70 for account operations: $250 direct "
                    "cost per location and $5,000 monthly contribution "
                    "before acquisition and shared overhead. This is "
                    "an optional service-line illustration inside an "
                    "agency portfolio, not an addition to the "
                    "canonical scorecard or an owner-profit forecast. "
                    "At sixty alerts monthly and twelve minutes "
                    "of review per alert, the team needs twelve "
                    "reviewer hours before escalations. If volume "
                    "doubles, the contract must specify additional "
                    "capacity pricing or a revised response target. "
                    "The fallback is a lower-frequency monitoring "
                    "and neutral-feedback service, not automated "
                    "mass reporting. Measure alert latency, evidence "
                    "quality, response turnaround, and client retention. "
                    "Do not sell predicted star-rating increases "
                    "or recovered sales without defensible measurement. "
                    "For any performance claim, retain the baseline, "
                    "measurement window, sample size, exclusions, "
                    "and attribution limits. Never classify every "
                    "negative reviewer as a competitor or every "
                    "removed review as proof of agency-created revenue."
                ),
            ],
            "table": {
                "caption": "Reputation Service Evidence Matrix for Google Business Profiles, Trustpilot, and Yelp",
                "headers": [
                    "Observed event requiring operator attention",
                    "Permitted service action and boundary",
                    "Evidence needed before client communication",
                    "Client-facing language or commercial fallback",
                ],
                "rows": [
                    [
                        "A newly posted one-star review triggers monitoring",
                        "Read through permitted access and classify the complaint",
                        "Original review link, publication time, and retrieval timestamp",
                        "We identified new feedback and prepared a factual response draft.",
                    ],
                    [
                        "A review appears to describe another business",
                        "Compare identifiable facts against the platform's published reporting grounds",
                        "Location mismatch and directly relevant public factual evidence",
                        "We can submit the documented mismatch for platform review.",
                    ],
                    [
                        "A client requests removal of legitimate criticism",
                        "Decline suppression and offer service recovery without review conditions",
                        "Original complaint and records supporting the proposed corrective action",
                        "We can address the experience without conditioning help on deletion.",
                    ],
                    [
                        "A completed service qualifies for an invitation",
                        "Apply equal eligibility rules and destination-specific solicitation requirements",
                        "Service completion record and authorized messaging preference evidence",
                        "Positive, mixed, and critical feedback are equally welcome.",
                    ],
                    [
                        "A healthcare review contains sensitive treatment details",
                        "Prepare a neutral response without confirming any patient relationship",
                        "Approved response template and designated privacy review record",
                        "Please contact our office privately so we can address your concern.",
                    ],
                    [
                        "A client requests a promised rating increase",
                        "Offer measured monitoring deliverables instead of an unsupported outcome",
                        "Historical baseline, delivery metrics, and documented attribution limits",
                        "Our package covers monitoring and response support, not purchased sentiment.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the margin by preserving evidence early",
                "body": (
                    "Reputation operations become expensive when the team reconstructs "
                    "facts after an angry client has already promised an outcome."
                ),
                "items": [
                    "Store the exact platform-policy provision beside each proposed report so a second reviewer can distinguish spam from ordinary criticism.",
                    "Separate review-alert timestamps from response-draft timestamps; otherwise feed latency gets mistaken for contractor delay.",
                    "Set an included monthly investigation allowance and price evidence-heavy escalations before selling multi-location monitoring.",
                    "Maintain different templates for public replies, private service recovery, and platform reports; never reuse sensitive client facts across those channels.",
                ],
            },
        },
        {
            "heading": "4. Screen telecom economics and use evidence-based outreach scripts",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The mapped play telecom_voice_traffic_pumping_8yy_sms_arbitrage "
                    "describes revenue-sharing CLECs, international Tier-2/3 "
                    "switches, free conference bridges, AI voice lines, "
                    "radio call-in utilities, and OTP or A2P endpoints "
                    "generating very large termination volumes. Treat "
                    "that description as a high-risk screening case, "
                    "not an implementation recipe. FCC access-stimulation "
                    "rules include 47 CFR § 61.3(bbb) and "
                    "§ 51.914; ordinary customer demand does not "
                    "automatically exempt a revenue-sharing arrangement. "
                    "Require the carrier to identify the applicable "
                    "service classification, settlement basis, access-stimulation "
                    "analysis, and responsible contracting entities. An "
                    "agency supplying software should not casually "
                    "become the telecommunications provider of record. "
                    "Depending on the actual service, federal "
                    "authorizations, state public-utility obligations, "
                    "registration, contributions, and other carrier "
                    "duties may apply. Toll-free and messaging "
                    "economics require separate analysis; voice "
                    "attestation cannot validate SMS consent. Do "
                    "not build artificial call generation, OTP "
                    "abuse, or routing intended to obscure "
                    "responsibility. The suggested fallback of "
                    "distributing traffic across jurisdictions does "
                    "not cure an unlawful arrangement. Replace "
                    "it with a genuine user-requested utility "
                    "funded by transparent subscriptions or "
                    "documented service fees, using providers "
                    "authorized for the actual routes and "
                    "retaining attributable demand records."
                ),
                (
                    "Use simple economics to expose dependence on questionable "
                    "settlements. At 20 million voice minutes monthly "
                    "and an assumed $0.002 net settlement spread, "
                    "the headline contribution is $40,000 before "
                    "disputes, transport, fraud losses, and operating "
                    "costs. A $0.002 change eliminates that entire "
                    "spread. Those receipts belong to the relevant "
                    "telecom operator, not automatically to the "
                    "implementation agency. A safer illustrative agency "
                    "engagement charges $12,000 for a bounded utility "
                    "deployment plus $1,500 monthly support, producing "
                    "$30,000 first-year fees over twelve support "
                    "months. At $8,000 implementation cost and "
                    "$800 monthly support cost, direct costs "
                    "are $17,600 and contribution is $12,400 "
                    "before shared overhead. Keep that illustration "
                    "inside the canonical portfolio totals. Require "
                    "genuine human initiation for the utility "
                    "and verified caller identity where applicable. "
                    "STIR/SHAKEN under 47 CFR § 64.6301 "
                    "addresses caller-ID authentication duties for "
                    "covered voice providers; it does not prove "
                    "consent, lawful content, or lawful compensation. "
                    "Use provider-documented attestation handling "
                    "rather than inventing an agency certification. "
                    "If carrier economics fail, retain the "
                    "customer's legitimate workflow through "
                    "subscription billing and ordinary metered "
                    "transport, or discontinue the uneconomic "
                    "feature. Never repair margin by manufacturing "
                    "traffic or bypassing provider controls."
                ),
                (
                    "Keep outbound acquisition separate from deployed client "
                    "messaging. Commercial email, including B2B outreach, "
                    "is subject to CAN-SPAM, 15 U.S.C. § 7704: "
                    "use accurate headers and subjects, applicable "
                    "advertising identification, a valid physical "
                    "postal address, and a working opt-out. "
                    "Honor opt-outs within ten business days "
                    "and supervise contractors sending on the "
                    "agency's behalf. The scripts below are "
                    "message bodies; production email must append "
                    "the agency's verified postal address and "
                    "functioning unsubscribe mechanism. Do not "
                    "invent an address to make a template "
                    "look complete. Before calls or texts, "
                    "classify the technology, number type, "
                    "purpose, recipient location, and applicable "
                    "consent requirements under 47 U.S.C. "
                    "§ 227 and 47 CFR § 64.1200, "
                    "alongside state restrictions. A published "
                    "business number is not blanket permission "
                    "for an AI-voice campaign. Artificial "
                    "or prerecorded voice rules can apply "
                    "independently of whether a system is "
                    "an automatic telephone dialing system. "
                    "Log the precise consent language, "
                    "number, timestamp, source, and revocation "
                    "status when consent is required. "
                    "A discovery conversation should establish "
                    "authority, baseline workload, permitted "
                    "data, and measurable acceptance before "
                    "discussing savings. Use named deliverables "
                    "and observed facts instead of invented "
                    "urgency, removal promises, or carrier-income "
                    "claims the agency cannot substantiate."
                ),
            ],
            "table": {
                "caption": "Verbatim Outreach and Discovery Bodies with Channel-Specific Preconditions",
                "headers": [
                    "Channel and verified prerequisite",
                    "Verbatim message or discovery question",
                    "Operational evidence captured afterward",
                    "Fallback when the condition is absent",
                ],
                "rows": [
                    [
                        "Commercial email with verified sender and required footer",
                        "Subject: Fixed-scope support workflow pilot. This is a commercial introduction. We configure ticket classification and human-reviewed reply drafts. Would a fifteen-minute discussion about your current workload be useful? Reply unsubscribe to stop future marketing emails.",
                        "Sent content, delivery record, postal footer, and suppression status",
                        "Use another permitted prospecting channel without recontacting suppressed recipients",
                    ],
                    [
                        "Reputation outreach based on an actually observed public review",
                        "We noticed a recent public review of your business. We offer monitoring and factual response support, not promised removals. Would you like a description of our fixed-scope service? Reply unsubscribe to stop marketing emails.",
                        "Verified review URL and accurate description of available services",
                        "Send a general service introduction without claiming an observed event",
                    ],
                    [
                        "Live discovery with the client's authorized system owner",
                        "Which entity controls this account, who can authorize our access, and which records may we read or change during the pilot?",
                        "Named owner, authorized signer, permitted objects, and operation boundaries",
                        "Continue process mapping with synthetic records until authority is documented",
                    ],
                    [
                        "Baseline discovery before any productivity or savings claim",
                        "How many items arrive each week, how long does handling take, and which errors require human review before anything reaches a customer?",
                        "Measured volume, handling sample, error categories, and reviewer availability",
                        "Quote a measurement sprint instead of promising unsupported savings",
                    ],
                    [
                        "Carrier discovery before building a voice utility",
                        "Which entity provides the telecommunications service, what genuine customer demand supports it, and what documented charges fund the utility without artificial traffic?",
                        "Provider contracts, service classification, demand records, and settlement explanation",
                        "Offer subscription-funded software using ordinary metered transport instead",
                    ],
                    [
                        "SMS only after applicable permission and channel checks",
                        "You asked us to contact you about a workflow pilot. Is tomorrow at 10 a.m. suitable for a brief discussion? Reply STOP to stop texts.",
                        "Actual request record, permission evidence, message timestamp, and revocation status",
                        "Do not send the message when the stated request never occurred",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Sell a bounded workflow with provable authority, not an outcome whose economics depend on somebody else's exposure.",
    "diagram_id": "diag-05",
    "action_checklist": [
        "Execute a tenant-specific access schedule identifying the signer, system owner, permitted operations, expiration, and revocation procedure.",
        "Map every data destination and confirm applicable processing terms, sector agreements, retention deadlines, and consequential-decision reviewers.",
        "Attach measurable acceptance tests, milestone fees, change-order triggers, support limits, ownership categories, and termination assistance to each sprint.",
        "Configure reputation monitoring around permitted access, equal invitation eligibility, platform-specific solicitation rules, and evidence-based reporting.",
        "Reject artificial telecom demand and jurisdiction-based avoidance; require provider classification, documented settlement economics, and a subscription-funded fallback.",
        "Deploy outreach only after sender, postal-footer, suppression, channel-permission, and claim-substantiation checks are recorded.",
    ],
    "statutory_citations": [
        {
            "title": "18 U.S.C. § 1030 — Fraud and related activity in connection with computers",
            "url": "https://www.law.cornell.edu/uscode/text/18/1030",
            "relevance": "Supports explicit access boundaries, named authorized systems, scoped credentials, and prompt revocation rather than assuming possession of a password establishes authority.",
        },
        {
            "title": "California Civil Code § 1798.100 — Consumer information and disclosure obligations",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1798.100.&lawCode=CIV",
            "relevance": "Subsection (d) establishes contractual requirements for covered disclosures to service providers, contractors, and third parties.",
        },
        {
            "title": "45 CFR § 164.504 — Uses and disclosures: organizational requirements",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504",
            "relevance": "Defines business associate contract requirements relevant to agency workflows involving protected health information.",
        },
        {
            "title": "California Penal Code § 632 — Confidential communications",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=632.&lawCode=PEN",
            "relevance": "Requires assessment of permission before recording confidential discovery or support conversations involving California participants.",
        },
        {
            "title": "42 U.S.C. § 2000e-2 — Unlawful employment practices",
            "url": "https://www.law.cornell.edu/uscode/text/42/2000e-2",
            "relevance": "Employment discrimination obligations remain relevant when an agency configures applicant screening or related decision-support workflows.",
        },
        {
            "title": "17 U.S.C. § 204 — Execution of transfers of copyright ownership",
            "url": "https://www.law.cornell.edu/uscode/text/17/204",
            "relevance": "Supports signed assignments and clear separation of client-specific work, agency libraries, third-party assets, and generated outputs.",
        },
        {
            "title": "15 U.S.C. § 45 — Unfair methods of competition and unfair or deceptive acts or practices",
            "url": "https://www.law.cornell.edu/uscode/text/15/45",
            "relevance": "Anchors truthful service claims, substantiated performance representations, and nondeceptive reputation operations.",
        },
        {
            "title": "16 CFR Part 465 — Rule on the Use of Consumer Reviews and Testimonials",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465",
            "relevance": "Addresses fake reviews, specified incentive practices, and prohibited review-suppression conduct.",
        },
        {
            "title": "15 U.S.C. § 45b — Consumer review protection",
            "url": "https://www.law.cornell.edu/uscode/text/15/45b",
            "relevance": "Restricts covered form-contract provisions that prohibit or penalize honest consumer reviews or improperly claim rights in them.",
        },
        {
            "title": "47 CFR § 61.3 — Definitions",
            "url": "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-61/subpart-A/section-61.3",
            "relevance": "Includes the access-stimulation definition used to screen telecom compensation arrangements rather than relying on marketing labels.",
        },
        {
            "title": "47 CFR § 51.914 — Additional provisions applicable to access stimulation",
            "url": "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-51/subpart-J/section-51.914",
            "relevance": "Imposes additional obligations relevant to carriers and traffic arrangements involving access stimulation.",
        },
        {
            "title": "47 CFR § 64.6301 — Caller ID authentication",
            "url": "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-HH/section-64.6301",
            "relevance": "Establishes caller-ID authentication requirements for covered providers without replacing consent, content, or settlement-law analysis.",
        },
        {
            "title": "15 U.S.C. § 7704 — Requirements for transmission of messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Governs commercial email headers, subjects, required identification and address information, opt-out mechanisms, and suppression timing.",
        },
        {
            "title": "47 U.S.C. § 227 — Restrictions on use of telephone equipment",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": "Provides the statutory framework for assessing outbound calling and messaging technology, purpose, recipient, and permission requirements.",
        },
        {
            "title": "47 CFR § 64.1200 — Delivery restrictions",
            "url": "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200",
            "relevance": "Supplies operational calling and messaging restrictions that must be assessed alongside applicable state requirements.",
        },
    ],
}
