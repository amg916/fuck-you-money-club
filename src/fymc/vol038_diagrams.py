"""Volume 038 diagram data: Contingent Corporate Bill-Audit & Tax-Credit Recovery."""

from typing import Dict, List

VOLUME_038_SUBTITLE: str = (
    "No Savings, No Fee: GSR Late-Package Refunds, Surcharge Rerating, Carrier "
    "Contract Engineering, Utility and Expense Audits, Property Tax Appeals, Cost "
    "Segregation and 179D, WOTC Capture, Shared-Savings Deals, and Reverse Audits"
)


def build_volume_038_diagrams_data() -> List[Dict]:
    return [
        {
            "diagram_id": "diag-01-gsr-refund-recovery-workflow",
            "chapter_number": 1,
            "title": "Small-Parcel GSR Refund Recovery Workflow",
            "subtitle": "From billing credentials to phone-escalated late-package refunds",
            "chart_type": "process_flow",
            "stages": [
                {
                    "step": "01",
                    "label": "Billing Credential Handoff",
                    "value": "Step 1",
                    "detail": (
                        "Take the shipper's online billing credentials; Refund Retriever "
                        "compares its constant invoice and shipping monitoring to mint.com."
                    ),
                },
                {
                    "step": "02",
                    "label": "Invoice Auto-Download",
                    "value": "Step 2",
                    "detail": (
                        "Auto-download every FedEx and UPS invoice so no late package "
                        "slips past, since the carriers never flag the refund themselves."
                    ),
                },
                {
                    "step": "03",
                    "label": "40-44 Point Shipment Audit",
                    "value": "Step 3",
                    "detail": (
                        "Audit 40 to 44 points per shipment and flag any package delivered "
                        "even 60 seconds late; scan the original reason column for "
                        "'systematic SVC fail' credits FedEx already refunded automatically."
                    ),
                },
                {
                    "step": "04",
                    "label": "GSR Dispute Filing",
                    "value": "Step 4",
                    "detail": (
                        "File inside the 15-day window and hold FedEx invoice payment until "
                        "disputes are in, because an existing payment on file triggered "
                        "automatic denial of every late-package claim."
                    ),
                },
                {
                    "step": "05",
                    "label": "Denial Escalation Loop",
                    "value": "Step 5",
                    "detail": (
                        "Resubmit denied claims and escalate to live phone agents; Refund "
                        "Retriever's agents reversed all 5 FedEx auto-denials, recovering "
                        "$98.42 on a $4,253.53 invoice (2.3%)."
                    ),
                },
            ],
            "caption": (
                "FedEx and UPS guarantee time-definite delivery, and practitioners from "
                "Refund Retriever, Empact Parcel, and Compete Consulting Group run the "
                "same credential-to-escalation loop on contingency, from Cerasis's 30 "
                "percent model to Refund Retriever's 50 percent starting split."
            ),
            "assumptions_note": (
                "Fee terms vary by firm: Refund Retriever starts at 50% of savings and "
                "negotiates down for higher-volume shippers, while Cerasis shows a $700 net "
                "refund on $1,000 of savings at 30%. Step order follows the reported "
                "workflow; the only reported clock is the 15-day late-package claim window."
            ),
            "note": (
                "Attributed to Refund Retriever (P3sA9eO0D-k, JeLyjRF9HEk, 8Bw_30ivpb4, "
                "vOX4irOA_Tk), Scarbrough Global (NKDaSW7CKiQ), Share a Refund "
                "(eTB0fyueR5A, PheSsrwvW9c), and Cerasis, now part of GlobalTranz "
                "(GnXmnbxCZ-A)."
            ),
        },
        {
            "diagram_id": "diag-02-property-tax-appeal-odds-funnel",
            "chapter_number": 6,
            "title": "Property Tax Appeal Odds-and-Leverage Funnel",
            "subtitle": "Deadline discipline, win rates, and the value levers that move assessments",
            "chart_type": "funnel",
            "stages": [
                {
                    "label": "Timely Filing Gate",
                    "value": 100,
                    "display": "Index 100",
                    "conversion": "Entry: on-time filings only",
                    "detail": (
                        "Miss the deadline by a single day and that year's assessment cannot "
                        "be appealed (USA Senior Laws Guide); calendar every 30-day county "
                        "change notice mid-appeal (Save Paulding)."
                    ),
                },
                {
                    "label": "Win or Partial Reduction Ceiling",
                    "value": 60,
                    "display": "60%",
                    "conversion": "Up to 60% of homeowner appeals",
                    "detail": (
                        "Wins mostly go to owners who gather specific evidence and show up "
                        "(USA Senior Laws Guide)."
                    ),
                },
                {
                    "label": "Win or Partial Reduction Floor",
                    "value": 30,
                    "display": "30%",
                    "conversion": "At least 30% in most counties",
                    "detail": (
                        "Roy requests that the appraiser present first; in one Douglas County "
                        "hearing the board cut land from $32,000 to $12,000 an acre "
                        "(Save Paulding)."
                    ),
                },
                {
                    "label": "Cap-Rate Value Lever",
                    "value": 20,
                    "display": "~20% value per 1% cap-rate move",
                    "conversion": "Income-approach swing on commercial assets",
                    "detail": (
                        "Wes Nichols flags owners who recently bought at very low cap rates "
                        "as prime review targets for tax years 23 and 24 (Paramount Property "
                        "Tax Appeal)."
                    ),
                },
                {
                    "label": "Hotel Intangible Strip Floor",
                    "value": 15,
                    "display": "15% to 20% off purchase price",
                    "conversion": "Goodwill removed from newly acquired hotels",
                    "detail": (
                        "Assessors fail to strip intangible and goodwill value when they work "
                        "the sale (Paramount Property Tax Appeal)."
                    ),
                },
            ],
            "caption": (
                "A property tax appeal is a fight over assessed value, never the bill. "
                "Contingency fees run 25% to 50% of savings; George Evers's 35% worked "
                "example earns $84,000, and Eric Nelson reports a $900,000 reduction that "
                "returned $12,900 more to the client."
            ),
            "assumptions_note": (
                "Stage 1 is indexed to 100 for scale. Stages 2 and 3 are the reported "
                "30%-60% homeowner win-or-partial band; stages 4 and 5 are commercial value "
                "levers on a percent scale, not a share of filings. Big wins can invite "
                "county counter-appeals: Save Paulding saw 6 of 18 same-day properties "
                "taken to court."
            ),
            "note": (
                "Attributed to USA Senior Laws Guide (LopTSxbolHY), Save Paulding "
                "(oIIj8lWBYVY), Paramount Property Tax Appeal (fOMz56wkRgs, R_juWiwAZ-k), "
                "Cross the River, Find the Treasure (7CfK4x3Fijc), and Eric Nelson "
                "(APAYRO4lrsk)."
            ),
        },
        {
            "diagram_id": "diag-03-minimum-charge-discount-erosion",
            "chapter_number": 3,
            "title": "How Minimum Net Charges Erode Headline Discounts",
            "subtitle": "Two worked carrier-contract examples, in discount percentage points",
            "chart_type": "waterfall",
            "bars": [
                {
                    "label": "Shipware Headline Discount",
                    "value": 50,
                    "display": "50% off",
                    "kind": "total",
                },
                {
                    "label": "$8.23 Minimum Net Charge Pin",
                    "value": -12,
                    "display": "-12 pts",
                    "kind": "deduction",
                },
                {
                    "label": "Shipware Effective Discount",
                    "value": 38,
                    "display": "38% effective",
                    "kind": "result",
                },
                {
                    "label": "LJM Grid Plus Tier Headline",
                    "value": 35,
                    "display": "35% (23% grid + 12% tier)",
                    "kind": "total",
                },
                {
                    "label": "LJM Minimum Floor Constraint",
                    "value": -13,
                    "display": "-13 pts",
                    "kind": "deduction",
                },
                {
                    "label": "LJM Constrained Discount",
                    "value": 22,
                    "display": "~22% effective",
                    "kind": "result",
                },
            ],
            "caption": (
                "Keith Myers works a Zone 4, 10 lb package at $13.27: 50% off nets $6.64, "
                "but the $8.23 minimum makes the effective discount 38%, and a 65% offer "
                "would save nothing. LJM shows a stacked 23% grid plus 12% tier constrained "
                "to about 22%, and tells shippers to maximize the grid portion."
            ),
            "assumptions_note": (
                "Deduction bars are the point gap between each reported headline and "
                "effective discount. Scarbrough Global reports 25-35% from full contract "
                "engineering versus about 3% (range 1-5%) from audit alone, over 3-6 "
                "negotiation rounds across 6-10 weeks per LJM."
            ),
            "note": (
                "Attributed to Shipware (rjelY0C_iQg), LJM (56winzXYmPA), Scarbrough "
                "Global (jEjymzbOEFQ), and Refund Retriever (JAnVvaSg0TA), which calls the "
                "minimum net charge a basement floor under discounts."
            ),
        },
        {
            "diagram_id": "diag-04-carrier-size-threshold-ladder",
            "chapter_number": 2,
            "title": "Carrier Size Threshold Ladder",
            "subtitle": "The inch lines where additional handling, oversize, and over-maximum fees start",
            "chart_type": "horizontal_bars",
            "unit": "inches",
            "bars": [
                {
                    "label": "Additional Handling 30-Inch Trigger",
                    "min": 30,
                    "max": 30,
                    "typical": 30,
                    "display": "30 in",
                },
                {
                    "label": "Additional Handling 48-Inch Trigger",
                    "min": 48,
                    "max": 48,
                    "typical": 48,
                    "display": "48 in",
                },
                {
                    "label": "FedEx Length Limit to Variance",
                    "min": 96,
                    "max": 98,
                    "typical": 97,
                    "display": "96 in limit; 97 in product; 98 in negotiated variance",
                },
                {
                    "label": "Oversize Length Plus Girth Line",
                    "min": 130,
                    "max": 130,
                    "typical": 130,
                    "display": "130 in length plus girth; 90 lb minimum billable weight",
                },
                {
                    "label": "UPS Over-Maximum Line",
                    "min": 165,
                    "max": 165,
                    "typical": 165,
                    "display": "165 in length plus girth; $1,325 per package",
                },
            ],
            "caption": (
                "Invoices price on billable weight, the greater of scale and dimensional "
                "weight, and surcharges now drive spend: Joe Wilkinson puts base rate in "
                "the high 20s to 30 percent of total cost. Refund Retriever's Brian asks for "
                "a 98-inch variance on a 97-inch product instead of only a discount."
            ),
            "assumptions_note": (
                "Additional handling also triggers at 50 pounds; Refund Retriever pushes "
                "that definition to 53 or 55 pounds. Glenn Gooding's 20x20x22 inch, 20 lb "
                "box jumped 190% ($19.69 to $57.18, zone 5) under the UPS 8,640-cubic-inch "
                "rule. DIM divisors in play run 139, 166, 194, and custom 250."
            ),
            "note": (
                "Attributed to Refund Retriever (iizNycveRfc, TzPaNZCC4js, v9AT9Omrd5c), "
                "iDrive Logistics (H64bWcLI0O8), S3 Stores (q9kvSNRcgfs), Amware "
                "Fulfillment (d3jQIelSHJM), and Experidium (8-Sguow2LDM), whose rerate "
                "surfaced 2.38% of audited spend."
            ),
        },
        {
            "diagram_id": "diag-05-indirect-expense-audit-gates",
            "chapter_number": 5,
            "title": "Telecom, Waste, and Vendor Audit Gate Check",
            "subtitle": "Four gates before an indirect-expense engagement pays out",
            "chart_type": "decision_tree",
            "nodes": [
                {
                    "gate": "G1",
                    "question": "Does the client spend at least $2,000 a month in one audited category?",
                    "pass_next": "G2",
                    "fail_action": (
                        "Park the account; Zog Inc sets $2,000 a month in a category as the "
                        "point where it is worth the conversation."
                    ),
                },
                {
                    "gate": "G2",
                    "question": "Is a ledger baseline locked and an inflation cap in place before the term ends?",
                    "pass_next": "G3",
                    "fail_action": (
                        "Talk to the current hauler and competing haulers before renewal; "
                        "Barracuda B2B has seen rates jump as much as 25% at year end with "
                        "no cap."
                    ),
                },
                {
                    "gate": "G3",
                    "question": "Is every overfill or overage fee backed by driver photo proof?",
                    "pass_next": "G4",
                    "fail_action": (
                        "Back-claim credits; Zog Inc reports Paige clawed back three years of "
                        "credits on a $25-a-week overfill fee."
                    ),
                },
                {
                    "gate": "G4",
                    "question": "Are disconnected telecom circuits fully dead, with USF taxes and exemptions checked line by line?",
                    "pass_next": "Contingent savings report to the CFO",
                    "fail_action": (
                        "Kill half-disconnected circuits where the modem or NID still bills, "
                        "per Macronet Services."
                    ),
                },
            ],
            "caption": (
                "Schooley Mitchell practitioners claim 28% average savings since 1998, with "
                "80 percent of recommendations requiring no supplier change. Street wins "
                "include a 37% UPS cut on a $400K account by stripping the fuel surcharge "
                "and about $370K in Auditel telecom credits."
            ),
            "assumptions_note": (
                "Gate order follows a spend-first, then contract, then fee-proof, then "
                "circuit sequence; practitioners split on DIY versus analyst-led work. "
                "Watchdog Advisory reports $25M recovered plus $5M in future workers' comp "
                "savings, with lookbacks of five to seven years."
            ),
            "note": (
                "Attributed to Zog Inc (u-o74Ze2VNs), Barracuda B2B (vnkFP_2Jzng), "
                "Macronet Services (QMubvpeApZk), RiverForest Connections (VvAP-sQig0I), "
                "Auditel, Inc. Telecom Expense Management (gIcFGhjFIKI), and Watchdog "
                "Advisory (Joo1fuo4HkY)."
            ),
        },
        {
            "diagram_id": "diag-06-mssp-shared-savings-architecture",
            "chapter_number": 11,
            "title": "MSSP Shared-Savings Architecture",
            "subtitle": "Who the ACO answers to, and the number each party is measured on",
            "chart_type": "org_architecture",
            "center": {
                "role": "Medicare Shared Savings Program ACO",
                "headcount": "541 ACOs in MSSP (2019)",
                "focus": (
                    "Bill fee-for-service, clear the roughly 3% minimum savings corridor, "
                    "and let quality set bonus size"
                ),
            },
            "spokes": [
                {
                    "role": "Participating Physicians",
                    "type": "Gainsharing partner",
                    "kpi": "Split capped near 50%; metrics tiered at 85/90/95% (Fredrikson)",
                },
                {
                    "role": "CMS",
                    "type": "Benchmark owner",
                    "kpi": "At 2.5% savings the ACO gets 20% and CMS keeps 80% (Reyann Davis)",
                },
                {
                    "role": "Payer Input Validation",
                    "type": "Clinical review",
                    "kpi": "Third-party and payer figures validated before tiering any preferred network (Garrett Schmitt)",
                },
                {
                    "role": "Convener Network",
                    "type": "ACO organizer",
                    "kpi": "About $171 per beneficiary dispersed vs about $95 local (Health Affairs)",
                },
            ],
            "caption": (
                "Contingent models get paid from measured results against a defensible "
                "baseline. In MSSP that baseline is the benchmark, and Health Affairs warns "
                "any benchmark can be gamed; Reyann Davis cites a one-time $250,000 upfront "
                "payment as an ACO."
            ),
            "assumptions_note": (
                "About 160 participants in 2018 generated savings and got no check because "
                "of the minimum savings rate (COPE Health Solutions). Fredrikson's $100,000 "
                "bonus at 90% on-time starts died at about 87%, which is why tiers beat "
                "all-or-nothing triggers."
            ),
            "note": (
                "Attributed to Nolan Feeny (lKGpIaNHgRw), Reyann Davis (EotsrYaUjUs), "
                "Fredrikson (VMuMGmjYplc), Garrett Schmitt (UEDbkKJ-9Xk), Health Affairs "
                "(Zzb5OKFwcbg), and COPE Health Solutions (PDcTn9Sq3mg)."
            ),
        },
        {
            "diagram_id": "diag-07-utility-audit-recovery-bands",
            "chapter_number": 4,
            "title": "Utility Bill Audit Recovery Bands",
            "subtitle": "Hit rates, savings, error sizing, and fee share, in percent",
            "chart_type": "stacked_comparison",
            "total_range": (
                "$150,000 to $450,000 from a 1% to 3% error on $5 million of spend over "
                "three years (Daniel Burke)"
            ),
            "buckets": [
                {
                    "label": "Audit Recovery Hit Rate",
                    "low": 30,
                    "high": 80,
                    "notes": (
                        "Poteck Power recovers in about 30% of cases; Puleo Energy and Waste "
                        "Consultants report errors or savings in about 80% of audits."
                    ),
                },
                {
                    "label": "Average Client Savings",
                    "low": 10,
                    "high": 20,
                    "notes": "Vert Energy Group says 70% of clients save 10% to 20%.",
                },
                {
                    "label": "Billing Error Rate Modeled",
                    "low": 1,
                    "high": 3,
                    "notes": "Daniel Burke's illustration across multi-year commercial and industrial spend.",
                },
                {
                    "label": "Contingency Fee Share",
                    "low": 50,
                    "high": 50,
                    "notes": (
                        "Puleo's NUR schedule: 50% of refunds received and 50% of realized "
                        "savings for 24 months, 100% to the client from month 25."
                    ),
                },
            ],
            "caption": (
                "Commercial utility invoices are routinely wrong, errors almost always favor "
                "the utility, and the customer carries the burden before the lookback closes. "
                "Vert Energy Group and UtilityBillAudits each cite a small-business rate-plan "
                "misclassification worth $21,000."
            ),
            "assumptions_note": (
                "Buckets mix rates on one percent scale and are not additive. Puleo reaches "
                "back about 36 months, as far as the state allows; UtilityBillAudits cites a "
                "30-month review. Oncor's demand ratchet equals 80% of the highest peak "
                "across the current and previous 11 months."
            ),
            "note": (
                "Attributed to Puleo Energy (a4dO2n1QfzQ), Vert Energy Group "
                "(bQpXnGBfNJY), Daniel Burke (4pb6YRGZx4s), UtilityBillAudits "
                "(5A8gPPLuUaY, V-4ioYMhiuo), and Oncor (yHlhF0nEJ14)."
            ),
        },
        {
            "diagram_id": "diag-08-reverse-audit-launch-roadmap",
            "chapter_number": 12,
            "title": "Reverse Audit Launch Roadmap",
            "subtitle": "Run your own look-back, because the other side only hunts underpayments",
            "chart_type": "timeline_roadmap",
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Engage a Fully Contingent Firm",
                    "deliverable": "Signed engagement covering identification through check in hand",
                    "gate": (
                        "Firm does 100 percent of the work on a 100 percent contingent "
                        "basis (PM Business Advisors)"
                    ),
                },
                {
                    "week": "Week 2",
                    "title": "Set the Look-Back Window",
                    "deliverable": (
                        "Refund scope at 3 years in most states, 4 in some, and 7 to 10 years "
                        "where an old audit stays open"
                    ),
                    "gate": (
                        "Settle what is owed and build an audit trail for the entire audit "
                        "period (Sales Tax Sisters)"
                    ),
                },
                {
                    "week": "Week 3",
                    "title": "Reconcile CAM and Customs Files",
                    "deliverable": (
                        "Landlord general ledger, big-ticket invoices, and controllable-expense "
                        "definitions; 7501 value matched to the commercial invoice and payments"
                    ),
                    "gate": (
                        "Before a CAPE upload, add 80 days to each liquidation date, confirm a "
                        "US ACH account in ACE, and confirm no drawback on any entry line (Flexport)"
                    ),
                },
                {
                    "week": "Week 4",
                    "title": "Lock the Gains",
                    "deliverable": (
                        "Pre-purchase taxability check routed from purchasing to the tax team "
                        "(Cherry Bekaert)"
                    ),
                    "gate": (
                        "Any FedEx CSA renegotiation goes in writing with an exact-dollar "
                        "revenue ask (Route Consultant)"
                    ),
                },
            ],
            "caption": (
                "Sales tax, workers comp, customs, CAM, and FedEx contract operators run the "
                "same play: find the overpayments the other side's audit never looks for. "
                "SMP Consulting Group cites a $190,000 Kentucky workers comp recovery over "
                "three years."
            ),
            "assumptions_note": (
                "Week slots sequence the reported steps; no week-by-week durations were "
                "reported. Reported clocks: 7 days to pick a MISO for the 1% early-accept "
                "bonus ($10,000 on $1,000,000), 4 to 6 months ahead for unique "
                "characteristics, and 4 to over 20 hours per CAM location (RE BackOffice)."
            ),
            "note": (
                "Attributed to PM Business Advisors (ePf76grjr8U), Sales Tax Sisters "
                "(LibBgjGxja4), Flexport (xtorVFI9g4c), Commercial Real Estate Escalations "
                "Made Simple (CWHu33HRBVY), Cherry Bekaert (S7Qlojol4pE), Route Consultant "
                "(-AnzYDP3LQw, 39UxCZgtvHU), Greg Walker (sM254iPKhSo), and RE BackOffice "
                "(5wJlP07wwrM)."
            ),
        },
    ]


VOLUME_038_POSITIONING_ALTERNATIVES: List[Dict] = [
    {
        "title": "The Late-Package Money Machine",
        "subtitle": "GSR Refunds, Surcharge Rerating, and Carrier Contract Engineering on Contingency",
        "audience": "Ecommerce and B2B shippers, parcel auditors, and logistics finance leads",
        "research_basis": (
            "Refund Retriever's 15-day GSR window and payment-on-file denial trap, "
            "Shipware's 50%-to-38% minimum-charge math, Scarbrough Global's 25-35% "
            "contract engineering versus about 3% audit savings, and Experidium's 2.38% "
            "line-by-line rerate yield."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=JeLyjRF9HEk&t=66s",
            "https://www.youtube.com/watch?v=8Bw_30ivpb4&t=48s",
            "https://www.youtube.com/watch?v=rjelY0C_iQg&t=217s",
            "https://www.youtube.com/watch?v=jEjymzbOEFQ&t=2719s",
            "https://www.youtube.com/watch?v=8-Sguow2LDM&t=157s",
        ],
        "validation_status": "Grounded strictly in Vol. 038 YouTube practitioner transcripts.",
    },
    {
        "title": "No Savings, No Fee",
        "subtitle": "Utility, Telecom, Waste, Workers' Comp, and Sales Tax Recovery for the CFO",
        "audience": "CFOs, controllers, and contingency audit firm founders",
        "research_basis": (
            "Puleo Energy's 50% refund and 24-month savings split, Zog Inc's 37% cut on a "
            "$400K UPS account, Watchdog Advisory's $25M recovered, and PM Business "
            "Advisors' 100% contingent reverse audits reaching 7 to 10 years on open audits."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=a4dO2n1QfzQ&t=357s",
            "https://www.youtube.com/watch?v=u-o74Ze2VNs&t=203s",
            "https://www.youtube.com/watch?v=Joo1fuo4HkY&t=40s",
            "https://www.youtube.com/watch?v=ePf76grjr8U&t=92s",
        ],
        "validation_status": "Grounded strictly in Vol. 038 YouTube practitioner transcripts.",
    },
    {
        "title": "Found Money in the Tax Code",
        "subtitle": "Property Tax Appeals, Cost Segregation, 179D, and WOTC Claims That Survive Review",
        "audience": "Commercial property owners, A&E firms, high-turnover employers, and their CPAs",
        "research_basis": (
            "Paramount's 20% value swing per 1% cap-rate move, Engineered Tax Services' "
            "$794K year-one write-off on a $2.5M basis, Cherry Bekaert's 179D rise from "
            "$1.80 to $5 per square foot, WOTC.com's 20% fee paid only after the credit is "
            "used, and the 28-day state agency filing wall."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=fOMz56wkRgs&t=30s",
            "https://www.youtube.com/watch?v=qEFJIGNNOkw&t=733s",
            "https://www.youtube.com/watch?v=JZ5NlVOVnnw&t=667s",
            "https://www.youtube.com/watch?v=kuYWnLG5-A4&t=1056s",
            "https://www.youtube.com/watch?v=ujWX1IZPyFc&t=322s",
        ],
        "validation_status": "Grounded strictly in Vol. 038 YouTube practitioner transcripts.",
    },
]
