# Chapter 01: What Exactly Is Heir Hunting?

*Three adjacent businesses with different claimants, rules and evidence.*

> THE BIG MONEY PLAYBOOKS · THE FUCK YOU MONEY CLUB

## Executive Summary

Heir hunting is evidence work that connects a legally entitled person to an asset or estate, not a universal license to collect abandoned money. Three adjacent lanes share public records but differ in authority: intestate probate research, state custodial unclaimed property, and foreclosure or tax-sale surplus recovery. Choose the lane before calculating a fee or contacting a claimant. This chapter turns public records into a documented research queue, distinguishes kinship from entitlement, and replaces brittle portal scraping with permissioned data access, source provenance, and measurable case qualification.

### Key Metrics

| Metric | Value | Confidence | Source |
| --- | --- | --- | --- |
| Legal lanes | 3 |  |  |
| Qualified yield | 8 / 200 = 4% |  |  |

## Separate the three businesses before accepting a file  `🏷️ STATUTORY_FACT`

Intestate probate heir research asks which people inherit property that passes without an effective testamentary disposition. California Probate Code section 6402 supplies an order of succession for the part of an intestate estate not passing to a surviving spouse under section 6401, or the entire intestate estate when there is no surviving spouse. Start with the death certificate, probate petition, docket, and any will or trust references; a surname match does not establish intestacy. A personal representative may commission genealogy, but the probate court resolves disputed rights and supervises distribution through applicable proceedings. Your deliverable is a sourced family reconstruction and evidentiary packet, not a private declaration that someone owns a percentage of the decedent's assets.

State custodial unclaimed property concerns a holder's transfer of dormant property to a state administrator for the owner's benefit. The claimant may be a living individual, corporation, estate, or successor, so this lane often needs identity and authority documents rather than an extended family tree. California's State Controller administers the state claim process; it does not become the probate court merely because an account owner died. Locate the property identifier, reported owner, former address, reporting holder, and available property description. Then establish the claimant's right to that particular item. An heir who proves kinship may still need estate authority or another permitted succession procedure before the Controller can release funds to the appropriate recipient.

Foreclosure and tax-sale surplus recovery concerns proceeds left after legally prioritized payments, not a dormant bank account waiting in a state database. California Civil Code section 2924k orders distribution of trustee-sale proceeds, including sale expenses, secured obligations, junior interests, and the remaining balance to the trustor or successor as specified. Tax-sale excess proceeds follow a different statutory process; do not transplant the trustee-sale sequence into a tax file. Identify whether the custodian is a trustee, court, county tax collector, or clerk acting in a particular role. Obtain the sale record, proceeds accounting, lien history, and governing claim instructions. The former owner is a lead, not proof that no competing interest has priority.

**Same research skills, different legal destinations**

| Lane | Decision-maker or administrator | Core evidence | Critical distinction |
| --- | --- | --- | --- |
| Intestate probate | Probate court; personal representative | Vital records, family tree, docket | Kinship plus applicable succession law |
| Custodial property | State Controller or equivalent | Property ID, owner identity, authority | Claim to a specific reported asset |
| Sale surplus | Trustee, county official, or court | Sale accounting, title and liens | Priority and timely claim procedure |

## Contracts follow authority, not the investigator's label  `🏷️ OPERATING_FRAMEWORK`

A fee agreement must identify the actual service, authorized client, payment source, and event that earns compensation. An individual heir can engage research concerning their own interest without thereby authorizing expenses against an entire estate. A personal representative's engagement raises a separate question: whether that representative can retain the service on the proposed terms and whether payment requires court review. A state claim assistance contract faces its own timing, disclosure, and compensation rules. Calling all three services heir hunting does not harmonize those rules. Misclassification can produce an unenforceable agreement, an invalid assignment, or a demand against someone who never owed the fee. Classify the asset and authority before choosing contractual language or projecting collections.

Use a lane memorandum as the first work product. Record the asset identifier, decedent or reported owner, current custodian, jurisdiction, procedural posture, prospective claimant, and evidence of signing authority. Keep entitlement and contactability in separate fields: a located relative may have no inheritable share, while a well-supported heir may remain difficult to reach. For a probate matter, distinguish letters appointing the representative from a petition merely requesting appointment. For a corporate property claim, distinguish an officer's current position from authority to act for a dissolved predecessor. For surplus, distinguish the auction price from the custodian's confirmed balance. Each distinction prevents a plausible public record from silently becoming an unsupported contractual assumption.

Consider an illustrative file showing a deceased homeowner, a completed trustee sale, and a state listing for an old utility refund. There are at least two assets, potentially two procedures, and possibly an estate proceeding needed to establish who may act. The same death certificate can support both files, but neither an engagement nor an award automatically transfers between them. Build separate asset records linked to one research subject, assign separate deadlines, and document which custodian receives each packet. If the surplus was already distributed, close that opportunity rather than attaching its stale amount to the utility claim. This asset-level discipline makes case economics intelligible and prevents double-counting recoveries in the sales pipeline.

> **OPERATOR GATE — Name the asset, claimant, and authority**
> 
> Do not quote a recovery percentage from a name match alone.
> - Confirm the legal lane and jurisdiction.
> - Identify the custodian and current balance evidence.
> - Document who can engage the firm and who can receive payment.

## Track 01: Public-Record & API Intelligence  `🏷️ OPERATING_FRAMEWORK`

The public_record_api_intelligence play converts permitted public data into a prioritized evidence queue. Inputs include probate docket indexes, appointment entries, recorder instruments, published surplus lists, state property listings, and official business registry records. Supplement with authorized vital records and source-specific exports where access permits; public visibility does not mean unrestricted bulk access or access to sealed attachments. Preserve the source URL, retrieval date, query parameters, record identifier, and a copy or permitted reference to the underlying document. A docket index describes events but may omit the operative order. Treat index-only findings as leads until the document supports them, and separate verified fields from inferred relationships in the case database.

The four-step workflow is acquire, normalize, corroborate, and route. Acquire from documented APIs, downloads, or records requests at the source's allowed pace. Normalize dates, entity suffixes, addresses, and instrument numbers without deleting raw values. Corroborate each promising match against an independent identifier and the document establishing the asset or authority. Route the result to the correct legal lane with an assigned researcher, next evidence request, and explicit rejection reason when unsuitable. A shared surname and city are weak signals; a matching predecessor corporation number and historical address are stronger, but still require successor evidence. Maintain one canonical asset key so repeated downloads do not inflate the inventory or trigger duplicate claimant outreach.

Measure the queue rather than boasting about scraped rows. Record source coverage against the stated jurisdiction list, document retrieval success, duplicate rate, verified claimant yield, median record age, and labor minutes per qualified file. In an illustrative batch of 200 leads, 40 duplicates and 80 obsolete records leave 80 for review; eight supported cases represent a four percent yield on gross intake, not ten percent on all available opportunities. If acquisition and review cost $640, qualified acquisition cost is $80 before deeper genealogy, outreach, and claim preparation. Track those later costs separately. A rising yield can conceal shrinking source coverage, so report both denominators alongside the case count and avoid treating incomplete downloads as empty jurisdictions.

**SOP — Standard Operating Procedure**

1. Acquire
   - Use permitted feeds or records requests.
   - Save source identifiers, retrieval dates, and access conditions.
2. Normalize
   - Create stable asset and subject keys.
   - Retain raw names and dates beside standardized values.
3. Corroborate
   - Inspect underlying records and independent identifiers.
   - Keep inferred kinship separate from demonstrated entitlement.
4. Route
   - Assign a lane, owner, and next evidence task.
   - Reject stale, duplicated, or unsupported opportunities explicitly.

## Replace portal fragility with a durable evidence queue  `🏷️ OPERATING_FRAMEWORK`

The naive portal-scraping trap begins when an operator equates faster requests with better inventory. HTTP 429 responses and CAPTCHA blocks indicate that the acquisition method has reached an access boundary; retries without a budget can turn one missed update into an entire night's corrupted intake. Do not route around controls with identity rotation or CAPTCHA defeat. Honor documented retry instructions, stop automated access when required, and preserve the last successful snapshot as historical data. Mark freshness explicitly rather than presenting cached records as current balances. Distinguish a transport failure from a genuine zero-result response, and retain response metadata sufficient to explain why a jurisdiction's apparent opportunity count suddenly fell.

The durable fallback is a records-request and cached-queue operating model. Ask the custodian whether a bulk extract, scheduled export, or documented API is available, describing the record fields and date range needed. Use the applicable state public-records process for state or county records; federal FOIA does not govern a county probate office merely because the request concerns public information. Calendar acknowledgment and production milestones under the applicable rules, log fees, and ingest deliveries through the same deduplication path as online records. While waiting, researchers work already acquired cases in priority order, with a fresh custodian check before reliance. Pending requests remain pending inventory, never invented new assets or assumed recoveries.

Close each research cycle with an evidence audit of a small, defined sample. Select both accepted and rejected records, reproduce the match from stored identifiers, and inspect whether the underlying document supports the chosen lane. Count erroneous merges, stale balances, and missing appointment documents separately because each calls for a different repair. An erroneous merge needs entity resolution changes; stale balances need refresh scheduling; missing authority needs a new documentary task. Compare the cost of an official extract with researcher hours lost to unreliable acquisition. The winning operation is not the one collecting the most names. It is the one producing defensible, correctly routed files without letting access failures or speculative family links masquerade as money.

**Forensic acquisition failures and durable alternatives**

| Naive Portal-Scraping Trap | Detection Metric | Durable FOIA/Cached Queue Operator Fallback |
| --- | --- | --- |
| HTTP 429/CAPTCHA blocks | 429 share; blocked sessions; last successful fetch | Respect access limits; request authorized export; work dated cache |
| Zero results treated as zero assets | Response validity; expected pagination; source coverage | Record failed acquisition separately; reconcile official delivery |
| Names merged without asset keys | Duplicate rate; sampled false merges | Retain raw fields and stable IDs; manually resolve ambiguity |
| Old balances sold as current | Record age; custodian-confirmed balance rate | Refresh before reliance; flag historical snapshots |

---

> ### “A name is a lead. An asset, an entitlement chain, and an authorized payer make a case.”

## Action Checklist

- [ ] Classify each asset as probate, custodial property, or sale surplus.
- [ ] Record the decision-maker, custodian, claimant, and signing authority.
- [ ] Retrieve the operative document behind each promising index entry.
- [ ] Run acquire, normalize, corroborate, and route with stable asset keys.
- [ ] Measure qualified yield and cost using explicit denominators.
- [ ] Replace blocked acquisition with permitted exports and dated queues.

## Statutory & Primary Authorities

1. California Probate Code section 6402: Intestate succession for the share not passing to a surviving spouse under section 6401. — <https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6402.&lawCode=PROB>
2. California Civil Code section 2924k: Priority of distribution of trustee-sale proceeds; not the tax-sale excess proceeds procedure. — <https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=2924k.&lawCode=CIV>
3. California Revenue and Taxation Code section 4675: Separate claim framework for tax-sale excess proceeds. — <https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=4675.&lawCode=RTC>

## Sources

1. Unclaimed Funds: How to Get Your Client's Documents in OrderUnclaimed fund Client Document finding (Surplus Institute / David Church / Unclaimed Funds) — Surplus Institute / David Church / Unclaimed Funds @ [00:00:01]: Deceased-owner claim packet - owner death and candidate heirs - Match the owner to the reported name/address using independent records. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=1AMk1-SB5ic&t=1s>
2. Surplus Funds: Owner Died - STILL CLAIM! (SurplusFundsRiches) — SurplusFundsRiches @ [00:05:03]: to her the day before the foreclosure she gets all the Surplus you don't have to worry about probate or estate big deal now here's where it gets wacky let's talk about if the D doesn't li... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=1N1Z99kUvRw&t=303s>
3. Declaration Under Probate Code 13101 Tutorial (California State Controller's Office) — California State Controller's Office @ [00:00:35]: no Probate was required for an estate, or that the Administrator or Personal Representative of the estate has provided consent in writing stating the claimant is entitled to the Unclaimed... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=1ahhduhMdd0&t=35s>
4. TGP 19 - Eileen O'Duill - Probate Research (The Genealogy Professional Podcast) — The Genealogy Professional Podcast @ [00:01:11]: years I'm the probate genealogist which means my job is to assist solicitors lawyers and err locating firms to identify rightful heirs in mostly intestate estates my task is to find the n... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=7v_UB7hKgKg&t=71s>
5. Probate Process for Real Estate Agents & Investors: 12 Steps From Filing to Sale (Probate Mastery) — Probate Mastery @ [00:00:01]: Testate and intestate routing - death, domicile, assets and possible will - Locate the original will, codicils and any admission order; a found will is not necessarily an admitted will. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=7xCfSyqYEys&t=1s>
6. Sub-to strategy for probate investing | Probate foreclosures | Probate real estate marketing tips (Probate Mastery) — Probate Mastery @ [00:00:01]: Testate and intestate routing - death, domicile, assets and possible will - Locate the original will, codicils and any admission order; a found will is not necessarily an admitted will. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=AAF69oF79DU&t=1s>
7. Heirs' Property 101 (Center for Community Progress) — Center for Community Progress @ [00:07:16]: uh that has passed to an heir. Um either there was a will or some kind of estate plan, but there was further action needed to record or take title to a deed and that was never done or if... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=DG4Uhckk-fU&t=436s>
8. Florida Probate Explained: What Happens When Someone Dies Owning Real Estate? (Courtney Fricke) — Courtney Fricke @ [00:00:01]: Ten-heir fractional consolidation - proved owners and rational shares - Build a tenancy-in-common cap table and verify shares sum to one. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=Dutmzc9gb30&t=1s>
9. $200,000 California Foreclosure Heir Claim Case Study (Money Making Juggernaut) — Money Making Juggernaut @ [00:00:01]: Unclaimed property versus surplus - candidate asset - Classify state-held intangible property separately from county tax-sale and mortgage-sale proceeds. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=MiiGrCZZAZk&t=1s>
10. Hyperlocal real estate marketing at probate court & How to buy a probate property as a sub2 deal (Probate Mastery) — Probate Mastery @ [00:00:01]: Testate and intestate routing - death, domicile, assets and possible will - Locate the original will, codicils and any admission order; a found will is not necessarily an admitted will. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=Odf2VQ3AZsg&t=1s>
11. How to Find Heirs for a Florida Probate Property (Courtney Fricke) — Courtney Fricke @ [00:00:25]: with Florida real estate attorney who focuses on probate. His name is Al Nicoleti. Maybe you've heard of him. Al does a great job talking about all things probate and even the curative wo... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=RmtbOq_vtuU&t=25s>
12. Probate Property Headed to Foreclosure Auction... Is It Worth Pursuing? (Probate Mastery) — Probate Mastery @ [00:00:01]: Unclaimed property versus surplus - candidate asset - Classify state-held intangible property separately from county tax-sale and mortgage-sale proceeds. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=T2gvkByDlFU&t=1s>
13. Probate Data and Property Lookups: Live Real Estate Coaching with Probate Mastery — Probate Mastery @ [00:00:01]: Testate and intestate routing - death, domicile, assets and possible will - Locate the original will, codicils and any admission order; a found will is not necessarily an admitted will. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=TA4mtGUeNo8&t=1s>
14. What's in a Probate Record and How to Use it for Genealogical Research- James Tanner (10 Sep 2023) (BYU Library Family History Center) — BYU Library Family History Center @ [00:22:04]: property and they would have what was called a deed of distribution which would then take the property the farm out of the estate and then The Heirs would divide up the proceeds so there'... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=TBB8OPPFSsM&t=1324s>
15. How To Become An Unclaimed Property Investigator (Surplus Funds 101) — Surplus Funds 101 @ [00:00:01]: Deceased-owner claim packet - owner death and candidate heirs - Match the owner to the reported name/address using independent records. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=TTMtgtc31k4&t=1s>
