"""Volume 007 diagram data: Unclaimed Property Recovery."""

from typing import Any, Dict, List

VOLUME_007_SUBTITLE: str = (
    "Free State Searches, Capped Finder Fees, Skip-Traced Heirs, Licensed "
    "Claim Filing, Bankruptcy and Royalty Recoveries, and Holder Audit Defense"
)


def build_volume_007_diagrams_data() -> List[Dict[str, Any]]:
    """Return the eight structured diagram dicts for Volume 007."""
    return [
        {
            "diagram_id": "diag-01-search-entry-sequence",
            "chapter_number": 1,
            "title": "Unclaimed Property Search Entry Sequence",
            "subtitle": "From dormancy clock to a free claim or a capped finder agreement",
            "chart_type": "process_flow",
            "stages": [
                {
                    "step": "01",
                    "label": "Confirm Dormancy Has Run",
                    "value": "Step 1",
                    "detail": (
                        "Dormancy runs one year for payroll and three to five years for "
                        "bank accounts; an empty search may only mean the property has "
                        "not yet been reported to the state (Hoang Le CFP, EA)."
                    ),
                },
                {
                    "step": "02",
                    "label": "Sweep MissingMoney.com First",
                    "value": "Step 2",
                    "detail": (
                        "More than $70 billion sits in state custody and about one in "
                        "seven Americans has a stake; the median claim is about $100 "
                        "against a $2,080 average (Hoang Le; Money Missed)."
                    ),
                },
                {
                    "step": "03",
                    "label": "Search Every State Portal",
                    "value": "Step 3",
                    "detail": (
                        "Search each state where the owner lived or worked, including "
                        "deceased relatives; Illinois traced 119 relatives back five "
                        "generations on the $11 million Stancak estate (Money Missed)."
                    ),
                },
                {
                    "step": "04",
                    "label": "Check Federal Registries",
                    "value": "Step 4",
                    "detail": (
                        "State databases do not hold federal assets such as wages, "
                        "pensions, FHA refunds, failed banks, or bankruptcy court funds, "
                        "so one portal never proves a zero result (This Guy Knows Tech)."
                    ),
                },
                {
                    "step": "05",
                    "label": "File Free or Use a Capped Finder",
                    "value": "Step 5",
                    "detail": (
                        "Self-filing costs nothing; registered finders are commonly "
                        "capped at 10% to 30%, and a legitimate locator never asks to be "
                        "paid first. State payouts typically land in 16 to 120 days."
                    ),
                },
            ],
            "caption": (
                "Five-step entry sequence for locating custodial money before it is "
                "worked as a claim."
            ),
            "assumptions_note": (
                "Step order follows the practitioner consensus on search entry points; "
                "dollar figures are attributed practitioner claims, not audited totals."
            ),
            "note": (
                "Attributed to Hoang Le CFP, EA, Real Estate Agent; Money Missed; "
                "This Guy Knows Tech; Money Making Juggernaut (Eric Richardson)."
            ),
        },
        {
            "diagram_id": "diag-02-licensed-volume-funnel",
            "chapter_number": 6,
            "title": "Licensed Recovery Volume Funnel",
            "subtitle": "Dial volume narrowing to a few collections under a 10% ceiling",
            "chart_type": "funnel",
            "stages": [
                {
                    "label": "Weekly Dial Volume",
                    "value": 1000,
                    "display": "Over 1,000 calls a week",
                    "conversion": "Entry volume",
                    "detail": (
                        "Joe Green's first mentor taught calling every skip-traced "
                        "prospect at least 10 times; most never answered (Unclaimed CEO)."
                    ),
                },
                {
                    "label": "Skip-Traced Lead List",
                    "value": 100,
                    "display": "100 leads",
                    "conversion": "10 calls per lead on a 100-lead list",
                    "detail": (
                        "Paid tracing beats free sites; Tracers runs about $1.50 per "
                        "skip and Skip Matrix $0.14 per matched record."
                    ),
                },
                {
                    "label": "Business Targets Pitched",
                    "value": 20,
                    "display": "15 to 20 corporations",
                    "conversion": "15 to 20 corporations contacted per batch",
                    "detail": (
                        "David Church pitches business owners, including local banks, "
                        "on balances found in downloaded state lists."
                    ),
                },
                {
                    "label": "Licensed Fee Ceiling",
                    "value": 10,
                    "display": "10% cap in Texas and California",
                    "conversion": "At or under 10% on California and Texas agreements",
                    "detail": (
                        "Sharalyn Criswell cites the Texas 10% PI cap; Michelle sponsors "
                        "registrants at $295 per year; ShadowAnyone warns unlicensed work "
                        "can bar a PI license with no time limit."
                    ),
                },
                {
                    "label": "Collections Landed",
                    "value": 3,
                    "display": "2 to 3 collections",
                    "conversion": "2 to 3 collections per 15 to 20 corporations",
                    "detail": (
                        "Church reports checks of $1,400 to $1,600 on mid-size claims; "
                        "Michelle relies on volume rather than workarounds."
                    ),
                },
            ],
            "caption": (
                "Volume pipeline for a licensed or registered operator, from dials to "
                "paid collections."
            ),
            "assumptions_note": (
                "Stages combine separately reported operator figures; the fee ceiling "
                "stage is a percentage, while other stages are counts. Upper ends of "
                "reported ranges are plotted as values."
            ),
            "note": (
                "Attributed to Unclaimed CEO (Joe Green); Surplus Institute / David "
                "Church; Texas Licensed Private Investigator (Sharalyn Criswell); Money "
                "Making Juggernaut (Michelle, Shai Korn); ShadowAnyone (Larry Kay)."
            ),
        },
        {
            "diagram_id": "diag-03-state-return-waterfall",
            "chapter_number": 3,
            "title": "State Intake Versus Returns",
            "subtitle": "Delaware net retention beside Illinois and California pools (USD millions)",
            "chart_type": "waterfall",
            "bars": [
                {
                    "label": "Delaware Gross Intake",
                    "value": 554,
                    "display": "$554 million",
                    "kind": "total",
                },
                {
                    "label": "Owner Refunds Paid",
                    "value": 128,
                    "display": "$128 million",
                    "kind": "deduction",
                },
                {
                    "label": "Delaware Net Booked",
                    "value": 426,
                    "display": "About $426 million",
                    "kind": "result",
                },
                {
                    "label": "Illinois Pool Held",
                    "value": 5000,
                    "display": "About $5 billion",
                    "kind": "total",
                },
                {
                    "label": "Illinois Proactive Check Run",
                    "value": 13.2,
                    "display": "140,000 checks, $13.2 million",
                    "kind": "deduction",
                },
                {
                    "label": "California Backlog Awaiting Owners",
                    "value": 7000,
                    "display": "$7 billion across 28 million accounts",
                    "kind": "total",
                },
            ],
            "caption": (
                "Delaware kept about $426 million net after refunds, while Illinois and "
                "California pools dwarf their proactive returns."
            ),
            "assumptions_note": (
                "All values in USD millions as reported; Illinois and California bars are "
                "separate pools, not a continuation of the Delaware sequence. New York "
                "separately reports $1.5 million paid per day with automatic checks on "
                "claims of $250 or less."
            ),
            "note": (
                "Attributed to Off The Receipt (Delaware); WGN News (Treasurer Michael "
                "Frerichs, Illinois); CBS News Sacramento (California); NBC New York."
            ),
        },
        {
            "diagram_id": "diag-04-launch-benchmarks",
            "chapter_number": 2,
            "title": "Launch-Phase Operator Benchmarks",
            "subtitle": "Follow-up, tracing cost, tracking, and fee-split ranges",
            "chart_type": "horizontal_bars",
            "unit": "Mixed operator benchmarks (unit shown in each label)",
            "bars": [
                {
                    "label": "Follow-Up Calls Per Prospect (calls)",
                    "min": 3,
                    "max": 5,
                    "typical": 5,
                    "display": "3 to 5 follow-up calls",
                },
                {
                    "label": "Contact Where Most Sales Close (contact number)",
                    "min": 5,
                    "max": 12,
                    "typical": 5,
                    "display": "80% of sales on the 5th to 12th contact",
                },
                {
                    "label": "Batch Skip Tracing Per 100 Leads (USD)",
                    "min": 14,
                    "max": 15,
                    "typical": 14,
                    "display": "About $14 to $15 per 100 leads",
                },
                {
                    "label": "Calls-To-Pickups Tracking Window (weeks)",
                    "min": 2,
                    "max": 3,
                    "typical": 2,
                    "display": "Track 2 to 3 weeks before doubling volume",
                },
                {
                    "label": "Florida Lawyer Fee Split, Operator Share (percent)",
                    "min": 50,
                    "max": 70,
                    "typical": 50,
                    "display": "50/50 now, pushing toward 70/30",
                },
            ],
            "caption": (
                "Benchmarks for the first months of a state funds operation, after the "
                "fee cap and claim-package rules are read."
            ),
            "assumptions_note": (
                "Typical markers sit on a value the speaker actually stated, not on a "
                "computed midpoint; units differ per bar as labeled."
            ),
            "note": (
                "Attributed to Surplus Funds 101 (David Wilkerson); Money Making "
                "Juggernaut (Eric Richardson); Unclaimed CEO; Surplus Institute / David "
                "Church."
            ),
        },
        {
            "diagram_id": "diag-05-business-name-gates",
            "chapter_number": 5,
            "title": "Business-Name Claim Gates",
            "subtitle": "Four checks before filing on a company balance",
            "chart_type": "decision_tree",
            "nodes": [
                {
                    "gate": "G1",
                    "question": (
                        "Was the company entered in the last-name field with the first "
                        "name left blank?"
                    ),
                    "pass_next": "G2",
                    "fail_action": (
                        "Re-run with the company in the last-name field and legal "
                        "suffixes like LLC, Inc., or Corp. dropped on the first pass."
                    ),
                },
                {
                    "gate": "G2",
                    "question": (
                        "Have DBAs, prior names, acronyms, FEIN, and former office zip "
                        "codes all been searched?"
                    ),
                    "pass_next": "G3",
                    "fail_action": (
                        "Stack every name variant and old zip code; check federal "
                        "sources separately because federal agencies are exempt from "
                        "state escheatment."
                    ),
                },
                {
                    "gate": "G3",
                    "question": (
                        "For a merged or dissolved entity, is the full ownership chain "
                        "documented?"
                    ),
                    "pass_next": "G4",
                    "fail_action": (
                        "Pull certified articles of merger or dissolution plus a "
                        "certificate of good standing; budget 6 to 12 months for the "
                        "lineage audit."
                    ),
                },
                {
                    "gate": "G4",
                    "question": (
                        "Is the locator fee inside the state cap and past the "
                        "unenforceable window?"
                    ),
                    "pass_next": (
                        "File, then calendar the payout; South Carolina checks void at "
                        "90 days and force a full refile."
                    ),
                    "fail_action": (
                        "Hold; Missouri voids deals in the first 12 months, Colorado in "
                        "the first 24 months with a 10% cap, and Georgia caps general "
                        "agents at 10%."
                    ),
                },
            ],
            "caption": (
                "Most business-name misses come from searching wrong; these gates catch "
                "the common traps before a claim is filed."
            ),
            "assumptions_note": (
                "Gate order reflects search-then-document-then-fee sequencing; state "
                "rules cited are as reported by the named channels and vary by state."
            ),
            "note": (
                "Attributed to Как се прави; GardenShop.Pro; Garden Shop Pro; Surplus "
                "Institute / David Church."
            ),
        },
        {
            "diagram_id": "diag-06-specialty-asset-architecture",
            "chapter_number": 11,
            "title": "Royalty, Insurance, and Share Recovery Architecture",
            "subtitle": "One claimant working four custodian channels",
            "chart_type": "org_architecture",
            "center": {
                "role": "Claimant or Heir",
                "headcount": "Every heir named in the will or letter of administration",
                "focus": (
                    "Name-variant searches across every state, portal, and registrar, "
                    "backed by ID and probate or heirship proof."
                ),
            },
            "spokes": [
                {
                    "role": "Texas Comptroller",
                    "type": "State custodian for royalties",
                    "kpi": (
                        "MI02 royalties abandoned after 3 years; finder fee capped at "
                        "10%; $10,000 affidavit-of-heirship ceiling."
                    ),
                },
                {
                    "role": "Well Operator",
                    "type": "Royalty holder",
                    "kpi": (
                        "Redirect future checks after the claim; claiming suspended "
                        "royalties can cure title and restore pay status."
                    ),
                },
                {
                    "role": "Policy Locator",
                    "type": "Insurance search",
                    "kpi": (
                        "Run NAIC and MissingMoney.com first; MIB costs $75 for "
                        "policies after 1995 as an absolute last resort."
                    ),
                },
                {
                    "role": "Share Registrar",
                    "type": "Statutory dividend custodian",
                    "kpi": (
                        "7 years to the IEPFA in India, 6 years to the Nigerian trust "
                        "fund; get the amount from the registrar, not the broker."
                    ),
                },
            ],
            "caption": (
                "Specialty assets escheat on the same dormancy mechanic, but each "
                "custodian channel has its own proof and fee rules."
            ),
            "assumptions_note": (
                "Spokes group the custodians named by practitioners; dormancy periods "
                "and fees are as stated for Texas, India, and Nigeria only."
            ),
            "note": (
                "Attributed to Royalty Clerk; txcomptroller; Blue Mesa Minerals; Garden "
                "Shop Pro; Mint; Broadstreet Radio."
            ),
        },
        {
            "diagram_id": "diag-07-finder-fee-ceilings",
            "chapter_number": 4,
            "title": "Finder Fee Ceilings by State",
            "subtitle": "Reported caps across four state walkthroughs (percent)",
            "chart_type": "stacked_comparison",
            "total_range": "10% to 40% finder fee ceilings across reported states",
            "buckets": [
                {
                    "label": "New York",
                    "low": 15,
                    "high": 15,
                    "notes": (
                        "Capped at 15% with a written, notarized contract; the state "
                        "sends 100% of the check to the owner."
                    ),
                },
                {
                    "label": "Kansas",
                    "low": 15,
                    "high": 15,
                    "notes": (
                        "15% ceiling; Kansas intercepts delinquent state taxes, child "
                        "support, and court fines and pays only the net."
                    ),
                },
                {
                    "label": "Georgia",
                    "low": 10,
                    "high": 30,
                    "notes": "Reported range of 10% to 30% depending on agent type.",
                },
                {
                    "label": "Montana",
                    "low": 10,
                    "high": 40,
                    "notes": (
                        "Reported range of 10% to 40%; the state auto-mails up to "
                        "$1,000 without a formal claim."
                    ),
                },
            ],
            "caption": (
                "Finder ceilings split widely by state even though every portal runs on "
                "the same free search engine."
            ),
            "assumptions_note": (
                "Single-value caps are shown with equal low and high; ranges are as "
                "reported and may reflect different agent categories."
            ),
            "note": (
                "Attributed to Как се прави (New York); GardenShop.Pro (Kansas, Georgia, "
                "Montana); WFAA; KHOU 11."
            ),
        },
        {
            "diagram_id": "diag-08-holder-compliance-roadmap",
            "chapter_number": 12,
            "title": "Holder Compliance Roadmap",
            "subtitle": "Four-week sprint from exposure review to audit posture",
            "chart_type": "timeline_roadmap",
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Exposure Assessment",
                    "deliverable": (
                        "Review receivable credit balances and the voided check register; "
                        "stop sweeping stale items into miscellaneous income."
                    ),
                    "gate": (
                        "Voided and stale items flagged before they age into unclaimed "
                        "property within three to five years."
                    ),
                },
                {
                    "week": "Week 2",
                    "title": "Due Diligence Letters",
                    "deliverable": (
                        "Send South Carolina letters on items of $50 or more no more "
                        "than 120 days before filing; apply the Texas $250 notice floor."
                    ),
                    "gate": "Texas July 1 and Utah November 1 report deadlines calendared.",
                },
                {
                    "week": "Week 3",
                    "title": "Exemption Review",
                    "deliverable": (
                        "Screen recoupment, business-to-business, and de minimis "
                        "exemptions; Kodiak counts about 100 in healthcare."
                    ),
                    "gate": "Compliant but not overly compliant before remitting.",
                },
                {
                    "week": "Week 4",
                    "title": "Audit and Disclosure Posture",
                    "deliverable": (
                        "Decide on any Delaware VDA invitation within 90 days; voluntary "
                        "disclosure cuts look-back to about ten years and waives penalties."
                    ),
                    "gate": (
                        "Participating-state list pulled from state notifications, never "
                        "from the auditor."
                    ),
                },
            ],
            "caption": (
                "Non-filing, missing property types, and M&A trigger audits; Tennessee "
                "penalizes willful failure at $1,000 a day up to $25,000 plus 25%."
            ),
            "assumptions_note": (
                "The four-week cadence is an organizing frame; deadlines, floors, and "
                "penalties are as stated by the named examiners and advisors."
            ),
            "note": (
                "Attributed to TNTreasury; Utah Office of State Treasurer; SimekScott "
                "LLC; Friedman LLP; Kodiak Solutions; COMPUTERSHARE (Pam Wentz, Jennifer "
                "Borden)."
            ),
        },
    ]


VOLUME_007_POSITIONING_ALTERNATIVES: List[Dict[str, Any]] = [
    {
        "title": "The Ten Percent Locator",
        "subtitle": (
            "Capped fees, data-loaded calls, relative tracing, and interest clauses "
            "for state funds operators"
        ),
        "audience": "New and early-stage unclaimed funds locators and heir finders",
        "research_basis": (
            "David Church's California 10% direct payout and $5,400 invoice on a "
            "$54,000 claim, David Wilkerson's 5th-to-12th contact close rate, Sean "
            "Boujie's 40-50% relative outreach lift, and Jay's interest clause lifting "
            "a fee from $18,000 to $31,000."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=IIBKDdChS-k&t=103s",
            "https://www.youtube.com/watch?v=qyRWV76TgwE&t=439s",
            "https://www.youtube.com/watch?v=wp5vC44yQQg&t=256s",
            "https://www.youtube.com/watch?v=kb-pXZgQdoE&t=57s",
            "https://www.youtube.com/watch?v=ZvJ4yCc9em4&t=262s",
            "https://www.youtube.com/watch?v=ujbTh1In_c4&t=157s",
        ],
        "validation_status": "Grounded strictly in Vol. 007 YouTube practitioner transcripts.",
    },
    {
        "title": "Claim It Free",
        "subtitle": (
            "Finding your own dormant money across state, federal, and business-name "
            "searches without paying anyone"
        ),
        "audience": "Individuals, families, and small business owners searching on their own behalf",
        "research_basis": (
            "More than $70 billion in state custody, a $100 median claim, federal "
            "assets missing from state portals, New York automatic checks on claims of "
            "$250 or less, and a 37 business day Texas turnaround."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=kZMkghcevh8&t=423s",
            "https://www.youtube.com/watch?v=sfcrjWHv_7k&t=737s",
            "https://www.youtube.com/watch?v=74IHdXzW4aQ&t=167s",
            "https://www.youtube.com/watch?v=wCk_H4rThTo&t=19s",
            "https://www.youtube.com/watch?v=7Fc0D2RuIJE&t=194s",
            "https://www.youtube.com/watch?v=0UUN2j2_dFU&t=102s",
        ],
        "validation_status": "Grounded strictly in Vol. 007 YouTube practitioner transcripts.",
    },
    {
        "title": "Before the Auditor Calls",
        "subtitle": (
            "Holder reporting, exemption hunting, voluntary disclosure, and audit "
            "defense for unclaimed property"
        ),
        "audience": "Controllers, compliance leads, and counsel at companies that hold unclaimed property",
        "research_basis": (
            "States estimating 65% to 90% non-filing, roughly 90% to 95% of remitted "
            "property kept by states, Tennessee's $1,000-a-day willful penalty, and "
            "Delaware's 90-day VDA decision window."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=duwB7Y82flc&t=158s",
            "https://www.youtube.com/watch?v=2BplqmdsUpU&t=664s",
            "https://www.youtube.com/watch?v=KiR-ZUeCE5g&t=165s",
            "https://www.youtube.com/watch?v=79d39hagJ6U&t=40s",
            "https://www.youtube.com/watch?v=TGu6R9Pc0-4&t=19s",
        ],
        "validation_status": "Grounded strictly in Vol. 007 YouTube practitioner transcripts.",
    },
]
