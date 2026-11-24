"""Canonical 49-volume registry, slug resolver, and dynamic builder loader for FYMC."""
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
        'volume_number': 1,
        'volume_id': 'vol-001-heir-hunting',
        'short_slug': 'heir-hunting',
        'candidate_number': 1,
        'score': 87,
        'title': 'Heir Hunting',
        'subtitle': 'Trace the Family, Prove the Heir, Verify the Assets — Documented Kinship, Probate Discovery, Recovery Claims, and Curative Title',
        'site_ui': _ui(
            ['HEIR', 'HUNTING'],
            ['TEST FAMILY LINKS, IDENTITIES, AND POSSIBLE PRIOR HEIRS', 'BUILD SOURCED FAMILY TREES AND DOCUMENTED BENEFICIARY SEARCHES'],
            'Follow practitioners as they trace living relatives through family trees, newspapers, and vital records, test competing identities, and document the kinship behind inheritance searches.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies with timestamped inline attribution. Practitioners describe relationship checks, missing-beneficiary searches, research documentation, fee arrangements, and cases where newly discovered wills or closer relatives changed the outcome.',
            ['The Heir-Hunting Profession: Services, Fees, and Cases', 'Tracing Descendants Through Family Trees, Newspapers, and Vital Records', 'Find Probate Files Beyond the Name Index', 'Read Wills, Estate Files, and Probate Procedures', 'Resolve Conflicting Evidence and Uncertain Identities', 'Genealogical Sources, Research Documentation, and Digital Record Tools', 'Prepare Deceased-Owner and Unclaimed-Property Claims', 'Surplus & Unclaimed Funds Recovery: County Expertise, State Registration & Business Operations', 'Source Probate Leads and Build Outreach', 'Find Missing Owners and Work Curative-Title Deals', "Heirs' Property, Tangled Title, and Ownership Checks", 'Property Data, Ownership Research & Genealogy'],
            [['ASSESS THE CASE', 'Run preliminary research to assess the fit with your skills; check available funds and other claimants before extending fieldwork.'], ['GATHER FAMILY EVIDENCE', 'Start with known relationships, existing sources, family photographs, and inherited papers; search locality-specific catalogs, newspapers, and vital records.'], ['TRACE EACH GENERATION', 'Build sourced parent-child links and follow whole families, including siblings and unmarried relatives; read multiple obituary versions for additional leads.'], ['TEST IDENTITY AND KINSHIP', 'Distinguish same-named households and biological, foster, step, and half relationships; use PBI’s two-source relationship check and second-reviewer approach.'], ['CHECK ENTITLEMENT AND CONTACT', 'Investigate wills and possible closer relatives before treating a wider family as entitled; pursue contact through existing numbers, relatives, and field visits, and verify suspicious letters independently.'], ['DOCUMENT THE SEARCH', 'Record sources, negative findings, unresolved relationships, and contact efforts; use reusable report and citation templates to prepare documented findings.']],
        ),
    },
    2: {
        'volume_number': 2,
        'volume_id': 'vol-002-surplus-funds-recovery',
        'short_slug': 'surplus-funds-recovery',
        'candidate_number': 2,
        'score': 87,
        'title': 'Surplus Funds Recovery',
        'subtitle': 'Find the Funds, Prove the Claim, Reach Owners and Heirs, and Build a Repeatable Recovery Pipeline',
        'site_ui': _ui(
            ['SURPLUS', 'FUNDS', 'RECOVERY'],
            ['TEST FREE-LIST RESEARCH, CLAIMANT OUTREACH, AND CLAIM VERIFICATION', 'BUILD REPEATABLE RECOVERY WORKFLOWS FROM RECORDS TO PAYOUT'],
            'Follow practitioner workflows for finding surplus funds, verifying claimant entitlement and competing debt, reaching owners and heirs, and moving documented claims toward recovery.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies with timestamped inline attribution. They trace surplus recovery from free-list research and claimant outreach through agreements, claim submission, state-specific timing, and payout risks, distinguishing reported recoveries and collected fees from contracted or expected income.',
            ['How the Surplus Recovery Business Works', 'Starting and Growing a Surplus Funds Recovery Business', 'Find Free Lists and Build Your Own', 'Verify the Surplus and Research Competing Debt', 'Mortgage Foreclosures and Sheriff-Sale Recovery', 'Difficult Claimants, Heirs, and Estate Cases', 'Reach Claimants and Address Distrust', 'The Surplus-Funds Call: Scripts and Live Examples', 'From Signed Agreement to Claim Submission', 'State Rules, Claim Timing, and Payout Risks', 'Beyond Foreclosure: State and Bankruptcy Funds', 'Build a Repeatable Recovery Operation'],
            [['FIND', 'Search county surplus and excess-proceeds records, compare auction results, and learn how the holding office publishes balances and claim instructions.'], ['VERIFY', 'Confirm funds remain, check existing claims and deadlines, and research ownership and competing debt as they stood at the sale.'], ['LOCATE', 'Identify the correct claimant, trace current contact details, and examine deeds and death dates when heirs or estates may be involved.'], ['CONTACT', 'Use calls, texts, and letters to reach claimants, address distrust with evidence, and keep a record of each contact and follow-up.'], ['DOCUMENT', 'Secure the applicable agreement and claim paperwork, resolve identification gaps, and check originals, notarization, and attorney needs.'], ['SUBMIT AND TRACK', 'Submit to the appropriate holding office, follow the claim through processing, and distinguish recovery proceeds, owner allocations, expenses, and collected fees.']],
        ),
    },
    3: {
        'volume_number': 3,
        'volume_id': 'vol-003-digital-product-empire',
        'short_slug': 'digital-product-empire',
        'candidate_number': 27,
        'score': 94,
        'title': 'Digital Product Empire',
        'subtitle': 'Solve One Buyer Problem, Build AI-Assisted Products, and Sell Through Templates, Offer Stacks, Newsletters, Communities, and Faceless Content',
        'site_ui': _ui(
            ['DIGITAL', 'PRODUCT', 'EMPIRE'],
            ['192 PRACTITIONERS BUILD PDFS, EBOOKS, APPS, AND NOTION TEMPLATES', 'TEST BUYER DEMAND, STOREFRONTS, CONTENT, AND OFFER SEQUENCES'],
            'Build a digital product around a specific buyer and problem, then connect product creation, storefront setup, distribution, and follow-on offers while tracking customer outcomes and sales economics.',
            'All 12 chapters of Digital Product Empire synthesize 192 verbatim YouTube practitioner testimonies with timestamped inline attribution. The accounts connect AI-assisted products and Notion templates with storefront economics, payment choices, upsells, paid funnels, communities, launch models, newsletters, and faceless content, examining both demonstrated workflows and operational bottlenecks.',
            ['Choose Your Digital Product Business Model', 'Build Products with AI: PDFs, eBooks, and Apps', 'Create and Sell Notion Templates', 'Choose a Storefront and Calculate What You Keep', 'Payments, Sales Tax, and Merchant-of-Record Choices', 'Build the Order Bump and Upsell Sequence', 'Build a Self-Liquidating Offer Funnel', 'Low-Ticket Ads, Funnel Economics, and Scaling Cases', 'Launch and Operate a Paid Community', 'Choose Between Cohorts, Live Launches, and Evergreen', 'Build and Monetize an Expertise-Led Newsletter', 'Sell Digital Products Through Faceless Content'],
            [['CHOOSE THE BUYER', 'Research a specific buyer and painful problem, then define the offer before choosing the product format.'], ['BUILD AND INSPECT', 'Create a focused PDF, ebook, app, or Notion template; edit AI output and inspect the pages, formulas, and functions before sale.'], ['SET UP THE SALE', 'Publish the product listing, make access instructions clear, connect payments, and test the app purchase flow with a real credit card.'], ['BUILD DISTRIBUTION', 'Start audience-building during creation, connect a small-win freebie to the paid offer, and use organic content to test demand before paid promotion.'], ['CONNECT THE OFFERS', 'Use email follow-up and relevant courses, memberships, or coaching to extend the entry product without switching to a different customer.'], ['DIAGNOSE AND IMPROVE', 'Separate weak views, visits, and purchases when diagnosing sales; improve listings and support instructions while tracking actual customer outcomes.']],
        ),
    },
    4: {
        'volume_number': 4,
        'volume_id': 'vol-004-ai-powered-micro-saas',
        'short_slug': 'ai-powered-micro-saas',
        'candidate_number': 22,
        'score': 90,
        'title': 'AI-Powered Micro SaaS',
        'subtitle': 'Find Paid Pain, Build Narrow AI Tools, Secure Access, Meter Usage, and Keep Customers',
        'site_ui': _ui(
            ['AI-POWERED', 'MICRO', 'SAAS'],
            ['TEST NARROW PROBLEMS, BUYER DEMAND, AND DELIVERY ECONOMICS', 'BUILD SPECIALIZED AI TOOLS AROUND REAL CUSTOMER WORKFLOWS'],
            'Explore how practitioners turn recurring manual work and dissatisfaction with existing tools into focused AI products, testing customer demand, distribution, workflow reliability, and margins along the way.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies with timestamped inline attribution. They examine problem selection, vertical specialization, building and launching, application security, AI costs, billing, recurring-revenue economics, platform integrations, discovery, and retention without flattening competing approaches into a single formula.',
            ['Find a Narrow Problem Worth Building For', 'Choose a Vertical and Examine Its Defensibility', 'Building and Launching AI-Powered Micro SaaS', 'Launching on Product Hunt and Securing Multi-Tenant Apps with PostgreSQL RLS', 'Reduce AI Costs with Caching and Model Routing', 'Bootstrapped AI Micro-SaaS: Economics, Startup Credits & Launch', 'Usage-Based Billing for APIs, AI Apps & SaaS', 'Read the Economics Behind Recurring Revenue', 'Build Around Chrome, Shopify, and Existing Platforms', 'Bootstrapped SaaS: First Revenue, Product Hunt Launches, and Scaling', 'Win Discovery Through SEO and AI Recommendations', 'Reduce Churn and Recover Failed Payments'],
            [['FIND THE PROBLEM', 'Map repeated manual work, study complaints about existing tools, and validate that the problem exists beyond your own workplace.'], ['LOCATE THE BUYER', 'Identify where customers will come from and explore customer segments one at a time before committing to development.'], ['TEST THE COMMITMENT', 'Sell a single valuable outcome, seek outside customer usage, and make any pre-sale delivery and refund commitments explicit.'], ['BUILD THE WORKFLOW', 'Separate judgment from mechanical tasks and build specialized AI workflows around customer needs, relevant data, and integrations.'], ['SECURE AND EVALUATE', 'Resolve missing authentication before publishing paid-generation features, define gold-standard answers, and rerun existing tests after prompt changes.'], ['CHECK THE ECONOMICS', 'Compare pricing with delivery costs, reassess free-plan limits, and track whether product improvements strengthen gross margins.']],
        ),
    },
    5: {
        'volume_number': 5,
        'volume_id': 'vol-005-high-ticket-affiliate-marketing',
        'short_slug': 'high-ticket-affiliate-marketing',
        'candidate_number': 24,
        'score': 92,
        'title': 'High-Ticket Affiliate Marketing',
        'subtitle': 'Recurring SaaS, Buyer-Intent Content, and Trust-Building Funnels—Scale Calls, Leads, Paid Traffic, and Email with Verified Tracking and Clear Disclosures',
        'site_ui': _ui(
            ['HIGH-TICKET', 'AFFILIATE', 'MARKETING'],
            ['TEST RECURRING OFFERS, BUYER INTENT, AND ACQUISITION ECONOMICS', 'BUILD BRIDGE FUNNELS, TRACKED LEAD FLOWS, AND EMAIL AUDIENCES'],
            'Explore how practitioners select recurring and high-ticket offers, build trust through content and funnels, and track affiliate sales, calls, and leads against acquisition costs and program rules.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies with timestamped inline attribution. They examine offer selection, affiliate networks, bridge funnels, search visibility, call and lead delivery, conversion tracking, paid acquisition, newsletters, and disclosure requirements while distinguishing reported results from illustrative economics.',
            ['Recurring SaaS & High-Ticket Affiliate Marketing', 'Find and Manage Offers on PartnerStack and Impact', 'Build Bridge Pages and High-Ticket Sales Funnels', 'Borrowed-Authority SEO and Reputation-Abuse Risk', 'Capture Buyer Searches with Reviews and Comparisons', 'AI-Era SEO, GEO & High-Ticket Affiliate Growth', 'Pay-Per-Call Affiliate Marketing: Traffic, Buyers, Tracking & Scaling', 'Lead Arbitrage: Traffic, Buyers, and Delivery', 'Track Referrals, Sold Leads, and Conversion Events', 'Paid Affiliate Traffic and Acquisition Economics', 'Newsletter Growth, Email Offers, and Paid Recommendations', 'Affiliate Disclosures, Endorsements, and Brand-Name Advertising'],
            [['QUALIFY OFFERS AND BUYERS', 'Match products to audience problems, inspect demand and retention, apply to relevant programs, and confirm commission terms, refund windows, buyer criteria, and payment timing.'], ['BUILD THE CONVERSION PATH', 'Connect opt-in pages, bridge videos, useful follow-up emails, and offer-specific destinations; for calls and leads, establish routing, delivery, and buyer acceptance requirements.'], ['CREATE BUYER-FOCUSED CONTENT', 'Publish reviews, comparisons, tutorials, and newsletters grounded in product experience, clear answers, and consistent entities; weigh borrowed-authority visibility against removal and reputation-abuse risk.'], ['VALIDATE TRACKING AND PERMISSIONS', 'Test affiliate links, referral IDs, call routes, webhooks, and sold-lead events before sending traffic; verify clear disclosures, endorsement accuracy, and brand-advertising permissions.'], ['TEST ACQUISITION ECONOMICS', 'Run bounded traffic tests, check search terms and subscriber quality, and compare acquisition costs with accepted calls, sold leads, commissions, refunds, and delayed payment.'], ['REFINE AND SCALE SELECTIVELY', 'Use conversion evidence and buyer feedback to improve content, targeting, and follow-up; expand only where margins, lead acceptance, retention, and delivery capacity support it.']],
        ),
    },
    6: {
        'volume_number': 6,
        'volume_id': 'vol-006-productized-ai-agencies',
        'short_slug': 'productized-ai-agencies',
        'candidate_number': 29,
        'score': 89,
        'title': 'Productized AI Agencies',
        'subtitle': 'Sell the Outcome, Charge for Diagnosis, Build Reliable Agents, and Earn Retainers with Clear Scope and Human Handoffs',
        'site_ui': _ui(
            ['PRODUCTIZED', 'AI', 'AGENCIES'],
            ['BUILD PAID AUDITS, AUTOMATIONS, AND RECURRING SERVICE OFFERS', 'TEST VOICE AGENTS, RAG, AND CUSTOMER SUPPORT SYSTEMS'],
            'Turn business bottlenecks into scoped AI services through paid audits, productized delivery, practical agent tests, and monthly support with clear operating boundaries.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies with timestamped inline attribution, covering offer selection, design subscriptions, paid audits, retainers, prospecting, and client delivery. Practitioners compare automation platforms, test voice agents and retrieval systems, build customer-support workflows, and examine the costs, scope limits, privacy controls, and human handoffs behind those services.',
            ['Choose an AI Agency Offer Businesses Actually Need', 'The Designjoy Model: Building a Profitable Solo Design Subscription', 'Sell and Deliver Paid AI Audits', 'Package Projects into Monthly Retainers', 'Selling AI Services: Prospecting, Outreach, Audits & Closing Clients', 'Win B2B Clients with LinkedIn and Better CRM Data', 'Zapier vs Make vs n8n: AI Automation Tools, Costs & Self-Hosted Agents', 'AI Voice Agents: Build Tutorials, Platform Comparisons & Real-World Tests', 'AI Agents, RAG, and Knowledge Graphs Explained', 'AI Customer Support: Tools, Automation & Agency Business Models', 'n8n Client Delivery, Scope-Creep Control & White-Label AI Voice Agents', 'Set Privacy, Contract, and Acceptance Boundaries'],
            [['VALIDATE THE OFFER', 'Find a business willing to pay for a specific improvement in time, money, or focus; start with a small quick win rather than building workflows nobody wants.'], ['PROSPECT WITH CONTEXT', 'Define the buyer, improve CRM data, and use referrals, LinkedIn, or targeted outreach to surface a concrete operational problem before pitching implementation.'], ['AUDIT AND PRIORITIZE', 'Interview leaders and frontline staff, map the current workflow, confirm estimated savings with the client, and rank opportunities by impact and implementation effort.'], ['SCOPE AND BUILD', 'Agree on deliverables, connected tools, payment terms, usage limits, privacy requirements, and acceptance criteria; then build the smallest useful automation, voice agent, or support workflow.'], ['TEST AND HAND OVER', 'Test normal requests, interruptions, failures, retrieval quality, and human escalation; document the workflow and walk the client through credentials, operation, and recovery.'], ['OPERATE AND RETAIN', 'Package monitoring, maintenance, or ongoing improvements into explicitly bounded monthly service; control request queues and capacity, separate running costs, and route new features through change approval.']],
        ),
    },
    7: {
        'volume_number': 7,
        'volume_id': 'vol-007-unclaimed-property-recovery',
        'short_slug': 'unclaimed-property-recovery',
        'candidate_number': 5,
        'score': 89,
        'title': 'Unclaimed Property Recovery',
        'subtitle': 'Free State Searches, Capped Finder Fees, Skip-Traced Heirs, Licensed Claim Filing, Bankruptcy and Royalty Recoveries, and Holder Audit Defense',
        'site_ui': _ui(
            ['UNCLAIMED', 'PROPERTY', 'RECOVERY'],
            ['SEARCH STATE AND FEDERAL DATABASES, TRACE OWNERS AND HEIRS, FILE CLAIMS UNDER STATE FEE CAPS', 'BUILD REGISTERED RECOVERY BUSINESSES ON ONE NICHE, DAILY FOLLOW-UP, AND FEES PAID ONLY AFTER PAYOUT'],
            'Field-tested playbooks from unclaimed property practitioners on searching state and federal databases, launching a registered recovery business, tracing owners and heirs, and closing claims under state fee caps.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, each quoted with timestamped inline attribution to its source video. Coverage runs from search entry points and state claim filing through skip tracing, prospect outreach, fee collection, bankruptcy funds, and holder compliance.',
            ['Unclaimed Property Fundamentals and Search Entry Points', 'Launch and Focus the Recovery Business', 'Public Portals and State Return Practices', 'State-by-State Personal Property Searches', 'Find Unclaimed Funds Under Business Names', 'Investigator Requirements and State Claim Filing', 'Skip Tracing, Heirs, and Estate Claims', 'Prospect Outreach and Recovery-Service Credibility', 'Close Claims and Collect Recovery Fees', 'Bankruptcy Unclaimed Funds Recovery', 'Royalties, Insurance, Shares, and Dividends', 'Holder Reporting, Compliance, and Audit Risk'],
            [['RESEARCH', "Pull the state's registration requirements, fee cap, agreement form, and claim-package instructions before dialing, and call the state office if anything is unclear."], ['TARGET', 'Pick one niche and one or two states, download or buy state lists, and filter for big claims, holding a $10,000 floor under a 10% cap.'], ['SEARCH', 'Start at MissingMoney.com, then unclaimed.org state portals, then federal registries for wages, pensions, FHA refunds, failed banks, and bankruptcy courts.'], ['SKIP TRACE', 'Locate owners and heirs for free or through batch skip tracing at about $14 to $15 per 100 leads instead of hours of manual research.'], ['OUTREACH', 'Prospect daily in a roughly three-hour block, weekends included, and commit to three to five follow-up calls per prospect.'], ['CLOSE AND COLLECT', 'Sign notarized agreements, file the claim package, and collect the capped fee only after the claimant is paid, with states like California paying the locator directly.']],
        ),
    },
    8: {
        'volume_number': 8,
        'volume_id': 'vol-008-commercial-lead-generation',
        'short_slug': 'commercial-lead-generation',
        'candidate_number': 18,
        'score': 89,
        'title': 'Commercial Lead Generation',
        'subtitle': 'Own the Asset, Price Backward from Buyer ROAS, and Touch Every Lead in Minutes - Pay-Per-Lead Arbitrage, Waterfall-Verified Lists, Protected Sending Fleets, One-to-One Consent and Ping-Post Routing from the Operators Who Run Them',
        'site_ui': _ui(
            ['COMMERCIAL', 'LEAD', 'GENERATION'],
            ['PAY-PER-LEAD, PAY-PER-APPOINTMENT AND RETAINER MATH TESTED AGAINST A 2X TO 3X BUYER ROAS FLOOR', 'OWNED LEAD ASSETS BUILT ON ONE NICHE, CLEAN LISTS, WARMED INBOXES AND ONE-TO-FIVE-MINUTE SPEED-TO-LEAD'],
            'Operators who left retainers show how to generate commercial leads at $18 to $50, resell them at 1.5x to 3x, and keep buyers reordering by clearing a 2x to 3x return and reaching every lead within minutes.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, each claim carrying timestamped inline attribution to the operator who said it. The chapters run from agency pricing models and campaign economics through list building, cold email infrastructure, local search assets, TCPA consent capture, and lead distribution and follow-up.',
            ['Lead Agency Models, Pricing, and Scale', 'Commercial Campaign Economics and Industry Workflows', 'Build Prospect Lists from LinkedIn, Maps, and Apollo', 'Clay Enrichment and Outbound Workflows', 'Email Infrastructure and Deliverability', 'Run Cold Email Campaigns with Smartlead and AI', 'LinkedIn Outreach and Appointment-Setting Systems', 'Cold Email Agency Launch and Compliance', 'Google Maps, Business Profiles, and Local Services Ads', 'Rank-and-Rent Assets and Roofing Lead Generation', 'TCPA Consent Workshops and Lead-Capture Workflows', 'Lead Distribution, Call Routing, and Follow-Up'],
            [['NICHE', 'Pick one vertical, one brand and one channel where a customer is worth thousands, and confirm each lead is worth $100 or more before copying a blueprint.'], ['PRICE', 'Work every lead price backward from a 2x to 3x buyer ROAS, resell at 1.5x to 3x generated cost, and never sell a lead below what it costs to generate.'], ['TARGET', 'Build prospect lists from LinkedIn, Maps and Apollo, enrich them in Clay, and time outreach to signals such as renewal windows or executives new to the seat.'], ['SEND', 'Start outbound on about 20 inboxes at 20 sends per day, roughly 400 emails daily through Smartlead, for one to two booked calls a day, and avoid cheap scraped lists.'], ['SIGNAL', 'Fire ad-platform conversions only on qualified answers or sold leads, posting them back server-side through the Conversions API instead of thank-you page views.'], ['DELIVER', 'Touch every lead within 1 to 5 minutes using round-robin assignment, auto-call transfer and AI SMS, then require prepayment and cap credits at 10% or less of delivery.']],
        ),
    },
    9: {
        'volume_number': 9,
        'volume_id': 'vol-009-million-dollar-lead-generation',
        'short_slug': 'million-dollar-lead-generation',
        'candidate_number': 21,
        'score': 86,
        'title': 'Million-Dollar Lead Generation',
        'subtitle': 'Problem-led ICPs, tiered ABM, signal-triggered outbound, warm gifting, live-extracted thought leadership, proprietary deal sourcing, exclusive solar and legal lead engines, consistent CRM attribution, and risk-shared commercial models',
        'site_ui': _ui(
            ['MILLION-DOLLAR', 'LEAD', 'GENERATION'],
            ['PROBLEM-LED ICPS, SCORECARDS THAT DISQUALIFY 20-30%, AND SMALL LISTS THAT MORE THAN DOUBLE REPLIES', 'ABM, SIGNAL-LED OUTBOUND, M&A DEAL SOURCING, SOLAR, PROPERTY AND LEGAL LEAD ENGINES WIRED INTO CRM AND REVENUE ATTRIBUTION'],
            'Practitioners show how to define the buyer by the pain you fix, then build account-based, signal-led, podcast-led and sector-specific lead engines across B2B, M&A, solar, property and legal markets, tracked through CRM and revenue attribution.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies on lead generation, from buyer definition and account-based marketing to M&A, solar, property, legal and financial-sector plays. Every claim, metric and quote carries timestamped inline attribution to the practitioner and video it came from.',
            ['Define the Buyer and the Route to Market', 'Build the Account-Based Marketing Operating System', 'Enterprise Account Plays: Gifting, Personalization, and Outbound', 'Build Signal-Led Outbound with Clay and AI', 'Thought Leadership and Podcast-Led Business Development', 'Source Proprietary M&A Deals', 'From M&A Opportunity to Transaction', 'Solar Leads: Prospecting, Appointments, and Sales Results', 'Property Opportunities: Site Readiness, Roof Damage, and Liens', 'Legal Lead Acquisition, Intake, and Retainer Engagements', 'CRM, Revenue Attribution, and AI-Assisted Sales', 'Commercial Models and Financial-Sector Guardrails'],
            [['DEFINE', 'Build the ICP from the problem and outcome rather than product or title, and run the Five Whys until you reach the emotional reason the buyer will act.'], ['SCORE', 'Score accounts on 5 to 7 criteria and disqualify 20 to 30% of open deals. A strong ICP shows roughly a 3x win-rate gap between high and low scores.'], ['SEGMENT', 'Keep lists at 100 leads or fewer, split a 10,000-lead list into 10 x 1,000 segments, cap each sending box at 50 or fewer per day, and email more than one person per company.'], ['TIER', 'Gate ABM entry at about $20,000 ACV or CFO sign-off. Work a short, tiered account list rather than 1,000 accounts, and run sales and marketing as one operating system.'], ['ENGAGE', 'Fire pre-SDR ad campaigns 2 days to 2 weeks before outreach, target open opportunities with ads that answer the top 10 objections, and mine champion job changes.'], ['PROVE', 'Time-box any POV or pilot at 2 or 4 weeks with agreed KPIs. Track accounts in weekly meetings, read no impressions as a distribution problem and no engagement as a content problem, and never ask for more budget to rescue a weak pilot.']],
        ),
    },
    10: {
        'volume_number': 10,
        'volume_id': 'vol-010-building-an-seo-empire',
        'short_slug': 'building-an-seo-empire',
        'candidate_number': 25,
        'score': 89,
        'title': 'Building an SEO Empire',
        'subtitle': 'Building an SEO Empire Through CTR and Click Signals, Rank & Rent, Parasite SEO, Programmatic Pages, Expired Domains, Backlinks, and AI Search/GEO',
        'site_ui': _ui(
            ['BUILDING AN', 'SEO', 'EMPIRE'],
            ['BUILD LOCAL LEAD ASSETS, TOPICAL NETWORKS & AI CONTENT WORKFLOWS', 'TEST LINKS, USER SIGNALS & AI SEARCH VISIBILITY AGAINST BUSINESS RESULTS'],
            'Explore practitioner workflows for Rank & Rent, programmatic and AI SEO, CTR and user-signal tests, parasite SEO and expired domains, backlinks, and AI search visibility—alongside their measurement limits and operating costs.',
            'All 12 chapters synthesize 192 verbatim YouTube SEO practitioner testimonies with timestamped inline attribution. They connect keyword selection, site architecture, content production, authority building, visibility testing, technical diagnosis, and monetization while distinguishing reported outcomes from repeatable evidence.',
            ['Rank & Rent, Real-Estate SEO & Local GBP', 'Keyword Research, Clustering & Topical Opportunity', 'Semantic Authority, Site Architecture & Internal Links', 'Programmatic SEO & AI Content Workflows', 'Backlinks, PBN-Style Portfolios & Digital PR', 'Parasite SEO & Expired-Domain Strategies', 'CTR Manipulation, IP Clicks, Mobile/Residential Proxies & User-Signal Testing', 'Technical Indexing, Crawl Budgets & Log Diagnostics', 'Core Updates, Traffic-Drop Diagnosis & Recovery', 'AI Overviews, LLM Search & GEO Visibility', 'Display-Ad Monetization, RPM & Affiliate Alternatives', 'Agency, SaaS, Directory & Website-Investment Models'],
            [['QUALIFY', 'Start with buyer, seller, or purchase intent; inspect actual search results and exact-query targeting rather than trusting difficulty scores alone.'], ['CLUSTER', 'Group related queries into page opportunities, compare ranking coverage with published coverage, and prioritize contested topical gaps.'], ['ARCHITECT', 'Organize market pages, categories, and contextual content networks; plan publication order and connect detailed pages through relevant internal links.'], ['BUILD', "Develop local lead-generation assets and programmatic or AI content workflows, alongside the corpus's backlink, digital PR, parasite SEO, and expired-domain strategies."], ['TEST', 'Evaluate CTR and user-signal claims alongside local and AI search visibility; account for reporting conditions, ongoing costs, and reversals rather than equating appearances with clicks.'], ['DIAGNOSE & MONETIZE', 'Investigate indexing, crawl behavior, and traffic drops; assess rental, commission, advertising, affiliate, agency, SaaS, directory, and website-investment models against business results.']],
        ),
    },
    11: {
        'volume_number': 11,
        'volume_id': 'vol-011-high-ticket-brokerage',
        'short_slug': 'high-ticket-brokerage',
        'candidate_number': 26,
        'score': 88,
        'title': 'High-Ticket Brokerage',
        'subtitle': 'Commission-only closer seats, Main Street and double Lehman fee ladders, state-by-state M&A broker exemptions, license-state maps, genuine NCNDAs, 60/40 yacht splits and scrubbed jet specs, sub-60-word off-market outreach, SDE and EBITDA multiples, specialist-lane pricing, and seller notes with offset rights that protect closing certainty',
        'site_ui': _ui(
            ['HIGH-TICKET', 'BROKERAGE'],
            ['COMMISSION SPLITS, CLOSE RATES, FEE LADDERS, AND BUYER SCREENS TESTED ON LIVE DEALS', 'LICENSED BROKERAGES, OFF-MARKET PIPELINES, AND PROTECTED CLOSINGS BUILT FROM THE GROUND UP'],
            'From $3K-$25K coaching offers closed over Zoom to double Lehman M&A mandates, yacht and aircraft listings, and tax-credit transfers, practitioners show how intermediaries source, protect, value, and collect on high-ticket deals.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, each claim carrying timestamped inline attribution to its source video. Together they cover the path from remote commission closing and intermediary role selection through registration, NDAs, valuation, specialist markets, and certainty at closing.',
            ['High-Ticket Sales: From First Offer to Repeatable Closings', 'Choosing Your Role: Business Broker, M&A Advisor, or Investment Banker', 'Broker-Dealer Registration and M&A Exemptions', 'Licensing, Supervision, and Brokerage Controls', 'NDAs and Non-Circumvention Agreements', 'Yacht and Aircraft Brokerage: Entry, Sourcing, and Economics', 'Protecting Commissions and Collecting at Closing', 'Building and Running a Brokerage', 'Off-Market Outreach and Deal-Pipeline Management', 'Business Valuation: Earnings, Multiples, and Deal Structure', 'Specialist Markets: Digital Businesses, Infrastructure, and Tax Credits', 'From Deal Presentation to Diligence and Closing Certainty'],
            [['CHOOSE THE LANE', 'Match deal size to buyer pool: Main Street brokers sell owner-operated companies to individuals, M&A advisors run auctions above roughly $5M in value, and bankers enter near $100M.'], ['REGISTER AND LICENSE', 'Clear broker-dealer registration or M&A exemptions, along with licensing and supervision controls, before taking mandates.'], ['SOURCE OFF-MARKET', 'Run high-volume outreach such as 100 DMs a day and 60-second Looms, and track every lead in a managed deal pipeline.'], ['PROTECT AND QUALIFY', 'Sign NDAs and non-circumvention agreements, then screen buyers for cash on hand, backing, and the experience to actually complete.'], ['VALUE AND STRUCTURE', 'Never quote a price before seeing the returns: build the credit memo, run DSCR, and apply earnings multiples to the deal structure.'], ['CLOSE AND COLLECT', 'Carry the deal from presentation through diligence to closing certainty, and collect success fees and commissions at closing.']],
        ),
    },
    12: {
        'volume_number': 12,
        'volume_id': 'vol-012-equipment-brokerage',
        'short_slug': 'equipment-brokerage',
        'candidate_number': 11,
        'score': 86,
        'title': 'Equipment Brokerage',
        'subtitle': 'Consign the Iron, Price on Condition, Measure the Wear, Clear the Lien, and Broker the Money Behind the Seller',
        'site_ui': _ui(
            ['EQUIPMENT', 'BROKERAGE'],
            ["BROKER OTHER PEOPLE'S IRON ON CONSIGNMENT FOR 5 TO 12 PERCENT ACROSS RETAIL, WHOLESALE, AND AUCTION", 'READ PRICES THROUGH SUPPLY, HOUR METERS, HIDDEN OIL LEAKS, AND DOCUMENTED SERVICE HISTORY'],
            "Practitioners who broker, auction, inspect, finance, rent, haul, and machine used equipment show how a home-office broker earns 5 to 12 percent on someone else's machine by pricing on condition, reading auction supply, and demanding the paperwork buyers pay for.",
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, with every claim carried by timestamped inline attribution to the source video. The chapters run from consignment brokering and auction price reading through inspection, liens and fraud, finance, rental economics, heavy haul, carrier compliance, CNC shops, medical imaging and data-center gear, and adjacent business models.',
            ['Building a Used-Equipment Brokerage', 'Reading Used-Equipment Prices', 'Buying and Selling at Equipment Auctions', 'Undercarriage Inspection and Oil Analysis', 'Liens, Sales Paperwork, and Fraud Risks', 'Equipment Finance: Referrals Through Funding', 'Rental Economics and Contractor Equipment Costs', 'Heavy-Haul Planning and Fleet Control', 'Freight-Broker and Carrier Compliance', 'CNC Machines, Shop Economics, and Used Purchases', 'Medical Imaging and Data-Center Equipment', 'Adjacent Business Models and Equipment Case Studies'],
            [['SOURCE', 'Sign consignors averaging 3.5 machines each and hunt badly presented listings that open the door to tougher negotiation and lower prices.'], ['QUALIFY', 'Call the seller before money moves and get the story of why the machine is on the market: a fire, worn-out iron, or a job that ran out.'], ['INSPECT', 'Count hour-meter digits on older Deere tractors, climb up to check transmission and hydraulic housings for oil, and look for fresh drip stripes where it parked.'], ['PRICE', 'Price on condition, not seller hope, using hour-banded auction comps and supply shifts, and bring work orders and warranty paperwork that buyers pay for.'], ['LIST', 'Refuse to go live with poor photos or thin descriptions and push one listing to several channels, then play the long game of 105 days or more.'], ['CLOSE', 'Shield the seller from tire kickers, probe price by phone, and close remotely, with the Academy selling over 50 percent of equipment sight unseen.']],
        ),
    },
    13: {
        'volume_number': 13,
        'volume_id': 'vol-013-intellectual-property-licensing',
        'short_slug': 'intellectual-property-licensing',
        'candidate_number': 19,
        'score': 88,
        'title': 'Intellectual Property Licensing',
        'subtitle': 'Keep Title, Rent the Rights: Perceived Ownership on a $65 Provisional, 5% Royalty Anchors, 20-30 Company Outreach, Half-Projection Minimum Guarantees, Claim-Charted Portfolios, Audit Clauses and AI-Data Deletion Terms',
        'site_ui': _ui(
            ['INTELLECTUAL', 'PROPERTY', 'LICENSING'],
            ['PERCEIVED OWNERSHIP, PROVISIONAL FILINGS AND ASSIGNMENT RECORD SEARCHES', 'ROYALTY RATES, ANNUAL MINIMUMS AND EXCLUSIVE VERSUS NON-EXCLUSIVE GRANTS'],
            'Patent attorneys, licensing coaches and product founders show how to keep title, file a provisional for perceived ownership, and license an invention for 2 to 10% of wholesale backed by annual minimums instead of floating $250,000 in inventory.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, with every quote carrying timestamped inline attribution to its channel and video. The chapters run from choosing a licensing business model through royalty administration to licensing digital IP, AI data and software.',
            ['Choose the Licensing Business Model', 'Research and Protect the Invention', 'Understand Inventor Royalty Economics', 'Find Licensees and Pitch the Product', 'Negotiate the License and Term Sheet', 'Commercialize Research Through Technology Transfer', 'Build a Brand Licensing Program', 'Value and Monetize Patent Portfolios', 'Clear Permissions and Address Infringement', 'Administer, Audit and Account for Royalties', 'License Creative Work and Knowledge', 'License Digital IP, AI Data and Software'],
            [['RESEARCH', 'Run concept-based Boolean searches with parentheses, confirm the exact application number, and pull assignment records for current owners and security interests'], ['PROTECT', 'File a provisional for perceived ownership at the $65 micro entity rate, disclosing every implementation detail and paying the fee the same day'], ['CHOOSE', 'Weigh licensing against assignment and manufacturing, and manufacture only with strong demand, healthy margins, a clear sales channel and operating capacity'], ['PITCH', 'Approach manufacturers as a product developer with polished brochures, formal letters and prototypes, never paying a broker upfront fees'], ['NEGOTIATE', "Lock price, annual minimums and a refusal to indemnify before the first meeting, settling price last against the licensee's next best alternative"], ['STRUCTURE', 'Keep title, pick exclusive or non-exclusive grants carefully, and tier royalties at 7% granted, 5% pending and 1% if the patent never issues']],
        ),
    },
    14: {
        'volume_number': 14,
        'volume_id': 'vol-014-specialty-finance-brokerage',
        'short_slug': 'specialty-finance-brokerage',
        'candidate_number': 20,
        'score': 89,
        'title': 'Specialty Finance Brokerage',
        'subtitle': 'Score the File, Match the One Lender Whose Credit Box Fits, and Get Paid at Funding: Points and Packaging Deposits, Dealer-Channel Equipment Deals, Lifetime Factoring Residuals, SBA and DSCR Underwriting Math, MCA Takeout Ladders, and Capital-Stack Placement',
        'site_ui': _ui(
            ['SPECIALTY', 'FINANCE', 'BROKERAGE'],
            ['MATCH EACH BORROWER TO THE ONE LENDER WHOSE CREDIT BOX FITS, PACKAGE A CLEAN FILE, AND GET PAID ONLY WHEN IT FUNDS', 'PRICE POINTS, PACKAGING DEPOSITS, BACK-END SPLITS, AND FACTORING RESIDUALS ACROSS EQUIPMENT, FACTORING, ABL, SBA, MCA, DSCR, AND CAPITAL STACKS'],
            'Practitioners show how a commercial loan broker who never lends a dollar of their own money turns bank declines into funded deals, from $30,000 on a $2 million loan at 1.5 points to factoring residuals of 10% to 15% of monthly factor fees.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, with every quote, metric, pro-tip, and operator gate carrying timestamped inline attribution to its source video. The chapters cover the full brokerage path, from deal economics and launching a brokerage through equipment finance, factoring, SBA lending, merchant cash advances, DSCR underwriting, and capital stacks.',
            ["The Broker's Role and Deal Economics", 'Launching a Commercial Loan Brokerage', 'Licensing, Compliance, and Professional Positioning', 'Building an Equipment Finance Brokerage', 'Equipment Leasing, Asset-Backed, and Contractor Finance Products', 'Factoring and Accounts Receivable Financing', 'Asset-Based Lending and Supply Chain Finance', 'SBA 7(a) and 504 Lending', 'Merchant Cash Advances: ISO Operations and Debt Restructuring', 'Working Capital, Revenue-Based Financing, and Capital Raising', 'DSCR Loans and Commercial Real Estate Underwriting Metrics', 'Capital Stacks, Tax Credit Finance, and Litigation Funding'],
            [['QUALIFY', "Score the file on deal size, deal type, borrower constraints, and time pressure, and check that the prospect's story matches the bank statements and balance sheet before quoting points."], ['UNDERWRITE', 'Run LTV, DSCR, and debt yield yourself from the rent roll, P&L, and PFS, because a 10% debt yield against an 11% lender test opens a funding gap.'], ['MATCH', 'Call bank commercial managers on Monday or Tuesday to ask where the money is going this week, then place the file with one lender whose credit box fits instead of spraying it.'], ['COMMIT', 'Take a packaging deposit, even $250 with a 45-day LOI refund clause, and set the hair clause up front so messy deals add points at the end.'], ['PACKAGE', 'Scrub the package for credit reports older than 60 days, inactive LLCs, and missing pages, and answer every borrower and referral within 24 to 48 hours.'], ['FUND AND REPEAT', 'Get paid only when the deal funds, then work the capital stack for repeat financing events across acquisition, rehab, permanent financing, equipment, and working capital.']],
        ),
    },
    15: {
        'volume_number': 15,
        'volume_id': 'vol-015-judgment-recovery',
        'short_slug': 'judgment-recovery',
        'candidate_number': 8,
        'score': 79,
        'title': 'Judgment Recovery',
        'subtitle': 'Take the Assignment, Trace the Assets, Levy Every Bank, Record the Lien, and Keep the Judgment Alive Without Breaking Collection Rules',
        'site_ui': _ui(
            ['JUDGMENT', 'RECOVERY'],
            ['SCREEN, ASSIGN, LOCATE ASSETS, AND ENFORCE THE 80 PERCENT OF JUDGMENTS COURTS NEVER COLLECT', 'GARNISHMENTS, LEVIES, LIENS, DEBTOR EXAMS, AND COMPLIANCE GATES BUILT INTO CONTINGENCY DEAL FLOW'],
            'Courts award money but never enforce it, so the practitioners in these 12 chapters take assignment of unpaid judgments, front enforcement costs, locate bank accounts, wages, and property, and keep one-third to one-half of what they collect.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies covering the judgment recovery business, from assignments and debtor examinations to garnishments, liens, out-of-state domestication, bankruptcy, FDCPA and Regulation F risk, and judgment lifespan. Every claim, metric, pro-tip, and operator gate carries timestamped inline attribution to the practitioner channel and video it came from.',
            ['The Judgment Recovery Business Opportunity', 'Assignments, Legal Boundaries, and Deal Paperwork', 'Post-Judgment Enforcement Fundamentals', 'Debtor Examinations and Citations to Discover Assets', 'Wage Garnishments, Bank Levies, and Writs of Execution', 'Judgment Liens, Abstracts, and Real Property', 'Skip Tracing, Asset Investigation, and Court Record Research', 'Domesticating and Enforcing Foreign and Out-of-State Judgments', 'Bankruptcy, Creditor Claims, and Claims Trading', 'Commercial Debt Recovery and Collection Operations', 'FDCPA and Regulation F Compliance Risk', 'Judgment Lifespan, Statutes of Limitation, and Debtor Resistance'],
            [['SCREEN', 'Check bankruptcy filings and death records first, then rate each judgment on where the debtor moved, its size, and other judgments, refusing the roughly 30 percent rated uncollectible'], ['ASSIGN', "Convert the creditor's judgment into a notarized assignment on a 50/50 contingency split or cash purchase, and do not start collecting until it is filed and returned by the court"], ['LOCATE', 'Confirm an attachable asset exists before signing, locating bank accounts first and sending notices only to debtors with a verified asset'], ['ENFORCE', "Pursue driver's license suspension, bank garnishment, wage garnishment of up to 25 percent of gross pay, liens, and till taps"], ['SETTLE', 'Trade writ dismissal for $500 down plus $100 to $200 a month, building a payment stream of about $3,000 per month by the third month'], ['SATISFY', "File SC-130, SC-290, or EJ-100 on full payment without letting a debtor's written demand sit 14 days, and re-check dead files about six months later"]],
        ),
    },
    16: {
        'volume_number': 16,
        'volume_id': 'vol-016-probate-real-estate',
        'short_slug': 'probate-real-estate',
        'candidate_number': 9,
        'score': 80,
        'title': 'Probate Real Estate',
        'subtitle': 'Letters before listings, overbid-ready court confirmations, step-up appraisals, Medicaid claim checks, call-first probate pipelines, attorney referral runways, and pre-completion wholesale contracts',
        'site_ui': _ui(
            ['PROBATE', 'REAL', 'ESTATE'],
            ['COURT LETTERS, FULL VS. LIMITED AUTHORITY, AND CONFIRMATION OVERBIDS BEFORE ANY ESTATE SALE', 'ATTORNEY REFERRALS, SKIP-TRACED DIRECT MAIL, LEAD CALLING, AND WHOLESALE EXITS FOR PROBATE SPECIALISTS'],
            'Probate practitioners converge on one hard rule, that nothing moves on an estate property until the court issues letters, and this volume maps every step from petition and letters through court confirmation, heir decisions, and the specialist business built around them.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies from realtors, estate attorneys, and probate software operators, with timestamped inline attribution on every quote, metric, pro-tip, and operator gate. Coverage runs from filing and letters through court confirmation and overbids, inherited-house decisions, cleanouts, agent listing playbooks, attorney referrals, lead data, calling, wholesaling, and senior transitions.',
            ['Probate From Filing to Letters: The Legal Roadmap Behind Every Estate Property', 'Court Confirmation and Overbids: Selling Probate Property Under Limited vs. Full Authority', 'The Inherited House: Executor and Heir Decisions Before the Sale', "Before and Beyond the Will: Estate Planning, Medicaid Recovery, Reverse Mortgages, and Heirs' Property", 'Estate Cleanouts, Estate Sales, and Property Preservation', 'The Probate Listing Playbook for Agents', 'Building a Probate Specialist Business: The Probate Mastery Methodology', 'Attorney Referral Partnerships', 'Probate Lead Data, Skip Tracing, and Direct Mail', 'Calling and Converting Probate Leads', 'Wholesaling Probate Properties', 'Senior Transitions, Assisted Living, and Real Estate Economics'],
            [['FILE THE PETITION', "File in the decedent's county of domicile with the original will, certified death certificate, petition and fee, listing every heir and relative, including disinherited ones."], ['NOTIFY AND PUBLISH', 'Notify heirs and publish, have a non-party mail the DE121 notice with proof filed, and clear the hearing.'], ['SECURE LETTERS', 'Request full IAEA authority, order at least 5 to 10 certified copies of letters, and treat the letters date as the earliest listing date.'], ['OPEN THE ESTATE ACCOUNT', 'Obtain an EIN, run all estate money through a dedicated estate account, and pay debts in statutory priority order.'], ['CLEAR TITLE AND HEIRS', "Order a preliminary title report as soon as full-authority letters issue, and confirm every heir and heir's spouse can sign before any contract."], ['CONFIRM OR CLOSE', 'Full-authority sales close in 18 to 30 days like regular listings. Limited-authority sales go to a confirmation hearing, where overbids open at the price plus 10 percent of the first $10,000 and 5 percent of the balance.']],
        ),
    },
    17: {
        'volume_number': 17,
        'volume_id': 'vol-017-domain-investing',
        'short_slug': 'domain-investing',
        'candidate_number': 16,
        'score': 83,
        'title': 'Domain Investing',
        'subtitle': 'Buy Low on Comps, Vet Expired Names on Links and Archive History, List Wide on Afternic and Atom, Close Through Escrow or Lease-to-Own, Defend Against UDRP, and Survive the Renewal Bill',
        'site_ui': _ui(
            ['DOMAIN', 'INVESTING'],
            ['192 PRACTITIONERS TEST BUY-LOW, SELL-HIGH FLIPS AGAINST NAMEBIO COMPS, AI APPRAISALS, AND RENEWAL MATH', 'THEY BUILD PORTFOLIOS FROM EXPIRED-DOMAIN HUNTS, DEDICATED REGISTRARS, MARKETPLACE LISTINGS, OUTBOUND SALES, AND ESCROW-CLOSED DEALS'],
            'Domain Investing distills 192 practitioners on how to source cheap names, vet them against comparable sales, list them across Afternic, Sedo, and Atom, and close safely through escrow without letting renewal fees eat the margin.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, spanning beginner flips, registrar and DNS setup, expired-domain auctions, valuation, negotiation, parking, trademarks, and capital. Every claim carries timestamped inline attribution to the channel and video it came from, so each tactic, price point, and warning traces back to its source.',
            ["Domain Flipping from Zero: The Beginner's Buy-Low, Sell-High Playbook", 'Registrars and DNS Infrastructure for the Domain Portfolio', 'Hunting Expired Domains: Auctions, Backorders, and Drop Catching', 'Due Diligence on Aged Domains: Backlink Audits and Wayback History', 'Exact-Match and One-Word Domains: SEO Power and Generic Valuation', 'The DomainSherpa Valuation Room: Portfolio Reviews and Pricing Strategy', 'Outbound Sales, Brokers, and Negotiation', 'Marketplace Listings: Afternic, Sedo, and Atom', 'Closing the Deal: Escrow, Lease-to-Own, and Seller Safety', 'Domain Parking and Traffic Monetization', 'Trademarks, Disputes, and the TLD Landscape', 'Investor Journeys, Challenges, and Capital'],
            [['HUNT', 'Hand-register or snipe cheap names via ExpiredDomains.net, auctions, backorders, and drop catching, treating AI-generated name lists as raw ore'], ['FILTER', 'Reject dashes, misspellings, numbers, and dates; favor short, memorable .com first with .ai and .io as alternates, and audit backlinks and Wayback history on aged names'], ['VALUE', 'Pair GoDaddy appraisals with NameBio comparable sales, discount highball AI estimates, and cap beginner buys around $20 to $50 per name'], ['REGISTER', 'Hold names at a dedicated registrar with free WHOIS privacy priced on renewal rate, and point nameservers to Afternic to cut commission from 25% to 15%'], ['SELL', 'List wide on Afternic, Sedo, Atom, and Namecheap, pitch niche businesses directly, and relist at a new price after 90 days unsold'], ['CLOSE', 'Refuse pay-later buyers and close through escrow or lease-to-own before transfer, then auto-renew keepers and drop dead weight before the renewal bill hits']],
        ),
    },
    18: {
        'volume_number': 18,
        'volume_id': 'vol-018-land-flipping',
        'short_slug': 'land-flipping',
        'candidate_number': 6,
        'score': 86,
        'title': 'Land Flipping',
        'subtitle': 'Buy Deep, Scrub Hard, Sell on Terms: Practitioner Playbooks for Priced Mail and Texting, Per-Acre Comping, Perc and Access Checks, Subdivides and Double Closes, Seller Financing, and RV and Energy Land Plays',
        'site_ui': _ui(
            ['LAND', 'FLIPPING'],
            ['BUY VACANT PARCELS FROM APATHETIC OWNERS AT A DEEP DISCOUNT AND RESELL NEAR MARKET', 'SCRUBBED COUNTY LISTS, HAND-COMPED OFFERS, AND MAIL, TEXT, AND CALL VOLUME THAT CLOSES DEALS'],
            'Land flippers buy vacant parcels from apathetic, free-and-clear owners at a deep discount, verify perc, access, and flood risk, and resell to builders, investors, or retail buyers, with texting and direct mail feeding the pipeline at a reported 3x to 23x return on ad spend.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies covering the full land flipping cycle, from market selection and list building through due diligence, subdividing, title, selling, and alternative land uses. Every metric, pro-tip, operator gate, and quote carries timestamped inline attribution to the practitioner channel and video it came from.',
            ['The Land Flipping Business Model', 'Direct Mail Campaigns for Vacant Land', 'Cold Calling, Texting, and Multichannel Deal Acquisition', 'Data Tools and List Building', 'Comping and Pricing Vacant Land', 'Due Diligence: Perc Tests, Septic, and Site Checks', 'Access, Easements, and Flood Zones', 'Subdividing Land for Profit', 'Approvals, Restrictions, and Encumbrances', 'Offers, Double Closing, and Title', 'Selling Land: Buyers, Seller Financing, and Drone Media', 'Alternative Land Uses: RV Parks, Solar, and Battery Storage'],
            [['PICK THE COUNTY', 'Target counties with at least 200 land sales a year, days on market under 90 to 120, and fewer active listings than sold listings.'], ['BUILD AND SCRUB THE LIST', 'Pull free-and-clear, inherited, or absentee owners, then strip the 40% to 50% of parcels with wetlands, flood, slope, or bad access and the garbage records.'], ['PRICE THE OFFERS', 'Hand-comp acreage bands from median price per acre minus agent, closing, and lender costs, and never let software auto-price the offers.'], ['RUN OUTREACH', 'Send priced mailers at roughly 58 to 69 cents a piece, short texts near 100 characters, and cold calls, then remail and keep working stale leads.'], ['VERIFY THE PARCEL', 'Confirm soil and septic where there is no city sewer, legal deeded access, and flood status, extending inspection 30 to 45 days before earnest money goes hard.'], ['EXIT THE DEAL', 'Resell to builders, investors, or retail buyers, or subdivide to manufacture margin, because the deal picks the exit.']],
        ),
    },
    19: {
        'volume_number': 19,
        'volume_id': 'vol-019-enterprise-software-reselling',
        'short_slug': 'enterprise-software-reselling',
        'candidate_number': 23,
        'score': 87,
        'title': 'Enterprise Software Reselling',
        'subtitle': 'Thin License Margins, Fat Services Stacks: Tiered Partner Margins, Marketplace Private Offers, CSP Thresholds, Renewal Deadlines and Audit Defense from Working Resellers',
        'site_ui': _ui(
            ['ENTERPRISE', 'SOFTWARE', 'RESELLING'],
            ['THE LICENSE IS A THIN-MARGIN ENTRY TICKET; THE MONEY SITS IN IMPLEMENTATION, TRAINING, CUSTOMIZATION AND SUPPORT', "FIX DIRECT SALES FIRST, RECRUIT A NARROW SET OF PARTNERS, AND MAKE THE PARTNER'S MONEY OBVIOUS WITH TIERED MARGINS"],
            'Practitioners who resell enterprise software explain how they make money: VAR margins, channel programs, distributors and marketplaces, Microsoft CSP operations, FinOps, revenue recognition, renewals, procurement, public sector controls, and licensing negotiation.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies on enterprise software reselling, from VAR economics and channel funding to renewals, audits and licensing economics. Every claim, metric and pro-tip carries timestamped inline attribution to the practitioner and video it came from.',
            ['The VAR Business Model', 'Building and Funding a Reseller Channel Program', 'Distributors, Aggregators, and the Marketplace Shift', 'Selling Through AWS Marketplace: Seller Setup and Private Offers', 'Channel Partner Private Offers and Multi-Party Marketplace Deals', 'Operating as a Microsoft CSP', 'FinOps for SaaS and Licensing', 'Revenue Recognition for Resold Software', 'SaaS Renewal Management', 'Procure-to-Pay and Vendor Onboarding', 'Public Sector Reselling and Vendor Risk Controls', 'Negotiation, Audits, and Licensing Economics'],
            [['PROVE DIRECT', 'Do not open a VAR channel until the product sells and converts direct, because no partner will sell it better than you can.'], ['RECRUIT SELECTIVELY', 'Sign only partners you can activate, not 200 logos with 195 sitting idle, and mine your existing user base for agencies already using the product.'], ['TIER THE ECONOMICS', 'Offer free training, no joining fees and tiered margins such as 10/20/30 percent, pricing partner payouts against the stages of a $21,500 direct CAC.'], ['REGISTER DEALS', 'Run deal registration and lead distribution through PRM, keeping partner-submitted data in separate CRM fields instead of letting partners edit the CRM directly.'], ['QUOTE TRANSPARENTLY', 'Publish implementation ballparks, provide budgetary numbers up front, and require a written markup definition and a broken-out tax line on every quote.'], ['TRACK GO-LIVE', 'Track go-live into production and active users for every customer from purchase, since failing to go live is the primary non-renewal driver.']],
        ),
    },
    20: {
        'volume_number': 20,
        'volume_id': 'vol-020-government-contract-brokering',
        'short_slug': 'government-contract-brokering',
        'candidate_number': 4,
        'score': 79,
        'title': 'Government Contract Brokering',
        'subtitle': 'Three Quotes, a 7-25% Markup, and the 50% Line: Middleman Primes, DIBBS Parts Brokering, FPDS Price Intelligence, Set-Aside Outreach, and Funding the 30-Day Payment Gap',
        'site_ui': _ui(
            ['GOVERNMENT', 'CONTRACT', 'BROKERING'],
            ['SAM.GOV REGISTRATION, SET-ASIDE TARGETING AND THREE-QUOTE MARKUP BIDS', 'PRIME LIABILITY, SUBCONTRACTING LIMITS AND THE CASH FLOAT TO GET PAID'],
            'Practitioners from boosters to former contracting officers show how to register free through Login.gov and SAM.gov, filter for small business set-asides, pull three vendor quotes, add a 20% to 100% markup, and win as a prime that carries full performance liability without crossing the 100% pass-through line.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies on government contract brokering, from registration and set-aside targeting to pricing, subcontracting limits, DIBBS parts brokering and getting paid. Every claim, metric, pro-tip and quote carries timestamped inline attribution to the practitioner and video it came from.',
            ['The Middleman Model and Its Legal Line', 'Getting Registered and Credentialed', 'Micro-Purchases, Simplified Acquisitions and Commercial Items', 'Case Studies: From First Win to Nine Figures', 'Targeting Set-Asides and State, Local and Cooperative Bids', 'Pricing Intelligence and Cost Buildup', 'Responding to Solicitations and Building Compliant Proposals', 'Teaming, Subcontracting and Prime–Sub Relationships', 'Limitations on Subcontracting, Affiliation and Enforcement', 'Navigating the FAR and Contract Administration', 'Brokering DLA Parts Through DIBBS', 'Funding the Contract and Getting Paid'],
            [['REGISTER', 'Sign in through Login.gov, validate the entity in SAM.gov for a 12-character UEI, and let DLA assign the free five-character CAGE code; renew every 365 days.'], ['TARGET', 'Filter SAM.gov for small business set-asides, open every attachment, and check whether clause 52.219-14 is checked before planning to subcontract.'], ['QUOTE', 'Pull three vendor quotes from the big players before opening a Word document, and line up a backup sub at the same price.'], ['PRICE', 'Pull the prior contract amount from the point of contact, USA Spending or FPDS, then add a 20% to 100% markup.'], ['SUBMIT', 'Confirm the vendor accepts pay-after-paid with a stop-work clause, and document management with an org chart, defined roles and Gantt charts.'], ['FLOAT', 'Prove you can carry sub payroll for 60 to 90 days through a line of credit or cash reserve, because agencies can pay months late.']],
        ),
    },
    21: {
        'volume_number': 21,
        'volume_id': 'vol-021-automated-e-commerce',
        'short_slug': 'automated-e-commerce',
        'candidate_number': 28,
        'score': 85,
        'title': 'Automated E-Commerce',
        'subtitle': 'Authorized-dealer dropshipping on $1,000-plus US brands, supplier accounts won by persistent outreach, contribution margin before CAC, landed cost beyond the invoice, a shorter cash cycle, register-first sales tax, tested 3PLs, scam-proof automation, budgeted returns, AI support with human refund gates, feed-first Google Shopping, and scaling on CAC payback',
        'site_ui': _ui(
            ['AUTOMATED', 'E-COMMERCE'],
            ['THEY TEST NICHES, STRICT MAP POLICIES, AND MULTI-TOUCH SUPPLIER OUTREACH', 'THEY BUILD AUTHORIZED-DEALER STORES ON GOOGLE SHOPPING AT 15-30% MARGINS'],
            "Practitioners show how authorized-dealer stores list $1,000-plus products from established US brands, collect the customer's money first, and let the supplier ship within days, from opening supplier accounts through conversion and scaling to eight figures.",
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies into one operating playbook for automated e-commerce. Every claim, metric, and quote carries timestamped inline attribution to the practitioner and video it came from.',
            ['The High-Ticket Dropshipping Model: Niches, Products, and Real Store Results', 'Opening Supplier Accounts: High-Ticket Brands and Amazon Wholesale Distributors', 'Unit Economics and Contribution Margin', 'Landed Cost: Duties, Tariffs, and the True Cost of Goods', 'Cash Conversion Cycle and Working Capital', 'Sales Tax Nexus and Compliance Automation', 'Outsourced Fulfillment: Inside the 3PL', 'Automating the Back Office, and the Automation Traps', 'Returns, Refunds, and Chargebacks', 'Automated Support and Retention', 'Google Shopping Feeds and Merchant Center', 'Conversion and Scaling to Eight Figures'],
            [['VALIDATE NICHE', "Confirm demand with WordStream or Semrush, keep evergreen trends, drop anything seasonal or under $1,000, and skip products sold by Best Buy, Home Depot, Lowe's or Walmart"], ['BENCHMARK DEALERS', "Search 'buy [brand] [product]' in the Shopping tab, count thriving online-only dealers through Similarweb math, and confirm strict MAP on identical models"], ['APPLY TO BRANDS', 'Register a real business and apply to 10-20 brands at once for 30-50% acceptance, following up on day 1, day 4, a call on day 8, LinkedIn on day 12, and a final email on day 18'], ['VET SUPPLIERS', 'Check address, About Us, social media, Trustpilot and BBB, and reject $5,000-plus minimums, drop-ship fees over $15 per order, or margin under 10 to 15 percent'], ['LIST AND ADVERTISE', "Price chargeback, return and warranty exposure into each brand's margin, then run bottom-of-funnel Google Shopping with Meta pushed to remarketing"], ['COLLECT AND SHIP', "Collect the customer's money first, email the supplier the order, let them ship within days, and keep adding brands so no single supplier dominates revenue"]],
        ),
    },
    22: {
        'volume_number': 22,
        'volume_id': 'vol-022-medical-equipment-resale',
        'short_slug': 'medical-equipment-resale',
        'candidate_number': 14,
        'score': 85,
        'title': 'Medical Equipment Resale',
        'subtitle': 'Buy Hospital Surplus, Biomed-Check Every Unit, Resell or Rerent It: Medicare Rentals, Cross-Border Refurbishing, Third-Party Service, Bench Safety Testing, QMSR and 510(k) Readiness, Helium-Safe Imaging Resale, Sterile-Processing Buyers, and Referral-Driven Device Sales',
        'site_ui': _ui(
            ['MEDICAL', 'EQUIPMENT', 'RESALE'],
            ['BIOMED-CHECKED SURPLUS GEAR, ELECTRICAL SAFETY BENCH TESTS, AND PRE-SHIP QA PROOF WITHIN ORIGINAL MANUFACTURER SPECIFICATIONS', 'REFURBISHING, AUCTION, RENTAL, AND CROSS-BORDER RESALE OPERATIONS BUILT AROUND QMSR, 510(K), AND RECALL OBLIGATIONS'],
            'Practitioners who buy surplus hospital gear cheap, biomed-check and document it, then resell or rerent it show how garage operations, auction houses, and third-party biomeds turn the gap between OEM pricing and the secondary market into a business.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies on medical equipment resale, from sourcing, servicing, and bench testing through FDA regulation, imaging, lasers, clinic buyers, and sales careers. Every claim, metric, pro-tip, and operator gate carries timestamped inline attribution to the practitioner and video it came from.',
            ['The Used Medical Equipment Resale Business', 'Sourcing, Shipping, and Selling Across Borders', 'Servicing, Remanufacturing, and the Third-Party Biomed Business', 'On the Bench: Electrical Safety Testing and Troubleshooting', '21 CFR 820: From QSR to QMSR', 'FDA Device Regulation Fundamentals', 'Building the 510(k) Submission', 'Recalls, Removals, and the MAUDE Database', 'Imaging Equipment: MRI, CT, and X-Ray', 'Medical and Aesthetic Lasers', 'Clinic Buyers: Veterinary, Dental, and Ambulatory Surgery', 'Selling Medical Equipment: Sales Careers and Industry Economics'],
            [['SOURCE', 'Buy surplus hospital gear cheap through liquidations, auctions, and manufacturer trade-in programs, hunting high-demand SKUs and pricing used units on eBay or DotMed against OEM repair quotes.'], ['VERIFY', 'Never ship on a power-on check alone; recheck every unit with a biomed team or sell it explicitly as is.'], ['SANITIZE', 'Confirm HIPAA data removal and internal decontamination with the refurbisher before payment or resale.'], ['DOCUMENT', 'Write condition limits and clear pictures into the listing and provide an unedited functionality video plus pre-ship QA results within original manufacturer specifications.'], ['SHIP', 'Use air-ride, climate-controlled freight with a carrier that has moved medical loads and carries insurance matched to the freight value.'], ['RESELL', 'Sell through showrooms, auctions, and online marketplaces, or bill 13-month Medicare rentals and rerent returned units to the next patient.']],
        ),
    },
    23: {
        'volume_number': 23,
        'volume_id': 'vol-023-mineral-rights',
        'short_slug': 'mineral-rights',
        'candidate_number': 7,
        'score': 81,
        'title': 'Mineral Rights',
        'subtitle': 'Rebuild every decimal before you sign, convert every offer to net royalty acres, trade bonus for royalty, cure title before it costs you, and follow the drill bit from permit to payout.',
        'site_ui': _ui(
            ['MINERAL', 'RIGHTS'],
            ['192 PRACTITIONERS STRESS-TEST DEEDS, LEASES, DECIMALS AND EVERY OFFER PER NET ROYALTY ACRE', 'THEY BUILD TRACT INVENTORIES, TITLE CHAINS, DECLINE-CURVE VALUATIONS AND LEGACIES FOR HEIRS'],
            'Learn what you actually own beneath the surface, how to prove it on a separate mineral chain of title, and how to reconcile your decimal and price every offer the way working landmen, buyers and royalty owners do.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, from mineral estates and leases to division orders, title, shale drilling, valuation, taxes, regulators and market news. Every claim, metric, pro-tip and quote carries timestamped inline attribution to the practitioner and video it came from.',
            ['What You Actually Own: Mineral Estates, Royalties and Their Carve-Outs', 'Locating, Researching and Inventorying Your Minerals', 'The Oil and Gas Lease, Pooling and Owner Bargaining Power', 'Working the Numbers: WI and NRI Calculations', 'Division Orders and the Decimal Interest on Your Check', 'Landmen and Title: From Courthouse to Curative', 'How Wells Get Drilled: Horizontal Technology and the Major Shale Plays', 'Decline Curves, Well Performance and Mineral Valuation', 'Buying and Selling Mineral Rights', 'Taxes, Working Interests and Passing Minerals to Heirs', 'Regulators, Hearings and Permits', 'Mineral Market News, Capital and Emerging Opportunities'],
            [['INVENTORY', 'Pull the legal description from the source deed, plot it on a free state GIS, and log every tract in one spreadsheet with interest type, net acres, lease status and provenance.'], ['TITLE', 'Run a dedicated mineral title search on its separate chain from the surface, hiring a landman at about $600 a day or a limited search at about $3,000 when needed.'], ['VERIFY ACTIVITY', 'Before trusting an alert or a nearby pad, pull the permit and plat and confirm the first take point and lateral footage fall inside your tract.'], ['LEASE', 'Negotiate before signing, confirm which rights the document affects and who the contact represents, and favor the highest royalty rate over the bonus.'], ['RECONCILE DECIMALS', "Check that every owner's decimal sums back to the lease royalty, pull the deeds when it misses, and ask the payer which records support its division order."], ['PRICE AND SELL', 'Convert every offer to dollars per net royalty acre, ask which royalty rate the buyer assumed, and price to remaining economic life after reviewing declines, reserves, operators, rights and lease terms.']],
        ),
    },
    24: {
        'volume_number': 24,
        'volume_id': 'vol-024-tax-lien-investing',
        'short_slug': 'tax-lien-investing',
        'candidate_number': 3,
        'score': 81,
        'title': 'Tax Lien Investing',
        'subtitle': 'Statutory-Rate Certificates, Bid-Down and Premium Auctions, Over-the-Counter Leftovers, Redeemable Deeds, Quiet Title Exits, and IRA-Funded Lien Portfolios as County Tax Sale Practitioners Actually Run Them',
        'site_ui': _ui(
            ['TAX LIEN', 'INVESTING'],
            ['COUNTY SCRIPTS, STATUTORY RATES, REDEMPTION CLOCKS AND OVER-THE-COUNTER LEFTOVERS', 'LIEN YIELD VERSUS DEED DISCOUNTS, PRICED AGAINST TITLE TRAPS AND ATTORNEY COSTS'],
            'Practitioners show how a county sells unpaid property taxes as a first-position certificate that pays a state-set rate of 12 to 36 percent when the owner redeems, which they put at about 95 percent of the time, and how a smaller set of deed and redeemable-deed plays turns unredeemed parcels into property bought at 10 to 20 cents on the dollar.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, each claim carrying timestamped inline attribution to the speaker and video it came from. Together they span foundations, lien-versus-deed models, state playbooks, auction formats, online and over-the-counter buying, due diligence, foreclosure and quiet title, risks, federal tax liens, court challenges, and portfolio funding.',
            ['Tax Lien Investing Foundations', 'Liens vs. Deeds vs. Redeemable Deeds', 'The State-by-State Lien Playbook', 'Auction Formats and the Real Yield', 'Online Auctions and Cheap-Property Deed Plays', 'Over-the-Counter Liens and Deeds', 'Pre-Bid Due Diligence and GIS Research', 'Foreclosure and Quiet Title', 'Risks, Title Traps, and Field Case Studies', 'Federal Tax Liens and IRS Redemption', 'Tyler v. Hennepin, Bankruptcy, and Court Challenges', 'Funding, Structuring, and Scaling the Portfolio'],
            [['SCOUT THE COUNTY', "Call the county for last year's lien count and attendance; 200 to 500 liens with 20 bidders beats 30 liens with 50, and starting small in one county teaches how its auction works."], ['READ THE RULES', "Read the county's terms, deadlines and deposits, and check the state's interest ceiling or penalty, surplus and redemption rules before bringing a dollar."], ['VET THE PARCEL', 'Look at every property and confirm its value, search municipal liens and code violations that survive the sale, and pass on landlocked lots and demolition-grade structures.'], ['RUN THE ALL-IN NUMBER', 'Add the lien or deed price to roughly $2,000 to $5,000 in attorney and foreclosure fees and make sure the total sits well under resale value, with an exit strategy before you bid.'], ['BID OR BUY OVER THE COUNTER', "Bid for yield on parcels likely to redeem or for property on those less likely to, mind Florida's 5 percent floor that a 0 percent bid forfeits, and work the unsold list that appears about 30 days after the sale."], ['TRACK, FORECLOSE AND EXIT', "Log every redemption and expiration date on the day you buy, act before deadlines such as Florida's seven-year deed application lapse, and move foreclosed houses with big signs and Craigslist."]],
        ),
    },
    25: {
        'volume_number': 25,
        'volume_id': 'vol-025-freight-brokerage',
        'short_slug': 'freight-brokerage',
        'candidate_number': 12,
        'score': 85,
        'title': 'Freight Brokerage',
        'subtitle': 'Niche into steel, lumber and machinery, post the $75,000 bond at a negotiated premium, win five great shippers with relentless touches, price from the truck up, lock accessorials into the rate con, and fence out double brokers before the cargo goes dark',
        'site_ui': _ui(
            ['FREIGHT', 'BROKERAGE'],
            ['HOW 192 PRACTITIONERS LAUNCH AN MC AUTHORITY, POST THE $75,000 BOND AND PROSPECT NICHE SHIPPERS', 'HOW THEY VET CARRIERS, PRICE THE SPREAD, FUND THE FLOAT AND DEFEND AGAINST DOUBLE BROKERING'],
            "Freight brokerage operators describe the business as a spread trade financed like a bank: contract the shipper's rate, buy the truck cheaper, and fund the gap between quick-paying carriers and slow-paying shippers.",
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, from authority filing and the $75,000 surety bond to cold calling, accessorials, double brokering and cargo claims. Every metric, pro-tip, operator gate and quote carries timestamped inline attribution to the practitioner and video it came from.',
            ['The Business Case and Launch Roadmap', 'Broker Authority, Registration and the Transparency Fight', 'The $75,000 Surety Bond', 'Freight Agent vs. Freight Broker', 'Finding and Winning Shippers', 'Cold Calling That Books Freight', 'Quote to Cash: Pricing, Load Operations and Payment', 'Reading the Freight Market', 'Equipment Niches: Van, Reefer, Flatbed, Heavy Haul and Drayage', 'Accessorials: Detention, Layover and TONU', 'Double Brokering and Freight Fraud Defense', 'Cargo Liability, Insurance and Claims'],
            [['AUTHORITY', "Apply through FMCSA's registration system, pay $300 per authority type, file a BOC-3 process agent covering every operating state, then check SAFER for the MC number about 24 hours later."], ['SECURITY', 'Post $75,000 via a BMC-84 surety bond or BMC-85 trust; credit-based premiums run $900 to $9,000, and a shortfall gets 7 business days to restore before suspension.'], ['PROSPECT', 'Pick a narrow niche like steel, lumber or machinery, scout shippers with satellite recon and help-wanted pages, and star 50 rows before dialing toward five great clients.'], ['VET CARRIER', 'Require a clean SAFER snapshot: authorized status, matching phone, more than zero trucks and a known authority grant date, while screening for double-brokering red flags.'], ['PRICE AND POST', 'Contract the shipper rate, buy the truck cheaper at roughly $100 to $600 per load, and post loads with driver candy: light, no tarp, quick pay and price shown.'], ['FUND THE FLOAT', 'Line up funding before volume, since 10 loads a week puts a new desk $40,000 out of pocket by week four, and know break-even loads before the owner earns anything.']],
        ),
    },
    26: {
        'volume_number': 26,
        'volume_id': 'vol-026-government-surplus-auctions',
        'short_slug': 'government-surplus-auctions',
        'candidate_number': 17,
        'score': 79,
        'title': 'Government Surplus Auctions',
        'subtitle': 'Fee-stacked bid ceilings, in-person inspections, SF-97 title paperwork, hammer-to-landed cost math, pallet freight traps, and resale-certificate discipline from the operators who buy at the government block',
        'site_ui': _ui(
            ['GOVERNMENT', 'SURPLUS', 'AUCTIONS'],
            ['FLEET CARS, POLICE UNITS, HUMVEES, AND HEAVY IRON BID ON ACROSS GSA AUCTIONS, GOVDEALS, PUBLIC SURPLUS, AND MUNICIBID', "SOLD-PRICE MATH, LIQUIDATION PALLETS, CIRCUIT-BOARD SCRAP, AND SELLER'S PERMITS FOR FLIPPING THE LOTS"],
            "Government surplus inventory is real, public, and fragmented across GSA Auctions, GovDeals, Public Surplus, and Municibid, and practitioners show how buyer's premiums of 5% to 15%, short pickup windows, and as-is condition decide whether a $900 Expedition or a $4,150 F-250 turns into profit.",
            "All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, each claim carrying timestamped inline attribution to the channel and video it came from. The chapters move from finding sales and bidding on fleet vehicles, heavy equipment, and military disposition lots to titles, liquidation pallets, electronics scrap, seller's permits, and compliance.",
            ['Finding the Sales: Government Auction Platforms and How Bidding Works', 'Buying Fleet Cars, Trucks, and Police Vehicles', 'Sold-Price Walkthroughs: Real Hammer Prices From GSA and State Auctions', 'Heavy Equipment and IronPlanet: Bidding on Iron', 'The GovPlanet Humvee Purchase', 'Titles, Street-Legal Registration, and True Build Cost', 'Military Disposition, Scrap Codes, and Diesel Generators', 'Local Surplus Sales and Flipping the Lots', 'Liquidation Pallets: Sourcing, Freight, and Unboxing Math', 'Electronics, Test Equipment, and Circuit-Board Scrap', "Getting Your Seller's Permit and Resale Certificate", 'Compliance, Contracts, and Claims'],
            [['FIND THE SALE', 'Search GSA Auctions, GovDeals radius listings, Public Surplus, and Municibid, and pull years of US Gov Bid past-auction prices before setting a max.'], ['READ THE TERMS', "Check payment method and deadline, the 5% to 12.5% buyer's premium, the pickup window, and whether you get a title or a bill of sale."], ['INSPECT ON PREVIEW', 'Scan with an OBD reader, check every tire and the door sticker, match the VIN, walk from poke-through rust or flood signs, or hire a mobile ASE inspector.'], ['SET A STOP PRICE', 'Build a KBB-based ceiling that includes premium, sales tax, and shipping, write it down, and let the lot go if bidding passes it.'], ['BID THE CLOSE', 'Use proxy bids and expect soft-close extensions that blunt sniping, watching Monday through Thursday afternoon and evening end times.'], ['PAY AND REMOVE', 'Pay inside the 5 to 15 business day window and pull the unit within a removal window as short as two days by temporary tag or tow, or risk losing it and being blocked.']],
        ),
    },
    27: {
        'volume_number': 27,
        'volume_id': 'vol-027-business-acquisition',
        'short_slug': 'business-acquisition',
        'candidate_number': 13,
        'score': 86,
        'title': 'Business Acquisition',
        'subtitle': 'Buy Cash Flow, Not Hope: Source Belly to Belly, Pay 2.5-4.5x Earnings, Clear SBA 7(a) at 1.25x DSCR, Prove Every Add-Back With a QoE, Lock the Working Capital Peg, and Stabilize Before You Accelerate',
        'site_ui': _ui(
            ['BUSINESS', 'ACQUISITION'],
            ['BUY A CASH-FLOWING SMALL BUSINESS AT 2.5-4.5X EARNINGS INSTEAD OF STARTING ONE', 'SOURCE, SCREEN, LOI, DILIGENCE, SBA 7(A) FINANCE, AND OPERATE THE FIRST 100 DAYS'],
            'Professors, brokers, attorneys, and searchers make the case that buying a cash-flowing small business at a half to a third of private equity multiples, financed with SBA 7(a) debt and a seller note, beats starting one from scratch.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies on entrepreneurship through acquisition, from deal sourcing and SBA lending through LOI drafting, quality of earnings, closing mechanics, and post-acquisition integration. Every claim, metric, pro-tip, and operator gate carries timestamped inline attribution to the source video.',
            ['Entrepreneurship Through Acquisition: The Case for Buying Instead of Starting', "Buy Then Build: The First-Time Acquirer's Playbook", 'Search Funds and Self-Funded Search: Running the Search', 'Deal Sourcing: Off-Market Origination and Online Marketplaces', 'SBA 7(a) Acquisition Lending and the SOP 50 10 8.1 Rules', 'Seller Financing, Earnouts, and Bridging the Down Payment', 'The Letter of Intent: Anatomy and Drafting', 'Quality of Earnings and Financial Due Diligence', 'Add-Backs, Cash Flow, and Calculating Net Working Capital', 'Closing Price Mechanics and LOI Negotiation', 'Asset vs. Stock Purchases, Tax Allocation, and Buyer Protections', 'Post-Acquisition: The First 100 Days, Integration, and Roll-Ups'],
            [['SOURCE', 'Work brokers, trade-show lists, and belly-to-belly direct outreach in one geography, targeting $1-5M revenue businesses and reviewing every listing to build reps.'], ['SCREEN', 'Price at about 2.5-4.5x earnings, kill razor-thin-margin labor- or capital-intensive targets, and flag any client above 10% of sales or a top-five list routed through one referrer.'], ['LOI', 'Open low near 2.5x and concede a quarter or half turn, refuse deposits and breakage fees on small deals, and strike working capital pegs from Main Street asset deals.'], ['DILIGENCE', 'Run legal, then financial, then operational review over about 60 days with a QoE, 36 months of reconciled bank statements, and time cards pulled by hand; kill any target with two sets of books.'], ['FINANCE', 'Fund with SBA 7(a) debt up to $5M for up to 90% of price with a personal guarantee, plus a seller note or earnout and $100-150K of working capital.'], ['OPERATE', 'Freeze personnel changes for six months, keep your salary low, name an owner for every P&L line, book the top 20 customers, and change processes incrementally in months 3-7.']],
        ),
    },
    28: {
        'volume_number': 28,
        'volume_id': 'vol-028-commercial-cleaning-contracts',
        'short_slug': 'commercial-cleaning-contracts',
        'candidate_number': 10,
        'score': 82,
        'title': 'Commercial Cleaning Contracts',
        'subtitle': 'From a sub-$1,000 launch and 100 calls a day to production-rate bids, loaded-wage margins, porter and medical accounts, public bids, QR-verified quality, BBP-ready teams, W2 control, and the franchise fee traps that turn owners into glorified employees',
        'site_ui': _ui(
            ['COMMERCIAL', 'CLEANING', 'CONTRACTS'],
            ['PRODUCTION-RATE BIDDING, 30% MARGIN FLOORS, AND PROPOSALS SENT WITHIN HOURS OF THE WALKTHROUGH', '100-CALL-A-DAY PROSPECTING, PAIN-DECISION-BUDGET QUALIFYING, AND RECURRING CONTRACTS WON ON DEPENDABILITY, NOT THE LOWEST BID'],
            'Operators who launched under $1,000 and grew to seven figures show how to bid by production rates instead of square footage, turn proposals around within hours of the walkthrough, and win recurring contracts even though roughly 90% of prospects already have a cleaner.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies covering lean launches, first-contract closes, prospecting, bidding formulas, government bids, specialty work, software, OSHA compliance, workforce classification, insurance, and franchise traps. Every claim, metric, pro-tip, and quote carries timestamped inline attribution to the practitioner and video it came from.',
            ['Starting Lean: Founder Playbooks from Zero to Seven Figures', 'Landing the First Contract: Walkthrough, Proposal, Close, Onboard', 'Prospecting Engine: Cold Calls, Cold Email, Doors, and Paid Search', 'Bidding Methods: Production Rates, Square Footage, and Hourly Formulas', 'Worked Bids and Pricing Calculators', 'Big Accounts and High-Profit Niches', 'Government and Public-Sector Janitorial Bids', 'Post-Construction Cleaning, Floor Care, and Specialty Add-Ons', 'Janitorial Software, QR Verification, and Selling with Systems', 'Bloodborne Pathogens: OSHA Compliance and Spill Cleanup', 'Workforce Classification, Insurance, and Bonding', 'Franchises, Remote Models, and Ownership Traps'],
            [['PROSPECT', 'Build a qualified list from Google Maps and call 100 businesses a day; 2,000 calls a month projects 10-20 appointments and 1-2 closes.'], ['QUALIFY', 'Screen every lead on pain, decision, and budget, and offer a complimentary quote to keep on file when the prospect already has a cleaner.'], ['WALKTHROUGH', 'Arrive 20 minutes early, scan for ledge dust, cobwebs, and floor smudges, and laser-measure only cleanable square footage.'], ['PRICE', 'Convert footage to labor hours with production rates such as 3,500-4,000 sq ft per hour for offices and hold a 30% margin floor.'], ['PROPOSE', 'Send a forwardable proposal within two to three hours that shows facility understanding, systems, scope, and security procedures.'], ['CLOSE AND ONBOARD', 'Set work-order and billing rules up front, price for the employees the account will need, and expand only when current accounts run smoothly.']],
        ),
    },
    29: {
        'volume_number': 29,
        'volume_id': 'vol-029-insurance-restoration',
        'short_slug': 'insurance-restoration',
        'candidate_number': 15,
        'score': 87,
        'title': 'Insurance Restoration',
        'subtitle': 'Remove It Physically, Prove It on the Meter, Price It Line by Line, Collect It Clean: S500/S520 Field Mechanics, Mitigation Billing, Xactimate Repricing, Roof Supplements, Adjuster and TPA Negotiation, Plumber Referrals, LSA Launches, AOB Risk, Legal Deductibles and Storm Crew Margins from the Operators Who Run Them',
        'site_ui': _ui(
            ['INSURANCE', 'RESTORATION'],
            ['REMOVE MOLD PHYSICALLY, HOLD -5 PA, AND CLOSE DRYING FILES ON MONITORED READINGS', 'WRITE, DOCUMENT, AND DEFEND EVERY LINE ITEM FROM XACTIMATE TO THE NEGOTIATION TABLE'],
            'Working restorers show how they hold containment at -5 pascals, prove dryness with the same meter from start to finish, and price every truck roll at $400 to $500 or more, then carry that discipline through Xactimate line items, roof supplements, adjuster negotiations, TPA programs, and assignment-of-benefits fights.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, from IICRC S500 and S520 field mechanics to mitigation billing, Xactimate, roof supplementing, adjusters, TPAs, fire and contents documentation, plumber referrals, company launch, assignment of benefits, claim law, and storm roofing. Every claim, metric, pro-tip, and operator gate carries timestamped inline attribution to the practitioner and video it came from.',
            ['Working to the Standard: IICRC S500 Water Damage and S520 Mold Remediation', 'Water Mitigation Estimates and Getting Paid', 'Xactimate Fundamentals and Line-Item Mastery', 'Roof Claim Supplementing', 'Adjusters, Public Adjusters, and the Negotiation Table', 'TPAs, Carrier Programs, and Preferred Vendors', 'Fire, Smoke, Contents, and Job-Site Documentation', 'The Plumber Referral Engine and Closing the Call', 'Launching the Restoration Company: Contracts, Paid Leads, and Margin', 'Assignment of Benefits: Mechanics, Abuse, and Reform', 'Deductibles, Claim Checks, and Claim Law', 'Storm Roofing: Hail Inspections, Roof Estimates, and Crew Economics'],
            [['RESPOND', 'Make at least $400-$500 every time the truck rolls, set a $2,000 floor on small cash-pay jobs, and require a deposit and a thirds payment schedule before self-pay mitigation starts.'], ['CONTAIN', 'Seal 6 mil fire-retardant poly and confirm -5 pascals on a manometer before any demolition or air movers, never draw negative air from a crawlspace, and remove mold physically instead of fogging or bleaching it.'], ['DRY', 'Extract water from the top of the floor and from underneath before mats go down, place 12-16 air movers for a 750 sq ft loss, take readings every 5 ft, and close the file on monitored readings from the same meter, not on fan-days.'], ['DOCUMENT', 'Reconcile billed equipment against photos and equipment logs, write F9 notes explaining each charge, quantity, and duration, and get written owner authorization for any deviation from the standard.'], ['ESTIMATE', 'Run one locked naming, bundling, and pricing protocol on every claim using saved templates, and change your pricing, never your scope, by never writing work the crew did not do.'], ['GET PAID', 'Stop negotiating line by line: have the adjuster tally the attempted reductions, then offer a streamline discount capped at 10 percent in exchange for immediate payment.']],
        ),
    },
    30: {
        'volume_number': 30,
        'volume_id': 'vol-030-lending-and-flash-funding-arbitrage',
        'short_slug': 'lending-and-flash-funding-arbitrage',
        'candidate_number': 30,
        'score': 93,
        'title': 'Lending & Flash-Funding Arbitrage',
        'subtitle': 'Back-to-back double closes, 1% transactional funding, Gator EMD chunks, title and wire controls, first-lien private money, exit-first bridge debt, and 0% business credit stacks',
        'site_ui': _ui(
            ['LENDING &', 'FLASH-FUNDING', 'ARBITRAGE'],
            ['WHOLESALERS, TITLE OPERATORS AND TRANSACTIONAL LENDERS TEST ASSIGNMENTS AGAINST BACK-TO-BACK DOUBLE CLOSES FUNDED AT 1% TO 3% OF PURCHASE', 'THEY BUILD CLOSER, ESCROW, LOAN-DOCUMENT AND LENDING PLAYBOOKS FROM SAME-DAY FLASH CASH TO PRIVATE MONEY, BRIDGE LOANS AND 0% BUSINESS CREDIT STACKING'],
            "Practitioners show how to decide between assigning and double closing, price transactional funding at 1% to 3% of purchase or a flat $850 to $2,000, and wire nothing on the A leg until the end buyer's cash is sitting in escrow.",
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies on double closes, transactional funding, title and escrow, earnest money, and lending. Every claim, metric, pro-tip and operator gate carries timestamped inline attribution to the practitioner and video it came from.',
            ['The Double Close Playbook', 'Assign, Double Close, or Fund the Transaction', 'Transactional Funding Costs, Terms & Lender Selection', 'Title, Escrow & the Settlement Statement', 'Earnest Money Deposits: Holding, Protecting & Losing Them', 'Proof of Funds, Prorations & Wire Fraud', 'The Gator Method', 'Becoming the Transactional Lender', 'Private Money & Hard Money Lending', 'Loan Documents, Security & Usury', 'Bridge Loans & Lines of Credit', '0% Business Credit Stacking'],
            [['LOCK THE SELLER', 'Contract the A-to-B purchase, bake fees into the price at the table ($97,000 instead of $100,000), and screen bank-owned and short sale deals for 30, 60 or 90-day resale restrictions.'], ['LOCK THE END BUYER', 'Sign the B-to-C contract first and secure a $2,500 minimum non-refundable deposit, $5,000 to $10,000 preferred, backed by a release clause.'], ['PICK THE CLOSER', 'Write an investor-friendly title company or attorney into both contracts, confirm they actually do double escrows, and lock their wire instructions on the first call.'], ['CHOOSE THE EXIT', 'Assign by default; double close when the spread crosses roughly $10,000 to $20,000 or when REO, HUD or no-assignment paper blocks an assignment.'], ['LINE UP FUNDING', 'Send both contracts to a transactional funder priced at 1% to 3% of purchase, flat $850 to $2,000, or 1% plus $100, and budget for fees if closing slips.'], ['CLOSE BACK TO BACK', "Fund the A leg only after the end buyer's B-to-C funds land in escrow, then repay the funder from the second closing, often within an hour."]],
        ),
    },
    31: {
        'volume_number': 31,
        'volume_id': 'vol-031-uber-and-commercial-fleet-arbitrage',
        'short_slug': 'uber-and-commercial-fleet-arbitrage',
        'candidate_number': 31,
        'score': 89,
        'title': 'Uber & Commercial Fleet Arbitrage',
        'subtitle': 'Uber Fleet Partner SUVs at $600 a Week, Black-Car Private Clienteles at $100 an Hour, $350-$450 Weekly Gig Rentals, Co-Hosting Off the Gross, and the Plate, Insurance, Kill-Switch, and Booking-Software Gates That Guard the Margin',
        'site_ui': _ui(
            ['UBER &', 'FLEET', 'ARBITRAGE'],
            ['192 PRACTITIONERS TEST UBER BLACK SUVS, RIDESHARE RENTALS, AND TURO CO-HOSTING FOR REAL PER-CAR RETURNS', 'THEY BUILD LICENSED, INSURED, GPS-PROTECTED FLEETS WITH BOOKING SITES, DISPATCH TOOLS, AND WEEKLY RENTAL TERMS'],
            'Fleet owners show how to launch through the Uber Fleet Partner Program, pick the right revenue vehicle, license and insure it, rent it to gig drivers by the week or off-platform, and scale without the mistakes that kill rental businesses.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, from Uber Black fleet owners and private chauffeurs to rideshare rental hosts and Turo co-hosts. Every claim carries timestamped inline attribution, so each lease rate, payback horizon, and permit cost traces back to the operator who said it.',
            ['Launching an Uber Fleet: Partner Program Setup and Black-Fleet Owner Lessons', 'Choosing the Revenue Vehicle: Uber Black SUVs, Rideshare Hybrids, and Cargo Vans', 'Uber Black Unit Economics: Real Shift Earnings and Platform Comparisons', 'Licensing the Fleet: NYC TLC Plates and California TCP Permits', 'From Uber Black to Private Chauffeur: Building and Dispatching a Black Car Business', 'Rideshare Rentals: Leasing Cheap Cars to Gig Drivers by the Week', 'Off-Platform Rentals: Building a Private Car Rental Business Without Turo', "Co-Hosting Arbitrage: Scaling a Turo Fleet With Other People's Cars", 'Insuring the Fleet: Rideshare, Commercial, and Rental Coverage and Liability', 'Protecting the Asset: GPS Trackers, Kill Switches, and the Rental Toolkit', 'Fleet Software Stack: Booking Sites, Rental Management, and Dispatch Tools', 'Scaling and Survival: Fleet Economics, Teams, and the Mistakes That Kill Rental Businesses'],
            [['SET UP THE FLEET ACCOUNT', 'Sign up for Uber Fleet, enter tax information carefully, and start with one vehicle instead of buying five at once, keeping cash reserves for licensing, permits, insurance, and a surprise repair week.'], ['CHOOSE THE VEHICLE', "Let the job pick the car: confirm the market's model-year floor, favor seven-seat black SUVs for Uber Black or Toyota hybrids for low cost per mile, and stack the full monthly note, insurance, and fuel before signing."], ['QUOTE INSURANCE AND LICENSE', 'Get a commercial auto insurance quote on the exact VIN before buying, then secure permits such as NYC TLC plates, California TCP permits, or Houston permit stickers at $794 per SUV plus a $75 limo license.'], ['VET AND RENT TO DRIVERS', 'Require a limousine license and full payment up front, treat repeating account flags as red alerts, and charge $450 to $800 per week flat or a 50/50 earnings split.'], ['PROTECT THE ASSET', 'Monitor driving with tracking apps, issue one warning for speeding over 80 and remove the driver on the second, and equip cars with GPS trackers and kill switches.'], ['SCALE THE FLEET', 'Target full vehicle payoff within about 15 months, build private clientele beyond the apps, and expand through off-platform rentals, Turo co-hosting, and fleet software for booking and dispatch.']],
        ),
    },
    32: {
        'volume_number': 32,
        'volume_id': 'vol-032-payment-processing-and-atm-arbitrage',
        'short_slug': 'payment-processing-and-atm-arbitrage',
        'candidate_number': 32,
        'score': 94,
        'title': 'ISO Payment Processing & ATM Arbitrage',
        'subtitle': 'Board Merchants on Interchange Plus, Capture Level 3 Savings, Pass Fees Through Compliant Dual Pricing, Protect a Vested Residual Book, Defend High-Risk Accounts with Chargeback Alerts, and Build Location-First ATM Routes on Signed Agreements and Disciplined Vault Cash',
        'site_ui': _ui(
            ['PAYMENT &', 'ATM', 'ARBITRAGE'],
            ['INTERCHANGE-PLUS PRICING, STATEMENT MATH, AND DURBIN DEBIT COST TESTS', 'RESIDUAL SPLITS, ISO PARTNERSHIPS, AND ATM LOCATION ECONOMICS'],
            'Merchant-services and ATM operators show how card fees split among issuing banks, card brands, processors, and ISOs, and how agents turn the processor markup into monthly residual income.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, with every quote, metric, and tip carrying timestamped inline attribution to its source video. The chapters run from card processing flow, pricing models, and interchange optimization through dual pricing, surcharging, residual economics, ISO building, high-risk accounts, and ATM unit economics, locations, hardware, and vault cash.',
            ['How Card Processing Works: Players, Payment Flow, and Debit Regulation', 'Merchant Pricing Models and Statement Analysis', 'Interchange Optimization: Level 2/3 Data, Visa CEDP, and Debit Rate Rulings', 'Dual Pricing and Cash Discount: Mechanics and the Sales Pitch', 'Surcharging Compliance and the Legal Ways to Pass On Card Fees', 'Residual Income Economics and ISO Agreement Terms', 'Building, Keeping, and Selling a Merchant Portfolio', 'Becoming an ISO: Registration, Partner Programs, and Scaling', 'High-Risk Accounts and Chargeback Defense', 'ATM Unit Economics: Real Profit, Hidden Costs, and Startup Budget', 'ATM Locations, Contracts, and Surcharge Setting', 'ATM Hardware, Vault Cash, Security, and High-Risk Cash Businesses'],
            [['ANALYZE', 'Open with a free cost analysis: divide total interchange by volume to land near 1.7 percent, then subtract interchange from total fees to expose the real markup.'], ['QUALIFY', 'Pull the average ticket and card mix first; tickets under about 15 dollars need per-item fees that cover the 22-cent regulated debit cost.'], ['CODE', 'Verify the SIC or MCC code and the card-present versus card-not-present setup so the merchant is not miscoded into higher rates.'], ['PRICE', 'Price from Schedule A costs on interchange plus, charging the cost of the card plus a set margin such as 0.25 or 0.60 percent so Durbin cost drops pass through.'], ['SUPPORT', 'Resolve past-due gateway accounts before they go delinquent, since after 6 months of uncollected fees the balance is debited from the affiliate account.'], ['EARN', 'Collect the residual on the split: at 80/20, 280 dollars of gross profit on a 20,000-dollar-per-month cafe pays the agent 224 dollars every month.']],
        ),
    },
    33: {
        'volume_number': 33,
        'volume_id': 'vol-033-insurance-housing-and-rental-arbitrage',
        'short_slug': 'insurance-housing-and-rental-arbitrage',
        'candidate_number': 33,
        'score': 90,
        'title': 'Insurance Housing & Corporate Rental Arbitrage',
        'subtitle': 'Getting booked by ALE Solutions, CRS, and Sedgwick, pricing claim homes off Coverage D and hotel bills, pitching landlords as a corporate housing company, lining up demand before the lease, scaling with VAs, and locking sublease, exit, and landlord-policy protections in writing',
        'site_ui': _ui(
            ['INSURANCE', 'HOUSING', 'ARBITRAGE'],
            ['HOW OPERATORS GET LISTED WITH ALE SOLUTIONS, CRS, SEDGWICK, AND THD, AND GET THE FAMILY TO PICK THEIR HOME OVER THE HOTEL', 'HOW OPERATORS PRICE AGAINST COVERAGE D, CAP UTILITIES IN CONTRACTS, AND HOLD RESERVES BEFORE ARBITRAGING FOR CLAIMS'],
            'Operators show how displaced families stuck in hotels become multi-month house placements: an $8,100 house replaced a roughly $15,000-a-month hotel bill, and 15 insurance families brought in more than $100K in one month.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, from getting booked by insurance relocation companies through leases, lease exits, and insuring the rental operation. Every claim, metric, pro-tip, and operator gate carries timestamped inline attribution to the practitioner who said it.',
            ['Getting Booked by Insurance Relocation Companies', 'Insurance Housing Case Studies and Operator Playbooks', "The Payer's Side: ALE Coverage, Adjusters, and Relocation Benefits", 'Building a Corporate Housing Business', 'Pitching Landlords and Launching Rental Arbitrage', 'Scaling, Automating, and Stress-Testing Arbitrage', 'Midterm Rental Fundamentals', 'Pivoting From Airbnb: Models, Regulations, and Taxes', 'Housing Travel Nurses and Contract Workers', 'Leases, Subleases, and Required Insurance Clauses', 'Lease Exits: Early Termination, Non-Renewal, and Tenant Protections', 'Insuring the Rental Operation'],
            [['LIST', 'Submit the home to ALE Solutions, CRS, Sedgwick, and Temporary Housing Directory forms, then confirm each submission by phone within a week because the forms send no confirmation and can create duplicates.'], ['PROSPECT', 'Send weekly or biweekly email blasts to relocation specialists with a PS asking them to forward it and a PPS offering referrals in other cities, and add BNI networking and local fire department outreach.'], ['PRICE', 'Ask for the nightly price range instead of the budget, let the agency name a number first, and anchor against the hotel-plus-kennel cost, aiming for about 1.5 to 2x long-term rent.'], ['CONTRACT', 'Write electric and water caps into the agreement and notes, keep cleaning, pet, and deposit fees low enough for the family, and remember the contract is with the agency, not the person.'], ['CALENDAR', 'Run a duplicate 30-day-minimum Airbnb with an open calendar, open the short-stay window no more than 30 days out, and hold a unit 24 hours pending adjuster approval.'], ['RESERVE', 'Before arbitraging a home for claims, set aside at least six months of reserves, plan three exit strategies, and confirm you can cover net-30 payment terms.']],
        ),
    },
    34: {
        'volume_number': 34,
        'volume_id': 'vol-034-nemt-and-medical-courier-arbitrage',
        'short_slug': 'nemt-and-medical-courier-arbitrage',
        'candidate_number': 34,
        'score': 90,
        'title': 'NEMT & Medical Courier Dispatch Arbitrage',
        'subtitle': 'Land the contract before the van, price every route on miles, hours and deadhead, stack STAT and direct facility work over gig apps, enroll before you bill, diversify off broker dependence, and prove every trip',
        'site_ui': _ui(
            ['NEMT &', 'COURIER', 'ARBITRAGE'],
            ['DIRECT MEDICAL COURIER CONTRACTS, SPECIMEN AND COLD-CHAIN ROUTES, AND THE SPREAD BETWEEN $10 DRIVER STOPS AND $20 TO $50 CLIENT BILLING', 'NEMT STARTUP ROADMAPS, MEDICAID BROKER WORK, FACILITY REFERRAL PIPELINES, RATES AND BILLING, AND DISPATCH SOFTWARE WITH TRIP VERIFICATION'],
            "Practitioners show how to land the contract before buying the vehicle, carry HIPAA and bloodborne pathogen training, and win direct lab, pharmacy, medical supply and VA courier work instead of taking brokered runs booked at triple the driver's pay.",
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies covering medical courier launches, direct contracts, specialized specimen work, NEMT operations, broker relationships, billing and dispatch enforcement. Every claim, metric, pro-tip and quote carries timestamped inline attribution to the practitioner and video it came from.',
            ['Launching a Medical Courier Operation from Zero', 'Hunting and Landing Direct Medical Courier Contracts', 'Medical Courier Companies, Brokerages, and Apps Hiring 1099 Drivers', 'Specimens, Cold Chain, Organs, and STAT: Specialized Courier Work', 'Courier Pay Reality, Pricing, and Route Profitability', 'Entity, Insurance, Enrollment, and Legal Foundations', 'NEMT Startup Roadmap and the Mistakes That Bankrupt New Owners', 'NEMT Vehicles and Day-to-Day Trip Execution', 'Working With (and Around) Medicaid Brokers', 'Private Pay, Facility Contracts, and Direct Referral Pipelines', 'NEMT Rates, Billing, and Unit Economics', 'Dispatch Software, Trip Verification, and Fraud Enforcement'],
            [['CERTIFY', 'Complete HIPAA and bloodborne pathogen training and launch in the car you already own, with no van or Sprinter purchase until a signed contract covers the payment.'], ['INSURE', 'Ask each client whether it requires a $300,000 or $1 million liability limit before buying commercial auto and business liability coverage, since the contract dictates the insurance.'], ['PROSPECT', 'Send 25 or more applications a day with same-day follow-up calls, set keyword alerts on Indeed, CB Driver and Google, call department lines 9 to 11 a.m. Tuesday or Wednesday, and mine sam.gov for VA courier awards.'], ['PRICE', 'Charge a $35 minimum per pickup or a $750 to $1,000 weekly retainer and negotiate weekend, after-hour and wait-time terms with lab directors and pharmacy managers.'], ['CONTRACT', "Write the client's stated volume assumptions into the bid, add pay-the-remainder cancellation language, and check deadhead miles, waiting time, stop count, exclusivity and equipment before signing."], ['SCALE', 'Bank three months of operating expenses for 90-day first checks, then hire a driver only when $300 to $500 a week remains after driver pay and the contract allows subcontractors.']],
        ),
    },
    35: {
        'volume_number': 35,
        'volume_id': 'vol-035-subject-to-and-wraparound-note-arbitrage',
        'short_slug': 'subject-to-and-wraparound-note-arbitrage',
        'candidate_number': 35,
        'score': 90,
        'title': 'Subject-To & Wraparound Note Arbitrage',
        'subtitle': 'Buy on a Mirror Wrap, Sell on an Equity Wrap: Subject-To Takeovers, Hybrid Seller Notes, Due-on-Sale Defense, Servicer-Run Back Offices, and Note Partials That Recycle Capital',
        'site_ui': _ui(
            ['SUBJECT-TO', '& WRAP', 'ARBITRAGE'],
            ['BUY THE LOW-RATE LOAN, NOT THE HOUSE: SUBJECT-TO TAKEOVERS, MIRROR WRAPS, AND SELLER-AS-BANK PITCHES', 'SELL ON AN EQUITY WRAP FOR SPREAD, DOWN PAYMENT, AND CASH FLOW, THEN SERVICE, DISCLOSE, AND PLAN EVERY NOTE EXIT'],
            'Practitioners take over existing low-rate loans subject-to, then sell on a wraparound note that earns the spread on the full balance while a third-party servicer pays the underlying lender first.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies on subject-to acquisition, wraparound note arbitrage, seller financing, compliance, servicing, and note exits. Every claim, metric, and quote carries timestamped inline attribution to the practitioner and video it came from.',
            ['Wraparound Mortgage Mechanics: How the Wrap Rides on the Underlying Loan', 'Buying Subject-To: Pitching Sellers, Agents, and Lenders', 'Wrap Arbitrage: Selling on a Wrap for Spread, Down Payment, and Cash Flow', 'Seller Finance Fundamentals: Making the Seller the Bank', 'Structuring and Underwriting Creative Deals: Hybrids and the Morby Method', 'The Due-on-Sale Clause: Law, Exceptions, and Practitioner Workarounds', 'Sub-To and Wrap Failure Modes: When Deals Go Sideways', 'Closing, Title, and Taxing Creative Sales', 'Dodd-Frank and Seller Financing: Exemptions and Ability-to-Repay', 'Compliance and Loan Servicing: The Back Office of Every Note', 'Buying Mortgage Notes: Discounted and Non-Performing Loan Investing', 'Note Exits and Liquidity: Partials, Sales, Funding, and Marketplaces'],
            [['TARGET', 'Pull absentee owners with values above $300,000, at least 20% equity, and two-plus years of ownership, plus preforeclosures that can be bought before auction.'], ['PITCH', "Frame the retail sale as roughly 10% lost to commissions and closing costs, offer to take over payments and cover arrears, and reverse-engineer the seller's monthly number without mentioning interest."], ['ACQUIRE', "Buy subject-to or on a mirror wrap, assemble the lender access package (SSN, authorization to release, notarized limited POA), and keep the seller's insurance in force with the trust as additional insured."], ['CLOSE', 'Open escrow and get the title report before promising a move-out date, then record the deed of trust or mortgage with the wraparound rider as the security instrument, never the note itself.'], ['WRAP', 'Sell on an equity wrap that marks up both price and interest rate so the spread runs on the full balance, with disclosure of the existing mortgage and due-on-sale clause up front and at closing.'], ['SERVICE & EXIT', 'Route every payment through a servicer that pays the underlying lender first, name a refinance, reserves, and timeline plan if the loan is called, and ask to renew and extend balloons before paying off or selling the note.']],
        ),
    },
    36: {
        'volume_number': 36,
        'volume_id': 'vol-036-gpu-compute-and-telecom-capacity-arbitrage',
        'short_slug': 'gpu-compute-and-telecom-capacity-arbitrage',
        'candidate_number': 36,
        'score': 94,
        'title': 'GPU Compute & Telecom Capacity Arbitrage',
        'subtitle': 'Renting VRAM Instead of Hashing, Pricing the Job Instead of the Hour, Keeping Neocloud GPUs Busy, Packing Tokens per Weight Read, and Clearing 10DLC Vetting and STIR/SHAKEN Before the Carrier Margin Disappears',
        'site_ui': _ui(
            ['GPU &', 'TELECOM', 'ARBITRAGE'],
            ['RENTING VRAM, NOT HASHING: 4090, 5090, 3090 AND CMP 170HX RIGS TESTED ON VAST, RUNPOD, SIMPLEPOD AND SALAD', 'MEMORY BANDWIDTH OVER TERAFLOPS: 8-GPU HGX BASEBOARDS, INFERENCE ENGINES, SIP TRUNKS AND A2P 10DLC SMS'],
            'Operators who moved from crypto mining to AI rentals report that the money now sits in renting VRAM, with Salad 4090s netting about $2.92 a day, a 10x CMP 170HX server pulling $36.37 in a day, and memory capacity and bandwidth, not headline teraflops, pricing data-center silicon.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, with every claim carrying timestamped inline attribution to its speaker and source video. Coverage runs from hand-built rental rigs, data-center GPUs and marketplace hosting through colocation, FinOps, neocloud brokerage, Kubernetes GPU sharing, inference engines and token routing to SIP trunking, A2P 10DLC and carrier compliance.',
            ['From Mining Rig to AI Rental Rig: Building and Hosting Your Own GPUs for Profit', 'Inside the Silicon: Data-Center GPUs, AI Servers, and Challenger Chips', 'Renting GPUs on Marketplaces: RunPod vs Vast.ai in the Field', 'Colocation, Warehouses, and Data-Center Plumbing for GPU Operators', 'FinOps and Repatriation: Controlling Cloud and AI Compute Spend', 'Neocloud Economics and Multi-Cloud GPU Brokerage', 'Multi-Tenant GPU Sharing on Kubernetes', 'Inference Engines: Getting Maximum Tokens per GPU', 'Routing Tokens vs Self-Hosting: Gateways, Cheap Hardware, and Confidential Inference', 'SIP Trunking, CPaaS Carriers, and Voice-AI Telephony', 'A2P 10DLC: Registering, Vetting, and Delivering Business SMS', 'Carrier Compliance and Telecom Business Models'],
            [['SOURCE', 'Test any used GPU in person before paying, price-check it on gpudeals.net, and play OEMs against each other, as with Dell at $1M versus Supermicro at $750K.'], ['STRESS-TEST', 'Run the C-Payne stress tool for 48 hours to a week, watch for throttling such as a 4090 dropping from 450 W to 230 W, and reseat or swap risers one at a time if System interrupts climb.'], ['HARDEN', 'Size PSUs, PDUs and rack circuits for a steady 80% load, put IPMI on its own out-of-band VLAN, keep InfiniBand off the management switch, and hold GPUs under 83 C.'], ['LIST', 'Rent capacity on marketplaces that take about 25% on Vast, 20% on SimplePod, or 10% plus 40 cents on Salad, never power-limiting below 90% on Salad.'], ['SERVE', 'Benchmark tokens per GPU across more than one inference server, since Ollama showed an H200 at near-parity with an H100 at 36.6 tok/s, and price silicon on memory capacity and bandwidth.'], ['CONNECT', 'Wire voice-AI telephony over SIP trunks and CPaaS carriers, then register and vet A2P 10DLC campaigns to deliver business SMS within carrier compliance.']],
        ),
    },
    37: {
        'volume_number': 37,
        'volume_id': 'vol-037-saas-discount-and-gpo-arbitrage',
        'short_slug': 'saas-discount-and-gpo-arbitrage',
        'candidate_number': 37,
        'score': 94,
        'title': 'SaaS Discount Brokerage & GPO Arbitrage',
        'subtitle': 'From Partner Center to Pooled Buying - Indirect CSP Incentive Stacking, Distributor Margin Wraps, VIPMP Migrations, Brokered UCaaS, GPO Admin Fees, Contingency Telecom Audits, SaaS Rightsizing and Renewal Defense',
        'site_ui': _ui(
            ['SAAS & GPO', 'DISCOUNT', 'ARBITRAGE'],
            ['RESALE MARGINS, STACKED PARTNER INCENTIVES AND POOLED BUYING POWER ACROSS MICROSOFT, ADOBE, GOOGLE WORKSPACE AND UCAAS CHANNELS', 'LICENSE AUDITS, CONTINGENCY COST REDUCTION, RENEWAL DEFENSE AND SEAT, USAGE AND AI-CREDIT PRICING ARCHITECTURE'],
            'With resold license margin running just 8-15%, practitioners earn on the service layer, stacked partner incentives and pooled buying power rather than on the software itself.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, with every claim carrying timestamped inline attribution to its source video. Coverage runs from Microsoft Partner Center enrollment and CSP resale through distributor marketplaces, group purchasing, SaaS license audits, buy-side renewal defense and pricing architecture.',
            ['Entering the Microsoft Channel: Partner Center, MPN Enrollment, and CSP Resale Models', 'Harvesting Microsoft Incentives: MCI Rebates, CPOR Credit, and the Managed Intelligence Pivot', 'Distributor Marketplaces and the MSP Margin Engine: Pax8, Ingram Micro, and the VAR Model', 'Reselling Adobe Through VIP Marketplace: Provisioning, Transfers, and Team Licensing', 'Adobe Discounts and Google Workspace Reselling: Pricing Shifts, Promotions, and Partner Arbitrage', 'UCaaS and CCaaS Resale: Zoom, RingCentral, and the Partner Channel Opportunity', 'Group Purchasing Organizations: How Pooled Buying Power Creates Discounts', 'Contingency Cost Reduction and Telecom Expense Management Audits', 'SaaS License Audits, Shadow IT, and Rightsizing', 'Buy-Side SaaS Negotiation and Renewal Defense', 'Selling SaaS: Cold Calling, Closing Against Procurement, Quotas, and CRM Automation', 'SaaS Pricing Architecture: Seats, Usage, AI Credits, and Renewal Uplifts'],
            [['ENROLL', 'Register a Partner Center account under a domain email and primary Entra tenant, clear business verification, and join the free AI Cloud Partner Program.'], ['LINK PROVIDER', 'Link the MPN ID to an indirect provider such as Ingram Micro, Pax8, TD Synnex or Sherweb, since direct bill now demands $1M trailing revenue.'], ['TRANSACT NCE', 'Lock seat counts and term choice inside the 7-day NCE window, knowing monthly terms carry a 20% premium over annual.'], ['BUNDLE SERVICES', 'Treat the 8-15% license margin as a floor and earn on the service layer by selling a complete solution, not just a license.'], ['HARVEST INCENTIVES', 'Enroll in Microsoft Commerce Incentives separately, clear the $25K trailing-12-month revenue floor plus a designation or 25 capability points, and file CPOR claims for a 60% rebate / 40% co-op payout.'], ['MANAGE INTELLIGENCE', 'Layer fixed-fee assessments, scoped builds and workflow-priced management on Copilot and Agent 365, giving every agent a named owner, least-privilege access and a credit limit.']],
        ),
    },
    38: {
        'volume_number': 38,
        'volume_id': 'vol-038-contingent-bill-audit-and-tax-credit-recovery',
        'short_slug': 'contingent-bill-audit-and-tax-credit-recovery',
        'candidate_number': 38,
        'score': 94,
        'title': 'Contingent Corporate Bill-Audit & Tax-Credit Recovery',
        'subtitle': 'No Savings, No Fee: GSR Late-Package Refunds, Surcharge Rerating, Carrier Contract Engineering, Utility and Expense Audits, Property Tax Appeals, Cost Segregation and 179D, WOTC Capture, Shared-Savings Deals, and Reverse Audits',
        'site_ui': _ui(
            ['BILL-AUDIT &', 'TAX-CREDIT', 'RECOVERY'],
            ['PARCEL AUDITORS RERATE EVERY INVOICE LINE, FILE LATE-PACKAGE REFUND CLAIMS INSIDE 15 DAYS, AND ESCALATE DENIALS BY PHONE', 'CONTINGENCY RECOVERY ACROSS CARRIER, UTILITY, TELECOM, PROPERTY TAX, COST SEGREGATION, 179D, AND WOTC CLAIMS'],
            'Practitioners show how a package delivered even 60 seconds late earns a refund the carriers will never flag, how surcharges rather than base rates now drive parcel spend, and how auditors recover that money on contingency.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, from guaranteed-service refund recovery and surcharge rerating to property tax appeals, cost segregation, and the Work Opportunity Tax Credit. Every claim, metric, and quote carries timestamped inline attribution to the practitioner and video it came from.',
            ['Small-Parcel Auditing and Guaranteed-Service Refund Recovery', 'Decoding Carrier Surcharges, Dimensional Weight, and Invoice Rerating', 'Negotiating UPS and FedEx Shipper Agreements', 'Utility Bill Audits and Error Recovery', "Telecom, Waste, and Workers' Comp Expense Audits", 'Property Tax Assessment Appeals', 'Cost Segregation Fundamentals and Payoff Analysis', 'Catch-Up Depreciation and the Section 179D Deduction', 'Capturing the Work Opportunity Tax Credit', 'Claim Mechanics: Forms, Deadlines, and Documentation', 'Contingency Fees, Shared Savings, and Contingency Planning', 'Reverse Audits, Reconciliations, and Rate Renegotiation'],
            [['CONNECT', "Take the client's online billing credentials and auto-download every carrier invoice to monitor shipping activity continuously"], ['AUDIT', 'Rerate package by package with no sampling or average weights, checking 40 to 44 points per shipment against billable weight, DIM factors, and surcharge thresholds'], ['FILE', 'Hold invoice payment and file guaranteed-service refund disputes inside the 15-day window, since a payment on file triggers automatic denials'], ['ESCALATE', 'Work denied claims through repeated resubmission and live phone agents, or choose an address correction dispute instead'], ['VERIFY', 'Screen out automatic systematic SVC fail credits and require analyst sign-off on every figure before a dispute reaches the carrier'], ['BILL', 'Charge only a contingent share of recovered savings, from 30 percent up to a 50 percent starting split, with no fee if nothing is saved']],
        ),
    },
    39: {
        'volume_number': 39,
        'volume_id': 'vol-039-inbound-pay-per-call-and-ping-post-arbitrage',
        'short_slug': 'inbound-pay-per-call-and-ping-post-arbitrage',
        'candidate_number': 39,
        'score': 95,
        'title': 'Inbound Pay-Per-Call & RTB Ping-Post Arbitrage',
        'subtitle': 'Own the Tracking Layer, Gate Every Caller with IVR, Bid in Milliseconds, Prove One-to-One Consent, and Broker the Spread from Network Offers to Direct Buyers Who Pay Up Front',
        'site_ui': _ui(
            ['PAY-PER-CALL', '& PING-POST', 'ARBITRAGE'],
            ['HOW 192 PRACTITIONERS BUY TRAFFIC, ROUTE LIVE CALLS THROUGH RTB RING TREES, AND RESELL THEM AT A SPREAD', 'TRACKING NUMBERS, IVR PRE-QUALIFICATION, TCPA CONSENT, BUYER NETWORKS, AND THE UNIT ECONOMICS OF SCALING'],
            'Learn how working operators price, route, and resell live inbound calls, from a $50 call that nets a $15 margin and a 40% broker markup to ring trees with minimum-revenue floors and an 8-second billing buffer.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies on inbound pay-per-call and RTB ping-post arbitrage, from platform setup and IVR design to TCPA compliance, verticals, network building, and unit economics. Every claim, metric, pro-tip, and quote carries timestamped inline attribution to its source video.',
            ['Pay-Per-Call Fundamentals: The Model, the Vocabulary, and Choosing Your Lane', 'Platform Setup and Real-Time Bidding for Calls', 'IVR Design and Call Flows That Pre-Qualify Callers', 'Routing Optimization and Call Attribution', 'Ping-Post Lead and Call Distribution', 'TCPA One-to-One Consent and Lead-Gen Compliance', 'Generating Inbound Calls with Google and Meta Ads', 'Home-Services Call Verticals', 'The Insurance Buyer Side: Inbound Calls and Live Transfers', 'Mass Tort Mechanics and TCPA Litigation Exposure', 'Building the Network: Buyers, Publishers, and Negotiation', 'Unit Economics, Call Quality, and Scaling Case Studies'],
            [['CHOOSE THE LANE', 'Weigh pay-per-call against pay-per-lead and affiliate networks against direct clients, then read every line of the offer: minimum call length, buyer hours, hold period, and who owns the buyer.'], ['MODEL THE SPREAD', 'Price the gap between traffic cost and call payout with at least a 40% markup, and model the worst-case paid ratio before you spend.'], ['OWN THE TRACKING', "Assign unique tracking numbers per publisher and put your own number in front of the network's so you can verify every call and catch skimming."], ['BUILD THE RING TREE', 'Set eligibility filters on geo, hours, caps, and concurrency, add a minimum-revenue floor with static fallback targets, and prefer SIP when the buyer accepts it.'], ['PAD AND TEST', "Add an 8-second latency buffer over the buyer's billable duration and run real test calls that confirm tracking, routing, answer, timing, and recording end to end."], ['LAUNCH AND PROTECT', 'Send paid traffic only after testing, keep publisher IDs and your margin hidden from buyers, and capture consent records to limit TCPA exposure.']],
        ),
    },
    40: {
        'volume_number': 40,
        'volume_id': 'vol-040-self-funded-erisa-pbm-and-workers-comp-arbitrage',
        'short_slug': 'self-funded-erisa-pbm-and-workers-comp-arbitrage',
        'candidate_number': 40,
        'score': 93,
        'title': "Self-Funded Health, PBM & Workers' Comp Arbitrage",
        'subtitle': "Surplus Splits, Laser Counters, Captive Pools, PBM Spread Audits, Medicare-Plus Pricing, Broker Pay Disclosure, Gag-Clause Attestations, and Workers' Comp Mod and Lien Recovery",
        'site_ui': _ui(
            ['SELF-FUNDED', 'PBM & E-MOD', 'ARBITRAGE'],
            ['BROKERS, TPAS AND STOP-LOSS CARRIERS TEST LEVEL-FUNDED QUOTES, SURPLUS SPLITS, LASERS AND RENEWAL LOSS RATIOS AGAINST FULLY INSURED PREMIUMS', "THEY BUILD PBM CONTRACT FORENSICS, CAA COMPLIANCE FILINGS, RBP AND DPC PLAN REDESIGNS, AND WORKERS' COMP E-MOD, AUDIT AND RECOVERY PLAYBOOKS"],
            "Twelve chapters of practitioner testimony map how employers escape double-digit fully insured renewals through level-funded and self-funded plans, interrogate stop-loss contracts, captives and PBM spread pricing, test reference-based pricing, direct contracting and broker commissions, and control CAA compliance, ERISA fiduciary exposure and workers' comp experience mods.",
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, with every claim carrying timestamped inline attribution to its source video. Benefits brokers, TPAs, stop-loss carriers and healthcare finance educators supply the street numbers, operator gates and pro-tips, and the chapters flag where they disagree on size cutoffs, surplus splits and underwriting thresholds.',
            ['Fully Insured vs. Self-Funded vs. Level-Funded: The Funding Architecture', 'The Level-Funding Playbook: Quoting, Renewals, and Plan Redesign', 'Stop-Loss Insurance: Specific, Aggregate, and the Contract Traps', 'Medical Stop-Loss Captives: Pooling Risk Outside the Traditional Market', 'Pharmacy Benefit Managers: Following the Money', 'PBM Contract Forensics: Spread, Rebates, MAC Pricing, and Audits', 'Reference-Based Pricing and Direct Contracting', 'Brokers, Commissions, and the Broker of Record Letter', 'CAA Compliance: Gag Clauses, Disclosures, and Plan Filings', 'ERISA Fiduciary Litigation and TPA Claims Administration', "Workers' Comp Experience Mods and Class Codes", "Workers' Comp Cost Control, Audits, Liens, and Recovery"],
            [['DIAGNOSE', 'Run the loss-ratio math on the current renewal: a 120-employee group at a 60% loss ratio left roughly $560,000 of about $1.4 million in premium with the carrier'], ['COLLECT', 'Gather the census with SIC and zip, every IHQ at 5 to 10 minutes per employee, and the quarterly wage and tax report, with the owner setting a hard Friday deadline'], ['UNDERWRITE', 'Price admin, specific and aggregate stop-loss and the claims fund, using Milliman Curve pharmacy underwriting and specific stop-loss of $10,000 to $20,000 with 125% aggregate'], ['GATE', 'Get surplus-split and renewal language in writing, model a year-two laser to $200,000, and walk away from above-average claims, high ER use or a sale within one to two years'], ['BIND & ENROLL', 'Confirm the 12-month contract and 12/18 or 12/24 runout, start enrollment 30 days before the effective date, and brief providers on the new ID card logo'], ['RENEW & REDESIGN', 'Reopen admin and stop-loss fees every year, test regional networks or RBP at $9 versus $25 access fees and DPC diverting about $40 PMPM, and convert broker commission to a visible fee']],
        ),
    },
    41: {
        'volume_number': 41,
        'volume_id': 'vol-041-buying-group-card-float-and-rebate-arbitrage',
        'short_slug': 'buying-group-card-float-and-rebate-arbitrage',
        'candidate_number': 41,
        'score': 93,
        'title': 'Buying Group, Commercial Card-Float & Rebate Arbitrage',
        'subtitle': 'Buying-group spreads of 2-5 percent turned into points, $500-$1,000 orders that survive cancellation, liquidation fees of 5-6 percent netted against rewards, 0% intro stacks spaced six months apart, Plum 60-day float vs. the 1.5 percent early-pay discount, Spark and Ink flat-rate engines, Amex financial-review survival, and portal stacks that only pay when every statement is cleared in full',
        'site_ui': _ui(
            ['BUYING GROUP', '& CARD-FLOAT', 'ARBITRAGE'],
            ['BUY HOUSEHOLD-CAPPED RETAIL UNITS ON REWARDS CARDS, SHIP TO GROUP WAREHOUSES, AND HARVEST POINTS, MINIMUM SPEND AND STATUS ON NEAR-BREAK-EVEN 2-5% SPREADS', 'LOCK A BUYER, EXIT OR REPAYMENT PLAN BEFORE THE SWIPE, STACK 0% INTRO CARDS, AND NEVER FLOAT MORE THAN THE CASH IN YOUR BANK ACCOUNT'],
            'Practitioners run buying groups, gift card resale and the interest-free card float as a points engine: they buy capped items on their own cards for thin 2-5% spreads, line up a buyer at an agreed rate before every swipe, and never float more than their bank balance.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, and every claim carries timestamped inline attribution to its creator and video. Coverage runs from buying-group mechanics, gift card liquidation and float economics through approvals, account shutdowns, issuer card stacks, portal stacking and premium fee math.',
            ['Buying Groups: Mechanics, Platforms & Order Survival', 'Gift Card Resale, Manufactured Spend & Credit-to-Cash Liquidation', 'The Float: Bank Economics, Interest-Free Leverage & Business Credit Structure', 'Approvals, Limit Increases & Credit Cycling', 'Amex Financial Reviews & Account Shutdowns', 'Capital One Spark & Venture X Business', 'Net-60 Float & High-Spend Charge Cards', 'The Chase Ink Stack', 'Amex Business Gold: Bonus & 4x Engine', 'Rakuten & Portal Stacking', 'Capital One Shopping, Transfer Bonuses & Point Currencies', 'Wallet Strategy & Premium Fee Math'],
            [['SEASON', 'Season bank relationships for 30 to 60 days, space 0% intro cards six months apart, and target long 0% windows before scaling spend'], ['RESERVE', 'Commit to the deal before researching it, since reservations hold only 12 to 24 hours, then match the exact SKU and log every order in a spreadsheet'], ['CHECKOUT', 'Keep orders between $500 and $1,000, split carts, pay through PayPal, Apple Pay or Shop Pay, and rotate backup addresses and names'], ['SHIP', "Ship only to addresses the group posts, ignore Discord DMs from 'admins', and never resubmit failed orders or return unsold items"], ['LIQUIDATE', 'Confirm a buyer at an agreed rate before buying promo gift cards, send $100 through any new route first, and weigh 5-6% liquidator fees against 2-3% invoice routes'], ['REPAY', 'Collect the ACH reimbursement, clear charge cards every 30 days so interest never accrues, and report sales at or above the 1099-K total under the matching EIN']],
        ),
    },
    42: {
        'volume_number': 42,
        'volume_id': 'vol-042-cell-tower-billboard-and-ios-lease-arbitrage',
        'short_slug': 'cell-tower-billboard-and-ios-lease-arbitrage',
        'candidate_number': 42,
        'score': 91,
        'title': 'Cell-Tower, Digital-Billboard & IOS Lease Arbitrage',
        'subtitle': 'Sell the rent stream at 16 to 19 times or strike the ROFR and make buyers bid, buy the billboard permit instead of the steel and underwrite at 85% fill, and lease gravel yards, truck stalls and substation-adjacent acres on day-one yield',
        'site_ui': _ui(
            ['TOWER, SIGN', '& IOS LEASE', 'ARBITRAGE'],
            ['CELL LEASE BUYOUT MULTIPLES, ROFR PENALTIES AND CARRIER RISK, TESTED SITE BY SITE', 'BILLBOARD COMPANIES, IOS AND TRUCK PARKING YARDS, AND GROUND RENT BUILT FROM THE DIRT'],
            'Practitioners show how a cell site rent stream that typically sells for 16 to 17.5 times annual rent can swing by hundreds of thousands of dollars on right of first refusal, escalator, easement and carrier fine print.',
            'All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies on cell tower leases, billboards and industrial outdoor storage. Every claim, metric and quote carries timestamped inline attribution to the practitioner channel and video it came from.',
            ["Cell Tower Lease Buyouts: What They Are and What They're Worth", 'Perpetual Easements, ROFR and Cell Lease Fine Print', 'Negotiating the Cell Tower Lease', 'Renting the Dirt: Ground Rent from Cell Sites, Billboards and Yards', 'The Economics of Owning a Cell Tower', 'The Billboard Moat: Regulation, Permits and Who Owns What', 'Starting and Building a Billboard Company', 'Billboard Unit Economics: The Full Accounting', 'Selling the Face: Billboard Ad Sales and New Formats', 'Industrial Outdoor Storage: The Asset Class and the Market', 'Building and Running IOS and Truck Parking Yards', 'Under the Lease: Cell Site Technology and Battery Storage Sites'],
            [['IDENTIFY TENANTS', 'Name every carrier on the site from meter labels, equipment cabinets and building permits, flag Dish exposure, and walk away from single-tenant sites.'], ['READ THE FINE PRINT', 'Check the lease for right of first refusal, confidentiality, consent-to-assign, defined premises and owner relocation rights before soliciting any offer.'], ['VERIFY TITLE', 'Pull title and confirm rent is still flowing, because even a paid attorney-title review can miss a previously sold easement.'], ['MODEL THE RISK', 'Price the stream as a multiple of annual rent, compare buyer discount rates of 8 to 12% against owner-side 4 to 6%, and stress-test rent stopping in year five to eight.'], ['SHOP COMPETITIVELY', 'Demand written letters of intent and sample easement documents from every buyer, since a handful of money sources sit behind roughly 20 buyout brands and clawbacks surface only on paper.'], ['NEGOTIATE AND CLOSE', 'Push for revenue share, escalators of at least 3% and ROFR removal, keep renewals short, and split the lump sum across December and January to spread the tax.']],
        ),
    },
    43: {
        'volume_number': 43,
        'volume_id': 'vol-043-live-event-super-bowl-and-vip-ticket-brokering',
        'short_slug': 'live-event-super-bowl-and-vip-ticket-brokering',
        'candidate_number': 43,
        'score': 95,
        'title': 'Live-Event, Super Bowl & VIP Ticket Brokering',
        'subtitle': 'Allotment Sourcing, 48-to-72-Hour Resale Timing, PSL Fee Math, Paddock Club and Suite Hospitality, Ticketmaster and AXS Transfer Custody, BOTS Act Limits and the 25% Margin Flipping Playbook',
        'site_ui': _ui(
            ['SUPER BOWL &', 'VIP TICKET', 'BROKERING'],
            ['READING SUPER BOWL RESALE FLOORS, 48-TO-72-HOUR DIPS, ONE-WEEK COLLAPSES AND GAME-DAY DUMPS', 'SOURCING PLAYER, COACH AND TEAM ALLOTMENTS, THEN VERIFYING, LISTING AND FLIPPING SEATS ON DIGITAL RAILS'],
            'Broker-level testimony on how Super Bowl and marquee-event seats are allocated, sourced, priced, verified and flipped, from $950 face value to $40,000-plus seats near the 50-yard line.',
            "All 12 chapters synthesize 192 verbatim YouTube practitioner testimonies, and every quote carries timestamped inline attribution to its channel and video. Together they map the market from StubHub's 25% average commission and the NFL's 17.5-percent-per-team allocation through VIP hospitality, seat licenses, transfers, resale law and the reseller's flipping playbook.",
            ['Reading the Super Bowl Resale Market', 'Sourcing Super Bowl Seats: Allotments, Face Value and Fraud Avoidance', 'Super Bowl VIP Packages, Suites and Stadium Premium Hospitality', 'F1 Paddock Club and Ultra-Premium Event Hospitality', 'Marquee Events Beyond the NFL: Masters, Tennis, UFC, Coachella and College Finals', 'Personal Seat Licenses: The Right to Buy', 'World Cup and Soccer Demand: Hospitality, Resale and Scams', 'Ticketmaster Delivery, Transfers and Refunds', 'AXS Workflows and Back-Office Ticketing Tools', 'The Law of Reselling: BOTS Act, FTC Actions and Broker Failures', 'Concert Pricing Mechanics: Dynamic Pricing, Platinum Seats and Fees', "The Reseller's Playbook: Sourcing, Selection and Flipping"],
            [['READ THE MARKET', 'Watch prices early, let the conference-championship spike burn off, and read buyer geography, since one traveling fan base kept StubHub sales 30 to 40% ahead of the prior year.'], ['SOURCE INVENTORY', "Fill the board from players, coaches, agents and team front-door deals, which supplied about 80 percent of one broker's listings, with roster players 35 through 53 the most likely to resell."], ['VERIFY', 'Stay on digital rails through verified marketplaces such as NFL Ticket Exchange, reject physical tickets for a mobile-only game, and kill any listing $1,000 to $2,000 under the going market.'], ['LIST AND SELL', 'List the same seats on multiple sites at once, sell direct to fans to dodge secondary-site fees, and bundle a perk such as a tailgate bash to move inventory in a soft year.'], ['TIME THE BUY', 'Set price alerts under the current floor and target the 48-to-72-hour window before kickoff, staying out of the final rush when desperation pushes prices back up.'], ['EXIT', 'Gauge leftover game-day supply before betting on a collapse, and never carry unsold inventory into a soft-matchup week without an exit plan, as game-day sellers cut hardest.']],
        ),
    },
    44: {
        'volume_number': 44,
        'volume_id': 'vol-044-customs-duty-drawback-and-tariff-refund-recovery',
        'short_slug': 'customs-duty-drawback-and-tariff-refund-recovery',
        'candidate_number': 44,
        'score': 95,
        'title': 'Customs Duty Drawback, Tariff Refund & Antitrust Claim Recovery',
        'subtitle': 'The Money-to-Manpower Playbook for 5-Year CBP 19 U.S.C. § 1313 Duty Drawbacks, § 1514 Tariff Protests, HTS Reclassifications & B2B Antitrust Class-Action Splits',
        'site_ui': _ui(
            ['DUTY DRAWBACK', '& TARIFF', 'RECOVERY'],
            ['TRACE THE DUTY. PROVE THE CLAIM.', 'THREE LANES. DISTINCT RECOVERY RULES.'],
            'Find recoverable dollars in import records, tariff classifications, and antitrust settlements before the filing windows close.',
            'Eligible drawback can return up to 99% of qualifying duties, taxes, and fees, but document completeness, exclusions, and processing time determine whether a recovery engagement earns its margin. Build distinct revenue lanes around drawback administration, legally supportable tariff refunds, and antitrust settlement claims support, pricing each against verified eligibility, collection timing, and the applicable representation rules.',
            ['Q1: The Three-Lane Recovery Thesis', 'Q2: Importers, Exporters & Claimants', 'Q3: Recovery Fees & Cash Cycles', 'Q4: Eligibility, Authority & Deadlines', 'Q5: Source the Recovery Pipeline', 'Q6: Audit Entries & Export Evidence', 'Q7: Build the Claim Package', 'Q8: Price Each Recovery Lane', 'Q9: Broker, Counsel & Client Channels', 'Q10: Run the Recovery Ledger', 'Q11: Defend Against Denials & Clawbacks', 'Q12: Scale Repeatable Claim Cohorts'],
            [['SOURCE', 'Identify authorized importers, exporters, and settlement claimants with material, documentable recovery potential.'], ['SCREEN', 'Separate drawback, tariff-refund, and antitrust matters; verify standing, exclusions, and filing deadlines.'], ['RECONCILE', 'Match entries, duty payments, exports, purchases, and settlement evidence without double-counting recovery.'], ['ASSEMBLE', 'Prepare auditable claim files with qualified customs professionals or counsel where required.'], ['FILE', 'Submit through the proper authorized channel and track inquiries, corrections, and determinations.'], ['COLLECT', 'Reconcile actual proceeds, invoice contracted fees, and retain evidence for audits and overlapping-claim checks.']],
        ),
    },
    45: {
        'volume_number': 45,
        'volume_id': 'vol-045-no-surprises-act-idr-and-medical-arbitration',
        'short_slug': 'no-surprises-act-idr-and-medical-arbitration',
        'candidate_number': 45,
        'score': 94,
        'title': 'No Surprises Act (IDR) Medical Arbitration & Out-of-Network Recovery',
        'subtitle': 'The Money-to-Manpower Playbook for Federal 42 U.S.C. § 300gg-111 IDR Batching, 30-Day Open-Negotiation Automation, QPA Uplift Dossiers & Specialty Group Splits',
        'site_ui': _ui(
            ['NO SURPRISES', 'ACT MEDICAL', 'ARBITRATION'],
            ['RECOVER ELIGIBLE UNDERPAYMENTS.', 'UNDERWRITE EVERY DISPUTE.'],
            'Turn eligible out-of-network underpayments into disciplined recovery cases, not a volume-driven arbitration gamble.',
            'Federal No Surprises Act IDR economics depend on eligibility, applicable state processes, timely open negotiation, evidence quality, and expected incremental collections after administrative, entity, and servicing costs. Keep IDR case administration distinct from contractual underpayment appeals and other lawful out-of-network recovery work, using permitted fixed or collection-based fees without shifting prohibited balances to patients.',
            ['Q1: The Provider Recovery Thesis', 'Q2: Specialties, Plans & Dispute Routes', 'Q3: Expected Recovery per Case', 'Q4: Federal IDR & State Boundaries', 'Q5: Source Authorized Provider Accounts', 'Q6: Screen Claims & Filing Clocks', 'Q7: Negotiate & Prepare the Record', 'Q8: Price IDR & Appeals Separately', 'Q9: Provider & RCM Partnerships', 'Q10: Operate the Dispute Calendar', 'Q11: Control Fees, PHI & Denials', 'Q12: Scale Profitable Claim Cohorts'],
            [['INGEST', 'Receive authorized claim, remittance, and plan data through HIPAA-compliant workflows.'], ['ROUTE', 'Determine federal IDR eligibility, applicable state processes, and alternative appeal rights.'], ['UNDERWRITE', 'Estimate incremental collections net of current fees, labor, loss exposure, and payment delay.'], ['NEGOTIATE', 'Complete required open negotiation and preserve the evidence and statutory deadlines.'], ['SUBMIT', 'Present a supported offer through the applicable dispute process using current evidentiary and batching rules.'], ['RECONCILE', 'Track determinations and payments, pursue appropriate enforcement, and measure realized contribution margin.']],
        ),
    },
    46: {
        'volume_number': 46,
        'volume_id': 'vol-046-mass-tort-intake-hitech-triage-and-law-firm-msos',
        'short_slug': 'mass-tort-intake-hitech-triage-and-law-firm-msos',
        'candidate_number': 46,
        'score': 93,
        'title': 'Mass-Tort Case Acquisition, HITECH Record Triage & Law-Firm MSOs',
        'subtitle': 'The Money-to-Manpower Playbook for Compliant Law-Firm MSOs, Arizona ABS Co-Ventures, $6.50 HITECH EMR Verification & MDL Plaintiff Funnel Operations',
        'site_ui': _ui(
            ['MASS-TORT', 'HITECH & LAW', 'FIRM MSOS'],
            ['QUALIFIED INTAKE. VERIFIED RECORDS.', 'NONLEGAL SERVICES. CLEAR BOUNDARIES.'],
            'Build the compliant intake, medical-record, and operating infrastructure that helps law firms evaluate cases faster.',
            'Measure acquisition cost per attorney-accepted, evidence-supported matter rather than per raw lead, including advertising, consent verification, record retrieval, triage, and rejection costs. Separate permissible marketing and intake services, HIPAA/HITECH-compliant record support, and nonlegal MSO administration, with jurisdiction-specific review of solicitation, referral compensation, fee splitting, ownership, and attorney independence.',
            ['Q1: The Legal-Services Infrastructure Thesis', 'Q2: Tort Criteria & Firm Demand', 'Q3: Cost per Qualified Matter', 'Q4: Ethics, Consent & MSO Boundaries', 'Q5: Build Compliant Acquisition Channels', 'Q6: Verify Intake & Record Authority', 'Q7: Retrieve & Triage Medical Records', 'Q8: Price Three Nonlegal Service Lanes', 'Q9: Win & Retain Firm Accounts', 'Q10: Operate Intake, QA & Handoffs', 'Q11: Control Fraud & Privacy Exposure', 'Q12: Scale Without Owning Legal Judgment'],
            [['ATTRACT', 'Use accurate, jurisdiction-reviewed advertising without outcome promises or prohibited solicitation.'], ['CONSENT', 'Document contact consent, privacy disclosures, and valid authority for medical-record requests.'], ['SCREEN', 'Apply attorney-defined intake criteria while leaving legal advice and case acceptance to counsel.'], ['RETRIEVE', 'Obtain records through applicable access or authorization pathways without assuming universal fee caps.'], ['TRIAGE', 'Organize source-linked medical timelines and flag gaps for qualified clinical or attorney review.'], ['SERVICE', 'Deliver contracted nonlegal support while preserving professional independence and lawful compensation structures.']],
        ),
    },
    47: {
        'volume_number': 47,
        'volume_id': 'vol-047-ai-data-center-powered-land-and-bess-optioning',
        'short_slug': 'ai-data-center-powered-land-and-bess-optioning',
        'candidate_number': 47,
        'score': 92,
        'title': 'AI Data-Center Powered Land, Substation Headroom & BESS Site Optioning',
        'subtitle': 'The Money-to-Manpower Playbook for FERC/ISO Queue GIS Overlays, 69kV–345kV Substation Capacity Screening, Dark-Fiber Corridors & Assignable Land Options',
        'site_ui': _ui(
            ['AI POWERED', 'LAND & BESS', 'OPTIONING'],
            ['CONTROL THE SITE. VERIFY THE POWER.', 'OPTIONS BEFORE LAND OWNERSHIP.'],
            'Secure conditional control of promising data-center and battery-storage sites before committing capital to unverified power stories.',
            'Site-option economics depend on option premiums, extension payments, diligence burn, assignment rights, and the probability of securing a buyer before expiry; nearby transmission or a substation does not establish available capacity. Distinct revenue lanes include negotiated option assignments, development-stage site sales, and permitted siting or development services, with data-center load service and BESS interconnection underwritten separately.',
            ['Q1: The Power-Constrained Land Thesis', 'Q2: Data-Center & Storage Buyer Maps', 'Q3: Option Carry & Exit Economics', 'Q4: Land Rights, Zoning & Brokerage', 'Q5: Map Parcels & Power Signals', 'Q6: Verify Utility & Site Constraints', 'Q7: Negotiate Conditional Site Control', 'Q8: Package Assignments & Development Fees', 'Q9: Reach Qualified Project Buyers', 'Q10: Manage Diligence & Milestones', 'Q11: Stress-Test Power, Permits & Expiry', 'Q12: Scale a Stage-Gated Site Portfolio'],
            [['MAP', 'Screen parcels for utility territory, network proximity, zoning, access, fiber, and environmental constraints.'], ['VERIFY', 'Seek utility-backed load-service or interconnection information; treat mapped headroom as an unconfirmed signal.'], ['CONTROL', 'Negotiate counsel-reviewed options with diligence access, milestones, and explicit assignment provisions.'], ['DILIGENCE', 'Evaluate title, engineering, permitting, utility costs, and project-specific operating constraints.'], ['MATCH', 'Present a source-documented package to qualified buyers without describing speculative capacity as secured.'], ['EXIT', 'Close an authorized assignment or development transaction, or terminate before additional carry destroys the margin.']],
        ),
    },
    48: {
        'volume_number': 48,
        'volume_id': 'vol-048-qui-tam-sec-and-irs-whistleblower-analytics',
        'short_slug': 'qui-tam-sec-and-irs-whistleblower-analytics',
        'candidate_number': 48,
        'score': 92,
        'title': 'Data-Mined Qui Tam, SEC & IRS Whistleblower Analytics',
        'subtitle': 'The Money-to-Manpower Playbook for Public-Dataset Medicare/Procurement Fraud Forensics, 31 U.S.C. § 3730 Independent-Analysis Relator Filings & SEC/CFTC/IRS Awards',
        'site_ui': _ui(
            ['QUI TAM &', 'WHISTLEBLOWER', 'ANALYTICS'],
            ['FIND ANOMALIES. BUILD EVIDENCE.', 'SEPARATE SIGNAL FROM ALLEGATION.'],
            'Turn lawfully obtained data into counsel-ready investigative leads without mistaking anomalies for proven misconduct.',
            'False Claims Act, SEC, and IRS matters have different standing, original-information, procedure, and award requirements, with uncertain outcomes and potentially multiyear collection timelines. Keep eligible whistleblower awards separate from lawful research retainers and counsel-directed analytics services, underwriting service work on its own margin rather than treating contingent awards as recurring revenue.',
            ['Q1: The Evidence-First Analytics Thesis', 'Q2: FCA, SEC & IRS Pathways', 'Q3: Research Burn & Award Uncertainty', 'Q4: Lawful Access, Seals & Privilege', 'Q5: Source Public & Authorized Data', 'Q6: Test Anomalies & Alternative Explanations', 'Q7: Build a Traceable Evidence Record', 'Q8: Separate Awards from Service Revenue', 'Q9: Engage Qualified Whistleblower Counsel', 'Q10: Operate Secure Case Workflows', 'Q11: Control Disclosure & Retaliation Risk', 'Q12: Scale Research Without Speculative Claims'],
            [['SOURCE', 'Use public records and lawfully accessible information without unauthorized access or data exfiltration.'], ['ANALYZE', 'Identify reproducible patterns and test innocent explanations, data errors, and materiality.'], ['CORROBORATE', 'Preserve provenance and distinguish direct evidence, analytical inference, and unresolved questions.'], ['REVIEW', 'Have qualified counsel assess eligibility, public-disclosure issues, privilege, deadlines, and reporting duties.'], ['REPORT', "Follow the chosen program's submission requirements and any applicable court-seal restrictions."], ['TRACK', 'Support authorized follow-up and record outcomes without booking speculative awards as earned revenue.']],
        ),
    },
    49: {
        'volume_number': 49,
        'volume_id': 'vol-049-prediction-market-terminals-and-igaming-affiliates',
        'short_slug': 'prediction-market-terminals-and-igaming-affiliates',
        'candidate_number': 49,
        'score': 91,
        'title': 'Regulated Prediction-Market Terminals & Licensed iGaming Affiliates',
        'subtitle': 'The Money-to-Manpower Playbook for Non-Custodial CFTC Event-Contract Analytics & Builder Routing, Cross-Venue Odds Engines & State-Licensed Sportsbook/Casino CPA Portals',
        'site_ui': _ui(
            ['PREDICTION', 'TERMINALS &', 'IGAMING CPA'],
            ['SELL DECISION TOOLS. QUALIFY REFERRALS.', 'REGULATED VENUES. LICENSED PARTNERS.'],
            'Build subscription-grade prediction-market tools and compliant gaming referral funnels without blurring their regulatory boundaries.',
            'Prediction-market terminal economics depend on subscription retention after market-data licensing, infrastructure, support, and acquisition costs, while brokerage, execution, or advisory functions may introduce separate obligations. Licensed iGaming affiliate economics depend on approved jurisdictions, qualified-player CPA or permitted revenue share, fraud reversals, and operator terms, so gross signups and customer deposits are not earned affiliate revenue.',
            ['Q1: The Two-Lane Distribution Thesis', 'Q2: Permitted Venues & Licensed Operators', 'Q3: Subscription Margin & Qualified CPA', 'Q4: Licensing, Data Rights & Disclosures', 'Q5: Source Data & Build Audience', 'Q6: Validate Access & User Eligibility', 'Q7: Launch Terminals & Referral Funnels', 'Q8: Price Seats & Negotiate Affiliate Terms', 'Q9: Acquire Users Without Misleading Claims', 'Q10: Reconcile Usage & Qualified Conversions', 'Q11: Control Fraud & Gambling Harm', 'Q12: Scale by Approved Jurisdiction'],
            [['SCOPE', 'Define separate terminal and affiliate offerings, approved markets, and activities requiring legal review.'], ['CONTRACT', 'Secure necessary data rights, venue permissions, operator agreements, and affiliate approvals.'], ['BUILD', 'Deliver reliable analytics and clearly disclosed referrals without guaranteed-return claims.'], ['GATE', 'Apply required access and marketing controls; never bypass operator age, identity, location, or self-exclusion checks.'], ['CONVERT', 'Measure paid subscriptions and operator-validated qualifying customers rather than clicks or unverified registrations.'], ['RECONCILE', 'Net revenue against data costs, acquisition spend, cancellations, reversals, and compliance overhead.']],
        ),
    },
}

ACTIVE_PUBLISHED_NUMBERS: tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49)
CANDIDATE_TO_VOLUME_NUMBER: dict[int, int] = {
    int(spec["candidate_number"]): num for num, spec in ALL_VOLUME_SPECS.items()
}


def get_volume_spec_by_candidate(candidate_number: object) -> dict | None:
    """Return the canonical volume spec for a 1..49 candidate_number, or None."""
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
    """Return the canonical spec dict for any of the 49 registered volumes."""
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
