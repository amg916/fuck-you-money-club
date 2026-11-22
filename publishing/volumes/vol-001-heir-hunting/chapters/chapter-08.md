# Chapter 08: Tools, Public Databases & Investigative Stack

*Choose authoritative records, lawful access, and reproducible source capture.*

> THE BIG MONEY PLAYBOOKS · THE FUCK YOU MONEY CLUB

## Executive Summary

Organize investigative tools by evidentiary role rather than subscription price. Official records establish the starting facts; indexed historical collections connect households; licensed tracing and newspaper sources help locate people and test hypotheses. Preserve the original record, retrieval context, and assertion supported by every source. This chapter translates access restrictions into concrete research decisions and follows severed mineral interests from recorded instruments to pooling dockets. Its mineral example separates a deadline-driven opportunity from an unproven title claim, using curative escrow and documented ownership conditions instead of assuming a database match creates a payable interest.

### Key Metrics

| Metric | Value | Confidence | Source |
| --- | --- | --- | --- |
| Investigative tiers | 3 |  |  |
| Source identity | 1 stable ID |  |  |

## Use a three-tier stack without confusing leads with proof  `🏷️ OPERATING_FRAMEWORK`

Tier 1 consists of official probate dockets, county recorder instruments, and vital registries. Begin with the court case number, decedent's identity, filing jurisdiction, representative, petition, inventory, notices, and distribution orders. A docket entry is an index event, not necessarily the complete filed document; retrieve the underlying petition or order when the assertion depends on its contents. At the recorder, capture instrument number, grantor, grantee, execution and recording dates, legal description, and referenced earlier instruments. At a vital registry, distinguish an index result from an informational copy or certified record and check who can request each. Official provenance does not make every statement true: an informant can still report an incorrect parent, and a petition may contain allegations never adopted by the court.

Tier 2 supplies historical linkage and property discovery through FamilySearch, Ancestry census collections, Social Security Death Index entries, digitized probate packets, and Regrid or DataTree parcel history. Search indexes broadly, then inspect images for household structure, marginal notes, neighbors, and transcription mistakes. A census relationship field can support co-residence and reported kinship without conclusively establishing legal parentage. SSDI coverage is incomplete and varies with source availability; absence does not prove a person is alive. Parcel aggregators are useful for locating assessment identifiers and likely ownership changes, but they do not replace recorded deeds or a title examination. A probate image hosted by a commercial platform remains a reproduction of a court record; preserve that provenance instead of automatically downgrading or upgrading its evidentiary value based on the website.

Tier 3 covers licensed skip-tracing, obituary archives, newspaper collections, and other corroboration used to locate potential claimants. Treat address and telephone matches as contact leads with retrieval dates, not evidence that a person inherited anything. An obituary can reveal married names, relatives, and migration paths, but family submissions may omit estranged relatives or use social relationships loosely. Confirm the relationship with stronger records before presenting a share schedule. Compare the cost of each query with its expected information value: spending $40 on a decisive court packet can outperform ten inexpensive searches repeating the same unsupported address. Maintain a source-purpose matrix so the investigator knows whether a tool is being used to discover a record, establish an event, corroborate an identity, or find a contact channel.

**Investigative stack and evidentiary handoff**

| Tier | Resources | Best use | Required follow-through |
| --- | --- | --- | --- |
| 1 | Probate courts; recorders; vital registries | Orders, instruments, registered events | Retrieve complete documents and evaluate informants |
| 2 | FamilySearch; Ancestry; SSDI; probate packets | Historical family linkage | Inspect images and resolve identity conflicts |
| 2 | Regrid; DataTree | Parcel and ownership leads | Reconcile against recorded instruments |
| 3 | Licensed tracing; obituaries; newspapers | Locate and corroborate | Confirm identity and relationship independently |

## Make every useful search reproducible  `🏷️ OPERATING_FRAMEWORK`

Give every captured source a stable identifier such as HH001-S0042, linked to the case and relevant person IDs. The source log should record repository, collection, jurisdiction, case or instrument number, document date, page range, retrieval timestamp with timezone, query terms, filters, and access method. Save the original permitted download before making annotations or OCR derivatives. Record a SHA-256 digest of the saved bytes and preserve the filename and media type. A hash can demonstrate that your saved file has not changed; it cannot prove the repository was accurate or that the document is genuine. For dynamically rendered pages, preserve a permitted page capture and the retrieval context, since a search URL alone may expire or reproduce a different result tomorrow.

Separate source records from assertions. A single marriage application may support a date, prior surname, age, and parental identity with different confidence levels. Create an assertion entry containing subject ID, predicate, proposed value, source ID, exact page or image reference, transcription, and analyst interpretation. Preserve the distinction between what the record says and what the investigator infers. When two sources conflict, retain both assertions and attach a resolution note rather than overwriting the older value. Track image derivatives back to the original bytes, including OCR software output and manual corrections. If access terms prevent storing a full image, record the allowed citation and retrieval path, plus the storage restriction, instead of quietly copying prohibited material into the shared case folder.

Negative searches deserve the same discipline. Record that the county birth index was searched for three spellings from 1900 through 1910 and note whether the collection excludes delayed registrations or certain districts. This supports a bounded conclusion about the search, not a claim that no birth occurred. Use a second reviewer to retrieve one decisive record from the citation alone and to reproduce one negative search with the documented filters. A failure points to missing collection names, unstable links, or ambiguous page numbering. Restrict shared working copies to the data needed for the assignment and keep contact details separate from broadly circulated proof exhibits. Before delivery, reconcile all cited source IDs, flag unavailable attachments, and preserve a versioned manifest identifying the exact exhibit set reviewed.

**SOP — Standard Operating Procedure**

1. Identify
   - Assign case, person, and source IDs.
   - Never use a mutable name as the sole record key.
2. Capture
   - Save the permitted original and retrieval context.
   - Include page references, timestamps, restrictions, and a byte digest.
3. Extract
   - Link assertions to exact evidence locations.
   - Separate transcriptions from analyst conclusions.
4. Reproduce
   - Have another researcher retrieve decisive evidence.
   - Resolve broken citations before releasing the exhibit manifest.

## Match the access route to the actual permitted purpose  `🏷️ STATUTORY_FACT`

The Driver's Privacy Protection Act, 18 U.S.C. section 2721, restricts disclosure of personal information from state motor vehicle records subject to enumerated exceptions. An heir research business does not gain blanket access because its work is useful or because a database vendor accepts payment. Identify the actual statutory basis and verify that the proposed use fits it. The litigation-related exception requires the appropriate connection to a proceeding or qualifying investigation, not a decorative case label added to an unrelated marketing search. The licensed private investigative agency exception ties permitted use to purposes allowed under the statute; a license is not an unrestricted pass. Highly restricted personal information has narrower treatment. Keep the vendor's permitted-use certification and the factual basis for the specific search together.

Section 2721 also addresses authorized recipients' resale and redisclosure, including recordkeeping requirements that can apply to redisclosures. Do not assume that information lawfully obtained for one purpose may be placed in a general prospecting list or handed to an unrelated buyer. Map the data's source, permitted purpose, recipient, and planned disclosure before using motor vehicle information to contact an alleged heir. Where the proposed purpose does not fit an available exception, use public probate notices, authorized vital-record requests, voluntarily supplied documents, or other lawful sources instead. Vendor marketing phrases such as public data or investigator grade do not settle the statutory question. Capture the precise product and source restrictions because a single search service may mix unrestricted public records with restricted datasets in one interface.

The Computer Fraud and Abuse Act, 18 U.S.C. section 1030, addresses specified unauthorized computer access and related conduct; it is not a general declaration that every terms-of-service dispute is a federal crime. Access analysis depends on the system, credentials, restrictions, conduct, and governing case law. Use accounts issued to the authorized researcher, approved export functions, and the repository's available public or licensed access routes. Do not bypass authentication, enter restricted accounts, reuse someone else's credentials, or defeat a denial to obtain records. Rate limits and licensing terms also matter operationally even when they do not independently determine CFAA liability. When a download is unavailable, request records from the clerk or repository rather than treating a technical obstacle as permission to circumvent it. Log the alternative route so the exhibit remains reproducible.

> **OPERATOR GATE — A subscription is not a permitted purpose**
> 
> Match restricted data access to the actual assignment and authorized route.
> - Identify the dataset's source and restrictions.
> - Document the applicable purpose before searching.
> - Use an alternative lawful source when the requested access is unavailable.

## Forced-Pooling Docket & Non-Consent Mineral Lease Curve-Jumping  `🏷️ OPERATING_FRAMEWORK`

Track 01 Operator Play forced_pooling_mineral_lease_curve_jumping traces missing mineral owners before state oil and gas commission pooling deadlines. The opportunity starts with a recorded severance: surface ownership and mineral ownership may have followed different chains for decades. Search deeds, mineral reservations, assignments, probate distributions, royalty instruments, and relevant court records using the tract's legal description, not merely a street address or assessor parcel. Compare those instruments with the pooling application, respondent list, notice documents, hearing calendar, and eventual order. A respondent list identifies parties the applicant believes may have interests; it is not a title opinion or an adjudicated heirship schedule. Match names through documented family relationships and trace each transfer until the claimed fractional mineral ownership has a supported chain.

Pooling procedures, election options, notice standards, and consequences of non-consent vary by state and by order. Oklahoma's forced-pooling framework under title 52, section 87.1 is one example, not a nationwide template. Extract the specific election period, payment terms, alternatives, and default consequence from the controlling order and applicable rules. Record the triggering event and actual calendar deadline rather than assuming every state gives the same number of days after a hearing. Locate heirs early enough to obtain documents and independent review, but do not promise that an assignment restarts a deadline or cures defective notice. Verify whether a proposed transaction concerns an unleased mineral interest, a royalty interest, lease rights, or a working interest; their costs, election rights, and exposure are materially different.

For an illustrative tract, assume the decedent owned eight net mineral acres and a verified heir takes one quarter, yielding two net mineral acres. A hypothetical $1,500 per net mineral acre bonus suggests $3,000 gross before deductions, but only if title, lease terms, acreage, and the available election actually support it. An unreleased prior lease, omitted probate, ambiguous reservation, or competing heir can eliminate that expected payment. The curative escrow fallback specifies the required instruments, who obtains them, escrow funding and release conditions, a cure deadline, and what happens if the defects remain. It does not itself extend a commission deadline or establish ownership. Separate any time-sensitive authorized election from the contingent purchase closing. Preserve the docket order and title exceptions together so a buyer cannot mistake deadline urgency for evidence of a transferable interest.

**Title-Defect Trap vs Curative Escrow Fallback**

| Evidence problem | Title-defect trap | Curative escrow fallback |
| --- | --- | --- |
| Surface parcel match | Assume surface owner owns minerals | Trace severance instruments and mineral chain |
| Missing probate link | Pay an alleged heir on surname alone | Require distribution or other adequate curative evidence |
| Outstanding lease | Price a new bonus before checking burdens | Resolve lease status and document releases if required |
| Pooling deadline | Assume escrow pauses the order | Track the order separately; obtain authorized timely action |
| Uncured exception | Release funds against a promised future fix | Apply documented cure conditions or return funds as agreed |

---

> ### “A fast search finds a name; a reproducible source chain establishes what the name means.”

## Action Checklist

- [ ] Choose the source tier for the assertion being tested.
- [ ] Retrieve underlying records rather than relying on indexes.
- [ ] Log stable source IDs and exact page references.
- [ ] Preserve permitted originals and separate derivatives.
- [ ] Document restricted-data purposes and access routes.
- [ ] Trace mineral ownership independently of surface parcels.
- [ ] Calendar pooling elections from controlling orders.
- [ ] Tie escrow release to specified curative evidence.

## Statutory & Primary Authorities

1. 18 U.S.C. section 2721: Motor vehicle personal-information restrictions, permitted purposes, and redisclosure rules. — <https://www.law.cornell.edu/uscode/text/18/2721>
2. 18 U.S.C. section 1030: Unauthorized computer access and related statutory offenses. — <https://www.law.cornell.edu/uscode/text/18/1030>
3. Oklahoma Statutes title 52, section 87.1: Official title compilation containing the pooling framework; check current amendments and the controlling commission order. — <https://oksenate.gov/sites/default/files/2019-12/os52.pdf>

## Sources

1. Skip Tracing for Curative Title: Find Owners Others Can't (Logan Fullmer) — Logan Fullmer @ [00:00:01]: DIY chain of title - parcel and current recorded owner - Retrieve the current vesting deed and copy the full legal description. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=dJ-LTFmMsTg&t=1s>
2. Quick tip: How to do an Online Title Search (San Luis Obispo County Clerk-Recorder) — San Luis Obispo County Clerk-Recorder @ [00:00:01]: DIY chain of title - parcel and current recorded owner - Retrieve the current vesting deed and copy the full legal description. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=EDl18zX1-F0&t=1s>
3. How Ex-FBI Agents Skip Trace Anyone for Real Estate Deals (Logan Fullmer) — Logan Fullmer @ [00:00:01]: DIY chain of title - parcel and current recorded owner - Retrieve the current vesting deed and copy the full legal description. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=GK-4kFznJlA&t=1s>
4. U.S. Probate Records for Genealogy | Midwest Genealogy Center (Mid-Continent Public Library) — Mid-Continent Public Library @ [00:03:28]: Especially when you're doing lineage papers, you get that connection going back. Uh deeds and probate go all the way back to the beginning of the country because they involved assets or m... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=uAcku9kesK4&t=208s>
5. DataTree Hacks: How to Search and Find Property Owners Nationwide (REtipster) — REtipster @ [00:00:01]: Regrid acquisition and import - spatial scope and licensed dataset - Choose state/county coverage and inspect County Coverage Report plus Parcel Schema/Data Dictionary. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=y5XZp-4n_uc&t=1s>
6. Curative Title Research: How She Finds Missing Owners (Logan Fullmer) — Logan Fullmer @ [00:00:01]: DIY chain of title - parcel and current recorded owner - Retrieve the current vesting deed and copy the full legal description. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=zMW-iFWYX9w&t=1s>
7. How to Find Wills and Probate Records for Free and What They Can Tell Us (Ancestry Aimee) — Ancestry Aimee @ [00:13:05]: in the video that i just did on deed research i talked about the fact that ancestry has quite a lot of these land records and some of their records are actually referencing documents that... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=0c5trJYJTyQ&t=785s>
8. Targeted Genealogical Research: Probate Example (Genealogy TV) — Genealogy TV @ [00:10:23]: records. So that's a clue to me that he actually owned land and there may be some deeds to go find. I also found um Mary J. Booth in a uh table of tracks of land um on Graston's Creek, wh... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=10DuXkEoTRA&t=623s>
9. Online Digital Newspaper Sources - James Tanner (BYU Library Family History Center) — BYU Library Family History Center @ [00:00:01]: SSDI and SS-5 - death identity and Social Security clues - Search SSDI variants and compare dates with primary death records. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=1Ptl1u6wRoY&t=1s>
10. Getting Started with Digital Preservation: Fixity Pro (ScottishArchivesTV) — ScottishArchivesTV @ [00:00:01]: Regrid acquisition and import - spatial scope and licensed dataset - Choose state/county coverage and inspect County Coverage Report plus Parcel Schema/Data Dictionary. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=1pRY7lpZ7nA&t=1s>
11. What death records are you missing? (Ancestry Aimee) — Ancestry Aimee @ [00:03:09]: under family search search and cemeteries sometimes maybe even a hundred years ago somebody made a listing of all the people that were buried in a particular Cemetery which maybe now thos... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=6TDebNoMsvQ&t=189s>
12. Digging Deep into Death Records - James Tanner (BYU Library Family History Center) — BYU Library Family History Center @ [00:00:01]: Death-first research - subject identity and estimated death interval - Search death evidence first to bound the life timeline and locate the final jurisdiction. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=70ya-VPbkBc&t=1s>
13. DataTree Hacks: How to Find Portfolio Owners With Multiple Properties (REtipster) — REtipster @ [00:00:01]: Regrid acquisition and import - spatial scope and licensed dataset - Choose state/county coverage and inspect County Coverage Report plus Parcel Schema/Data Dictionary. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=9RvXCiHUzlo&t=1s>
14. Daniel Curran Finders International - Todays Wills & Probate Podcast — Daniel Curran @ [00:19:09]: they're going to change their name um and people can change their name at any time anyway using Deeds so you have to bear that in mind someone might then be more inclined to change their... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=AKvEFJHf5K0&t=1149s>
15. Peeling Back the Layers: Citing Sources from Online Materials, Part 1 (FamilySearch) — FamilySearch @ [00:00:01]: Collateral lines and brickwalls - unresolved parentage or migration - Build a sibling set from censuses, probate distributions and household records. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=DUAbGD8rVzA&t=1s>
