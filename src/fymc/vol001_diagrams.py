__all__ = [
    "VOLUME_001_SUBTITLE",
    "build_volume_001_diagrams_data",
    "VOLUME_001_POSITIONING_ALTERNATIVES",
]

VOLUME_001_SUBTITLE: str = (
    "Trace the Family, Prove the Heir, Verify the Assets — "
    "Documented Kinship, Probate Discovery, Recovery Claims, and Curative Title"
)


def build_volume_001_diagrams_data() -> list[dict]:
    return [
        {
            "diagram_id": "diag-01-document-the-right-family",
            "chapter_number": 1,
            "title": "From Case Screening to Documented Kinship",
            "subtitle": "Check the opportunity before extending the family search.",
            "caption": (
                "Leslie Lawson recommends preliminary case screening; John and "
                "Char check funds and competing claims; HeirSearch and PBI "
                "Research Services describe kinship verification."
            ),
            "assumptions_note": (
                "Leslie Lawson, John and Char, HeirSearch, Daniel Curran, and "
                "PBI Research Services describe separate practices. This sequence "
                "combines those practices without implying a shared firm, fee "
                "model, or guaranteed recovery."
            ),
            "note": (
                "PBI Research Services reports finding at least one relative "
                "over 95% of the time, not proving every beneficiary's entitlement. "
                "Daniel Curran's charity-will example demonstrates that research "
                "can still be written off."
            ),
            "chart_type": "process_flow",
            "stages": [
                {
                    "step": "01",
                    "label": "Screen the assignment",
                    "value": "Step 1",
                    "detail": (
                        "Leslie Lawson recommends a preliminary hour to assess "
                        "whether the case fits the researcher's skills."
                    ),
                },
                {
                    "step": "02",
                    "label": "Confirm funds and case activity",
                    "value": "Step 2",
                    "detail": (
                        "John and Char visit the courthouse to check other "
                        "claimants and confirm that the money remains."
                    ),
                },
                {
                    "step": "03",
                    "label": "Resolve prior kin and any will",
                    "value": "Step 3",
                    "detail": (
                        "HeirSearch requires excluding living heirs at the prior "
                        "level before moving up the chart. Daniel Curran's cases "
                        "show how half siblings or a newly found will can "
                        "displace a wider-family search."
                    ),
                },
                {
                    "step": "04",
                    "label": "Corroborate each relationship",
                    "value": "Step 4",
                    "detail": (
                        "PBI Research Services marks a relationship possible "
                        "with one source and confirmed with two sources, "
                        "and adds a second reviewer."
                    ),
                },
                {
                    "step": "05",
                    "label": "Deliver the documented finding",
                    "value": "Step 5",
                    "detail": (
                        "Lawson uses reusable report and citation templates. "
                        "PBI Research Services supplies PDF and Excel reports "
                        "for reading, retention, and client-system use."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-02-research-tool-benchmarks",
            "chapter_number": 6,
            "title": "Research Settings Without Conversion Claims",
            "subtitle": (
                "Image quality, preservation access, planning size, "
                "and candidate similarity measure different things."
            ),
            "caption": (
                "Transkribus supplies the image recommendation; "
                "ScottishArchivesTV states the Fixity Pro trial period; "
                "Rebecca Coford supplies the planning examples; Johannes "
                "demonstrates the Neo4j similarity threshold."
            ),
            "assumptions_note": (
                "Transkribus, ScottishArchivesTV, Rebecca Coford, and Johannes "
                "report independent measures with different units. These are "
                "not successive populations, and their widths do not establish "
                "attrition or conversion. Coford's five and ten are alternative "
                "plan sizes, not a measured reduction."
            ),
            "note": (
                "Johannes calls 0.20 unusually low for the Neo4j demonstration. "
                "ScottishArchivesTV's trial duration is a tutorial-era product "
                "statement, not a research deadline."
            ),
            "chart_type": "funnel",
            "stages": [
                {
                    "label": "Recognition image resolution",
                    "value": 300,
                    "display": "300 DPI JPEGs",
                    "conversion": "Not a conversion measure",
                    "detail": (
                        "Transkribus recommends 300 DPI JPEGs in its introductory "
                        "tutorial while also accepting PNGs and PDFs."
                    ),
                },
                {
                    "label": "Preservation trial period",
                    "value": 30,
                    "display": "First 30 days free",
                    "conversion": "Not a conversion measure",
                    "detail": (
                        "ScottishArchivesTV states this Fixity Pro trial period "
                        "while demonstrating repeated checksum scans."
                    ),
                },
                {
                    "label": "Initial plan with ten ideas",
                    "value": 10,
                    "display": "10 research ideas",
                    "conversion": "Alternative planning example",
                    "detail": (
                        "Rebecca Coford describes a simple initial plan as "
                        "five or ten ideas because plans evolve."
                    ),
                },
                {
                    "label": "Initial plan with five ideas",
                    "value": 5,
                    "display": "5 research ideas",
                    "conversion": "Alternative planning example",
                    "detail": (
                        "Rebecca Coford emphasizes choosing records that answer "
                        "the research question, whether online or offline."
                    ),
                },
                {
                    "label": "Candidate similarity threshold",
                    "value": 0.20,
                    "display": "0.20 demonstration threshold",
                    "conversion": "Not an identity-confirmation rate",
                    "detail": (
                        "Johannes applies this threshold after multiplying "
                        "structural similarity by embedding cosine similarity "
                        "in the Neo4j example."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-03-record-access-cost-reference",
            "chapter_number": 3,
            "title": "Record Access and Escalation Costs",
            "subtitle": (
                "Keep a record lookup, a preliminary title search, "
                "and a probate proceeding financially distinct."
            ),
            "caption": (
                "GenealogyMagazine quotes ordinary courthouse copies; "
                "Matt Hecker on Logan Fullmer quotes Smart Skip; Seth on "
                "REtipster quotes portfolio-result viewing; Jamel Gibbs quotes "
                "preliminary title searches; Al Nicoletti on Courtney Fricke "
                "quotes a single probate."
            ),
            "assumptions_note": (
                "These GenealogyMagazine, Matt Hecker, Seth, Jamel Gibbs, and "
                "Al Nicoletti figures are independent US-dollar price references. "
                "Every bar is a standalone total, not a cumulative balance, "
                "deduction, or profit calculation. The title-search endpoints "
                "are alternatives within one quoted range."
            ),
            "note": (
                "GenealogyMagazine excludes vital records from its usual copy "
                "price and notes higher certification charges. Seth's surcharge "
                "applies upon viewing results. Nicoletti's approximately "
                "$4,000–$4,500 example is not a document-retrieval fee."
            ),
            "chart_type": "waterfall",
            "bars": [
                {
                    "label": "Smart Skip search",
                    "value": 0.15,
                    "display": "$0.15 per skip trace",
                    "kind": "total",
                },
                {
                    "label": "Portfolio-result viewing surcharge",
                    "value": 0.25,
                    "display": "$0.25 per record",
                    "kind": "total",
                },
                {
                    "label": "Ordinary courthouse copy",
                    "value": 1.00,
                    "display": "Usually $1.00 per page",
                    "kind": "total",
                },
                {
                    "label": "Preliminary title search lower quote",
                    "value": 100,
                    "display": "$100 lower endpoint",
                    "kind": "total",
                },
                {
                    "label": "Preliminary title search upper quote",
                    "value": 150,
                    "display": "$150 upper endpoint",
                    "kind": "total",
                },
                {
                    "label": "Single probate lower quote",
                    "value": 4000,
                    "display": "Approximately $4,000 lower endpoint",
                    "kind": "total",
                },
            ],
        },
        {
            "diagram_id": "diag-04-family-research-counts",
            "chapter_number": 2,
            "title": "Family Research Counts Are Not Entitlement Proof",
            "subtitle": (
                "Separate display depth, competing identities, "
                "located relatives, and signed beneficiaries."
            ),
            "caption": (
                "James Tanner demonstrates FamilySearch generations; "
                "Christa Cowen separates Daniel Jones identities; Heir Hunters "
                "reports the Victor and Wearing cases; Amy Moyes on Ancestry "
                "reports signed maternal heirs in the Eileen Holmes case."
            ),
            "assumptions_note": (
                "James Tanner, Christa Cowen, Heir Hunters, and Amy Moyes "
                "describe different units and cases. Equal minimum, maximum, "
                "and typical entries preserve each quoted count or ceiling; "
                "they do not assert a statistical distribution or typical "
                "case size."
            ),
            "note": (
                "Tanner's four generations are a display ceiling. "
                "Cowen's five men are competing identities, not heirs. "
                "Heir Hunters did not confirm the Wearing estate value, "
                "and Amy Moyes's eighteen signatures were a progress report."
            ),
            "chart_type": "horizontal_bars",
            "unit": "Reported count; the counted item is identified in each label",
            "bars": [
                {
                    "label": "FamilySearch generation display ceiling",
                    "min": 4,
                    "max": 4,
                    "typical": 4,
                    "display": "Up to 4 generations",
                },
                {
                    "label": "Distinct Daniel Jones identities",
                    "min": 5,
                    "max": 5,
                    "typical": 5,
                    "display": "5 men distinguished",
                },
                {
                    "label": "Victor estate heirs",
                    "min": 16,
                    "max": 16,
                    "typical": 16,
                    "display": "16 heirs sharing the reported estate",
                },
                {
                    "label": "Eileen Holmes signed maternal heirs",
                    "min": 18,
                    "max": 18,
                    "typical": 18,
                    "display": "18 signed so far",
                },
                {
                    "label": "Wearing investigation heirs",
                    "min": 53,
                    "max": 53,
                    "typical": 53,
                    "display": "53 heirs; estate value unconfirmed",
                },
            ],
        },
        {
            "diagram_id": "diag-05-resolve-identity-before-entitlement",
            "chapter_number": 5,
            "title": "Resolve Identity Before Asserting Entitlement",
            "subtitle": (
                "Separate candidates, test evidence, document uncertainty, "
                "and verify the economic premise."
            ),
            "caption": (
                "Christa Cowen on Ancestry separates namesakes; FamilySearch "
                "presenters distinguish negative evidence and require written "
                "conflict analysis; Katherine Moore separates genetic leads "
                "from confirmation; Heir Hunters illustrates unknown estate value."
            ),
            "assumptions_note": (
                "Christa Cowen, FamilySearch presenters, Katherine Moore, and "
                "Heir Hunters supply distinct checks. Genetic confirmation "
                "applies when genetic evidence is used; no DNA threshold "
                "automatically establishes identity or inheritance."
            ),
            "note": (
                "Katherine Moore's 228 cM match advanced an identification "
                "investigation but did not replace further testing and "
                "investigation. Heir Hunters' 53-heir Wearing case did not "
                "establish the estate's value."
            ),
            "chart_type": "decision_tree",
            "nodes": [
                {
                    "gate": "G1",
                    "question": (
                        "Have competing namesakes been separated through "
                        "relatives, places, chronology, and associated records?"
                    ),
                    "pass_next": "G2",
                    "fail_action": (
                        "Keep candidates separate and compare original images. "
                        "Cowen's five Daniel Joneses could not be distinguished "
                        "by their shared farming occupation."
                    ),
                },
                {
                    "gate": "G2",
                    "question": (
                        "Does each claimed absence concern information expected "
                        "in an extant source rather than only a failed search?"
                    ),
                    "pass_next": "G3",
                    "fail_action": (
                        "Record the unsuccessful search without treating it as "
                        "proof of absence, following the FamilySearch distinction."
                    ),
                },
                {
                    "gate": "G3",
                    "question": (
                        "Are conflicts written up and relevant genetic-tree "
                        "connections documented, with leads distinguished "
                        "from confirmatory identification?"
                    ),
                    "pass_next": "G4",
                    "fail_action": (
                        "Preserve provisional relationships, explain unresolved "
                        "conflicts, and obtain the further testing or "
                        "investigation Katherine Moore requires when applicable."
                    ),
                },
                {
                    "gate": "G4",
                    "question": (
                        "Has estate value been established separately "
                        "from the number of heirs?"
                    ),
                    "pass_next": (
                        "Evaluate the documented case without equating "
                        "heir count with recovery value."
                    ),
                    "fail_action": (
                        "Keep the value unconfirmed. Heir Hunters' Wearing "
                        "investigation and Katherine O'Connell's mineral-rights "
                        "case show why family size is not an earnings estimate."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-06-ownership-verification-coordination",
            "chapter_number": 11,
            "title": "Coordinate Family, Title, Debt, and Probate Evidence",
            "subtitle": "Inherited ownership and an insurable closing are different findings.",
            "caption": (
                "NOLA City Archives emphasizes the family tree; Eric Richardson "
                "searches owner-indexed liens; Jamel Gibbs distinguishes "
                "preliminary title work; Al Nicoletti checks probate and "
                "underwriting; housing and Farm Aid presenters address debt."
            ),
            "assumptions_note": (
                "NOLA City Archives, Eric Richardson, Jamel Gibbs, Al Nicoletti, "
                "Farm Aid, and National Housing Resource Center describe "
                "complementary responsibilities, not a shared organization. "
                "Headcount is unspecified, and the checks below are qualitative "
                "completion criteria rather than numerical performance targets."
            ),
            "note": (
                "Al Nicoletti warns that a proposed curative order may still "
                "fail underwriting. Farm Aid presenters distinguish taxes from "
                "foreclosure fees, and National Housing Resource Center "
                "presenters distinguish reverse mortgages from ordinary "
                "stay-and-pay situations."
            ),
            "chart_type": "org_architecture",
            "center": {
                "role": "Inherited-property case coordination",
                "headcount": "Not specified",
                "focus": (
                    "Bring the acquisition deed, complete family tree, debts, "
                    "property conditions, and proposed cure into the same "
                    "case assessment."
                ),
            },
            "spokes": [
                {
                    "role": "Family-history research",
                    "type": "Kinship evidence",
                    "kpi": (
                        "Family tree includes deceased siblings and their "
                        "children, following NOLA City Archives and Nicoletti's "
                        "warning about undisclosed relatives."
                    ),
                },
                {
                    "role": "Recorded-title research",
                    "type": "Deed and lien evidence",
                    "kpi": (
                        "Acquisition deed and owner-name searches are examined; "
                        "Richardson's lien search and Gibbs's preliminary "
                        "screening remain distinct from a full purchase search."
                    ),
                },
                {
                    "role": "Probate counsel and title underwriting",
                    "type": "Authority and insurability",
                    "kpi": (
                        "Nicoletti's proposed cure and complaint are put in "
                        "writing and checked for underwriting acceptance before "
                        "treating a probate order as closing-ready."
                    ),
                },
                {
                    "role": "Debt and property-condition assessment",
                    "type": "Financial and environmental exposure",
                    "kpi": (
                        "Tax recipient, payment status, foreclosure fees, "
                        "mortgage type, and environmental conditions are "
                        "examined before authorizing probate expenditure."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-07-separate-document-and-cure-costs",
            "chapter_number": 4,
            "title": "Separate Record Costs From Legal Cure Costs",
            "subtitle": "Different services carry different quoted costs and exclusions.",
            "caption": (
                "GenealogyMagazine quotes ordinary copies; Jamel Gibbs quotes "
                "preliminary title searches; Alex Goldovansky on Logan Fullmer "
                "quotes mortgage-release work; Al Nicoletti on Courtney Fricke "
                "quotes a single probate."
            ),
            "assumptions_note": (
                "GenealogyMagazine, Jamel Gibbs, Alex Goldovansky, and "
                "Al Nicoletti supply independent US-dollar price references. "
                "These are not components of a reported combined transaction "
                "budget and must not be summed into an asserted total."
            ),
            "note": (
                "Nicoletti explains that additional deceased owners and "
                "downstream estates multiply probate expense. Goldovansky "
                "notes lender-dependent difficulty and cases that cannot "
                "be resolved."
            ),
            "chart_type": "stacked_comparison",
            "total_range": (
                "No combined total reported; independent quoted prices in USD"
            ),
            "buckets": [
                {
                    "label": "Ordinary courthouse copy per page",
                    "low": 1.00,
                    "high": 1.00,
                    "notes": (
                        "GenealogyMagazine reports usually $1.00 per page, "
                        "except vital records; certification costs more."
                    ),
                },
                {
                    "label": "Preliminary professional title search",
                    "low": 100,
                    "high": 150,
                    "notes": (
                        "Jamel Gibbs gives this approximate provider-dependent "
                        "range for preliminary screening, not the full purchase "
                        "search and process."
                    ),
                },
                {
                    "label": "Mortgage-release work",
                    "low": 150,
                    "high": 175,
                    "notes": (
                        "Alex Goldovansky quotes this all-in range depending "
                        "on the lender; private creditors and deceased lenders "
                        "can be more difficult."
                    ),
                },
                {
                    "label": "Single probate proceeding",
                    "low": 4000,
                    "high": 4500,
                    "notes": (
                        "Al Nicoletti gives this approximate single-probate "
                        "example. Complete title and property investigation "
                        "before authorizing paid probate work."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-08-property-and-genealogy-work-plan",
            "chapter_number": 12,
            "title": "Property Identification to Documented Case Assessment",
            "subtitle": "Check coverage, inspect matches, retrieve evidence, and price the work.",
            "caption": (
                "Regrid demonstrators explain coverage and import checks; "
                "Seth on REtipster demonstrates ownership and document "
                "research; Amy Moyes tests heirship; Vanessa Bland explains "
                "the consequences of omitting business expenses."
            ),
            "assumptions_note": (
                "The week headings are planning slots, not elapsed times "
                "reported by Regrid, Seth, Amy Moyes, or Vanessa Bland. "
                "Certificates, retrieval, and case resolution may remain "
                "outstanding beyond these slots; no four-week completion "
                "promise is implied."
            ),
            "note": (
                "Regrid states a maximum 30-day sandbox token lifespan and "
                "limited trial coverage. Seth reports about 24–48 hours for "
                "abstractor document retrieval. Neither establishes an "
                "end-to-end heir-recovery timetable."
            ),
            "chart_type": "timeline_roadmap",
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Establish owner identity and coverage",
                    "deliverable": (
                        "Owner-name search and property references, with "
                        "Regrid trial counties and Seth's title-chain coverage "
                        "start dates checked."
                    ),
                    "gate": (
                        "Do not treat unavailable trial counties or records "
                        "before the report's start date as evidence of absence."
                    ),
                },
                {
                    "week": "Week 2",
                    "title": "Inspect parcel matches and owner duplicates",
                    "deliverable": (
                        "Reviewed import matches and a narrowed owner list "
                        "with duplicate owners removed, following Regrid "
                        "and Seth."
                    ),
                    "gate": (
                        "Inspect match results before Finish Import. Regrid's "
                        "accepted 97% example is not a universal acceptance "
                        "threshold."
                    ),
                },
                {
                    "week": "Week 3",
                    "title": "Retrieve documents and test family assertions",
                    "deliverable": (
                        "Retrieved ownership documents and a family-research "
                        "record that keeps outstanding certificates visible; "
                        "divide surname variants among colleagues as Amy Moyes "
                        "does with Gardner spellings."
                    ),
                    "gate": (
                        "Keep the possible-child question tied to certificate "
                        "evidence. Amy Moyes's cousin interview does not settle "
                        "whether wider relatives remain entitled."
                    ),
                },
                {
                    "week": "Week 4",
                    "title": "Assess service pricing and unresolved work",
                    "deliverable": (
                        "Expense-aware genealogy pricing and an assessment "
                        "that distinguishes signed beneficiaries from unresolved "
                        "document and entitlement questions."
                    ),
                    "gate": (
                        "Apply Vanessa Bland's lesson by including actual "
                        "business expenses rather than copying an employment "
                        "wage. Amy Moyes's 18 signed maternal heirs do not "
                        "replace outstanding evidence."
                    ),
                },
            ],
        },
    ]


VOLUME_001_POSITIONING_ALTERNATIVES: list[dict] = [
    {
        "title": "Prove the Family Before You Pursue the Estate",
        "subtitle": (
            "Documented descendancy, independent corroboration, "
            "and clear treatment of uncertain identities."
        ),
        "audience": (
            "Genealogists and probate researchers locating missing beneficiaries "
            "and documenting kinship for estate work."
        ),
        "research_basis": (
            "HeirSearch requires excluding prior levels of living heirs; "
            "PBI Research Services distinguishes possible and confirmed "
            "relationships; James Tanner requires sourced parent-child links; "
            "Christa Cowen separates namesakes; Leslie Lawson recommends "
            "reusable report and citation templates."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=aOXjjN53MT8&t=155s",
            "https://www.youtube.com/watch?v=rR4YCKGVNmg&t=585s",
            "https://www.youtube.com/watch?v=9Q4qYeK5DTg&t=404s",
            "https://www.youtube.com/watch?v=K6-4Y6O5bbQ&t=1425s",
            "https://www.youtube.com/watch?v=R5XtgGL0gkQ&t=2427s",
        ],
        "validation_status": (
            "Grounded strictly in Vol. 001 YouTube practitioner transcripts."
        ),
    },
    {
        "title": "From Missing Owner to Documented Claim",
        "subtitle": (
            "Qualify the funds, explain the evidence, collect the documents, "
            "and complete the correct claim submission."
        ),
        "audience": (
            "Deceased-owner and unclaimed-property recovery practitioners "
            "building jurisdiction-specific research and claimant support."
        ),
        "research_basis": (
            "Eric Richardson checks existing claims and liens and uses "
            "first-call proof rather than immediate closing; David Church "
            "collects complete document bundles; California's declaration "
            "tutorial distinguishes Property IDs; Ohio's presenters emphasize "
            "matching uploads to the correct Claim ID."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=FNbqvZGEzeE&t=168s",
            "https://www.youtube.com/watch?v=DMdtmrWAO6c&t=459s",
            "https://www.youtube.com/watch?v=1AMk1-SB5ic&t=56s",
            "https://www.youtube.com/watch?v=1ahhduhMdd0&t=85s",
            "https://www.youtube.com/watch?v=o1cc3hUtIv4&t=710s",
        ],
        "validation_status": (
            "Grounded strictly in Vol. 001 YouTube practitioner transcripts."
        ),
    },
    {
        "title": "Trace the Heirs, Underwrite the Cure",
        "subtitle": (
            "Connect family evidence, recorded ownership, property conditions, "
            "and title acceptance before committing to a deal."
        ),
        "audience": (
            "Curative-title practitioners and inherited-property researchers "
            "evaluating ownership problems and transaction feasibility."
        ),
        "research_basis": (
            "Courtney Fricke requires underwriting the cure; Logan Fullmer's "
            "wrong-heir reversal emphasizes exact identity and vesting; "
            "Al Nicoletti requires property investigation before probate "
            "filings and checks proposed orders against underwriting; "
            "Seth on REtipster checks title-report coverage."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=-QzABvCmtVc&t=348s",
            "https://www.youtube.com/watch?v=zMW-iFWYX9w&t=942s",
            "https://www.youtube.com/watch?v=pQwwvYbUYrU&t=229s",
            "https://www.youtube.com/watch?v=onebNbNQSBM&t=3711s",
            "https://www.youtube.com/watch?v=GfyX48eCbRY&t=162s",
        ],
        "validation_status": (
            "Grounded strictly in Vol. 001 YouTube practitioner transcripts."
        ),
    },
]
