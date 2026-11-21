from __future__ import annotations


def build_volume_008_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-008-commercial-lead-generation",
        "volume_id": "vol-008-commercial-lead-generation",
        "title": "Commercial Lead Generation — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for B2B Vertical Underwriting, "
            "Accepted-Appointment Economics, Multi-Inbox Execution, Outreach "
            "Controls, CRM Routing, and a Transferable Small-Team Revenue Engine"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Vertical Underwriting and Counterparty Qualification",
                "purpose": (
                    "Select a commercial niche where verified buyer demand, client "
                    "delivery capacity, and measurable appointment acceptance support "
                    "repeatable operator revenue. Document counterparty evidence, "
                    "qualification boundaries, territory rights, and rejection rules "
                    "before committing staff time, purchasing contact data, or "
                    "activating outbound infrastructure."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Choose one initial vertical and one serviceable territory. "
                        "Interview three prospective clients and five target buyers "
                        "about actual purchasing triggers, budget ownership, and "
                        "vendor selection. Record dated evidence rather than treating "
                        "a large contact database as demonstrated demand."
                    ),
                    (
                        "Underwrite the paying client separately from the prospect "
                        "population. Verify entity identity, service capacity, payment "
                        "authority, complaint history, and relevant trade licenses. "
                        "A client unable to fulfill appointments will convert apparent "
                        "campaign success into disputes and churn."
                    ),
                    (
                        "Translate the offer into observable acceptance conditions "
                        "that both parties can reproduce from CRM records. Separate "
                        "contact eligibility, meeting attendance, commercial fit, and "
                        "sales conversion; the agency should not invoice an unheld "
                        "meeting as a qualified appointment."
                    ),
                    (
                        "Inspect a small, documented contact sample before buying "
                        "the full list. Trace source provenance, suppression status, "
                        "job relevance, business location, and channel restrictions. "
                        "Reject suppliers that cannot explain collection methods "
                        "or contractually support correction and deletion requests."
                    ),
                    (
                        "Complete the counterparty and vertical decision using "
                        "evidence references, named owners, and explicit stop conditions. "
                        "Treat the published opportunity score as a screening input, "
                        "not proof that a particular client, geography, or acquisition "
                        "channel will produce acceptable economics."
                    ),
                ],
                "fields": [
                    field(
                        "Vertical thesis and purchase trigger",
                        "textarea",
                        (
                            "Define the commercial service, buyer role, geography, "
                            "purchase trigger, and typical procurement interval. Explain "
                            "why buyers would accept a relevant conversation now, "
                            "using interviews or observable operating events rather "
                            "than broad market-size claims."
                        ),
                        (
                            "Target independent facilities managers overseeing 5–30 "
                            "commercial buildings in greater Atlanta. The offer is "
                            "an appointment with a licensed commercial HVAC contractor "
                            "about preventive-maintenance renewal. Three client interviews "
                            "identified contracts expiring within 120 days as the "
                            "strongest purchasing trigger; residential replacement "
                            "requests remain outside scope."
                        ),
                    ),
                    field(
                        "Candidate score and operating constraints",
                        "textarea",
                        (
                            "Record the canonical candidate identity, score components, "
                            "startup envelope, operating-cost range, and first-deal horizon. "
                            "Translate these portfolio-level indicators into a specific "
                            "resource limit without substituting them for client-level "
                            "underwriting or actual campaign results."
                        ),
                        (
                            "Candidate #18 ranks #08 of 29: Commercial Lead Generation "
                            "scores 85/100, labeled Elite Small-Team Cash Machine. "
                            "Components are 21 revenue, 21 margin, 18 team efficiency, "
                            "12 accessibility, and 13 automation. Screening ranges are "
                            "$5,000–$40,000 startup, $2,000–$12,000 monthly opex, and "
                            "1–4 months to first deal; scaled all-in costs require "
                            "separate budgets."
                        ),
                    ),
                    field(
                        "Client identity and payment authority",
                        "textarea",
                        (
                            "Identify the contracting entity, authorized signer, payment "
                            "contact, operating address, and verification evidence. Separate "
                            "the brand name from the legal counterparty and document "
                            "who can approve invoices, resolve disputes, and authorize "
                            "changes to campaign scope."
                        ),
                        (
                            "Illustrative client Peachtree Commercial Mechanical LLC "
                            "contracts under its registered entity name, not its "
                            "advertising brand. The operations director signs under "
                            "documented delegated authority; accounts payable confirms "
                            "ACH details by a known telephone number. The onboarding "
                            "packet retains registry evidence, tax documentation, and "
                            "the signed services schedule."
                        ),
                    ),
                    field(
                        "Client fulfillment capacity and service credentials",
                        "textarea",
                        (
                            "Verify the client's capacity to answer routed calls, attend "
                            "appointments, issue proposals, and deliver the advertised "
                            "service. Record relevant license checks and operational "
                            "limits so lead volume never outruns the client's ability "
                            "to serve qualified buyers."
                        ),
                        (
                            "The contractor allocates two estimators and eight "
                            "appointment slots weekly, with a two-business-day proposal "
                            "target. The account owner verifies applicable Georgia "
                            "conditioned-air credentials through the state licensing "
                            "board. Dispatch confirms a 40-mile service radius; "
                            "overflow requests are paused rather than sold into "
                            "unavailable calendar capacity."
                        ),
                    ),
                    field(
                        "Ideal customer and exclusion boundaries",
                        "textarea",
                        (
                            "Specify required account attributes, relevant decision-maker "
                            "roles, geographic boundaries, and explicit exclusions. Include "
                            "rules for franchise ownership, existing customers, public "
                            "procurement, and sensitive personal information where those "
                            "factors change qualification, routing, or the permitted "
                            "outreach method."
                        ),
                        (
                            "Eligible accounts operate at least five commercial "
                            "properties, have a facilities or operations decision-maker, "
                            "and expect maintenance procurement within 120 days. "
                            "Exclude residential owners, existing client customers, "
                            "staff recruitment inquiries, and buyers outside the "
                            "service radius. Municipal accounts enter a separate "
                            "procurement workflow rather than the standard appointment offer."
                        ),
                    ),
                    field(
                        "Billable appointment acceptance definition",
                        "textarea",
                        (
                            "Write an acceptance rule covering attendance, buyer "
                            "authority, account fit, expressed interest, required "
                            "evidence, and review timing. Identify which conditions "
                            "are objectively measurable and prevent sales outcomes "
                            "outside agency control from becoming retrospective "
                            "rejection reasons."
                        ),
                        (
                            "A $100 appointment fee applies only after a meeting "
                            "is held with an eligible account's responsible buyer "
                            "and renewal interest is documented. A scheduled but "
                            "unattended meeting earns no fee. The client reviews "
                            "evidence within five business days; failure to close "
                            "a sale is not a qualification defect."
                        ),
                    ),
                    field(
                        "Data provenance and permitted channel evidence",
                        "textarea",
                        (
                            "Describe the source, collection date, supplier permissions, "
                            "contact attributes, and available channel evidence for "
                            "each prospect cohort. Distinguish business relevance from "
                            "permission to use a particular dialing method, recording "
                            "feature, or automated communication technology."
                        ),
                        (
                            "A 200-record evaluation sample contains company-domain "
                            "addresses and role descriptions supplied under a documented "
                            "data license. Twenty-six stale or irrelevant records are "
                            "removed. Vendor claims of universal telephone permission "
                            "are rejected; mobile-number outreach remains disabled "
                            "until the intended calling method and supporting evidence "
                            "have been reviewed."
                        ),
                    ),
                    field(
                        "Territory rights and duplicate ownership",
                        "textarea",
                        (
                            "Define exclusivity, account ownership, duplicate lookback "
                            "periods, and treatment of overlapping client territories. "
                            "Specify the identity keys used to detect an existing "
                            "relationship and the evidence needed before sharing "
                            "the same buyer with another paying client."
                        ),
                        (
                            "The contract grants no market-wide exclusivity. A "
                            "90-day account lookback uses normalized company domain "
                            "plus service location; existing opportunities supplied "
                            "before launch are excluded. One buyer request routes "
                            "to one contracted provider unless the buyer explicitly "
                            "requests alternatives and the applicable data-sharing "
                            "terms permit that additional disclosure."
                        ),
                    ),
                    field(
                        "Pilot evidence and commercial offer",
                        "textarea",
                        (
                            "Design a bounded pilot with a fixed service period, "
                            "retainer, accepted-appointment fee, reporting cadence, and "
                            "client responsibilities. State the evidence needed to "
                            "continue without promising revenue, ranking improvements, "
                            "or a meeting volume unsupported by observed demand."
                        ),
                        (
                            "Offer a 30-day pilot at a $4,000 retainer plus "
                            "$100 per accepted held appointment. The client supplies "
                            "suppression records, calendar capacity, and qualification "
                            "feedback before launch. Weekly reviews inspect delivery "
                            "and acceptance evidence; media purchases are client-funded "
                            "and excluded from recognized operator revenue in this model."
                        ),
                    ),
                    field(
                        "Underwriting decision and stop conditions",
                        "textarea",
                        (
                            "Record the accountable decision-maker, evidence reviewed, "
                            "unresolved dependencies, spending ceiling, and stop conditions. "
                            "Use observable criteria for proceeding or declining so "
                            "commercial enthusiasm cannot override missing authority, "
                            "unverifiable claims, or deficient client service capacity."
                        ),
                        (
                            "Proceed with one client after entity verification, "
                            "executed terms, and eight weekly calendar slots are "
                            "confirmed. Cap pilot preparation spending at $2,000. "
                            "Stop if the client requests misleading service claims, "
                            "cannot substantiate required credentials, or rejects "
                            "three documented appointments for reasons outside the "
                            "agreed acceptance definition."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The owner signs a dated underwriting record containing verified "
                    "counterparty authority, service capacity, source provenance, "
                    "objective appointment criteria, a pilot spending cap, and "
                    "named owners for every remaining dependency."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Defect Reserve, and Cash Float Calculator",
                "purpose": (
                    "Reconcile retainers and accepted-appointment fees to the three "
                    "canonical annual scenarios while separating client advertising "
                    "funds from operator revenue. Calculate rejection exposure, "
                    "delivery contribution, staffing costs, receivable timing, and "
                    "minimum cash so profitable reporting cannot conceal an "
                    "unfunded operating cycle."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Start with the canonical annual revenue and owner-profit "
                        "figures, then build explicit retainer and accepted-appointment "
                        "bridges. Label every other calculation as an operating "
                        "illustration or sensitivity rather than silently replacing "
                        "the Conservative, Base, or Scaled Small-Team scenario."
                    ),
                    (
                        "Keep submitted appointments, accepted appointments, client "
                        "advertising funds, invoices, recognized revenue, and collected "
                        "cash in separate columns. A booked calendar event does "
                        "not become fee revenue until the contractual acceptance "
                        "conditions and the applicable recognition requirements "
                        "are satisfied."
                    ),
                    (
                        "Estimate scrub losses from a documented cohort and hold "
                        "sufficient liquidity for disputes and rework. Distinguish "
                        "a cash reserve from an expense, and distinguish excluded "
                        "billings from credits against previously recognized revenue "
                        "to prevent counting the same defect twice."
                    ),
                    (
                        "Construct a dated cash schedule using actual payment "
                        "terms, not annual profit divided by twelve. Include "
                        "setup spending, payroll, contractor commitments, collection "
                        "delays, client concentration, and the earliest point when "
                        "a client-funded advertising balance could create a "
                        "restricted-funds shortfall."
                    ),
                    (
                        "Stress-test one variable at a time before combining "
                        "downside cases. Assign an owner to each corrective action, "
                        "and preserve the canonical scenario table unchanged so "
                        "the sensitivity analysis remains distinguishable from "
                        "the published operating opportunity and its staffing assumptions."
                    ),
                ],
                "fields": [
                    field(
                        "Revenue recognition and pass-through boundary",
                        "textarea",
                        (
                            "Define the services represented by retainers and appointment "
                            "fees, their recognition conditions, and the treatment of "
                            "client-funded advertising. Identify which cash movements "
                            "belong in revenue, receivables, deferred service balances, "
                            "or separate client-funds records."
                        ),
                        (
                            "Recognize the $4,000 monthly retainer as contracted "
                            "services are delivered and the $100 appointment fee "
                            "after documented acceptance. A client's $6,000 advertising "
                            "budget is excluded from this workbook's operator revenue; "
                            "the client preferably pays platforms directly. Any agency-held "
                            "media cash receives a separate liability and reconciliation record."
                        ),
                    ),
                    field(
                        "Conservative annual scenario bridge",
                        "textarea",
                        (
                            "Reproduce Conservative revenue, margin, owner net profit, "
                            "and staffing exactly. Build a transparent annual revenue "
                            "bridge using retained accounts and accepted appointment "
                            "fees, then derive the total expense ceiling without "
                            "including client media spending."
                        ),
                        (
                            "Four clients paying $1,500 monthly produce $72,000 "
                            "in annual retainers; 280 accepted appointments at $100 "
                            "add $28,000. Gross revenue is $100,000. Expenses of "
                            "$80,000 leave $20,000 annual owner net profit at "
                            "20% margin. Staffing remains 1 FT plus 3 C; "
                            "contractor hours flex with demand."
                        ),
                    ),
                    field(
                        "Base annual scenario bridge",
                        "textarea",
                        (
                            "Reproduce Base revenue, margin, owner net profit, and "
                            "staffing exactly. Connect the annual appointment volume "
                            "to retainer revenue and show how excluded submissions "
                            "affect billable units rather than inflating recognized "
                            "service revenue."
                        ),
                        (
                            "Five clients at $4,000 monthly generate $240,000 "
                            "in retainers. Of 2,056 submitted appointment outcomes, "
                            "206 fail acceptance and 1,850 earn $100 each, "
                            "adding $185,000. Gross revenue is $425,000; expenses "
                            "are $297,500; owner net profit is $127,500 at "
                            "30.0%, with 1 FT plus 3 C."
                        ),
                    ),
                    field(
                        "Scaled Small-Team annual scenario bridge",
                        "textarea",
                        (
                            "Reproduce Scaled Small-Team revenue, margin, owner net "
                            "profit, and six-person staffing exactly. Specify the "
                            "client and accepted-appointment mix while keeping higher "
                            "operating capacity distinct from advertising pass-through "
                            "or the underlying value of client sales."
                        ),
                        (
                            "Ten clients at $4,000 monthly generate $480,000 "
                            "in retainers; 2,700 accepted appointments at $100 "
                            "add $270,000. Gross revenue equals $750,000. Expenses "
                            "of $450,000 leave $300,000 annual owner net profit "
                            "at 40%. Staffing is 2 FT plus 4 C, "
                            "six people total, with explicitly scheduled contractor capacity."
                        ),
                    ),
                    field(
                        "Base expense allocation and owner-profit definition",
                        "textarea",
                        (
                            "Allocate the Base expense ceiling across labor, acquisition, "
                            "software, administration, and remediation. State whether "
                            "owner operating compensation is already included, and "
                            "avoid subtracting distributions or a liquidity reserve "
                            "as another operating expense."
                        ),
                        (
                            "Allocate $108,000 to three contractors, $39,500 to "
                            "the full-time operating role, $72,000 to agency acquisition, "
                            "$36,000 to software and data, $24,000 to administration, "
                            "and $18,000 to remediation. Total expenses equal "
                            "$297,500. The $127,500 residual follows the included "
                            "operating-role compensation; owner distributions do not "
                            "reduce profit again."
                        ),
                    ),
                    field(
                        "Scrub rate and fee reserve",
                        "textarea",
                        (
                            "Calculate the rejected-submission rate, excluded fee value, "
                            "and temporary cash holdback. Explain how rejection decisions "
                            "flow into invoicing and why the reserve must not "
                            "be deducted again from already netted accepted-unit "
                            "revenue or remediation expenses."
                        ),
                        (
                            "The Base cohort rejects 206 of 2,056 submissions, "
                            "a 10.02% defect rate. Excluded fees equal $20,600 "
                            "and never enter the $185,000 accepted-fee total. "
                            "A temporary 12% liquidity holdback on $205,600 "
                            "of potential fees is $24,672; release it after "
                            "review closure rather than expensing it automatically."
                        ),
                    ),
                    field(
                        "Accepted-unit contribution and acquisition burden",
                        "textarea",
                        (
                            "Calculate appointment-level contribution using a clearly "
                            "defined subset of delivery costs, then show the "
                            "retainer contribution separately. Identify excluded "
                            "overhead so a useful marginal delivery metric is "
                            "not misrepresented as fully loaded net margin."
                        ),
                        (
                            "For an illustrative delivery cohort, 150 accepted "
                            "appointments generate $15,000 in fees. At $45 "
                            "direct fulfillment cost each, contribution is $8,250, "
                            "or 55%, before acquisition, software, and administration. "
                            "The associated five retainers add $20,000 separately. "
                            "This $35,000 cohort is not substituted for the "
                            "canonical Base annual revenue."
                        ),
                    ),
                    field(
                        "Receivable timing and minimum cash float",
                        "textarea",
                        (
                            "Model opening unrestricted cash, retainer collection dates, "
                            "appointment invoicing dates, customer payment terms, and "
                            "monthly cash operating costs. Calculate the lowest "
                            "balance before fee collections and identify the "
                            "funding source supporting that interval."
                        ),
                        (
                            "Fund $30,000 initially, spend $8,000 on setup, "
                            "and retain $22,000 working cash. Two months of "
                            "Base expenses at $24,791.67 total $49,583.34; "
                            "two prepaid retainer collections total $40,000. "
                            "Cash falls to $12,416.66 before fees arrive "
                            "on day 75 under 45-day terms after month-end invoicing."
                        ),
                    ),
                    field(
                        "Client loss and acquisition-cost sensitivity",
                        "textarea",
                        (
                            "Quantify revenue concentration and test a client departure "
                            "alongside a separate increase in agency acquisition "
                            "spending. Hold other assumptions explicit, calculate "
                            "the residual profit, and identify corrective actions "
                            "without relabeling the canonical Base result."
                        ),
                        (
                            "One equally sized Base client represents $85,000 "
                            "annual revenue: $48,000 retainer plus $37,000 "
                            "appointment fees. Losing that client for a full "
                            "year with unchanged costs reduces profit to $42,500. "
                            "Separately, a 20% increase on $72,000 acquisition "
                            "spending costs $14,400; combined residual profit "
                            "would be $28,100."
                        ),
                    ),
                    field(
                        "Cash release and pricing decision",
                        "textarea",
                        (
                            "Set numerical thresholds for minimum cash, defect exposure, "
                            "collection delays, and pricing review. Explain who "
                            "can release reserved funds or change commercial "
                            "terms, using evidence that separates temporary timing "
                            "pressure from structurally unprofitable delivery."
                        ),
                        (
                            "Maintain at least $10,000 unrestricted operating cash "
                            "after committed payments and separately track any "
                            "unresolved fee reserve. The owner reviews pricing "
                            "when accepted-unit direct cost exceeds $60 for "
                            "two cohorts or defects exceed 15%. Reserve release "
                            "requires reconciled acceptance records, settled disputes, "
                            "and a refreshed thirteen-week cash forecast."
                        ),
                    ),
                ],
                "completion_gate": (
                    "All three annual scenarios reconcile exactly, pass-through "
                    "funds remain outside operator revenue, defect losses appear "
                    "only once, and a dated cash forecast demonstrates funding "
                    "above the chosen minimum under the stated collection delay."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "Execution Ledger and Technical QA Pre-Flight",
                "purpose": (
                    "Build a reproducible path from approved source records to "
                    "accepted appointments and reconciled invoices. Validate "
                    "sender identity, suppression checks, CRM state changes, "
                    "calendar ownership, call handling, and evidence retention "
                    "before live delivery so failures remain detectable, "
                    "reversible, and attributable."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Draw the complete record lifecycle before configuring "
                        "integrations. Give every prospect, campaign, appointment, "
                        "acceptance decision, and invoice line a stable identifier. "
                        "Define the system of record for each object so "
                        "a webhook retry cannot create another billable event."
                    ),
                    (
                        "Inspect domain ownership, authentication, mailbox access, "
                        "provider policies, suppression propagation, and recipient "
                        "visibility before sending. Use internal seed accounts "
                        "for testing; do not manufacture engagement or rotate "
                        "identities to overcome recipient objections or provider "
                        "enforcement actions."
                    ),
                    (
                        "Run both the happy path and adverse cases through "
                        "CRM routing and scheduling. Test duplicate records, "
                        "canceled meetings, disconnected calls, missing permission "
                        "evidence, timezone errors, occupied calendars, and service "
                        "outages before relying on automation for client delivery."
                    ),
                    (
                        "Reconcile appointment evidence against the contract before "
                        "creating an invoice. Preserve rejection reasons and "
                        "credit history instead of deleting inconvenient records. "
                        "Require a second person to review a sample of "
                        "accepted units and every material adjustment during "
                        "the initial pilot."
                    ),
                    (
                        "Finish with an operational handoff containing monitoring "
                        "owners, incident contacts, rollback procedures, and "
                        "a documented pause mechanism. Technical success means "
                        "the workflow handles failures safely, not merely "
                        "that one test message arrived or one appointment "
                        "appeared on a calendar."
                    ),
                ],
                "fields": [
                    field(
                        "Object identifiers and lifecycle states",
                        "textarea",
                        (
                            "Define stable identifiers and allowed transitions for "
                            "prospects, outreach attempts, appointments, client decisions, "
                            "and billing events. Identify the authoritative datastore "
                            "and prohibit state changes that would bypass suppression, "
                            "qualification evidence, or documented service completion."
                        ),
                        (
                            "HubSpot stores account AC-1042, contact CT-8831, "
                            "and appointment AP-0207. Allowed appointment states "
                            "are scheduled, held, submitted, accepted, rejected, "
                            "and credited, with cancellations tracked explicitly. "
                            "Invoice line INV-104-07 references AP-0207 once. "
                            "A canceled meeting cannot transition directly to "
                            "accepted without a newly evidenced held appointment."
                        ),
                    ),
                    field(
                        "Sending domains and mailbox inventory",
                        "textarea",
                        (
                            "List owned domains, authorized mailboxes, responsible staff, "
                            "authentication status, and provider usage restrictions. "
                            "Explain how the inventory supports clear sender "
                            "identity and capacity management without using extra "
                            "inboxes to bypass restrictions or disguise a sender."
                        ),
                        (
                            "The pilot uses one clearly branded agency domain "
                            "and three named Google Workspace mailboxes. Cloudflare "
                            "DNS records document SPF, DKIM, and DMARC alignment. "
                            "Each mailbox has a named operator and access review "
                            "date. Additional mailboxes require a legitimate staffing "
                            "reason; a provider suspension stops the campaign "
                            "instead of triggering domain rotation."
                        ),
                    ),
                    field(
                        "Message authentication and delivery tests",
                        "textarea",
                        (
                            "Record authentication results, visible sender identity, "
                            "reply handling, link destinations, and unsubscribe behavior "
                            "from controlled tests. Distinguish successful transport "
                            "from inbox placement and avoid using opening metrics "
                            "as proof of interest or channel permission."
                        ),
                        (
                            "Ten internal seed messages across Gmail and Microsoft "
                            "365 show aligned SPF or DKIM and passing DMARC "
                            "in received headers. Replies enter the shared "
                            "assignment queue; unsubscribe links reach the suppression "
                            "endpoint. The operator checks plain-text rendering "
                            "and the postal address. Seed delivery does not "
                            "establish performance for live recipients."
                        ),
                    ),
                    field(
                        "Suppression and duplicate pre-flight",
                        "textarea",
                        (
                            "Specify the final checks executed immediately before "
                            "each contact attempt, including global suppression, "
                            "client exclusions, recent attempts, and duplicate "
                            "account ownership. Explain what happens when a "
                            "required lookup fails or returns conflicting records."
                        ),
                        (
                            "A pre-send check compares normalized email, account "
                            "domain, and telephone identifiers against channel "
                            "suppression and client exclusions. The test set "
                            "includes twelve opted-out contacts and eight duplicates; "
                            "all twenty are blocked. If the suppression service "
                            "times out, sending pauses and the queued task "
                            "requires a fresh check before release."
                        ),
                    ),
                    field(
                        "Routing rules and response ownership",
                        "textarea",
                        (
                            "Document territory selection, qualification filters, "
                            "calendar capacity, primary ownership, and fallback "
                            "routing. Set a measurable response target while "
                            "preventing uncontrolled distribution of one buyer's "
                            "information to multiple clients or unrelated contractor "
                            "workspaces."
                        ),
                        (
                            "Eligible Atlanta requests route to the contracted "
                            "HVAC client's assigned estimator after account "
                            "matching. The response target is fifteen business "
                            "minutes for an inbound inquiry. If both calendars "
                            "are full, the dispatcher offers the next available "
                            "slot; the record is not automatically sold "
                            "to another contractor."
                        ),
                    ),
                    field(
                        "Calendar and meeting evidence",
                        "textarea",
                        (
                            "Define scheduling fields, timezone handling, attendance "
                            "evidence, rescheduling behavior, and no-show treatment. "
                            "Identify the evidence sufficient for appointment "
                            "acceptance without collecting unnecessary meeting "
                            "content or turning a calendar invitation into "
                            "proof that services were delivered."
                        ),
                        (
                            "Calendly stores the buyer's timezone, account ID, "
                            "assigned estimator, and scheduled start. Attendance "
                            "is supported by the estimator's timestamped CRM "
                            "note and meeting participation metadata where available. "
                            "A rescheduled meeting retains its parent reference; "
                            "only the eventual held event can earn the "
                            "$100 fee. No-show invitations earn zero."
                        ),
                    ),
                    field(
                        "Call routing and recording configuration",
                        "textarea",
                        (
                            "Specify the authorized call flow, caller identity, "
                            "routing destination, metadata captured, and recording "
                            "state. Describe how the system handles consent "
                            "requirements, unavailable agents, dropped transfers, "
                            "and recipients who request that future calls stop."
                        ),
                        (
                            "Twilio routes requested inbound calls to the "
                            "client's service desk using verified numbers. "
                            "Recording is disabled by default. A dropped "
                            "transfer creates a service ticket, not an accepted "
                            "appointment. Agents log stop requests immediately; "
                            "recording can be enabled only for an approved "
                            "jurisdictional workflow with the required participant agreement."
                        ),
                    ),
                    field(
                        "Webhook integrity and retry behavior",
                        "textarea",
                        (
                            "Define authentication, secret storage, deduplication keys, "
                            "retry limits, and failure handling for integration "
                            "events. State how an operator verifies that "
                            "replayed or out-of-order messages cannot create "
                            "duplicate appointments, invoices, or unauthorized "
                            "state transitions."
                        ),
                        (
                            "The receiver validates Twilio request signatures "
                            "using the provider's documented procedure and retrieves "
                            "secrets from a managed vault. Event IDs receive "
                            "unique database constraints. Three failed deliveries "
                            "enter a review queue. Replaying AP-0207's acceptance "
                            "event five times leaves one accepted appointment "
                            "and one invoice line."
                        ),
                    ),
                    field(
                        "Invoice ledger and evidence reconciliation",
                        "textarea",
                        (
                            "Define invoice-line inputs, reviewer responsibilities, "
                            "acceptance references, dispute codes, and credit "
                            "handling. Reconcile operational units to accounting "
                            "totals and preserve a traceable correction record "
                            "when an accepted appointment is subsequently "
                            "found defective."
                        ),
                        (
                            "The monthly ledger contains 150 accepted appointment "
                            "IDs at $100, totaling $15,000, plus five "
                            "$4,000 retainers totaling $20,000. The illustrative "
                            "invoice total is $35,000. QuickBooks entries reference "
                            "the exported acceptance register. A later duplicate "
                            "creates a linked $100 credit rather than "
                            "silently removing the original line."
                        ),
                    ),
                    field(
                        "Pre-flight test matrix and rollback owner",
                        "textarea",
                        (
                            "List the minimum test cases, expected outcomes, "
                            "observed evidence, responsible reviewer, and rollback "
                            "procedure. Include failure cases involving suppression, "
                            "access control, duplicate billing, client routing, "
                            "and integration outages rather than testing only "
                            "successful delivery."
                        ),
                        (
                            "Run thirty controlled cases: ten eligible paths, "
                            "eight duplicates, six suppressed contacts, three "
                            "calendar conflicts, and three webhook failures. "
                            "Expected results are ten routable records and "
                            "zero premature fees. The owner authorizes live "
                            "operation after review; rollback disables campaign "
                            "workers and preserves queued events for reconciliation."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The reviewed test matrix demonstrates correct suppression, "
                    "authentication, routing, idempotency, and billing behavior; "
                    "all failures have owners; and the team can pause outreach "
                    "without losing records or issuing duplicate invoices."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract, and Outreach Audit",
                "purpose": (
                    "Map each outreach channel and data flow to concrete legal "
                    "and contractual operating requirements. Document sender "
                    "identification, opt-outs, calling permissions, privacy rights, "
                    "recording settings, service credentials, and supplier duties "
                    "so a B2B label never substitutes for evaluating the "
                    "actual activity."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Build a jurisdiction map from agency location, client "
                        "location, recipient location, data sources, and communication "
                        "technology. Evaluate email, live calls, automated dialing, "
                        "texts, recording, and resale separately; an exception "
                        "covering one activity does not automatically extend "
                        "to another channel."
                    ),
                    (
                        "Attach primary statutory references and implementation "
                        "evidence to each applicable requirement. Assign an "
                        "owner for current-law verification before activation, "
                        "especially when state telemarketing rules, privacy "
                        "thresholds, registration duties, or vendor restrictions "
                        "depend on facts that differ across clients."
                    ),
                    (
                        "Review actual message templates and call scripts, "
                        "not just a policy document. Verify identification, "
                        "claims, postal information, withdrawal mechanisms, "
                        "and response handling in the live workflow. "
                        "Treat an outsourced sender or caller as "
                        "a managed operational dependency."
                    ),
                    (
                        "Align the contract with the system's real capabilities. "
                        "Specify qualification evidence, rejection periods, "
                        "data roles, permitted channels, client responsibilities, "
                        "payment terms, and termination handling. Do not "
                        "promise exclusive ownership or unrestricted contact "
                        "rights that the source agreements cannot support."
                    ),
                    (
                        "Close every material issue with evidence or disable "
                        "the affected activity while other authorized work "
                        "continues. Preserve a dated applicability decision "
                        "and configuration snapshot so a later reviewer "
                        "can reconstruct which rules governed a particular "
                        "campaign and why."
                    ),
                ],
                "fields": [
                    field(
                        "Jurisdiction and channel applicability register",
                        "textarea",
                        (
                            "Identify the locations and technologies that determine "
                            "applicable requirements. Separate corporate email, "
                            "business landlines, mobile numbers, prerecorded "
                            "messages, SMS, and recorded calls; document "
                            "which activities are enabled and the evidence "
                            "supporting that decision."
                        ),
                        (
                            "The initial campaign targets Georgia business "
                            "email addresses using manually reviewed commercial "
                            "messages. SMS, artificial-voice calls, prerecorded "
                            "calls, and outbound mobile dialing remain disabled. "
                            "The register evaluates 15 U.S.C. § 7704, "
                            "47 U.S.C. § 227, and relevant recipient-state "
                            "rules before any additional channel is activated."
                        ),
                    ),
                    field(
                        "Commercial email requirements",
                        "textarea",
                        (
                            "Document how commercial messages satisfy CAN-SPAM "
                            "requirements for headers, subjects, advertising "
                            "identification, postal addresses, and functioning "
                            "opt-outs. Record both the statutory timing "
                            "requirements and the tighter internal service "
                            "target used to prevent repeated unwanted contact."
                        ),
                        (
                            "Under 15 U.S.C. § 7704, the template uses "
                            "accurate sender information, a nondeceptive subject, "
                            "clear commercial identification, a valid postal "
                            "address, and an unsubscribe method. The mechanism "
                            "remains available for at least 30 days after "
                            "sending; requests are honored within 10 business "
                            "days, with a 24-hour internal target."
                        ),
                    ),
                    field(
                        "Telephone technology and permission evidence",
                        "textarea",
                        (
                            "Classify the proposed dialing technology, destination "
                            "number type, message content, and available permission "
                            "evidence. Evaluate applicable TCPA and FCC conditions "
                            "without assuming every automated tool is legally "
                            "identical or that a business contact is "
                            "categorically exempt."
                        ),
                        (
                            "Review 47 U.S.C. § 227 and 47 CFR "
                            "§ 64.1200 before enabling outbound telephone "
                            "automation. Artificial or prerecorded telemarketing "
                            "calls to covered numbers require the applicable "
                            "prior express written consent unless an exception "
                            "applies. A purchased mobile number and a supplier's "
                            "generic assurance do not establish that evidence."
                        ),
                    ),
                    field(
                        "Do-not-call, revocation, and calling-hour controls",
                        "textarea",
                        (
                            "Determine applicable national, state, and entity-specific "
                            "calling restrictions, local-time limits, and revocation "
                            "handling. Explain how exceptions are established "
                            "and how a recipient's direct stop request "
                            "changes eligibility across active queues and "
                            "outsourced calling teams."
                        ),
                        (
                            "The calling register evaluates 47 CFR § 64.1200 "
                            "and 16 CFR § 310.4 for the actual "
                            "recipient and campaign. Internal policy permits "
                            "approved live calls only between 9 a.m. "
                            "and 5 p.m. recipient local time. Direct "
                            "stop requests immediately block further promotional "
                            "calls, including contractor queues."
                        ),
                    ),
                    field(
                        "B2B telemarketing scope and state registration",
                        "textarea",
                        (
                            "Evaluate the scope of federal B2B exceptions, "
                            "remaining misrepresentation restrictions, and state "
                            "seller or telemarketer registration duties. Record "
                            "the actual business model and recipient class "
                            "rather than using a B2B label as "
                            "a universal exemption."
                        ),
                        (
                            "The review cites 16 CFR § 310.6(b)(7) "
                            "and the B2B misrepresentation provisions in "
                            "§ 310.3(a)(2) and (4). Florida campaigns "
                            "receive a separate scope and exemption analysis "
                            "under Fla. Stat. §§ 501.601–501.626. Registration "
                            "evidence or a documented exemption must precede "
                            "any activity requiring that registration."
                        ),
                    ),
                    field(
                        "Privacy roles and individual rights",
                        "textarea",
                        (
                            "Determine whether the agency and client act "
                            "as independent businesses, service providers, "
                            "contractors, or another applicable role. Map "
                            "collection notices, access, correction, deletion, "
                            "sale or sharing choices, and contractual "
                            "restrictions to the actual data flow."
                        ),
                        (
                            "For covered California activity, assess Cal. "
                            "Civ. Code §§ 1798.100, 1798.105, 1798.120, "
                            "and 1798.140, including applicable current-year "
                            "thresholds. Business-contact records receive no "
                            "blanket B2B exclusion. The data map identifies "
                            "collection sources and client disclosures; a "
                            "verified deletion request propagates to active "
                            "systems and contracted recipients as required."
                        ),
                    ),
                    field(
                        "Data-broker classification and supplier terms",
                        "textarea",
                        (
                            "Assess whether selling or sharing prospect "
                            "information triggers data-broker obligations, "
                            "and verify supplier rights independently. "
                            "Record registration, deletion-interface, downstream "
                            "restriction, and audit requirements applicable "
                            "to the actual activity rather than "
                            "assuming appointment services eliminate those duties."
                        ),
                        (
                            "A California data-broker assessment examines Cal. "
                            "Civ. Code § 1798.99.80 et seq. and "
                            "Delete Act duties under § 1798.99.86. "
                            "If applicable, registration and deletion-mechanism "
                            "obligations enter the operating calendar. Supplier "
                            "terms must permit the specific processing and "
                            "client disclosure; a license invoice alone "
                            "does not prove collection rights."
                        ),
                    ),
                    field(
                        "Recording, retention, and evidence minimization",
                        "textarea",
                        (
                            "Define when recording is permitted, which "
                            "participants must agree, what evidence is "
                            "retained, and how retention periods are "
                            "selected. Separate required operational records "
                            "from unnecessary audio or sensitive content "
                            "that increases exposure without improving qualification."
                        ),
                        (
                            "Calls involving California receive analysis under "
                            "Cal. Penal Code §§ 632 and 632.7, "
                            "including confidentiality and telephone-type facts. "
                            "Recording stays off unless the required participant "
                            "agreement is established. Where 16 CFR § 310.5 "
                            "recordkeeping applies, covered records follow "
                            "its five-year period; other records use "
                            "a documented purpose-based schedule."
                        ),
                    ),
                    field(
                        "Service contract and professional licensing boundaries",
                        "textarea",
                        (
                            "Specify services, acceptance evidence, review deadlines, "
                            "fees, credits, termination, and licensed-service "
                            "boundaries. Address regulated verticals explicitly "
                            "so a standard commercial appointment agreement "
                            "is not reused for referral arrangements "
                            "that carry different statutory restrictions."
                        ),
                        (
                            "The HVAC schedule defines a $4,000 retainer, "
                            "$100 accepted held appointments, five-business-day "
                            "review, and documented credits. The agency does "
                            "not perform licensed HVAC work. Mortgage settlement "
                            "referrals require a separate review of "
                            "12 U.S.C. § 2607; the standard per-appointment "
                            "offer is not carried into that vertical."
                        ),
                    ),
                    field(
                        "Claims review and issue closure register",
                        "textarea",
                        (
                            "Review campaign claims, testimonials, service credentials, "
                            "comparisons, and savings statements against available "
                            "evidence. Record each issue, accountable owner, "
                            "affected channel, corrective action, and closure "
                            "artifact so unresolved problems lead to "
                            "specific operational restrictions."
                        ),
                        (
                            "Remove an unsupported promise that every facility "
                            "will save 30% on maintenance. Under 15 U.S.C. "
                            "§ 45, the claim review requires support "
                            "for material representations. The revised message "
                            "offers a maintenance-contract assessment without "
                            "invented savings. The account owner archives "
                            "the approved copy and disables the older template."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Every enabled channel has a documented applicability decision, "
                    "implemented recipient-rights controls, supported claims, and "
                    "executed terms; activities with unresolved statutory, licensing, "
                    "permission, or source-rights issues remain disabled."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation, Growth, and Risk Fallback Tracker",
                "purpose": (
                    "Automate repeatable qualification, permission tracking, routing, "
                    "and reporting without scaling defects or unwanted outreach. "
                    "Connect observed buyer responses to controlled offer "
                    "improvements, monitor acquisition and retention signals, "
                    "and prepare practical fallback procedures for infrastructure "
                    "outages, data failures, and client churn."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Automate only a workflow that has passed manual "
                        "execution and evidence review. Start with suppression, "
                        "record validation, assignment, and reporting; preserve "
                        "human judgment for disputed qualification, ambiguous "
                        "permission evidence, unusual buyer requests, and "
                        "changes to a client's promised service."
                    ),
                    (
                        "Instrument each conversion stage with stable cohort "
                        "definitions and a named owner. Separate contact "
                        "eligibility, message delivery, positive replies, held "
                        "meetings, accepted appointments, collections, and "
                        "client renewals so improvements in one metric "
                        "cannot conceal deterioration in another."
                    ),
                    (
                        "Run small experiments that alter one material "
                        "variable and respect channel restrictions. Evaluate "
                        "accepted appointments and client value rather "
                        "than opening counts. Stop an experiment when "
                        "recipient objections, defects, or service-capacity "
                        "constraints exceed the prewritten operating threshold."
                    ),
                    (
                        "Design fallback behavior for every dependency that "
                        "can stop delivery or corrupt evidence. A safe "
                        "fallback may pause sending, switch to a "
                        "review queue, or offer manual scheduling; it "
                        "must not bypass a provider restriction or "
                        "a recipient's expressed preference."
                    ),
                    (
                        "Review automation outcomes weekly with the client "
                        "and delivery pod. Use defect reasons and "
                        "renewal feedback to refine qualification, positioning, "
                        "and fulfillment capacity. Increase spending only "
                        "when accepted-unit economics, cash coverage, and "
                        "team workload support the additional demand."
                    ),
                ],
                "fields": [
                    field(
                        "Permission and suppression event model",
                        "textarea",
                        (
                            "Define the event fields needed to reconstruct "
                            "channel eligibility, permissions where required, "
                            "withdrawals, and suppression decisions. Preserve "
                            "scope and source evidence rather than "
                            "collapsing all communication choices into "
                            "one editable CRM checkbox."
                        ),
                        (
                            "Each event stores contact ID, channel, purpose, "
                            "timestamp, source, wording version where relevant, "
                            "and evidence reference. An email opt-out immediately "
                            "blocks promotional email; a request to stop "
                            "all marketing blocks every covered channel. "
                            "Fresh vendor imports cannot overwrite either "
                            "event with a generic marketable flag."
                        ),
                    ),
                    field(
                        "Automation stages and human exception queue",
                        "textarea",
                        (
                            "Map each automated stage to its inputs, "
                            "outputs, validation rules, and exception owner. "
                            "Identify decisions requiring review and "
                            "define queue aging limits so unresolved "
                            "records cannot silently accumulate or "
                            "be released through default permissive settings."
                        ),
                        (
                            "The pipeline validates source metadata, normalizes "
                            "account keys, checks suppression, scores commercial "
                            "fit, and assigns a reviewer. Ambiguous job "
                            "roles enter a one-business-day exception queue. "
                            "A missing permission artifact blocks the "
                            "affected calling workflow. The automation never "
                            "creates acceptance merely because a calendar "
                            "event ended."
                        ),
                    ),
                    field(
                        "Cohort funnel and accepted-appointment reporting",
                        "textarea",
                        (
                            "Define stage denominators and attribution windows "
                            "for a single campaign cohort. Show "
                            "how delivery, replies, scheduling, attendance, "
                            "and acceptance connect while keeping "
                            "campaign performance distinct from client "
                            "sales revenue and operator accounting totals."
                        ),
                        (
                            "An illustrative cohort starts with 1,000 "
                            "eligible records, 960 delivered messages, "
                            "48 positive replies, 24 scheduled meetings, "
                            "20 held meetings, and 18 accepted appointments. "
                            "Acceptance equals 90% of held meetings "
                            "and 1.8% of eligible records. At $100 "
                            "each, fees equal $1,800; client deal "
                            "values remain outside agency revenue."
                        ),
                    ),
                    field(
                        "Outbound experiment and learning rule",
                        "textarea",
                        (
                            "Specify the hypothesis, eligible audience, changed "
                            "variable, budget, observation period, and "
                            "decision rule. Include recipient-objection "
                            "and quality stop conditions, and "
                            "avoid extrapolating a small pilot's "
                            "results into unsupported annual performance claims."
                        ),
                        (
                            "Test renewal-focused copy against equipment-downtime "
                            "copy using two comparable 250-account groups "
                            "over fourteen days. Keep sender identity, "
                            "qualification, and scheduling capacity unchanged. "
                            "Compare accepted appointments and objection reasons; "
                            "pause on any serious source-rights complaint. "
                            "Treat two versus three accepted appointments "
                            "as preliminary evidence, not a definitive winner."
                        ),
                    ),
                    field(
                        "Deliverability and provider-policy monitoring",
                        "textarea",
                        (
                            "Select operational signals for authentication failures, "
                            "hard bounces, complaints, and provider "
                            "restrictions. Define internal pause thresholds "
                            "and investigation steps, acknowledging that "
                            "thresholds do not authorize unwanted "
                            "contact or override provider policies."
                        ),
                        (
                            "Review authentication daily and hard bounces "
                            "after each batch. A rolling hard-bounce "
                            "rate above 2% pauses the affected "
                            "source for investigation. Inspect Google "
                            "Postmaster Tools where data is available, "
                            "but do not interpret sparse reporting "
                            "as zero complaints. Provider restrictions "
                            "trigger investigation, never identity substitution."
                        ),
                    ),
                    field(
                        "Acquisition spending and growth release rule",
                        "textarea",
                        (
                            "Define the agency's own acquisition budget, "
                            "payback measure, observation window, and "
                            "incremental spending rule. Keep client-funded "
                            "media separate and require accepted-unit "
                            "quality, retention evidence, and available "
                            "working cash before expanding campaign commitments."
                        ),
                        (
                            "Base agency acquisition spending is $72,000 "
                            "annually, averaging $6,000 monthly, separate "
                            "from client media. Increase a tested "
                            "channel's monthly allocation by at most "
                            "$500 after two reviewed cohorts meet "
                            "quality targets and the thirteen-week forecast "
                            "preserves $10,000 minimum cash. Otherwise "
                            "retain the existing budget."
                        ),
                    ),
                    field(
                        "Client value reporting and retention loop",
                        "textarea",
                        (
                            "Define the client review cadence, attribution "
                            "boundaries, sales-feedback fields, and renewal "
                            "signals. Distinguish client pipeline value "
                            "from realized sales and operator fees, "
                            "then identify the corrective action "
                            "for service failures or deteriorating buyer fit."
                        ),
                        (
                            "A monthly review shows 31 accepted appointments, "
                            "12 proposals, and three client-reported wins. "
                            "The agency reports $3,100 appointment fees "
                            "plus the $4,000 retainer. Client-reported "
                            "contract values appear only in a "
                            "separate attribution section. Low proposal "
                            "conversion prompts a joint qualification "
                            "review rather than retroactive fee rejection."
                        ),
                    ),
                    field(
                        "CRM and scheduling outage fallback",
                        "textarea",
                        (
                            "Describe the fallback when CRM, calendar, "
                            "or routing services become unavailable. "
                            "Specify what pauses, what continues "
                            "manually, how sensitive records remain "
                            "protected, and how reconciliation prevents "
                            "duplicate assignments when normal service returns."
                        ),
                        (
                            "If HubSpot becomes unavailable, new outbound "
                            "work pauses because suppression and ownership "
                            "checks cannot be confirmed. Existing inbound "
                            "requests enter an access-controlled temporary "
                            "queue with unique IDs. Staff offer "
                            "manual callback windows. Recovery imports "
                            "the queue once, reconciles ownership, "
                            "and rechecks suppression before any follow-up."
                        ),
                    ),
                    field(
                        "Poor quality, churn, and cost risk register",
                        "textarea",
                        (
                            "Track the three primary commercial risks "
                            "with observable triggers, leading indicators, "
                            "assigned owners, and concrete fallback "
                            "actions. Include both immediate containment "
                            "and the evidence required before "
                            "returning to normal operating volume."
                        ),
                        (
                            "Quality risk triggers at more than 15% "
                            "defects across a reviewed cohort; pause "
                            "the source and rescrub. Churn risk "
                            "triggers when a client misses two "
                            "feedback reviews; the owner schedules "
                            "a service recovery call. Rising acquisition "
                            "cost triggers the pricing review before "
                            "new spending commitments."
                        ),
                    ),
                    field(
                        "Access, backup, and automation change control",
                        "textarea",
                        (
                            "Specify role-based access, credential handling, "
                            "backup verification, and change-review requirements. "
                            "Explain how a configuration update "
                            "is tested and reversed without "
                            "exposing prospect data, losing suppression "
                            "history, or interrupting evidence needed "
                            "for client billing."
                        ),
                        (
                            "Contractors receive client-scoped CRM roles "
                            "and multifactor authentication; secrets remain "
                            "in a managed vault. Encrypted backups "
                            "include suppression history and acceptance "
                            "events. A monthly restore test uses "
                            "an isolated environment. Routing changes "
                            "run against thirty saved test cases "
                            "before deployment, with the prior "
                            "configuration retained for reversal."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Permission tracking, CRM routing, and lead-quality reporting "
                    "operate with tested exception handling; growth decisions "
                    "use accepted-unit evidence; and each major risk has a "
                    "named owner, numeric trigger, and rehearsed fallback."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch, Pod Scorecard, and Exit-Readiness Ledger",
                "purpose": (
                    "Translate the underwriting and control design into a "
                    "funded thirty-day operating sprint. Assign accountable "
                    "roles, inspect quality and cash weekly, preserve "
                    "canonical scenario discipline, and assemble transferable "
                    "records that allow another operator to continue "
                    "delivery without relying on founder memory."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Set a thirty-day launch objective around a "
                        "verified operating system and a bounded pilot, "
                        "not an assumed annual revenue run rate. "
                        "The canonical first-deal horizon is one "
                        "to four months, so an unsigned client "
                        "at day thirty requires diagnosis rather "
                        "than invented sales."
                    ),
                    (
                        "Assign one accountable owner to each deliverable "
                        "and define contractor hours explicitly. The "
                        "Base structure contains one full-time role "
                        "and three contractors, not four full-time "
                        "employees. Match coverage to response commitments "
                        "and retain a backup for critical "
                        "client-facing tasks."
                    ),
                    (
                        "Review the same scorecard every week using "
                        "stable definitions and source records. "
                        "Include acceptance quality, appointment attendance, "
                        "client response time, collections, unrestricted "
                        "cash, and workload. Record actual results "
                        "separately from targets and explain "
                        "any missed commitment."
                    ),
                    (
                        "Prepare transfer evidence from the beginning: "
                        "executed contracts, source rights, sender "
                        "assets, access records, invoice reconciliations, "
                        "and operating procedures. Preserve assignment "
                        "restrictions and client obligations instead "
                        "of assuming that an eventual buyer "
                        "can inherit every account or "
                        "contact dataset automatically."
                    ),
                    (
                        "Finish the sprint with a documented continue, "
                        "repair, or stop decision. Compare the "
                        "observed operating evidence with the "
                        "underwritten assumptions, specify the next "
                        "funded milestone, and leave unresolved "
                        "items visibly assigned rather than "
                        "reporting launch completion while essential "
                        "work remains undone."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–7 underwriting and offer milestones",
                        "textarea",
                        (
                            "List the first week's deliverables, owners, "
                            "evidence artifacts, and spending limit. "
                            "Prioritize counterparty verification, service "
                            "capacity, source sampling, and measurable "
                            "acceptance terms before purchasing a "
                            "large dataset or configuring broad "
                            "outbound campaigns."
                        ),
                        (
                            "By day seven, the owner completes three "
                            "client interviews, selects commercial HVAC, "
                            "verifies one prospective client's credentials, "
                            "and reviews a 200-record source sample. "
                            "The contract draft defines held-meeting "
                            "acceptance and five-business-day review. "
                            "Preparation spending remains below $2,000; "
                            "no live outreach starts before "
                            "source and message review."
                        ),
                    ),
                    field(
                        "Days 8–14 infrastructure and control milestones",
                        "textarea",
                        (
                            "Define the second week's technical deliverables, "
                            "test evidence, access assignments, and "
                            "operating dependencies. Include sender "
                            "authentication, suppression propagation, CRM "
                            "identifiers, calendar ownership, contract "
                            "execution, and the practical conditions "
                            "required before enabling a pilot."
                        ),
                        (
                            "By day fourteen, three authorized mailboxes "
                            "pass authentication checks, the CRM "
                            "contains the approved lifecycle, and "
                            "all thirty pre-flight tests have "
                            "documented outcomes. The owner verifies "
                            "executed client terms and prepaid "
                            "retainer receipt before live services. "
                            "If the contract remains unsigned, "
                            "internal tests continue without external sending."
                        ),
                    ),
                    field(
                        "Days 15–21 bounded pilot milestones",
                        "textarea",
                        (
                            "Set the pilot cohort size, daily "
                            "review cadence, delivery boundaries, and "
                            "stop conditions. Identify which results "
                            "are observations rather than commitments "
                            "and define how quality feedback "
                            "changes the next batch without "
                            "rewriting the original evidence."
                        ),
                        (
                            "With the client active, release an initial "
                            "250-record reviewed cohort and inspect "
                            "responses daily. Record eligibility, delivery, "
                            "held meetings, and acceptance separately. "
                            "Pause the source if hard bounces "
                            "exceed 2% or material source concerns "
                            "arise. The pilot promises the "
                            "defined service process, not a "
                            "predetermined appointment count."
                        ),
                    ),
                    field(
                        "Days 22–30 reconciliation and next-step milestones",
                        "textarea",
                        (
                            "Specify the final week's acceptance review, "
                            "invoice reconciliation, cash update, client "
                            "feedback, and operating decision. Include "
                            "the branch for an unclosed "
                            "first deal so the launch "
                            "review remains useful throughout the "
                            "canonical sales-cycle range."
                        ),
                        (
                            "By day thirty, reconcile every held "
                            "appointment to accepted or rejected "
                            "status, produce the invoice register, "
                            "and refresh the thirteen-week cash "
                            "forecast. If no client has "
                            "signed, review interview-to-proposal conversion "
                            "and fund a specific next "
                            "sales milestone; the 1–4 month "
                            "first-deal horizon remains unchanged."
                        ),
                    ),
                    field(
                        "Base pod roles and contractor capacity",
                        "textarea",
                        (
                            "Assign the full-time owner and three "
                            "contractor roles, their weekly hours, "
                            "handoff responsibilities, and backup coverage. "
                            "Connect staffing to actual workflow "
                            "capacity without treating headcount as "
                            "equivalent full-time labor or overlooking "
                            "the owner's operating workload."
                        ),
                        (
                            "The Base pod has one full-time owner "
                            "covering sales, account management, and "
                            "cash. Three contractors cover data "
                            "operations at 15 hours weekly, "
                            "campaign operations at 20, and "
                            "qualification QA at 15. Contractor "
                            "spending is budgeted at $108,000 "
                            "annually; the owner backs up "
                            "routing and client escalation."
                        ),
                    ),
                    field(
                        "Weekly KPI definitions and escalation thresholds",
                        "textarea",
                        (
                            "Define a compact scorecard with precise "
                            "numerators, denominators, reporting periods, "
                            "owners, and escalation thresholds. Avoid "
                            "vanity metrics and separate attendance "
                            "from acceptance so missing meetings "
                            "cannot be hidden inside a "
                            "favorable qualification percentage."
                        ),
                        (
                            "Track held divided by scheduled meetings, "
                            "accepted divided by held meetings, "
                            "hard bounces divided by attempted "
                            "messages, and overdue invoices by "
                            "aging bucket. Targets include at "
                            "least 85% acceptance on reviewed "
                            "held cohorts and $10,000 minimum "
                            "cash. Two missed client reviews "
                            "trigger an owner-led retention discussion."
                        ),
                    ),
                    field(
                        "Canonical scenario and capacity review",
                        "textarea",
                        (
                            "Restate all three canonical annual outcomes "
                            "and compare observed capacity with "
                            "the relevant staffing structure. Label "
                            "annual averages clearly and explain "
                            "what additional evidence is needed "
                            "before moving from the Base "
                            "pod to the six-person scaled operation."
                        ),
                        (
                            "Conservative is $100,000 revenue and $20,000 "
                            "owner profit at 20%; Base is "
                            "$425,000 and $127,500 at 30.0%; "
                            "Scaled is $750,000 and $300,000 "
                            "at 40%. Base averages 154.17 "
                            "accepted appointments monthly. Scaling to "
                            "225 monthly requires verified capacity "
                            "and 2 FT plus 4 C, "
                            "not merely more inboxes."
                        ),
                    ),
                    field(
                        "Transferable contracts and asset ownership ledger",
                        "textarea",
                        (
                            "Inventory customer agreements, domain ownership, "
                            "mailbox administration, software subscriptions, "
                            "source licenses, and operating procedures. "
                            "Record transfer restrictions and required "
                            "counterparty actions so an eventual "
                            "transaction does not presume rights "
                            "the agency cannot convey."
                        ),
                        (
                            "The ledger lists five client contracts, "
                            "one agency-owned sending domain, three "
                            "mailboxes, CRM administration, and supplier "
                            "licenses. Two client agreements require "
                            "written permission for assignment. Vendor "
                            "licenses are reviewed individually for "
                            "transfer rights. The handoff package "
                            "contains procedures and access ownership, "
                            "not exported passwords or unrestricted prospect lists."
                        ),
                    ),
                    field(
                        "Revenue quality and exit-readiness evidence",
                        "textarea",
                        (
                            "Specify the records needed to substantiate "
                            "recurring revenue, accepted-unit fees, "
                            "client concentration, contractor continuity, "
                            "and owner dependence. Reconcile operating "
                            "records to accounting and bank "
                            "evidence without treating client pipeline "
                            "value as agency earnings."
                        ),
                        (
                            "Prepare twelve monthly reconciliations linking "
                            "retainers and accepted appointment IDs "
                            "to invoices, credits, receivables, and "
                            "bank collections. Base revenue comprises "
                            "$240,000 retainers and $185,000 fees. "
                            "Report the largest client's 20% "
                            "revenue concentration and document contractor "
                            "continuity. Client contract wins remain "
                            "outside the agency earnings schedule."
                        ),
                    ),
                    field(
                        "Day-thirty decision and funded next milestone",
                        "textarea",
                        (
                            "Record the decision, evidence, remaining "
                            "defects, accountable owners, spending "
                            "authorization, and next review date. "
                            "Distinguish completed work from planned "
                            "work and connect expansion to "
                            "observed quality, service capacity, "
                            "cash availability, and client retention."
                        ),
                        (
                            "Continue the pilot for thirty additional "
                            "days after eighteen accepted appointments "
                            "from twenty held meetings, no "
                            "unresolved suppression failures, and "
                            "$14,200 forecast minimum cash. "
                            "Authorize $1,500 of additional source "
                            "and testing expense within the "
                            "forecast. Assign the owner to "
                            "resolve two qualification disputes before expansion."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The thirty-day review records actual outcomes, reconciled "
                    "fees and cash, a functioning 1 FT plus 3 C "
                    "responsibility map, transfer restrictions, and an explicitly "
                    "funded next milestone; unfinished work remains identified "
                    "with owners and dates."
                ),
            },
        ],
    }
