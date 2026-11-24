from __future__ import annotations

CHAPTER_12 = {'id': 'Q12',
 'chapter_id': 'Q12',
 'chapter_number': 12,
 'question_number': 12,
 'slug': 'negotiation-audits-licensing-economics',
 'question_prompt': 'How do enterprise software negotiations, license audits, and services economics shape '
                    'reseller margins?',
 'kicker': 'Q12 / THE BIG MONEY PLAYBOOKS',
 'title': 'Negotiation, Audits, and Licensing Economics',
 'subtitle': 'Counter-tactics against vendor sales maneuvers, Microsoft audit defense and audit readiness, '
             'protecting hosting margins, switching CSPs, Snowflake vs. Databricks pricing, SAP–CodeMeter '
             'license integration, professional services margins and utilization, and the cybersecurity '
             'vendor outlook',
 'layout_template': 'action_worksheet_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners from Virtualization Options, SAMexpert TV, Innovia Consulting, ISM '
                      'New Jersey, and The SaaS CFO converge on one rule: enterprise software leverage '
                      'exists before signature, and vendor audits are commercial weapons aimed at new '
                      'deals. The street mechanics are numeric. Microsoft audits penalize non-compliance '
                      'of 5% or more with licenses at 125% of your discounted price list plus $27k to $40k '
                      'in audit fees, under 30-day respond and settle deadlines. Contract defenses include '
                      'a hard 3% escalator cap, 3-5% multi-year price locks, 50% ROI realization haircuts, '
                      'and costed exit pilots. Resellers face SPLA prices rising about 10% a year, with '
                      'inbound cost cuts lifting margin from roughly 5% to 35%. The split: Innovia calls '
                      'Microsoft “very fair” in compliance dealings, while SAMexpert insists audit '
                      'mistakes “are always in favor of microsoft” and settlements feed upsells.',
 'key_metrics': [{'label': 'Microsoft audit penalty license price',
                  'metric': 'Microsoft audit penalty license price',
                  'value': '125% of your discounted price list once non-compliance hits 5% or more',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Penalty for buying shortfall licenses after an audit finds 5%+ '
                             'non-compliance; formerly 125% of the public list price, and paired with '
                             'reimbursement of audit fees.',
                  'source': 'SAMexpert TV – Microsoft Licensing and Cloud ([7shzxv1SUFc @ 00:10:22])'},
                 {'label': 'Audit fee reimbursement exposure',
                  'metric': 'Audit fee reimbursement exposure',
                  'value': '$27-28k up to about $40k',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Daryl cites formal documents showing the auditor fee range a non-compliant '
                             'customer must reimburse; the rumored figure is about $40k.',
                  'source': 'SAMexpert TV – Microsoft Licensing and Cloud ([7shzxv1SUFc @ 00:18:31])'},
                 {'label': 'Uncapped escalator compounding over three years',
                  'metric': 'Uncapped escalator compounding over three years',
                  'value': '15-25% over a three-year term',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Cumulative price drift when annual increases are left uncapped; the '
                             'prescribed counter is a 3-5% annual cap.',
                  'source': 'Virtualization Options LLC Free Learning Portal ([xP4R2F8hbBw @ 00:06:54])'},
                 {'label': 'SPLA margin after inbound cost cuts',
                  'metric': 'SPLA margin after inbound cost cuts',
                  'value': 'Roughly 5% to 35% after a 30% inbound cost reduction',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Goliff reports hosting providers cutting inbound SPLA costs by 30%, moving '
                             'margin from about 5% to 35%, while 13% of surveyed providers break even or '
                             'earn about 5%.',
                  'source': 'SAMexpert TV – Microsoft Licensing and Cloud ([S-D4c7b8-94 @ 00:10:53])'}],
 'sections': [{'section': 1,
               'title': 'The Practitioner Consensus: Leverage Lives Before the Signature, and Audits Are a '
                        'Sales Weapon',
               'paragraphs': ['Across the Virtualization Options LLC explainers and the SAMexpert TV audit '
                              'training, the operating premise is identical: enterprise software leverage '
                              'is a pre-signature asset, and everything after the ink dries is defense. '
                              'The Virtualization Options narrator puts it flatly: “the only moment of '
                              'genuine enterprise leverage is before the signature line,” and '
                              "post-purchase governance “simply can't recover capital you've already "
                              'surrendered” [L-DrE5qghM8 @ 00:03:50]. The same channel warns that the '
                              'shift from perpetual licenses to mandatory subscriptions strips deployment '
                              'rights, adds switching friction, and hands the vendor pricing power at '
                              'every renewal [fTqBORy9ePo @ 00:01:31]. Price only moves when the vendor '
                              "believes you will leave: “If they sense you won't walk away, there's "
                              "absolutely no way they're dropping the price” [fTqBORy9ePo @ 00:03:00]. The "
                              'counter to vendor “constructive tension” is a credible willingness to '
                              'reassign the deal to a competitor or delay the project outright. The Data & '
                              'AI Playground lands on the same point from the architecture side, warning '
                              'buyers never to decide from a vendor demo and framing platform choice as “a '
                              '3-year decision” [yhgHAMKkOqc @ 00:03:35]. That three-year horizon is '
                              'exactly the window over which escalators, lock-in, and renewal pricing '
                              'power compound against a buyer who signed without an exit.',
                              'On audits, the consensus is that the stated compliance purpose is cover for '
                              "a commercial play. SAMexpert TV's Daryl states it without softening: “the "
                              "idea of an audit is to create leverage that's the bottom line,” with the "
                              'end goal being a cloud agreement or Office 365 [7shzxv1SUFc @ 00:01:46]. '
                              'Alex adds that customers get “lured into a new deal often on unfavorable '
                              'terms,” and that partner-run SAM reviews carry an expectation that the '
                              "partner upsells a multiple of Microsoft's investment; a partner that comes "
                              'back with zero gets no more business [7shzxv1SUFc @ 00:08:52]. The '
                              'Virtualization Options guide describes the identical pattern in '
                              'vendor-neutral terms: after signature, vendors run “malicious license '
                              'audits” to extract unbudgeted revenue, so audit triggers, true-up cost '
                              'caps, and frequency limits must be fixed in the contract up front '
                              '[L-DrE5qghM8 @ 00:04:07]. On the hosting side, Alexander Goliff of '
                              'SAMexpert TV reports that audit settlements may demand Azure consumption at '
                              'a multiple of the penalties themselves [S-D4c7b8-94 @ 00:43:06], and that '
                              'over 50% of surveyed providers were audited in the last 12 months. The '
                              'shared conclusion: treat every audit notice as the opening move of a sales '
                              'negotiation, then staff and sequence the response the way you would a major '
                              'renewal.',
                              'The third pillar is controlling who talks to the vendor and refusing '
                              'manufactured urgency. The Virtualization Options Chapter 9 explainer '
                              'documents vendors bypassing procurement through informal networks and '
                              'cultivating executive champions with strategic gifting and pilot offers. '
                              'The prescribed defense is routing all vendor communications through '
                              'procurement, backed by written do-not-contact directives [xP4R2F8hbBw @ '
                              "00:01:40]. ISM New Jersey's Graham, drawing on roughly 1,000 category "
                              'managers, confirms the same leak from the buyer side: stakeholders “use the '
                              'back door” to circumvent procurement, and supplier-written statements of '
                              'work are a recurring trap [ZeVBT8JVp-U @ 00:09:35]. The urgency rule is '
                              'absolute in the Virtualization Options material: “Treat all deadline-driven '
                              'urgency as entirely artificial,” and enforce pre-signature audit gates '
                              "regardless of the vendor's quarter-end calendar [L-DrE5qghM8 @ 00:04:36]. "
                              'Vendor ROI math is presumed inflated. Separate hard savings from soft labor '
                              'savings, since 4 hours a month saved is not real unless it cuts headcount '
                              'or overtime, and apply a 50% realization haircut because vendors assume '
                              '100% [fTqBORy9ePo @ 00:04:03]. The baseline prerequisite is a buyer who '
                              'centralizes vendor access, owns the cost model, and walks into every '
                              'renewal with a credible, costed exit.'],
               'table': {'caption': 'Consensus rules the practitioners apply before and during licensing '
                                    'negotiations and audits',
                         'headers': ['Consensus Principle',
                                     'What Practitioners Do',
                                     'Why It Works',
                                     'Expert Source'],
                         'rows': [['Real leverage exists only before the signature line',
                                   'Enforce pre-signature audit gates and falsifiable pilots before any '
                                   'commitment is signed',
                                   'Post-purchase governance cannot recover capital already surrendered to '
                                   'the vendor',
                                   'Virtualization Options LLC Free Learning Portal ([L-DrE5qghM8 @ '
                                   '00:03:50])'],
                                  ['Vendor audits are commercial leverage, not neutral compliance checks',
                                   'Staff the audit like a negotiation and expect a cloud or Office 365 '
                                   'pitch',
                                   'The audit endgame is a new deal, often on unfavorable customer terms',
                                   'SAMexpert TV – Microsoft Licensing and Cloud ([7shzxv1SUFc @ '
                                   '00:01:46])'],
                                  ["Only a credible walk-away moves the vendor's price",
                                   'Be ready to reassign the deal to a competitor or delay the project',
                                   'Vendors refuse to drop price once they sense you will not walk',
                                   'Virtualization Options LLC Free Learning Portal ([fTqBORy9ePo @ '
                                   '00:02:45])'],
                                  ['Every vendor deadline and quarter-end discount is artificial urgency',
                                   'Ignore calendar pressure and hold your own pre-signature audit gates '
                                   'firmly',
                                   "Rushed signatures exploit time scarcity and the buyer's sunk cost "
                                   'fallacy',
                                   'Virtualization Options LLC Free Learning Portal ([xP4R2F8hbBw @ '
                                   '00:03:39])'],
                                  ['All vendor contact must route through central procurement only',
                                   'Issue written do-not-contact directives and freeze internal vendor '
                                   'communications entirely',
                                   'Stakeholders use the back door and vendor champions bypass governance '
                                   'otherwise',
                                   'ISM New Jersey ([ZeVBT8JVp-U @ 00:09:35])'],
                                  ['Vendor ROI and TCO models are inflated by default',
                                   'Split hard from soft savings and apply a 50% realization haircut',
                                   'Vendors assume 100% realization and count soft labor savings as cash',
                                   'Virtualization Options LLC Free Learning Portal ([fTqBORy9ePo @ '
                                   '00:04:03])'],
                                  ["Audit calculation errors consistently land in the vendor's favor",
                                   'Put someone who understands license calculation on every effective '
                                   'license position',
                                   'Without that expertise, the speaker promises you will be overpaying '
                                   'every time',
                                   'SAMexpert TV – Microsoft Licensing and Cloud ([7shzxv1SUFc @ '
                                   '00:42:05])']]}},
              {'section': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers: Audit Math, Defense Sequencing, and '
                        'Clause Economics',
               'paragraphs': ['The Microsoft audit penalty mechanics are precise and worth memorizing. Per '
                              'SAMexpert TV, non-compliance of 5% or more triggers two penalties. First, '
                              'you buy the shortfall at 125% of your own discounted price list, which was '
                              "formerly 125% of public list. Second, you reimburse the auditor's fees, "
                              'which Daryl puts at $27-28k up to about $40k based on formal documents '
                              '[7shzxv1SUFc @ 00:16:59]. The contract sets two deadlines, 30 days to '
                              'respond and 30 days to settle, and purchases must land within 30 days of '
                              "settlement. Innovia Consulting's Jeff Balski reports that self-audit "
                              'deadlines typically run 60 days and advises requesting an extension right '
                              'away, adding that Microsoft has never been seen refusing such requests '
                              '[WV0uRh3yMX4 @ 00:18:59]. The negotiation opening sits inside the threshold '
                              'itself: Daryl calls the “5% of what?” question deliberately vague and “a '
                              'good place to start the negotiations” [7shzxv1SUFc @ 00:21:27]. One '
                              "customer's pushback forced a recalculation that ended at 50k with no "
                              'penalties. Timing matters because Microsoft pushes the CIO or CFO toward an '
                              'early commercial close, and entering talks against a $1M disputed figure is '
                              'a different negotiation from entering against 50k [7shzxv1SUFc @ 00:45:44]. '
                              'Fix the technical number before anyone discusses money.',
                              "Defense execution runs on a fixed team and a paper trail. Alex's SAMexpert "
                              'TV roster is SecOps (who run the scripts), procurement, ITAM, the '
                              'licensing-design owner, and legal. The full team matters because Microsoft '
                              'will try to “divide and conquer” the CIO away from it [7shzxv1SUFc @ '
                              '00:51:15]. At kickoff, sign the NDA and hand over nothing, not even the org '
                              'structure, since an acquisition may breach the EA affiliate threshold '
                              '[7shzxv1SUFc @ 00:54:49]. Declarations are accepted only for data that '
                              'cannot be scripted, so disclose dev/test, DR/HA, and OEM/ISV/SPLA coverage '
                              'up front. Missed OEM and ISV entitlements such as Commvault and NICE can '
                              'mean hundreds of thousands of dollars in SQL licensing. Keep a written '
                              'protocol of disagreement throughout, because the technical analysis cannot '
                              'be reopened later without extra fees. Excel errors appear in every audit, '
                              'and corrected mistakes can resurface in a later ELP version [7shzxv1SUFc @ '
                              '01:09:04]. Goliff adds the asymmetry that makes the paper trail mandatory: '
                              'one hosting provider was short €4M while having overpaid €11M, and '
                              'overpayments are ignored in audits [S-D4c7b8-94 @ 00:45:40]. The 2016 '
                              'core-conversion example, where a customer received 40 licenses per server '
                              'instead of 16, shows how much entitlement sits on the table for teams that '
                              'document it.',
                              'The contract clause stack is numerically specific. Virtualization Options '
                              'prescribes capping the annual escalator “at a hard maximum of 3%,” plus a '
                              'net-price lock for expansion, SKU downgrade rights, and an annual 10-20% '
                              'commitment reduction right. It adds a TCO remedy credit if savings fall '
                              'below 75%, SLA clawbacks, and “stressed exit run rights” [fTqBORy9ePo @ '
                              '00:06:41]. The Chapter 9 explainer widens the cap to 3-5% and shows why it '
                              'matters: uncapped escalators compound to 15-25% over a three-year term. '
                              'Pair the cap with 90-day auto-renewal notice windows, early termination '
                              'rights, and fixed-fee SOWs with not-to-exceed caps [xP4R2F8hbBw @ '
                              '00:06:54]. For resellers and hosters, the margin math is just as hard. '
                              'Goliff reports SPLA prices rising about 10% a year, with providers able to '
                              'do “nearly nothing” about it. In the survey, 13% of providers break even or '
                              'earn about 5%, while 30% inbound cost cuts lifted SPLA margin from roughly '
                              '5% to 35% [S-D4c7b8-94 @ 00:10:53]. On the services line attached to any '
                              'resale, The SaaS CFO benchmarks margins at a 35% median, 50% top quartile, '
                              'and 15% bottom quartile, and warns that sales discounts services first '
                              '[gQvlawVvuzw @ 00:01:40].'],
               'table': {'caption': 'Hard numbers and levers practitioners use in audits, renewals, and '
                                    'reseller margin defense',
                         'headers': ['Lever or Number',
                                     'Exact Figure or Rule',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Microsoft audit non-compliance penalty threshold',
                                   'Penalties trigger at 5% or more non-compliance',
                                   'Contest the vague “5% of what?” baseline as the opening negotiation '
                                   'point',
                                   'SAMexpert TV – Microsoft Licensing and Cloud ([7shzxv1SUFc @ '
                                   '00:21:27])'],
                                  ['Penalty pricing on shortfall licenses after audit',
                                   '125% of your discounted price list, plus audit fee reimbursement',
                                   'Drive the disputed figure down before the penalty math ever applies',
                                   'SAMexpert TV – Microsoft Licensing and Cloud ([7shzxv1SUFc @ '
                                   '00:10:22])'],
                                  ['Annual price escalator cap in renewal contracts',
                                   'Hard maximum of 3% per year, with a net-price lock for expansion',
                                   'Pair with SKU downgrade rights and a 10-20% annual commitment '
                                   'reduction',
                                   'Virtualization Options LLC Free Learning Portal ([fTqBORy9ePo @ '
                                   '00:06:41])'],
                                  ['Counter to a vendor claiming list price is firm',
                                   'Demand a 3-5% multi-year price lock cap or net 90 terms',
                                   'Use non-price levers first when the vendor refuses headline discounts',
                                   'Virtualization Options LLC Free Learning Portal ([L-DrE5qghM8 @ '
                                   '00:05:51])'],
                                  ['TCO remedy credit tied to vendor savings promises',
                                   'Credit triggers if delivered savings fall below 75% of the promise',
                                   'Force the vendor to underwrite its own ROI model contractually',
                                   'Virtualization Options LLC Free Learning Portal ([fTqBORy9ePo @ '
                                   '00:07:11])'],
                                  ['SPLA hosting margin recovery through inbound cost cuts',
                                   '30% inbound cut moved margin from roughly 5% to 35%',
                                   'Measure SPLA profitability first, since 19% of providers do not',
                                   'SAMexpert TV – Microsoft Licensing and Cloud ([S-D4c7b8-94 @ '
                                   '00:10:53])'],
                                  ['Compliant disaster recovery licensing for hosting providers',
                                   'Compliant DR is free; one provider saved $1.2M per year',
                                   'Restructure DR licensing and get the savings confirmed in writing',
                                   'SAMexpert TV – Microsoft Licensing and Cloud ([S-D4c7b8-94 @ '
                                   '00:34:34])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Timing, Exit Pilots, and Partner Switching Plays',
                           'body': 'These moves come straight from operators who sit across the table from '
                                   'Microsoft auditors and enterprise vendor sales teams. Each one '
                                   'converts a vendor pressure point into buyer leverage.',
                           'items': ['Time Microsoft negotiations to its June year-end and bring in the '
                                     'local office by trading on what Microsoft needs, such as winning SAP '
                                     'HANA on Azure instead of AWS [SAMexpert TV – Microsoft Licensing and '
                                     'Cloud — 7shzxv1SUFc @ 01:15:49]',
                                     "Turn the auditor's extrapolation threat into an internal weapon: one "
                                     'customer used the extrapolation report to force their own teams to '
                                     'deliver real data, and fed-up auditors will extrapolate “20 30” '
                                     'forward just to close [SAMexpert TV – Microsoft Licensing and Cloud '
                                     '— 7shzxv1SUFc @ 00:37:37]',
                                     'Run a costed exit pilot, the “most impactful lever” against lock-in, '
                                     'and sequence baseline hardware metrics, consolidation, per-cluster '
                                     'bundle scoping, exit pilot, and discount last [Virtualization '
                                     'Options LLC Free Learning Portal — fTqBORy9ePo @ 00:05:39]',
                                     'Move CSP subscriptions midterm to the partner of your choice with '
                                     'the transfer tool at any point; existing bundles and promotions stay '
                                     'attached to the subscription [Heartland Business Systems — '
                                     'jqaG0NHe-0c @ 00:00:57]']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock the team and the NDA before any data moves',
                              'action': 'Assemble SecOps, procurement, ITAM, the licensing-design owner, '
                                        'and legal; sign a direct NDA with the auditor at kickoff and '
                                        'release no data, including the org structure.',
                              'detail': 'An acquisition visible in the org structure may breach the EA '
                                        'affiliate threshold, and Microsoft will try to split the CIO from '
                                        'the team, so the full roster and NDA come first [SAMexpert TV – '
                                        'Microsoft Licensing and Cloud — 7shzxv1SUFc @ 00:54:49]'},
                             {'step': 2,
                              'title': 'Script the inventory to full coverage',
                              'action': 'Collect deployment data with scripts run by SecOps, reserving '
                                        'declarations only for data that cannot be scripted, and disclose '
                                        'dev/test, DR/HA, and OEM/ISV/SPLA coverage up front.',
                              'detail': 'Auditors demand 100% coverage, distrust SCCM, and in one case '
                                        'found Snow data covered only 85%, which opens the door to '
                                        'extrapolation [SAMexpert TV – Microsoft Licensing and Cloud — '
                                        '7shzxv1SUFc @ 00:34:43]'},
                             {'step': 3,
                              'title': 'Rebuild the ELP and log every dispute',
                              'action': 'Check the MLS for missing CSP and MPSA entitlements, missed '
                                        'OEM/ISV rights, and active/passive SQL errors, and keep a written '
                                        'protocol of disagreement.',
                              'detail': 'The technical analysis cannot be reopened later without extra '
                                        'fees, and Excel errors appear in every audit, so every disputed '
                                        'line goes on paper before the commercial phase [SAMexpert TV – '
                                        'Microsoft Licensing and Cloud — 7shzxv1SUFc @ 01:09:04]'},
                             {'step': 4,
                              'title': 'Convert the settlement into contract leverage',
                              'action': 'Close commercially only on the corrected figure, then write the '
                                        'renewal with escalator caps, commitment reduction rights, and a '
                                        'costed exit pilot before any discount talk.',
                              'detail': 'Sequence baseline hardware metrics, consolidation, per-cluster '
                                        'bundle scoping, and the exit pilot, and take the discount last '
                                        '[Virtualization Options LLC Free Learning Portal — fTqBORy9ePo @ '
                                        '00:06:10]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over what a Microsoft audit actually is. Innovia '
                              "Consulting's team says that in all cases they have found Microsoft to be "
                              'very fair when dealing with compliance issues, and frames the SAM '
                              'engagement as a voluntary review where Microsoft pays the partner '
                              "[WV0uRh3yMX4 @ 00:17:39]. SAMexpert TV's Daryl rejects that framing "
                              'outright: the idea of an audit is to create leverage, usually toward a '
                              'cloud agreement or Office 365 [7shzxv1SUFc @ 00:01:46]. Alex adds that '
                              'partners running soft-touch reviews are expected to upsell a multiple of '
                              "Microsoft's investment, and a partner that comes back with zero gets no "
                              'more business [7shzxv1SUFc @ 00:08:52]. The two camps also read the threat '
                              'level differently. Innovia warns that ignoring self-audit requests '
                              'eventually triggers a Legal Contracts and Compliance audit, punitive enough '
                              'that the advice is to get your lawyers involved, and recommends asking for '
                              'an extension immediately on the typical 60-day deadline. Daryl tells '
                              "customers not to be afraid of threats, saying that in today's environment "
                              'they cannot see Microsoft taking anyone to court [7shzxv1SUFc @ 01:16:06]. '
                              'Operators selling into this space have to pick a posture: cooperative '
                              'self-audit hygiene, or a defense team that treats every number as '
                              'negotiable.',
                              'On data platforms, the vendors and the neutral integrators disagree about '
                              "where the cost trap sits. Snowflake's speaker, who ran Sprint network "
                              'analytics with a 250-person team and roughly $90M a year in budget, says '
                              'locked-in platforms left them stuck, calls it a myth that lock-in is more '
                              'secure, and argues interoperable platforms are more secure than closed ones '
                              '[S0AC7agW8Uc @ 00:01:11]. Kanerika pushes back on the comfort of '
                              "predictable credit pricing: Snowflake's model is only a trap if you fall "
                              'asleep at the wheel, but without monitors the bill can scale into the '
                              'stratosphere, while Databricks layers DBUs on top of a separate cloud bill '
                              '[mhNqARg0Yi8 @ 00:09:41]. The Data & AI Playground refuses to crown either '
                              'side, stating that neither platform is inherently cheaper, comparing '
                              'Snowflake to a taxi and Databricks to leasing a car, and defining total '
                              'cost as platform cost plus engineering hours, ops overhead and migration '
                              'risk [yhgHAMKkOqc @ 00:07:42]. Where they converge is the hybrid endgame. '
                              'Kanerika predicts many large organizations will run both, and the '
                              "Playground's five-question framework treats a split result as a proven, "
                              'real-world architecture rather than indecision [yhgHAMKkOqc @ 00:09:26]. '
                              "The Playground's opening warning applies to both camps: never decide from a "
                              'vendor demo.',
                              'Negotiation posture splits the same way. Virtualization Options teaches '
                              "walk-away pressure: if a vendor senses you won't walk away, there is no way "
                              'they drop the price, so counter constructive tension by being willing to '
                              'reassign the deal to a competitor or delay the project [fTqBORy9ePo @ '
                              '00:02:45]. Daryl at SAMexpert runs a more collaborative play inside '
                              "Microsoft, telling buyers to understand Microsoft's needs and pull in the "
                              'local office, for example by offering to land SAP HANA on Azure rather than '
                              'AWS, and to time talks to the June year-end [7shzxv1SUFc @ 01:14:13]. On '
                              'services pricing, the SaaS CFO says 45 to 50 percent margins are achievable '
                              'with fixed-fee packages and treats 35 percent as the ideal [gQvlawVvuzw @ '
                              '00:02:17]. Graham at ISM New Jersey sees the buy side differently: time and '
                              'materials is by far the most popular model out of necessity, fixed fee only '
                              "works if scope won't creep, and bonus structures raise the question of who "
                              'pays [ZeVBT8JVp-U @ 00:36:12]. Even the price caps differ: Virtualization '
                              "Options' negotiation guide sets a hard 3 percent escalator maximum, while "
                              'its procurement guides allow a 3 to 5 percent multi-year lock, with net 90 '
                              'payment terms offered as the fallback when list price is called firm.'],
               'table': {'caption': 'Contested Playbooks: Audits, Platforms, Price Caps and Services '
                                    'Pricing',
                         'headers': ['Contested Question', 'Position A', 'Position B', 'Expert Source'],
                         'rows': [['Is a Microsoft audit fair process or pure leverage?',
                                   'Innovia: Microsoft has been very fair on compliance issues in all '
                                   'cases',
                                   'SAMexpert: the idea of an audit is leverage, and mistakes always favor '
                                   'Microsoft',
                                   'Innovia Consulting ([WV0uRh3yMX4 @ 00:01:56]); SAMexpert TV – '
                                   'Microsoft Licensing and Cloud ([7shzxv1SUFc @ 00:42:05])'],
                                  ['What a partner-led SAM engagement is really for',
                                   'Innovia: a voluntary review where Microsoft pays the partner for the '
                                   'work',
                                   "SAMexpert: the partner must upsell a multiple of Microsoft's "
                                   'investment or lose business',
                                   'Innovia Consulting ([WV0uRh3yMX4 @ 00:17:39]); SAMexpert TV – '
                                   'Microsoft Licensing and Cloud ([7shzxv1SUFc @ 00:08:52])'],
                                  ['How seriously to take escalation and legal threats',
                                   'Innovia: ignored requests eventually trigger a punitive Legal '
                                   'Contracts and Compliance audit',
                                   'SAMexpert: do not fear threats, court action is super extreme in '
                                   "today's environment",
                                   'Innovia Consulting ([WV0uRh3yMX4 @ 00:19:16]); SAMexpert TV – '
                                   'Microsoft Licensing and Cloud ([7shzxv1SUFc @ 01:16:06])'],
                                  ['Where to set the annual price escalator ceiling',
                                   'Negotiation guide: cap annual price escalators at a hard maximum of 3 '
                                   'percent',
                                   'Procurement guides: demand a 3 to 5 percent multi-year lock or net 90 '
                                   'terms',
                                   'Virtualization Options LLC Free Learning Portal ([fTqBORy9ePo @ '
                                   '00:06:41]); Virtualization Options LLC Free Learning Portal '
                                   '([L-DrE5qghM8 @ 00:05:51])'],
                                  ['Does platform lock-in actually buy better security posture?',
                                   'Snowflake speaker: calling lock-in more secure is a myth, open '
                                   'platforms are safer',
                                   'Kanerika: Unity Catalog needs self-configured RBAC while Snowflake '
                                   'enforces MFA by default',
                                   'Snowflake Inc. ([S0AC7agW8Uc @ 00:01:11]); Kanerika Inc. ([mhNqARg0Yi8 '
                                   '@ 00:11:10])'],
                                  ['Which data platform is actually cheaper to operate long term?',
                                   'Kanerika: Snowflake stays predictable until unmonitored bills scale '
                                   'into the stratosphere',
                                   'Playground: neither platform is inherently cheaper, it is taxi versus '
                                   'leased car',
                                   'Kanerika Inc. ([mhNqARg0Yi8 @ 00:09:41]); The Data & AI Playground '
                                   '([yhgHAMKkOqc @ 00:07:42])'],
                                  ['Best pricing model for professional services engagements',
                                   'SaaS CFO: fixed-fee packages make 45 to 50 percent services margins '
                                   'achievable',
                                   'ISM New Jersey: time and materials dominates, fixed fee works only '
                                   'without scope creep',
                                   'The SaaS CFO ([gQvlawVvuzw @ 00:02:17]); ISM New Jersey ([ZeVBT8JVp-U '
                                   '@ 00:36:12])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["The most expensive failure is accepting an auditor's spreadsheet at face "
                              "value. SAMexpert's Daryl says every audit contains mistakes, that without "
                              'someone who understands the calculation you will be overpaying, and that '
                              'the mistakes are always in favor of Microsoft [7shzxv1SUFc @ 00:42:05]. The '
                              'SAMexpert hosts explain why: the auditors are often apprentices with two to '
                              'four years in the industry, the MLS they work from is incomplete, CSP never '
                              'appears in it, and OEM and ISV entitlements such as Commvault and NICE get '
                              'missed, which can mean hundreds of thousands of dollars in SQL licensing '
                              '[7shzxv1SUFc @ 00:38:28]. Excel errors show up in every audit, and mistakes '
                              'corrected in one ELP version can quietly reappear in the next [7shzxv1SUFc '
                              '@ 00:43:38]. Fatigue makes it worse: when auditors get fed up they will '
                              'extrapolate twenty or thirty forward just to close the order. '
                              'Over-reporting is a separate leak. Alexander Goliff describes one hosting '
                              'provider that was short €4M while having already overpaid €11M, and audits '
                              'ignored the overpayment entirely [S-D4c7b8-94 @ 00:45:40]. The economics '
                              'check is the size of the opening number: Microsoft pushes the CIO or CFO '
                              'toward an early commercial close, and walking in with a $1M disputed figure '
                              'is a very different negotiation from walking in with 50k.',
                              "Margin blindness is the quiet killer on the reseller side. In Goliff's "
                              'survey of 200-plus hosting providers, 19 percent do not measure SPLA '
                              'profitability at all, 23 percent use no reporting tools, and 13 percent '
                              'either break even or earn about 5 percent [S-D4c7b8-94 @ 00:10:32]. '
                              'Meanwhile SPLA prices climb about 10 percent a year and Goliff says '
                              'providers can do nearly nothing about it. Counting errors compound the '
                              'damage: per-user licensing must include everyone authorized through any '
                              'remote desktop tool, uncounted security groups or domain users inflate the '
                              'numbers, and penalties reach back 30 to 60 months. One firm with £200K in '
                              'profit faced an initial penalty of about £3M [S-D4c7b8-94 @ 00:17:06]. '
                              'Goliff also warns that roughly half of AI-sourced licensing information is '
                              'rubbish and that no tool can be set and forgotten. The SaaS CFO sees the '
                              'same pattern in services: mispriced services lose money and consume cash as '
                              'you scale [gQvlawVvuzw @ 00:02:03], and sales tends to discount services '
                              'first, so chasing 50 percent services margins at the expense of ARR '
                              'discounts is a trap [gQvlawVvuzw @ 00:02:36]. The upside is real: Goliff '
                              'cites inbound costs cut 30 percent, lifting SPLA margin from roughly 5 to '
                              '35 percent.',
                              "Self-inflicted procurement leaks round out the failure list. Innovia's "
                              'licensing team warns that buying software on eBay is a risky business: keys '
                              'get deactivated after 30, 60 or 90 days, and fake partner vendors are in '
                              'circulation [WV0uRh3yMX4 @ 00:34:47]. Simply installing software creates '
                              'the need for a license, which is how one standard image put unused Project '
                              'on 50 laptops, and removing software after an audit notice counts as a '
                              'violation. Buying from scattered vendors such as CDW and Best Buy left one '
                              'customer photographing keys and digging up old receipts. On the CSP side, '
                              'Amy at Heartland Business Systems flags partners who do not help with '
                              'renewals, which risks buying or renewing excess quantities, plus missing '
                              'transparency on order status and pricing [jqaG0NHe-0c @ 00:00:21]. Tooling '
                              'is not a rescue either: Alex at SAMexpert imported a 10,000-record MLS into '
                              'a tool and spent six years sorting it out, auditors ignore built-in '
                              'compliance reports, and one tool failed to recognize SQL Server 2019 for '
                              'months [7shzxv1SUFc @ 01:19:36]. Graham at ISM New Jersey adds the '
                              'organizational version of the same leak: stakeholders use the back door to '
                              'circumvent procurement, and supplier-written statements of work are a '
                              'separate warning [ZeVBT8JVp-U @ 00:09:35].'],
               'table': {'caption': 'Firsthand Traps and the Economics Behind Them',
                         'headers': ['Trap', 'What Went Wrong', 'Economics Check', 'Expert Source'],
                         'rows': [['Hosting user counts inflated by uncounted groups',
                                   'Security groups or domain users inflate per-user counts across remote '
                                   'desktop tools',
                                   'A firm with £200K profit faced roughly £3M initial penalty',
                                   'SAMexpert TV – Microsoft Licensing and Cloud ([S-D4c7b8-94 @ '
                                   '00:17:06])'],
                                  ['Overpayments never credited back during the audit',
                                   'Provider came up short €4M after already overpaying €11M',
                                   'Audits ignore overpayments, so over-reporting is pure lost margin',
                                   'SAMexpert TV – Microsoft Licensing and Cloud ([S-D4c7b8-94 @ '
                                   '00:45:40])'],
                                  ['Crossing the 5 percent non-compliance threshold line',
                                   'Licenses priced at 125 percent of discounted price list plus audit '
                                   'fees',
                                   'Formal documents show audit fees from $27-28k to about $40k',
                                   'SAMexpert TV – Microsoft Licensing and Cloud ([7shzxv1SUFc @ '
                                   '00:18:31])'],
                                  ['Buying grey-market license keys on eBay',
                                   'Keys get deactivated after 30, 60 or 90 days; fake partner vendors '
                                   'exist',
                                   'Cheap keys can go dark within 30 to 90 days of purchase',
                                   'Innovia Consulting ([WV0uRh3yMX4 @ 00:35:28])'],
                                  ['Auditor extrapolation once their patience runs out',
                                   'Fed-up auditors extrapolate 20 or 30 forward just to close the order',
                                   'Snow data covering only 85 percent failed a 100 percent coverage '
                                   'demand',
                                   'SAMexpert TV – Microsoft Licensing and Cloud ([7shzxv1SUFc @ '
                                   '00:36:59])'],
                                  ['Mispriced professional services quietly eating cash',
                                   'Services priced too low lose money and consume cash as you scale',
                                   'Median services margin is 35 percent; bottom quartile only 15 percent',
                                   'The SaaS CFO ([gQvlawVvuzw @ 00:01:40])'],
                                  ['Over-utilized or idle professional services bench',
                                   'Utilization above 80 percent risks burnout; below 70 means something '
                                   'is wrong',
                                   'Backlog in months dropping to three triggers pipeline and staffing '
                                   'checks',
                                   'The SaaS CFO ([pC3bnU1ivL8 @ 00:01:55]); The SaaS CFO ([X9tvWcO_2KI @ '
                                   '00:00:58])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Stop-Ship Checks Before Any Audit Figure or Renewal Gets Signed',
                           'body': 'Every item below comes from a loss, overpayment or penalty the '
                                   'practitioners saw firsthand. Clear all four before a number leaves the '
                                   'building.',
                           'items': ['Sign a direct NDA with the auditor at kickoff and hand over no data, '
                                     'not even the org structure, because an acquisition may breach the EA '
                                     'affiliate threshold [SAMexpert TV – Microsoft Licensing and Cloud — '
                                     '7shzxv1SUFc @ 00:54:49].',
                                     'Keep a written protocol of disagreement throughout the audit, '
                                     'because the technical analysis cannot be reopened later without '
                                     'extra fees [SAMexpert TV – Microsoft Licensing and Cloud — '
                                     '7shzxv1SUFc @ 01:09:04].',
                                     'Confirm per-user SPLA counts include everyone authorized through any '
                                     'remote desktop tool such as VNC, Guacamole or TeamViewer before the '
                                     'next report [SAMexpert TV – Microsoft Licensing and Cloud — '
                                     'S-D4c7b8-94 @ 00:14:57].',
                                     'If the CSP partner offers no renewal help, pricing transparency or '
                                     'self-service portal, use the midterm transfer tool instead of '
                                     'waiting for renewal [Heartland Business Systems — jqaG0NHe-0c @ '
                                     '00:00:57].']}}],
 'pull_quote': "Every audit there are mistakes we find; if you don't have somebody who understands how "
               'this is calculated you will be overpaying, I promise you. Attributed to SAMexpert TV – '
               'Microsoft Licensing and Cloud (7shzxv1SUFc @ 00:41:46).',
 'diagram_id': 'diag-08',
 'action_checklist': ['Run a costed exit pilot as the most impactful lever, sequenced after baseline '
                      'hardware metrics, consolidation and per-cluster bundle scoping, and take the '
                      'discount last [Virtualization Options LLC Free Learning Portal — fTqBORy9ePo @ '
                      '00:05:39].',
                      'Apply a 50% realization haircut to every vendor TCO or ROI model and separate hard '
                      'savings from soft labor savings [Virtualization Options LLC Free Learning Portal — '
                      'fTqBORy9ePo @ 00:04:03].',
                      'Set audit parameters before signature: what triggers an audit, a cap on true-up '
                      'costs, and a limit on audit frequency [Virtualization Options LLC Free Learning '
                      'Portal — L-DrE5qghM8 @ 00:05:20].',
                      'Cap annual increases at 3-5%, require 90-day auto-renewal notice windows and early '
                      'termination rights, and enforce fixed-fee SOWs with NTE caps [Virtualization '
                      'Options LLC Free Learning Portal — xP4R2F8hbBw @ 00:07:26].',
                      'Stand up an audit team of SecOps, procurement, ITAM, the licensing-design owner and '
                      'legal so Microsoft cannot divide and conquer the CIO [SAMexpert TV – Microsoft '
                      'Licensing and Cloud — 7shzxv1SUFc @ 00:51:15].',
                      'Track services backlog, backlog in months, billable utilization and services '
                      'margins, targeting 70-80% utilization and 30-35% margin [The SaaS CFO — X9tvWcO_2KI '
                      '@ 00:00:28].'],
 'statutory_citations': [{'title': 'SAMexpert TV – Microsoft Licensing and Cloud — Microsoft Licensing '
                                   'Audit Readiness and Audit Defence: a survival guide [Training 6/8] '
                                   '[00:42:05]',
                          'url': 'https://www.youtube.com/watch?v=7shzxv1SUFc&t=2525s',
                          'relevance': 'Primary practitioner testimony on auditor errors, penalty math and '
                                       'Microsoft audit defense.'},
                         {'title': 'Innovia Consulting — Would Your Company Pass a Licensing Audit '
                                   '[00:11:36]',
                          'url': 'https://www.youtube.com/watch?v=WV0uRh3yMX4&t=696s',
                          'relevance': 'Primary practitioner testimony on audit selection, self-audit '
                                       'deadlines and non-compliance causes.'},
                         {'title': 'SAMexpert TV – Microsoft Licensing and Cloud — Protecting Your Hosting '
                                   'Margin as the Rules of the Game Change [00:17:06]',
                          'url': 'https://www.youtube.com/watch?v=S-D4c7b8-94&t=1026s',
                          'relevance': 'Primary practitioner testimony on SPLA margin, user-count '
                                       'penalties and over-reporting losses.'},
                         {'title': 'Virtualization Options LLC Free Learning Portal — Enterprise '
                                   'Procurement Secrets: How to Win the License Audit War [00:03:50]',
                          'url': 'https://www.youtube.com/watch?v=L-DrE5qghM8&t=230s',
                          'relevance': 'Primary practitioner testimony on pre-signature leverage and '
                                       'contractual audit controls.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'fTqBORy9ePo',
                       'title': 'Enterprise Software Vendors HATE When You Use This Negotiation Tactic',
                       'channel': 'Virtualization Options LLC Free Learning Portal',
                       'author': 'Virtualization Options LLC Free Learning Portal',
                       'text': "If they sense you won't walk away, there's absolutely no way they're "
                               'dropping the price.',
                       'tip': "If they sense you won't walk away, there's absolutely no way they're "
                              'dropping the price.',
                       'timestamp': 180,
                       'timestamp_seconds': 180,
                       'timestamp_label': '[00:03:00]',
                       'url': 'https://www.youtube.com/watch?v=fTqBORy9ePo&t=180s',
                       'markdown': '[00:03:00](https://www.youtube.com/watch?v=fTqBORy9ePo&t=180s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'V9sCxI7fIKk',
                       'title': "AI's Double-Edged Sword for Cybersecurity: Outlook for CRWD, PANW, OKTA",
                       'channel': 'Schwab Network',
                       'author': 'Schwab Network',
                       'text': 'The market is bringing all that growth too much into the near term.',
                       'tip': 'The market is bringing all that growth too much into the near term.',
                       'timestamp': 204,
                       'timestamp_seconds': 204,
                       'timestamp_label': '[00:03:24]',
                       'url': 'https://www.youtube.com/watch?v=V9sCxI7fIKk&t=204s',
                       'markdown': '[00:03:24](https://www.youtube.com/watch?v=V9sCxI7fIKk&t=204s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gQvlawVvuzw',
                       'title': 'My Top 4 Professional Services Metrics – Services Margins | SaaS Metrics '
                                'School',
                       'channel': 'The SaaS CFO',
                       'author': 'The SaaS CFO',
                       'text': "Don't chase 50% services margins at the cost of ARR discounts, because "
                               'sales tends to discount services first.',
                       'tip': "Don't chase 50% services margins at the cost of ARR discounts, because "
                              'sales tends to discount services first.',
                       'timestamp': 156,
                       'timestamp_seconds': 156,
                       'timestamp_label': '[00:02:36]',
                       'url': 'https://www.youtube.com/watch?v=gQvlawVvuzw&t=156s',
                       'markdown': '[00:02:36](https://www.youtube.com/watch?v=gQvlawVvuzw&t=156s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'pC3bnU1ivL8',
                       'title': 'My Top 4 Professional Services Metrics – Billable Utilization | SaaS '
                                'Metrics School',
                       'channel': 'The SaaS CFO',
                       'author': 'The SaaS CFO',
                       'text': 'Target 70 to 80% billable utilization, because above 80% risks burnout and '
                               "below 70% means there isn't enough work or something is wrong.",
                       'tip': 'Target 70 to 80% billable utilization, because above 80% risks burnout and '
                              "below 70% means there isn't enough work or something is wrong.",
                       'timestamp': 115,
                       'timestamp_seconds': 115,
                       'timestamp_label': '[00:01:55]',
                       'url': 'https://www.youtube.com/watch?v=pC3bnU1ivL8&t=115s',
                       'markdown': '[00:01:55](https://www.youtube.com/watch?v=pC3bnU1ivL8&t=115s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'BmR1sqXk9DA',
                       'title': 'Effortless SAP Integration with CodeMeter License Central: Scenarios, '
                                'Benefits, and Key Features',
                       'channel': 'WIBU-SYSTEMS AG',
                       'author': 'WIBU-SYSTEMS AG',
                       'text': 'The LCC connector eliminates interface programming and cuts project '
                               'duration and cost significantly without interfering with standard SAP '
                               'flows.',
                       'tip': 'The LCC connector eliminates interface programming and cuts project '
                              'duration and cost significantly without interfering with standard SAP '
                              'flows.',
                       'timestamp': 110,
                       'timestamp_seconds': 110,
                       'timestamp_label': '[00:01:50]',
                       'url': 'https://www.youtube.com/watch?v=BmR1sqXk9DA&t=110s',
                       'markdown': '[00:01:50](https://www.youtube.com/watch?v=BmR1sqXk9DA&t=110s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'X9tvWcO_2KI',
                       'title': 'My Top 4 Professional Services Metrics | SaaS Metrics School | SaaS '
                                'Professional Services',
                       'channel': 'The SaaS CFO',
                       'author': 'The SaaS CFO',
                       'text': '30 35% is a good target.',
                       'tip': '30 35% is a good target.',
                       'timestamp': 89,
                       'timestamp_seconds': 89,
                       'timestamp_label': '[00:01:29]',
                       'url': 'https://www.youtube.com/watch?v=X9tvWcO_2KI&t=89s',
                       'markdown': '[00:01:29](https://www.youtube.com/watch?v=X9tvWcO_2KI&t=89s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZeVBT8JVp-U',
                       'title': 'Professional Services Category Spotlight',
                       'channel': 'ISM New Jersey',
                       'author': 'ISM New Jersey',
                       'text': 'Stakeholders use the back door to circumvent procurement.',
                       'tip': 'Stakeholders use the back door to circumvent procurement.',
                       'timestamp': 575,
                       'timestamp_seconds': 575,
                       'timestamp_label': '[00:09:35]',
                       'url': 'https://www.youtube.com/watch?v=ZeVBT8JVp-U&t=575s',
                       'markdown': '[00:09:35](https://www.youtube.com/watch?v=ZeVBT8JVp-U&t=575s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'S0AC7agW8Uc',
                       'title': 'Snowflake vs Databricks: Why Interoperability Matters for AI Agents',
                       'channel': 'Snowflake Inc.',
                       'author': 'Snowflake Inc.',
                       'text': "In fact, they're more secure than platforms that are closed.",
                       'tip': "In fact, they're more secure than platforms that are closed.",
                       'timestamp': 88,
                       'timestamp_seconds': 88,
                       'timestamp_label': '[00:01:28]',
                       'url': 'https://www.youtube.com/watch?v=S0AC7agW8Uc&t=88s',
                       'markdown': '[00:01:28](https://www.youtube.com/watch?v=S0AC7agW8Uc&t=88s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mhNqARg0Yi8',
                       'title': 'Databricks vs Snowflake 2026: Pricing, AI, Security Compared',
                       'channel': 'Kanerika Inc.',
                       'author': 'Kanerika Inc.',
                       'text': "Snowflake's predictable pricing is only a trap if you fall asleep at the "
                               'wheel, but without monitors the bill can scale into the stratosphere.',
                       'tip': "Snowflake's predictable pricing is only a trap if you fall asleep at the "
                              'wheel, but without monitors the bill can scale into the stratosphere.',
                       'timestamp': 581,
                       'timestamp_seconds': 581,
                       'timestamp_label': '[00:09:41]',
                       'url': 'https://www.youtube.com/watch?v=mhNqARg0Yi8&t=581s',
                       'markdown': '[00:09:41](https://www.youtube.com/watch?v=mhNqARg0Yi8&t=581s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yhgHAMKkOqc',
                       'title': 'Databricks vs Snowflake -Complete Architectural and Technical Decision '
                                'Framework',
                       'channel': 'The Data & AI Playground',
                       'author': 'The Data & AI Playground',
                       'text': 'The best platform in the world is useless if your team cannot operate it.',
                       'tip': 'The best platform in the world is useless if your team cannot operate it.',
                       'timestamp': 462,
                       'timestamp_seconds': 462,
                       'timestamp_label': '[00:07:42]',
                       'url': 'https://www.youtube.com/watch?v=yhgHAMKkOqc&t=462s',
                       'markdown': '[00:07:42](https://www.youtube.com/watch?v=yhgHAMKkOqc&t=462s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7shzxv1SUFc',
                       'title': 'Microsoft Licensing Audit Readiness and Audit Defence: a survival guide '
                                '[Training 6/8]',
                       'channel': 'SAMexpert TV – Microsoft Licensing and Cloud',
                       'author': 'SAMexpert TV – Microsoft Licensing and Cloud',
                       'text': "Every audit there are mistakes we find; if you don't have somebody who "
                               'understands how this is calculated you will be overpaying, I promise you.',
                       'tip': "Every audit there are mistakes we find; if you don't have somebody who "
                              'understands how this is calculated you will be overpaying, I promise you.',
                       'timestamp': 2506,
                       'timestamp_seconds': 2506,
                       'timestamp_label': '[00:41:46]',
                       'url': 'https://www.youtube.com/watch?v=7shzxv1SUFc&t=2506s',
                       'markdown': '[00:41:46](https://www.youtube.com/watch?v=7shzxv1SUFc&t=2506s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7shzxv1SUFc',
                       'title': 'Microsoft Licensing Audit Readiness and Audit Defence: a survival guide '
                                '[Training 6/8]',
                       'channel': 'SAMexpert TV – Microsoft Licensing and Cloud',
                       'author': 'SAMexpert TV – Microsoft Licensing and Cloud',
                       'text': "The idea of an audit is to create leverage, that's the bottom line.",
                       'tip': "The idea of an audit is to create leverage, that's the bottom line.",
                       'timestamp': 106,
                       'timestamp_seconds': 106,
                       'timestamp_label': '[00:01:46]',
                       'url': 'https://www.youtube.com/watch?v=7shzxv1SUFc&t=106s',
                       'markdown': '[00:01:46](https://www.youtube.com/watch?v=7shzxv1SUFc&t=106s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WV0uRh3yMX4',
                       'title': 'Would Your Company Pass a Licensing Audit',
                       'channel': 'Innovia Consulting',
                       'author': 'Innovia Consulting',
                       'text': 'I will warn you that buying software on eBay is a risky business.',
                       'tip': 'I will warn you that buying software on eBay is a risky business.',
                       'timestamp': 2087,
                       'timestamp_seconds': 2087,
                       'timestamp_label': '[00:34:47]',
                       'url': 'https://www.youtube.com/watch?v=WV0uRh3yMX4&t=2087s',
                       'markdown': '[00:34:47](https://www.youtube.com/watch?v=WV0uRh3yMX4&t=2087s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'L-DrE5qghM8',
                       'title': 'Enterprise Procurement Secrets: How to Win the License Audit War',
                       'channel': 'Virtualization Options LLC Free Learning Portal',
                       'author': 'Virtualization Options LLC Free Learning Portal',
                       'text': 'The critical point here is that the only moment of genuine enterprise '
                               'leverage is before the signature line.',
                       'tip': 'The critical point here is that the only moment of genuine enterprise '
                              'leverage is before the signature line.',
                       'timestamp': 230,
                       'timestamp_seconds': 230,
                       'timestamp_label': '[00:03:50]',
                       'url': 'https://www.youtube.com/watch?v=L-DrE5qghM8&t=230s',
                       'markdown': '[00:03:50](https://www.youtube.com/watch?v=L-DrE5qghM8&t=230s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xP4R2F8hbBw',
                       'title': '9 The Truth About Enterprise Software Procurement (And How to Fight Back)',
                       'channel': 'Virtualization Options LLC Free Learning Portal',
                       'author': 'Virtualization Options LLC Free Learning Portal',
                       'text': 'Also, enforce fixed fee statements of work with not to exceed or NTE caps.',
                       'tip': 'Also, enforce fixed fee statements of work with not to exceed or NTE caps.',
                       'timestamp': 446,
                       'timestamp_seconds': 446,
                       'timestamp_label': '[00:07:26]',
                       'url': 'https://www.youtube.com/watch?v=xP4R2F8hbBw&t=446s',
                       'markdown': '[00:07:26](https://www.youtube.com/watch?v=xP4R2F8hbBw&t=446s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'S-D4c7b8-94',
                       'title': 'Protecting Your Hosting Margin as the Rules of the Game Change',
                       'channel': 'SAMexpert TV – Microsoft Licensing and Cloud',
                       'author': 'SAMexpert TV – Microsoft Licensing and Cloud',
                       'text': "You can't set and forget any tool, neither a security tool nor ERP nor any "
                               'IT tool; every tool requires babysitting and steering.',
                       'tip': "You can't set and forget any tool, neither a security tool nor ERP nor any "
                              'IT tool; every tool requires babysitting and steering.',
                       'timestamp': 1120,
                       'timestamp_seconds': 1120,
                       'timestamp_label': '[00:18:40]',
                       'url': 'https://www.youtube.com/watch?v=S-D4c7b8-94&t=1120s',
                       'markdown': '[00:18:40](https://www.youtube.com/watch?v=S-D4c7b8-94&t=1120s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jqaG0NHe-0c',
                       'title': 'Get the Most from Your Microsoft Licensing: How to Switch to the Right '
                                'Cloud Solution Provider (CSP)',
                       'channel': 'Heartland Business Systems',
                       'author': 'Heartland Business Systems',
                       'text': 'Customers can now transfer subscriptions midterm to a CSP partner of their '
                               'choice, and the transfer tool can be used at any point in time.',
                       'tip': 'Customers can now transfer subscriptions midterm to a CSP partner of their '
                              'choice, and the transfer tool can be used at any point in time.',
                       'timestamp': 57,
                       'timestamp_seconds': 57,
                       'timestamp_label': '[00:00:57]',
                       'url': 'https://www.youtube.com/watch?v=jqaG0NHe-0c&t=57s',
                       'markdown': '[00:00:57](https://www.youtube.com/watch?v=jqaG0NHe-0c&t=57s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'}]}
