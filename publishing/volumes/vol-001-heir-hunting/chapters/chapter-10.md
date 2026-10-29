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
