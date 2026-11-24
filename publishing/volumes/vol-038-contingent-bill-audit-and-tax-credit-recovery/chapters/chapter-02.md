# Chapter 02: Decoding Carrier Surcharges, Dimensional Weight, and Invoice Rerating

*Dimensional and billable weight, box measurement, additional handling, large-package and oversize fees, the 5-cubic-foot rule, One Rate flat pricing, commercial invoices and duties, and automated freight bill audit and payment platforms*

> THE BIG MONEY PLAYBOOKS · THE FUCK YOU MONEY CLUB

## Executive Summary

Carrier-side trainers and parcel auditors agree that invoices are priced on billable weight, which is the greater of scale weight and dimensional weight. They also agree that surcharges, not base rates, now drive spend: Intelligent Audit's Joe Wilkinson puts base rate in the high 20s to 30 percent of total cost. The street mechanics hinge on exact thresholds. Additional handling triggers sit at 48 inches, 30 inches and 50 pounds. Oversize lines sit at 96 inches and 130 inches length plus girth, with a 90-pound minimum. UPS's new 8,640-cubic-inch rule, per iDrive's Glenn Gooding, inflates one 20x20x22 box by 190 percent. Experidium's line-by-line rerate surfaced 2.38 percent of audited spend. Practitioners split on DIM divisors (139, 166, 194, custom 250) and on rounding rules. They also differ on whether to fight fees through discounts, definition variances, repackaging, or carrier diversification.

### Key Metrics

| Metric | Value | Confidence | Source |
| --- | --- | --- | --- |
| UPS 5-Cubic-Foot Additional Handling Cost Jump | 190% increase ($19.69 to $57.18 on one zone 5 parcel) | 🏷️ ATTRIBUTED_PRACTITIONER_CLAIM | iDrive Logistics ([H64bWcLI0O8 @ 00:08:56]) |
| Line-by-Line Rerate Recovery Yield | 2.38% of audited spend; 42 findings worth $11,414 | 🏷️ ATTRIBUTED_PRACTITIONER_CLAIM | Experidium ([8-Sguow2LDM @ 00:02:37]) |
| Base Rate Share of Total Parcel Spend | High 20s to 30 percent; 50 percent would be extremely high | 🏷️ ATTRIBUTED_PRACTITIONER_CLAIM | Amware Fulfillment ([d3jQIelSHJM @ 00:24:20]) |
| Negotiated Discount on FedEx Oversize Charges | 15 to 75 percent off | 🏷️ ATTRIBUTED_PRACTITIONER_CLAIM | Refund Retriever ([iizNycveRfc @ 00:01:47]) |

## 1. The Practitioner Consensus

Every carrier-side and audit-side speaker lands on the same root mechanic. The invoice is priced on billable weight, not scale weight, and billable weight is whichever is larger: actual weight or dimensional weight. UPS walks it as a three-step routine. You weigh on a scale, compute DIM from length times width times height, and take the greater of the two. For a multi-package shipment, you total the billable weight across every parcel [dp5xVhpuf64 @ 00:01:31]. The official FedEx packing guide says the same thing in plain language: many carriers compare actual weight with DIM weight and charge the higher. Charges are based on the external length times width times height of the sealed package. Internal measurements only tell you whether the product fits [OpAC2Ev8SH0 @ 00:01:33]. S3 Stores explains why the rule exists at all. If shipping charge tracked only actual weight, a rival could paralyze a network within three days by shipping large empty boxes from every location. So the carrier defines billable weight as a function of both values, then reads the price off its tables by destination and service method [q9kvSNRcgfs @ 00:01:28]. For an auditor, every line on a carrier invoice is only as defensible as the dimensions and weight behind it. Every rerate starts by rebuilding that comparison package by package.

The second point of agreement is that the base rate is no longer where the money hides. FedEx APAC tells shippers that the base rate and fuel surcharge are the predictable pieces. The other fees fall into shipment-related surcharges and customs-clearance-related fees, and the customs fees are often undetermined at booking [wFYAxOSZzMg @ 00:00:00]. FedEx Europe sorts extra charges into duties and taxes, processing fees, and carrier surcharges. It lists the usual surcharges billed to the sender: fuel, special handling for fragile or oddly shaped goods, dangerous goods, remote-area delivery, and address correction [KB4Xoe9MLWk @ 00:01:45]. Joe Wilkinson of Intelligent Audit, a former FedEx strategic pricing analyst, puts numbers on the drift. Over the last five to ten years of general rate increases, the percentage increase on surcharges has well outpaced the increase on freight charges. The published 6.9 figure pulls back to double digits once surcharges are counted. Base rate commonly sits in the high 20s or 30 percent of total spend, and a 50 percent base share would be extremely high [d3jQIelSHJM @ 00:23:42]. Wilkinson points to UPS operating income rising 67 percent year over year in 2021. He calls the rate and surcharge increases a yield management play, not a pure cost offset [d3jQIelSHJM @ 00:02:30].

Refund Retriever's Brian and iDrive's Glenn Gooding agree that additional handling has become a revenue lever, not just an operational fee. On UPS, Brian lists three trigger buckets [XPU680Aw1bg @ 00:01:22]:
- Weight: actual weight above 50 pounds domestic or 70 pounds international.
- Dimensions: a longest side over 48 inches, a second-longest side at 30 inches, or length plus girth over 105 inches.
- Packaging: non-cardboard containers, shrink wrap, banding, wheels, cylinders, and soft packs over 18 inches.
A separate peak additional handling charge stacks on every package. On FedEx, Brian cites the same 50-pound, 48-inch and 30-inch lines. He notes the FedEx weight trigger dropped from 70 pounds to 50 beginning in 2020 [TzPaNZCC4js @ 00:02:06]. Gooding priced at the highest levels for a major carrier. He explains the original logic: the fee covered non-conveyable freight that cannot make a 90-degree turn or slide safely down a gravity chute. Then the thresholds drifted. 70 pounds became 50, and six feet became five and then four, as carriers made billing more complex to lift revenue outside the GRI [H64bWcLI0O8 @ 00:06:27]. His warning is that when UPS or FedEx changes billing methodology, the other has historically followed closely [H64bWcLI0O8 @ 00:11:18].

**Where carrier trainers and parcel auditors line up on how invoices get built**

| Consensus Point | What Practitioners Report | Audit Implication | Expert Source |
| --- | --- | --- | --- |
| Billable weight is the greater of two weights | Scale weight and dimensional weight are compared, and the greater sets the rate | Rerate disputed lines from rebuilt dimensions and scale weight, package by package | UPS ([dp5xVhpuf64 @ 00:01:31]) |
| Measure the external sealed package at the widest points | Charges use external length times width times height, including handles, bulges and irregular shapes | Under-reported dimensions invite surcharges and delays once the carrier measures the sealed box | FedEx ([OpAC2Ev8SH0 @ 00:02:26]) |
| Accurate booking data controls the surcharge outcome | Non-Standard Shipment Fees hinge on dimension, weight and packaging criteria at booking | Accurate weight and dimensions at booking produce precise rate estimates from the start | FedEx APAC ([wFYAxOSZzMg @ 00:01:07]) |
| Surcharges outpace base rate increases | Surcharge percentage increases have well outpaced freight charge increases over five to ten years | Hit accessorial lines first, because base rate is often only high 20s to 30 percent | Amware Fulfillment ([d3jQIelSHJM @ 00:23:42]) |
| Additional handling thresholds keep creeping down | Thresholds moved from 70 to 50 pounds and from six feet down to four feet | Reprofile every SKU against each new threshold before the next invoice cycle lands | iDrive Logistics ([H64bWcLI0O8 @ 00:06:27]) |
| UPS and FedEx mirror each other's billing changes | When one carrier imposes a billing methodology change, the other historically follows suit closely | Model both carriers under the stricter rule before betting on a carrier switch | iDrive Logistics ([H64bWcLI0O8 @ 00:11:18]) |
| Carriers will not flag their own billing errors | Billing errors, duplicate charges and missed refunds add up across hundreds of monthly shipments | Scan every carrier invoice automatically instead of trusting invoices that merely look accurate | LateShipment ([WvGPHvucRD0 @ 00:00:00]) |

## 2. Exact Street Mechanics, Tools & Numbers

Rerating starts with the tape measure. The FedEx guide defines three measurements, all taken externally at the widest points with bulges included [OpAC2Ev8SH0 @ 00:00:30]:
- Length: the longest side.
- Width: the shortest side of the base.
- Height: from the base to the top, ignoring flaps.
Any fraction rounds up, so 11.2 inches becomes 12. FedEx's worked example: 20 by 12 by 10 inches is 2,400 cubic inches. Divided by 139, that is 17.26, billed as 18 pounds of DIM weight [OpAC2Ev8SH0 @ 00:01:33].

On metric UPS small parcel, dimensions go in centimeters and cubic centimeters are divided by 5,000. Every weight fraction rounds up to the next half kilogram, so 5.3 kg bills as 5.5 kg [dp5xVhpuf64 @ 00:01:09].

S3 Stores runs a different domestic US model [q9kvSNRcgfs @ 00:16:11]:
- Rounding: dimensions round to the nearest whole inch, so 13.2 drops to 13 while 14.6 goes to 15.
- Domestic ground: volume is divided by 194. DIM only overrides actual weight when volume exceeds 5,184 cubic inches, which works out to a DIM weight of 27 pounds or more.
- Air: the 27-pound floor disappears.
- International, including Canada: the divisor is 166.
The result is that the same box can bill at actual weight on domestic ground but at DIM on air or export.

Once a box crosses the oversize line, the math changes category. Refund Retriever's 2025 UPS breakdown covers the large package surcharge [v9AT9Omrd5c @ 00:00:15]:
- Trigger: the longest side exceeds 96 inches, or length plus girth exceeds 130 inches. Girth is two times width plus two times height.
- Price: $205 to $297 per package, depending on destination type and zone.
- Minimum: a 90-pound billable weight.
- Stacking: no additional handling charge is added once the large package charge applies.
Past 165 inches length plus girth, UPS bills an over maximum fee of $1,325 per package [v9AT9Omrd5c @ 00:00:57].

FedEx's 2026 oversize triggers are length over 96 inches, length plus girth over 130 inches, cubic size over 17,280 inches, or actual weight over 110 pounds. Any one of these flags the parcel, and the 90-pound minimum applies. Express and Ground fees, including home delivery, run as follows [iizNycveRfc @ 00:01:25]:
- Zone 2: $255.
- Zones 3 and 4: $275.
- Zones 5 and 6: $320.
- Zone 7 and up: $330.
- International: an additional $280 per package.
Brian's sharpest warning is that FedEx can remeasure in transit. A parcel that leaves compliant can arrive oversize with a $300 charge attached [iizNycveRfc @ 00:01:08]. S3 Stores had logged the older UPS oversize regime as a 90-pound floor plus a $45 surcharge [q9kvSNRcgfs @ 00:27:01].

Gooding's 5-cubic-foot case is the cleanest rerating drill. UPS moved domestic additional handling off length plus girth and onto cubic size above 8,640 cubic inches. The effective date slid from June 1 to August 17 [H64bWcLI0O8 @ 00:02:59]. His test box is 20 by 20 by 22 inches and weighs 20 pounds on the scale. Under the old rules, with a negotiated custom DIM factor of 250 instead of the published 139:
- 8,800 cubic inches bills at 36 pounds.
- In zone 5 at a 50 percent ground commercial discount, transportation costs $19.69.
Under the new rule:
- The custom DIM factor no longer applies, and the parcel bills at a 40-pound minimum.
- Transportation becomes $21.18, plus a $36 additional handling charge.
- The total is $57.18, a 190 percent jump before fuel, DAS or residential surcharges [H64bWcLI0O8 @ 00:08:32].
The trap is that most UPS billing detail lines carry no package dimensions. Post-audit math comes up blank unless the shipper holds its own dimension data for every SKU [H64bWcLI0O8 @ 00:10:19].

On detection, Experidium's agent rerated 90 days from one carrier: 402 invoices and 1,870 lines, with no sampling. It surfaced 42 findings worth $11,414. Among them was a shipment invoiced twice and paid twice. Another invoice was billed at $2,791 against $1,339 expected, because the carrier charged the full $2,342 tariff on the linehaul and never applied the contracted 62 percent discount [8-Sguow2LDM @ 00:01:31].

**Surcharge trigger and price ledger for rerating UPS and FedEx invoice lines**

| Charge | Trigger | Stated Price or Rule | Expert Source |
| --- | --- | --- | --- |
| UPS additional handling, weight category | Domestic actual weight over 50 pounds; international actual weight over 70 pounds | 2024 pricing: $34.50 zone 2, $37.50 zones 3 and 4, $41.50 zone 5 and up | Refund Retriever ([XPU680Aw1bg @ 00:01:22]) |
| UPS additional handling, dimensions category | Longest side over 48 inches, second side 30 inches, or length plus girth over 105 | 2024 pricing: $22 zone 2, $24.50 zones 3 and 4, $28.25 zone 5 and up | Refund Retriever ([XPU680Aw1bg @ 00:01:43]) |
| UPS additional handling, cubic rule (2025 update) | Domestic cubic size above 8,640 cubic inches, which equals five cubic feet | Custom DIM factor voided, 40 pound minimum billed, $36 charge in zone 5 | iDrive Logistics ([H64bWcLI0O8 @ 00:08:32]) |
| FedEx additional handling (weight, length, width, packaging) | Actual weight over 50 pounds, longest side over 48 inches, second side over 30 inches, or non-standard packaging | $24 weight charge, $15 length, $15 width, $13 non-standard packaging fee | Refund Retriever ([TzPaNZCC4js @ 00:00:33]) |
| UPS large package surcharge (2025) | Longest side over 96 inches, or length plus girth over 130 inches | $205 to $297 per package by destination type and zone, 90 pound minimum | Refund Retriever ([v9AT9Omrd5c @ 00:00:15]) |
| UPS over maximum fee | Package length plus girth exceeding 165 inches per individual package shipped | $1,325 per package over maximum fee, described as a big hit | Refund Retriever ([v9AT9Omrd5c @ 00:00:57]) |
| FedEx oversize charge (2026) | Over 96 inches long, length plus girth over 130 inches, cubic size over 17,280 inches, or weight over 110 pounds | $255 zone 2 up to $330 zone 7 and up, international adds $280 per package | Refund Retriever ([iizNycveRfc @ 00:01:25]) |

**SOP — Standard Operating Procedure**

1. Build your own dimension master
   - Record sealed, external dimensions and scale weight for every SKU and carton configuration.
   - UPS billing detail mostly omits package dimensions, so post-audit math comes up blank without your own data [iDrive Logistics — H64bWcLI0O8 @ 00:10:19]. Measure after sealing, at the widest points including handles and bulges, and round up to the whole inch [FedEx — OpAC2Ev8SH0 @ 00:02:26].
2. Rerate every line against the signed contract
   - Run every invoice line, not a sample, through the contract rate, discount, fuel and accessorial terms.
   - Experidium's engine checks fuel, accessorials and linehaul separately. It flagged a linehaul billed at the full $2,342 tariff when the 62 percent contract discount put the rate at $890, and it says so when it cannot rate an invoice instead of guessing [Experidium — 8-Sguow2LDM @ 00:01:31].
3. Flag threshold crossings and illegal stacks
   - Test each parcel against the 48, 96, 130, 165 inch, 8,640 cubic inch and 50/90/110 pound lines, then check for fees that should not stack.
   - UPS states that no additional handling charge applies when the large package charge is applied, so an invoice showing both is a dispute target [Refund Retriever — v9AT9Omrd5c @ 00:01:19]. Also expect the separate peak additional handling charge on every qualifying package [Refund Retriever — XPU680Aw1bg @ 00:02:48].
4. Package the evidence, approve, dispute, then renegotiate
   - Attach the invoice, contract clause and computation to each finding, approve it, send the dispute, and feed the recurring findings into the contract talks.
   - Every Experidium finding ships with an evidence pack. Claude drafts the dispute using only audit figures, and nothing reaches the carrier without analyst approval [Experidium — 8-Sguow2LDM @ 00:02:17]. LateShipment pitches claims backtracked up to 45 days on a pay-only-on-recovery model [LateShipment — WvGPHvucRD0 @ 00:00:32].

> **INSIDER PRO-TIPS — Bend the definition, not just the price**
> 
> The highest-leverage plays change which bucket a parcel falls into, or attack spend the carrier never negotiates on.
> - Request a size variance instead of only a discount. A 97-inch product against FedEx's 96-inch limit carries a massive fee; ask FedEx to raise your limit to 98 inches, which can eliminate the charge entirely [Refund Retriever — iizNycveRfc @ 00:02:04].
> - Negotiate the additional handling definition itself. Push the actual weight trigger to 53 or 55 pounds when a product sits just over 50, rather than settling for a 25 to 75 percent fee reduction [Refund Retriever — TzPaNZCC4js @ 00:02:57].
> - Never accept a high-level parcel analysis. Rerate package by package, with no average weights or zones, because discounts, minimums, DIM factors, DIM thresholds and fuel can each swing the numbers five million dollars [Amware Fulfillment — d3jQIelSHJM @ 00:19:26].
> - Harvest the savings that cost no negotiation capital first. Stop shipping air through DIM weighting, and kill address correction charges, which can run half a million dollars, with address validation software [Amware Fulfillment — d3jQIelSHJM @ 00:22:54].

## Section 3: Where Practitioners Disagree & Alternative Playbooks

Refund Retriever's Brian runs a two-track playbook on handling and oversize fees, and the tracks pull in different directions. On FedEx additional handling, he says many shippers simply cannot avoid the definitions, so they buy down the fee in contract talks, cutting it 25 to 75 percent, but he pushes a sharper move: negotiate a variance in the definition itself, lifting the actual weight trigger to 53 or 55 pounds when a product sits just over the line [TzPaNZCC4js @ 00:02:57]. On FedEx oversize he repeats the pattern, citing 15 to 75 percent discounts and a size variance from 96 to 98 inches for a 97-inch product, calling that the place where the real savings happens [iizNycveRfc @ 00:02:04]. For UPS large package fees, though, his first lever is physical: smaller, more efficient boxes to stay under the 130-inch girth limit, then alternative carriers or LTL freight [v9AT9Omrd5c @ 00:01:37]. Intelligent Audit's Joe Wilkinson flips the sequence entirely. He tells shippers to start with the non-contractual items, packaging that ships air through dim weighting and address correction charges that validation software can fix, because those savings cost no negotiation capital at all, and only then does he move to rate caps, minimums, and the most common surcharges [d3jQIelSHJM @ 00:22:54].

Wilkinson and iDrive Logistics' Glenn Gooding split on how much carrier diversification actually buys a shipper. Wilkinson treats it as a key element of a parcel program, but draws a hard floor: a two million dollar shipper may do best consolidating under a single national and becoming the account executive's best friend [d3jQIelSHJM @ 00:15:12]. Above that size he doubts consolidation still pays, recommending regional carve-outs that leave roughly 80 percent with the national, and never more than two new regionals at once, because four or five at a time is a recipe for chaos [d3jQIelSHJM @ 00:17:44]. Gooding, who priced at the highest levels inside a major carrier, is more skeptical that switching nationals solves a methodology change. He says history shows when UPS or FedEx imposes a billing change the other follows closely, and that FedEx, lacking dimension data on UPS shipping history, would likely mirror the new cubic rule and just aggressively discount it [H64bWcLI0O8 @ 00:11:37]. His escape hatch is different: brands will break bulk cartons into smaller parcels, raising volume and opening the door for other viable carriers. Brian at Refund Retriever, meanwhile, frames switching as zone-by-zone arbitrage, noting FedEx might be cheaper for some zones or that freight may beat parcel for large shipments [v9AT9Omrd5c @ 00:01:37].

The audit vendors themselves sell competing models, and the differences matter for who controls the dispute. Experidium's agent rerates every line of every invoice against the signed contract, flags where it cannot rate instead of guessing, and keeps a person approving every dispute before anything reaches the carrier; its 90-day run on one carrier surfaced 42 findings worth $11,414 [8-Sguow2LDM @ 00:00:20]. LateShipment pitches the opposite posture, software that scans invoices and files refund claims on the shipper's behalf with no manual effort, no monthly fee, payment only when refunds land, and claims backtracked up to 45 days [WvGPHvucRD0 @ 00:00:51]. Wilkinson warns that no dashboard summary replaces the math: there is no such thing as a high-level parcel analysis, because discounts, minimum package charges, dim factors, dim thresholds, and fuel can each swing the numbers five million dollars, so he insists on package-by-package re-rating rather than average weights or zones [d3jQIelSHJM @ 00:19:26]. CT Logistics president Alan Minor sells longevity instead of automation, telling buyers to look for stability, ongoing investment in people and technology, and a firm with 90 years in business and the same leadership for decades that keeps putting money behind its name [35fjaKeQp-I @ 00:03:02].

**Side-by-side playbooks where practitioners take different routes on the same billing problem**

| Decision Point | Playbook A | Playbook B | Expert Source |
| --- | --- | --- | --- |
| Which dim divisor converts cubic inches into billed pounds | S3 Stores divides cubic inches by 194 for domestic ground and by 166 for international shipments. | FedEx's measuring guide divides length times width times height by 139, then rounds the result up. | S3 Stores ([q9kvSNRcgfs @ 00:09:29]); FedEx ([OpAC2Ev8SH0 @ 00:01:33]) |
| How fractional inches are rounded before dim weight is computed | S3 Stores rounds each side to the nearest whole inch, so a 13.2-inch side becomes 13. | FedEx rounds every fraction up, turning an 11.2-inch measurement into a billed 12 inches. | S3 Stores ([q9kvSNRcgfs @ 00:08:39]); FedEx ([OpAC2Ev8SH0 @ 00:01:01]) |
| How to attack a recurring FedEx additional handling charge | Buy the fee down 25 to 75 percent inside the contract agreement negotiation with FedEx. | Negotiate a definition variance that raises the actual weight trigger to 53 or 55 pounds. | Refund Retriever ([TzPaNZCC4js @ 00:02:57]) |
| How to escape a UPS large package surcharge of $205 to $297 | Re-engineer into smaller, more efficient boxes that stay inside the 130-inch length plus girth limit. | Shift those zones to FedEx or move the large shipments to LTL less-than-truckload freight. | Refund Retriever ([v9AT9Omrd5c @ 00:01:37]) |
| Whether to consolidate volume or diversify across national and regional carriers | A two million dollar shipper consolidates under one national to maximize the leverage it has. | Larger shippers carve out regionals, keep roughly 80 percent national, and add two regionals maximum at once. | Amware Fulfillment ([d3jQIelSHJM @ 00:15:12]); Amware Fulfillment ([d3jQIelSHJM @ 00:17:44]) |
| Who controls the refund claim once an invoice error is found | Experidium rerates every line and a person approves each dispute before it reaches the carrier. | LateShipment files claims automatically with no monthly fee and gets paid only when refunds are recovered. | Experidium ([8-Sguow2LDM @ 00:00:03]); LateShipment ([WvGPHvucRD0 @ 00:00:51]) |
| Whether to fight dim weight or sidestep it with flat pricing | FedEx One Rate ignores package weight under 50 pounds and prices by box and service speed. | Gooding's negotiated custom dim factor of 250 cuts billed weight against the published 139 divisor. | FedEx ([jPerYiSDCp0 @ 00:01:13]); iDrive Logistics ([H64bWcLI0O8 @ 00:07:31]) |

## Section 4: Firsthand Failure Modes, Traps & Economics Checks

The first trap is that the carrier's tape measure, not yours, sets the bill. Every practitioner who touched measurement framed it as a self-inflicted, preventable leak. Brian at Refund Retriever warns that FedEx can remeasure a package in transit, so a carton that left the dock within limits arrives flagged oversize and draws a $300 charge nobody expected [iizNycveRfc @ 00:01:08]. UPS spells out the companion penalty: enter the wrong billable weight when creating the shipment and a shipping charge correction audit fee gets applied to the invoice, which is why its metric method rounds every fraction up to the next half kilogram and divides centimeter cubes by 5,000 [dp5xVhpuf64 @ 00:01:49]. FedEx's own packing team lists the habits that trigger these corrections: measuring internal instead of external dimensions, skipping bulges and handles, and under-reporting dimensions on the label; their fix is to measure the sealed box at its widest points and round 11.2 inches up to 12 [OpAC2Ev8SH0 @ 00:02:26]. Wilkinson ties the same sloppiness to real money on the address side, describing shippers paying half a million dollars in address correction charges that address validation software could have resolved upstream, without spending any negotiation capital with the carrier [d3jQIelSHJM @ 00:22:54].

The second trap is the threshold cliff, where a fraction of an inch or a cubic foot reprices the whole parcel. Gooding walks a 20x20x22-inch, 20-pound box through UPS's new 5-cubic-foot additional handling rule: under a negotiated dim factor of 250 and a 50 percent ground discount it cost $19.69 in zone 5, but crossing the cube threshold voids the custom dim factor, imposes a 40-pound minimum, and adds a $36 handling charge, for $57.18 total, a 190 percent jump [H64bWcLI0O8 @ 00:08:32]. His point is that the hit lands on exactly the mid-size cartons carriers used to covet. He also had to correct his own launch date on air, from June 1st to August 17th, a reminder that the trigger dates move too [H64bWcLI0O8 @ 00:01:01]. Brian's UPS numbers show the cliff at the top end: past 165 inches of length plus girth, an over maximum fee of $1,325 per package dwarfs the $205 to $297 large package surcharge, and every large package still carries a 90-pound minimum billable weight [v9AT9Omrd5c @ 00:00:57]. Stacking compounds it: his UPS handling breakdown notes a peak additional handling charge layered on every handling charge, so each flagged box pays twice during peak [XPU680Aw1bg @ 00:02:48].

The third trap is assuming the invoice matches the contract. Experidium's 90-day run caught a shipment invoiced twice with both invoices paid, and a line haul where the carrier billed the full $2,342 tariff and never applied the contract's 62 percent discount, against a contract rate of $890 [8-Sguow2LDM @ 00:01:31]. Gooding warns that post-audit math can fail outright: most UPS billing detail for these parcels carries no package dimensions, so without your own SKU dimension data any impact estimate is a swag at best, and he found most companies he worked with lack that data [H64bWcLI0O8 @ 00:10:19]. Wilkinson's economics check is surcharge share: if surcharges reach 50 percent of spend, check them, because that would be extremely high, while high 20s to 30 percent is common, and surcharge increases have well outpaced freight charges over the last five to ten years [d3jQIelSHJM @ 00:24:20]. His leverage horror stories are the final check. A carrier gave a $200 million shipper 30 days to rehome 15 percent of its volume, and another handed a $40 million shipper a take-it-or-lose-pickups agreement that analyzed out to a 35 percent net cost increase; shippers without diversified carriers had no operational exit [d3jQIelSHJM @ 00:07:52].

**Firsthand traps, what they cost, and the countermeasure each practitioner teaches**

| Trap | Firsthand Cost or Trigger | Countermeasure Taught | Expert Source |
| --- | --- | --- | --- |
| FedEx remeasures the package somewhere during transit | A carton leaves within limits, arrives reclassified as oversize, and draws a $300 surprise charge. | Request a size variance, shrink the box, and avoid bulging or irregular shapes at tender. | Refund Retriever ([iizNycveRfc @ 00:01:08]) |
| Wrong billable weight entered when the UPS shipment is created | UPS applies a shipping charge correction audit fee on top of the corrected parcel charge. | Compare actual and dim weight, enter the greater, and total billable weight across multi-package shipments. | UPS ([dp5xVhpuf64 @ 00:01:49]) |
| Bulk carton crosses the UPS 5-cubic-foot additional handling threshold | A $19.69 zone 5 parcel becomes $57.18, a 190 percent increase before any other surcharges. | Split five-unit cartons into smaller packs and recheck whether free shipping still holds margin. | iDrive Logistics ([H64bWcLI0O8 @ 00:08:32]) |
| Length plus girth creeps past the 165-inch over maximum line | UPS charges an over maximum fee of $1,325 per package on anything beyond 165 inches. | Measure length plus girth before tender and route anything over the line to UPS freight or trucking. | Refund Retriever ([v9AT9Omrd5c @ 00:00:57]); S3 Stores ([q9kvSNRcgfs @ 00:29:04]) |
| Carrier bills duplicates or skips the contracted discount entirely | One shipment invoiced twice and both paid; a $2,342 line billed against an $890 contract rate. | Rerate every line against the signed contract and build an evidence pack for each finding. | Experidium ([8-Sguow2LDM @ 00:01:08]) |
| Customs paperwork stalls clearance and triggers storage and disbursement fees | Storage fees apply when shipments stay uncleared past the allowed time; disbursement fees follow duty prepayment. | Complete documentation accurately, declare true market value, and include the correct HS code and origin. | FedEx APAC ([wFYAxOSZzMg @ 00:01:32]); FedEx Europe ([yIHtr7s1k6o @ 00:01:29]) |
| Minimum commitment clause conflicts with the carrier's own capacity cap | Shipper must keep 90 percent of volume while the carrier will only service 85 percent. | Strip out or soften early termination and minimum commitment penalties before signing the agreement. | Amware Fulfillment ([d3jQIelSHJM @ 00:09:00]) |

> **OPERATOR GATE — Four checks before you pay, rerate, or dispute a parcel invoice**
> 
> Each check comes straight from a loss or trap a practitioner reported. Run all four before an invoice is paid or a dispute leaves the building.
> - Measure every oversize-adjacent SKU sealed, at its widest points including bulges, because FedEx can remeasure in transit and hit a compliant-looking carton with a $300 oversize charge [Refund Retriever — iizNycveRfc @ 00:01:08].
> - Build your own SKU dimension file before modeling the 5-cubic-foot rule, since most UPS billing detail carries no package dimensions and any estimate without them is a swag at best [iDrive Logistics — H64bWcLI0O8 @ 00:10:19].
> - Reject any high-level parcel analysis and re-rate package by package across discounts, minimum package charges, dim factors, dim thresholds, and fuel [Amware Fulfillment — d3jQIelSHJM @ 00:19:26].
> - Send no dispute whose figures did not come from the audit itself; Experidium rejects any rewrite that drops a number and requires analyst sign-off before anything reaches the carrier [Experidium — 8-Sguow2LDM @ 00:02:17].

---

> ### “If you are someone that ships a lot of packages that fall into this size range, brace yourself. Next week's invoice is going to be a doozy." — Glenn Gooding, iDrive Logistics (H64bWcLI0O8 @ 00:15:58).”

## Action Checklist

- [ ] Pull your shipping spend by service level and learn what is actually driving costs before fighting over discounts on services you barely use [Amware Fulfillment — d3jQIelSHJM @ 00:22:20].
- [ ] Measure external sealed dimensions, round fractions up, compute dim weight at length times width times height divided by 139, and bill the higher of dim or actual weight [FedEx — OpAC2Ev8SH0 @ 00:01:33].
- [ ] Run every carrier invoice, not a sample, through line-level rerating against the signed contract to catch rate mismatches, duplicate invoices, missing service credits, and fuel surcharge errors [Experidium — 8-Sguow2LDM @ 00:00:46].
- [ ] For SKUs sitting just over a trigger, request a size or weight variance, such as raising a 96-inch oversize limit to 98 inches for a 97-inch product [Refund Retriever — iizNycveRfc @ 00:02:04].
- [ ] Model 5-cubic-foot exposure on bulk cartons and re-engineer five-unit packs into individual, two-pack, or three-pack shipments where the 190 percent jump lands [iDrive Logistics — H64bWcLI0O8 @ 00:14:56].
- [ ] Check the ZIP and postal code tier list for ODA and OPA surcharges before shipping, and consolidate deliveries to those areas when possible [FedEx APAC — wFYAxOSZzMg @ 00:00:46].

## Statutory & Primary Authorities

1. iDrive Logistics — UPS Additional Handling 2025: How a 5‑Cubic‑Foot Rule Can Add 190 % to Your Parcel Costs [00:08:32]: Primary practitioner testimony on the UPS 5-cubic-foot additional handling cliff turning a $19.69 parcel into $57.18. — <https://www.youtube.com/watch?v=H64bWcLI0O8&t=512s>
2. Amware Fulfillment — Making Sense of Parcel Costs with Joe Wilkinson at Intelligent Audit [00:19:44]: Primary practitioner testimony on package-by-package re-rating and why high-level parcel analysis fails. — <https://www.youtube.com/watch?v=d3jQIelSHJM&t=1184s>
3. Refund Retriever — FedEx Oversize Accessorial Fees 2026 [00:01:08]: Primary practitioner testimony on FedEx in-transit remeasurement triggering surprise oversize charges. — <https://www.youtube.com/watch?v=iizNycveRfc&t=68s>
4. Experidium — Freight Audit & Recovery Agent: Claude Checks Every Carrier Invoice [00:01:31]: Primary practitioner testimony on contract rerating exposing a skipped 62 percent discount and duplicate paid invoices. — <https://www.youtube.com/watch?v=8-Sguow2LDM&t=91s>

## Sources

1. How UPS and FedEx Dimensional Weight Works? — S3 Stores @ [00:27:01]: So first consequence is that the minimum billable weight for this kind of package is going to be 90 lb. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=q9kvSNRcgfs&t=1621s>
2. Understanding shipping surcharges — FedEx APAC @ [00:00:46]: Before shipping check the ZIP and postal code list by tier to see if ODA or OPA applies, and when possible consolidate deliveries to optimize costs. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=wFYAxOSZzMg&t=46s>
3. Extra shipping charges explained | Fees, duties and surcharges — FedEx Europe @ [00:03:12]: Typos can be pricey, especially when your carrier needs to adjust the paperwork for you, so just check, check, and double check. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=KB4Xoe9MLWk&t=192s>
4. How to Calculate Billable Weight on UPS Small Parcels | UPS — UPS @ [00:01:49]: It's important to ensure that you enter the correct billable weight when creating your shipment in order to avoid the shipping charge correction audit fee from being applied. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=dp5xVhpuf64&t=109s>
5. FedEx I How to Ship Learning Center | How to complete a commercial invoice for shipping — FedEx Europe @ [00:01:29]: If the value doesn't seem reasonable, customs may ask you or your receiver for evidence of the value you have declared on the invoice. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=yIHtr7s1k6o&t=89s>
6. How to Measure a Box for Shipping | The Official FedEx Guide — FedEx @ [00:02:26]: Don't under-report dimensions; include handles, bulges, and irregular shapes, and measure everything at the widest point. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=OpAC2Ev8SH0&t=146s>
7. UPS Large Package Surcharge for 2025 — Refund Retriever @ [00:00:57]: If a package exceeds 165 in in length and girth, UPS is going to charge an over maximum fee of $1,325 per package. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=v9AT9Omrd5c&t=57s>
8. UPS Additional Handling Charge: What you need to know — Refund Retriever @ [00:03:07]: If you have a package that you see a lot of, try to get a variance, try to get discounts on things. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=XPU680Aw1bg&t=187s>
9. Freight Audit & Recovery Agent: Claude Checks Every Carrier Invoice — Experidium @ [00:01:31]: The signed contract quoted its page base tariff less a 62% discount, and the carrier billed the full tariff of $2,342 and never applied the discount. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=8-Sguow2LDM&t=91s>
10. Freight Audit & Recovery Agent: Claude Checks Every Carrier Invoice — Experidium @ [00:02:37]: Your analyst approves the finding, then you decide to pursue it, and you get a findings report with 2.38% of audited spend identified and evidenced. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=8-Sguow2LDM&t=157s>
11. Top 10 Parcel Audit Software Solutions for E-Commerce — LateShipment @ [00:00:51]: Reducing shipping costs by up to 20% with claims backtracked up to 45 days and no monthly fee; you only pay when refunds are recovered. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=WvGPHvucRD0&t=51s>
12. FedEx Additional Handling Surcharge: What to know — Refund Retriever @ [00:02:57]: What if instead of a cost reduction a company could negotiate a variance in the definition of additional handling. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=TzPaNZCC4js&t=177s>
13. FedEx Oversize Accessorial Fees 2026 — Refund Retriever @ [00:01:08]: Your shipment might leave your facility within the limits, but arrives as oversize after a remeasure, and just like that you're hit with a $300 charge you didn't expect. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=iizNycveRfc&t=68s>
14. UPS Additional Handling 2025: How a 5‑Cubic‑Foot Rule Can Add 190 % to Your Parcel Costs — iDrive Logistics @ [00:08:32]: It does cross the 5 cubic foot threshold, therefore the custom dim factor no longer applies, it's billed at a minimum 40 lb, and the additional handling charge applies for this zone 5 of $36. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=H64bWcLI0O8&t=512s>
15. UPS Additional Handling 2025: How a 5‑Cubic‑Foot Rule Can Add 190 % to Your Parcel Costs — iDrive Logistics @ [00:10:19]: If you were to pull down your billing invoice detail from UPS, you would note that the vast majority of the parcels being billed do not contain package dimensions. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=H64bWcLI0O8&t=619s>
16. CT Logistics Freight Bill Audit and Payment — CT Logistics @ [00:01:49]: We have capability to show them the cost savings through validation of those invoices outside of North America. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=35fjaKeQp-I&t=109s>
17. Making Sense of Parcel Costs with Joe Wilkinson at Intelligent Audit — Amware Fulfillment @ [00:19:44]: There are so many variables that any one of them can swing the numbers five million dollars; you've got to do package level analytics, don't use average package weights, don't use average zones, package by package re-rating. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=d3jQIelSHJM&t=1184s>
18. What is FedEx One Rate and how does flat rate shipping work? — FedEx @ [00:01:13]: The weight of your packages below 50 pounds doesn't affect shipping rates, so just make sure it doesn't exceed the weight limits. — Verbatim practitioner testimony from Chapter Q2. — <https://www.youtube.com/watch?v=jPerYiSDCp0&t=73s>
