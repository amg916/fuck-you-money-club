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

## 5. Route inbound identity-graph signals into verified postal outreach  `🏷️ OPERATING_FRAMEWORK`

Integrate Track 02 Operator Play identity_graph_pixel_arbitrage as an inbound research channel, not a license to expose anonymous visitors or manufacture permission to email them. Capture high-intent traffic through useful county-specific pages and search advertisements answering queries such as county excess-proceeds lists and unclaimed foreclosure funds. Link the actual custodian, identify the business as an independent service, and explain the public self-claim route alongside the paid service. An identity graph can suggest an address candidate from permitted first-party or licensed matching inputs, but shared devices, household links, and stale identifiers make that result probabilistic. Use a disclosed, authorized matching implementation and record its source, permitted purpose, match date, and uncertainty. Do not send bankruptcy details, surplus balances, identity documents, or raw sensitive search strings to advertising pixels. Keep the keyword campaign and county landing-page identifier separate from the protected claimant file. A visitor seeking information for a relative is not necessarily the former owner. Require a county-record identity link and an independently supported current mailing address before a graph-derived candidate becomes a postcard recipient; leave ambiguous matches unresolved rather than buying additional speculative contacts.

Enforce US-only access for the campaign at the CDN edge before serving the matching script or forwarding collection requests. Apply the country decision to landing pages, pixel endpoints, redirects, and address-resolution APIs; deny non-US and unknown classifications. Trust only the CDN's authenticated country metadata, not a browser-supplied country header, and prevent direct-origin access from bypassing the edge restriction. Ensure cached responses cannot leak a US-only script to excluded traffic, and test US, non-US, unknown-country, and forged-header requests on both page and collection routes. Location inferred from an IP address does not prove residence, identity, or permission; US-only delivery therefore narrows exposure without settling data-use obligations. California Civil Code section 1798.120 provides covered consumers a right to opt out of sale or sharing, and section 1798.135 addresses implementation duties for covered businesses. Evaluate applicability and honor applicable opt-out signals before exporting matching data. Never cold-email unconsented consumer Gmail inboxes from primary domains, and do not evade this rule by cycling secondary domains. Purchased email matches are not subscriptions. The CAN-SPAM Act, 15 U.S.C. section 7704, regulates commercial email practices but does not establish a safe inbox-delivery entitlement; provider restrictions and this channel policy remain distinct from its statutory requirements.

Route eligible resolved homeowner addresses into a next-business-day PostGrid or Lob verification-postcard queue after postal standardization, independent corroboration, deduplication, and suppression checks. Address validation establishes deliverability characteristics, not that a particular person lives there or owns the surplus right. Record the county source, address evidence, chosen vendor, template revision, unique case-and-campaign mailing key, submission time, and returned vendor identifier. Retry a failed submission only after checking whether the vendor already accepted it; use supported idempotency controls to prevent duplicate postcards. Next-day submission is an operating target, not next-day delivery, and weekends, vendor cutoffs, and rejected addresses require explicit queue handling. Use this verbatim postcard copy: 'We are an independent records-research business, not a government office. Public county records may concern a former property owner with your name. You may verify records directly with [county office] at [official website or published phone]. To ask about our optional service, contact [business contact] and reference [opaque code]. If this reached the wrong person or you prefer no further mail, tell us and we will update our records.' Omit the fund amount, foreclosure label, probate status, and sensitive identifiers from the exposed card. The opaque code opens a neutral contact page, never claimant documents. Log returns, wrong-party reports, opt-outs, verified responses, and cost per verified claimant; suppress unsuccessful identities across future exports instead of treating every delivered card as a successful match.

**Naive Cold-Email Spam Trap vs Direct Postcard & Geo-Fenced Search Fallback**

| Forensic check | Naive cold-email spam trap | Direct postcard and geo-fenced search fallback |
| --- | --- | --- |
| Intent | Purchased inbox treated as interest | County-specific inbound query; identity still corroborated |
| Geography | Browser header or ad targeting alone | US-only CDN rules on pages and collection; origin restricted |
| Identity | Graph match declared homeowner | County linkage plus independent current address evidence |
| Channel | Unconsented Gmail blast from primary domain | No cold-email export; eligible address enters postal queue |
| Privacy | Pixel receives claim amount and documents | Minimal matching inputs; applicable opt-outs honored |
| Timing | Instant send interpreted as delivery | Next-business-day vendor submission; delivery tracked separately |
| Evidence | Open rates treated as verified claimants | Vendor receipt, returned mail, and verified responses retained |

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

1. The Most Overlooked Surplus Funds Recovery Business You Can Start With $0 (Overage Acquisition) — Overage Acquisition @ [00:04:09]: To track these individuals from a parcel number, you would need skip tracing tools like True People Search, been verified, and Intellius. If you want to learn more about it, watch the video linked in the description. — Attributed practitioner commentary on skip-tracing stacks, recorder/assessor portals, PACER bankruptcy checks, and right-party contact verification. — <https://www.youtube.com/watch?v=q2gk3WmK5xs&t=249s>
2. How to start a Surplus Funds Recovery Business in 2026 (for beginners) (Money Making Juggernaut) — Money Making Juggernaut @ [00:07:06]: The best option is to use Excess Leads, which is the best software in the game. You can get daily leads across the entire country, both tax sales and mortgage foreclosures, and every lead comes with skip trace phone numbers, DNC compliance, relatives numbers, and emails. — Attributed practitioner commentary on skip-tracing stacks, recorder/assessor portals, PACER bankruptcy checks, and right-party contact verification. — <https://www.youtube.com/watch?v=suJSu-vn6yI&t=426s>
3. Overages & Surplus Fund Debt & Title Research: Not As Easy As It Seems.  Two tips To Help (Nick Fullmer- Overage Syndicate) — Nick Fullmer- Overage Syndicate @ [00:05:23]: Third thing you could do is actually call the county recorder, give them the property address, give them the parcel number, and see if they will do a due diligence search for you. If it's just one case, just one-off case you're looking at, they might do that for you as well. — Attributed practitioner commentary on skip-tracing stacks, recorder/assessor portals, PACER bankruptcy checks, and right-party contact verification. — <https://www.youtube.com/watch?v=KOYBZFn2k7w&t=323s>
4. Skip Tracing for Curative Title: Find Owners Others Can't (Logan Fullmer) — Logan Fullmer @ [00:18:51]: I mean, you could skip trace anybody. We've got people that are doing um What is it? Unclaimed funds, uh debt collection, some property managers that deal with evictions, um just stuff Any It It's skip tracing skip tracing. — Attributed practitioner commentary on skip-tracing stacks, recorder/assessor portals, PACER bankruptcy checks, and right-party contact verification. — <https://www.youtube.com/watch?v=dJ-LTFmMsTg&t=1131s>
5. Surplus Funds Recovery Cold Calling - STEP-BY-STEP SCRIPT (Money Making Juggernaut) — Money Making Juggernaut @ [00:04:10]: Think about your own phone. How many unknown calls do you answer on the first try? So why would your client be any different? One call is not an attempt, but three touches is a real attempt. And don't stop with the client. Your skip trace also gives you a few relatives. — Attributed practitioner commentary on skip-tracing stacks, recorder/assessor portals, PACER bankruptcy checks, and right-party contact verification. — <https://www.youtube.com/watch?v=DMdtmrWAO6c&t=250s>
6. How to Find Surplus Funds Lists (Tax Sales and Foreclosures) (Alfred Taren) — Alfred Taren @ [00:04:14]: From there, the real research starts. Court records, second mortgages, other liens, back taxes, the cost of the sale, figuring out who's actually entitled to what's left, then skip tracing to find a current phone number for the homeowner or the heirs. — Attributed practitioner commentary on skip-tracing stacks, recorder/assessor portals, PACER bankruptcy checks, and right-party contact verification. — <https://www.youtube.com/watch?v=YCb5jYZX_A8&t=254s>
7. Unclaimed Funds: Lead Sourcing Masterclass (Surplus Funds 101) — Surplus Funds 101 @ [00:03:47]: Skip trace those people and see if they have a relationship with the owner. Depending on the skip tracing platform, you can even get somebody's driver's license number and then you can send a sheriff to their property to do a quote unquote welfare checkup. — Attributed practitioner commentary on skip-tracing stacks, recorder/assessor portals, PACER bankruptcy checks, and right-party contact verification. — <https://www.youtube.com/watch?v=h4Qz3EvAAnw&t=227s>
8. Tax Sale Overages Course (Bob Diamond - America's Tax Sale Attorney) — Bob Diamond - America's Tax Sale Attorney @ [00:03:25]: 's left over, like this list that has probably 50 leads on it, $3,341,087. Once you get the list, then what you have to do is learn how to get the contact information for the people. That's a process called skip tracing. — Attributed practitioner commentary on skip-tracing stacks, recorder/assessor portals, PACER bankruptcy checks, and right-party contact verification. — <https://www.youtube.com/watch?v=qGPsbhsEAVQ&t=205s>
9. Cold Calling for Surplus Funds: What Actually Works (Surplus Institute / David Church / Unclaimed Funds) — Surplus Institute / David Church / Unclaimed Funds @ [00:18:21]: Landlines almost never work on any skip tracing service, but the older you get, the more the landline will work. The guy is 76, so he probably does have a couple of land. Um, it's po I'm sorry, let me say that again. It's possible that his landline does work. — Attributed practitioner commentary on skip-tracing stacks, recorder/assessor portals, PACER bankruptcy checks, and right-party contact verification. — <https://www.youtube.com/watch?v=xqpLsq3JVlU&t=1101s>
10. How to Run a Surplus Funds Business with One CRM: Full 2026 Walkthrough (Surplus Funds List) — Surplus Funds List @ [00:04:10]: You can uh also update the status on the client portal so the homeowner can go on your site and search for the case and they will see the detail as to what is the progress on the case without waiting on you um to get them an update. — Attributed practitioner commentary on skip-tracing stacks, recorder/assessor portals, PACER bankruptcy checks, and right-party contact verification. — <https://www.youtube.com/watch?v=lOnYUxDdOdI&t=250s>
11. Top 5 Things Nobody Tells You About the Surplus Funds Recovery Business (Overage Acquisition) — Overage Acquisition @ [00:02:37]: So, always check if a claim has already been filed before. Some counties have online portals where you can search by case number or property address, or you can always make a phone call to the county office and verify. — Attributed practitioner commentary on skip-tracing stacks, recorder/assessor portals, PACER bankruptcy checks, and right-party contact verification. — <https://www.youtube.com/watch?v=bpxSOg1_xbE&t=157s>
12. How To File a Claim - PA Treasury Unclaimed Property Tutorial (PA Treasury Department) — PA Treasury Department @ [00:07:33]: Email topmail patreasury.gov and our unclaimed property staff will be happy to assist you if you'd like to search for unclaimed property in other states visit missingmoney.com thank. — Attributed practitioner commentary on skip-tracing stacks, recorder/assessor portals, PACER bankruptcy checks, and right-party contact verification. — <https://www.youtube.com/watch?v=eRjGqaIOHWI&t=453s>
13. How to Start a Surplus Funds Business in 2026 (Step by Step) (Alfred Taren) — Alfred Taren @ [00:09:18]: Their page says email the court registry to request a listing. And there's a $5 research fee to look up a case by phone. So once you have your list, you find the people, you're gonna skip trace them, look for heirs where the owner has passed and build a short list. — Attributed practitioner commentary on skip-tracing stacks, recorder/assessor portals, PACER bankruptcy checks, and right-party contact verification. — <https://www.youtube.com/watch?v=8-8koApqnYA&t=558s>
14. Curative Title Research: How She Finds Missing Owners (Logan Fullmer) — Logan Fullmer @ [00:04:43]: And when you when a person thinks, I'm going to skip trace someone and say, all right, I'm going to skip trace, I don't know, Aaron Rodgers. You go you put the name in the first field. Aaron first name or last name last name first, whatever. — Attributed practitioner commentary on skip-tracing stacks, recorder/assessor portals, PACER bankruptcy checks, and right-party contact verification. — <https://www.youtube.com/watch?v=zMW-iFWYX9w&t=283s>
15. CA Unclaimed Property - Are you missing out? - Tutorial (Emend The Mass Media Group) — Emend The Mass Media Group @ [00:16:01]: So, you're going to go ahead and select that or probably like push it or something like that. So, you're going to push that option and it's going to take you uh to a search page. — Attributed practitioner commentary on skip-tracing stacks, recorder/assessor portals, PACER bankruptcy checks, and right-party contact verification. — <https://www.youtube.com/watch?v=ijLtjR0tTd8&t=961s>
