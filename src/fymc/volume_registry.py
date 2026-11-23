"""Canonical 37-volume registry, slug resolver, and dynamic builder loader for FYMC."""
from __future__ import annotations

import importlib


def _ui(
    cover: list[str],
    deck: list[str],
    lead: str,
    summary: str,
    chapters: list[str] | None = None,
    flow: list[list[str]] | None = None,
) -> dict:
    default_chapters = [
        "Business model & revenue boundaries",
        "Decision-makers & payment rails",
        "Unit economics & margin waterfall",
        "Startup capital & lean stack",
        "Beginner traps & failure modes",
        "Sourcing & first deals",
        "End-to-end operating blueprint",
        "Public records, APIs & tooling",
        "Contracts, statutes & scripts",
        "Automation & distribution loops",
        "Small-team pod & exit valuation",
        "First 30-day launch sprint",
    ]
    default_flow = [
        ["SOURCE", "Mine high-intent deal triggers"],
        ["UNDERWRITE", "Screen margin, float & rules"],
        ["ENGAGE", "Execute mandate or pre-sell"],
        ["DELIVER", "Run standardized SOP & ledger"],
        ["VERIFY", "Audit quality, scrubs & statutes"],
        ["COMPOUND", "Reconcile cash & scale pod"],
    ]
    return {
        "cover": cover,
        "deck": deck,
        "lead": lead,
        "summary": summary,
        "chapters": chapters or default_chapters,
        "flow": flow or default_flow,
    }


ALL_VOLUME_SPECS: dict[int, dict] = {
    1: {
        "volume_number": 1,
        "volume_id": "vol-001-heir-hunting",
        "short_slug": "heir-hunting",
        "candidate_number": 1,
        "score": 87,
        "title": "Heir Hunting",
        "subtitle": "The Money-to-Manpower Playbook for Unclaimed Estate Recovery",
        "site_ui": _ui(
            ["HEIR", "HUNTING"],
            ["FIND THE ASSET. TRACE THE HEIR.", "UNDERSTAND THE PROCESS."],
            "A field manual for the intersection of unclaimed assets, family research, and careful casework.",
            "From the first lead to a documented claim: a practical editorial framework for understanding the business without confusing practitioner experience with legal authority.",
            [
                "The business model",
                "Jurisdiction & compliance",
                "Finding unclaimed assets",
                "Qualifying a lead",
                "Genealogy & heir tracing",
                "Evidence & documentation",
                "Ethical first contact",
                "Agreements & fee limits",
                "Building the claim file",
                "Submission & follow-up",
                "Payment & case closure",
                "Systems for a small team",
            ],
            [
                ["DISCOVER", "Source an asset lead"],
                ["SCREEN", "Verify local rules"],
                ["RESEARCH", "Trace & verify heirs"],
                ["ENGAGE", "Contact & agree terms"],
                ["DOCUMENT", "Prepare & file claim"],
                ["RESOLVE", "Track, reconcile, close"],
            ],
        ),
    },
    2: {
        "volume_number": 2,
        "volume_id": "vol-002-surplus-funds-recovery",
        "short_slug": "surplus-funds-recovery",
        "candidate_number": 2,
        "score": 87,
        "title": "Surplus Funds Recovery",
        "subtitle": "The Money-to-Manpower Playbook for Tax-Sale Overages & Foreclosure Excess Proceeds",
        "site_ui": _ui(
            ["SURPLUS", "FUNDS", "RECOVERY"],
            ["FIND THE SURPLUS. VERIFY THE CLAIM.", "BUILD THE RECOVERY FIRM."],
            "The Complete Playbook for Tax-Sale Overages, Foreclosure Excess Proceeds & Building a Contingent Recovery Firm",
            "From tax-sale records and foreclosure dockets to claimant verification, lien priority, and documented disbursement: build a small-team recovery operation around traceable funds and carefully costed casework.",
            [
                "The surplus recovery business model",
                "Tax-sale overages & foreclosure proceeds",
                "Finding surplus funds records",
                "Screening recovery opportunities",
                "Tracing owners & eligible claimants",
                "Lien priority & competing claims",
                "Claimant outreach & engagement",
                "Contingency agreements & fee limits",
                "Building the recovery claim",
                "Filing & tracking disbursement",
                "Recovery fees & case economics",
                "Scaling a contingent recovery firm",
            ],
            [
                ["DISCOVER", "Find tax-sale & foreclosure surplus"],
                ["SCREEN", "Verify funds & filing deadlines"],
                ["RESEARCH", "Trace claimants & lien priority"],
                ["ENGAGE", "Document authority & fee terms"],
                ["FILE", "Submit the supported claim"],
                ["RECOVER", "Reconcile proceeds & close"],
            ],
        ),
    },
    3: {
        "volume_number": 3,
        "volume_id": "vol-003-digital-product-empire",
        "short_slug": "digital-product-empire",
        "candidate_number": 27,
        "score": 94,
        "title": "Digital Product Empire",
        "subtitle": "The Money-to-Manpower Playbook for High-Margin Digital Products & Self-Liquidating Funnels",
        "site_ui": _ui(
            ["DIGITAL", "PRODUCT", "EMPIRE"],
            ["VALIDATE DEMAND. LIQUIDATE CAC.", "SCALE THE CATALOG."],
            "The Complete Playbook for High-Margin Templates, Self-Liquidating Funnels, Merchant-of-Record Checkout & Scaling an $800k/yr 4-Person Catalog",
            "From Ad-Library pain validation and modular B2B systems to Merchant-of-Record global tax automation, order bumps, and evergreen traffic loops: build a zero-COGS digital product portfolio with disciplined contribution margins.",
            [
                "What is a digital product empire?",
                "Who pays & Merchant-of-Record rails",
                "Pricing, order bumps & SLO unit math",
                "Startup stack & zero-COGS hosting",
                "Disputes, tax nexus & piracy traps",
                "Demand mining & 72-hour pre-sales",
                "Packaging, checkout & onboarding",
                "Pixels, micro-extensions & GEO",
                "Billing rules, VAT & DMCA protection",
                "Viral loops & faceless traffic engines",
                "Scaling a 4-person multi-SKU pod",
                "First 30-day SKU launch sprint",
            ],
            [
                ["VALIDATE", "Mine pain & pre-sell"],
                ["PACKAGE", "Ship modular v1.0 SKU"],
                ["WIRE", "MoR tax & order bumps"],
                ["LIQUIDATE", "Co-reg & SLO funnels"],
                ["PROTECT", "CE 3.0 & DMCA hygiene"],
                ["ASCEND", "Compound annual LTV"],
            ],
        ),
    },
    4: {
        "volume_number": 4,
        "volume_id": "vol-004-ai-powered-micro-saas",
        "short_slug": "ai-powered-micro-saas",
        "candidate_number": 22,
        "score": 90,
        "title": "AI-Powered Micro SaaS",
        "subtitle": "The Money-to-Manpower Playbook for Vertical B2B AI Wedges, Token Metering & Lean SaaS Margins",
        "site_ui": _ui(
            ["AI-POWERED", "MICRO", "SAAS"],
            ["ISOLATE THE WEDGE. METER THE TOKENS.", "COMPOUND RECURRING MRR."],
            "The Complete Playbook for Vertical B2B Wedges, Token Metering, Cloud-Credit Stacks & Scaling a $700k ARR 3-to-5 Person Software Firm",
            "From technographic churn mining and multi-tenant Row-Level Security to hybrid token metering, cloud-credit routers, and diagnostic-scanner outbound: build a sticky B2B AI micro-SaaS with >80% gross margins.",
            [
                "Vertical B2B wedges vs wrappers",
                "Who pays & embedded fintech rails",
                "Hybrid pricing & token metering",
                "Startup stack & cloud credit grants",
                "Token loops, injection & churn traps",
                "Scanner outbound & paid-pilot tests",
                "Multi-tenant RLS, RAG & <5m onboarding",
                "Telemetry, extensions & GEO stack",
                "Zero-retention DPAs & ROSCA rules",
                "Competitor hijacking & PLG loops",
                "Scaling a 3-person pod & 4x-6x exits",
                "First 30-day B2B MRR launch sprint",
            ],
            [
                ["VALIDATE", "Mine G2 pain & pre-sell pilots"],
                ["ISOLATE", "Multi-tenant RLS & RAG"],
                ["METER", "Hybrid seat + token caps"],
                ["LAUNCH", "Scanner outbound & vs-pages"],
                ["RETAIN", "Smart dunning & ZDR trust"],
                ["COMPOUND", "Expand NRR & exit-ready books"],
            ],
        ),
    },
    5: {
        "volume_number": 5,
        "volume_id": "vol-005-high-ticket-affiliate-marketing",
        "short_slug": "high-ticket-affiliate-marketing",
        "candidate_number": 24,
        "score": 92,
        "title": "High-Ticket Affiliate Marketing",
        "subtitle": "The Money-to-Manpower Playbook for Recurring B2B Software Shares, Fintech CPA Bounties & S2S Attribution",
        "site_ui": _ui(
            ["HIGH-TICKET", "AFFILIATE", "MARKETING"],
            ["INTERCEPT BUYER INTENT. WIRE S2S.", "COMPOUND RECURRING SHARES."],
            "The Complete Playbook for Recurring B2B Software Shares, Stacked Fintech CPA Bounties, S2S Attribution & Scaling a $600k/yr 3-to-5 Person Referral Portfolio",
            "From bottom-of-funnel comparison calculators and PartnerStack/Impact/Everflow S2S postbacks to FTC 16 CFR Part 255 disclosures, SparkLoop co-reg, and <=25% merchant-concentration caps: build an exit-ready referral media asset.",
            [
                "High-ticket recurring & CPA models",
                "Merchant LTV & 8 attribution rails",
                "Net EPC, clawbacks & Net-60 float",
                "Edge comparison hubs & clean domains",
                "Site-reputation abuse & poaching defense",
                "Spend-velocity & BOFU query mining",
                "Calculators, S2S postbacks & ping-post",
                "Extensions, pixels & multi-engine GEO",
                "FTC 255, TM+ riders & TCPA consent",
                "YouTube, SparkLoop co-reg & SERP loops",
                "3-to-5 person pods & 30x-45x exits",
                "First 30-day commission launch sprint",
            ],
            [
                ["UNDERWRITE", "Approve 3+ high-LTV offers"],
                ["PRE-SELL", "Ship edge ROI calculator"],
                ["TRACK", "Mint click_id & S2S webhooks"],
                ["DISCLOSE", "Enforce FTC 255 & TM+ rules"],
                ["ACQUIRE", "BOFU search, YouTube & co-reg"],
                ["DIVERSIFY", "Cap single merchant <=25%"],
            ],
        ),
    },
    6: {
        "volume_number": 6,
        "volume_id": "vol-006-productized-ai-agencies",
        "short_slug": "productized-ai-agencies",
        "candidate_number": 29,
        "score": 89,
        "title": "Productized AI Agencies",
        "subtitle": "The Money-to-Manpower Playbook for Fixed-Scope B2B AI Sprints, Managed Workflow Retainers & 5-Person Delivery Pods",
        "site_ui": _ui(
            ["PRODUCTIZED", "AI", "AGENCIES"],
            ["FIX THE SCOPE. DEPLOY THE WORKFLOW.", "LOCK IN THE RETAINER."],
            "Fixed-Scope B2B AI Implementation Sprints, Human-in-the-Loop SLA Retainers & Scaling a $1.0M/yr 5-Person Delivery Pod",
            "Replace custom-consulting scope creep with standardized B2B workflow sprints, client-owned inference credentials, and recurring maintenance retainers.",
        ),
    },
    7: {
        "volume_number": 7,
        "volume_id": "vol-007-unclaimed-property-recovery",
        "short_slug": "unclaimed-property-recovery",
        "candidate_number": 5,
        "score": 89,
        "title": "Unclaimed Property Recovery",
        "subtitle": "The Money-to-Manpower Playbook for State Treasury Escheatment, Uncashed Corporate Warrants & Statutory Finder Claims",
        "site_ui": _ui(
            ["UNCLAIMED", "PROPERTY", "RECOVERY"],
            ["INGEST THE LEDGER. VERIFY AUTHORITY.", "EARN THE CONTINGENT FEE."],
            "State-Controller Escheatment Ledgers, Corporate Warrant Matching, Statutory Fee Caps & Lean 3-Person Recovery Operations",
            "Cross-match public state escheatment datasets and municipal warrant registers with corporate officer records under explicit state finder rules.",
        ),
    },
    8: {
        "volume_number": 8,
        "volume_id": "vol-008-commercial-lead-generation",
        "short_slug": "commercial-lead-generation",
        "candidate_number": 18,
        "score": 89,
        "title": "Commercial Lead Generation",
        "subtitle": "The Money-to-Manpower Playbook for Multi-Inbox Outbound, Pay-Per-Call Routing & Verified B2B Pipeline Pods",
        "site_ui": _ui(
            ["COMMERCIAL", "LEAD", "GENERATION"],
            ["ENRICH THE TRIGGER. VERIFY CONSENT.", "ROUTE EXCLUSIVE DEMAND."],
            "Signal-Triggered B2B Outbound, Rank-and-Rent Pay-Per-Call Routing, Ping-Post Ledgers & Scaling a $750k/yr 4-Person Desk",
            "Combine public-filing triggers, multi-domain deliverability hygiene, and seller-specific consent verification to monetize qualified B2B demand.",
        ),
    },
    9: {
        "volume_number": 9,
        "volume_id": "vol-009-million-dollar-lead-generation",
        "short_slug": "million-dollar-lead-generation",
        "candidate_number": 21,
        "score": 86,
        "title": "Million-Dollar Lead Generation",
        "subtitle": "The Money-to-Manpower Playbook for Enterprise ABM Signals, Seven-Figure Deal Origination & Retainer + SQL Mandates",
        "site_ui": _ui(
            ["MILLION-DOLLAR", "LEAD", "GENERATION"],
            ["TRACK EXECUTIVE TRIGGERS. OPEN DOORS.", "PROTECT ATTRIBUTION."],
            "Enterprise Demand Origination, SEC/UCC Trigger Intelligence & Retainer + Qualified-Opportunity Structures for High-ACV Sellers",
            "Originate qualified enterprise opportunities for million-dollar B2B, industrial, and M&A sellers with airtight CRM stage attribution.",
        ),
    },
    10: {
        "volume_number": 10,
        "volume_id": "vol-010-building-an-seo-empire",
        "short_slug": "building-an-seo-empire",
        "candidate_number": 25,
        "score": 89,
        "title": "Building an SEO Empire",
        "subtitle": "The Money-to-Manpower Playbook for Topical-Authority Portfolios, Programmatic Data Hubs, GEO Citations & 30x–45x Exits",
        "site_ui": _ui(
            ["BUILDING AN", "SEO", "EMPIRE"],
            ["OWN THE DATASET. CAPTURE SERP & GEO.", "COMPOUND MEDIA EQUITY."],
            "Programmatic Utility Hubs, Topical-Continuity Domain Rebuilds, Multi-Engine GEO & Scaling a $900k/yr 4-Person Search Portfolio",
            "Build resilient search and AI-citation portfolios backed by proprietary calculators, clean link equity, and diversified ad/lead/affiliate yield.",
        ),
    },
    11: {
        "volume_number": 11,
        "volume_id": "vol-011-high-ticket-brokerage",
        "short_slug": "high-ticket-brokerage",
        "candidate_number": 26,
        "score": 88,
        "title": "High-Ticket Brokerage",
        "subtitle": "The Money-to-Manpower Playbook for Exclusive Sell-Side Mandates, NCNDA Protection & Specialist Asset Closings",
        "site_ui": _ui(
            ["HIGH-TICKET", "BROKERAGE"],
            ["LOCK EXCLUSIVITY. QUALIFY BUYERS.", "CLEAR ESCROW CLEANLY."],
            "Specialist Lower-Middle-Market, Digital Asset, Easement & Luxury Transaction Brokerage for Lean 4-Person Deal Desks",
            "Structure enforceable exclusive mandates, verify licensing boundaries, screen institutional buyers, and settle commissions directly from escrow.",
        ),
    },
    12: {
        "volume_number": 12,
        "volume_id": "vol-012-equipment-brokerage",
        "short_slug": "equipment-brokerage",
        "candidate_number": 11,
        "score": 86,
        "title": "Equipment Brokerage",
        "subtitle": "The Money-to-Manpower Playbook for Heavy Construction, CNC & Fleet Machinery Arbitrage, UCC-1 Lien Checks & Escrow Settlement",
        "site_ui": _ui(
            ["EQUIPMENT", "BROKERAGE"],
            ["VERIFY SERIAL & UCC. INSPECT IRON.", "SETTLE VIA ESCROW."],
            "Surplus Plant, Yellow-Iron, CNC & Commercial Fleet Brokerage Without Warehouse Overhead or Inventory Balance-Sheet Risk",
            "Broker high-ticket industrial machinery across regional price spreads using serial-level UCC-1 searches, third-party inspections, and escrow wires.",
        ),
    },
    13: {
        "volume_number": 13,
        "volume_id": "vol-013-intellectual-property-licensing",
        "short_slug": "intellectual-property-licensing",
        "candidate_number": 19,
        "score": 88,
        "title": "Intellectual Property Licensing",
        "subtitle": "The Money-to-Manpower Playbook for Patent, Brand & Dataset Royalties, Minimum Annual Guarantees & Audit Clauses",
        "site_ui": _ui(
            ["INTELLECTUAL", "PROPERTY", "LICENSING"],
            ["VERIFY CHAIN OF TITLE. DEFINE FIELD.", "AUDIT NET ROYALTIES."],
            "Commercializing Dormant Patents, Trademarks, Industrial Designs & Proprietary Datasets via Minimum-Guarantee Royalty Contracts",
            "Structure field-of-use licensing agreements, quarterly royalty reporting, and audit rights without taking manufacturing inventory risk.",
        ),
    },
    14: {
        "volume_number": 14,
        "volume_id": "vol-014-specialty-finance-brokerage",
        "short_slug": "specialty-finance-brokerage",
        "candidate_number": 20,
        "score": 89,
        "title": "Specialty Finance Brokerage",
        "subtitle": "The Money-to-Manpower Playbook for Commercial Equipment, AR Factoring, SBA & Bridge Debt Placement Without Balance-Sheet Risk",
        "site_ui": _ui(
            ["SPECIALTY", "FINANCE", "BROKERAGE"],
            ["PACKAGE THE FILE. MATCH CREDIT BOX.", "PROTECT ORIGINATION FEES."],
            "Fee-Only Commercial Capital Placement Across Equipment Leasing, Asset-Based Lending, SBA 7(a)/504 & Transferable Tax Credits",
            "Underwrite borrower DSCR and UCC positions upfront, match multi-lender credit matrices, and comply with state commercial finance disclosure laws.",
        ),
    },
    15: {
        "volume_number": 15,
        "volume_id": "vol-015-judgment-recovery",
        "short_slug": "judgment-recovery",
        "candidate_number": 8,
        "score": 79,
        "title": "Judgment Recovery",
        "subtitle": "The Money-to-Manpower Playbook for Commercial Civil Docket Screening, Lawful Assignment & Lien-Priority Enforcement",
        "site_ui": _ui(
            ["JUDGMENT", "RECOVERY"],
            ["SCREEN COLLECTABILITY. PERFECT LIENS.", "ENFORCE WITH COUNSEL."],
            "Unsatisfied Commercial Judgment Underwriting, Assignee-of-Record Protocols, Post-Judgment Discovery & Attorney Co-Enforcement",
            "Filter civil dockets for solvent operating debtors, avoid uncollectible paper, and execute lawful levy, lien, and settlement recoveries.",
        ),
    },
    16: {
        "volume_number": 16,
        "volume_id": "vol-016-probate-real-estate",
        "short_slug": "probate-real-estate",
        "candidate_number": 9,
        "score": 80,
        "title": "Probate Real Estate",
        "subtitle": "The Money-to-Manpower Playbook for Executor Concierge Brokerage, Letters Testamentary Dockets & Estate-Attorney Referral Flywheels",
        "site_ui": _ui(
            ["PROBATE", "REAL", "ESTATE"],
            ["SERVE THE EXECUTOR. SOLVE ESTATE FRICTION.", "EARN REPEAT REFERRALS."],
            "Licensed Probate Brokerage, Independent-Administration vs Court-Confirmation Sales & Estate-Attorney Concierge Partnerships",
            "Build a referral-compounding probate real estate desk around docket intelligence, estate cleanout coordination, and fiduciary transparency.",
        ),
    },
    17: {
        "volume_number": 17,
        "volume_id": "vol-017-domain-investing",
        "short_slug": "domain-investing",
        "candidate_number": 16,
        "score": 83,
        "title": "Domain Investing",
        "subtitle": "The Money-to-Manpower Playbook for Drop-Catch Auctions, Sell-Through Renewal Math, UDRP/ACPA Clearance & Outbound Founder Upgrades",
        "site_ui": _ui(
            ["DOMAIN", "INVESTING"],
            ["UNDERWRITE SELL-THROUGH. CLEAR TESS.", "PRICE FOR END USERS."],
            "Disciplined 1-to-2 Person Domain Portfolio Management Across Exact-Match Category Killers, Aged Authority Drops & Lease-to-Own Rails",
            "Model renewal carry against historical sell-through rates, clear USPTO trademarks pre-bid, and close five-figure upgrades via Escrow.com.",
        ),
    },
    18: {
        "volume_number": 18,
        "volume_id": "vol-018-land-flipping",
        "short_slug": "land-flipping",
        "candidate_number": 6,
        "score": 86,
        "title": "Land Flipping",
        "subtitle": "The Money-to-Manpower Playbook for GIS Parcel Screening, Access/Wetlands Diligence, Minor Subdivisions & Title-Insured Flips",
        "site_ui": _ui(
            ["LAND", "FLIPPING"],
            ["PRICE BY GIS DATA. VERIFY LEGAL ACCESS.", "SUBDIVIDE FOR SPREAD."],
            "Data-Driven Vacant & Infill Land Acquisitions, FEMA/Perc/Easement Underwriting & Fast Cash or Compliant Note Dispositions",
            "Eliminate landlocked and wetland traps before closing, buy below market via ranged mailers, and unlock margin through minor splits.",
        ),
    },
    19: {
        "volume_number": 19,
        "volume_id": "vol-019-enterprise-software-reselling",
        "short_slug": "enterprise-software-reselling",
        "candidate_number": 23,
        "score": 87,
        "title": "Enterprise Software Reselling",
        "subtitle": "The Money-to-Manpower Playbook for Cloud Marketplace Private Offers (CPPO/CSP), Deal Registration & High-Margin FinOps Services",
        "site_ui": _ui(
            ["ENTERPRISE", "SOFTWARE", "RESELLING"],
            ["REGISTER THE DEAL. ATTACH IMPLEMENTATION.", "PROTECT NET SPREAD."],
            "Modern Cloud & Security VAR Operations Across AWS CPPO, Microsoft CSP, Distributor Credit Lines & Renewal Co-Terming",
            "Separate gross license billings from ASC 606 net agency margin and attach high-margin deployment and FinOps retainers.",
        ),
    },
    20: {
        "volume_number": 20,
        "volume_id": "vol-020-government-contract-brokering",
        "short_slug": "government-contract-brokering",
        "candidate_number": 4,
        "score": 79,
        "title": "Government Contract Brokering",
        "subtitle": "The Money-to-Manpower Playbook for SAM.gov Simplified Acquisitions, FAR 52.219-14 Teaming & Lawful Bona Fide Agency Structures",
        "site_ui": _ui(
            ["GOVERNMENT", "CONTRACT", "BROKERING"],
            ["SCORE SOLICITATIONS. OBEY FAR RULES.", "FUND WAWF FLOAT."],
            "Compliant Federal, State & Municipal Bid-Desk Operations, Commercial-Item Supply Fulfilment & Prime/Subcontractor Teaming",
            "Navigate FAR 3.4 contingent-fee and FAR 52.219-14 subcontracting limits cleanly while quoting simplified acquisitions with verified suppliers.",
        ),
    },
    21: {
        "volume_number": 21,
        "volume_id": "vol-021-automated-e-commerce",
        "short_slug": "automated-e-commerce",
        "candidate_number": 28,
        "score": 85,
        "title": "Automated E-Commerce",
        "subtitle": "The Money-to-Manpower Playbook for 3PL-Backed Brands, Authorized High-Ticket Dealer Rails, POAS Accounting & Retention Flows",
        "site_ui": _ui(
            ["AUTOMATED", "E-COMMERCE"],
            ["TRACK CONTRIBUTION MARGIN. AUTOMATE 3PL.", "PROTECT CASH CYCLE."],
            "Lean 5-Person E-Commerce Operations Built on Profit-on-Ad-Spend (POAS), 3PL SLAs, Landed-Cost Discipline & Automated LTV",
            "Avoid deceptive 'passive store' scams and run real 3PL and authorized-dealer retail with strict inventory, tariff, and return controls.",
        ),
    },
    22: {
        "volume_number": 22,
        "volume_id": "vol-022-medical-equipment-resale",
        "short_slug": "medical-equipment-resale",
        "candidate_number": 14,
        "score": 85,
        "title": "Medical Equipment Resale",
        "subtitle": "The Money-to-Manpower Playbook for Hospital Decommissions, Biomed Electrical/Calibration QA, ePHI Sanitization & FDA 21 CFR Rules",
        "site_ui": _ui(
            ["MEDICAL", "EQUIPMENT", "RESALE"],
            ["SANITIZE EPHI. BENCH-TEST BIOMED.", "RESELL WITH DOCUMENTATION."],
            "Acquiring, Bench-Testing & Remarketing Diagnostic, Surgical, Dental & Veterinary Devices Across Domestic & Export Channels",
            "Distinguish lawful servicing from FDA remanufacturing, wipe patient storage media to NIST 800-88 standards, and protect rigging margins.",
        ),
    },
    23: {
        "volume_number": 23,
        "volume_id": "vol-023-mineral-rights",
        "short_slug": "mineral-rights",
        "candidate_number": 7,
        "score": 81,
        "title": "Mineral Rights",
        "subtitle": "The Money-to-Manpower Playbook for Net Mineral Acre Underwriting, Permit/Pooling Dockets, Severed Title Curative & Aggregator Flips",
        "site_ui": _ui(
            ["MINERAL", "RIGHTS"],
            ["VERIFY NET REVENUE DECIMAL. TRACK PERMITS.", "AVOID WORKING-INTEREST LIABILITY."],
            "Acquiring & Flipping Non-Cost-Bearing Mineral & Royalty Interests Ahead of Horizontal Drilling Permits and Forced-Pooling Orders",
            "Calculate exact Net Mineral Acres and division-order decimals, cure severed chains of title, and sell de-risked packages to institutional funds.",
        ),
    },
    24: {
        "volume_number": 24,
        "volume_id": "vol-024-tax-lien-investing",
        "short_slug": "tax-lien-investing",
        "candidate_number": 3,
        "score": 81,
        "title": "Tax Lien Investing",
        "subtitle": "The Money-to-Manpower Playbook for County Certificate Auctions, Bid-Down Yield Math, Sub-Taxing & Post-Tyler Foreclosure Rules",
        "site_ui": _ui(
            ["TAX LIEN", "INVESTING"],
            ["UNDERWRITE PARCEL EQUITY. MODEL REDEMPTION.", "RESPECT STATUTORY NOTICE."],
            "Data-Screened Tax Lien Certificate & Redeemable-Deed Investing Without Blind Landlocked, Brownfield, or Bid-Down Yield Traps",
            "Separate returned principal from statutory interest income, screen EPA/GIS parcel hazards pre-auction, and follow post-Tyler equity rules.",
        ),
    },
    25: {
        "volume_number": 25,
        "volume_id": "vol-025-freight-brokerage",
        "short_slug": "freight-brokerage",
        "candidate_number": 12,
        "score": 85,
        "title": "Freight Brokerage",
        "subtitle": "The Money-to-Manpower Playbook for FMCSA Authority, BMC-84 Bonding, Double-Brokering Defense & Shipper-to-Carrier Float Discipline",
        "site_ui": _ui(
            ["FREIGHT", "BROKERAGE"],
            ["VERIFY CARRIER IDENTITY. PROTECT NET SPREAD.", "CONTROL RECEIVABLE FLOAT."],
            "Specialized Reefer, Flatbed, Oversize & Drayage Freight Brokerage Built on Verified Carrier Vetting and Shipper Credit Limits",
            "Protect thin gross-to-net spreads with 49 CFR 371 compliance, ELD/VIN anti-fraud checks, and disciplined quick-pay vs receivable float.",
        ),
    },
    26: {
        "volume_number": 26,
        "volume_id": "vol-026-government-surplus-auctions",
        "short_slug": "government-surplus-auctions",
        "candidate_number": 17,
        "score": 79,
        "title": "Government Surplus Auctions",
        "subtitle": "The Money-to-Manpower Playbook for GSA/GovDeals Fleet & Lab Lots, SF-97/DEMIL Rules, Rigging Cost Caps & Fast B2B Remarketing",
        "site_ui": _ui(
            ["GOVERNMENT", "SURPLUS", "AUCTIONS"],
            ["CAP ALL-IN LANDED BID. CLEAR DEMIL/SF-97.", "TURN INVENTORY FAST."],
            "Sourcing Undervalued Municipal Fleet, Heavy Equipment & Laboratory Lots and Remarketing to End-User Commercial Buyers",
            "Price buyer premiums, rigging, deadlines, and defect reserves before bidding, and enforce strict DEMIL/ITAR and title compliance.",
        ),
    },
    27: {
        "volume_number": 27,
        "volume_id": "vol-027-business-acquisition",
        "short_slug": "business-acquisition",
        "candidate_number": 13,
        "score": 86,
        "title": "Business Acquisition",
        "subtitle": "The Money-to-Manpower Playbook for Cash-Flowing SMB Acquisitions, Quality of Earnings, Working-Capital Pegs & 100-Day Operator Systems",
        "site_ui": _ui(
            ["BUSINESS", "ACQUISITION"],
            ["AUDIT CASH PROOF. STRESS-TEST DSCR.", "INSTALL GENERAL MANAGEMENT."],
            "Entrepreneurship Through Acquisition (ETA): Off-Market Deal Sourcing, SBA 7(a) + Seller-Note Structuring & Post-Close Margin Expansion",
            "Verify tax-return-to-bank-statement QoE, cap customer concentration, set net working-capital pegs, and avoid buying an underpaid job.",
        ),
    },
    28: {
        "volume_number": 28,
        "volume_id": "vol-028-commercial-cleaning-contracts",
        "short_slug": "commercial-cleaning-contracts",
        "candidate_number": 10,
        "score": 82,
        "title": "Commercial Cleaning Contracts",
        "subtitle": "The Money-to-Manpower Playbook for Recurring B2B & Medical Janitorial Bids, ISSA Production Rates, W-2 Labor Compliance & Supervisor Pods",
        "site_ui": _ui(
            ["COMMERCIAL", "CLEANING", "CONTRACTS"],
            ["BID BY PRODUCTION RATE. VERIFY CLOCK-INS.", "RETAIN RECURRING ACCOUNTS."],
            "Building a $1.2M ARR B2B Facility & Medical Office Cleaning Operation Without Predatory Franchise Fees or Owner Night-Shift Labor",
            "Price square-footage walkthroughs on ISSA labor standards, prevent 1099 misclassification, and lock in high-margin floor/consumable add-ons.",
        ),
    },
    29: {
        "volume_number": 29,
        "volume_id": "vol-029-insurance-restoration",
        "short_slug": "insurance-restoration",
        "candidate_number": 15,
        "score": 87,
        "title": "Insurance Restoration",
        "subtitle": "The Money-to-Manpower Playbook for Emergency Water/Fire/Storm Mitigation, IICRC Psychrometrics, Xactimate Supplements & UPPA Boundaries",
        "site_ui": _ui(
            ["INSURANCE", "RESTORATION"],
            ["DOCUMENT PSYCHROMETRICS. SCOPE ACCURATELY.", "FINANCE CARRIER FLOAT."],
            "High-Ticket Water Mitigation, Contents Packout & Commercial Storm Restoration Backed by Auditable Moisture Logs and Clean Carrier Billing",
            "Separate licensed contracting from public adjusting, never rebate deductibles, and bridge mortgage two-party check float with strict AR controls.",
        ),
    },
    30: {
        "volume_number": 30,
        "volume_id": "vol-030-lending-and-flash-funding-arbitrage",
        "short_slug": "lending-and-flash-funding-arbitrage",
        "candidate_number": 30,
        "score": 93,
        "title": "Lending & Flash-Funding Arbitrage",
        "subtitle": "The Money-to-Manpower Playbook for Escrow-Locked Transactional Double-Close Funding, Gator EMD Lending & Corporate Credit Liquidity Velocity",
        "site_ui": _ui(
            ["LENDING &", "FLASH-FUNDING", "ARBITRAGE"],
            ["VERIFY ESCROW. UNDERWRITE THE EXIT.", "RECYCLE CAPITAL WITH CONTROLS."],
            "Transactional Double-Close Funding, Earnest-Money Deposit Loans & Corporate Credit Liquidity for a Lean Lending Desk",
            "Screen both closing legs, document earnest-money refund rights, and reconcile escrow-controlled disbursements while pricing credit costs, failed exits, and state lending requirements.",
            [
                "Transactional funding vs EMD lending",
                "Title partners & verified closing instructions",
                "Funding fees, cost of capital & velocity",
                "Corporate credit terms & liquidity reserves",
                "Failed closings, wire fraud & deposit losses",
                "Sourcing wholesalers & repeat borrowers",
                "Double-close underwriting & escrow controls",
                "EMD refund rights & release conditions",
                "Lending licenses, usury & loan documents",
                "Funding calendars & repayment reconciliation",
                "Lean credit desk & concentration limits",
                "First 30-day funded-deal launch sprint",
            ],
            [
                ["SOURCE", "Qualify borrowers & title partners"],
                ["UNDERWRITE", "Verify both closings & repayment exit"],
                ["DOCUMENT", "Set loan terms & escrow conditions"],
                ["FUND", "Confirm instructions before disbursement"],
                ["RECONCILE", "Track principal, fees & exceptions"],
                ["RECYCLE", "Release capital within exposure caps"],
            ],
        ),
    },
    31: {
        "volume_number": 31,
        "volume_id": "vol-031-uber-and-commercial-fleet-arbitrage",
        "short_slug": "uber-and-commercial-fleet-arbitrage",
        "candidate_number": 31,
        "score": 89,
        "title": "Uber & Commercial Fleet Arbitrage",
        "subtitle": "The Money-to-Manpower Playbook for Uber Fleet Partner Portals, Commercial Black SUV Shift Dispatch & Zero-Owned-Metal Co-Hosting",
        "site_ui": _ui(
            ["UBER &", "FLEET", "ARBITRAGE"],
            ["CONTRACT THE CAPACITY. VERIFY COVERAGE.", "DISPATCH PROFITABLE SHIFTS."],
            "Uber Fleet Partner Operations, Commercial Black SUV Dispatch & Owner-Vehicle Co-Hosting Without Buying the Fleet",
            "Match eligible owner vehicles with qualified drivers, verify platform and local operating permissions, and manage shift contribution margins after insurance, downtime, cleaning, and claims reserves.",
            [
                "Fleet partner vs co-host operating models",
                "Owner agreements & platform eligibility",
                "Shift revenue, utilization & net contribution",
                "Fleet portals & lean dispatch tooling",
                "Insurance gaps, accidents & downtime traps",
                "Recruiting vehicle owners & qualified drivers",
                "Black SUV shift planning & handover checks",
                "Maintenance, cleaning & incident response",
                "Commercial permits & worker classification",
                "Payout reconciliation & owner reporting",
                "Dispatcher pods & fleet concentration caps",
                "First 30-day managed-fleet launch sprint",
            ],
            [
                ["SOURCE", "Recruit eligible owner vehicles"],
                ["VERIFY", "Check drivers, permits & coverage"],
                ["CONTRACT", "Define custody, payouts & liability"],
                ["DISPATCH", "Schedule shifts & document handovers"],
                ["RECONCILE", "Audit fares, costs & owner shares"],
                ["OPTIMIZE", "Improve utilization & reserve for repairs"],
            ],
        ),
    },
    32: {
        "volume_number": 32,
        "volume_id": "vol-032-payment-processing-and-atm-arbitrage",
        "short_slug": "payment-processing-and-atm-arbitrage",
        "candidate_number": 32,
        "score": 94,
        "title": "ISO Payment Processing & ATM Arbitrage",
        "subtitle": "The Money-to-Manpower Playbook for Wholesale Schedule A ISO Residuals, Dual-Pricing Merchant Terminals & Exclusive Venue ATM Routes",
        "site_ui": _ui(
            ["PAYMENT &", "ATM", "ARBITRAGE"],
            ["AUDIT SCHEDULE A. SECURE THE VENUE.", "RECONCILE RECURRING RESIDUALS."],
            "Wholesale ISO Residual Portfolios, Compliant Dual-Pricing Terminals & Exclusive-Venue ATM Route Economics",
            "Separate merchant processing volume from earned residuals, validate sponsor and network rules, and price ATM placements around cash replenishment, venue shares, security, and transaction density.",
            [
                "ISO residuals vs ATM surcharge revenue",
                "Sponsor banks, processors & Schedule A terms",
                "Basis-point spreads & route unit economics",
                "Terminal deployment & ATM startup capital",
                "Chargebacks, reserves & residual clawbacks",
                "Merchant statement audits & venue prospecting",
                "Dual-pricing disclosures & terminal setup",
                "ATM cash loading & settlement reconciliation",
                "Network rules, PCI scope & local compliance",
                "Residual audits & merchant retention loops",
                "Lean service pods & portfolio transfer rights",
                "First 30-day merchant-and-venue launch sprint",
            ],
            [
                ["SOURCE", "Audit merchant demand & venue traffic"],
                ["PRICE", "Model Schedule A & cash-service costs"],
                ["CONTRACT", "Confirm sponsor terms & placement rights"],
                ["DEPLOY", "Configure terminals & verify disclosures"],
                ["RECONCILE", "Match settlements, residuals & cash"],
                ["RETAIN", "Service accounts & monitor route yield"],
            ],
        ),
    },
    33: {
        "volume_number": 33,
        "volume_id": "vol-033-insurance-housing-and-rental-arbitrage",
        "short_slug": "insurance-housing-and-rental-arbitrage",
        "candidate_number": 33,
        "score": 90,
        "title": "Insurance Housing & Corporate Rental Arbitrage",
        "subtitle": "The Money-to-Manpower Playbook for Displaced-Policyholder ALE Placements, Corporate Master Leases & Mid-Term Relocation Arbitrage",
        "site_ui": _ui(
            ["INSURANCE", "HOUSING", "ARBITRAGE"],
            ["VERIFY THE PLACEMENT. SECURE LEASE RIGHTS.", "CONTROL VACANCY AND PAYMENT FLOAT."],
            "Displaced-Policyholder Housing, Corporate Master Leases & Mid-Term Relocation Placements for a Lean Housing Desk",
            "Coordinate authorized ALE and corporate placements with suitable furnished inventory, written landlord permissions, documented payer commitments, and reserves for vacancy, damage, and collection delays.",
            [
                "ALE placements vs corporate rental models",
                "Housing vendors, adjusters & payer authority",
                "Nightly spreads, occupancy & collection float",
                "Furnished inventory & startup reserve budgets",
                "Vacancy, coverage limits & unpaid extensions",
                "Relocation referrals & landlord sourcing",
                "Master leases & written subletting permissions",
                "Move-in evidence, maintenance & guest support",
                "Habitability, fair housing & local rental rules",
                "Extension approvals & invoice reconciliation",
                "Placement pods & property concentration caps",
                "First 30-day housing-placement launch sprint",
            ],
            [
                ["QUALIFY", "Confirm housing needs & payer authority"],
                ["SOURCE", "Match suitable inventory & lease rights"],
                ["AUTHORIZE", "Document rates, dates & payment terms"],
                ["PLACE", "Inspect the unit & record move-in"],
                ["SERVICE", "Track repairs & approved extensions"],
                ["SETTLE", "Reconcile invoices, deposits & turnover"],
            ],
        ),
    },
    34: {
        "volume_number": 34,
        "volume_id": "vol-034-nemt-and-medical-courier-arbitrage",
        "short_slug": "nemt-and-medical-courier-arbitrage",
        "candidate_number": 34,
        "score": 90,
        "title": "NEMT & Medical Courier Dispatch Arbitrage",
        "subtitle": "The Money-to-Manpower Playbook for Medicaid TPA Transportation Brokers, STAT Lab Specimen Routes & 1099 Fleet Dispatch",
        "site_ui": _ui(
            ["NEMT &", "COURIER", "ARBITRAGE"],
            ["CREDENTIAL THE FLEET. VERIFY THE ORDER.", "DISPATCH WITH TRACEABLE HANDOFFS."],
            "Medicaid Transportation Networks, STAT Laboratory Routes & Credentialed Fleet Dispatch with Documented Service Controls",
            "Separate passenger transportation from specimen logistics, verify broker contracts and service authorizations, and control route margins through credential checks, custody records, and lawful worker classification.",
            [
                "NEMT trips vs medical courier route models",
                "Medicaid TPAs, laboratories & service buyers",
                "Per-trip rates, deadhead & route contribution",
                "Dispatch systems & credentialing startup costs",
                "Missed trips, rejected claims & specimen loss",
                "Broker enrollment & laboratory route sourcing",
                "Driver qualifications & vehicle inspections",
                "STAT dispatch, cold chain & custody records",
                "Privacy, transport rules & 1099 classification",
                "Service verification & clean billing workflows",
                "Dispatch pods & backup fleet coverage",
                "First 30-day credentialed-route launch sprint",
            ],
            [
                ["CONTRACT", "Confirm network terms & service scope"],
                ["CREDENTIAL", "Verify drivers, vehicles & coverage"],
                ["AUTHORIZE", "Validate trip or specimen orders"],
                ["DISPATCH", "Assign qualified capacity & track timing"],
                ["VERIFY", "Record delivery, custody & exceptions"],
                ["RECONCILE", "Audit claims, payouts & route margins"],
            ],
        ),
    },
    35: {
        "volume_number": 35,
        "volume_id": "vol-035-subject-to-and-wraparound-note-arbitrage",
        "short_slug": "subject-to-and-wraparound-note-arbitrage",
        "candidate_number": 35,
        "score": 90,
        "title": "Subject-To & Wraparound Note Arbitrage",
        "subtitle": "The Money-to-Manpower Playbook for Low-Rate SubTo Acquisitions, RMLO-Underwritten Wrap Mortgages & Performing Note Spreads",
        "site_ui": _ui(
            ["SUBJECT-TO", "& WRAP", "ARBITRAGE"],
            ["DISCLOSE THE DEBT. UNDERWRITE THE BUYER.", "SERVICE EVERY PAYMENT."],
            "Subject-To Acquisitions, RMLO-Underwritten Wrap Mortgages & Serviced Performing-Note Spreads with Explicit Debt Risk Controls",
            "Evaluate existing loan terms, due-on-sale exposure, seller liability, and buyer repayment capacity before structuring counsel-reviewed acquisitions and wraps with independent servicing and payment reserves.",
            [
                "Subject-to acquisitions vs wrap note structures",
                "Existing lenders, sellers & buyer obligations",
                "Payment spreads, amortization & reserve math",
                "Title review, servicing & closing costs",
                "Due-on-sale calls, defaults & insurance gaps",
                "Seller sourcing & informed risk disclosures",
                "Acquisition diligence & counsel-led closings",
                "RMLO underwriting & ability-to-repay review",
                "Mortgage licensing & consumer credit rules",
                "Third-party servicing & underlying loan audits",
                "Note portfolio controls & workout planning",
                "First 30-day acquisition-screening sprint",
            ],
            [
                ["SCREEN", "Review loan terms, title & seller goals"],
                ["DISCLOSE", "Explain seller liability & acceleration risk"],
                ["UNDERWRITE", "Verify buyer capacity with an RMLO"],
                ["CLOSE", "Execute counsel-reviewed documents"],
                ["SERVICE", "Track wrap & underlying loan payments"],
                ["MONITOR", "Audit reserves, insurance & defaults"],
            ],
        ),
    },
    36: {
        "volume_number": 36,
        "volume_id": "vol-036-gpu-compute-and-telecom-capacity-arbitrage",
        "short_slug": "gpu-compute-and-telecom-capacity-arbitrage",
        "candidate_number": 36,
        "score": 94,
        "title": "GPU Compute & Telecom Capacity Arbitrage",
        "subtitle": "The Money-to-Manpower Playbook for Bare-Metal H100/H200 Cluster Slicing, Inference Routing & Wholesale SIP/A2P Telecom Spreads",
        "site_ui": _ui(
            ["GPU &", "TELECOM", "ARBITRAGE"],
            ["RESERVE CAPACITY. METER REAL USAGE.", "PROTECT SPREADS AND SERVICE LEVELS."],
            "Bare-Metal H100/H200 Capacity Resale, Metered Inference Routing & Authorized Wholesale SIP/A2P Telecom Operations",
            "Match contracted compute and telecom capacity to verified customer demand, isolate tenants, meter billable consumption, and protect margins with resale permissions, service-level controls, and consent-based messaging safeguards.",
            [
                "GPU capacity vs SIP and A2P resale models",
                "Infrastructure suppliers & authorized resale terms",
                "GPU-hour, token, minute & message margins",
                "Capacity commitments & working-capital reserves",
                "Idle clusters, toll fraud & service-credit losses",
                "Demand validation & committed customer sourcing",
                "H100/H200 slicing & tenant isolation",
                "Inference routing, metering & failover controls",
                "Telecom registration, consent & data obligations",
                "Usage reconciliation & automated spend limits",
                "Lean operations pods & supplier diversification",
                "First 30-day metered-capacity launch sprint",
            ],
            [
                ["VALIDATE", "Confirm workloads & lawful traffic demand"],
                ["CONTRACT", "Secure resale rights & capacity terms"],
                ["PROVISION", "Isolate tenants & configure routes"],
                ["METER", "Track usage, cost & customer limits"],
                ["PROTECT", "Enforce service levels & abuse controls"],
                ["RECONCILE", "Audit supplier bills & realized spreads"],
            ],
        ),
    },
    37: {
        "volume_number": 37,
        "volume_id": "vol-037-saas-discount-and-gpo-arbitrage",
        "short_slug": "saas-discount-and-gpo-arbitrage",
        "candidate_number": 37,
        "score": 94,
        "title": "SaaS Discount Brokerage & GPO Arbitrage",
        "subtitle": "The Money-to-Manpower Playbook for Partner-of-Record (CPOR/VIP/CSP) License Transfers, Master-Agent UCaaS Residuals & Private GPO Spend Splits",
        "site_ui": _ui(
            ["SAAS & GPO", "DISCOUNT", "ARBITRAGE"],
            ["ZERO-MIGRATION LICENSE TRANSFERS", "RECURRING CHANNEL & GPO SPREADS"],
            "Cut SMB Zoom, Adobe, Microsoft 365, and cloud bills through authorized two-tier distributor transfers, Telarus/Avant master-agent residuals, and negotiated GPO volume brackets.",
            "Benchmark invoices against eligible distributor pricing, secure customer-approved license transfers without tenant migration where supported, and reconcile Telarus/Avant UCaaS residuals alongside private GPO spend splits. Separate CPOR attribution from VIP/CSP transfer rules, verify volume commitments, and count only contracted savings and earned rebates after fees and clawbacks.",
            [
                "SaaS discount brokerage & private GPO models",
                "SMB buyers, two-tier distributors & master-agent payment rails",
                "License spreads, UCaaS residuals & GPO split economics",
                "Partner enrollment, lean stack & working-capital needs",
                "Transfer restrictions, clawbacks & volume shortfall traps",
                "Technographic triggers, invoice audits & first customers",
                "Customer consent, VIP/CSP transfers & GPO bracket locks",
                "Distributor portals, billing APIs & renewal tooling",
                "CPOR attribution, channel contracts & savings disclosures",
                "Autopay, eligible VCC rebates & referral loops",
                "Lean account pods, residual ownership & exit valuation",
                "First 30-day license-and-GPO launch sprint",
            ],
            [
                ["TECHNOGRAPHIC TRIGGER", "Find SMB renewal windows & eligible software spend"],
                ["INVOICE BENCHMARK", "Compare net pricing, commitments & service scope"],
                ["CPOR / VIP TRANSFER", "Verify attribution vs transfer rules & authorize VIP/CSP moves"],
                ["GPO BRACKET LOCK", "Document pooled volume, pricing tiers & spend splits"],
                ["AUTOPAY & VCC REBATE", "Authorize payments & reconcile eligible rebates net of fees"],
                ["RENEWAL COMPOUNDING", "Audit savings, residuals & retention before renewal"],
            ],
        ),
    },
}

ACTIVE_PUBLISHED_NUMBERS: tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37)
CANDIDATE_TO_VOLUME_NUMBER: dict[int, int] = {
    int(spec["candidate_number"]): num for num, spec in ALL_VOLUME_SPECS.items()
}


def get_volume_spec_by_candidate(candidate_number: object) -> dict | None:
    """Return the canonical volume spec for a 1..37 candidate_number, or None."""
    if isinstance(candidate_number, bool):
        return None
    try:
        cnum = int(candidate_number)
    except (TypeError, ValueError):
        return None
    vnum = CANDIDATE_TO_VOLUME_NUMBER.get(cnum)
    return ALL_VOLUME_SPECS.get(vnum) if vnum is not None else None


def get_published_volume_ids() -> tuple[str, ...]:
    """Return ordered volume_id slugs for all currently active published volumes."""
    return tuple(ALL_VOLUME_SPECS[n]["volume_id"] for n in ACTIVE_PUBLISHED_NUMBERS)


def _match_volume_number(volume_id: object) -> int | None:
    if isinstance(volume_id, bool):
        return None
    if isinstance(volume_id, int):
        return volume_id if volume_id in ALL_VOLUME_SPECS else None
    if isinstance(volume_id, str):
        if volume_id == "":
            return 1
        for num, spec in ALL_VOLUME_SPECS.items():
            if volume_id in {
                str(num),
                f"{num:03d}",
                f"vol-{num:03d}",
                spec["volume_id"],
                spec["short_slug"],
            }:
                return num
    return None


def get_volume_spec(volume_id_or_num: object = None) -> dict:
    """Return the canonical spec dict for any of the 37 registered volumes."""
    if volume_id_or_num is None:
        return ALL_VOLUME_SPECS[1]
    num = _match_volume_number(volume_id_or_num)
    if num is None:
        raise ValueError("Invalid volume_id")
    return ALL_VOLUME_SPECS[num]


def resolve_registered_volume_slug(
    volume_id: object = None,
    *,
    allow_unpublished: bool = False,
) -> str:
    """Resolve volume aliases strictly without coercing booleans, floats, or whitespace."""
    if volume_id is None:
        return ALL_VOLUME_SPECS[1]["volume_id"]
    num = _match_volume_number(volume_id)
    if num is None:
        raise ValueError("Invalid volume_id")
    if not allow_unpublished and num not in ACTIVE_PUBLISHED_NUMBERS:
        raise ValueError("Invalid volume_id")
    return ALL_VOLUME_SPECS[num]["volume_id"]


def load_volume_builders(volume_slug: str):
    """Return `(diagrams_builder, manuscript_builder, workbook_builder)` for `volume_slug`."""
    spec = get_volume_spec(volume_slug)
    num = spec["volume_number"]
    if num == 1:
        from .volume_001_manuscript import (
            build_volume_001_diagrams_data,
            build_volume_001_manuscript,
            build_volume_001_workbook,
        )
        return build_volume_001_diagrams_data, build_volume_001_manuscript, build_volume_001_workbook
    if num == 2:
        from .volume_002_manuscript import (
            build_volume_002_diagrams_data,
            build_volume_002_manuscript,
        )
        from .volume_002_chapters_b import build_volume_002_workbook
        return build_volume_002_diagrams_data, build_volume_002_manuscript, build_volume_002_workbook
    if num in (3, 4, 5):
        mod = importlib.import_module(f".volume_{num:03d}_manuscript", package=__package__)
        return (
            getattr(mod, f"build_volume_{num:03d}_diagrams_data"),
            getattr(mod, f"build_volume_{num:03d}_manuscript"),
            getattr(mod, f"build_volume_{num:03d}_workbook"),
        )
    mod = importlib.import_module(f".volume_{num:03d}_manuscript", package=__package__)
    diagrams_fn = getattr(mod, f"build_volume_{num:03d}_diagrams_data")
    manuscript_fn = getattr(mod, f"build_volume_{num:03d}_manuscript")
    workbook_fn = getattr(mod, f"build_volume_{num:03d}_workbook", None)
    if workbook_fn is None:
        wb_mod = importlib.import_module(f".vol{num:03d}_workbook", package=__package__)
        workbook_fn = getattr(wb_mod, f"build_volume_{num:03d}_workbook")
    return diagrams_fn, manuscript_fn, workbook_fn
