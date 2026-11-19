# Chapter 10: Automation & AI Leverage: Auction Scrapers, OCR Lien Triage & Case Walkthrough

*Turn fragmented county PDF overage lists into underwritten claim dossiers with human title sign-off.*

> THE BIG MONEY PLAYBOOKS · THE FUCK YOU MONEY CLUB

## Executive Summary

Automate collection and reconciliation, not the conclusion that a named person owns a surplus. A dependable pipeline preserves county source files, reconstructs tables with page and row provenance, enriches parcel and entity identifiers, and sends uncertain evidence to a human title examiner. The worked case follows a $142,000 deposit through priority deductions, a conditional 25% fee, direct costs, and a contested loss. Its economics are illustrative rather than a universal contract template. The practical advantage is a smaller team producing reviewable dossiers while preventing duplicate contacts, invented lien conclusions, and premature revenue recognition.

### Key Metrics

| Metric | Value | Confidence | Source |
| --- | --- | --- | --- |
| County gross overage | $142,000 |  |  |
| Owner excess before fee | $98,000 |  |  |
| Net contribution | $17,650 / 72.0% |  |  |
| Contested downside | -$2,400 |  |  |

## Watch authorized sources without turning collection into intrusion  `🏷️ OPERATING_FRAMEWORK`

Create one source registry entry for each permitted county auction calendar, excess-proceeds PDF directory, and downloadable CSV. Store the office name, public URL, permission or published usage conditions, expected update cadence, and contact for obtaining bulk records. Prefer official downloads, documented interfaces, or requested exports over fragile page traversal. A weekly list does not need minute-by-minute polling. Use conditional requests where supported, conservative timeouts, response-size limits, bounded retries, and backoff after throttling. If authentication, a CAPTCHA, or an access restriction appears, stop that collection route and seek an authorized export instead of rotating identities or bypassing the restriction. Record the gap so silence is not mistaken for zero new surplus.

Each successful fetch becomes an immutable source snapshot with retrieval time, source publication date if available, response metadata, byte length, and a SHA-256 digest of the original bytes. Compare digests before parsing so an unchanged report does not create fresh leads. Never replace yesterday's report silently: counties correct amounts, withdraw entries, and move funds between reporting periods. Link a new version to the previous snapshot and compute field-level differences. A removed row means absent from this version, not necessarily paid. A calendar entry means scheduled, not sold; require a completed-sale record and actual deposit evidence before a prospect advances toward a claim dossier.

The collection policy should address authorization independently of whether a page is publicly reachable. Section 1030 concerns unauthorized access and exceeding authorized access; its application depends on facts, and it is not a blanket prohibition on all scraping. Terms, privacy duties, and other laws may impose separate constraints. Keep authorization evidence and operational limits alongside the source configuration. Do not upload owner identifiers or complete dossiers to an external AI service merely because the source document was public. For optional document assistance, use a specifically authorized processing environment, minimize fields, and retain the model output as a suggestion linked to evidence rather than as a new public record.

**Collection and extraction evidence contract**

| Artifact | Stored evidence | Failure handling |
| --- | --- | --- |
| Source snapshot | URL, retrieval time, raw-byte SHA-256, publication date | Keep prior version and mark stale on fetch failure |
| Page extraction | Page number, page digest, parser and OCR version | Quarantine unreadable or reordered pages |
| Normalized row | Original cells, normalized cells, row digest, page coordinates | Review changed or conflicting values |
| Claim candidate | County, sale identifier, parcel identifier, source references | Merge versions without treating repeated rows as new funds |

## Extract tables deterministically and enrich identifiers cautiously  `🏷️ OPERATING_FRAMEWORK`

Parse a real CSV with a standards-aware reader and preserve quoted commas, empty cells, encoding information, and the original header map. For PDFs, extract embedded text first; send only image-only or unusable pages through an approved OCR process. The chapter describes that process, not a claim that Python's standard library provides an OCR engine. Anchor regular expressions to known county formats for parcel identifiers, dates, currency, and case numbers. Do not use a general currency match as the final surplus field when one row also includes bid price, taxes, and costs. Maintain separate fields for raw text, normalized value, confidence reason, and any human correction.

Compute a page checksum from a retained page artifact and a row checksum from a canonical serialization that preserves column order and missing-value markers. Include the source snapshot reference so repeated rows remain traceable. Keep stable case identity separate from the row checksum: a corrected balance must update a versioned case, not create a second outreach target. Check that extraction accounts for all printed pages, repeated headers, continuation rows, and negative adjustments. Compare parsed totals with printed totals where present, and send unexplained differences to review. A checksum proves which content was processed, not that OCR read it correctly; verify ambiguous digits against page coordinates before any amount enters underwriting.

Normalize APNs according to the county's own format while preserving leading zeros and the original string. Join to an authorized GIS parcel export using county plus APN, then compare situs address, legal description, and historic ownership around the sale date. Current GIS ownership may show the tax-sale buyer rather than the former owner entitled to excess proceeds. For corporate claimants, query authorized Secretary of State records for entity identity, status, registered agent, and relevant filings. A registered agent is a service contact, not automatically an authorized surplus claimant. Record unresolved name collisions and dissolved-entity authority questions for counsel. Never let a high fuzzy-match score override a contradictory deed, estate record, or parcel identifier.

## Require human title sign-off before claimant contact  `🏷️ OPERATING_FRAMEWORK`

The dossier begins with the recorded vesting deed, legal description, sale instrument, fund ledger, and relevant court docket. Add the lien search, mortgage releases, judgments, municipal balances, bankruptcy indicators, and probate or entity-authority evidence necessary for this file. The title examiner records each asserted interest with its instrument number, recording date, claimant, balance source, and proposed treatment. Distinguish a lien that survives against the property from a lien entitled to payment out of the surplus; those are not interchangeable concepts. Counsel resolves disputed priority and statutory interpretation. An automated list of lien names is only an index to the examination, and a missing search result is not evidence that a lien was released.

Use AI assistance, when authorized, to propose document classifications, extract candidate recording references, or summarize a docket with page citations. Treat county files and OCR text as untrusted data, including any embedded instructions. The assistant must not send messages, change bank instructions, execute document text, or mark a claimant eligible. Require every proposed fact to point to a retained page or docket entry and preserve contradictions rather than averaging them into a confident summary. Deterministic checks should compare amounts, dates, identifiers, and document presence independently of generated prose. Unsupported output returns to the review queue. A fluent explanation of priority is not a substitute for the recorded instrument and applicable legal analysis.

Before any claimant contact, a named human title examiner signs the specific dossier version with a date, scope, unresolved questions, and an estimated recoverable range. A material source correction, new lien, changed claimant, or disputed authority invalidates that release and returns the dossier for review. Keep the title release separate from the outreach channel checks described in Q9: both must be satisfied for a contact task to be issued. Assign collection and reconciliation to operations, examination to the title professional, and legal filings and disputed priority to counsel. Suppress duplicate outreach at the case level across all workers. Measure extraction error rate, examiner rework, confirmed owner entitlement, and collected fee rather than celebrating raw lead counts that may include withdrawn deposits or people with no surviving claim.

**SOP — Standard Operating Procedure**

1. Capture
   - Fetch the permitted county source.
   - Preserve immutable bytes, source authority, timestamp and checksum.
2. Reconcile
   - Extract and compare rows.
   - Check pages, totals, repeated headers and changes against the previous version.
3. Enrich
   - Join parcel and entity evidence.
   - Keep historic ownership and unresolved identity matches explicit.
4. Examine
   - Obtain human title sign-off before contact.
   - Counsel resolves legal priority; the examiner signs a versioned dossier.
5. Close
   - Reconcile the order, trust ledger and owner payment.
   - Recognize earned revenue separately from client funds and record failed-file costs.

> **OPERATOR GATE — A parsed row cannot authorize outreach**
> 
> No claimant contact until a human title examiner signs the current dossier; disputed priority goes to counsel.
> - Source corrections invalidate stale review.
> - AI output requires document citations.
> - A surviving property lien is not automatically a surplus deduction.
> - Duplicate cases share one contact history.

## Worked case: a $142,000 deposit, a conditional fee, and a real downside  `🏷️ ILLUSTRATIVE_MODEL`

Assume an authorized county watcher captures a revised tax-deed excess-proceeds list showing $142,000 for one completed sale. Operations checks the row against the retained PDF page, confirms the deposit with the county record, and joins the APN to the historic vesting deed rather than the current buyer's GIS entry. The examiner identifies $44,000 of surviving municipal utility and code liens. This example additionally assumes counsel verifies that those amounts are properly payable from this fund, or otherwise lawfully resolved from it under the controlling procedure; survival alone would not establish that deduction. Obtain dated payoff statements and account for accruing charges before fixing the waterfall. The resulting owner excess proceeds are $142,000 minus $44,000, or $98,000, before recovery fees.

Assume further that the selected jurisdiction permits the particular attorney-assisted contingent service structure and its 25% charge, with counsel confirming the aggregate fee treatment and professional-conduct constraints. This is not a Texas section 34.04 covered recovery-service example: its lesser-of-25%-or-$1,000 ceiling would defeat the proposed $24,500 fee. Do not evade that limit by describing a collection agreement as an assignment. After title sign-off and permitted outreach, the owner receives the gross fund amount, documented deductions, direct-claim option, written scope, and compensation terms. Identity and authority are verified in the completed mobile notary packet. Counsel files the appropriate claim, resolves the priority treatment, and obtains the distribution authority before recognizing a successful recovery.

The modeled fee is 25% of $98,000, producing $24,500 gross fee and $73,500 for the owner after that fee. The business bears $3,500 for partner surplus counsel, $650 for the full title abstract, $250 for mobile notary and overnight courier, $1,250 for research and operations labor, and $1,200 allocated from the dead-lead cohort. Those costs total $6,850 and are not deducted a second time from the owner's $73,500. The fee recipient and each professional's payment must follow the lawful engagement structure; this economic budget does not authorize splitting legal fees with a nonlawyer. Cleared funds, the approved settlement statement, individual trust ledger, and payment evidence reconcile the full $142,000 before the file is closed.

Net contribution is $24,500 minus $6,850, or $17,650. Dividing by gross fee gives 72.0408%, displayed as 72.0%; dividing by the county deposit would answer a different question. This contribution excludes general overhead, taxes, and financing costs, so it is not owner net income. In the separate contested scenario, a verified senior-priority claim exhausts the available surplus before an owner distribution. The firm earns zero contingent fee and stops after $650 in abstract costs, $1,250 in research labor, and $500 in preliminary counsel review, producing a $2,400 loss. These are alternative failed-file costs, not another deduction from the successful file. Track them at cohort level without double-counting the successful model's dead-lead allocation, and update forecasts when actual loss frequency replaces the initial planning assumption.

**Illustrative successful-file waterfall and separate contested outcome**

| Line item | Amount | Treatment |
| --- | --- | --- |
| County tax-deed overage | $142,000 | Gross deposited fund |
| Municipal utility / code liens | -$44,000 | Assumed verified payable priority deductions |
| Net owner excess proceeds before fee | $98,000 | $142,000 - $44,000 |
| Structured attorney-assisted contingency | $24,500 | 25% of $98,000, only where this structure is lawful |
| Owner distribution after fee | $73,500 | $98,000 - $24,500; firm bears costs below |
| Partner surplus counsel | -$3,500 | Business cost under lawful professional arrangement |
| Full title abstract | -$650 | Business cost |
| Mobile notary / overnight courier | -$250 | Business cost |
| Research / operations labor | -$1,250 | Business cost |
| Dead-lead cohort allocation | -$1,200 | Allocated failed-acquisition expense |
| Total direct costs | -$6,850 | Includes the stated cohort allocation |
| Net contribution | $17,650 | $24,500 - $6,850; 72.0% of gross fee |
| Alternative senior-lien wipeout | -$2,400 | $0 fee - $650 abstract - $1,250 labor - $500 counsel |

---

> ### “Automate the evidence trail, never the owner's entitlement.”

## Action Checklist

- [ ] Register permitted county calendars, PDF lists and CSV exports with bounded fetch schedules.
- [ ] Retain source, page and row checksums with parser versions and extraction coordinates.
- [ ] Reconcile missing pages, amount totals, duplicate rows and changed balances.
- [ ] Join APNs to historic ownership and verify entity authority independently of registered-agent listings.
- [ ] Require a named human title examiner to sign the current dossier before claimant contact.
- [ ] Have counsel establish priority, permissible aggregate fees and the appropriate claim procedure.
- [ ] Reconcile $142,000 gross, $44,000 priority deductions, $98,000 excess and $73,500 owner distribution.
- [ ] Record $6,850 business costs, $17,650 contribution and separate failed-file losses without double counting.

## Statutory & Primary Authorities

1. 18 U.S.C. 1030: Computer-access restrictions relevant to collection authorization; does not itself establish permission for a particular source. — <https://www.law.cornell.edu/uscode/text/18/1030>
2. Tex. Tax Code 34.04: Tax-sale excess-proceeds claims, covered compensation ceiling and assignment requirements; explains why the illustrative $24,500 fee cannot be transplanted into a capped Texas recovery engagement. — <https://statutes.capitol.texas.gov/Docs/TX/htm/TX.34.htm#34.04>
3. Fla. Stat. 197.582: Example of a jurisdiction-specific tax-deed surplus distribution process; not proof that every municipal lien is payable from every surplus. — <https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0100-0199/0197/Sections/0197.582.html>
4. Cal. Rev. & Tax. Code 4675: Tax-sale claim and assignment framework illustrating why source extraction must retain sale dates and transaction classifications. — <https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=4675.>

## Sources

1. Primary Sources: Understanding guardianship in probate proceedings @ [00:03:58]: That wasn't the case at all. That's how you got educated. Let's look at an example of how to misinterpret guardianship. Here’s an excerpt from a genealogy of the Slough family in Pennsylvania. The story is that a wicked step-father banished his step children from their home and placed them into the care of guardians on nearby farms. You can already see the problem right there. The author equated guardianship with custody. What really happened is that when — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=7_oRhXnhlag&t=238s>
2. State Funds Tutorial Top 4 Tech Tools Needed For Your State Funds Business @ [00:03:30]: advanced people listening to this they're going to say no David you're wrong what you need to do is have an automation trigger on your auto dealer that pushes a lead information in your CRM and yes that's true that's how I run my business but I know a lot of you guys are going through YouTube University you don't want to spend a penny on your business and you want to do this the — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=ApkuK7OOL9w&t=210s>
3. State Funds Tutorial: 5 Tech Tools For Your State Funds Business @ [00:01:09]: when you're just getting started to run your state funds business, the 0:01:13.1 S1: Very first thing you guys is a CRM stands for customer relationship software for you guys that are brand new. 0:01:21.0 S2: Pretty much all this does is it keeps track and it manages all the people that you're speaking with that you're gonna follow up with to hopefully get some deals and get some business. So what CRMS crucial? It's probably one thing I will never, ever, e — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=ES6y4iF-bBM&t=69s>
4. How to Underwrite a Curative Title Deal (And Know When to Walk Away) @ [00:10:16]: you do, well, it's the one that you don't do. So, before you leave, I want you to watch this next video. It's going to be here on the screen. And we've really just talked about a case study of a lead that came my way that wasn't worth doing. But now I want to talk to you about one that is worth doing. And it's a case study with my friend Matt Pamillis who's an operator who does a — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=-QzABvCmtVc&t=616s>
5. Affidavits of Heirship and Other Texas Probate Pitfalls | TPRE Podcast Ep 3 @ [00:13:57]: lawyer. They don't understand how the law works, the different kinds of statutes, how they apply to their case. Um, are they do you find them getting into trouble? What's the result of that? >> I won. >> Okay. Okay. Oh, was this was this a litigation in the probate? >> Okay, got it. So, tell me a little bit more about the the the the situation. Like, set it up for us. >> Well, I mean, it was was it wasn't a — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=n8jP0gweIR4&t=837s>
6. Import Your Own Property Data - Regrid Property App (Web) @ [00:01:40]: as the field names for each of the columns uh that's been pulled from the sheet that you had as well as the file type or rather sorry the column type um this has gone through the testing and we can see it's 100% matched here now uh it's worth uh looking at that match rate of course is an important part and then also to scroll down to the other section sections in this import dialogue just to make sure — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=6nMKiCCsK60&t=100s>
7. How to Find Old Probate Leads @ [00:03:30]: And now we got to pick the uh filing fr- uh at the case filing date, right? So, this is really important. This is where uh some of you might make mistakes and you might end up with like tens of thousands of cases. You'll be overwhelmed. So, we don't want to do that. We just want to go back to first we select the year. We go back to 2024. Then we select November of 2024. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=nRRFhMEip8c&t=210s>
8. $200,000 California Foreclosure Heir Claim Case Study (Money Making Juggernaut) — Money Making Juggernaut @ [00:01:55]: that, which justifies us getting our 25% fee on such a large claim. Now, how did I get this deal? Everything was through XCES Elite. XCES Elite truly is the number one CRM for this business. They have the leading databas — Matched corpus commentary on surplus funds, lien priority, skip tracing, or claim execution; verify against local statute. — <https://www.youtube.com/watch?v=MiiGrCZZAZk&t=115s>
9. Probate case study: Illegitimacy and conflicting surnames (Five-minute genealogy) — Five-minute genealogy @ [00:01:03]: as well as a son Doctor Benjamin Franklin M. Huggins. Fun fact: Doctor wasn’t a title, it was actually the poor guy’s first name. What a mouthful. Anyway, the probate file noted that William owned land in Frederick Count — Matched corpus commentary on surplus funds, lien priority, skip tracing, or claim execution; verify against local statute. — <https://www.youtube.com/watch?v=YNOLd8LZB48&t=63s>
10. How Matt Solved a 10 Heir Title Nightmare (A Curative Title Case Study) (Courtney Fricke) — Courtney Fricke @ [00:07:12]: who, um was ultimately the one who'd been dragging this along. But you said that they never really had fee simple interest. Can you explain that? What do you mean by that? >> Yeah, so when the ownership divests, each hei — Matched corpus commentary on surplus funds, lien priority, skip tracing, or claim execution; verify against local statute. — <https://www.youtube.com/watch?v=nYQaov_liDw&t=432s>
11. Troubleshooting Data Import - Regrid Property App (Web) — Regrid @ [00:05:42]: you know anything that's out of place in this case i'm looking for blanks in the parcel numbers and going down here i don't see any blanks it's possible that there's something else going on here so there's a couple thing — Matched corpus commentary on surplus funds, lien priority, skip tracing, or claim execution; verify against local statute. — <https://www.youtube.com/watch?v=VAtPDJ1KDjw&t=342s>
12. Scraping Data--Probate--Public Notice (Brian Evins) — Brian Evins @ [00:01:57]: there's really there's only a few data points that were after after the case number right we're after the estate of that person obviously and the most important data is the PRS first and last name the PRS address mailing — Matched corpus commentary on surplus funds, lien priority, skip tracing, or claim execution; verify against local statute. — <https://www.youtube.com/watch?v=sX_SYXDaDeA&t=117s>
13. Surplus Funds 101 Tutorial: Top 4 FREE Software Platforms For Your State Funds Business — Surplus Funds 101 @ [00:03:30]: SE right next to us right now. Right. 0:03:32.2 S2: Well, when you go into the Apple store, they're gonna tell you about the new iPhone and it has this updated camera, it has all these other new techy apps included in Ya — Matched corpus commentary on surplus funds, lien priority, skip tracing, or claim execution; verify against local statute. — <https://www.youtube.com/watch?v=Gk0D4wVEXmc&t=210s>
14. Amador county Tax Sale Surplus Funds Case Study (Money Making Juggernaut) — Money Making Juggernaut @ [00:04:40]: entitled, we shoot over the agreement form. They choose us, we contact the county, we make sure we have all of our requirements, all of our documents, you follow up with the county, and then you get paid. All right? So, — Matched corpus commentary on surplus funds, lien priority, skip tracing, or claim execution; verify against local statute. — <https://www.youtube.com/watch?v=4-lZwuXtY6Y&t=280s>
15. The Probate Mistake New Real Estate Investors Make (Florida Attorney Case Study) (Courtney Fricke) — Courtney Fricke @ [00:00:51]: member that owned the property in their sole name and I said, "Okay, great. We got one person on title. This shouldn't be that bad." We walked through the whole analysis and it ended up being a very linear chain of proba — Matched corpus commentary on surplus funds, lien priority, skip tracing, or claim execution; verify against local statute. — <https://www.youtube.com/watch?v=pQwwvYbUYrU&t=51s>
16. Probate Part 3, "Wording of Wills" by James Tanner @ [00:02:22]: usually someone on the opposite side who is making a different and exactly opposite argument so the court has to sort out which of the case is applied to this particular mat to the particular matter before the court it's a little bit different in the probate court action with concerning a will there is not all with someone on the opposite side most of the probate cases are unopposed but there are many times when — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=7120UjJPqZM&t=142s>
17. Crafting Source Citations in Your Ancestry Tree | Ancestry @ [00:03:19]: your family tree in a different light to see where some of your own data entry errors might be or where you might have um missed following some of the genealogical standards or where might not have made some of the edits that need to be made um or in my case I just make silly mistakes sometimes um and so I like the life story view because it helps to see my tree in a in a new way — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=7M3XZfN7814&t=199s>
18. Peeling Back the Layers: Citing Sources From Online Materials, Part 2 @ [00:07:39]: so we wouldn't need to put again that this was an entry for dot keras and that it was the draft registration cards we simply just need to cite the information shown there and i'll i'll explain what that is in a minute but think about that that when we're doing a letter citation we don't have to duplicate any of the information because sometimes one place is fine in this case the digital layer shown first explains completely — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=KtpN2Ws9PA4&t=459s>
