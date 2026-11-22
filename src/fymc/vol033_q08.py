from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-and-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small insurance housing & corporate rental arbitrage desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "County Title Evidence, OpenFEMA, ALE and CRS Portals, Microsoft Graph, Guesty, and Auditable 30-to-270-Day Housing Operations",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #33, Insurance Housing & Corporate Rental Arbitrage, ranks #07 of 36 "
        "with a 90/100 Money-to-Manpower Score. This chapter connects 12 mapped plays "
        "to an eighteen-resource directory, evidence-backed property selection, authorized "
        "placement feeds, and exception-driven operations. The edge is faster verified "
        "availability, not indiscriminate scraping: county records establish ownership clues; "
        "written landlord authority establishes permission; carrier intermediaries establish "
        "placement demand. Canonical annual owner profit is $21,600 Conservative, $150,100 "
        "Base, and $364,000 Scaled. Gross billings of $180,000, $790,000, and $1,400,000 "
        "produce modeled retained revenue of $81,000, $355,500, and $630,000. Build around "
        "claim-closeout risk, vacancy gaps, utility caps, and dated sublease addenda. Every "
        "connector needs a source timestamp, commercial-use permission, reconciliation "
        "method, and human fallback before it earns operational trust."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$180,000",
            "context": "Annual gross housing billings; $81,000 retained at 45%.",
            "note": "12% gross-billings net margin; $21,600 owner profit; 1 FT + 3 C; 26.67% retained net margin.",
        },
        {
            "label": "Base",
            "value": "$790,000",
            "context": "Annual gross housing billings; $355,500 retained at 45%.",
            "note": "19.0% gross-billings net margin; $150,100 owner profit; 1 FT + 3 C; 42.22% retained net margin.",
        },
        {
            "label": "Scaled",
            "value": "$1,400,000",
            "context": "Annual gross housing billings; $630,000 retained at 45%.",
            "note": "26% gross-billings net margin; $364,000 owner profit; 2 FT + 4 C; 57.78% retained net margin.",
        },
    ],
    "sections": [
        {
            "heading": "1. Establish Property Authority Before Turning Public Signals into Inventory",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a property evidence packet, not a scraped availability list. "
                    "County assessor records can connect an address to a parcel and assessed "
                    "owner, but they do not establish current title, signing authority, lawful "
                    "occupancy, or permission to sublease. For a Los Angeles pilot, join the "
                    "Assessor parcel record to recorded conveyances, then obtain the landlord's "
                    "executed corporate-housing addendum and evidence that the signer can bind "
                    "the owner. Confirm the actual municipality before using a permit portal: "
                    "a Los Angeles postal address can sit outside Los Angeles city jurisdiction. "
                    "The chapter's local mapping P01, parcel authority check, and P02, permit "
                    "viability screen, turn these distinctions into repeatable work. An illustrative "
                    "funnel of 100 addresses, 70 clean parcel matches, 40 operationally suitable "
                    "units, and 12 signed addenda yields 12 usable prospects, not 100 units "
                    "of inventory. Preserve document dates and unresolved discrepancies. If "
                    "ownership or permit evidence conflicts, stop promising that unit and "
                    "request the recorded instrument or building-department response. Never "
                    "substitute an assessor screenshot for contractual authority. Price searches "
                    "and certified copies separately from free index access, and collect "
                    "personal owner information only when the transaction requires it."
                ),
                (
                    "OpenFEMA and National Weather Service feeds identify where to investigate "
                    "demand, not which households have payable insurance claims. FEMA declarations "
                    "arrive through an administrative process; weather alerts can precede loss "
                    "verification and expire without producing placements. Local mapping P03, "
                    "storm-demand watch, therefore creates a geography-level research queue "
                    "rather than resident outreach. Local mapping P04, address normalization, "
                    "uses the Census geocoder to standardize candidate addresses and attach "
                    "geography without treating a successful match as proof of deliverability. "
                    "For illustration, five affected counties multiplied by twenty verified "
                    "corporate-housing prospects creates a 100-property review queue; three "
                    "documented placement requests are still only three requests. Ask ALE "
                    "Solutions, CRS Temporary Housing, and existing corporate relocation buyers "
                    "for authorized requirements before acquiring speculative master leases. "
                    "A weather signal cannot supply a carrier authorization, household budget, "
                    "pet requirement, accessibility requirement, or expected repair duration. "
                    "If either public feed fails, retain its last successful snapshot with "
                    "a visible stale flag and confirm demand directly with the placement "
                    "coordinator. Do not infer displaced households from public incident "
                    "addresses or market insurance eligibility to residents from disaster "
                    "maps alone; use those maps to allocate operator research time."
                ),
                (
                    "Normalize legal requirements at the jurisdiction and contract levels "
                    "instead of encoding a nationwide thirty-day exemption. Texas Tax Code "
                    "Section 156.101 addresses permanent-resident hotel occupancy, but the "
                    "documented right to occupy, duration, local rules, and transaction facts "
                    "matter. A thirty-night reservation field is insufficient evidence by "
                    "itself. Store the applicable taxing authority, supporting agreement, "
                    "qualifying dates, and review date beside the reservation. California "
                    "Civil Code Section 1941.1 supplies concrete dwelling-condition requirements "
                    "for California residential inventory; permit records alone do not prove "
                    "that heating, plumbing, or other conditions remain adequate today. Require "
                    "a condition inspection and property-specific commercial liability review "
                    "before offering a unit. An illustrative $4,500 monthly placement with "
                    "$2,475 of landlord rent and utility pass-throughs leaves $2,025 before "
                    "desk expenses, consistent with the modeled 45% retained share. An "
                    "unbudgeted $450 charge reduces that placement's retained amount to "
                    "$1,575; public-record precision protects real contribution. The directory "
                    "below distinguishes source publication latency from desk polling targets. "
                    "Targets are internal operating choices, not provider service promises. "
                    "Record source-specific usage terms, avoid collecting unnecessary resident "
                    "details, and retain source documents in access-controlled storage rather "
                    "than broad sales folders."
                ),
            ],
            "table": {
                "caption": "Named Resource Directory, Entries 01–06: Public Evidence and Demand Signals",
                "headers": [
                    "Named resource and operating purpose",
                    "Exact access method and evidence",
                    "Cost tier and refresh discipline",
                    "Rate-limit hygiene and fallback source",
                ],
                "rows": [
                    [
                        "01. Los Angeles County Assessor for parcel identity checks",
                        "Use https://portal.assessor.lacounty.gov/ and search the address or assessor identification number; preserve the matching parcel evidence.",
                        "Public portal access carries no subscription charge; reassess before contracting because assessment updates do not establish current title.",
                        "Use permitted manual searches rather than an assumed API; resolve conflicts through recorded deeds and landlord ownership documentation.",
                    ],
                    [
                        "02. Los Angeles County Registrar-Recorder for recorded ownership evidence",
                        "Enter https://www.lavote.gov/ and follow Real Estate Records to the current search, inspection, or copy-request procedure.",
                        "Inspection and copy options have different fee schedules; obtain current charges and note recording dates before ordering certified evidence.",
                        "Batch necessary requests within published procedures; use a licensed title provider when remote access or indexing cannot resolve ownership.",
                    ],
                    [
                        "03. Los Angeles Department of Building and Safety for permit history",
                        "Open https://www.ladbs.org/ and select Online Services and building records; confirm the parcel falls inside city jurisdiction.",
                        "Public lookup and document products have distinct charges; review before commitment because record publication can lag field conditions.",
                        "Do not scrape access-controlled search screens; request records directly or consult the correct municipal building department when jurisdiction differs.",
                    ],
                    [
                        "04. OpenFEMA Disaster Declarations Summaries for regional research queues",
                        "GET https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries using documented OData filters, selected fields, and paginated results.",
                        "Public API access has no subscription fee; poll daily locally while treating declaration publication as event-dependent administrative data.",
                        "Honor current pagination rules and back off after throttling; use https://www.fema.gov/disaster/declarations as the human review fallback.",
                    ],
                    [
                        "05. National Weather Service alerts for event timing",
                        "GET https://api.weather.gov/alerts/active with documented area filters and a descriptive User-Agent containing operator contact information.",
                        "Public API access has no subscription fee; a five-minute desk poll is an internal target, not guaranteed publication latency.",
                        "Cache responses, honor retry instructions, and slow polling after errors; verify conditions through https://www.weather.gov/ and coordinator communication.",
                    ],
                    [
                        "06. Census Geocoder for normalized address geography",
                        "GET https://geocoding.geo.census.gov/geocoder/geographies/onelineaddress with address, benchmark=Public_AR_Current, vintage=Current_Current, and format=json.",
                        "Public geocoding access has no subscription fee; benchmark releases govern source currency, while the desk processes new addresses once.",
                        "Use documented batch facilities for larger jobs and cache matches; resolve unit-level ambiguity with parcel records and landlord documents.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy certainty before buying another data subscription",
                "body": "The expensive failure is a confidently offered unit with weak authority, stale availability, or unsupported occupancy treatment.",
                "items": [
                    "Save the parcel identifier alongside every normalized address; postal spelling changes should not create duplicate master-lease prospects.",
                    "Ask the placement coordinator for extension-decision timing before negotiating landlord notice deadlines; the timing spread can exceed the nightly-rate spread.",
                    "Keep FEMA declaration time, weather-alert time, and confirmed placement-request time as separate fields; combining them creates false demand velocity.",
                    "Request the corporate-housing addendum before paying for furnishing estimates; an unsigned sublease permission is not usable inventory.",
                ],
            },
        },
        {
            "heading": "2. Synchronize Placement, Booking, Billing, and Access Without Inventing APIs",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Local mapping P05, authorized placement-feed sync, begins with the vendor "
                    "relationship rather than a reverse-engineered login flow. ALE Solutions "
                    "and CRS Temporary Housing can supply requirements through approved "
                    "supplier workflows, but public websites do not establish universal API "
                    "availability. Ask each coordinator what the specific supplier agreement "
                    "permits: portal entry, scheduled exports, structured messages, or a "
                    "documented integration. Store the placement reference, requested dates, "
                    "authorized payer, approved amount, decision deadline, and revision number. "
                    "Local mapping P06, booking-state reconciliation, connects those records "
                    "to Guesty or the desk's property system through documented access. Use "
                    "separate states for requested, quoted, approved, occupied, extended, and "
                    "closed; a portal inquiry must never become committed inventory "
                    "automatically. In an illustrative batch of forty requests, eight quotes "
                    "and two approved thirty-night placements produce sixty approved unit "
                    "nights, not 1,200. Recheck availability before transmitting each acceptance. "
                    "If a feed fails, mark affected records stale, suspend automatic promises, "
                    "and reconcile with the coordinator by an approved channel. An exported "
                    "CSV with a source timestamp is more valuable than an undocumented "
                    "connector that silently drops cancellations. Retain the original source "
                    "revision for every material change."
                ),
                (
                    "Local mapping P07, utility-cap extension billing, separates occupancy "
                    "rights from payer authorization. Track the landlord notice deadline, "
                    "guest departure expectation, carrier extension approval, utility meter "
                    "period, included allowance, and collectible excess under the executed "
                    "agreement. A scheduled reminder cannot extend a lease, and an automated "
                    "invoice cannot create a contractual utility obligation. For illustration, "
                    "a ten-night extension at $150 per night creates $1,500 of additional "
                    "billings only after the responsible payer accepts the extension; applying "
                    "the scorecard's 45% planning share gives $675 before desk expenses. "
                    "Actual incremental landlord and utility costs may differ, so record "
                    "the realized placement contribution separately. Local mapping P08, "
                    "payment-evidence matching, links Stripe invoices, bank receipts, or "
                    "approved intermediary remittances to that exact placement revision. "
                    "Stripe is an optional collection rail, not an assumption that insurers "
                    "pay by card. Match invoice identifiers, gross amounts, fees, settlement "
                    "dates, and credits. If remittance lacks a placement reference, hold "
                    "the receipt in an unapplied queue and request allocation rather than "
                    "closing the oldest invoice. Never close a claim in the booking system "
                    "merely because one invoice was paid; repair completion and occupancy "
                    "closeout require separate evidence."
                ),
                (
                    "Local mapping P09, access-window automation, makes a lock credential "
                    "a consequence of verified occupancy status, not merely a calendar "
                    "event. RemoteLock access should follow compatible hardware capabilities, "
                    "documented account permissions, and property-specific access rules. "
                    "Issue a unique time-bounded code after confirming move-in details; "
                    "separate guest, cleaner, and maintenance credentials. Do not automatically "
                    "revoke access to an occupied dwelling because a payer is late or "
                    "a claim closes: local possession rules and the actual tenancy govern "
                    "that situation. Local mapping P10, leak-and-noise exception routing, "
                    "uses installed devices through their documented dashboards or authorized "
                    "connectors, with clear guest notice and no interior audio recording. "
                    "A sensor alert should create an assessment task, not an accusation "
                    "or automatic utility surcharge. In an illustrative twenty-unit fleet, "
                    "five alerts requiring six minutes each consume thirty operator minutes; "
                    "sending every measurement to the operator destroys that efficiency. "
                    "Deduplicate repeated alerts, preserve device health separately from "
                    "incident severity, and escalate unresolved water alarms promptly. "
                    "Twilio can carry approved operational notices, while failed delivery "
                    "must create a call task or alternate contact attempt. Keep a physical "
                    "access fallback and a named local responder for every property."
                ),
            ],
            "table": {
                "caption": "Named Resource Directory, Entries 07–12: Placement and Operating Rails",
                "headers": [
                    "Named resource and operating purpose",
                    "Exact access method and evidence",
                    "Cost tier and refresh discipline",
                    "Rate-limit hygiene and fallback source",
                ],
                "rows": [
                    [
                        "07. ALE Solutions for approved supplier placement workflows",
                        "Begin at https://www.alesolutions.com/ and request supplier onboarding; use only the account-specific portal or integration supplied under agreement.",
                        "Commercial supplier terms determine access and economics; review the approved queue each business day and after coordinator notices.",
                        "Do not automate authenticated screens without permission; use coordinator confirmation and approved exports when no documented integration is available.",
                    ],
                    [
                        "08. CRS Temporary Housing for authorized placement coordination",
                        "Begin at https://www.crsth.com/ and request the relevant supplier relationship; retain coordinator-issued portal instructions and placement references.",
                        "Commercial relationship terms determine available access; a fifteen-minute desk review during staffed hours is a local target only.",
                        "Follow the supplied interface limits and escalation process; reconcile through the coordinator when exports or portal updates become stale.",
                    ],
                    [
                        "09. Guesty Open API for property booking reconciliation",
                        "Use https://open-api-docs.guesty.com/ and the documented https://open-api.guesty.com/v1 interface with account-authorized credentials and reservation identifiers.",
                        "Paid product and API entitlements depend on the agreement; prefer available events plus a daily full reservation reconciliation.",
                        "Honor documented account limits and retry instructions; recover missing changes through supported exports and the account's reservation dashboard.",
                    ],
                    [
                        "10. Stripe API for optional invoice and receipt matching",
                        "Call https://api.stripe.com/v1/invoices and configured payment webhooks; verify signatures and use idempotency keys for supported write operations.",
                        "Usage-based payment and optional billing fees vary by plan; webhooks target prompt updates but settlement remains rail-dependent.",
                        "Read response headers, apply bounded retries, and deduplicate events; reconcile against dashboard exports and bank settlement evidence after failures.",
                    ],
                    [
                        "11. RemoteLock for authorized time-bounded property access",
                        "Consult https://developer.remotelock.com/ and use documented OAuth access to https://api.remotelock.com/ for compatible devices and approved accounts.",
                        "Hardware, subscription, and integration costs depend on the deployment; verify command acknowledgments because device connectivity controls actual execution.",
                        "Follow documented request limits and avoid repeated unlock commands; use the property access procedure and local responder during outages.",
                    ],
                    [
                        "12. Twilio Messaging for approved operational guest notices",
                        "Use https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Messages.json with scoped credentials and validate configured status-callback signatures.",
                        "Usage-based messaging, number, and carrier charges apply; delivery callbacks reflect carrier outcomes rather than a promised arrival time.",
                        "Queue within sender throughput limits and handle error codes; escalate failed urgent notices through the documented alternate contact procedure.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Capture the source contract",
                    "action": "Register the connector owner, permitted purpose, credential scope, and current provider documentation.",
                    "detail": "Record whether access is API, approved export, portal entry, or coordinator communication; attach the agreement and renewal date.",
                },
                {
                    "step": 2,
                    "title": "Normalize without overwriting evidence",
                    "action": "Write the original payload and normalize property, placement, reservation, and invoice identifiers.",
                    "detail": "Retain source_updated_at, observed_at, revision, and payload hash; place unmatched identifiers in a review queue.",
                },
                {
                    "step": 3,
                    "title": "Reconcile the consequential transition",
                    "action": "Require current evidence before accepting dates, extending charges, or issuing occupancy credentials.",
                    "detail": "Check landlord authority, available inventory, approved payer terms, and the latest placement revision before changing committed state.",
                },
                {
                    "step": 4,
                    "title": "Exercise the human fallback",
                    "action": "Run a connector outage drill and complete one placement update through the approved manual route.",
                    "detail": "Measure restoration time, reconcile the backlogged events, and document which automated actions remained suspended during the outage.",
                },
            ],
        },
        {
            "heading": "3. Build an Eligibility-First Enrichment Waterfall and Honest Outreach Economics",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Local mapping P11, eligibility-first enrichment, starts with organizations "
                    "that plausibly buy housing: relocation departments, contracted housing "
                    "coordinators, and employers with documented temporary assignments. Use "
                    "a company website and existing relationship records first, a licensed "
                    "business-contact source second, and verification only for addresses "
                    "the desk may legitimately process. Hunter's domain search and verifier "
                    "can support that sequence, but neither proves recipient interest, "
                    "deliverability, or permission under a mail provider's rules. Store "
                    "source provenance, role relevance, last verification time, suppression "
                    "status, and the reason for contact. An illustrative waterfall of "
                    "1,000 relevant organizations, 600 role matches, 450 usable business "
                    "addresses, and 300 eligible contacts should report 300 contacts, "
                    "not 1,000 enriched leads. Catch-all results are inconclusive; hold "
                    "them for corroboration or omit them instead of treating acceptance "
                    "of arbitrary SMTP recipients as validation. Never harvest policyholder "
                    "contacts from claim material for marketing. If enrichment becomes "
                    "expensive or ambiguous, fall back to an organization's published "
                    "supplier form or switchboard. Evaluate cost per qualified housing "
                    "conversation, not cost per address. An inexpensive dataset becomes "
                    "costly when stale roles cause complaints, suppressions, and wasted "
                    "coordinator time across a small operating desk."
                ),
                (
                    "The supplied play multi_inbox_free_workspace_outbound_clusters is the "
                    "twelfth mapping; the other eleven are chapter-local operating mappings, "
                    "not additional supplied catalog identifiers. Its advertised scale needs "
                    "explicit arithmetic and entitlement checks. Three hundred inboxes "
                    "sending twenty messages across twenty-five sending days produce "
                    "150,000 messages; using twenty business days produces 120,000. Across "
                    "the stated fifteen-to-twenty-five daily range, 300 inboxes and twenty-five "
                    "days produce 112,500–187,500 messages. Those are send counts, not primary "
                    "inbox placements or qualified demand. Microsoft developer subscriptions "
                    "depend on current eligibility and development-use terms; they are "
                    "not a general free production outreach entitlement. Partner benefits "
                    "also require the actual agreement. Cloudflare Email Routing forwards "
                    "incoming mail and does not provide outbound SMTP mailboxes. Therefore, "
                    "implement this mapping only with licenses and sending services that "
                    "expressly permit the intended production use. At the supplied retail "
                    "comparison of $6–$12 per mailbox monthly, 300 mailboxes imply "
                    "$1,800–$3,600 monthly before verification, domains, and labor. That "
                    "comparison is planning arithmetic, not a current vendor quote. "
                    "If entitlements fail, reduce scope to licensed relationship outreach "
                    "rather than manufacturing tenants to bypass commercial restrictions."
                ),
                (
                    "Operational controls must protect recipient choice and sender identity, "
                    "not disguise unwanted traffic. Two or three domains per tenant can "
                    "be an internal administrative cap, but it does not authorize sending "
                    "or override platform rules. Remove open pixels and click redirects "
                    "to minimize unnecessary tracking; the message still needs truthful "
                    "headers, an accurate subject, required sender information, and a "
                    "working opt-out under 15 U.S.C. Section 7704. Honor opt-outs within "
                    "the statutory period and suppress them immediately in the desk's "
                    "own queue. Do not claim that checking every address through SMTP "
                    "eliminates catch-all uncertainty. Do not rotate standby domains to "
                    "evade complaints, blocks, or provider enforcement; pause the affected "
                    "campaign and repair eligibility, targeting, and authentication instead. "
                    "A replacement domain belongs in documented outage recovery, with "
                    "suppression history preserved, not reputation laundering. Use Microsoft "
                    "Graph for authorized mailbox workflows, Postmark for permitted "
                    "transactional notices, and Amazon SES only for use approved by "
                    "its current service policies and account permissions. If the "
                    "licensed sender cannot support a campaign, use approved supplier "
                    "introductions and direct account development. A small housing desk "
                    "wins through credible available inventory and responsive quotes, "
                    "not an impressive mailbox count."
                ),
            ],
            "table": {
                "caption": "Named Resource Directory, Entries 13–18: Identity, Enrichment, and Messaging",
                "headers": [
                    "Named resource and operating purpose",
                    "Exact access method and evidence",
                    "Cost tier and refresh discipline",
                    "Rate-limit hygiene and fallback source",
                ],
                "rows": [
                    [
                        "13. Microsoft Graph for licensed shared-workflow mailbox access",
                        "Use https://graph.microsoft.com/v1.0/ with tenant-approved OAuth scopes; consult https://learn.microsoft.com/graph/ for message and subscription operations.",
                        "Production mailbox licensing and current API terms govern cost; renew change subscriptions before expiry and run scheduled reconciliation.",
                        "Honor Retry-After and service-specific throttles; use the licensed mailbox interface during outages without creating bypass tenants.",
                    ],
                    [
                        "14. Cloudflare Email Routing for inbound alias forwarding",
                        "Use the Cloudflare dashboard or https://api.cloudflare.com/client/v4/accounts/{account_id}/email/routing/addresses for documented destination-address management.",
                        "Standard Email Routing has a free service tier under current product terms; domain registration and destination mailbox costs remain separate.",
                        "Respect account API limits and confirm destination verification; receive directly at the destination mailbox when forwarding is disrupted.",
                    ],
                    [
                        "15. Hunter Domain Search for licensed business-role discovery",
                        "GET https://api.hunter.io/v2/domain-search and the documented email-verifier endpoint with an authorized API key and permitted business addresses.",
                        "Free and paid credit tiers differ; check current allowances and reverify selected records before use rather than repeatedly buying duplicates.",
                        "Throttle against endpoint limits and monthly credits; use published company contacts when catch-all results or weak provenance prevent confident matching.",
                    ],
                    [
                        "16. Postmark for permitted transactional placement communications",
                        "POST https://api.postmarkapp.com/email using a server token and appropriate message stream; configure documented delivery and bounce webhooks.",
                        "Subscription and volume tiers govern cost; event callbacks support prompt processing but do not establish recipient reading or inbox placement.",
                        "Follow stream rules and current rate guidance; use approved operational contact channels after failure rather than moving cold campaigns here.",
                    ],
                    [
                        "17. Amazon Simple Email Service for approved sending workloads",
                        "Use the documented regional SES API with signed AWS requests; inspect account sending status and quotas before submitting messages.",
                        "Usage-based regional pricing applies; sandbox restrictions and production quotas differ, so obtain account-specific authorization before scheduling volume.",
                        "Stay inside daily and per-second quotas and process suppression events; pause rejected workloads instead of switching accounts to bypass limits.",
                    ],
                    [
                        "18. Google Admin Toolbox CheckMX for domain setup verification",
                        "Open https://toolbox.googleapps.com/apps/checkmx/ and inspect the sending domain; corroborate results with authoritative DNS queries.",
                        "Public diagnostic access has no subscription charge; DNS TTL and resolver caching determine when changed records become observable.",
                        "Use targeted manual diagnostics rather than bulk scraping; fall back to authoritative DNS answers and the sender's authentication reports.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify the four conditions before enabling a connector or campaign",
                "body": "A working credential proves technical access; it does not establish permitted use, current facts, or safe operating economics.",
                "items": [
                    "Confirm that supplier, mailbox, enrichment, and sending agreements expressly cover the intended production workload and data processing.",
                    "Verify the signed landlord sublease addendum, municipal jurisdiction, condition inspection, and applicable occupancy-tax evidence for every offered property.",
                    "Test suppression, truthful sender identity, authentication, bounce handling, and the campaign pause procedure before sending any commercial outreach.",
                    "Demonstrate stale-data detection, credential revocation, backup restoration, and coordinator-led reconciliation before allowing automatic booking or billing actions.",
                ],
            },
        },
        {
            "heading": "4. Instrument Exceptions and Reconcile Every Dashboard to the Scorecard",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Use a small evidence architecture before purchasing a large automation "
                    "stack. A single-writer SQLite database can support an early desk; "
                    "move to managed PostgreSQL when concurrent workflows justify the "
                    "operational change. Keep separate property, authority, placement, "
                    "reservation, invoice, receipt, device, and contact-suppression records. "
                    "A source identifier is not a universal identifier: retain a mapping "
                    "table and reject ambiguous joins. For every inbound object, record "
                    "source_updated_at, observed_at, schema_version, payload_hash, and "
                    "processing_status. Encrypt sensitive documents, limit household data "
                    "to staff who need it, and avoid storing claim narratives when dates "
                    "and approved housing requirements suffice. Design retries around "
                    "idempotency: a duplicate webhook must not create another invoice "
                    "or guest credential. For illustration, processing 200 events with "
                    "ten duplicate deliveries should produce 190 unique effects if those "
                    "duplicates repeat ten distinct originals. A dead-letter queue holds "
                    "records needing operator intervention without silently discarding "
                    "them. Bound retry attempts, log redacted error details, and preserve "
                    "the original event for investigation. Keep credentials out of "
                    "spreadsheets and repositories. Test a restore from encrypted backup "
                    "and verify that suppression records survive it before enabling "
                    "outbound processing after recovery."
                ),
                (
                    "The scorecard bridge must remain explicit. Conservative gross billings "
                    "of $180,000 less $99,000 of modeled landlord rent and utility "
                    "pass-throughs leave $81,000 retained; subtracting $59,400 of remaining "
                    "modeled expenses yields $21,600 owner profit. Base gross billings "
                    "of $790,000 less $434,500 leave $355,500 retained; subtracting "
                    "$205,400 yields $150,100. Scaled gross billings of $1,400,000 "
                    "less $770,000 leave $630,000 retained; subtracting $266,000 yields "
                    "$364,000. These produce gross-billings net margins of 12%, "
                    "19.0%, and 26%, and retained net margins of 26.67%, 42.22%, "
                    "and 57.78%, respectively. Preserve the teams: one full-time operator "
                    "plus three contractors in Conservative and Base, then two full-time "
                    "operators plus four contractors in Scaled. The scorecard uses a "
                    "45% retained-share presentation associated with ASC 606 analysis; "
                    "actual gross-versus-net recognition depends on contract-specific "
                    "principal-versus-agent conclusions. Maintain gross billings, modeled "
                    "retained revenue, and booked accounting revenue as separate fields. "
                    "Do not recognize the carrier's claim reserve, underlying property "
                    "value, or unused housing authorization as operator revenue. The "
                    "remaining expense envelopes are derived reconciliations, not a "
                    "new assertion that software, labor, and every cash payment share "
                    "one monthly timing pattern."
                ),
                (
                    "Measure tooling against contribution and response quality, not record "
                    "volume. An illustrative $600 monthly software bundle costs $7,200 "
                    "annually; include it within the existing expense envelope or show "
                    "an explicit variance rather than silently subtracting it twice. "
                    "At the illustrative $2,025 retained monthly placement contribution, "
                    "that bundle requires about 3.56 additional occupied unit-months "
                    "to cover its annual cost before incremental operating expenses. "
                    "A vacancy gap of ten nights at $150 per night removes $1,500 "
                    "of potential billings, but the profit effect depends on unavoidable "
                    "landlord rent and saved variable costs; applying 45% mechanically "
                    "would conceal lease exposure. Track quote response time, approval-to-move-in "
                    "conversion, stale inventory, unpaid approved extensions, failed access "
                    "issuance, and unresolved water alerts. Establish an owner for each "
                    "exception and record the next action deadline. Separate startup "
                    "capital of $12,000–$60,000 from the $3,000–$18,000 monthly opex "
                    "planning range and the annual scorecard's accounting bridge; cash "
                    "deposits, payment timing, and pass-through treatment can differ. "
                    "Keep the one-to-three-month first-deal expectation visible in the "
                    "cash plan. If a tool cannot demonstrate fewer exceptions, faster "
                    "verified quotes, or lower collection friction, remove it before "
                    "adding another subscription."
                ),
            ],
            "table": {
                "caption": "Eight Operating Controls: Diagnostic Evidence, Exact Economics, and Recovery Actions",
                "headers": [
                    "Control and specific operating objective",
                    "Concrete test or canonical calculation",
                    "Evidence retained by the operating desk",
                    "Failure response and responsible human action",
                ],
                "rows": [
                    [
                        "Conservative bridge protects the smallest team's actual profit",
                        "$180,000 gross minus $99,000 pass-throughs minus $59,400 remaining expenses equals $21,600 annual owner profit.",
                        "Retained revenue equals $81,000; gross margin equals 12%; retained net margin rounds to 26.67%.",
                        "The owner reconciles category errors before comparing actual results with the one-full-time-plus-three-contractor operating case.",
                    ],
                    [
                        "Base bridge separates customer billings from retained contribution",
                        "$790,000 gross minus $434,500 pass-throughs minus $205,400 remaining expenses equals $150,100 annual owner profit.",
                        "Retained revenue equals $355,500; gross margin equals 19.0%; retained net margin rounds to 42.22%.",
                        "The owner traces every unexplained variance to occupancy, pricing, pass-through classification, or remaining expenses before changing targets.",
                    ],
                    [
                        "Scaled bridge preserves six-person small-team operating discipline",
                        "$1,400,000 gross minus $770,000 pass-throughs minus $266,000 remaining expenses equals $364,000 annual owner profit.",
                        "Retained revenue equals $630,000; gross margin equals 26%; retained net margin rounds to 57.78%.",
                        "The two-full-time-plus-four-contractor team reviews workload concentration before allowing added automation to create unowned exception queues.",
                    ],
                    [
                        "curl and Python unittest validate connector behavior safely",
                        "Replay redacted fixtures containing duplicate events, stale revisions, permission errors, and throttling responses against an isolated test endpoint.",
                        "Save expected state transitions, request identifiers, redacted response headers, and assertions proving repeated delivery creates no duplicate charge.",
                        "The connector owner disables consequential writes while preserving read-only visibility and completes the approved manual reconciliation route.",
                    ],
                    [
                        "Authoritative DNS and message headers verify sender configuration",
                        "Use dig or nslookup to inspect MX, SPF, DKIM selectors, and DMARC, then examine delivered-message authentication results.",
                        "Retain timestamped DNS answers and redacted headers; distinguish authentication success from recipient interest and inbox placement.",
                        "The messaging owner pauses affected sending, corrects identity configuration, and preserves recipient suppression across every recovery action.",
                    ],
                    [
                        "Webhook inspection and queue age reveal silent operational loss",
                        "Validate provider signatures, compare event counts with source exports, and alert when pending placement changes exceed the desk's response target.",
                        "Keep source timestamps, arrival timestamps, event hashes, retry counts, and documented ownership of every unresolved exception.",
                        "The duty operator confirms live placement status with the coordinator and prevents stale records from creating new commitments.",
                    ],
                    [
                        "Physical access and sensor drills expose property-level failure",
                        "Test one authorized credential issuance, one offline-device scenario, and one synthetic water-alert workflow without disturbing occupied units.",
                        "Record command acknowledgment, actual device response, responder contact, guest notice method, and documented access fallback availability.",
                        "The property responder follows the access or incident procedure; billing disputes never trigger automatic occupied-dwelling lockout.",
                    ],
                    [
                        "Backup restoration and ledger matching protect continuity and cash",
                        "Restore an encrypted backup into an isolated environment and match sampled invoices, bank receipts, placement approvals, and suppression records.",
                        "Document recovery duration, missing-event recovery, unapplied receipts, access restrictions, and comparison against the last reconciled source snapshot.",
                        "The owner resumes consequential automation only after resolving conflicting states and confirming that restored suppression prevents repeated outreach.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "The housing desk with the best information is the one that can prove authority, availability, payer approval, and contribution before promising a single night.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Build ten property evidence packets linking normalized address, parcel identifier, recorded ownership evidence, condition inspection, and signed corporate-housing sublease authority.",
        "Register all eighteen directory resources with an access owner, permitted purpose, current cost terms, source latency, polling target, and tested fallback.",
        "Obtain ALE Solutions and CRS Temporary Housing supplier instructions directly; map placement revisions to booking states without assuming public API access.",
        "Implement extension approval, utility-cap evidence, receipt allocation, and time-bounded access as separate auditable workflows with named exception owners.",
        "Run an eligibility-first outreach pilot using licensed sending infrastructure, truthful identity, immediate internal suppression, and no domain rotation to bypass enforcement.",
        "Reconcile the three canonical profit bridges, test duplicate-event handling and backup restoration, and demonstrate a complete manual placement update during an outage drill.",
    ],
    "statutory_citations": [
        {
            "title": "15 U.S.C. Section 7704 — Requirements for transmission of messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Commercial email controls include truthful routing and subject information, required sender identification, a functioning opt-out mechanism, and timely honoring of opt-outs.",
        },
        {
            "title": "Texas Tax Code Section 156.101 — Exception for permanent residents",
            "url": "https://statutes.capitol.texas.gov/Docs/TX/htm/TX.156.htm#156.101",
            "relevance": "Evaluate the actual right to occupy and qualifying duration before coding a Texas state hotel-occupancy-tax exception; retain supporting agreements and separately review local treatment.",
        },
        {
            "title": "California Civil Code Section 1941.1 — Tenantable dwelling conditions",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1941.1.",
            "relevance": "California residential inventory requires property-condition evidence addressing applicable dwelling standards, not merely a clean permit search or a landlord's verbal assurance.",
        },
        {
            "title": "47 U.S.C. Section 227 — Restrictions on telephone equipment",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": "Assess calling and messaging requirements against the actual technology, content, recipient relationship, and applicable exceptions before enabling automated guest or prospect communications.",
        },
        {
            "title": "42 U.S.C. Section 3604 — Discrimination in housing",
            "url": "https://www.law.cornell.edu/uscode/text/42/3604",
            "relevance": "Do not use property enrichment, household requirements, or automated placement rules to make prohibited housing distinctions; review accommodations and placement criteria on their actual facts.",
        },
        {
            "title": "California Civil Code Section 789.3 — Interference with residential occupancy",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=789.3.",
            "relevance": "Smart-lock and utility workflows must not become prohibited self-help measures to terminate residential occupancy; a claim closure or unpaid invoice does not independently authorize access removal.",
        },
    ],
}
