VOLUME_004_SUBTITLE: str = (
    "Find Paid Pain, Build Narrow AI Tools, Secure Access, "
    "Meter Usage, and Keep Customers"
)


def build_volume_004_diagrams_data() -> list[dict]:
    return [
        {
            "diagram_id": "diag-01-problem-to-paid-commitment",
            "chapter_number": 1,
            "title": "From a Recurring Problem to a Paid Commitment",
            "subtitle": (
                "Find existing demand, understand the work, identify distribution, "
                "and make a delivery promise you can honor."
            ),
            "caption": (
                "Rob Walling, Greg Isenberg, Fomin Unscripted, and founders featured "
                "on Starter Story describe complementary problem-selection checks."
            ),
            "assumptions_note": (
                "These checks combine Rob Walling's outside validation, Greg "
                "Isenberg's task mapping, Fomin Unscripted's distribution-first "
                "approach, and Starter Story cases; they are not one founder's "
                "reported sequence."
            ),
            "note": (
                "Gil's Starter Story account reports $20,000 from 50 lifetime "
                "licenses before building Subscribr, with delivery promised in "
                "60 days and refund access for two weeks after delivery."
            ),
            "chart_type": "process_flow",
            "stages": [
                {
                    "step": "01",
                    "label": "Find repeated pain",
                    "value": "Step 1",
                    "detail": (
                        "Rob Walling recommends identifying the problem rather "
                        "than pitching the idea. Abhishek, on Starter Story, "
                        "looks for dissatisfaction with established tools."
                    ),
                },
                {
                    "step": "02",
                    "label": "Validate beyond work",
                    "value": "Step 2",
                    "detail": (
                        "Rob Walling warns that an employer can be uniquely "
                        "dysfunctional. Check that outside customers share the pain."
                    ),
                },
                {
                    "step": "03",
                    "label": "Separate judgment from mechanics",
                    "value": "Step 3",
                    "detail": (
                        "Greg Isenberg documents each task precisely and separates "
                        "judgment from mechanical work before automation."
                    ),
                },
                {
                    "step": "04",
                    "label": "Name the acquisition channel",
                    "value": "Step 4",
                    "detail": (
                        "Fomin Unscripted identifies where customers will come "
                        "from before building. Brett Malinowski describes "
                        "demonstrating the customer's desired outcome in content."
                    ),
                },
                {
                    "step": "05",
                    "label": "Price the delivery commitment",
                    "value": "Step 5",
                    "detail": (
                        "Gil's Subscribr pre-sale includes delivery and refund "
                        "commitments. Screenshot One's founder, on Starter Story, "
                        "raises prices and reduces free usage after the early "
                        "$7 offer leaves almost zero margins."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-02-cloud-credit-package-ladder",
            "chapter_number": 6,
            "title": "Cloud Credit Packages Have Different Entry Conditions",
            "subtitle": (
                "Separate reported package amounts from eligibility, coverage "
                "periods, and the recurring bill."
            ),
            "caption": (
                "XRaise describes Google startup coverage and AWS Activate "
                "packages with different qualification routes."
            ),
            "assumptions_note": (
                "The XRaise amounts are independent package references arranged "
                "by size, not successive funnel populations. No applicant "
                "conversion rates or guaranteed awards are reported."
            ),
            "note": (
                "XRaise recommends checking the AWS credit expiration date and "
                "setting a budget alert. Trapture Explains emphasizes that "
                "credits are temporary while the monthly bill remains."
            ),
            "chart_type": "funnel",
            "stages": [
                {
                    "label": "Google AI first-year ceiling",
                    "value": 250000,
                    "display": "Up to $250,000",
                    "conversion": "Not a conversion rate",
                    "detail": (
                        "XRaise describes first-year coverage of 100% of usage "
                        "up to this amount for AI startups; qualification is "
                        "separate from the headline ceiling."
                    ),
                },
                {
                    "label": "AWS Portfolio ceiling",
                    "value": 200000,
                    "display": "Up to $200,000",
                    "conversion": "Not a conversion rate",
                    "detail": (
                        "XRaise describes the provider-linked Activate Portfolio "
                        "route, requiring an Activate provider Org ID."
                    ),
                },
                {
                    "label": "Google first-year standard ceiling",
                    "value": 100000,
                    "display": "Up to $100,000",
                    "conversion": "Not a conversion rate",
                    "detail": (
                        "XRaise describes first-year coverage of 100% of usage "
                        "up to this standard amount, distinct from the AI ceiling."
                    ),
                },
                {
                    "label": "Selected AWS Founders awards",
                    "value": 5000,
                    "display": "Up to $5,000",
                    "conversion": "Not a conversion rate",
                    "detail": (
                        "XRaise reports selected Founders awards up to this "
                        "amount; this is not an automatic upgrade."
                    ),
                },
                {
                    "label": "AWS Founders starting package",
                    "value": 1000,
                    "display": "$1,000",
                    "conversion": "Not a conversion rate",
                    "detail": (
                        "XRaise describes Founders as the direct route for "
                        "self-funded startups."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-03-launch-price-and-cost-reference",
            "chapter_number": 3,
            "title": "Monthly Prices and Gateway Cost References",
            "subtitle": (
                "Keep customer plan prices separate from infrastructure expense "
                "and model-spend crossover estimates."
            ),
            "caption": (
                "Mikey No Code demonstrates invoice-converter prices, The Bridge "
                "Dev demonstrates a subscription with overages, and Bryan "
                "Software presents gateway community math."
            ),
            "assumptions_note": (
                "All six bars are independent monthly dollar references from "
                "Mikey No Code, The Bridge Dev, or Bryan Software. They are "
                "standalone totals, not deductions or a reconciled profit bridge."
            ),
            "note": (
                "Bryan Software explicitly distinguishes the approximate gateway "
                "crossover from an audited figure. Mikey No Code tests checkout, "
                "free-limit enforcement, and the paid-plan update after publishing."
            ),
            "chart_type": "waterfall",
            "bars": [
                {
                    "label": "Bridge subscription base",
                    "value": 9,
                    "display": "$9/month plus metered overages",
                    "kind": "total",
                },
                {
                    "label": "Invoice Starter",
                    "value": 19,
                    "display": "$19/month for 50 invoices",
                    "kind": "total",
                },
                {
                    "label": "Invoice Pro",
                    "value": 49,
                    "display": "$49/month for 500 invoices",
                    "kind": "total",
                },
                {
                    "label": "Invoice Team",
                    "value": 99,
                    "display": "$99/month with unlimited usage and priority support",
                    "kind": "total",
                },
                {
                    "label": "Gateway infrastructure estimate",
                    "value": 200,
                    "display": "Roughly $200/month infrastructure",
                    "kind": "total",
                },
                {
                    "label": "Gateway model-spend crossover",
                    "value": 3600,
                    "display": "About $3,600/month in model spend",
                    "kind": "total",
                },
            ],
        },
        {
            "diagram_id": "diag-04-vertical-ai-evidence",
            "chapter_number": 2,
            "title": "Specialization Requires More Than a Wrapper",
            "subtitle": (
                "Founder objectives, contract values, savings, prompt chains, "
                "and evaluation depth describe different parts of vertical AI."
            ),
            "caption": (
                "Rob Walling, Bessemer Venture Partners, Jamie Cuffe on Sequoia "
                "Capital, and Y Combinator supply these distinct reference points."
            ),
            "assumptions_note": (
                "Units differ and bar lengths must not be read as a common "
                "ranking. For ranges reported by Rob Walling, Jamie Cuffe, and "
                "Jake Heller, typical repeats the lower endpoint solely as a "
                "plot marker; no central estimate is asserted."
            ),
            "note": (
                "Rob Walling's ARR range is an objective, not an outcome "
                "guarantee. Bessemer's ACV comparison and Jamie Cuffe's customer "
                "savings have different denominators. Y Combinator's evaluation "
                "example concerns a specific marketplace setting."
            ),
            "chart_type": "horizontal_bars",
            "unit": "Separate source units shown in each display; not comparable",
            "bars": [
                {
                    "label": "Walling vertical SaaS objective",
                    "min": 2,
                    "max": 20,
                    "typical": 2,
                    "display": "$2–20 million ARR objective",
                },
                {
                    "label": "Bessemer contract comparison",
                    "min": 80,
                    "max": 80,
                    "typical": 80,
                    "display": "Around 80% of existing software ACVs",
                },
                {
                    "label": "Pace customer cost savings",
                    "min": 50,
                    "max": 75,
                    "typical": 50,
                    "display": "50–75% for some insurance customers",
                },
                {
                    "label": "Heller prompt-chain depth",
                    "min": 12,
                    "max": 24,
                    "typical": 12,
                    "display": "A dozen or two dozen individual prompts",
                },
                {
                    "label": "Gig ML marketplace evaluation",
                    "min": 10000,
                    "max": 10000,
                    "typical": 10000,
                    "display": "10,000 tailored test cases",
                },
            ],
        },
        {
            "diagram_id": "diag-05-cache-and-routing-gates",
            "chapter_number": 5,
            "title": "Reduce AI Cost Without Losing Correctness",
            "subtitle": (
                "Preserve reusable input, expire changing answers, evaluate "
                "routing, and inspect the actual operating result."
            ),
            "caption": (
                "IBM Technology, Mastra, Learn with Vichu, AmanAI Lab, Hunter "
                "Sneed, and Morning Maker Show with Sandra and Dan describe "
                "the checks behind cost optimization."
            ),
            "assumptions_note": (
                "Mastra's 90% cached-input discount is not a whole-bill "
                "reduction. Hunter Sneed's roughly 50% saving belongs to an "
                "eight-task demonstration, not every routed workload."
            ),
            "note": (
                "Hunter Sneed includes routing costs and observes variable "
                "tier selection on borderline requests. Sandra on Morning "
                "Maker Show reports a launch-morning functionality failure "
                "that could otherwise be mistaken for weak demand."
            ),
            "chart_type": "decision_tree",
            "nodes": [
                {
                    "gate": "G1",
                    "question": "Does the reusable prompt prefix stay identical?",
                    "pass_next": "G2",
                    "fail_action": (
                        "Follow Mastra by moving changing memory after stable "
                        "knowledge. Follow Learn with Vichu by keeping tool "
                        "names, order, schemas, and JSON ordering stable."
                    ),
                },
                {
                    "gate": "G2",
                    "question": "Can a cached answer remain valid until it expires?",
                    "pass_next": "G3",
                    "fail_action": (
                        "Follow AmanAI Lab by checking expiration for changing "
                        "answers rather than retaining stale balances indefinitely."
                    ),
                },
                {
                    "gate": "G3",
                    "question": (
                        "Do routed outputs meet quality needs after classifier "
                        "and retry costs are included?"
                    ),
                    "pass_next": "G4",
                    "fail_action": (
                        "Re-evaluate model choices and borderline requests as "
                        "Hunter Sneed recommends; attribute usage by user, "
                        "tenant, workload, or department."
                    ),
                },
                {
                    "gate": "G4",
                    "question": (
                        "Do memory behavior, core functionality, and checkout "
                        "survive the change?"
                    ),
                    "pass_next": (
                        "Monitor attributable spending and retained usage, "
                        "following Hunter Sneed and The Startup Podcast."
                    ),
                    "fail_action": (
                        "Benchmark memory behavior as IBM Technology recommends "
                        "and repair functionality before interpreting missing "
                        "sales, as Sandra's launch experience illustrates."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-06-buyer-discovery-operating-map",
            "chapter_number": 11,
            "title": "Organize Discovery Around Buyer Decisions",
            "subtitle": (
                "Connect customer language, comparison content, indexing, "
                "and attribution to qualified demand."
            ),
            "caption": (
                "Federico Jorge on UserActive, Rob Hoffman, Micael Coutinho, "
                "and Paul Ogonowski describe complementary discovery functions."
            ),
            "assumptions_note": (
                "These are operating responsibilities, not a reported staffing "
                "chart. Federico Jorge, Rob Hoffman, Micael Coutinho, and Paul "
                "Ogonowski do not establish a shared team size or hiring plan."
            ),
            "note": (
                "Rob Hoffman reports roughly 10 qualified weekly demos from "
                "comparison pages. Paul Ogonowski contrasts 2% of visits "
                "attributed to AI in analytics with 23% of new signups reporting "
                "AI discovery; the populations differ."
            ),
            "chart_type": "org_architecture",
            "center": {
                "role": "Buyer discovery and qualified pipeline",
                "headcount": "Not specified",
                "focus": (
                    "Judge discovery by qualified demand rather than traffic "
                    "alone, as Rob Hoffman and Loopex Digital emphasize."
                ),
            },
            "spokes": [
                {
                    "role": "Customer-language research",
                    "type": "Research responsibility",
                    "kpi": (
                        "Buyer questions and wording captured from recorded, "
                        "transcribed customer conversations, following Federico "
                        "Jorge on UserActive."
                    ),
                },
                {
                    "role": "Comparison content",
                    "type": "Publishing responsibility",
                    "kpi": (
                        "Qualified demos associated with comparison pages, "
                        "tracked through GA4 in Rob Hoffman's account."
                    ),
                },
                {
                    "role": "Search indexing",
                    "type": "Maintenance responsibility",
                    "kpi": (
                        "Google and Bing indexing checked weekly, with missing "
                        "pages investigated and improved, following Micael Coutinho."
                    ),
                },
                {
                    "role": "Discovery attribution",
                    "type": "Measurement responsibility",
                    "kpi": (
                        "New-signup discovery answers and the questions asked "
                        "of AI assistants, following Paul Ogonowski."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-07-launch-and-isolation-observations",
            "chapter_number": 4,
            "title": "Launch Attention and Tenant Isolation Are Separate Tests",
            "subtitle": (
                "Audience response does not establish authorization safety, "
                "and a concurrency exercise does not establish market demand."
            ),
            "caption": (
                "Jack Smith reports Product Hunt launch observations; Alex "
                "Rusin reports a configuration-specific Prisma concurrency test."
            ),
            "assumptions_note": (
                "Each low and high repeats the same reported observation, "
                "not an estimated range. Jack Smith's upvotes, video audience, "
                "and hours cannot be added to Alex Rusin's request count or "
                "interpreted as shares of a common total."
            ),
            "note": (
                "Alex Rusin limits the no-contamination result to the tested "
                "configuration and failure mode. Past The Diagram recommends "
                "testing isolation through the actual application role rather "
                "than relying on a privileged owner's apparent success."
            ),
            "chart_type": "stacked_comparison",
            "total_range": (
                "No additive total; separate observations in upvotes, "
                "video views, hours, and concurrent requests"
            ),
            "buckets": [
                {
                    "label": "Product Hunt launch result",
                    "low": 17,
                    "high": 17,
                    "notes": (
                        "17 upvotes reported by Jack Smith, used as the "
                        "benchmark to beat on the next attempt."
                    ),
                },
                {
                    "label": "Bespoke launch video audience",
                    "low": 2,
                    "high": 2,
                    "notes": (
                        "Two views reported by Jack Smith after hours of "
                        "production; they preferred reallocating effort "
                        "toward more engaging outbound content."
                    ),
                },
                {
                    "label": "Hidden-vote opening period",
                    "low": 4,
                    "high": 4,
                    "notes": (
                        "Jack Smith describes the first four hours with "
                        "hidden vote totals and randomized product ordering."
                    ),
                },
                {
                    "label": "Prisma concurrency exercise",
                    "low": 800,
                    "high": 800,
                    "notes": (
                        "Alex Rusin reports 800 concurrent requests with "
                        "no contamination in the tested configuration."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-08-retention-and-payment-recovery-roadmap",
            "chapter_number": 12,
            "title": "Separate Cancellation Causes and Recover Failed Payments",
            "subtitle": (
                "Diagnose churn, validate first value, configure payment "
                "recovery, and inspect cohort economics."
            ),
            "caption": (
                "RonBuilds, Hormozi on Business Beast Mode, Freemius, Dodo "
                "Payments, Recurly, Gravy, and Ask a VC supply the operating checks."
            ),
            "assumptions_note": (
                "Week headings are planning slots, not a shared implementation "
                "schedule reported by these practitioners. Recurly's recovery "
                "windows and Gravy's 30-day claim remain separate observations, "
                "not weekly performance promises."
            ),
            "note": (
                "Recurly reports median recovery of 47% for 1–7-day windows "
                "and 57.7% for 15–21-day windows. Gravy reports average recovery "
                "of 51% within 30 days. Neither establishes a universal "
                "recovery target or a like-for-like vendor comparison."
            ),
            "chart_type": "timeline_roadmap",
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Separate voluntary and involuntary churn",
                    "deliverable": (
                        "A cohort breakdown separating deliberate cancellations "
                        "from failed-payment losses, following RonBuilds."
                    ),
                    "gate": (
                        "Keep gross losses visible even when expansion improves "
                        "net churn, as Ask a VC recommends."
                    ),
                },
                {
                    "week": "Week 2",
                    "title": "Validate the first-value event",
                    "deliverable": (
                        "An activation check and hands-on onboarding approach "
                        "grounded in RonBuilds and Hormozi on Business Beast Mode."
                    ),
                    "gate": (
                        "Confirm that the proposed activation event distinguishes "
                        "retained users from departing users; RonBuilds warns "
                        "that a universally completed event is not enough."
                    ),
                },
                {
                    "week": "Week 3",
                    "title": "Configure retries and payment updates",
                    "deliverable": (
                        "Retries, reminders, and an easy card-update path as "
                        "Freemius describes, with Dodo Payments distinguishing "
                        "fixable failures from stolen-card failures."
                    ),
                    "gate": (
                        "Inspect payment-status conditions and unsuccessful "
                        "branches as Ecom Mastery recommends. Recurly advises "
                        "experimenting with recovery windows for the business."
                    ),
                },
                {
                    "week": "Week 4",
                    "title": "Evaluate recovered value and follow-up cost",
                    "deliverable": (
                        "A recovery assessment that considers Gravy's dedicated "
                        "human follow-up approach alongside automated recovery."
                    ),
                    "gate": (
                        "Check cohort value before personalized price offers "
                        "and keep retargeting cost below customer value, "
                        "following RonBuilds."
                    ),
                },
            ],
        },
    ]


VOLUME_004_POSITIONING_ALTERNATIVES: list[dict] = [
    {
        "title": "Paid Pain Before Product",
        "subtitle": (
            "Find a narrow buyer problem, validate outside your own workplace, "
            "and sell a delivery commitment before expanding the build."
        ),
        "audience": (
            "Solo founders and small teams choosing a focused AI product "
            "without assuming that technical novelty creates demand."
        ),
        "research_basis": (
            "Rob Walling warns against validating only inside an employer's "
            "environment. Fomin Unscripted identifies acquisition channels "
            "before development. Gil's Subscribr account on Starter Story "
            "reports $20,000 in pre-build sales tied to delivery and refund "
            "commitments. Jamie Cuffe on Sequoia Capital connects vertical "
            "automation to documented insurance operations and customer savings."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=6sgCo6fMSGY&t=332s",
            "https://www.youtube.com/watch?v=8lmA9UgwNQs&t=142s",
            "https://www.youtube.com/watch?v=7KqlwjBM_tM&t=334s",
            "https://www.youtube.com/watch?v=Uqr2U24uxOs&t=818s",
        ],
        "validation_status": (
            "Grounded strictly in Vol. 004 YouTube practitioner transcripts."
        ),
    },
    {
        "title": "Build Where Customers Already Work",
        "subtitle": (
            "Turn platform friction into a focused integration, then win "
            "discovery with customer language and comparison content."
        ),
        "audience": (
            "Builders of Chrome extensions, Shopify apps, Airtable integrations, "
            "and focused alternatives to established SaaS products."
        ),
        "research_basis": (
            "Andy on Starter Story searches for pain inside existing platforms "
            "and emphasizes early user testing. Super Lemon on hexdevs uses "
            "Shopify autocomplete and marketplace evidence to assess demand. "
            "Federico Jorge on UserActive builds messaging from customer "
            "conversations. Rob Hoffman connects comparison pages to qualified "
            "demos, while Paul Ogonowski captures buyer-reported discovery."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=NvtsM8Nk72c&t=287s",
            "https://www.youtube.com/watch?v=NvtsM8Nk72c&t=593s",
            "https://www.youtube.com/watch?v=KP61wa0qiSU&t=991s",
            "https://www.youtube.com/watch?v=JVpDfAIFgYk&t=398s",
            "https://www.youtube.com/watch?v=mPeQxVCunPU&t=1975s",
            "https://www.youtube.com/watch?v=smAcRrXdcgw&t=98s",
        ],
        "validation_status": (
            "Grounded strictly in Vol. 004 YouTube practitioner transcripts."
        ),
    },
    {
        "title": "Protect the Recurring Revenue Engine",
        "subtitle": (
            "Isolate tenants, control AI consumption, reconcile usage billing, "
            "and repair activation and failed-payment losses."
        ),
        "audience": (
            "Operators of paid AI applications whose margins and retention "
            "depend on reliable access, metering, onboarding, and collection."
        ),
        "research_basis": (
            "Past The Diagram tests cross-tenant access through the application "
            "role. Mastra preserves stable prompt prefixes, and Hunter Sneed "
            "evaluates routing quality alongside classifier and retry costs. "
            "CJ Avilla ties generated activity to billing records. One Minute "
            "Finance distinguishes return ratios from gross-profit payback. "
            "RonBuilds separates cancellation causes, and Recurly recommends "
            "testing payment-recovery windows rather than assuming one default."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=h1KAW_izGl8&t=232s",
            "https://www.youtube.com/watch?v=eBB0dBqfvuQ&t=188s",
            "https://www.youtube.com/watch?v=raEBR_2VbXE&t=562s",
            "https://www.youtube.com/watch?v=v8cN4pEofy8&t=3355s",
            "https://www.youtube.com/watch?v=Xpw9vNbYna0&t=439s",
            "https://www.youtube.com/watch?v=FtbQGH3sZ3c&t=120s",
            "https://www.youtube.com/watch?v=eBy7DfSz09g&t=21s",
        ],
        "validation_status": (
            "Grounded strictly in Vol. 004 YouTube practitioner transcripts."
        ),
    },
]
