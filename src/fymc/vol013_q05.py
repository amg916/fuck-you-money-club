from __future__ import annotations

CHAPTER_5 = {
    "id": "Q5",
    "chapter_id": "Q5",
    "chapter_number": 5,
    "question_number": 5,
    "slug": "beginner-traps-clawbacks-asymmetric-failure-modes",
    "question_prompt": "What kills 80% of newcomers in intellectual property licensing, and what forensic metrics detect margin leaks, regulatory landmines, or platform bans before they wipe out capital?",
    "kicker": "Q5 / THE BIG MONEY PLAYBOOKS",
    "title": "Beginner Traps, Clawbacks & Asymmetric Failure Modes",
    "subtitle": "Patent Title, Brand Quality Control, Catalog Takedowns, Dataset Provenance, and Royalty Clawback Circuit-Breakers",
    "layout_template": "expert_insights",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #19, Intellectual Property Licensing, ranks #09 with a 88/100 "
        "Money-to-Manpower Score. Its four mapped operator plays are patent licensing, "
        "brand licensing, catalog licensing, and dataset licensing. Each converts controlled "
        "rights into license fees and royalties, not ownership of the licensee's sales. "
        "The canonical annual owner profit cases are $12,500 Conservative, $180,625 Base, "
        "and $480,000 Scaled. This chapter turns title defects, royalty leakage, minimum "
        "guarantee misunderstandings, infringement disputes, and platform enforcement into "
        "observable stop conditions. The one-full-time, three-contractor pod must reject "
        "unverifiable rights before selling them and reconcile earned royalties before "
        "distributing cash. The question's 80% framing is not an established failure "
        "statistic; the actionable evidence is contract-level exposure, missing documentation, "
        "collection aging, and unresolved usage exceptions."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$50,000",
            "context": "Annual license fees and royalties; excludes licensees' product sales",
            "note": "25% net margin; $12,500 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$425,000",
            "context": "Annual license fees and royalties; excludes licensees' product sales",
            "note": "42.5% net margin; $180,625 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$800,000",
            "context": "Annual license fees and royalties; excludes licensees' product sales",
            "note": "60% net margin; $480,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Reject Rights You Cannot Trace, Bound, and Deliver",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with four rights lanes: patent claims, brand identifiers, catalog "
                    "works, and dataset permissions. They share a contract workflow but not "
                    "a common ownership test. The patent lane requires an assignment chain, "
                    "current legal status, territorial coverage, and a claim-to-product "
                    "analysis; a patent license does not establish freedom to operate "
                    "against other owners. Under 35 U.S.C. 261, assignment documentation "
                    "and timely recording matter, but a USPTO Assignment Center entry "
                    "does not independently prove the transferor owned everything conveyed. "
                    "For catalog assets, 17 U.S.C. 204 generally requires a signed writing "
                    "for a copyright ownership transfer. Purchasing source files or paying "
                    "a freelancer does not automatically convey copyright. Brand licenses "
                    "need an enforceable quality-control program, not merely logo delivery. "
                    "Dataset access requires permission for the actual collection, processing, "
                    "redistribution, and proposed downstream use; public availability alone "
                    "does not supply those permissions. These are four separate beginner "
                    "traps with one circuit-breaker: no delivery until the rights register "
                    "links each licensed asset to evidence, scope, owner, and exceptions. "
                    "The full-time principal owns that register; the rights contractor "
                    "assembles evidence, and specialist counsel resolves defects rather "
                    "than allowing sales urgency to substitute for title."
                ),
                (
                    "Scope defects often cost more than missing signatures because they "
                    "surface after distribution. A music catalog can contain separate "
                    "composition, master-recording, performer, and artwork interests. A "
                    "synchronization grant for one recording does not clear every layer. "
                    "A photograph license can still leave publicity or location restrictions "
                    "unresolved. A dataset may include contributor terms allowing analytics "
                    "but excluding model training, resale, or reidentification. A patent "
                    "portfolio may cover one jurisdiction while the licensee manufactures "
                    "and sells elsewhere. Encode media, territory, field, term, sublicensing, "
                    "and modification rights as separate fields in Airtable or a controlled "
                    "spreadsheet, then attach the executed grant rather than a salesperson's "
                    "summary. Treat every unsupported combination as blocked inventory. "
                    "A second trap is promising exclusive rights while retaining existing "
                    "nonexclusive customers or lacking an upstream exclusivity grant. "
                    "A third is overlooking liens, prior grants, or termination rights "
                    "that survive an acquisition. Search relevant UCC records and examine "
                    "the security documents; the effect of a lien depends on the asset "
                    "and applicable perfection rules. Count unresolved exceptions by "
                    "licensed asset, not by contract, because one defective track or "
                    "training-data slice can contaminate a large delivery."
                ),
                (
                    "Build an evidence packet before negotiating a minimum guarantee. "
                    "For patents, include signed assignments, prosecution and maintenance "
                    "status, remaining term, and counsel's documented scope analysis. "
                    "For brands, include registration status, approved specimens, product "
                    "standards, sampling frequency, and corrective-action rights. For "
                    "catalogs, preserve contributor agreements, cue-sheet identifiers, "
                    "territorial splits, and restrictions on automated rights enforcement. "
                    "For datasets, retain source terms, collection dates, permitted purposes, "
                    "deletion duties, and a manifest identifying the delivered version. "
                    "Hash files with SHA-256 so later disputes concern a reproducible "
                    "delivery rather than an ambiguous folder. One missing signature "
                    "affecting a material right stops that asset's release; it need not "
                    "stop unrelated assets with complete evidence. Allocate the three "
                    "contractors to specialist counsel, rights operations, and royalty "
                    "accounting, with scoped assignments and recorded hours. The principal "
                    "remains accountable for acceptance and commercial decisions. This "
                    "one-full-time, three-contractor pod cannot investigate an unlimited "
                    "catalog cheaply: cap active diligence work to available review hours "
                    "and price exceptions separately. The $12,000–$75,000 startup range "
                    "is capital capacity, not permission to buy doubtful rights before "
                    "a qualified licensee confirms demand, budget, and intended use."
                ),
            ],
            "table": {
                "caption": "Four-Play Rights Defects and Asset-Level Release Evidence",
                "headers": [
                    "Failure pattern and affected operator play",
                    "Evidence required before promising licensed scope",
                    "Early warning requiring an immediate intervention",
                    "Named pod owner and concrete circuit-breaker",
                ],
                "rows": [
                    [
                        "Patent licensing inherits an incomplete inventor assignment chain",
                        "Signed assignments connect every relevant owner and covered patent",
                        "Any missing conveyance affects a claim being commercially offered",
                        "Specialist counsel blocks affected claims until the chain closes",
                    ],
                    [
                        "Brand licensing substitutes logo files for actual quality control",
                        "Written standards accompany inspection rights and documented corrective actions",
                        "A scheduled product sample remains unreviewed before commercial shipment",
                        "Rights contractor escalates defects and principal suspends new approvals",
                    ],
                    [
                        "Catalog licensing clears recordings but overlooks underlying composition interests",
                        "Separate grants establish required recording and composition permissions explicitly",
                        "One delivered work lacks a required rights-layer evidence link",
                        "Rights contractor removes that work from the delivery manifest",
                    ],
                    [
                        "Dataset licensing treats publicly accessible records as unrestricted inventory",
                        "Source terms and collection evidence support each proposed downstream use",
                        "A requested training use conflicts with recorded source restrictions",
                        "Specialist counsel narrows permitted uses before any dataset delivery",
                    ],
                    [
                        "Exclusive licensing ignores earlier grants covering overlapping commercial uses",
                        "Prior agreements establish territory, field, duration, and surviving exceptions",
                        "Two active grants promise incompatible rights for identical uses",
                        "Principal withdraws exclusivity language until the overlap is resolved",
                    ],
                    [
                        "Acquired rights arrive with unexamined security interests or restrictions",
                        "Relevant lien searches and underlying documents establish transfer constraints",
                        "A creditor claim or upstream restriction remains materially unresolved",
                        "Specialist counsel requires documented resolution before acquisition funds move",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Pre-Flight Checks Before Rights Leave the Pod",
                "body": (
                    "Apply these checks to the specific asset, licensed use, and delivery "
                    "version. A signed commercial agreement does not repair an upstream defect."
                ),
                "items": [
                    "Trace ownership through executed source documents; resolve missing signatures and material prior grants before releasing the affected asset.",
                    "Match territory, field, media, sublicensing, and modification permissions against the licensee's written deployment plan.",
                    "For brand deals, approve the first production sample and record recurring inspection duties with a named reviewer.",
                    "For datasets and catalogs, freeze a versioned manifest, record source restrictions, and confirm the removal procedure works before delivery.",
                ],
            },
        },
        {
            "heading": "2. Reconcile Royalties Before Minimum Guarantees Become Illusions",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The canonical cases measure operator revenue, not licensee product "
                    "sales: Conservative produces $50,000 revenue and $12,500 owner profit "
                    "at 25%; Base produces $425,000 and $180,625 at 42.5%; Scaled "
                    "produces $800,000 and $480,000 at 60%. Corresponding total expense "
                    "envelopes are $37,500, $244,375, and $320,000. Conservative and Base "
                    "use one full-time operator plus three contractors; Scaled uses two "
                    "full-time operators plus four contractors. As illustrative bridges, "
                    "$1,000,000 of eligible sales at 5% yields $50,000 royalties; "
                    "$10,000,000 at 4% plus $25,000 of separately earned license fees "
                    "yields $425,000; $16,000,000 at 5% yields $800,000. Those sales "
                    "bases belong to licensees and are not additional operator revenue. "
                    "They are arithmetic examples, not evidence that customers exist. "
                    "The $2,000–$12,000 monthly operating range is a planning input, "
                    "not a substitute for each scenario's complete annual expense envelope. "
                    "Reconcile contractor work, acquisition charges, audit costs, collection "
                    "losses, and other applicable expenses without double counting. A "
                    "6–24 month first-deal cycle makes prepaid acquisition commitments "
                    "especially dangerous: a profitable annual model can still run out "
                    "of cash before the first enforceable royalty becomes collectible."
                ),
                (
                    "Minimum guarantees create two distinct traps: double-counted revenue "
                    "and uncapped recoupment. Suppose a licensee pays a $60,000 "
                    "recoupable advance against royalties for the same contract period. "
                    "If earned royalties total $80,000, the incremental payment is "
                    "$20,000, not another $80,000. If earned royalties total $45,000 "
                    "and the contract establishes an unconditional $60,000 minimum, "
                    "the contractual floor remains $60,000, subject to the agreement's "
                    "actual refund, breach, and termination provisions. Cash receipt, "
                    "contractual entitlement, and recognized revenue require separate "
                    "ledger fields; the accountant determines recognition from the "
                    "performance obligations and applicable accounting basis. Do not "
                    "automatically book an advance as fully earned on receipt. Another "
                    "trap is letting a licensee recoup marketing, distribution, returns, "
                    "and development costs across every property indefinitely. Specify "
                    "which costs qualify, evidence requirements, period limits, and "
                    "whether recoupment is restricted to one property. Separate any "
                    "upstream minimum the operator owes the rights owner from downstream "
                    "minimums customers owe the operator. A cancellation downstream "
                    "does not automatically cancel an upstream payment. Maintain a "
                    "rolling thirteen-week cash forecast that stresses delayed collections "
                    "and still includes every binding upstream commitment."
                ),
                (
                    "Royalty leakage hides in definitions rather than headline rates. "
                    "Define gross billings, eligible deductions, bundled allocations, "
                    "affiliate transfers, currency conversion dates, returns, and reporting "
                    "cutoffs before signing. A 5% royalty on $1,000,000 of eligible "
                    "sales is $50,000; an unsupported $100,000 deduction removes "
                    "$5,000, or 40% of Conservative owner profit if unrecovered and "
                    "other costs stay unchanged. Require transaction-level schedules "
                    "that reconcile to source systems such as Shopify, Amazon settlement "
                    "reports, Stripe, or NetSuite, using only contractually authorized "
                    "exports and minimum necessary customer fields. Settlement cash alone "
                    "does not equal the royalty base because fees, reserves, refunds, "
                    "and settlement timing distort it. Set internal review triggers "
                    "at an unexplained variance above 1% of reported royalty or "
                    "$500, whichever is lower, and at any unsupported deduction "
                    "category. These are operating choices, not statutory thresholds. "
                    "The accounting contractor investigates exceptions; the principal "
                    "issues a timely contractual notice and preserves audit rights. "
                    "Specify record retention, sampling access, audit frequency, and "
                    "who pays when an agreed underpayment threshold is exceeded. "
                    "Without enforceable access to underlying records, automated royalty "
                    "reporting merely accelerates acceptance of an unverified number."
                ),
            ],
            "table": {
                "caption": "Royalty Waterfall, Clawback, and Cash-Exposure Controls",
                "headers": [
                    "Hidden economic defect in the licensing agreement",
                    "Required calculation or source record supporting review",
                    "Internal trigger demanding a documented operator response",
                    "Correction owned by the lean operating pod",
                ],
                "rows": [
                    [
                        "Recoupable advance gets counted again when royalties are earned",
                        "Maintain separate advance balances and period-level earned royalty schedules",
                        "Cash plus accrual postings exceed the same contractual entitlement",
                        "Accounting contractor corrects the ledger before owner distributions occur",
                    ],
                    [
                        "Cross-property recoupment consumes income from otherwise profitable licensed assets",
                        "Track eligible costs and recoupment balances separately by property",
                        "One property's deficit reduces another property's contractually protected royalties",
                        "Principal disputes the offset using the executed recoupment schedule",
                    ],
                    [
                        "Refund reserves grow without transaction evidence or release deadlines",
                        "Match reserve movements to returns and agreed contractual aging",
                        "A reserve exceeds its contractual cap or release date",
                        "Accounting contractor requests supporting records and calculates the balance due",
                    ],
                    [
                        "Affiliate transfers depress the base before external retail sales",
                        "Apply the agreement's affiliate valuation and downstream reporting provisions",
                        "Transfer pricing changes materially without supporting contractual valuation evidence",
                        "Principal invokes reporting rights and renegotiates unsupported future structures",
                    ],
                    [
                        "Currency conversion silently shifts value between reporting and settlement",
                        "Recompute amounts using the specified rate source and date",
                        "Any conversion method differs from the executed royalty schedule",
                        "Accounting contractor documents the difference and requests corrected reporting",
                    ],
                    [
                        "Upstream minimum survives a downstream termination or collection failure",
                        "Forecast binding upstream payments against collectible downstream cash receipts",
                        "Thirteen-week forecast falls below committed payments and essential expenses",
                        "Principal freezes discretionary acquisitions and negotiates payment timing promptly",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four Moves That Protect Collectible Royalty Value",
                "body": (
                    "Preserve evidence and negotiating leverage before revenue is booked. "
                    "These tactics support all four plays without adding another full-time role."
                ),
                "items": [
                    "Attach a worked royalty example to the agreement covering a return, bundle, affiliate sale, and currency conversion.",
                    "Negotiate a small test statement before full launch so the licensee proves their export can support the actual royalty definition.",
                    "Keep upstream and downstream minimums on different schedules; model termination on either side without assuming an automatic offset.",
                    "Calendar audit notice deadlines and record-retention expirations alongside renewals; a valuable claim can become impractical when source records disappear.",
                ],
            },
        },
        {
            "heading": "3. Stop Enforcement Shortcuts Before Platforms and Counterparties Act",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Platform access is a revocable distribution channel, not proof "
                    "of intellectual-property ownership. Beginners create asymmetric exposure "
                    "by registering shared catalog assets as exclusive references in "
                    "YouTube Content ID, filing automated complaints against authorized "
                    "licensees, or submitting trademark reports without checking territorial "
                    "rights. YouTube reference eligibility generally requires exclusive "
                    "rights in the relevant territories; stock material and overlapping "
                    "grants can make a reference unsuitable. Check the current platform "
                    "rules before submission because eligibility and enforcement procedures "
                    "change. Under 17 U.S.C. 512(f), knowing material misrepresentations "
                    "in copyright notices or counter-notices can create liability. "
                    "That provision is not a universal penalty for every mistaken "
                    "claim, but it makes fabricated authority especially costly. "
                    "Maintain an allowlist of authorized channels and reconcile it "
                    "before any enforcement batch. One substantiated ownership conflict "
                    "pauses the affected reference and associated claims pending review. "
                    "Do not evade a suspension through replacement identities or "
                    "recycled accounts; preserve notices, correct the underlying defect, "
                    "and use the platform's appeal process. An account-wide restriction "
                    "can strand unrelated legitimate assets, so separate rights evidence "
                    "from platform dashboards and keep distribution contracts accessible "
                    "outside the service."
                ),
                (
                    "The dataset shortcut is removing attribution or source restrictions "
                    "and presenting the resulting compilation as clean proprietary "
                    "inventory. Dataset rights can involve copyright, contract, privacy, "
                    "trade-secret, and sector-specific obligations; ownership of an "
                    "arrangement does not necessarily confer ownership of every record. "
                    "For covered California businesses, Civil Code section 1798.100 "
                    "sets collection and use requirements, including reasonably necessary "
                    "and proportionate processing within the statutory framework. "
                    "Determine whether the transaction is a sale, sharing, or a "
                    "service-provider arrangement under applicable definitions rather "
                    "than relying on a contract label. Keep deletion propagation "
                    "and permitted-use restrictions technically enforceable through "
                    "versioned deliveries and downstream notices. For catalogs, stripping "
                    "copyright management information can implicate 17 U.S.C. 1202 "
                    "when its statutory conditions are met; removing metadata is "
                    "not a reliable way to remove rights obligations. For brands, "
                    "counterfeit provenance, fabricated endorsements, and misleading "
                    "affiliation claims can trigger platform action and claims under "
                    "15 U.S.C. 1125(a). The rights contractor samples delivered "
                    "assets against original manifests monthly. Any newly identified "
                    "restricted source quarantines the affected version while counsel "
                    "determines correction, notification, and replacement duties. Do "
                    "not keep selling during that investigation."
                ),
                (
                    "Contract leverage also has limits outside platform rules. Patent "
                    "licenses need term-aware payment schedules: under Kimble v. Marvel "
                    "Entertainment, collecting royalties for post-expiration use of an "
                    "expired patent remains impermissible under the rule the Court "
                    "retained, while deferred payment for pre-expiration use and "
                    "genuinely distinct nonpatent rights require separate analysis. "
                    "Have counsel distinguish payment timing from the licensed conduct "
                    "rather than copying a perpetual royalty clause. Competition "
                    "review should examine tying, coordinated pricing, market allocation, "
                    "and restrictions among competitors under 15 U.S.C. 1; a "
                    "field-of-use limitation is not automatically unlawful, and "
                    "ownership does not excuse anticompetitive coordination. Another "
                    "trap is promising uninterrupted rights after an upstream "
                    "licensor enters bankruptcy. Section 365(n) can protect certain "
                    "intellectual-property licensees after rejection, but the statutory "
                    "definition does not include trademarks, whose treatment requires "
                    "separate analysis. Preserve executed licenses, payment history, "
                    "source-access provisions, and rights elections before a distress "
                    "event. The principal should map each deal's maximum contractual "
                    "refund, defense obligation, and indemnity exposure. Uncapped "
                    "promises against uncertain title can erase several years of "
                    "Base profit; an attractive royalty rate cannot compensate for "
                    "an obligation the pod cannot investigate or fund."
                ),
            ],
            "table": {
                "caption": "Enforcement Shortcuts, Primary Authorities, and Containment Actions",
                "headers": [
                    "Shortcut creating disproportionate legal or platform exposure",
                    "Authority or platform mechanism requiring precise factual review",
                    "Observable event requiring immediate containment of affected activity",
                    "Evidence-preserving response assigned to the operating pod",
                ],
                "rows": [
                    [
                        "Shared catalog references are represented as exclusively controlled recordings",
                        "YouTube Content ID eligibility depends on applicable exclusive rights",
                        "A supported ownership conflict appears against an active reference",
                        "Rights contractor pauses affected claims and verifies territorial exclusivity",
                    ],
                    [
                        "Automated copyright complaints target customers holding valid existing licenses",
                        "17 U.S.C. 512(f) addresses knowing material notice misrepresentations",
                        "One verified license conflicts with an issued infringement complaint",
                        "Principal stops the batch and counsel coordinates appropriate corrections",
                    ],
                    [
                        "Dataset resale ignores original collection purposes and downstream restrictions",
                        "California Civil Code 1798.100 governs covered collection and processing",
                        "Requested deployment exceeds documented purposes or applicable source permissions",
                        "Rights contractor quarantines that version pending a lawful resolution",
                    ],
                    [
                        "Catalog metadata is stripped to conceal original ownership information",
                        "17 U.S.C. 1202 addresses specified copyright management information misconduct",
                        "Delivery comparisons reveal unexplained removal of protected ownership information",
                        "Specialist counsel evaluates exposure while operations preserve original files",
                    ],
                    [
                        "Patent royalties continue unchanged after the licensed patent expires",
                        "Kimble retains the restriction on royalties for post-expiration use",
                        "Billing schedule includes use periods beyond the relevant expiration",
                        "Specialist counsel separates valid accrued payments from prohibited charges",
                    ],
                    [
                        "Competing licensees use the operator to coordinate market pricing",
                        "15 U.S.C. 1 governs agreements restraining trade among parties",
                        "A negotiation requests competitors' future prices or allocation commitments",
                        "Principal stops that discussion and seeks specialist competition review",
                    ],
                ],
            },
        },
        {
            "heading": "4. Run a Weekly Exception System That Fits Four People",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Create one weekly exception board with asset, contract, counterparty, "
                    "amount exposed, evidence link, deadline, and accountable owner. "
                    "Use Airtable for rights and obligations, QuickBooks or NetSuite "
                    "for the ledger, and a restricted document repository for "
                    "executed agreements. Automate royalty-report reminders, renewal "
                    "alerts, and obligation tracking, but never let an integration "
                    "change licensed scope or submit infringement notices without "
                    "human review. Trigger a reminder five business days before "
                    "each contractual report deadline; escalate any missed deadline "
                    "on the next business day. Escalate receivables fifteen days "
                    "past their contractual due date and calculate concentration "
                    "using collectible revenue, not impressive licensee sales. "
                    "Flag a counterparty exceeding 35% of trailing twelve-month "
                    "operator revenue for a collection-delay stress test. Flag any "
                    "uncured quality-control failure, missing material title document, "
                    "or unauthorized dataset use immediately regardless of dollars. "
                    "These thresholds are internal starting rules, not universal "
                    "industry norms. The principal reviews the board weekly; each "
                    "contractor receives only their assigned evidence and access. "
                    "Limit the dashboard to decisions the pod can actually execute, "
                    "because fifty unattended alerts are less useful than five "
                    "exceptions with documented deadlines and remedies."
                ),
                (
                    "Separate a warning from an available contractual remedy. A "
                    "late royalty report may justify a notice but not immediate "
                    "termination, deletion of customer systems, or public accusations. "
                    "Read cure periods, service requirements, dispute procedures, "
                    "and survival language before acting. The first response is "
                    "evidence preservation: save the executed agreement, delivery "
                    "manifest, royalty statement, source export, correspondence, and "
                    "calculation version. The accounting contractor quantifies the "
                    "undisputed amount and disputed difference; counsel identifies "
                    "the permitted remedy; the principal sends the required notice. "
                    "Pause new discretionary grants while respecting existing "
                    "performance duties. If an upstream rights defect affects a "
                    "delivered catalog or dataset, trace every downstream recipient "
                    "and version rather than broadcasting an inaccurate blanket "
                    "recall. For brand defects, require documented corrective samples "
                    "and apply agreed suspension provisions where available. For "
                    "patent disputes, preserve claim analyses and avoid escalating "
                    "a collection disagreement into an unsupported infringement "
                    "threat. Recovery metrics should distinguish invoiced corrections, "
                    "accepted corrections, and cash collected. A $20,000 adjustment "
                    "is not recovered value until its payment and ledger treatment "
                    "are resolved. Close the incident only after the originating "
                    "process changes and the next report confirms the fix."
                ),
                (
                    "Protect the scorecard with explicit downside bridges instead "
                    "of silently rewriting its assumptions. In the Base case, "
                    "a $25,000 unrecovered leakage event reduces $180,625 owner "
                    "profit to $155,625 if every other expense stays fixed. "
                    "A separate $40,000 dispute expense reduces it to $140,625; "
                    "both together reduce it to $115,625. These are stress "
                    "illustrations, not replacement canonical cases. Likewise, a "
                    "$5,000 unrecovered deduction consumes 40% of the $12,500 "
                    "Conservative profit. Require a twelve-month cash stress view "
                    "before accepting an upstream minimum, using the actual "
                    "acquisition schedule, essential expenses, and delayed collections. "
                    "Route added asset volume to contractors only after estimating "
                    "review hours and pricing the resulting cost inside the "
                    "scenario expense envelope. Move to the Scaled two-full-time, "
                    "four-contractor configuration when recurring collections and "
                    "workload support it, not because the royalty dashboard "
                    "shows large licensee sales. Across all four plays, reject "
                    "deals whose maximum plausible refund or defense exposure "
                    "exceeds available liquidity without a credible contractual "
                    "or insurance solution. Verify exclusions, deductibles, and "
                    "claim conditions rather than assuming coverage. The operating "
                    "objective is collectible, defensible rights income with bounded "
                    "obligations, not the largest signed headline guarantee."
                ),
            ],
            "table": {
                "caption": "Weekly Forensic Telemetry and Contract-Aware Circuit-Breakers",
                "headers": [
                    "Metric tied to a specific licensing failure",
                    "Starting internal threshold for principal-level exception review",
                    "Evidence source maintained by the four-person pod",
                    "Response that preserves rights and limits exposure",
                ],
                "rows": [
                    [
                        "Royalty statement variance against the independently reconstructed contractual base",
                        "Unexplained difference exceeds one percent or five hundred dollars",
                        "Accounting contractor retains source exports and a reproducible calculation",
                        "Principal requests correction and calendars the applicable audit deadline",
                    ],
                    [
                        "Reporting delay measured against the executed contractual submission deadline",
                        "Any report remains missing on the next business day",
                        "Rights contractor maintains contract dates and documented reminder history",
                        "Principal sends the required notice without inventing termination rights",
                    ],
                    [
                        "Collection aging measured from the actual contractual payment date",
                        "An undisputed receivable becomes fifteen days past its due date",
                        "Accounting contractor reconciles invoices, receipts, disputes, and payment terms",
                        "Principal updates the cash forecast and begins contractual escalation",
                    ],
                    [
                        "Counterparty concentration measured using trailing operator revenue rather than sales",
                        "One counterparty contributes more than thirty-five percent of revenue",
                        "Accounting contractor produces a counterparty-level twelve-month revenue bridge",
                        "Principal stress-tests delayed collections before accepting additional upstream commitments",
                    ],
                    [
                        "Material rights evidence completeness for assets awaiting commercial delivery",
                        "Any required title or permitted-use document remains materially unresolved",
                        "Rights contractor links each asset to executed evidence documents",
                        "Principal withholds affected delivery while counsel resolves the defect",
                    ],
                    [
                        "Available cash compared with binding payments and essential operating expenses",
                        "Thirteen-week forecast shows any uncovered binding obligation or essential expense",
                        "Principal combines bank balances with dated commitments and collection estimates",
                        "Principal stops discretionary acquisitions and pursues timely contractual payment adjustments",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the incident evidence",
                    "action": "Save the exact contract, asset version, report, and source export.",
                    "detail": (
                        "The rights contractor records timestamps and SHA-256 hashes; "
                        "the accounting contractor preserves the original royalty calculation."
                    ),
                },
                {
                    "step": 2,
                    "title": "Quantify the bounded exposure",
                    "action": "Separate unpaid entitlement, refundable cash, and prospective dispute expense.",
                    "detail": (
                        "The principal updates the thirteen-week cash forecast without "
                        "counting disputed corrections as collected receipts."
                    ),
                },
                {
                    "step": 3,
                    "title": "Apply the actual contractual remedy",
                    "action": "Have counsel identify notice, cure, audit, and suspension provisions.",
                    "detail": (
                        "Send the required notice through the agreed channel and pause "
                        "only activity the contract or applicable rights permit pausing."
                    ),
                },
                {
                    "step": 4,
                    "title": "Verify recovery and eliminate recurrence",
                    "action": "Reconcile payment, corrected reports, and the next affected delivery.",
                    "detail": (
                        "Close the exception after evidence confirms the repair; update "
                        "the rights register, reporting rule, or delivery control responsible."
                    ),
                },
            ],
        },
    ],
    "pull_quote": "A royalty is only as valuable as the rights you can prove, the base you can audit, and the cash you can keep.",
    "diagram_id": "diag-05",
    "action_checklist": [
        "Build separate patent, brand, catalog, and dataset rights lanes with asset-level ownership evidence and explicit permitted-use fields.",
        "Reconcile the $50,000, $425,000, and $800,000 canonical revenue cases to their exact profit and expense envelopes without including licensee sales.",
        "Attach worked royalty waterfalls and distinct upstream and downstream minimum schedules to every proposed deal.",
        "Assign specialist counsel, rights operations, and royalty accounting to the three contractor seats, with the full-time principal accountable for exceptions.",
        "Configure report deadlines, renewal alerts, audit expirations, collection aging, and material rights defects on one weekly exception board.",
        "Run a cash-delay and dispute-cost stress test before accepting exclusivity, uncapped obligations, or a binding upstream minimum.",
    ],
    "statutory_citations": [
        {
            "title": "35 U.S.C. 261 — Ownership and assignment",
            "url": "https://www.law.cornell.edu/uscode/text/35/261",
            "relevance": (
                "Supports written patent assignment diligence and analysis of recording "
                "priority; a database entry alone does not settle every ownership question."
            ),
        },
        {
            "title": "17 U.S.C. 204 — Execution of transfers of copyright ownership",
            "url": "https://www.law.cornell.edu/uscode/text/17/204",
            "relevance": (
                "Generally requires a signed writing for copyright ownership transfers, "
                "including exclusive grants, subject to the statutory exception."
            ),
        },
        {
            "title": "15 U.S.C. 1127 — Trademark definitions, related companies, and abandonment",
            "url": "https://www.law.cornell.edu/uscode/text/15/1127",
            "relevance": (
                "Provides statutory context for controlled trademark use and abandonment "
                "analysis supporting documented brand quality-control procedures."
            ),
        },
        {
            "title": "17 U.S.C. 512(f) — Material misrepresentations in copyright notices",
            "url": "https://www.law.cornell.edu/uscode/text/17/512",
            "relevance": (
                "Addresses knowing material misrepresentations in covered notices and "
                "counter-notices, making evidence review essential before enforcement."
            ),
        },
        {
            "title": "17 U.S.C. 1202 — Integrity of copyright management information",
            "url": "https://www.law.cornell.edu/uscode/text/17/1202",
            "relevance": (
                "Defines prohibited conduct involving copyright management information "
                "with specified knowledge and intent requirements."
            ),
        },
        {
            "title": "15 U.S.C. 1125(a) — False designations and misleading representations",
            "url": "https://www.law.cornell.edu/uscode/text/15/1125",
            "relevance": (
                "Addresses specified misleading origin, affiliation, sponsorship, and "
                "commercial representations relevant to brand licensing."
            ),
        },
        {
            "title": "15 U.S.C. 1 — Agreements in restraint of trade",
            "url": "https://www.law.cornell.edu/uscode/text/15/1",
            "relevance": (
                "Requires competition-law analysis of licensing arrangements involving "
                "competitor coordination, pricing restraints, or market allocation."
            ),
        },
        {
            "title": "11 U.S.C. 365(n) and 101(35A) — Intellectual-property licenses in bankruptcy",
            "url": "https://www.law.cornell.edu/uscode/text/11/365",
            "relevance": (
                "Provides certain licensee elections after rejection of covered licenses; "
                "the cross-referenced definition excludes trademarks."
            ),
        },
        {
            "title": "California Civil Code 1798.100 — Collection and use of personal information",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1798.100.&lawCode=CIV",
            "relevance": (
                "Establishes collection and processing requirements for covered businesses, "
                "including purpose and proportionality requirements relevant to datasets."
            ),
        },
        {
            "title": "Kimble v. Marvel Entertainment, LLC, 576 U.S. 446 (2015)",
            "url": "https://www.supremecourt.gov/opinions/14pdf/13-720_jiel.pdf",
            "relevance": (
                "Retains the rule against royalties for post-expiration patent use "
                "while explaining distinctions involving deferred payments and other rights."
            ),
        },
    ],
}
