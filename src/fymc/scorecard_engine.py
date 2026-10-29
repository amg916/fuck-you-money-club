"""Editorial scorecards; economics are illustrative USD planning assumptions.

Confidence and production stages are supplied editorial classifications, not
claims that this module has verified sources or reviewed a research corpus.
Ranges describe operating businesses, not guaranteed startup outcomes. A new
operator can earn nothing or lose capital. Scores are judgment-based, not
investment advice; uncertainty bands are not statistical confidence intervals.
"""

from __future__ import annotations

from copy import deepcopy
from math import isfinite
import re

SCORE_KEYS = ("money_to_manpower_score", "total_score", "composite_score", "score")
_SCORE_STRING_RE = re.compile(r"^\s*([+-]?\d+(?:\.\d+)?)\s*(?:/\s*100)?\s*$")


def resolve_score_value(scorecard: dict | None, default: float | None = None) -> float | None:
    """Resolve the numeric composite score deterministically without truthiness traps."""
    if not isinstance(scorecard, dict):
        return default
    for key in SCORE_KEYS:
        if key not in scorecard:
            continue
        raw = scorecard[key]
        if raw is None or isinstance(raw, bool):
            continue
        if isinstance(raw, (int, float)):
            try:
                as_float = float(raw)
            except (ValueError, OverflowError):
                continue
            if isfinite(as_float):
                return int(raw) if isinstance(raw, int) else (int(as_float) if as_float.is_integer() else as_float)
            continue
        if isinstance(raw, str):
            match = _SCORE_STRING_RE.match(raw)
            if match:
                try:
                    parsed = float(match.group(1))
                except (ValueError, OverflowError):
                    continue
                if isfinite(parsed):
                    return int(parsed) if parsed.is_integer() else parsed
    return default

SCORE_DIMENSIONS = {
    "revenue_potential": 25,
    "profit_margin_potential": 25,
    "team_efficiency": 20,
    "startup_accessibility": 15,
    "automation_potential": 15,
}
DIMENSION_LABELS = {
    "revenue_potential": "Revenue Potential",
    "profit_margin_potential": "Profit Margin Potential",
    "team_efficiency": "Team Efficiency",
    "startup_accessibility": "Startup Accessibility",
    "automation_potential": "Automation Potential",
}
_CONFIDENCE_BANDS = {
    "High": "±3 pts",
    "Moderate": "±6 pts",
    "Preliminary — Uncertainty Range": "±10 pts",
}


def compute_scorecard(spec: dict) -> dict:
    """Validate weighted subscores and return a detached, normalized scorecard."""
    if not isinstance(spec, dict):
        raise ValueError("spec must be a dictionary")
    scores = spec.get("scores")
    if not isinstance(scores, dict) or set(scores) != set(SCORE_DIMENSIONS):
        raise ValueError("scores must contain exactly the five score dimensions")
    for key, maximum in SCORE_DIMENSIONS.items():
        value = scores[key]
        if (isinstance(value, bool) or not isinstance(value, (int, float))
                or not 0 <= value <= maximum or not isfinite(value)):
            raise ValueError(f"{key} must be a finite number between 0 and {maximum}")
    confidence = spec.get("evidence_confidence")
    if not isinstance(confidence, str) or confidence not in _CONFIDENCE_BANDS:
        raise ValueError("invalid evidence_confidence")
    total = sum(scores.values())
    uncertainty_band = _CONFIDENCE_BANDS[confidence]
    band_delta = int(uncertainty_band.removeprefix("±").split()[0])
    if total >= 85:
        tier = "Elite Small-Team Cash Machine"
    elif total >= 75:
        tier = "High-Leverage Operator Play"
    elif total >= 65:
        tier = "Disciplined Specialist Play"
    else:
        tier = "Capital / Labor Intensive"
    result = {
        "candidate_number": spec.get("candidate_number"),
        "slug": spec.get("slug", ""),
        "title": spec.get("title", ""),
        "category": spec.get("category", ""),
        "production_stage": spec.get("production_stage", "candidate_scored"),
        "scores": dict(scores),
        "dimension_max": dict(SCORE_DIMENSIONS),
        "total_score": total,
        "tier_label": tier,
        "evidence_confidence": confidence,
        "uncertainty_band": uncertainty_band,
        "uncertainty_bounds": {
            "low": max(0, total - band_delta),
            "high": min(100, total + band_delta),
        },
        "uncertainty_note": spec.get("uncertainty_note", (
            "Editorial sensitivity band, not a statistical interval. Confidence "
            "is a supplied classification; independent source review is required."
        )),
        "score_rationale": spec.get("score_rationale", {}),
        "economics": spec.get("economics", {}),
        "scenarios": spec.get("scenarios", {}),
        "automation_levers": spec.get("automation_levers", []),
        "key_risks": spec.get("key_risks", []),
        "regulatory_notes": spec.get("regulatory_notes", []),
    }
    return deepcopy(result)


def get_flagship_scorecard() -> dict:
    """Return candidate 1 irrespective of its eventual pipeline ranking."""
    return compute_scorecard(next(
        spec for spec in _CANDIDATE_SPECS if spec["candidate_number"] == 1
    ))


def _money_range(values: tuple) -> str:
    return f"${values[0]:,.0f}–${values[1]:,.0f} USD"


def _candidate(number, title, category, points, gross, margins, capital, opex,
               timing, team, rationale, levers, risks, regulations,
               revenue_basis="Recognized service fees, not client asset value",
               confidence="Moderate") -> dict:
    """Build a uniform schema from explicit, candidate-specific assumptions.

    Gross revenue is annual. Margins already include non-owner labor and all
    operating expenses; monthly opex is an indicative fixed/semi-fixed budget,
    not an additional deduction. Inventory, pass-through and financing capital
    are separate from fixed opex. Owner profit assumes sole ownership, before
    personal taxes, debt principal and reinvestment, with no owner salary charged.
    """
    scores = dict(zip(SCORE_DIMENSIONS, points))
    ft, contractors = team
    staffing = {
        "full_time_including_owner": ft,
        "contractors": contractors,
        "total_people": ft + contractors,
    }
    scenarios = {}
    for name, revenue, margin, extra in (
        ("conservative", gross[0], margins[0], 0),
        ("base_case", sum(gross) / 2, sum(margins) / 2, 0),
        ("scaled_small_team", gross[1], margins[1], 2),
    ):
        scenarios[name] = {
            "annual_gross_revenue_usd": revenue,
            "net_profit_margin_pct": margin,
            "annual_owner_net_profit_usd": round(revenue * margin / 100),
            "full_time_including_owner": ft + (1 if extra else 0),
            "contractors": contractors + (1 if extra else 0),
            "total_people": ft + contractors + extra,
            "assumption": (
                "Illustrative established-operation run rate, not first-year "
                "earnings. Margin includes operating costs and non-owner labor; "
                "owner labor is not separately compensated. Scale requires "
                "additional demand, working capital and delivery capacity."
            ),
        }
    confidence = "High" if number in {1, 2, 5, 9} else confidence
    stage = ("flagship_in_design_review" if number == 1 else
             "research_corpus_ready" if number in {2, 5, 9} else "candidate_scored")
    return {
        "candidate_number": number,
        "slug": title.lower().replace(" ", "-"),
        "title": title,
        "category": category,
        "production_stage": stage,
        "scores": scores,
        "evidence_confidence": confidence,
        "score_rationale": {
            key: f"{DIMENSION_LABELS[key]}: {score}/{SCORE_DIMENSIONS[key]}. {rationale}"
            for key, score in scores.items()
        },
        "economics": {
            "gross_revenue_range": _money_range(gross) + " annually",
            "net_profit_margin_range": f"{margins[0]}–{margins[1]}%",
            "owner_net_profit_potential": _money_range((
                gross[0] * margins[0] / 100, gross[1] * margins[1] / 100,
            )) + " annually, before personal taxes and reinvestment",
            "startup_capital_range": _money_range(capital),
            "monthly_opex_range": _money_range(opex),
            "time_to_first_deal": timing,
            "typical_team_size": staffing,
            "includes_contractors_note": (
                "Headcount includes the working owner and recurring contractors "
                "as people, not FTE equivalents. Contractors may be part-time. "
                "Scaled scenario adds one employee and one contractor; external "
                "vendor workforces are not counted as internal team members."
            ),
            "revenue_basis": revenue_basis,
            "cost_basis": (
                "Annual net margins include operating expenses and non-owner "
                "labor; monthly opex is fixed/semi-fixed overhead only. No owner "
                "salary is deducted. Capital needs may grow beyond startup range."
            ),
            "estimate_status": "Illustrative assumptions; not verified earnings data",
        },
        "scenarios": scenarios,
        "automation_levers": levers,
        "key_risks": risks,
        "regulatory_notes": regulations,
    }


_CANDIDATE_SPECS = [
    _candidate(1, "Heir Hunting", "Estate research", (22, 23, 18, 12, 12),
        (80000, 600000), (25, 50), (10000, 50000), (2000, 10000), "6–24 months", (1, 3),
        "Contingent fees support lean research teams, but estate delays defer cash.",
        ["Public-record alerts", "Genealogy case tracking", "Document indexing"],
        ["Unsuccessful research", "Contested kinship", "Long collection cycles"],
        ["Check heir-finder fee restrictions and solicitation rules by jurisdiction.",
         "Do not provide legal representation without appropriate authorization."]),
    _candidate(2, "Surplus Funds Recovery", "Recovery services", (22, 22, 18, 12, 12),
        (100000, 750000), (25, 45), (10000, 60000), (2500, 14000), "3–18 months", (2, 2),
        "Fee-based recovery has low inventory needs but uneven claim conversion.",
        ["Auction-result monitoring", "Claim deadlines", "Document checklists"],
        ["Competing claims", "Denied claims", "Fee compression"],
        ["Surplus recovery fee caps, assignment validity and waiting periods vary.",
         "Court filings may require licensed counsel."]),
    _candidate(3, "Tax Lien Investing", "Asset investing", (17, 15, 17, 5, 8),
        (15000, 180000), (30, 55), (100000, 1500000), (500, 4000), "6–36 months", (1, 2),
        "Lean administration cannot offset capital lockup and adverse property selection.",
        ["Auction screening", "Redemption tracking"],
        ["Nonredeeming liens", "Title defects", "Capital loss"],
        ["Auction eligibility, interest limits and foreclosure procedures are local."],
        revenue_basis="Realized interest, penalties and disposition gains; excludes returned principal"),
    _candidate(4, "Government Contract Brokering", "Procurement services", (22, 16, 14, 8, 10),
        (120000, 1000000), (15, 30), (25000, 150000), (5000, 25000), "6–18 months", (2, 3),
        "Large awards do not translate to large fees; compliance and sales require labor.",
        ["Solicitation alerts", "Bid calendars", "Compliance checklists"],
        ["Award uncertainty", "Payment delays", "Supplier failure"],
        ["Review contingent-fee restrictions, procurement integrity and anti-kickback rules.",
         "Pass-through restrictions and set-aside rules can prohibit proposed structures."]),
    _candidate(5, "Unclaimed Property Recovery", "Recovery services", (20, 22, 18, 13, 12),
        (60000, 450000), (25, 50), (5000, 35000), (1500, 8000), "3–12 months", (1, 2),
        "Low-capital research scales moderately; free state claims constrain pricing.",
        ["Record matching", "Claim status tracking"],
        ["Identity mismatch", "Low claim values", "Customer distrust"],
        ["Check finder registration, fee caps, waiting periods and privacy obligations.",
         "Disclose the owner's ability to claim directly without a recovery service."]),
    _candidate(6, "Land Flipping", "Real estate trading", (21, 18, 17, 6, 10),
        (200000, 1500000), (12, 25), (50000, 400000), (3000, 15000), "3–12 months", (1, 3),
        "Small teams can trade parcels, but inventory capital and due diligence limit access.",
        ["Parcel screening", "Comparable-sale tracking"],
        ["Illiquidity", "No legal access", "Environmental constraints"],
        ["Review zoning, title, disclosures and broker licensing when representing others."],
        revenue_basis="Gross parcel sale proceeds; acquisition costs included in net margin"),
    _candidate(7, "Mineral Rights", "Resource assets", (20, 17, 16, 3, 7),
        (30000, 400000), (20, 45), (150000, 2000000), (1000, 12000), "6–24 months", (1, 3),
        "Specialist title work and substantial capital outweigh passive-income appeal.",
        ["Royalty reconciliation", "Production monitoring"],
        ["Commodity prices", "Depletion", "Title disputes"],
        ["Review severed mineral title, leases, tax obligations and securities rules if pooling funds."],
        revenue_basis="Royalty receipts and realized rights-trading gains, excluding returned basis"),
    _candidate(8, "Judgment Recovery", "Recovery services", (20, 21, 16, 10, 10),
        (60000, 500000), (20, 40), (10000, 75000), (2000, 12000), "6–24 months", (1, 3),
        "Contingent collections can be efficient but many judgments are uncollectible.",
        ["Court deadline tracking", "Payment reconciliation"],
        ["Insolvent debtors", "Bankruptcy stays", "Enforcement costs"],
        ["Check collection licensing, consumer-debt rules, exemptions and lawful data access."]),
    _candidate(9, "Probate Real Estate", "Real estate services", (23, 18, 16, 9, 10),
        (120000, 900000), (20, 35), (15000, 100000), (3000, 18000), "4–18 months", (2, 3),
        "Modeled as licensed brokerage rather than capital-heavy property acquisition.",
        ["Docket alerts", "Transaction checklists"],
        ["Court delays", "Family disputes", "Housing-market cycles"],
        ["Real estate licensing, fiduciary duties and court-sale approvals may apply."],
        revenue_basis="Retained brokerage commissions after brokerage splits, not home sale values"),
    _candidate(10, "Commercial Cleaning Contracts", "Facility services", (21, 12, 6, 11, 6),
        (250000, 1200000), (8, 16), (15000, 90000), (4000, 18000), "1–4 months", (5, 4),
        "Recurring contracts are attractive, but delivery headcount grows with revenue.",
        ["Scheduling", "Inspection logs", "Billing"],
        ["Labor turnover", "Underpriced contracts", "Customer concentration"],
        ["Observe wage laws, worker classification, chemical safety and insurance requirements."],
        revenue_basis="Cleaning contract revenue; scalable only with more paid crew hours"),
    _candidate(11, "Equipment Brokerage", "Industrial brokerage", (22, 20, 18, 11, 10),
        (100000, 800000), (25, 45), (10000, 75000), (2500, 14000), "2–9 months", (1, 3),
        "Fee-only brokerage avoids inventory, while inspections and deal sourcing remain manual.",
        ["Inventory matching", "Buyer alerts"],
        ["Equipment defects", "Fraud", "Lumpy commissions"],
        ["Check dealer licensing, lien releases, warranties and export controls."],
        revenue_basis="Broker commissions only; excludes equipment transaction value"),
    _candidate(12, "Freight Brokerage", "Logistics", (23, 10, 10, 7, 12),
        (1000000, 5000000), (3, 8), (50000, 250000), (6000, 30000), "2–6 months", (3, 2),
        "Large billings conceal carrier costs, thin net margins and intensive exception handling.",
        ["Load matching", "Shipment tracking", "Invoice reconciliation"],
        ["Carrier fraud", "Claims", "Shipper nonpayment"],
        ["US property brokers generally need FMCSA authority and $75,000 bond or trust security.",
         "Verify current financial-responsibility and carrier-vetting requirements."],
        revenue_basis="Gross shipper billings including carrier costs; accounting presentation can differ"),
    _candidate(13, "Business Acquisition", "Operating business ownership", (24, 16, 7, 2, 8),
        (750000, 3000000), (8, 18), (200000, 1000000), (15000, 70000), "6–18 months", (7, 3),
        "Existing cash flow requires purchase capital, retained staff and debt-service discipline.",
        ["Financial reporting", "Back-office workflows"],
        ["Hidden liabilities", "Customer attrition", "Leverage"],
        ["Review employment, tax, licenses, lender covenants and transaction disclosures."],
        revenue_basis="Acquired business sales; margin after interest, before principal repayments"),
    _candidate(14, "Medical Equipment Resale", "Equipment trading", (21, 16, 13, 6, 8),
        (250000, 1800000), (10, 22), (75000, 400000), (5000, 22000), "3–9 months", (2, 4),
        "Specialist refurbishment, inventory and traceability reduce lean-team economics.",
        ["Inventory tracking", "Service-history indexing"],
        ["Device liability", "Obsolescence", "Unsellable inventory"],
        ["Check device-specific FDA obligations, servicing versus remanufacturing and state licensing.",
         "Sanitize stored patient data and verify decontamination procedures."],
        revenue_basis="Gross equipment resale proceeds; acquisition and refurbishment included in margin"),
    _candidate(15, "Insurance Restoration", "Property restoration", (24, 13, 5, 5, 7),
        (500000, 2500000), (8, 18), (75000, 350000), (10000, 45000), "1–6 months", (5, 6),
        "High ticket sizes require field crews, working capital and demanding project oversight.",
        ["Dispatch", "Photo documentation", "Job-cost tracking"],
        ["Claim disputes", "Cash-flow gaps", "Safety incidents"],
        ["Check contractor and remediation licensing; public adjusting may require a separate license.",
         "Do not promise insurer coverage or waive deductibles unlawfully."],
        revenue_basis="Gross restoration billings; subcontractor and material costs included in margin"),
]
_CANDIDATE_SPECS.extend([
    _candidate(16, "Domain Investing", "Digital asset trading", (17, 18, 19, 9, 11),
        (20000, 300000), (15, 40), (10000, 150000), (500, 5000), "3–24 months", (1, 1),
        "Lean portfolios can produce high-margin sales, but low sell-through ties up capital.",
        ["Renewal tracking", "Comparable-sale monitoring", "Inbound inquiry routing"],
        ["Illiquid inventory", "Renewal costs", "Trademark disputes"],
        ["Review trademark conflicts, domain dispute policies and anti-cybersquatting laws."],
        revenue_basis="Gross domain sale proceeds; acquisition and renewal costs included in margin"),
    _candidate(17, "Government Surplus Auctions", "Surplus asset trading", (20, 14, 12, 8, 8),
        (150000, 1000000), (8, 20), (25000, 200000), (3000, 15000), "1–6 months", (2, 3),
        "Discounted lots offer resale spreads, but transport, storage and defects consume margin.",
        ["Auction alerts", "Bid-limit worksheets", "Inventory tracking"],
        ["As-is defects", "Removal deadlines", "Unsold inventory"],
        ["Check auction eligibility, resale permits, title transfer and restricted-item rules."],
        revenue_basis="Gross resale proceeds; purchase, transport and refurbishment included in margin"),
    _candidate(18, "Commercial Lead Generation", "B2B marketing services", (21, 21, 18, 12, 13),
        (100000, 750000), (20, 40), (5000, 40000), (2000, 12000), "1–4 months", (1, 3),
        "Recurring prospecting fees support lean delivery, but qualification and retention need oversight.",
        ["Consent tracking", "CRM routing", "Lead-quality reporting"],
        ["Poor lead quality", "Client churn", "Rising acquisition costs"],
        ["Observe applicable privacy, email marketing, telemarketing and opt-out requirements."],
        revenue_basis="Retainers and accepted-lead fees; excludes client-funded advertising pass-through"),
    _candidate(19, "Intellectual Property Licensing", "Licensing services", (22, 23, 18, 6, 10),
        (50000, 800000), (25, 60), (25000, 250000), (2000, 15000), "6–24 months", (1, 3),
        "Reusable rights can earn royalties, but defensible IP and licensee adoption are costly to establish.",
        ["Royalty reporting", "License renewal alerts", "Contract obligation tracking"],
        ["Unproven demand", "Infringement disputes", "Licensee underreporting"],
        ["Verify chain of title, permitted uses, territorial rights and competition-law constraints."],
        revenue_basis="License fees and royalties; excludes licensees' underlying product sales",
        confidence="Preliminary — Uncertainty Range"),
    _candidate(20, "Specialty Finance Brokerage", "Finance intermediary services", (23, 21, 17, 8, 10),
        (120000, 1000000), (25, 45), (20000, 100000), (4000, 18000), "3–9 months", (2, 2),
        "Fee-only placement avoids lending capital, but underwriting coordination and licensing constrain scale.",
        ["Application checklists", "Lender matching", "Renewal tracking"],
        ["Failed closings", "Lender concentration", "Commission clawbacks"],
        ["Check loan-broker licensing, fee disclosures, fair-lending and data-security duties.",
         "Securities placements may require separate broker-dealer registration."],
        revenue_basis="Retained origination or referral fees only; excludes loan principal"),
    _candidate(21, "Million-Dollar Lead Generation", "Enterprise demand generation", (24, 21, 16, 9, 12),
        (150000, 1200000), (20, 40), (15000, 100000), (4000, 20000), "3–12 months", (2, 3),
        "Targets buyers of million-dollar contracts, not guaranteed million-dollar lead fees or earnings.",
        ["Account qualification", "CRM attribution", "Meeting scheduling"],
        ["Long sales cycles", "Attribution disputes", "Customer concentration"],
        ["Check privacy, outreach consent and sector-specific referral or contingent-fee restrictions."],
        revenue_basis="Retainers and qualified-opportunity fees; excludes client contract values",
        confidence="Preliminary — Uncertainty Range"),
    _candidate(22, "AI-Powered Micro SaaS", "Subscription software", (22, 22, 19, 11, 14),
        (50000, 700000), (15, 45), (10000, 100000), (2000, 15000), "2–9 months", (1, 2),
        "Narrow software products support lean recurring revenue, but inference costs and churn limit margins.",
        ["Subscription billing", "Usage metering", "Onboarding workflows"],
        ["Weak product-market fit", "Model-provider dependency", "Security incidents"],
        ["Review data privacy, model and content licenses, subscription terms and sector obligations.",
         "Validate consequential outputs and avoid unsupported accuracy claims."],
        revenue_basis="Subscription and usage fees; hosting, model usage and support included in margin",
        confidence="Preliminary — Uncertainty Range"),
    _candidate(23, "Enterprise Software Reselling", "Software channel sales", (23, 14, 15, 9, 11),
        (300000, 2500000), (8, 20), (25000, 150000), (5000, 25000), "3–12 months", (2, 3),
        "Large license billings mask vendor costs; renewals help but enterprise sales need specialist labor.",
        ["Renewal alerts", "Quote generation", "License reconciliation"],
        ["Vendor policy changes", "Slow collections", "Channel competition"],
        ["Verify reseller authorization, license terms, procurement requirements and data-processing duties."],
        revenue_basis="Gross license resale and service billings; vendor costs included in margin"),
    _candidate(24, "High-Ticket Affiliate Marketing", "Referral publishing", (21, 22, 19, 12, 13),
        (50000, 600000), (20, 50), (5000, 50000), (1500, 12000), "3–12 months", (1, 2),
        "Commission income avoids fulfillment, but traffic costs and merchant dependence create volatility.",
        ["Link validation", "Conversion reporting", "Content scheduling"],
        ["Commission cuts", "Refund clawbacks", "Traffic loss"],
        ["Clearly disclose affiliate relationships and substantiate advertising and earnings claims.",
         "Check sector-specific restrictions on paid referrals."],
        revenue_basis="Earned affiliate commissions net of reversals; excludes referred purchase values"),
    _candidate(25, "Building an SEO Empire", "Search-driven publishing", (22, 21, 17, 10, 12),
        (80000, 900000), (20, 45), (15000, 120000), (3000, 20000), "6–24 months", (2, 4),
        "A site portfolio can monetize recurring traffic, but editorial quality and search volatility require investment.",
        ["Technical site audits", "Content refresh queues", "Revenue reporting"],
        ["Ranking losses", "Slow audience growth", "Revenue concentration"],
        ["Respect copyright, advertising disclosures, privacy requirements and search platform policies."],
        revenue_basis="Advertising, affiliate and sponsorship revenue; excludes referred merchant sales"),
    _candidate(26, "High-Ticket Brokerage", "Specialist transaction services", (23, 22, 18, 10, 9),
        (100000, 1000000), (25, 50), (15000, 100000), (3000, 18000), "3–12 months", (1, 3),
        "Large specialist transactions can yield substantial commissions, but closing frequency is uneven.",
        ["Buyer-seller matching", "Deal milestone tracking", "Document checklists"],
        ["Failed closings", "Misrepresentation claims", "Lumpy cash flow"],
        ["Confirm asset-specific brokerage licenses, agency disclosures and client-fund handling rules."],
        revenue_basis="Retained transaction commissions only; excludes underlying asset values"),
    _candidate(27, "Digital Product Empire", "Digital education and tools", (22, 23, 19, 12, 14),
        (50000, 800000), (20, 55), (5000, 60000), (1500, 15000), "1–6 months", (1, 3),
        "Reusable products have low delivery costs, but audience building, refunds and updates absorb profit.",
        ["Digital fulfillment", "Customer onboarding", "Sales-tax reporting"],
        ["Weak demand", "Piracy", "Paid acquisition losses"],
        ["Verify content rights, consumer refund rules, digital sales taxes and truthful marketing."],
        revenue_basis="Digital product sales net of refunds; acquisition, platform and support costs included in margin"),
    _candidate(28, "Automated E-Commerce", "Online retail", (23, 13, 14, 8, 12),
        (250000, 2000000), (5, 18), (30000, 250000), (4000, 25000), "2–6 months", (2, 3),
        "Automation reduces routine order work, not inventory exposure, returns or supplier oversight.",
        ["Order routing", "Inventory alerts", "Returns tracking"],
        ["Ad-cost inflation", "Stockouts", "Product liability"],
        ["Check product safety, import duties, sales taxes, privacy and consumer protection requirements."],
        revenue_basis="Retail sales net of refunds; goods, fulfillment and advertising included in margin"),
    _candidate(29, "Productized AI Agencies", "Technology implementation services", (23, 21, 17, 12, 13),
        (100000, 1000000), (20, 40), (5000, 60000), (2500, 18000), "1–4 months", (2, 3),
        "Standardized implementations improve repeatability, but integration exceptions and human review remain costly.",
        ["Client intake workflows", "Deployment checklists", "Usage and quality monitoring"],
        ["Scope creep", "Unreliable outputs", "Client data exposure"],
        ["Obtain authorization for client-system access and define data-processing and IP terms.",
         "Maintain human review for consequential decisions and substantiate performance claims."],
        revenue_basis="Implementation fees and support retainers; excludes client revenue attributed to automation",
        confidence="Preliminary — Uncertainty Range"),
])


def build_29_candidate_pipeline() -> list[dict]:
    """Return all 29 normalized scorecards ranked by score, then candidate number."""
    pipeline = [compute_scorecard(spec) for spec in _CANDIDATE_SPECS]
    pipeline.sort(key=lambda card: (-card["total_score"], card["candidate_number"]))
    for rank, card in enumerate(pipeline, start=1):
        card["rank"] = rank
    return pipeline
