from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small mineral rights desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "County Instrument Chains, RRC and OCC Surveillance, NMA/NPRI Interest Math, and Evidence-Backed Institutional Exits",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #7, Mineral Rights, holds Rank #23 with a 63/100 Money-to-Manpower Score. "
        "This chapter maps the tooling stack to five operator plays: severed-title acquisitions, "
        "NPRI cash-flow purchases, pooling-docket curve-jumping, owned-asset royalty recovery, and "
        "institutional flips. County instruments establish the ownership evidence; state production "
        "systems and hearing dockets expose changes; licensed datasets accelerate screening without "
        "replacing source documents. A 1 FT + 3 C pod needs reproducible joins, exception queues, "
        "and acquisition-specific evidence packets rather than another oversized dashboard. Canonical "
        "annual owner profits remain $6,000 Conservative, $69,875 Base, and $180,000 Scaled. Revenue "
        "means royalty receipts plus realized rights-trading gains, excluding returned basis. The "
        "directory distinguishes access costs, source latency, extraction restraint, and practical "
        "fallbacks so automation improves decisions without manufacturing title certainty."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$30,000",
            "context": "Annual royalty receipts and realized rights-trading gains; returned basis excluded",
            "note": "20% net margin; $6,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$215,000",
            "context": "Annual royalty receipts and realized rights-trading gains; returned basis excluded",
            "note": "32.5% net margin; $69,875 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$400,000",
            "context": "Annual royalty receipts and realized rights-trading gains; returned basis excluded",
            "note": "45% net margin; $180,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build a source hierarchy that distinguishes ownership from operating signals",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with five explicit queues, not a universal parcel scraper. Severed-title acquisitions "
                    "need county conveyances and tract interpretation; NPRI cash-flow purchases need the creating "
                    "instrument, lease terms, and payment evidence; pooling-docket curve-jumping needs applications, "
                    "hearing changes, and signed orders; owned-asset royalty recovery needs statements and production "
                    "comparisons; institutional flips need transferable evidence and clean provenance. These are the "
                    "chapter's five operating mappings, not five extra revenue streams. Assign the full-time principal "
                    "to pricing, seller decisions, and capital allocation. Use three contractors for land/title research, "
                    "petroleum and production analysis, and data/reconciliation work, with counsel engaged within the "
                    "land/title scope when interpretation requires it. Contractor counts describe functional coverage, "
                    "not three full-time salaries. Restrict the initial footprint to one basin and a manageable county "
                    "set. A recorded instrument can establish a link in ownership but may omit earlier reservations; "
                    "a tax roll can identify a mailing lead but cannot establish the mineral estate. An operator's "
                    "division order can support payment reconciliation without curing title. Encode these distinctions "
                    "in source types so a mailing address, production observation, and ownership conclusion never "
                    "share the same confidence label. Every queued opportunity needs a named reviewer and a next "
                    "evidence request."
                ),
                (
                    "Acquire evidence from the most authoritative source available for the question being answered. "
                    "For Texas, county clerk records supply deeds and assignments, while Railroad Commission systems "
                    "supply well, lease, completion, and reported production records. Texas production often arrives "
                    "at lease level, so a lease total cannot automatically become one horizontal well's revenue "
                    "forecast. Oklahoma Corporation Commission imaging and electronic case records support separate "
                    "operating and pooling investigations; an application is neither a final order nor proof that "
                    "the target interest participates. New Mexico OCD well files and hearing materials require the "
                    "same distinction between requested relief and executed development. BLM MLRS adds federal "
                    "land-status and case context, while ONRR public datasets provide aggregate revenue context "
                    "rather than an individual's royalty ledger. Commercial products shorten the search path, but "
                    "licensing, coverage, export rights, and historical depth determine usefulness. Ask each vendor "
                    "for a trial using twenty already-researched tracts and a written description of correction "
                    "handling. Measure missed wells, duplicated laterals, stale operator names, and title documents "
                    "that cannot be reproduced. Prefer a narrower feed with traceable timestamps over broad coverage "
                    "whose fields conceal their origin. Keep the trial findings alongside the purchase decision."
                ),
                (
                    "Treat the directory's latency descriptions as source characteristics and desk polling choices, "
                    "not promised publication schedules. Before enabling a connector, record its actual access "
                    "terms, permitted automation, advertised limits, export format, and responsible contact. Public "
                    "search access does not imply unrestricted bulk retrieval, and a free portal does not make "
                    "certified copies free. When a documented API exists, use the licensed endpoint and the "
                    "provider's current authentication instructions; otherwise use an authorized export or a human "
                    "download rather than reverse-engineering private application calls. Set one worker per host "
                    "until documented limits justify more, honor Retry-After, apply bounded exponential backoff, "
                    "and cache immutable instrument images by content digest. Poll active dockets each business "
                    "day where permitted, but refresh monthly production after each observed reporting release "
                    "and revisit revisions. Capture both the reporting period and retrieval time. A portal outage "
                    "should create a visible stale-source flag, not silently extend yesterday's values into today's "
                    "underwriting. Maintain a county clerk request path and a regulator records contact before "
                    "depending on any feed. This modest discipline gives a four-person pod durable coverage without "
                    "turning retrieval failures into speculative acquisition signals or spending contractor hours "
                    "repairing avoidable duplicate downloads."
                ),
            ],
            "table": {
                "caption": "Eighteen Named Sources: Access, Cost, Latency, Retrieval Hygiene, and Fallback Paths",
                "headers": [
                    "Named source and decision supported",
                    "Exact access method and useful evidence",
                    "Cost tier and observed latency discipline",
                    "Rate hygiene and authoritative fallback route",
                ],
                "rows": [
                    [
                        "Texas county clerk Official Public Records for severed mineral chains",
                        "Use the county government's clerk link; search grantor, grantee, instrument number, and legal description.",
                        "Search charges vary by county platform; images and certified copies may carry separate fees; indexing follows recording.",
                        "Use permitted exports or individual requests; avoid bulk assumptions; obtain missing instruments directly from the clerk.",
                    ],
                    [
                        "Oklahoma county clerk records for reservations, assignments, and probate links",
                        "Start at the county clerk site; where participating, use OKCountyRecords.com indexed searches and document images.",
                        "Search, subscription, and image prices follow the county or provider schedule; recent recordings may await indexing.",
                        "Respect session and download terms; reconcile instrument numbers; request absent books or certified copies from the clerk.",
                    ],
                    [
                        "New Mexico county clerk recording systems for tract ownership evidence",
                        "Use the relevant county government's recording portal; search indexed parties and retrieve referenced instruments.",
                        "Public search and paid image access vary locally; track recording dates separately from portal availability.",
                        "Download only through authorized paths; use clerk copy requests and local abstract research when online coverage ends.",
                    ],
                    [
                        "Texas RRC Public GIS Viewer for spatial well screening",
                        "Open rrc.texas.gov and select Public GIS Viewer; inspect wells, identifiers, and available spatial layers.",
                        "Public viewing is free; map refresh differs by layer and does not establish production reporting currency.",
                        "Use published GIS downloads where available; avoid scripted map-tile harvesting; confirm details in underlying RRC well records.",
                    ],
                    [
                        "Texas RRC Production Data Query for reported lease volumes",
                        "Navigate RRC online research queries to Production Data Query; filter district, lease, operator, and reporting period.",
                        "Public queries are free; monthly reporting arrives after production and can receive later corrections.",
                        "Batch narrowly within published rules; retain revised observations; use RRC published production files when query access fails.",
                    ],
                    [
                        "Texas RRC Oil and Gas Imaged Records for completion evidence",
                        "Use the RRC Oil and Gas Imaged Records application; retrieve filings by available well and lease identifiers.",
                        "Online image viewing is generally free; filing, processing, and image publication occur on different dates.",
                        "Cache each retrieved filing; avoid repeated image requests; use RRC records requests for missing or illegible documents.",
                    ],
                    [
                        "Oklahoma Corporation Commission imaging for well and completion records",
                        "Navigate oklahoma.gov/occ to Oil and Gas well-record imaging; search API numbers and available indexed fields.",
                        "Public record searches are free; image availability follows filing and processing rather than a guaranteed daily release.",
                        "Use approved downloads with restrained concurrency; request absent records from OCC and cross-check operator-submitted documents.",
                    ],
                    [
                        "Oklahoma OCC Electronic Case Filing for pooling and spacing events",
                        "Follow the OCC Electronic Case Filing link; search cause numbers and inspect applications, notices, orders, and docket entries.",
                        "Public case access is free where offered; posting follows case activity; check active opportunities each business day.",
                        "Do not bypass session controls; preserve docket snapshots; use OCC court clerk records and hearing calendars as fallback.",
                    ],
                    [
                        "New Mexico OCD Permitting well search for production and files",
                        "Open wwwapps.emnrd.nm.gov/ocd/ocdpermitting; use the well search and linked production or well-file pages.",
                        "Public queries are free; monthly production and document publication carry different lags and revision patterns.",
                        "Use published export options and conservative polling; obtain missing well records through OCD district or records contacts.",
                    ],
                    [
                        "New Mexico OCD hearing materials for pooling application surveillance",
                        "Navigate emnrd.nm.gov/ocd to hearings and orders; connect hearing dockets, applications, exhibits, and signed orders.",
                        "Public materials are free; hearing schedules can change and orders may post after the hearing date.",
                        "Check active cases each business day where permitted; confirm postponements and missing exhibits with OCD hearing staff.",
                    ],
                    [
                        "BLM Mineral and Land Records System for federal case context",
                        "Open mlrs.blm.gov; use available public research and reports for land status, serial numbers, and case actions.",
                        "Public research is free; transaction entry and historical migration affect currency; retain each report's retrieval date.",
                        "Use supported reports rather than undocumented calls; verify gaps through the responsible BLM field office and land records.",
                    ],
                    [
                        "ONRR Natural Resources Revenue Data for federal royalty context",
                        "Open revenuedata.doi.gov; download published datasets and documentation for revenue, disbursements, and production context.",
                        "Public downloads are free; each dataset states its reporting period and update history; aggregates are not owner statements.",
                        "Cache versioned downloads and inspect metadata; use ONRR source documentation and operator statements for asset-level questions.",
                    ],
                    [
                        "EIA API version two for commodity and regional benchmarks",
                        "Register at eia.gov/opendata; use documented API v2 routes and series metadata for selected benchmark observations.",
                        "Public API keys are free; release timing varies by series and must accompany every imported benchmark.",
                        "Follow current key limits and pagination rules; cache releases; use EIA published spreadsheets when API retrieval fails.",
                    ],
                    [
                        "USGS National Map and topoView for geographic verification",
                        "Open apps.nationalmap.gov/downloader or ngmdb.usgs.gov/topoview; retrieve map products and geographic reference layers.",
                        "Public downloads are free; map editions and layer publication dates vary and cannot establish mineral ownership.",
                        "Download products once and retain edition metadata; use official survey plats and recorded descriptions for boundary questions.",
                    ],
                    [
                        "Enverus licensed products for cross-basin screening and historical comparisons",
                        "Request a product demonstration and contracted exports or documented API access covering the target basin and fields.",
                        "Commercial pricing is quote-based; historical depth, seats, API rights, and update cadence depend on the subscription.",
                        "Observe contracted quotas and redistribution terms; reconcile material observations against regulator filings and county source instruments.",
                    ],
                    [
                        "TGS Well Data Analytics for licensed production and well intelligence",
                        "Request current TGS coverage and delivery documentation; obtain authorized portal exports or separately contracted data delivery.",
                        "Commercial pricing is quote-based; verify basin coverage, refresh schedules, historical revisions, and export entitlements before purchasing.",
                        "Use only contracted interfaces and limits; backstop underwriting fields with state well files and operator payment evidence.",
                    ],
                    [
                        "LandGate mineral analytics for property screening and valuation comparisons",
                        "Use landgate.com product access or request a licensed dataset demonstration; verify the precise mineral product scope.",
                        "Commercial analytics and data delivery use current product pricing; modeled estimates refresh differently from recorded ownership evidence.",
                        "Confirm permitted exports and usage limits; replace modeled ownership assumptions with county records and documented interest calculations.",
                    ],
                    [
                        "QGIS and GDAL local diagnostics for tract and well joins",
                        "Download from qgis.org and gdal.org; load authorized geometries, inspect coordinate systems, and validate spatial overlays locally.",
                        "Open-source software has no license fee; contractor time and source-layer vintage determine practical cost and currency.",
                        "Local processing avoids remote query pressure; repair invalid geometry and verify disputed boundaries against surveys and recorded descriptions.",
                    ],
                ],
            },
        },
        {
            "heading": "2. Turn mixed records into a tract-centered, auditable enrichment waterfall",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use a tract-centered model with separate entities for instruments, parties, interests, wells, units, "
                    "leases, docket events, and payments. Store the source's identifier unchanged alongside a normalized "
                    "search key. API well identifiers must remain strings so leading zeroes survive; preserve "
                    "sidetrack and completion suffixes where supplied instead of collapsing every record to one "
                    "borehole. Texas district-and-lease identifiers belong in their own namespace. County instrument "
                    "numbers require county and recording jurisdiction, because the same number can recur elsewhere. "
                    "Represent an interest as a dated assertion linked to supporting instruments, not a permanent "
                    "percentage attached to a person's name. Separate mineral ownership, executive rights, lease "
                    "royalty, NPRI burden, depth limitations, and tract participation. For illustration, forty gross "
                    "acres multiplied by a one-quarter mineral ownership fraction equals ten NMA; it does not "
                    "determine the royalty decimal without lease and allocation terms. An NPRI can be fixed or "
                    "floating depending on the instrument and governing interpretation, so a single generic royalty "
                    "multiplier is unsafe. Keep geometry provenance and coordinate reference systems explicit. A "
                    "wellbore crossing a polygon supports a spatial investigation, not a conclusion about unit "
                    "allocation, effective pooling, or the seller's transferable interest. Require a reviewer to "
                    "resolve those relationships."
                ),
                (
                    "Build the enrichment waterfall around increasing evidence cost. First normalize a seller-supplied "
                    "legal description and search the county index for the creating and latest relevant instruments. "
                    "Second connect the tract to regulator wells, leases, and units using identifiers and documented "
                    "spatial relationships. Third retrieve docket materials for pending activity and distinguish "
                    "application, continuance, hearing, and signed-order states. Fourth enrich with licensed production "
                    "history and commercial interpretations only where those fields reduce a specific underwriting "
                    "uncertainty. Fifth request seller statements, division orders, leases, and tax documents to "
                    "reconcile actual ownership and cash receipts. Stop paid enrichment when a fatal reservation "
                    "or excluded depth makes the target unbuyable. Maintain name variants, trust names, estates, "
                    "and entity successors as candidate links until instruments support consolidation. An assessor "
                    "mailing address is a contact clue, not proof that the addressee owns minerals. Use official "
                    "entity records and seller confirmation before relying on a business-name match. Avoid broad "
                    "personal-data purchases when a narrow county search answers the question. Log each match's "
                    "basis, competing candidates, reviewer, and unresolved conflict. The principal should see the "
                    "next cheapest decisive evidence request, not a decorative confidence percentage generated "
                    "from loosely matched names."
                ),
                (
                    "Implement a small append-only evidence store before adding orchestration software. Python's "
                    "urllib.request, csv, json, sqlite3, hashlib, decimal, and logging modules cover authorized "
                    "HTTP retrieval, structured exports, local indexing, checksums, money arithmetic, and run records. "
                    "Keep original files outside the working tables, store their SHA-256 digests, and record source "
                    "URL, retrieval time, document date, reporting period, parser version, and access entitlement. "
                    "PDF image extraction may require a separately installed desktop OCR product; its output remains "
                    "a searchable derivative, never the controlling deed text. Save corrections as new observations "
                    "with links to the superseded record. Make ingestion idempotent using source identity plus "
                    "document digest or a documented observation key, not filename alone. Test fixtures should "
                    "include duplicate downloads, revised production, missing pages, leading-zero identifiers, and "
                    "one deliberately conflicting ownership chain. Export a narrow review workbook for the land "
                    "contractor rather than requiring everyone to operate the database. Back up the evidence store "
                    "and test restoration to a separate directory. The data contractor owns failed imports; the "
                    "land contractor owns title exceptions; the production contractor owns allocation and decline "
                    "questions. This division prevents software repairs from silently becoming substantive "
                    "ownership decisions during a rushed bid."
                ),
            ],
            "table": {
                "caption": "Enrichment Waterfall: Evidence Costs Rise Only After Decisive Checks",
                "headers": [
                    "Waterfall stage and accountable pod role",
                    "Required input and join discipline",
                    "Stored output and acceptance evidence",
                    "Stop condition and lower-cost fallback",
                ],
                "rows": [
                    [
                        "County-first triage owned by the land and title contractor",
                        "Seller legal description plus county-specific instrument searches; preserve exact party spelling and recording jurisdiction.",
                        "A referenced chain segment with page images, reservations, effective dates, and the next missing instrument identified.",
                        "Stop when excluded depths defeat the thesis; request the missing county instrument before buying broader data.",
                    ],
                    [
                        "Operating linkage owned by the petroleum and production contractor",
                        "Regulator identifiers plus verified tract geometry; distinguish well, completion, lease, unit, and production reporting levels.",
                        "A reviewed relationship map explaining why each well or lease can affect the proposed interest.",
                        "Pause valuation when allocation cannot be supported; obtain unit exhibits or operator documentation instead of guessing.",
                    ],
                    [
                        "Commercial enrichment owned by the data and reconciliation contractor",
                        "A defined missing field and licensed coverage sample; compare vendor records with already-researched source observations.",
                        "A source-tagged dataset with revision timestamps, permitted uses, match explanations, and unresolved discrepancies retained.",
                        "Reject feeds that cannot reproduce critical fields; use narrow regulator downloads and targeted manual research.",
                    ],
                    [
                        "Seller evidence reconciliation owned by the principal with contractor review",
                        "Statements, leases, division orders, and tax records matched to documented interests and production accounting periods.",
                        "A bid packet separating supported receipts, disputed deductions, unresolved title conditions, and the maximum acceptable purchase price.",
                        "Suspend the bid when material payment ownership conflicts persist; request specific missing documents from the seller.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four mineral-desk habits that beat a larger unstructured feed",
                "body": "Spend contractor hours on interpretation and exceptions; use retrieval automation to preserve the evidence that makes those judgments reproducible.",
                "items": [
                    "Search deed references backward before paying for owner enrichment; the operative reservation often sits several instruments before the seller's acquisition.",
                    "Keep Texas lease production separate from well-level forecasts; ask the production contractor to explain any allocation across multiple producing wells.",
                    "Track OCC cause numbers through continuances and signed orders; a rescheduled hearing changes the timing thesis without changing the tract itself.",
                    "Save the exact exhibit and page supporting each institutional-buyer claim; a concise evidence index can shorten repeated diligence requests.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register the source and permitted retrieval route",
                    "action": "Record access terms, cost, source owner, refresh behavior, and fallback contact before the first recurring import.",
                    "detail": "For a portal without documented automation rights, schedule a human export and retain its retrieval metadata.",
                },
                {
                    "step": 2,
                    "title": "Capture originals before parsing derivatives",
                    "action": "Save the source file, compute its digest, and attach document and reporting dates before extracting fields.",
                    "detail": "Keep OCR text, normalized identifiers, and interpreted interests linked to the original rather than replacing it.",
                },
                {
                    "step": 3,
                    "title": "Route conflicts to the responsible specialist",
                    "action": "Run identifier, geometry, ownership, volume, and payment checks; create a named exception for each material conflict.",
                    "detail": "The principal sees unresolved bid blockers separately from routine import repairs and harmless formatting differences.",
                },
                {
                    "step": 4,
                    "title": "Publish a dated decision packet",
                    "action": "Export the interest calculation, source index, current event state, cash model, and unresolved conditions for review.",
                    "detail": "Freeze the packet used for each bid so later source revisions do not rewrite the original decision record.",
                },
            ],
        },
        {
            "heading": "3. Diagnose false signals before converting observations into bids or recovery claims",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The highest-value diagnostic is a contradiction queue. Compare new production against the prior "
                    "reported vintage, not just against the previous month, because amended reports can create "
                    "false growth. Flag zero-to-positive transitions, sharp volume changes, operator changes, and "
                    "new completion filings for review, while distinguishing shut-ins, workovers, meter adjustments, "
                    "and first sales. Keep oil, gas, and water units separate; do not add barrels to Mcf or treat "
                    "a gas conversion convention as a contractual payment factor. A benchmark price from EIA is "
                    "context, not the operator's realized sale price after quality, location, and contract effects. "
                    "For pooling-docket curve-jumping, monitor the tract's relationship to requested spacing and "
                    "pooling relief, applicant identity, notice evidence, hearing disposition, order terms, and "
                    "subsequent development. Receiving a docket alert creates a research task, not proof of imminent "
                    "cash flow. If a filed exhibit and a commercial map disagree, retain both and resolve the "
                    "underlying survey or legal-description issue. Use the land contractor for ownership and order "
                    "interpretation, the production contractor for timing and allocation, and the principal for "
                    "the bid ceiling. That separation stops optimistic event narratives from flowing directly "
                    "into price assumptions without a reviewed evidentiary bridge."
                ),
                (
                    "Royalty reconciliation starts with the asset's documented payment decimal and statement structure. "
                    "In a simplified illustration with uniform unit treatment, ten NMA inside a 640-acre unit "
                    "under a one-fifth lease royalty produces a 0.003125 decimal before other burdens or contractual "
                    "adjustments. If the applicable sales volume is 10,000 barrels at $70 per barrel, multiplying "
                    "$700,000 by that decimal yields $2,187.50 before applicable deductions and taxes. This is "
                    "an interest-math illustration, not an addition to the canonical revenue cases. Actual allocation "
                    "can differ for horizontal wells, tract factors, effective dates, and NPRI language. Match "
                    "statement lines by property, product, production month, sale month, and adjustment references. "
                    "Separate gross value, deductions, withholding, suspense releases, and prior-period corrections "
                    "so a larger check does not masquerade as improved reservoir performance. Under Texas Natural "
                    "Resources Code Section 91.402, payment timing and withholding conditions require fact-specific "
                    "review; a delayed payment is not automatically wrongful. Prepare a recovery inquiry with "
                    "statement extracts, supporting instruments, a decimal calculation, and the precise disputed "
                    "period. Log the operator's response and any corrected payment. Count recovered receipts only "
                    "once, when recognized under the desk's consistent accounting policy, rather than treating "
                    "the demand amount as earned revenue."
                ),
                (
                    "Instrument and spatial diagnostics matter as much as payment arithmetic. Run duplicate-document "
                    "checks, page-count comparisons, and OCR spot checks on fractions, exceptions, depth clauses, "
                    "and exhibit references. A scanned one-eighth can be misread as one-third, and an omitted "
                    "exhibit can remove the only precise tract description. QGIS can reveal invalid polygons, "
                    "coordinate-system mismatches, or lateral paths that appear shifted after an incorrect "
                    "transformation; it cannot interpret a reservation or resolve conflicting surveys. Validate "
                    "intersections against recorded descriptions and appropriate survey evidence. For institutional "
                    "flips, create a buyer-facing source index that identifies what the buyer can independently "
                    "retrieve and what requires a separate license. Do not redistribute commercial datasets merely "
                    "because the desk purchased access. Keep seller tax documents, bank details, and personal "
                    "identifiers out of general review exports; use restricted storage and share only material "
                    "needed for the transaction. Apply the same restraint to contractor access. Before outreach "
                    "or data-room publication, have the principal confirm recipients and the intended disclosure "
                    "scope. A clean packet should expose unresolved questions plainly, not bury them behind "
                    "composite scores. The objective is a defensible interest and a reproducible cash explanation, "
                    "not a visually persuasive map with unsupported ownership labels."
                ),
            ],
            "table": {
                "caption": "Forensic Checks That Separate Useful Signals from Expensive False Positives",
                "headers": [
                    "Diagnostic trigger and relevant operator play",
                    "Comparison performed on preserved source evidence",
                    "Common failure mode requiring specialist review",
                    "Decision output and accountable next action",
                ],
                "rows": [
                    [
                        "Production jump affecting NPRI purchases and institutional exit pricing",
                        "Compare reporting vintages, lease aggregation, completion dates, product units, and the operator's actual statement periods.",
                        "A revised lease report or combined-well total can impersonate new production from the target well.",
                        "The production contractor supplies a reviewed allocation and revised timing assumption before the principal changes price.",
                    ],
                    [
                        "New pooling filing affecting the docket curve-jumping acquisition queue",
                        "Compare application tracts, notice materials, requested relief, docket changes, signed orders, and subsequent development evidence.",
                        "An application may be continued, amended, dismissed, or granted without immediate drilling or target-interest participation.",
                        "The land contractor updates event state and open questions; the principal retains a conditional bid ceiling.",
                    ],
                    [
                        "Payment mismatch affecting owned-asset royalty recovery and NPRI underwriting",
                        "Recompute the supported decimal and reconcile product months, taxes, deductions, suspense, and prior-period statement adjustments.",
                        "Timing differences and prior-period releases can look like missing revenue or sudden operating improvement.",
                        "The reconciliation contractor prepares a period-specific inquiry; the principal approves external communication and tracks actual receipts.",
                    ],
                    [
                        "Geometry or instrument conflict affecting title purchases and institutional flips",
                        "Compare original pages, referenced exhibits, survey descriptions, coordinate systems, depth restrictions, and competing chain interpretations.",
                        "OCR errors, omitted exhibits, and invalid spatial joins can assign the wrong acreage or ownership fraction.",
                        "The land contractor resolves the source conflict or records a transaction condition; unsupported interests stay outside valuation.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before a bid or buyer packet leaves the desk",
                "body": "Require named reviewers and dated evidence for each check; unresolved material exceptions remain visible in the decision packet.",
                "items": [
                    "Verify the seller's transferable interest against the instrument chain, including reservations, depth limits, executive rights, and any probate or entity authority issue.",
                    "Verify the well-to-tract and unit relationship; document whether production is reported by well, completion, lease, or another aggregation level.",
                    "Verify payment arithmetic against actual statements and supported decimals; distinguish suspense releases and realized gains from recurring royalty receipts.",
                    "Verify source freshness, redistribution rights, recipient authorization, and the packet's treatment of personal identifiers before sending it externally.",
                ],
            },
        },
        {
            "heading": "4. Fund the stack from canonical economics and operate a four-person exception desk",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The scorecard is the operating boundary, not a target to rewrite with optimistic automation "
                    "savings. Conservative revenue is $30,000 at a 20% net margin, producing $6,000 annual owner "
                    "profit and implying $24,000 of total annual expenses. Base revenue is $215,000 at 32.5%, "
                    "producing $69,875 and implying $145,125 of expenses. Scaled revenue is $400,000 at 45%, "
                    "producing $180,000 and implying $220,000 of expenses. Conservative and Base use 1 FT + "
                    "3 C; Scaled uses 2 FT + 4 C. Do not subtract a new software budget from these "
                    "profits and still claim the same canonical scenario. Instead allocate any proposed subscription "
                    "inside its existing expense envelope or show a separately labeled sensitivity. For example, "
                    "a $6,000 annual data package would consume one-quarter of the Conservative expense envelope "
                    "before title work, administration, or other costs. A free-source pilot is therefore a sensible "
                    "starting posture, not an assertion that diligence is free. The stated $1,000–$12,000 monthly "
                    "opex range is a planning band, not a promise that every scenario's total annual expenses "
                    "equal twelve times recurring overhead. Transaction-specific costs and accounting classifications "
                    "still need explicit treatment in the desk ledger."
                ),
                (
                    "Keep capital deployment, cash proceeds, and recognized revenue in separate views. The stated "
                    "$150,000–$2,000,000 startup capital range primarily describes the ability to buy and hold "
                    "rights while research and payment cycles unfold; it is not operator revenue. In an illustrative "
                    "flip, an interest purchased for $100,000 and sold for $130,000 produces $130,000 of sale "
                    "proceeds, including $100,000 of returned basis and a $30,000 realized gain before separately "
                    "modeled transaction costs. Only the gain belongs in the scorecard's rights-trading revenue "
                    "component, with expense treatment kept consistent. Record royalty receipts separately and "
                    "prevent a recovered payment from appearing in both ordinary receipts and a second recovery "
                    "line. For institutional flips, preserve a basis schedule by acquired interest and track partial "
                    "disposals so the remaining asset does not inherit an arbitrary zero basis. Never value the "
                    "desk by the underlying operator's gross hydrocarbon sales or the buyer's total portfolio "
                    "capital. The six-to-twenty-four-month first-deal window also means a promising research "
                    "pipeline can coexist with limited near-term receipts. Track cash runway, committed purchase "
                    "capital, research spend, and delayed payments alongside the profit model. Automation reduces "
                    "clerical friction but cannot eliminate commodity exposure, depletion, or title disputes."
                ),
                (
                    "Run a weekly evidence meeting with one page per live opportunity and a strict exception "
                    "agenda. The data contractor reports failed imports, stale sources, and revised records; the "
                    "land contractor reports ownership breaks and docket changes; the production contractor reports "
                    "volume, allocation, and decline concerns; the principal resolves spend and bid decisions. "
                    "Measure instrument retrieval time, reviewed matches per paid hour, material exceptions caught "
                    "before bidding, statement lines reconciled, and buyer questions answered from existing evidence. "
                    "Avoid optimizing raw lead count when title research is the bottleneck. Promote a paid feed "
                    "only after a basin-specific pilot demonstrates saved review hours or a documented reduction "
                    "in costly misses, with both effects evaluated inside the canonical expense envelope. Recheck "
                    "access terms and source coverage at renewal. If raising pooled capital, evaluate the proposed "
                    "structure against securities definitions and applicable offering requirements before soliciting "
                    "investors; fractional mineral interests and investment contracts require careful analysis under "
                    "15 U.S.C. Section 77b(a)(1). Texas recording priorities under Property Code Section 13.001 "
                    "and federal communitization under 30 U.S.C. Section 226(m) likewise belong in targeted "
                    "transaction review, not generic software labels. The winning small desk maintains a shorter "
                    "distance between source evidence, specialist judgment, and an economically disciplined decision."
                ),
            ],
            "table": {
                "caption": "Canonical Economics and Tooling Decisions Without Revenue Inflation",
                "headers": [
                    "Scenario or control with exact operating scope",
                    "Recognized revenue and owner-profit reconciliation",
                    "Staffing or capital interpretation used by the desk",
                    "Tooling decision constrained by the existing economics",
                ],
                "rows": [
                    [
                        "Conservative case for a narrowly focused mineral acquisition desk",
                        "$30,000 annual revenue minus $24,000 implied expenses equals $6,000 owner profit at a 20% margin.",
                        "One full-time principal plus three contractors; contractor engagement must fit the limited annual expense envelope.",
                        "Begin with official sources and targeted copy purchases; a $6,000 annual feed consumes 25% of implied expenses.",
                    ],
                    [
                        "Base case for repeatable acquisitions and owned-asset royalty monitoring",
                        "$215,000 annual revenue minus $145,125 implied expenses equals $69,875 owner profit at a 32.5% margin.",
                        "One full-time principal plus three contractors; allocate title, production, and data work to explicit review queues.",
                        "Fund licensed coverage only within existing expenses after a documented pilot establishes useful coverage and review-hour savings.",
                    ],
                    [
                        "Scaled case for a six-person mineral operating team",
                        "$400,000 annual revenue minus $220,000 implied expenses equals $180,000 owner profit at a 45% margin.",
                        "Two full-time staff plus four contractors; additional capacity expands reviewed coverage rather than eliminating specialist interpretation.",
                        "Add contracted exports and monitoring depth where exception throughput supports them; preserve source rights and reconciliation controls.",
                    ],
                    [
                        "Capital and proceeds control applying across all five plays",
                        "Royalty receipts and realized rights-trading gains enter revenue; returned purchase basis stays outside recognized operator revenue.",
                        "$150,000–$2,000,000 startup capital supports acquisitions and holding periods; first-deal planning remains six to twenty-four months.",
                        "Track data spend, committed capital, and cash runway separately; do not count underlying hydrocarbon sales as desk revenue.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "The edge is not finding a record first; it is proving what that record changes before committing capital.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Choose one basin and a defined county set; assign the five play queues across the principal, land/title contractor, production contractor, and data contractor.",
        "Register the eighteen directory sources with current access terms, permitted extraction methods, actual prices, observed latency, and a named fallback contact.",
        "Create tract, instrument, interest, well, lease, unit, docket, and payment entities; preserve original identifiers, source files, digests, and reporting vintages.",
        "Run twenty researched tracts through the enrichment waterfall; measure missed relationships, stale observations, duplicate records, and specialist review time before buying a feed.",
        "Reconcile one owned interest from creating instrument through supported payment decimal and statement lines; resolve production-level and prior-period adjustment differences.",
        "Publish a dated bid packet and a separate capital ledger; reconcile all scenario reporting to $6,000, $69,875, and $180,000 annual owner profit without counting returned basis.",
    ],
    "statutory_citations": [
        {
            "title": "Texas Property Code Section 13.001 — Validity of Unrecorded Instrument",
            "url": "https://statutes.capitol.texas.gov/Docs/PR/htm/PR.13.htm#13.001",
            "relevance": "Recording and notice affect enforceability against specified creditors and subsequent purchasers; preserve the recorded chain rather than treating tax rolls or vendor ownership fields as controlling.",
        },
        {
            "title": "Texas Natural Resources Code Section 91.402 — Time for Payment of Proceeds",
            "url": "https://statutes.capitol.texas.gov/Docs/NR/htm/NR.91.htm#91.402",
            "relevance": "Establishes payment timing and circumstances permitting withholding; evaluate transaction facts and statement periods before asserting a royalty-payment deficiency.",
        },
        {
            "title": "30 U.S.C. Section 226(m) — Federal Lease Communitization or Drilling Agreements",
            "url": "https://www.law.cornell.edu/uscode/text/30/226",
            "relevance": "Addresses approved communitization or drilling agreements involving federal leases; obtain the applicable agreement and allocation evidence rather than inferring participation from map overlap.",
        },
        {
            "title": "15 U.S.C. Section 77b(a)(1) — Definition of Security",
            "url": "https://www.law.cornell.edu/uscode/text/15/77b",
            "relevance": "Includes investment contracts and fractional undivided interests in oil, gas, or other mineral rights; assess pooled-capital and offering structures before investor solicitation.",
        },
        {
            "title": "15 U.S.C. Section 77e — Prohibitions Relating to Interstate Commerce and the Mails",
            "url": "https://www.law.cornell.edu/uscode/text/15/77e",
            "relevance": "Sets registration-related restrictions for securities offers and sales; determine applicable registration or exemption requirements when a mineral investment structure involves securities.",
        },
    ],
}
