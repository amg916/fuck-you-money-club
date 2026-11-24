from __future__ import annotations

CHAPTER_12 = {
    "id": "Q12",
    "chapter_id": "Q12",
    "chapter_number": 12,
    "question_number": 12,
    "slug": "reduce-churn-and-recover-failed-payments",
    "question_prompt": "How do I distinguish customer cancellations from failed-payment churn and use onboarding, risk signals, and recovery workflows to address each?",
    "kicker": "Q12 / THE BIG MONEY PLAYBOOKS",
    "title": "Reduce Churn and Recover Failed Payments",
    "subtitle": "Onboarding to first value, cancellation flows, at-risk customer identification, churn prediction, dunning windows, payment recovery, and Churnkey, Dodo, GoHighLevel, Freemius, Gravy, and Recurly approaches",
    "layout_template": "action_worksheet_summary",
    "reading_time_minutes": 15,
    "executive_summary": (
        "RonBuilds separates deliberate cancellations from failed-card losses, then checks activation, engagement, and acquisition channel before choosing a fix. "
        "Hormozi pushes hands-on onboarding; Dan Martell adds cohort instrumentation and at-risk monitoring. "
        "CSM Practice balances outcomes with relationships, while Gamify Data tests prediction against existing rules. "
        "Churnkey, Dodo, GoHighLevel, and Freemius combine retries with payment-update messages; Churnkey adds in-app recovery walls. "
        "Recurly reports 47% median recovery for one-to-seven-day windows versus 57.7% for fifteen-to-twenty-one-day windows. "
        "The approaches diverge: Gravy emphasizes dedicated human follow-up, while Churnkey promotes automated recovery. "
        "Vasco Aires builds a multistep cancellation sequence; Raaft emphasizes reason-matched offers and fixing broken cancellation paths. "
        "Ask a VC keeps gross losses visible even when account expansion makes net churn look better."
    ),
    "key_metrics": [
        {
            "label": "Initial video activation",
            "metric": "Initial video activation",
            "value": "Around 50% in the first week",
            "confidence": "attributed_practitioner_claim",
            "context": "The founder speaking with Hormozi reports that around half of new users create their first video during the first week; only 10% edit their first photo.",
            "source": "Business Beast Mode ([iGqudu6WmHs @ 00:00:51])",
        },
        {
            "label": "Churnkey multichannel payment recovery",
            "metric": "Churnkey multichannel payment recovery",
            "value": "Up to 89%",
            "confidence": "attributed_practitioner_claim",
            "context": "Churnkey attributes this recovery claim to its combined recovery channels, including email, SMS, payment walls, and routing to the appropriate billing contact.",
            "source": "Churnkey ([vp4SwMY-QrM @ 00:02:21])",
        },
        {
            "label": "Gravy failed-revenue recovery",
            "metric": "Gravy failed-revenue recovery",
            "value": "Average 51% within 30 days",
            "confidence": "attributed_practitioner_claim",
            "context": "Gravy reports this result for its payment-recovery framework, which emphasizes full-time focus, personalized follow-up, and visibility.",
            "source": "Gravy ([7MuS7PqfUyo @ 00:01:20])",
        },
        {
            "label": "Recurly recovery by dunning window",
            "metric": "Recurly recovery by dunning window",
            "value": "47% at 1–7 days; 57.7% at 15–21 days",
            "confidence": "attributed_practitioner_claim",
            "context": "Recurly presents these merchant median recovery rates and recommends experimenting with window lengths for the individual business.",
            "source": "Recurly ([eBy7DfSz09g @ 00:00:21])",
        },
    ],
    "sections": [
        {
            "id": "practitioner-consensus",
            "title": "The Practitioner Consensus",
            "paragraphs": [
                (
                    "Separate the customer who chooses to leave from the customer whose renewal simply fails. "
                    "RonBuilds starts with a cohort of cancellations and payment failures, then divides it into voluntary cancellation by the customer and involuntary loss through declining cards, insufficient funds, or expiry. "
                    "That distinction changes the work: the first group requires an explanation for leaving; the second may need a working payment method rather than another product pitch. "
                    "Churnkey describes the silent version as friction rather than dissatisfaction: the customer did not cancel or complain, but the card did not go through. "
                    "Freemius gives the same operational sequence for that problem: retry, remind, and provide an easy way to update payment details. "
                    "Keep the revenue view alongside the customer count. "
                    "Ryan Floyd of Ask a VC emphasizes dollar churn in enterprise B2B because customers can contribute very different amounts of revenue; logo churn and revenue churn align only when customers pay the same amount. "
                    "Floyd also separates gross cancellations from net churn, which incorporates expansion and contraction. "
                    "RonBuilds warns against treating the aggregate churn rate as a diagnosis and immediately launching win-back campaigns. "
                    "The shared starting point is therefore specific: identify what happened, which customers experienced it, and what revenue those customers represent. "
                    "[FtbQGH3sZ3c @ 00:02:00] [O51fzGSuixY @ 00:00:00] "
                    "[iJ-6ibkTVyg @ 00:00:17] [su9KuGnbAW8 @ 00:00:50]"
                ),
                (
                    "Onboarding must lead to value, not merely a completed checklist. "
                    "The founder speaking with Alex Hormozi reports that around 50% of users make their first video in the first week, while only 10% edit their first photo. "
                    "Hormozi immediately asks whether making the video actually correlates with staying, then insists that the founder verify the relationship. "
                    "RonBuilds makes the same distinction through setup moments, first-value moments, and habit moments: completing a sequence is not enough if people never continue using the product. "
                    "Their practical overlap is to examine activation alongside the customer's acquisition channel rather than assume every signup has the same expectations or potential value. "
                    "Hormozi asks who buys, what they do, and where they come from; RonBuilds looks for mismatches between an advertisement's promise and the experience after signup. "
                    "Dan Martell supplies the instrumentation prerequisite: know when customers enrolled, which plan they use, and which cohorts are churning at what rate. "
                    "That gives the operator something more useful than a monthly total of lost revenue. "
                    "For RonBuilds, customers who never reached value are primarily an onboarding and activation problem; heavily personalized win-back work does not repair that upstream failure. "
                    "For Hormozi, watching people use the product is how the automated checklist starts getting corrected. "
                    "[iGqudu6WmHs @ 00:00:51] [FtbQGH3sZ3c @ 00:03:33] "
                    "[2y-cxWkz_jQ @ 00:00:37]"
                ),
                (
                    "At-risk monitoring moves the intervention ahead of the cancellation decision. "
                    "Dan Martell asks operators to define what healthy usage looks like, what an account about to churn looks like, which features customers have deployed, and when they log in. "
                    "The resulting signals should feed customer support or customer success rather than remain an unused measurement exercise. "
                    "CSM Practice broadens that view beyond activity and pleasant interactions: a useful health score must detect both desired customer outcomes and an appropriate experience. "
                    "The speakers say many models emphasize experience because outcomes can be harder to collect and may require information from customers themselves. "
                    "They also describe a practical advantage of a strong relationship: customers missing value may give advance notice about a required capability instead of disappearing without warning. "
                    "Gamify Data makes the prediction target explicit. "
                    "Cancellation, contraction, renewal after usage collapses, and failed-card loss are different events; choose one per model and specify the prediction window. "
                    "Its example scores renewal 120 days ahead, then produces a weekly list ranked by revenue at risk, with a reason and a named representative. "
                    "Together, these approaches connect usage, outcomes, relationships, and an assigned response while keeping the predicted event specific. "
                    "The score is useful to the team because it identifies an account to work, not simply an account to label. "
                    "[2y-cxWkz_jQ @ 00:02:35] [YGbTHo5OkdI @ 00:02:32] "
                    "[YGbTHo5OkdI @ 00:04:47] [SFcHnbb87E8 @ 00:00:14]"
                ),
            ],
            "table": {
                "caption": "Separate the loss, establish value, and identify the customer worth intervening with.",
                "headers": ["Operator question", "Practitioner instruction", "Expert Source"],
                "rows": [
                    [
                        "Did the customer cancel manually or lose access through payment failure?",
                        "Divide the churn cohort into voluntary cancellations and involuntary payment failures before diagnosing causes.",
                        "RonBuilds ([FtbQGH3sZ3c @ 00:02:00])",
                    ],
                    [
                        "Does the headline churn number hide differences in customer revenue?",
                        "Track dollar churn because customer counts can conceal substantial differences in revenue lost.",
                        "Ask a VC ([su9KuGnbAW8 @ 00:00:50])",
                    ],
                    [
                        "Do the selected activation actions actually correlate with customers staying?",
                        "Verify the connection between first-video creation, photo editing, and retention rather than assuming it.",
                        "Business Beast Mode ([iGqudu6WmHs @ 00:01:08])",
                    ],
                    [
                        "Can the team identify which customer cohorts are actually leaving?",
                        "Instrument enrollment timing and subscription plan so churn can be examined by customer cohort.",
                        "Dan Martell ([2y-cxWkz_jQ @ 00:00:37])",
                    ],
                    [
                        "Does customer health measure outcomes as well as the relationship?",
                        "Design the health score to detect delivered outcomes and the appropriateness of customer experience.",
                        "CSM Practice ([YGbTHo5OkdI @ 00:02:32])",
                    ],
                    [
                        "Which specific loss event is the prediction model trying to anticipate?",
                        "Choose one churn definition per model and fix the window before building the prediction.",
                        "Gamify Data ([SFcHnbb87E8 @ 00:00:14])",
                    ],
                ],
            },
        },
        {
            "id": "street-mechanics-tools-numbers",
            "title": "Exact Street Mechanics, Tools & Numbers",
            "paragraphs": [
                (
                    "Hormozi's onboarding prescription is deliberately hands-on: run two group Zoom onboardings each day, one in the morning and one at night, and book new customers into onboarding when they sign up. "
                    "Walk them through the product, watch the friction, and get the video and editing actions completed in roughly 20 minutes. "
                    "The booking push is not limited to a passive dashboard button: Hormozi names text, calls, email, and making the booking the next step inside the signup flow. "
                    "He then segments by acquisition channel and customer avatar so the strongest customer groups can shape front-end messaging. "
                    "Billing is another lever in the same discussion. "
                    "The founder sells a $60 monthly package and a roughly $360 annual option, reporting that 40–50% now choose annual. "
                    "For customers selling only a few houses each year, Hormozi discusses quarterly or annual billing to align the billing cycle with the value cycle. "
                    "Vasco Aires uses human contact at the other end of the relationship: a client-success call during cancellation can reveal confusing interfaces or inadequate documentation. "
                    "RonBuilds adds the data plumbing needed to connect these interactions: set the user identifier in the application's database and share it with external tools so emails, support tickets, conversions, and value can be related to one person. "
                    "[iGqudu6WmHs @ 00:02:09] [iGqudu6WmHs @ 00:04:55] "
                    "[HrOp5FtcoxM @ 00:05:31] [FtbQGH3sZ3c @ 00:20:00]"
                ),
                (
                    "For payment recovery, configure the retry engine and the customer-facing path as distinct pieces of work. "
                    "In Churnkey's roundtable, Precision Retries are enabled through a toggle in advanced payment-recovery settings, while Stripe remains the source of truth for subscription status. "
                    "The recommendation is four Stripe retries within one month, alongside four or five Churnkey Precision Retries during that month. "
                    "Dodo Payments describes automatic retries for fixable failures such as insufficient funds, while skipping a stolen card; a successful attempt returns the subscription to active. "
                    "Its manual retry is separate from automatic attempts and is intended for moments such as a customer saying funds have just been added. "
                    "Freemius presents a built-in alternative: failed card or PayPal renewals retry one day later, then three days, then five, with update-link emails along the way. "
                    "Ecom Mastery shows GoHighLevel's payment-received trigger filtered to failed transactions, followed by an invoice or payment-link message, a wait, and an if/else payment-status check. "
                    "Success sends thanks and exits; an unresolved payment proceeds to the next reminder and retry. "
                    "After the final retry, the operator chooses the demonstrated cancellation or pause path and communicates that result. "
                    "These are specific platform workflows, each with its own settings and sequence, rather than one identical retry schedule applied everywhere. "
                    "[B-tr3MgFk_s @ 00:02:32] [kcrWGXCiECs @ 00:00:24] "
                    "[iJ-6ibkTVyg @ 00:00:50] [op7llsNLoJQ @ 00:03:31]"
                ),
                (
                    "Make the recovery message easy to recognize and the payment update easy to finish. "
                    "Churnkey's roundtable setup calls for a new custom billing subdomain, a destination after payment details are updated, and sender verification. "
                    "Its email guidance is plain text, two or three sentences, and a prominent call to action; later messages can place a discount directly in the subject line. "
                    "The same session describes an optional card attempt immediately before a later email: if that attempt succeeds, the email is suppressed. "
                    "Churnkey's multichannel presentation adds SMS with a one-tap link to mobile checkout, an in-app recovery wall, and a billing-contacts API for reaching the person who actually controls payment in a multiseat account. "
                    "RonBuilds concentrates personalization on activated, engaged users: match the message to expiry or insufficient funds, use in-app messaging, and remind power users of concrete value already received. "
                    "He also considers retargeting for valuable accounts, including an example of a $499 subscription, while checking that advertising cost does not outweigh customer value. "
                    "Ecom Mastery closes the loop through failed-payment counts, recovery rate, payment-failure churn, and average recovery time. "
                    "Those observations inform changes to the retry schedule or messaging, including whether most customers already resolve the problem after the first reminder. "
                    "[B-tr3MgFk_s @ 00:05:44] [vp4SwMY-QrM @ 00:01:27] "
                    "[FtbQGH3sZ3c @ 00:12:13] [op7llsNLoJQ @ 00:07:22]"
                ),
            ],
            "table": {
                "caption": "Concrete settings, customer actions, and recovery routes described by the operators.",
                "headers": ["Execution point", "Exact mechanism or stated number", "Expert Source"],
                "rows": [
                    [
                        "Replace passive onboarding with scheduled sessions that expose actual product friction.",
                        "Run two daily group Zoom onboardings and complete video creation and editing in about 20 minutes.",
                        "Business Beast Mode ([iGqudu6WmHs @ 00:02:09])",
                    ],
                    [
                        "Configure Stripe retries alongside the additional Churnkey precision recovery attempts.",
                        "Set four Stripe retries within one month; Churnkey also runs four to five during the month.",
                        "Churnkey ([B-tr3MgFk_s @ 00:02:32])",
                    ],
                    [
                        "Retry immediately when a customer reports that funds have become available.",
                        "Dodo's manual retry charges the saved card without consuming the separate automatic retry attempts.",
                        "Dodo Payments ([kcrWGXCiECs @ 00:01:03])",
                    ],
                    [
                        "Use the existing payment platform before adding another standalone recovery tool.",
                        "Freemius includes card and PayPal recovery, with retries one day later, then three, then five.",
                        "Freemius - Selling Software ([iJ-6ibkTVyg @ 00:00:31])",
                    ],
                    [
                        "Start the workflow only when the filtered payment event actually fails.",
                        "Use payment received, filter failed transactions, send the payment link, wait, then check status.",
                        "Ecom Mastery ([op7llsNLoJQ @ 00:03:31])",
                    ],
                    [
                        "Reach the account contact who can actually change the payment method.",
                        "Use the billing contacts API to route recovery messages to the billing administrator or account owner.",
                        "Churnkey ([vp4SwMY-QrM @ 00:02:02])",
                    ],
                    [
                        "Recover unfinished checkouts separately from customers whose existing subscription renewal failed.",
                        "Dodo sends checkout reminders with a return link and an optional small discount in those emails.",
                        "Dodo Payments ([kcrWGXCiECs @ 00:01:31])",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Small recovery details the practitioners explicitly use",
                "body": "Churnkey emphasizes attention and fewer unnecessary messages; RonBuilds adds a profitability check to retargeting.",
                "items": [
                    "Enable the pre-email payment attempt on later Churnkey messages: a successful charge suppresses the unnecessary email. The immediate first email cannot use this option. [Churnkey — B-tr3MgFk_s @ 00:10:19]",
                    "Churnkey suggests two or three sender names and explicitly allows fictitious names, while reporting that recognizable founders, CEOs, or marketing personalities produce the strongest opens and clicks. [Churnkey — B-tr3MgFk_s @ 00:15:22]",
                    "Keep recovery email copy to two or three sentences, make the payment button prominent, and place later-message discounts in the subject line when using them. [Churnkey — B-tr3MgFk_s @ 00:12:28]",
                    "Consider retargeting valuable failed-payment accounts when advertising cost remains below customer value; keep social-feed personalization limited rather than exposing personal details publicly. [RonBuilds — FtbQGH3sZ3c @ 00:13:47] [RonBuilds — FtbQGH3sZ3c @ 00:14:37]",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Split and diagnose the churn cohort",
                    "action": "Separate manual cancellations from payment failures, then inspect activation, engagement, and acquisition channel.",
                    "detail": "RonBuilds starts with voluntary versus involuntary churn and examines whether customers actually activated; channel comparisons can expose expectation mismatches before signup. [RonBuilds — FtbQGH3sZ3c @ 00:02:00]",
                },
                {
                    "step": 2,
                    "title": "Observe first value directly",
                    "action": "Book customers into hands-on onboarding and complete the selected activation actions with them.",
                    "detail": "Hormozi proposes two daily group Zoom sessions, watches customers encounter friction, and targets video creation plus editing in about 20 minutes. [Business Beast Mode — iGqudu6WmHs @ 00:02:09] [Business Beast Mode — iGqudu6WmHs @ 00:05:57]",
                },
                {
                    "step": 3,
                    "title": "Build the failed-payment recovery branch",
                    "action": "Trigger on a failed payment, send the payment link, wait, check status, and continue only if unresolved.",
                    "detail": "Ecom Mastery demonstrates GoHighLevel's payment-received trigger with a failed-transaction filter, a wait matching the retry gap, and a success branch that sends thanks and exits. [Ecom Mastery — op7llsNLoJQ @ 00:03:31]",
                },
                {
                    "step": 4,
                    "title": "Measure recovery and adjust the window",
                    "action": "Review failed payments, collected recoveries, unresolved losses, and recovery time before changing cadence.",
                    "detail": "Ecom Mastery monitors failed-payment count, recovery rate, payment-failure churn, and average recovery time; Recurly recommends experimenting with dunning lengths to find what works for the business. [Ecom Mastery — op7llsNLoJQ @ 00:07:22] [Recurly — eBy7DfSz09g @ 00:01:00]",
                },
            ],
        },
        {
            "id": "disagreements-alternative-playbooks",
            "title": "Where Practitioners Disagree & Alternative Playbooks",
            "paragraphs": [
                (
                    "The sharpest disagreement is how far automation can carry payment recovery. "
                    "Churnkey promotes an automated combination of retries, payment walls, and campaigns; its involuntary-churn presentation reports recovery of up to 70% of failed payments, while its multichannel presentation claims up to 89% across the channels it describes. "
                    "Gravy argues that dunning software and automated emails alone are not enough, saying 85% of people are not responsive to those efforts. "
                    "Its alternative has three ingredients: a person focused on recovery, a proven one-to-one communication process, and visibility into the recovery metric. "
                    "Gravy attributes over 70% of saved payments to a person sending a customized email and reports average recovery of 51% of failed revenue within 30 days. "
                    "Freemius puts a different question ahead of buying another service: what is already included in the payment platform? "
                    "It identifies built-in dunning, standalone software, and building internally as three routes, then says standalone tools offer more control but run from about $130 to $269 monthly. "
                    "Freemius includes its own dunning without an extra tool fee. "
                    "The choices therefore differ in staffing, platform packaging, and claimed results: Churnkey sells automation breadth, Gravy sells dedicated human attention, and Freemius tells sellers to inspect existing recovery numbers before purchasing another tool. "
                    "[O51fzGSuixY @ 00:02:07] [vp4SwMY-QrM @ 00:02:21] "
                    "[7MuS7PqfUyo @ 00:00:31] [iJ-6ibkTVyg @ 00:00:17]"
                ),
                (
                    "Cancellation handling also has competing operating styles. "
                    "Vasco Aires deliberately adds steps: a video and invitation to book a call, a cancellation-reason form requiring a substantive comment, an option to send feedback and wait for the team, and a final confirmation emphasizing what the customer loses. "
                    "Vasco explicitly rejects the extreme of making customers call during a narrow window, but still says the business tries to delay cancellation and gather as much feedback as possible. "
                    "Dan Martell's early-stage suggestion is a conversation before automatic cancellation, potentially through email, when the team does not yet understand why people leave; later, those responses can become self-cancellation choices and roadmap input. "
                    "Raaft centers the reason-matched response instead: show the next charge and exact end date for billing confusion, repair a broken cancellation path, offer human contact for support problems, and offer a cheaper plan or pause for price objections. "
                    "RonBuilds narrows where intensive save work belongs. "
                    "Activated, engaged, valuable customers with a clear reason may justify personalized win-back treatment; low-value, price-sensitive users who are unlikely to stay may not. "
                    "These approaches put different weight on conversation, deliberate cancellation friction, and matching the remedy to the reason. "
                    "Vasco's sequence also distinguishes a final cancellation from sending feedback and waiting, which leaves the subscription uncanceled. "
                    "[HrOp5FtcoxM @ 00:05:02] [2y-cxWkz_jQ @ 00:00:55] "
                    "[mDiVVA7DAh8 @ 00:00:56] [FtbQGH3sZ3c @ 00:07:31]"
                ),
                (
                    "Recovery timing is another choice the practitioners do not reduce to a universal schedule. "
                    "Recurly reports a 47% merchant median recovery rate for dunning windows of one to seven days and 57.7% for fifteen to twenty-one days. "
                    "The speaker observes higher recovery with longer cycles, then recommends experiments because individual businesses know their customers and differ from one another. "
                    "Freemius describes its included retries as one day later, then three, then five. "
                    "Churnkey's roundtable instead works through a month-long example: four Stripe retries, another four or five precision attempts, and emails spread across the customer's grace period. "
                    "For a 30-day grace period, the speaker gives days 1, 5, 7, 15, and 28 as an example and places the final email one or two days before access ends. "
                    "RonBuilds starts from observed payback behavior: determine when recovery usually happens and put communications in that period, whether the first two weeks or the first month. "
                    "He also limits deep personalization for customers who never activated, favoring a general dunning sequence while the team fixes onboarding. "
                    "The alternative playbooks therefore differ both in elapsed time and in which customers receive extra work. "
                    "Recurly's comparison supports testing window length; RonBuilds makes the customer's activation state part of deciding how much effort the sequence deserves. "
                    "[eBy7DfSz09g @ 00:00:21] [iJ-6ibkTVyg @ 00:00:50] "
                    "[B-tr3MgFk_s @ 00:16:14] [FtbQGH3sZ3c @ 00:17:40]"
                ),
            ],
            "table": {
                "caption": "Keep the competing approaches visible rather than collapsing their claims into one recipe.",
                "headers": ["Decision under debate", "Contrasting practitioner approaches", "Expert Source"],
                "rows": [
                    [
                        "Should recovery primarily run automatically or receive dedicated human attention?",
                        "Churnkey promotes automated multichannel recovery; Gravy emphasizes full-time ownership and personalized one-to-one follow-up.",
                        "Churnkey ([vp4SwMY-QrM @ 00:02:21]); Gravy ([7MuS7PqfUyo @ 00:00:31])",
                    ],
                    [
                        "Should the business purchase another tool before reviewing built-in recovery?",
                        "Freemius says inspect monthly failed, recovered, and silently lost renewals before paying for additional software.",
                        "Freemius - Selling Software ([iJ-6ibkTVyg @ 00:00:50])",
                    ],
                    [
                        "Should cancellation emphasize deliberate extra steps or reason-matched assistance?",
                        "Vasco uses multiple confirmations and feedback collection; Raaft emphasizes billing clarity and offers matching cancellation reasons.",
                        "Vasco Aires ([HrOp5FtcoxM @ 00:07:44]); Raaft ([mDiVVA7DAh8 @ 00:00:56])",
                    ],
                    [
                        "Should early customers self-cancel immediately or first explain their problem?",
                        "Martell suggests an early conversation by email, then using those responses to develop self-cancellation choices.",
                        "Dan Martell ([2y-cxWkz_jQ @ 00:00:55])",
                    ],
                    [
                        "Should the operator adopt a longer recovery window without further testing?",
                        "Recurly observes higher recovery over longer windows but recommends experiments to determine the business's own length.",
                        "Recurly ([eBy7DfSz09g @ 00:00:41])",
                    ],
                    [
                        "Should every departed customer receive the same depth of personalized win-back?",
                        "RonBuilds prioritizes activated, engaged, valuable customers and questions intensive work for low-value price-sensitive segments.",
                        "RonBuilds ([FtbQGH3sZ3c @ 00:07:31])",
                    ],
                    [
                        "Should annual billing replace monthly billing immediately after winning a test?",
                        "Hormozi suggests testing annual-only while retaining monthly temporarily for its faster feedback on unresolved churn.",
                        "Business Beast Mode ([iGqudu6WmHs @ 00:06:13])",
                    ],
                ],
            },
        },
        {
            "id": "failure-modes-economics-checks",
            "title": "Firsthand Failure Modes, Traps & Economics Checks",
            "paragraphs": [
                (
                    "A completed activation event can be a false signal. "
                    "RonBuilds describes teams copying actions performed by successful users, choosing an arbitrary repetition count, and declaring a habit without verifying that the action distinguishes customers who stay from those who leave. "
                    "If departing users perform the same event, that event alone does not prove activation. "
                    "He calls for checking the data and correlation rather than stopping at a retention curve. "
                    "The founder in Hormozi's discussion exposes the same gap by saying they believe first-video creation correlates with retention but would need to double-check. "
                    "Hormozi's response is to verify it, observe onboarding directly, and avoid scaling beyond the current position until the churn problem is fixed. "
                    "Vasco Aires supplies a concrete discovery from customer calls: some people want to cancel because they do not understand the product, possibly because the documentation is inadequate or the interface is confusing. "
                    "A ten-to-fifteen-minute conversation can uncover that issue and keep a customer. "
                    "Vasco also says the business still has churn and that improvements take time, describing one or two months before seeing an actual reduction. "
                    "The operational trap is confusing a checked box, a new feature, or a newly installed sequence with a demonstrated change in customer behavior. "
                    "[FtbQGH3sZ3c @ 00:15:34] [iGqudu6WmHs @ 00:00:51] "
                    "[iGqudu6WmHs @ 00:06:44] [HrOp5FtcoxM @ 00:05:50]"
                ),
                (
                    "A recovery workflow can look complete while still needing configuration. "
                    "Ecom Mastery demonstrates GoHighLevel's AI-generated automation, then points out that part of the if/else condition may need to be configured and describes the result as a useful skeleton. "
                    "The demonstration also calls for tweaking the unsuccessful branch to continue the retry workflow. "
                    "Churnkey's roundtable identifies a different operational miss: payment auto-retries are often not toggled on in customer campaigns, so the opportunity to collect immediately before sending a reminder is unused. "
                    "The same speaker calls the failed-payment wall the most underutilized recovery product encountered on customer calls, despite seeing teams use it effectively. "
                    "Retry intensity has its own trap. "
                    "The roundtable warns that eight attempts in the first two weeks might draw pushback from card companies or look suspicious, and instead recommends its stated month-long arrangement with Stripe. "
                    "Dodo draws the failure-reason boundary explicitly: retry insufficient funds, but skip a stolen card; when the card needs replacing, move to update-link reminders rather than expecting retries to fix it. "
                    "The operational distinctions are specific: an automation skeleton still needs its conditions configured, an available recovery option can remain switched off, and a dead payment method needs customer action rather than another ordinary attempt. "
                    "[op7llsNLoJQ @ 00:10:54] [B-tr3MgFk_s @ 00:10:02] "
                    "[B-tr3MgFk_s @ 00:02:50] [kcrWGXCiECs @ 00:00:24]"
                ),
                (
                    "Keep the economics and evidence checks attached to the recovery work. "
                    "Ryan Floyd warns that expansion in some accounts can hide gross churn, so both gross and net figures matter. "
                    "He also cautions that monthly churn views can be misleading when customers pay annually and only some contracts come up for renewal during the period. "
                    "Gamify Data names a prediction failure that can make the dashboard look much better than the deployed model: letting a cancellation ticket enter inputs that are supposed to represent an earlier scoring date. "
                    "Build inputs as of that date, test on later renewals, and compare the model with an existing rule such as usage falling more than 30%. "
                    "If the model cannot beat the rule, keep the rule. "
                    "Raaft separates evidence of reasons from evidence of successful saves: its review analysis found 53 leaving accounts among 1,024 reviews, with overlapping explanations, but those reviews cannot establish which intervention would have worked. "
                    "RonBuilds adds a direct reminder that failed-payment loss can be accidental: after receiving a new card, they forgot to update subscriptions and experienced involuntary cancellations. "
                    "Their wider recovery approach still checks customer value before investing heavily in discounts or retargeting. "
                    "Recovered revenue, expansion, and prediction scores each need the particular checks their practitioners describe. "
                    "[su9KuGnbAW8 @ 00:02:54] [SFcHnbb87E8 @ 00:00:31] "
                    "[mDiVVA7DAh8 @ 00:00:19] [FtbQGH3sZ3c @ 00:11:07]"
                ),
            ],
            "table": {
                "caption": "Observed bottlenecks and explicit checks before interpreting a retention improvement.",
                "headers": ["Failure or misleading signal", "Practitioner check or reported correction", "Expert Source"],
                "rows": [
                    [
                        "Customers complete the supposed activation event but still leave the product.",
                        "Verify correlation and check whether departing users perform the same event before declaring it activation.",
                        "RonBuilds ([FtbQGH3sZ3c @ 00:15:34])",
                    ],
                    [
                        "Cancellation conversations reveal that customers never understood how the product worked.",
                        "Vasco reports discovering confusing interfaces or inadequate documentation through short client-success conversations with canceling customers.",
                        "Vasco Aires ([HrOp5FtcoxM @ 00:05:50])",
                    ],
                    [
                        "The generated recovery workflow appears finished while its conditions remain incomplete.",
                        "Ecom Mastery says the status condition may need configuration and the unsuccessful branch needs tweaking.",
                        "Ecom Mastery ([op7llsNLoJQ @ 00:10:54])",
                    ],
                    [
                        "A dense retry schedule attracts unwanted scrutiny from the card companies.",
                        "Churnkey warns about eight attempts in two weeks and recommends four Stripe attempts within one month.",
                        "Churnkey ([B-tr3MgFk_s @ 00:02:50])",
                    ],
                    [
                        "Account expansion makes the net result obscure the actual canceled business.",
                        "Floyd says to examine gross churn separately because expansion can hide cancellation problems in other accounts.",
                        "Ask a VC ([su9KuGnbAW8 @ 00:04:02])",
                    ],
                    [
                        "The prediction test includes information unavailable when the real score would run.",
                        "Build inputs as of the scoring day and exclude later cancellation tickets that create data leakage.",
                        "Gamify Data ([SFcHnbb87E8 @ 00:00:31])",
                    ],
                    [
                        "Reasons collected from reviews are mistaken for demonstrated evidence of successful saves.",
                        "Raaft says reviews reveal what went wrong but cannot show which retention offer would have worked.",
                        "Raaft ([mDiVVA7DAh8 @ 00:01:13])",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Checks that keep the recovery work tied to the actual problem",
                "body": "Use the practitioners' own failure checks for activation, automation, prediction, and customer economics.",
                "items": [
                    "Check whether the proposed activation event distinguishes retained users from departing users; RonBuilds warns that an event everyone performs is not proof of activation. [RonBuilds — FtbQGH3sZ3c @ 00:16:11]",
                    "Inspect the generated payment-status condition and unsuccessful branch; Ecom Mastery describes the AI-built workflow as a skeleton with configuration still needed. [Ecom Mastery — op7llsNLoJQ @ 00:10:54]",
                    "Keep future cancellation information out of prediction inputs, test on later renewals, and retain the existing usage rule if the model cannot beat it. [Gamify Data — SFcHnbb87E8 @ 00:00:31] [Gamify Data — SFcHnbb87E8 @ 00:01:01]",
                    "Check cohort value before spending heavily on personalized price offers, and keep retargeting cost from outweighing customer value. [RonBuilds — FtbQGH3sZ3c @ 00:07:31] [RonBuilds — FtbQGH3sZ3c @ 00:14:37]",
                ],
            },
        },
    ],
    "pull_quote": (
        '"We want the value cycle to be aligned with the billing cycle." '
        "— Alex Hormozi, Business Beast Mode (iGqudu6WmHs @ 00:05:09)."
    ),
    "diagram_id": "diag-08",
    "action_checklist": [
        "Split churn into manual cancellations and payment failures, then compare activation, engagement, and acquisition channel within those groups. [RonBuilds — FtbQGH3sZ3c @ 00:02:00]",
        "Run hands-on group onboarding, complete the intended first-value actions, and verify that those actions correlate with staying. [Business Beast Mode — iGqudu6WmHs @ 00:01:08] [Business Beast Mode — iGqudu6WmHs @ 00:05:57]",
        "Build a health view that includes customer outcomes and relationship quality, then route at-risk customers to support or customer success. [CSM Practice — YGbTHo5OkdI @ 00:02:32] [Dan Martell — 2y-cxWkz_jQ @ 00:02:35]",
        "Ask why the customer is leaving and match the response: clarify billing, offer human help, offer a cheaper plan or pause, or route product failures to the person who can fix them. [Raaft — mDiVVA7DAh8 @ 00:00:56]",
        "Configure failed-payment retries and update-link reminders, use in-app recovery for customers still using the product, and route multiseat billing messages to the responsible contact. [Dodo Payments — kcrWGXCiECs @ 00:00:24] [Churnkey — vp4SwMY-QrM @ 00:01:45]",
        "Review failed, recovered, and silently lost renewals each month; experiment with dunning window lengths rather than adopting the benchmark window without testing. [Freemius - Selling Software — iJ-6ibkTVyg @ 00:00:50] [Recurly — eBy7DfSz09g @ 00:01:00]",
    ],
    "statutory_citations": [
        {
            "title": "RonBuilds — How to Recover Failed Payments and Cancellations in B2C SaaS (Full Lifecycle Flow) [00:02:00]",
            "url": "https://www.youtube.com/watch?v=FtbQGH3sZ3c&t=120s",
            "relevance": "Primary practitioner testimony on separating voluntary cancellation from involuntary payment failure and diagnosing the customer cohort.",
        },
        {
            "title": "Business Beast Mode — Alex Hormozi: Fix SaaS Churn With This Onboarding Strategy (AMA) [00:02:09]",
            "url": "https://www.youtube.com/watch?v=iGqudu6WmHs&t=129s",
            "relevance": "Primary practitioner testimony on twice-daily hands-on onboarding and observing friction before scaling.",
        },
        {
            "title": "Churnkey — Retention Roundtable - Reducing Involuntary Churn with Payment Recovery [00:02:32]",
            "url": "https://www.youtube.com/watch?v=B-tr3MgFk_s&t=152s",
            "relevance": "Primary practitioner testimony on coordinating Stripe Smart Retries with Churnkey Precision Retries.",
        },
        {
            "title": "Gravy — Why Dunning Software Is Not Enough - Gravy [00:00:31]",
            "url": "https://www.youtube.com/watch?v=7MuS7PqfUyo&t=31s",
            "relevance": "Primary practitioner testimony on dedicated recovery ownership, personalized communication, and visibility.",
        },
    ],
    "source_citations": [
        {
            "source_type": "video_pro_tip",
            "video_id": "iGqudu6WmHs",
            "title": "Alex Hormozi: Fix SaaS Churn With This Onboarding Strategy (AMA)",
            "channel": "Business Beast Mode",
            "author": "Business Beast Mode",
            "text": "We want the value cycle to be aligned with the billing cycle.",
            "tip": "We want the value cycle to be aligned with the billing cycle.",
            "timestamp": 309,
            "timestamp_seconds": 309,
            "timestamp_label": "[00:05:09]",
            "url": "https://www.youtube.com/watch?v=iGqudu6WmHs&t=309s",
            "markdown": "[00:05:09](https://www.youtube.com/watch?v=iGqudu6WmHs&t=309s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on aligning subscription billing with the customer's value cycle.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "O51fzGSuixY",
            "title": "Recover More Failed Payments: The Churnkey Involuntary Churn Engine",
            "channel": "Churnkey",
            "author": "Churnkey",
            "text": "Together, they recovered up to 70% of all failed payments. Retries are the most effective. Most failed payments aren't final. They're temporary.",
            "tip": "Together, they recovered up to 70% of all failed payments. Retries are the most effective. Most failed payments aren't final. They're temporary.",
            "timestamp": 145,
            "timestamp_seconds": 145,
            "timestamp_label": "[00:02:25]",
            "url": "https://www.youtube.com/watch?v=O51fzGSuixY&t=145s",
            "markdown": "[00:02:25](https://www.youtube.com/watch?v=O51fzGSuixY&t=145s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the combined recovery claim and the role of retries.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "vp4SwMY-QrM",
            "title": "How to Recover 89% of Failed Payments (SaaS Dunning Strategy)",
            "channel": "Churnkey",
            "author": "Churnkey",
            "text": "Together, these channels recover up to 89% of failed payments.",
            "tip": "Together, these channels recover up to 89% of failed payments.",
            "timestamp": 141,
            "timestamp_seconds": 141,
            "timestamp_label": "[00:02:21]",
            "url": "https://www.youtube.com/watch?v=vp4SwMY-QrM&t=141s",
            "markdown": "[00:02:21](https://www.youtube.com/watch?v=vp4SwMY-QrM&t=141s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the multichannel recovery claim following the explanation of billing-contact routing.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "FtbQGH3sZ3c",
            "title": "How to Recover Failed Payments and Cancellations in B2C SaaS (Full Lifecycle Flow)",
            "channel": "RonBuilds",
            "author": "RonBuilds",
            "text": "One of the first things I do is take a cohort of the people who have payment failures and cancellations, people who have churned, and I break that down into voluntary and involuntary.",
            "tip": "One of the first things I do is take a cohort of the people who have payment failures and cancellations, people who have churned, and I break that down into voluntary and involuntary.",
            "timestamp": 120,
            "timestamp_seconds": 120,
            "timestamp_label": "[00:02:00]",
            "url": "https://www.youtube.com/watch?v=FtbQGH3sZ3c&t=120s",
            "markdown": "[00:02:00](https://www.youtube.com/watch?v=FtbQGH3sZ3c&t=120s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the initial voluntary-versus-involuntary cohort split.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "kcrWGXCiECs",
            "title": "Stop Losing SaaS Revenue to Failed Payments - 4 Fixes with Dodo Payments",
            "channel": "Dodo Payments",
            "author": "Dodo Payments",
            "text": "It retries the fixable stuff like insufficient funds and skips the hopeless stuff like a stolen card.",
            "tip": "It retries the fixable stuff like insufficient funds and skips the hopeless stuff like a stolen card.",
            "timestamp": 24,
            "timestamp_seconds": 24,
            "timestamp_label": "[00:00:24]",
            "url": "https://www.youtube.com/watch?v=kcrWGXCiECs&t=24s",
            "markdown": "[00:00:24](https://www.youtube.com/watch?v=kcrWGXCiECs&t=24s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on distinguishing retryable payment failures from failures needing a different response.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "su9KuGnbAW8",
            "title": "AskAVC #2 - SaaS Churn: what is it?",
            "channel": "Ask a VC",
            "author": "Ask a VC",
            "text": "If you have a lot of expansion in some accounts, you may miss some of what the gross churn is as well.",
            "tip": "If you have a lot of expansion in some accounts, you may miss some of what the gross churn is as well.",
            "timestamp": 242,
            "timestamp_seconds": 242,
            "timestamp_label": "[00:04:02]",
            "url": "https://www.youtube.com/watch?v=su9KuGnbAW8&t=242s",
            "markdown": "[00:04:02](https://www.youtube.com/watch?v=su9KuGnbAW8&t=242s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on keeping gross churn visible alongside expansion and net churn.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "op7llsNLoJQ",
            "title": "GoHighLevel Payment Dunning Tutorial: Failed Payment Recovery for Subscriptions",
            "channel": "Ecom Mastery",
            "author": "Ecom Mastery",
            "text": "Now, it looks like some of this might need to be configured, but again, at least you have a really good skeleton here to start from and you're not staring at a blank automation screen.",
            "tip": "Now, it looks like some of this might need to be configured, but again, at least you have a really good skeleton here to start from and you're not staring at a blank automation screen.",
            "timestamp": 654,
            "timestamp_seconds": 654,
            "timestamp_label": "[00:10:54]",
            "url": "https://www.youtube.com/watch?v=op7llsNLoJQ&t=654s",
            "markdown": "[00:10:54](https://www.youtube.com/watch?v=op7llsNLoJQ&t=654s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on configuration still required after generating the recovery workflow with AI.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "iJ-6ibkTVyg",
            "title": "Dunning Software: Recover Lost MRR From Failed Payments",
            "channel": "Freemius - Selling Software",
            "author": "Freemius - Selling Software",
            "text": "You retry the payment, remind the customer, and give them an easy way to update their card. There are three ways to run it. Either it's built into your payment platform, you use a standalone tool on top, or you build it yourself.",
            "tip": "You retry the payment, remind the customer, and give them an easy way to update their card. There are three ways to run it. Either it's built into your payment platform, you use a standalone tool on top, or you build it yourself.",
            "timestamp": 17,
            "timestamp_seconds": 17,
            "timestamp_label": "[00:00:17]",
            "url": "https://www.youtube.com/watch?v=iJ-6ibkTVyg&t=17s",
            "markdown": "[00:00:17](https://www.youtube.com/watch?v=iJ-6ibkTVyg&t=17s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on dunning mechanics and the built-in, standalone, or self-built implementation choices.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "HrOp5FtcoxM",
            "title": "How to Reduce SaaS Churn to 0% (flow revealed)",
            "channel": "Vasco Aires",
            "author": "Vasco Aires",
            "text": "Oftentimes people just cancel because they don't understand how the product works, maybe because our documentation isn't good enough, maybe because our UI is confusing.",
            "tip": "Oftentimes people just cancel because they don't understand how the product works, maybe because our documentation isn't good enough, maybe because our UI is confusing.",
            "timestamp": 350,
            "timestamp_seconds": 350,
            "timestamp_label": "[00:05:50]",
            "url": "https://www.youtube.com/watch?v=HrOp5FtcoxM&t=350s",
            "markdown": "[00:05:50](https://www.youtube.com/watch?v=HrOp5FtcoxM&t=350s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on usability and documentation problems uncovered during cancellation conversations.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "B-tr3MgFk_s",
            "title": "Retention Roundtable - Reducing Involuntary Churn with Payment Recovery",
            "channel": "Churnkey",
            "author": "Churnkey",
            "text": "If you're leveraging Stripe Smart Retries with Churnkey's Precision Retries, which is our recommendation, we recommend that you set the retry schedule from Stripe for four times within one month.",
            "tip": "If you're leveraging Stripe Smart Retries with Churnkey's Precision Retries, which is our recommendation, we recommend that you set the retry schedule from Stripe for four times within one month.",
            "timestamp": 152,
            "timestamp_seconds": 152,
            "timestamp_label": "[00:02:32]",
            "url": "https://www.youtube.com/watch?v=B-tr3MgFk_s&t=152s",
            "markdown": "[00:02:32](https://www.youtube.com/watch?v=B-tr3MgFk_s&t=152s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the recommended Stripe retry schedule when paired with Precision Retries.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "7MuS7PqfUyo",
            "title": "Why Dunning Software Is Not Enough - Gravy",
            "channel": "Gravy",
            "author": "Gravy",
            "text": "We've created a framework for payment recovery that's saving on average 51% of failed revenue within 30 days for businesses all across North America.",
            "tip": "We've created a framework for payment recovery that's saving on average 51% of failed revenue within 30 days for businesses all across North America.",
            "timestamp": 80,
            "timestamp_seconds": 80,
            "timestamp_label": "[00:01:20]",
            "url": "https://www.youtube.com/watch?v=7MuS7PqfUyo&t=80s",
            "markdown": "[00:01:20](https://www.youtube.com/watch?v=7MuS7PqfUyo&t=80s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the average recovery result claimed for Gravy's recovery framework.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "mDiVVA7DAh8",
            "title": "How To Reduce SaaS Churn: I Analyzed 1,024 Reviews Across 41 Companies",
            "channel": "Raaft",
            "author": "Raaft",
            "text": "These reviews show what went wrong. They can't show which save would have worked. That's the part you have to test.",
            "tip": "These reviews show what went wrong. They can't show which save would have worked. That's the part you have to test.",
            "timestamp": 73,
            "timestamp_seconds": 73,
            "timestamp_label": "[00:01:13]",
            "url": "https://www.youtube.com/watch?v=mDiVVA7DAh8&t=73s",
            "markdown": "[00:01:13](https://www.youtube.com/watch?v=mDiVVA7DAh8&t=73s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on distinguishing cancellation reasons from tested retention interventions.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "YGbTHo5OkdI",
            "title": "How to Reduce SaaS Churn by Identifying At-Risk Customers Early",
            "channel": "CSM Practice",
            "author": "CSM Practice",
            "text": "You want to really ask yourself: is my health score designed to detect whether I am delivering outcomes as well as the appropriate customer experience.",
            "tip": "You want to really ask yourself: is my health score designed to detect whether I am delivering outcomes as well as the appropriate customer experience.",
            "timestamp": 152,
            "timestamp_seconds": 152,
            "timestamp_label": "[00:02:32]",
            "url": "https://www.youtube.com/watch?v=YGbTHo5OkdI&t=152s",
            "markdown": "[00:02:32](https://www.youtube.com/watch?v=YGbTHo5OkdI&t=152s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on measuring both customer outcomes and customer experience in account health.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "2y-cxWkz_jQ",
            "title": "How To Reduce Your SaaS Churn",
            "channel": "Dan Martell",
            "author": "Dan Martell",
            "text": "Step number one, instrument your metrics. Most SaaS founders have no clue what cohort of customers are actually churning and at what rate.",
            "tip": "Step number one, instrument your metrics. Most SaaS founders have no clue what cohort of customers are actually churning and at what rate.",
            "timestamp": 37,
            "timestamp_seconds": 37,
            "timestamp_label": "[00:00:37]",
            "url": "https://www.youtube.com/watch?v=2y-cxWkz_jQ&t=37s",
            "markdown": "[00:00:37](https://www.youtube.com/watch?v=2y-cxWkz_jQ&t=37s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on cohort instrumentation as the first retention step.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "eBy7DfSz09g",
            "title": "Dunning: 5 do's and don’ts to minimize subscriber churn | Recovery benchmarks",
            "channel": "Recurly",
            "author": "Recurly",
            "text": "The best way to determine your actual dunning window is really to experiment with different lengths to see what gets the best results for your company.",
            "tip": "The best way to determine your actual dunning window is really to experiment with different lengths to see what gets the best results for your company.",
            "timestamp": 60,
            "timestamp_seconds": 60,
            "timestamp_label": "[00:01:00]",
            "url": "https://www.youtube.com/watch?v=eBy7DfSz09g&t=60s",
            "markdown": "[00:01:00](https://www.youtube.com/watch?v=eBy7DfSz09g&t=60s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on using window-length experiments rather than adopting a benchmark unchanged.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "SFcHnbb87E8",
            "title": "SaaS Churn Prediction: How to Predict Churn Before Renewal",
            "channel": "Gamify Data",
            "author": "Gamify Data",
            "text": "If the model can't beat that rule, keep the rule.",
            "tip": "If the model can't beat that rule, keep the rule.",
            "timestamp": 61,
            "timestamp_seconds": 61,
            "timestamp_label": "[00:01:01]",
            "url": "https://www.youtube.com/watch?v=SFcHnbb87E8&t=61s",
            "markdown": "[00:01:01](https://www.youtube.com/watch?v=SFcHnbb87E8&t=61s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on comparing churn prediction with an existing operational rule.",
        },
    ],
}
