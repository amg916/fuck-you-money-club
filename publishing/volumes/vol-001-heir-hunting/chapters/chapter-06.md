# Chapter 06: Finding Your First Qualified Opportunities

*A repeatable official-source workflow beats an indiscriminate lead list.*

> THE BIG MONEY PLAYBOOKS · THE FUCK YOU MONEY CLUB

## Executive Summary

Qualified opportunities begin with official records and survive four tests: an open matter with a verified custodian balance, a plausible unrepresented heir class, at least $35,000 of estimated net residue, and a documentary proof path within budget. This chapter turns county probate dockets, public administrator inventories, and unknown heirs citations into a repeatable queue. It integrates the probate docket operator play without confusing foreclosure distress with inheritance entitlement. Measure source latency, preserve provenance, investigate exceptions manually, and approach potential heirs with calm, verifiable facts rather than manufactured urgency or implied government authority.

### Key Metrics

| Metric | Value | Confidence | Source |
| --- | --- | --- | --- |
| Qualification floor | $35,000 |  |  |
| Qualification tests | 4 |  |  |
| Research ceiling | $775 |  |  |

## Build an official-source queue with a traceable identity  `🏷️ OPERATING_FRAMEWORK`

Choose one county where probate indexes, filed documents, and public administrator information are accessible through official channels. Map the court portal, the public administrator's published inventories or reports, and the office handling document requests. Record access method, publication cadence, available date range, and any charges before collecting leads. Begin with probate petitions, appointment orders, inventories and appraisals, notices of hearing, accounts, and distribution orders. A public administrator's involvement can indicate an estate needing administration, but it does not prove that no heirs exist or that a private operator has authority to act. Keep the raw source title and retrieval date beside each candidate so another researcher can repeat the search without relying on your memory or a commercial aggregator's description.

Use court plus case number as the primary case key, with decedent name, death date when available, and jurisdiction as matching fields. Names alone are insufficient: two estates can share a surname, a middle initial can disappear in an index, and one estate can generate several proceedings. Preserve the official case identifier exactly while maintaining a normalized search version separately. Attach document dates and docket entry references to extracted facts. If a portal returns a search snippet without the underlying filing, label the assertion unconfirmed. Defer sensitive family details until they are necessary to resolve a specific relationship. The output of discovery is a small evidence queue, not a contact database populated with every person whose name resembles the decedent's.

Unknown heirs citations and notices are useful signals because they show an issue being addressed in a proceeding, not because they prove an undiscovered inheritance. Read the document to establish who issued it, what relief is requested, which persons are named, and what date governs the response. Check later entries for amended petitions, appearances, and distribution orders before assuming the situation remains open. Compare public administrator inventories against the court account because publication dates may differ substantially. A county report listing $90,000 of assets from last year can coexist with a current account showing no distributable residue. Where documents cannot be retrieved online, use the clerk's published request process and budget the delay instead of treating a missing download as evidence of a missing heir.

**Official sources and the questions they can actually answer**

| Source | Useful evidence | Do not infer |
| --- | --- | --- |
| Probate docket | Proceeding, filings, orders, dates | Current cash from case status alone |
| Public administrator inventory | Reported assets and administration | Unrepresented heirs or final residue |
| Unknown heirs citation | Notice scope and hearing context | That all recipients remain unknown |
| Current account or custodian response | Dated balance and disbursements | Unrestricted distribution without claims review |

## Run the four qualification tests in their economic order  `🏷️ OPERATING_FRAMEWORK`

Gate one requires both open status and an active custodian balance. Verify procedural status from the latest docket and identify the representative, public administrator, or other actual holder of assets. Obtain a dated account or a properly authorized balance confirmation; do not solicit private banking credentials or assume the court clerk holds the money. Record the balance date and reconcile subsequent payments. An open case with an exhausted account fails the economic purpose of this test. A valuable but unsold parcel without verified liquid funds remains a separate property research candidate, not a passed cash opportunity. If access restrictions prevent balance confirmation, mark the test pending and specify the exact document or authorized response needed to resolve it.

Gate two asks whether a plausible heir class remains unrepresented in the relevant matter. California Probate Code section 6402 sets the intestate succession order for the portion not passing to a surviving spouse under section 6401, or the entire intestate estate when there is no surviving spouse. Issue, parents, and other relatives appear in a statutory sequence with conditions; a matching surname does not establish rank or entitlement. Check whether a will governs, whether a nearer class exists, and whether identified people already have a representative or an active claim. Gate three then requires at least $35,000 of estimated net residue after known claims and realistic reserves. This internal threshold concerns the estate, so calculate the prospective heir's fraction separately before estimating any potential fee.

Gate four requires a feasible documentary proof path within the staged budget. Draw each necessary parent to child link and assign a proposed record, jurisdiction, access route, expected cost, and delay. Birth, marriage, death, adoption, and court records may establish different facts; a copied online tree is a lead, not a substitute for admissible proof. Suppose a $70,000 supported residue appears divisible between two equal heirs: the candidate's provisional share is $35,000, not $70,000. If one essential foreign record requires costs beyond the remaining $775 plan, the lead does not pass merely because its estate clears the residue floor. Log a pending alternative retrieval path or reject the economics. Reapply earlier tests when new documents reveal nearer relatives, additional claims, or a changed balance.

**SOP — Standard Operating Procedure**

1. Open status and active balance
   - Verify the latest status and identify the actual asset custodian.
   - Attach dated balance evidence; unknown balances remain pending.
2. Plausible unrepresented heir class
   - Map the apparent statutory class and check appearances.
   - Resolve will status, nearer relatives, and existing representation.
3. Net residue of at least $35,000
   - Subtract known claims and supported reserves.
   - Record the estate residue separately from the candidate's potential share.
4. Feasible documentary proof
   - Cost every indispensable kinship link.
   - Require a realistic access path and fit within the staged research budget.

> **OPERATOR GATE — Four passes, not four optimistic blanks**
> 
> Advance a lead only when each test has dated supporting evidence. Pending is a useful status, not a pass.
> - Attach the decisive record.
> - Name the unresolved question.
> - Set a review trigger rather than repeatedly buying the same search.

## Integrate the probate docket play without inheriting scraper fragility  `🏷️ OPERATING_FRAMEWORK`

Track 01 Operator Play probate_docket_inheritance_arbitrage, titled Probate Docket & Pre-Foreclosure Notice-of-Default Scraping, becomes useful here as an official record change detection workflow. Use permitted feeds, published downloads, or documented search access; keep probate and recorder events in separate queues. A notice of default can flag property distress and a possible threat to estate equity, but it neither establishes a death nor identifies a legal heir. Join that event to an estate only after matching supported owner and parcel identifiers and reviewing title context. Send a reliable match into the residue worksheet as a debt or timing investigation, not as proof of an inheritance. Ambiguous matches stay unmatched until a researcher resolves the identity question.

For each permitted collection run, store the source reference, retrieval timestamp, document identifier, publication date when provided, and an integrity digest if the storage system supports it. Normalize identifiers without destroying the original values. Compare the new record set against the last successful run, queue additions and material changes, and route extraction failures for manual review. Keep the last successful checkpoint when a portal changes or returns an access error. A successful HTTP response containing a login page is not a successful document retrieval. Respect published access restrictions and use an official request or manual review when automated access is unavailable. The durable advantage is reproducible evidence and controlled exceptions, not a higher request rate against a fragile county website.

Measure event to publication latency separately from publication to discovery latency and discovery to qualification latency. A docket filing entered Monday but published Thursday has a source delay that faster polling cannot remove. If publication time is absent, report it as unknown rather than substituting the event date. An illustrative internal target might be discovery within one business day of availability and an initial qualification decision within two business days of discovery; these are planning targets, not observed performance claims. Report median and ninetieth percentile delays alongside sample counts, failed collection runs, and the share of candidates awaiting documents. Recheck a recent overlapping date window after each successful run to catch backdated additions, deduplicate by stable identifiers, and compare occasional manual samples against the automated queue.

**Forensic Naive Scraper Trap vs Durable Operator Fallback**

| Naive scraper trap | Forensic symptom | Durable operator fallback |
| --- | --- | --- |
| Treat every HTTP success as data | Login markup replaces docket fields | Validate document shape and request the record officially |
| Use name as the unique key | Unrelated deaths collapse into one lead | Keep court and case identifiers; manually resolve identity |
| Query only today's entries | Backdated filings disappear from the queue | Overlap date windows and deduplicate stable document IDs |
| Equate default notice with inheritance | Parcel match lacks a decedent connection | Verify ownership and probate linkage before qualification |
| Retry blocked access aggressively | Repeated denial and no new evidence | Pause collection and use permitted manual or clerk access |
| Measure speed only on completed leads | Pending requests vanish from reports | Report pending age, failures, and sample sizes with latency |

## Make the first contact verifiable, calm, and economically honest  `🏷️ OPERATING_FRAMEWORK`

Contact a potential heir only after the evidence supports a specific relationship hypothesis and the source permits the intended use. Introduce the business by its real name, state that the connection is preliminary, and provide a public case reference that the recipient can independently verify. Explain the service without implying appointment by the court or exclusive access to government funds. A suitable opening says that public probate records suggest a possible family connection and asks whether the person would like the case reference and a written description of the service. Do not assert that money is waiting for them, demand identity documents in the first message, or manufacture a deadline because a sales script performs better under pressure.

Separate open probate work from locating property already delivered to the California State Controller. California Code of Civil Procedure section 1582 governs agreements to locate or recover property within its unclaimed property scope, including a restricted agreement period tied to statutory notice and delivery, a ten percent fee limit for agreements covered by the provision, and written agreement requirements. Those rules are not a universal price schedule for every probate research engagement. Before proposing terms, identify the actual custodian and property regime, check the current statutory text and official instructions, and explain any direct claim route available to the owner. If the record has moved from estate administration to Controller custody, reassess the engagement rather than recycling a probate contract with a different heading.

Use a restrained follow up schedule and stop when the recipient declines or asks for no further contact. Keep a suppression entry sufficient to prevent another researcher from restarting the same approach. Verify identity through proportionate steps only when needed, and move sensitive documents through a suitable private channel rather than public comments or a bulk mailing. Log outreach date, channel, response, and any factual correction supplied by the recipient. Distinguish a refusal from an invalid lead: an heir may be real and simply prefer to proceed independently. At the weekly review, compare official source candidates, four test passes, willing conversations, and documented outcomes. That funnel reveals where research quality fails without treating pressure, repeated messaging, or unsupported entitlement claims as substitutes for a qualified opportunity.

---

> ### “A lead list is a pile of names; an opportunity is a chain of evidence.”

## Action Checklist

- [ ] Map one county's official probate, administrator, and recorder sources.
- [ ] Key each candidate by court and case number, preserving provenance.
- [ ] Verify open status and a dated active custodian balance.
- [ ] Identify the plausible unrepresented class and any nearer relatives.
- [ ] Document at least $35,000 of net residue and the candidate's separate share.
- [ ] Cost the documentary proof path before specialist research.
- [ ] Track publication, discovery, qualification, and pending request latency separately.
- [ ] Use verifiable non-urgent outreach and honor contact refusals.
- [ ] Reassess applicable agreement rules if assets move to Controller custody.

## Statutory & Primary Authorities

1. California Probate Code section 6402: Intestate succession order for the estate portion governed by this section; informs plausible heir class research. — <https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=6402.>
2. California Code of Civil Procedure section 1582: Restrictions and requirements for locator agreements within California's unclaimed property regime. — <https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1582.>

## Sources

1. Probates List on Propstream Wholesale Real Estate (Biz Matthew) — Biz Matthew @ [00:00:01]: Curative lead sourcing - geographic buy box - Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates.|Separate pre-probate from filed estates and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=W0bwM9N_98Y&t=1s>
2. How to Underwrite a Curative Title Deal (And Know When to Walk Away) (Courtney Fricke) — Courtney Fricke @ [00:00:01]: Curative lead sourcing - geographic buy box - Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates.|Separate pre-probate from filed estates and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=-QzABvCmtVc&t=1s>
3. Curative Title for Wholesalers: How He Turned a Dead Lead Into a Deal (Courtney Fricke) — Courtney Fricke @ [00:00:01]: Curative lead sourcing - geographic buy box - Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates.|Separate pre-probate from filed estates and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=2agNOU2taXA&t=1s>
4. Law Talks: Heirs' Property 1-21-2025 (LSBA Access To Justice) — LSBA Access To Justice @ [00:00:01]: Curative lead sourcing - geographic buy box - Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates.|Separate pre-probate from filed estates and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=59C1meISvlc&t=1s>
5. How a Curative Title Investor Finds & Solves Deals Others Can't (Courtney Fricke) — Courtney Fricke @ [00:00:01]: Curative lead sourcing - geographic buy box - Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates.|Separate pre-probate from filed estates and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=5LDDkiUTmXI&t=1s>
6. Curative Title + Creative Finance: The Combo Most Investors Miss (Courtney Fricke) — Courtney Fricke @ [00:00:01]: Curative lead sourcing - geographic buy box - Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates.|Separate pre-probate from filed estates and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=DcB4tJku4-A&t=1s>
7. Curative Title Explained: How Investors Make Money When Deals Can't Close (Courtney Fricke) — Courtney Fricke @ [00:00:01]: Curative lead sourcing - geographic buy box - Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates.|Separate pre-probate from filed estates and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=GH5TN_iIdMs&t=1s>
8. Heirs' Property with Jonathan Reynolds of Louisiana Appleseed (NOLA City Archives) — NOLA City Archives @ [00:00:01]: Curative lead sourcing - geographic buy box - Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates.|Separate pre-probate from filed estates and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=JPgk0Y7ZzuY&t=1s>
9. Successor in Interest and Tangled Title (National Housing Resource Center) — National Housing Resource Center @ [00:00:01]: Curative lead sourcing - geographic buy box - Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates.|Separate pre-probate from filed estates and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=ME2xl7cczH8&t=1s>
10. Heirs' Property Training (Webinar from DBAN) (Farm Aid) — Farm Aid @ [00:00:01]: Curative lead sourcing - geographic buy box - Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates.|Separate pre-probate from filed estates and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=OODJe43FyEs&t=1s>
11. Differentiating Yourself From The Competition: How To HASHTAG Your ELEVATOR PITCH | #10 (Probate Mastery) — Probate Mastery @ [00:00:01]: Curative lead sourcing - geographic buy box - Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates.|Separate pre-probate from filed estates and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=OrEz4Qk-EZ0&t=1s>
12. How to Build a Nationwide Notary Team (Step-by-Step) (Surplus Funds 101) — Surplus Funds 101 @ [00:00:01]: Curative lead sourcing - geographic buy box - Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates.|Separate pre-probate from filed estates and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=Qn63DtrxFts&t=1s>
13. Resolving Heirs' Property (MD Ag Law Education Initiative) — MD Ag Law Education Initiative @ [00:00:01]: Curative lead sourcing - geographic buy box - Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates.|Separate pre-probate from filed estates and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=TP6n8TBsCGs&t=1s>
14. How Wholesalers Can Turn Title Problems Into Profitable Curative Deals (Courtney Fricke) — Courtney Fricke @ [00:00:01]: Curative lead sourcing - geographic buy box - Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates.|Separate pre-probate from filed estates and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=U_Eh790rq3o&t=1s>
15. Preserving Homeownership: A Guide to Heirs Property for Housing Counselors (National Housing Resource Center) — National Housing Resource Center @ [00:00:01]: Curative lead sourcing - geographic buy box - Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates.|Separate pre-probate from filed estates and... — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=VFSnbIIfy-M&t=1s>
16. What Do I Enter Into My Family Tree? Resolving Conflicting Evidence | Ancestry @ [00:09:21]: your person and sometimes that means you need to do more research first so um I'm a big fan you can see up here across the top of my web browser I'm a big fan of tabs um I use extra tabs a lot and so um first of all what I did was I've actually looked at the record itself never rely solely on this index page for your information always if there is an — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=ElrY5ALsx1Y&t=561s>
17. TGP - 13 Leslie Lawson - Forensic Genealogist @ [00:30:46]: always come to the top first and have to be dealt with so I love volunteer work but I just don't have any more room on my plate for anymore and I keep getting asked I tell them no did you do you hear what you just said I have never heard so many big volunteer positions coming from the mouth one person my god Leslie this is exactly why I asked this question when — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=R5XtgGL0gkQ&t=1846s>
18. TGP - 13 Leslie Lawson - Forensic Genealogist @ [00:48:34]: with a profile or get the business card and have it available and then clients will be able to find that information on their own of course that's not really enough that's just the first step you want to take a more active approach to finding clients so here's something that you can do couple ideas to actively seek out clients other things you can do is to respond to discussions on a professional association list for example the apg has — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=R5XtgGL0gkQ&t=2914s>
