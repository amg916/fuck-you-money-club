from __future__ import annotations

from copy import deepcopy
from .volume_001_chapters_b import CHAPTERS_7_TO_12, build_volume_001_workbook


def build_volume_001_diagrams_data() -> list[dict]:
    """Return fresh, renderer-neutral data; examples are not market benchmarks."""
    specs = [
        ("diag-01-end-to-end-workflow", "process_flow", "From lead to documented recovery", "Five gates, not a promise of payment", 1,
         "operating_framework", "Ordinal numeric values indicate sequence, not elapsed time or success probability.",
         "Identify the legal lane before researching relatives or offering a recovery contract.", [
             ("Classify", "Gate 1", 1.0, "Separate probate, custodial unclaimed property and sale surplus."),
             ("Qualify", "Gate 2", 2.0, "Verify the record, claimant eligibility, deadlines and likely net value."),
             ("Prove", "Gate 3", 3.0, "Build a sourced relationship chain and resolve contradictory records."),
             ("Authorize", "Gate 4", 4.0, "Obtain lawful consent and locally reviewed contractual authority."),
             ("Resolve", "Gate 5", 5.0, "Submit through the authorized channel and reconcile actual distributions.")]),
        ("diag-02-deal-funnel", "funnel", "A qualification funnel worth measuring", "Illustrative cohort of 100 records", 6,
         "illustrative_model", "Invented nested cohort; these counts are not observed conversion rates or a forecast.",
         "Measure why records leave each gate; signed clients and completed distributions are different outcomes.", [
             ("Records screened", "100", 100.0, "Deduplicated records with identifiable custodians or case numbers."),
             ("Plausible net value", "30", 30.0, "Illustrative survivors after preliminary eligibility and liability checks."),
             ("Evidence feasible", "12", 12.0, "A credible document path exists within a defined research budget."),
             ("Authorized clients", "4", 4.0, "Eligible claimants choose assistance under lawful agreements."),
             ("Paid resolutions", "2", 2.0, "Actual collected fees, potentially many months after intake.")]),
        ("diag-03-fee-waterfall", "waterfall", "What remains of a collected fee", "Business contribution, not the estate distribution", 3,
         "illustrative_model", "USD; first and last bars are totals, middle bars are signed deductions. Assumed lawful fee is $6,000 on $60,000 recovered.",
         "A $6,000 fee less $1,200 records, $800 review and $1,000 allocated acquisition leaves $3,000 before overhead, owner pay and tax.", [
             ("Collected fee", "$6,000", 6000.0, "Opening total: a hypothetical 10% fee, only if lawful for this claim."),
             ("Records and research", "-$1,200", -1200.0, "Direct evidence costs, including paid research labor."),
             ("Professional review", "-$800", -800.0, "Business-paid review; not an asserted statutory charge."),
             ("Acquisition allocation", "-$1,000", -1000.0, "Allocated costs include unsuccessful leads, not just this winner."),
             ("Contribution", "$3,000", 3000.0, "Closing total, not an additional movement and not owner net profit.")]),
        ("diag-04-jurisdiction-fee-caps", "horizontal_bars", "Fee-cap sensitivity before choosing a market", "Hypothetical legal ceilings, not a state-law comparison", 2,
         "illustrative_model", "Percent of a $40,000 recovery. A-D are hypothetical jurisdictions; no bar states an actual legal limit. Replace only after current legal review.",
         "Identical recoveries can support different maximum fees; timing restrictions can make an agreement unavailable regardless of percentage.", [
             ("Hypothetical A", "5% / $2,000", 5.0, "Assumed ceiling only; agreement eligibility still requires review."),
             ("Hypothetical B", "10% / $4,000", 10.0, "Assumed ceiling, not a recommendation to charge the maximum."),
             ("Hypothetical C", "15% / $6,000", 15.0, "Assumed ceiling; the allowable compensation base may differ."),
             ("Hypothetical D", "20% / $8,000", 20.0, "Assumed ceiling; expense reimbursement can also be regulated.")]),
        ("diag-05-kinship-decision-tree", "decision_tree", "Build proof before naming an heir", "A research triage tree, not a distribution formula", 7,
         "operating_framework", "Numeric values identify nodes. Edges are stated in detail; local law decides succession, representation and shares.",
         "Relationship evidence supports legal analysis; it does not replace a court's finding of entitlement.", [
             ("Governing instrument?", "Node 1", 1.0, "Valid will or trust: follow counsel's instrument analysis; otherwise continue to node 2."),
             ("Spouse or descendants?", "Node 2", 2.0, "Yes: document and refer for allocation; no: continue to node 3. Spousal rights may coexist with descendants."),
             ("Parents or collateral kin?", "Node 3", 3.0, "Yes: prove each link and refer for statutory priority; no or uncertain: continue to node 4."),
             ("Evidence unresolved?", "Node 4", 4.0, "Stop distribution assumptions; obtain missing records and counsel's direction on further classes or escheat.")]),
        ("diag-06-small-team-org", "org_architecture", "Separate research, review and client care", "Roles may be fractional; authority must remain distinct", 9,
         "operating_framework", "Numeric values are role identifiers, not headcounts, hierarchy ranks or compensation.",
         "The owner coordinates researchers and client care; independent licensed advisers retain professional judgment.", [
             ("Owner / case lead", "Role 1", 1.0, "Accountable for intake gates, budgets and secure case access."),
             ("Research specialist", "Role 2", 2.0, "Reports case evidence to the lead; does not decide legal entitlement."),
             ("Client coordinator", "Role 3", 3.0, "Reports to the lead; tracks consent, requests and plain-language updates."),
             ("Independent counsel", "Role 4", 4.0, "Advises within a separate engagement; not controlled by a research sales target.")]),
        ("diag-07-startup-budget-stack", "stacked_comparison", "A lean pilot's startup cash stack", "Compare cost composition, not promised earnings", 4,
         "illustrative_model", "USD; one scenario with four additive components totaling $5,000. This is not a vendor quote or paired market comparison; living expenses are excluded.",
         "Keep a reserve for failed cases and delays; a cheap subscription does not make the business fully funded.", [
             ("Setup and review", "$1,500", 1500.0, "Illustrative formation, contract review and insurance allowance; obtain actual quotes."),
             ("Research tools", "$600", 600.0, "Illustrative three-month subscriptions and basic secure working tools."),
             ("Pilot case costs", "$900", 900.0, "Illustrative records, postage and limited paid research."),
             ("Business reserve", "$2,000", 2000.0, "Uncommitted buffer; owner living costs and taxes require a separate plan.")]),
        ("diag-08-30-day-roadmap", "timeline_roadmap", "Thirty days to a controlled pilot", "Readiness milestones, not a collection deadline", 12,
         "operating_framework", "Numeric values are milestone end-days; ranges are calendar targets, not statutory deadlines.",
         "The first month should produce a reviewable process and documented cases, not an unsupported income promise.", [
             ("Choose the lane", "Days 1-7", 7.0, "Select one jurisdiction, custodian and claim type; get legal gates reviewed."),
             ("Build the controls", "Days 8-14", 14.0, "Set record provenance, privacy, case budgets and written stop rules."),
             ("Run a small cohort", "Days 15-21", 21.0, "Screen a bounded batch and build evidence only for qualified leads."),
             ("Review and decide", "Days 22-30", 30.0, "Audit economics and compliance; continue, redesign or stop the pilot.")]),
    ]
    return [dict(diagram_id=identifier, chart_type=kind, title=title, subtitle=subtitle,
                 chapter_number=chapter, epistemic_tag=tag, assumptions_note=note, caption=caption,
                 stages=[dict(label=label, value=value, numeric_value=float(number), detail=detail)
                         for label, value, number, detail in stages])
            for identifier, kind, title, subtitle, chapter, tag, note, caption, stages in specs]


def _ch(number, slug, title, subtitle, layout, minutes, summary, metrics, sections, quote, diagram, checklist, citations):
    return dict(id=f"Q{number}", chapter_id=f"Q{number}", chapter_number=number,
                question_number=number, slug=slug, question_prompt=f"Q{number}: {title}",
                kicker=f"Q{number} / THE BIG MONEY PLAYBOOKS", title=title, subtitle=subtitle,
                layout_template=layout, reading_time_minutes=minutes, executive_summary=summary,
                key_metrics=[dict(label=label, value=value, context=context) for label, value, context in metrics],
                sections=sections, pull_quote=quote, diagram_id=diagram, action_checklist=checklist,
                statutory_citations=[dict(title=title, url=url, relevance=relevance) for title, url, relevance in citations])


CHAPTERS_1_TO_6 = [
    _ch(1, "what-is-heir-hunting", "What Exactly Is Heir Hunting?",
        "Three adjacent businesses with different claimants, rules and evidence.", "opportunity_overview", 4,
        "Heir hunting is paid identity and relationship research used to locate people who may have inheritance rights. It is not a universal license to recover every kind of abandoned money. Start by identifying the legal lane and the decision-maker.",
        [("Legal lanes", "3", "Probate, custodial property and sale surplus must not be conflated."), ("Proof standard", "Case-specific", "A family-tree hint is not an adjudicated entitlement."), ("Revenue timing", "Uncertain", "Research completion does not equal distribution.")], [
            dict(heading="Probate research follows the estate", epistemic_status="statutory_fact", paragraphs=["A probate researcher locates potential heirs and documents relationships. Intestacy statutes govern succession where applicable; a will, trust, spousal rights and other facts can change who receives property.", "The court or authorized fiduciary determines the administration path. Researchers should describe evidence and uncertainty, not promise a share or represent that discovering a relative proves entitlement."], table={"headers": ["Lane", "Typical decision-maker", "Central evidence"], "rows": [["Probate heir research", "Court / estate fiduciary", "Vital records, instruments and kinship chain"], ["State-held unclaimed property", "State custodian", "Owner identity and statutory successor authority"], ["Foreclosure or tax surplus", "Court / trustee / county under local law", "Title history, liens, sale record and priority"]]}),
            dict(heading="Custodial property is a different workflow", epistemic_status="operating_framework", paragraphs=["State-held accounts, checks and other property are claimed through the relevant custodian. A deceased owner's claimant may need estate authority, but that does not turn every custodial claim into an open probate lead.", "Owners can generally use official state claim channels without hiring a finder. Disclose that option, check finder-agreement restrictions and never imply affiliation with the government."], callout={"title": "Name the lane", "body": "Write the asset holder, claim type and governing jurisdiction at the top of every intake record."}),
            dict(heading="Sale surplus follows its own priority rules", epistemic_status="operating_framework", paragraphs=["Foreclosure and tax-sale surplus concerns proceeds remaining after legally specified payments. The claimant may be an owner, successor or lienholder, and the priority analysis differs from identifying an intestate heir.", "Before outreach, identify the specific sale process and current filing procedure. A large posted surplus can produce no payable amount for the person you found once senior claims and eligibility are considered."], sop_steps=["Record the official case or property identifier.", "Classify the asset and the authority handling it.", "List unresolved entitlement and priority questions.", "Refer legal questions before drafting an offer."])
        ], "The opportunity is not finding a name. It is building a lawful, provable path from an asset to the right claimant.", "diag-01-end-to-end-workflow",
        ["Choose one claim lane.", "Identify the governing jurisdiction.", "Save the official source record.", "Separate identity from entitlement.", "Have counsel review the service boundary."],
        [("California Probate Code section 6402", "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=6402.", "Illustrative intestate succession authority; not a nationwide rule."), ("California Civil Code section 2924k", "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=2924k.", "Illustrates allocation of trustee-sale proceeds, distinct from probate succession.")]),
    _ch(2, "who-pays-and-where-capital-sits", "Who Pays, Why They Pay & Where Estate Capital Sits",
        "Find the payer, the asset holder and the authority to act before discussing price.", "executive_summary", 4,
        "People pay for documented research, coordination and reduced administrative burden, not for secret access to public funds. Payment depends on a lawful engagement and its actual terms. A claimant, fiduciary and asset custodian are different roles.",
        [("Payer", "Contract-specific", "Do not assume the court or state pays the finder."), ("Asset value", "Not distributable cash", "Debts, costs and competing rights matter."), ("DIY route", "Disclose", "Explain available official claim channels.")], [
            dict(heading="Who can authorize and who can pay", epistemic_status="operating_framework", paragraphs=["A potential heir might retain a researcher; a fiduciary might commission genealogy within their authority. Those arrangements have different approval, expense and conflict considerations, so the client and payer must be explicit.", "Do not charge an estate merely because a relative signed a contract. Determine who has authority, whether approval is required and whether a fee is payable from a claimant's recovery or under a separate professional engagement."], table={"headers": ["Role", "Typical responsibility", "Do not assume"], "rows": [["Claimant", "Provide identity and authorize permitted assistance", "Authority over the whole estate"], ["Fiduciary", "Administer within legal authority", "Unlimited power to approve expenses"], ["Custodian", "Evaluate claims and release property", "Liability for your private fee"]]}),
            dict(heading="Where capital actually sits", epistemic_status="operating_framework", paragraphs=["Estate assets may sit in bank accounts, real property or investments controlled through administration. State unclaimed property is held by a statutory custodian; sale surplus is held under a separate distribution process.", "An inventory is a snapshot, not a fee base. Verify liquidity, ownership, restrictions and whether the listed amount is still available. Treat an old docket entry or commercial lead list as a research pointer until the official record confirms it."], sop_steps=["Identify the current asset holder.", "Check the record's date and status.", "Separate gross value from likely distributable value.", "Document who can sign and who would pay."]),
            dict(heading="Value without pressure", epistemic_status="operating_framework", paragraphs=["A credible offer describes the records to be obtained, the work excluded, the applicable fee arrangement and the client's alternatives. Give people time to verify your identity through independently located contact details.", "Fee restrictions depend on jurisdiction and claim lane. The accompanying graphic is a sensitivity exercise, not a state comparison: hypothetical ceilings show why legal screening precedes acquisition spending."], callout={"title": "No government-affiliation claim", "body": "Use your own business identity and explain that hiring assistance is optional where a direct claim route exists."})
        ], "Locate the authority to pay before treating an asset as revenue.", "diag-04-jurisdiction-fee-caps",
        ["Name the client and payer separately.", "Verify the current custodian.", "Estimate net distributable value.", "Explain direct-claim alternatives.", "Review compensation and timing restrictions locally."],
        [("California Code of Civil Procedure section 1582", "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1582.", "Investigate current finder-agreement restrictions for state-held property; do not transplant them to probate."), ("California Probate Code section 8800", "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=8800.", "Inventory and appraisal framework; gross inventory is not a promised distribution.")]),
    _ch(3, "contingency-fees-and-unit-economics", "How the Business Makes Money: Contingency Structures, Fee Caps & Unit Economics",
        "Model collected fees after failed leads, costs and delay.", "financial_breakdown", 5,
        "A contingency model earns compensation only on the contract's lawful trigger. The percentage, fee base, expenses, cancellation provisions and timing restrictions require local review. Measure contribution and cash flow separately from headline recoveries.",
        [("Illustrative recovery", "$60,000", "Assumed client recovery, not business revenue."), ("Illustrative fee", "$6,000", "Assumed lawful 10%; not a recommended or universal rate."), ("Contribution", "$3,000", "Before fixed overhead, owner pay and taxes in this example.")], [
            dict(heading="Write the economic contract clearly", epistemic_status="operating_framework", paragraphs=["Specify the services, authorized claimant, payment trigger and amount on which any percentage is calculated. Address unsuccessful cases, document charges and termination without implying that a signed agreement guarantees a valid fee.", "A percentage below a nominal ceiling can still be unlawful if the agreement is premature, the service is regulated or mandatory disclosures are missing. Do not repackage prohibited compensation as expenses or obtain broad control of client assets to evade restrictions."], callout={"title": "Legal gate before pricing", "body": "Confirm the current statute, agency procedure and permitted agreement timing for the exact claim lane."}),
            dict(heading="Walk the fee down to contribution", epistemic_status="illustrative_model", paragraphs=["Assume a $60,000 actual recovery and a lawful 10% fee: collected business revenue is $6,000. Subtract $1,200 in research and records, $800 in professional review and $1,000 allocated acquisition cost to obtain $3,000 contribution.", "This is not owner net profit. Fixed overhead, owner compensation, taxes and financing costs remain. Allocate unsuccessful lead costs across the cohort; otherwise successful files appear more profitable than the business really is."], table={"headers": ["Line", "USD", "Treatment"], "rows": [["Collected fee", "6,000", "Revenue"], ["Research and records", "-1,200", "Direct costs"], ["Professional review", "-800", "Direct costs"], ["Acquisition allocation", "-1,000", "Includes failed leads"], ["Contribution", "3,000", "Before fixed costs, owner pay and tax"]]}),
            dict(heading="Cash timing can defeat paper margins", epistemic_status="illustrative_model", paragraphs=["For a hypothetical 20-lead cohort with two paid cases at $6,000 each, revenue is $12,000. If all cohort research, review and acquisition spend totals $9,000, contribution is $3,000. One paid case at the same spending produces a $3,000 loss.", "Track when money leaves as well as when it returns. A fee that arrives after a long administration cannot fund next month's expenses without reserves. Model no recovery, half the expected recoveries and twice the expected wait before expanding."], sop_steps=["Track cohort-level spend, including dead leads.", "Record actual collections rather than unsigned forecasts.", "Calculate contribution before owner profit.", "Stress-test both conversion and collection delay."])
        ], "Gross recovery belongs to the claimant; only lawful collected fees belong in your revenue model.", "diag-03-fee-waterfall",
        ["Obtain local agreement review.", "Define the permitted fee base.", "Allocate unsuccessful lead costs.", "Build a cash-flow reserve model.", "Reconcile every collection against the signed terms."],
        [("California Code of Civil Procedure section 1582", "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1582.", "Example of statutory restrictions on unclaimed-property compensation agreements."), ("California Probate Code section 11420", "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=11420.", "Estate payment priorities affect available distributions; this is not a finder fee schedule.")]),
    _ch(4, "realistic-startup-requirements", "Realistic Startup Requirements",
        "A bounded research pilot, professional review and enough cash to wait.", "comparison_table", 4,
        "The essential startup investment is a reliable evidence and compliance process. Begin in one jurisdiction with a defined research budget, secure records, reviewed contracts and a reserve. Do not confuse inexpensive access to records with low business risk.",
        [("Pilot cash", "$5,000", "Illustrative business-only budget, not a market estimate."), ("Operating scope", "One lane", "Limit initial legal and procedural complexity."), ("Owner runway", "Separate", "Living expenses are excluded from the example.")], [
            dict(heading="Buy capacity, not a stack of subscriptions", epistemic_status="illustrative_model", paragraphs=["An illustrative $5,000 pilot allocates $1,500 to setup and review, $600 to tools, $900 to pilot case costs and $2,000 to reserve. Actual legal, insurance and document costs vary substantially; obtain quotes before relying on these amounts.", "Purchase only the sources your initial cases require. Free official indexes may identify a lead, while certified records and specialist work can determine whether the relationship chain is usable. Budget for the evidence rather than collecting software subscriptions."], table={"headers": ["Component", "Illustrative USD", "Boundary"], "rows": [["Setup and professional review", "1,500", "Replace with quotes"], ["Tools for a short pilot", "600", "No implied vendor prices"], ["Pilot case costs", "900", "Bounded research spend"], ["Business reserve", "2,000", "Not owner living costs"]]}),
            dict(heading="Build defensible operating controls", epistemic_status="operating_framework", paragraphs=["Use a case register, source log, budget tracker and access-controlled document store. Capture record provenance and maintain a clear distinction between verified identities, possible matches and disproved hypotheses.", "Collect only the personal information needed for the claim and use secure transfer channels. Confirm licensing, registration, insurance and unauthorized-practice boundaries with qualified local advisers before offering services or accepting sensitive client records."], sop_steps=["Define the lane and permitted services.", "Obtain local professional review and actual quotes.", "Create case, consent and evidence templates.", "Set retention, access and deletion policies."]),
            dict(heading="Validate demand before committing overhead", epistemic_status="operating_framework", paragraphs=["A small pilot tests whether official leads can be screened, evidence can be obtained and eligible people value assistance at a lawful price. Set a fixed amount of time and cash you can afford to lose; an unresolved pilot is not a reason to keep spending indefinitely.", "Avoid commitments that depend on rapid distributions. A home-based researcher can still face extended collections and failed files. Continue only when the pilot shows a repeatable process and economics that survive realistic unsuccessful cases."], callout={"title": "Stop rule", "body": "Pause when the approved research budget is exhausted, a legal gate fails or the evidence no longer supports a plausible claim."})
        ], "Start small enough to discover the process is wrong without putting your household at risk.", "diag-07-startup-budget-stack",
        ["Select one jurisdiction and lane.", "Get professional and insurance quotes.", "Create secure evidence storage.", "Fund business and personal reserves separately.", "Set a written pilot budget and stop date."],
        [("California Business and Professions Code section 6125", "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=6125.", "Illustrates restrictions on practicing law; research services must respect local professional boundaries."), ("California Code of Civil Procedure section 1582", "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1582.", "Review applicable finder-agreement constraints before budgeting for a state-property service.")]),
    _ch(5, "what-experienced-operators-know", "What Experienced Operators Know That Beginners Miss",
        "The best early decision is often a documented no-go.", "expert_insights", 5,
        "Experienced case screening asks what can reach the claimant after priority claims, administration costs and legal restrictions. Liens, Medicaid estate recovery and insolvency can change the economics completely. Treat operator advice as a hypothesis until official records and professional review support it.",
        [("Gross versus net", "Different", "A listed asset is not a payable inheritance."), ("Research budget", "Capped", "Use staged approvals rather than unlimited investigation."), ("Dead leads", "Log reasons", "Disqualification data improves the next cohort.")], [
            dict(heading="Lien priority comes before the exciting headline", epistemic_status="operating_framework", paragraphs=["A property value or sale-surplus amount is only the beginning. Secured claims, taxes, administration expenses and competing rights can consume the amount that appeared available. Obtain the relevant title, docket and payment records rather than assuming the first person located receives the balance.", "Priority rules differ between estate administration, trustee sales and tax sales. Record each known claim, its source, the unresolved amount and the legal question it raises. Have qualified counsel resolve priority disputes; a researcher should not turn an incomplete spreadsheet into a legal distribution opinion."], table={"headers": ["Risk", "Evidence to obtain", "Triage response"], "rows": [["Secured claim", "Recorded instrument and current payoff evidence", "Recalculate plausible net value"], ["Competing priority", "Official claims and court orders", "Seek legal allocation review"], ["Uncertain estate solvency", "Inventory, allowed debts and administration costs", "Pause optimistic recovery assumptions"], ["Stale or duplicate lead", "Current docket and custodian confirmation", "Close or merge with an audit trail"]]}),
            dict(heading="Medicaid estate recovery is not a universal clawback", epistemic_status="statutory_fact", paragraphs=["Federal Medicaid law requires estate recovery for certain assistance and allows states choices within the statutory framework. For people receiving covered assistance at age 55 or older, specified long-term-care services are central to the mandatory recovery rules. States can differ in covered recoveries and in whether their estate definition reaches certain nonprobate interests.", "Surviving-spouse and qualifying-child protections, deferral rules and hardship-waiver procedures can affect recovery. Do not assume that every Medicaid beneficiary's estate owes the same claim, or that every family qualifies for an exception. Obtain the state program's current notice and have counsel assess enforceability, timing and any applicable waiver before estimating distributions."], callout={"title": "MERP review gate", "body": "42 U.S.C. section 1396p(b) supplies a federal framework, not a case-specific payoff figure. State law and the actual facts remain essential."}),
            dict(heading="Insolvent estates and dead-lead triage", epistemic_status="operating_framework", paragraphs=["An estate can contain valuable property and still have nothing distributable to heirs. If assets are insufficient after legally prior payments, locating additional relatives does not create a recovery. Record whether the problem is insolvency, missing authority, inadequate evidence, a closed deadline or an uneconomic research path.", "Use staged research: inexpensive source confirmation first, a bounded evidence search second, and specialist escalation only after the file passes the earlier gates. Close a lead with a reason and a reopening condition rather than repeatedly rediscovering it. This preserves both cash and respectful treatment of families."], sop_steps=["Confirm current asset and claim status.", "List debts, liens and unresolved priority issues.", "Check Medicaid recovery questions where relevant.", "Estimate a conservative range of distributable value.", "Close, pause or approve the next research stage in writing."])
        ], "The discipline is not chasing every estate. It is knowing which uncertainty deserves another dollar.", "diag-02-deal-funnel",
        ["Build a priority and liability checklist.", "Flag potential Medicaid recovery for legal review.", "Test estate solvency before deep genealogy.", "Cap each stage's research spend.", "Record dead-lead reasons and reopening conditions."],
        [("42 U.S.C. section 1396p(b)", "https://www.law.cornell.edu/uscode/text/42/1396p", "Federal Medicaid estate-recovery framework, protections and hardship-waiver requirements; state implementation must also be checked."), ("California Probate Code section 11420", "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=11420.", "Illustrative order of payment of estate debts; do not generalize this state's priorities nationwide.")]),
    _ch(6, "finding-qualified-opportunities", "Finding Your First Qualified Opportunities",
        "A repeatable official-source workflow beats an indiscriminate lead list.", "step_by_step_sop", 5,
        "Choose one claim lane, screen a small batch of official records and advance only leads with plausible entitlement, net value and a feasible evidence path. Keep discovery separate from permission to contact, contract or file. The output is a qualified research queue, not a list of guaranteed recoveries.",
        [("Initial batch", "20 records", "Suggested pilot size, not an evidence-based optimum."), ("Required gates", "4", "Status, eligibility, net value and proof feasibility."), ("Success measure", "Paid cohort economics", "Do not substitute raw lead count for useful outcomes.")], [
            dict(heading="Choose sources that match the lane", epistemic_status="operating_framework", paragraphs=["For probate, begin with accessible court dockets and official public-administrator information in the selected jurisdiction. For custodial property, use the state's official search and claim instructions. For sale surplus, identify the responsible court, trustee or county and its specific official records.", "A listing's existence does not establish that the case is open, the money remains available or your proposed client is eligible. Respect access terms, record restrictions and privacy rules. Do not bypass access controls or use a commercial lead vendor's eligibility claim as a substitute for official confirmation."], table={"headers": ["Source lane", "Capture", "Verify next"], "rows": [["Probate docket", "Case number, decedent and fiduciary", "Current status and governing instruments"], ["State property record", "Property identifier and custodian", "Owner identity and successor requirements"], ["Sale-surplus record", "Sale identifier and holding authority", "Priority, deadlines and remaining balance"]]}),
            dict(heading="Run four qualification gates", epistemic_status="operating_framework", paragraphs=["First verify status and current availability. Second identify a plausible claimant and the authority they would need. Third estimate net distributable value after known claims, costs and uncertainty. Fourth assess whether the necessary records can be obtained within the pilot budget.", "For a suggested 20-record batch, time-box preliminary screening and escalate only documented survivors. The separate 100-record funnel is an invented teaching example, not a conversion target. Track observed outcomes in your own batch before making acquisition or staffing decisions."], sop_steps=["Save the official source URL, retrieval date and identifier.", "Confirm case status, availability and deadlines.", "Document the claimant hypothesis and missing authority.", "Estimate net value with unresolved claims explicitly flagged.", "Approve a bounded evidence search or close the lead."]),
            dict(heading="Approach qualified people without manufacturing urgency", epistemic_status="operating_framework", paragraphs=["Use a clear introduction identifying your business, the general nature of the matter and an independent way to verify your identity. Do not expose sensitive family details to an unverified recipient or demand identity documents through an insecure channel. A plausible match is not permission to reveal someone else's personal records.", "Before presenting an agreement, explain the scope, fee basis, available direct-claim route and limitations. Check contact, privacy and consumer-protection rules for the channel you use. Declined assistance is a valid outcome; log it and respect any request not to be contacted again."], callout={"title": "A qualified opportunity is not a signed client", "body": "Keep lead qualification, identity verification, informed consent and lawful representation as separate gates."})
        ], "Find the official record first, the evidence path second and the commercial opportunity last.", "diag-02-deal-funnel",
        ["Pick one official source and claim lane.", "Screen a bounded pilot batch.", "Record provenance and status for every lead.", "Advance only leads that pass all four gates.", "Use reviewed, privacy-conscious outreach and consent procedures."],
        [("California Probate Code section 6402", "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=6402.", "Illustrates why a claimant hypothesis needs jurisdiction-specific succession analysis."), ("California Code of Civil Procedure section 1582", "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1582.", "Check current restrictions before offering a compensated custodial-property recovery agreement.")]),
]


def compute_manuscript_word_count(chapters: list[dict] | None) -> int:
    """Compute prose word count across chapter content, excluding IDs and URLs."""
    import re

    def prose_words(value):
        if isinstance(value, str):
            return len(re.findall(r"\b[\w]+(?:['-][\w]+)*\b", value))
        if isinstance(value, (list, tuple)):
            return sum(prose_words(item) for item in value)
        if isinstance(value, dict):
            excluded = {"id", "chapter_id", "slug", "diagram_id", "layout_template", "epistemic_status",
                        "source_type", "url", "video_id", "timestamp_label", "markdown"}
            return sum(prose_words(item) for key, item in value.items() if key not in excluded)
        return 0

    return sum(
        prose_words({key: chapter.get(key) for key in (
            "title", "subtitle", "executive_summary", "key_metrics", "sections", "pull_quote",
            "action_checklist", "statutory_citations", "source_citations")})
        for chapter in (chapters or []) if isinstance(chapter, dict)
    )


def build_volume_001_manuscript(abridged_videos: list[dict] | None = None) -> dict:
    """Build an isolated manuscript with matched, attributed video references.

    Video commentary is not statutory authority. Untimed or unmatchable tips are
    omitted rather than assigned invented timestamps or unrelated chapter claims.
    """
    import math
    import re
    from urllib.parse import parse_qs, urlparse

    chapters = deepcopy(CHAPTERS_1_TO_6 + CHAPTERS_7_TO_12)
    for ch in chapters:
        ch.setdefault("id", f"Q{ch['chapter_number']}")
        ch.setdefault("chapter_id", f"Q{ch['chapter_number']}")
    keywords = {
        1: {"probate", "intestacy", "heir", "hunting", "surplus"},
        2: {"payer", "custodian", "fiduciary", "capital", "assets"},
        3: {"fee", "fees", "contingency", "economics", "profit", "margin", "cashflow"},
        4: {"startup", "budget", "tools", "demand", "validate", "insurance"},
        5: {"lien", "liens", "medicaid", "merp", "insolvent", "insolvency", "triage"},
        6: {"leads", "opportunities", "prospecting", "outreach", "docket"},
    }

    def seconds_of(value):
        if value is None or isinstance(value, bool):
            return None
        try:
            if isinstance(value, str) and ":" in value:
                parts = value.strip().strip("[]").split(":")
                if len(parts) not in (2, 3):
                    return None
                parts = [float(part) for part in parts]
                if any(not math.isfinite(part) or part < 0 for part in parts):
                    return None
                if any(part >= 60 for part in parts[1:]):
                    return None
                seconds = sum(part * 60 ** index for index, part in enumerate(reversed(parts)))
            else:
                seconds = float(value)
            return int(seconds) if math.isfinite(seconds) and seconds >= 0 else None
        except (ValueError, TypeError, OverflowError):
            return None

    for chapter in chapters:
        chapter["source_citations"] = []
    for video in abridged_videos or []:
        if not isinstance(video, dict):
            continue
        video_id = str(video.get("video_id") or "")
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
            try:
                parsed = urlparse(str(video.get("url") or video.get("video_url") or ""))
                host = (parsed.hostname or "").lower()
                if host in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
                    video_id = parse_qs(parsed.query).get("v", [""])[0]
                    if not video_id and parsed.path.startswith(("/shorts/", "/embed/", "/live/")):
                        video_id = parsed.path.split("/")[2]
                elif host == "youtu.be":
                    video_id = parsed.path.strip("/").split("/")[0]
            except ValueError:
                continue
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
            continue
        tips = []
        for key in ("pro_tips", "tips", "key_points"):
            items = video.get(key)
            if isinstance(items, list):
                tips.extend(items)
        for tip in tips:
            if not isinstance(tip, dict):
                continue
            text = str(tip.get("text") or tip.get("tip") or tip.get("summary") or "").strip()
            seconds = None
            for key in ("timestamp", "start", "start_seconds", "timestamp_seconds"):
                seconds = seconds_of(tip.get(key))
                if seconds is not None:
                    break
            if not text or seconds is None:
                continue
            explicit = tip.get("chapter_number", tip.get("question_number"))
            if explicit is not None:
                explicit = str(explicit).upper().removeprefix("Q")
            tokens = set(re.findall(r"[a-z]+", text.lower()))
            scores = []
            for chapter in chapters:
                number = chapter["chapter_number"]
                chapter_tokens = set(re.findall(r"[a-z]+", str(chapter.get("title", "")).lower()))
                chapter_tokens -= {"the", "a", "an", "is", "to", "of", "and", "in", "for", "what", "how", "your", "with", "who", "why", "where"}
                scores.append((len(tokens & (keywords.get(number, set()) | chapter_tokens)), number))
            best_score = max((score for score, number in scores), default=0)
            targets = ({number for score, number in scores if str(number) == explicit}
                       if explicit is not None else {number for score, number in scores if score == best_score and score > 0})
            label = f"{seconds // 3600:02d}:{seconds % 3600 // 60:02d}:{seconds % 60:02d}"
            url = f"https://www.youtube.com/watch?v={video_id}&t={seconds}s"
            citation = dict(source_type="video_pro_tip", video_id=video_id,
                            title=str(video.get("title") or video_id), text=text,
                            timestamp=seconds, timestamp_seconds=seconds, timestamp_label=f"[{label}]",
                            url=url, markdown=f"[{label}]({url})", epistemic_status="attributed_practitioner_claim",
                            relevance="Matched source commentary; not independent verification or legal authority.")
            for chapter in chapters:
                if chapter["chapter_number"] in targets:
                    existing = chapter["source_citations"]
                    if not any(item["url"] == url and item["text"] == text for item in existing):
                        existing.append(deepcopy(citation))

    total_words = compute_manuscript_word_count(chapters)
    return {
        "volume_id": "vol-001-heir-hunting", "volume_number": "001",
        "series_title": "THE BIG MONEY PLAYBOOKS", "parent_brand": "THE FUCK YOU MONEY CLUB",
        "tagline": "Big Money. Small Teams. No Bullshit.", "title": "HEIR HUNTING",
        "subtitle": "The Complete Playbook for Finding Missing Heirs, Researching Unclaimed Estates & Building a Probate Research Business",
        "positioning_alternatives": [
            {"title": "The Probate Research Operator", "subtitle": "Build documented kinship cases, not inheritance promises.",
             "audience": "Researchers building a narrow probate service", "research_basis": "State-law succession makes evidence and jurisdictional scope central to a defensible service.",
             "sources": ["https://www.law.cornell.edu/wex/intestacy"], "validation_status": "Source-informed editorial positioning; not market-tested."},
            {"title": "Evidence Before Inheritance", "subtitle": "A risk-first guide to finding heirs and screening estates.",
             "audience": "Operators who need stronger liability and solvency triage", "research_basis": "Federal Medicaid recovery provisions demonstrate why gross estate value cannot stand in for distributable value.",
             "sources": ["https://www.law.cornell.edu/uscode/text/42/1396p"], "validation_status": "Source-informed editorial positioning; not market-tested."},
            {"title": "The Missing-Heir Research Desk", "subtitle": "A small-team workflow from public records to reviewable proof.",
             "audience": "Genealogists developing a professional research workflow", "research_basis": "Intestacy identifies heirs under state law; positioning around sourced relationship research avoids promising a legal distribution result.",
             "sources": ["https://www.law.cornell.edu/wex/intestacy"], "validation_status": "Source-informed editorial positioning; not market-tested."},
        ],
        "epistemic_framework": [
            {"tier": 1, "tag": "statutory_fact", "label": "Primary legal authority", "standard": "Read the cited current law and applicable state implementation; citations are not individualized legal advice. California links are reference pointers, not certification of current text."},
            {"tier": 2, "tag": "attributed_practitioner_claim", "label": "Attributed source commentary", "standard": "Timestamped pro-tips identify who said what; they do not establish consensus or verify a legal or earnings claim."},
            {"tier": 3, "tag": "operating_framework", "label": "Editorial operating guidance", "standard": "Recommended controls and workflows require local adaptation and pilot validation; they are not measured industry norms."},
            {"tier": 4, "tag": "illustrative_model", "label": "Explicit hypothetical", "standard": "Invented budgets, conversion counts and fee examples explain mechanics, not actual market performance, legal ceilings or guaranteed results."},
        ],
        "total_word_count": total_words, "chapter_count": len(chapters), "chapters": chapters,
    }
