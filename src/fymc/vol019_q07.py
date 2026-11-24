from __future__ import annotations

CHAPTER_7 = {'id': 'Q7',
 'chapter_id': 'Q7',
 'chapter_number': 7,
 'question_number': 7,
 'slug': 'finops-for-saas-and-licensing',
 'question_prompt': 'How do enterprises apply FinOps to SaaS and licensing spend, and what does that mean '
                    'for the vendors and resellers who sell to them?',
 'kicker': 'Q7 / THE BIG MONEY PLAYBOOKS',
 'title': 'FinOps for SaaS and Licensing',
 'subtitle': 'FinOps fundamentals and scopes, SaaS spend at Priceline and Danske Bank, ITAM/SAM '
             'intersections, Microsoft 365 license optimization, ServiceNow SaaS license management, '
             'AI-assisted SaaS cost modules, Datadog cloud cost optimization, and State of FinOps trends',
 'layout_template': 'thirty_day_roadmap',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners from Priceline, Danske Bank, Roku, Under Armour and Avala treat SaaS '
                      "and licensing as a second cloud bill carrying the same waste rate. Gartner's "
                      'up-to-30% figure is quoted repeatedly, and SaaS now sits inside 90% of FinOps '
                      'scopes. The consensus mechanics are to build one central vendor list, rank it by '
                      'spend, focus on the top 20 to 25 vendors, and use identity and SSO data to reclaim '
                      "inactive seats on 30- or 90-day thresholds. Street numbers include Danske's 3,000 "
                      'discovered apps against a 600-800 target, a concurrent-license cut from 50 seats to '
                      "20 after peak use of 15, Mason's $100K shortfall example on a $1M commit, and soft "
                      'caps giving 20% free overage. Disagreements center on headline waste stats (Danske '
                      'rejects the 50% figure), on central versus business-unit ownership, and on whether '
                      'a tool or Excel comes first.',
 'key_metrics': [{'label': 'SaaS spend lost to waste',
                  'metric': 'SaaS spend lost to waste',
                  'value': 'Up to 30% of SaaS spend',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Chris Reed of Priceline cites Gartner: up to 30% of SaaS spend is waste, the '
                             'same figure quoted for cloud.',
                  'source': 'FinOps Foundation ([hQDjTANIaTo @ 00:04:01])'},
                 {'label': 'Danske Bank application sprawl',
                  'metric': 'Danske Bank application sprawl',
                  'value': '3,000 apps found over two years; target estate of 600-800',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Scott Beasley reports what near-real-time discovery surfaced at a bank of '
                             'about 22,000 employees, with about 100 new apps appearing per month.',
                  'source': 'FinOps Foundation ([F-5GIklN_Ps @ 00:04:28])'},
                 {'label': 'Concurrent license right-size',
                  'metric': 'Concurrent license right-size',
                  'value': 'Peak use of 15 of 50 seats; contract cut to 20',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Peter Greenshaw used a manually built heat map to size concurrent licenses '
                             'to actual peak demand.',
                  'source': 'FinOps Weekly ([sqpO85TKjEI @ 00:11:09])'},
                 {'label': 'Commitment shortfall exposure',
                  'metric': 'Commitment shortfall exposure',
                  'value': '$100K owed on a $1M 12-month commit with $900K spent',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Derer Mason of Roku explains that a mini business case committing $1.2M may '
                             'get the shortfall forgiven.',
                  'source': 'FinOps Foundation ([LF1AK1WypX0 @ 00:14:06])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every operator on this circuit treats SaaS and licensing as a second cloud '
                              'bill hiding in plain sight. Chris Reed runs IT finance inside the Priceline '
                              'CTO org and owns the full tech budget. Reed ranks software as the '
                              'number-two spend after cloud and repeats the Gartner line that up to 30% of '
                              'SaaS spend is waste, the same ratio quoted for cloud [hQDjTANIaTo @ '
                              '00:04:01]. Eddy Says Hi goes further, arguing that software spend can be '
                              "'as big, if not bigger' than infrastructure and using a mortgage analogy to "
                              'land the point [sIJo4dVD-jc @ 00:01:02]. At the Applying the FinOps '
                              'Framework session, Amy Ashby of Under Armour and Lindberg, director of cost '
                              'optimization at Avala, stacked the waste figures. More than 30% of desktop, '
                              'software and SaaS spend is wasted, 50% of installed software sits unused, '
                              'and SaaS overspend is projected at 25% [iIwpcQbBkmM @ 00:01:29]. The State '
                              'of FinOps 2026 numbers presented by Steve Trasch show the mandate has '
                              'already landed. SaaS now sits inside 90% of FinOps scopes, and nearly half '
                              'of practices also manage data center spend [O3FqsxJScI4 @ 00:10:51]. The '
                              'operating conclusion is blunt: a FinOps practice that stops at the cloud '
                              'invoice is ignoring a cost pool of comparable size carrying the same waste '
                              'rate.',
                              'The second point of agreement is that visibility comes before any '
                              'negotiation, and that it starts crude. Peter Greenshaw, interviewed by '
                              'FinOps Weekly, lays out the order: build one central vendor list, rank it '
                              'by spend, deep-dive the contracts at the top, and run the cycle year-round '
                              'instead of only at budget season [sqpO85TKjEI @ 00:05:26]. Scott Beasley at '
                              'Danske Bank, roughly 22,000 employees, shows what that list looks like once '
                              'discovery is switched on. Over two years, 3,000 applications surfaced, the '
                              'target estate is 600 to 800, and about 100 new apps appear every month '
                              'through near-real-time discovery [F-5GIklN_Ps @ 00:04:28]. Reed starts from '
                              'the P&L and pulls the highest software categories. Each one is classified '
                              'as usage-based or license-based, and then vendors are asked for monthly '
                              "utilization reports, a request vendors answered with 'no one has ever asked "
                              "us' [hQDjTANIaTo @ 00:13:11]. The 2026 trends podcast on Eddy Says Hi names "
                              "the control point those lists hang from: 'Identity is rapidly becoming the "
                              "primary control plane for SAS cost management' [byD2FJ-NF0M @ 00:12:17]. "
                              'That is why SSO and identity data feed nearly every reclaim workflow in the '
                              'mechanics below. Nobody on the circuit waits for a perfect tool before '
                              'starting this inventory; the first pass is a list, not a platform.',
                              'Third, the practitioners agree on ownership and on where to aim limited '
                              'hours. Derer Mason runs a three-person Cloud CoE at Roku and insists on '
                              'being the single commercial point of contact for every vendor. At the same '
                              "time, Mason acts as 'a facilitator, not the owner' of each contract and "
                              'keeps the whole function centralized [LF1AK1WypX0 @ 00:20:47]. On '
                              "accountability, Reed pulled costs out of a single 'core Tech' bucket and "
                              'pushed them into product cost centers covering hotels, rental cars, flights '
                              'and packages. Reed then published showback with named owners, explicitly '
                              'framed as not a name-and-shame exercise [hQDjTANIaTo @ 00:14:54]. Reed also '
                              'applies the 80/20 cut hard: the top 20 vendors carry roughly 80% of spend, '
                              'so the long tail is simply ignored during audits [hQDjTANIaTo @ 00:33:09]. '
                              'Lindberg lands in the same place with about 25 focus vendors, the top 20% '
                              "of the base. Lindberg's reasoning is that the same hour of optimization "
                              'work returns far more on a $1M vendor than on a $10K one [iIwpcQbBkmM @ '
                              '00:15:37]. The combined rule is simple: one central commercial desk, named '
                              'budget owners who can see their own numbers, and scarce analyst hours '
                              'concentrated on the handful of vendors that actually move the total.'],
               'table': {'caption': 'Where the practitioners line up: the baseline SaaS and licensing '
                                    'FinOps operating rules',
                         'headers': ['Consensus Point',
                                     'What Practitioners Actually Do',
                                     'Why It Pays',
                                     'Expert Source'],
                         'rows': [['SaaS waste mirrors cloud waste levels',
                                   'Treat software as the second-largest tech line after cloud spend',
                                   'Gartner figure cited: up to 30% of SaaS spend is waste',
                                   'FinOps Foundation ([hQDjTANIaTo @ 00:04:01])'],
                                  ['A central vendor list comes first',
                                   'Build one list, rank vendors by spend, deep-dive top contracts',
                                   'Turns a once-a-year budget scramble into a year-round cycle',
                                   'FinOps Weekly ([sqpO85TKjEI @ 00:05:26])'],
                                  ['Discovery exposes far more apps than expected',
                                   'Run near-real-time discovery and set a rationalization target estate',
                                   'Danske found 3,000 apps and now targets 600 to 800',
                                   'FinOps Foundation ([F-5GIklN_Ps @ 00:04:28])'],
                                  ['Roles must be split cleanly, not siloed',
                                   'FinOps orchestrates, ITAM/SAM license, procurement negotiates, '
                                   'engineering tags resources',
                                   'Gives FinOps the orchestration seat across licensing, buying and '
                                   'tagging work',
                                   'Eddy Says Hi #EddySaysHi ([sIJo4dVD-jc @ 00:03:41])'],
                                  ['Identity data is the cost control plane',
                                   'Drive license right-sizing off SSO and identity usage signals directly',
                                   'Entitlements get matched to real usage instead of contract assumptions',
                                   'Eddy Says Hi #EddySaysHi ([byD2FJ-NF0M @ 00:12:17])'],
                                  ['Concentrate effort on the biggest vendors',
                                   'Focus optimization on roughly 25 vendors, the top 20% by spend',
                                   'The same analyst hour returns more on a $1M vendor than on a $10K one',
                                   'FinOps Foundation ([iIwpcQbBkmM @ 00:15:37])'],
                                  ['One commercial point of contact wins',
                                   'Central team fronts every vendor conversation as the single commercial '
                                   'contact',
                                   "Mason's rule: 'make sure you're the single point of contact' with "
                                   'vendors',
                                   'FinOps Foundation ([LF1AK1WypX0 @ 00:20:47])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['License harvesting is where the hard money gets clawed back, and the '
                              'mechanics are already scripted. Michelle Campos of the ServiceNow Community '
                              'ranks integrations by strength: direct vendor integration first, SSO '
                              'through Azure or Okta second, and custom open API last. The Salesforce '
                              'playbook then auto-builds a software model and a reclaim rule with a 30-day '
                              'inactivity threshold. Campos recommends reviewing that threshold and '
                              'possibly stretching it to 90 days [8mJc7j3DW28 @ 00:03:48]. In the live '
                              'demo that rule surfaced 572 reclaim candidates, which can be reclaimed one '
                              'at a time, all at once, or on full automation [8mJc7j3DW28 @ 00:05:14]. '
                              'Scogo AI ran the same play against Microsoft 365 with a natural-language '
                              'prompt in Cira CLI, stripping Business Premium licenses from disabled and '
                              'never-signed-in users. Out of 25 licenses, the available count jumped from '
                              '21 to 24. That is three seats reclaimed, including one the presenter had '
                              'missed, confirmed in the admin portal [hkNjUpPIx6M @ 00:02:27]. Procure '
                              "IT's module hooks the same identity providers (Azure Entra, Okta or G "
                              'Suite) to split power users from light users. The renewal conversation '
                              'therefore starts with a list of who does not need a seat [_PyR6G51QW4 @ '
                              '00:01:11]. Every one of these workflows runs on the same two inputs: an '
                              'identity signal and an inactivity threshold.',
                              'The contract math is where these practitioners get brutally specific. Mason '
                              'walks through the commitment shortfall at Roku. Commit $1M over 12 months, '
                              'spend only $900K, and you owe the vendor $100K. The escape hatch is a mini '
                              'business case committing to $1.2M, which may get the shortfall forgiven '
                              '[LF1AK1WypX0 @ 00:14:06]. The opposite failure bites too. Burn through '
                              'prepaid funds at month nine and the discount ends, forcing an early '
                              'renewal, which matters because some of those Roku discounts run over 90% '
                              '[LF1AK1WypX0 @ 00:15:42]. At the negotiating table, Mason asks for '
                              'discounted overages, free training and support, and an at-will termination '
                              "clause carrying 30, 60 or 90 days' notice [LF1AK1WypX0 @ 00:25:11]. Reed "
                              'bakes soft caps into a standard tech-contract framework originally built at '
                              'UBS, complete with reporting clauses. Usage up to 20% over the cap is free '
                              'in year one, and in year two the customer pays 50% of the delta '
                              '[hQDjTANIaTo @ 00:29:33]. That clause structure converts a surprise true-up '
                              'into a negotiated, predictable ramp. Together these levers turn every '
                              'renewal from a vendor-driven event into a buyer-scheduled one, with the '
                              'shortfall, overage and exit terms written in well before anyone signs.',
                              'Rate versus usage is the sharpest piece of street math on the board, and it '
                              "is where most negotiated wins quietly evaporate. Lindberg's worked example "
                              'is to buy 1,000 licenses up front and watch the rollout take a full year. '
                              'Every gap between contracted and active licenses is pure waste. The '
                              'effective rate, contract cost divided by actual usage, can equal or exceed '
                              'on-demand pricing, so procurement needs to hear that its recorded savings '
                              'are not real [iIwpcQbBkmM @ 00:11:03]. The fix is to buy in steps rather '
                              'than full-year upfront; it annoys accounts payable but saves '
                              "'thousands…hundreds of thousands' [iIwpcQbBkmM @ 00:16:36]. Greenshaw "
                              "attacks the tier mix instead: 'I bet 90% of your organization is just "
                              "updating PDFs and signing them,' so most Adobe users move to cheaper PDF "
                              'tools while creatives keep full licenses [sqpO85TKjEI @ 00:09:41]. On '
                              'concurrent licensing, Greenshaw found peak use of 15 seats against 50 '
                              'purchased and cut to 20. The heat map behind that cut had to be built by '
                              'hand [sqpO85TKjEI @ 00:11:09]. The pattern across all three plays is the '
                              'same: measure actual peak usage first, then buy to that line plus a little '
                              'headroom rather than to whatever volume the vendor proposes.'],
               'table': {'caption': 'Street-level levers with the exact numbers and tools the '
                                    'practitioners reported',
                         'headers': ['Lever',
                                     'Exact Mechanic or Number',
                                     'Tool or Channel Used',
                                     'Expert Source'],
                         'rows': [['Inactive-seat reclaim rule',
                                   'Default 30-day inactivity threshold; review it and consider moving to '
                                   '90 days',
                                   'ServiceNow SaaS License Management Salesforce playbook with automated '
                                   'reclaim',
                                   'ServiceNow Community ([8mJc7j3DW28 @ 00:03:48])'],
                                  ['M365 premium license strip',
                                   '25 Business Premium licenses; available count rose from 21 to 24',
                                   'Natural-language prompt in Cira CLI, verified in the admin portal',
                                   'Scogo AI ([hkNjUpPIx6M @ 00:02:27])'],
                                  ['Concurrent license right-size',
                                   'Peak usage of 15 of 50 seats; contract cut down to 20',
                                   'Manually built usage heat map because the analysis has no native '
                                   'tooling',
                                   'FinOps Weekly ([sqpO85TKjEI @ 00:11:09])'],
                                  ['Commitment shortfall exposure',
                                   '$1M commit, $900K spent, $100K owed unless a $1.2M case forgives it',
                                   'Mini business case presented to the vendor during negotiation',
                                   'FinOps Foundation ([LF1AK1WypX0 @ 00:14:06])'],
                                  ['Soft-cap overage clause',
                                   '20% over the cap is free in year one; 50% of the delta in year two',
                                   'Standard tech-contract framework with reporting clauses, first built '
                                   'at UBS',
                                   'FinOps Foundation ([hQDjTANIaTo @ 00:29:33])'],
                                  ['Discount benchmark at renewal',
                                   '10, 20 or 30% is typical; 5% means not working hard enough',
                                   'Renewal negotiation measured against typical vendor discount bands',
                                   'FinOps Foundation ([iIwpcQbBkmM @ 00:10:20])'],
                                  ['Consumption SKU burn tracking',
                                   'SKU E at 67% of its limit with 42% of the contract elapsed, trend '
                                   'dropping',
                                   'Custom SKU-level report combining contract, usage and billing data',
                                   'FinOps Foundation ([iIwpcQbBkmM @ 00:30:15])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Moves the operators actually run',
                           'body': 'Small, specific plays that the speakers report returning money or '
                                   'leverage at renewal time.',
                           'items': ["Time the negotiation to the vendor's fiscal year-end (April in "
                                     "Mason's worked example), when the vendor needs to close [FinOps "
                                     'Foundation — LF1AK1WypX0 @ 00:24:28].',
                                     'On unmetered enterprise SKUs, Amy Ashby hounded a vendor for months '
                                     'to get a usage extract, found a calculation error, and got a credit '
                                     'back [FinOps Foundation — iIwpcQbBkmM @ 00:41:34].',
                                     'At every renewal, strip out auto-uplifts or drop to a lower tier '
                                     'instead of rolling the contract forward as-is [FinOps Weekly — '
                                     'sqpO85TKjEI @ 00:05:26].',
                                     'Clean up seats before a self-attestation audit, and budget for '
                                     '10-20% organic growth in seat counts [FinOps Foundation — '
                                     'LF1AK1WypX0 @ 00:41:17].']},
               'sop_steps': [{'step': 1,
                              'title': 'Build the central list and rank by spend',
                              'action': 'Pull every SaaS and license vendor into one list, rank them by '
                                        'spend, and deep-dive the top contracts.',
                              'detail': "Greenshaw's sequence is a central list, a spend ranking, and a "
                                        'contract deep-dive, repeated year-round rather than only at '
                                        'budget time [FinOps Weekly — sqpO85TKjEI @ 00:05:26].'},
                             {'step': 2,
                              'title': 'Wire identity data into a reclaim rule',
                              'action': 'Connect direct integrations or SSO, set an inactivity threshold, '
                                        'and reclaim seats in bulk or on automation.',
                              'detail': 'Campos runs the Salesforce playbook with a 30-day inactivity rule '
                                        'and suggests reviewing it and possibly moving it to 90 days '
                                        'before automating reclaim [ServiceNow Community — 8mJc7j3DW28 @ '
                                        '00:03:48].'},
                             {'step': 3,
                              'title': 'Run a renewal calendar with 90-day events',
                              'action': 'Put every renewal on a shared calendar with a 90-day lead event '
                                        'so no contract renews at current usage by default.',
                              'detail': 'Mason uses a renewal calendar with 90-day events to stay ahead of '
                                        'a renewal almost every week [FinOps Foundation — LF1AK1WypX0 @ '
                                        '00:38:33].'},
                             {'step': 4,
                              'title': 'Forecast demand before contacting the vendor',
                              'action': 'Size real demand from utilization data first, then open the '
                                        'negotiation on usage before rate.',
                              'detail': 'Lindberg forecasts demand before sending the first email to the '
                                        'vendor, so the negotiation starts from usage rather than the '
                                        "vendor's proposed volume [FinOps Foundation — iIwpcQbBkmM @ "
                                        '00:14:16].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The first split is who owns the SaaS book. Amy Ashby runs FinOps at Under '
                              'Armour with no central team at all: business units own their SaaS, and '
                              'there is no central tool or process beyond purchasing [iIwpcQbBkmM @ '
                              "00:04:23]. Lindberg's shop at Avala went the opposite direction, recently "
                              'folding IT software into the cost-optimization program so roughly 60% of '
                              'software spend is now managed by one organization [iIwpcQbBkmM @ 00:05:27]. '
                              'Derer Mason at Roku backs centralization from the commercial side and is '
                              "blunt about it: 'make sure you're the single point of contact,' with every "
                              'vendor conversation routed through one desk instead of scattered across '
                              'requesters [LF1AK1WypX0 @ 00:20:47]. Yet Mason draws a line that pure '
                              "centralizers skip, telling operators to be 'a facilitator, not the owner' "
                              'of the contract itself [LF1AK1WypX0 @ 00:37:12]. That distinction is the '
                              "real fork in the road. Ashby's model keeps decisions close to the business "
                              'units that consume the tools but leaves purchasing as the only shared '
                              'checkpoint. The Avala and Roku models concentrate leverage and visibility '
                              "in one function, and Mason's facilitator rule keeps the business owner "
                              'carrying the decision. The operator move: if the org chart will not '
                              'centralize, centralize the vendor contact point and the spend data first, '
                              'then let owners keep the call.',
                              'The second fight is rate versus usage. Derer Mason plays commitment as the '
                              "weapon and reports bluntly that 'some of our discounts are over 90%' "
                              '[LF1AK1WypX0 @ 00:15:42]. Lindberg pushes back on rate obsession. Typical '
                              "vendor discounts land at 10, 20 or 30%, and 'if you're getting 5%' you are "
                              "'not working hard enough' [iIwpcQbBkmM @ 00:10:20]. But Lindberg's core "
                              "warning is that the headline number can lie: 'that best rate you negotiated "
                              "actually may cost you more because of underutilization,' so the ladder is "
                              'to optimize usage rather than rate [iIwpcQbBkmM @ 00:13:59]. Chris Reed at '
                              'Priceline takes a third path and writes elasticity into the paper itself, '
                              'with a soft cap where usage 20% over the cap is free in year one, then 50% '
                              'of the delta is paid in year two [hQDjTANIaTo @ 00:29:33]. That gives '
                              'operators three distinct playbooks: deep commit for discount, usage first '
                              'and rate second, or cap the overage inside the contract. They are not '
                              "mutually exclusive, but they create opposite instincts at renewal. Mason's "
                              "approach leans toward a bigger committed number to unlock price, Lindberg's "
                              'approach leans toward proving utilization before any number reaches the '
                              "vendor, and Reed's approach buys room to be wrong on the forecast.",
                              'The third split is how big the problem really is and what it takes to see '
                              'it. Chris Reed cites Gartner that up to 30% of SaaS spend is waste, the '
                              'same figure Gartner gives for cloud [hQDjTANIaTo @ 00:04:01]. Scott '
                              'Beasley, running ITAM at a 22,000-employee bank in the middle of an AWS '
                              "migration, refuses to accept the popular '50% not being utilized' figure "
                              'for Danske [F-5GIklN_Ps @ 00:06:02]. On tooling, Peter Greenshaw says '
                              "flatly that no tool 'scrapes all of that SaaS data natively' into a single "
                              "pane, and the field's single source of truth is still mostly spreadsheets "
                              '[sqpO85TKjEI @ 00:01:28]. Michelle Campos at ServiceNow shows the opposite '
                              'end of the spectrum, letting the platform surface reclaim candidates, 572 '
                              'of them in one demo, to be reclaimed one at a time, all at once, or fully '
                              'automated [8mJc7j3DW28 @ 00:05:14]. The spreadsheet camp and the platform '
                              'camp are not arguing about whether reclaim works; both assume it does. They '
                              'are arguing about when the tooling pays for itself. The operator read: get '
                              'the first utilization report out of whatever data you already have, then '
                              'automate once the reclaim queue runs into the hundreds.'],
               'table': {'caption': 'Competing SaaS FinOps playbooks, side by side',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Who owns SaaS spend across the business',
                                   'Business units own SaaS with no central FinOps team, tool or process '
                                   'beyond purchasing',
                                   'Centralize under one organization so roughly 60% of software spend '
                                   'sits in one cost-optimization program',
                                   'FinOps Foundation ([iIwpcQbBkmM @ 00:04:23]); FinOps Foundation '
                                   '([iIwpcQbBkmM @ 00:05:27])'],
                                  ['Commercial control over vendor conversations and renewals',
                                   'Be the single commercial point of contact for every vendor '
                                   'conversation and renewal',
                                   'Act as a facilitator, not the owner, so the business owner still holds '
                                   'the contract',
                                   'FinOps Foundation ([LF1AK1WypX0 @ 00:20:47]); FinOps Foundation '
                                   '([LF1AK1WypX0 @ 00:37:12])'],
                                  ['Rate versus usage as the primary savings lever',
                                   'Push commitment hard for deep discounts, with some Roku discounts '
                                   'running over 90%',
                                   'Optimize usage before rate, because the best negotiated rate can cost '
                                   'more through underutilization',
                                   'FinOps Foundation ([LF1AK1WypX0 @ 00:15:42]); FinOps Foundation '
                                   '([iIwpcQbBkmM @ 00:13:59])'],
                                  ['Sizing the SaaS waste baseline for the business case',
                                   'Accept the Gartner figure that up to 30% of SaaS spend is waste, same '
                                   'as cloud',
                                   'Reject the popular 50% not-utilized figure when it does not match what '
                                   'your own estate shows',
                                   'FinOps Foundation ([hQDjTANIaTo @ 00:04:01]); FinOps Foundation '
                                   '([F-5GIklN_Ps @ 00:06:02])'],
                                  ['Tooling for the first utilization report',
                                   'Download the monthly user list into Excel and treat that as the '
                                   'utilization report',
                                   'Let a platform surface reclaim candidates, 572 in one demo, and '
                                   'reclaim them in bulk or automatically',
                                   'FinOps Foundation ([iIwpcQbBkmM @ 00:15:19]); ServiceNow Community '
                                   '([8mJc7j3DW28 @ 00:05:14])'],
                                  ['Whose paper the software contract is written on',
                                   'Bring your own standard tech-contract framework with reporting clauses '
                                   'built in from day one',
                                   "Sign on vendor paper instead; Reed's live poll split roughly 50/50 "
                                   'between the two approaches',
                                   'FinOps Foundation ([hQDjTANIaTo @ 00:27:48])'],
                                  ['The future role of ITAM next to FinOps',
                                   'FinOps acts as the overlayer across ITAM, SAM and ITFM, since ITAM '
                                   'carries no cost component',
                                   'ITAM evolves into a strategic partner to FinOps rather than being '
                                   'replaced by it',
                                   'FinOps Foundation ([hQDjTANIaTo @ 00:36:14]); Eddy Says Hi #EddySaysHi '
                                   '([byD2FJ-NF0M @ 00:05:38])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive surprises arrive at contract end. The Eddy Says Hi '
                              'true-up example is the cleanest: licensed for 100 CPUs, spike to 120, and '
                              "'the vendor can true up your bill to that 120 rate for the entire year,' "
                              'with no true down when usage falls back [sIJo4dVD-jc @ 00:02:38]. Chris '
                              'Reed warns the same mechanic scales up badly, with a three-year '
                              'over-license recoup landing at contract end [hQDjTANIaTo @ 00:23:09]. Derer '
                              'Mason runs the opposite failure, the shortfall: commit $1M over 12 months, '
                              "spend only $900K, and you owe $100K anyway. Mason's escape hatch is a mini "
                              'business case committing $1.2M, which may get the shortfall forgiven '
                              '[LF1AK1WypX0 @ 00:14:06]. Amy Ashby maps how differently vendors punish '
                              'overage: some bill overages at a higher rate, some cut features off, and '
                              'some force a true-up or a higher contract at the end [iIwpcQbBkmM @ '
                              '00:19:57]. Each trap is set at signing and sprung months later. '
                              'Under-forecast and you pay the true-up at the spike rate; over-forecast and '
                              'you pay for the gap you never consumed. Either way, the contract terms '
                              'drive the bill as much as usage does, so read the overage, shortfall and '
                              'true-up clauses before the price line.',
                              'The second failure family is spend nobody signed off on. Chris Reed found '
                              'recurring corporate-card charges still billing after employees left: '
                              "'$5,000 a month, that's 60k a year,' multiplied by 20, plus a $300 charge "
                              'multiplied across 800 other engineers [hQDjTANIaTo @ 00:09:23]. Lindberg '
                              'reports a vendor that allowed overage and then threatened a cutoff at '
                              "renewal, with 'millions of dollars' on the table [iIwpcQbBkmM @ 00:34:27]. "
                              "Derer Mason's version is pure usage velocity: an intern's logging change "
                              'cost $30,000 a day, which is the argument for near-real-time monitoring '
                              'rather than waiting on the invoice [LF1AK1WypX0 @ 00:27:49]. Amy Ashby '
                              "flags load tests as the recurring spike trigger: 'people kicking off load "
                              "tests and then I'm seeing all these SAS products spiked because they're all "
                              "tightly integrated,' and questions whether dev environments even need log "
                              'shipping and advanced analytics [iIwpcQbBkmM @ 00:37:31]. None of these '
                              'losses came from a bad negotiation. They came from usage and purchasing '
                              'that happened outside the renewal conversation, where nobody was watching '
                              'the meter. The economics check is simple: a monthly review catches the '
                              '$5,000 card charge, but only a threshold alert catches a $30,000-a-day '
                              'logging change before it compounds across a billing cycle.',
                              'The third trap is data you cannot get and paper you did not check. Peter '
                              'Greenshaw asked every vendor to adopt FOCUS and roughly one agreed '
                              '[sqpO85TKjEI @ 00:02:00]. Amy Ashby confirms the gap from the consumption '
                              'side: consumption SaaS often lacks APIs, overage data is rarer still, and '
                              'SAM and ITAM tools show only contract-level data [iIwpcQbBkmM @ 00:23:37]. '
                              'The payoff for pushing anyway is real. Ashby hounded one vendor for months '
                              'to get an extract on an unmetered enterprise SKU, found a calculation '
                              "error, and received a credit [iIwpcQbBkmM @ 00:41:34]. Derer Mason's paper "
                              'trap is the marketplace: the EULA must match the signed contract, because '
                              "'you don't want the vendor to have the option to choose' which terms apply "
                              '[LF1AK1WypX0 @ 00:33:07]. Each of these failures is quiet. No alert fires '
                              'when a vendor declines a data format, when a SKU calculation is wrong, or '
                              'when a marketplace click-through carries different terms than the '
                              'negotiated agreement. The economics check: put data delivery into the '
                              'contract ask, reconcile vendor extracts against your own usage at least '
                              'once per term, and match every marketplace EULA to the signed agreement '
                              'before the first invoice lands.'],
               'table': {'caption': 'Firsthand SaaS and licensing traps with the economics behind them',
                         'headers': ['Trap', 'What Happened', 'Economics Check', 'Expert Source'],
                         'rows': [['CPU true-up with no true down',
                                   'Licensed for 100 CPUs, a spike to 120 gets billed at 120 for the '
                                   'entire year',
                                   'One spike sets the annual bill, and usage dropping back earns no '
                                   'refund at all',
                                   'Eddy Says Hi #EddySaysHi ([sIJo4dVD-jc @ 00:02:38])'],
                                  ['Commitment shortfall at term end',
                                   'Committed $1M over 12 months, spent only $900K, and still owed the '
                                   '$100K gap',
                                   'A mini business case committing $1.2M may get the shortfall forgiven '
                                   'by the vendor',
                                   'FinOps Foundation ([LF1AK1WypX0 @ 00:14:06])'],
                                  ['Running out of committed funds early',
                                   'Committed funds exhausted at month nine end the discount and force an '
                                   'early renewal',
                                   'Forecast drawdown monthly so the negotiated discount does not lapse '
                                   'before the term ends',
                                   'FinOps Foundation ([LF1AK1WypX0 @ 00:15:42])'],
                                  ['Zombie corporate-card subscriptions after offboarding',
                                   'Recurring charges kept billing after employees left, at $5,000 a month '
                                   'per charge',
                                   '$5,000 a month is 60k a year, and Reed saw that multiplied by 20',
                                   'FinOps Foundation ([hQDjTANIaTo @ 00:09:23])'],
                                  ['Discount illusion on a slow license rollout',
                                   'Bought 1,000 licenses that took a full year to deploy across actual '
                                   'users',
                                   'Contract cost divided by actual usage can match or exceed the '
                                   'on-demand price',
                                   'FinOps Foundation ([iIwpcQbBkmM @ 00:10:43]); FinOps Foundation '
                                   '([iIwpcQbBkmM @ 00:11:03])'],
                                  ['Uncontrolled usage spike from one small change',
                                   "An intern's logging change ran up $30,000 a day in vendor charges",
                                   'Near-real-time usage monitoring catches spikes that waiting on the '
                                   'monthly invoice misses',
                                   'FinOps Foundation ([LF1AK1WypX0 @ 00:27:49])'],
                                  ['Engineering around a price that can move',
                                   'Made code availability-zone aware and cut cross-AZ charges by 66',
                                   'About a week later AWS dropped the price to zero, and the code was '
                                   'reverted',
                                   'Datadog ([hmqskc5iaNc @ 00:24:03]); Datadog ([hmqskc5iaNc @ '
                                   '00:24:25])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before any renewal or commitment is signed',
                           'body': 'Each check below comes from a loss or near-miss a practitioner '
                                   'reported firsthand. Clear all four before money moves.',
                           'items': ['Model the shortfall before committing: $1M committed against $900K '
                                     'spent still owes $100K unless a $1.2M mini business case gets it '
                                     'forgiven [FinOps Foundation — LF1AK1WypX0 @ 00:14:06].',
                                     'Recompute the effective rate as contract cost divided by actual '
                                     'usage, and tell procurement the recorded savings are not real if it '
                                     'meets or exceeds on-demand [FinOps Foundation — iIwpcQbBkmM @ '
                                     '00:11:03].',
                                     'Clean up seats before any self-attestation audit, and plan for 10 to '
                                     '20% organic growth in the count [FinOps Foundation — LF1AK1WypX0 @ '
                                     '00:41:17].',
                                     'Protect telemetry rights in the contract before signing, the top '
                                     'priority call for the 2026 licensing shift [Eddy Says Hi #EddySaysHi '
                                     '— byD2FJ-NF0M @ 00:14:12].']}}],
 'pull_quote': '"That best rate you negotiated actually may cost you more because of underutilization." — '
               'FinOps Foundation (iIwpcQbBkmM @ 00:13:59).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Build a central vendor list, rank vendors by spend, deep-dive their contracts, and '
                      'repeat year-round while removing auto-uplifts or lowering tiers at renewal (FinOps '
                      'Weekly, sqpO85TKjEI @ 00:05:26).',
                      'Ask each vendor for a user list and the last time each user logged on, then map '
                      'those users to cost centers (FinOps Foundation, iIwpcQbBkmM @ 00:42:52).',
                      "Review the auto-created reclaim rule's 30-day inactivity threshold and consider "
                      'moving it to 90 days before reclaiming at scale (ServiceNow Community, 8mJc7j3DW28 '
                      '@ 00:03:48).',
                      'Run a weekly procurement, tech and finance triad that reviews renewals 3, 6 and 9 '
                      'months out and requires a competitor review (FinOps Foundation, hQDjTANIaTo @ '
                      '00:34:46).',
                      'Ask for discounted overages, free training and support, and an at-will termination '
                      'clause with 30, 60 or 90-day notice (FinOps Foundation, LF1AK1WypX0 @ 00:25:11).',
                      'Strip premium Microsoft 365 licenses from disabled and never-signed-in users, then '
                      'verify the reclaimed count in the admin portal (Scogo AI, hkNjUpPIx6M @ 00:01:34).'],
 'statutory_citations': [{'title': 'FinOps Foundation — Applying the FinOps Framework to SaaS at Scale '
                                   '[00:11:03]',
                          'url': 'https://www.youtube.com/watch?v=iIwpcQbBkmM&t=663s',
                          'relevance': 'Primary practitioner testimony on effective-rate math and why '
                                       'negotiated SaaS discounts can mask underutilization.'},
                         {'title': 'FinOps Foundation — Licensing and SaaS at Scale: Cloud+ FinOps Scopes '
                                   'Intersecting with ITAM & SAM [00:14:06]',
                          'url': 'https://www.youtube.com/watch?v=LF1AK1WypX0&t=846s',
                          'relevance': 'Primary practitioner testimony on commitment shortfalls, '
                                       'forgiveness business cases and renewal timing.'},
                         {'title': 'FinOps Foundation — Mastering FinOps for SaaS Optimization [00:09:23]',
                          'url': 'https://www.youtube.com/watch?v=hQDjTANIaTo&t=563s',
                          'relevance': 'Primary practitioner testimony on shadow corporate-card '
                                       'subscriptions and over-license true-up exposure.'},
                         {'title': 'Eddy Says Hi #EddySaysHi — SaaS & Licensing in FinOps [00:02:38]',
                          'url': 'https://www.youtube.com/watch?v=sIJo4dVD-jc&t=158s',
                          'relevance': 'Primary practitioner testimony on true-up billing with no true '
                                       'down.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'hQDjTANIaTo',
                       'title': 'Mastering FinOps for SaaS Optimization',
                       'channel': 'FinOps Foundation',
                       'author': 'FinOps Foundation',
                       'text': 'Recurring corporate-card charges kept billing after employees left, $5,000 '
                               "a month, that's 60k a year.",
                       'tip': 'Recurring corporate-card charges kept billing after employees left, $5,000 '
                              "a month, that's 60k a year.",
                       'timestamp': 563,
                       'timestamp_seconds': 563,
                       'timestamp_label': '[00:09:23]',
                       'url': 'https://www.youtube.com/watch?v=hQDjTANIaTo&t=563s',
                       'markdown': '[00:09:23](https://www.youtube.com/watch?v=hQDjTANIaTo&t=563s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sIJo4dVD-jc',
                       'title': 'SaaS & Licensing in FinOps',
                       'channel': 'Eddy Says Hi #EddySaysHi',
                       'author': 'Eddy Says Hi #EddySaysHi',
                       'text': 'Well, the vendor can true up your bill to that 120 rate for the entire '
                               'year.',
                       'tip': 'Well, the vendor can true up your bill to that 120 rate for the entire '
                              'year.',
                       'timestamp': 158,
                       'timestamp_seconds': 158,
                       'timestamp_label': '[00:02:38]',
                       'url': 'https://www.youtube.com/watch?v=sIJo4dVD-jc&t=158s',
                       'markdown': '[00:02:38](https://www.youtube.com/watch?v=sIJo4dVD-jc&t=158s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'F-5GIklN_Ps',
                       'title': 'FinOps for SaaS: Realities of Managing SaaS Value at Danske Bank',
                       'channel': 'FinOps Foundation',
                       'author': 'FinOps Foundation',
                       'text': 'Over two years, we found 3,000 applications.',
                       'tip': 'Over two years, we found 3,000 applications.',
                       'timestamp': 268,
                       'timestamp_seconds': 268,
                       'timestamp_label': '[00:04:28]',
                       'url': 'https://www.youtube.com/watch?v=F-5GIklN_Ps&t=268s',
                       'markdown': '[00:04:28](https://www.youtube.com/watch?v=F-5GIklN_Ps&t=268s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '472D_UGqdxA',
                       'title': 'FinOps Explained: Master Cloud Cost Management & Optimization for '
                                'Beginners',
                       'channel': 'CodeLucky',
                       'author': 'CodeLucky',
                       'text': 'Reserved instances can save 30 to 70% compared with on-demand pricing.',
                       'tip': 'Reserved instances can save 30 to 70% compared with on-demand pricing.',
                       'timestamp': 277,
                       'timestamp_seconds': 277,
                       'timestamp_label': '[00:04:37]',
                       'url': 'https://www.youtube.com/watch?v=472D_UGqdxA&t=277s',
                       'markdown': '[00:04:37](https://www.youtube.com/watch?v=472D_UGqdxA&t=277s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hkNjUpPIx6M',
                       'title': 'Advanced FinOps License Optimization in Microsoft 365',
                       'channel': 'Scogo AI',
                       'author': 'Scogo AI',
                       'text': 'Companies waste millions of premium paid licenses that are assigned to '
                               'deactivated employees or even to users who have never been onboarded.',
                       'tip': 'Companies waste millions of premium paid licenses that are assigned to '
                              'deactivated employees or even to users who have never been onboarded.',
                       'timestamp': 41,
                       'timestamp_seconds': 41,
                       'timestamp_label': '[00:00:41]',
                       'url': 'https://www.youtube.com/watch?v=hkNjUpPIx6M&t=41s',
                       'markdown': '[00:00:41](https://www.youtube.com/watch?v=hkNjUpPIx6M&t=41s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8mJc7j3DW28',
                       'title': 'How To: SaaS License Management to reduce and optimize spend',
                       'channel': 'ServiceNow Community',
                       'author': 'ServiceNow Community',
                       'text': 'The playbook creates a reclaim rule with a 30-day inactivity threshold, so '
                               'review it and consider changing it to 90 days.',
                       'tip': 'The playbook creates a reclaim rule with a 30-day inactivity threshold, so '
                              'review it and consider changing it to 90 days.',
                       'timestamp': 228,
                       'timestamp_seconds': 228,
                       'timestamp_label': '[00:03:48]',
                       'url': 'https://www.youtube.com/watch?v=8mJc7j3DW28&t=228s',
                       'markdown': '[00:03:48](https://www.youtube.com/watch?v=8mJc7j3DW28&t=228s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'byD2FJ-NF0M',
                       'title': '(Podcast) Preparing for 2026: Software Licensing, ITAM and FinOps Trends',
                       'channel': 'Eddy Says Hi #EddySaysHi',
                       'author': 'Eddy Says Hi #EddySaysHi',
                       'text': 'Identity is rapidly becoming the primary control plane for SaaS cost '
                               'management.',
                       'tip': 'Identity is rapidly becoming the primary control plane for SaaS cost '
                              'management.',
                       'timestamp': 737,
                       'timestamp_seconds': 737,
                       'timestamp_label': '[00:12:17]',
                       'url': 'https://www.youtube.com/watch?v=byD2FJ-NF0M&t=737s',
                       'markdown': '[00:12:17](https://www.youtube.com/watch?v=byD2FJ-NF0M&t=737s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gWDTRf_kGHI',
                       'title': 'FinOps Explained in 5 Minutes | What is FinOps?',
                       'channel': 'Anglepoint',
                       'author': 'Anglepoint',
                       'text': 'Crawl, walk, run maturity is assessed per capability, and few companies '
                               'are fully run.',
                       'tip': 'Crawl, walk, run maturity is assessed per capability, and few companies are '
                              'fully run.',
                       'timestamp': 264,
                       'timestamp_seconds': 264,
                       'timestamp_label': '[00:04:24]',
                       'url': 'https://www.youtube.com/watch?v=gWDTRf_kGHI&t=264s',
                       'markdown': '[00:04:24](https://www.youtube.com/watch?v=gWDTRf_kGHI&t=264s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sqpO85TKjEI',
                       'title': 'The Complete SaaS FinOps Playbook Explained in 17 Minutes | FinOps X '
                                'Interview',
                       'channel': 'FinOps Weekly',
                       'author': 'FinOps Weekly',
                       'text': 'If you query what they do with Adobe, I bet 90% of your organization is '
                               'just updating PDFs and signing them.',
                       'tip': 'If you query what they do with Adobe, I bet 90% of your organization is '
                              'just updating PDFs and signing them.',
                       'timestamp': 581,
                       'timestamp_seconds': 581,
                       'timestamp_label': '[00:09:41]',
                       'url': 'https://www.youtube.com/watch?v=sqpO85TKjEI&t=581s',
                       'markdown': '[00:09:41](https://www.youtube.com/watch?v=sqpO85TKjEI&t=581s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ryko_HHYy18',
                       'title': 'What Is a FinOps Scope? How FinOps Frames SaaS, Licensing, AI, Data '
                                'Center, and Other Cost and Usage',
                       'channel': 'FinOps Foundation',
                       'author': 'FinOps Foundation',
                       'text': 'Informed ignoring of capabilities is acceptable.',
                       'tip': 'Informed ignoring of capabilities is acceptable.',
                       'timestamp': 340,
                       'timestamp_seconds': 340,
                       'timestamp_label': '[00:05:40]',
                       'url': 'https://www.youtube.com/watch?v=ryko_HHYy18&t=340s',
                       'markdown': '[00:05:40](https://www.youtube.com/watch?v=ryko_HHYy18&t=340s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SdoLFHhMm1Q',
                       'title': '02: A FinOps Case Study',
                       'channel': 'Forest Lin',
                       'author': 'Forest Lin',
                       'text': 'Costs are up 45% in two years.',
                       'tip': 'Costs are up 45% in two years.',
                       'timestamp': 460,
                       'timestamp_seconds': 460,
                       'timestamp_label': '[00:07:40]',
                       'url': 'https://www.youtube.com/watch?v=SdoLFHhMm1Q&t=460s',
                       'markdown': '[00:07:40](https://www.youtube.com/watch?v=SdoLFHhMm1Q&t=460s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LF1AK1WypX0',
                       'title': 'Licensing and SaaS at Scale: Cloud+ FinOps Scopes Intersecting with ITAM '
                                '& SAM',
                       'channel': 'FinOps Foundation',
                       'author': 'FinOps Foundation',
                       'text': "So, make sure you're the single point of contact.",
                       'tip': "So, make sure you're the single point of contact.",
                       'timestamp': 1247,
                       'timestamp_seconds': 1247,
                       'timestamp_label': '[00:20:47]',
                       'url': 'https://www.youtube.com/watch?v=LF1AK1WypX0&t=1247s',
                       'markdown': '[00:20:47](https://www.youtube.com/watch?v=LF1AK1WypX0&t=1247s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LF1AK1WypX0',
                       'title': 'Licensing and SaaS at Scale: Cloud+ FinOps Scopes Intersecting with ITAM '
                                '& SAM',
                       'channel': 'FinOps Foundation',
                       'author': 'FinOps Foundation',
                       'text': "And you don't want the vendor to have the option to choose.",
                       'tip': "And you don't want the vendor to have the option to choose.",
                       'timestamp': 1987,
                       'timestamp_seconds': 1987,
                       'timestamp_label': '[00:33:07]',
                       'url': 'https://www.youtube.com/watch?v=LF1AK1WypX0&t=1987s',
                       'markdown': '[00:33:07](https://www.youtube.com/watch?v=LF1AK1WypX0&t=1987s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hmqskc5iaNc',
                       'title': 'FinOps and Cloud Cost Optimization',
                       'channel': 'Datadog',
                       'author': 'Datadog',
                       'text': 'We deployed that we saw a uh actually uh 66 price reduction in our cross '
                               'availability Zone charges which was very very nice.',
                       'tip': 'We deployed that we saw a uh actually uh 66 price reduction in our cross '
                              'availability Zone charges which was very very nice.',
                       'timestamp': 1443,
                       'timestamp_seconds': 1443,
                       'timestamp_label': '[00:24:03]',
                       'url': 'https://www.youtube.com/watch?v=hmqskc5iaNc&t=1443s',
                       'markdown': '[00:24:03](https://www.youtube.com/watch?v=hmqskc5iaNc&t=1443s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'O3FqsxJScI4',
                       'title': 'FinOps Forward 2026: FinOps Foundation Keynote',
                       'channel': 'Flexera | ITAM, FinOps & SaaS Management',
                       'author': 'Flexera | ITAM, FinOps & SaaS Management',
                       'text': "You don't need a team to do FinOps.",
                       'tip': "You don't need a team to do FinOps.",
                       'timestamp': 124,
                       'timestamp_seconds': 124,
                       'timestamp_label': '[00:02:04]',
                       'url': 'https://www.youtube.com/watch?v=O3FqsxJScI4&t=124s',
                       'markdown': '[00:02:04](https://www.youtube.com/watch?v=O3FqsxJScI4&t=124s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_PyR6G51QW4',
                       'title': 'SaaS FinOps Module: Taking Control of SaaS Costs and User Data with AI',
                       'channel': 'Procure IT',
                       'author': 'Procure IT',
                       'text': 'So that we can see and tackle the inactive users and remove them from the '
                               'system as it deemed appropriate.',
                       'tip': 'So that we can see and tackle the inactive users and remove them from the '
                              'system as it deemed appropriate.',
                       'timestamp': 34,
                       'timestamp_seconds': 34,
                       'timestamp_label': '[00:00:34]',
                       'url': 'https://www.youtube.com/watch?v=_PyR6G51QW4&t=34s',
                       'markdown': '[00:00:34](https://www.youtube.com/watch?v=_PyR6G51QW4&t=34s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iIwpcQbBkmM',
                       'title': 'Applying the FinOps Framework to SaaS at Scale',
                       'channel': 'FinOps Foundation',
                       'author': 'FinOps Foundation',
                       'text': "So often times we're focused on optimizing rate right negotiating the best "
                               'rate but I just showed you that that best rate you negotiated actually may '
                               'cost you more because of underutilization.',
                       'tip': "So often times we're focused on optimizing rate right negotiating the best "
                              'rate but I just showed you that that best rate you negotiated actually may '
                              'cost you more because of underutilization.',
                       'timestamp': 839,
                       'timestamp_seconds': 839,
                       'timestamp_label': '[00:13:59]',
                       'url': 'https://www.youtube.com/watch?v=iIwpcQbBkmM&t=839s',
                       'markdown': '[00:13:59](https://www.youtube.com/watch?v=iIwpcQbBkmM&t=839s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iIwpcQbBkmM',
                       'title': 'Applying the FinOps Framework to SaaS at Scale',
                       'channel': 'FinOps Foundation',
                       'author': 'FinOps Foundation',
                       'text': 'What I usually ask for is just a user list the two things I ask for is a '
                               'user list and the last time they logged on.',
                       'tip': 'What I usually ask for is just a user list the two things I ask for is a '
                              'user list and the last time they logged on.',
                       'timestamp': 2572,
                       'timestamp_seconds': 2572,
                       'timestamp_label': '[00:42:52]',
                       'url': 'https://www.youtube.com/watch?v=iIwpcQbBkmM&t=2572s',
                       'markdown': '[00:42:52](https://www.youtube.com/watch?v=iIwpcQbBkmM&t=2572s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'}]}
