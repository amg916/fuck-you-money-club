"""Printable operator worksheets for FYMC Volume 004."""


def build_volume_004_workbook() -> dict:
    """Return a fresh workbook with independent nested worksheet records."""
    def sheet(number, title, refs, purpose, instructions, rows, gate):
        return {
            "worksheet_id": f"ws-{number:02d}",
            "number": number,
            "title": title,
            "purpose": purpose,
            "chapter_ref": refs,
            "instructions": instructions,
            "fields": [
                {"name": name, "type": "textarea", "prompt": prompt, "example": example}
                for name, prompt, example in rows
            ],
            "completion_gate": gate,
        }

    worksheets = [
        sheet(1, "Vertical B2B Wedge, G2 1-Star Pain & Paid-Pilot Validation Sheet",
              "Q1, Q6", "Validate one recurring buyer problem with paid pilot evidence.", [
                  "Print one sheet per vertical and date every source.",
                  "Read negative reviews in context; distinguish old defects from current gaps.",
                  "Interview buyers about frequency, workaround costs, and purchasing authority.",
                  "Offer a bounded paid pilot and record cash separately from verbal interest.",
              ], [
                  ("Vertical wedge", "Name buyer, recurring task, and narrow outcome.", "Freight brokers: extract shipment exceptions into a review queue."),
                  ("Review evidence", "Record G2 URLs, dates, product versions, and short 1-star pain excerpts.", "REV-01, dated capture: manual re-entry; verify on current version."),
                  ("Pain frequency", "Record interviews, occurrences per month, and time lost.", "INT-03: 40 exceptions/month at 15 minutes each."),
                  ("Workaround cost", "Calculate hours times loaded hourly cost; label estimates.", "10 hours x $40 = $400/month estimated labor."),
                  ("Buyer authority", "Identify user, budget owner, and purchase path.", "Dispatcher uses; operations manager approves $200/month."),
                  ("Pilot offer", "Specify price, duration, scope, delivery, and acceptance test.", "$150 for 14 days; 50 records; buyer reviews extraction accuracy."),
                  ("Paid evidence", "Log prospects, offers, payments, refunds, and receipt references.", "10 interviews; 4 offers; 2 paid; $300 collected; no refunds."),
                  ("Decision", "Set thresholds before testing; record Build, Revise, or Stop and counterevidence.", "Build after 2 paid pilots; revise if both require unrelated workflows."),
              ], "Dated pain evidence, payment records, acceptance criteria, and a decision are recorded."),
        sheet(2, "Hybrid Seat + Token Metering, Cloud-Credit Cliff & Gross-Margin Calculator",
              "Q3, Q4", "Price usage sustainably before temporary cloud credits expire.", [
                  "Use one monthly period and currency; label forecasts and actuals.",
                  "Separate seat revenue, included usage, and billable overages.",
                  "Calculate uncapped provider cost, including retries and failed requests.",
                  "Compare subsidized and post-credit economics; use N/A for zero denominators.",
              ], [
                  ("Seats", "Enter paid seats and realized monthly seat price excluding tax.", "10 seats x $30 = $300."),
                  ("Included allowance", "Define pooled or per-seat token allowance and reset policy.", "Pooled 2 million tokens/month; no rollover."),
                  ("Metering ledger", "Define tenant attribution, token source, deduplication, and invoice reconciliation.", "Unique request ID; input/output counters; retries cost us but are not rebilled."),
                  ("Overages", "Compute max(0, billable usage - allowance) x overage rate.", "3M - 2M = 1M excess; $40/M yields $40."),
                  ("Provider cost", "Sum input, output, cache, tool, and retry charges at dated rates.", "Illustrative: input $12 + output $24 + retries $4 = $40."),
                  ("Other COGS", "Add hosting, storage, payment fees, and delivery support without double counting.", "$25 hosting + $10 fees + $25 support = $60."),
                  ("Credit cliff", "Record eligible credits, expiry, burn, and full-rate cost after expiry.", "$200 remaining; $40/month eligible burn; expiry in 2 months wins over 5-month runway."),
                  ("Margin and limits", "GM = (net revenue - full COGS) / net revenue; compare cash cost after credits and stress usage.", "$340 revenue; $100 COGS; GM 70.6%; $40 credit gives 82.4% subsidized margin; test 2x usage."),
              ], "Usage reconciles to invoices and post-credit margin supports the chosen price and usage limits."),
        sheet(3, "Multi-Tenant RLS, Model-Router, Semantic-Cache & Prompt-Injection Audit",
              "Q5, Q7", "Test tenant isolation and model execution boundaries before pilot access.", [
                  "Use synthetic data and two authorized test tenants.",
                  "Test reads, writes, exports, storage, and background jobs across tenant boundaries.",
                  "Exercise routing failures, cache separation, and hostile retrieved text.",
                  "Record expected versus actual results and rerun repaired failures.",
              ], [
                  ("Tenant identities", "Map authenticated users to server-validated tenant membership.", "User A belongs only to tenant A; forged tenant B header rejected."),
                  ("RLS policies", "Record Row-Level Security (RLS) read/write policy and privileged-role bypass handling.", "Tenant key required; service credentials never reach browser."),
                  ("Isolation tests", "Log attempts to access another tenant's IDs, exports, files, and jobs.", "TEST-12: tenant A cannot download tenant B export; denied."),
                  ("Model router", "Specify task tiers, quality threshold, budget, and fallback.", "Cheap extraction first; escalate low confidence; stop after one retry."),
                  ("Semantic cache", "Define tenant, permission, model, prompt-version keys and invalidation.", "Tenant-scoped cache; revoke access invalidates entries; no cross-tenant similarity hits."),
                  ("Injection probes", "Test retrieved instructions trying to override task or request secrets.", "Synthetic document requests unrelated export; ignored; no tool executed."),
                  ("Tool boundary", "List allowlisted operations and server-side authorization checks.", "Read shipment tool validates tenant membership on every call."),
                  ("Audit outcomes", "Record test ID, actual result, evidence, owner, and retest date.", "CACHE-02 failed; owner Alex adds tenant filter; retest passes with saved trace."),
              ], "Cross-tenant and injection probes pass; routing, cache, and tool failures have recorded outcomes."),
    ]
    worksheets.extend([
        sheet(4, "Enterprise Trust, Zero-Data-Retention (ZDR) DPA & ROSCA Cancel Checklist",
              "Q2, Q9", "Document verifiable data commitments and test subscription cancellation.", [
                  "Map customer data through every processor, log, backup, and support tool.",
                  "Verify ZDR eligibility by provider, endpoint, and account; do not infer it from no-training terms.",
                  "Match the DPA and trust answers to implemented controls and retention periods.",
                  "Review ROSCA applicability and test disclosures, express consent, and simple cancellation.",
              ], [
                  ("Data map", "List data categories, purpose, destination, and owner.", "Shipment text -> extraction endpoint; billing data -> payment processor."),
                  ("ZDR evidence", "Record written approval, covered endpoints, exclusions, and verification date.", "Approval Z-01 covers endpoint A; file uploads excluded and disabled."),
                  ("Retention schedule", "Separate provider retention from application logs, caches, and backups.", "Payload logs off; cache 24h; backup deletion window 30 days."),
                  ("DPA register", "Record controller/processor roles, subprocessors, transfers, deletion, and incident terms.", "DPA v2 lists hosting and inference providers; deletion request owner assigned."),
                  ("Trust evidence", "Link access controls, encryption, incident contact, and accurate assurance statements.", "MFA enabled; TLS tested; no certification claimed without evidence."),
                  ("Subscription disclosure", "Capture price, interval, trial conversion, renewal, and consent evidence before charging.", "$30/seat monthly displayed beside purchase; consent event stored with terms version."),
                  ("Cancel test", "Record customer path, effective date, receipt, and future-charge suppression.", "Settings -> Cancel; access ends at period end; next invoice suppressed in test."),
                  ("Exceptions and owners", "Record gaps, applicability review, remedy owner, and retest evidence.", "Upload route lacked ZDR coverage; disabled; endpoint inventory rechecked."),
              ], "Claims match documented controls; retention exceptions are explicit and cancellation stops future renewals."),
        sheet(5, 'Scanner Outbound, "[Competitor] Alternative", Chrome Extension & GEO Tracker',
              "Q8, Q10", "Measure qualified acquisition across four channels without confusing visibility with revenue.", [
                  "Assign campaign IDs, dated evidence, and one conversion definition per channel.",
                  "Use permitted public observations for scanner outreach; honor opt-outs.",
                  "Publish accurate comparisons and keep extension permissions minimal.",
                  "Repeat generative engine optimization (GEO) queries with recorded context; attribute pilots separately.",
              ], [
                  ("Channel hypothesis", "Name buyer, pain signal, offer, and campaign owner.", "OPS-01: brokers with manual shipment intake; offer a paid pilot."),
                  ("Scanner evidence", "Record permitted source, observed issue, date, and validation before outreach.", "Public intake page requires copy/paste; manually verified; no private system probing."),
                  ("Outbound funnel", "Track delivered messages, positive replies, meetings, paid pilots, and opt-outs.", "40 delivered; 6 positive replies; 3 meetings; 1 paid pilot; 2 suppressed contacts."),
                  ("Alternative page", "Record competitor, comparison sources, dates, use-case fit, and landing-page conversion.", "Comparison v1: current published features cited; 100 sessions, 3 pilot requests."),
                  ("Chrome extension", "Define useful workflow, minimum permissions, activation event, and installation source.", "User-triggered extraction on selected tab; 20 installs, 8 first successful runs."),
                  ("GEO observations", "Log engine, date, query, locale, signed-in state, citations, and repeat count.", "Five fresh runs of a broker-software query; cited twice; not treated as two customers."),
                  ("Attribution and CAC", "Deduplicate customers; record attribution model, spend, labor, and new paying accounts.", "First-touch OPS-01; $120 spend + $80 labor / 2 new accounts = $100 CAC."),
                  ("Channel decision", "Compare qualified conversions and retained revenue; set next test budget.", "Continue outbound for 7 days at $100 cap; revise extension activation flow."),
              ], "All four channels have evidence or explicit not-tested status, deduplicated outcomes, and a next action."),
        sheet(6, "30-Day MVP Launch Sprint, Smart-Dunning & Exit-Readiness MRR Scorecard",
              "Q11, Q12", "Ship a bounded MVP and reconcile recurring revenue into an inspectable operating record.", [
                  "Assign one owner, dated deliverable, and acceptance test to each sprint week.",
                  "Launch only the validated workflow; track incidents and buyer acceptance.",
                  "Test dunning with synthetic payment failures and idempotent billing events.",
                  "Reconcile MRR movements to subscriptions; separate cash, pilots, and usage revenue.",
              ], [
                  ("Days 1-7", "Record paid-pilot target, interviews, scope, and stop criterion.", "Two paid pilots; one extraction workflow; stop if no buyer pays."),
                  ("Days 8-14", "Specify working vertical slice and isolation acceptance tests.", "Upload -> extract -> review -> export; both tenant isolation tests pass."),
                  ("Days 15-21", "Record billing, metering, cancellation, and onboarding tests.", "Synthetic checkout and cancellation pass; usage reconciles to invoice."),
                  ("Days 22-30", "Record pilot outcomes, incidents, launch decision, and next owner.", "Two pilots accepted; one converted; publish bounded offer on day 30."),
                  ("Smart dunning", "Define retry timing, decline handling, notices, grace period, and recovery evidence.", "Retry eligible soft declines on days 1/3/7; hard declines request payment update; duplicate webhook ignored."),
                  ("MRR bridge", "Closing MRR = opening + new + expansion - contraction - churn; state recognition policy.", "$1,000 + $300 + $100 - $50 - $150 = $1,200; exclude pilots and variable overages; annual plans / 12."),
                  ("Retention and collections", "NRR = (opening + expansion - contraction - churn) / opening; separate recovered cash.", "NRR = 900 / 1,000 = 90%; $60 recovered cash is not new MRR; zero opening means N/A."),
                  ("Exit-readiness record", "Link reconciled billing, churn cohorts, COGS, concentration, IP ownership, and runbooks; mark gaps.", "Billing export reconciled; top customer 25% MRR; contractor IP record missing, owner Alex due day 30."),
              ], "Sprint deliverables have evidence, dunning is tested, and the MRR bridge reconciles with explicit data gaps."),
    ])
    return {
        "workbook_id": "wb-004-ai-powered-micro-saas",
        "volume_id": "vol-004-ai-powered-micro-saas",
        "title": "AI-Powered Micro SaaS — Operator Companion Workbook",
        "subtitle": "6 Printable Worksheets for Paid Validation, SaaS Economics, Secure Delivery & Launch Execution",
        "worksheets": worksheets,
    }
