from __future__ import annotations

CHAPTER_4 = {
    "id": "Q4",
    "chapter_id": "Q4",
    "chapter_number": 4,
    "question_number": 4,
    "slug": "startup-capital-lean-infrastructure-pre-flight-stack",
    "question_prompt": "How do you allocate startup capital ($50,000–$250,000 USD) and configure a lean, low-opex ($6,000–$30,000 USD/mo) production stack without wasting cash on bloated overhead?",
    "kicker": "Q4 / THE BIG MONEY PLAYBOOKS",
    "title": "Startup Capital, Lean Infrastructure & Pre-Flight Stack",
    "subtitle": "Reserve-First Carrier Payments, FMCSA Security, Highway/RMIS Screening, and a Twelve-Layer Dispatch Stack",
    "layout_template": "comparison_table",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #12, Freight Brokerage, ranks #25 with a 62/100 Money-to-Manpower "
        "Score because carrier payments arrive before many shipper collections. "
        "Allocate at least half of startup capital to accessible freight float, "
        "separate statutory security from operating cash, and purchase software only "
        "against a documented control requirement. This chapter organizes eight mapped "
        "plays: the supplied FMCSA/DOT trigger funnel plus seven chapter-local operating "
        "plays covering reserve allocation, payment terms, security procurement, lean "
        "infrastructure, carrier identity, invoice evidence, and launch rehearsal. "
        "Canonical annual owner profits remain $30,000 Conservative, $165,000 Base, "
        "and $400,000 Scaled, on gross shipper billings rather than brokerage spread. "
        "The production design combines bounded credit exposure, independent carrier "
        "verification, twelve infrastructure layers, and explicit stop conditions "
        "before the first truck moves."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$1,000,000",
            "context": "Annual gross shipper billings including carrier costs",
            "note": "3% net margin; $30,000 annual owner net profit; 3 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$3,000,000",
            "context": "Annual gross shipper billings including carrier costs",
            "note": "5.5% net margin; $165,000 annual owner net profit; 3 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$5,000,000",
            "context": "Annual gross shipper billings including carrier costs",
            "note": "8% net margin; $400,000 annual owner net profit; 4 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Allocate Capital Around the Carrier Payment Clock",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Start with the Reserve-First Capital Allocation play: divide startup "
                    "cash into unrestricted carrier float, security procurement, formation "
                    "and insurance, production systems, launch labor, and incident cash. "
                    "The budgets below allocate $30,000 of $50,000 and $150,000 of "
                    "$250,000 to float, preserving 60% in both cases. These are spending "
                    "envelopes, not promises that every applicant can obtain a bond "
                    "within the allowance. A BMC-84 surety bond has a $75,000 penal "
                    "sum; its premium and any collateral depend on underwriting. A "
                    "BMC-85 trust ties up qualifying assets and cannot simultaneously "
                    "serve as unrestricted carrier-payment cash. At $50,000, a fully "
                    "funded $75,000 trust is outside the budget before operations even "
                    "begin. Obtain written security terms before committing payroll or "
                    "annual software contracts. If the surety demands substantial "
                    "collateral, increase capitalization, reduce initial exposure, or "
                    "delay launch rather than relabel restricted money as reserve. "
                    "Keep the incident allocation separate from float because a "
                    "deductible and a shipper default can occur together. The startup "
                    "range also assumes a staged launch: a small initial desk cannot "
                    "support the canonical full team indefinitely without collections "
                    "or additional capital. Model the entire two-to-six-month sales "
                    "ramp before hiring against hoped-for freight."
                ),
                (
                    "The Payment-Term Compression play converts sales promises into "
                    "fundable loads. Estimate required float as monthly carrier "
                    "purchases multiplied by the positive collection-payment gap, "
                    "divided by thirty, then add concentration and dispute cushions. "
                    "For an illustrative Base desk, $250,000 monthly shipper billings "
                    "and an 82% carrier-cost ratio produce $205,000 monthly carrier "
                    "purchases. Collecting in forty-five days while paying in twenty "
                    "requires approximately $170,833 before any cushion. That exceeds "
                    "even the $150,000 reserve in the larger startup budget. Collecting "
                    "in thirty days and paying in twenty-one reduces the estimate to "
                    "$61,500; adding $30,000 for exceptions yields $91,500. These are "
                    "planning approximations: build a daily invoice-level cash forecast "
                    "because weekly payment batches and concentrated customers create "
                    "larger troughs than averages suggest. A $15,000 shipper deposit "
                    "covers ten $1,500 carrier commitments only if the deposit is "
                    "available and those obligations have no other funding claim. "
                    "For a slow-paying customer, offer prepaid pilot loads, negotiate "
                    "shorter terms, or decline additional tenders. Factoring is a "
                    "priced funding option, not improved freight economics; examine "
                    "recourse, reserves, minimum charges, assignment notices, and "
                    "termination fees before counting proceeds. Never finance one "
                    "customer's overdue balance by silently delaying another "
                    "carrier's agreed payment."
                ),
                (
                    "Reconcile the scorecard before declaring the infrastructure lean. "
                    "Conservative gross shipper billings of $1,000,000 at 3% produce "
                    "$30,000 annual owner net profit; Base billings of $3,000,000 at "
                    "5.5% produce $165,000; Scaled billings of $5,000,000 at 8% produce "
                    "$400,000. One illustrative bridge uses carrier purchases of "
                    "$850,000, $2,460,000, and $4,000,000 respectively. The resulting "
                    "spreads are $150,000, $540,000, and $1,000,000, leaving total "
                    "other operating costs of $120,000, $375,000, and $600,000. These "
                    "bridge assumptions explain the canonical results without "
                    "claiming the scorecard supplied carrier percentages. Monthly "
                    "fixed overhead of $6,000, $15,000, and $30,000 would leave "
                    "another $4,000, $16,250, and $20,000 monthly for commissions, "
                    "variable labor, funding charges, claims allowances, and other "
                    "costs. Therefore, the stated overhead band is not a cap on all "
                    "expenses. Conservative and Base staffing remain 3 FT + 2 C; "
                    "Scaled remains 4 FT + 3 C. Price actual wages, payroll taxes, "
                    "benefits, and contractor scopes before accepting the bridge "
                    "as feasible. The leanest case is particularly demanding. "
                    "Maintain separate reporting for shipper billings, carrier "
                    "purchases, brokerage spread, and owner profit; determine "
                    "principal-versus-agent accounting presentation from the actual "
                    "contracts rather than treating customer freight value as margin."
                ),
            ],
            "table": {
                "caption": "Six Capital Envelopes Preserve Sixty Percent as Accessible Freight Float",
                "headers": [
                    "Capital envelope and operating purpose",
                    "$50,000 startup allocation",
                    "$250,000 startup allocation",
                    "Release condition and cash protection",
                ],
                "rows": [
                    [
                        "Unrestricted carrier float held outside routine spending",
                        "$30,000 reserved exclusively for documented carrier payment obligations",
                        "$150,000 reserved exclusively for documented carrier payment obligations",
                        "Release against accepted freight obligations and daily cash forecasting",
                    ],
                    [
                        "Surety premium and security procurement spending allowance",
                        "$5,000 allowance subject to actual surety underwriting terms",
                        "$20,000 allowance subject to actual surety underwriting terms",
                        "Rebudget any collateral requirement before accepting shipper tenders",
                    ],
                    [
                        "Entity formation, contracts, and insurance binding expenses",
                        "$3,000 reserved for scoped setup and insurance deposits",
                        "$10,000 reserved for scoped setup and insurance deposits",
                        "Bind required coverage before assuming contractual freight exposure",
                    ],
                    [
                        "Production software setup and initial subscription runway",
                        "$2,000 reserved for necessary activation and short commitments",
                        "$10,000 reserved for necessary activation and short commitments",
                        "Activate seats only after assigning owners and acceptance tests",
                    ],
                    [
                        "Launch labor and customer acquisition runway allocation",
                        "$8,000 supports a tightly staged initial operating desk",
                        "$50,000 supports a longer measured customer acquisition runway",
                        "Expand payroll only against funded demand and collection evidence",
                    ],
                    [
                        "Incident cash outside the ordinary carrier float",
                        "$2,000 cushions small exceptions without pretending full loss coverage",
                        "$10,000 cushions exceptions while preserving ordinary payment capacity",
                        "Escalate losses exceeding this envelope before booking more freight",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the Money That Keeps Carriers Answering",
                "body": "Treat liquidity as a dispatch constraint, not a month-end accounting observation.",
                "items": [
                    "Maintain separate bank subaccounts for carrier float and overhead; reconcile both to a single controlled general ledger.",
                    "Negotiate pilot-load deposits before offering volume discounts; a cheaper rate does not repair a forty-five-day collection cycle.",
                    "Ask the surety for premium, collateral, indemnity, cancellation, and renewal terms in writing before buying annual software.",
                    "Measure customer days-to-cash from invoice eligibility, not dispatch date; missing delivery evidence can consume the entire apparent margin cushion.",
                ],
            },
        },
        {
            "heading": "2. Build Twelve Layers Without Buying Twelve Enterprise Contracts",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The Lean Infrastructure Procurement play starts with a single "
                    "load identifier shared across dispatch, carrier onboarding, "
                    "tracking, billing, and bank reconciliation. Select a "
                    "transportation management system only after testing that "
                    "identifier through a complete shipment. The matrix names "
                    "twelve production layers and precise purchasing assumptions. "
                    "Dollar figures are illustrative internal monthly budget caps, "
                    "not verified vendor tariffs; named tiers identify the intended "
                    "scope, and quote-based products require written pricing. This "
                    "distinction prevents an outdated public price from becoming "
                    "a procurement commitment. Three core users at a $15-per-user "
                    "planning allowance consume $45 monthly, while a $250 TMS cap "
                    "and $150 load-board cap consume another $400. The twelve "
                    "listed caps total $1,150 monthly before taxes, transaction "
                    "charges, and implementation. That leaves $4,850 within a "
                    "$6,000 fixed-overhead envelope, but does not establish that "
                    "the full canonical team fits. Begin with monthly subscriptions "
                    "and an export test; prepay annually only after measured usage "
                    "and an acceptable cancellation position. For every overlapping "
                    "feature, nominate one system of record. Paying both a TMS and "
                    "an accounting tool to generate uncontrolled invoice numbers "
                    "creates reconciliation work rather than automation. Reject "
                    "bundles whose savings depend on seats the desk cannot use."
                ),
                (
                    "Automate evidence movement before automating freight decisions. "
                    "A TMS webhook can open a shipment folder, queue a tracking "
                    "request, and prepare an invoice checklist without granting "
                    "software authority to approve a new payee. Use Google "
                    "Workspace shared drives or Microsoft 365 team storage rather "
                    "than a dispatcher's personal mailbox as the record archive. "
                    "Keep application administrators separate from daily dispatch "
                    "roles, require multifactor authentication, and store integration "
                    "secrets in a managed password vault. A $15 monthly vault "
                    "allowance is trivial compared with one misdirected $2,000 "
                    "carrier payment. Configure tracking to collect shipment-relevant "
                    "positions only for the agreed movement; stop access when "
                    "delivery closes. Establish an exception queue for missing "
                    "pickup confirmation, stale location data, changed appointment "
                    "times, and unreturned proof of delivery. Assign each exception "
                    "an owner and deadline instead of sending every alert to "
                    "everyone. Test exports of loads, documents, invoices, and "
                    "carrier records before entering an annual contract. If a "
                    "vendor becomes unavailable, the desk should still retrieve "
                    "pickup numbers, contact verified carriers, document delivery, "
                    "and produce an invoice using its own retained records. "
                    "A manual continuity sheet is useful only when updated "
                    "from the actual production load register."
                ),
                (
                    "The Invoice Evidence Capture play protects both cash conversion "
                    "and dispute resolution. At tender acceptance, record the shipper "
                    "purchase-order requirement, billing address, appointment rules, "
                    "accessorial authorization method, and proof-of-delivery standard. "
                    "At delivery, collect legible paperwork and reconcile seal, "
                    "quantity, exception, and appointment information before sending "
                    "the invoice. Ten invoices at $2,000 each delayed seven days "
                    "lock up $20,000 in receivables for that additional week; at "
                    "an illustrative 18% annual funding rate, the direct carrying "
                    "cost is about $69, excluding collection labor and lost capacity. "
                    "Preventing the delay matters more than saving a few dollars "
                    "on document storage. The Carrier Identity Verification play "
                    "then connects the payment record to the onboarded legal "
                    "carrier, rather than trusting a familiar display name. "
                    "Highway or RMIS can organize identity and insurance evidence, "
                    "but neither replaces independent callbacks or a documented "
                    "response to conflicting information. Set automation to flag "
                    "changes in bank details, contact domains, insurance status, "
                    "and dispatch authority. When a signal cannot be resolved, "
                    "pause the affected tender or payment and use a previously "
                    "verified contact channel. Cheap alternatives are acceptable "
                    "when they preserve evidence and accountability; they are "
                    "not acceptable when they simply remove the control."
                ),
            ],
            "table": {
                "caption": "Twelve-Layer Vendor Stack: Named Tiers, Internal Budget Caps, and Lean Substitutes",
                "headers": [
                    "Production layer and named vendor tier",
                    "Exact planning cap and purchasing basis",
                    "Required operating role and acceptance evidence",
                    "Cheaper lean alternative with explicit limitation",
                ],
                "rows": [
                    [
                        "Business identity using Google Workspace Business Starter",
                        "$45 monthly cap for three users; verify current tariff",
                        "Shared company communications with controlled access and retained records",
                        "Microsoft 365 Business Basic if its written quote is lower",
                    ],
                    [
                        "Credential control using Bitwarden Teams organization subscription",
                        "$15 monthly cap for three users; verify current tariff",
                        "Shared secrets with individual accounts and immediate staff offboarding",
                        "KeePassXC encrypted vault requires disciplined sharing and recovery procedures",
                    ],
                    [
                        "Load execution using AscendTMS quoted paid operating tier",
                        "$250 monthly cap; obtain exact tier and implementation quote",
                        "Unique load records, rate confirmations, milestones, and exportable history",
                        "Controlled spreadsheet register only while manual checks remain reliable",
                    ],
                    [
                        "Spot capacity sourcing using DAT One Standard subscription",
                        "$150 monthly cap for one seat; verify current tariff",
                        "Lane discovery and capacity contacts without substituting for onboarding",
                        "Direct carrier roster reduces subscription spending but narrows coverage",
                    ],
                    [
                        "Carrier screening using Highway broker onboarding quoted package",
                        "$200 monthly cap; written quote determines package and affordability",
                        "Identity evidence and exception handling before first carrier dispatch",
                        "Quote RMIS or document manual checks with lower load limits",
                    ],
                    [
                        "Shipment visibility using Trucker Tools quoted broker tracking",
                        "$100 monthly cap; confirm usage charges and integration scope",
                        "Shipment-specific tracking with stale-location alerts and delivery closure",
                        "Scheduled driver check calls require consent and dispatcher availability",
                    ],
                    [
                        "General ledger using QuickBooks Online Simple Start subscription",
                        "$50 monthly cap; verify current tariff and user limitations",
                        "Reconcile invoices, carrier liabilities, funding charges, and bank activity",
                        "GnuCash supports bookkeeping but requires more manual document linking",
                    ],
                    [
                        "Banking and ACH using Relay business account offering",
                        "$25 monthly service cap; transaction fees require separate confirmation",
                        "Separate cash buckets with payment permissions and bank reconciliation",
                        "Existing insured business bank works if controls meet requirements",
                    ],
                    [
                        "Agreement signatures using Dropbox Sign Essentials subscription",
                        "$25 monthly cap for one sender; verify current tariff",
                        "Executed agreements linked to carrier and shipper legal identities",
                        "Signed PDFs with verified counterparties require manual evidence retention",
                    ],
                    [
                        "Customer pipeline using HubSpot CRM free tools tier",
                        "$0 software subscription cap within documented free-tier feature limits",
                        "Track qualified shippers, credit status, next actions, and concentration",
                        "Shared spreadsheet works with named owners and version history",
                    ],
                    [
                        "Company calling using Zoom Phone US and Canada Unlimited",
                        "$60 monthly cap for three users; confirm taxes separately",
                        "Stable business numbers, coverage routing, and retrievable call metadata",
                        "One dedicated business line limits concurrent dispatch conversations",
                    ],
                    [
                        "Recovery copies using Backblaze B2 pay-as-you-go object storage",
                        "$130 monthly combined cap for storage and scoped integration",
                        "Independent exports with tested restoration and restricted deletion access",
                        "Encrypted offline exports cost less but require daily ownership",
                    ],
                ],
            },
        },
        {
            "heading": "3. Separate Authority, Identity, and Trigger-Based Acquisition",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The Authority and Security Procurement play begins with matching "
                    "legal names across the entity record, IRS employer identification "
                    "number, FMCSA application, bank account, shipper agreement, "
                    "carrier agreement, and surety filing. Obtain the EIN directly "
                    "from the IRS, document signing authority, and keep personal "
                    "transactions outside business accounts. Confirm active broker "
                    "authority, process-agent designation, and required security "
                    "before arranging transportation subject to federal broker "
                    "registration. Under 49 U.S.C. 13904 and 13906, registration "
                    "and financial security are substantive operating requirements, "
                    "not website badges. Distinguish the BMC-84 premium from its "
                    "$75,000 coverage amount and review the current BMC-85 asset "
                    "and trustee requirements in 49 CFR 387.307. Purchase insurance "
                    "against the actual contractual exposure: contingent cargo, "
                    "errors and omissions, general liability, and cyber coverage "
                    "have different triggers and exclusions. A carrier cargo "
                    "certificate is evidence to investigate, not proof that every "
                    "commodity, theft method, or unattended vehicle loss is covered. "
                    "Obtain confirmation from the insurer or authorized producer "
                    "through an independently sourced channel. If a shipper demands "
                    "coverage the business does not hold, revise the contract or "
                    "bind the coverage before accepting freight. Do not fund "
                    "insurance deposits by borrowing silently from committed "
                    "carrier-payment cash."
                ),
                (
                    "Implement fmcsa_dot_inspection_trigger_arbitrage as the supplied "
                    "TRACK_1 acquisition play, with accurate timing and transparent "
                    "branding. Its intended signals are new MC/DOT activity and "
                    "recent hours-of-service or maintenance findings. However, a "
                    "universal mandatory twenty-one-day insurance-filing window is "
                    "not the correct operating premise: the twenty-one-day interval "
                    "generally concerns the published authority application's protest "
                    "period. A new USDOT number, pending application, and granted "
                    "operating authority are different events. Ingest permitted "
                    "FMCSA Census and Licensing & Insurance data daily where "
                    "available, recording source publication dates and status "
                    "transitions. Poll for SMS releases, but do not represent SMS "
                    "as a universal daily violation feed; public SMS data are "
                    "generally refreshed monthly, and access to detailed inspection "
                    "information varies. Contact operators about visible, relevant "
                    "issues without claiming federal affiliation or privileged "
                    "knowledge. For example, 200 screened records yielding twenty "
                    "qualified responses and four $250 documentation engagements "
                    "produce $1,000 of separate service receipts. At twelve "
                    "research hours valued at $30 and $100 distribution cost, "
                    "$540 remains before delivery expenses. Those receipts are "
                    "neither freight billings nor assumed scorecard upside. If "
                    "freshness or access is inadequate, use transparent private "
                    "compliance-agency branding, free BOC-3/MCS-150 status checks, "
                    "and inbound hand-raiser forms instead of manufacturing urgency."
                ),
                (
                    "Keep the trigger funnel separate from carrier acceptance. A "
                    "fleet with a fresh maintenance citation may be a prospect "
                    "for an administrative service while remaining unsuitable for "
                    "a particular load. Do not imply that buying assistance "
                    "improves access to brokerage freight or erases enforcement "
                    "history. Screen authority, insurance, relevant safety evidence, "
                    "equipment suitability, and the actual dispatch relationship "
                    "on their own merits. Independent callbacks should use a "
                    "previously verified number, especially when someone changes "
                    "the carrier's bank account or requests payment to another "
                    "entity. Require documented shipper authorization and contract "
                    "structure before using a co-broker; ordinary motor-carrier "
                    "authority does not establish brokerage authority. For an "
                    "illustrative $2,400 load with a $2,000 carrier commitment, "
                    "the $400 gross spread cannot justify a plausible $2,000 "
                    "diversion loss. A thirty-minute verification costing $20 "
                    "of staff time consumes 5% of spread but protects the "
                    "whole payable and customer relationship. If identity remains "
                    "unresolved, substitute a verified carrier or decline the "
                    "movement. Commercial email must meet 15 U.S.C. 7704 "
                    "requirements, including accurate identification and functioning "
                    "opt-outs. Evaluate telephone and text outreach separately "
                    "under applicable calling rules; a public federal record "
                    "does not itself provide permission for every contact method."
                ),
            ],
            "table": {
                "caption": "Authority and Fraud Evidence Matrix Before a Shipment Becomes a Payable",
                "headers": [
                    "Control surface and primary evidence",
                    "Required verification action before commercial reliance",
                    "Failure signal requiring immediate operational response",
                    "Fallback preserving service without accepting unresolved exposure",
                ],
                "rows": [
                    [
                        "Entity identity across registration, tax, and banking records",
                        "Match exact legal names and documented authorized signers",
                        "Payment beneficiary differs from the contracted legal entity",
                        "Obtain independently verified assignment documentation before releasing funds",
                    ],
                    [
                        "Broker authority shown through FMCSA registration status",
                        "Confirm active status rather than relying on application receipt",
                        "Website claims authority while official status remains pending",
                        "Delay regulated brokerage activity until registration becomes effective",
                    ],
                    [
                        "BMC-84 or BMC-85 filing and underlying security terms",
                        "Confirm current filing plus premium, collateral, and renewal obligations",
                        "Restricted collateral has been counted as accessible operating float",
                        "Recapitalize or shrink exposure before accepting additional tenders",
                    ],
                    [
                        "Carrier insurance evidence and commodity-specific coverage requirements",
                        "Verify applicable coverage through an independently sourced producer contact",
                        "Certificate and policy information conflict about covered cargo",
                        "Use another verified carrier meeting the actual shipment requirements",
                    ],
                    [
                        "Authority transition and inspection trigger acquisition records",
                        "Store publication dates and distinguish applications from granted authority",
                        "Marketing message depends on unsupported filing deadlines or affiliation",
                        "Use clearly branded inbound status checks without artificial urgency",
                    ],
                    [
                        "Carrier dispatch authority and requested payment beneficiary",
                        "Confirm changes through established contacts outside the initiating message",
                        "Urgent bank change arrives alongside unfamiliar dispatch contact details",
                        "Suspend affected payment while verifying the legitimate contractual payee",
                    ],
                ],
            },
        },
        {
            "heading": "4. Rehearse the First Load, Then Release Capacity Gradually",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The Launch Rehearsal and Exception Drill play turns configuration "
                    "into an observable production test. Build one synthetic load "
                    "with a $2,400 shipper charge and $2,000 carrier payable; mark "
                    "it clearly as a test so nobody issues a real tender or "
                    "payment. Move it through credit review, carrier verification, "
                    "rate confirmation, pickup, tracking, delivery evidence, invoice "
                    "creation, and reconciliation. Confirm that the $400 spread "
                    "appears once and that neither the bank transfer nor the "
                    "carrier invoice becomes a second revenue entry. Inject a "
                    "bank-change request, an unreadable delivery document, a stale "
                    "tracking event, and a disputed detention charge. Each "
                    "exception must have a named owner, evidence requirements, "
                    "and a documented release decision. Test after-hours coverage "
                    "with the person actually assigned to answer, not the "
                    "founder assuming permanent availability. Restore the load "
                    "packet from an independent export and time the recovery. "
                    "A desk that can only recover by contacting a departed "
                    "employee has not passed. Finish by checking the daily "
                    "cash forecast against the intended carrier payment date "
                    "and the customer's actual invoice-acceptance rules. The "
                    "exercise should produce a retained evidence packet, not "
                    "a verbal assurance that the software appears to work."
                ),
                (
                    "Release credit and capacity in measured increments. A "
                    "$30,000 unrestricted reserve with a $10,000 liquidity "
                    "cushion supports no more than $20,000 of otherwise "
                    "unfunded carrier commitments under this simple exposure "
                    "rule. At $2,000 per load, that is ten loads, not "
                    "twenty merely because the shipper promises repeat volume. "
                    "Deduct other due obligations and anticipated deductions "
                    "before using this ceiling; released customer payments "
                    "replenish capacity only when available to spend. Set "
                    "customer limits using all outstanding exposure, including "
                    "delivered but unbilled freight and accepted tenders. "
                    "Concentration matters because ten loads for one debtor "
                    "are not ten independent credit risks. Review aging "
                    "daily during the pilot and immediately stop additional "
                    "unsecured commitments when an agreed threshold is "
                    "breached. Use cleared deposits, shorter payment terms, "
                    "or a properly reviewed funding facility to reopen "
                    "capacity. Never confuse an undrawn line with cash "
                    "unless the borrowing conditions are satisfied. Measure "
                    "automation by exception minutes per load and clean "
                    "invoice turnaround, not the number of integrations "
                    "installed. If forty monthly shipments each save fifteen "
                    "minutes, ten recovered hours valued at $30 justify "
                    "at most $300 of monthly labor savings before "
                    "maintenance and error costs."
                ),
                (
                    "Maintain a weekly owner dashboard joining cash, service, "
                    "and control evidence. Include unrestricted float, restricted "
                    "security assets, next fourteen days of carrier maturities, "
                    "customer aging, unbilled deliveries, disputed accessorials, "
                    "claims reserves, and identity exceptions. Display gross "
                    "shipper billings separately from brokerage spread and "
                    "owner profit so a large booked load cannot hide "
                    "deteriorating collections. Review vendor invoices against "
                    "actual seats and transactions; cancel duplicate tracking "
                    "or document features only after proving the remaining "
                    "system retains the necessary record. Broker transaction "
                    "records under 49 CFR 371.3 generally require three "
                    "years of retention and must support the specified "
                    "transaction information and review rights. Retain longer "
                    "where contracts, claims, tax obligations, or preservation "
                    "duties require it. Document each material change in "
                    "banking, security, insurance, carrier onboarding, and "
                    "customer terms, then rerun the relevant rehearsal "
                    "step. This closes the eight-play operating map: "
                    "reserve allocation, payment terms, authority and "
                    "security, infrastructure procurement, carrier identity, "
                    "invoice evidence, trigger acquisition, and launch "
                    "rehearsal. Seven are chapter-local operating labels; "
                    "only the trigger identifier was supplied as a "
                    "catalog play. Expand toward the canonical team "
                    "and revenue cases only when observed collection "
                    "behavior and tested staffing capacity support the "
                    "next block of carrier commitments."
                ),
            ],
            "table": {
                "caption": "Pre-Flight Evidence and Bounded Production Release Decisions",
                "headers": [
                    "Production readiness test and operating owner",
                    "Evidence required before the first live tender",
                    "Concrete release criterion tied to actual exposure",
                    "Failure response that preserves cash and records",
                ],
                "rows": [
                    [
                        "Founder verifies authority, security, and process-agent readiness",
                        "Official active registration and current required filings retained",
                        "Legal entity and operating records match across all documents",
                        "Postpone regulated brokerage activity until every discrepancy is resolved",
                    ],
                    [
                        "Treasury owner proves available float and payment permissions",
                        "Daily forecast separates unrestricted balances from all restricted assets",
                        "Next carrier commitments fit reserves after the liquidity cushion",
                        "Reduce tender capacity or obtain cleared customer deposits first",
                    ],
                    [
                        "Carrier owner tests onboarding and independent identity verification",
                        "Verified contact, authority, coverage, equipment, and beneficiary evidence retained",
                        "Every material conflict has a documented resolution before dispatch",
                        "Substitute a verified carrier or decline the affected shipment",
                    ],
                    [
                        "Billing owner rehearses invoice eligibility and document retrieval",
                        "Complete test packet contains required delivery and accessorial evidence",
                        "Invoice reconciles to agreed charges without duplicate revenue entries",
                        "Repair the document workflow before granting additional customer credit",
                    ],
                    [
                        "Dispatch owner exercises tracking and after-hours incident response",
                        "Assigned responder successfully handles delayed pickup and stale tracking",
                        "Customer updates and carrier contacts remain available during outage",
                        "Reduce operating hours or secure qualified coverage before launch",
                    ],
                    [
                        "System owner restores shipment evidence from independent exports",
                        "Recovered records include rates, contacts, documents, invoices, and timestamps",
                        "Restored packet supports operations without the unavailable primary application",
                        "Repair exports and access controls before increasing shipment volume",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Conditions Before the First Live Shipment",
                "body": "Retain the evidence for each condition and assign one accountable owner.",
                "items": [
                    "Verify effective broker registration, process-agent filing, and $75,000 security; an application receipt does not establish active authority.",
                    "Prove the first shipment's carrier payment fits unrestricted cash after existing obligations and the documented liquidity cushion.",
                    "Complete independent carrier identity, coverage, equipment, and beneficiary checks; resolve conflicting dispatch or bank instructions before release.",
                    "Pass the synthetic shipment, invoice, outage, and exception drills with named daytime and after-hours responders.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the funded operating envelope",
                    "action": "Approve startup allocations and a daily thirteen-week cash forecast.",
                    "detail": "Separate accessible float, restricted security, fixed overhead, and incident cash; attach actual surety and insurance terms.",
                },
                {
                    "step": 2,
                    "title": "Configure the minimum connected stack",
                    "action": "Assign one owner, identifier, and record location to each production layer.",
                    "detail": "Obtain written vendor pricing, limit seats, enable multifactor authentication, and test exports before annual commitments.",
                },
                {
                    "step": 3,
                    "title": "Execute the complete shipment rehearsal",
                    "action": "Run the synthetic load through dispatch, exceptions, invoicing, and reconciliation.",
                    "detail": "Retain results for changed payee details, missing delivery evidence, tracking outage, recovery, and customer credit exhaustion.",
                },
                {
                    "step": 4,
                    "title": "Release a bounded live pilot",
                    "action": "Accept only shipments inside verified carrier capacity and funded customer limits.",
                    "detail": "Review aging, unbilled deliveries, reserve coverage, and exception minutes daily before increasing tenders or staffing.",
                },
            ],
        },
    ],
    "pull_quote": "Buy the controls that protect carrier cash before buying the software that makes the desk look large.",
    "diagram_id": "diag-07",
    "action_checklist": [
        "Allocate at least 50% of startup capital to accessible carrier float, excluding surety collateral and trust assets.",
        "Obtain written BMC-84 or BMC-85 terms and verify effective broker authority, process-agent filing, and insurance scope.",
        "Build a daily thirteen-week forecast using actual shipper collection dates, carrier maturities, and concentration cushions.",
        "Quote the twelve stack layers, cap seats and commitments, and prove load-level exports before production use.",
        "Configure the FMCSA trigger play with source timestamps, accurate authority stages, transparent branding, and inbound fallback.",
        "Pass the four pre-flight conditions, retain the synthetic shipment evidence, and launch within documented cash and credit limits.",
    ],
    "statutory_citations": [
        {
            "title": "49 U.S.C. 13904 — Registration of brokers",
            "url": "https://www.law.cornell.edu/uscode/text/49/13904",
            "relevance": "Establishes federal broker registration requirements relevant to activating the operating desk.",
        },
        {
            "title": "49 U.S.C. 13906(b) — Broker financial security",
            "url": "https://www.law.cornell.edu/uscode/text/49/13906",
            "relevance": "Provides the statutory framework for the $75,000 broker security requirement and related security protections.",
        },
        {
            "title": "49 CFR 387.307 — Property broker surety bond or trust fund",
            "url": "https://www.ecfr.gov/current/title-49/section-387.307",
            "relevance": "Controls required broker security, including current trust and surety requirements that must be distinguished from unrestricted float.",
        },
        {
            "title": "49 CFR 366.4 — Designation of process agents",
            "url": "https://www.ecfr.gov/current/title-49/section-366.4",
            "relevance": "Supports verification of the process-agent designation required for applicable registered operations.",
        },
        {
            "title": "49 CFR 371.3 — Records to be kept by brokers",
            "url": "https://www.ecfr.gov/current/title-49/section-371.3",
            "relevance": "Specifies broker transaction records, the three-year retention period, and transaction review rights.",
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Governs commercial email identification, message practices, opt-out mechanisms, and processing of opt-out requests.",
        },
        {
            "title": "47 CFR 64.1200 — Restrictions on telephone solicitation",
            "url": "https://www.ecfr.gov/current/title-47/section-64.1200",
            "relevance": "Requires separate evaluation of calling and texting methods rather than treating public fleet records as permission for outreach.",
        },
    ],
}
