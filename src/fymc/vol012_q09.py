from __future__ import annotations

CHAPTER_9 = {'id': 'Q9',
 'chapter_id': 'Q9',
 'chapter_number': 9,
 'question_number': 9,
 'slug': 'freight-broker-and-carrier-compliance',
 'question_prompt': 'What do these trucking sources report about freight-broker financial requirements, '
                    'operating authority, complaints, inspections, and carrier eligibility?',
 'kicker': 'Q9 / THE BIG MONEY PLAYBOOKS',
 'title': 'Freight-Broker and Carrier Compliance',
 'subtitle': 'FMCSA authority types, unpaid broker claims, financial-responsibility rule coverage, '
             'transparency, complaint reporting, DOT-status problems, inspections, and CDL revocations',
 'layout_template': 'tool_resource_directory',
 'reading_time_minutes': 15,
 'executive_summary': 'Carrier-side operators and broker-watchers converge on one message: the $75,000 '
                      'broker security floor finally has teeth. From January 16, 2026, BMC-85 trust money '
                      'must sit in cash, irrevocable letters of credit from federally insured depository '
                      'institutions, or Treasury bonds, and a broker that drops under $75,000 and fails to '
                      'replenish within seven calendar days faces suspension. Nobody treats that as a '
                      'reason to stop vetting: FMCSA will not text a carrier when a bond drains, so '
                      'operators pull SAFER, confirm BMC-84/85 status, call the bond agency, and watch '
                      "days-to-pay trends. Transportli's data shows only about 22% of 114,000-plus granted "
                      'broker authorities remain active. Disagreement runs over whether the rule is '
                      'overdue bare minimum, whether bonds change at all, and whether rate transparency '
                      'helps or backfires on carriers.',
 'key_metrics': [{'label': 'Broker financial security floor and replenish window',
                  'metric': 'Broker financial security floor and replenish window',
                  'value': '$75,000 floor; 7 calendar days to replenish after FMCSA notice',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Read from the broker financial responsibility rule text: security falling '
                             'below $75,000 via consented drawdown, ignored claim notice, or judgment '
                             'triggers a suspension notice if not replenished in seven calendar days.',
                  'source': 'Trucking Made Successful ([iwQkqbEBCrM @ 00:01:54])'},
                 {'label': 'Broker authorities still active',
                  'metric': 'Broker authorities still active',
                  'value': 'About 22% (roughly 25,000 active of 114,000+ ever granted)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Transportli's pull of FMCSA's own broker authority data showing how few "
                             'granted brokerages survive.',
                  'source': 'Transportli ([HRlIiVKracc @ 00:00:00])'},
                 {'label': 'Broker revocation notices in 2024',
                  'metric': 'Broker revocation notices in 2024',
                  'value': '4,768 notices, 4.4 times the roughly 1,100 issued in 2016',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Notices usually follow a lapsed bond or insurance filing; 99.6% were cured '
                             'with a median of 17 days, while final revocations peaked at 8,545 in 2023.',
                  'source': 'Transportli ([HRlIiVKracc @ 00:00:39])'},
                 {'label': 'Dead DOT number fix time after press escalation',
                  'metric': 'Dead DOT number fix time after press escalation',
                  'value': '16 hours 26 minutes versus almost 3 months through normal channels',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Darryl Gibbs's USDOT number sat inactive after a Motus glitch until "
                             'Overdrive called FMCSA about the case.',
                  'source': 'Jim Campbell - Official Trucking Channel ([misVtmF2XjA @ 00:08:44])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every channel that covered the broker financial responsibility rule lands '
                              'on the same core mechanic: the $75,000 broker and freight forwarder '
                              'security is now a live tripwire instead of a paperwork formality. Trucking '
                              'Made Successful reads the November 2023 rule text straight: when available '
                              'security falls below $75,000 because of a consented drawdown, an ignored '
                              'claim notice, or a claim converted to a judgment, FMCSA notifies the '
                              'broker, and if the money is not replenished within seven calendar days, a '
                              'suspension notice follows [iwQkqbEBCrM @ 00:01:54]. ET Transport frames the '
                              'same trigger as an immediate red card: no new contracts, no arranging '
                              'shipments, and no piling up additional unpaid claims over time [Y4Qa3jy-WNw '
                              '@ 00:06:06]. Vitali of AFT Dispatch adds that a broker who goes silent '
                              'after a drawdown gets suspended outright, and argues the floor is modest '
                              'anyway, since a carrier losing its $750,000 auto liability coverage becomes '
                              'unauthorized and goes out of service while the broker number is ten times '
                              'less money [4m_pJHgvrpc @ 00:04:17]. Alex Mai of Mutha Trucker pitches the '
                              'result as the end of the six-month grace window in which shady brokers kept '
                              'moving freight while carrier claims stacked up unpaid [ZSZAVstSGl8 @ '
                              '00:04:11].',
                              'The second point of agreement is that the rule shrinks the bad-broker pool '
                              "without removing the carrier's homework. Trucking Made Successful is blunt "
                              "that FMCSA is not going to text anyone when a broker's bond drops below "
                              '$75,000, so the risk is hauling a load, invoicing, and only then learning '
                              'the authority is suspended; the answer is to vet more, not less '
                              "[iwQkqbEBCrM @ 00:07:27]. Transportli's study of FMCSA records backs the "
                              'urgency: about 25,000 broker authorities are active out of more than '
                              "114,000 ever granted, roughly 22% survival, and 35% of today's active "
                              'brokers logged at least one revocation event in the past five years '
                              "[HRlIiVKracc @ 00:01:00]. The funny farm's YMC Transport case shows why the "
                              'name on the paperwork is not enough on the carrier side either: even after '
                              'a November 10 out-of-service order, 33 trucks that ran under YMC were last '
                              'seen operating under MLTZX Group, so the advice is to check the USDOT '
                              'number on the truck that actually shows up [t1CJB1XA9y0 @ 00:01:36]. Zach '
                              'Myborg, on Mutha Trucker, describes the same chameleon pattern from '
                              'fraudulent fleets that simply file for another DOT number and burn the old '
                              'company down [ksCNlUOCnHc @ 00:06:11].',
                              "Baseline prerequisites come straight from FMCSA's own operating-authority "
                              "walkthrough. Anyone paid to arrange transportation of other people's "
                              'property through an authorized motor carrier needs Broker of Property '
                              'authority, with a separate Broker of Household Goods authority for moves, '
                              'while a freight forwarder differs because it takes responsibility for the '
                              'freight, assembles and consolidates shipments, and handles break-bulk '
                              'distribution [qJ2zB-OEb8o @ 00:02:08]. Both brokers and forwarders must '
                              'carry either a surety bond filed by an insurance company or a trust fund '
                              'agreement filed by a financial institution for $75,000, from FMCSA-approved '
                              'providers, plus a BOC-3 process agent designation, usually through a '
                              'blanket company with agents in every state; failing to promptly submit the '
                              'forms can get an application dismissed and the fee lost [qJ2zB-OEb8o @ '
                              '00:08:35]. FMCSA REGISTRATION dot com sells directly into that pain, '
                              'pitching registration paperwork and safety-audit preparation on the '
                              'argument that non-compliance means hefty fines, revoked licenses, and a '
                              'business put at risk [pK4RGE_1My4 @ 00:00:37]. ET Transport sizes the '
                              'regulated pool at roughly 32,000 registered brokers and freight forwarders, '
                              "and quotes FMCSA's Chris Henry that most operate with integrity while a "
                              'minority with unscrupulous practices creates unnecessary financial hardship '
                              'for unsuspecting motor carriers [Y4Qa3jy-WNw @ 00:01:43].'],
               'table': {'caption': 'Where carrier-side and broker-watching practitioners agree on broker '
                                    'and carrier compliance',
                         'headers': ['Consensus Point',
                                     'What the Practitioner Reported',
                                     'Operator Takeaway',
                                     'Expert Source'],
                         'rows': [['The $75,000 security floor now triggers suspension',
                                   'Security below $75,000 that is not replenished within seven calendar '
                                   'days draws an FMCSA notification of suspension',
                                   'Treat any broker drawdown or claim chatter as a live warning before '
                                   'booking the next load',
                                   'Trucking Made Successful ([iwQkqbEBCrM @ 00:01:54])'],
                                  ['Trust fund assets narrowed to liquid instruments only',
                                   'Only cash, irrevocable letters of credit, and Treasury bonds qualify, '
                                   'effective January 2026, two years from the effective date',
                                   'Brokers whose trusts leaned on real estate, stocks, or loans lose '
                                   'their financial footing',
                                   'AFT Dispatch ([4m_pJHgvrpc @ 00:05:35])'],
                                  ['Going silent after a drawdown gets a broker suspended',
                                   'Brokers that do not respond after a drawdown have their brokerage '
                                   'authority immediately suspended by FMCSA',
                                   'A broker dodging claim communication is signaling authority trouble '
                                   'that can strand an unpaid invoice',
                                   'AFT Dispatch ([4m_pJHgvrpc @ 00:02:54])'],
                                  ['Regulation does not replace carrier-side broker vetting work',
                                   'FMCSA will not text carriers when a broker bond drops below the '
                                   '$75,000 minimum',
                                   'Run independent broker checks on every load instead of assuming the '
                                   'agency is watching for you',
                                   'Trucking Made Successful ([iwQkqbEBCrM @ 00:07:27])'],
                                  ['Broker authority churn is massive across the whole market',
                                   'About 22% of more than 114,000 granted broker authorities remain '
                                   'active, with roughly 25,000 active today',
                                   "Check the full revocation history of a broker, not just today's active "
                                   'status line',
                                   'Transportli ([HRlIiVKracc @ 00:00:00])'],
                                  ['Chameleon carrier operations survive federal out-of-service shutdown '
                                   'orders',
                                   '33 trucks from out-of-service YMC Transport were last seen running '
                                   'under a new name, MLTZX Group',
                                   'Match the USDOT number on the arriving truck against the name on the '
                                   'paperwork every time',
                                   'the funny farm ([t1CJB1XA9y0 @ 00:00:35])'],
                                  ['Enforcement squeeze on rule-breakers lifts the rate floor',
                                   'Knight-Swift CEO Adam Miller linked regulators removing rule-breaking '
                                   'carriers to a durable, higher floor for rates',
                                   'Compliant carriers gain pricing leverage as non-compliant capacity '
                                   'gets forced out of the market',
                                   'the funny farm ([t1CJB1XA9y0 @ 00:04:35])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The mechanics start with the two instruments a broker can use to carry the '
                              '$75,000. Trucking Made Successful explains that a BMC-84 is a surety bond '
                              'underwritten by a surety company that takes the financial risk, with the '
                              'broker splitting the $75,000 into monthly payments, while a BMC-85 is a '
                              'trust requiring the full $75,000 deposited as collateral with a trust '
                              'company; FreightWaves called the BMC-85 side the Wild West because it ran '
                              'with no financial checks, no credit checks, and no underwriting, and some '
                              'providers sat outside the reach of US regulators [iwQkqbEBCrM @ 00:04:07]. '
                              'AFT Dispatch lists what is now off the table: real estate, stocks, '
                              'non-Treasury bonds, and other securities, with loan and finance companies '
                              'no longer eligible as trustees as of January 2026 [4m_pJHgvrpc @ 00:05:53]. '
                              'Alex Mai of Mutha Trucker describes the scam those gaps allowed, trust '
                              'funds propped up with borrowed money, real estate, or IOUs and held by '
                              "providers that were not real banks, so a carrier's claim hit an empty "
                              'account; after an FMCSA audit found fake providers, brokers got 30 days to '
                              'land on a compliant list or go straight to suspension, while surety bonds '
                              'stay largely unchanged [ZSZAVstSGl8 @ 00:05:16].',
                              'The vetting stack is specific. Trucking Made Successful relays '
                              "FreightWaves' checklist: pull the broker in SAFER and the FMCSA licensing "
                              'and insurance portal, confirm the BMC-84 or BMC-85 is current and active, '
                              'call the bond agency to confirm the $75,000 is actually there, and watch '
                              'for insurance cancellations; higher-tier DAT or Truckstop subscriptions '
                              'show credit score and days-to-pay trends, and a climbing days-to-pay line '
                              'signals cash-flow trouble [iwQkqbEBCrM @ 00:08:15]. Factoring companies do '
                              'this homework too, which is how RNR Express showed up rated F with RTS '
                              'Factoring while still posting loads [iwQkqbEBCrM @ 00:05:22]. Transportli '
                              'supplies the history filter: revocation notices hit 4,768 in 2024, 4.4 '
                              'times the 2016 level, yet 99.6% were cured with a median of 17 days, 17% of '
                              'revocations were later reinstated, 947 brokers logged three or more events, '
                              'more than half of brokers aged three to ten years had an event versus 10% '
                              'under three years, and September carries over 14% of annual notices '
                              '[HRlIiVKracc @ 00:01:21]. In a Truckstop ad read, Alex Mai notes the board '
                              'requires active broker authority and bakes in risk signals, and that a rate '
                              'way above the lane is a scam or double-brokering tell [BE6n1FfpOO8 @ '
                              '00:05:20].',
                              'Carriers also have to defend their own record, because broker vetting '
                              'software reads it too. Jim Campbell, with 33 years as driver, dispatcher, '
                              "and broker, reports that FMCSA's Motus system raised required coverage for "
                              '150,076 carriers, 27,287 of which had been fully covered before, and '
                              'wrongly tagged more than 6,475 companies as hazmat, jumping requirements '
                              'from $750,000 to $1 million and, in some reports, $5 million [misVtmF2XjA @ '
                              '00:04:30]. The fix routine: look yourself up on the SAFER Company Snapshot '
                              'and the public Motus search, check carrier type and coverage number, call '
                              'the insurance agent before touching anything, screenshot and date '
                              'everything, keep one support ticket open, and ignore fee-demanding fake '
                              "Motus emails; when Darryl Gibbs's number sat inactive for almost three "
                              'months, an Overdrive call got it reactivated in 16 hours and 26 minutes '
                              '[misVtmF2XjA @ 00:08:44]. For broker misconduct, Carlton of Freight Pro Hub '
                              "points to FMCSA's upgraded complaint center, which takes reports on brokers "
                              'operating without authority or under an unregistered name and on '
                              'registration identity theft; file as a driver or industry professional, '
                              'attach dates, company names, DOT numbers, emails, and photos, save the case '
                              'number, or call 1-888-DOT-SAFT weekdays 8 a.m. to 8 p.m. Eastern, knowing a '
                              'filing neither forces an investigation nor collects an unpaid invoice '
                              '[8X37vkZBHyo @ 00:03:23].'],
               'table': {'caption': 'Street mechanics, tools, and hard numbers for broker and carrier '
                                    'compliance checks',
                         'headers': ['Mechanic or Tool',
                                     'Exact Number or Rule',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['BMC-84 surety bond underwritten by a surety company',
                                   'Surety company carries the risk while the broker splits the $75,000 '
                                   'into monthly payments',
                                   'Underwriting gives carriers a backstop that steps in and pays when '
                                   'brokers do not',
                                   'Trucking Made Successful ([iwQkqbEBCrM @ 00:03:45])'],
                                  ['BMC-85 trust fund held with a trust company',
                                   'Full $75,000 deposited as collateral; only cash, irrevocable letters '
                                   'of credit, or Treasury bonds qualify',
                                   "Ask what assets actually back a broker's trust before hauling on its "
                                   'promise to pay',
                                   'Trucking Made Successful ([iwQkqbEBCrM @ 00:03:07])'],
                                  ['Trust provider purge after the FMCSA audit findings',
                                   'Brokers with kicked-out providers get 30 days to move to a provider on '
                                   'the compliant list',
                                   'Brokers scrambling to replace a trust provider are near-term '
                                   'suspension candidates to watch closely',
                                   'Mutha Trucker - Official Trucking Channel ([ZSZAVstSGl8 @ 00:05:16])'],
                                  ['Higher-tier DAT or Truckstop load board credit tools',
                                   "Shows a broker's credit score movement and days to pay tracked over "
                                   'time',
                                   'A rising days-to-pay line flags cash-flow trouble before an invoice '
                                   'goes unpaid',
                                   'Trucking Made Successful ([iwQkqbEBCrM @ 00:08:54])'],
                                  ['Broker revocation history pull from public FMCSA data',
                                   '99.6% of notices cured at a median 17 days; 29% of reinstatements took '
                                   'over a year',
                                   'One cured notice is fine; repeated notices or revoke-then-reinstate '
                                   'patterns deserve hard questions',
                                   'Transportli ([HRlIiVKracc @ 00:01:40])'],
                                  ['Motus and SAFER self-audit of the carrier record',
                                   'Check SAFER Company Snapshot and the public Motus search, which do not '
                                   'always match right now',
                                   'Catch false inactive or hazmat flags before broker vetting software '
                                   'auto-rejects the carrier',
                                   'Jim Campbell - Official Trucking Channel ([misVtmF2XjA @ 00:07:17])'],
                                  ['FMCSA complaint center phone line for broker problems',
                                   '1-888-DOT-SAFT, Monday through Friday, 8 a.m. to 8 p.m. Eastern time',
                                   'Report brokers misrepresenting names or operating without authority, '
                                   'backed by dates and DOT numbers',
                                   'Freight Pro Hub ([8X37vkZBHyo @ 00:04:20])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'What sharp carriers do that the rule will not do for them',
                           'body': 'Practitioners treat the January 2026 broker rule as a filter, not a '
                                   'shield, and stack their own checks on top of it.',
                           'items': ['Track days to pay as a trend line, not a snapshot; a broker whose '
                                     'days to pay keeps climbing is showing cash-flow trouble [Trucking '
                                     'Made Successful — iwQkqbEBCrM @ 00:09:11].',
                                     'Match the USDOT number on the truck that shows up to the paperwork; '
                                     "YMC Transport's trucks kept rolling under MLTZX Group after the "
                                     'shutdown order [the funny farm — t1CJB1XA9y0 @ 00:01:36].',
                                     'When the help desk stalls, call the trucking press: an Overdrive '
                                     'inquiry revived a dead DOT number in 16 hours and 26 minutes after '
                                     'almost three months of doing it the right way [Jim Campbell - '
                                     'Official Trucking Channel — misVtmF2XjA @ 00:08:44].',
                                     'Do not burn a complaint on a low rate con; a low rate by itself is '
                                     'not a federal violation, so bring facts on authority or name '
                                     'misrepresentation instead [Freight Pro Hub — 8X37vkZBHyo @ '
                                     '00:01:16].']},
               'sop_steps': [{'step': 1,
                              'title': 'Pull live authority and insurance status',
                              'action': 'Look the broker up in SAFER and the FMCSA licensing and insurance '
                                        'portal before booking.',
                              'detail': 'Confirm active broker authority and watch for insurance '
                                        'cancellations, because FMCSA will not text carriers when a bond '
                                        'drops below $75,000 [Trucking Made Successful — iwQkqbEBCrM @ '
                                        '00:08:15].'},
                             {'step': 2,
                              'title': 'Verify the $75,000 instrument',
                              'action': 'Confirm whether the broker files a BMC-84 or BMC-85 and call the '
                                        'bond agency to confirm the money is present.',
                              'detail': 'From January 2026 a trust may only hold cash, irrevocable letters '
                                        'of credit, or Treasury bonds, and loan and finance companies can '
                                        'no longer act as trustees [AFT Dispatch — 4m_pJHgvrpc @ '
                                        '00:05:35].'},
                             {'step': 3,
                              'title': 'Read the revocation history and payment trend',
                              'action': 'Pull the full revocation history and the days-to-pay trend '
                                        "instead of trusting today's status.",
                              'detail': 'One cured notice is not a red flag, but repeated notices or a '
                                        'revocation followed by reinstatement deserve questions, and a '
                                        'quote far below market is a warning sign [Transportli — '
                                        'HRlIiVKracc @ 00:01:40].'},
                             {'step': 4,
                              'title': 'Audit your own record and escalate',
                              'action': 'Check your SAFER snapshot and Motus record, then document and '
                                        'escalate any errors.',
                              'detail': 'Call your insurance agent before changing anything, screenshot '
                                        'and date every screen, keep one support ticket open, and ignore '
                                        'emails demanding a fee to fix your record [Jim Campbell - '
                                        'Official Trucking Channel — misVtmF2XjA @ 00:08:05].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Practitioners split hard on whether the January 16, 2026 '
                              "financial-responsibility rule lets carriers relax. Mutha Trucker's Alex Mai "
                              'calls it a big win that shuts down the scammy fake brokers, but draws a '
                              'line most headlines miss: the crackdown targets fake trust funds and '
                              'unregulated trust providers, while BMC-84 bonds, which work like insurance '
                              'with a monthly fee, are not changing much [ZSZAVstSGl8 @ 00:03:41]. '
                              'Trucking Made Successful flips the comfort narrative entirely, warning that '
                              "FMCSA is not going to text you when a broker's bond drops below $75,000, so "
                              'carriers will have to vet more, not less, because some will learn about a '
                              'suspension after the invoice is already sitting unpaid [iwQkqbEBCrM @ '
                              '00:07:27]. ET Transport sells the upside, repeating an FMCSA '
                              "representative's line that carriers could receive payment for completed "
                              "work in a more timely manner [Y4Qa3jy-WNw @ 00:03:00]. AFT Dispatch's "
                              'Vitali lands in a third camp: the rule is supported by both TIA and OOIDA, '
                              "groups that are usually at each other's necks, yet suspending a broker "
                              "under the $75,000 floor looks like a bare minimum when a carrier's own "
                              'authority goes unauthorized the moment its $750,000 auto liability lapses, '
                              "ten times the broker's number [4m_pJHgvrpc @ 00:04:17].",
                              'The cure clock itself gets reported differently depending on who is '
                              'talking. ET Transport puts it at seven calendar days to patch security that '
                              'falls below $75,000 before operating authority gets the red card '
                              '[Y4Qa3jy-WNw @ 00:03:31], while Mutha Trucker describes a 30-day window for '
                              'brokers whose trust providers were kicked out, after which it is no more '
                              'loads, no more grace periods, and straight to authority suspension '
                              '[ZSZAVstSGl8 @ 00:05:16]. The vetting playbooks diverge too. Trucking Made '
                              'Successful calls a factoring company the easier road because it does its '
                              'own vetting and surfaces credit score and days to pay; without one, check '
                              'SAFER and the licensing and insurance portal, confirm the BMC-84 or BMC-85 '
                              'is current, call the bond agency, and treat rising days to pay on DAT or '
                              'Truckstop higher tiers as a cash-flow warning [iwQkqbEBCrM @ 00:08:15]. '
                              "Transportli argues from FMCSA's own data that a single cured revocation "
                              'notice is not a red flag, since 99.6% were cured at a median of 17 days, '
                              'but repeated notices or a revoke-then-reinstate pattern deserve hard '
                              'questions [HRlIiVKracc @ 00:01:40]. Mutha Trucker takes the blunter line: '
                              'do not haul for brokers who cannot show real money in the bank.',
                              'Broker transparency is the oldest fight on the board. This Week in Trucking '
                              'reports that brokers only have to disclose shipper pay after delivery and '
                              'on a written request, and that broker-carrier agreements carry a waiver '
                              'signing that right away; small fleets say whoever hauls the freight should '
                              'know what it paid [YWQYZLDM6dY @ 00:00:58]. The TIA counters that forced '
                              'transparency could trigger a race to the bottom where small brokers who '
                              'might pay better get squeezed out by mega firms and carriers end up making '
                              'less, and that brokers may profit on a few choice loads while breaking even '
                              'on the rest [YWQYZLDM6dY @ 00:01:27]. The carrier-side rebuttal from This '
                              'Week in Trucking: knowing which brokers consistently take higher margins '
                              'lets you negotiate smarter or walk away. On the wider rule churn, '
                              "thatDOTcop, a state DOT officer, frames FMCSA's 11 of 18 finalized "
                              'deregulatory actions as administrative cleanup with small or negligible '
                              'economic impact, noting ATA and OOIDA call it common sense while some '
                              'drivers call it surface-level [5KIDTEBQD18 @ 00:06:16]. Trucking Life with '
                              'Shawn treats the same fuse and flare removals as a live roadside trap, '
                              'telling drivers to push back politely when an inspector still running the '
                              'old rule book writes them up for missing spare fuses [UlW-GlLugUg @ '
                              '00:04:05].'],
               'table': {'caption': 'Contested playbooks on broker security, transparency, rule changes, '
                                    'and the driver purge',
                         'headers': ['Contested Question', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Does the January 16, 2026 rule mean carriers can stop vetting brokers?',
                                   'Mutha Trucker: big win, shady brokers who cannot replenish trust funds '
                                   'get straight authority suspension.',
                                   'Trucking Made Successful: FMCSA will not text you, so vet every broker '
                                   'like crazy.',
                                   'Mutha Trucker - Official Trucking Channel ([ZSZAVstSGl8 @ 00:05:49]); '
                                   'Trucking Made Successful ([iwQkqbEBCrM @ 00:07:27])'],
                                  ['Which side of broker security does the new rule actually hit hardest?',
                                   'Mutha Trucker: BMC-84 bonds work like monthly-fee insurance and are '
                                   'not changing much.',
                                   'Trucking Made Successful: BMC-85 trusts were the Wild West with no '
                                   'credit checks or underwriting.',
                                   'Mutha Trucker - Official Trucking Channel ([ZSZAVstSGl8 @ 00:03:55]); '
                                   'Trucking Made Successful ([iwQkqbEBCrM @ 00:04:07])'],
                                  ['Is the financial-responsibility rule a real carrier win or just the '
                                   'bare minimum?',
                                   'ET Transport: carriers get more information and could be paid for '
                                   'completed work faster.',
                                   'AFT Dispatch: TIA and OOIDA both agree, but these requirements '
                                   'belonged on the books from day one.',
                                   'ET Transport ([Y4Qa3jy-WNw @ 00:03:16]); AFT Dispatch ([4m_pJHgvrpc @ '
                                   '00:06:50])'],
                                  ['How long does a broker get to cure a security shortfall before '
                                   'suspension?',
                                   'ET Transport: seven calendar days after available security drops below '
                                   '$75,000, then authority is suspended.',
                                   'Mutha Trucker: 30 days to land on a compliant trust provider list, '
                                   'then no more loads.',
                                   'ET Transport ([Y4Qa3jy-WNw @ 00:06:06]); Mutha Trucker - Official '
                                   'Trucking Channel ([ZSZAVstSGl8 @ 00:05:32])'],
                                  ['Should carriers get to see what the shipper paid the broker on every '
                                   'load?',
                                   'Small fleets and owner-operators: whoever hauls the freight deserves '
                                   'to know what the load paid.',
                                   'TIA: forced disclosure sparks a race to the bottom that leaves '
                                   'carriers earning less on average.',
                                   'This Week in Trucking ([YWQYZLDM6dY @ 00:00:58]); This Week in '
                                   'Trucking ([YWQYZLDM6dY @ 00:01:11])'],
                                  ["Do FMCSA's 11 finalized deregulatory changes matter on the road today?",
                                   'thatDOTcop: modernization and administrative cleanup with small or '
                                   'negligible economic impact per change.',
                                   'Trucking Life with Shawn: inspectors on the old rule book still write '
                                   'drivers up for missing fuses.',
                                   'thatDOTcop ([5KIDTEBQD18 @ 00:05:18]); Trucking Life with Shawn '
                                   '([UlW-GlLugUg @ 00:04:05])'],
                                  ['Is the non-domiciled CDL purge good or bad news for veteran carriers?',
                                   'The Trucker Report: pulling up to 194,000 drivers drains capacity and '
                                   'nudges rates back up.',
                                   'Critics cited by The Trucker Report: the roadside English test is '
                                   'subjective and sweeps up clean bilingual drivers.',
                                   'The Trucker Report ([W2zyskEb3zQ @ 00:13:26]); The Trucker Report '
                                   '([W2zyskEb3zQ @ 00:16:07])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive trap is hauling for a broker whose money is already '
                              'gone. Trucking Made Successful names RNR Express: once a decent broker, now '
                              'rated F with RTS Factoring, credit score in the toilet, and still posting '
                              "and selling loads to carriers; when a crappy broker's bond gets depleted to "
                              'zero and you file too late, you end up without money for the load you '
                              'hauled [iwQkqbEBCrM @ 00:05:22]. Mutha Trucker hears the same story from '
                              'owner-operators who front fuel and lumpers, deliver on time, then call a '
                              'broker that cannot pay, while shady brokers rode a grace period and went '
                              'another six months without paying anybody [ZSZAVstSGl8 @ 00:04:26]. Freight '
                              "Pro Hub's Carlton warns carriers not to mistake the upgraded FMCSA "
                              'complaint center for a collections desk: filing does not automatically '
                              'trigger an investigation or a fine, a low rate con by itself is not a '
                              'federal violation, and a complaint does not get an unpaid invoice paid '
                              "[8X37vkZBHyo @ 00:03:41]. Transportli's data shows how routine broker "
                              'trouble is: 35% of active brokers had at least one revocation event in five '
                              'years, 947 had three or more, and more than half of brokers aged three to '
                              'ten years had an event [HRlIiVKracc @ 00:01:21].',
                              'Carriers also get burned by the registration system itself. Jim Campbell, '
                              'with 33 years driving, dispatching, and brokering, reports that after FMCSA '
                              'switched on Motus in May, 150,076 carriers saw their required coverage '
                              'number rise and 27,287 of them were covered fine before; Dynamic M.D., a '
                              'flatbed and step deck outfit in Carol Stream, Illinois, was relabeled '
                              'hazmat, told it needed $1 million instead of $750,000, and had authority '
                              'shut off with the fix button grayed out [misVtmF2XjA @ 00:03:56]. TexLink '
                              'Logistics got a BOC-3 glitch that made broker vetting tools treat a '
                              'years-old company like new authority, and brokers scared of fraud '
                              'auto-reject anything that reads new [misVtmF2XjA @ 00:05:36]. The reverse '
                              'failure hits brokers and shippers vetting carriers: the funny farm reports '
                              'FMCSA ordered YMC Transport out of service on November 10, yet 33 of its '
                              'trucks were already running under MLTZX Group, with the next entity, ZPVR '
                              'Auto, logging its first inspection November 1; the order took the name off '
                              'the door, not the trucks off the road [t1CJB1XA9y0 @ 00:01:36]. Mutha '
                              "Trucker's guest Zach Myborg adds that fraudulent operators simply file for "
                              'another DOT number and burn the company down [ksCNlUOCnHc @ 00:06:11].',
                              'The economics check on fraud cuts both ways. An owner-operator featured by '
                              'Mutha Trucker puts compliant cost at about three dollars a mile against '
                              'roughly two for log-cheaters, and Zach Myborg says operators erasing logs '
                              'nightly advertise 4,000 to 5,000 miles a week solo against a compliant '
                              'ceiling of about 2,500 to 3,000, easily a $1.50 a mile gap; Myborg also '
                              'wants FMCSA to scrap the 60 days it traditionally gives carriers on '
                              'decertified ELDs [ksCNlUOCnHc @ 00:15:02]. Trucking Life with Shawn, a '
                              '17-year driver and trainer at Rosedale Transport, warns that under the SMS '
                              'overhaul an out-of-service violation counts two, everything else one, and '
                              'the most recent inspection carries the maximum weight, so a single busted '
                              'brake hose can set your percentile; tapping all good on an electronic DVIR '
                              'without walking the truck is fraud that costs CDLs [UlW-GlLugUg @ '
                              '00:02:25]. The Trucker Report counts more than 20,000 drivers pulled out of '
                              'service on the English standard after June 25, with the truck parked until '
                              'a qualified driver arrives, the load late, and the mark following the '
                              "record into insurance costs [W2zyskEb3zQ @ 00:15:06]. FMCSA's own "
                              'registration video adds that failing to submit required forms can dismiss '
                              'an application and forfeit the fee [qJ2zB-OEb8o @ 00:10:09].'],
               'table': {'caption': 'Firsthand failure modes and the money or time they cost',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Economics or Operational Hit',
                                     'Expert Source'],
                         'rows': [['Hauling for a broker already in financial trouble',
                                   'RNR Express, rated F with RTS Factoring, kept posting and selling '
                                   'loads to carriers.',
                                   'Bond gets depleted to zero and late filers end up unpaid for the load '
                                   'hauled.',
                                   'Trucking Made Successful ([iwQkqbEBCrM @ 00:05:22])'],
                                  ['Treating the FMCSA complaint center like a collections agency',
                                   'Carriers file over unpaid invoices or simply because they dislike a '
                                   'low rate con.',
                                   'Filing does not get you paid and does not guarantee any investigation '
                                   'or fine.',
                                   'Freight Pro Hub ([8X37vkZBHyo @ 00:03:41])'],
                                  ['Motus silently relabeling a general freight carrier as hazmat',
                                   'Dynamic M.D. was flagged hazmat, required coverage jumped to $1 '
                                   'million, authority cut automatically.',
                                   'The owner could not book a single shipment; more than 6,475 companies '
                                   'took the same hit.',
                                   'Jim Campbell - Official Trucking Channel ([misVtmF2XjA @ 00:04:12])'],
                                  ['Inactive USDOT number nobody told the carrier about',
                                   'Darryl Gibbs showed inactive for almost three months and was unaware '
                                   'for the first month.',
                                   'Fixed sixteen hours and twenty-six minutes after Overdrive called '
                                   'FMCSA about the case.',
                                   'Jim Campbell - Official Trucking Channel ([misVtmF2XjA @ 00:08:25])'],
                                  ['Vetting the carrier name on paperwork instead of the truck',
                                   'YMC Transport was ordered out of service while 33 trucks already ran '
                                   'under MLTZX Group.',
                                   'The order took the name off the door but left the same trucks rolling '
                                   'on the road.',
                                   'the funny farm ([t1CJB1XA9y0 @ 00:00:35])'],
                                  ['One sloppy inspection under the overhauled SMS scoring model',
                                   'Most recent inspection now carries maximum weight and out-of-service '
                                   'violations count as two.',
                                   'A single inspection can flag the carrier for audit and cost a driver '
                                   'the job.',
                                   'Trucking Life with Shawn ([UlW-GlLugUg @ 00:02:25])'],
                                  ['Running on tampered or erased electronic logs to stretch miles',
                                   'Drivers let dispatchers tamper with logs or call providers to erase '
                                   'their shifts.',
                                   'An accident in the wrong place means criminal fraud prosecution while '
                                   'the fleet walks away.',
                                   'Mutha Trucker - Official Trucking Channel ([ksCNlUOCnHc @ '
                                   '00:05:11])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Checks Before You Book, Haul, or Roll',
                           'body': 'Every item below comes from a loss, glitch, or out-of-service order a '
                                   'practitioner reported firsthand. Clear all four before committing a '
                                   'truck to a load.',
                           'items': ['Pull the broker on SAFER and the licensing and insurance portal, '
                                     'confirm the BMC-84 or BMC-85 is current, and call the bond agency to '
                                     'confirm the $75,000 is actually there [Trucking Made Successful — '
                                     'iwQkqbEBCrM @ 00:08:15].',
                                     'Look yourself up the way a broker would on the Company Snapshot and '
                                     'the public Motus search, check your carrier type and required '
                                     'coverage number, and call your agent before changing anything in the '
                                     'system [Jim Campbell - Official Trucking Channel — misVtmF2XjA @ '
                                     '00:07:17].',
                                     'When a load is tendered, check the USDOT number on the truck that '
                                     'actually shows up, not just the name on the paperwork [the funny '
                                     'farm — t1CJB1XA9y0 @ 00:01:36].',
                                     'Do the real walk-around first and sign the electronic DVIR second, '
                                     'because tapping all good from the cab is fraud that costs CDLs '
                                     '[Trucking Life with Shawn — UlW-GlLugUg @ 00:06:26].']}}],
 'pull_quote': "FMCSA is not going to text you when a broker's bond drops below $75,000. So, it will "
               'basically be up to you to start vetting these brokers like crazy. Trucking Made Successful '
               '(iwQkqbEBCrM @ 00:07:27).',
 'diagram_id': 'diag-05',
 'action_checklist': ['Before booking, check the broker on SAFER and the licensing and insurance portal, '
                      'confirm the BMC-84 or BMC-85 is current and active, and call the bond agency to '
                      'verify the $75,000 [Trucking Made Successful — iwQkqbEBCrM @ 00:08:15].',
                      'Use a DAT or Truckstop higher-tier load board to watch broker credit score and days '
                      'to pay over time, and treat rising days to pay as a cash-flow warning [Trucking '
                      'Made Successful — iwQkqbEBCrM @ 00:09:11].',
                      "Check a counterparty's full revocation history rather than today's status, ask for "
                      'USDOT and MC numbers, and question repeated notices or revoke-then-reinstate '
                      'patterns [Transportli — HRlIiVKracc @ 00:01:40].',
                      'If Motus breaks your record, screenshot everything with a date, open one support '
                      'ticket and stay on it, ignore emails demanding a fix fee, and escalate to your '
                      'state trucking association, congressman, and the trucking press [Jim Campbell - '
                      'Official Trucking Channel — misVtmF2XjA @ 00:08:05].',
                      'File FMCSA complaints on brokers using a different name or misusing your '
                      'registration with dates, company names, DOT numbers, emails, pictures, and '
                      'documents, then save the case number [Freight Pro Hub — 8X37vkZBHyo @ 00:03:23].',
                      'Challenge any violation you believe is wrong through DataQs, which now runs a '
                      'three-stage independent review where the first reviewer is not the issuing officer '
                      '[Trucking Life with Shawn — UlW-GlLugUg @ 00:09:12].'],
 'statutory_citations': [{'title': 'Trucking Made Successful — R.I.P. Broke Brokers: FMCSA’s New Rule '
                                   'Kicks In Jan 16 – What Every Carrier MUST Know [00:04:47]',
                          'url': 'https://www.youtube.com/watch?v=iwQkqbEBCrM&t=287s',
                          'relevance': 'Primary practitioner testimony on the seven-day replenishment rule '
                                       'and broker authority revocation below $75,000.'},
                         {'title': 'Mutha Trucker - Official Trucking Channel — Big Win! FMCSA Will '
                                   'Shutdown Thousands Of Freight Brokers In 2026 🤯 [00:06:07]',
                          'url': 'https://www.youtube.com/watch?v=ZSZAVstSGl8&t=367s',
                          'relevance': 'Primary practitioner testimony on the 2026 crackdown on fake trust '
                                       'funds, unregulated trust providers, and non-cash assets.'},
                         {'title': 'Jim Campbell - Official Trucking Channel — FMCSA Computer Glitch Is '
                                   'Causing Inactive DOT Numbers For Trucking Companies [00:03:39]',
                          'url': 'https://www.youtube.com/watch?v=misVtmF2XjA&t=219s',
                          'relevance': 'Primary practitioner testimony on Motus hazmat mislabeling, '
                                       'inflated coverage requirements, and automatic authority shutoffs.'},
                         {'title': 'FMCSA — Defining FMCSA Operating Authority Types for Freight '
                                   'Forwarders and Brokers (FMCSA OFFICIAL VIDEO) [00:08:35]',
                          'url': 'https://www.youtube.com/watch?v=qJ2zB-OEb8o&t=515s',
                          'relevance': 'Primary practitioner testimony on the $75,000 surety bond or trust '
                                       'fund requirement for brokers and freight forwarders.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'iwQkqbEBCrM',
                       'title': 'R.I.P. Broke Brokers: FMCSA’s New Rule Kicks In Jan 16 – What Every '
                                'Carrier MUST Know',
                       'channel': 'Trucking Made Successful',
                       'author': 'Trucking Made Successful',
                       'text': "If a broker's surety bond of $75,000 falls below $75,000 and they do not "
                               'replenish that amount within seven calendar days, the FMCSA has the '
                               "authority to revoke the broker's operating authority.",
                       'tip': "If a broker's surety bond of $75,000 falls below $75,000 and they do not "
                              'replenish that amount within seven calendar days, the FMCSA has the '
                              "authority to revoke the broker's operating authority.",
                       'timestamp': 287,
                       'timestamp_seconds': 287,
                       'timestamp_label': '[00:04:47]',
                       'url': 'https://www.youtube.com/watch?v=iwQkqbEBCrM&t=287s',
                       'markdown': '[00:04:47](https://www.youtube.com/watch?v=iwQkqbEBCrM&t=287s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iwQkqbEBCrM',
                       'title': 'R.I.P. Broke Brokers: FMCSA’s New Rule Kicks In Jan 16 – What Every '
                                'Carrier MUST Know',
                       'channel': 'Trucking Made Successful',
                       'author': 'Trucking Made Successful',
                       'text': 'They are rated an F with RTS Factoring, their credit score is in the '
                               'toilet, yet they continue posting and selling loads to carriers.',
                       'tip': 'They are rated an F with RTS Factoring, their credit score is in the '
                              'toilet, yet they continue posting and selling loads to carriers.',
                       'timestamp': 322,
                       'timestamp_seconds': 322,
                       'timestamp_label': '[00:05:22]',
                       'url': 'https://www.youtube.com/watch?v=iwQkqbEBCrM&t=322s',
                       'markdown': '[00:05:22](https://www.youtube.com/watch?v=iwQkqbEBCrM&t=322s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4m_pJHgvrpc',
                       'title': 'New FMCSA Rule to Protect Truckers from Unpaid Broker Claims',
                       'channel': 'AFT Dispatch',
                       'author': 'AFT Dispatch',
                       'text': 'I would think that yes, your authority should be suspended if it goes '
                               'below the $75,000 minimum required by the federal government.',
                       'tip': 'I would think that yes, your authority should be suspended if it goes below '
                              'the $75,000 minimum required by the federal government.',
                       'timestamp': 257,
                       'timestamp_seconds': 257,
                       'timestamp_label': '[00:04:17]',
                       'url': 'https://www.youtube.com/watch?v=4m_pJHgvrpc&t=257s',
                       'markdown': '[00:04:17](https://www.youtube.com/watch?v=4m_pJHgvrpc&t=257s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'BE6n1FfpOO8',
                       'title': 'FMCSA New Rule Change Affecting All Truck Drivers Now',
                       'channel': 'Mutha Trucker - Official Trucking Channel',
                       'author': 'Mutha Trucker - Official Trucking Channel',
                       'text': 'When you know how much the lanes are actually paying and you see something '
                               'is just completely off where the rate is just way high, then you know this '
                               'is some sort of scam or double brokering.',
                       'tip': 'When you know how much the lanes are actually paying and you see something '
                              'is just completely off where the rate is just way high, then you know this '
                              'is some sort of scam or double brokering.',
                       'timestamp': 320,
                       'timestamp_seconds': 320,
                       'timestamp_label': '[00:05:20]',
                       'url': 'https://www.youtube.com/watch?v=BE6n1FfpOO8&t=320s',
                       'markdown': '[00:05:20](https://www.youtube.com/watch?v=BE6n1FfpOO8&t=320s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Y4Qa3jy-WNw',
                       'title': "FMCSA Cracks Down On Brokers That DON'T PAY! 🚚 Major Trucking Industry "
                                'Shakeup Revealed!',
                       'channel': 'ET Transport',
                       'author': 'ET Transport',
                       'text': 'If the available financial security of a broker or freight forwarder falls '
                               "below $75,000 and they don't patch it up within seven calendar days, their "
                               'operating authority gets the red card.',
                       'tip': 'If the available financial security of a broker or freight forwarder falls '
                              "below $75,000 and they don't patch it up within seven calendar days, their "
                              'operating authority gets the red card.',
                       'timestamp': 366,
                       'timestamp_seconds': 366,
                       'timestamp_label': '[00:06:06]',
                       'url': 'https://www.youtube.com/watch?v=Y4Qa3jy-WNw&t=366s',
                       'markdown': '[00:06:06](https://www.youtube.com/watch?v=Y4Qa3jy-WNw&t=366s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8X37vkZBHyo',
                       'title': 'FMCSA Complaint Center: Report Broker Problems, Fraud & Bad Chassis',
                       'channel': 'Freight Pro Hub',
                       'author': 'Freight Pro Hub',
                       'text': "Filing a complaint doesn't automatically mean that FMCSA is going to "
                               'investigate somebody or issue a fine, and if a broker owes you money, '
                               "don't confuse this system with collecting an unpaid invoice.",
                       'tip': "Filing a complaint doesn't automatically mean that FMCSA is going to "
                              "investigate somebody or issue a fine, and if a broker owes you money, don't "
                              'confuse this system with collecting an unpaid invoice.',
                       'timestamp': 221,
                       'timestamp_seconds': 221,
                       'timestamp_label': '[00:03:41]',
                       'url': 'https://www.youtube.com/watch?v=8X37vkZBHyo&t=221s',
                       'markdown': '[00:03:41](https://www.youtube.com/watch?v=8X37vkZBHyo&t=221s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 't1CJB1XA9y0',
                       'title': 'Trucker Regs Daily: FMCSA Shuts Down YMC Transport, Trucking Jobs Flat, '
                                'Reefer Rejections Hit 21%',
                       'channel': 'the funny farm',
                       'author': 'the funny farm',
                       'text': 'If a broker or a shipper hands you a load, check the USDOT number on the '
                               'truck that shows up, not just the name on the paperwork.',
                       'tip': 'If a broker or a shipper hands you a load, check the USDOT number on the '
                              'truck that shows up, not just the name on the paperwork.',
                       'timestamp': 96,
                       'timestamp_seconds': 96,
                       'timestamp_label': '[00:01:36]',
                       'url': 'https://www.youtube.com/watch?v=t1CJB1XA9y0&t=96s',
                       'markdown': '[00:01:36](https://www.youtube.com/watch?v=t1CJB1XA9y0&t=96s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YWQYZLDM6dY',
                       'title': 'FMCSA Finally Closing Broker LOOPHOLES! | Broker Transparency 2025',
                       'channel': 'This Week in Trucking',
                       'author': 'This Week in Trucking',
                       'text': 'Brokers are only required to share that information after delivery and '
                               'only if a carrier requests it in writing.',
                       'tip': 'Brokers are only required to share that information after delivery and only '
                              'if a carrier requests it in writing.',
                       'timestamp': 43,
                       'timestamp_seconds': 43,
                       'timestamp_label': '[00:00:43]',
                       'url': 'https://www.youtube.com/watch?v=YWQYZLDM6dY&t=43s',
                       'markdown': '[00:00:43](https://www.youtube.com/watch?v=YWQYZLDM6dY&t=43s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'pK4RGE_1My4',
                       'title': 'FMCSA Compliance EXPLAINED: What Every Truck Driver & Carrier MUST Know '
                                'in 2025!',
                       'channel': 'FMCSA REGISTRATION dot com',
                       'author': 'FMCSA REGISTRATION dot com',
                       'text': 'Non-compliance can lead to hefty fines, revoked licenses, and even putting '
                               'your business at risk.',
                       'tip': 'Non-compliance can lead to hefty fines, revoked licenses, and even putting '
                              'your business at risk.',
                       'timestamp': 37,
                       'timestamp_seconds': 37,
                       'timestamp_label': '[00:00:37]',
                       'url': 'https://www.youtube.com/watch?v=pK4RGE_1My4&t=37s',
                       'markdown': '[00:00:37](https://www.youtube.com/watch?v=pK4RGE_1My4&t=37s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HRlIiVKracc',
                       'title': 'How Many Freight Brokers Lose Their Authority? (FMCSA Data Study) | '
                                'Transportli',
                       'channel': 'Transportli',
                       'author': 'Transportli',
                       'text': "One cured notice isn't a red flag, but repeated notices or a revocation "
                               'then reinstatement deserve questions, so check the full history, not just '
                               "today's status.",
                       'tip': "One cured notice isn't a red flag, but repeated notices or a revocation "
                              'then reinstatement deserve questions, so check the full history, not just '
                              "today's status.",
                       'timestamp': 100,
                       'timestamp_seconds': 100,
                       'timestamp_label': '[00:01:40]',
                       'url': 'https://www.youtube.com/watch?v=HRlIiVKracc&t=100s',
                       'markdown': '[00:01:40](https://www.youtube.com/watch?v=HRlIiVKracc&t=100s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qJ2zB-OEb8o',
                       'title': 'Defining FMCSA Operating Authority Types for Freight Forwarders and '
                                'Brokers (FMCSA OFFICIAL VIDEO)',
                       'channel': 'FMCSA',
                       'author': 'FMCSA',
                       'text': 'Both brokers and freight forwarders must have either a surety bond filed '
                               'by an insurance company or a trust fund agreement filed by a financial '
                               'institution in the amount of $75,000.',
                       'tip': 'Both brokers and freight forwarders must have either a surety bond filed by '
                              'an insurance company or a trust fund agreement filed by a financial '
                              'institution in the amount of $75,000.',
                       'timestamp': 515,
                       'timestamp_seconds': 515,
                       'timestamp_label': '[00:08:35]',
                       'url': 'https://www.youtube.com/watch?v=qJ2zB-OEb8o&t=515s',
                       'markdown': '[00:08:35](https://www.youtube.com/watch?v=qJ2zB-OEb8o&t=515s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZSZAVstSGl8',
                       'title': 'Big Win! FMCSA Will Shutdown Thousands Of Freight Brokers In 2026 🤯',
                       'channel': 'Mutha Trucker - Official Trucking Channel',
                       'author': 'Mutha Trucker - Official Trucking Channel',
                       'text': 'Starting 2026, that $75,000 needs to be real or something that can be '
                               'turned into cash very fast, with no more loans, no more fake assets, and '
                               'no more shady finance companies.',
                       'tip': 'Starting 2026, that $75,000 needs to be real or something that can be '
                              'turned into cash very fast, with no more loans, no more fake assets, and no '
                              'more shady finance companies.',
                       'timestamp': 367,
                       'timestamp_seconds': 367,
                       'timestamp_label': '[00:06:07]',
                       'url': 'https://www.youtube.com/watch?v=ZSZAVstSGl8&t=367s',
                       'markdown': '[00:06:07](https://www.youtube.com/watch?v=ZSZAVstSGl8&t=367s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5KIDTEBQD18',
                       'title': "FMCSA Just Changed These Rules.. Here's What It Means for Truckers",
                       'channel': 'thatDOTcop',
                       'author': 'thatDOTcop',
                       'text': 'FMCSA finalized 11 of 18 deregulatory proposals, and they emphasize that '
                               'the economic impact of each change is expected to be small or negligible.',
                       'tip': 'FMCSA finalized 11 of 18 deregulatory proposals, and they emphasize that '
                              'the economic impact of each change is expected to be small or negligible.',
                       'timestamp': 318,
                       'timestamp_seconds': 318,
                       'timestamp_label': '[00:05:18]',
                       'url': 'https://www.youtube.com/watch?v=5KIDTEBQD18&t=318s',
                       'markdown': '[00:05:18](https://www.youtube.com/watch?v=5KIDTEBQD18&t=318s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ksCNlUOCnHc',
                       'title': 'Breaking News! Head Of FMCSA Major Public Announcement Affecting Truck '
                                'Drivers',
                       'channel': 'Mutha Trucker - Official Trucking Channel',
                       'author': 'Mutha Trucker - Official Trucking Channel',
                       'text': 'These guys that are erasing their log books nightly are openly advertising '
                               'on Facebook 4,000 to 5,000 miles a week as a solo, and with all the same '
                               "costs it's easily a $1.50 a mile difference.",
                       'tip': 'These guys that are erasing their log books nightly are openly advertising '
                              'on Facebook 4,000 to 5,000 miles a week as a solo, and with all the same '
                              "costs it's easily a $1.50 a mile difference.",
                       'timestamp': 902,
                       'timestamp_seconds': 902,
                       'timestamp_label': '[00:15:02]',
                       'url': 'https://www.youtube.com/watch?v=ksCNlUOCnHc&t=902s',
                       'markdown': '[00:15:02](https://www.youtube.com/watch?v=ksCNlUOCnHc&t=902s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'misVtmF2XjA',
                       'title': 'FMCSA Computer Glitch Is Causing Inactive DOT Numbers For Trucking '
                                'Companies',
                       'channel': 'Jim Campbell - Official Trucking Channel',
                       'author': 'Jim Campbell - Official Trucking Channel',
                       'text': 'Three months doing it the right way, sixteen hours once somebody made '
                               "noise, so keep your records, work the system, and if it won't listen, make "
                               'some noise.',
                       'tip': 'Three months doing it the right way, sixteen hours once somebody made '
                              "noise, so keep your records, work the system, and if it won't listen, make "
                              'some noise.',
                       'timestamp': 524,
                       'timestamp_seconds': 524,
                       'timestamp_label': '[00:08:44]',
                       'url': 'https://www.youtube.com/watch?v=misVtmF2XjA&t=524s',
                       'markdown': '[00:08:44](https://www.youtube.com/watch?v=misVtmF2XjA&t=524s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UlW-GlLugUg',
                       'title': 'FMCSA Just Changed DOT Inspections For 2026 — Most Drivers Have NO Idea',
                       'channel': 'Trucking Life with Shawn',
                       'author': 'Trucking Life with Shawn',
                       'text': 'Under this new model, your most recent inspection carries the most weight, '
                               "so a clean record in earlier years doesn't matter much anymore.",
                       'tip': 'Under this new model, your most recent inspection carries the most weight, '
                              "so a clean record in earlier years doesn't matter much anymore.",
                       'timestamp': 131,
                       'timestamp_seconds': 131,
                       'timestamp_label': '[00:02:11]',
                       'url': 'https://www.youtube.com/watch?v=UlW-GlLugUg&t=131s',
                       'markdown': '[00:02:11](https://www.youtube.com/watch?v=UlW-GlLugUg&t=131s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'W2zyskEb3zQ',
                       'title': 'The Great CDL Purge Is Here — 28,000 Trucking Licenses Already GONE in '
                                '2026!',
                       'channel': 'The Trucker Report',
                       'author': 'The Trucker Report',
                       'text': 'If an inspector is not satisfied, that truck does not roll, it sits on the '
                               'shoulder or in the yard until a qualified driver comes to get it, and the '
                               'load goes late.',
                       'tip': 'If an inspector is not satisfied, that truck does not roll, it sits on the '
                              'shoulder or in the yard until a qualified driver comes to get it, and the '
                              'load goes late.',
                       'timestamp': 906,
                       'timestamp_seconds': 906,
                       'timestamp_label': '[00:15:06]',
                       'url': 'https://www.youtube.com/watch?v=W2zyskEb3zQ&t=906s',
                       'markdown': '[00:15:06](https://www.youtube.com/watch?v=W2zyskEb3zQ&t=906s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'}]}
