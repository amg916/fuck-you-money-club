from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 1 FT + 3 C (4 people) contingent corporate bill-audit & tax-credit recovery team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Event Queues, Authorized FedEx/UPS Claims, Utility Meter OCR, Form 8850 Workflows, and Evidence-Led Partner Distribution",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #38, ranked #06 of 42 with a 94/100 Money-to-Manpower Score, "
        "turns corporate expense recovery into an evidence-processing operation rather "
        "than a document-chasing practice. This chapter maps 12 operator plays onto "
        "one permissioned pipeline: acquire records, normalize evidence, calculate "
        "eligibility, route exceptions, obtain human approval, and reconcile earned "
        "fees. Python workers handle repeatable transformations; language models "
        "extract and classify without deciding entitlement or transmitting claims. "
        "The target is 70%+ task automation measured against a fixed work inventory. "
        "Canonical annual owner profits remain $33,000 Conservative, $217,150 Base, "
        "and $504,000 Scaled. Distribution compounds through verified recovery "
        "examples, accountant referrals, ATS integrations, and narrowly targeted "
        "outreach, while source-linked review protects deadlines, client authority, "
        "and the distinction between client recoveries and operator revenue."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$110,000",
            "context": "Annual earned contingency, shared-savings, and processing revenue",
            "note": "30% net margin; $33,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$505,000",
            "context": "Annual earned contingency, shared-savings, and processing revenue",
            "note": "43.0% net margin; $217,150 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$900,000",
            "context": "Annual earned contingency, shared-savings, and processing revenue",
            "note": "56% net margin; $504,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build one evidence spine for twelve recovery plays",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a signed Letter of Authorization, a scoped service agreement, and an immutable baseline invoice snapshot before disclosing account-specific tariff or refund findings. "
                    "The owner controls engagement acceptance, pricing, and final release; three contractors own parcel analysis, utility and property research, and credentialed tax-credit work respectively, with external specialists added only through explicit scopes. "
                    "A Python intake service accepts authorized exports or signed webhooks and creates a tenant-scoped case identifier. "
                    "Use hashlib.sha256 for source fingerprints, decimal.Decimal for money, zoneinfo for local deadlines, and sqlite3 for a single-worker pilot ledger. "
                    "At higher concurrency, replace the pilot ledger with a transactional queue and database rather than sharing a writable file across machines. "
                    "Store originals separately from extracted fields; every amount needs document identifier, page or record location, currency, service period, account, and extraction version. "
                    "A language model receives only the minimum permitted document excerpt and returns constrained fields plus source locations. "
                    "It cannot authorize access, invent a tariff, determine tax eligibility, or release a filing. "
                    "Treat instructions embedded in invoices as untrusted document content. "
                    "The deterministic validator rejects missing provenance and arithmetic mismatches before the case reaches a specialist. "
                    "This spine makes automation transferable without confusing a faster extraction with a defensible recovery."
                ),
                (
                    "Use twelve explicitly named operating lanes, not twelve disconnected applications. "
                    "The first seven are parcel service-guarantee refunds, parcel invoice adjustments, utility tariff corrections, cooling-tower sewer credits, waste contract savings, telecom contract savings, and property-assessment appeals. "
                    "These are chapter-local mappings rather than invented identifiers from an external play catalog. "
                    "For service-guarantee work, forty accepted $20 refunds at a 35% fee generate $280 of operator revenue; the $800 refunded belongs to the client. "
                    "Twelve accepted $50 billing adjustments at the same percentage generate another $210, provided they are different charges. "
                    "A $2,000 utility recovery at 30% earns $600, while a $3,000 sewer credit earns $900. "
                    "Waste savings of $500 monthly produce $5,400 over thirty-six verified months at 30%; telecom savings of $400 monthly produce $4,320 over the same term. "
                    "Neither thirty-six-month total becomes immediate earned revenue merely because a contract is signed. "
                    "A permitted property appeal producing $10,000 of realized tax reduction supports a $2,500 fee at 25%, subject to the engagement and local licensing rules. "
                    "Version each baseline and exclude tax-rate changes, occupancy shifts, overlapping refunds, and unimplemented recommendations from credited savings. "
                    "The same source expense can support several diagnostic tests, but never multiple incompatible recovery invoices."
                ),
                (
                    "The remaining lanes are ATS-integrated WOTC processing, specialty-credit substantiation, b2b_class_action_contingency_recovery, duplicate vendor-payment recovery, and shared-savings verification servicing. "
                    "For WOTC, twenty completed, contractually billable processing cases at $100 produce $2,000; employer credits are separate and certification does not by itself establish the final credit amount. "
                    "Six specialty-credit evidence reviews at a fixed $250 produce $1,500 only when the contracted reviews are delivered. "
                    "Use that fixed-fee route where a proposed contingent tax arrangement is restricted; do not camouflage a credit-based fee as processing. "
                    "A verified $12,000 settlement distribution at 25% produces $3,000, and a recovered $4,000 duplicate payment at 25% produces $1,000. "
                    "Savings servicing on $1,000 of verified monthly savings at 30% generates $300 for that month. "
                    "When servicing implements an existing waste or telecom split, that $300 is the same revenue stream, not an additional charge. "
                    "All these figures are illustrative lane economics, not additive forecasts or replacements for the canonical scorecard. "
                    "The event envelope records lane, client authority, deadline, contractual fee basis, and overlapping-charge identifiers. "
                    "A routing rule then assigns the required credential and submission channel. "
                    "Unsupported channels fall back to documented manual processing; missing authority stops the case rather than prompting a worker to improvise access."
                ),
            ],
            "table": {
                "caption": "First Seven Play Mappings: Earned-Fee Arithmetic and Operating Fallbacks",
                "headers": [
                    "Mapped operating lane and source evidence",
                    "Illustrative units and operator revenue calculation",
                    "Repeatable automation with explicit evidence linkage",
                    "Failure fallback and accountable human decision",
                ],
                "rows": [
                    [
                        "Play 01 covers parcel service-guarantee refund recovery.",
                        "Forty accepted $20 refunds multiplied by 35% yield $280.",
                        "Join tracking events with purchased services and effective guarantee terms.",
                        "Carrier waivers or suspended guarantees require specialist exclusion before submission.",
                    ],
                    [
                        "Play 02 covers parcel invoice adjustment recovery.",
                        "Twelve accepted $50 adjustments multiplied by 35% yield $210.",
                        "Compare billed surcharges against contracted rates and package evidence.",
                        "Missing dimensions require original shipment records rather than estimated measurements.",
                    ],
                    [
                        "Play 03 covers commercial utility tariff correction.",
                        "A realized $2,000 utility refund multiplied by 30% yields $600.",
                        "Match account attributes against effective tariff schedules and rider dates.",
                        "Ambiguous service classifications require written utility clarification before filing.",
                    ],
                    [
                        "Play 04 covers cooling-tower sewer credit recovery.",
                        "A realized $3,000 sewer credit multiplied by 30% yields $900.",
                        "Reconcile approved deduct-meter readings with billing periods and local rules.",
                        "Unapproved meters require municipal acceptance before claiming eligible consumption.",
                    ],
                    [
                        "Play 05 covers verified waste contract savings.",
                        "Monthly $500 savings multiplied by 36 and 30% yield $5,400.",
                        "Compare normalized service frequency and container charges against baseline invoices.",
                        "Changed pickup volumes require baseline adjustment and documented client agreement.",
                    ],
                    [
                        "Play 06 covers verified telecom contract savings.",
                        "Monthly $400 savings multiplied by 36 and 30% yield $4,320.",
                        "Match circuit inventories against billing accounts and implemented cancellation dates.",
                        "Termination penalties must reduce savings before any operator fee calculation.",
                    ],
                    [
                        "Play 07 covers licensed property-assessment appeal coordination.",
                        "Realized $10,000 tax reduction multiplied by 25% yields $2,500.",
                        "Extract assessment notices and route statutory deadlines to licensed reviewers.",
                        "Local representation restrictions require qualified counsel or licensed consultant handoff.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Preserve the evidence that makes small recoveries repeatable",
                "body": "The highest-value automation usually removes avoidable disputes rather than producing more speculative claims.",
                "items": [
                    "Fingerprint the carrier contract and effective service-guarantee terms alongside each shipment batch; a later contract version must not silently rewrite earlier eligibility.",
                    "For cooling-tower accounts, retain meter serial numbers, installation acceptance, photographs, and reading intervals before calculating sewer credits.",
                    "Save the pre-change utility, waste, or telecom invoice with normalized units; aggregate spend alone cannot distinguish savings from reduced consumption.",
                    "Ask settlement administrators whether third-party filing and fee riders are accepted before collecting a client's full transaction history.",
                ],
            },
        },
        {
            "heading": "2. Automate extraction and routing without automating entitlement",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "For FedEx and UPS, distinguish authorized invoice or tracking access from permission to submit refund claims. "
                    "An EDI feed can provide billing records without exposing a public refund endpoint; a tracking API does not establish filing rights. "
                    "Configure only the carrier interfaces actually granted to the client or authorized agent, and send unsupported submissions through the accepted portal or documented manual channel. "
                    "Persist account, tracking number, service date, charge identifier, and claim reason as an idempotency key. "
                    "A Python worker first checks contractual guarantee waivers, service exclusions, filing windows, and prior credits, then calculates the candidate amount with Decimal. "
                    "The model may classify invoice descriptions but cannot infer delivery commitments from marketing language. "
                    "A reviewer compares every proposed claim with source evidence before releasing a batch. "
                    "Use bounded exponential backoff with jitter for transient failures, respect carrier rate limits, and stop retries on revoked authorization or permanent validation errors. "
                    "A network timeout after submission is an uncertain outcome, not proof of failure. "
                    "Query status or reconcile acknowledgments before retrying, otherwise a well-intentioned queue creates duplicate claims. "
                    "Daily reconciliation links submitted, accepted, rejected, credited, and invoiced states. "
                    "Only the credited result and applicable engagement terms support the downstream fee event; estimated refunds remain operational forecasts."
                ),
                (
                    "Utility automation begins with a tariff registry keyed by jurisdiction, utility, service class, effective date, and authoritative source document. "
                    "OCR extracts meter readings, demand, consumption, riders, taxes, and billing intervals; deterministic checks recompute totals and flag unexpected units. "
                    "A cooling-tower meter reading in gallons cannot be compared directly with billed hundred-cubic-foot units without an explicit conversion and period alignment. "
                    "Retain photographs and original scans because a visually plausible OCR result can still swap a meter identifier or decimal point. "
                    "Use confidence thresholds calibrated on reviewed invoices rather than trusting a vendor's score across every document type. "
                    "Low confidence, a changed tariff, a meter rollover, or a newly appearing rider routes the account to the utility specialist. "
                    "For waste and telecom, normalize quantities before comparing prices, then subtract implementation expenses and termination charges according to the agreement. "
                    "Municipal refund issuance can lag an approved adjustment, so maintain separate approved, posted, paid, and fee-collected dates. "
                    "An account credit may satisfy the contract's recovery definition even when no check arrives; establish that treatment before filing. "
                    "If the tariff archive is unavailable, suspend recommendation generation and retain the case for manual research. "
                    "Do not substitute a neighboring municipality's schedule or ask a model to reconstruct missing rates from memory."
                ),
                (
                    "ATS-integrated Form 8850 processing needs deadline engineering before model engineering. "
                    "Under 26 U.S.C. §51(d)(13), the prescreening notice generally must be completed on or before the employment offer, with the certification request submitted to the designated local agency within twenty-eight days after work begins. "
                    "Track offer, prescreening, start, submission, and acknowledgment timestamps separately; a start-date webhook alone cannot establish timely prescreening. "
                    "Verify the statute's applicable hiring period and any enacted extension before accepting a cohort, especially for starts after December 31, 2025. "
                    "Never assume authorization continues because an ATS integration still works. "
                    "The worker can request missing fields, prepare forms, calculate reminders, and reconcile agency acknowledgments, but must not invent targeted-group eligibility or backdate signatures. "
                    "A specialist reviews certification evidence, qualified wages, retention periods, and interaction with other credits before tax use. "
                    "Circular 230 §10.27 requires engagement-specific fee analysis; ordinary parcel contingency economics cannot simply be copied onto federal tax-return work. "
                    "Where tax-preparer information is involved, assess 26 U.S.C. §7216 before disclosure to an outside model or marketing service. "
                    "Use restricted processing or a manual workflow when the proposed disclosure lacks an applicable basis. "
                    "An expired webhook credential triggers an ATS export reconciliation, not an assumption that no hires occurred."
                ),
            ],
            "table": {
                "caption": "Remaining Five Play Mappings and Two Cross-Lane Automation Controls",
                "headers": [
                    "Mapped lane or shared processing control",
                    "Concrete unit economics or operating requirement",
                    "Permitted automated work and source material",
                    "Required fallback when evidence becomes incomplete",
                ],
                "rows": [
                    [
                        "Play 08 covers ATS-integrated WOTC processing services.",
                        "Twenty completed processing cases multiplied by $100 yield $2,000.",
                        "Prepare timely forms from authorized ATS records and employee responses.",
                        "Missing prescreening evidence requires specialist review without backdating any records.",
                    ],
                    [
                        "Play 09 covers specialty-credit evidence substantiation services.",
                        "Six delivered evidence reviews multiplied by $250 yield $1,500.",
                        "Index wage and expense evidence against specialist-defined qualification requirements.",
                        "Restricted contingent arrangements require a permitted fee structure before engagement.",
                    ],
                    [
                        "Play 10 is b2b_class_action_contingency_recovery for verified operating businesses.",
                        "An actual $12,000 settlement payout multiplied by 25% yields $3,000.",
                        "Match administrator criteria against primary processor or vendor transaction statements.",
                        "Use court-approved third-party claim-filing riders and reject unsupported claimant identities.",
                    ],
                    [
                        "Play 11 covers duplicate vendor-payment recovery services.",
                        "A recovered $4,000 duplicate payment multiplied by 25% yields $1,000.",
                        "Match payment references while distinguishing installments and legitimate recurring invoices.",
                        "Unclear payment allocation requires vendor confirmation before requesting any refund.",
                    ],
                    [
                        "Play 12 covers recurring shared-savings verification servicing.",
                        "Verified monthly $1,000 savings multiplied by 30% yield $300.",
                        "Recompute realized savings against adjusted baselines and implemented service changes.",
                        "Existing waste or telecom splits prevent counting servicing revenue twice.",
                    ],
                    [
                        "Shared control handles carrier submission acknowledgment reconciliation.",
                        "Every uncertain submission receives status checking before any repeated transmission.",
                        "Join submission identifiers with carrier acknowledgments and subsequent invoice credits.",
                        "Unavailable status channels require documented manual confirmation before another attempt.",
                    ],
                    [
                        "Shared control handles utility measurement normalization and provenance.",
                        "Every converted measurement retains original units and explicit conversion factors.",
                        "Compare meter intervals with tariff periods and approved deduction categories.",
                        "Conflicting meter identifiers require source inspection before calculating customer entitlement.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before any consequential release",
                "body": "A reviewer records these checks before transmitting a claim, tax-related filing package, or client-facing recovery assertion.",
                "items": [
                    "Confirm signed authority covers the exact account, service period, submission channel, and requested disclosure; preserve the original baseline snapshot.",
                    "Verify current eligibility rules, contractual waivers, statutory deadlines, required licensing, and the engagement-specific fee structure.",
                    "Recalculate amounts from primary evidence, check prior credits and overlapping claims, and confirm every material model extraction against its source.",
                    "Record the named reviewer, approved payload fingerprint, destination, submission acknowledgment plan, and recovery procedure for an uncertain transmission.",
                ],
            },
        },
        {
            "heading": "3. Measure automation economics and keep claims evidence-first",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Define the automation denominator before reporting a percentage. "
                    "Build a fixed inventory of repetitive research, qualification, fulfillment, and acquisition tasks, with task boundaries and completion criteria frozen for each measurement period. "
                    "In an illustrative thousand-task sample, 740 completed without human intervention and 260 required a person, producing 74% task automation. "
                    "Do not relabel one manual review as ten automated subtasks halfway through the month. "
                    "Track minutes separately because automated document routing and specialist eligibility review carry different labor weights. "
                    "A second, independent thousand-run cost sample can budget $0.10 for intake and storage, $0.02 for OCR, $0.03 for model extraction, $0.01 for queue execution, and $0.04 for expected retries per run. "
                    "That is $0.20 in machine cost. "
                    "If 15% of runs require six minutes of review at $45 hourly, expected review cost is $0.675 per run, producing $0.875 total or $875 for the sample. "
                    "These are workload assumptions, not supplier quotations, and exclude acquisition, specialist filing, owner oversight, and fixed infrastructure. "
                    "Every consequential release still requires human review even when most upstream runs do not. "
                    "Measure accepted findings, rejected claims, correction minutes, and realized fee collection alongside throughput. "
                    "An inexpensive run that creates an unsupported filing is not productive automation."
                ),
                (
                    "Keep the canonical scenarios intact while using unit economics to identify bottlenecks. "
                    "Conservative revenue is $110,000, with $77,000 of implied total costs and $33,000 owner profit at 30%. "
                    "Base revenue is $505,000, with $287,850 of implied costs and $217,150 owner profit at 43.0%. "
                    "Scaled revenue is $900,000, with $396,000 of implied costs and $504,000 owner profit at 56%. "
                    "The first two cases use one full-time owner and three contractors; Scaled uses two full-time people and four contractors. "
                    "These implied costs include the total expense envelope, so do not add the illustrative automation budget again without changing another cost line. "
                    "The revenue basis is earned operator contingency shares, earned shared-savings splits, and processing fees, excluding underlying bills, employer credits, client refunds, and settlement principal. "
                    "A 30% share of a $10,000 client recovery produces $3,000 operator revenue, not $10,000 followed by an invented revenue haircut. "
                    "There is no additional retained-share multiplier supplied for this scorecard. "
                    "Evaluate ASC 606 principal-versus-agent presentation and variable consideration against actual contracts rather than equating receipts with revenue. "
                    "Invoice timing, revenue recognition, and cash collection need separate ledger fields. "
                    "A thirty-six-month agreement provides a monitoring horizon, not permission to book thirty-six months of speculative savings on signature."
                ),
                (
                    "For b2b_class_action_contingency_recovery, build a TRACK_1 watchlist covering payment-card interchange, freight, auto parts, commercial insurance, and SaaS settlements. "
                    "Some corporate antitrust funds reach multibillion-dollar scale, but fund size says nothing about one business's payable award. "
                    "Treat the often-cited 85–90% nonfiling premise as a cohort hypothesis to validate against administrator reports, not a universal conversion statistic. "
                    "Monitor official settlement sites, court orders, claim deadlines, class definitions, exclusions, and distribution updates. "
                    "A parser may flag a client whose primary processor or vendor statements overlap the class period; a reviewer must verify the operating entity, eligible purchases, releases, and prior submissions. "
                    "Use the required fallback of filing strictly for verified operating businesses with primary statements and court-approved third-party claim-filing riders. "
                    "Where the court or administrator does not permit the arrangement, stop that filing route rather than relabeling the agency relationship. "
                    "At a 25–33% contingent share, a verified $12,000 payout yields $3,000–$3,960, subject to permitted terms. "
                    "Model neither face-value purchases nor advertised settlement funds as collectible revenue. "
                    "Proration, objections, appeals, and distribution schedules can change both amount and timing. "
                    "Keep claim acknowledgment, adjudication, payment, and operator collection distinct. "
                    "The strongest outreach artifact is an eligibility checklist tied to primary records, not an inflated recovery estimate."
                ),
            ],
            "table": {
                "caption": "Automation Economics, Canonical Profit Reconciliation, and Exception Thresholds",
                "headers": [
                    "Measured operating quantity or scenario basis",
                    "Exact calculation using stated modeling assumptions",
                    "Evidence required before reporting the result",
                    "Management response to a failed check",
                ],
                "rows": [
                    [
                        "Task automation measures a frozen thousand-task operating sample.",
                        "740 automated completions divided by 1,000 tasks equals 74%.",
                        "Versioned task definitions and completion events support the reported denominator.",
                        "Changed task boundaries require a new baseline rather than retrospective inflation.",
                    ],
                    [
                        "Machine expense measures each normalized extraction workflow run.",
                        "$0.10 plus $0.02 plus $0.03 plus $0.01 plus $0.04 equals $0.20.",
                        "Provider usage records and retry logs support each allocated expense.",
                        "Rising retries trigger connector diagnosis before increasing the processing budget.",
                    ],
                    [
                        "Expected review expense measures the separate illustrative run sample.",
                        "15% multiplied by six minutes and $0.75 equals $0.675.",
                        "Reviewer time records distinguish extraction checks from final release decisions.",
                        "Higher review frequency requires revised pricing or improved source capture.",
                    ],
                    [
                        "Conservative retains the canonical one-owner and three-contractor operating case.",
                        "$110,000 revenue minus $77,000 costs equals $33,000 owner profit.",
                        "Earned fee records and total expenses substantiate the 30% margin.",
                        "Delayed refunds require cash planning without changing earned-fee accounting rules.",
                    ],
                    [
                        "Base retains the canonical one-owner and three-contractor operating case.",
                        "$505,000 revenue minus $287,850 costs equals $217,150 owner profit.",
                        "Earned fee records and total expenses substantiate the 43.0% margin.",
                        "Excess specialist hours require workflow redesign within the stated cost envelope.",
                    ],
                    [
                        "Scaled retains the canonical two-full-time and four-contractor operating case.",
                        "$900,000 revenue minus $396,000 costs equals $504,000 owner profit.",
                        "Earned fee records and total expenses substantiate the 56% margin.",
                        "Capacity shortages require narrower intake until qualified review coverage expands.",
                    ],
                    [
                        "Settlement recovery measures actual client distributions rather than fund headlines.",
                        "$12,000 paid multiplied by 25–33% yields $3,000–$3,960 operator fees.",
                        "Administrator payment records and permitted agreements support the earned share.",
                        "Court restrictions or missing primary statements stop third-party claim submission.",
                    ],
                ],
            },
        },
        {
            "heading": "4. Compound distribution while rehearsing failure recovery",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build distribution around a useful eligibility artifact rather than generic recovery promises. "
                    "Publish programmatic pages only when each page contains a genuinely distinct utility jurisdiction, carrier rule, or settlement class with an authoritative source and review date. "
                    "A Python job can refresh source fingerprints and open an editorial task when terms change; it should not automatically publish model-written interpretations. "
                    "The conversion offer is a narrow diagnostic requiring only minimum account attributes, followed by secure evidence intake after authorization. "
                    "For an illustrative cohort, 200 relevant visitors producing twenty diagnostic requests and five qualified engagements represent 10% request conversion and 25% request-to-engagement conversion. "
                    "If content and distribution cost $600, acquisition cost is $120 per engagement before sales labor. "
                    "Compare that figure with collected contribution over a defined cohort period, not a thirty-six-month theoretical contract total. "
                    "Close the referral loop by asking a satisfied client to share a client-approved savings summary containing methodology and verified results but no account identifiers. "
                    "Never publish tax-preparer information merely because the same client approved an unrelated parcel case study. "
                    "The resulting artifact attracts similar operating profiles, which improves extraction templates and qualification rules. "
                    "This is the flywheel: better evidence produces better segmentation, better segmentation produces cleaner records, and cleaner records reduce review cost."
                ),
                (
                    "Accountants, payroll providers, property managers, and logistics advisers offer better context than indiscriminate prospect lists. "
                    "Create partner-specific intake links that attribute introductions without exposing another client's files or tax status. "
                    "A partner receives a checklist, authority template, expected evidence request, and status vocabulary; they do not receive unrestricted access to the recovery ledger. "
                    "For a monthly pilot, ten active partners producing two introductions each yield twenty introductions. "
                    "At 30% qualification and a 50% close rate, that creates three engagements. "
                    "A $450 enablement budget implies $150 acquisition expense per engagement before owner time and any permitted referral compensation. "
                    "Check professional referral restrictions and disclose arrangements where required before offering compensation. "
                    "Outbound messages should identify one plausible operational condition, such as multi-location utility billing, without claiming a refund has already been found. "
                    "Apply 15 U.S.C. §7704 requirements for commercial email, including accurate headers, identification where required, a valid postal address, and timely opt-out handling. "
                    "Synchronize suppression across campaigns and partners rather than merely hiding a contact from one list. "
                    "A language model can draft from approved factual templates; a person approves new claims and targeting logic. "
                    "Measure qualified engagements and retained clients, not message volume, because poor-fit traffic consumes the same scarce specialist review capacity as legitimate cases."
                ),
                (
                    "Make failure recovery an explicit service capability before adding volume. "
                    "Webhooks require authenticated delivery, replay protection, bounded payloads, and durable acknowledgment only after the event is safely recorded. "
                    "Use per-client queues and concurrency limits so one malformed utility export cannot block parcel deadlines across the book. "
                    "Poison messages enter an exception queue with source fingerprint, error category, retry history, and named owner; they never disappear into a generic log. "
                    "For deadline-sensitive WOTC work, schedule a daily ATS-versus-ledger reconciliation independent of webhook delivery. "
                    "For carrier outages, preserve prepared claims and switch to the contractually accepted manual route before the filing window closes. "
                    "For municipal delays, update client status and cash forecasts without repeatedly submitting the same request. "
                    "Version prompts, extraction schemas, tariff rules, and fee calculations, then replay a fixed reviewed test set before deployment. "
                    "Include contradictory invoices, duplicate shipments, meter rollovers, late hires, and settlement entities with similar names. "
                    "A failed test blocks the changed component while unaffected lanes continue. "
                    "The Scaled team adds a second full-time operator and a fourth contractor only when measured queue age, review utilization, and collected contribution justify the handoff. "
                    "Maintain a weekly drill that reconstructs one case from original evidence through collected fee; scalability means another authorized operator can reproduce the result."
                ),
            ],
            "table": {
                "caption": "Distribution Flywheels and Failure-Recovery Ownership",
                "headers": [
                    "Acquisition loop or operational failure condition",
                    "Concrete mechanism and measurable operating output",
                    "Human review and restricted disclosure boundary",
                    "Fallback action that preserves service continuity",
                ],
                "rows": [
                    [
                        "Programmatic research pages target distinct jurisdiction-specific recovery conditions.",
                        "200 visitors yield twenty requests and five qualified engagements.",
                        "An editor validates authoritative sources before publishing any recovery interpretation.",
                        "Changed source terms pause affected claims and trigger page revision.",
                    ],
                    [
                        "Client-approved case summaries support evidence-led referral distribution.",
                        "Track referral requests and qualified introductions separately from page impressions.",
                        "The client approves the exact artifact and permitted disclosure scope.",
                        "Sensitive records remain private while a generic methodology summary circulates.",
                    ],
                    [
                        "Accountant and payroll partnerships supply context-rich client introductions.",
                        "Ten partners generate twenty introductions and three engagements under stated assumptions.",
                        "Partner access remains limited to their authorized introduction status records.",
                        "Restricted referral compensation shifts the arrangement to uncompensated educational collaboration.",
                    ],
                    [
                        "Narrow outbound campaigns identify plausible operational fit without recovery promises.",
                        "Measure cost per qualified engagement and subsequent collected contribution.",
                        "A reviewer verifies factual claims and required commercial-email operating controls.",
                        "An opt-out suppresses the contact across all connected campaign systems.",
                    ],
                    [
                        "Carrier submission outages threaten short contractual filing windows.",
                        "Queue age alerts compare remaining time with manual processing capacity.",
                        "The parcel specialist verifies uncertain submissions before choosing another channel.",
                        "Use the accepted manual route while retaining all acknowledgment evidence.",
                    ],
                    [
                        "ATS webhook interruptions can conceal deadline-sensitive hiring events.",
                        "Daily source reconciliation compares new hires against recorded case events.",
                        "The tax-credit specialist validates prescreening and applicable hiring-period eligibility.",
                        "Authorized ATS exports restore intake while missing credentials are repaired.",
                    ],
                    [
                        "Municipal refund delays create cash timing and client communication pressure.",
                        "Report approved credits, posted credits, payments, and collected fees separately.",
                        "The utility specialist confirms status without promising an unsupported payment date.",
                        "Maintain documented follow-up intervals instead of repeatedly resubmitting identical claims.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Authorize and snapshot",
                    "action": "Obtain scoped authority and preserve original account evidence before account-specific findings leave the team.",
                    "detail": "Record client identity, permitted channels, baseline periods, fee terms, disclosure restrictions, and source fingerprints in the tenant ledger.",
                },
                {
                    "step": 2,
                    "title": "Extract and test",
                    "action": "Run deterministic normalization and constrained model extraction against versioned eligibility rules.",
                    "detail": "Reject arithmetic mismatches, missing provenance, stale tariffs, duplicate claims, unsupported units, and incomplete deadline evidence into assigned exception queues.",
                },
                {
                    "step": 3,
                    "title": "Review and transmit",
                    "action": "Have the qualified reviewer approve the exact payload before submission through an authorized channel.",
                    "detail": "Preserve reviewer identity, approved payload fingerprint, submission identifier, acknowledgment, and the no-duplicate retry decision.",
                },
                {
                    "step": 4,
                    "title": "Reconcile and compound",
                    "action": "Reconcile realized outcomes and earned fees, then update reviewed templates and permitted referral artifacts.",
                    "detail": "Separate client recovery from operator revenue, measure automation and acquisition costs, and replay failures before expanding the affected workflow.",
                },
            ],
        },
    ],
    "pull_quote": "Automate the evidence trail, not the entitlement decision, and scale only the recoveries another reviewer can reproduce.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Create twelve lane records with explicit authority, evidence, fee basis, reviewer credentials, deadlines, and overlapping-recovery identifiers.",
        "Implement tenant-scoped event intake with source fingerprints, idempotent submission records, bounded retries, and an assigned exception queue.",
        "Connect only authorized FedEx/UPS interfaces, register effective utility tariffs, and reconcile ATS hires against timely Form 8850 evidence.",
        "Benchmark a frozen task inventory against the 70%+ automation target while separately measuring review minutes and cost per completed run.",
        "Reconcile the three canonical revenue and owner-profit cases without counting client refunds, credits, settlement principal, or future savings as current operator revenue.",
        "Launch one reviewed research-page cohort and one partner cohort, then rehearse carrier, municipal, and ATS failure recovery before increasing intake.",
    ],
    "statutory_citations": [
        {
            "title": "31 CFR §10.27 — Fees",
            "url": "https://www.ecfr.gov/current/title-31/subtitle-A/part-10/subpart-B/section-10.27",
            "relevance": "Evaluate contingent-fee restrictions, applicable exceptions, and the actual federal tax engagement before adopting a recovery-based pricing arrangement.",
        },
        {
            "title": "31 CFR §10.22 — Diligence as to accuracy",
            "url": "https://www.ecfr.gov/current/title-31/subtitle-A/part-10/subpart-B/section-10.22",
            "relevance": "Tax practitioners must exercise diligence in covered submissions and representations; automated extraction does not replace source-linked review.",
        },
        {
            "title": "26 U.S.C. §51 — Work opportunity credit",
            "url": "https://www.law.cornell.edu/uscode/text/26/51",
            "relevance": "Check targeted-group rules, certification timing under subsection (d)(13), qualified wages, and the applicable hiring-period limitation under subsection (c)(4).",
        },
        {
            "title": "26 U.S.C. §7216 — Disclosure or use of information by preparers of returns",
            "url": "https://www.law.cornell.edu/uscode/text/26/7216",
            "relevance": "Assess permitted use and disclosure of tax-return preparation information before routing records to outside processors or using them in distribution materials.",
        },
        {
            "title": "Federal Rule of Civil Procedure 23 — Class Actions",
            "url": "https://www.law.cornell.edu/rules/frcp/rule_23",
            "relevance": "Court-supervised class-action procedures frame settlement administration; actual orders, notices, and administrator requirements control each claim and third-party filing arrangement.",
        },
        {
            "title": "15 U.S.C. §7704 — Requirements for transmission of messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Commercial-email acquisition requires accurate transmission information, required identification and address details, functioning opt-out mechanisms, and timely suppression.",
        },
    ],
}
