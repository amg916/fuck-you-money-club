from __future__ import annotations


def build_volume_039_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-039-inbound-pay-per-call-and-ping-post-arbitrage",
        "volume_id": "vol-039-inbound-pay-per-call-and-ping-post-arbitrage",
        "title": "Inbound Pay-Per-Call & RTB Ping-Post Arbitrage — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Buyer Underwriting, Call-Level Spread "
            "Math, Settlement Float, Idempotent Ping-Post Execution, Statutory Evidence, "
            "Automated Acquisition, and a Measured 30-Day Launch"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Arbitrage Deal / Counterparty Underwriting & Spread Qualification",
                "purpose": (
                    "Qualify an inbound call market before buying traffic, assigning numbers, "
                    "or enabling an auction. Establish which buyer actually owes payment, "
                    "which publisher creates the demand, and which measurable call conditions "
                    "convert a quoted bid into a collectible settlement with an auditable spread."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Select one vertical and one geographic footprint, then document the "
                        "caller's intended service. Separate emergency trades, insurance, and "
                        "legal inquiries because their qualification, licensing, advertising, "
                        "and transfer requirements cannot safely share an undifferentiated routing policy."
                    ),
                    (
                        "Obtain buyer and publisher agreements before negotiating volume. "
                        "Verify the contracting entity, payment contact, dispute window, and "
                        "permitted acquisition methods against independent records; a dashboard "
                        "balance or enthusiastic account manager does not establish collectible settlement value."
                    ),
                    (
                        "Express the spread using accepted, billable calls rather than raw "
                        "dial attempts. Specify when the duration clock starts, how transfers "
                        "are treated, and whether duplicate callers, disconnected agents, or "
                        "out-of-area requests invalidate an otherwise long conversation."
                    ),
                    (
                        "Run a deliberately capped pilot and match its recordings, source "
                        "identifiers, qualification timestamps, invoices, and bank receipts. "
                        "Keep publisher limits unchanged until an actual net-7 buyer payment "
                        "demonstrates the collection behavior assumed by the proposed working-capital plan."
                    ),
                    (
                        "Assign one owner to each unresolved underwriting exception and "
                        "record a dated remedy. Reject opportunities whose attractive bids "
                        "depend on unsupported consent, prohibited referral compensation, "
                        "unilateral retroactive scrubs, or a payment obligation that nobody will sign."
                    ),
                ],
                "fields": [
                    field(
                        "Vertical, territory, and caller intent",
                        "textarea",
                        (
                            "Define the initial service category, permitted caller locations, "
                            "operating hours, and intended transaction. Identify categories "
                            "that must remain outside this route because their qualification "
                            "or licensing conditions differ materially."
                        ),
                        (
                            "Pilot route serves emergency plumbing inquiries in three Phoenix "
                            "ZIP-code clusters, Monday through Saturday, 07:00–19:00 Arizona "
                            "time. Callers must request service at a residential property. "
                            "Insurance enrollment, attorney matching, employment inquiries, "
                            "and existing-customer warranty calls use separate routes or receive "
                            "a clear unavailable-service message."
                        ),
                    ),
                    field(
                        "Buyer identity and payment obligation",
                        "textarea",
                        (
                            "Record the buyer's contracting entity, service authority, settlement "
                            "signer, payment account verification method, and evidence of operating "
                            "capacity. Distinguish the actual debtor from an intermediary selling "
                            "access to somebody else's demand."
                        ),
                        (
                            "Buyer A contracts directly through its verified Arizona operating "
                            "entity, supplies its contractor-license record, and names a controller "
                            "authorized to approve invoices. A callback to an independently "
                            "verified office number confirms payment instructions. The signed "
                            "schedule requires net-7 settlement for accepted calls."
                        ),
                    ),
                    field(
                        "Publisher provenance and acquisition restrictions",
                        "textarea",
                        (
                            "Identify every publisher, acquisition account, landing page, and "
                            "subpublisher permission. Describe evidence connecting the consumer "
                            "request to the call, and prohibit traffic sources that cannot "
                            "produce the agreed provenance records."
                        ),
                        (
                            "Publisher P receives one source identifier for its owned search "
                            "campaign and one approved landing-page version. The agreement bars "
                            "undisclosed subpublishers, impersonation, incentivized dialing, and "
                            "purchased callback lists. Each call carries campaign, click, page-version, "
                            "and timestamp references; missing provenance stops new routing immediately."
                        ),
                    ),
                    field(
                        "Billable call definition and duration clock",
                        "textarea",
                        (
                            "Write the exact qualification predicate, including buyer connection, "
                            "duration threshold, service intent, geography, duplicate period, "
                            "and exclusions. Specify which system measures each condition and "
                            "how contradictory timestamps are resolved."
                        ),
                        (
                            "A call becomes billable at 120 seconds after a live buyer agent "
                            "answers, provided the caller requests covered plumbing service "
                            "inside the accepted territory. IVR time does not count. Calls "
                            "from the same normalized number within 30 days require documented "
                            "distinct service intent."
                        ),
                    ),
                    field(
                        "Quoted bid and matched acquisition spread",
                        "textarea",
                        (
                            "Translate the buyer bid into gross settlement, publisher payment, "
                            "media allocation, and retained contribution per accepted call. "
                            "State whether rejected calls still incur acquisition expense and "
                            "keep that exposure outside optimistic headline spreads."
                        ),
                        (
                            "The reference unit settles at $100, pays $42 to the publisher, "
                            "and allocates $3 to click-to-call media, leaving $55 retained "
                            "contribution before other costs. The $45 combined acquisition "
                            "allocation must include rejected-attempt expense when reconciled "
                            "across the whole accepted-call cohort."
                        ),
                    ),
                    field(
                        "Scrub rights and dispute evidence",
                        "textarea",
                        (
                            "Specify allowed rejection reasons, submission deadlines, required "
                            "evidence, appeal ownership, and treatment of undisputed amounts. "
                            "Measure disputed value separately from accepted value so a "
                            "duration disagreement cannot silently rewrite settled revenue."
                        ),
                        (
                            "Buyer A may dispute duplicate, geography, service-intent, or duration "
                            "failures within seven calendar days, supplying call identifiers "
                            "and supporting timestamps. Undisputed amounts remain payable. "
                            "A 20-call dispute at $100 each creates a $2,000 contested balance, "
                            "not an automatic publisher deduction."
                        ),
                    ),
                    field(
                        "Capacity, pacing, and concentration limits",
                        "textarea",
                        (
                            "Document concurrent-call capacity, geographic coverage, hourly pacing, "
                            "and buyer concentration limits. Describe the routing response when "
                            "capacity disappears after a bid, including whether an alternate "
                            "buyer has independently satisfied the applicable requirements."
                        ),
                        (
                            "Buyer A accepts two simultaneous calls and at most 40 accepted "
                            "calls daily. The pilot starts at 10 daily calls with a $1,000 "
                            "gross exposure ceiling. A prequalified Buyer B may receive "
                            "overflow only within its own service footprint and documented "
                            "consumer-transfer permissions."
                        ),
                    ),
                    field(
                        "Net-7 collectability verification",
                        "textarea",
                        (
                            "Record the first invoice, acceptance evidence, due date, collected "
                            "amount, and bank-clearing date. Define the exposure ceiling that "
                            "remains active until payment is verified and the response to "
                            "a partial or late receipt."
                        ),
                        (
                            "The first 50 accepted calls produce a $5,000 invoice issued "
                            "March 8, 2027, due March 15. The exposure ceiling stays at "
                            "$5,000 until the full receipt clears. A $4,500 remittance "
                            "leaves $500 unresolved and prevents any automatic increase "
                            "in publisher traffic."
                        ),
                    ),
                    field(
                        "Contract economics and change control",
                        "textarea",
                        (
                            "Capture rate-card version, duration rule, payment terms, source "
                            "restrictions, and prospective amendment procedure. Require economic "
                            "changes to preserve traceability between the terms offered during "
                            "the auction and the terms applied during settlement."
                        ),
                        (
                            "Rate card PL-2027-03 pays $100 for the defined 120-second call "
                            "and permits changes only for calls initiated after the documented "
                            "effective timestamp. The buyer cannot apply a new 150-second "
                            "threshold to yesterday's calls. Both parties retain the original "
                            "auction terms with each settlement record."
                        ),
                    ),
                    field(
                        "Underwriting decision and exception register",
                        "textarea",
                        (
                            "Make a proceed, revise, or reject decision using collectible spread, "
                            "verified authority, evidence completeness, and available cash. "
                            "Assign an accountable owner and deadline to every exception "
                            "that prevents the next volume increase."
                        ),
                        (
                            "Decision is proceed with a 50-call capped pilot, not unrestricted "
                            "scale. The operator owns payment verification; the routing contractor "
                            "owns duration-clock testing. A missing publisher source declaration "
                            "must be resolved before its first call. The next cap review "
                            "occurs after cleared net-7 payment."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance only when both counterparties are verified, qualification and "
                    "scrub terms are signed, source evidence is reproducible, and a named "
                    "owner has approved a cash-funded pilot cap without assuming uncollected receipts."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Escrow/Reserve Float & Working-Capital Calculator",
                "purpose": (
                    "Reconcile gross exchange settlements, acquisition payouts, retained "
                    "contribution, operating costs, and owner profit without treating buyer "
                    "sales as operator revenue. Use the canonical annual scenarios as fixed "
                    "anchors, then calculate payment timing, restricted balances, and stress "
                    "losses as separate cash-management schedules."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Enter the three canonical scenarios exactly before testing any "
                        "custom assumptions. Calculate retained contribution as gross "
                        "settlements multiplied by 0.55, and calculate owner profit using "
                        "the stated gross-basis margin rather than applying that margin "
                        "again to retained contribution."
                    ),
                    (
                        "Build one accepted-call cohort with all associated publisher and "
                        "media costs, including unsuccessful attempts. Divide aggregate "
                        "costs by accepted calls only after reconciliation; otherwise, "
                        "cheap-looking accepted units can conceal the acquisition expense "
                        "generated by rejected traffic."
                    ),
                    (
                        "Separate baseline monthly overhead from the complete annual expense "
                        "bridge. The published overhead range does not replace contractors, "
                        "transaction costs, other operating expenses, or losses already "
                        "needed to reconcile the canonical owner-profit figures without double counting."
                    ),
                    (
                        "Model receipt dates and payment dates on a calendar rather than "
                        "using profit as a cash proxy. Keep contractual escrow, internal "
                        "reserves, receivables, and available bank cash in distinct accounts "
                        "with explicit release conditions and reconciled ownership."
                    ),
                    (
                        "Stress collections, acquisition prices, and dispute rates independently "
                        "before combining them. Label every stress result as a deviation "
                        "from the canonical scenario, then set a traffic reduction rule "
                        "that activates before unrestricted cash falls below the funded payment floor."
                    ),
                ],
                "fields": [
                    field(
                        "Conservative canonical annual bridge",
                        "textarea",
                        (
                            "Reproduce the Conservative scenario with gross settlements, the "
                            "45% acquisition allocation, 55% retained contribution, residual "
                            "costs, owner profit, and both margin denominators. Preserve "
                            "the stated staffing model without adding hypothetical revenue."
                        ),
                        (
                            "Conservative gross settlements are $200,000; acquisition costs "
                            "are $90,000; retained contribution is $110,000. Other costs "
                            "total $80,000, leaving $30,000 owner net profit. Gross-basis "
                            "margin is 15%; retained-basis margin is 27.27%. Staffing "
                            "remains one full-time operator plus two contractors."
                        ),
                    ),
                    field(
                        "Base canonical annual bridge",
                        "textarea",
                        (
                            "Reproduce the Base scenario exactly and show why the retained "
                            "margin differs from the gross-basis margin. Record the owner-profit "
                            "amount without rounding it to a nearby marketing headline "
                            "or changing its denominator."
                        ),
                        (
                            "Base gross settlements are $850,000; acquisition costs are "
                            "$382,500; retained contribution is $467,500. Other costs "
                            "total $267,750, leaving exactly $199,750 owner net profit. "
                            "The margins are 23.5% of gross and 42.73% of retained "
                            "contribution, with one full-time operator plus two contractors."
                        ),
                    ),
                    field(
                        "Scaled canonical annual bridge",
                        "textarea",
                        (
                            "Reproduce the Scaled Small-Team scenario, including all five "
                            "people and the residual cost bridge. Distinguish increasing "
                            "settlement volume from increasing retained share, which remains "
                            "fixed at the canonical 55% assumption."
                        ),
                        (
                            "Scaled gross settlements are $1,500,000; acquisition costs "
                            "are $675,000; retained contribution is $825,000. Other costs "
                            "total $345,000, leaving $480,000 owner net profit. Gross "
                            "margin is 32%; retained margin is 58.18%. Staffing "
                            "is two full-time people plus three contractors."
                        ),
                    ),
                    field(
                        "Accepted-call unit bridge and revenue presentation",
                        "textarea",
                        (
                            "Convert the Base scenario into an illustrative accepted-call "
                            "count, then distinguish settlement volume from retained revenue. "
                            "Document the principal-versus-agent assessment needed for actual "
                            "ASC 606 presentation instead of assuming every exchange is identical."
                        ),
                        (
                            "At $100 per settled call, 8,500 annual calls produce $850,000 "
                            "gross settlements. Each allocates $45 acquisition, $55 retained "
                            "contribution, $31.50 other costs, and $23.50 owner profit. "
                            "The model uses net presentation; actual presentation follows "
                            "the control assessment in ASC 606-10-55-36 through 55-40."
                        ),
                    ),
                    field(
                        "Baseline overhead and complete cost allocation",
                        "textarea",
                        (
                            "Allocate baseline overhead and remaining expenses so their sum "
                            "equals each scenario's residual costs. Identify which ledger "
                            "accounts include people, platforms, losses, and transaction "
                            "charges, preventing any expense from appearing twice."
                        ),
                        (
                            "An illustrative allocation uses Conservative core overhead "
                            "$48,000 plus $32,000 other costs; Base $108,000 plus "
                            "$159,750; Scaled $168,000 plus $177,000. Monthly core "
                            "amounts are $4,000, $9,000, and $14,000. These reconcile "
                            "the annual bridges while remaining inside the stated overhead range."
                        ),
                    ),
                    field(
                        "Payment-gap working-capital requirement",
                        "textarea",
                        (
                            "Calculate acquisition cash needed between publisher payment and "
                            "buyer receipt using annual acquisition expense divided by 365. "
                            "State the timing assumptions explicitly and model late payment "
                            "as additional exposure rather than extra revenue."
                        ),
                        (
                            "Base acquisition outflow averages $382,500 / 365 = $1,047.95 "
                            "daily. Publisher net-2 against buyer net-7 creates a five-day "
                            "gap requiring $5,239.73 before other cash needs. Collection "
                            "on day 21 instead requires $19,910.96 for the 19-day "
                            "gap, adding $14,671.23 of funding pressure."
                        ),
                    ),
                    field(
                        "Dispute reserve and accounting treatment",
                        "textarea",
                        (
                            "Set a reserve policy using unsettled exposure and observed dispute "
                            "behavior. Distinguish earmarked cash from recognized expense, "
                            "buyer receivable allowances, and publisher liabilities; specify "
                            "who authorizes a release after the relevant risk expires."
                        ),
                        (
                            "For $20,000 of unsettled gross invoices, management earmarks "
                            "10%, or $2,000, as internal cash reserve. Moving that cash "
                            "does not itself create expense. A separately supported $600 "
                            "receivable allowance affects earnings; the controller checks "
                            "existing loss allocations before posting any additional charge."
                        ),
                    ),
                    field(
                        "Startup cash, escrow, and unrestricted balance",
                        "textarea",
                        (
                            "Allocate startup capital among setup spending, payment-gap funding, "
                            "internal reserves, and accessible operating cash. Identify any "
                            "third-party escrow agreement separately, including ownership, "
                            "release triggers, and whether the balance can fund publisher payments."
                        ),
                        (
                            "A $30,000 startup budget allocates $6,000 to setup, $5,239.73 "
                            "to the modeled payment gap, and $2,000 to an internal "
                            "reserve, leaving $16,760.27 unrestricted. If a buyer also "
                            "requires $3,000 contractual escrow, accessible cash falls "
                            "to $13,760.27; the escrow is not another expense."
                        ),
                    ),
                    field(
                        "Acquisition and collection sensitivity",
                        "textarea",
                        (
                            "Apply one explicit acquisition-cost shock and one collection-loss "
                            "shock to the Base scenario. Keep the canonical reference "
                            "unchanged, disclose the changed retained share, and avoid "
                            "presenting stressed results as the published Base case."
                        ),
                        (
                            "If annual media allocation of $25,500 rises 20%, additional "
                            "cost is $5,100 and Base profit falls to $194,650. "
                            "An additional 2% collection loss on $850,000 removes "
                            "$17,000. Combined incremental shocks leave $177,650, assuming "
                            "no recovery, volume change, or duplicate loss provision."
                        ),
                    ),
                    field(
                        "Cash release and owner distribution test",
                        "textarea",
                        (
                            "Specify a cash waterfall that pays due obligations before "
                            "distributions. Include collected receipts, publisher liabilities, "
                            "operating payments, restricted balances, and the minimum "
                            "liquidity floor; do not substitute accrued owner profit for available cash."
                        ),
                        (
                            "With $40,000 bank cash, deduct $9,000 payable to publishers, "
                            "$9,000 due operating costs, $3,000 escrow, $2,000 internal "
                            "reserve, and a $10,000 liquidity floor. Maximum distributable "
                            "cash is $7,000. The annual $199,750 Base profit figure "
                            "does not override this current cash limit."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance when all three annual bridges reconcile exactly, the retained "
                    "share remains 0.55 in canonical cases, startup allocations sum to cash "
                    "available, and the operator can fund the modeled payment delay without "
                    "spending escrow or counting unpaid receivables as cash."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "End-to-End Execution, Idempotent Ledger & QA Pre-Flight Sheet",
                "purpose": (
                    "Map each call from source attribution through auction, connection, "
                    "qualification, dispute, and cash settlement. Establish deterministic "
                    "identifiers and append-only accounting events so retries, delayed "
                    "webhooks, contradictory duration records, and partial remittances cannot "
                    "create duplicate revenue or erase the original transaction evidence."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Draw the complete event sequence before configuring Ringba or "
                        "Retreaver. Name the authoritative system for call identity, "
                        "buyer connection, measured duration, qualification status, "
                        "invoice issuance, and bank receipt so conflicting records "
                        "have a predetermined resolution path."
                    ),
                    (
                        "Create a stable internal call identifier and persist every "
                        "provider identifier as a mapping. Use separate keys for "
                        "event delivery and economic posting because one call can "
                        "legitimately produce several events but only one settlement "
                        "for each contracted obligation."
                    ),
                    (
                        "Implement transaction boundaries around qualification and ledger "
                        "posting. Acknowledge a webhook only after durable receipt, "
                        "process it with bounded retries, and send exhausted failures "
                        "to a review queue without manufacturing a successful disposition "
                        "or replaying an uncontrolled buyer transfer."
                    ),
                    (
                        "Test duration boundaries, caller disconnects, stale bid responses, "
                        "duplicate callbacks, and buyer capacity exhaustion using authorized "
                        "test numbers. Compare expected events with actual ledger "
                        "entries, including the absence of entries when a call "
                        "never satisfies the agreed billable conditions."
                    ),
                    (
                        "Reconcile the first production cohort across call records, "
                        "qualification evidence, invoices, publisher accruals, and bank "
                        "receipts. Resolve differences by appending documented corrections "
                        "rather than editing history, and preserve the exact route "
                        "and rate versions used when each call occurred."
                    ),
                ],
                "fields": [
                    field(
                        "Event map and authoritative timestamps",
                        "textarea",
                        (
                            "List the events that define the call lifecycle and identify "
                            "the authoritative timestamp for each. Explain how the system "
                            "handles delayed delivery without confusing webhook arrival "
                            "time with the underlying business event."
                        ),
                        (
                            "Call C039-0001 records source capture, ping sent, bid accepted, "
                            "buyer answered, 120-second qualification, disconnect, invoice, "
                            "and receipt. Buyer-answer time starts the duration clock. "
                            "A webhook arriving 40 seconds late keeps its original "
                            "event timestamp and records ingestion time separately for "
                            "latency measurement."
                        ),
                    ),
                    field(
                        "Idempotency keys and uniqueness constraints",
                        "textarea",
                        (
                            "Define delivery deduplication, economic uniqueness, and correction "
                            "identifiers separately. Describe how the database prevents two "
                            "workers from posting the same billable event while permitting "
                            "a later, explicitly linked reversal or adjustment."
                        ),
                        (
                            "Webhook delivery is unique on provider plus provider_event_id. "
                            "The settlement posting is unique on internal_call_id, buyer_id, "
                            "and obligation_version. Two workers racing on C039-0001 "
                            "produce one $100 receivable. A later $100 reversal uses "
                            "a new adjustment identifier referencing the original posting, "
                            "never a deleted row."
                        ),
                    ),
                    field(
                        "Ping request minimization and timeout budget",
                        "textarea",
                        (
                            "Specify the auction request fields, permissible recipients, "
                            "timeout budget, and treatment of late responses. Send only "
                            "attributes needed to price eligible demand, reserving consumer "
                            "identifiers for a justified and authorized transfer stage."
                        ),
                        (
                            "The ping carries service category, coarse geography, source "
                            "class, and a short-lived auction identifier rather than "
                            "the caller's phone number. The engineering target is a "
                            "700-millisecond total decision budget, subject to provider "
                            "capabilities. Bids received after auction closure cannot "
                            "replace the selected buyer."
                        ),
                    ),
                    field(
                        "Bid token, reservation, and post behavior",
                        "textarea",
                        (
                            "Describe how the selected bid becomes a single authorized "
                            "transfer, including token expiry, capacity reservation, and "
                            "ambiguous response handling. Prevent network retries from "
                            "creating two live transfers or a second charge."
                        ),
                        (
                            "Buyer A returns a $100 bid with a five-second validity "
                            "window. The adapter stores the winning token before transfer "
                            "and consumes it once. If the post request times out "
                            "after possible acceptance, the worker queries status or "
                            "holds for review rather than blindly posting again."
                        ),
                    ),
                    field(
                        "Qualification state machine and duration boundary",
                        "textarea",
                        (
                            "Define permitted state transitions and the evidence required "
                            "for billable status. Include exact boundary behavior and "
                            "ensure an apparently long total call cannot qualify "
                            "when connected buyer conversation remains below the contracted threshold."
                        ),
                        (
                            "States progress from received to auctioned, connected, qualified, "
                            "invoiced, and settled, with separate rejected and disputed "
                            "branches. A 119.999-second buyer connection fails a 120-second "
                            "rule; 120.000 seconds passes if other predicates hold. "
                            "A 150-second call containing 40 seconds of IVR "
                            "remains below the buyer-duration threshold."
                        ),
                    ),
                    field(
                        "Settlement subledger and accounting adapter",
                        "textarea",
                        (
                            "Show the gross settlement, acquisition obligations, retained "
                            "contribution, and later cash movements for one accepted "
                            "call. Separate operational subledger facts from the journal "
                            "presentation required by the approved principal-versus-agent accounting assessment."
                        ),
                        (
                            "For C039-0001, the subledger records $100 buyer receivable, "
                            "$42 publisher obligation, $3 media allocation, and $55 "
                            "retained contribution. A net-presentation adapter recognizes "
                            "the retained amount under the documented accounting policy. "
                            "Buyer receipt clears the receivable; publisher payment clears "
                            "its liability without recognizing revenue again."
                        ),
                    ),
                    field(
                        "Webhook authentication and retry handling",
                        "textarea",
                        (
                            "Record the provider-supported authentication method, replay controls, "
                            "durable receipt procedure, and retry schedule. Define how "
                            "unauthenticated events and exhausted retries are isolated "
                            "without exposing secrets or losing the original event body."
                        ),
                        (
                            "Where supported, the endpoint verifies the provider's documented "
                            "signature over the original request body and checks its "
                            "timestamp tolerance. A restricted inbox stores accepted events "
                            "before processing. Retries occur after 5, 30, and 120 "
                            "seconds; repeated failure opens a ticket with redacted "
                            "payload references."
                        ),
                    ),
                    field(
                        "Recording, transcript, and evidence linkage",
                        "textarea",
                        (
                            "Specify how recording identifiers, transcript versions, permissions, "
                            "and evidence hashes attach to the call record. Prevent "
                            "a regenerated transcript or renamed object from silently "
                            "replacing the evidence used for qualification and dispute review."
                        ),
                        (
                            "C039-0001 links to an access-controlled recording object, its "
                            "SHA-256 digest, capture timestamp, disclosure evidence, and "
                            "transcript version 1. A corrected transcript becomes version "
                            "2 with reviewer identity. The original remains intact "
                            "under the applicable retention schedule; ordinary dashboard "
                            "users receive no unrestricted recording download."
                        ),
                    ),
                    field(
                        "Pre-flight test matrix and expected postings",
                        "textarea",
                        (
                            "Write concrete test cases for duration, duplication, auction "
                            "failure, and partial settlement. Include expected ledger "
                            "counts and monetary amounts so a passing dashboard "
                            "status cannot conceal an incorrect or duplicated economic result."
                        ),
                        (
                            "Six fixtures cover 119-second rejection, 120-second acceptance, "
                            "duplicate qualification webhook, expired bid, caller abandonment, "
                            "and $60 partial receipt. Only the accepted fixture posts "
                            "$100 once. Its partial receipt leaves $40 outstanding; "
                            "none of the rejected fixtures creates a buyer receivable "
                            "or an automatic publisher payment."
                        ),
                    ),
                    field(
                        "Daily reconciliation and correction ownership",
                        "textarea",
                        (
                            "Define the daily comparison across provider records, internal "
                            "qualification, invoices, publisher obligations, and bank receipts. "
                            "State how unmatched records are aged, assigned, and "
                            "corrected without changing historical evidence or silently netting unrelated balances."
                        ),
                        (
                            "The daily cohort contains 100 accepted calls and $10,000 "
                            "gross settlement, with $4,200 publisher obligations and "
                            "$300 media allocation. A buyer report containing only "
                            "98 calls creates a $200 exception. The operator investigates "
                            "the two identifiers before invoicing corrections or releasing "
                            "any associated disputed amount."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance after all boundary and replay fixtures produce the expected "
                    "single postings, unauthorized events are rejected, ambiguous transfers "
                    "are contained, and the first production cohort reconciles to source "
                    "records with individually owned exceptions."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract Addendum & Compliance Audit",
                "purpose": (
                    "Translate applicable communications, insurance, recording, privacy, "
                    "and professional-referral rules into route-specific controls and "
                    "evidence requirements. Distinguish current legal obligations from "
                    "stricter contractual policies, especially for inbound calls, automated "
                    "callbacks, Medicare marketing, and attorney advertising, where "
                    "different activities trigger materially different duties."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Classify the actual activity before applying a rule: consumer-initiated "
                        "inbound call, live outbound callback, automated marketing contact, "
                        "Medicare appointment, or attorney referral. Record applicable "
                        "jurisdictions and effective dates rather than treating every "
                        "call exchange as one statutory category."
                    ),
                    (
                        "Correct the consent premise in the operating specification: "
                        "the FCC's 2023 one-to-one lead-generation amendment was "
                        "vacated before taking effect. Preserve named-buyer permission "
                        "as a contractual control where appropriate, while separately "
                        "applying existing TCPA requirements and CMS-specific sharing restrictions."
                    ),
                    (
                        "Inspect actual consumer-facing language and preserved evidence "
                        "instead of accepting a certificate label as conclusive. "
                        "TrustedForm and Jornaya records support provenance, but "
                        "the route still needs valid disclosures, appropriate scope, "
                        "revocation handling, and proof matching the communication actually made."
                    ),
                    (
                        "Create separate Medicare and legal-service schedules before "
                        "either vertical receives traffic. Test call-recording duties, "
                        "appointment timing, permitted information sharing, professional "
                        "licensing, and referral compensation against the specific "
                        "service and jurisdiction rather than copying emergency-trade terms."
                    ),
                    (
                        "Assign remediation owners and evidence deadlines for every "
                        "failed control, then disable only the affected route "
                        "until repaired. Preserve lawful records under a documented "
                        "retention schedule, restrict access by role, and verify "
                        "the repair with a reproducible test before restoring traffic."
                    ),
                ],
                "fields": [
                    field(
                        "TCPA rule status and named-buyer policy",
                        "textarea",
                        (
                            "Document the distinction between the vacated FCC amendment, "
                            "existing TCPA consent duties, and your own buyer-specific "
                            "permission requirement. Cite the applicable authorities and "
                            "identify the communication technology and purpose being evaluated."
                        ),
                        (
                            "The register cites 47 U.S.C. § 227 and 47 CFR "
                            "§ 64.1200. Insurance Marketing Coalition Ltd. v. FCC, "
                            "127 F.4th 303 (11th Cir. 2025), vacated the new "
                            "one-to-one amendment. Our contract still requires named-buyer "
                            "permission for covered transfers without describing that "
                            "policy as the vacated federal rule."
                        ),
                    ),
                    field(
                        "Consent evidence and revocation linkage",
                        "textarea",
                        (
                            "Identify the consent language, seller identity, capture timestamp, "
                            "page version, evidence reference, and revocation status "
                            "required for the planned contact. Explain how evidence "
                            "is verified without assuming a vendor certificate establishes every legal element."
                        ),
                        (
                            "Record CF-039-81 links the rendered disclosure, Buyer A "
                            "identity, consumer action, timestamp, source page, and "
                            "TrustedForm certificate reference. Jornaya evidence, when used, "
                            "receives the same review. A subsequent revocation is "
                            "linked to the consumer record and suppresses affected "
                            "future contacts before another campaign export."
                        ),
                    ),
                    field(
                        "Inbound versus outbound contact classification",
                        "textarea",
                        (
                            "Separate consumer-initiated inbound calls from callbacks, prerecorded "
                            "messages, automated dialing, and marketing texts. Record "
                            "which technology and purpose trigger consent requirements "
                            "so an inbound inquiry is not treated as unlimited permission for later campaigns."
                        ),
                        (
                            "A consumer directly dialing the plumbing number enters "
                            "the inbound route. A requested live callback receives "
                            "its own purpose and timing record. Prerecorded promotional "
                            "callbacks and automated marketing texts remain disabled "
                            "unless their applicable consent requirements are satisfied; "
                            "the original inbound call alone does not authorize them."
                        ),
                    ),
                    field(
                        "DNC suppression and restricted-contact screening",
                        "textarea",
                        (
                            "Specify registry refresh, entity-specific suppression, permitted "
                            "exceptions, and real-time checks for applicable outbound "
                            "activity. Distinguish statutory suppression from supplementary "
                            "litigation-risk screening, which cannot replace consent evidence or justify evasive contacting."
                        ),
                        (
                            "Outbound telemarketing checks the National Do Not Call "
                            "Registry on the required refresh cycle, including the "
                            "31-day framework in 16 CFR § 310.4(b)(3)(iv), plus "
                            "current entity-specific suppression. Supplementary litigation-risk "
                            "screening is documented separately. A registry match does "
                            "not block a consumer's voluntary inbound service request."
                        ),
                    ),
                    field(
                        "Medicare TPMO recording and retention",
                        "textarea",
                        (
                            "Identify whether the organization acts as a Medicare "
                            "third-party marketing organization and which calls require "
                            "recording. Specify recording scope, applicable retention, "
                            "access restrictions, and the technical response when required capture fails."
                        ),
                        (
                            "For the Medicare route, the register maps TPMO marketing, "
                            "sales, and enrollment call recording to 42 CFR "
                            "§§ 422.2274(g) and 423.2274(g), including applicable "
                            "ten-year retention obligations. Required calls cannot proceed "
                            "without working capture and required disclosures. Other "
                            "service calls follow their own purpose-specific retention rules."
                        ),
                    ),
                    field(
                        "Medicare scope-of-appointment timing",
                        "textarea",
                        (
                            "Document when a Medicare scope of appointment is required, "
                            "the applicable 48-hour timing rule, and supported "
                            "exceptions. Keep appointment timing separate from inbound "
                            "call qualification so a duration threshold cannot substitute for appointment evidence."
                        ),
                        (
                            "A scheduled personal marketing appointment records its scope "
                            "at least 48 hours beforehand under 42 CFR "
                            "§§ 422.2264(c) and 423.2264(c), unless a documented "
                            "exception applies. Relevant exceptions include beneficiary-initiated "
                            "walk-ins and qualifying end-of-election-period circumstances. "
                            "The worksheet does not impose a blanket 48-hour hold "
                            "on every inbound call."
                        ),
                    ),
                    field(
                        "Medicare TPMO sharing and recipient permission",
                        "textarea",
                        (
                            "Identify proposed recipients of Medicare beneficiary information "
                            "and the written permission supporting each transfer. "
                            "Separate CMS's TPMO sharing requirements from FCC "
                            "rule status and prohibit broad distribution unsupported by the applicable recipient-specific permission."
                        ),
                        (
                            "The Medicare intake flow names each receiving TPMO "
                            "and supports separate permission for each under 42 "
                            "CFR §§ 422.2274(g) and 423.2274(g). Permission for "
                            "Buyer M does not authorize sending beneficiary contact "
                            "information to Buyers N and P. An auction must "
                            "not broadcast personal information to unauthorized recipients."
                        ),
                    ),
                    field(
                        "Legal advertising, referral compensation, and licensing",
                        "textarea",
                        (
                            "Define the jurisdiction-specific legal-services model, attorney "
                            "license verification, advertising review, and compensation "
                            "structure. Determine whether the exchange constitutes "
                            "a regulated referral service or prohibited solicitation rather than assuming a call fee is always permissible."
                        ),
                        (
                            "A California legal route remains disabled until its "
                            "model is reviewed against Business and Professions "
                            "Code §§ 6151–6156 and Rule of Professional Conduct "
                            "7.2. The draft excludes case-proceeds percentages, "
                            "paid recommendations, and prohibited runner activity. "
                            "An advertising label alone does not resolve lawyer-referral "
                            "service registration requirements."
                        ),
                    ),
                    field(
                        "State recording, privacy, and deletion controls",
                        "textarea",
                        (
                            "Map caller and recipient locations to recording and "
                            "privacy requirements, including notice, permission, access, "
                            "and deletion handling. Explain how legally required "
                            "retention or a documented preservation hold interacts with ordinary deletion requests."
                        ),
                        (
                            "California calls receive review under Penal Code § 632; "
                            "federal interception requirements are assessed under "
                            "18 U.S.C. § 2511. Where applicable, California "
                            "privacy requests follow Civil Code § 1798.100 "
                            "et seq. A deletion request triggers verification "
                            "and a documented exception assessment, not automatic "
                            "destruction of required Medicare records."
                        ),
                    ),
                    field(
                        "Contract addendum and audit remediation",
                        "textarea",
                        (
                            "Write enforceable operational clauses for evidence access, "
                            "source restrictions, subcontractors, security incidents, "
                            "scrub deadlines, and rule changes. Identify the "
                            "audit sample and restoration evidence required after a material source or routing failure."
                        ),
                        (
                            "The addendum requires approved sources, preserved disclosure "
                            "versions, prompt incident notice, and evidence delivery "
                            "within two business days. A 25-call sample with "
                            "three missing permission records suspends that source. "
                            "Restoration requires corrected capture, review of the "
                            "affected cohort, and a clean ten-call verification "
                            "sample with named reviewer sign-off."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance only when the activity-specific legal register distinguishes "
                    "current rules from stricter policy, applicable licenses are verified, "
                    "required consent and recording evidence can be retrieved, and unresolved "
                    "Medicare or legal-service defects keep those routes disabled."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation Pipeline, Acquisition Flywheel & Risk Fallback Tracker",
                "purpose": (
                    "Design a small-team operating loop that acquires suitable callers, "
                    "routes them to eligible buyers, learns from verified outcomes, "
                    "and limits losses when dependencies fail. Connect automation "
                    "decisions to settlement evidence rather than optimizing for "
                    "cheap calls, long conversations, or uncollected dashboard revenue."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Implement one observable routing path before adding branches. "
                        "Use Ringba or Retreaver capabilities actually enabled "
                        "in the account, record configuration versions, and "
                        "measure the complete decision latency rather than "
                        "assuming a vendor feature makes every auction sub-second."
                    ),
                    (
                        "Connect source evidence and eligibility checks before "
                        "price optimization. A high bid cannot repair missing "
                        "permission, an unlicensed service recipient, or exhausted "
                        "buyer capacity; those conditions must remove the "
                        "buyer from the candidate set before economic ranking begins."
                    ),
                    (
                        "Treat AI transcript disposition as an assisted classification "
                        "layer with sampled review. Keep deterministic duration, "
                        "geography, and ledger rules authoritative, and prevent "
                        "unreviewed model output from creating retroactive scrubs, "
                        "new consumer-contact permission, or irreversible payment deductions."
                    ),
                    (
                        "Send server-to-server advertising feedback only after the "
                        "chosen outcome has satisfied its definition. Separate "
                        "qualified, accepted, and collected events so campaign "
                        "optimization does not reward disputed calls or "
                        "count the same transaction multiple times across retries."
                    ),
                    (
                        "Define a fallback for every external dependency and "
                        "exercise it with authorized fixtures. Prefer reduced "
                        "volume, a clearly unavailable route, or a "
                        "permitted alternate buyer over silent evidence loss, "
                        "uncontrolled transfers, or acquisition spending that continues during a collection freeze."
                    ),
                ],
                "fields": [
                    field(
                        "Routing tree and latency service objective",
                        "textarea",
                        (
                            "Describe the routing order, eligible buyer filters, "
                            "auction timing, and measurable latency objective. "
                            "Record the behavior when the deadline expires "
                            "and avoid implying that a sub-second target supersedes permission or capacity checks."
                        ),
                        (
                            "Route version R17 checks service eligibility, recipient "
                            "permission, geography, capacity, and then bid price. "
                            "The target is 95% of decisions within "
                            "700 milliseconds during the pilot. An expired "
                            "auction sends the caller to the documented "
                            "unavailable-service path unless an independently eligible "
                            "fallback buyer is already configured."
                        ),
                    ),
                    field(
                        "Evidence verification and dependency failure",
                        "textarea",
                        (
                            "Specify how TrustedForm or Jornaya references are "
                            "retrieved, validated, and attached to the call. "
                            "Define which activities can continue during "
                            "verification outages and which require holding or stopping the affected contact workflow."
                        ),
                        (
                            "The intake worker retrieves the evidence reference "
                            "and checks it against source, timestamp, and "
                            "disclosure version before a covered transfer. "
                            "A vendor timeout creates an evidence-pending "
                            "state, not assumed permission. A direct "
                            "inbound service route may continue only if "
                            "its own documented requirements are independently satisfied."
                        ),
                    ),
                    field(
                        "AI disposition controls and review sample",
                        "textarea",
                        (
                            "Define transcript labels, model confidence handling, "
                            "human review sampling, and prohibited automated "
                            "actions. Measure classification errors against adjudicated "
                            "examples, especially where a wrong label changes billing, source restrictions, or consumer treatment."
                        ),
                        (
                            "The classifier suggests service intent, wrong geography, "
                            "duplicate inquiry, and agent disconnect. Twenty "
                            "of every 100 pilot calls receive manual "
                            "review, plus every low-confidence result. A "
                            "model suggestion cannot reverse the $100 "
                            "settlement; a reviewer must link contract "
                            "criteria and evidence before an adjustment is posted."
                        ),
                    ),
                    field(
                        "Server-to-server conversion event design",
                        "textarea",
                        (
                            "List conversion stages, stable identifiers, event "
                            "values, and supported correction behavior for "
                            "the advertising platform. Send the minimum "
                            "permitted information and ensure retries preserve event identity instead of manufacturing additional conversions."
                        ),
                        (
                            "Event C039-0001-qualified reports the defined qualification "
                            "stage; C039-0001-collected reports verified collection "
                            "when the destination supports that separate "
                            "goal. Retained value is $55 before "
                            "other costs, not the buyer's plumbing "
                            "invoice. Duplicate deliveries retain the same "
                            "event identifier, and corrections use documented platform mechanisms."
                        ),
                    ),
                    field(
                        "Acquisition flywheel and source cohort learning",
                        "textarea",
                        (
                            "Describe how source-level outcomes inform keyword "
                            "selection, landing-page revisions, publisher allocations, "
                            "and bid limits. Compare cohorts using "
                            "accepted and collected contribution rather than raw call count, while preserving evidence for each revision."
                        ),
                        (
                            "Campaign A sends 80 calls, produces 50 "
                            "accepted settlements, and collects $5,000. "
                            "Its matched acquisition expense is $2,250, "
                            "leaving $2,750 retained contribution. Campaign B "
                            "has more calls but worse collected "
                            "contribution per acquisition dollar. The next "
                            "test shifts only 10% of budget and retains page-version records."
                        ),
                    ),
                    field(
                        "CPC spike detector and acquisition ceiling",
                        "textarea",
                        (
                            "Set an acquisition-cost ceiling using the "
                            "complete accepted-call cohort, not isolated "
                            "click prices. Define the observation window, "
                            "minimum sample, reduction amount, and restoration conditions when paid-search cost rises faster than collectible settlement value."
                        ),
                        (
                            "The reference ceiling is $45 combined acquisition "
                            "per accepted $100 call. If a "
                            "50-call cohort exceeds $49.50, spend "
                            "falls 25% pending source review. A "
                            "rise from $3 to $3.60 in "
                            "allocated media cost alone increases combined "
                            "cost to $45.60 and triggers monitoring rather than immediate shutdown."
                        ),
                    ),
                    field(
                        "Buyer scrub and collectability circuit breaker",
                        "textarea",
                        (
                            "Define buyer-level disputed-value, overdue-value, and "
                            "collection-lag thresholds with distinct responses. "
                            "Prevent a high auction bid from "
                            "overriding a collection freeze, and state which verified evidence is required before restoring the original traffic ceiling."
                        ),
                        (
                            "A buyer with more than $2,000 overdue "
                            "or disputed value above 5% of "
                            "its recent $20,000 cohort loses "
                            "new allocation. Existing disputes remain "
                            "tracked individually. Restoration requires cleared "
                            "receipts, resolved systemic qualification issues, "
                            "and a reduced 25-call test rather than an account manager's payment promise."
                        ),
                    ),
                    field(
                        "Observability, alert routing, and response ownership",
                        "textarea",
                        (
                            "Choose operational and economic metrics with "
                            "explicit thresholds, recipients, and response "
                            "times. Separate availability failures from "
                            "margin erosion so a green telephony dashboard cannot hide missing evidence, growing disputes, or unpaid settlement balances."
                        ),
                        (
                            "Alerts fire when auction latency exceeds "
                            "900 milliseconds at the 95th percentile, "
                            "evidence-pending calls exceed five, or "
                            "unmatched accepted calls exceed two. "
                            "The routing contractor handles latency; "
                            "the operator handles settlement exposure. "
                            "Critical routing faults receive a ten-minute response target and a documented traffic decision."
                        ),
                    ),
                    field(
                        "Dependency fallback and recovery exercise",
                        "textarea",
                        (
                            "List failure responses for telephony, buyer "
                            "availability, evidence retrieval, ledger posting, "
                            "and advertising feedback. Distinguish safely "
                            "queued work from live calls that cannot wait, and require a reconciliation check before queued events are replayed."
                        ),
                        (
                            "If the ledger is unavailable, new paid "
                            "acquisition pauses and durable received "
                            "events remain queued. If Buyer A "
                            "fails, only eligible Buyer B receives "
                            "live transfers. During recovery, the "
                            "worker deduplicates 300 queued events "
                            "against existing postings before resuming normal volume, preventing duplicate revenue and publisher liabilities."
                        ),
                    ),
                    field(
                        "Access control and automation change record",
                        "textarea",
                        (
                            "Define least-privilege roles, secret storage, "
                            "configuration review, and rollback evidence "
                            "for route changes. Identify which "
                            "permissions can change payouts, export recordings, or alter buyer destinations, and separate those powers from ordinary monitoring access."
                        ),
                        (
                            "The routing contractor can propose R18 "
                            "but cannot edit bank instructions "
                            "or export bulk recordings. The "
                            "operator approves destination and rate "
                            "changes after fixture comparison. Credentials "
                            "remain in the platform's supported "
                            "secret store. A failed R18 deployment restores R17 and preserves both configuration versions and test results."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance when source evidence, routing, disposition review, and conversion "
                    "feedback operate with stable identifiers; each critical dependency has "
                    "an exercised fallback; and collection or acquisition thresholds can "
                    "reduce traffic without manual reconstruction of the call ledger."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod KPI Scorecard & Exit-Readiness Ledger",
                "purpose": (
                    "Turn the operating design into a bounded launch with dated "
                    "deliverables, measurable evidence, and explicit staffing ownership. "
                    "Track whether the pod can acquire, qualify, collect, reconcile, "
                    "and document calls consistently before increasing exposure or "
                    "presenting the business as a transferable operating asset."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Schedule the launch around evidence-producing milestones rather "
                        "than a promised revenue date. The expected first "
                        "deal window is one to three months, so "
                        "a 30-day sprint can finish with a verified "
                        "pipeline and tested system even when commercial collection occurs later."
                    ),
                    (
                        "Assign the one full-time operator and two contractors "
                        "to distinct responsibilities with explicit coverage. Keep "
                        "payment authority, source review, routing changes, and "
                        "daily reconciliation visible so a small team "
                        "does not depend on undocumented access or a single contractor's private notes."
                    ),
                    (
                        "Use cohort-based daily metrics for qualification, acceptance, "
                        "collection, retained contribution, and evidence completeness. "
                        "Always show the denominator and observation period; "
                        "a strong first invoice does not establish "
                        "annual scale, and a short pilot cannot validate the full Base scenario."
                    ),
                    (
                        "Assemble transferable records while operating instead of "
                        "reconstructing them for a future buyer. Preserve "
                        "contracts, assignment provisions, settlement history, source "
                        "ownership, route versions, and restricted evidence "
                        "inventories without unnecessarily sharing consumer recordings or contact information with prospective purchasers."
                    ),
                    (
                        "Finish the sprint with a continue, hold, "
                        "or stop decision tied to collection, "
                        "cash, evidence, and concentration thresholds. "
                        "Record unfinished work honestly, maintain "
                        "the current cap where proof is missing, and distinguish a conditional operating plan from an achieved result."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–5 market and counterparty package",
                        "textarea",
                        (
                            "Define the first week's deliverables for "
                            "vertical selection, buyer verification, publisher "
                            "provenance, and contract terms. Attach "
                            "owners and evidence locations, and identify what must remain disabled while any essential commercial or statutory condition is unresolved."
                        ),
                        (
                            "By day 5, the operator selects emergency "
                            "plumbing, verifies Buyer A and "
                            "Publisher P, and assembles the "
                            "$100 rate card with the "
                            "120-second predicate. The evidence contractor "
                            "checks source disclosures. Medicare and "
                            "legal routes remain disabled because their separate activity-specific reviews are outside this initial pilot."
                        ),
                    ),
                    field(
                        "Days 6–10 routing and ledger fixtures",
                        "textarea",
                        (
                            "Specify the configuration, integration, and "
                            "test artifacts required before live "
                            "traffic. Include idempotency, timing boundaries, "
                            "evidence retrieval, and permission checks, with concrete pass criteria that another operator can reproduce from the recorded fixtures."
                        ),
                        (
                            "By day 10, the routing contractor delivers "
                            "R17, six boundary fixtures, and "
                            "a replay report showing one "
                            "$100 posting despite three duplicate "
                            "callbacks. The operator verifies partial "
                            "receipt handling and unavailable-buyer behavior. "
                            "Production spending stays at zero until every required fixture matches its expected event and ledger results."
                        ),
                    ),
                    field(
                        "Days 11–15 capped pilot and evidence review",
                        "textarea",
                        (
                            "Set pilot call limits, maximum "
                            "gross exposure, acquisition funding, and "
                            "review sampling. State what happens "
                            "if counterparties are not ready, rather than using the sprint calendar to justify unverified traffic or unsupported revenue claims."
                        ),
                        (
                            "If agreements are executed, days 11–15 "
                            "permit 10 accepted calls daily "
                            "up to 50 total, representing "
                            "$5,000 gross exposure and $2,250 "
                            "matched acquisition allocation. Twenty calls "
                            "receive full manual review. If "
                            "the buyer is not ready, the team completes authorized synthetic tests and records commercial launch as pending."
                        ),
                    ),
                    field(
                        "Days 16–20 invoice and payment verification",
                        "textarea",
                        (
                            "Define invoice preparation, buyer acceptance, "
                            "dispute review, publisher accrual, and "
                            "receipt verification deliverables. Preserve the "
                            "pilot exposure cap until actual payment evidence supports a change, even if the buyer's portal marks the invoice approved."
                        ),
                        (
                            "The operator submits the 50-call invoice "
                            "with qualification references and monitors "
                            "the net-7 due date. A "
                            "$5,000 portal approval is recorded "
                            "as receivable status, not cash. "
                            "Only a verified bank receipt "
                            "satisfies collection. Any disputed identifiers receive individual owners while undisputed publisher liabilities remain visible."
                        ),
                    ),
                    field(
                        "Days 21–25 controlled acquisition iteration",
                        "textarea",
                        (
                            "Specify the first source or "
                            "landing-page experiment, its budget limit, "
                            "evaluation window, and stopping condition. "
                            "Tie any volume increase to verified collection and evidence quality instead of extrapolating from click-through rate or raw inbound volume."
                        ),
                        (
                            "After cleared pilot payment, test a "
                            "second landing-page headline with 10% "
                            "of acquisition budget while keeping "
                            "disclosures unchanged. Increase the daily "
                            "accepted-call ceiling from 10 to "
                            "15 only if matched acquisition "
                            "stays within $45, evidence completeness remains 100%, and the modeled payment-gap cash remains funded."
                        ),
                    ),
                    field(
                        "Days 26–30 resilience and handover review",
                        "textarea",
                        (
                            "List the final resilience exercise, "
                            "ledger close, evidence inventory, and "
                            "handover tasks. Identify which launch "
                            "claims are actually demonstrated and which remain untested, including collection cycles, buyer redundancy, and sustained acquisition economics over longer observation periods."
                        ),
                        (
                            "By day 30, simulate Buyer A "
                            "unavailability, replay duplicate events, "
                            "close the pilot ledger, and "
                            "have the evidence contractor retrieve "
                            "five sampled call records. Report "
                            "one collected cohort if that "
                            "is all the evidence supports. Do not describe a 30-day pilot as proof of annual Base profit."
                        ),
                    ),
                    field(
                        "Pod ownership, staffing, and coverage",
                        "textarea",
                        (
                            "Assign operator and contractor responsibilities, "
                            "time budgets, escalation coverage, and "
                            "decision rights. Preserve the canonical "
                            "team structures while explaining the work that must be redesigned before moving from one full-time operator to the five-person Scaled pod."
                        ),
                        (
                            "Base staffing is one full-time operator "
                            "plus two contractors: one handles "
                            "routing and integrations, the other "
                            "evidence and reconciliation support. The "
                            "operator owns cash and counterparties. "
                            "Scaled staffing adds a second "
                            "full-time operator and a third contractor, reaching five people with documented backup coverage rather than hidden unpaid labor."
                        ),
                    ),
                    field(
                        "Pod KPI scorecard with cohort denominators",
                        "textarea",
                        (
                            "Record call counts, accepted value, "
                            "collected value, acquisition allocation, "
                            "disputes, evidence completeness, and "
                            "latency for one defined cohort. Show denominators and distinguish retained contribution before other expenses from owner profit after the complete cost allocation."
                        ),
                        (
                            "For a closed 100-attempt cohort, 80 "
                            "calls connect and 50 settle "
                            "and collect at $100, producing "
                            "$5,000 cash receipts. Matched acquisition "
                            "is $2,250 and retained contribution "
                            "$2,750 before other costs. Acceptance "
                            "is 50% of attempts; evidence completeness is 50/50 accepted calls, with zero unresolved settlement disputes."
                        ),
                    ),
                    field(
                        "Exit-readiness asset and obligation ledger",
                        "textarea",
                        (
                            "Inventory transferable contracts, domains, numbers, "
                            "configuration ownership, accounting records, "
                            "publisher relationships, and outstanding "
                            "obligations. Identify assignment restrictions and consumer-information limits before sharing diligence materials, keeping valuation assumptions separate from verified historical operating results."
                        ),
                        (
                            "The ledger lists two buyer agreements, "
                            "one publisher agreement, owned domains, "
                            "number-porting rights, R17 configuration, and "
                            "monthly settlement reconciliations. Buyer A "
                            "requires written assignment permission. A "
                            "prospective purchaser receives redacted cohort "
                            "summaries first; recording access requires a separately justified process. Outstanding publisher liabilities and disputes remain attached to the period."
                        ),
                    ),
                    field(
                        "Day-30 decision and next exposure ceiling",
                        "textarea",
                        (
                            "Choose continue, hold, or stop "
                            "using explicit collection, cash, "
                            "evidence, and concentration criteria. "
                            "State the next exposure ceiling, responsible owner, review date, and unfinished conditions without converting an internal readiness score into a promise of earnings."
                        ),
                        (
                            "Decision is continue at 15 accepted "
                            "calls daily only after full "
                            "net-7 collection, 100% required evidence, "
                            "and funded liquidity floor. Otherwise "
                            "hold at the current cap. "
                            "The operator reviews again after "
                            "two additional collected cohorts. The 95/100 candidate score and pipeline rank #01 are selection metadata, not measured pilot performance."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Close the sprint with a dated decision, reconciled cohort scorecard, "
                    "named pod owners, and an evidence-backed exposure ceiling. Mark any "
                    "uncollected invoice, untested route, missing assignment right, or incomplete "
                    "statutory control as unfinished work rather than reporting full launch completion."
                ),
            },
        ],
    }
