from __future__ import annotations

VOLUME_011_SUBTITLE = (
    "The Complete Playbook for $100,000–$1,000,000 USD in Annual Retained "
    "Commissions: A 1 FT + 3 C (4-Person) Core Pod, Scaling to Six"
)

VOLUME_011_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Control-Sale Mandate Desk",
        "subtitle": (
            "Build exclusive owner-exit mandates, qualify controlling buyers, "
            "and earn retained commissions on completed private-company sales."
        ),
        "audience": (
            "Experienced sector operators and transaction advisers serving "
            "privately held businesses with identifiable strategic buyers."
        ),
        "research_basis": (
            "15 U.S.C. 78o(b)(13) provides a conditional federal registration "
            "exemption for qualifying M&A brokers, not a universal permission "
            "to arrange securities transactions. Scope each engagement against "
            "eligible-company requirements, buyer control and active management, "
            "prohibited activities, disqualifications, and applicable state rules. "
            "The exemption does not remove securities antifraud duties. Exclusive "
            "mandates should define commission triggers, excluded buyers, tail "
            "periods, disclosure responsibilities, and settlement instructions."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/78o",
            "https://www.ecfr.gov/current/title-17/section-240.10b-5",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Verified Equipment Transaction Desk",
        "subtitle": (
            "Match specialist machinery buyers with documented sellers, "
            "resolve liens, and close asset-only transactions through escrow."
        ),
        "audience": (
            "Industrial equipment specialists with inspection expertise, "
            "repeat buyer relationships, and access to independent settlement providers."
        ),
        "research_basis": (
            "UCC 9-315 explains when a security interest continues after an "
            "asset disposition; UCC 9-513 addresses termination statements. "
            "The operating edge is a verified equipment schedule, inspection "
            "record, seller authority, lien search, and secured-party release "
            "package. Apply the governing state's enacted UCC provisions and "
            "any asset-specific title or dealer rules. A sale invoice alone "
            "does not establish that secured interests have been discharged."
        ),
        "sources": [
            "https://www.law.cornell.edu/ucc/9/9-315",
            "https://www.law.cornell.edu/ucc/9/9-513",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Licensed Business-Opportunity Specialist",
        "subtitle": (
            "Operate a narrow California business-sale desk with documented "
            "agency authority, verified buyer capacity, and independent escrow."
        ),
        "audience": (
            "California real estate brokers and properly supervised teams "
            "specializing in business opportunities within a defined industry."
        ),
        "research_basis": (
            "California Business and Professions Code sections 10130 and "
            "10131 establish licensing requirements and include specified "
            "business-opportunity brokerage activities. Section 10145 addresses "
            "handling money belonging to others. These provisions support a "
            "license-led operating model; they do not establish buyer demand "
            "or clear a securities transaction under federal or state law. "
            "Classify the actual transaction before accepting the mandate."
        ),
        "sources": [
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?lawCode=BPC&sectionNum=10130."
            ),
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?lawCode=BPC&sectionNum=10131."
            ),
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?lawCode=BPC&sectionNum=10145."
            ),
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_011_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-exclusive-mandate-to-settlement",
            "process_flow",
            "Earn the Commission Through Five Controlled Handoffs",
            "Exclusive authority, verified counterparties, and documented settlement.",
            1,
            "operating_framework",
            (
                "Applies to specialist asset and private-company transactions "
                "after jurisdiction and license review. Annual revenue means "
                "retained transaction commissions, never underlying asset value, "
                "buyer deposits, or escrow principal. First-deal timing is "
                "3–12 months; the workflow is not a one-month closing forecast."
            ),
            (
                "Each handoff requires a named owner and a complete evidence "
                "packet. Automation moves records and reminders; accountable "
                "people verify authority, representations, and closing conditions."
            ),
            [
                (
                    "Classify and mandate",
                    "Execute scoped exclusive authority before marketing the asset.",
                    1.0,
                    (
                        "The principal confirms transaction form, operating "
                        "jurisdictions, license requirements, seller authority, "
                        "commission basis, exclusivity, excluded buyers, and "
                        "tail provisions. Reject unsupported ownership claims "
                        "before signing an engagement."
                    ),
                ),
                (
                    "Build the evidence room",
                    "Reconcile seller claims against indexed supporting records.",
                    2.0,
                    (
                        "The document contractor assembles ownership records, "
                        "operating statements, material contracts, asset lists, "
                        "and lien information in SharePoint. Restrict access "
                        "by role and record every material correction."
                    ),
                ),
                (
                    "Match and qualify",
                    "Introduce authorized buyers with verified capacity and fit.",
                    3.0,
                    (
                        "Use HubSpot sector tags and Airtable buyer criteria "
                        "to shortlist counterparties. Confirm decision authority, "
                        "funding evidence, acquisition criteria, and confidentiality "
                        "terms before releasing sensitive seller materials."
                    ),
                ),
                (
                    "Negotiate and diligence",
                    "Track signed terms, exceptions, and unresolved closing conditions.",
                    4.0,
                    (
                        "The principal leads commercial negotiations while "
                        "independent counsel handles transaction documents. Track "
                        "LOI terms, diligence exceptions, lender dependencies, "
                        "secured-party releases, and deadlines in a milestone register."
                    ),
                ),
                (
                    "Settle and reconcile",
                    "Release the earned commission through documented settlement instructions.",
                    5.0,
                    (
                        "An independent escrow provider handles transaction "
                        "funds. Verify changed payment instructions through a "
                        "known telephone contact, reconcile the closing statement, "
                        "and record only the operator's retained commission."
                    ),
                ),
            ],
        ),
        (
            "diag-02-annual-mandate-conversion-funnel",
            "funnel",
            "Ten Closings From One Tracked Annual Cohort",
            "A mature pipeline illustration supporting $550,000 in retained commissions.",
            6,
            "illustrative_model",
            (
                "The five stages are nested counts from the same 200-owner "
                "cohort, observed across its complete sales cycle. They are "
                "planning assumptions, not measured conversion benchmarks. "
                "Ten completed transactions at $55,000 retained commission "
                "each produce the canonical $550,000 Base-Case annual revenue. "
                "A steady-state annual pipeline can contain overlapping cohorts."
            ),
            (
                "Stage conversions are 50%, 40%, 50%, and 50%; overall "
                "owner-to-close conversion is 5%. Deduplicate seller mandates "
                "rather than counting multiple buyer conversations as separate deals."
            ),
            [
                (
                    "Relevant owner accounts",
                    "200 screened owners with a documented transaction thesis.",
                    200.0,
                    (
                        "Research owners inside one specialist sector and "
                        "record a plausible sale trigger, asset profile, "
                        "decision-maker, and permitted contact channel. Purchased "
                        "contact volume alone does not qualify an account."
                    ),
                ),
                (
                    "Qualified seller discussions",
                    "100 owners confirm authority, motivation, timing, and fit.",
                    100.0,
                    (
                        "Fifty percent of the screened cohort completes a "
                        "substantive discussion. Capture valuation expectations, "
                        "records availability, ownership structure, and willingness "
                        "to disclose defects before offering representation."
                    ),
                ),
                (
                    "Executed exclusive mandates",
                    "40 sellers execute scoped mandates with workable fee terms.",
                    40.0,
                    (
                        "Forty percent of qualified discussions becomes an "
                        "exclusive engagement. Record fee triggers, buyer exclusions, "
                        "conflicts, termination rights, and tail dates; an unsigned "
                        "proposal remains outside the mandate count."
                    ),
                ),
                (
                    "Signed transaction LOIs",
                    "20 mandated sellers reach documented preliminary transaction terms.",
                    20.0,
                    (
                        "Half the executed mandates reaches a signed LOI "
                        "with a qualified buyer. Count each seller mandate "
                        "once, even if a replacement buyer later signs another "
                        "LOI after the first transaction fails."
                    ),
                ),
                (
                    "Completed commission events",
                    "10 closings earn $55,000 each in retained commissions.",
                    10.0,
                    (
                        "Half the LOI-stage mandates closes. An illustrative "
                        "$1,100,000 asset price at a 5% retained commission "
                        "produces $55,000; the resulting $11,000,000 aggregate "
                        "asset value is excluded from operator revenue."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-commission-waterfall",
            "waterfall",
            "$550,000 Revenue to $206,250 Owner Net",
            "Four expense deductions reconcile exactly to the 37.5% Base-Case margin.",
            3,
            "illustrative_model",
            (
                "USD annually. Opening revenue and closing profit are absolute "
                "total bars; the four intervening bars are signed deductions. "
                "The expense allocation is editorial, while scenario totals "
                "are canonical. Conservative: $100,000 revenue, 25% margin, "
                "$25,000 owner net, 1 FT + 3 C. Base: $550,000 revenue, "
                "37.5% margin, $206,250 owner net, 1 FT + 3 C. Scaled: "
                "$1,000,000 revenue, 50% margin, $500,000 owner net, 2 FT + 4 C."
            ),
            (
                "$550,000 - $150,000 - $108,000 - $60,000 - $25,750 "
                "= $206,250. Total expenses are $343,750, or 62.5% of "
                "retained commissions. Owner net is modeled before personal "
                "income taxes; owner draws are not a second expense."
            ),
            [
                (
                    "Retained commission revenue",
                    "$550,000 earned from ten completed commission events.",
                    550000.0,
                    (
                        "Opening total equals ten closings multiplied by "
                        "$55,000 retained commission. Outside-broker shares "
                        "are excluded before this revenue basis is measured; "
                        "escrow principal and asset purchase prices never enter it."
                    ),
                ),
                (
                    "Deal-specific delivery costs",
                    "Deduct $150,000 for externally purchased transaction support.",
                    -150000.0,
                    (
                        "Budget $15,000 per closing-equivalent for specialist "
                        "inspection, transaction support, travel, and diligence. "
                        "The annual allocation includes work on failed deals. "
                        "Vendors are purchased services, not additional pod seats."
                    ),
                ),
                (
                    "Three contractor seats",
                    "Deduct $108,000 across three defined contractor scopes.",
                    -108000.0,
                    (
                        "Allocate $36,000 annually to each core contractor "
                        "scope: research, documents, and transaction coordination. "
                        "These are budgeted service scopes rather than three "
                        "full-time employee salaries; classification follows actual work arrangements."
                    ),
                ),
                (
                    "Core operating overhead",
                    "Deduct $60,000 for systems, prospecting, and administration.",
                    -60000.0,
                    (
                        "Allocate $5,000 monthly to CRM, secure document "
                        "storage, sector data, prospecting, bookkeeping, and "
                        "administration. Combined with $9,000 monthly contractor "
                        "spend, recurring modeled overhead is $14,000 monthly."
                    ),
                ),
                (
                    "Insurance and dispute expense",
                    "Deduct $25,750 for coverage and modeled dispute costs.",
                    -25750.0,
                    (
                        "Include transaction-services coverage, deductibles, and "
                        "dispute-resolution costs as annual modeled expenses. "
                        "This line is not an escrow balance or a cash "
                        "reserve transfer. Avoid duplicating deal-specific delivery costs."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$206,250 remains after all four modeled expense categories.",
                    206250.0,
                    (
                        "Closing total equals $550,000 multiplied by 37.5%. "
                        "The full-time principal receives the residual owner "
                        "economics; no separate principal salary is deducted "
                        "in this illustrative owner-operated expense bridge."
                    ),
                ),
            ],
        ),
        (
            "diag-04-specialist-retained-fee-yields",
            "horizontal_bars",
            "Compare Retained Fees, Not Asset Prices",
            "Five independent commission illustrations per $1,000,000 of closed asset value.",
            2,
            "illustrative_model",
            (
                "Numeric bars show retained commission dollars on a common "
                "$1,000,000 underlying transaction denominator. Rates are "
                "negotiated planning assumptions, not published market averages "
                "or promised yields. Bars are alternatives, not components "
                "of the Base-Case revenue model. All examples assume no "
                "outside-broker share and no separately modeled settlement charge."
            ),
            (
                "Choose a niche using accessible mandates, required licenses, "
                "diligence workload, and closing probability. A higher fee rate "
                "can still produce weaker annual economics if transactions stall."
            ),
            [
                (
                    "Operating-business asset sale",
                    "$50,000 retained at an illustrative five-percent fee.",
                    50000.0,
                    (
                        "A negotiated 5% commission on a $1,000,000 asset "
                        "sale yields $50,000. Validate business-opportunity "
                        "licensing where applicable; use independent escrow "
                        "and resolve purchase-price allocation before settlement."
                    ),
                ),
                (
                    "Private-company control sale",
                    "$30,000 retained at an illustrative three-percent fee.",
                    30000.0,
                    (
                        "A negotiated 3% commission on a $1,000,000 control "
                        "transaction yields $30,000. Document securities "
                        "registration or exemption analysis, buyer control, "
                        "active management, and settlement without broker custody."
                    ),
                ),
                (
                    "Industrial real property",
                    "$25,000 retained at an illustrative two-and-a-half-percent fee.",
                    25000.0,
                    (
                        "A negotiated 2.5% commission on a $1,000,000 property "
                        "sale yields $25,000. Perform brokerage through the "
                        "required licensed structure and route proceeds through "
                        "the designated title or escrow closing provider."
                    ),
                ),
                (
                    "Specialist production equipment",
                    "$20,000 retained at an illustrative two-percent fee.",
                    20000.0,
                    (
                        "A negotiated 2% commission on a $1,000,000 equipment "
                        "package yields $20,000. Match serial numbers to "
                        "inspection reports, search applicable lien records, "
                        "and obtain secured-party releases tied to settlement."
                    ),
                ),
                (
                    "Commercial aircraft asset",
                    "$15,000 retained at an illustrative one-and-a-half-percent fee.",
                    15000.0,
                    (
                        "A negotiated 1.5% commission on a $1,000,000 aircraft "
                        "sale yields $15,000. Use aviation-specific title and "
                        "escrow expertise, verify recorded interests and "
                        "maintenance records, and resolve applicable registration requirements."
                    ),
                ),
            ],
        ),
        (
            "diag-05-statutory-and-settlement-decision-tree",
            "decision_tree",
            "Four Checks Before a Mandate Becomes Executable",
            "Each unresolved branch returns the transaction for correction or rejection.",
            5,
            "operating_framework",
            (
                "Stage numbers identify sequential decision nodes, not risk "
                "scores. At each node, a documented pass advances to the "
                "next check; an unresolved result stops the affected activity. "
                "Apply current law to the transaction's actual jurisdictions "
                "and structure. An NCNDA cannot substitute for a required license."
            ),
            (
                "Record the evidence, reviewer, date, and resulting action "
                "for every node. Recheck after a switch from an asset sale "
                "to an equity sale, a new buyer, or changed payment instructions."
            ),
            [
                (
                    "Asset and license classification",
                    "Proceed only after identifying the asset and required authority.",
                    1.0,
                    (
                        "Identify asset versus securities transfers and every "
                        "relevant jurisdiction. California BPC 10130 and 10131 "
                        "cover specified real-property and business-opportunity "
                        "brokerage activities. If required authority is absent, "
                        "stop brokerage activity until an appropriate structure exists."
                    ),
                ),
                (
                    "Securities route and exclusions",
                    "Proceed only with a documented registration or exemption route.",
                    2.0,
                    (
                        "For securities transactions, test 15 U.S.C. "
                        "78o(b)(13), including current eligible-company limits, "
                        "buyer control, active management, prohibited activities, "
                        "and disqualifications. Required dual-representation "
                        "disclosure and written consent must be documented. "
                        "An asset-only conclusion requires its own recorded basis."
                    ),
                ),
                (
                    "Authority, claims, and title",
                    "Proceed only with supported representations and releasable interests.",
                    3.0,
                    (
                        "Verify signatory authority, agency disclosures, conflicts, "
                        "and evidence behind material claims. For securities, "
                        "17 CFR 240.10b-5 addresses deceptive statements and "
                        "omissions. For secured assets, apply enacted UCC "
                        "9-315 and 9-513. Scope NCNDA introductions, exclusions, "
                        "duration, and remedies without treating the document as automatic protection."
                    ),
                ),
                (
                    "Funds and release instructions",
                    "Proceed only through verified settlement and permitted funds handling.",
                    4.0,
                    (
                        "Use independent escrow and known-contact callbacks "
                        "for payment changes. The M&A exemption under "
                        "15 U.S.C. 78o(b)(13) excludes specified custody "
                        "activities. California BPC 10145 governs covered "
                        "broker trust-money handling. If release instructions "
                        "conflict, freeze disbursement and obtain corrected instructions."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-person-core-pod",
            "org_architecture",
            "One Principal, Three Bounded Contractor Scopes",
            "The Base pod has four people; the Scaled pod expands to six.",
            11,
            "operating_framework",
            (
                "Each stage represents one core person: 1 FT + 3 C. "
                "Conservative and Base retain this four-person structure; "
                "Scaled uses 2 FT + 4 C by adding one full-time execution "
                "lead and one contractor for buyer research. Contractor "
                "status depends on actual working conditions and applicable law."
            ),
            (
                "The principal owns mandates, negotiations, and commercial "
                "decisions. Automation handles matching suggestions, milestone "
                "alerts, and document completeness checks, never substantive "
                "verification or unattended movement of client funds."
            ),
            [
                (
                    "Principal and mandate owner",
                    "One full-time operator owns representation and commercial decisions.",
                    1.0,
                    (
                        "Qualify sellers, confirm the permitted brokerage "
                        "scope, sign engagements, negotiate commercial terms, "
                        "and resolve conflicts. Maintain the cash forecast "
                        "and capacity plan. Scaled adds a full-time execution "
                        "lead rather than silently overloading this seat."
                    ),
                ),
                (
                    "Buyer and seller researcher",
                    "One contractor maintains evidence-backed prospect and buyer records.",
                    1.0,
                    (
                        "Maintain HubSpot records, Airtable matching criteria, "
                        "ownership research, buyer capacity evidence, and "
                        "suppression lists. The Base allocation is $36,000 "
                        "annually for the defined scope. Scaled adds another "
                        "research contractor to increase qualified coverage."
                    ),
                ),
                (
                    "Document and diligence coordinator",
                    "One contractor keeps the evidence room complete and controlled.",
                    1.0,
                    (
                        "Maintain SharePoint permissions, document indexes, "
                        "version history, request lists, and discrepancy logs. "
                        "Escalate contradictory seller statements rather than "
                        "editing them into consistency. The Base allocation "
                        "is $36,000 annually for this service scope."
                    ),
                ),
                (
                    "Transaction milestone coordinator",
                    "One contractor tracks dependencies through independent escrow settlement.",
                    1.0,
                    (
                        "Maintain deadlines, counsel requests, inspection "
                        "dependencies, secured-party releases, and closing "
                        "checklists. Prepare reconciliations without controlling "
                        "client funds. The Base allocation is $36,000 annually; "
                        "counsel and escrow providers remain external vendors."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "A $60,000 Launch Budget Inside the Canonical Range",
            "Four distinct buckets within the $15,000–$100,000 USD startup envelope.",
            4,
            "illustrative_model",
            (
                "Numeric values are USD capital allocations totaling $60,000; "
                "they are not four expense deductions from the annual scorecard. "
                "The startup range is $15,000–$100,000, monthly operating "
                "expense range is $3,000–$18,000, and first-deal timing is "
                "3–12 months. Cash reserved for runway is not itself an expense."
            ),
            (
                "$12,000 + $8,000 + $15,000 + $25,000 = $60,000. "
                "The $25,000 runway bucket covers about 8.3 months at "
                "$3,000 monthly, but only 1.8 months at the modeled "
                "$14,000 Base recurring burn. Do not deploy Base spending "
                "before the cash plan can support delayed closings."
            ),
            [
                (
                    "Authority and engagement setup",
                    "$12,000 establishes the scoped operating and contracting structure.",
                    12000.0,
                    (
                        "Fund jurisdiction-specific license analysis, required "
                        "applications, engagement drafting, agency disclosures, "
                        "insurance setup, and escrow-provider onboarding. Confirm "
                        "actual requirements before allocating money to promotion "
                        "for a service the operator cannot yet perform."
                    ),
                ),
                (
                    "Data room and operating systems",
                    "$8,000 establishes secure records and repeatable transaction workflows.",
                    8000.0,
                    (
                        "Configure HubSpot, Airtable, SharePoint, access controls, "
                        "backup procedures, templates, and electronic signatures. "
                        "Separate initial setup from recurring subscriptions; "
                        "each paid invoice belongs once in the cash ledger "
                        "and receives appropriate accounting treatment."
                    ),
                ),
                (
                    "Sector research and mandate acquisition",
                    "$15,000 funds a bounded specialist-market acquisition program.",
                    15000.0,
                    (
                        "Purchase targeted sector data, conduct owner "
                        "research, prepare evidence-led outreach, and attend "
                        "selected industry meetings. Release spend in measured "
                        "batches based on qualified discussions and signed "
                        "mandates rather than raw contact counts."
                    ),
                ),
                (
                    "Uncommitted operating runway",
                    "$25,000 remains available for lean operations and closing delays.",
                    25000.0,
                    (
                        "Keep this bucket liquid and separate from client "
                        "funds. Twelve months at the $3,000 monthly floor "
                        "requires $36,000 before additional deal costs; this "
                        "allocation therefore requires lower deployment, added "
                        "capital, or an explicit pause plan for a prolonged delay."
                    ),
                ),
            ],
        ),
        (
            "diag-08-first-thirty-days-roadmap",
            "timeline_roadmap",
            "Thirty Days to a Documented Brokerage Operating System",
            "Build executable mandates and pipeline evidence, not an invented first-month close.",
            12,
            "operating_framework",
            (
                "Numeric values are cumulative milestone days: 7, 14, 21, "
                "and 30. Work begins only within an authorized service "
                "scope. Licensing, seller readiness, and diligence can extend "
                "the schedule. The canonical first-deal window remains "
                "3–12 months; these milestones do not forecast commission receipts."
            ),
            (
                "End the sprint with an auditable mandate process, qualified "
                "counterparty records, a tested document workflow, and a "
                "cash plan that survives missed closing dates."
            ),
            [
                (
                    "Days 1-7",
                    "Define the niche, permitted activities, and cash constraints.",
                    7.0,
                    (
                        "Select one asset category and operating jurisdiction; "
                        "document license and securities analysis, excluded "
                        "activities, escrow arrangements, and a 13-week cash "
                        "forecast. Complete the four statutory and risk checks "
                        "before launching brokerage outreach."
                    ),
                ),
                (
                    "Days 8-14",
                    "Install the mandate packet and controlled evidence workflow.",
                    14.0,
                    (
                        "Prepare the exclusive engagement, scoped NCNDA, "
                        "agency disclosures, seller questionnaire, buyer "
                        "qualification checklist, and document index. Configure "
                        "HubSpot stages and SharePoint access, then test "
                        "a sample record without real client funds."
                    ),
                ),
                (
                    "Days 15-21",
                    "Run a bounded owner-research and buyer-matching pilot.",
                    21.0,
                    (
                        "Research 25 relevant owners and 15 plausible "
                        "buyers as activity targets, not conversion promises. "
                        "Log authority, sector fit, acquisition criteria, "
                        "contact permissions, and evidence gaps. Review "
                        "qualified conversations before expanding outreach spend."
                    ),
                ),
                (
                    "Days 22-30",
                    "Audit the pilot and rehearse a failed-closing response.",
                    30.0,
                    (
                        "Review actual mandate progress, reconcile the cash "
                        "ledger, and test document retrieval, milestone alerts, "
                        "payment-change callbacks, and a canceled transaction. "
                        "Assign remediation owners and revise the next "
                        "30-day work plan using observed conversion evidence."
                    ),
                ),
            ],
        ),
    ]
    return [
        dict(
            diagram_id=identifier,
            chart_type=kind,
            title=title,
            subtitle=subtitle,
            chapter_number=chapter,
            epistemic_tag=tag,
            assumptions_note=note,
            caption=caption,
            stages=[
                dict(
                    label=label,
                    value=value,
                    numeric_value=float(number),
                    detail=detail,
                )
                for label, value, number, detail in stages
            ],
        )
        for identifier, kind, title, subtitle, chapter, tag, note, caption, stages
        in specs
    ]
