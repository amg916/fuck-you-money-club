from __future__ import annotations

CHAPTER_7 = {'id': 'Q7',
 'chapter_id': 'Q7',
 'chapter_number': 7,
 'question_number': 7,
 'slug': 'government-contracts-cyber-fraud-fca-exposure',
 'question_prompt': 'How do government contractors face FCA exposure from procurement conduct and '
                    'cybersecurity noncompliance, and what triggers those investigations?',
 'kicker': 'Q7 / THE BIG MONEY PLAYBOOKS',
 'title': 'Government Contracts and Cyber-Fraud: FCA Exposure for Contractors',
 'subtitle': "DOJ's Civil Cyber-Fraud Initiative, CMMC and NIST attestation risk, whistleblower triggers "
             'in defense contracting, GSA procurement-integrity and leaked-pricing cases, common contract '
             'FCA scenarios, risk prevention, defense counsel strategy, and UAP-program FCA theories',
 'layout_template': 'thirty_day_roadmap',
 'reading_time_minutes': 15,
 'executive_summary': 'Relator counsel, a former EDVA U.S. Attorney, a DOJ fraud-section alumna and '
                      "contractor-side defense firms converge on one point: since DOJ's October 2021 Civil "
                      'Cyber-Fraud Initiative, a cybersecurity gap stops being a fixable contract defect '
                      'and becomes a knowing false claim the moment an invoice goes out. Three theories '
                      'drive the cases: deficient cyber products or services, misrepresented controls such '
                      'as NIST 800-171 and SPRS certifications, and late incident reporting. The economics '
                      'are brutal: treble damages, per-claim penalties quoted from about $11,665 to '
                      "$28,619, relator shares of 15-30%, and settlements ranging from Georgia Tech's "
                      "roughly $1M to Aerojet Rocketdyne's $9M. The pipeline is insider-fed, led by "
                      'overworked security officers who say nobody listened. Practitioners split on '
                      'whether a misrepresented security posture is automatically material, whether a '
                      'breach is needed to prove materiality, and how hard relator counsel should push the '
                      'government during the seal period.',
 'key_metrics': [{'label': 'Relator Share of Government Recovery',
                  'metric': 'Relator Share of Government Recovery',
                  'value': '15% to 30%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Julie Bracker's stated range for the whistleblower's cut; even at one-third, "
                             'the government still nets double damages and the defendant also pays '
                             "attorney's fees.",
                  'source': 'ClearanceJobs ([j_QEFJG-ON4 @ 00:05:12])'},
                 {'label': 'Per-Claim Civil Penalty (July 2025)',
                  'metric': 'Per-Claim Civil Penalty (July 2025)',
                  'value': '$14,308 to $28,619 per claim',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Inflation-adjusted penalty range stacked on top of treble damages, applied '
                             'to each false claim submitted.',
                  'source': 'UAP Legion ([Y9DOny35SW0 @ 00:03:15])'},
                 {'label': 'Aerojet Rocketdyne Cyber Settlement',
                  'metric': 'Aerojet Rocketdyne Cyber Settlement',
                  'value': '$9M',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'DOJ declined to intervene; the relator case settled in April 2022 after '
                             'summary judgment was denied.',
                  'source': 'Thompson Coburn LLP ([CNlX3Qfdluw @ 00:31:43])'},
                 {'label': 'Average Qui Tam Lifecycle',
                  'metric': 'Average Qui Tam Lifecycle',
                  'value': '2 to 3 years from filing to resolution',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Bracker's average across relator-side cases, against a 60-day statutory "
                             'investigation window; the longest seal ran over 10 years.',
                  'source': 'ClearanceJobs ([j_QEFJG-ON4 @ 00:15:32])'}],
 'sections': [{'section_number': 1,
               'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner starts from the same premise: the False Claims Act is, '
                              "in Julie Bracker's words, the federal government's 'primary tool for "
                              "addressing the knowing misuse of taxpayer funds,' and since October 2021 "
                              'DOJ has pointed that tool straight at contractor cybersecurity [j_QEFJG-ON4 '
                              "@ 00:01:33]. Thompson Coburn's panel dates the Civil Cyber-Fraud Initiative "
                              'to that October 2021 announcement, enforcing 31 USC 3729 against knowing '
                              'cybersecurity violations, in a year when FCA recoveries topped $5.6B, more '
                              "than $5B of it from healthcare [CNlX3Qfdluw @ 00:05:25]. PilieroMazza's "
                              'cyber team is blunt about the design: the initiative does not invent any '
                              'new cybersecurity requirements; it uses the FCA to enforce the ones already '
                              'sitting in your contracts and to deter noncompliance [OqheRWaihEo @ '
                              '01:08:36]. Blue Ocean Law Group frames the before-and-after in operator '
                              'terms: before 2021 a vulnerability was a fixable fine, after 2021 it is '
                              "fraud, because 'the crime is the lie' [4mXSodsYqr4 @ 00:03:00]. The "
                              'consensus takeaway is that cyber exposure now rides on representations '
                              'rather than on incidents. A contractor that certifies controls it does not '
                              'actually run, then keeps billing against those certifications, has handed '
                              'both DOJ and any disgruntled insider a ready-made theory that requires no '
                              'stolen data and no breach report. That is the baseline every speaker builds '
                              'on.',
                              'On the theories of liability, the speakers are unanimous. Jones Day lays '
                              'out the three uses DOJ announced: knowingly failing to comply with '
                              'cybersecurity standards, knowingly misrepresenting controls such as '
                              'encryption claims or incident-response plans, and knowingly failing to '
                              'timely report cyber incidents [ah8GhXnbe-8 @ 00:00:57]. Bracker maps the '
                              'same trio onto contractor paperwork, treating every NIST and DFARS '
                              'certification made since January 1, 2018 as a potential misrepresentation '
                              'and arguing that an inaccurate SPRS score carries a duty to correct, with '
                              "'no patience' for riding out the three-year recertification cycle "
                              '[j_QEFJG-ON4 @ 00:08:40]. The scienter line is equally settled. Thompson '
                              'Coburn stresses that the knowledge standard means actual knowledge, '
                              'deliberate ignorance or reckless disregard, a lower bar than the CFAA '
                              'hacking statute, yet one that still excludes innocent mistake, mere error '
                              "or negligence [CNlX3Qfdluw @ 00:12:17]. PilieroMazza's Matt Feinberg and "
                              "Camilla Hundley compress it into one line: 'a mere mistake or accident' is "
                              'not enough, but recklessness is [ZyG_Zu7OvIg @ 00:04:45]. For an operator, '
                              'the practical read is that ignorance stops being a shelter once warning '
                              'signs exist. Deliberate ignorance and reckless disregard sit inside the '
                              'definition, so a company that declines to look at its own security posture, '
                              'then invoices on the strength of that posture, has walked into the standard '
                              'rather than around it.',
                              'The third pillar of consensus is that the invoice, not the breach, is the '
                              'trigger. Daniel Strauss of Cordatus LLP, speaking on CMMC LaunchPad, '
                              'describes two liability paths: representations made at proposal or award, '
                              'covering 8(a) status, 51% veteran ownership and cyber status, and an '
                              'implied re-certification riding on every invoice, which the government '
                              'reads as a license to claw back every contract dollar [GkIQylusGaw @ '
                              '00:05:21]. Blue Ocean Law Group lands in the same place, warning that '
                              'simply sending an invoice while noncompliant can be a false claim and '
                              "calling the Act 'the government's number one weapon for fighting fraud' "
                              '[4mXSodsYqr4 @ 00:01:21]. The speakers also agree on who pulls the trigger. '
                              'Jones Day flags the overworked, under-resourced information security '
                              "officer as 'somebody who could legitimately turn out to be a whistleblower' "
                              '[ah8GhXnbe-8 @ 00:03:26]. Former DOJ fraud-section assistant director Sarah '
                              'Mlan, interviewed by Federal News Network, confirms the pattern from the '
                              'government side: in cyber matters it is in-house cybersecurity '
                              'professionals with extensive information who come forward, typically '
                              'because nobody listened to them [ovf7HOfeGQ0 @ 00:06:38]. The baseline '
                              'prerequisite is therefore cultural as much as technical. The internal '
                              'security complaint that management shrugs off is effectively the first '
                              'draft of a sealed qui tam complaint, written by the person who knows '
                              'exactly where the gaps sit.'],
               'table': {'caption': 'Where the practitioners agree: the baseline mechanics of cyber-driven '
                                    'FCA exposure',
                         'headers': ['Consensus Point',
                                     'What Practitioners Agree On',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['FCA is the primary enforcement weapon',
                                   "The Act is DOJ's primary tool against knowing misuse of taxpayer "
                                   'funds, now aimed at cyber',
                                   'Treat every cybersecurity certification as fraud exposure rather than '
                                   'a routine IT ticket',
                                   'ClearanceJobs ([j_QEFJG-ON4 @ 00:01:33])'],
                                  ['No new rules, only new enforcement',
                                   'The initiative enforces cyber requirements already in contracts '
                                   'instead of creating new ones',
                                   'Your exposure already lives inside clauses incorporated into your '
                                   'current contract portfolio',
                                   'PilieroMazza PLLC ([OqheRWaihEo @ 01:08:36])'],
                                  ['Three announced theories of liability',
                                   'Knowing noncompliance, misrepresented security controls, and knowing '
                                   'failure to timely report incidents',
                                   'Audit standards, representations and notification windows as three '
                                   'separate exposure lanes',
                                   'Jones Day ([ah8GhXnbe-8 @ 00:00:57])'],
                                  ['Scienter floor excludes honest mistakes',
                                   'Actual knowledge, deliberate ignorance or reckless disregard count; '
                                   'innocent mistake and negligence do not',
                                   'Documented good-faith effort is what separates a contract dispute from '
                                   'fraud liability',
                                   'Thompson Coburn LLP ([CNlX3Qfdluw @ 00:12:55])'],
                                  ['Every invoice re-certifies compliance',
                                   'Implied re-certification rides on each invoice, letting the government '
                                   'seek every contract dollar back',
                                   'Never keep billing a contract while knowingly carrying unreported '
                                   'cybersecurity gaps on file',
                                   'CMMC LaunchPad ([GkIQylusGaw @ 00:05:21])'],
                                  ['No breach needs to be proven',
                                   'Promising security and failing to deliver it is fraud even when no '
                                   'data is stolen',
                                   'A clean incident history provides zero cover for false certifications '
                                   'already submitted',
                                   'Blue Ocean Law Group. innovative Counsel [iC] ([4mXSodsYqr4 @ '
                                   '00:00:32])'],
                                  ['Insiders are the relator pipeline',
                                   'In-house cybersecurity professionals holding extensive information are '
                                   'the people actually coming forward',
                                   'Unresolved internal security complaints are the leading indicator of '
                                   'incoming qui tam risk',
                                   'Federal News Network ([ovf7HOfeGQ0 @ 00:06:38])']]}},
              {'section_number': 2,
               'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The unit economics are where contractors get blindsided. Zack Trilliger, '
                              "the former EDVA U.S. Attorney who now runs a firm's DC office, walks the "
                              'math: damages triple, so $5M becomes $15M, and penalties of $14K to $28K '
                              'attach to each claim, including every invoice on an IDIQ, before suspension '
                              'and debarment even enter the picture [-2BTi30xXrA @ 00:07:24]. Daniel '
                              'Strauss pushes the base number higher, explaining that on a $1M contract '
                              "carrying $100K of profit the government's position is that the full $1M is "
                              'owed regardless of profit, and treble damages turn it into $3M [GkIQylusGaw '
                              "@ 00:49:01]. PilieroMazza's cyber panel runs the same multiplier on a $10M "
                              'contract to reach a $30M recovery claim [OqheRWaihEo @ 01:07:40]. Matt '
                              'Feinberg then layers the per-invoice penalty on top: 60 invoices means 60 '
                              'violations, a $150K billing error balloons to roughly $475K at about '
                              "'23,000 a pop,' and a $7M HUBZone contract can generate a whistleblower "
                              "share of roughly $7M on its own [ZyG_Zu7OvIg @ 00:46:22]. Trilliger's own "
                              "label for this exposure is 'extinction level events for certain companies.' "
                              'The operator lesson is to model risk per invoice rather than per contract, '
                              'because the penalty count scales directly with billing frequency, and '
                              'monthly invoicing on a multi-year IDIQ quietly stacks dozens of separate '
                              'violations onto a single underlying compliance gap.',
                              'The procedural clock is long and lopsided. Bracker notes that the statute '
                              'gives the government 60 days to investigate, which is barely enough to '
                              'assemble a team and interview the relator; extensions run from three months '
                              'to a year, the longest seal Bracker has carried lasted over ten years, and '
                              'the average case runs two to three years from filing to resolution '
                              "[j_QEFJG-ON4 @ 00:14:44]. On the government's investigative toolkit, "
                              'Trilliger reports civil investigative demands for both documents and '
                              'testimony, one of them reaching back seven years across all records, with '
                              '30-day or 14-day turnarounds and a public motion to compel waiting for '
                              'anyone who ignores them [-2BTi30xXrA @ 00:14:47]. The relator economics run '
                              'on a sliding scale. UAP Legion breaks out 15-25% when DOJ intervenes and '
                              '25-30% when it declines, so a $300M recovery pays the relator between $45M '
                              'and $90M, with the first-to-file rule rewarding whoever reaches the '
                              'courthouse first [Y9DOny35SW0 @ 00:13:09]. Sarah Mlan adds that relators '
                              "collect up to 30% plus attorney's fees and that 'you don't actually have to "
                              "have a lot of information' to qualify [ovf7HOfeGQ0 @ 00:06:04]. Low "
                              'evidentiary entry cost, a first-to-file race and a percentage-of-recovery '
                              'payout mean the relator pipeline stays full, and a contractor should assume '
                              'any known gap is already being documented by someone inside the building.',
                              'The live-fire mechanics center on SPRS scores, notification windows and '
                              'self-disclosure. Strauss gives the concrete play for a score that collapses '
                              'from 110 to -200: update SPRS and fire an FYI email to the contracting '
                              'officer now, then move to formal notice once a minimum score becomes '
                              'mandatory, partly so a competitor cannot report you first [GkIQylusGaw @ '
                              '00:14:03]. On incident reporting, Jones Day tells contractors to pull the '
                              'actual notification timeframe from each contract, because it may be vague, '
                              "such as 'reasonable time' or 'without undue delay,' or hard, like the "
                              "GDPR's 72-hour deadline [ah8GhXnbe-8 @ 00:02:05]. Thompson Coburn adds the "
                              'DFARS overlay: rapid incident reporting tied to NIST 800-171, plus '
                              'preservation of anything related to the incident for at least 90 days '
                              '[CNlX3Qfdluw @ 00:22:47]. Self-disclosure carries a measurable discount; '
                              'Bracker cites Verizon coming forward on its own and settling at a '
                              'multiplier of roughly 1.5 rather than the full treble [j_QEFJG-ON4 @ '
                              '00:12:07]. Strauss reports the same dynamic from the defense chair, where '
                              'going first let the client control the narrative and lowered the '
                              'settlement. The working rule is to treat SPRS as a living certification, '
                              "pre-map every contract's reporting deadline, and assume that whoever tells "
                              'the contracting officer first sets the terms of the conversation.'],
               'table': {'caption': 'Street numbers: penalties, clocks, splits and retention windows '
                                    'quoted by practitioners',
                         'headers': ['Mechanic',
                                     'Stated Number or Tool',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Per-claim civil penalty range',
                                   '$14,308 to $28,619 per claim as of July 2025, on top of treble damages',
                                   'Multiply by total invoice count across the contract life to size '
                                   'worst-case exposure',
                                   'UAP Legion ([Y9DOny35SW0 @ 00:03:15])'],
                                  ['Civil investigative demand turnaround',
                                   '30-day or 14-day response windows; one CID demanded seven years of all '
                                   'records',
                                   'Pre-stage document collection so a CID never forces a public motion to '
                                   'compel',
                                   'Cape Endeavors, Inc. ([-2BTi30xXrA @ 00:14:47])'],
                                  ['Seal period and case lifecycle',
                                   '60 statutory days, extensions of three months to one year, longest '
                                   'seal over ten years',
                                   'Budget legal spend and management attention for a two-to-three-year '
                                   'campaign, not weeks',
                                   'ClearanceJobs ([j_QEFJG-ON4 @ 00:14:44])'],
                                  ['Relator share sliding scale',
                                   '15-25% if DOJ intervenes, 25-30% if declined; $300M recovery pays '
                                   '$45M-$90M',
                                   'Recognize that declination does not end the case and actually raises '
                                   'the relator payout',
                                   'UAP Legion ([Y9DOny35SW0 @ 00:13:09])'],
                                  ['Incident data preservation window',
                                   'Anything related to a cyber incident must be maintained for at least '
                                   '90 days',
                                   'Lock incident artifacts immediately so destruction never becomes a '
                                   'second false-claim theory',
                                   'Thompson Coburn LLP ([CNlX3Qfdluw @ 00:22:47])'],
                                  ['POA&M gap closure deadline',
                                   'Open plan-of-action-and-milestones items must close within 180 days',
                                   'Track every open POA&M item against the clock before the next SPRS '
                                   'update',
                                   'CMMC LaunchPad ([GkIQylusGaw @ 00:36:35])'],
                                  ['Statute of limitations',
                                   'Six years, or three years from discovery, capped at a ten-year maximum',
                                   'Keep certification and invoice records retrievable for the full '
                                   'ten-year tail of exposure',
                                   'PilieroMazza PLLC ([ZyG_Zu7OvIg @ 00:50:18])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Moves the defense and relator bar actually make',
                           'body': 'These are the small, specific habits practitioners say separate a '
                                   'contract dispute from a sealed qui tam: who gets notified, how '
                                   'contracts get read, how subpoenas get narrowed, and what the insurance '
                                   'policy actually says.',
                           'items': ['Route every material change to the contracting officer, not just the '
                                     'project manager: an email for minor changes, a formal letter for an '
                                     'organizational conflict of interest [CMMC LaunchPad — GkIQylusGaw @ '
                                     '00:09:44]',
                                     "On award, 'read that thing front to back and highlight the actual "
                                     "requirements that you're responsible for' so no certification is "
                                     'made blind [PilieroMazza PLLC — OqheRWaihEo @ 00:46:52]',
                                     'Negotiate subpoena date ranges down hard; one demand reaching back '
                                     'to 2006 was narrowed to 2009-2013 [WilliamsMullen — NdqYGSN5BYc @ '
                                     '00:57:16]',
                                     "Demand explicit FCA coverage in D&O and E&O policies: 'it costs "
                                     "something but if you don't ask for it you're not going to get "
                                     "covered' [WilliamsMullen — NdqYGSN5BYc @ 01:00:31]"]},
               'sop_steps': [{'step': 1,
                              'title': 'Map every certification you are making',
                              'action': 'Build a contract-specific checklist of every cyber clause and '
                                        'representation tied to each award.',
                              'detail': 'Pull FAR 52.204-21 and its roughly 26 safeguards, the DFARS '
                                        'clause requiring NIST 800-171, and DFARS 252.204-7021 CMMC tiers '
                                        'into one register [Thompson Coburn LLP — CNlX3Qfdluw @ 00:17:58]; '
                                        'then designate a compliance employee, run internal audits and '
                                        'keep contract-specific checklists [PilieroMazza PLLC — '
                                        'ZyG_Zu7OvIg @ 00:39:01].'},
                             {'step': 2,
                              'title': 'Keep SPRS live and tell the contracting officer',
                              'action': 'Update SPRS the moment the score moves and notify the contracting '
                                        'officer in writing.',
                              'detail': 'On a drop from 110 to -200, update SPRS and send an FYI email to '
                                        'the contracting officer, escalating to formal notice once a '
                                        'minimum score is mandatory, and close POA&M gaps inside 180 days '
                                        '[CMMC LaunchPad — GkIQylusGaw @ 00:14:03].'},
                             {'step': 3,
                              'title': 'Clock every incident against the contract',
                              'action': "Pre-map each contract's notification window and lock incident "
                                        'data on discovery.',
                              'detail': "Identify whether the contract says 'reasonable time,' 'without "
                                        "undue delay' or a hard 72-hour deadline [Jones Day — ah8GhXnbe-8 "
                                        '@ 00:02:05], and preserve everything tied to the incident for at '
                                        'least 90 days [Thompson Coburn LLP — CNlX3Qfdluw @ 00:22:47].'},
                             {'step': 4,
                              'title': 'Run the CID and subpoena playbook',
                              'action': 'Freeze destruction, engage outside counsel and open a channel '
                                        'with DOJ early.',
                              'detail': "On a subpoena or CID, don't panic, call counsel and halt document "
                                        'destruction [PilieroMazza PLLC — ZyG_Zu7OvIg @ 00:44:22]; '
                                        'designate a point of contact, issue a litigation hold and line up '
                                        'IT resources [WilliamsMullen — NdqYGSN5BYc @ 00:54:27]; then stop '
                                        'any ongoing problem, investigate internally and engage DOJ early '
                                        '[Cape Endeavors, Inc. — -2BTi30xXrA @ 00:29:21].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is when to fix a bad SPRS number. Julie Bracker, a '
                              'relator-side attorney on ClearanceJobs who has practiced only FCA work '
                              'since 2005, asserts a duty to correct an inaccurate SPRS score now, has “no '
                              'patience” for waiting, and expects the defense bar to lean on the 3-year '
                              'recertification cycle instead [j_QEFJG-ON4 @ 00:08:40]. The CMMC LaunchPad '
                              "panel with Cordatus LLP's Daniel Strauss runs a tiered play: when a score "
                              'drops from 110 to -200, update SPRS and send the contracting officer an FYI '
                              'email, then switch to formal notice once a minimum score becomes mandatory, '
                              'partly so a competitor cannot report you first [GkIQylusGaw @ 00:14:36]. '
                              'Strauss adds that voluntary disclosure has been eliminated, disclosure is '
                              'now mandatory, and going first let the client control the narrative and '
                              'lowered the settlement [GkIQylusGaw @ 00:55:12]. Theodore Watson goes '
                              'further, telling contractors who spot a potential FCA issue during '
                              'performance to report it immediately, “over and beyond any mandatory '
                              'disclosure requirements,” because paying counsel beats a tarnished '
                              "reputation [uJurzK0qLLU @ 00:01:55]. Bracker's own scoreboard backs the "
                              'early-mover camp: Verizon self-disclosed and received a multiplier of about '
                              '1.5 rather than the full treble every speaker describes.',
                              'The second fault line is whether a cyber gap is fraud or just a contract '
                              "problem. Blue Ocean Law Group's narrator takes the hard line: promising "
                              'security and failing to deliver is fraud even if no data is stolen, no '
                              'breach needs to be proven, and “the crime is the lie” [4mXSodsYqr4 @ '
                              "00:00:48]. WilliamsMullen's defense panel runs the opposite playbook: a "
                              'mere breach of contract is not a False Claims Act violation, so the civil '
                              'defense goal is to convert the claim into a breach of contract and win '
                              'summary judgment, and after Escobar, years of payment despite known '
                              'noncompliance is a strong materiality defense [NdqYGSN5BYc @ 00:30:12]. '
                              "PilieroMazza PLLC's Part 1 panel sits between them: defective glue is not "
                              'an FCA violation but falsified testing is, and some product disputes look '
                              'like “a contract dispute question, not a false claim question,” yet DOJ in '
                              'certain regions has started to “grasp at those issues” [OqheRWaihEo @ '
                              '00:54:52]. On CMMC LaunchPad the split played out live: Strauss ties '
                              'materiality to what the contract says, while attendee Joe and law student '
                              'Leslie argued a misrepresented security posture is material, even though '
                              'Leslie reports contracting officers treat CMMC as a “check in the box” '
                              '[GkIQylusGaw @ 00:22:27].',
                              'Practitioners also read the enforcement machine differently. Bracker openly '
                              "opposes relator counsel who want to hold the government's “feet to the "
                              "fire” on investigations that, by Bracker's count, average 2 to 3 years from "
                              'filing to resolution [j_QEFJG-ON4 @ 00:35:03]. Former EDVA U.S. Attorney '
                              'Zack Trilliger, on Cape Endeavors, frames DOJ as reloading rather than '
                              'retreating: a May Criminal Division memo lists procurement fraud as a top '
                              'priority, Inspectors General carry on DOGE work, and the whistleblower '
                              'pipeline is unaffected by resource reallocation [-2BTi30xXrA @ 00:34:02]. '
                              "Federal News Network's guest, a former assistant director in DOJ's fraud "
                              'section, undercuts the idea of a dedicated cyber squad: there is no '
                              'separate cyber fraud unit, just a civil fraud section of about 130 lawyers '
                              "partnering with U.S. Attorney's offices and agency cyber experts who are "
                              "“essentially the clients” [ovf7HOfeGQ0 @ 00:07:48]. ASI Education's hosts "
                              'attack the compliance regime itself, floating a “hot take” that incumbents '
                              'want CMMC kept as a barrier to entry and arguing the fix is to make CMMC a '
                              'CLIN so contractors simply price to it, while phase two sits paused since '
                              'July [95bEAYfWTiY @ 00:12:20].'],
               'table': {'caption': 'Contested Calls on Cyber-FCA Exposure: Side-by-Side Practitioner '
                                    'Positions',
                         'headers': ['Contested Question',
                                     'Practitioner Position',
                                     'Counter-Position or Alternative Playbook',
                                     'Expert Source'],
                         'rows': [['Deadline for correcting an inaccurate SPRS score after discovery',
                                   'Bracker asserts a present duty to correct and has no patience for '
                                   'waiting',
                                   'Defense bar expected to argue the 3-year recertification cycle allows '
                                   'delay',
                                   'ClearanceJobs ([j_QEFJG-ON4 @ 00:08:40])'],
                                  ['How far to go on disclosure after finding a problem',
                                   'Strauss: disclosure is now mandatory, and going first lowered the '
                                   "client's settlement",
                                   'Watson: report immediately, over and beyond any mandatory disclosure '
                                   'requirements at all',
                                   'CMMC LaunchPad ([GkIQylusGaw @ 00:55:12]); Theodore Watson '
                                   '([uJurzK0qLLU @ 00:01:55])'],
                                  ['Whether a cybersecurity gap with no breach is already fraud',
                                   'Blue Ocean: promising security and failing to deliver is fraud without '
                                   'stolen data',
                                   'WilliamsMullen: a mere breach of contract is not a False Claims Act '
                                   'violation',
                                   'Blue Ocean Law Group. innovative Counsel [iC] ([4mXSodsYqr4 @ '
                                   '00:00:48]); WilliamsMullen ([NdqYGSN5BYc @ 00:11:38])'],
                                  ['Whether a misrepresented security posture is material to payment '
                                   'decisions',
                                   'Strauss ties materiality to what the specific contract actually says '
                                   'on paper',
                                   'Joe and Leslie argue posture is material although officers treat CMMC '
                                   'as check-the-box',
                                   'CMMC LaunchPad ([GkIQylusGaw @ 00:22:27])'],
                                  ['Working per-claim penalty number to use when modeling total exposure',
                                   'UAP Legion cites $14,308 to $28,619 per claim as of July 2025',
                                   'Jones Day models a maximum of about $23,000 for each false claim',
                                   'UAP Legion ([Y9DOny35SW0 @ 00:03:15]); Jones Day ([ah8GhXnbe-8 @ '
                                   '00:02:24])'],
                                  ['How the relator share splits depending on the DOJ intervention '
                                   'decision',
                                   'UAP Legion: 15 to 25% with intervention, 25 to 30% after declination',
                                   'Bracker quotes a single band of 15 to 30% of the government recovery',
                                   'UAP Legion ([Y9DOny35SW0 @ 00:13:09]); ClearanceJobs ([j_QEFJG-ON4 @ '
                                   '00:05:12])'],
                                  ['Whether CMMC functions as protection or as a market entry barrier',
                                   'ASI hosts float a hot take that incumbents want CMMC kept as a barrier',
                                   'Their fix is to make CMMC a CLIN so contractors simply price to it',
                                   'ASI Education ([95bEAYfWTiY @ 00:12:20])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The first economics check is that resolution costs can dwarf whatever the '
                              "gap saved. Thompson Coburn's panel walked through CHS, which paid $930,000 "
                              "plus $531,691 toward the relators' fees, while the relators themselves "
                              'collected $172,050 against $474,018 in reimbursements [CNlX3Qfdluw @ '
                              '00:28:02]. Their verdict: “the cost of the settlement far exceeded the '
                              'original benefit to CHS” [CNlX3Qfdluw @ 00:31:03]. Aerojet Rocketdyne shows '
                              'the declined-case trap: DOJ declined to intervene, the case kept going, '
                              'summary judgment was denied, and the company settled for $9 million on the '
                              'first day of trial, which Daniel Strauss on CMMC LaunchPad guesses compares '
                              'to a possible $100 million ask [GkIQylusGaw @ 01:01:14]. Strauss also pegs '
                              'Georgia Tech at about $1 million for having no SSP, and Trilliger notes the '
                              'investigation alone can run years and cost millions while the government '
                              'offers no settlement number upfront. Trilliger has seen defendants '
                              'fabricate SPRS scores and submit blank documents, and warns “this is '
                              'something you do not want to screw around with” [-2BTi30xXrA @ 00:29:06]. '
                              "Thompson Coburn's defense menu reflects that math: run an internal "
                              'investigation, seek declination, offer refunds, avoid parallel proceedings, '
                              'and push for the broadest release.',
                              'The second trap is assuming exposure tracks profit. The CMMC LaunchPad '
                              'panel walks the math: on a $1 million contract with $100,000 of profit, the '
                              "government's position is that the contractor owes the full $1 million, or "
                              '$3 million once trebled, “regardless of profit” [GkIQylusGaw @ 00:49:01]. '
                              "PilieroMazza's Matt Feinberg and Camilla Hundley show how fast that "
                              'compounds: 60 invoices are 60 violations at roughly $23,000 “a pop,” a '
                              '$150,000 error becomes about $475,000, and a $7 million HUBZone contract '
                              'produces a whistleblower share of about $7 million [ZyG_Zu7OvIg @ '
                              '00:46:22]. Small-business status claims carry their own multiplier: '
                              "PilieroMazza's Part 1 panel explains that deemed-certification and "
                              'presumed-loss rules set damages at three times the gross contract value '
                              'plus about $25,000 per invoice, with settlements of $48.5 million for a '
                              'pass-through and $1.75 million for failing to recertify after an '
                              'acquisition [OqheRWaihEo @ 00:20:46]. Trilliger converts the abstraction '
                              'into extinction risk: $5 million in damages becomes $15 million, penalties '
                              'of $14,000 to $28,000 attach to each claim including every IDIQ invoice, '
                              'and suspension and debarment can follow, “massive penalties like extinction '
                              'level events for certain companies” [-2BTi30xXrA @ 00:07:24].',
                              'The third failure mode is the ignored insider. Jones Day flags the '
                              'overworked, under-resourced information security officer as someone who '
                              '“could legitimately turn out to be a whistleblower” [ah8GhXnbe-8 @ '
                              "00:03:26]. Federal News Network's former DOJ fraud official confirms the "
                              'pattern from the inside: in cyber cases, in-house security professionals '
                              'holding extensive information are the ones coming forward saying “nobody '
                              'listened to me,” and a relator does not need much information to qualify '
                              "for up to 30% plus fees [ovf7HOfeGQ0 @ 00:06:38]. PilieroMazza's Feinberg "
                              'and Hundley tell contractors to take every internal complaint seriously '
                              'because the complainer can become a qui tam relator and competitors can '
                              'file too, while Bracker urges giving complainants a written resolution '
                              '[ZyG_Zu7OvIg @ 00:06:20]. Process mistakes compound the damage once DOJ '
                              'arrives. Trilliger has seen a CID demand seven years of all records, '
                              'turnaround runs 30 or 14 days, and ignoring one draws a public motion to '
                              "compel [-2BTi30xXrA @ 00:14:47]. WilliamsMullen's panel adds that people "
                              'must preserve documents and not destroy or modify them, and that D&O and '
                              'E&O coverage costs something but only exists if you ask for it.'],
               'table': {'caption': 'Firsthand Losses, Reversals and Bottlenecks Reported by Cyber-FCA '
                                    'Practitioners',
                         'headers': ['Failure Mode',
                                     'What Practitioners Saw Happen',
                                     'Economics or Consequence',
                                     'Expert Source'],
                         'rows': [['Resolving a cyber certification gap only after relators surface it',
                                   "CHS paid $930,000 plus $531,691 toward the relators' attorney fees",
                                   'The cost of the settlement far exceeded the original benefit to CHS',
                                   'Thompson Coburn LLP ([CNlX3Qfdluw @ 00:31:03])'],
                                  ['Riding a declined qui tam all the way to the trial date',
                                   'Aerojet saw summary judgment denied and settled on the first day of '
                                   'trial',
                                   "Paid $9 million against a possible $100 million ask by Strauss's "
                                   'estimate',
                                   'CMMC LaunchPad ([GkIQylusGaw @ 01:01:14]); Thompson Coburn LLP '
                                   '([CNlX3Qfdluw @ 00:31:43])'],
                                  ['Fabricating cyber scores to stay eligible for defense awards',
                                   'Some defendants fabricated SPRS scores outright and submitted blank '
                                   'documents',
                                   'Trilliger warns this is something you do not want to screw around with',
                                   'Cape Endeavors, Inc. ([-2BTi30xXrA @ 00:29:06])'],
                                  ['Treating each recurring invoice as harmless back-office paperwork',
                                   'Sixty invoices become sixty separate violations at roughly $23,000 a '
                                   'pop',
                                   'A $150,000 billing error grows to about $475,000 in total exposure',
                                   'PilieroMazza PLLC ([ZyG_Zu7OvIg @ 00:46:22])'],
                                  ['Ignoring or slow-walking a civil investigative demand from DOJ',
                                   'CIDs carry 30 or 14 day turnarounds and can reach seven years of '
                                   'records',
                                   'Ignoring one draws a public motion to compel from the government',
                                   'Cape Endeavors, Inc. ([-2BTi30xXrA @ 00:14:47])'],
                                  ['Leaving D&O and E&O insurance policies silent on FCA coverage',
                                   "PF Chang's stands as the cautionary tale on unclear insurance coverage "
                                   'terms',
                                   'Coverage costs something, but if you do not ask you are not covered',
                                   'WilliamsMullen ([NdqYGSN5BYc @ 00:59:51])'],
                                  ["Brushing off the overworked information security officer's repeated "
                                   'warnings',
                                   'Under-resourced security staff and in-house cyber professionals come '
                                   'forward saying nobody listened',
                                   "Relators qualify for up to 30% of recovery plus attorney's fees",
                                   'Jones Day ([ah8GhXnbe-8 @ 00:02:55]); Federal News Network '
                                   '([ovf7HOfeGQ0 @ 00:06:38])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Stop-Work Checks Before the Next Invoice, CID Response, or SPRS '
                                    'Filing',
                           'body': 'Each check below maps to a loss, reversal, or bottleneck practitioners '
                                   'hit firsthand; clear all four before the next invoice goes out the '
                                   'door.',
                           'items': ['Halt document destruction the moment a subpoena or CID lands, call '
                                     'counsel, and do not panic [PilieroMazza PLLC — ZyG_Zu7OvIg @ '
                                     '00:44:22].',
                                     'Calendar the CID return date on its 30- or 14-day clock; ignoring it '
                                     'triggers a public motion to compel [Cape Endeavors, Inc. — '
                                     '-2BTi30xXrA @ 00:14:47].',
                                     'Route every SPRS score change and material change to the contracting '
                                     'officer, not only the project manager [CMMC LaunchPad — GkIQylusGaw '
                                     '@ 00:09:44].',
                                     'Do not retaliate against a potential whistleblower; retaliation '
                                     'claims carry double back pay, attorney fees, and a 3-year '
                                     'limitations window [WilliamsMullen — NdqYGSN5BYc @ 00:15:39].']}}],
 'pull_quote': '“So, massive penalties like extinction level events for certain companies.” — Cape '
               'Endeavors, Inc. (-2BTi30xXrA @ 00:07:24).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Read every awarded contract front to back and highlight the actual requirements you '
                      'are responsible for [PilieroMazza PLLC — OqheRWaihEo @ 00:46:52].',
                      'When your SPRS score drops, update SPRS and send the contracting officer an FYI '
                      'email, then move to formal notice once a minimum score is mandatory [CMMC LaunchPad '
                      '— GkIQylusGaw @ 00:14:03].',
                      'Pull the incident notification timeframe from each contract and flag vague terms '
                      "like “reasonable time” versus hard windows like the GDPR's 72 hours [Jones Day — "
                      'ah8GhXnbe-8 @ 00:02:05].',
                      'Retain all data tied to a cyber incident for at least 90 days under the DFARS '
                      'reporting clause [Thompson Coburn LLP — CNlX3Qfdluw @ 00:22:47].',
                      'Pre-build a search warrant and subpoena plan: one point of contact, employee '
                      'training on agent interviews, outside counsel, a litigation hold, and IT resources '
                      '[WilliamsMullen — NdqYGSN5BYc @ 00:54:27].',
                      'Commission an outside 360-degree compliance review, stop chasing contracts you '
                      'cannot perform, and build a speak-up culture [Cape Endeavors, Inc. — -2BTi30xXrA @ '
                      '00:29:21].'],
 'statutory_citations': [{'title': 'ClearanceJobs — Defense TechCast: False Claims Act with Julie Bracker '
                                   '[00:08:40]',
                          'url': 'https://www.youtube.com/watch?v=j_QEFJG-ON4&t=520s',
                          'relevance': 'Primary practitioner testimony on the three Civil Cyber Fraud '
                                       'Initiative theories and the duty to correct an inaccurate SPRS '
                                       'score.'},
                         {'title': 'Thompson Coburn LLP — DOJ Cyber Fraud Initiative - Cyber Faces the FCA '
                                   'Hammer [00:28:02]',
                          'url': 'https://www.youtube.com/watch?v=CNlX3Qfdluw&t=1682s',
                          'relevance': 'Primary practitioner testimony on CHS settlement economics and '
                                       'relator fee exposure.'},
                         {'title': 'CMMC LaunchPad — False Claims Act and Other Risks of Non Compliance '
                                   '[00:55:12]',
                          'url': 'https://www.youtube.com/watch?v=GkIQylusGaw&t=3312s',
                          'relevance': 'Primary practitioner testimony on mandatory disclosure and going '
                                       'first to lower settlement value.'},
                         {'title': 'Cape Endeavors, Inc. — Whistleblowers, CMMC & the DOJ: The Hidden '
                                   'Triggers Behind False Claims Act Investigations [00:13:07]',
                          'url': 'https://www.youtube.com/watch?v=-2BTi30xXrA&t=787s',
                          'relevance': 'Primary practitioner testimony on CID scope, turnaround deadlines, '
                                       'and front-end counsel investment.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'j_QEFJG-ON4',
                       'title': 'Defense TechCast: False Claims Act with Julie Bracker',
                       'channel': 'ClearanceJobs',
                       'author': 'ClearanceJobs',
                       'text': 'The statute gives the US 60 days to investigate, which is exactly the '
                               'right amount of time to get a team together, maybe enough time to '
                               'interview the relator.',
                       'tip': 'The statute gives the US 60 days to investigate, which is exactly the right '
                              'amount of time to get a team together, maybe enough time to interview the '
                              'relator.',
                       'timestamp': 884,
                       'timestamp_seconds': 884,
                       'timestamp_label': '[00:14:44]',
                       'url': 'https://www.youtube.com/watch?v=j_QEFJG-ON4&t=884s',
                       'markdown': '[00:14:44](https://www.youtube.com/watch?v=j_QEFJG-ON4&t=884s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'j_QEFJG-ON4',
                       'title': 'Defense TechCast: False Claims Act with Julie Bracker',
                       'channel': 'ClearanceJobs',
                       'author': 'ClearanceJobs',
                       'text': "I always say the first defense is we didn't do anything wrong and the "
                               "second is if we did we didn't mean to.",
                       'tip': "I always say the first defense is we didn't do anything wrong and the "
                              "second is if we did we didn't mean to.",
                       'timestamp': 1144,
                       'timestamp_seconds': 1144,
                       'timestamp_label': '[00:19:04]',
                       'url': 'https://www.youtube.com/watch?v=j_QEFJG-ON4&t=1144s',
                       'markdown': '[00:19:04](https://www.youtube.com/watch?v=j_QEFJG-ON4&t=1144s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-2BTi30xXrA',
                       'title': 'Whistleblowers, CMMC & the DOJ: The Hidden Triggers Behind False Claims '
                                'Act Investigations',
                       'channel': 'Cape Endeavors, Inc.',
                       'author': 'Cape Endeavors, Inc.',
                       'text': 'This is something you do not want to screw around with.',
                       'tip': 'This is something you do not want to screw around with.',
                       'timestamp': 1701,
                       'timestamp_seconds': 1701,
                       'timestamp_label': '[00:28:21]',
                       'url': 'https://www.youtube.com/watch?v=-2BTi30xXrA&t=1701s',
                       'markdown': '[00:28:21](https://www.youtube.com/watch?v=-2BTi30xXrA&t=1701s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '95bEAYfWTiY',
                       'title': 'Can a Contract Award Survive When Competitors’ Prices Are Leaked? The FAR '
                                'is Lava Ep. 9',
                       'channel': 'ASI Education',
                       'author': 'ASI Education',
                       'text': 'The solution to me still is just make it a CLIN in the contract.',
                       'tip': 'The solution to me still is just make it a CLIN in the contract.',
                       'timestamp': 1018,
                       'timestamp_seconds': 1018,
                       'timestamp_label': '[00:16:58]',
                       'url': 'https://www.youtube.com/watch?v=95bEAYfWTiY&t=1018s',
                       'markdown': '[00:16:58](https://www.youtube.com/watch?v=95bEAYfWTiY&t=1018s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CNlX3Qfdluw',
                       'title': 'DOJ Cyber Fraud Initiative - Cyber Faces the FCA Hammer',
                       'channel': 'Thompson Coburn LLP',
                       'author': 'Thompson Coburn LLP',
                       'text': 'Defense attorneys handling these cases must know that the requisite '
                               'knowledge of a civil FCA defendant does not include an innocent mistake, '
                               'mere error, or negligence.',
                       'tip': 'Defense attorneys handling these cases must know that the requisite '
                              'knowledge of a civil FCA defendant does not include an innocent mistake, '
                              'mere error, or negligence.',
                       'timestamp': 775,
                       'timestamp_seconds': 775,
                       'timestamp_label': '[00:12:55]',
                       'url': 'https://www.youtube.com/watch?v=CNlX3Qfdluw&t=775s',
                       'markdown': '[00:12:55](https://www.youtube.com/watch?v=CNlX3Qfdluw&t=775s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CNlX3Qfdluw',
                       'title': 'DOJ Cyber Fraud Initiative - Cyber Faces the FCA Hammer',
                       'channel': 'Thompson Coburn LLP',
                       'author': 'Thompson Coburn LLP',
                       'text': 'So you can see that the cost of the settlement far exceeded the original '
                               'benefit to CHS.',
                       'tip': 'So you can see that the cost of the settlement far exceeded the original '
                              'benefit to CHS.',
                       'timestamp': 1863,
                       'timestamp_seconds': 1863,
                       'timestamp_label': '[00:31:03]',
                       'url': 'https://www.youtube.com/watch?v=CNlX3Qfdluw&t=1863s',
                       'markdown': '[00:31:03](https://www.youtube.com/watch?v=CNlX3Qfdluw&t=1863s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ah8GhXnbe-8',
                       'title': "What is the Department of Justice's Civil Cyber-Fraud Initiative?",
                       'channel': 'Jones Day',
                       'author': 'Jones Day',
                       'text': 'So, that number can grow quite exponentially, even when the government '
                               "hasn't shown that they have suffered any losses at all.",
                       'tip': 'So, that number can grow quite exponentially, even when the government '
                              "hasn't shown that they have suffered any losses at all.",
                       'timestamp': 159,
                       'timestamp_seconds': 159,
                       'timestamp_label': '[00:02:39]',
                       'url': 'https://www.youtube.com/watch?v=ah8GhXnbe-8&t=159s',
                       'markdown': '[00:02:39](https://www.youtube.com/watch?v=ah8GhXnbe-8&t=159s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GkIQylusGaw',
                       'title': 'False Claims Act and Other Risks of Non Compliance',
                       'channel': 'CMMC LaunchPad',
                       'author': 'CMMC LaunchPad',
                       'text': 'But the safest and most compliant approach will always be open and '
                               'transparent communication.',
                       'tip': 'But the safest and most compliant approach will always be open and '
                              'transparent communication.',
                       'timestamp': 675,
                       'timestamp_seconds': 675,
                       'timestamp_label': '[00:11:15]',
                       'url': 'https://www.youtube.com/watch?v=GkIQylusGaw&t=675s',
                       'markdown': '[00:11:15](https://www.youtube.com/watch?v=GkIQylusGaw&t=675s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GkIQylusGaw',
                       'title': 'False Claims Act and Other Risks of Non Compliance',
                       'channel': 'CMMC LaunchPad',
                       'author': 'CMMC LaunchPad',
                       'text': 'So technically anytime you have a reasonable basis to believe that your '
                               'company has committed some sort of false claim you are, in contract by '
                               'contract, required to report it.',
                       'tip': 'So technically anytime you have a reasonable basis to believe that your '
                              'company has committed some sort of false claim you are, in contract by '
                              'contract, required to report it.',
                       'timestamp': 3173,
                       'timestamp_seconds': 3173,
                       'timestamp_label': '[00:52:53]',
                       'url': 'https://www.youtube.com/watch?v=GkIQylusGaw&t=3173s',
                       'markdown': '[00:52:53](https://www.youtube.com/watch?v=GkIQylusGaw&t=3173s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4mXSodsYqr4',
                       'title': 'How the False Claims Act transforms CyberSecurity Non-compliance Risks '
                                'into Fraud against the US Gov',
                       'channel': 'Blue Ocean Law Group. innovative Counsel [iC]',
                       'author': 'Blue Ocean Law Group. innovative Counsel [iC]',
                       'text': 'The crime is the lie.',
                       'tip': 'The crime is the lie.',
                       'timestamp': 48,
                       'timestamp_seconds': 48,
                       'timestamp_label': '[00:00:48]',
                       'url': 'https://www.youtube.com/watch?v=4mXSodsYqr4&t=48s',
                       'markdown': '[00:00:48](https://www.youtube.com/watch?v=4mXSodsYqr4&t=48s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'OqheRWaihEo',
                       'title': 'Common Scenarios Triggering False Claims Act Violations, Part 1: Gov. '
                                'Contracts and Cybersecurity',
                       'channel': 'PilieroMazza PLLC',
                       'author': 'PilieroMazza PLLC',
                       'text': "That seems to me like that's a contract dispute question, not a false "
                               "claim question, but I'm pointing it out because we've started to see DOJ "
                               'in certain regions grasp at those issues.',
                       'tip': "That seems to me like that's a contract dispute question, not a false claim "
                              "question, but I'm pointing it out because we've started to see DOJ in "
                              'certain regions grasp at those issues.',
                       'timestamp': 3292,
                       'timestamp_seconds': 3292,
                       'timestamp_label': '[00:54:52]',
                       'url': 'https://www.youtube.com/watch?v=OqheRWaihEo&t=3292s',
                       'markdown': '[00:54:52](https://www.youtube.com/watch?v=OqheRWaihEo&t=3292s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ovf7HOfeGQ0',
                       'title': 'Trump administration looks to False Claims Act to curb cybersecurity '
                                'violations',
                       'channel': 'Federal News Network',
                       'author': 'Federal News Network',
                       'text': 'There is a section of the Justice Department, the civil fraud section, '
                               'that is sort of the mothership for False Claims Act cases.',
                       'tip': 'There is a section of the Justice Department, the civil fraud section, that '
                              'is sort of the mothership for False Claims Act cases.',
                       'timestamp': 468,
                       'timestamp_seconds': 468,
                       'timestamp_label': '[00:07:48]',
                       'url': 'https://www.youtube.com/watch?v=ovf7HOfeGQ0&t=468s',
                       'markdown': '[00:07:48](https://www.youtube.com/watch?v=ovf7HOfeGQ0&t=468s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uJurzK0qLLU',
                       'title': 'False Claims Act Defense Lawyers for Government Contractors',
                       'channel': 'Theodore Watson',
                       'author': 'Theodore Watson',
                       'text': "Immediately assess the strengths and weaknesses of the government's case, "
                               'which can save you tens of thousands in unnecessary attorney fees.',
                       'tip': "Immediately assess the strengths and weaknesses of the government's case, "
                              'which can save you tens of thousands in unnecessary attorney fees.',
                       'timestamp': 30,
                       'timestamp_seconds': 30,
                       'timestamp_label': '[00:00:30]',
                       'url': 'https://www.youtube.com/watch?v=uJurzK0qLLU&t=30s',
                       'markdown': '[00:00:30](https://www.youtube.com/watch?v=uJurzK0qLLU&t=30s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rZEktgyZwgk',
                       'title': 'False Claims Act Training',
                       'channel': 'Changing Options',
                       'author': 'Changing Options',
                       'text': 'Reporting suspected false claims is mandatory, and regular training is '
                               'required.',
                       'tip': 'Reporting suspected false claims is mandatory, and regular training is '
                              'required.',
                       'timestamp': 191,
                       'timestamp_seconds': 191,
                       'timestamp_label': '[00:03:11]',
                       'url': 'https://www.youtube.com/watch?v=rZEktgyZwgk&t=191s',
                       'markdown': '[00:03:11](https://www.youtube.com/watch?v=rZEktgyZwgk&t=191s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Y9DOny35SW0',
                       'title': 'UAP Whistleblowers: The False Claims Act',
                       'channel': 'UAP Legion',
                       'author': 'UAP Legion',
                       'text': 'The government has 60 days to investigate, though extensions are common.',
                       'tip': 'The government has 60 days to investigate, though extensions are common.',
                       'timestamp': 573,
                       'timestamp_seconds': 573,
                       'timestamp_label': '[00:09:33]',
                       'url': 'https://www.youtube.com/watch?v=Y9DOny35SW0&t=573s',
                       'markdown': '[00:09:33](https://www.youtube.com/watch?v=Y9DOny35SW0&t=573s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZyG_Zu7OvIg',
                       'title': 'Risk Prevention Strategies: FCA Risk Prevention for Government '
                                'Contractors',
                       'channel': 'PilieroMazza PLLC',
                       'author': 'PilieroMazza PLLC',
                       'text': 'Take every internal complaint seriously, because the person complaining '
                               'could become a qui tam relator, and competitors can file too.',
                       'tip': 'Take every internal complaint seriously, because the person complaining '
                              'could become a qui tam relator, and competitors can file too.',
                       'timestamp': 380,
                       'timestamp_seconds': 380,
                       'timestamp_label': '[00:06:20]',
                       'url': 'https://www.youtube.com/watch?v=ZyG_Zu7OvIg&t=380s',
                       'markdown': '[00:06:20](https://www.youtube.com/watch?v=ZyG_Zu7OvIg&t=380s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NdqYGSN5BYc',
                       'title': 'The “Risky Business” of the Federal False Claims Act:  Strategic Thinking '
                                'for 2017',
                       'channel': 'WilliamsMullen',
                       'author': 'WilliamsMullen',
                       'text': "It's important to keep in mind that a mere breach of contract is not a "
                               'False Claims Act [violation].',
                       'tip': "It's important to keep in mind that a mere breach of contract is not a "
                              'False Claims Act [violation].',
                       'timestamp': 698,
                       'timestamp_seconds': 698,
                       'timestamp_label': '[00:11:38]',
                       'url': 'https://www.youtube.com/watch?v=NdqYGSN5BYc&t=698s',
                       'markdown': '[00:11:38](https://www.youtube.com/watch?v=NdqYGSN5BYc&t=698s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NdqYGSN5BYc',
                       'title': 'The “Risky Business” of the Federal False Claims Act:  Strategic Thinking '
                                'for 2017',
                       'channel': 'WilliamsMullen',
                       'author': 'WilliamsMullen',
                       'text': "You can get that coverage, it costs something, but if you don't ask for it "
                               "you're not going to get covered.",
                       'tip': "You can get that coverage, it costs something, but if you don't ask for it "
                              "you're not going to get covered.",
                       'timestamp': 3631,
                       'timestamp_seconds': 3631,
                       'timestamp_label': '[01:00:31]',
                       'url': 'https://www.youtube.com/watch?v=NdqYGSN5BYc&t=3631s',
                       'markdown': '[01:00:31](https://www.youtube.com/watch?v=NdqYGSN5BYc&t=3631s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'}]}
