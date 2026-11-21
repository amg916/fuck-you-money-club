from __future__ import annotations

CHAPTER_3 = {
    "id": "Q3",
    "chapter_id": "Q3",
    "chapter_number": 3,
    "question_number": 3,
    "slug": "unit-economics-margin-waterfall-working-capital-float",
    "question_prompt": "What are the real unit economics, gross-to-net margin deductions, scrub/reversal reserves, and working-capital float requirements for intellectual property licensing?",
    "kicker": "Q3 / THE BIG MONEY PLAYBOOKS",
    "title": "Unit Economics, Margin Waterfall & Working-Capital Float",
    "subtitle": "Patent, Brand, Catalog and Dataset Royalties: Recoupable Minimums, Audit Reserves, CBP Valuation and Collection Float",
    "layout_template": "financial_breakdown",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #19, Intellectual Property Licensing, ranks #13 with a 79/100 "
        "Money-to-Manpower Score. Its four operating plays here are patent "
        "field-of-use licensing, territorial brand licensing, catalog-and-dataset "
        "licensing, and customs_first_sale_rule_valuation_arbitrage. The first "
        "three are chapter-local operating mappings; the fourth is the supplied "
        "customs adjacency, monetized only through genuine licensed deliverables. "
        "Conservative, Base, and Scaled annual owner profits reconcile to "
        "$12,500, $180,625, and $480,000 on recognized revenue of $50,000, "
        "$425,000, and $800,000. This chapter separates licensee sales from "
        "operator revenue, decomposes deductions and contractor costs, and prices "
        "the cash delay between delivery and unrestricted collection. Minimum "
        "guarantees, royalty audits, title verification, and controlled reserves "
        "determine whether attractive paper margins become distributable cash."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$50,000",
            "context": "Annual license fees and royalties; excludes licensee product sales",
            "note": "25% net margin; $12,500 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$425,000",
            "context": "Annual license fees and royalties; excludes licensee product sales",
            "note": "42.5% net margin; $180,625 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$800,000",
            "context": "Annual license fees and royalties; excludes licensee product sales",
            "note": "60% net margin; $480,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Define the Revenue Unit Before Pricing the Rights",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Use one active licensee agreement for one measured year as the "
                    "economic unit, with separate schedules for territories, permitted "
                    "uses, reporting periods, and collection dates. The illustrative "
                    "Conservative cohort contains two agreements generating $25,000 "
                    "each after deductions; Base contains ten generating $42,500 "
                    "each; Scaled contains sixteen generating $50,000 each. Those "
                    "cohorts reproduce the canonical revenue totals without treating "
                    "licensees' merchandise sales as operator revenue. Base starts "
                    "with $8 million of eligible licensee sales at a five percent "
                    "royalty, producing $400,000 of royalty billings, plus $50,000 "
                    "of separately earned fixed license fees. Contract credits of "
                    "$15,000 and an expected reversal allowance of $10,000 reduce "
                    "$450,000 of billings to $425,000 of recognized revenue. A "
                    "$200,000 recoupable minimum already credited against those "
                    "royalties is a collection mechanism, not another revenue line. "
                    "Advance cash remains deferred where the associated performance "
                    "has not occurred. Maintain separate fields in PostgreSQL or "
                    "Airtable for underlying sales, billings, earned consideration, "
                    "receivables, and cash. A dashboard that collapses these fields "
                    "can show growth while quietly spending money owed for future "
                    "delivery. Require a contract identifier on every adjustment so "
                    "the audit trail survives staff changes and spreadsheet exports."
                ),
                (
                    "Map the first three operating plays to rights packages with "
                    "different delivery burdens rather than applying one royalty "
                    "percentage everywhere. Patent field-of-use licensing can price "
                    "100,000 qualifying units at $0.20 each plus a separately "
                    "earned $10,000 implementation license, yielding $30,000 before "
                    "deductions; invalidity allegations or disputed claim coverage "
                    "trigger a narrow evaluation license instead of an expensive "
                    "exclusive grant. Territorial brand licensing can combine a "
                    "$20,000 annual minimum with four percent of $750,000 in "
                    "eligible sales: total royalty consideration is $30,000, not "
                    "$50,000, when the minimum is fully recoupable. Its fallback "
                    "is a shorter, nonexclusive territory with documented product "
                    "quality inspections. Catalog-and-dataset licensing can sell "
                    "four permitted-use packages at $7,500 each, also yielding "
                    "$30,000, while charging separately for additional refreshes "
                    "only when the contract permits them. If provenance is "
                    "incomplete, remove affected assets and reprice the remaining "
                    "package rather than promising unrestricted downstream rights. "
                    "These are chapter-local pricing examples, not extra scorecard "
                    "revenue. Copyright transfers require the signed writing "
                    "specified by 17 U.S.C. 204; patent assignments follow "
                    "35 U.S.C. 261. Dataset ownership does not automatically "
                    "supply privacy permissions or rights in every embedded work."
                ),
                (
                    "Treat customs_first_sale_rule_valuation_arbitrage as an adjacent "
                    "licensing opportunity only when the operator actually licenses "
                    "a valuation workflow, evidence taxonomy, or controlled software "
                    "package. Under 19 CFR 152.103 and the Nissho Iwai framework, "
                    "an eligible factory sale must be substantiated as a bona fide "
                    "sale for export to the United States at an acceptable "
                    "transaction value; a lower invoice alone proves nothing. "
                    "At an illustrative ten percent duty rate, moving an eligible "
                    "unit's valuation from $18 to $8 reduces duty from $1.80 "
                    "to $0.80, a $1 saving. That is 55.56 percent on eligible "
                    "units before valuation additions, not an automatic portfolio "
                    "saving. Eligibility covering 63 to 99 percent of otherwise "
                    "comparable import value produces approximately 35 to 55 "
                    "percent aggregate reduction under these assumptions. At "
                    "$10 million of importer-invoice value and 90 percent "
                    "eligibility, modeled annual duty savings are $500,000. A "
                    "$25,000 annual workflow license captures five percent of "
                    "that benefit; only the fee enters operator revenue. For "
                    "$250 million programs, validate entry-level evidence rather "
                    "than extrapolating eligibility. The fallback is encrypted "
                    "factory invoices in confidential customs-broker escrow with "
                    "full CBP access, backed by a formal customs-counsel opinion "
                    "letter; unsupported entries retain the defensible valuation."
                ),
            ],
            "table": {
                "caption": "Rights-Package Pricing and Customs-Adjacency Revenue Boundaries",
                "headers": [
                    "Agreement structure and licensed economic asset",
                    "Concrete calculation of operator fee consideration",
                    "Evidence required before treating consideration as earned",
                    "Fallback when the modeled premise fails",
                ],
                "rows": [
                    [
                        "Patent field-of-use rights limited to identified product families",
                        "100,000 covered units times $0.20 plus $10,000 implementation license",
                        "Executed patent schedule, coverage analysis, and accepted implementation deliverables",
                        "Offer narrow evaluation rights while resolving coverage disputes",
                    ],
                    [
                        "Territorial brand rights with measurable product quality controls",
                        "$750,000 eligible sales times four percent yields $30,000 royalties",
                        "Royalty sales reports and documented quality inspection results",
                        "Shorten territory duration and remove unsupported exclusive rights",
                    ],
                    [
                        "Catalog and dataset packages limited to enumerated permitted uses",
                        "Four independently priced packages times $7,500 yields $30,000",
                        "Asset provenance register, delivery receipts, and permitted-use schedules",
                        "Exclude disputed assets and credit only affected consideration",
                    ],
                    [
                        "Licensed customs evidence workflow rather than importer merchandise",
                        "$25,000 license against modeled $500,000 annual duty savings",
                        "Genuine licensed deliverables plus counsel-reviewed transaction evidence dossier",
                        "Use broker escrow and retain defensible values on unsupported entries",
                    ],
                    [
                        "Base cohort minimum guarantees recoupable against earned royalties",
                        "$200,000 collected minimum offsets the existing $400,000 royalty stream",
                        "Contract recoupment ledger reconciled against each licensee statement",
                        "Defer unearned collections and prevent duplicate royalty invoicing",
                    ],
                    [
                        "Base cohort fixed fees distinct from underlying product sales",
                        "$50,000 earned fixed fees supplement $400,000 royalty billings",
                        "Separate performance records supporting each earned fixed license fee",
                        "Reverse unsupported fees without changing licensee sales measurements",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the Royalty Base Before Negotiating the Rate",
                "body": (
                    "A tightly defined royalty base often produces more collectible "
                    "cash than a higher headline percentage with broad deductions."
                ),
                "items": [
                    "Attach a numeric minimum-guarantee example showing exactly how each payment recoups against subsequent royalties.",
                    "Require SKU-level returns and affiliate-transfer data so licensees cannot silently move sales outside the royalty base.",
                    "For brand rights, budget actual inspection work and preserve evidence of quality control rather than relying on a contractual sentence.",
                    "For first-sale workflows, escrow encrypted factory invoices with authorized broker access, CBP access procedures, and a customs-counsel opinion letter.",
                ],
            },
        },
        {
            "heading": "2. Reconcile Every Deduction to the Canonical Owner Profit",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Build the waterfall from gross contractual billings rather "
                    "than from cash deposits. Conservative billings of $55,000 "
                    "less $3,000 of credits and $2,000 of expected reversals "
                    "produce $50,000 revenue. Base billings of $450,000 less "
                    "$15,000 and $10,000 produce $425,000. Scaled billings of "
                    "$840,000 less $24,000 and $16,000 produce $800,000. Credits "
                    "represent identified returns, canceled permissions, and "
                    "contractually valid true-ups; the reversal allowance covers "
                    "supported estimates of additional price adjustments. Do not "
                    "mix either category with unpaid but valid receivables: credit "
                    "losses require their own assessment and accounting treatment. "
                    "The illustrative gross-billings scrub rates are 9.09 percent, "
                    "5.56 percent, and 4.76 percent respectively. Better reporting "
                    "can reduce leakage, but these rates are assumptions rather "
                    "than evidence that scale automatically improves contracts. "
                    "Give each deduction a reason code, source document, owner, "
                    "and resolution date. Preserve the original statement and "
                    "post a linked correcting record instead of overwriting "
                    "history. For quarterly royalties, estimate earned amounts "
                    "using defensible reporting data and reconcile promptly when "
                    "the licensee statement arrives. Collection timing changes "
                    "cash availability; it does not by itself determine whether "
                    "the licensed performance has been completed."
                ),
                (
                    "Subtract direct contractor delivery labor of $12,000, "
                    "$70,000, and $90,000, then third-party rights participation "
                    "of $7,500, $55,000, and $80,000. Gross contribution becomes "
                    "$30,500, $300,000, and $630,000, equivalent to 61 percent, "
                    "70.59 percent, and 78.75 percent of recognized revenue. "
                    "The labor budgets correspond to 120, 700, and 900 hours "
                    "at a $100 blended hourly rate, covering technical rights "
                    "packaging, metadata remediation, reporting setup, and "
                    "scheduled quality reviews. These are purchased hours, not "
                    "three or four full-time contractor salaries. Rights "
                    "participation is modeled as an expense because this example "
                    "assumes the operator controls the licensed rights and acts "
                    "as principal; an agency arrangement may require net "
                    "presentation instead. Obtain an accounting assessment before "
                    "reusing this presentation for represented creators. Log "
                    "contractor time by agreement and task so remediation cannot "
                    "hide inside platform overhead. Separate revenue-share "
                    "obligations from recoupable advances paid to rights owners. "
                    "An advance can consume cash before its expense is recognized. "
                    "Require the contract to state whether participation is "
                    "calculated on invoiced, earned, or collected fees, because "
                    "that distinction determines who finances a late-paying "
                    "licensee and whether deductions can be passed through."
                ),
                (
                    "Below gross contribution, charge acquisition spending of "
                    "$6,000, $35,000, and $45,000; platforms and operating "
                    "infrastructure of $4,000, $18,000, and $24,000; counsel, "
                    "audit, and insurance of $5,000, $26,375, and $31,000; "
                    "and retained staffing and administrative support of "
                    "$3,000, $40,000, and $50,000. Total operating costs are "
                    "$37,500, $244,375, and $320,000, leaving the required "
                    "$12,500, $180,625, and $480,000 owner profits. Net margins "
                    "therefore remain exactly 25 percent, 42.5 percent, and "
                    "60 percent. Support spending covers non-delivery work and, "
                    "in Scaled, the second full-time role; allocate time once "
                    "rather than duplicating it in contractor delivery. This "
                    "illustration treats the founder's residual as owner "
                    "earnings before personal taxes, without a separate imputed "
                    "replacement salary. Validate whether the support budget "
                    "can actually purchase the proposed staffing locally. "
                    "Conservative and Base use one full-time operator plus "
                    "three contractors; Scaled uses two full-time people plus "
                    "four contractors. The stated $2,000 to $15,000 monthly "
                    "opex range describes the platform's operating envelope, "
                    "not an all-inclusive cap on royalties and delivery costs. "
                    "Base all-in monthly costs average $20,364.58 and Scaled "
                    "$26,666.67; budgeting only recurring overhead would materially "
                    "underfund both cohorts."
                ),
            ],
            "table": {
                "caption": "Complete Annual Billings-to-Owner-Profit Waterfall in USD",
                "headers": [
                    "Waterfall stage and treatment of the amounts",
                    "Conservative cohort calculation and resulting annual balance",
                    "Base cohort calculation and resulting annual balance",
                    "Scaled cohort calculation and resulting annual balance",
                ],
                "rows": [
                    [
                        "Start with contractual billings before any deduction estimates",
                        "$55,000 gross billings across two active annual agreements",
                        "$450,000 gross billings across ten active annual agreements",
                        "$840,000 gross billings across sixteen active annual agreements",
                    ],
                    [
                        "Deduct identified credits and supported expected royalty reversals",
                        "Subtract $3,000 credits and $2,000 reversals; revenue equals $50,000",
                        "Subtract $15,000 credits and $10,000 reversals; revenue equals $425,000",
                        "Subtract $24,000 credits and $16,000 reversals; revenue equals $800,000",
                    ],
                    [
                        "Deduct direct contractor labor and third-party rights participation",
                        "Subtract $12,000 labor and $7,500 participation; contribution equals $30,500",
                        "Subtract $70,000 labor and $55,000 participation; contribution equals $300,000",
                        "Subtract $90,000 labor and $80,000 participation; contribution equals $630,000",
                    ],
                    [
                        "Deduct acquisition spending and platform operating infrastructure costs",
                        "Subtract $6,000 acquisition and $4,000 platforms; remaining balance $20,500",
                        "Subtract $35,000 acquisition and $18,000 platforms; remaining balance $247,000",
                        "Subtract $45,000 acquisition and $24,000 platforms; remaining balance $561,000",
                    ],
                    [
                        "Deduct counsel, audit, insurance, and retained operating support",
                        "Subtract $5,000 professional costs and $3,000 support; profit $12,500",
                        "Subtract $26,375 professional costs and $40,000 support; profit $180,625",
                        "Subtract $31,000 professional costs and $50,000 support; profit $480,000",
                    ],
                    [
                        "Verify total costs, exact margin, and assigned team capacity",
                        "$37,500 costs; 25% margin; one full-time operator plus three contractors",
                        "$244,375 costs; 42.5% margin; one full-time operator plus three contractors",
                        "$320,000 costs; 60% margin; two full-time people plus four contractors",
                    ],
                ],
            },
        },
        {
            "heading": "3. Fund the Collection Gap Without Spending Deferred Cash",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Measure the cash gap from payment of delivery obligations "
                    "to unrestricted receipt, not simply from invoice date. "
                    "For a comparable steady-state planning screen, assume costs "
                    "are paid as incurred, no supplier credit, and a uniform "
                    "daily cost rate. Conservative uses 90 days sales outstanding "
                    "plus a separate 30-day payout lock; Base uses 75 plus "
                    "15; Scaled uses 60 plus ten. Here the lock begins after "
                    "the licensee pays into a collecting intermediary, so adding "
                    "the periods does not double-count the same delay. A direct "
                    "bank receipt without a contractual restriction has no such "
                    "lock. Applying total annual costs divided by 365 to gaps "
                    "of 120, 90, and 70 days yields operating bridges of "
                    "$12,328.77, $60,256.85, and $61,369.86. Add designated "
                    "liquidity buffers of $2,000, $10,000, and $16,000 to "
                    "obtain $14,328.77, $70,256.85, and $77,369.86 of modeled "
                    "funding. Those buffers mirror the reversal allowances for "
                    "planning convenience but are cash allocations, not second "
                    "expenses. Quarterly settlement cliffs, upfront acquisition "
                    "payments, and disputed statements can require substantially "
                    "more cash than this daily-average screen. Build a dated "
                    "receipts-and-disbursements schedule before committing the "
                    "operator to a minimum guarantee owed upstream."
                ),
                (
                    "Maintain a rolling thirteen-week cash forecast with separate "
                    "columns for unrestricted bank cash, intermediary-held cash, "
                    "receivables, unearned advances, rights-owner payables, and "
                    "contractor commitments. QuickBooks can hold the accounting "
                    "ledger while a controlled spreadsheet carries contract-level "
                    "settlement dates; reconcile both to bank statements every "
                    "week. A $100,000 license advance does not create $100,000 "
                    "of distributable profit when refresh obligations or "
                    "recoupable royalties remain outstanding. Similarly, accrued "
                    "royalties may be profitable without financing next Friday's "
                    "contractor payments. Negotiate staged fixed fees at signed "
                    "delivery milestones, minimum guarantees paid before the "
                    "licensed selling season, and rights participation payable "
                    "after collection where commercially achievable. Do not "
                    "rewrite existing payout obligations through an internal "
                    "forecast assumption. Model withholding taxes separately "
                    "from contractual royalty deductions, including any treaty "
                    "documentation and recoverability assessment relevant to "
                    "cross-border collections. An unrecoverable withholding "
                    "reduces economics; a recoverable amount can still extend "
                    "the cash gap. Keep customs duty savings completely outside "
                    "this treasury schedule because that cash belongs to the "
                    "importer. Only the operator's earned license invoices and "
                    "associated costs belong in the licensing cohort. Restrict "
                    "bank-account changes to verified counterparties using an "
                    "independent callback rather than an emailed instruction."
                ),
                (
                    "Startup capital of $25,000 to $250,000 must finance both "
                    "origination and the collection bridge, with first deals "
                    "potentially taking six to 24 months. At $2,000 monthly "
                    "predeal overhead, six months consumes $12,000 and 24 months "
                    "$48,000 before acquisition spikes or rights purchases. "
                    "At $15,000 monthly overhead, those amounts become $90,000 "
                    "and $360,000, so the long-delay, high-burn combination "
                    "exceeds the stated upper capital range even before "
                    "working capital. Do not present all endpoints as jointly "
                    "affordable. A six-month low-burn launch plus the "
                    "Conservative bridge already requires $26,328.77, slightly "
                    "above the minimum startup amount. Reduce committed overhead, "
                    "obtain an earned milestone payment, or secure committed "
                    "funding before accepting that path. For Base, a 30-day "
                    "collection slip adds $20,085.62 to bridge needs without "
                    "changing recognized profit if collectibility remains "
                    "intact. Track disputed balances separately because an "
                    "eventual price concession changes revenue as well as cash. "
                    "Prepare a weekly concentration view showing the cash "
                    "forecast with the largest licensee delayed. A profitable "
                    "portfolio can still fail when one quarterly remittance "
                    "finances nearly all payroll and the operator has "
                    "distributed last month's unrestricted cash too early."
                ),
            ],
            "table": {
                "caption": "Collection-Delay, Payout-Lock and Liquidity Funding Matrix",
                "headers": [
                    "Cash mechanism and explicit modeling assumption",
                    "Conservative cash requirement or operating treatment",
                    "Base cash requirement or operating treatment",
                    "Scaled cash requirement or operating treatment",
                ],
                "rows": [
                    [
                        "Collection interval followed by a distinct intermediary payout lock",
                        "90 collection days plus 30 locked days equals 120 days",
                        "75 collection days plus 15 locked days equals 90 days",
                        "60 collection days plus ten locked days equals 70 days",
                    ],
                    [
                        "Daily cash cost calculated from complete annual operating costs",
                        "$37,500 divided by 365 produces $102.74 daily cash costs",
                        "$244,375 divided by 365 produces $669.52 daily cash costs",
                        "$320,000 divided by 365 produces $876.71 daily cash costs",
                    ],
                    [
                        "Operating bridge uses unrounded daily costs and stated delays",
                        "120 days of operating costs requires $12,328.77 bridge funding",
                        "90 days of operating costs requires $60,256.85 bridge funding",
                        "70 days of operating costs requires $61,369.86 bridge funding",
                    ],
                    [
                        "Designated reversal liquidity buffer adds cash without another expense",
                        "$2,000 additional liquidity produces $14,328.77 total modeled funding",
                        "$10,000 additional liquidity produces $70,256.85 total modeled funding",
                        "$16,000 additional liquidity produces $77,369.86 total modeled funding",
                    ],
                    [
                        "Thirty additional collection days increase funding without immediate repricing",
                        "Add $3,082.19 funding if collectibility and contractual pricing remain intact",
                        "Add $20,085.62 funding if collectibility and contractual pricing remain intact",
                        "Add $26,301.37 funding if collectibility and contractual pricing remain intact",
                    ],
                    [
                        "Contractual cash controls replace assumptions before actual distribution decisions",
                        "Verify both licensees' settlement dates before distributing owner cash",
                        "Reconcile all ten agreements against weekly bank and intermediary balances",
                        "Model sixteen settlement schedules and maintain second-employee payroll coverage",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the statement population",
                    "action": "Export contract, invoice, royalty, adjustment, and settlement records for the same reporting cutoff.",
                    "detail": "Retain source files and immutable identifiers; reconcile beginning balances before calculating current-period economics.",
                },
                {
                    "step": 2,
                    "title": "Rebuild earned consideration",
                    "action": "Apply permitted-use pricing, minimum recoupment, documented credits, and supported reversal estimates by agreement.",
                    "detail": "Keep underlying licensee sales separate from operator fees and prevent advances from appearing twice.",
                },
                {
                    "step": 3,
                    "title": "Schedule every cash obligation",
                    "action": "Place contractor payments, rights participation, overhead, expected receipts, and lock releases into thirteen weekly columns.",
                    "detail": "Use actual contractual dates where available and separately identify disputed or conditional receipts.",
                },
                {
                    "step": 4,
                    "title": "Set the distribution ceiling",
                    "action": "Retain committed operating cash and designated reserves before calculating available owner distributions.",
                    "detail": "Re-run the largest-licensee delay case and document the funded response before releasing surplus cash.",
                },
            ],
        },
        {
            "heading": "4. Stress the Cohort and Price the Failure Modes",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Calculate acquisition efficiency at the cohort level before "
                    "celebrating the headline net margin. Assuming every modeled "
                    "agreement is newly acquired and all acquisition spending "
                    "belongs to that cohort, Conservative CAC is $6,000 divided "
                    "by two, or $3,000; Base is $35,000 divided by ten, "
                    "or $3,500; Scaled is $45,000 divided by sixteen, or "
                    "$2,812.50. Annual contribution before acquisition and "
                    "overhead is $15,250, $30,000, and $39,375 per agreement. "
                    "Dividing CAC by monthly contribution gives approximately "
                    "2.36, 1.40, and 0.86 months of contribution-equivalent "
                    "payback, but these are not elapsed cash payback periods. "
                    "Origination may consume six to 24 months, and collection "
                    "delays follow delivery. Include failed pitches, technical "
                    "evaluations, and negotiation expense in CAC rather than "
                    "assigning costs only to signed accounts. If renewals "
                    "dominate the portfolio, separate new-customer CAC from "
                    "retention costs instead of dividing by every active "
                    "agreement. Annual owner profit per active agreement is "
                    "$6,250, $18,062.50, and $30,000. Use these figures to "
                    "prioritize reporting automation and renewal alerts, not "
                    "to assume each account has identical profitability. One "
                    "catalog client demanding weekly manual exports can consume "
                    "the contribution generated by several clean annual licenses."
                ),
                (
                    "Run sensitivity cases without changing the canonical "
                    "baseline. A ten percent reduction in recognized revenue "
                    "with operating costs held fixed reduces annual owner "
                    "profit to $7,500, $138,125, and $400,000. This intentionally "
                    "assumes no immediate participation savings, as may occur "
                    "with fixed upstream minimums. A twenty percent contractor "
                    "labor overrun instead reduces profit to $10,100, $166,625, "
                    "and $462,000. Combining both shocks produces $5,100, "
                    "$124,125, and $382,000. Keep collection stress separate "
                    "until there is evidence of a concession or credit loss; "
                    "adding 30 DSO days increases required liquidity by "
                    "$3,082.19, $20,085.62, and $26,301.37 rather than "
                    "automatically reducing earnings. For audit economics, "
                    "a five percent royalty on $200,000 of substantiated "
                    "omitted sales supports a $10,000 claim. If recovery "
                    "probability is 80 percent and audit cost is $6,000, "
                    "expected recovery less cost is $2,000 before collection "
                    "delay and relationship damage. The risk fallback is "
                    "a targeted records request before a broad audit. Do "
                    "not book an unagreed audit claim as ordinary recurring "
                    "revenue. Require documented access rights, a defined "
                    "lookback period, and contractual cost-shifting thresholds "
                    "before assuming the licensee will pay investigative expenses."
                ),
                (
                    "Translate legal boundaries into observable operating checks "
                    "rather than ceremonial contract language. Verify signed "
                    "copyright transfers under 17 U.S.C. 204, patent assignment "
                    "records under 35 U.S.C. 261, and the trademark quality "
                    "control implications of 15 U.S.C. 1127. A trademark "
                    "assignment also requires attention to associated goodwill "
                    "under 15 U.S.C. 1060. Territory and field restrictions "
                    "require competition analysis under 15 U.S.C. 1 rather "
                    "than an assumption that ownership permits every restraint. "
                    "For customs-related licenses, test whether royalty "
                    "payments must be added to transaction value under "
                    "19 U.S.C. 1401a(b)(1)(D); a workflow fee's label does "
                    "not settle its customs treatment. These checks affect "
                    "price, reserves, and whether delivery can proceed at all. "
                    "Use automated obligation tracking to flag expiring rights, "
                    "missed reports, inspection dates, and territory changes, "
                    "but assign a named human to each exception. Before "
                    "scaling, reproduce the Base waterfall from original "
                    "contracts and bank records, demonstrate a funded delayed "
                    "collection case, and show contractor capacity for the "
                    "proposed reporting calendar. When title or permitted use "
                    "fails verification, suspend the affected grant and offer "
                    "a narrower documented package. More volume cannot repair "
                    "rights that the operator never possessed."
                ),
            ],
            "table": {
                "caption": "Acquisition Economics and Explicit Downside Sensitivities",
                "headers": [
                    "Test condition and variables held constant",
                    "Conservative result with a specific operating response",
                    "Base result with a specific operating response",
                    "Scaled result with a specific operating response",
                ],
                "rows": [
                    [
                        "All modeled agreements newly acquired using allocated acquisition spending",
                        "$3,000 CAC per agreement; include failed pitches in acquisition records",
                        "$3,500 CAC per agreement; separate prospecting from renewal servicing",
                        "$2,812.50 CAC per agreement; verify channel efficiency persists at volume",
                    ],
                    [
                        "Ten percent recognized revenue decline with all costs unchanged",
                        "$7,500 owner profit remains; stop discretionary acquisition before cash tightens",
                        "$138,125 owner profit remains; renegotiate fixed upstream minimums where possible",
                        "$400,000 owner profit remains; protect reporting capacity for retained accounts",
                    ],
                    [
                        "Twenty percent contractor delivery overrun without additional earned fees",
                        "$10,100 owner profit remains; constrain custom packaging and manual remediation",
                        "$166,625 owner profit remains; charge separately for permitted incremental refreshes",
                        "$462,000 owner profit remains; batch repeatable tasks without weakening inspections",
                    ],
                    [
                        "Combine ten percent revenue decline with twenty percent labor overrun",
                        "$5,100 owner profit remains; retain cash before taking owner distributions",
                        "$124,125 owner profit remains; prioritize collectible accounts and standard delivery",
                        "$382,000 owner profit remains; preserve reserves against concentrated licensee exposure",
                    ],
                    [
                        "Add thirty collection days while price and collectibility remain intact",
                        "$3,082.19 extra funding required; confirm both counterparties' actual payment dates",
                        "$20,085.62 extra funding required; fund delayed quarterly settlements before distributions",
                        "$26,301.37 extra funding required; reserve liquidity before adding another cohort",
                    ],
                    [
                        "Audit omitted sales using a documented recovery probability and cost",
                        "$10,000 claim less risk and cost yields $2,000 expected recovery",
                        "Apply the same $2,000 expected recovery test before commissioning audits",
                        "Aggregate evidence carefully without assuming every licensee omitted equivalent sales",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify Rights, Economics, Cash and Capacity Before Expansion",
                "body": (
                    "Expansion requires reproducible evidence in four areas; "
                    "a signed sales agreement alone does not establish a funded, "
                    "deliverable licensing cohort."
                ),
                "items": [
                    "Verify signed chain-of-title documents, permitted uses, territories, sublicensing authority, and scheduled trademark quality inspections.",
                    "Reproduce the exact canonical revenue and profit totals, with each credit, reversal estimate, and rights participation linked to a contract.",
                    "Fund the dated collection schedule and a 30-day delay case while excluding deferred advances from distributable cash.",
                    "Confirm contractor hours, renewal ownership, reporting access, and customs evidence custody before adding agreements or promising exclusive rights.",
                ],
            },
        },
    ],
    "pull_quote": "A royalty is only valuable when the rights are defensible, the deductions are bounded, and the cash arrives before the obligations fall due.",
    "diagram_id": "diag-03",
    "action_checklist": [
        "Create a contract-level ledger separating licensee sales, gross billings, earned fees, recoupable advances, receivables, and unrestricted cash.",
        "Reconcile the three annual waterfalls to $12,500, $180,625, and $480,000 owner profit without counting product sales or customs savings as revenue.",
        "Document credit reason codes and reversal estimates, then designate cash buffers without recording duplicate expenses.",
        "Build a thirteen-week cash forecast using actual settlement dates, intermediary lock releases, rights-owner payouts, and contractor commitments.",
        "Run revenue, contractor-overrun, and additional-30-day collection stresses separately and together before setting owner distributions.",
        "Verify title and permitted uses, establish royalty audit access, and document broker escrow plus a customs-counsel opinion for first-sale workflow licenses.",
    ],
    "statutory_citations": [
        {
            "title": "19 CFR 152.103 — Transaction value",
            "url": "https://www.ecfr.gov/current/title-19/section-152.103",
            "relevance": "Governs transaction-value mechanics and valuation adjustments relevant to substantiated multi-tier import transactions.",
        },
        {
            "title": "19 U.S.C. 1401a — Valuation of merchandise",
            "url": "https://www.law.cornell.edu/uscode/text/19/1401a",
            "relevance": "Section 1401a(b)(1)(D) addresses additions for qualifying royalties and license fees required as conditions of sale.",
        },
        {
            "title": "17 U.S.C. 204 — Execution of transfers of copyright ownership",
            "url": "https://www.law.cornell.edu/uscode/text/17/204",
            "relevance": "Requires a signed writing for covered copyright ownership transfers, supporting catalog chain-of-title verification.",
        },
        {
            "title": "35 U.S.C. 261 — Ownership; assignment",
            "url": "https://www.law.cornell.edu/uscode/text/35/261",
            "relevance": "Establishes patent assignment and recording rules relevant to authority to grant patent rights.",
        },
        {
            "title": "15 U.S.C. 1127 — Construction and definitions; intent of chapter",
            "url": "https://www.law.cornell.edu/uscode/text/15/1127",
            "relevance": "Defines related-company control and abandonment concepts relevant to trademark licensing and actual quality oversight.",
        },
        {
            "title": "15 U.S.C. 1060 — Assignment",
            "url": "https://www.law.cornell.edu/uscode/text/15/1060",
            "relevance": "Addresses trademark assignments with associated goodwill and restrictions affecting transfer validity.",
        },
        {
            "title": "15 U.S.C. 1 — Trusts, etc., in restraint of trade illegal; penalty",
            "url": "https://www.law.cornell.edu/uscode/text/15/1",
            "relevance": "Provides the competition-law foundation for evaluating licensing restraints, including territorial and coordinated pricing arrangements.",
        },
    ],
}
