VOLUME_006_SUBTITLE: str = (
    "Sell the Outcome, Charge for Diagnosis, Build Reliable Agents, "
    "and Earn Retainers with Clear Scope and Human Handoffs"
)


def build_volume_006_diagrams_data() -> list[dict]:
    return [
        {
            "diagram_id": "diag-01-outcome-first-offer",
            "chapter_number": 1,
            "title": "Sell the Outcome Before Building the System",
            "subtitle": (
                "Find a paying business problem, bound the package, "
                "customize delivery, and prove the result."
            ),
            "caption": (
                "Nate Herk emphasizes time, money, and focus; Noah Epstein "
                "collects payment before building; Mikey No Code defines "
                "the package and demonstrates its business result."
            ),
            "assumptions_note": (
                "Nate Herk, Noah Epstein, and Mikey No Code describe "
                "complementary approaches, not a jointly reported engagement. "
                "Mikey's commercial terms are an example offer, not receipts."
            ),
            "note": (
                "Nate Herk — SAerRtQLD0I at 00:01:33 and 00:04:08; "
                "Noah Epstein — fMdUS6amki0 at 00:02:14; "
                "Mikey No Code — i4z0kCcByY8 at 00:29:31, 00:29:51, "
                "00:33:46, and 00:38:08."
            ),
            "chart_type": "process_flow",
            "stages": [
                {
                    "step": "01",
                    "label": "Choose the business result",
                    "value": "Step 1",
                    "detail": (
                        "Nate Herk frames the offer around time, money, "
                        "and focus rather than workflow nodes or models."
                    ),
                },
                {
                    "step": "02",
                    "label": "Secure paid demand",
                    "value": "Step 2",
                    "detail": (
                        "Noah Epstein identifies a business willing to pay "
                        "and collects payment before committing to the build."
                    ),
                },
                {
                    "step": "03",
                    "label": "Bound the initial package",
                    "value": "Step 3",
                    "detail": (
                        "Mikey No Code specifies connected tools, an initial "
                        "three-agent limit, and setup-payment terms. Their "
                        "example is $2,500 setup plus $750 monthly."
                    ),
                },
                {
                    "step": "04",
                    "label": "Customize the reusable base",
                    "value": "Step 4",
                    "detail": (
                        "Nate Herk uses the business owner's subject-matter "
                        "expertise to customize the system; a template "
                        "bundle alone is not the service."
                    ),
                },
                {
                    "step": "05",
                    "label": "Demonstrate the result",
                    "value": "Step 5",
                    "detail": (
                        "Mikey No Code recommends a two- or three-minute "
                        "Loom showing the arriving lead, response, routing "
                        "decision, and final report."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-02-linkedin-acquisition-checkpoints",
            "chapter_number": 6,
            "title": "LinkedIn Activity and Response Checkpoints",
            "subtitle": (
                "Keep sent counts, acceptance rates, message counts, "
                "response rates, and advertising engagement distinct."
            ),
            "caption": (
                "Jack reports workspace connection and messaging results; "
                "Adam Holmgren separately gives a cold thought-leader "
                "advertising engagement benchmark."
            ),
            "assumptions_note": (
                "Jack's counts and percentages are different measures, "
                "not five comparable cohort counts. Adam Holmgren's "
                "benchmark belongs to a separate advertising approach. "
                "Numeric widths must not imply a continuous conversion "
                "funnel or comparable magnitude across these mixed units."
            ),
            "note": (
                "Jack — 4RYnbUHayhM at 00:01:24, 00:02:18, and 00:02:32; "
                "Adam Holmgren — qy4FW_qglNo at 00:06:20. "
                "No accepted-contact count, reply count, or sales count "
                "is inferred."
            ),
            "chart_type": "funnel",
            "stages": [
                {
                    "label": "Connection requests sent",
                    "value": 31000,
                    "display": "About 31,000 requests",
                    "conversion": "Activity count, not a conversion rate",
                    "detail": (
                        "Jack describes the previous year's connection "
                        "requests in the displayed workspace."
                    ),
                },
                {
                    "label": "Connection acceptance rate",
                    "value": 34,
                    "display": "34% accepted",
                    "conversion": "Reported request acceptance rate",
                    "detail": (
                        "Jack reports the percentage accepted; an accepted "
                        "contact count is not supplied."
                    ),
                },
                {
                    "label": "Messages sent",
                    "value": 10000,
                    "display": "Close to 10,000 messages",
                    "conversion": "No acceptance-to-message rate supplied",
                    "detail": (
                        "Jack reports message volume separately from "
                        "connection acceptance."
                    ),
                },
                {
                    "label": "Message response rate",
                    "value": 26,
                    "display": "About 26% responses",
                    "conversion": "Reported message response rate",
                    "detail": (
                        "Jack reports responses, not qualified meetings "
                        "or completed sales."
                    ),
                },
                {
                    "label": "Cold advertising engagement",
                    "value": 15,
                    "display": "Above 15% engagement-inclusive CTR",
                    "conversion": "Separate advertising benchmark",
                    "detail": (
                        "Adam Holmgren calls above 15% good for cold "
                        "thought-leader advertising. This CTR includes "
                        "likes and see-more clicks, not only site visits."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-03-audit-commercial-benchmarks",
            "chapter_number": 3,
            "title": "Audit Prices and Delivery Expenditure",
            "subtitle": (
                "Separate entry prices, larger engagements, and the "
                "cost of delivering an initial free audit."
            ),
            "caption": (
                "Antonio on Belt Course describes bronze audit pricing; "
                "Andrew Dunn describes larger engagements; Liam Ottley "
                "reports initial delivery expenditure and a later engagement."
            ),
            "assumptions_note": (
                "Antonio's and Andrew Dunn's amounts are range endpoints, "
                "not sequential revenue movements. Liam Ottley's $30,000 "
                "is delivery expenditure, while $60,000 is a separate "
                "engagement. Every bar is an independent total; these "
                "amounts do not establish a profit waterfall."
            ),
            "note": (
                "Antonio on Belt Course — YaFtlj9qXQc at 00:04:30; "
                "Andrew Dunn | AI Consulting describes $5,000–$15,000 "
                "engagements; Liam Ottley — noivN2hIXLY at 00:03:53 "
                "for the initial free audit's $30,000 delivery cost. "
                "Liam also reports progressing to a $60,000 engagement."
            ),
            "chart_type": "waterfall",
            "bars": [
                {
                    "label": "Antonio bronze lower price",
                    "value": 1500,
                    "display": "$1,500 audit price",
                    "kind": "total",
                },
                {
                    "label": "Antonio bronze upper price",
                    "value": 3000,
                    "display": "$3,000 audit price",
                    "kind": "total",
                },
                {
                    "label": "Dunn engagement lower price",
                    "value": 5000,
                    "display": "$5,000 engagement",
                    "kind": "total",
                },
                {
                    "label": "Dunn engagement upper price",
                    "value": 15000,
                    "display": "$15,000 engagement",
                    "kind": "total",
                },
                {
                    "label": "Ottley initial delivery expenditure",
                    "value": 30000,
                    "display": "$30,000 cost, not revenue",
                    "kind": "total",
                },
                {
                    "label": "Ottley later engagement",
                    "value": 60000,
                    "display": "$60,000 engagement",
                    "kind": "total",
                },
            ],
        },
        {
            "diagram_id": "diag-04-design-subscription-benchmarks",
            "chapter_number": 2,
            "title": "Design Subscription Economics in Context",
            "subtitle": (
                "Distinguish operating costs, launch pricing, package "
                "pricing, and a teaching target."
            ),
            "caption": (
                "Brett Williams reports Designjoy's tool cost and package "
                "price; Harry Roper reports their launch price. Starter "
                "Story also presents a $500-versus-$5,000 client contrast."
            ),
            "assumptions_note": (
                "Brett Williams's $25,000 monthly figure is a teaching "
                "target, not a promised result. Harry Roper's launch price "
                "is a separate business example. Each equal minimum, "
                "maximum, and typical value represents a quoted point, "
                "not a measured distribution. The $500 client contrast "
                "has no stated billing cadence."
            ),
            "note": (
                "Brett Williams on Starter Story — dXKzST0FE-A at 00:04:54; "
                "Creative Crew with Brad Hussey — o-UR3rkPgJ4 at 00:01:36; "
                "The Futur — 8vwgUwgH2Js at 00:43:19; "
                "Harry Roper — rO0i7sGwhCU at 00:00:00; "
                "Starter Story — vedkm3ZmHIE at 00:05:33. "
                "Williams separately identifies payment fees and taxes."
            ),
            "chart_type": "horizontal_bars",
            "unit": "USD; billing cadence and economic meaning shown per bar",
            "bars": [
                {
                    "label": "Williams operating tools",
                    "min": 176,
                    "max": 176,
                    "typical": 176,
                    "display": "$176/month reported tool cost",
                },
                {
                    "label": "Starter Story lower-price client",
                    "min": 500,
                    "max": 500,
                    "typical": 500,
                    "display": "$500 client contrast; cadence unstated",
                },
                {
                    "label": "Roper launch subscription",
                    "min": 1000,
                    "max": 1000,
                    "typical": 1000,
                    "display": "$1,000/month launch price",
                },
                {
                    "label": "Williams popular subscription",
                    "min": 5000,
                    "max": 5000,
                    "typical": 5000,
                    "display": "$5,000/month package",
                },
                {
                    "label": "Williams teaching target",
                    "min": 25000,
                    "max": 25000,
                    "typical": 25000,
                    "display": "Five clients at $5,000 = $25,000/month",
                },
            ],
        },
        {
            "diagram_id": "diag-05-evidence-led-sales-gates",
            "chapter_number": 5,
            "title": "Require Evidence Before Scaling the Sale",
            "subtitle": (
                "Verify the problem, prove outreach, distinguish pipeline "
                "events, and inspect the delivered result."
            ),
            "caption": (
                "Tom Gaddis verifies audit findings; Marcus on Carson Reed "
                "requires a personal outreach baseline; Aaron Shepherd "
                "separates bookings from projections; Aletto checks results."
            ),
            "assumptions_note": (
                "Tom Gaddis, Marcus on Carson Reed, Aaron Shepherd, and "
                "Aletto supply separate operating checks. Their examples "
                "do not establish a shared sales conversion rate."
            ),
            "note": (
                "Tom Gaddis | Smart AI Operators — Z3ZaxxexqYE at 00:16:04; "
                "Marcus on Carson Reed — L1LsEN_iuIc at 00:38:12; "
                "Aaron Shepherd | GrowthFlare — RQg5jgraVg8 at 00:19:17; "
                "Aletto — IfS3QohXxG8 at 00:21:55."
            ),
            "chart_type": "decision_tree",
            "nodes": [
                {
                    "gate": "G1",
                    "question": (
                        "Does the actual business profile confirm the "
                        "claimed audit gap?"
                    ),
                    "pass_next": "G2",
                    "fail_action": (
                        "Correct the finding before presenting it. "
                        "Tom Gaddis found existing review responses "
                        "where Claude had reported none."
                    ),
                },
                {
                    "gate": "G2",
                    "question": (
                        "Has the personal DM process produced Marcus's "
                        "baseline of two or three appointments weekly?"
                    ),
                    "pass_next": "G3",
                    "fail_action": (
                        "Keep improving the personal process before "
                        "delegating it to a virtual assistant."
                    ),
                },
                {
                    "gate": "G3",
                    "question": (
                        "Are interested replies, bookings, attended calls, "
                        "and projected deals recorded separately?"
                    ),
                    "pass_next": "G4",
                    "fail_action": (
                        "Separate counted events from assumptions. "
                        "Aaron Shepherd counted about 20 bookings; "
                        "later deal estimates were not counted sales."
                    ),
                },
                {
                    "gate": "G4",
                    "question": (
                        "Does the actual delivered result satisfy "
                        "the definition of done?"
                    ),
                    "pass_next": "Accept the inspected result",
                    "fail_action": (
                        "Aletto allows up to three repair attempts, "
                        "then escalates with proof. A success message "
                        "alone does not establish completion."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-06-client-delivery-accountability",
            "chapter_number": 11,
            "title": "Give Every Delivery Responsibility an Owner",
            "subtitle": (
                "Coordinate installation, migration, support, and "
                "priced scope changes around explicit accountability."
            ),
            "caption": (
                "Scott Bartnick assigns onboarding owners; Austin Reed "
                "checks production installation; Nate Herk distinguishes "
                "migration from credential setup; Automate AI Consulting "
                "bounds support; Quiet Client prepares reviewed add-ons."
            ),
            "assumptions_note": (
                "Scott Bartnick calls for named owners, not a specified "
                "staffing count. Austin Reed, Nate Herk, Automate AI "
                "Consulting, and Quiet Client describe responsibilities "
                "that need not correspond to separate employees."
            ),
            "note": (
                "Scott Bartnick — d9zqCrUn7mY at 00:06:07 and 00:08:30; "
                "Austin Reed — mw1V2GoYHsk at 00:04:05; "
                "Nate Herk | AI Automation — t1PTmpas0bg at 00:03:55 "
                "and 00:08:56; Automate AI Consulting — 91lw5ubtLMc "
                "at 00:04:45; Quiet Client — csELc0aBrp4 at 00:03:42; "
                "The Contractor AI — J5BBjGKyoUE at 00:26:06."
            ),
            "chart_type": "org_architecture",
            "center": {
                "role": "Named delivery accountability",
                "headcount": "Not specified by the practitioners",
                "focus": (
                    "Scott Bartnick assigns an owner at each onboarding "
                    "stage, tracks due dates, and confirms client strategy."
                ),
            },
            "spokes": [
                {
                    "role": "Production installation",
                    "type": "Delivery responsibility",
                    "kpi": (
                        "Austin Reed checks production credentials and "
                        "behavior when moving beyond the test environment."
                    ),
                },
                {
                    "role": "Migration reconciliation",
                    "type": "Migration responsibility",
                    "kpi": (
                        "Nate Herk marks processed items and manually "
                        "resets credentials; users and executions do "
                        "not transfer through the demonstrated method."
                    ),
                },
                {
                    "role": "Delivered-work support",
                    "type": "Support responsibility",
                    "kpi": (
                        "Automate AI Consulting provides 30 days of "
                        "support on delivered work; ongoing maintenance "
                        "is a separate commitment."
                    ),
                },
                {
                    "role": "Scope and change approval",
                    "type": "Commercial responsibility",
                    "kpi": (
                        "Quiet Client leaves missing facts and prices "
                        "bracketed for review. The Contractor AI collects "
                        "change orders upfront rather than at final invoicing."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-07-retainer-package-boundaries",
            "chapter_number": 4,
            "title": "Price the Package Without Hiding the Boundary",
            "subtitle": (
                "Compare quoted commercial components while keeping "
                "setup fees separate from recurring service."
            ),
            "caption": (
                "Sean Standberry proposes an avatar and conversion-system "
                "package; Agency Stack Guide illustrates a managed "
                "newsletter; Brett Malinowski describes a bounded "
                "design subscription."
            ),
            "assumptions_note": (
                "Sean Standberry's setup and monthly fees belong to "
                "the same example package. Agency Stack Guide and Brett "
                "Malinowski describe separate offers. Equal endpoints "
                "preserve quoted amounts, not estimated ranges. These "
                "buckets are not additive costs or a shared revenue mix."
            ),
            "note": (
                "Sean Standberry — 5558JLgLk50 at 00:11:13; "
                "Agency Stack Guide — raRxPWQp8ao, including newsletter "
                "quality checks at 00:04:59; Brett Malinowski — "
                "vBXCdVHBK3o at 00:00:48. "
                "Liam Ottley separately recommends estimating maintenance "
                "labor before pricing — kgE01J875dY at 00:18:22."
            ),
            "chart_type": "stacked_comparison",
            "total_range": (
                "Separate USD quotes; one-time and monthly amounts "
                "must not be stacked into a shared total."
            ),
            "buckets": [
                {
                    "label": "Standberry system setup",
                    "low": 500,
                    "high": 500,
                    "notes": (
                        "$500 one-time setup for landing pages, calendar "
                        "integration, automation sequences, and CRM."
                    ),
                },
                {
                    "label": "Standberry recurring delivery",
                    "low": 1000,
                    "high": 1000,
                    "notes": (
                        "$1,000 monthly for ongoing avatar content, "
                        "posting, and system maintenance."
                    ),
                },
                {
                    "label": "Agency Stack Guide newsletter",
                    "low": 297,
                    "high": 297,
                    "notes": (
                        "$297 managed newsletter example. Send a test "
                        "to yourself and check custom fields and links "
                        "before client distribution."
                    ),
                },
                {
                    "label": "Malinowski design example",
                    "low": 5000,
                    "high": 5000,
                    "notes": (
                        "$5,000 monthly design service with one request "
                        "at a time and a stated 48-hour completion period "
                        "per request."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-08-privacy-scope-acceptance-roadmap",
            "chapter_number": 12,
            "title": "Make Privacy, Scope, and Acceptance Observable",
            "subtitle": (
                "Organize boundary checks before treating the work "
                "as ready for acceptance."
            ),
            "caption": (
                "Augusto Digital defines the shipped outcome; ProtaSystem "
                "bounds changes and liability; Protecto and Cognitive "
                "Capital separate privacy checks; Bryan Taylor exposes "
                "usage costs; neomanex verifies observable requirements."
            ),
            "assumptions_note": (
                "The weekly sequence is a planning arrangement, not a "
                "practitioner-reported four-week delivery promise. "
                "Augusto Digital reports a six-week launch. "
                "SecureCyberGates's 35-day deletion review is a "
                "contract-dependent example, not a Week 4 deadline."
            ),
            "note": (
                "Augusto Digital — VzBpfD_Dcq8 at 00:07:01 and 00:08:05; "
                "ProtaSystem — 6l0a6If9Oyk at 00:02:38 and 00:03:49; "
                "Protecto — e8kcLoVVX_A at 00:01:54; "
                "Cognitive Capital — j2Bqq0VTv0o at 00:03:38; "
                "Bryan Taylor — yLxvwa45vR8 at 00:03:04 and 00:03:17; "
                "neomanex — wOkT9r5iVME at 00:02:25, 00:06:42, "
                "and 00:07:01; SecureCyberGates — TcAbiyEqBFM at 00:04:39."
            ),
            "chart_type": "timeline_roadmap",
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Freeze the outcome and commercial boundary",
                    "deliverable": (
                        "Use Augusto Digital's outcome, owner, and date. "
                        "Define each requirement by who acts, what they "
                        "can do, and externally observable proof, as "
                        "neomanex describes. Include ProtaSystem's priced "
                        "change-order pause and aggregate liability cap "
                        "tied to the amount actually paid."
                    ),
                    "gate": (
                        "Is the shipped outcome explicit, with extra "
                        "work separated from the original commitment?"
                    ),
                },
                {
                    "week": "Week 2",
                    "title": "Check sensitive information handling",
                    "deliverable": (
                        "Apply Protecto's separate checks for training, "
                        "retention eligibility, exceptions, abuse monitoring, "
                        "storage location, inference location, and necessary "
                        "sensitive fields. Follow Cognitive Capital's "
                        "redaction checks for documents, prompts, responses, "
                        "and observability records."
                    ),
                    "gate": (
                        "Have privacy settings been checked separately "
                        "and redaction tested against actual business "
                        "information rather than assumed from a "
                        "no-training promise?"
                    ),
                },
                {
                    "week": "Week 3",
                    "title": "Expose consumption and price additions",
                    "deliverable": (
                        "Provide consumption reporting and an admin tool "
                        "as Bryan Taylor recommends. Keep Augusto Digital's "
                        "deferred ideas outside the current build, with "
                        "requester names attached. Apply ProtaSystem's "
                        "pause before unpriced additions."
                    ),
                    "gate": (
                        "Can the owner inspect usage, and does boundary "
                        "crossing trigger a documented, priced change?"
                    ),
                },
                {
                    "week": "Week 4",
                    "title": "Inspect acceptance and deletion commitments",
                    "deliverable": (
                        "Use neomanex's observable acceptance checks, "
                        "including promised screens and states. Define "
                        "backup and snapshot deletion verification and "
                        "ticket review according to the project contract, "
                        "following SecureCyberGates."
                    ),
                    "gate": (
                        "Can each promised behavior be observed, are "
                        "remaining owner decisions explicit, and is "
                        "deletion verification scheduled? neomanex "
                        "reported 36 of 36 requirements passing in "
                        "round five, yet a later done-when review "
                        "still found four gaps."
                    ),
                },
            ],
        },
    ]


VOLUME_006_POSITIONING_ALTERNATIVES: list[dict] = [
    {
        "title": "Paid Diagnosis to Accountable Retainers",
        "subtitle": (
            "Find expensive friction, sell a feasible roadmap, and "
            "extend successful delivery into bounded recurring work."
        ),
        "audience": (
            "AI consultants and service operators selling business "
            "improvements rather than isolated automation builds."
        ),
        "research_basis": (
            "Antonio on Belt Course recommends a paid AI business audit "
            "as the entry point. Andrew Dunn schedules discovery and "
            "delivery, then tests feasibility before the finished deck. "
            "Nick Saraev treats project handoff as the strongest moment "
            "to introduce recurring work. Liam Ottley prices maintenance "
            "against developer effort, while Jeff Sauer distinguishes "
            "availability from accountable enablement."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=YaFtlj9qXQc&t=46s",
            "https://www.youtube.com/watch?v=LSmxwtNHu4k&t=391s",
            "https://www.youtube.com/watch?v=LSmxwtNHu4k&t=624s",
            "https://www.youtube.com/watch?v=RmYTguzXrVM&t=1098s",
            "https://www.youtube.com/watch?v=kgE01J875dY&t=1102s",
            "https://www.youtube.com/watch?v=afaXZkksQs0&t=297s",
        ],
        "validation_status": (
            "Grounded strictly in Vol. 006 YouTube practitioner transcripts."
        ),
    },
    {
        "title": "Focused Agents with Human Backup",
        "subtitle": (
            "Recover missed opportunities, answer repetitive questions, "
            "and make escalation and knowledge access part of delivery."
        ),
        "audience": (
            "Agencies building lead-response, voice, and customer-support "
            "services for businesses with repeatable service needs."
        ),
        "research_basis": (
            "Mikey No Code packages lead response, qualification, and "
            "reporting. Alex Leischow demonstrates rapid lead callback. "
            "Brendan Jowett moves nonessential work after the call and "
            "checks the AI introduction. AIWealthPath requires a human "
            "handoff after unsuccessful attempts. Unstructured emphasizes "
            "permission-aware retrieval and business-relevant evaluation, "
            "while Jonas adds duplicate safety and failure notifications."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=i4z0kCcByY8&t=1771s",
            "https://www.youtube.com/watch?v=8yIHmsMHMYc&t=901s",
            "https://www.youtube.com/watch?v=Ky2Z6kGp1Vk&t=474s",
            "https://www.youtube.com/watch?v=Ky2Z6kGp1Vk&t=123s",
            "https://www.youtube.com/watch?v=JKmSoDIpfdI&t=196s",
            "https://www.youtube.com/watch?v=ruilmyfVgrI&t=904s",
            "https://www.youtube.com/watch?v=ruilmyfVgrI&t=1048s",
            "https://www.youtube.com/watch?v=4imOFZeP7nk&t=440s",
        ],
        "validation_status": (
            "Grounded strictly in Vol. 006 YouTube practitioner transcripts."
        ),
    },
    {
        "title": "Productized Delivery Without Unlimited Scope",
        "subtitle": (
            "Pair a recognizable offer and disciplined prospecting "
            "with request boundaries, named owners, and visible acceptance."
        ),
        "audience": (
            "Solo specialists and small agencies turning repeatable "
            "design or AI services into manageable recurring packages."
        ),
        "research_basis": (
            "Brett Williams maintains a defined request and communication "
            "process rather than accommodating every client preference. "
            "Lily Latzo reuses a focused niche demonstration. Jack uses "
            "LinkedIn response evidence before expanding email investment. "
            "Scott Bartnick assigns onboarding ownership. ProtaSystem "
            "pauses out-of-scope work for pricing, and neomanex tests "
            "requirements through observable product behavior."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=8vwgUwgH2Js&t=1773s",
            "https://www.youtube.com/watch?v=NjvNF17_97w&t=475s",
            "https://www.youtube.com/watch?v=4RYnbUHayhM&t=138s",
            "https://www.youtube.com/watch?v=d9zqCrUn7mY&t=367s",
            "https://www.youtube.com/watch?v=6l0a6If9Oyk&t=158s",
            "https://www.youtube.com/watch?v=wOkT9r5iVME&t=145s",
            "https://www.youtube.com/watch?v=wOkT9r5iVME&t=402s",
        ],
        "validation_status": (
            "Grounded strictly in Vol. 006 YouTube practitioner transcripts."
        ),
    },
]
