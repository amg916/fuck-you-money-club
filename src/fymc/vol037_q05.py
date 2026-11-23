from __future__ import annotations

CHAPTER_5 = {
    "id": "Q5",
    "chapter_id": "Q5",
    "chapter_number": 5,
    "question_number": 5,
    "slug": "beginner-traps-clawbacks-asymmetric-failure-modes",
    "question_prompt": "What kills 80% of newcomers in saas discount brokerage & gpo arbitrage, and what forensic metrics detect margin leaks, regulatory landmines, or platform bans before they wipe out capital?",
    "kicker": "Q5 / THE BIG MONEY PLAYBOOKS",
    "title": "Beginner Traps, Clawbacks & Asymmetric Failure Modes",
    "subtitle": "Microsoft NCE Credit Exposure, CSP Attribution Defects, VIP Entitlements, GPO Rebate Recapture, and SEC-Triggered Outreach Controls",
    "layout_template": "expert_insights",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #37, ranked #04 of 37 with a 94/100 Money-to-Manpower Score, "
        "wins through retained software spreads, residual commissions, GPO rebates, "
        "and verified renewal savings, not subscription billings disguised as revenue. "
        "Across the volume's 12 mapped plays, newcomer losses cluster around annual "
        "commitment exposure, defective partner attribution, unauthorized seat pooling, "
        "retroactive rebate changes, and acquisition practices that outrun evidence. "
        "The canonical annual owner profit cases are $32,000 Conservative, $225,000 "
        "Base, and $522,000 Scaled. This chapter converts those risks into contract "
        "checks, exposure limits, reconciliation tests, and stop-work rules. The "
        "question's 80% framing is a stress-test prompt, not an observed failure "
        "rate. Protect capital by measuring collectible contribution after reversals "
        "before expanding any apparently profitable channel."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$100,000",
            "context": "Annual retained fee revenue; client subscription spend excluded",
            "note": "32% net margin; $32,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$500,000",
            "context": "Annual retained fee revenue; client subscription spend excluded",
            "note": "45.0% net margin; $225,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$900,000",
            "context": "Annual retained fee revenue; client subscription spend excluded",
            "note": "58% net margin; $522,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Cap Annual Commitments Before Selling Monthly Convenience",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The first fatal trap is selling a payment schedule as if it changed "
                    "the underlying commitment. Microsoft NCE annual subscriptions billed "
                    "monthly can leave the transacting reseller owing the distributor after "
                    "the customer stops paying. Under an illustrative contract, 100 seats "
                    "at a $20 monthly wholesale cost create $24,000 of annual supplier "
                    "obligations. Billing the customer $22 per seat produces only $2,400 "
                    "of annual spread before servicing costs. If the customer pays three "
                    "months and defaults, nine remaining supplier installments total "
                    "$18,000, versus $600 of spread collected during those first three "
                    "months. An enforceable customer promise does not fund tomorrow's "
                    "supplier debit. Require annual prefunding wherever possible, verify "
                    "settlement before activating the commitment, and treat ACH mandates "
                    "or stored cards as collection mechanisms rather than credit protection. "
                    "Measure uncovered exposure as remaining noncancelable supplier "
                    "obligations minus specifically allocable settled customer funds and "
                    "collectible contractual protection. Do not subtract expected future "
                    "customer payments. A startup with $15,000 of available capital cannot "
                    "safely absorb this example merely because its projected margin is "
                    "positive. If prefunding fails, offer an available monthly commitment, "
                    "use a documented referral-only structure, or decline the transaction "
                    "instead of becoming an accidental lender."
                ),
                (
                    "The second trap is confusing relationship attribution with authority "
                    "to transfer subscriptions or receive compensation. CPOR is not a "
                    "universal billing-transfer instruction, and a customer relationship "
                    "record does not automatically establish CSP resale rights. Confirm "
                    "the exact Microsoft workload, partner program, transacting entity, "
                    "customer acceptance, and distributor procedure before promising a "
                    "migration date. Adobe VIP Marketplace transfers likewise depend on "
                    "the applicable agreement, reseller process, anniversary timing, and "
                    "eligible entitlements. The third trap is unauthorized cross-customer "
                    "seat pooling: a spreadsheet showing unused licenses does not permit "
                    "assignment across unrelated organizations. Keep each customer's "
                    "tenant, subscription identifiers, purchased quantities, assignments, "
                    "and approved reseller relationships separately traceable. At 400 "
                    "seats and a $1.50 monthly retained spread, annual contribution is "
                    "$7,200; a $12,000 contractual audit settlement consumes more than "
                    "twenty months of that contribution before remediation labor. "
                    "Never model the settlement as a published vendor penalty schedule; "
                    "actual remedies follow the executed terms and established facts. "
                    "Reject synthetic member companies, borrowed partner identifiers, "
                    "educational-license laundering, and fabricated customer acceptance. "
                    "The fallback is an authorized transfer or separate customer agreement, "
                    "even when that sacrifices the volume bracket. Losing a discount "
                    "is cheaper than losing the right to transact."
                ),
                (
                    "The fourth trap is assuming cancellations, seat reductions, renewals, "
                    "and suspensions share one reversible workflow. Record the applicable "
                    "Microsoft NCE cancellation window from current program terms and "
                    "the distributor's accepted order record; do not assume a generic "
                    "refund period or that suspension extinguishes the commitment. "
                    "Store order timestamps in UTC, renewal settings, quantity-change "
                    "deadlines, and evidence that the customer approved the precise "
                    "term. Run a daily renewal queue at 90, 60, 30, and seven days, "
                    "with an earlier internal deadline wherever the supplier requires "
                    "it. One mistaken renewal of 250 seats at $18 wholesale monthly "
                    "creates $54,000 of annual obligations. A $2 monthly spread on "
                    "those seats would generate only $6,000 annually, so the contractual "
                    "exposure is nine times the expected spread. Set a proposed startup "
                    "limit of uncovered commitments below 25% of unrestricted cash, "
                    "plus a separate prohibition on any single customer exceeding "
                    "that limit. These are internal risk limits, not vendor rules. "
                    "If the queue is incomplete, stop new annual orders rather than "
                    "rushing transfers. Preserve service continuity through supplier "
                    "support and customer coordination; never delete tenant data or "
                    "use administrative access as improvised debt collection leverage."
                ),
            ],
            "table": {
                "caption": "Commitment and Entitlement Defects That Overwhelm Small Spreads",
                "headers": [
                    "Failure pattern and underlying contractual exposure",
                    "Evidence required before accepting customer orders",
                    "Early warning threshold for operator intervention",
                    "Capital preserving response when evidence fails",
                ],
                "rows": [
                    [
                        "Annual commitment sold as cancellable monthly service",
                        "Signed term acceptance matched to distributor order",
                        "Any annual obligation lacking settled customer prefunding",
                        "Switch eligible orders to monthly commitment terms",
                    ],
                    [
                        "Stored payment method mistaken for credit protection",
                        "Settled funds reconciled against remaining supplier obligations",
                        "Uncovered obligations exceed 25% of unrestricted cash",
                        "Pause additional commitments and require incremental prefunding",
                    ],
                    [
                        "CPOR attribution mistaken for universal transfer authority",
                        "Workload specific partner rights and supplier transfer acceptance",
                        "Customer transfer promised before receiving written eligibility confirmation",
                        "Retain existing service until authorized transfer completes",
                    ],
                    [
                        "Unrelated tenants pooled into artificial purchasing entities",
                        "Separate customer contracts and tenant entitlement evidence",
                        "Any assigned seat lacks its authorized customer linkage",
                        "Stop pooling and regularize entitlements through supplier support",
                    ],
                    [
                        "Renewal accepted without current customer quantity confirmation",
                        "Timestamped renewal instruction and applicable supplier deadline",
                        "Renewal approaching seven days without documented owner response",
                        "Escalate immediately and follow permitted nonrenewal procedures",
                    ],
                    [
                        "Service suspension mistaken for extinguished supplier liability",
                        "Supplier terms describing suspension and continuing payment duties",
                        "Suspended subscription remains absent from exposure reporting ledger",
                        "Restore obligation tracking and coordinate customer collection separately",
                    ],
                    [
                        "Expired promotional pricing carried into renewal quotations",
                        "Current distributor quote showing renewal period pricing",
                        "Quoted customer spread falls below documented servicing costs",
                        "Requote before acceptance or decline the renewal transaction",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Checks Before an Annual Commitment Becomes Real",
                "body": (
                    "The deal owner records these checks against the order identifier. "
                    "A missing check blocks commitment creation, not customer discussion."
                ),
                "items": [
                    "Match the legal customer, tenant identifier, subscription SKU, term, quantity, and authorized purchasing contact to the accepted supplier order.",
                    "Verify annual prefunding has settled and document remaining return or dispute exposure; a payment mandate alone does not satisfy funding.",
                    "Capture the current cancellation and renewal rules, distributor processing deadlines, and named operator responsible for acting before them.",
                    "Confirm permitted partner attribution, transfer authority, and customer-specific entitlement boundaries without cross-tenant pooling or fabricated affiliations.",
                ],
            },
        },
        {
            "heading": "2. Reconstruct Every Rebate, Residual, and Savings Dollar",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The fifth trap is pricing from the highest rebate tier before "
                    "earning its conditions. Separate contractual wholesale spread from "
                    "conditional incentives, and version the partner schedule used for "
                    "every quote. Suppose eligible annual client purchases are $600,000 "
                    "and a GPO administrative rebate is 2%; the potential operator "
                    "receipt is $12,000, not $600,000. If returns and excluded product "
                    "categories reduce eligible purchases to $450,000, the same rate "
                    "produces $9,000. If the agreement instead applies a lower 1% "
                    "tier retroactively at that volume, the receipt becomes $4,500. "
                    "The $7,500 difference from the original expectation can erase "
                    "an entire acquisition cohort's contribution. Document whether "
                    "tiers are incremental or retroactive, whether affiliated members "
                    "aggregate, which products qualify, and whether the administrative "
                    "fee belongs to the GPO or is shared with members. Maintain "
                    "a provisional rebate ledger until eligibility and measurement "
                    "conditions support recognition. Monitor qualified volume against "
                    "the relevant threshold weekly, using actual accepted purchases "
                    "rather than proposals. If volume falls within 10% above a "
                    "critical threshold, forecast both adjacent tiers and stop "
                    "subsidizing customer prices with the higher tier. The fallback "
                    "is a viable unconditional spread, not fictitious member enrollment "
                    "or purchases manufactured solely to cross the bracket."
                ),
                (
                    "The sixth trap is treating an evergreen commission as an "
                    "unconditional annuity. Telarus or Avant arrangements for Zoom "
                    "and other UCaaS services depend on executed supplier and agent "
                    "terms, eligible service charges, attribution, collections, and "
                    "reversal provisions. An illustrative $20,000 monthly eligible "
                    "billing base at a 10% commission rate yields $2,000 monthly "
                    "operator revenue before any upstream split. If the operator "
                    "retains 70% of that commission, retained revenue is $1,400, "
                    "not $2,000 and certainly not $20,000. A cancellation that "
                    "reverses three months of retained commissions creates a $4,200 "
                    "exposure under that assumed clause. Do not substitute this "
                    "example for a distributor's actual recovery schedule. The "
                    "seventh trap is paying sales contractors immediately while "
                    "the operator remains exposed to later chargebacks. Tie "
                    "contractor payouts to collectible receipts and documented "
                    "reversal allocation, with a lawful written recovery mechanism "
                    "rather than arbitrary deductions. Track billed, eligible, "
                    "earned, received, and reversible amounts separately. Investigate "
                    "a commission variance exceeding 2% of expected retained "
                    "receipts or any missing customer identifier before releasing "
                    "the related payout. Where attribution remains disputed, "
                    "stop advancing commissions, preserve correspondence, and "
                    "escalate through the designated master-agent channel "
                    "without attempting duplicate registrations under another identity."
                ),
                (
                    "The eighth trap is charging shared savings against a fabricated "
                    "baseline. Define the comparison basket before negotiation: exact "
                    "SKUs, licensed quantities, service levels, currency, taxes, "
                    "contract term, credits, and implementation charges. With "
                    "comparable annual spend falling from $120,000 to $96,000, "
                    "verified savings are $24,000 and a 30% contingent fee is "
                    "$7,200. If $8,000 of the apparent reduction comes from "
                    "removing seats the customer had already scheduled to cancel, "
                    "incremental negotiated savings are only $16,000 under a "
                    "contract excluding preplanned removals, producing a $4,800 "
                    "fee. The ninth trap is collecting both supplier compensation "
                    "and a customer fee while concealing the overlap or counting "
                    "the same benefit twice. Disclose the compensation structure "
                    "and implement the agreed offset or credit treatment. Keep "
                    "the baseline signed, vendor quotes preserved, realized "
                    "invoices matched, and disputes tied to particular line "
                    "items. If verification covers less than 95% of the claimed "
                    "savings amount, hold the disputed portion instead of "
                    "billing the full forecast. Use a fixed diagnostic fee "
                    "only when separately agreed and actually earned. A "
                    "defensible savings ledger protects both collection and "
                    "renewal trust; an impressive percentage without a stable "
                    "denominator creates a future refund demand."
                ),
            ],
            "table": {
                "caption": "Rebate Waterfalls, Residual Reversals, and Savings Baseline Controls",
                "headers": [
                    "Margin leak hidden inside commercial terms",
                    "Concrete unit economics requiring separate tracking",
                    "Evidence and telemetry for early detection",
                    "Fallback preserving collectible contribution after corrections",
                ],
                "rows": [
                    [
                        "Conditional GPO tier treated as unconditional revenue",
                        "Two percent of eligible purchases produces rebate revenue",
                        "Qualified purchase volume approaches within 10% above threshold",
                        "Price customer offers using the lower sustainable tier",
                    ],
                    [
                        "Excluded products counted toward eligible member purchases",
                        "Removing $150,000 eligible volume reduces rebate by $3,000",
                        "Supplier eligibility report disagrees with member purchase ledger",
                        "Reclassify exclusions and revise the provisional rebate estimate",
                    ],
                    [
                        "Retroactive tier reduction ignored in customer subsidy",
                        "$450,000 at one percent produces only $4,500",
                        "Executed schedule applies lower rates across entire volume",
                        "Remove subsidies dependent on an unearned higher bracket",
                    ],
                    [
                        "Master-agent split omitted from retained residual calculation",
                        "$2,000 upstream commission times 70% retains $1,400",
                        "Expected retained receipts differ from statements beyond 2%",
                        "Freeze related contractor payouts until attribution is reconciled",
                    ],
                    [
                        "Early contractor payout precedes supplier reversal exposure",
                        "Three reversed $1,400 receipts create $4,200 exposure",
                        "Contractor payable exceeds collected receipts after reversal allowance",
                        "Apply agreed payout timing and contractual recovery procedures",
                    ],
                    [
                        "Seat reductions misrepresented as incremental negotiated savings",
                        "$16,000 eligible savings times 30% earns $4,800",
                        "Baseline includes cancellations already approved before the engagement",
                        "Remove preplanned reductions and invoice only eligible savings",
                    ],
                    [
                        "Supplier compensation overlaps an undisclosed customer success fee",
                        "Apply agreed compensation offsets before calculating customer invoice",
                        "Customer agreement lacks explicit treatment of dual compensation",
                        "Resolve fee treatment in writing before issuing invoices",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Veteran Controls That Keep Small Spreads Collectible",
                "body": (
                    "Experienced operators preserve evidence at the moment terms are "
                    "accepted, then reconcile economic rights separately from cash timing."
                ),
                "items": [
                    "Snapshot the distributor quote, partner schedule, and effective date together; a later portal screenshot cannot establish an earlier rebate entitlement.",
                    "Maintain residual cohorts by supplier, customer activation month, agent split, and reversal window so one problematic vintage cannot hide inside aggregate growth.",
                    "Negotiate a signed savings basket before contacting vendors, including preplanned seat reductions and the exact treatment of supplier-funded credits.",
                    "Match every GPO member purchase to its eligibility category and return status before using that purchase to support a higher volume bracket.",
                ],
            },
        },
        {
            "heading": "3. Keep Trigger Intelligence From Becoming Outreach Liability",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The tenth trap is letting trigger speed outrun source quality. "
                    "The mapped play sec_edgar_8k_vendor_trigger_arbitrage uses SEC "
                    "Form D and Form 8-K events to prioritize timely outreach, "
                    "not to prove purchasing intent. Ingest available EDGAR RSS "
                    "and supported JSON sources, retain accession numbers, and "
                    "deduplicate amendments before routing a lead. Form D reports "
                    "exempt offerings; amounts offered, amounts sold, and filing "
                    "dates are different facts, and none establishes unrestricted "
                    "cash available for software procurement. Item 5.02 covers "
                    "specified director and officer events, Item 1.01 material "
                    "definitive agreements, and Item 2.01 completed acquisitions "
                    "or dispositions of assets. Read the filing before assigning "
                    "a renewal hypothesis. For an illustrative 200-event monthly "
                    "queue, a 20% qualification rate produces 40 accounts; a "
                    "10% meeting rate produces four meetings; a 25% close "
                    "rate produces one customer. At $3,000 retained contribution "
                    "before acquisition costs and $800 of research and outreach "
                    "costs, expected cohort contribution is $2,200. If qualification "
                    "falls to 5%, the same downstream rates yield 0.25 expected "
                    "customers and $750 before acquisition costs, producing a "
                    "$50 loss. Faster alerts cannot rescue a negative qualified "
                    "cohort. Pause the segment and revise the event-to-need "
                    "hypothesis rather than increasing message volume."
                ),
                (
                    "The eleventh trap is turning public-data access into aggressive "
                    "scraping. Apply a shared token bucket capped at five requests "
                    "per second across workers, identify the organization in the "
                    "User-Agent, cache immutable filing documents, and honor SEC "
                    "fair-access guidance. Five requests per second is the "
                    "chapter's conservative operating cap, not a promise of "
                    "unrestricted access. On throttling or access-denial responses, "
                    "stop the affected fetches, honor server instructions, and "
                    "use bounded backoff rather than rotating identities or "
                    "addresses. Mirror SEC nightly bulk ZIP archives where "
                    "published for the required dataset, together with published "
                    "indexes for historical lookbacks; do not assume every "
                    "filing type has an equivalent real-time JSON endpoint "
                    "or nightly archive. Separate historical backfills from "
                    "the live queue so neither starves the other. The "
                    "sub-hour objective runs from detected filing availability "
                    "to a reviewed, channel-eligible outreach draft, not "
                    "guaranteed contact before all commercial databases. If "
                    "the live feed fails, process the cached backlog "
                    "and mark source freshness explicitly. DNS, MX, and "
                    "SPF observations provide another weak signal: Microsoft "
                    "mail routing does not establish seat count, license "
                    "edition, reseller identity, or renewal date. Request "
                    "customer-provided subscription evidence before pricing "
                    "a transfer or claiming recoverable savings."
                ),
                (
                    "The twelfth trap is assuming business targeting exempts every "
                    "message from channel rules. The TCPA, 47 U.S.C. 227, "
                    "and implementing FCC rules distinguish technology, message "
                    "type, destination, and consent; a business contact's "
                    "mobile number does not become unrestricted because "
                    "their employer appears in an SEC filing. Artificial "
                    "or prerecorded voice campaigns need a separate "
                    "rules analysis from individually placed live calls. "
                    "The FTC Telemarketing Sales Rule also prohibits "
                    "specified deceptive practices in business-to-business "
                    "telemarketing; verify which additional provisions and "
                    "recordkeeping duties apply to the actual campaign. "
                    "For commercial email, implement accurate routing "
                    "information, nondeceptive subjects, required sender "
                    "identification and postal address, and a working "
                    "opt-out under CAN-SPAM. Honor opt-outs within "
                    "the statutory deadline and synchronize suppression "
                    "across contractors immediately as an operating "
                    "standard. Never pitch an SEC-triggered lead "
                    "as if the SEC recommended the offer. "
                    "Use vendor names to identify genuine services, "
                    "not to imply an unearned partnership. At "
                    "100 contacts costing $8 each, a campaign "
                    "already consumes $800 before complaint handling. "
                    "One supported complaint involving impersonation "
                    "or a suppression failure should pause that "
                    "workflow immediately. The fallback is corrected, "
                    "human-reviewed outreach through an eligible channel, "
                    "not another sending domain or contractor identity."
                ),
            ],
            "table": {
                "caption": "SEC Trigger Qualification and Outreach Failure Detection",
                "headers": [
                    "Acquisition shortcut creating avoidable operating risk",
                    "Required source evidence and attribution discipline",
                    "Suggested threshold triggering immediate operator review",
                    "Specific fallback without bypassing access restrictions",
                ],
                "rows": [
                    [
                        "Form D offering size treated as available budget",
                        "Distinguish amounts offered from amounts already sold",
                        "Any proposal asserts cash availability without customer confirmation",
                        "Replace budget assertions with a verified discovery question",
                    ],
                    [
                        "Officer departure mistaken for confirmed procurement authority",
                        "Read Item 5.02 and verify current decision ownership",
                        "Lead routing relies solely on an outdated executive name",
                        "Contact the verified business function through eligible channels",
                    ],
                    [
                        "Material agreement interpreted as a software renewal event",
                        "Read Item 1.01 agreement description and relevant exhibits",
                        "Renewal claim lacks subscription evidence from the customer",
                        "Offer a scoped spend review without invented deadlines",
                    ],
                    [
                        "Acquisition filing assumed to authorize tenant consolidation",
                        "Review Item 2.01 and confirm customer integration mandate",
                        "Transfer request lacks approval from each affected organization",
                        "Defer migration until authorized ownership and entitlements reconcile",
                    ],
                    [
                        "Historical backfill consumes the live SEC request budget",
                        "Shared token bucket caps total traffic at five requests",
                        "Any throttling response or access denial interrupts fetching",
                        "Back off and use cached published bulk archives",
                    ],
                    [
                        "B2B label used to bypass channel eligibility checks",
                        "Record destination type and applicable consent evidence",
                        "Any suppressed contact receives another commercial outreach attempt",
                        "Pause affected workflow and synchronize every suppression list",
                    ],
                    [
                        "MX discovery presented as confirmed license inventory",
                        "Customer supplied subscription records establish actual purchased quantities",
                        "Quote relies on inferred seats or inferred renewal dates",
                        "Request verified inventory before calculating price or savings",
                    ],
                ],
            },
        },
        {
            "heading": "4. Reconcile Retained Revenue and Trip Circuit-Breakers Early",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The thirteenth trap is celebrating client subscription spend "
                    "as operator revenue. The Formula v2.0 scorecard labels "
                    "its top line gross revenue, but this candidate's "
                    "specified basis is retained spreads, retained residuals, "
                    "GPO administrative rebates, and shared-savings fees, "
                    "excluding pass-through subscription spend. Apply any "
                    "upstream split once at the relevant commission "
                    "or fee layer. For example, $100,000 of "
                    "eligible annual subscriptions at a 10% commission "
                    "and 70% retained_share produces $7,000 of "
                    "operator revenue, not $70,000 or $10,000. "
                    "Do not apply retained_share again to a "
                    "figure already reported net. ASC 606 "
                    "principal-versus-agent analysis depends on control "
                    "of the specified service and contractual "
                    "facts; this operating model does not "
                    "make every reseller arrangement an agency "
                    "transaction. Reconcile the ledger presentation "
                    "with the actual arrangement while preserving "
                    "the scorecard's comparable retained-revenue basis. "
                    "The canonical cases remain $100,000 revenue "
                    "less $68,000 total modeled costs equals "
                    "$32,000 owner profit; $500,000 less $275,000 "
                    "equals $225,000; and $900,000 less $378,000 "
                    "equals $522,000. Those are 32%, 45.0%, "
                    "and 58% margins, respectively. Keep the "
                    "teams at 1 FT plus 3 contractors "
                    "for Conservative and Base, and 2 FT "
                    "plus 4 contractors for Scaled. Neither "
                    "higher billings nor more seats changes "
                    "these canonical outputs."
                ),
                (
                    "The fourteenth trap is treating accounting profit as spendable "
                    "cash while prefunding, reversals, and supplier debits move "
                    "on different clocks. Customer subscription prefunding must "
                    "remain traceable to its service obligations; do not "
                    "use it to mask an unrelated residual shortfall. "
                    "Maintain separate views of recognized retained revenue, "
                    "cash receipts, customer funds supporting future delivery, "
                    "reversible compensation, and remaining supplier commitments. "
                    "For a clearly labeled stress case outside the "
                    "canonical scorecard, a $15,000 clawback plus $20,000 "
                    "of unrecovered supplier exposure reduces Base owner "
                    "profit from $225,000 to $190,000 if both "
                    "losses are incremental and no offsetting recovery "
                    "exists. That stress case does not replace "
                    "the $225,000 canonical result. Build a rolling "
                    "13-week cash forecast using actual settlement "
                    "dates and contractual debit dates, not invoice "
                    "issue dates. Exclude customer funds required "
                    "for future supplier payments when estimating "
                    "freely deployable liquidity. Trigger intervention if "
                    "projected unrestricted cash cannot cover eight "
                    "weeks of unavoidable operating outflows, if "
                    "a supplier debit lacks assigned funding, "
                    "or if a material disputed receipt "
                    "is assumed collectible without supporting evidence. "
                    "Freeze discretionary acquisition spend first; "
                    "then curtail new commitments. Protect existing "
                    "service delivery while pursuing documented "
                    "recoveries, rather than financing old "
                    "defects with new customer deposits."
                ),
                (
                    "Run a daily exception queue and a weekly contribution "
                    "review that join customer, tenant, subscription, supplier "
                    "order, agent registration, invoice, payment, and rebate "
                    "identifiers. Pax8, Ingram, and master-agent exports "
                    "can support reconciliation where available, but "
                    "automation must use supported access and "
                    "documented permissions. Do not give a "
                    "billing script broad tenant administration "
                    "rights merely because both systems "
                    "mention the same customer. Restrict "
                    "credentials, record changes, and alert "
                    "on payout-account edits or unexplained "
                    "partner reassignment. Require complete identifier "
                    "coverage for new orders; investigate "
                    "any orphaned supplier charge before "
                    "the next payment run. Track "
                    "retained contribution by customer cohort "
                    "after acquisition, servicing, reversals, and "
                    "collection costs. A suggested warning "
                    "is a two-percentage-point decline in "
                    "retained margin for two consecutive "
                    "weekly closes, with immediate review "
                    "for any negative-contribution cohort. "
                    "Thresholds are initial operating settings, "
                    "not claims about industry averages. "
                    "The response sequence is containment, "
                    "evidence preservation, supplier or customer "
                    "correction, and controlled resumption after "
                    "a clean reconciliation. Preserve original "
                    "records rather than rewriting history "
                    "to make dashboards agree. A "
                    "small team earns its leverage "
                    "by resolving exceptions early; unattended "
                    "automation simply distributes the same "
                    "contractual mistake across more customers."
                ),
            ],
            "table": {
                "caption": "Retained-Revenue Reconciliation and Capital Protection Dashboard",
                "headers": [
                    "Metric defining actual retained operating economics",
                    "Calculation or evidence required for reconciliation",
                    "Initial intervention threshold set by operator",
                    "Action preserving service and limiting further exposure",
                ],
                "rows": [
                    [
                        "Canonical Conservative retained revenue and owner profit",
                        "$100,000 minus $68,000 costs yields $32,000 profit",
                        "Any presentation counts pass-through subscriptions as operator revenue",
                        "Rebuild the revenue bridge and retain canonical outputs",
                    ],
                    [
                        "Canonical Base retained revenue and owner profit",
                        "$500,000 minus $275,000 costs yields $225,000 profit",
                        "Any retained commission receives its split a second time",
                        "Remove duplicate reductions and reconcile source commission schedules",
                    ],
                    [
                        "Canonical Scaled retained revenue and owner profit",
                        "$900,000 minus $378,000 costs yields $522,000 profit",
                        "Staffing assumption exceeds two employees plus four contractors",
                        "Label expanded staffing separately instead of altering canonical assumptions",
                    ],
                    [
                        "Unrestricted liquidity after customer service funding allocations",
                        "Available cash excludes funds needed for future supplier payments",
                        "Forecast covers less than eight weeks of unavoidable outflows",
                        "Freeze discretionary acquisition and reduce new commitment exposure",
                    ],
                    [
                        "Daily supplier order and customer identifier completeness",
                        "Every new charge joins its authorized customer subscription",
                        "Any orphaned supplier charge remains before payment processing",
                        "Investigate ownership and funding before routine payment release",
                    ],
                    [
                        "Weekly retained margin deterioration across comparable customer cohorts",
                        "Contribution includes servicing costs and attributable realized reversals",
                        "Two percentage points lost across two consecutive weekly closes",
                        "Review pricing eligibility and collections before adding cohort volume",
                    ],
                    [
                        "Payout destination integrity and supported system access",
                        "Approved change records match supplier and master-agent exports",
                        "Any unexplained payout edit or partner attribution reassignment",
                        "Contain affected access and verify changes through established channels",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Capture the contractual obligation",
                    "action": "Record the signed customer order and accepted supplier terms before commitment creation.",
                    "detail": (
                        "Attach tenant and subscription identifiers, effective pricing, "
                        "renewal deadlines, partner rights, and the compensation waterfall."
                    ),
                },
                {
                    "step": 2,
                    "title": "Reconcile funding and eligibility",
                    "action": "Match settled customer funds, supplier obligations, and eligible compensation line by line.",
                    "detail": (
                        "Separate subscription pass-throughs from retained fees and "
                        "identify every conditional rebate, split, and reversible receipt."
                    ),
                },
                {
                    "step": 3,
                    "title": "Contain the exception",
                    "action": "Pause affected new orders or payouts when a defined threshold is breached.",
                    "detail": (
                        "Preserve existing service, retain original evidence, assign an "
                        "owner, and pursue correction through the authorized supplier channel."
                    ),
                },
                {
                    "step": 4,
                    "title": "Resume against verified records",
                    "action": "Reopen the workflow only after corrected terms, funding, and identifiers reconcile.",
                    "detail": (
                        "Document the correction, rerun the contribution calculation, "
                        "and test the automation against the defect before restoring volume."
                    ),
                },
            ],
        },
    ],
    "pull_quote": "A narrow software spread is an asset only when the obligation behind it is funded, authorized, and collectible.",
    "diagram_id": "diag-05",
    "action_checklist": [
        "Build a customer-level NCE exposure ledger showing remaining supplier obligations, settled prefunding, renewal deadlines, and uncovered commitments.",
        "Validate CSP, CPOR, Adobe VIP Marketplace, and master-agent rights against the specific program and executed agreement before promising transfers or compensation.",
        "Reconcile GPO eligibility, residual splits, reversal windows, and shared-savings baselines before releasing contractor payouts or customer invoices.",
        "Implement the SEC trigger queue with accession deduplication, a shared five-request-per-second token bucket, and published bulk-archive lookbacks.",
        "Test channel eligibility, suppression propagation, sender identity, and filing-derived claims before activating executive outreach.",
        "Close the retained-revenue bridge weekly, preserve all three canonical scorecard cases, and run separate liquidity and clawback stress scenarios.",
    ],
    "statutory_citations": [
        {
            "title": "47 U.S.C. 227 — Restrictions on use of telephone equipment",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": (
                "Classify calling technology, destination numbers, message content, "
                "and applicable consent requirements before launching telephone outreach."
            ),
        },
        {
            "title": "47 CFR 64.1200 — Delivery restrictions",
            "url": "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200",
            "relevance": (
                "Implement applicable FCC calling restrictions, do-not-call procedures, "
                "and consent controls for the particular campaign."
            ),
        },
        {
            "title": "16 CFR 310.3 — Deceptive telemarketing acts or practices",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-310/section-310.3",
            "relevance": (
                "Prevent material misrepresentations about affiliation, software savings, "
                "commercial terms, and other covered aspects of telemarketing offers."
            ),
        },
        {
            "title": "16 CFR 310.6 — Exemptions",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-310/section-310.6",
            "relevance": (
                "Evaluate the scope and exceptions of B2B treatment rather than "
                "assuming business-directed calls escape all TSR requirements."
            ),
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for transmission of messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Use accurate commercial-email headers and subjects, required sender "
                "disclosures, a postal address, and functioning opt-out handling."
            ),
        },
        {
            "title": "17 CFR 239.500 — Form D",
            "url": "https://www.ecfr.gov/current/title-17/chapter-II/part-239/section-239.500",
            "relevance": (
                "Identify Form D as the notice filing for specified exempt offerings; "
                "distinguish reported offering facts from verified procurement capacity."
            ),
        },
        {
            "title": "17 CFR 249.308 — Form 8-K",
            "url": "https://www.ecfr.gov/current/title-17/chapter-II/part-249/section-249.308",
            "relevance": (
                "Anchor event-trigger research in the SEC current-report framework "
                "and inspect the actual filing before assigning an outreach hypothesis."
            ),
        },
        {
            "title": "SEC Form 8-K — Items 1.01, 2.01, and 5.02",
            "url": "https://www.sec.gov/files/form8-k.pdf",
            "relevance": (
                "Read the item-specific reporting requirements for material definitive "
                "agreements, completed asset transactions, and specified leadership events."
            ),
        },
    ],
}
