# Chapter 10: Automation & AI Leverage: Docket Scrapers, OCR Triage & Case Walkthrough

*Use bounded collection and evidence-linked triage with human approval gates.*

> THE BIG MONEY PLAYBOOKS · THE FUCK YOU MONEY CLUB

## Executive Summary

Use permitted docket collection, OCR, and language-model assistance to organize records, never to fabricate relationships or make legal determinations. Evaluate economics using collected revenue and documented costs, not estate headlines.

### Key Metrics

| Metric | Value | Confidence | Source |
| --- | --- | --- | --- |
| Illustrative estate | $180,000 |  |  |
| Illustrative gross fee | $9,000 |  |  |
| Illustrative contribution | $4,300 |  |  |

## Bound the collection and OCR pipeline  `🏷️ TECHNICAL DESIGN RECOMMENDATION; PORTAL AUTHORIZATION MUST BE VERIFIED.`

Prefer official feeds or exports. Run a docket scraper only where automated access is permitted, with conservative request rates, caching, duplicate detection, and backoff. Stop on access denial; do not evade access controls or use automation against sealed material.

Preserve originals and attach page references to OCR output. Flag names, dates, amounts, handwriting, and low-confidence text for human comparison. Model-generated summaries must cite source passages; unsupported statements remain unverified and cannot populate a proven relationship.

**SOP — Standard Operating Procedure**

1. Collect with provenance
   - Log authorization basis, retrieval time, docket identifier, and source file checksum.
2. Triage locally where feasible
   - Redact unnecessary personal data and approve vendor retention terms before external processing.
3. Require human sign-off
   - Verify extracted facts against originals before outreach, contracts, or filing preparation.

## Illustrative Economic Model  `🏷️ HYPOTHETICAL SCENARIO; NOT A FORECAST, PERMITTED-FEE ASSERTION, OR INVESTMENT CLAIM.`

Assume the branch structure in Chapter 7 and a $180,000 net distributable intestate estate. Suppose the firm lawfully contracts with child A ($60,000) and grandchild C1 ($30,000), representing $90,000 in eventual distributions. A hypothetical 10% fee on those distributions produces $9,000 only if valid, payable, and collected.

Assume 60 research hours at a fully burdened $45 per hour ($2,700), $500 in records, $1,200 in external legal review, and $300 in outreach costs. Direct costs total $4,700; contribution is $4,300 before overhead and tax. With zero collection and all costs incurred, the case loses $4,700; delays also consume working capital.

| Model component | Calculation | Result |
| --- | --- | --- |
| Represented distributions | $60,000 + $30,000 | $90,000 |
| Hypothetical gross fee | $90,000 × 10% | $9,000 |
| Direct costs | $2,700 + $500 + $1,200 + $300 | $4,700 |
| Contribution | $9,000 - $4,700 | $4,300 |
| Contribution margin | $4,300 / $9,000 | 47.8% |
| Zero-collection scenario | $0 - $4,700 | -$4,700 |

## Keep authority outside the model  `🏷️ HUMAN-OVERSIGHT AND INFORMATION-SECURITY POLICY.`

Treat docket text and uploaded documents as untrusted data, including instructions embedded inside them. Extraction tools should have no independent authority to send messages, modify contracts, change payment instructions, or disclose case records.

Review a sample of outputs after every parser or model change and record errors by field type. Stop automation when identity mismatches or fabricated citations appear. Preserve a manual path so a tool outage does not compromise evidence handling or deadlines.

> **CONTROL — No autonomous entitlement decisions**
> 
> Automation prepares a review queue; qualified people approve consequential decisions.
> - Verify every material extraction.
> - Block unapproved external disclosure.
> - Log approvals and retain a rollback path.

---

> ### “Automate the queue, not the conclusion.”

## Action Checklist

- [ ] Confirm permitted docket access.
- [ ] Preserve originals and page-linked OCR.
- [ ] Approve data-processing safeguards.
- [ ] Stress-test economics against noncollection.
- [ ] Require human approval for consequential actions.

## Statutory & Primary Authorities

1. 18 U.S.C. § 1030 (computer-access restrictions relevant to collection workflows).
2. California Probate Code § 11604.5 (review covered estate-interest agreements; the modeled fee is not legal guidance).

## Sources

1. State Funds Tutorial: 5 Tech Tools For Your State Funds Business (Surplus Funds 101) — Surplus Funds 101 @ [00:01:09]: when you're just getting started to run your state funds business, the 0:01:13.1 S1: Very first thing you guys is a CRM stands for customer relationship software for you guys that are bra... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=ES6y4iF-bBM&t=69s>
2. How to Spot a Fake Probate Letter | 3 Steps to Avoid Scams (Probate TV) — Probate TV @ [00:00:52]: printed on the letter, don't automatically trust it. The number may be fake. >> [music] >> It could connect to an automated message which scammers can use to impersonate HMCTS in a follow... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=le9BUKYDl1A&t=52s>
3. Watch our Demo on How to Claim Your Ohio Unclaimed Funds (ohiocommerce) — ohiocommerce @ [00:08:31]: Please. Okay. It's asking me to Yes. Okay. As I Okay, this exactly first name John. Okay. Okay. Okay. Well, obviously I it is going to make sure you are submitting the right one and I I d... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=o1cc3hUtIv4&t=511s>
4. Probate Part 6 "Finding Probate Documents" by James Tanner (BYU Library Family History Center) — BYU Library Family History Center @ [00:14:29]: there has been a probate action filed and it is then appropriate to start looking at the time and place indicated by the deed for the probate even if you don't aren't looking for land and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=oZiYbKNvxJY&t=869s>
5. Post-1940 Descendancy Research | Ancestry — Ancestry @ [00:19:28]: singular database that then links you out to wherever that obituary exists online. Now keep in mind that sometimes newspapers depublish information. So they may only publish an obituary i... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=rKKDh07PmVc&t=1168s>
6. Scraping Data--Probate--Public Notice (Brian Evins) — Brian Evins @ [00:01:57]: there's really there's only a few data points that were after after the case number right we're after the estate of that person obviously and the most important data is the PRS first and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=sX_SYXDaDeA&t=117s>
7. How to start a Surplus Funds Recovery Business in 2026 (for beginners) (Money Making Juggernaut) — Money Making Juggernaut @ [00:00:55]: your first signed client. And I'm also going to show you the mistakes that will cost you deals if you don't catch them early. So, stick around because by the end of this, you'll have ever... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=suJSu-vn6yI&t=55s>
8. State Funds Tutorial: Cold Calling Objections vs. Complaints. Surplus Funds 101 — Surplus Funds 101 @ [00:02:10]: Okay, so the very first thing is, what is a complaint? A complaint is just a way of communicating something 0:02:17.6 S1: From somebody that has something that they don't like, we live in... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=t4w_wFimZ9A&t=130s>
9. What Happens After Death: Finding and Using Probate Records (Allen County Public Library) — Allen County Public Library @ [01:00:09]: actually court record on it. Um but uh yeah, if if there's nobody close um and and I'll kind of make a caveat with that. So, there could still be an heir at law, but let's say there's not... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=t_t1v7TPbFA&t=3609s>
10. Analyzing Evidence: A Research Game Changer (FamilySearch) — FamilySearch @ [00:04:26]: can have a mistake or an error in it, so keep that in mind. Then we always want to try and find the original record. The original record 90% of the time, maybe even more will have more in... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=tljNDoj74TI&t=266s>
11. Unraveling Forensic Genealogy With Juli Whittaker (Hittin' The Bricks with Kathleen) — Hittin' The Bricks with Kathleen @ [00:09:02]: find the family members. So, in your case with the property work, are you tracing deeds? Is that what you're doing? How do you prove who owns it? >> Well, I'm actually looking for the liv... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=u2HltZJ1FrM&t=542s>
12. All The Leads Probate Mastermind #447 — All The Leads @ [00:30:46]: phone calls so I just would want your insight into uh you know what what that script might look like or what your your best suggestions are once I get the leads good question good questio... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=xumwh2SPKv4&t=1846s>
13. DelcoPA ROW | Searching for the Existence of Marriage Records Online (Rachel Ezzell Berry) — Rachel Ezzell Berry @ [00:03:22]: but you should feel free to search however you please here in the bar next name is where you want to type your own name to search our records for this image i've typed name just so you ca... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=yFnDG9Lf6kc&t=202s>
14. NALP webinar, May 2024 - what is it like working in the Probate Research Industry (NALP - National Association of Licenced Paralegals) — NALP - National Association of Licenced Paralegals @ [00:24:44]: like a tech version of it so we have a software that we can plug the information into and it generates like a really nice family tree still so it also saves a lot of time like uh transfer... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=zz_ksXmJqyI&t=1484s>
15. How to Analyze Genealogical Sources - James Tanner (BYU Library Family History Center) — BYU Library Family History Center @ [00:02:34]: important topic. Uh it's not something that uh comes naturally to uh to people as they begin to do their genealogi- their genealogical research. It's a topic about that is a learned skill... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=7Jn_XMUozo0&t=154s>
