# Chapter 08: Tools, Public Databases & Skip-Tracing Investigative Stack

*County recorder indexes, Regrid/DataTree parcel GIS, PACER bankruptcy checks, and waterfall skip tracing.*

> THE BIG MONEY PLAYBOOKS · THE FUCK YOU MONEY CLUB

## Executive Summary

Build the investigative stack around record provenance rather than the number of subscriptions. County indexes establish recorded transactions, assessor rolls identify parcels and mailing addresses, commercial platforms accelerate matching, and court dockets expose authority problems before outreach. A controlled skip-tracing waterfall corroborates identity without treating purchased contact data as proof. The same dated tax-roll pipeline can support a separate property-tax appeal service, provided comparable evidence, assessment dates, and local appeal rules drive the work. This chapter explains which source answers each question and where a convenient lookup becomes a misleading shortcut.

### Key Metrics

| Metric | Value | Confidence | Source |
| --- | --- | --- | --- |
| Contact corroboration | 2+ independent sources |  |  |
| Illustrative assessment reduction | $75,000 |  |  |
| Illustrative appeal fee | $450 |  |  |

## 1. Build a parcel-first public-record spine  `🏷️ OPERATING_FRAMEWORK`

Begin with a dated county tax-roll export and a separate surplus ledger, preserving each source's retrieval date, assessment year, field definitions, and update cadence. Normalize assessor parcel numbers without losing leading zeros, suffixes, or the county identifier; an APN is not globally unique. Keep situs address separate from owner mailing address, and preserve original owner text before creating normalized matching fields. Join sale cases to parcels using both identifiers and legal descriptions, flagging splits, combinations, and condominium units for review. A tax-roll owner can lag a recorded transfer, so a successful join is a research lead rather than proof of entitlement. Maintain one internal case identifier linking the raw row, sale record, recorder evidence, and later claimant research.

County Recorder Grantor/Grantee indexes answer who recorded which instrument and when. Search the former owner's exact name, common variants, trust capacities, and entity names in both directions, then obtain the deed, mortgage, assignment, release, or notice image associated with each relevant index entry. Document book and page or instrument number so another researcher can reproduce the finding. The Tax Assessor APN roll contributes land use, assessed values, tax districts, exemptions, building attributes, and mailing data, but those fields do not establish clean title or current contactability. When the recorder and assessor disagree, retain both versions and explain the effective dates. Do not silently overwrite a deed-derived owner with a more recent commercial enrichment result that merely repeats the assessor feed.

Regrid can accelerate parcel geometry, address matching, and geographic review; DataTree can help locate property records, vesting information, and document products where its coverage supports the county. Treat both as discovery and retrieval layers whose specific fields, permissions, and update dates must be checked. A boundary drawn on a map is not a survey, and a cached owner name is not a certified vesting finding. Use a source register to distinguish original county evidence from vendor transformations and manually corrected values. For bulk work, use available official exports, documented APIs, or licensed downloads within their terms, and retain the original record identifier beside the normalized one. This makes a parcel mismatch repairable without rebuilding the entire investigative file from memory.

**Source directory: assign each tool a bounded job**

| Source | Primary use | Required cross-check |
| --- | --- | --- |
| Recorder grantor/grantee index | Find recorded instruments | Read complete document images |
| Assessor APN roll | Parcel attributes and mailing leads | Check vintage and deed ownership |
| Regrid | Parcel matching and geographic context | Confirm county identifiers and geometry limits |
| DataTree | Property and document discovery | Verify coverage and original records |
| PACER | Bankruptcy proceedings and orders | Read docket and authority documents |
| Secretary of State | Entity status and filed officials | Verify current authority separately |

## 2. Search bankruptcy and entity authority before outreach  `🏷️ OPERATING_FRAMEWORK`

Run a bankruptcy search before contacting a former owner about an available fund. Use the PACER Case Locator and appropriate bankruptcy court docket, searching name variants and corroborating matches with lawful identifiers such as addresses, filing jurisdiction, or entity details. A common name match is not enough to label someone a debtor. Capture the petition date, chapter, case status, trustee, debtor counsel, and docket entries relevant to the property or proceeds. For an open Chapter 7 case, identify the trustee and examine schedules, exemption claims, sale orders, abandonment notices, and any order addressing surplus. For Chapter 13, identify the trustee and read the plan and confirmation order, because property-of-estate and vesting treatment can depend on the plan, statute, and controlling decisions.

Section 541 of title 11 broadly defines bankruptcy estate property, including many interests held at commencement and certain proceeds, but it does not tell a researcher that every post-sale dollar automatically belongs to the debtor or trustee. Analyze when the ownership interest and surplus right arose, whether exemptions apply, and whether property was properly abandoned or otherwise dealt with by order. A discharge is not proof that an unadministered asset has returned to the debtor; an unscheduled asset can remain estate property after closing. Record uncertainty and direct authority questions to the appropriate representative or counsel before solicitation or an agreement concerning the asset. Separate locating a person from advising them to transfer or collect property that may be controlled by the bankruptcy estate.

For entity-owned parcels, search Secretary of State filings in the formation jurisdiction and any relevant foreign registration jurisdiction. Officer, manager, registered-agent, annual-report, merger, and dissolution records help identify a current point of contact, but a registered agent's service address is not necessarily an operational office or authority to sign a recovery agreement. Cross-check the entity number, exact name, historical names, and filing dates against the deed and bankruptcy results. Where public filings omit members or use outdated officials, request current authority documents rather than guessing. Save a short authority memorandum naming the apparent claimant, evidence supporting that conclusion, unresolved questions, and the next document required. This prevents the skip-tracing team from pursuing a former employee while the actual entity is in receivership or bankruptcy.

> **OPERATOR GATE — Find the authorized recipient before outreach**
> 
> A matched phone number does not resolve bankruptcy ownership, entity authority, or probate succession.
> - Corroborate debtor identity.
> - Identify open Chapter 7 or 13 representatives.
> - Read relevant orders rather than relying on case status alone.

## 3. Operate a corroborated skip-tracing waterfall  `🏷️ OPERATING_FRAMEWORK`

Start the waterfall with low-cost public evidence: deed mailing addresses, assessor correspondence addresses, filed court contacts, entity filings, and public obituary information. An obituary may connect a deceased owner to relatives or reveal a changed surname, but it does not establish heirship or authorize contacting every person listed. Compare address histories by date and distinguish residence, business, mailing service, and care-facility addresses. Use forwarding information only through authorized postal services or lawfully obtained records; a return-mail annotation is a lead, not a license to obtain restricted postal data. Document the source and date of each candidate address, and keep a deceased indicator separate from a confirmed death record. This preserves useful leads without letting an inference overwrite verified identity evidence.

Next use a licensed people-search or skip-tracing product under a documented permissible purpose, then corroborate the result against at least one genuinely independent source. Wireless numbers, landlines, household members, and relatives should each carry a source, observed date, and confidence reason. Two vendors selling the same underlying telephone feed are one evidentiary lineage, not two independent confirmations. A shared surname and nearby address are weak support for a recycled mobile number; a consistent historical address chain plus a separate current public filing is stronger. Rank contacts by recency and agreement, set aside contradictory records, and record wrong-party responses promptly. For relatives, use a limited locating inquiry without disclosing the surplus amount or sensitive financial circumstances, and do not imply that the relative has any claim to the money.

Before outreach, review the intended contact channel against applicable calling, texting, do-not-call, and professional solicitation rules. A vendor's verified label does not supply consent or establish that an automated dialing campaign is permitted. Use a neutral first message identifying the business and inviting the intended recipient to verify the matter through the official custodian. Do not publish sensitive identifiers or attach probate and bankruptcy documents to an unverified contact. Confirm identity through proportionate evidence before discussing the claim in detail, then move documents into a restricted case file. Track returned mail, wrong numbers, refusals, and contact preferences in a suppression record shared across the team. This turns the waterfall into a controlled investigation rather than repeated outreach to every purchased contact associated with a surname.

**SOP — Standard Operating Procedure**

1. Collect public leads
   - Create dated address and identity candidates.
   - Use county records, entity filings, obituaries, and authorized forwarding evidence.
2. Enrich selectively
   - Query a licensed source for the documented purpose.
   - Purchase only fields needed for this case and retain source lineage.
3. Corroborate independently
   - Compare two or more independent sources.
   - Resolve conflicting addresses and recycled phone indications before ranking contacts.
4. Contact and correct
   - Use an appropriate channel and verify the recipient.
   - Suppress wrong parties and refusals; record evidence without exposing financial details.

## 4. Respect data boundaries and reuse the roll for assessment appeals  `🏷️ OPERATING_FRAMEWORK`

The Driver's Privacy Protection Act, 18 U.S.C. section 2721, limits disclosure and use of personal information from motor vehicle records to specified exceptions. Ordinary surplus prospecting is not automatically one of them, and a business identity does not create blanket access. Gramm-Leach-Bliley Act restrictions and its prohibition on obtaining financial customer information through false pretenses likewise do not disappear because a vendor sells a search box. Require the actual source, applicable purpose, and contractual permission for restricted datasets; omit them where the purpose is unsupported. The Computer Fraud and Abuse Act, 18 U.S.C. section 1030, addresses unauthorized computer access and related conduct. Use authorized credentials and permitted interfaces without bypassing access controls. Public availability, contractual permission, and statutory permitted use are distinct questions that deserve separate records.

Reuse the same versioned county tax-roll pipeline for Track 01 Operator Play property_tax_assessment_appeal_contingency, Automated Commercial/Residential Property-Tax Appeal Arbitrage. This is an adjacent service for authorized owners, not a reason to represent former owners after they have lost the property. Screen assessed values against independently supported market values or uniformity measures allowed locally, using the correct valuation date and assessment ratio. Segment residential properties by neighborhood, size, age, condition, and sale validity; segment commercial properties by use, occupancy, income evidence, and capitalization assumptions where relevant. Automation can rank anomalies and assemble comparable candidates, but someone must inspect comparability, exemptions, equalization factors, and filing deadlines. Maintain separate engagements and permissions for appeals and surplus recovery even when both originate from one parcel record.

The Valuation-Rejection Trap is filing an appeal supported by attractive but irrelevant sales, such as renovated houses outside the assessment neighborhood or commercial transfers with unusual financing. The Comparable-Equity Ratio Fallback is a documented uniformity argument only where that appeal basis is recognized: use similar properties, explain exclusions, calculate consistent assessment-to-market ratios, and reconcile material differences. Suppose the subject's supported market value is $1,000,000, its assessment is $300,000, and a valid comparable analysis supports a 22.5% assessment ratio. The modeled target is $225,000, a $75,000 reduction. At an effective 2.4% tax rate on the assessment reduction, annual savings would be $1,800; a permitted 25% realized-savings fee would be $450. Check caps, exemptions, tax-rate mechanics, and actual bills before invoicing, and revalidate annually rather than assuming an automatic recurring award.

**Forensic appeal comparison: evidence determines the available argument**

| Issue | Valuation-Rejection Trap | Comparable-Equity Ratio Fallback |
| --- | --- | --- |
| Comparable set | Cherry-picked cheap or dissimilar sales | Matched cohort with documented exclusions |
| Measurement date | Current listing prices replace statutory valuation | Evidence aligned to the assessment date |
| Theory | Low price asserted without a recognized appeal basis | Uniformity analysis where locally available |
| Calculation | Assessment reduction mistaken for tax savings | $75,000 x 2.4% = $1,800 modeled savings |
| Fee | Invoice projected multi-year benefits immediately | Apply permitted terms to verified realized savings |

---

> ### “Buy speed from tools; take proof from records.”

## Action Checklist

- [ ] Preserve raw county exports and normalize APNs without losing identifiers.
- [ ] Verify vendor findings against recorder images and dated assessor records.
- [ ] Check bankruptcy identity, trustees, plans, and relevant orders before outreach.
- [ ] Confirm entity representatives through current authority evidence.
- [ ] Corroborate contacts across independent source lineages and suppress wrong parties.
- [ ] Document permissible use and avoid restricted data without a supported purpose.
- [ ] Separate assessment appeal engagements and invoice only under verified fee terms.

## Statutory & Primary Authorities

1. 18 U.S.C. section 2721: Restrictions and enumerated permitted uses for motor vehicle record personal information. — <https://www.law.cornell.edu/uscode/text/18/2721>
2. 11 U.S.C. section 541: Defines bankruptcy estate property relevant to surplus entitlement and proceeds. — <https://www.law.cornell.edu/uscode/text/11/541>
3. 11 U.S.C. section 554: Abandonment rules and treatment of property not administered or abandoned. — <https://www.law.cornell.edu/uscode/text/11/554>
4. 15 U.S.C. section 6802: Financial institution disclosure restrictions and exceptions for nonpublic personal information. — <https://www.law.cornell.edu/uscode/text/15/6802>
5. 15 U.S.C. section 6821: Prohibits obtaining financial institution customer information through false pretenses. — <https://www.law.cornell.edu/uscode/text/15/6821>
6. 18 U.S.C. section 1030: Computer access offenses relevant to unauthorized database access and access-control circumvention. — <https://www.law.cornell.edu/uscode/text/18/1030>

## Sources

1. Find More Wills and Probate Records for Using Both Ancestry and FamilySearch Together @ [00:12:02]: between especially you can pull together probably a whole major probate package between ancestry and family search you may even be able to continue to do more searching on family search to pull this in so I can download this whole thing I can include the image with highlights without out highlights don't include the record image at all but I would include the transcri script and of course always always please include the source — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=zIOhXZZxDDM&t=722s>
2. How To Find family members of a deceased person! @ [00:00:19]: D on it which shows that they're deceased. Here's what I do and I've had some real success in doing this. So, I'm going to go over about a five-step system with you that I do. First of all, when I run the skip tracing, the red D means that they're deceased. The first thing I do is I try the numbers on there just to see if a family member has kept the numbers. I've had numerous times — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=eiQ53kxE6ZA&t=19s>
3. Unclaimed Funds: Lead Sourcing Masterclass @ [00:07:43]: using both free and paid services to locate the current information for the claimants enhancing your chances of successful contact. Okay. Now remember you always get what you pay for skip tracing. Okay. Now, you can get it done for free, but you are going to get free content back. Okay? I skip racing is something I never go cheap with at all. Okay? So, you're going to pay for what you get. But you guys, that's a good — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=h4Qz3EvAAnw&t=463s>
4. DataTree Hacks: Find Full Legal Descriptions and Title Vesting Information @ [00:06:56]: go on any future deed, getting transferred to anybody else. And it also shows us how they were holding title together. This is another very important thing that might not be evident without doing an actual title search, to see how it was written on the most recent deed. And speaking of that title search, there's actually a separate video I have on how to do a title search through DataTree. It's actually pretty easy, but in this case with this particular re — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=aUiod-Jy68U&t=416s>
5. DataTree Hacks: How to Search and Find Property Owners Nationwide @ [00:00:33]: You don't have a parcel number. You don't have anything else, just a name. Preferably you know what state and county that person or busines is in but even if you don't have that, you still can most likely find them in DataTree. All you got to do is go up here. You want to make sure this dropdown thing is set to owner. And in this case, I'm going to pretend that I do know the state and the county. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=y5XZp-4n_uc&t=33s>
6. Troubleshooting Data Import - Regrid Property App (Web) @ [00:04:36]: match using a parcel id so i want to change that and re-run this matching process and see if changing the partial number will help so i'll click parcel number and then for these other fields i'm actually just going to select none just to make sure that we're truly matching on the parcel number again just one variable at a time okay so now that we've rerun this on parcel number we see that the match rate — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=VAtPDJ1KDjw&t=276s>
7. Quick Start - The Regrid Property App (Web) @ [00:04:07]: of segment of the parcel uh we also have a bunch of things like elevation Contours that you can turn on if you're interested in those types of things under here that's uh pretty much the quick rundown uh remember you can always get back to your dashboard if you'd like uh from the top left uh you can also have a quick link to your billing there um you can sign in and out from here if you're — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=1Wm_NPEagT8&t=247s>
8. DataTree Hacks: TaxSource Reports and Property Tax Verification @ [00:04:14]: when you click on advanced search. And one thing that DataTree allows you to used as a filtering option is right down here under assessor information where it says delinquent, and you can click yes. And the idea behind this is if you click yes, there, it's only supposed to include properties and property owners that are currently delinquent on their taxes, or at least that's in theory, what it's trying to do. However, there's one issue with this — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=2ThZ61aal9k&t=254s>
9. Feature Service Product Demo (Regrid) — Regrid @ [00:00:32]: our premium parcel data into arcgis online you can do the same to configure web apps hosted on agol the first and key step is to use our token and url to link the feature service to the arcgis online environment so to do — Matched corpus commentary on surplus funds, lien priority, skip tracing, or claim execution; verify against local statute. — <https://www.youtube.com/watch?v=X-_cLY3_96Y&t=32s>
10. Regrid Parcel Data - Overview & Coverage — Regrid @ [00:23:29]: we're sharing with you will have boundary data on it so that's one of our core requirements here is anything that's coming through in any of these formats we're going to have boundaries for it for the ownership percent t — Matched corpus commentary on surplus funds, lien priority, skip tracing, or claim execution; verify against local statute. — <https://www.youtube.com/watch?v=EToN9mWFZWc&t=1409s>
11. Skip Tracing for Curative Title: Find Owners Others Can't (Logan Fullmer) — Logan Fullmer @ [00:53:01]: it?" "13 months." Man, I hope you're doing something else to keep your bills paid along the way. >> Yeah. No, exactly. I mean, I don't Yeah, I don't think the number of heirs or that plaque that you get or credibility yo — Matched corpus commentary on surplus funds, lien priority, skip tracing, or claim execution; verify against local statute. — <https://www.youtube.com/watch?v=dJ-LTFmMsTg&t=3181s>
12. Watch our Demo on How to Claim Your Ohio Unclaimed Funds (ohiocommerce) — ohiocommerce @ [00:01:04]: a moment to think about that. You or someone you know probably has lost or forgotten money. So today I'm going to demonstrate our new system and show you how to go to our website, claim your funds, search for your proper — Matched corpus commentary on surplus funds, lien priority, skip tracing, or claim execution; verify against local statute. — <https://www.youtube.com/watch?v=o1cc3hUtIv4&t=64s>
13. DelcoPA ROW | Searching for Probated Estates Online (Rachel Ezzell Berry) — Rachel Ezzell Berry @ [00:03:45]: to a screen with search results or you'll receive a message in red font that no documents were found that matched the specified criteria this could be for more than one reason it could in fact be that we don't have any d — Matched corpus commentary on surplus funds, lien priority, skip tracing, or claim execution; verify against local statute. — <https://www.youtube.com/watch?v=hpvnOFjxwaM&t=225s>
14. Quick Start Regrid's Interactive API Sandbox Guide — Regrid @ [00:05:11]: token here I'm going to remove the previous token but I'm going to go ahead and paste our token that we created just before this we're gonna I'm gonna enter that here it then goes and adds our token to the snippet um we' — Matched corpus commentary on surplus funds, lien priority, skip tracing, or claim execution; verify against local statute. — <https://www.youtube.com/watch?v=RVakKAvFa_M&t=311s>
15. Regrid Mapping Platform - Filter Data — Regrid @ [00:03:42]: attributes that you're trying to filter on by clicking the little x to the left of their criteria in the box — Matched corpus commentary on surplus funds, lien priority, skip tracing, or claim execution; verify against local statute. — <https://www.youtube.com/watch?v=cKYlwRY3aVw&t=222s>
16. Finding Your Ancestors' Descendants - James Tanner (26 Feb 2023) @ [00:00:00]: Collateral lines and brickwalls — unresolved parentage or migration — Build a sibling set from censuses, probate distributions and household records.|Track witnesses, neighbors, sponsors and executors as an associates cluster.|Search each sibling in the destination jurisdiction and compare origin locations.|Test the proposed relationship against contradictory ages, occupations and simultaneous residences.|Write competing hypotheses and the next record that — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=9Q4qYeK5DTg&t=0s>
17. What Do I Enter Into My Family Tree? Resolving Conflicting Evidence | Ancestry @ [00:00:00]: Collateral lines and brickwalls — unresolved parentage or migration — Build a sibling set from censuses, probate distributions and household records.|Track witnesses, neighbors, sponsors and executors as an associates cluster.|Search each sibling in the destination jurisdiction and compare origin locations.|Test the proposed relationship against contradictory ages, occupations and simultaneous residences.|Write competing hypotheses and the next record that — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=ElrY5ALsx1Y&t=0s>
18. When Paper Trails Meet DNA: The Full Conversation with Professor Turi King and Neil Fraser @ [00:00:00]: Collateral lines and brickwalls — unresolved parentage or migration — Build a sibling set from censuses, probate distributions and household records.|Track witnesses, neighbors, sponsors and executors as an associates cluster.|Search each sibling in the destination jurisdiction and compare origin locations.|Test the proposed relationship against contradictory ages, occupations and simultaneous residences.|Write competing hypotheses and the next record that — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=LZWYe4jFvZM&t=0s>
