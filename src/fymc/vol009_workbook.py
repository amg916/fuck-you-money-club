from __future__ import annotations


def build_volume_009_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-009-million-dollar-lead-generation",
        "volume_id": "vol-009-million-dollar-lead-generation",
        "title": "Million-Dollar Lead Generation — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Enterprise Deal Underwriting, "
            "ABM Signal Orchestration, Qualified-Opportunity Economics, "
            "Outreach Controls, Delivery Automation, and Small-Team Launch Readiness"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Opportunity, Vertical Underwriting & Counterparty Qualification",
                "purpose": (
                    "Select an enterprise demand-generation niche where observable buying "
                    "signals, reachable decision makers, and client delivery capacity support "
                    "repeatable opportunity creation. Separate prospective client contract "
                    "values from agency revenue, and document the evidence required before "
                    "accepting an account into the operating pipeline."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Choose one vertical and one buying problem before purchasing data. "
                        "Document the expected enterprise procurement sequence, incumbent "
                        "alternatives, security review requirements, and reasons an economic "
                        "buyer would authorize a discovery meeting during the next two quarters."
                    ),
                    (
                        "Underwrite the client as carefully as the target account. Review "
                        "delivery references, existing pipeline, available account executives, "
                        "cash collection history, and authority to sign your services agreement. "
                        "Reject assignments whose promised outcomes exceed the client's fulfillment capacity."
                    ),
                    (
                        "Build a small evidence-backed account universe rather than buying "
                        "an indiscriminate contact list. For every proposed account, capture "
                        "source date, buying trigger, relevant role, geographic restrictions, "
                        "and exclusions arising from existing customer relationships or active opportunities."
                    ),
                    (
                        "Define a qualified opportunity through observable acceptance criteria "
                        "that both parties can inspect. Specify buyer involvement, problem "
                        "fit, realistic purchasing process, required meeting evidence, and "
                        "duplicate treatment before quoting any opportunity-based fee to the client."
                    ),
                    (
                        "Score commercial attractiveness and execution friction separately. "
                        "Use the completed evidence record to choose a narrow pilot, "
                        "establish client concentration limits, and assign an accountable "
                        "owner for every unresolved underwriting question before outreach begins."
                    ),
                ],
                "fields": [
                    field(
                        "Vertical thesis and enterprise buying problem",
                        "textarea",
                        (
                            "Describe the chosen vertical, expensive operating problem, "
                            "enterprise purchase category, and observable trigger. Explain "
                            "why the target buyer would consider a meeting without relying "
                            "on unsupported savings claims or generic personalization."
                        ),
                        (
                            "Target industrial manufacturers with 2,000–15,000 employees "
                            "replacing fragmented maintenance software. A new plant acquisition "
                            "or published modernization program supplies the trigger. The "
                            "client sells deployments worth approximately $1,000,000; our "
                            "agency earns retainers and accepted-opportunity fees, never the "
                            "client's implementation contract value."
                        ),
                    ),
                    field(
                        "Client identity, authority, and payment capacity",
                        "textarea",
                        (
                            "Identify the contracting entity, authorized signer, billing "
                            "contact, payment method, and evidence of operating capacity. "
                            "Record how you verified authority and what collection protection "
                            "applies before the delivery pod starts work."
                        ),
                        (
                            "Northstar Maintenance Software LLC signs through its authorized "
                            "chief operating officer. Finance confirms the purchase order "
                            "and an ACH mandate. Two reference calls validate completed "
                            "enterprise implementations. The agreement requires the first "
                            "$7,500 retainer before account research and pauses new delivery "
                            "after documented payment default."
                        ),
                    ),
                    field(
                        "Account universe and exclusion boundaries",
                        "textarea",
                        (
                            "Specify account size, industry, location, technology context, "
                            "and exclusion rules. Quantify the reachable universe after "
                            "removing existing customers, active opportunities, prohibited "
                            "territories, and accounts without a defensible reason for contact."
                        ),
                        (
                            "Begin with 240 manufacturers identified through company filings "
                            "and licensed firmographic data. Remove 35 existing customers, "
                            "25 active client opportunities, and 20 out-of-territory accounts. "
                            "The remaining 160 accounts form the research universe; the first "
                            "pilot uses 40 accounts with dated modernization evidence."
                        ),
                    ),
                    field(
                        "Buying committee and access hypothesis",
                        "textarea",
                        (
                            "Map the operational sponsor, economic buyer, technical reviewer, "
                            "procurement contact, and likely blocker. State which roles must "
                            "participate initially and which introductions the client must "
                            "secure after accepting an opportunity."
                        ),
                        (
                            "The maintenance director owns the operating problem, the chief "
                            "operating officer controls program funding, and enterprise IT "
                            "reviews integrations. Procurement enters after technical fit. "
                            "An initial meeting requires the director or a delegated program "
                            "owner; the client account executive must secure executive "
                            "sponsorship within 30 days."
                        ),
                    ),
                    field(
                        "Signal provenance and freshness standard",
                        "textarea",
                        (
                            "Record each trigger's source, observation date, account match, "
                            "permitted use, and expiration rule. Distinguish verified company "
                            "events from inferred intent, and identify evidence that would "
                            "invalidate the proposed outreach hypothesis."
                        ),
                        (
                            "A manufacturer announced a plant acquisition 18 days ago on "
                            "its investor-relations website. Store the URL, publication date, "
                            "and relevant excerpt in HubSpot. Refresh the trigger after "
                            "30 days. Treat third-party topic interest as directional "
                            "research, not proof that a named person requested contact."
                        ),
                    ),
                    field(
                        "Qualified-opportunity acceptance definition",
                        "textarea",
                        (
                            "Write the minimum evidence for an accepted opportunity, "
                            "including account eligibility, participant role, confirmed "
                            "problem, meeting attendance, and next step. Identify conditions "
                            "that create research leads but do not earn opportunity fees."
                        ),
                        (
                            "An accepted opportunity requires an eligible account, an "
                            "attended 30-minute discovery meeting with a maintenance program "
                            "owner, a documented modernization problem, and agreement to a "
                            "technical follow-up. A calendar booking alone earns no fee. "
                            "A student researcher, vendor solicitation, or unrelated inquiry "
                            "fails qualification."
                        ),
                    ),
                    field(
                        "Client fulfillment and sales capacity",
                        "textarea",
                        (
                            "Measure the client's ability to respond, conduct discovery, "
                            "supply technical support, and fulfill resulting contracts. "
                            "Set maximum weekly introductions and response deadlines so "
                            "your delivery does not overwhelm the client's available selling resources."
                        ),
                        (
                            "The client assigns two account executives and one solutions "
                            "engineer. Together they can handle four new discovery meetings "
                            "weekly and two technical workshops. The response commitment "
                            "is one business day. Reduce introductions when more than six "
                            "accepted opportunities lack a documented next action."
                        ),
                    ),
                    field(
                        "Sales-cycle and procurement friction map",
                        "textarea",
                        (
                            "Estimate the sequence and duration of discovery, technical "
                            "validation, security review, procurement, and contracting. "
                            "Separate the agency's first client-sale timeline from the "
                            "client's downstream enterprise buying cycle and resulting cash receipts."
                        ),
                        (
                            "Plan 3–12 months to win the agency's first client. For that "
                            "client's prospects, model 30 days of discovery, 60 days of "
                            "technical validation, and another 90–180 days for procurement. "
                            "Agency fees follow contracted service and acceptance milestones, "
                            "rather than waiting for the enterprise deployment to close."
                        ),
                    ),
                    field(
                        "Concentration and counterparty exposure",
                        "textarea",
                        (
                            "Calculate revenue exposure by client, vertical, and payment "
                            "status. State a practical concentration threshold, explain "
                            "temporary launch exceptions, and define the action required "
                            "when one counterparty becomes essential to payroll coverage."
                        ),
                        (
                            "At the Base case, six equally productive clients each generate "
                            "$112,500 annually, representing 16.67% of $675,000 revenue. "
                            "Set a mature-book limit of 25% per client. During the "
                            "one-client launch, maintain a separate cash runway and prospect "
                            "pipeline rather than describing concentration as diversified."
                        ),
                    ),
                    field(
                        "Underwriting decision and pilot boundary",
                        "textarea",
                        (
                            "Summarize the decision, supporting evidence, unresolved "
                            "conditions, pilot scope, and accountable owner. Include the "
                            "canonical candidate score without treating its aggregate "
                            "ranking as evidence that a particular client or account will perform."
                        ),
                        (
                            "Proceed with a 40-account pilot after signer verification "
                            "and CRM exclusion matching. Candidate #21 carries an 86/100 "
                            "Money-to-Manpower Score and pipeline rank #18 of 29. Its "
                            "component scores are 24 revenue, 21 margin, 16 team efficiency, "
                            "9 startup accessibility, and 12 automation."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The commercial lead signs a dated underwriting record containing "
                    "verified client authority, 40 evidence-backed pilot accounts, written "
                    "opportunity acceptance criteria, delivery capacity, and named owners "
                    "for every unresolved condition; excluded accounts cannot enter outreach."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Scrub Reserve & Working-Capital Float Calculator",
                "purpose": (
                    "Translate retainers and qualified-opportunity fees into reconciled "
                    "operator economics. Model rejected submissions, cash reserves, collection "
                    "delays, and staffing without counting client contract values as agency "
                    "revenue. Test whether available startup capital can support the actual "
                    "sales cycle and delivery commitments."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Enter the three canonical annual scenarios before building a "
                        "monthly forecast. Preserve their exact revenue, owner profit, "
                        "margin, and staffing figures. Treat the illustrated client counts "
                        "and fee combinations as operating bridges, not additional canonical assumptions."
                    ),
                    (
                        "Separate submitted opportunities, accepted opportunities, invoiced "
                        "fees, recognized revenue, and collected cash. Calculate scrub "
                        "rates on submitted records and document the accounting treatment "
                        "of rejected submissions, service credits, advance retainers, and temporary cash reserves."
                    ),
                    (
                        "Assign every annual operating cost to one category and reconcile "
                        "the total to the scenario margin. Include employee costs, "
                        "contractor delivery, acquisition, software, data, administration, "
                        "and rework without deducting an internal reserve allocation as another expense."
                    ),
                    (
                        "Build a collection calendar that reflects actual contract terms. "
                        "Model advance retainers separately from opportunity invoices, "
                        "calculate average receivables, and identify the lowest projected "
                        "cash balance before committing to additional payroll or annual software contracts."
                    ),
                    (
                        "Stress the plan for delayed client acquisition, a rejected "
                        "opportunity batch, and loss of the largest client. Where "
                        "funding is insufficient, reduce fixed commitments or secure "
                        "documented funding rather than assuming enterprise deals close earlier."
                    ),
                ],
                "fields": [
                    field(
                        "Conservative scenario revenue bridge",
                        "textarea",
                        (
                            "Reconstruct Conservative annual operator revenue from a "
                            "specific retainer and accepted-opportunity mix. Reconcile "
                            "costs, owner profit, margin, and team composition while "
                            "keeping downstream enterprise contract values outside the agency revenue calculation."
                        ),
                        (
                            "Three clients paying $3,500 monthly generate $126,000 annual "
                            "retainers. Another 24 accepted opportunities at $1,000 produce "
                            "$24,000. Total revenue is $150,000; annual costs are $120,000, "
                            "leaving $30,000 owner net profit at 20% margin. The canonical "
                            "team is 2 FT + 3 C."
                        ),
                    ),
                    field(
                        "Base scenario revenue bridge",
                        "textarea",
                        (
                            "Construct a Base annual revenue bridge with client count, "
                            "monthly retainer, accepted-opportunity volume, and fee. Show "
                            "the annual and monthly averages, then reconcile owner profit "
                            "and the required canonical staffing configuration."
                        ),
                        (
                            "Six clients at $7,500 monthly produce $540,000 retainers. "
                            "Ninety accepted opportunities at $1,500 add $135,000. Annual "
                            "revenue totals $675,000, averaging $56,250 monthly. Costs of "
                            "$472,500 leave $202,500 owner net profit at 30.0% margin "
                            "with 2 FT + 3 C."
                        ),
                    ),
                    field(
                        "Scaled small-team revenue bridge",
                        "textarea",
                        (
                            "Build the Scaled revenue bridge without increasing the "
                            "canonical seven-person team. Explain the client and opportunity "
                            "volumes supporting annual revenue, and reconcile all-in costs "
                            "and owner profit to the required net margin."
                        ),
                        (
                            "Eight clients paying $10,000 monthly generate $960,000 "
                            "retainers. Another 120 accepted opportunities at $2,000 add "
                            "$240,000. Revenue reaches $1,200,000; costs total $720,000, "
                            "leaving $480,000 owner net profit at 40% margin. Staffing "
                            "is 3 FT + 4 C, totaling seven people."
                        ),
                    ),
                    field(
                        "Base expense allocation and capacity assumptions",
                        "textarea",
                        (
                            "Allocate the Base annual expense ceiling across named "
                            "operating categories. Specify contractor availability and "
                            "employee assumptions, and identify any market wage or delivery "
                            "constraint that would make the canonical margin unattainable locally."
                        ),
                        (
                            "Allocate $168,000 to loaded employee costs, $120,000 to three "
                            "fractional contractors, $36,000 to software, $48,000 to data, "
                            "$24,500 to administration and insurance, $48,000 to acquisition, "
                            "and $28,000 to delivery rework. Total costs equal $472,500; "
                            "validate local compensation before hiring against this illustration."
                        ),
                    ),
                    field(
                        "Submission scrub and accepted-fee yield",
                        "textarea",
                        (
                            "Calculate submitted volume, rejected volume, accepted volume, "
                            "scrub percentage, and earned opportunity fees. Distinguish "
                            "pre-acceptance defects from post-recognition credits so the "
                            "same rejected opportunity cannot reduce revenue twice in the model."
                        ),
                        (
                            "Submit 100 opportunities during the Base year and reject "
                            "10 for duplicates or missing qualification evidence. The "
                            "10% scrub leaves 90 accepted opportunities earning $135,000. "
                            "The rejected submissions represent $15,000 of unearned potential "
                            "fees, not recognized revenue and not an additional expense."
                        ),
                    ),
                    field(
                        "Defect cash reserve and credit treatment",
                        "textarea",
                        (
                            "Set an internal cash reserve for disputed fees and remedial "
                            "delivery. Explain whether each reserve movement affects cash "
                            "availability, recognized revenue, or operating expense, and "
                            "state how actual credits change the forecast."
                        ),
                        (
                            "Earmark 10% of the Base year's $135,000 accepted-opportunity "
                            "fees, or $13,500, as an internal cash reserve. This transfer "
                            "does not reduce the $202,500 canonical profit. If a $1,500 "
                            "credit becomes valid, record its actual treatment and publish "
                            "a separate revised forecast rather than hiding the variance."
                        ),
                    ),
                    field(
                        "Receivables float and collection timing",
                        "textarea",
                        (
                            "Specify retainer collection dates, opportunity invoice terms, "
                            "expected payment delay, and average receivables. Separate "
                            "earned service revenue from advance cash receipts, and "
                            "identify which cash balances remain unavailable for owner distributions."
                        ),
                        (
                            "Collect $45,000 of monthly Base retainers in advance and "
                            "recognize them as services are delivered. Average monthly "
                            "opportunity fees are $11,250. At 45-day collection timing, "
                            "using a 30-day planning month, opportunity receivables average "
                            "$16,875. Retain additional cash for payroll, taxes, and disputed invoices."
                        ),
                    ),
                    field(
                        "Startup capital and pre-revenue runway",
                        "textarea",
                        (
                            "Choose a startup funding amount within the supplied range, "
                            "itemize initial commitments, and calculate runway without "
                            "client receipts. Compare that runway with the 3–12 month "
                            "first-deal window and identify the financing shortfall explicitly."
                        ),
                        (
                            "Start with $75,000, within the $15,000–$100,000 capital range. "
                            "Spend $25,000 on setup and retain $50,000 cash. At $12,500 "
                            "monthly pre-revenue burn, runway is four months. Twelve "
                            "months would require $175,000 including setup, leaving a "
                            "$100,000 shortfall against this funding plan."
                        ),
                    ),
                    field(
                        "Operating range and mature cash buffer",
                        "textarea",
                        (
                            "Compare the supplied monthly operating range with each "
                            "scenario's implied all-in costs. Do not force mature payroll "
                            "into an incompatible startup budget; document staged staffing "
                            "and the cash buffer required at the selected run rate."
                        ),
                        (
                            "The supplied monthly opex range is $4,000–$20,000, but "
                            "Base all-in costs average $39,375 and Scaled costs average "
                            "$60,000. Treat this as a planning mismatch requiring staged "
                            "commitments. A three-month Base cost buffer is $118,125, "
                            "already exceeding the $100,000 upper startup-capital figure."
                        ),
                    ),
                    field(
                        "Concentration stress and break-even sensitivity",
                        "textarea",
                        (
                            "Remove the largest client's revenue while initially holding "
                            "costs constant. Calculate remaining profit and margin, then "
                            "identify specific reducible commitments and the time required "
                            "to restore the planned earnings level."
                        ),
                        (
                            "Losing one equal Base client removes $112,500 annual revenue. "
                            "With costs initially unchanged at $472,500, revenue falls "
                            "to $562,500 and profit to $90,000, a 16% margin. Recovering "
                            "the original profit requires replacing that revenue or "
                            "reducing actual costs, not merely reallocating the cash reserve."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The operator and finance owner reconcile all three canonical "
                    "scenarios, document scrub and reserve treatments, and approve a "
                    "dated cash forecast showing funding sources for committed spending "
                    "through the next client-acquisition milestone."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "Execution, Opportunity Ledger & Technical QA Pre-Flight",
                "purpose": (
                    "Create an auditable delivery path from source evidence to client "
                    "acceptance and payment. Establish identifiers, ownership rules, "
                    "attribution records, technical checks, and dispute procedures that "
                    "prevent duplicate billing, unsupported qualification, lost handoffs, "
                    "and accidental exposure of one client's account data to another."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Map the workflow before configuring integrations. Give each "
                        "stage an entry condition, required evidence, accountable owner, "
                        "and permitted next state. Prevent a booked meeting from "
                        "automatically becoming an accepted opportunity or a billable ledger entry."
                    ),
                    (
                        "Configure stable identifiers and client boundaries across the "
                        "CRM, scheduling system, evidence store, and billing export. "
                        "Test duplicates and existing opportunities using the client's "
                        "actual suppression snapshot before importing the first production account batch."
                    ),
                    (
                        "Write the attribution policy into the services schedule and "
                        "mirror it in the ledger. Record first qualifying touch, "
                        "pre-existing opportunity status, acceptance evidence, and exceptions "
                        "so later disputes can be resolved from records rather than recollection."
                    ),
                    (
                        "Perform a complete synthetic journey using records controlled "
                        "by the delivery team. Validate permissions, message rendering, "
                        "calendar time zones, rescheduling, cancellation, event retries, "
                        "fee eligibility, and the exact evidence attached to the client's acceptance request."
                    ),
                    (
                        "Reconcile CRM acceptance counts, invoice lines, credits, and "
                        "cash receipts before each billing run. Assign unresolved "
                        "differences to named owners, retain an exception log, and "
                        "block duplicate or unsupported fee lines while continuing valid delivery."
                    ),
                ],
                "fields": [
                    field(
                        "Execution stages and state transitions",
                        "textarea",
                        (
                            "Define the ordered operational states from account research "
                            "through collection. Identify evidence required for each "
                            "transition, and specify which state changes require human "
                            "review instead of automatic promotion by an integration."
                        ),
                        (
                            "Use Researched, Eligible, Contacted, Engaged, Booked, Attended, "
                            "Submitted, Accepted, Invoiced, and Collected states. An attendance "
                            "record moves Booked to Attended; a qualification packet moves "
                            "Attended to Submitted. Only recorded client acceptance permits "
                            "Accepted status. Calendar events cannot create invoice lines "
                            "without that acceptance."
                        ),
                    ),
                    field(
                        "Stable identifiers and client isolation",
                        "textarea",
                        (
                            "Specify identifiers for clients, accounts, contacts, meetings, "
                            "opportunities, and invoices. Explain how access controls "
                            "and matching rules prevent cross-client exposure or duplicate "
                            "fees when names, domains, or meeting times change."
                        ),
                        (
                            "Assign client_id C006, account_id A0142, and opportunity_id "
                            "O006-0142-01. Use the CRM object ID as the durable contact "
                            "reference rather than an email address alone. Separate client "
                            "workspaces and permissions. A rescheduled meeting retains its "
                            "opportunity ID and cannot create a second billable opportunity."
                        ),
                    ),
                    field(
                        "Source evidence and qualification packet",
                        "textarea",
                        (
                            "List the evidence attached to each submitted opportunity, "
                            "including trigger provenance, participant role, attendance, "
                            "confirmed problem, and agreed next action. Limit captured "
                            "personal information to what delivery and dispute resolution actually require."
                        ),
                        (
                            "Opportunity O006-0142-01 includes the dated acquisition "
                            "announcement, participant job title, meeting attendance "
                            "confirmation, structured discovery notes, and a technical "
                            "workshop date. Store restricted notes in the client workspace. "
                            "Do not attach unrelated personal profiles or a full meeting "
                            "recording when concise evidence is sufficient."
                        ),
                    ),
                    field(
                        "Attribution window and pre-existing pipeline",
                        "textarea",
                        (
                            "Write the attribution window, baseline pipeline check, "
                            "duplicate hierarchy, and exception process. Distinguish "
                            "contractual fee attribution from claims about causal impact "
                            "on client revenue or influence across the entire buying committee."
                        ),
                        (
                            "The contract attributes eligible opportunities submitted within "
                            "90 days of the agency's documented qualifying touch. Exclude "
                            "opportunities already active in the client's kickoff snapshot. "
                            "For overlapping sources, use the signed exception schedule. "
                            "This rule determines the $1,500 fee; it does not establish "
                            "that the agency caused the client's entire sale."
                        ),
                    ),
                    field(
                        "Acceptance deadline and dispute packet",
                        "textarea",
                        (
                            "Define the client's review period, valid rejection reasons, "
                            "required rejection evidence, and escalation owner. State "
                            "whether silence has contractual effect and how disputed "
                            "records are withheld from billing during investigation."
                        ),
                        (
                            "Give the client five business days to accept or reject "
                            "a complete submission. Require a reason code and supporting "
                            "CRM record for duplicates. Silence leaves the submission "
                            "pending under this contract. Escalate overdue reviews to "
                            "the sales operations lead; disputed opportunities remain "
                            "outside the accepted-fee invoice batch."
                        ),
                    ),
                    field(
                        "Opportunity and invoice ledger columns",
                        "textarea",
                        (
                            "Specify the minimum ledger columns connecting operational "
                            "events with financial records. Include immutable references, "
                            "amounts, dates, status, credits, and cash application so "
                            "a reviewer can reconstruct one opportunity without searching unrelated systems."
                        ),
                        (
                            "Record client ID, opportunity ID, submitted date, accepted "
                            "date, fee amount, invoice ID, invoice date, due date, credit "
                            "reference, payment date, and applied cash. O006-0142-01 earns "
                            "$1,500 on acceptance, appears once on invoice I006-004, "
                            "and closes only when its payment allocation is recorded."
                        ),
                    ),
                    field(
                        "Scheduling and handoff quality checks",
                        "textarea",
                        (
                            "Describe calendar ownership, time-zone handling, invite "
                            "content, reminder behavior, cancellation rules, and client "
                            "handoff requirements. Include checks that distinguish actual "
                            "attendance from accepted invitations or automated calendar responses."
                        ),
                        (
                            "Calendly routes the meeting to the assigned account executive "
                            "and displays the buyer's local time zone. The invitation "
                            "states the discussion topic and includes cancellation links. "
                            "A controlled test checks daylight-saving behavior. The account "
                            "executive confirms attendance manually; an accepted invitation "
                            "does not satisfy the attended-meeting requirement."
                        ),
                    ),
                    field(
                        "Idempotency, retries, and event ordering",
                        "textarea",
                        (
                            "Define event identifiers, deduplication storage, retry limits, "
                            "and rules for late or out-of-order updates. Explain how "
                            "the system handles a cancellation arriving after booking "
                            "and prevents repeated webhook delivery from creating extra fees."
                        ),
                        (
                            "Persist each provider event ID before processing its effects. "
                            "A repeated meeting-created webhook returns the existing result. "
                            "Retry transient failures three times, then send the record "
                            "to a review queue. A later cancellation changes meeting "
                            "status but never deletes the audit history or silently "
                            "reverses an accepted invoice."
                        ),
                    ),
                    field(
                        "Pre-flight test cases and expected results",
                        "textarea",
                        (
                            "List representative test cases with expected outcomes and "
                            "evidence locations. Cover successful delivery, suppression, "
                            "duplicates, cancellations, access isolation, and billing errors "
                            "before connecting production lists or sending messages to external recipients."
                        ),
                        (
                            "Run 12 controlled cases: four valid journeys, two suppressed "
                            "contacts, two duplicates, one cancellation, one failed handoff, "
                            "one cross-client access attempt, and one repeated invoice "
                            "export. Expect four eligible submissions, zero suppressed "
                            "sends, zero duplicate fees, and denied cross-client access. "
                            "Store results beside the configuration version."
                        ),
                    ),
                    field(
                        "Monthly reconciliation and correction ownership",
                        "textarea",
                        (
                            "Describe the reconciliation between accepted opportunities, "
                            "invoice lines, credits, and receipts. Assign correction "
                            "owners and deadlines, and require an explanatory record "
                            "for differences rather than editing historical totals to force agreement."
                        ),
                        (
                            "April contains eight accepted opportunities at $1,500, totaling "
                            "$12,000. The draft export contains nine fee lines, or "
                            "$13,500. Finance removes the duplicate line before issuance "
                            "and records the integration defect. Retainers reconcile "
                            "separately to $45,000; cash receipts follow payment timing "
                            "rather than the acceptance count."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The delivery lead records passing results for all 12 controlled "
                    "cases, verifies client isolation and duplicate prevention, and "
                    "demonstrates a complete source-to-payment audit trail without "
                    "sending production outreach or issuing unsupported invoices."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract & Outreach Audit",
                "purpose": (
                    "Translate jurisdiction, communication channel, data provenance, "
                    "and compensation structure into concrete operating requirements. "
                    "Identify when ordinary enterprise marketing crosses into regulated "
                    "referral activity, establish enforceable contract boundaries, and "
                    "maintain evidence that outreach and data handling follow the "
                    "rules applicable to each campaign."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Inventory recipient locations, channels, data sources, and "
                        "the actual service being promoted. Evaluate requirements "
                        "for each combination rather than assuming a business email "
                        "address, public profile, or enterprise buyer removes all privacy and outreach obligations."
                    ),
                    (
                        "Document the relevant statutory provisions and operational "
                        "controls together. Identify the responsible reviewer, evidence "
                        "retained, refresh date, and conditions that stop a campaign. "
                        "Resolve uncertain channel or sector classifications before paying for production distribution."
                    ),
                    (
                        "Review the compensation model independently from the message "
                        "content. A fixed retainer, accepted-meeting fee, percentage "
                        "commission, and transaction-contingent payment can receive "
                        "different treatment, particularly in healthcare, settlement services, securities, and federal procurement."
                    ),
                    (
                        "Make the services agreement match the operating ledger. "
                        "Specify qualification, attribution, acceptance, rejection evidence, "
                        "credits, payment timing, data responsibilities, confidentiality, "
                        "and termination exports so neither party must invent commercial rules after a disputed introduction."
                    ),
                    (
                        "Test suppression, rights requests, incident escalation, and "
                        "vendor access using controlled records. Retain proof of "
                        "the tests and unresolved findings. A written policy is "
                        "insufficient when the sending platform or contractor workflow bypasses its requirements."
                    ),
                ],
                "fields": [
                    field(
                        "Jurisdiction and channel applicability register",
                        "textarea",
                        (
                            "List sender and recipient locations, intended channels, "
                            "recipient categories, and promoted services. Explain the "
                            "method used to determine applicable rules and identify "
                            "campaign combinations that require additional review before any contact."
                        ),
                        (
                            "The initial campaign uses email to United States manufacturing "
                            "employees and excludes SMS, automated voice, personal mobile "
                            "numbers, and European recipients. Record state locations "
                            "where available. A proposed United Kingdom expansion receives "
                            "a separate PECR and UK GDPR review before records enter "
                            "the sending segment."
                        ),
                    ),
                    field(
                        "Commercial email requirements and suppression",
                        "textarea",
                        (
                            "Translate commercial email requirements into message, sender, "
                            "address, and opt-out controls. Identify the applicable "
                            "statute, the operational deadline, and how suppression "
                            "propagates across client campaigns, vendors, and future list imports."
                        ),
                        (
                            "Apply 15 U.S.C. § 7704 and 16 CFR Part 316: use accurate "
                            "headers, nondeceptive subjects, required advertising identification, "
                            "a valid postal address, and a clear opt-out. Honor requests "
                            "within 10 business days; operationally suppress immediately. "
                            "Test that later imports cannot reactivate the same opted-out address."
                        ),
                    ),
                    field(
                        "Telephone, text, and recording restrictions",
                        "textarea",
                        (
                            "Identify any calling, texting, prerecorded content, automated "
                            "dialing, or recording planned for the campaign. Document "
                            "applicable consent and do-not-call requirements, relevant "
                            "state overlays, and proof required before enabling each channel."
                        ),
                        (
                            "Keep automated telemarketing calls and texts disabled until "
                            "47 U.S.C. § 227, 47 CFR § 64.1200, and applicable state "
                            "requirements are evaluated for the specific technology and "
                            "recipients. Maintain required consent evidence. Evaluate "
                            "California Penal Code § 632 before recording confidential "
                            "conversations involving California participants."
                        ),
                    ),
                    field(
                        "Privacy roles, notices, and individual rights",
                        "textarea",
                        (
                            "Determine whether the agency and client act as controllers, "
                            "processors, businesses, service providers, or another defined "
                            "role. Identify applicable thresholds, notices, rights handling, "
                            "and contractual restrictions rather than assuming business contacts are categorically exempt."
                        ),
                        (
                            "For covered California activity, assess Civil Code §§ "
                            "1798.100–1798.199.100, including notice and applicable rights "
                            "duties; business-contact data is not categorically outside "
                            "the statute. For EU expansion, document GDPR Articles 6, "
                            "14, and 21 analysis. A claimed legitimate interest does "
                            "not automatically authorize every outreach channel."
                        ),
                    ),
                    field(
                        "Data sourcing and broker status assessment",
                        "textarea",
                        (
                            "Document where contact data originates, contractual use "
                            "rights, refresh methods, and whether the business sells "
                            "personal information outside a direct relationship. Assess "
                            "registration and deletion duties where the actual business model triggers them."
                        ),
                        (
                            "The agency licenses 800 business-contact records for a "
                            "named campaign and records permitted uses and deletion "
                            "terms. Before offering standalone contact files to other "
                            "buyers, assess California Civil Code §§ 1798.99.80–1798.99.89 "
                            "and current implementing requirements. Do not assume that "
                            "calling the product research removes data-broker obligations."
                        ),
                    ),
                    field(
                        "Healthcare, property, and securities fee restrictions",
                        "textarea",
                        (
                            "Screen the promoted service and payment trigger for "
                            "sector-specific referral restrictions. Identify any "
                            "transaction-linked compensation, licensing question, or "
                            "covered service that requires restructuring or specialist review before accepting the engagement."
                        ),
                        (
                            "Exclude healthcare-program referrals pending review under "
                            "42 U.S.C. § 1320a-7b(b), settlement-service referrals under "
                            "12 U.S.C. § 2607, and securities introductions implicating "
                            "15 U.S.C. § 78o(a). A $2,000 fee labeled marketing can "
                            "still create a substantive issue when payment depends "
                            "on a regulated referral."
                        ),
                    ),
                    field(
                        "Federal procurement contingent-fee screening",
                        "textarea",
                        (
                            "Identify campaigns involving federal contract opportunities "
                            "and compensation tied to awards. Review relevant contract "
                            "clauses and exceptions, and distinguish ordinary enterprise "
                            "demand generation from conduct involving procurement influence or restricted payments."
                        ),
                        (
                            "A prospect requests 2% of any resulting federal software "
                            "award. Review FAR Subpart 3.4 and FAR 52.203-5, including "
                            "the facts supporting any bona fide employee or established "
                            "commercial selling agency exception. Do not launch the "
                            "award-linked arrangement merely because the client proposes "
                            "calling it a lead fee."
                        ),
                    ),
                    field(
                        "Services agreement and fee schedule",
                        "textarea",
                        (
                            "Draft the commercial clauses controlling scope, retainer "
                            "earning, opportunity acceptance, attribution, credits, "
                            "payment deadlines, and termination. Ensure the written "
                            "terms match the CRM workflow and avoid promising client sales outcomes outside your control."
                        ),
                        (
                            "Schedule A states a $7,500 monthly retainer and $1,500 per "
                            "accepted opportunity, payable within 30 days of invoice. "
                            "It incorporates qualification criteria, the 90-day attribution "
                            "window, five-business-day review, and evidence-based rejection. "
                            "Client contract values are excluded from agency fees; "
                            "termination requires an agreed data export and retention schedule."
                        ),
                    ),
                    field(
                        "Security, retention, and incident ownership",
                        "textarea",
                        (
                            "Specify access roles, authentication, encryption, retention, "
                            "vendor restrictions, and incident escalation. Connect "
                            "retention periods to operational or contractual needs, "
                            "while preserving minimal suppression information needed to avoid contacting people who opted out."
                        ),
                        (
                            "Require multifactor authentication for HubSpot and Google "
                            "Workspace, restrict exports to two named administrators, "
                            "and review contractor access monthly. Delete rejected "
                            "research records after 90 days under the documented schedule, "
                            "subject to holds. Retain minimal suppression identifiers "
                            "with restricted access so later imports do not restart outreach."
                        ),
                    ),
                    field(
                        "Audit findings and remediation evidence",
                        "textarea",
                        (
                            "Record each finding, affected campaign, severity, accountable "
                            "owner, target date, and verification evidence. Specify "
                            "which defects prevent sending or payment, and close "
                            "findings only after an observed test confirms the required control works."
                        ),
                        (
                            "Finding P-03 shows that a contractor CSV import bypasses "
                            "suppression matching. Pause that import path and assign "
                            "the CRM administrator a two-day repair deadline. Retest "
                            "20 controlled records, including five suppressed addresses. "
                            "Close the finding only when all five remain excluded "
                            "and the result is attached."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The responsible reviewer records the applicable channel and sector "
                    "requirements, the client signs matching commercial terms, and "
                    "controlled tests verify suppression and access restrictions. "
                    "Unresolved regulated-fee questions remain outside the active campaign."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation, Outbound Growth & Risk Fallback Tracker",
                "purpose": (
                    "Automate account qualification, CRM attribution, and scheduling "
                    "without automating unsupported claims or disputed fee decisions. "
                    "Connect account signals to bounded experiments, measurable funnel "
                    "improvement, and tested manual fallbacks so a small delivery "
                    "team can expand capacity while preserving evidence quality "
                    "and client trust."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Draw the automation path from approved data sources to "
                        "account scoring, outreach, replies, scheduling, qualification, "
                        "and billing. Mark every point where a machine inference "
                        "must remain provisional until supported by evidence or reviewed by an accountable person."
                    ),
                    (
                        "Start with the three canonical leverage points: account "
                        "qualification, CRM attribution, and meeting scheduling. "
                        "Measure minutes saved and errors introduced for each "
                        "automation before expanding it to additional clients, channels, or more sensitive data categories."
                    ),
                    (
                        "Design outbound experiments around a specific account "
                        "hypothesis and useful message. Change one meaningful variable "
                        "at a time, preserve comparison cohorts, and judge "
                        "performance using accepted opportunities and downstream quality rather than email opens alone."
                    ),
                    (
                        "Set service-health thresholds that protect recipients and "
                        "delivery quality. Investigate bounces, complaints, permission "
                        "failures, and unusual acceptance changes. Do not respond "
                        "to a broken or restricted channel by disguising identity or bypassing provider controls."
                    ),
                    (
                        "Rehearse manual fallback for data-provider failure, CRM "
                        "outage, calendar errors, and staff absence. Specify who "
                        "can pause sends, how pending work is preserved, "
                        "and how recovered systems reconcile events without duplicating meetings or opportunity fees."
                    ),
                ],
                "fields": [
                    field(
                        "Automation architecture and system ownership",
                        "textarea",
                        (
                            "Map the systems used for account research, CRM records, "
                            "outreach, scheduling, and billing export. Assign an owner "
                            "to each integration and explain which system is authoritative "
                            "for qualification, acceptance, suppression, and payment status."
                        ),
                        (
                            "Use licensed data and company websites for research, "
                            "HubSpot for account and opportunity state, a permitted "
                            "business-email platform for outreach, and Calendly for "
                            "scheduling. Finance controls invoice issuance. The CRM "
                            "administrator owns integrations; HubSpot acceptance records, "
                            "not calendar bookings, authorize opportunity-fee export."
                        ),
                    ),
                    field(
                        "Account qualification scoring and explainability",
                        "textarea",
                        (
                            "Define account-level scoring inputs, weights, minimum "
                            "evidence, and exclusion overrides. Require a readable "
                            "reason for each score and prevent weak inferred signals "
                            "from overriding contractual exclusions or explicit recipient preferences."
                        ),
                        (
                            "Score firmographic fit at 40 points, a verified modernization "
                            "trigger at 35, and identified relevant roles at 25. "
                            "Research accounts scoring at least 75. An existing active "
                            "opportunity or suppression match overrides the score. "
                            "Record the source behind each component so reviewers "
                            "can challenge stale or mismatched evidence."
                        ),
                    ),
                    field(
                        "AI-assisted research and message review",
                        "textarea",
                        (
                            "Describe permitted machine assistance, source requirements, "
                            "human review, and data minimization. Specify how unsupported "
                            "claims, mistaken identities, sensitive inferences, and invented "
                            "buying intent are detected before generated text reaches a recipient."
                        ),
                        (
                            "A language model drafts a 90-word message from approved "
                            "company facts and the client positioning brief. A researcher "
                            "checks every factual sentence against its source. Reject "
                            "invented budget claims and statements that a named person "
                            "visited a website. Send only reviewed drafts through "
                            "the normal suppression-controlled workflow."
                        ),
                    ),
                    field(
                        "Outbound cohort and experiment design",
                        "textarea",
                        (
                            "Define the experiment hypothesis, account cohorts, message "
                            "difference, observation period, and success metric. Keep "
                            "contact pressure controlled, and identify confounders "
                            "that would make apparent performance differences unsuitable for broad deployment."
                        ),
                        (
                            "Split 80 eligible accounts into two matched groups of "
                            "40. Variant A leads with acquisition integration; Variant "
                            "B leads with maintenance visibility. Use the same offer "
                            "and role coverage for 21 days. Compare positive replies "
                            "and accepted opportunities, while acknowledging that "
                            "small counts provide limited statistical precision."
                        ),
                    ),
                    field(
                        "Funnel math and accepted-opportunity target",
                        "textarea",
                        (
                            "Translate account coverage into delivered contacts, positive "
                            "replies, held meetings, submissions, and accepted opportunities. "
                            "Use consistent denominators and connect the resulting annual "
                            "accepted volume to the Base fee model rather than client contract values."
                        ),
                        (
                            "Across six clients, contact 1,200 distinct eligible people "
                            "annually. At 20% positive replies, obtain 240 conversations; "
                            "50% meeting conversion yields 120 held meetings. Submit "
                            "100 qualified records and accept 90 after scrub. Those "
                            "90 accepted opportunities generate $135,000 at the Base "
                            "$1,500 fee."
                        ),
                    ),
                    field(
                        "Sender health and recipient protection thresholds",
                        "textarea",
                        (
                            "Set monitoring thresholds for bounce rates, complaints, "
                            "opt-outs, and authentication failures. Explain the investigation "
                            "and pause procedure, including how small sample sizes "
                            "and provider-specific requirements affect decisions about continuing a campaign."
                        ),
                        (
                            "Verify SPF, DKIM, and DMARC alignment before sending. "
                            "Pause a batch when hard bounces exceed 2% or any "
                            "complaint suggests a sourcing defect; investigate even "
                            "one complaint in a small pilot. These are internal "
                            "thresholds, not provider entitlements. Repair sourcing "
                            "and permissions instead of cycling identities."
                        ),
                    ),
                    field(
                        "CRM attribution automation and reconciliation",
                        "textarea",
                        (
                            "Describe how touch events, baseline exclusions, attribution "
                            "windows, and acceptance decisions populate CRM records. "
                            "Specify exception handling and the checks that prevent "
                            "automatic attribution from becoming unsupported billing or exaggerated revenue influence claims."
                        ),
                        (
                            "A workflow stamps the first qualifying touch and checks "
                            "the 90-day attribution window against the kickoff pipeline "
                            "snapshot. Conflicting source records enter a review queue. "
                            "The automation proposes attribution but cannot mark client "
                            "acceptance. Weekly reconciliation compares accepted opportunity "
                            "IDs with exported fee lines and flags unmatched records."
                        ),
                    ),
                    field(
                        "Scheduling leverage and human capacity",
                        "textarea",
                        (
                            "Estimate scheduling workload before and after automation, "
                            "including exceptions and no-shows. Translate time saved "
                            "into available delivery capacity, and identify the human "
                            "judgment that must remain outside calendar routing and reminder automation."
                        ),
                        (
                            "At 120 held meetings annually, manual scheduling averaging "
                            "20 minutes consumes 40 hours. Automated routing plus "
                            "five minutes of exception handling per meeting consumes "
                            "10 hours, freeing 30 hours. Staff still verify role "
                            "fit and attendance; automated reminders do not establish "
                            "qualification or justify an opportunity fee."
                        ),
                    ),
                    field(
                        "Outage fallback and restart reconciliation",
                        "textarea",
                        (
                            "Define the manual process for unavailable CRM, scheduling, "
                            "data, or sending systems. Identify pause authority, "
                            "temporary records, access restrictions, and the reconciliation "
                            "steps required before restarting automation after service restoration."
                        ),
                        (
                            "If HubSpot is unavailable, pause new outreach and fee "
                            "exports. The delivery lead tracks existing meeting changes "
                            "in an access-restricted worksheet using durable opportunity "
                            "IDs. After recovery, compare timestamps and event IDs "
                            "before replaying updates. Resume only after pending "
                            "cancellations and suppression changes have synchronized."
                        ),
                    ),
                    field(
                        "Growth flywheel and dependency risk",
                        "textarea",
                        (
                            "Explain how validated delivery evidence improves targeting, "
                            "positioning, referrals, and retention. List vendor and "
                            "client dependencies, assign fallback owners, and prevent "
                            "case-study production from exposing confidential client pipeline or implying unverified closed revenue."
                        ),
                        (
                            "Each month, summarize accepted-opportunity reasons and "
                            "rejection patterns to improve the next account cohort. "
                            "Request client permission before publishing a case study "
                            "showing 15 accepted opportunities. Report client sales "
                            "outcomes only when verified and authorized. Maintain "
                            "portable CRM exports and an alternate licensed data "
                            "source to reduce dependency."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The automation owner demonstrates qualification scoring, attribution "
                    "review, scheduling, immediate suppression, and a successful outage "
                    "recovery using controlled records. The growth lead approves one "
                    "bounded experiment with defined denominators and documented pause criteria."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod KPI Scorecard & Exit-Readiness Ledger",
                "purpose": (
                    "Turn the operating design into a funded 30-day launch plan "
                    "with clear responsibilities, evidence-based milestones, and explicit "
                    "stop decisions. Track the small team's delivery quality and "
                    "financial health while organizing transferable contracts, clean "
                    "records, and documented processes for eventual ownership transition."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Treat the first 30 days as a readiness and learning "
                        "sprint, not a substitute for the stated 3–12 month "
                        "first-deal timeline. Set milestones around validated "
                        "accounts, contract terms, controlled tests, and qualified client conversations rather than assumed collections."
                    ),
                    (
                        "Assign every deliverable to one accountable person and "
                        "identify supporting contractors. Preserve the canonical "
                        "team structure when describing steady-state scenarios, "
                        "but stage launch commitments according to available cash and verified demand rather than hiring everyone immediately."
                    ),
                    (
                        "Use one weekly scorecard combining leading indicators, "
                        "accepted-opportunity quality, collections, cash runway, and "
                        "client concentration. Define each denominator and source "
                        "system so the pod cannot improve an apparent metric by changing its interpretation between reviews."
                    ),
                    (
                        "Maintain a decision log for changes to niche, pricing, "
                        "targeting, staffing, and automation. Record the evidence "
                        "behind each change and its expected cash impact. "
                        "Separate deviations from the forecast from revisions to the immutable canonical scenario reference."
                    ),
                    (
                        "Build transfer readiness while operating, not after "
                        "receiving an acquisition inquiry. Keep signed agreements, "
                        "reconciled financials, access inventories, documented procedures, "
                        "and client permissions organized, while restricting confidential information until a legitimate transaction process authorizes disclosure."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–7 underwriting and commercial foundation",
                        "textarea",
                        (
                            "Specify first-week deliverables, owners, spending limits, "
                            "and evidence required for completion. Focus on selecting "
                            "the vertical, validating the offer, preparing contract "
                            "terms, and reconciling the cash plan before configuring extensive automation."
                        ),
                        (
                            "The commercial lead completes five client-discovery interviews "
                            "and selects manufacturing modernization. The delivery lead "
                            "researches 40 pilot accounts. Finance reconciles the "
                            "$75,000 funding plan and limits week-one commitments "
                            "to $5,000 within the $25,000 setup budget. Completion "
                            "requires an evidence-backed offer and reviewed services schedule."
                        ),
                    ),
                    field(
                        "Days 8–14 data, systems, and controlled tests",
                        "textarea",
                        (
                            "List second-week system configuration and verification "
                            "work, including access roles, suppression, identifiers, "
                            "attribution, scheduling, and billing exports. Require "
                            "observable test results rather than treating installed software or purchased data as completed operational capability."
                        ),
                        (
                            "Configure the HubSpot stages, client access boundaries, "
                            "Calendly routing, and acceptance ledger. Run the 12 "
                            "controlled pre-flight cases and repair every fee-duplication "
                            "or suppression defect. Import only the 40 researched "
                            "pilot accounts after exclusion matching. Keep production "
                            "outreach disabled until the operational and channel "
                            "checks are complete."
                        ),
                    ),
                    field(
                        "Days 15–21 bounded client-acquisition experiment",
                        "textarea",
                        (
                            "Define the third-week acquisition experiment, target "
                            "counterparties, contact limits, measurement period, and "
                            "review owner. Distinguish selling the agency service "
                            "from performing outbound work for an unsigned client or claiming a downstream enterprise deal."
                        ),
                        (
                            "Approach 20 carefully selected software vendors that "
                            "serve the chosen manufacturing segment, using the "
                            "approved email controls. Target four substantive sales "
                            "conversations as a learning objective. Present the "
                            "$7,500 retainer and $1,500 accepted-opportunity structure. "
                            "Do not launch client-branded campaigns before a signed "
                            "agreement and required funding."
                        ),
                    ),
                    field(
                        "Days 22–30 review and next-month decision",
                        "textarea",
                        (
                            "Set the final-week review agenda, continuation criteria, "
                            "budget decision, and unresolved evidence requirements. "
                            "Explain how the operator proceeds if the sprint "
                            "produces learning and qualified conversations but no signed client or collected revenue."
                        ),
                        (
                            "Review interview evidence, contact quality, reply reasons, "
                            "test results, and actual cash spending. If no client "
                            "has signed, preserve the 3–12 month acquisition assumption "
                            "and authorize only the next funded experiment. Continue "
                            "with the niche when buyers validate the problem; revise "
                            "positioning when objections consistently reject the proposed value."
                        ),
                    ),
                    field(
                        "Pod roles and staged staffing commitments",
                        "textarea",
                        (
                            "Assign commercial, research, operations, quality, and "
                            "finance responsibilities across employees and contractors. "
                            "Document fractional availability, backup coverage, and "
                            "the revenue or cash milestones required before increasing fixed commitments toward the canonical team."
                        ),
                        (
                            "At Base steady state, two full-time roles cover commercial "
                            "leadership and delivery operations. Three fractional "
                            "contractors cover research, CRM automation, and finance "
                            "support. During launch, use limited contracted hours "
                            "until funding supports recurring commitments. The Scaled "
                            "structure adds one full-time client lead and one "
                            "contractor, reaching seven people."
                        ),
                    ),
                    field(
                        "Weekly pod KPI definitions and evidence",
                        "textarea",
                        (
                            "Define the weekly metrics, denominators, owners, and "
                            "source records. Include delivery quality, client response "
                            "speed, overdue reviews, collection performance, and "
                            "cash runway so volume metrics cannot hide rejection problems or deteriorating liquidity."
                        ),
                        (
                            "Track eligible accounts researched, positive replies "
                            "per delivered contact, held meetings per scheduled "
                            "meeting, accepted opportunities per submission, overdue "
                            "acceptance reviews, and collected cash per due invoice "
                            "dollar. Finance reports runway from unrestricted cash "
                            "and forecast net burn; the delivery lead reports "
                            "rejection reasons by client every Friday."
                        ),
                    ),
                    field(
                        "Monthly financial scorecard and variance bridge",
                        "textarea",
                        (
                            "Compare actual revenue, costs, owner profit, and "
                            "collections with the chosen scenario run rate. "
                            "Separate timing differences from structural shortfalls "
                            "and explain each material variance using ledger evidence rather than changing the reference scenario."
                        ),
                        (
                            "The Base monthly average is $56,250 revenue, $39,375 "
                            "costs, and $16,875 owner net profit. A month with "
                            "$45,000 retainers and eight accepted opportunities "
                            "produces $57,000 revenue. At $39,375 costs, profit "
                            "is $17,625, or $750 above the reference; cash may "
                            "differ because fees collect later."
                        ),
                    ),
                    field(
                        "Stop, repair, and expansion decision log",
                        "textarea",
                        (
                            "Write specific conditions for pausing outreach, repairing "
                            "delivery, changing the offer, or adding capacity. "
                            "Include decision authority and cash consequences, "
                            "and distinguish a failed experiment from evidence that the entire business model cannot work."
                        ),
                        (
                            "Pause a client's new submissions if two consecutive "
                            "batches exceed 20% rejection and investigate qualification "
                            "drift. Freeze hiring when forecast cash falls below "
                            "eight weeks of committed spending. Expand account "
                            "coverage only after acceptance quality stabilizes and "
                            "the client confirms sales capacity. Record each "
                            "decision with an owner and review date."
                        ),
                    ),
                    field(
                        "Transferable operating assets and rights ledger",
                        "textarea",
                        (
                            "Inventory contracts, process documents, domains, system "
                            "configurations, data rights, and staff knowledge that "
                            "a successor would need. Identify assignment restrictions, "
                            "client permissions, and vendor limitations before describing the business as readily transferable."
                        ),
                        (
                            "Maintain signed client agreements, renewal dates, assignment "
                            "clauses, domain ownership records, CRM configuration exports, "
                            "and documented qualification procedures. Flag two data "
                            "licenses requiring vendor permission before transfer. "
                            "Store contractor confidentiality and intellectual-property "
                            "terms with each engagement. A buyer receives only "
                            "information authorized for the transaction's current stage."
                        ),
                    ),
                    field(
                        "Exit-readiness financial and customer evidence",
                        "textarea",
                        (
                            "Define the financial, operational, and customer evidence "
                            "needed for a credible ownership-transition review. "
                            "Separate canonical owner profit from any buyer-specific "
                            "earnings measure, and identify unresolved adjustments without inventing a valuation multiple or sale price."
                        ),
                        (
                            "Organize 12 months of reconciled revenue, accepted-fee "
                            "ledgers, credits, bank collections, churn, concentration, "
                            "and contractor costs. Present $202,500 as the canonical "
                            "Base owner net profit, not automatically EBITDA. "
                            "Document owner duties and replacement-cost assumptions "
                            "separately. Support retention claims with renewals "
                            "and client correspondence rather than projected pipeline value."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The operator closes the 30-day sprint with documented test results, "
                    "actual spending, client-acquisition evidence, a funded next-month "
                    "plan, named pod responsibilities, and an organized operating ledger. "
                    "Any uncompleted milestone retains an owner, dependency, and review date."
                ),
            },
        ],
    }
