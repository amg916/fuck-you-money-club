# Chapter 10: Automation & AI Leverage: Docket Scrapers, OCR Triage & Case Walkthrough

*Use bounded collection and evidence-linked triage with human approval gates.*

> THE BIG MONEY PLAYBOOKS · THE FUCK YOU MONEY CLUB

## Executive Summary

Automate repetitive collection and document routing while reserving identity, inheritance, outreach, and contracting decisions for people. A useful pipeline preserves original bytes, links every extracted assertion to a page, and treats docket content as evidence rather than executable instructions. The worked case follows a $180,000 net intestate residue through represented shares, a $9,000 fee, and $4,700 of direct costs. Its $4,300 contribution is attractive only if the fee is enforceable and collected. A zero-collection case loses the entire direct-cost budget, so automation should improve selection and traceability rather than merely increase lead volume.

### Key Metrics

| Metric | Value | Confidence | Source |
| --- | --- | --- | --- |
| Represented distributions | $90,000 |  |  |
| Collected fee | $9,000 |  |  |
| Contribution | $4,300 / 47.8% |  |  |
| Zero collection | -$4,700 |  |  |

## Collect fewer documents with a better receipt  `🏷️ OPERATING_FRAMEWORK`

Start with a published court feed, authorized export, or permitted public endpoint rather than a browser session that happens to expose a document. Record the source's access terms, relevant account permissions, request limits, and document categories allowed for collection. Section 1030 of Title 18 addresses unauthorized computer access and related conduct; public visibility is not a universal authorization to defeat access controls. Do not bypass authentication, CAPTCHAs, sealed-record restrictions, or technical blocks. A terms dispute and a federal computer offense are not automatically equivalent, but neither ambiguity nor commercial value justifies evading a denial. Where automated collection is unsupported, use a permitted manual retrieval process and retain the same provenance fields as the feed collector.

Set conservative limits per host and keep them configurable: one request at a time and a five-second minimum interval can be an initial internal budget, not a claim about what any court permits. Honor stricter published limits and Retry-After instructions. On repeated 429 responses, stop the job and record the deferred items; on 401 or 403 responses, stop instead of rotating identities or proxies. Use conditional retrieval where supported, bounded timeouts, capped retries with backoff, and a daily document budget. Persist a checkpoint only after the downloaded object and its manifest entry are durable. That sequence prevents a transient failure from silently advancing the cursor past a petition that the research team never actually received.

Compute SHA-256 over the original response bytes before OCR or normalization. Store that digest with source URL, retrieval time in UTC, case number, docket entry identifier, media type, byte count, and collector version. Preserve the original object as read-only evidence and generate derived text under a separate identifier linked to the original hash. A matching digest demonstrates byte identity, not authenticity, completeness, or truth; compare the document with the official docket when those questions matter. If a court replaces a PDF at the same address, retain both versions and flag the change instead of overwriting history. Restrict access to sensitive documents and record any deletion required by the retention policy without pretending a deleted object remains reproducible.

**SOP — Standard Operating Procedure**

1. Authorize source
   - Record permitted collection scope.
   - Prefer official feeds; stop on access denial.
2. Acquire bounded bytes
   - Enforce rate, size, and timeout limits.
   - Checkpoint only durable objects and manifest entries.
3. Preserve provenance
   - Hash originals and link derivatives.
   - Keep source time, case identifier, and document version.
4. Review evidence
   - Resolve critical fields against page images.
   - No automated entitlement or outbound decision.

## Page-linked OCR and citation-locked extraction  `🏷️ OPERATING_FRAMEWORK`

Render each petition or handwritten will into ordered page images while preserving the PDF's original page index. Record both the machine index and any printed page label, because exhibits often restart numbering. OCR output should carry document hash, page index, bounding box when available, engine version, and a review state for each extracted field. Handwritten dates, crossed-out names, marginal additions, and faint signatures need visual comparison rather than confident reconstruction. A name that resembles two alternatives remains unresolved until another record supports the reading. Retain the uncertain transcription alongside the image rather than replacing it with a plausible surname. The purpose of OCR is to shorten navigation and search, not manufacture a clean evidentiary record from an ambiguous original.

Pass the extraction model only the bounded text and page references needed for the selected task. Require structured fields for asserted name, relationship, date, source hash, page index, exact supporting quotation, and uncertainty. Missing evidence must yield an explicit unknown value, not an inferred answer. Validate that the quoted text occurs in the cited page's extracted text and then have a researcher compare legally significant assertions with the page image. Text matching alone can validate an OCR error perfectly. Never treat a model confidence score as a probability that the inheritance relationship is correct. Link each proposed family-tree edge to its evidence and retain contradictory records so a fluent summary cannot erase the disagreement from the case file.

Docket PDFs are untrusted input, even when downloaded from a genuine court site. A filing can contain adversarial instructions, embedded links, or text that tells a model to ignore prior requirements and send information elsewhere. Treat all such material as quoted document content, never as authority to change the task. Run extraction without email, texting, contracting, payment, shell, or unrestricted network tools. Document links must not trigger automatic retrieval outside the allowlisted collection process. Use strict output validation and reject unexpected keys or executable payloads. A human reviewer approves any subsequent use in correspondence or contract preparation. The system has zero autonomous outreach or contract authority, and that boundary must be enforced by available capabilities rather than a polite instruction alone.

**Evidence promotion rules**

| Artifact | Required link | Reviewer decision |
| --- | --- | --- |
| Downloaded PDF | Original SHA-256 and docket identifier | Correct case and version? |
| OCR name or date | Page image and location | Legible and accurately transcribed? |
| Model relationship | Exact quotation and source hash | Supported assertion or unresolved lead? |
| Distribution calculation | Reviewed tree and governing succession rule | Counsel-confirmed entitlement assumptions? |

> **OPERATOR GATE — Evidence can suggest; people decide**
> 
> No source page, no promoted assertion. A citation is necessary but does not replace checking the underlying record.
> - Compare critical OCR fields with images.
> - Resolve competing relationship evidence.
> - Keep extraction isolated from outbound and signing tools.

## Worked case: from estate residue to collected fee  `🏷️ ILLUSTRATIVE_MODEL`

Assume a reviewed intestacy scenario with no surviving spouse, three child branches, and a $180,000 net distributable residue after estate debts, taxes, and administration expenses. Child A and Child B survive. Child C predeceased the decedent and left two surviving children, Grandchild C1 and Grandchild C2. Assume the applicable succession rule divides this estate into three equal child branches and divides Child C's branch equally between those two grandchildren. Counsel must confirm those assumptions, including survivorship and any adoption or disclaimer issues; they are not consequences of the arithmetic alone. The resulting shares are $60,000 for Child A, $60,000 for Child B, and $30,000 for each grandchild. These four shares reconcile to the full $180,000 residue.

The research firm represents only Child A and Grandchild C1 under separately reviewed agreements. Its fee base is therefore $60,000 plus $30,000, or $90,000, not the entire estate. At an assumed enforceable 10 percent fee, Child A contributes $6,000 and Grandchild C1 contributes $3,000, producing $9,000 of collected revenue. Their distributions after those fees are $54,000 and $27,000 respectively, before any other individually applicable costs. Neither Child B nor Grandchild C2 owes the firm money merely because its investigation established the complete family tree. If the proceeding is in California, evaluate the actual agreement under Probate Code Section 11604.5; a 10 percent price is a modeling assumption, not an automatic exemption from court review or a universally permissible rate.

Build the file in dependency order: docket and accounting review establish the residue, vital records establish the branches, counsel checks entitlement and contract treatment, and verified outreach reaches the intended beneficiaries. The worked budget allocates sixty research hours at $45 per hour, or $2,700; $500 for vital records; $1,200 for probate counsel review; and $300 for outreach. Total direct costs are $4,700. Allocate every invoice once, and do not quietly add the same counsel charge to both estate expenses and this firm's operating budget. Here the estate residue is already net and the counsel review is a separate firm expense. The accounting boundary matters because double counting can distort both the heirs' projected distributions and the operator's apparent profitability.

**Case waterfall: firm revenue is not estate value**

| Line | Calculation | Amount |
| --- | --- | --- |
| Net intestate residue | Three $60,000 branches | $180,000 |
| Represented shares | $60,000 + $30,000 | $90,000 |
| Collected fee | $90,000 x 10% | $9,000 |
| Research labor | 60 hours x $45 | $2,700 |
| Vital records | Direct case expense | $500 |
| Probate counsel review | Firm expense | $1,200 |
| Outreach | Direct case expense | $300 |
| Total direct costs | $2,700 + $500 + $1,200 + $300 | $4,700 |
| Contribution | $9,000 - $4,700 | $4,300 |
| Contribution margin | $4,300 / $9,000 | 47.8% |
| Zero-collection stress | $0 - $4,700 | -$4,700 |

## Use contribution, delay, and loss to control the queue  `🏷️ ILLUSTRATIVE_MODEL`

The successful case yields $4,300 contribution, calculated as $9,000 collected fees less $4,700 direct costs. Dividing contribution by collected fees gives 47.777 percent, rounded to 47.8 percent. This is not the firm's net profit margin: rent, general subscriptions, unallocated supervision, owner compensation, financing, and taxes remain outside the case calculation. Conversely, the zero-collection stress test assumes all four direct-cost categories have already been incurred and no fee is recovered, producing a loss of $4,700. Record work in progress separately from cash receipts. A signed contract or a proposed distribution should not be counted as collected revenue merely because an internal dashboard marks the relationship as confirmed or the petition as filed.

Under a deliberately simplified binary model, expected contribution equals the probability of collecting the full $9,000 multiplied by $9,000, minus the certain $4,700 cost. Break-even collection probability is therefore $4,700 divided by $9,000, or approximately 52.2 percent, before overhead and the time value of money. At 70 percent assumed collection probability, expected contribution is $1,600, not $4,300. This sensitivity is a decision aid, not an empirically measured success rate. Court reductions, partial distributions, record delays, disputes, and extra legal work create additional outcomes that the binary model omits. Replace hypothetical probabilities with cohort evidence when enough comparable closed cases exist, while keeping unresolved cases visible to avoid survivorship bias.

Assign a researcher to source acquisition and kinship evidence, an authorized reviewer to contract and entitlement questions, and a named operator to case spending and contact release. One person may fill several operational roles, but the record should still show which decision was made and on what evidence. Review spending after the initial docket review, after essential vital records arrive, and before expensive unresolved branches consume the remaining budget. Automation earns its place when it reduces duplicate retrieval, locates supporting pages faster, or exposes a weak case earlier. Do not assume fewer transcription minutes automatically lower the sixty-hour budget. Measure actual time saved, deduct review and correction time, and update future case estimates only when completed work supports the change.

---

> ### “Automate the document trail, not the decision to bind an heir.”

## Action Checklist

- [ ] Record source authorization and collection limits.
- [ ] Hash original bytes and preserve page-linked derivatives.
- [ ] Require source quotations and visual checks for critical fields.
- [ ] Disable autonomous outreach and contracting capabilities.
- [ ] Reconcile all estate shares before pricing represented interests.
- [ ] Track $4,300 contribution separately from net profit.
- [ ] Budget the -$4,700 zero-collection outcome.

## Statutory & Primary Authorities

1. 18 U.S.C. Section 1030: Unauthorized computer access boundaries for collection design. — <https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title18-section1030&num=0&edition=prelim>
2. Cal. Prob. Code Section 11604.5: Court review of heir-hunter agreements affecting distributions. — <https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=11604.5.>

## Sources

1. State Funds Tutorial: 5 Tech Tools For Your State Funds Business @ [00:01:09]: when you're just getting started to run your state funds business, the 0:01:13.1 S1: Very first thing you guys is a CRM stands for customer relationship software for you guys that are brand new. 0:01:21.0 S2: Pretty much all this does is it keeps track and it manages all the people that you're speaking with that you're gonna follow up with to hopefully get some deals and get some business. So what CRMS crucial? It's probably one thing I will never, ever, e — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=ES6y4iF-bBM&t=69s>
2. State Funds Tutorial: 5 Tech Tools For Your State Funds Business (Surplus Funds 101) — Surplus Funds 101 @ [00:01:09]: when you're just getting started to run your state funds business, the 0:01:13.1 S1: Very first thing you guys is a CRM stands for customer relationship software for you guys that are bra... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=ES6y4iF-bBM&t=69s>
3. How to Spot a Fake Probate Letter | 3 Steps to Avoid Scams (Probate TV) — Probate TV @ [00:00:52]: printed on the letter, don't automatically trust it. The number may be fake. >> [music] >> It could connect to an automated message which scammers can use to impersonate HMCTS in a follow... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=le9BUKYDl1A&t=52s>
4. Watch our Demo on How to Claim Your Ohio Unclaimed Funds (ohiocommerce) — ohiocommerce @ [00:08:31]: Please. Okay. It's asking me to Yes. Okay. As I Okay, this exactly first name John. Okay. Okay. Okay. Well, obviously I it is going to make sure you are submitting the right one and I I d... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=o1cc3hUtIv4&t=511s>
5. Probate Part 6 "Finding Probate Documents" by James Tanner (BYU Library Family History Center) — BYU Library Family History Center @ [00:14:29]: there has been a probate action filed and it is then appropriate to start looking at the time and place indicated by the deed for the probate even if you don't aren't looking for land and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=oZiYbKNvxJY&t=869s>
6. Post-1940 Descendancy Research | Ancestry — Ancestry @ [00:19:28]: singular database that then links you out to wherever that obituary exists online. Now keep in mind that sometimes newspapers depublish information. So they may only publish an obituary i... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=rKKDh07PmVc&t=1168s>
7. Scraping Data--Probate--Public Notice (Brian Evins) — Brian Evins @ [00:01:57]: there's really there's only a few data points that were after after the case number right we're after the estate of that person obviously and the most important data is the PRS first and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=sX_SYXDaDeA&t=117s>
8. How to start a Surplus Funds Recovery Business in 2026 (for beginners) (Money Making Juggernaut) — Money Making Juggernaut @ [00:00:55]: your first signed client. And I'm also going to show you the mistakes that will cost you deals if you don't catch them early. So, stick around because by the end of this, you'll have ever... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=suJSu-vn6yI&t=55s>
9. State Funds Tutorial: Cold Calling Objections vs. Complaints. Surplus Funds 101 — Surplus Funds 101 @ [00:02:10]: Okay, so the very first thing is, what is a complaint? A complaint is just a way of communicating something 0:02:17.6 S1: From somebody that has something that they don't like, we live in... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=t4w_wFimZ9A&t=130s>
10. What Happens After Death: Finding and Using Probate Records (Allen County Public Library) — Allen County Public Library @ [01:00:09]: actually court record on it. Um but uh yeah, if if there's nobody close um and and I'll kind of make a caveat with that. So, there could still be an heir at law, but let's say there's not... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=t_t1v7TPbFA&t=3609s>
11. Analyzing Evidence: A Research Game Changer (FamilySearch) — FamilySearch @ [00:04:26]: can have a mistake or an error in it, so keep that in mind. Then we always want to try and find the original record. The original record 90% of the time, maybe even more will have more in... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=tljNDoj74TI&t=266s>
12. Unraveling Forensic Genealogy With Juli Whittaker (Hittin' The Bricks with Kathleen) — Hittin' The Bricks with Kathleen @ [00:09:02]: find the family members. So, in your case with the property work, are you tracing deeds? Is that what you're doing? How do you prove who owns it? >> Well, I'm actually looking for the liv... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=u2HltZJ1FrM&t=542s>
13. All The Leads Probate Mastermind #447 — All The Leads @ [00:30:46]: phone calls so I just would want your insight into uh you know what what that script might look like or what your your best suggestions are once I get the leads good question good questio... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=xumwh2SPKv4&t=1846s>
14. DelcoPA ROW | Searching for the Existence of Marriage Records Online (Rachel Ezzell Berry) — Rachel Ezzell Berry @ [00:03:22]: but you should feel free to search however you please here in the bar next name is where you want to type your own name to search our records for this image i've typed name just so you ca... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=yFnDG9Lf6kc&t=202s>
15. NALP webinar, May 2024 - what is it like working in the Probate Research Industry (NALP - National Association of Licenced Paralegals) — NALP - National Association of Licenced Paralegals @ [00:24:44]: like a tech version of it so we have a software that we can plug the information into and it generates like a really nice family tree still so it also saves a lot of time like uh transfer... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=zz_ksXmJqyI&t=1484s>
16. How to Analyze Genealogical Sources - James Tanner (BYU Library Family History Center) — BYU Library Family History Center @ [00:02:34]: important topic. Uh it's not something that uh comes naturally to uh to people as they begin to do their genealogi- their genealogical research. It's a topic about that is a learned skill... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=7Jn_XMUozo0&t=154s>
17. Finding Probate Records That Aren't Indexed | Ancestry @ [00:00:00]: Probate lifecycle — case docket and jurisdiction — Extract petition, notice, service and hearing events with filed and effective dates.|Verify Letters Testamentary or Letters of Administration, representative identity and limitations.|Capture bond, waivers, inventory and appraisement.|Track creditor notice, filing deadlines, allowed claims and payment priority from actual rules.|Reconcile interim/final accounting, sale orders and distributions.|Use the fin — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=lOmly79G2Tk&t=0s>
18. Targeted Genealogical Research: Probate Example @ [00:00:00]: Probate lifecycle — case docket and jurisdiction — Extract petition, notice, service and hearing events with filed and effective dates.|Verify Letters Testamentary or Letters of Administration, representative identity and limitations.|Capture bond, waivers, inventory and appraisement.|Track creditor notice, filing deadlines, allowed claims and payment priority from actual rules.|Reconcile interim/final accounting, sale orders and distributions.|Use the fin — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=10DuXkEoTRA&t=0s>
