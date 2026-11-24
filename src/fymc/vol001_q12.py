from __future__ import annotations

CHAPTER_12 = {
    "id": "Q12",
    "chapter_id": "Q12",
    "chapter_number": 12,
    "question_number": 12,
    "slug": "property-data-ownership-research-and-genealogy",
    "question_prompt": "What do these videos cover about using Regrid and DataTree to research parcels, owners, titles and property taxes; working with mapping tools and real estate APIs for a deal-finder app; investigating a £140K forgotten estate and a WWII SAS hero’s story; and becoming a professional genealogist?",
    "kicker": "Q12 / THE BIG MONEY PLAYBOOKS",
    "title": "Property Data, Ownership Research & Genealogy",
    "subtitle": "Regrid parcel coverage, API sandbox, datasets, filters, import troubleshooting, ArcGIS exports and feature services; DataTree ownership searches, portfolio owners, legal descriptions, title vesting, title research, abstractor services and tax verification; real estate APIs, nationwide property research, heir hunting and starting a genealogy business.",
    "layout_template": "action_worksheet_summary",
    "reading_time_minutes": 15,
    "executive_summary": (
        "Regrid’s demonstrators, REtipster’s Seth, and the heir hunters make identification, "
        "record coverage, and verification central to their work. Regrid supplies parcel "
        "search, filtering, imports, and mapping delivery; Seth shows nationwide owner "
        "searches, document retrieval, and tax checks. Amy Moyes pursues Eileen Holmes’s "
        "roughly £140,000 estate while certificates are outstanding, ultimately reporting "
        "18 signed maternal heirs. Execution has separate clocks and costs: Regrid’s sandbox "
        "token lasts at most 30 days, while Seth reports 24–48 hours for abstractor retrieval. "
        "The alternatives matter: static exports versus feature services, convenient reports "
        "versus direct tax inquiries, and Amy’s competitive gamble versus Gareth Langford’s "
        "search for a quick, modest-value case. Vanessa Bland’s failed first business adds "
        "the commercial lesson: research skill alone did not supply marketing, adequate "
        "pricing, or staying power."
    ),
    "key_metrics": [
        {
            "label": "Sandbox token lifespan",
            "metric": "Sandbox token lifespan",
            "value": "Maximum 30 days",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Regrid’s sandbox demonstrator describes the generated trial token’s "
                "expiration and the product limits displayed alongside it."
            ),
            "source": "Regrid ([RVakKAvFa_M @ 00:01:41])",
        },
        {
            "label": "Portfolio-filter viewing surcharge",
            "metric": "Portfolio-filter viewing surcharge",
            "value": "$0.25 per record",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Seth reports this additional premium-filter charge upon viewing results, "
                "not merely exporting them, with 4,108 results visible in the example."
            ),
            "source": "REtipster ([9RvXCiHUzlo @ 00:03:16])",
        },
        {
            "label": "Eileen Holmes signed beneficiaries",
            "metric": "Eileen Holmes signed beneficiaries",
            "value": "18 signed maternal heirs",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Amy reports that 18 maternal heirs have signed with Finders International "
                "so far; the estate is described as worth around £140,000."
            ),
            "source": "Ancestry ([ClFseOLAURA @ 00:33:40])",
        },
        {
            "label": "Accepted import match rate",
            "metric": "Accepted import match rate",
            "value": "97%",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "After geocoding and matching by latitude and longitude, Regrid’s "
                "demonstrator accepts the example’s 97% match rate and finishes importing."
            ),
            "source": "Regrid ([VAtPDJ1KDjw @ 00:10:20])",
        },
    ],
    "sections": [
        {
            "title": "The Practitioner Consensus",
            "paragraphs": [
                (
                    "Start with the identifier that actually reaches the record. REtipster’s Seth "
                    "opens property research with an address, an assessor’s parcel number, or "
                    "an owner name plus the state and county. For the vacant Putnam County "
                    "lot, Seth prefers the parcel number because the owner may hold several "
                    "properties in the same county; the number takes the search to the specific "
                    "parcel [ntT8V0gnpAs @ 00:02:24]. Regrid’s import demonstrator makes the same "
                    "distinction operationally: the importer attaches information to individual "
                    "properties, not larger census geographies, and offers latitude/longitude, "
                    "parcel number, and address matching. Addresses are the least precise of "
                    "those choices because abbreviations and other variations interfere with "
                    "matching [VAtPDJ1KDjw @ 00:03:39]. On Ancestry, Amy Moyes faces the human "
                    "version of that identification problem: Stephen William Gardner also "
                    "appears as William Stephen, while Gardner has several spelling variants. "
                    "Amy orders possible records and divides surname searches among colleagues "
                    "rather than treating the first plausible entry as settled "
                    "[ClFseOLAURA @ 00:06:14]. The shared working behavior is specific: Seth "
                    "narrows a property, Regrid narrows a match, and Amy narrows a person. Each "
                    "demonstration moves from a broad label toward the record that can resolve "
                    "the actual question, with additional searching when that label remains ambiguous."
                ),
                (
                    "Coverage is something these operators inspect, not something they infer from "
                    "a nationwide label. Regrid’s Matt Hamill walks through a coverage spreadsheet "
                    "showing the state, county, geographic identifier, last refresh, parcel count, "
                    "and percentage coverage for individual fields. Some fields reach complete "
                    "coverage within a county; others depend on what the county or partner "
                    "supplies [EToN9mWFZWc @ 00:08:16]. Seth makes the equivalent move before "
                    "title research: open DataTree’s geographic coverage map, select the county, "
                    "and look for Transaction History Full and preferably the Title Chain and "
                    "Lien Report. The report’s existence and its historical reach are separate "
                    "questions [GfyX48eCbRY @ 00:01:23]. The heir hunters encounter precisely "
                    "that kind of reach problem on Audrey Barton’s case. Gareth Langford knows "
                    "Audrey married, but the marriage occurred in 2011, while the majority of "
                    "the indexes the team uses stop at 2005 [ClFseOLAURA @ 00:13:32]. Regrid "
                    "also distinguishes a county’s fresh acquisition from a smaller table edit; "
                    "Matt says the last-refresh date changes when fresh county data is pulled "
                    "[EToN9mWFZWc @ 00:21:46]. The practical baseline across these accounts is "
                    "to inspect which records, fields, and dates are reachable before expecting "
                    "the search interface to answer the whole research question."
                ),
                (
                    "The records business also has a time budget. Seth uses a worksheet to "
                    "avoid spending hours on each property and says the targeted-offer research "
                    "usually takes 15–20 minutes at most. The timing changes with the acquisition "
                    "approach: after a response to a neutral mailing, or after a response to "
                    "an initial blind offer [ntT8V0gnpAs @ 00:00:15]. Gareth describes a roughly "
                    "£30,000 estate as relatively low value for Fraser and Fraser, making a "
                    "small family, workable names, and limited research time especially desirable "
                    "[ClFseOLAURA @ 00:10:35]. Vanessa Bland reaches the same commercial issue "
                    "through a failed first business rather than an estate search. Vanessa "
                    "charged a first customer by reference to previous employment wages and "
                    "found that this did not cover the costs of operating a business "
                    "[DT_9__xTTeo @ 00:02:51]. Later, Vanessa recommends keeping reference "
                    "materials close at hand so paid research time is not consumed by repeated "
                    "trips to obtain basic resources [DT_9__xTTeo @ 00:11:52]. These are "
                    "different services, but the practitioners explicitly watch the hours "
                    "behind the deliverable. Seth streamlines a property decision, Gareth "
                    "looks for a case that can justify the effort, and Vanessa prices the "
                    "business beyond the hours spent performing the visible research."
                ),
            ],
            "table": {
                "caption": "Baseline research habits demonstrated across property and family records",
                "headers": ["Research starting point", "Practitioner execution", "Expert Source"],
                "rows": [
                    [
                        "A vacant parcel needs a more precise locator than an owner’s name alone.",
                        "Seth searches the county and APN to select the particular property being researched.",
                        "REtipster ([ntT8V0gnpAs @ 00:03:22])",
                    ],
                    [
                        "A person or entity can be searched without already knowing a property address.",
                        "Select owner search and use the name under which the real estate is held.",
                        "REtipster ([y5XZp-4n_uc @ 00:04:17])",
                    ],
                    [
                        "A nationwide parcel collection still has county-specific differences in field availability.",
                        "Matt checks coverage percentages, parcel counts, and refresh information in the detailed report.",
                        "Regrid ([EToN9mWFZWc @ 00:08:16])",
                    ],
                    [
                        "A title search depends on both available report types and their historical reach.",
                        "Seth checks Transaction History Full and preferably the Title Chain and Lien Report.",
                        "REtipster ([GfyX48eCbRY @ 00:01:23])",
                    ],
                    [
                        "An apparently missing marriage can fall outside the dates covered by working indexes.",
                        "Gareth identifies Audrey’s 2011 marriage as later than most indexes the team uses.",
                        "Ancestry ([ClFseOLAURA @ 00:13:32])",
                    ],
                    [
                        "An hourly research business still carries costs beyond the researcher’s own working wage.",
                        "Vanessa identifies omitted operating costs as the problem with the first customer’s fee.",
                        "Vanessa Bland ([DT_9__xTTeo @ 00:02:51])",
                    ],
                ],
            },
        },
        {
            "title": "Exact Street Mechanics, Tools & Numbers",
            "paragraphs": [
                (
                    "Regrid’s sandbox sequence starts with an account, a generated token, and "
                    "the endpoint examples. The latitude/longitude demonstration uses a ten-meter "
                    "radius and limits the response to three parcel records. The presenter "
                    "also warns that trial searches must stay within the counties included "
                    "in the trial subset [RVakKAvFa_M @ 00:05:44]. For a desktop search, Regrid’s "
                    "filter demonstrator first opens a project, sets calculated acres between "
                    "one and three, and loads the results onto the map. Adding residential "
                    "delivery indicator Y narrows the result to the combination of both "
                    "conditions; the selected boundary controls the area counted "
                    "[cKYlwRY3aVw @ 00:00:46]. Datasets are a separate working collection: "
                    "imported information, surveys, bookmarks, or publicly available platform "
                    "data. The demonstrator adds a Detroit tax-foreclosure dataset with the "
                    "plus button and removes it from the map with the X button "
                    "[-s07juX_8jE @ 00:00:17]. For an Esri destination, the feature-service "
                    "demo uses Content, New Item, and URL in ArcGIS Online, then supplies "
                    "Regrid’s URL and token [X-_cLY3_96Y @ 00:00:32]. Once loaded, the service "
                    "exposes parcel attributes for filtering and styling. These demonstrations "
                    "give distinct controls for requesting records, narrowing visible parcels, "
                    "adding a collection, and bringing the parcel layer into an Esri environment."
                ),
                (
                    "Seth’s owner search begins by setting the dropdown to Owner, entering "
                    "the name, and adding whatever geography is known. A common surname "
                    "produces a crowded result list; in the example, adding George to Jones "
                    "while searching California brings the result to 117 properties "
                    "[y5XZp-4n_uc @ 00:02:02]. Once a property is open, View Other Properties "
                    "Owned displays holdings nationwide under that same name. Alternatively, "
                    "Advanced Search offers a Properties Owned range, such as five to ten; "
                    "that range counts holdings nationwide, not only inside the selected "
                    "county [9RvXCiHUzlo @ 00:02:27]. For deed-ready detail, Seth selects "
                    "Rapid Legal & Vesting, supplies a reference number, and places the order. "
                    "The service extracts the legal description from the latest full-value "
                    "deed and vesting from the latest transfer document, then sends the "
                    "information to staff for review; Seth gives a usual turnaround of "
                    "30 minutes to two hours [aUiod-Jy68U @ 00:01:50]. Amy’s document ordering "
                    "is more urgent: while researching Eileen’s maternal relatives, Amy "
                    "asks for a record locally and requests faxed details or a telephone "
                    "reading if possible [ClFseOLAURA @ 00:08:36]. Both searches move beyond "
                    "a displayed name to the underlying record, but the property report "
                    "and the family certificate serve their own specific questions."
                ),
                (
                    "Title and tax work have their own delivery routes. In DataTree’s title "
                    "report, Seth uses document checkboxes to retrieve available images and "
                    "examine the actual wording. A different icon marks documents that are "
                    "not immediately available; selecting it requests an abstractor, with "
                    "a stated delivery of about 24–48 hours [GfyX48eCbRY @ 00:04:22]. TaxSource "
                    "starts from Property Data Reports and an order on the selected property. "
                    "Seth describes automatic reports at about $3–$4 and manual fulfillment "
                    "at $6–$8, with some exceptional cases costing more. The Minnesota "
                    "example costs $6 and takes about 24–48 hours "
                    "[2ThZ61aal9k @ 00:03:05]. Regrid’s static ArcGIS route is different: "
                    "export eligible bookmarks, surveys, or imported spreadsheet data as a "
                    "shapefile, wait for the download, extract the zipped folder, and drag "
                    "all component files into the ArcGIS contents pane "
                    "[EVN-9bqTEtM @ 00:01:21]. Vanessa’s genealogy setup puts everyday "
                    "research resources within reach: subscriptions such as Ancestry, Find "
                    "My Past, and My Heritage belong among the business expenses, alongside "
                    "marketing and further courses [DT_9__xTTeo @ 00:13:29]. The operators "
                    "therefore distinguish an instant screen result, an ordered document, "
                    "a manual retrieval, an exported spatial file, and the subscriptions "
                    "that support repeated research."
                ),
            ],
            "table": {
                "caption": "Concrete controls, delivery steps, and quoted operating numbers",
                "headers": ["Task and control", "Demonstrated sequence or number", "Expert Source"],
                "rows": [
                    [
                        "Test parcel responses using the sandbox’s latitude and longitude endpoint examples.",
                        "Use a ten-meter radius and limit the demonstration to three returned parcel records.",
                        "Regrid ([RVakKAvFa_M @ 00:06:00])",
                    ],
                    [
                        "Filter the project for acreage first and then add a residential delivery condition.",
                        "Set calculated acres from one to three, add residential Y, and reload the map.",
                        "Regrid ([cKYlwRY3aVw @ 00:01:25])",
                    ],
                    [
                        "Add an existing collection without confusing map removal with deleting the dataset.",
                        "Use plus to add the Detroit example and X to remove its map display.",
                        "Regrid ([-s07juX_8jE @ 00:00:31])",
                    ],
                    [
                        "Retrieve the full legal description and vesting through the separately ordered report.",
                        "Seth quotes $3 for Rapid Legal & Vesting plus a separate document-image charge.",
                        "REtipster ([aUiod-Jy68U @ 00:04:52])",
                    ],
                    [
                        "Request an unavailable document when its report entry lacks an instant-image checkbox.",
                        "Click the abstractor-request icon and expect the stated approximate 24–48-hour retrieval period.",
                        "REtipster ([GfyX48eCbRY @ 00:04:38])",
                    ],
                    [
                        "Move eligible personally created or imported spatial data into an ArcGIS desktop project.",
                        "Download the shapefile archive, extract it, and drag every component into the contents pane.",
                        "Regrid ([EVN-9bqTEtM @ 00:01:21])",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Small controls that change the research run",
                "body": "Use the specific switches the demonstrators actually put to work.",
                "items": [
                    (
                        "Use the sandbox’s count parameter when asking how many parcels match; "
                        "the presenter says count requests do not increment the results value "
                        "the way returned parcel records do. "
                        "[Regrid — RVakKAvFa_M @ 00:11:19]"
                    ),
                    (
                        "After narrowing a portfolio-owner list, remove duplicate owners so "
                        "the contact list does not repeat the same owner for every holding. "
                        "[REtipster — 9RvXCiHUzlo @ 00:04:02]"
                    ),
                    (
                        "When an owner dropdown shows only its top values, begin typing the "
                        "desired phrase to refine the available choices before loading the filter. "
                        "[Regrid — cKYlwRY3aVw @ 00:02:02]"
                    ),
                    (
                        "When family-name variants stall the search, divide those variants "
                        "among colleagues, as Amy does with Gardner spellings. "
                        "[Ancestry — ClFseOLAURA @ 00:07:08]"
                    ),
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Locate the property or named owner",
                    "action": "Select the appropriate DataTree search type and enter the known identifiers.",
                    "detail": (
                        "Seth uses an address, APN, or owner name with the state and county; "
                        "for the example vacant lot, the APN is the more precise locator. "
                        "[REtipster — ntT8V0gnpAs @ 00:02:24]"
                    ),
                },
                {
                    "step": 2,
                    "title": "Test an import before completing it",
                    "action": "Inspect results, correct the county, and rerun one matching change at a time.",
                    "detail": (
                        "Regrid’s demonstrator changes the location to Cuyahoga County and "
                        "retests before moving on to parcel-number matching. "
                        "[Regrid — VAtPDJ1KDjw @ 00:02:52]"
                    ),
                },
                {
                    "step": 3,
                    "title": "Order the required document detail",
                    "action": "Use Rapid Legal & Vesting when the full description and exact vesting are needed.",
                    "detail": (
                        "Place the order with a reference number and review the returned "
                        "report alongside its recorded deed; Seth describes staff review "
                        "and a usual 30-minute to two-hour turnaround. "
                        "[REtipster — aUiod-Jy68U @ 00:01:50]"
                    ),
                },
                {
                    "step": 4,
                    "title": "Resolve the outstanding family records",
                    "action": "Compare incoming certificates with the possible child and sibling matches.",
                    "detail": (
                        "Amy’s incoming birth certificate excludes the possible daughter; "
                        "the subsequent death-record check confirms the brother and identifies "
                        "Eileen as the informant. "
                        "[Ancestry — ClFseOLAURA @ 00:28:05] "
                        "[Ancestry — ClFseOLAURA @ 00:28:27]"
                    ),
                },
            ],
        },
        {
            "title": "Where Practitioners Disagree & Alternative Playbooks",
            "paragraphs": [
                (
                    "Seth gives two materially different descriptions of the Property Detail "
                    "Report’s legal-description usefulness. In the broad property walkthrough, "
                    "Seth calls the displayed description full and useful for a purchase "
                    "agreement or deed [ntT8V0gnpAs @ 00:07:04]. In the dedicated legal-and-vesting "
                    "demonstration, Seth says the same report usually supplies an abbreviated "
                    "description, with the example showing only Lot 38 Delmar. Rapid Legal "
                    "& Vesting instead returns the fuller wording and the underlying deed "
                    "[aUiod-Jy68U @ 00:06:10]. That is a concrete contrast in the examples, "
                    "not a reason to pretend every report contains identical detail. "
                    "Regrid likewise offers different mapping paths rather than one universal "
                    "export button. The desktop-export presenter says ordinary exports are "
                    "generally spreadsheets, while spatial exports are available for data "
                    "created through bookmarks or surveys, or brought in through a spreadsheet "
                    "[EVN-9bqTEtM @ 00:00:24]. The feature-service presenter instead demonstrates "
                    "a URL-and-token connection that brings nationwide parcel geometries and "
                    "attributes into an Esri environment [X-_cLY3_96Y @ 00:00:02]. The first "
                    "route downloads an eligible collection; the second loads a service layer. "
                    "The choice in these demonstrations follows the actual deliverable: a "
                    "description on a report, a reviewed deed extract, a local spatial file, "
                    "or a connected parcel layer."
                ),
                (
                    "The deal-finder builder at REI Tech Club wants active listings and "
                    "a tool that sends a promising deal each day. Their selection process "
                    "ends with Rentcast because pricing and API documentation are visible "
                    "up front and some APIs can be tested free shortly after signup "
                    "[NMsRlUhQbUI @ 00:03:54]. The presenter also states the tradeoff: Rentcast "
                    "uses third-party-derived information rather than a direct MLS source, "
                    "and the roughly 96% nationwide coverage figure is a claim the presenter "
                    "attributes to the service. Non-residential commercial categories were "
                    "the major omission they noticed [NMsRlUhQbUI @ 00:04:08]. Regrid’s "
                    "sandbox has a different target: parcel records, owner queries, addresses, "
                    "assessor parcel numbers, polygons, and metadata. Its query-by-fields "
                    "example combines the Dallas County identifier with an owner-name "
                    "condition to count 7-Eleven parcels [RVakKAvFa_M @ 00:07:23]. Seth’s "
                    "valuation process uses yet another approach, manually comparing similar "
                    "for-sale and sold properties on Zillow, with sold prices treated as "
                    "more realistic comparables and asking prices as evidence of competition "
                    "[ntT8V0gnpAs @ 00:16:52]. These are alternative research jobs: choosing "
                    "an on-market application feed, interrogating a parcel collection, and "
                    "checking comparable properties for an offer. The presenters do not "
                    "describe the three as interchangeable sources of the same information."
                ),
                (
                    "Amy’s Eileen Holmes strategy is deliberately aggressive about timing. "
                    "Unable to eliminate a possible daughter immediately, Amy orders the "
                    "birth record and continues into wider family research on a gut feeling "
                    "that neither marriage produced children. The stated downside is direct: "
                    "if closer children exist, the more distant heirs being traced would "
                    "not be entitled [ClFseOLAURA @ 00:04:32]. Gareth’s opening preference "
                    "on Audrey Barton is almost the opposite commercial posture: a modest "
                    "estate calls for a small family and quick work, although common "
                    "surnames and childless branches defeat that hoped-for simplicity "
                    "[ClFseOLAURA @ 00:35:12]. Vanessa’s professional-genealogy approach "
                    "emphasizes choosing a specialization, whether a record collection, "
                    "geography, or historical period, and using a business plan to keep "
                    "the work directed [DT_9__xTTeo @ 00:07:51]. Vanessa also describes "
                    "differing views on certification, saying some people consider it "
                    "very important and others do not; Vanessa has no certification "
                    "and draws on history qualifications and experience "
                    "[DT_9__xTTeo @ 00:05:27]. The contrast is between actual operating "
                    "approaches, not a manufactured dispute among the teams: Amy accepts "
                    "research risk to beat competitors, Gareth wants the case economics "
                    "to support the workload, and Vanessa builds a defined service around "
                    "skills, positioning, and business costs."
                ),
            ],
            "table": {
                "caption": "Different jobs, different approaches, and genuine changes in emphasis",
                "headers": ["First approach", "Contrasting approach or limitation", "Expert Source"],
                "rows": [
                    [
                        "Seth’s general walkthrough calls the displayed Property Detail Report description full and useful.",
                        "The dedicated demonstration finds an abbreviated description and orders the fuller legal-and-vesting report.",
                        "REtipster ([ntT8V0gnpAs @ 00:07:04]); REtipster ([aUiod-Jy68U @ 00:06:10])",
                    ],
                    [
                        "Export personally created or imported data as an eligible spatial file for desktop use.",
                        "Connect the nationwide feature-service layer through its URL and token inside ArcGIS Online.",
                        "Regrid ([EVN-9bqTEtM @ 00:00:24]); Regrid ([X-_cLY3_96Y @ 00:00:32])",
                    ],
                    [
                        "REI Tech Club selects Rentcast for accessible pricing, documentation, and early API testing.",
                        "The presenter acknowledges third-party-derived data and missing non-residential commercial categories in the review.",
                        "REI Tech Club ([NMsRlUhQbUI @ 00:03:54]); REI Tech Club ([NMsRlUhQbUI @ 00:04:08])",
                    ],
                    [
                        "Seth manually checks Zillow listings and sold properties when evaluating comparable land parcels.",
                        "REI Tech Club rejects scraping consumer sites for the application, citing fragility and liability.",
                        "REtipster ([ntT8V0gnpAs @ 00:16:52]); REI Tech Club ([NMsRlUhQbUI @ 00:01:19])",
                    ],
                    [
                        "Amy researches wider family branches while the possible daughter’s certificate remains outstanding.",
                        "Gareth initially wants a small, straightforward family because Audrey’s estate is relatively modest.",
                        "Ancestry ([ClFseOLAURA @ 00:04:53]); Ancestry ([ClFseOLAURA @ 00:10:35])",
                    ],
                    [
                        "Vanessa says some genealogists regard qualifications or certification as especially important professional signals.",
                        "Vanessa personally works without certification and recommends a useful research specialization either way.",
                        "Vanessa Bland ([DT_9__xTTeo @ 00:05:27]); Vanessa Bland ([DT_9__xTTeo @ 00:07:51])",
                    ],
                ],
            },
        },
        {
            "title": "Firsthand Failure Modes, Traps & Economics Checks",
            "paragraphs": [
                (
                    "Regrid’s import demonstration begins with a visibly poor match result "
                    "and improves only after specific corrections. Selecting Cuyahoga County "
                    "instead of the wrong location raises matching to 75%; switching "
                    "to parcel numbers raises it to 87% [VAtPDJ1KDjw @ 00:03:25]. The "
                    "presenter checks missing identifiers and formatting, inspects unmatched "
                    "rows, then geocodes the addresses after combining house number and "
                    "street name. Latitude/longitude matching reaches the accepted 97% "
                    "[VAtPDJ1KDjw @ 00:09:57]. The sandbox contains a smaller but revealing "
                    "reversal: the presenter initially expects 232 Dallas County 7-Eleven "
                    "results, gets 238, and explicitly corrects the earlier number "
                    "[RVakKAvFa_M @ 00:08:29]. Seth’s tax walkthrough exposes a different "
                    "trap. The Advanced Search delinquency filter draws from assessor "
                    "information sourced annually, works in about half the country as "
                    "described, and can indicate a delinquency sometime in the preceding "
                    "year rather than one still outstanding today "
                    "[2ThZ61aal9k @ 00:04:38]. The failures are concrete: an import can "
                    "attach too few rows, an expected query count can be wrong, and "
                    "a delinquency flag can describe an earlier condition. The corrections "
                    "shown are equally concrete—change matching inputs, accept the actual "
                    "returned count, and distinguish the assessor filter from the more "
                    "current tax information Seth seeks separately."
                ),
                (
                    "Genealogy produces reversals that a successful name match cannot "
                    "resolve on its own. Amy finds an 88-year-old cousin who eventually "
                    "recalls Eileen, but that conversation still cannot establish whether "
                    "Eileen had children. The incoming birth certificate finally excludes "
                    "the possible daughter, and the brother’s death record names Eileen "
                    "as informant [ClFseOLAURA @ 00:28:05]. The research then follows "
                    "Charles Alfred Mitchell, whose wartime survival leads to a marriage "
                    "and four children, including Christine Ayers in Norfolk "
                    "[ClFseOLAURA @ 00:31:25]. Christine receives news of a prospective "
                    "share and learns more about the family’s SAS history; Amy ultimately "
                    "reports 18 maternal heirs signed so far, calling the case a "
                    "successful gamble and a relief [ClFseOLAURA @ 00:33:40]. Vanessa’s "
                    "first business supplies a less triumphant operating history: a "
                    "website and a single share among friends did not amount to sustained "
                    "marketing. Vanessa obtained one customer, undercharged, and closed "
                    "the business after about six months, later judging that period "
                    "too short [DT_9__xTTeo @ 00:01:58]. Amy’s outcome depended on resolving "
                    "the contested records; Vanessa’s research result pleased the customer "
                    "but did not repair the business model. Both accounts separate "
                    "doing useful research from completing the broader job successfully."
                ),
                (
                    "The economics checks are visible before any final payout. Seth’s "
                    "portfolio search produces 4,108 results, but the premium filter "
                    "charges an additional 25 cents per record merely to view them. "
                    "Seth recommends adding more criteria before paying to see such "
                    "a broad list [9RvXCiHUzlo @ 00:03:16]. Vanessa describes the "
                    "same cost pressure in a service business: subscriptions, marketing, "
                    "courses, memberships, reference materials, and equipment must be "
                    "considered when setting an hourly rate, with some spending required "
                    "before customers arrive [DT_9__xTTeo @ 00:14:18]. REI Tech Club "
                    "encounters an access bottleneck even before selecting a provider: "
                    "a HouseCanary demo form rejects a personal Gmail address and "
                    "requires a corporate email [NMsRlUhQbUI @ 00:03:41]. Seth also "
                    "reports property-condition surprises despite useful imagery. The "
                    "map shows conditions when the image was taken, not necessarily "
                    "the property’s current state; the demonstrated alternative is "
                    "having someone drive by and take photographs "
                    "[ntT8V0gnpAs @ 00:13:36]. These practitioners report distinct "
                    "leaks in the workflow: expensive broad results, unpriced overhead, "
                    "a blocked sales process, and old imagery. None is resolved by "
                    "the mere appearance of a name, parcel boundary, or attractive "
                    "figure on a research screen."
                ),
            ],
            "table": {
                "caption": "Observed bottlenecks and the checks the practitioners actually describe",
                "headers": ["Observed trap or reversal", "Practitioner response and economic consequence", "Expert Source"],
                "rows": [
                    [
                        "The spreadsheet test initially matches poorly because the selected location is wrong.",
                        "Changing to the correct county produces a 75% match before further identifier corrections.",
                        "Regrid ([VAtPDJ1KDjw @ 00:03:25])",
                    ],
                    [
                        "The sandbox’s predicted Dallas owner-query count does not match the actual returned result.",
                        "The presenter corrects the expected 232 to the returned count of 238 parcels.",
                        "Regrid ([RVakKAvFa_M @ 00:08:29])",
                    ],
                    [
                        "Seth’s automatic tax report is dated February 9 during a February 18 demonstration.",
                        "Seth points to the collector’s phone number for asking whether payment is current now.",
                        "REtipster ([2ThZ61aal9k @ 00:01:41])",
                    ],
                    [
                        "Audrey’s modest-value estate takes more research than the small-family opening strategy anticipated.",
                        "The team eventually finds two paternal and ten maternal beneficiaries, twelve beneficiaries altogether.",
                        "Ancestry ([ClFseOLAURA @ 00:41:52])",
                    ],
                    [
                        "Vanessa’s first business closes after about six months without enough time to establish itself.",
                        "Vanessa contrasts that short attempt with two years spent developing the second genealogy business.",
                        "Vanessa Bland ([DT_9__xTTeo @ 00:04:13])",
                    ],
                    [
                        "Seth warns that a lower monthly DataTree plan can become expensive under heavy usage.",
                        "Report orders consume monthly credits, with further charges after those credits have been used.",
                        "REtipster ([ntT8V0gnpAs @ 00:25:41]); REtipster ([ntT8V0gnpAs @ 00:26:09])",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Checks tied to demonstrated breakdowns",
                "body": "Apply the checks to the particular research problem each practitioner describes.",
                "items": [
                    (
                        "Before clicking Finish Import, inspect the match results; Regrid’s "
                        "presenter warns that completing too early can produce an effectively "
                        "empty dataset with nothing attached to parcels. "
                        "[Regrid — VAtPDJ1KDjw @ 00:01:29]"
                    ),
                    (
                        "Before relying on a title-chain report’s history, read its coverage "
                        "start date. Seth’s Dallas example reaches only February 11, 2012, "
                        "while the Arizona example reaches 1970. "
                        "[REtipster — GfyX48eCbRY @ 00:02:42] "
                        "[REtipster — GfyX48eCbRY @ 00:03:12]"
                    ),
                    (
                        "Keep Amy’s possible-child question tied to the certificate: the "
                        "cousin’s recollection does not settle it, and the team’s wider "
                        "research could be displaced by a child of Eileen. "
                        "[Ancestry — ClFseOLAURA @ 00:27:22]"
                    ),
                    (
                        "Before setting a genealogy hourly rate, include the actual "
                        "business expenses rather than copying a previous employment wage; "
                        "Vanessa identifies that omission in the first paid project. "
                        "[Vanessa Bland — DT_9__xTTeo @ 00:02:51]"
                    ),
                ],
            },
        },
    ],
    "pull_quote": (
        "“You have to redo the search under variant spellings.” — "
        "Ancestry (ClFseOLAURA @ 00:07:08)."
    ),
    "diagram_id": "diag-08",
    "action_checklist": [
        (
            "Open DataTree’s owner search and enter the actual ownership name, adding "
            "state and county when known and widening geographically when necessary. "
            "[REtipster — y5XZp-4n_uc @ 00:04:17]"
        ),
        (
            "Inspect Regrid’s county coverage report for the required fields, their "
            "coverage percentages, and the last-refresh information. "
            "[Regrid — EToN9mWFZWc @ 00:08:16]"
        ),
        (
            "Test the Regrid sandbox with its preloaded examples and keep trial queries "
            "inside the counties available to the token. "
            "[Regrid — RVakKAvFa_M @ 00:05:25]"
        ),
        (
            "Order TaxSource for the selected property, read its update date, and "
            "use the tax collector’s listed number when asking about payment status now. "
            "[REtipster — 2ThZ61aal9k @ 00:01:41]"
        ),
        (
            "Order the records needed to resolve possible close kin while tracking "
            "the exact name variants that complicate the family search. "
            "[Ancestry — ClFseOLAURA @ 00:06:14]"
        ),
        (
            "Write the genealogy business plan around a chosen specialization and "
            "return to it when deciding the direction of the service. "
            "[Vanessa Bland — DT_9__xTTeo @ 00:08:27]"
        ),
    ],
    "statutory_citations": [
        {
            "title": "Regrid — Regrid Parcel Data - Overview & Coverage [00:08:16]",
            "url": "https://www.youtube.com/watch?v=EToN9mWFZWc&t=496s",
            "relevance": (
                "Primary practitioner testimony on county coverage, refresh information, "
                "parcel counts, and field-level availability."
            ),
        },
        {
            "title": "REtipster — DataTree Hacks: How to Do Title Research and Hire Abstractor Services [00:01:23]",
            "url": "https://www.youtube.com/watch?v=GfyX48eCbRY&t=83s",
            "relevance": (
                "Primary practitioner testimony on checking available transaction and "
                "title-chain reports before starting title research."
            ),
        },
        {
            "title": "Ancestry — The £140K Forgotten Estate & The WWII SAS Hero | Heir Hunters | Ancestry [00:33:40]",
            "url": "https://www.youtube.com/watch?v=ClFseOLAURA&t=2020s",
            "relevance": (
                "Primary practitioner testimony on the signed maternal heirs and the "
                "reported outcome of the Eileen Holmes investigation."
            ),
        },
        {
            "title": "Vanessa Bland — How to Start a Genealogy Business | Things I Wish I'd Known | Becoming a Professional Genealogist [00:02:51]",
            "url": "https://www.youtube.com/watch?v=DT_9__xTTeo&t=171s",
            "relevance": (
                "Primary practitioner testimony on undercharging and failing to include "
                "business operating costs in a research fee."
            ),
        },
    ],
    "source_citations": [
        {
            "source_type": "video_pro_tip",
            "video_id": "RVakKAvFa_M",
            "title": "Quick Start Regrid's Interactive API Sandbox Guide",
            "channel": "Regrid",
            "author": "Regrid",
            "text": "If you are on a trial token, it is a subset of the nationwide data, so make sure you are searching within the counties that are available for your token.",
            "tip": "If you are on a trial token, it is a subset of the nationwide data, so make sure you are searching within the counties that are available for your token.",
            "timestamp": 344,
            "timestamp_seconds": 344,
            "timestamp_label": "[00:05:44]",
            "url": "https://www.youtube.com/watch?v=RVakKAvFa_M&t=344s",
            "markdown": "[00:05:44](https://www.youtube.com/watch?v=RVakKAvFa_M&t=344s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on trial-token geographic limits and sandbox testing.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "aUiod-Jy68U",
            "title": "DataTree Hacks: Find Full Legal Descriptions and Title Vesting Information",
            "channel": "REtipster",
            "author": "REtipster",
            "text": "The time it takes to get these reports back is usually anywhere from 30 minutes to two hours.",
            "tip": "The time it takes to get these reports back is usually anywhere from 30 minutes to two hours.",
            "timestamp": 129,
            "timestamp_seconds": 129,
            "timestamp_label": "[00:02:09]",
            "url": "https://www.youtube.com/watch?v=aUiod-Jy68U&t=129s",
            "markdown": "[00:02:09](https://www.youtube.com/watch?v=aUiod-Jy68U&t=129s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on Rapid Legal & Vesting report turnaround.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "GfyX48eCbRY",
            "title": "DataTree Hacks: How to Do Title Research and Hire Abstractor Services",
            "channel": "REtipster",
            "author": "REtipster",
            "text": "You can request an abstractor to go and get this document from that state and county, and you'll get it in about 24 to 48 hours.",
            "tip": "You can request an abstractor to go and get this document from that state and county, and you'll get it in about 24 to 48 hours.",
            "timestamp": 278,
            "timestamp_seconds": 278,
            "timestamp_label": "[00:04:38]",
            "url": "https://www.youtube.com/watch?v=GfyX48eCbRY&t=278s",
            "markdown": "[00:04:38](https://www.youtube.com/watch?v=GfyX48eCbRY&t=278s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on requesting documents unavailable for instant retrieval.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "EVN-9bqTEtM",
            "title": "Exporting Regrid Data to ArcGIS - Regrid Property App (Web)",
            "channel": "Regrid",
            "author": "Regrid",
            "text": "Generally speaking, we allow for only spreadsheet exports, but there are certain edge cases where you can export data that you have created as a spatial file.",
            "tip": "Generally speaking, we allow for only spreadsheet exports, but there are certain edge cases where you can export data that you have created as a spatial file.",
            "timestamp": 24,
            "timestamp_seconds": 24,
            "timestamp_label": "[00:00:24]",
            "url": "https://www.youtube.com/watch?v=EVN-9bqTEtM&t=24s",
            "markdown": "[00:00:24](https://www.youtube.com/watch?v=EVN-9bqTEtM&t=24s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the distinction between spreadsheet exports and eligible spatial exports.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "X-_cLY3_96Y",
            "title": "Feature Service Product Demo",
            "channel": "Regrid",
            "author": "Regrid",
            "text": "The first and key step is to use our token and URL to link the feature service to the ArcGIS Online environment.",
            "tip": "The first and key step is to use our token and URL to link the feature service to the ArcGIS Online environment.",
            "timestamp": 32,
            "timestamp_seconds": 32,
            "timestamp_label": "[00:00:32]",
            "url": "https://www.youtube.com/watch?v=X-_cLY3_96Y&t=32s",
            "markdown": "[00:00:32](https://www.youtube.com/watch?v=X-_cLY3_96Y&t=32s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on connecting Regrid’s feature service to ArcGIS Online.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "9RvXCiHUzlo",
            "title": "DataTree Hacks: How to Find Portfolio Owners With Multiple Properties",
            "channel": "REtipster",
            "author": "REtipster",
            "text": "Not exporting them, but just viewing them is going to cost some more. At the time of this recording, it's an additional 25 cents per record.",
            "tip": "Not exporting them, but just viewing them is going to cost some more. At the time of this recording, it's an additional 25 cents per record.",
            "timestamp": 196,
            "timestamp_seconds": 196,
            "timestamp_label": "[00:03:16]",
            "url": "https://www.youtube.com/watch?v=9RvXCiHUzlo&t=196s",
            "markdown": "[00:03:16](https://www.youtube.com/watch?v=9RvXCiHUzlo&t=196s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on premium portfolio-filter charges triggered by viewing results.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "y5XZp-4n_uc",
            "title": "DataTree Hacks: How to Search and Find Property Owners Nationwide",
            "channel": "REtipster",
            "author": "REtipster",
            "text": "All you need to know is the name under which they own their real estate, be it their first and last name, the name of their spouse, or the name of whatever entity they own that owns their real estate.",
            "tip": "All you need to know is the name under which they own their real estate, be it their first and last name, the name of their spouse, or the name of whatever entity they own that owns their real estate.",
            "timestamp": 257,
            "timestamp_seconds": 257,
            "timestamp_label": "[00:04:17]",
            "url": "https://www.youtube.com/watch?v=y5XZp-4n_uc&t=257s",
            "markdown": "[00:04:17](https://www.youtube.com/watch?v=y5XZp-4n_uc&t=257s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the name needed for nationwide property-owner searches.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "EToN9mWFZWc",
            "title": "Regrid Parcel Data - Overview & Coverage",
            "channel": "Regrid",
            "author": "Regrid",
            "text": "We bump that last refresh date when we pull fresh data from the county, so that includes the geometries.",
            "tip": "We bump that last refresh date when we pull fresh data from the county, so that includes the geometries.",
            "timestamp": 1306,
            "timestamp_seconds": 1306,
            "timestamp_label": "[00:21:46]",
            "url": "https://www.youtube.com/watch?v=EToN9mWFZWc&t=1306s",
            "markdown": "[00:21:46](https://www.youtube.com/watch?v=EToN9mWFZWc&t=1306s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the meaning of the county last-refresh date.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "ClFseOLAURA",
            "title": "The £140K Forgotten Estate & The WWII SAS Hero | Heir Hunters | Ancestry",
            "channel": "Ancestry",
            "author": "Ancestry",
            "text": "We have established there are no paternal heirs, but there are several maternal heirs, and 18 of those have signed with us so far.",
            "tip": "We have established there are no paternal heirs, but there are several maternal heirs, and 18 of those have signed with us so far.",
            "timestamp": 2020,
            "timestamp_seconds": 2020,
            "timestamp_label": "[00:33:40]",
            "url": "https://www.youtube.com/watch?v=ClFseOLAURA&t=2020s",
            "markdown": "[00:33:40](https://www.youtube.com/watch?v=ClFseOLAURA&t=2020s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the reported beneficiary outcome of the Eileen Holmes case.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "-s07juX_8jE",
            "title": "Using Datasets - Regrid Property App (Web)",
            "channel": "Regrid",
            "author": "Regrid",
            "text": "A dataset, simply put, is any data that you have imported, that you've created with a survey or a bookmark, or which is publicly available on our platform.",
            "tip": "A dataset, simply put, is any data that you have imported, that you've created with a survey or a bookmark, or which is publicly available on our platform.",
            "timestamp": 3,
            "timestamp_seconds": 3,
            "timestamp_label": "[00:00:03]",
            "url": "https://www.youtube.com/watch?v=-s07juX_8jE&t=3s",
            "markdown": "[00:00:03](https://www.youtube.com/watch?v=-s07juX_8jE&t=3s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony defining the collections available through the dataset interface.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "cKYlwRY3aVw",
            "title": "Regrid Mapping Platform - Filter Data",
            "channel": "Regrid",
            "author": "Regrid",
            "text": "I put minimum one, maximum three, and I click Load on Map. This visually highlights the parcels that match my criteria.",
            "tip": "I put minimum one, maximum three, and I click Load on Map. This visually highlights the parcels that match my criteria.",
            "timestamp": 46,
            "timestamp_seconds": 46,
            "timestamp_label": "[00:00:46]",
            "url": "https://www.youtube.com/watch?v=cKYlwRY3aVw&t=46s",
            "markdown": "[00:00:46](https://www.youtube.com/watch?v=cKYlwRY3aVw&t=46s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on applying the demonstrated calculated-acreage filter.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "VAtPDJ1KDjw",
            "title": "Troubleshooting Data Import - Regrid Property App (Web)",
            "channel": "Regrid",
            "author": "Regrid",
            "text": "I generally consider over 95 to be acceptable.",
            "tip": "I generally consider over 95 to be acceptable.",
            "timestamp": 597,
            "timestamp_seconds": 597,
            "timestamp_label": "[00:09:57]",
            "url": "https://www.youtube.com/watch?v=VAtPDJ1KDjw&t=597s",
            "markdown": "[00:09:57](https://www.youtube.com/watch?v=VAtPDJ1KDjw&t=597s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the demonstrator’s preferred import match percentage after geocoding.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "DT_9__xTTeo",
            "title": "How to Start a Genealogy Business | Things I Wish I'd Known | Becoming a Professional Genealogist",
            "channel": "Vanessa Bland",
            "author": "Vanessa Bland",
            "text": "Whether or not you get any kind of certification, it is really useful to try to specialize.",
            "tip": "Whether or not you get any kind of certification, it is really useful to try to specialize.",
            "timestamp": 452,
            "timestamp_seconds": 452,
            "timestamp_label": "[00:07:32]",
            "url": "https://www.youtube.com/watch?v=DT_9__xTTeo&t=452s",
            "markdown": "[00:07:32](https://www.youtube.com/watch?v=DT_9__xTTeo&t=452s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on developing a specialization within a genealogy service.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "NMsRlUhQbUI",
            "title": "Best Real Estate Data APIs for Building a Deal Finder App",
            "channel": "REI Tech Club",
            "author": "REI Tech Club",
            "text": "They clearly shared their pricing and API documentation upfront on their website. I was even able to test a few of their APIs within just a few minutes of signing up and completely for free.",
            "tip": "They clearly shared their pricing and API documentation upfront on their website. I was even able to test a few of their APIs within just a few minutes of signing up and completely for free.",
            "timestamp": 234,
            "timestamp_seconds": 234,
            "timestamp_label": "[00:03:54]",
            "url": "https://www.youtube.com/watch?v=NMsRlUhQbUI&t=234s",
            "markdown": "[00:03:54](https://www.youtube.com/watch?v=NMsRlUhQbUI&t=234s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the accessibility factors behind selecting Rentcast.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "ntT8V0gnpAs",
            "title": "The Fastest Way to Research Any Property in the United States",
            "channel": "REtipster",
            "author": "REtipster",
            "text": "I usually spend about 15 to 20 minutes tops per deal to come up with this final targeted offer.",
            "tip": "I usually spend about 15 to 20 minutes tops per deal to come up with this final targeted offer.",
            "timestamp": 71,
            "timestamp_seconds": 71,
            "timestamp_label": "[00:01:11]",
            "url": "https://www.youtube.com/watch?v=ntT8V0gnpAs&t=71s",
            "markdown": "[00:01:11](https://www.youtube.com/watch?v=ntT8V0gnpAs&t=71s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on Seth’s reported time budget for targeted-offer research.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "2ThZ61aal9k",
            "title": "DataTree Hacks: TaxSource Reports and Property Tax Verification",
            "channel": "REtipster",
            "author": "REtipster",
            "text": "It's not pulling this information from the tax collector, it's pulling it from the assessor. And assessor data is only sourced annually in DataTree.",
            "tip": "It's not pulling this information from the tax collector, it's pulling it from the assessor. And assessor data is only sourced annually in DataTree.",
            "timestamp": 278,
            "timestamp_seconds": 278,
            "timestamp_label": "[00:04:38]",
            "url": "https://www.youtube.com/watch?v=2ThZ61aal9k&t=278s",
            "markdown": "[00:04:38](https://www.youtube.com/watch?v=2ThZ61aal9k&t=278s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony distinguishing the Advanced Search delinquency filter from collector-sourced tax status.",
        },
    ],
}
