from __future__ import annotations

CHAPTER_9 = {'id': 'Q9',
 'chapter_id': 'Q9',
 'chapter_number': 9,
 'question_number': 9,
 'slug': 'insurance-buyer-side-inbound-calls-live-transfers',
 'question_prompt': 'How do insurance agents and call centers buy, take and close inbound calls and live '
                    'transfers?',
 'kicker': 'Q9 / THE BIG MONEY PLAYBOOKS',
 'title': 'The Insurance Buyer Side: Inbound Calls and Live Transfers',
 'subtitle': 'Insurance vertical pros and cons, inbound standards and expectations, inbound scripts and '
             'getting back on script, live transfer sales and role plays, opener-to-closer transfers, '
             'buffer times, buying qualified calls, call center software and recording, and TCPA for '
             'agents',
 'layout_template': 'tool_resource_directory',
 'reading_time_minutes': 15,
 'executive_summary': 'Buyer-side insurance operators agree that inbound calls and live transfers are a '
                      'paid conversation, and the whole game is protecting revenue per call. Integrity '
                      'Connect and Ringba run final expense inbounds on billable buffers, PRiMeCalls sets '
                      'buffers from 20 to 180 seconds, and agents who drop below roughly a $5 to $9 RPC '
                      'get paused or removed. Carlos Corona pushes at least 10 buyers and AI catch-all '
                      'agents, while John Ventura sells a single platform with dead-air refunds. The '
                      'scripts converge: open with a question, never quote price inside 90 seconds, and '
                      "qualify area, health, bank account and age early. Willie Goldberg's test turned 49 "
                      'transfers at $25 into 5 sales. Adeline runs an $18 RPC while taking about 40% of '
                      'calls. Disagreements center on refunds, buyer concentration, and follow-up.',
 'key_metrics': [{'label': 'Live Transfer Close Rate and Cost Per Sale',
                  'metric': 'Live Transfer Close Rate and Cost Per Sale',
                  'value': '5 sales from 49 transfers (about 1 in 10) at $25 per transfer, roughly '
                           '$250-300 per sale',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Two-week live transfer test run by Willie Goldberg's team, with Willie "
                             'personally closing 3 of the 5 sales',
                  'source': 'Willie Goldberg ([A4zDgHX2VWI @ 00:01:15])'},
                 {'label': 'Inbound Agent RPC and Removal Floor',
                  'metric': 'Inbound Agent RPC and Removal Floor',
                  'value': 'About $18 RPC while taking about 40% of calls; below about $9 RPC gets the '
                           'agent removed',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Adeline's revenue per call on the Integrity Connect x Ringba final expense "
                             'inbound program',
                  'source': 'FFL Success Zone | Integrity Connect Inbounds ([-YRrdoKG1xs @ 00:07:47])'},
                 {'label': 'Final Expense Billable Buffer Lengths',
                  'metric': 'Final Expense Billable Buffer Lengths',
                  'value': '20 seconds on FE raw inbound, 180 seconds on FE inbound transfer, 90 seconds '
                           'on FE Spanish and FEX, 60 seconds on CTV',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Time on a call before it becomes billable, set per campaign in PRiMe Calls '
                             'agent training',
                  'source': 'PRiMeCalls ([B5upgjqvbi4 @ 00:00:36])'},
                 {'label': 'Agency Return on Inbound Spend',
                  'metric': 'Agency Return on Inbound Spend',
                  'value': '4-5x return: $500 spent yields $2,000-2,500 issued',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Return reported for agencies buying billable inbound calls through the '
                             'Integrity Connect x Ringba program',
                  'source': 'FFL Success Zone | Integrity Connect Inbounds ([N3imbfBa8rI @ 00:45:09])'}],
 'sections': [{'section_number': 1,
               'heading': 'The Practitioner Consensus',
               'paragraphs': ['Insurance is the default starting vertical for buyers and sellers of calls '
                              'alike. Dave Mamann of WeCall calls it one of the top paying verticals '
                              'because nearly every American carries a policy, the companies are enormous, '
                              'budgets tend to be huge, and demand is somewhat recession-proof '
                              '[HxYmbtP1ydQ @ 00:01:00]. Carlos Corona, who scaled from $2,000 a week to '
                              'six-figure days, tells new operators to pick large populations and start '
                              'with insurance before financial, home services, and legal [7Q7WzSONnX4 @ '
                              '00:32:22]. On the agent side, the consensus mindset is that an inbound call '
                              'is a conversation already bought. Tyler Glennon says to always answer '
                              'inbound calls because each one is a free conversation, while warning that '
                              'transfers suit agents with money rather than time, since a single '
                              "conversation can run $50 to $100 [LvZ0uD7-Xvs @ 00:01:31]. Glennon's own "
                              'shorthand is that you either have time or money in this business. The '
                              'Integrity Connect training puts it bluntly to agents on the Ringba program: '
                              'you treat it like you already paid for it [N3imbfBa8rI @ 00:36:38]. That '
                              'framing drives everything downstream: fallback products for confused '
                              'callers, callbacks on hang-ups, and refusing to burn a billable call on a '
                              'rushed price quote.',
                              'Practitioners agree that revenue per call, or RPC, is the number that '
                              'decides whether an agent keeps getting calls, and they explain the math '
                              "from the publisher's chair. Trey and Shanti Berlin of Ringba lay it out: a "
                              '$5 RPC forces publishers to produce calls for about $4, while a $20 RPC '
                              'lets them spend about $17 per call, and ads stating $1 to $2 per day cost '
                              'at least $20 per call [N3imbfBa8rI @ 00:14:24]. Adeline runs the same '
                              'arithmetic on a $50 billable call: if an agent takes 1 in 5, the publisher '
                              'earns $10 per call and has to generate calls for $6 to $8, but agents who '
                              'take half get the $15 to $20 calls instead [-YRrdoKG1xs @ 00:12:11]. The '
                              'billing trigger is the buffer. PRiMeCalls defines it as the time on a call '
                              'before it becomes billable, and a caller who answers yes to all four '
                              'qualifying questions is a qualified, billable call even if they hang up '
                              'afterward [B5upgjqvbi4 @ 00:01:45]. The Integrity Connect team warns that '
                              'rejecting good prospects trains the algorithm toward worse calls '
                              '[N3imbfBa8rI @ 00:19:18]. The counterintuitive conclusion: taking more '
                              'billable calls buys better traffic. As Adeline puts it, the more calls you '
                              "take, the less calls you'll get of people thinking it's free.",
                              'Across six different trainers, the opening of an inbound or transferred '
                              'call follows the same rules: take control with a question, hold price back, '
                              'and qualify fast. Cody Askins says 99% of agents open with how can I help '
                              'you, which hands control to the customer, and eighty seconds later the '
                              'prospect hangs up; the rule is that the first couple minutes are key '
                              '[lRuXMEO6hbI @ 00:24:31]. In the opener-to-closer workflow, Askins '
                              'qualifies in the first 3 to 5 minutes on area, health, payment, and age, '
                              'accepting checking or savings only and refusing direct bill, Direct '
                              'Express, and money orders, because interest is already there and time is '
                              'the most precious asset [E5sK0JQaXSY @ 00:05:08]. Adeline avoids giving a '
                              'price in the first 90 seconds and says tonality matters more than the words '
                              "[-YRrdoKG1xs @ 00:17:09]. Trey's breakdown of Melissa's calls makes the "
                              'same point from the other direction: Melissa never rushed, while other '
                              'agents pounce with a price to avoid the $55 billable charge, and prices '
                              'given too early sound expensive [XaPPDdvtCAA @ 00:28:10]. Askins ends every '
                              'single turn with a question, warning that one bad question surrenders all '
                              'control and that more information only breeds analysis paralysis.'],
               'table': {'caption': 'Where the insurance call-buying practitioners line up',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Insurance pays top dollar but carrier IVRs bite',
                                   'Enormous carriers with huge budgets run robust IVRs hardened by their '
                                   'legal departments',
                                   'Only very high intent, high quality calls reliably get through the '
                                   'carrier IVR',
                                   'Ringba ([HxYmbtP1ydQ @ 00:01:39])'],
                                  ['Inbound calls are conversations the agent already paid for',
                                   'Always answer inbound calls; transfers cost $50 to $100 per '
                                   'conversation for agents with money',
                                   'Agents with time but little money should buy cheap leads instead of '
                                   'transfers',
                                   'Tyler Glennon ([LvZ0uD7-Xvs @ 00:01:31])'],
                                  ['Revenue per call decides who keeps getting routed calls',
                                   'A $5 RPC forces publishers to make calls for about $4; a $20 RPC '
                                   'allows about $17',
                                   'Taking more billable calls buys the agent better-funded, higher-intent '
                                   'traffic over time',
                                   'FFL Success Zone | Integrity Connect Inbounds ([N3imbfBa8rI @ '
                                   '00:14:24])'],
                                  ['Qualified inside the buffer means the call is billable',
                                   'Four yeses inside the buffer make a call billable even if the caller '
                                   'then hangs up',
                                   'Call back qualified hang-ups who drop before giving Social Security or '
                                   'bank details',
                                   'PRiMeCalls ([B5upgjqvbi4 @ 00:01:45])'],
                                  ['Open with control instead of asking how can I help you',
                                   '99% of agents ask how can I help you, and prospects hang up eighty '
                                   'seconds later',
                                   'End every turn with a question and keep the first couple minutes tight '
                                   'and brief',
                                   'Cody Askins ([lRuXMEO6hbI @ 00:24:31])'],
                                  ['Qualify area, health, payment, and age in the first minutes',
                                   'Licensed state, knockout health questions, checking or savings only, '
                                   'ages such as 50 to 85',
                                   'Never spend 45 to 90 minutes on a prospect who cannot qualify for '
                                   'coverage',
                                   'Cody Askins ([E5sK0JQaXSY @ 00:05:08])'],
                                  ['Multiple buyers protect routed volume from going unanswered',
                                   'Have at least 10 buyers because buyers take lunch breaks and skip some '
                                   'states',
                                   'Route overflow to backup buyers or AI agents rather than letting calls '
                                   'drop',
                                   'Ryan Clogg ([7Q7WzSONnX4 @ 00:12:16])']]}},
              {'section_number': 2,
               'heading': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Buffer discipline is the first mechanic every buyer learns. PRiMeCalls '
                              'publishes campaign-specific buffers: 20 seconds on final expense raw '
                              'inbound, 180 seconds on final expense inbound transfer, 90 seconds each on '
                              'FE Spanish, FEX straight inbound, and FEX AI inbound, and 60 seconds on CTV '
                              'call inbound [B5upgjqvbi4 @ 00:00:36]. On a 20-second call the agent only '
                              'verifies a live person and hangs up before 20 seconds if nobody greets '
                              'them. On 60, 90, and 180-second calls the agent asks four questions inside '
                              'the buffer: interested in a final expense policy, under 85, has a checking '
                              'or savings account, and understands the plans are not free [B5upgjqvbi4 @ '
                              '00:01:08]. The hard rule is never to quote pricing during the buffer, '
                              'because a price inside the buffer makes the call billable, and disputes on '
                              'calls past the buffer are usually denied. Integrity Connect runs the same '
                              'no-price rule inside 90 seconds [N3imbfBa8rI @ 00:17:51]. The billable '
                              'charge on that program runs $55, which is exactly why Trey says other '
                              "agents pounce with a price early, and why Trey held up Melissa's patient "
                              'first 90 seconds, covering not free, most affordable payment, and spouse or '
                              'kids on the line if needed, as the model [XaPPDdvtCAA @ 00:26:43].',
                              "The scripts that close are sequenced, not improvised. Melissa's order on "
                              'Integrity Connect inbounds starts with a recorded-line opener and the line '
                              'that price is going to be dependent on age, a few health questions, and a '
                              'few discount questions, then moves through state, age, living '
                              'independently, a written-down name and direct number with a digital '
                              'business card by text, broker framing, a beneficiary story, and a $15,000 '
                              'average burial cost [XaPPDdvtCAA @ 00:09:33]. The close lands on Americo at '
                              '$10k for $50 a month or $15k for $75. Adeline kills the Social Security '
                              'number objection by saying no medical exam early and again right before '
                              'asking, and presents Transamerica FE Express at $10k for $59, $20k for $80, '
                              'and $30k for $100 [-YRrdoKG1xs @ 00:27:27]. Alexander Strate frames the '
                              'application as two minutes of health and two minutes of money, then '
                              'counters a tight budget by pushing the draft date up to 30 days out '
                              '[xdbb7zNo-kk @ 00:06:24]. Peter Roberts shops about 26 companies and, for a '
                              'prospect with COPD, quotes Royal Neighbors of America at $7,000 for $88 a '
                              'month, the only South Carolina option with no two-year wait, and a carrier '
                              'that pays claims in 24 to 48 hours [6NKrG957hww @ 00:08:31].',
                              'The buying platforms and performance standards are where the unit economics '
                              "get enforced. John Ventura's dashboard example shows $347 paid per "
                              'enrollment against a $79 cost, with 700 calls turning into 180 policies, '
                              'and the platform lets agents listen, barge, and whisper on live calls '
                              "[UFWPlbDFPOg @ 00:04:29]. Ventura's traffic flow runs CMS-approved, "
                              'benefit-led ads into a quiz funnel, reveals the phone number, then has an '
                              'IVR re-ask the same questions to make sure the caller is the right person '
                              'before connecting [UFWPlbDFPOg @ 00:16:27]. For agents building their own '
                              "stack, JustCall's review prices Ringba at $127 a month with an IVR builder "
                              'that screens each caller before an agent picks up and recording billed at '
                              'one cent a minute [DOcBtaUIjpE @ 00:03:52]. On the Integrity Connect x '
                              'Ringba program, the standard is a 50-call running total: an RPC under $5, '
                              'possibly raised to $8, gets the agent turned off, and the stated target is '
                              'taking three calls out of every 10 past 90 seconds [N3imbfBa8rI @ '
                              '00:26:18]. Penalties escalate from a temporary pause to a one-week pause to '
                              'removal. Agencies on the program report a 4 to 5x return, with $500 spent '
                              'yielding $2,000 to $2,500 issued, and reformed agents climb to a $26 to $27 '
                              'RPC.'],
               'table': {'caption': 'Buffers, platforms, seat prices, and transfer economics quoted by the '
                                    'operators',
                         'headers': ['Mechanic or Tool',
                                     'Exact Number or Rule',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['PRiMeCalls campaign-specific billable buffers',
                                   'FE raw inbound 20 seconds, FE transfer 180 seconds, Spanish and FEX '
                                   '90, CTV 60',
                                   'Verify a live person on 20-second calls; run four qualifiers on longer '
                                   'buffers',
                                   'PRiMeCalls ([B5upgjqvbi4 @ 00:00:36])'],
                                  ['Integrity Connect agent performance standard',
                                   '50-call running total; an RPC under $5, possibly $8, turns the agent '
                                   'off',
                                   'Target three of every 10 calls past 90 seconds to stay live on routing',
                                   'FFL Success Zone | Integrity Connect Inbounds ([N3imbfBa8rI @ '
                                   '00:26:18])'],
                                  ['Ventura qualified-call buying platform',
                                   '$347 paid per enrollment against $79 cost; about $250 loaded into the '
                                   'wallet',
                                   'Select carriers, products, and states in under 60 seconds, then fund '
                                   'and take calls',
                                   'John Ventura ([UFWPlbDFPOg @ 00:04:29])'],
                                  ['JustCall insurance contact center seat',
                                   '$29 per agent, skills-based routing at $49, billed annually, 14-day '
                                   'free trial',
                                   'Record, transcribe, and sync calls to CRM to meet six-year Medicare '
                                   'call retention',
                                   'JustCall ([DOcBtaUIjpE @ 00:01:09])'],
                                  ['Ringba and Ricochet360 low-cost seat options',
                                   'Ringba $127 a month, recording one cent a minute; Ricochet360 $20 with '
                                   '500 minutes',
                                   'Screen callers through the IVR builder before an agent ever picks up',
                                   'JustCall ([DOcBtaUIjpE @ 00:03:52])'],
                                  ['Two-week live transfer test economics',
                                   '49 transfers at $25 each produced 5 sales, about $250 to $300 per sale',
                                   'Use transfers for reps and volume; the aged final expense pool '
                                   'converted strongest',
                                   'Willie Goldberg ([A4zDgHX2VWI @ 00:01:15])'],
                                  ['Inbound agent RPC benchmark and removal floor',
                                   'Adeline runs about $18 RPC taking roughly 40% of calls; below about $9 '
                                   'gets removed',
                                   'Take more calls to earn the $15 to $20 traffic tier from publishers',
                                   'FFL Success Zone | Integrity Connect Inbounds ([-YRrdoKG1xs @ '
                                   '00:07:47])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Insider Pro-Tips From the Phones',
                           'body': 'Four moves the closers and buyers use to squeeze more issued premium '
                                   'out of every paid call.',
                           'items': ['Swap the passive how does that sound for have you heard enough to be '
                                     "able to make a decision today, and run Derek Maybin's three "
                                     'questions (the opener, the if everything lines up commitment, then '
                                     'Visa Mastercard or American Express), which Derek finished in 4.5 '
                                     'minutes [Cody Askins — lRuXMEO6hbI @ 00:19:22].',
                                     'When a prospect wants to think about it, Adeline submits for '
                                     'approval first so the numbers are real, because only about 20% buy '
                                     "on follow-up and you'll go broke relying on it [FFL Success Zone | "
                                     'Integrity Connect Inbounds — -YRrdoKG1xs @ 00:25:29].',
                                     'If the prospect pays through Direct Express, Melissa eliminates '
                                     'Americo, which takes neither Direct Express nor credit cards, and '
                                     'pivots to Transamerica or Corebridge [FFL Success Zone | Integrity '
                                     'Connect Inbounds — XaPPDdvtCAA @ 00:33:25].',
                                     'Be your own buyer: Carlos Corona catches unanswered calls with '
                                     'Retell AI or Synthflow, captures consent, and monetizes them later '
                                     'via call-back, SMS, email, or resale as a click or another phone '
                                     'call, never as a lead [Ryan Clogg — 7Q7WzSONnX4 @ 00:13:10].']},
               'sop_steps': [{'step': 1,
                              'title': 'Configure and fund the buy',
                              'action': 'Set carriers, products, states, and wallet balance before the '
                                        'first call routes.',
                              'detail': "Ventura's call sync signup asks for carriers, lead sources, "
                                        'products, and states in under 60 seconds, captures a card with no '
                                        'charge, and has the agent load about $250 into the wallet; calls '
                                        'only arrive from the selected states [John Ventura — UFWPlbDFPOg '
                                        '@ 00:02:40].'},
                             {'step': 2,
                              'title': 'Work the buffer clean',
                              'action': 'Run the four qualifiers inside the buffer and never quote price '
                                        'there.',
                              'detail': 'Ask about interest in a final expense policy, under 85, a '
                                        'checking or savings account, and understanding the plans are not '
                                        'free; four yeses make the call billable, and a price quoted '
                                        'inside the buffer makes it billable too [PRiMeCalls — B5upgjqvbi4 '
                                        '@ 00:01:08].'},
                             {'step': 3,
                              'title': 'Run the script spine',
                              'action': 'Open on a recorded line, defer price to age, health, and '
                                        'discounts, and anchor your direct number.',
                              'detail': 'Use the opener that price is dependent on age, a few health '
                                        'questions, and a few discount questions, collect state and age, '
                                        'have the prospect write down your name and direct number, and '
                                        'text a digital business card [FFL Success Zone | Integrity '
                                        'Connect Inbounds — XaPPDdvtCAA @ 00:09:33].'},
                             {'step': 4,
                              'title': 'Lock persistency after the sale',
                              'action': 'Stay in contact before the first draft so the policy sticks.',
                              'detail': 'Adeline positions the agent as family, makes a reminder call the '
                                        'day before the draft, sends a thank-you card with a gift card, '
                                        'and shares a digital business card with photo and license number '
                                        '[FFL Success Zone | Integrity Connect Inbounds — -YRrdoKG1xs @ '
                                        '00:32:04].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ["Carlos Corona, interviewed on Ryan Clogg's channel, gives a "
                              'volume-dependent answer on how many buyers a call operation actually needs. '
                              'The beginner rule is at least 10 buyers [7Q7WzSONnX4 @ 00:12:16], yet at '
                              'high volume Corona concedes one huge buyer running 500 to 600 agents can '
                              'probably get by, while still warning that buyers take lunch breaks and skip '
                              "states [7Q7WzSONnX4 @ 00:48:40]. John Ventura's call-sync model flips the "
                              'frame: the agent sits on the buy side of a single platform, selects states, '
                              'loads about $250 into a wallet, and pays one flat price per call, with '
                              'pricing tiers still pending [UFWPlbDFPOg @ 00:16:53]. Refund policy splits '
                              'just as hard. Ventura records every call, logs IP and location, and lets '
                              'agents submit dead-air calls for a refund, pitching that you are never '
                              'stuck paying for bad calls. PRiMeCalls trains the opposite expectation: '
                              'every campaign carries its own buffer, from 20 seconds on final expense raw '
                              'inbound to 180 seconds on final expense inbound transfers, and disputes on '
                              'calls that run past the buffer are usually denied [B5upgjqvbi4 @ 00:02:34]. '
                              'Inside that buffer, PRiMe agents run four yes-or-no qualifiers and never '
                              'quote price, since a quoted price makes the call billable on the spot.',
                              'The sharpest split is pacing. Cody Askins teaches that the third question '
                              'is already the close, framed as a hypothetical, and holds up Derek Maybin '
                              "running opener, commitment question, and 'Visa Mastercard or American "
                              "Express' in about 4.5 minutes once interest is confirmed [lRuXMEO6hbI @ "
                              '00:15:28]. Askins also wants qualification on area, health, payment, and '
                              'age inside the first three to five minutes so agents never burn 45 to 90 '
                              'minutes on someone who cannot qualify [E5sK0JQaXSY @ 00:04:10]. The '
                              'Integrity Connect camp coaches the reverse. Trey praised Melissa for never '
                              'rushing, contrasting agents who pounce with a price to dodge the $55 '
                              'billable charge, and warned that prices given too early sound expensive '
                              "[XaPPDdvtCAA @ 00:26:43]. Melissa's sixteen-step order runs state, age, "
                              'beneficiary story, burial math, discount questions, knockout health '
                              'questions, and a budget check before any number appears. Openers diverge '
                              'too. Tyler Glennon opens as the underwriting advisor and forces a choice '
                              'between final expense programs or leaving a little extra for family '
                              '[LvZ0uD7-Xvs @ 00:02:27], while Askins positions as the local field '
                              'underwriter and Melissa opens on a recorded line stating price depends on '
                              'age, health, and discount questions. Alexander Strate opens even more '
                              "directly: 'help you get your life insurance set up today.'",
                              'Payment mechanics and follow-up draw open contradictions. Alexander Strate '
                              'counters a tight budget by pushing the draft date up to 30 days out '
                              '[xdbb7zNo-kk @ 00:11:48], while Adeline on the Integrity Connect side '
                              'refuses to build draft dates into the close because prospects may call the '
                              'number again and get rewritten [-YRrdoKG1xs @ 00:29:50]. On Direct Express, '
                              'Cody Askins simply will not accept it, along with direct bill and money '
                              'orders, whereas Melissa keeps the call alive by eliminating Americo and '
                              'pivoting to Transamerica or Corebridge [XaPPDdvtCAA @ 00:33:25]. Willie '
                              'Goldberg reports Direct Express prepaid cards now being screened out of the '
                              'transfer pool. Follow-up splits the same way. Peter Roberts closed a Royal '
                              'Neighbors of America policy on a callback after the prospect was in the '
                              'hospital, calling it a live transfer that was not a one call close '
                              '[6NKrG957hww @ 00:15:15]. The Integrity Connect session puts follow-up '
                              'buyers at about 20 percent but warns you will go broke thinking that way, '
                              "and Adeline's answer to think-about-it is submitting for approval first so "
                              'the numbers are real. PRiMeCalls tells agents to call back qualified '
                              'hang-ups who dropped from question fatigue, while Integrity Connect '
                              'permanently bans agents caught hanging up and calling back.'],
               'table': {'caption': 'Side-by-side playbooks where inbound insurance practitioners split',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How many buyers a call operation needs',
                                   'Beginners line up at least 10 buyers for coverage and redundancy '
                                   'across states',
                                   'At high volume one huge buyer with 500 to 600 agents can probably get '
                                   'by',
                                   'Ryan Clogg ([7Q7WzSONnX4 @ 00:12:16]); Ryan Clogg ([7Q7WzSONnX4 @ '
                                   '00:48:40])'],
                                  ['Who eats the cost of bad calls after connection',
                                   'Ventura records every call and refunds dead-air calls submitted by '
                                   'agents',
                                   'PRiMeCalls says disputes on calls past the campaign buffer are usually '
                                   'denied',
                                   'John Ventura ([UFWPlbDFPOg @ 00:01:10]); PRiMeCalls ([B5upgjqvbi4 @ '
                                   '00:02:34])'],
                                  ['When to put a price or close on the table',
                                   'Derek Maybin runs three questions to Visa Mastercard or American '
                                   'Express in 4.5 minutes',
                                   'Trey praises never rushing and says prices given too early sound '
                                   'expensive',
                                   'Cody Askins ([lRuXMEO6hbI @ 00:15:28]); FFL Success Zone | Integrity '
                                   'Connect Inbounds ([XaPPDdvtCAA @ 00:28:10])'],
                                  ['Using the draft date as a budget lever',
                                   'Strate pushes the draft date up to 30 days out to overcome a tight '
                                   'budget',
                                   'Adeline keeps draft dates out of the close because prospects call '
                                   'again and get rewritten',
                                   'FFL Agent Academy ([xdbb7zNo-kk @ 00:11:48]); FFL Success Zone | '
                                   'Integrity Connect Inbounds ([-YRrdoKG1xs @ 00:29:50])'],
                                  ['Handling Direct Express and other non-bank payers',
                                   'Askins refuses direct bill, Direct Express cards, and money orders '
                                   'outright',
                                   'Melissa drops Americo and pivots to Transamerica or Corebridge to keep '
                                   'the sale alive',
                                   'Cody Askins ([E5sK0JQaXSY @ 00:07:55]); FFL Success Zone | Integrity '
                                   'Connect Inbounds ([XaPPDdvtCAA @ 00:33:25])'],
                                  ['Live transfers versus cheaper lead types for agents',
                                   'Glennon says agents with time should buy cheap leads instead of paying '
                                   '$50 to $100 per conversation',
                                   'Goldberg calls transfers ideal for part-timers and new agents but not '
                                   'for high producers',
                                   'Tyler Glennon ([LvZ0uD7-Xvs @ 00:01:31]); Willie Goldberg '
                                   '([A4zDgHX2VWI @ 00:08:59])'],
                                  ['Handing the call from opener to closer',
                                   'Cold transfer means pressing a button to send the call straight over',
                                   'Warm transfer is a three-way conference where the opener briefs the '
                                   'closer live',
                                   'Cody Askins ([E5sK0JQaXSY @ 00:08:41]); Cody Askins ([E5sK0JQaXSY @ '
                                   '00:09:04])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The Integrity Connect inbound program punishes picky agents by the numbers. '
                              'Trey and Shanti Berlin of Ringba explain that a $5 revenue per call forces '
                              'publishers to produce calls for about $4, while a $20 RPC lets them spend '
                              'about $17 per call, so cherry-picking directly degrades traffic '
                              '[N3imbfBa8rI @ 00:14:24]. Rejecting good prospects trains the algorithm '
                              'toward worse calls, and the AI flags a buyer after roughly 30 calls with no '
                              'conversion. Over a 50-call running total, an RPC under $5, possibly raised '
                              'to $8, gets the agent turned off, and penalties escalate from a temporary '
                              'pause to a one-week pause to removal [N3imbfBa8rI @ 00:26:18]. Adeline puts '
                              'the floor near $9 and runs about $18 RPC by taking roughly 40 percent of '
                              'calls [-YRrdoKG1xs @ 00:07:47]. The math is explicit: at a $50 billable '
                              'call with one in five taken, the publisher earns $10 per call and must '
                              'generate calls for $6 to $8, while taking half unlocks the $15 to $20 calls '
                              "[-YRrdoKG1xs @ 00:12:11]. Adeline's first week still produced 20-plus "
                              'billable calls and only one sale before Adeline went back to Go Leads. The '
                              "same training flags rudeness, profanity, pushing 'this isn't free,' and "
                              'impersonating the Department of Insurance.',
                              "Lead and transfer quality fails in predictable ways. Willie Goldberg's "
                              'two-week test of 49 transfers at $25 each produced 5 sales, roughly one in '
                              'ten, putting cost per sale near $250 to $300, and the ACA pool was cut '
                              "after a single term sale [A4zDgHX2VWI @ 00:01:15]. Goldberg's bigger "
                              'warning is vendors reselling sold leads and recycling them within 30, 60, '
                              'or 90 days, which means lower persistency and more replacement, plus ads '
                              'that mislead with free, Social Security, or VA claims, which Goldberg calls '
                              'a very shady practice [A4zDgHX2VWI @ 00:09:22]. Tyler Glennon hits the same '
                              'mismatch from the agent chair: some ads promise accidental coverage at '
                              '$500,000 for about $25 a month, so the agent must redirect to real coverage '
                              'or sell accidental as a fallback because the lead is already paid for '
                              "[LvZ0uD7-Xvs @ 00:05:08]. Carlos Corona's own scars are operational: a "
                              'flights campaign built on Google showed hundreds of missed calls in Ringba '
                              'three days later because the setup was incomplete, and Corona names poor '
                              'distribution and call routing, not creative, as the biggest mistake '
                              '[7Q7WzSONnX4 @ 00:04:54]. Dave Mamann of WeCall adds that the legal '
                              'department often makes big-carrier IVRs very challenging, a roadblock '
                              'usually overcome only by high-intent calls.',
                              'John Henson, the TCPA lawyer on Henson Legal, quantifies the downside for '
                              'agents who buy or dial leads. The statute sets $500 per call, up to $1,500, '
                              'so 10 calls means $5,000, and Mariah Gates cites one agent who settled for '
                              'over $220,000, which Henson says is not the biggest number seen '
                              '[8-P7UvS--tE @ 00:01:36]. Roughly 40 percent of TCPA cases come from repeat '
                              'filers, one of whom admitted to over a thousand followers [8-P7UvS--tE @ '
                              "00:24:25]. Buying leads means betting on the vendor's compliance program: "
                              'Henson flags $3 co-reg leads, insists consent name you and match the '
                              'product, and says to seek indemnification while confirming the vendor can '
                              'actually pay, noting Quote Wizard could not trace its leads [8-P7UvS--tE @ '
                              '00:29:51]. Dialer capability alone, such as RingCentral, can make a system '
                              'an ATDS, AI voice counts as artificial voice, and verbal consent does not '
                              "qualify for marketing. A mortgage company was sued over a fake 'calling you "
                              "back, press one' AI call. On the recording side, JustCall notes Medicare "
                              'sales calls must be kept for six years, as audio for at least the first '
                              'three, and prices Ringba recording at one cent a minute on top of a $127 '
                              'monthly plan [DOcBtaUIjpE @ 00:00:15].'],
               'table': {'caption': 'Firsthand traps and the economics check each one demands',
                         'headers': ['Trap',
                                     'What Practitioners Reported',
                                     'Economics Check Or Fix',
                                     'Expert Source'],
                         'rows': [['Incomplete call routing setup at campaign launch',
                                   'Flights campaign on Google showed hundreds of missed calls in Ringba '
                                   'three days later',
                                   'Corona says poor distribution and routing, not creative, is the '
                                   'biggest mistake',
                                   'Ryan Clogg ([7Q7WzSONnX4 @ 00:04:54]); Ryan Clogg ([7Q7WzSONnX4 @ '
                                   '00:11:35])'],
                                  ['Quoting price inside the campaign buffer window',
                                   'Any price quoted inside the buffer instantly turns the call into a '
                                   'billable call',
                                   'Qualify on four yes answers first and never quote pricing during the '
                                   'buffer',
                                   'PRiMeCalls ([B5upgjqvbi4 @ 00:01:45]); PRiMeCalls ([B5upgjqvbi4 @ '
                                   '00:02:34])'],
                                  ['Cherry-picking calls and starving the publisher of revenue',
                                   'An RPC under $5 over a 50-call running total gets the agent turned off',
                                   'Take three of every ten calls past 90 seconds; reformed agents reach '
                                   '$26 to $27 RPC',
                                   'FFL Success Zone | Integrity Connect Inbounds ([N3imbfBa8rI @ '
                                   '00:26:38]); FFL Success Zone | Integrity Connect Inbounds '
                                   '([N3imbfBa8rI @ 00:50:00])'],
                                  ['Recycled and resold live transfer leads from vendors',
                                   'Vendors resell sold leads and recycle them within 30, 60, or 90 days',
                                   'Expect lower persistency and more replacement, so be careful with the '
                                   'agency used',
                                   'Willie Goldberg ([A4zDgHX2VWI @ 00:09:22]); Willie Goldberg '
                                   '([A4zDgHX2VWI @ 00:10:02])'],
                                  ['Opening inbound calls with how can I help you',
                                   'Ninety-nine percent of agents hand control away and prospects hang up '
                                   'eighty seconds later',
                                   'Finish every statement with a question and keep the first couple '
                                   'minutes tight',
                                   'Cody Askins ([lRuXMEO6hbI @ 00:24:31]); Cody Askins ([lRuXMEO6hbI @ '
                                   '00:12:31])'],
                                  ['Relying on think-about-it follow-up calls to close',
                                   'About 20 percent buy on follow-up, but relying on it means going broke',
                                   'Submit for approval first so the numbers are real before the prospect '
                                   'leaves',
                                   'FFL Success Zone | Integrity Connect Inbounds ([-YRrdoKG1xs @ '
                                   '00:24:44]); FFL Success Zone | Integrity Connect Inbounds '
                                   '([-YRrdoKG1xs @ 00:25:29])'],
                                  ['Cheap co-reg leads without traceable consent records',
                                   'Quote Wizard could not trace its leads, and $3 co-reg leads draw '
                                   'scrutiny',
                                   'Consent must name you and match the product; seek indemnification from '
                                   'a vendor that can pay',
                                   'Henson Legal ([8-P7UvS--tE @ 00:27:43]); Henson Legal ([8-P7UvS--tE @ '
                                   '00:30:35])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Clear These Four Before Taking Or Selling Paid Inbound Calls',
                           'body': 'Each check traces to a missed-call loss, a billing dispute, a platform '
                                   'removal, or a lawsuit that practitioners saw firsthand.',
                           'items': ["Audit routing and buyer coverage before scaling spend: Corona's "
                                     'incomplete Google setup produced hundreds of missed calls, and poor '
                                     'routing, not creative, is the biggest mistake [Ryan Clogg — '
                                     '7Q7WzSONnX4 @ 00:11:35].',
                                     'Hold the price until the buffer clears and the four qualifiers are '
                                     'answered, because a price quoted inside the buffer makes the call '
                                     'billable and disputes past the buffer are usually denied [PRiMeCalls '
                                     '— B5upgjqvbi4 @ 00:02:34].',
                                     'Track RPC on a 50-call running total and stay above the $5 to $8 '
                                     'floor by taking at least three of every ten calls past 90 seconds '
                                     '[FFL Success Zone | Integrity Connect Inbounds — N3imbfBa8rI @ '
                                     '00:26:38].',
                                     'Before buying any lead or transfer feed, confirm consent names you, '
                                     'matches the product, and that the vendor can actually pay an '
                                     'indemnification claim [Henson Legal — 8-P7UvS--tE @ 00:29:51].']}}],
 'pull_quote': '"The hardest part in this business is getting people on the telephone." — FFL Success Zone '
               '| Integrity Connect Inbounds (N3imbfBa8rI @ 00:48:27).',
 'diagram_id': 'diag-05',
 'action_checklist': ['Line up at least 10 buyers, fund the first buyer yourself, and send redacted '
                      'screenshots, recordings, and 10 free trial calls to prospective buyers [Ryan Clogg '
                      '— 7Q7WzSONnX4 @ 00:19:37].',
                      'Catch unanswered calls with Retell AI or Synthflow, capture consent, and monetize '
                      'later by call-back, SMS, email, or resale as a click or call, never as a lead [Ryan '
                      'Clogg — 7Q7WzSONnX4 @ 00:13:10].',
                      'Inside 60, 90, and 180-second buffers, ask the four qualifiers: final expense '
                      'interest, under 85, checking or savings account, and understands the plans are not '
                      'free [PRiMeCalls — B5upgjqvbi4 @ 00:01:08].',
                      "Open with name, thanks, and 'what can I get you more information on,' then finish "
                      'every statement with a question to keep control [Cody Askins — lRuXMEO6hbI @ '
                      '00:06:57].',
                      'Qualify area, health, payment, and age within the first three to five minutes, then '
                      'cold or warm transfer to the closer [Cody Askins — E5sK0JQaXSY @ 00:04:10].',
                      'Protect persistency with a reminder call the day before the draft, a thank-you card '
                      'with a gift card, and a digital business card with photo and license number [FFL '
                      'Success Zone | Integrity Connect Inbounds — -YRrdoKG1xs @ 00:32:04].'],
 'statutory_citations': [{'title': 'FFL Success Zone | Integrity Connect Inbounds — Inbound Call Standards '
                                   '& Expectations | Integrity Connect x Ringba Training [00:26:18]',
                          'url': 'https://www.youtube.com/watch?v=N3imbfBa8rI&t=1578s',
                          'relevance': 'Primary practitioner testimony on RPC floors, 50-call running '
                                       'totals, and escalating pause-to-removal penalties for inbound '
                                       'agents.'},
                         {'title': 'PRiMeCalls — PRiMe Calls Agent Training: How to Work Buffer Times '
                                   '[00:02:34]',
                          'url': 'https://www.youtube.com/watch?v=B5upgjqvbi4&t=154s',
                          'relevance': 'Primary practitioner testimony on buffer billing rules, '
                                       'price-quoting traps, and denied disputes.'},
                         {'title': 'Henson Legal — TCPA Compliance for Insurance Agents: What You Need to '
                                   'Know in 2026 [00:01:36]',
                          'url': 'https://www.youtube.com/watch?v=8-P7UvS--tE&t=96s',
                          'relevance': 'Primary practitioner testimony on per-call TCPA exposure, repeat '
                                       'filers, and lead vendor indemnification.'},
                         {'title': 'Ryan Clogg — How Pay Per Call Makes $100K/Day (Nobody Talks About '
                                   'This) [00:48:40]',
                          'url': 'https://www.youtube.com/watch?v=7Q7WzSONnX4&t=2920s',
                          'relevance': 'Primary practitioner testimony on buyer count, routing failures, '
                                       'and buyer redundancy at high volume.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '7Q7WzSONnX4',
                       'title': 'How Pay Per Call Makes $100K/Day (Nobody Talks About This)',
                       'channel': 'Ryan Clogg',
                       'author': 'Ryan Clogg',
                       'text': "If you're running at high volume, you are going to need quite a few "
                               'buyers.',
                       'tip': "If you're running at high volume, you are going to need quite a few buyers.",
                       'timestamp': 2920,
                       'timestamp_seconds': 2920,
                       'timestamp_label': '[00:48:40]',
                       'url': 'https://www.youtube.com/watch?v=7Q7WzSONnX4&t=2920s',
                       'markdown': '[00:48:40](https://www.youtube.com/watch?v=7Q7WzSONnX4&t=2920s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7Q7WzSONnX4',
                       'title': 'How Pay Per Call Makes $100K/Day (Nobody Talks About This)',
                       'channel': 'Ryan Clogg',
                       'author': 'Ryan Clogg',
                       'text': 'When I started, I I started making like $2,000 a week.',
                       'tip': 'When I started, I I started making like $2,000 a week.',
                       'timestamp': 1075,
                       'timestamp_seconds': 1075,
                       'timestamp_label': '[00:17:55]',
                       'url': 'https://www.youtube.com/watch?v=7Q7WzSONnX4&t=1075s',
                       'markdown': '[00:17:55](https://www.youtube.com/watch?v=7Q7WzSONnX4&t=1075s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'B5upgjqvbi4',
                       'title': 'PRiMe Calls Agent Training: How to Work Buffer Times',
                       'channel': 'PRiMeCalls',
                       'author': 'PRiMeCalls',
                       'text': 'If you quote a price inside the buffer, the call becomes billable.',
                       'tip': 'If you quote a price inside the buffer, the call becomes billable.',
                       'timestamp': 154,
                       'timestamp_seconds': 154,
                       'timestamp_label': '[00:02:34]',
                       'url': 'https://www.youtube.com/watch?v=B5upgjqvbi4&t=154s',
                       'markdown': '[00:02:34](https://www.youtube.com/watch?v=B5upgjqvbi4&t=154s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UFWPlbDFPOg',
                       'title': 'The NEW Way to Buy Qualified Calls in 2026 (Pay Per Call)',
                       'channel': 'John Ventura',
                       'author': 'John Ventura',
                       'text': "So, you're not stuck paying for bad calls ever.",
                       'tip': "So, you're not stuck paying for bad calls ever.",
                       'timestamp': 70,
                       'timestamp_seconds': 70,
                       'timestamp_label': '[00:01:10]',
                       'url': 'https://www.youtube.com/watch?v=UFWPlbDFPOg&t=70s',
                       'markdown': '[00:01:10](https://www.youtube.com/watch?v=UFWPlbDFPOg&t=70s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HxYmbtP1ydQ',
                       'title': 'Insurance Vertical Pros and Cons Explained',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'Often the legal department gets their hands on the IVR and makes the IVR '
                               'very challenging.',
                       'tip': 'Often the legal department gets their hands on the IVR and makes the IVR '
                              'very challenging.',
                       'timestamp': 99,
                       'timestamp_seconds': 99,
                       'timestamp_label': '[00:01:39]',
                       'url': 'https://www.youtube.com/watch?v=HxYmbtP1ydQ&t=99s',
                       'markdown': '[00:01:39](https://www.youtube.com/watch?v=HxYmbtP1ydQ&t=99s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'N3imbfBa8rI',
                       'title': 'Inbound Call Standards & Expectations | Integrity Connect x Ringba '
                                'Training',
                       'channel': 'FFL Success Zone | Integrity Connect Inbounds',
                       'author': 'FFL Success Zone | Integrity Connect Inbounds',
                       'text': 'The hardest part in this business is getting people on the telephone.',
                       'tip': 'The hardest part in this business is getting people on the telephone.',
                       'timestamp': 2907,
                       'timestamp_seconds': 2907,
                       'timestamp_label': '[00:48:27]',
                       'url': 'https://www.youtube.com/watch?v=N3imbfBa8rI&t=2907s',
                       'markdown': '[00:48:27](https://www.youtube.com/watch?v=N3imbfBa8rI&t=2907s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'DOcBtaUIjpE',
                       'title': '10 Best Call Center Software for Insurance (Recording, Real Prices)',
                       'channel': 'JustCall',
                       'author': 'JustCall',
                       'text': 'The rule says those calls are recorded in full and kept for six years as '
                               'audio for at least the first three.',
                       'tip': 'The rule says those calls are recorded in full and kept for six years as '
                              'audio for at least the first three.',
                       'timestamp': 15,
                       'timestamp_seconds': 15,
                       'timestamp_label': '[00:00:15]',
                       'url': 'https://www.youtube.com/watch?v=DOcBtaUIjpE&t=15s',
                       'markdown': '[00:00:15](https://www.youtube.com/watch?v=DOcBtaUIjpE&t=15s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LvZ0uD7-Xvs',
                       'title': 'How To Take Live Transfers & Inbound Calls As A Life Insurance Agent',
                       'channel': 'Tyler Glennon',
                       'author': 'Tyler Glennon',
                       'text': 'You either have time or money in this business.',
                       'tip': 'You either have time or money in this business.',
                       'timestamp': 91,
                       'timestamp_seconds': 91,
                       'timestamp_label': '[00:01:31]',
                       'url': 'https://www.youtube.com/watch?v=LvZ0uD7-Xvs&t=91s',
                       'markdown': '[00:01:31](https://www.youtube.com/watch?v=LvZ0uD7-Xvs&t=91s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'A4zDgHX2VWI',
                       'title': 'Best Leads for Part-Time Insurance Agents? (Live Transfers Explained)',
                       'channel': 'Willie Goldberg',
                       'author': 'Willie Goldberg',
                       'text': "So you have to be careful with the agency that you're using.",
                       'tip': "So you have to be careful with the agency that you're using.",
                       'timestamp': 562,
                       'timestamp_seconds': 562,
                       'timestamp_label': '[00:09:22]',
                       'url': 'https://www.youtube.com/watch?v=A4zDgHX2VWI&t=562s',
                       'markdown': '[00:09:22](https://www.youtube.com/watch?v=A4zDgHX2VWI&t=562s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xdbb7zNo-kk',
                       'title': 'Life Insurance Live Transfer Phone Sales Training with Alexander Strate',
                       'channel': 'FFL Agent Academy',
                       'author': 'FFL Agent Academy',
                       'text': "They actually don't allow me to take money over the phone.",
                       'tip': "They actually don't allow me to take money over the phone.",
                       'timestamp': 708,
                       'timestamp_seconds': 708,
                       'timestamp_label': '[00:11:48]',
                       'url': 'https://www.youtube.com/watch?v=xdbb7zNo-kk&t=708s',
                       'markdown': '[00:11:48](https://www.youtube.com/watch?v=xdbb7zNo-kk&t=708s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lRuXMEO6hbI',
                       'title': 'The Perfect Inbound Call Script For Insurance Leads [Phone Phenom Ep. 10]',
                       'channel': 'Cody Askins',
                       'author': 'Cody Askins',
                       'text': 'The more information I give them the less likely they are to make a '
                               'decision.',
                       'tip': 'The more information I give them the less likely they are to make a '
                              'decision.',
                       'timestamp': 1557,
                       'timestamp_seconds': 1557,
                       'timestamp_label': '[00:25:57]',
                       'url': 'https://www.youtube.com/watch?v=lRuXMEO6hbI&t=1557s',
                       'markdown': '[00:25:57](https://www.youtube.com/watch?v=lRuXMEO6hbI&t=1557s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'B2hBsoovtEo',
                       'title': 'Live Transfer Leads! Build Your own Mini Call Center And Get Leads For '
                                '$8.75 To $9.97 Per Transfer.',
                       'channel': 'Selling Insurance While You Sleep',
                       'author': 'Selling Insurance While You Sleep',
                       'text': "Too many platforms require you to spend countless hours you don't have in "
                               'order to use them.',
                       'tip': "Too many platforms require you to spend countless hours you don't have in "
                              'order to use them.',
                       'timestamp': 55,
                       'timestamp_seconds': 55,
                       'timestamp_label': '[00:00:55]',
                       'url': 'https://www.youtube.com/watch?v=B2hBsoovtEo&t=55s',
                       'markdown': '[00:00:55](https://www.youtube.com/watch?v=B2hBsoovtEo&t=55s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6NKrG957hww',
                       'title': 'Watch Me Make A LIVE TRANSFER Insurance Sale',
                       'channel': 'Peter Roberts',
                       'author': 'Peter Roberts',
                       'text': "It wasn't a one call close but um but a good rapport so I hope this helps "
                               'you.',
                       'tip': "It wasn't a one call close but um but a good rapport so I hope this helps "
                              'you.',
                       'timestamp': 932,
                       'timestamp_seconds': 932,
                       'timestamp_label': '[00:15:32]',
                       'url': 'https://www.youtube.com/watch?v=6NKrG957hww&t=932s',
                       'markdown': '[00:15:32](https://www.youtube.com/watch?v=6NKrG957hww&t=932s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XaPPDdvtCAA',
                       'title': 'How She Wrote $10K in 19 Inbound Calls (Full Breakdown + Live Role Play)',
                       'channel': 'FFL Success Zone | Integrity Connect Inbounds',
                       'author': 'FFL Success Zone | Integrity Connect Inbounds',
                       'text': "Like they they pounce on people and try to sell them cuz they don't want "
                               'to spend the 55 bucks.',
                       'tip': "Like they they pounce on people and try to sell them cuz they don't want to "
                              'spend the 55 bucks.',
                       'timestamp': 1622,
                       'timestamp_seconds': 1622,
                       'timestamp_label': '[00:27:02]',
                       'url': 'https://www.youtube.com/watch?v=XaPPDdvtCAA&t=1622s',
                       'markdown': '[00:27:02](https://www.youtube.com/watch?v=XaPPDdvtCAA&t=1622s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'E5sK0JQaXSY',
                       'title': 'How To Transfer A Live Call From An Opener To A Closer!',
                       'channel': 'Cody Askins',
                       'author': 'Cody Askins',
                       'text': 'Warm transfer to a closer is where the three of you are actually going to '
                               'be on the phone together.',
                       'tip': 'Warm transfer to a closer is where the three of you are actually going to '
                              'be on the phone together.',
                       'timestamp': 544,
                       'timestamp_seconds': 544,
                       'timestamp_label': '[00:09:04]',
                       'url': 'https://www.youtube.com/watch?v=E5sK0JQaXSY&t=544s',
                       'markdown': '[00:09:04](https://www.youtube.com/watch?v=E5sK0JQaXSY&t=544s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-YRrdoKG1xs',
                       'title': '📞 How to Always Get Back on Script | Inbound Final Expense Insurance '
                                'Calls',
                       'channel': 'FFL Success Zone | Integrity Connect Inbounds',
                       'author': 'FFL Success Zone | Integrity Connect Inbounds',
                       'text': "They think that's going to happen and you'll go broke if you think that "
                               'way.',
                       'tip': "They think that's going to happen and you'll go broke if you think that "
                              'way.',
                       'timestamp': 1501,
                       'timestamp_seconds': 1501,
                       'timestamp_label': '[00:25:01]',
                       'url': 'https://www.youtube.com/watch?v=-YRrdoKG1xs&t=1501s',
                       'markdown': '[00:25:01](https://www.youtube.com/watch?v=-YRrdoKG1xs&t=1501s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-YRrdoKG1xs',
                       'title': '📞 How to Always Get Back on Script | Inbound Final Expense Insurance '
                                'Calls',
                       'channel': 'FFL Success Zone | Integrity Connect Inbounds',
                       'author': 'FFL Success Zone | Integrity Connect Inbounds',
                       'text': "The more calls you take, the less calls you'll get of people thinking it's "
                               'free.',
                       'tip': "The more calls you take, the less calls you'll get of people thinking it's "
                              'free.',
                       'timestamp': 714,
                       'timestamp_seconds': 714,
                       'timestamp_label': '[00:11:54]',
                       'url': 'https://www.youtube.com/watch?v=-YRrdoKG1xs&t=714s',
                       'markdown': '[00:11:54](https://www.youtube.com/watch?v=-YRrdoKG1xs&t=714s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8-P7UvS--tE',
                       'title': 'TCPA Compliance for Insurance Agents: What You Need to Know in 2026',
                       'channel': 'Henson Legal',
                       'author': 'Henson Legal',
                       'text': "But the thing that's really disturbing to me about it is last year, I "
                               'think it was 40% of all TCPA cases were filed by someone who had filed a '
                               'TCPA case before.',
                       'tip': "But the thing that's really disturbing to me about it is last year, I think "
                              'it was 40% of all TCPA cases were filed by someone who had filed a TCPA '
                              'case before.',
                       'timestamp': 1465,
                       'timestamp_seconds': 1465,
                       'timestamp_label': '[00:24:25]',
                       'url': 'https://www.youtube.com/watch?v=8-P7UvS--tE&t=1465s',
                       'markdown': '[00:24:25](https://www.youtube.com/watch?v=8-P7UvS--tE&t=1465s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'}]}
