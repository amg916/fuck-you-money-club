from __future__ import annotations

CHAPTER_12 = {'id': 'Q12',
 'chapter_id': 'Q12',
 'chapter_number': 12,
 'question_number': 12,
 'slug': 'cftc-machinery-brokers-customer-protection-ai-agents',
 'question_prompt': "How does the CFTC's broader machinery—broker rules, customer protections, position "
                    'limits, automated trading and AI agents—shape the trading environment?',
 'kicker': 'Q12 / THE BIG MONEY PLAYBOOKS',
 'title': 'CFTC Machinery: Brokers, Customer Protection & AI Agents',
 'subtitle': 'What the CFTC polices, introducing brokers, swap dealer CCO reports, perpetual futures '
             'funding rates, position-limit and customer-collateral roundtables, automated trading '
             'regulation, open commission meetings, and superintelligence and know-your-agent questions',
 'layout_template': 'action_worksheet_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners agree the CFTC stack runs on registration and segregation: exchanges '
                      'list, FCMs hold margin, IBs own the client, and a broker missing CFTC or NFA '
                      "registration is one to walk away from. Brokerchampion's retail forex rails are hard "
                      'numbers: 50:1 on seven majors, 20:1 elsewhere and a $20 million RFED capital floor, '
                      'checked through NFA BASIC and enforcement records. Roundtable speakers quantified '
                      'the collateral plumbing: about 10 firms holding 80% of customer funds, 60-minute '
                      'DCO payment windows, and guarantee funds jumping from about $3 billion to $25-50 '
                      "billion under LSOC. Optiver's Liam Smith showed perpetual funding every 8 hours, "
                      'capped near 2%. The fights are over LSOC versus individual custody, source-code '
                      'access, and who answers when an AI agent misbehaves, with Frontier Forum panelists '
                      'leaning toward the firm or operator that deployed it.',
 'key_metrics': [{'label': 'RFED Minimum Capital',
                  'metric': 'RFED Minimum Capital',
                  'value': '$20 million',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Minimum capital a retail foreign exchange dealer must hold; cited as the '
                             'reason Pepperstone, IC Markets and Tickmill refuse US clients.',
                  'source': 'Brokerchampion ([CIinXD9tbVo @ 00:02:46])'},
                 {'label': 'Automated Share of Futures Trading',
                  'metric': 'Automated Share of Futures Trading',
                  'value': 'More than 70%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Share of futures trading, financial and physical, stated as automated at the '
                             'Regulation AT supplemental proposal meeting.',
                  'source': 'CFTC ([ec9Mk3slriY @ 00:00:38])'},
                 {'label': 'Customer Funds Concentration',
                  'metric': 'Customer Funds Concentration',
                  'value': 'About 10 firms hold 80% of customer funds',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Gary DeWaal of Newedge on FCM concentration during the LSOC-for-futures '
                             "debate, called 'an incredible concentration.'",
                  'source': 'CFTC ([yUqRhv7w9Vs @ 00:52:22])'},
                 {'label': 'Perpetual Funding Rate Cap',
                  'metric': 'Perpetual Funding Rate Cap',
                  'value': 'About 2% per 8 hours, up to 6% per 24 hours',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Liam Smith of Optiver on the cap applied to periodic funding payments, '
                             'typically paid three times a day.',
                  'source': 'CFTC ([ZEPjpgVSavY @ 00:08:07])'}],
 'sections': [{'number': 1,
               'title': 'The Practitioner Consensus',
               'paragraphs': ['The registration stack is the first thing every practitioner points to. '
                              'Brokerchampion lays out the chain plainly: the exchange, CME or ICE, lists '
                              'the contract, the FCM holds the margin, and the introducing broker is the '
                              'retail-facing layer, with CPOs, CTAs, swap dealers and RFEDs filling out '
                              'the roster. The operator warning is that the broker brand on the screen may '
                              'not be the entity actually holding your funds [CIinXD9tbVo @ 00:01:06]. '
                              'Simple Explain describes the IB as the futures equivalent of a stockbroker: '
                              'it owns the client relationship, hands execution to an FCM, and splits fees '
                              'and commissions with the executing firm by agreement, registered with the '
                              'CFTC and regulated by the NFA [Osx2O3SjlCA @ 00:00:38]. The economics are '
                              'specialization. Most FCMs find nationwide offices financially impossible, '
                              'so local IBs, often one-person shops, supply the client reach while the FCM '
                              'carries platforms, account management and exchange relationships that most '
                              "IBs cannot afford to build. Earn2Trade's host Chris states that anyone "
                              'entering commodity futures must register with the CFTC first [fGEHMyG3ktY @ '
                              '00:02:17], and Brokerchampion says a broker missing either CFTC or NFA '
                              'registration is operating illegally [dvFmfWlkYq0 @ 00:08:04]. Their rule of '
                              'thumb is blunt: if either registration is missing, walk away.',
                              'On customer money, the consensus starts with segregation and daily '
                              'visibility. Brokerchampion traces daily reporting of customer funds to the '
                              '2011 MF Global collapse, with any shortfall triggering immediate action, '
                              'and is blunt that the CFTC does not reimburse trading losses [CIinXD9tbVo @ '
                              '00:04:04]. At the CFTC customer-collateral roundtable, Bill Thumb of '
                              'Vanguard/ICI said clients are astonished to learn they carry '
                              'fellow-customer risk inside an FCM pool and have no way to diligence it; '
                              'the prize everyone keeps circling is portability, margin walled off from '
                              'both the FCM and the defaulting client [yUqRhv7w9Vs @ 00:09:09]. Gary '
                              'DeWaal of Newedge put a number on the concentration problem: about 10 firms '
                              'hold 80% of customer funds, which they called an incredible concentration '
                              '[yUqRhv7w9Vs @ 00:52:22]. Even speakers who fought over LSOC agreed the buy '
                              'side will pay for safety; the Kalpers speaker framed it as return of '
                              "capital, not return on capital. Vanguard's public-disclosure wish list ran "
                              'to daily segregation reports, residual interest, monthly unaudited '
                              'financials and leverage, and reportable events. At the follow-on disclosure '
                              'roundtable, Todd, speaking for grain hedgers, said post-MF Global due '
                              'diligence and the ability to switch FCMs are what matter, and that '
                              'information plus the ability to port is the final backstop when mandated '
                              'clearing leaves no alternative [vqL3OS8Ot9o @ 02:26:16].',
                              'For AI trading agents, the practitioners converge on one principle: a human '
                              'or a firm stays on the hook. At the CFTC Frontier Forum, Chairman Selig '
                              'framed the open questions as developer registration, liability and know '
                              'your agent, and said regulation should rest on function, control and '
                              'economic reality [Ckw1w5mSMIQ @ 00:08:29]. Kush Bavaria of ORN said the '
                              'firm is liable for its agents and recommended chain-of-thought review and '
                              'red-teaming, while Brendan Ryan of Tempo said the operator is liable and '
                              'that risk controls and audit logs belong outside the agent harness '
                              '[Ckw1w5mSMIQ @ 01:04:27]. Andrew Ciraa of ICI compared an agent blunder to '
                              'an Excel spreadsheet error: the fund manager stays accountable, and that '
                              'should not fundamentally change [Ckw1w5mSMIQ @ 02:23:26]. The AI in '
                              'Regulated Industries narrator lands in the same place from the European '
                              'angle, arguing know your agent already exists under MiFID II in everything '
                              'but name, and that the move is to register the principal, not the '
                              'developer, and tag every order with an agent ID [bsDlbXqvPok @ 00:02:19]. '
                              'Brett Harrison of Architect added the operating reality: CME already '
                              'requires pre-registered operator IDs that feed commitments of traders and '
                              'position limits, and venues reject orders without them. As one Frontier '
                              "Forum panelist put it, the super intelligent agents are super, but they're "
                              'not special.'],
               'table': {'caption': 'Where Brokers, Clearing Speakers and AI Panelists Agree',
                         'headers': ['Consensus Point',
                                     'What Practitioners Say',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Brand versus actual fund holder',
                                   'The broker brand you see on screen may not be the entity holding your '
                                   'funds',
                                   'Identify which registered FCM actually carries your margin before '
                                   'wiring any money',
                                   'Brokerchampion ([CIinXD9tbVo @ 00:01:06])'],
                                  ['Introducing broker business model',
                                   'The IB owns the client relationship, delegates execution to an FCM, '
                                   'and splits fees by agreement',
                                   'Build client reach locally and rent platforms, account management and '
                                   'exchange access from the FCM',
                                   'Simple Explain ([Osx2O3SjlCA @ 00:00:38])'],
                                  ['Dual CFTC and NFA registration',
                                   'A broker without both CFTC and NFA registration is described as '
                                   'operating illegally',
                                   'Run every counterparty through registration lookups and walk away if '
                                   'either is missing',
                                   'Brokerchampion ([dvFmfWlkYq0 @ 00:08:04])'],
                                  ['Register before entering futures',
                                   'Any firm or person entering commodity futures must first register with '
                                   'the CFTC',
                                   'Treat registration as step zero; noncompliance brings heavy fines and '
                                   'possibly lengthy jail time',
                                   'Earn2Trade ([fGEHMyG3ktY @ 00:02:17])'],
                                  ['Fellow-customer risk is real',
                                   'Clients are astonished to learn they carry fellow-customer risk they '
                                   'cannot diligence inside the pool',
                                   'Prioritize portability and segregation that shields margin from both '
                                   'the FCM and defaulting clients',
                                   'CFTC ([yUqRhv7w9Vs @ 00:09:09])'],
                                  ['FCM concentration of customer money',
                                   'About 10 firms hold 80% of customer funds, called an incredible '
                                   'concentration',
                                   'Ask FCMs about client concentration and keep the ability to switch or '
                                   'port positions',
                                   'CFTC ([yUqRhv7w9Vs @ 00:52:22])'],
                                  ['Accountability for AI agents',
                                   'The firm is liable for its agents; chain-of-thought review and '
                                   'red-teaming are recommended controls',
                                   'Assign every deployed agent to a responsible firm and named human '
                                   'before it trades',
                                   'CFTC ([Ckw1w5mSMIQ @ 01:17:32])']]}},
              {'number': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The retail forex rails are hard numbers. Brokerchampion says RFEDs must '
                              'register and join the NFA, with leverage capped at 50:1 on seven majors and '
                              '20:1 on everything else, against offshore brokers that commonly advertise '
                              '500:1 or 1,000:1 [CIinXD9tbVo @ 00:01:56]. In dollar terms, $1,000 controls '
                              'up to $50,000 on a major or $20,000 on other pairs, with the EU/UK cap at '
                              '30:1 [dvFmfWlkYq0 @ 00:03:58]. The capital wall is a $20 million minimum '
                              'for an RFED, which is why Pepperstone, IC Markets and Tickmill refuse US '
                              'clients; on top sit fund segregation, daily reporting, FIFO execution and a '
                              'ban on same-pair hedging [CIinXD9tbVo @ 00:02:46]. Rule 4.41 forces a '
                              'hypothetical-results disclaimer on performance marketing. Enforcement '
                              'firepower is real: FY2024 brought 58 actions and over $17 billion in '
                              'relief, dominated by spoofing and crypto cases. The verification drill is '
                              'three steps: run the firm through NFA BASIC by name or ID, search the CFTC '
                              'enforcement database including principals and disqualification records, '
                              'then pull the monthly RFED financial filings [dvFmfWlkYq0 @ 00:07:10]. '
                              "Complaints escalate from NFA to CFTC to DOJ. Brokerchampion's closing "
                              'filter is simple: the broker worth using is the one whose registration, '
                              'funds and conduct you can verify.',
                              'Inside the collateral plumbing, the CFTC roundtable speakers put timing and '
                              'cost numbers on the table. Ron Filler of New York Law School noted MF '
                              'Global had about 35,000 futures accounts, DCOs had floated 50-70% margin '
                              'increases, and guarantee funds of about $3 billion could balloon to $25-50 '
                              'billion or more under LSOC [yUqRhv7w9Vs @ 00:20:27]. A Kansas City Board of '
                              'Trade speaker said customers get five business days to meet a margin call, '
                              'and a DCO cannot wait that long. On the CME-SIBA guaranteed clearing '
                              'participant model, Mark of SIBA said the FCM gets notified 45 minutes to an '
                              'hour before 7:30 central to top up the DCO settlement account, with excess '
                              "margin sitting in an individual segregated account in the customer's name "
                              'for the benefit of the DCO [yUqRhv7w9Vs @ 02:09:56]. Scott Paris of BMO '
                              'Harris countered that individual segregation turns net payments into many '
                              'separate early-morning DCO calls that must be met within 60 minutes, with '
                              'no flexibility [yUqRhv7w9Vs @ 02:22:09]. Joe of the KC Board of Trade '
                              'priced the wire burden: 250 days of variation margin at $4 per wire comes '
                              'to about $1,000 of DCO expense against a $4 fee [yUqRhv7w9Vs @ 02:47:09]. '
                              'Mark called custody cost a red herring at about a couple of thousand '
                              'dollars for an account.',
                              "For machine traders, the numbers come from the CFTC's own meetings. At the "
                              'Regulation AT supplemental meeting, the Chairman said more than 70% of '
                              'futures trading is automated; the registration trigger was an average of '
                              '20,000 contracts a day over six months across all products and DCMs, own '
                              'and customer accounts counted, with staff estimating about 120 AT persons, '
                              'roughly 70 already registered and 50 new [ec9Mk3slriY @ 00:33:25]. Source '
                              'code and log files carried five-year retention, reachable only by subpoena '
                              'or a Commission-authorized special call. Chairman Selig later said that '
                              'rule was never finalized and is ill suited to today [Ckw1w5mSMIQ @ '
                              '00:02:40]. On product mechanics, Liam Smith of Optiver walked through the '
                              'onshore perpetual: funding is paid typically every 8 hours, capped near 2% '
                              'per 8 hours or 6% a day; with the index at $100,000, the perp at $101,000 '
                              'and a $10,000 notional long at 1%, $100 moves to the short [ZEPjpgVSavY @ '
                              '00:08:40]. Onshore liquidation cancels open orders and sends a market '
                              'order, with residual losses hitting the guarantee fund or default '
                              "waterfall. For agents, the AI in Regulated Industries narrator's build list "
                              'is concrete: per-agent and per-strategy IDs, a named human owner, hard '
                              'limits, logged mandates and a tested kill switch [bsDlbXqvPok @ 00:03:00].'],
               'table': {'caption': 'Hard Numbers and Mechanics Operators Can Act On',
                         'headers': ['Mechanic',
                                     'Exact Number or Rule Stated',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Retail forex leverage caps',
                                   '50:1 on seven major pairs and 20:1 on all others; offshore commonly '
                                   '500:1 or 1,000:1',
                                   'Size US retail forex positions to the cap and treat offshore leverage '
                                   'offers as a red flag',
                                   'Brokerchampion ([CIinXD9tbVo @ 00:01:56])'],
                                  ['RFED capital floor',
                                   'At least $20 million in capital; Pepperstone, IC Markets and Tickmill '
                                   'refuse US clients',
                                   'Expect only well-capitalized RFEDs onshore and check monthly RFED '
                                   'financial filings',
                                   'Brokerchampion ([CIinXD9tbVo @ 00:02:46])'],
                                  ['Perpetual funding payments',
                                   'Typically every 8 hours, capped near 2% per 8 hours; $100 moves on '
                                   '$10,000 at 1%',
                                   'Model funding as a running carry cost that replaces convergence risk '
                                   'on perpetual positions',
                                   'CFTC ([ZEPjpgVSavY @ 00:08:07])'],
                                  ['DCO payment window',
                                   'Individual segregation creates many early-morning DCO calls that must '
                                   'be met within 60 minutes',
                                   'Pre-arrange liquidity and settlement bank credit before opting into '
                                   'individual segregation',
                                   'CFTC ([yUqRhv7w9Vs @ 02:22:09])'],
                                  ['GCP top-up notice timing',
                                   'FCM notified about 45 minutes to an hour before 7:30 central to top up',
                                   'Build morning cash workflows around the notice window to fund the DCO '
                                   'settlement account',
                                   'CFTC ([yUqRhv7w9Vs @ 02:09:56])'],
                                  ['Automated trader registration test',
                                   'Average 20,000 contracts per day over six months; about 120 AT persons '
                                   'estimated',
                                   'Track rolling six-month volume across all DCMs, counting own and '
                                   'customer accounts together',
                                   'CFTC ([ec9Mk3slriY @ 00:33:25])'],
                                  ['FCM capital reduction notices',
                                   'Pre-notice for a capital reduction of 30% or more; post-event notice '
                                   'at 20% decline',
                                   'Watch these triggers as early-warning signals on the health of your '
                                   'carrying FCM',
                                   'CFTC ([vqL3OS8Ot9o @ 01:32:31])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Moves the Practitioners Actually Use',
                           'body': 'Four plays straight from the speakers, from cutting CCO report spend '
                                   'to wiring kill switches outside the agent.',
                           'items': ['Foreign swap dealers in substituted-compliance jurisdictions (Japan, '
                                     'Mexico, the EU, the UK) can submit the unredacted home-regulator CCO '
                                     'report instead of building a Reg 3.3 report; Pete watched a London '
                                     'bank spend six figures a year on New York lawyers for this, and '
                                     "warns that hybrid 'Frankenstein' or redacted reports do not fly: "
                                     "'It's a yes or no.' [A Lawyer In Finance Explains  1.1M views — "
                                     'BO0iMB23sU4 @ 00:00:53]',
                                     "Before trading any perpetual, learn each venue's premium math and "
                                     'observation periods, because funding, not convergence, is where the '
                                     'risk now sits. [CFTC — ZEPjpgVSavY @ 00:09:43]',
                                     'Run the Vanguard due-diligence checklist on every FCM: capital '
                                     'levels, investments limited to top-tier 1.25 securities, audit and '
                                     'seg-compliance history, and custodian rigor. [CFTC — yUqRhv7w9Vs @ '
                                     '02:17:28]',
                                     'Keep risk controls and audit logs outside the agent harness, because '
                                     'agents are better at exploiting vulnerabilities than patching them; '
                                     'back it with hard limits and a kill switch. [CFTC — Ckw1w5mSMIQ @ '
                                     '01:04:27]']},
               'sop_steps': [{'step': 1,
                              'title': 'Verify the Registration Chain',
                              'action': 'Look up the broker and its carrying FCM before funding anything.',
                              'detail': 'Check NFA BASIC by name or ID, then the CFTC enforcement database '
                                        'and disqualification records, then NFA monthly RFED financials; '
                                        'if either registration is missing, walk away. [Brokerchampion — '
                                        'CIinXD9tbVo @ 00:05:37]'},
                             {'step': 2,
                              'title': 'Diligence the FCM Holding Your Margin',
                              'action': 'Score capital, investments, audit history and custodian quality, '
                                        'and keep a second FCM ready.',
                              'detail': 'Use the Vanguard checklist on capital, 1.25 investments, '
                                        'seg-compliance history and custodian rigor; Tim Doris of CME '
                                        'calls multiple FCM relationships best practice. [CFTC — '
                                        'yUqRhv7w9Vs @ 02:17:28]'},
                             {'step': 3,
                              'title': 'Model Funding and Liquidation Before Entry',
                              'action': 'Price funding carry and liquidation mechanics on any perpetual '
                                        'position.',
                              'detail': 'Funding is paid typically every 8 hours, capped near 2%; at a 1% '
                                        'rate a $10,000 notional long pays $100 to the short, and onshore '
                                        'liquidation cancels open orders then sends a market order. [CFTC '
                                        '— ZEPjpgVSavY @ 00:08:40]'},
                             {'step': 4,
                              'title': 'Tag and Fence Every Trading Agent',
                              'action': 'Give each agent an ID, an accountable owner, limits and a tested '
                                        'off switch.',
                              'detail': 'Give each agent and strategy its own ID and a named human owner, '
                                        'set hard limits, log every mandate, and test the kill switch. [AI '
                                        'in Regulated Industries — bsDlbXqvPok @ 00:03:00]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The customer-collateral fight splits cleanly between clearing '
                              'infrastructure and the buy side. Tim Dor of CME attacked the bankruptcy '
                              'legal basis for extending legal segregation with operational commingling '
                              '(LSOC) to futures. Dor argued that 24x6 trading, post-execution give-ups '
                              "and accounts that come and go make end-of-day portfolio reports 'dubious', "
                              "and urged regulators not to 'rush to judgment' [yUqRhv7w9Vs @ 00:04:00]. "
                              "Bill Thumb of Vanguard/ICI countered that clients are 'astonished' to learn "
                              'they carry fellow-customer risk they cannot diligence. Thumb sold '
                              'portability as the real prize, with FCMs sharing records with DCOs daily '
                              'under 22.11(c) and DCOs verifying them under 22.11(e) [yUqRhv7w9Vs @ '
                              '00:09:09]. Ron Filler put the cost on the table: DCOs had floated 50 to 70 '
                              'percent margin increases, and guarantee funds near $3B today could balloon '
                              'to $25B-$50B or more under LSOC [yUqRhv7w9Vs @ 00:20:27]. Dan McGuire of '
                              'LCH.Clearnet flatly disputed that math. LCH has run LSOC in Europe since '
                              "December 2009, protects value net of haircuts, and McGuire said 'We do not "
                              "expect to increase margins' [yUqRhv7w9Vs @ 01:49:38]. The Kalpers camp said "
                              "the buy side will happily pay extra margin for 'return of capital not "
                              "return on capital'. State Street's Steven Winter insisted LSOC would not "
                              'have stopped MF Global and pushed a custody solution instead.',
                              'Public disclosure of FCM health is the second open split. Bill Thum of '
                              'Vanguard, speaking for $2T under management and 9M shareholders, demanded '
                              'public daily segregation reports, daily or average residual interest, '
                              'monthly unaudited financials and leverage, and reportable events '
                              '[vqL3OS8Ot9o @ 01:44:08]. Alessandro Cocco of JPM pushed back that '
                              'proprietary margin and customer counts should be handed over on request, '
                              'not published to the world [vqL3OS8Ot9o @ 01:49:28]. Tom of NFA split the '
                              'difference with three buckets: public for all FCMs, mandatory on customer '
                              "request, and regulators-only so a 'Lifeline' can be extended before "
                              'disruptive information hits the market. Tom also flagged that leverage '
                              "figures come out 'vastly different' depending on whether seg funds are "
                              'counted [vqL3OS8Ot9o @ 02:14:27]. The early-warning camp described quietly '
                              'converting a weak firm into an introducing firm or transferring accounts '
                              "out, and warned that public leaks kill that window because 'the rumor "
                              "becomes reality' [vqL3OS8Ot9o @ 02:44:12]. Grace warned intrusive "
                              'disclosure could push broker-dealers and FCMs back into separate entities. '
                              'A panelist named Bill urged a holistic view that errs toward not '
                              "disclosing, calling MF Global and Peregrine 'two bad apples'. Grain hedger "
                              'Todd went the other way, saying post-MF Global diligence and the ability to '
                              'switch FCMs justify more public disclosure.',
                              'Automated and agentic trading draws the sharpest regulatory split. On '
                              'Regulation AT, Commissioner Giancarlo called special-call access to source '
                              "code an 'end run' around subpoenas and 'a reckless step onto a slippery "
                              "slope', citing the OPM breach of 21.5M records [ec9Mk3slriY @ 00:54:13]. "
                              'The Chairman shot back that enforcement had obtained code many times '
                              "without a breach, that 'this is not a slippery slope this is an uphill "
                              "climb', and the vote went 2-1. At the Frontier Forum, Andrew Ciraa backed "
                              'an internet-style liability shield for agent providers absent fraud or '
                              'misconduct. Another panelist argued the Section 230 logic of encouraging '
                              "adoption 'does not necessarily pertain' because superintelligence is "
                              'already spreading fast [Ckw1w5mSMIQ @ 02:25:58]. A show of hands on who '
                              'breaks the CEA when an agent independently places and cancels large orders '
                              'split badly. Brendan said the customer, Nick said the model developer, Brad '
                              'said customer and FCM, and nobody blamed the agent provider [Ckw1w5mSMIQ @ '
                              '02:39:21]. The AI in Regulated Industries narrator rejected developer '
                              'registration entirely: register the principal and tag every order with an '
                              'agent ID, as MiFID II already does with per-strategy algorithm codes. The '
                              'same narrator conceded that an ID shows who an agent works for, not what it '
                              'will do [bsDlbXqvPok @ 00:02:19].'],
               'table': {'caption': 'Side-by-side playbooks where CFTC-market practitioners openly split',
                         'headers': ['Contested Question',
                                     'Camp A Playbook',
                                     'Camp B Playbook',
                                     'Expert Source'],
                         'rows': [['Should LSOC segregation extend from cleared swaps to futures accounts',
                                   "CME's Tim Dor questions the bankruptcy basis and calls end-of-day "
                                   'portfolio reports dubious',
                                   "Vanguard/ICI's Bill Thumb says clients are astonished by "
                                   'fellow-customer risk and want portability',
                                   'CFTC ([yUqRhv7w9Vs @ 00:04:00]); CFTC ([yUqRhv7w9Vs @ 00:09:09])'],
                                  ['What LSOC really costs in margin and guarantee fund size',
                                   'Ron Filler cites floated 50 to 70 percent margin hikes and $3B funds '
                                   'growing to $25B-$50B',
                                   "LCH's Dan McGuire says LSOC has run since December 2009 and LCH does "
                                   'not expect margin increases',
                                   'CFTC ([yUqRhv7w9Vs @ 00:20:27]); CFTC ([yUqRhv7w9Vs @ 01:49:38])'],
                                  ['Individual GCP custody accounts versus staying inside the LSOC pool',
                                   'Mark of SIBA says the voluntary GCP model harms none and custody cost '
                                   'is a red herring at a couple thousand dollars',
                                   'Ron Filler says the GCP model kills portfolio, cross and '
                                   'single-currency margining and fellow-customer risk persists',
                                   'CFTC ([yUqRhv7w9Vs @ 02:37:04]); CFTC ([yUqRhv7w9Vs @ 02:01:15])'],
                                  ['How much FCM financial data should be made public',
                                   'Vanguard wants public daily seg reports, residual interest, monthly '
                                   'unaudited financials and leverage',
                                   "JPM's Alessandro Cocco wants proprietary margin and customer counts "
                                   'disclosed only on customer request',
                                   'CFTC ([vqL3OS8Ot9o @ 01:44:08]); CFTC ([vqL3OS8Ot9o @ 01:49:28])'],
                                  ['Whether unfixed-price merchandising positions count as genuine bona '
                                   'fide hedges',
                                   'Joe Nicosia of Louis Dreyfus says storage carry and spread changes '
                                   'justify the hedge, and ICE grants such exemptions routinely',
                                   'John Parsons of MIT cites Metallgesellschaft and says you are not '
                                   'reducing your total risk exposure',
                                   'CFTC ([jx5ZryxlRsI @ 00:44:39]); CFTC ([jx5ZryxlRsI @ 01:49:02])'],
                                  ['Regulator access to proprietary algorithmic trading source code under '
                                   'Regulation AT',
                                   'The Chairman says code review is not a taking and staff face criminal '
                                   'penalties for misuse',
                                   'Commissioner Giancarlo calls the special call an end run around '
                                   'subpoenas and predicts litigation',
                                   'CFTC ([ec9Mk3slriY @ 01:05:12]); CFTC ([ec9Mk3slriY @ 00:47:31])'],
                                  ['Who must register when AI agents trade CFTC-regulated markets',
                                   'The narrator says register the principal and tag every order with an '
                                   'agent ID instead',
                                   'A Frontier Forum panelist says sellers or operators of agentic '
                                   'software may need CPO, IB or CTA registration',
                                   'AI in Regulated Industries ([bsDlbXqvPok @ 00:02:19]); CFTC '
                                   '([Ckw1w5mSMIQ @ 02:32:24])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The customer-fund failures that rewrote the rulebook all hit people who '
                              'trusted the wrong layer. Brokerchampion warns that the broker brand on the '
                              'screen may not be the entity actually holding the money. The channel adds '
                              "that MF Global's 2011 collapse is why customer funds are now reported "
                              'daily, with shortfalls triggering immediate action, and that the CFTC does '
                              'not reimburse trading losses [CIinXD9tbVo @ 00:04:04]. Gary DeWaal of '
                              'Newedge recalled Volume Investors failing in 1985, when three traders '
                              'acting in concert dragged the whole firm down through fellow-customer risk. '
                              'DeWaal later flagged that about 10 firms hold 80 percent of customer funds, '
                              "calling it 'an incredible concentration' [yUqRhv7w9Vs @ 00:12:45]. One "
                              "roundtable panelist put the run in hard numbers: '75% of client funds left "
                              "5 days prior to its default' [yUqRhv7w9Vs @ 01:50:04]. Michael at the "
                              'customer-protection roundtable tallied MF Global and Peregrine at about '
                              '$1.8 billion in lost customer funds. Michael argued that the collapse in '
                              'confidence cost far more, and warned that letting an FCM put its hands on '
                              "seg money is 'an open invitation to theft' [vqL3OS8Ot9o @ 02:45:29]. Before "
                              'MF Global, small investors assumed an FCM segregated account was safer than '
                              'a savings account, and that assumption is exactly what burned them when the '
                              'firm went down.',
                              'Mechanical traps punish operators who never ran the numbers. Liam Smith of '
                              'Optiver, speaking for PTG, described perpetual funding as a payment between '
                              'participants, typically every 8 hours, capped around 2 percent per 8 hours '
                              'or up to 6 percent per 24 hours. On a $10,000 long at a 1 percent rate, '
                              "$100 moves to the short. Smith told traders to learn each venue's premium "
                              'math and observation periods [ZEPjpgVSavY @ 00:09:43]. Onshore liquidation '
                              'at maintenance margin cancels open orders and fires a market order rather '
                              'than using last price, with residual losses falling to the guarantee fund '
                              'or default waterfall. Offshore venues lean on auto-deleveraging and higher '
                              'leverage instead [ZEPjpgVSavY @ 00:10:41]. Brokerchampion notes that '
                              'offshore brokers commonly advertise 500:1 leverage against the US cap of '
                              '50:1 on seven majors and 20:1 elsewhere, and that Pepperstone, IC Markets '
                              'and TickMill do not serve the US at all [dvFmfWlkYq0 @ 00:04:35]. In '
                              'clearing plumbing, Scott Paris of BMO Harris said individually segregated '
                              'calls must be met within 60 minutes with no flexibility. Joe of the Kansas '
                              'City Board of Trade priced the drag: 250 days of variation margin at $4 per '
                              'wire comes to about $1,000 of DCO expense against a $4 fee [yUqRhv7w9Vs @ '
                              '02:47:09].',
                              'Paperwork and automation failures are the quiet killers. Pete, a finance '
                              'lawyer with 22 years at the CFTC reviewing chief compliance officer '
                              "reports, watched a London bank's chief legal officer spend what Pete "
                              "estimates at 'six figures every year' on New York lawyers. The foreign swap "
                              'dealer could have filed its unredacted home-regulator report for free '
                              "[BO0iMB23sU4 @ 00:01:36]. The trap is getting cute. Hybrid 'Frankenstein' "
                              'reports and filings redacted down to swaps or futures sections get rejected '
                              'because the CFTC cannot verify what was omitted. The commonly dropped '
                              '3.3(e) items are exactly what the operating divisions and enforcement '
                              "review, and Pete's verdict is 'It's a yes or no' [BO0iMB23sU4 @ 00:07:27]. "
                              'On agents, Ronet Jane of Liquid Compute warned that correlated agents can '
                              'trigger mass liquidity withdrawal and that a single model-provider outage '
                              'can leave stale quotes. Jane said each agent needs its own limits plus '
                              "collective limits across a customer's agents [Ckw1w5mSMIQ @ 00:53:11]. Kush "
                              'Bavaria of ORN ranked prompt injection as the top risk and demanded hard '
                              'limits and kill switches. Brendan Ryan warned that agents exploit '
                              'vulnerabilities better than they patch them. Brett Harrison pointed to the '
                              "roughly 50x Signal OTC spike as the risk 'times a thousand' [Ckw1w5mSMIQ @ "
                              '02:13:11].'],
               'table': {'caption': 'Firsthand traps and the economics checks practitioners attach to them',
                         'headers': ['Trap', 'What Practitioners Saw', 'Economics Check', 'Expert Source'],
                         'rows': [['Trusting the broker brand shown on your screen',
                                   'The brand may not be the entity holding funds, and the CFTC does not '
                                   'reimburse trading losses',
                                   'Run NFA BASIC, the CFTC enforcement database, then monthly RFED '
                                   'financials before funding anything',
                                   'Brokerchampion ([CIinXD9tbVo @ 00:01:06]); Brokerchampion '
                                   '([CIinXD9tbVo @ 00:05:37])'],
                                  ['Ignoring perpetual futures funding bleed on leveraged positions',
                                   'Funding hits typically every 8 hours, capped near 2 percent, up to 6 '
                                   'percent daily',
                                   'A $10,000 long at a 1 percent rate pays $100 to the short each funding '
                                   'period',
                                   'CFTC ([ZEPjpgVSavY @ 00:08:07]); CFTC ([ZEPjpgVSavY @ 00:09:29])'],
                                  ['Fellow-customer blowups inside commingled omnibus customer pools',
                                   'Volume Investors failed in 1985 when three traders acting in concert '
                                   'sank the firm',
                                   'About 10 firms hold 80 percent of customer funds, which DeWaal called '
                                   'an incredible concentration',
                                   'CFTC ([yUqRhv7w9Vs @ 00:12:45]); CFTC ([yUqRhv7w9Vs @ 00:52:22])'],
                                  ['Window-dressed FCM leverage figures reported only at month end',
                                   'James asked regulators to disclose average and peak leverage within '
                                   'each month',
                                   'Demand monthly average plus peak leverage to curtail the window '
                                   'dressing practice James described',
                                   'CFTC ([vqL3OS8Ot9o @ 02:01:41])'],
                                  ['Filing hybrid Frankenstein or redacted CCO annual reports to the CFTC',
                                   'Hybrid and redacted reports are rejected because the CFTC cannot '
                                   'verify what was omitted',
                                   'The unredacted home-regulator report is free versus six figures every '
                                   'year on outside lawyers',
                                   'A Lawyer In Finance Explains  1.1M views ([BO0iMB23sU4 @ 00:04:59]); A '
                                   'Lawyer In Finance Explains  1.1M views ([BO0iMB23sU4 @ 00:01:36])'],
                                  ['Position limits set too low for energy merchants and hedgers',
                                   'Table 11 shows 7 to 11 firms would have exceeded the RBOB and heating '
                                   'oil limits',
                                   "Energy's 3-day spot period makes assuming positions before exemption "
                                   'approval a real risk',
                                   'CFTC ([jx5ZryxlRsI @ 00:13:23]); CFTC ([jx5ZryxlRsI @ 02:12:33])'],
                                  ['Correlated, stale or hijacked AI trading agents hitting live markets',
                                   'A model-provider outage can trigger liquidity withdrawal or stale '
                                   'quotes, and prompt injection ranks as top risk',
                                   'Set per-agent limits, collective customer limits, hard limits and a '
                                   'tested kill switch',
                                   'CFTC ([Ckw1w5mSMIQ @ 00:53:11]); CFTC ([Ckw1w5mSMIQ @ 02:13:11])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Operator Gate: Clear These Before Capital Moves',
                           'body': 'Each gate is drawn from a loss, rejection or blowup the practitioners '
                                   'described directly. Fail any one and stop.',
                           'items': ['Confirm both CFTC registration and NFA membership through NFA BASIC '
                                     'before wiring a dollar; if either registration is missing, walk away '
                                     '[Brokerchampion — CIinXD9tbVo @ 00:06:10].',
                                     "Model perpetual funding with the venue's actual premium math and "
                                     'observation periods, not a headline rate, before sizing any '
                                     'leveraged position [CFTC — ZEPjpgVSavY @ 00:09:43].',
                                     'File either the unredacted home-regulator CCO report or a full Reg '
                                     "3.3 report, never a hybrid, because 'You can't do anything in the "
                                     "middle' [A Lawyer In Finance Explains  1.1M views — BO0iMB23sU4 @ "
                                     '00:04:39].',
                                     'Run agent risk controls and audit logs outside the agent harness, '
                                     'with hard limits and a kill switch that actually turns the agents '
                                     'off [CFTC — Ckw1w5mSMIQ @ 01:04:27].']}}],
 'pull_quote': '"Europe\'s model works because a regulated firm sits in the middle of every trade. Your '
               'fridge doesn\'t have a compliance officer." — AI in Regulated Industries (bsDlbXqvPok @ '
               '00:02:39).',
 'diagram_id': 'diag-08',
 'action_checklist': ['Run every broker through NFA BASIC by name or ID, then the CFTC enforcement '
                      "database including the firm's principals, then its monthly financial filings "
                      '[Brokerchampion — dvFmfWlkYq0 @ 00:07:10].',
                      'Diligence each FCM on capital levels, investments limited to top-tier 1.25 '
                      'securities, audit and seg-compliance history, and custodian rigor [CFTC — '
                      'yUqRhv7w9Vs @ 02:17:28].',
                      'Keep multiple FCM relationships as best practice so positions can move if one '
                      'clearing firm fails [CFTC — yUqRhv7w9Vs @ 02:47:49].',
                      'Price perpetual exposure with the worked funding example: index $100,000, perp '
                      '$101,000, $10,000 long at 1 percent moves $100 to the short [CFTC — ZEPjpgVSavY @ '
                      '00:08:40].',
                      'Give each agent and strategy its own ID and named human owner, set hard limits, log '
                      'every mandate, and test the kill switch [AI in Regulated Industries — bsDlbXqvPok @ '
                      '00:03:00].',
                      'As a foreign swap dealer in a substituted-compliance jurisdiction, submit the '
                      'unredacted home-regulator CCO report translated into English instead of paying for '
                      'a Reg 3.3 rewrite [A Lawyer In Finance Explains  1.1M views — BO0iMB23sU4 @ '
                      '00:03:38].'],
 'statutory_citations': [{'title': 'CFTC — Day 1: Roundtable to Discuss Additional Customer Collateral '
                                   'Protections [00:02:53]',
                          'url': 'https://www.youtube.com/watch?v=yUqRhv7w9Vs&t=173s',
                          'relevance': 'Primary practitioner testimony on LSOC, fellow-customer risk, GCP '
                                       'custody models and the cost of extending segregation to futures.'},
                         {'title': 'CFTC — CFTC Roundtable on Enhancing Protections Afforded Customers and '
                                   'Funds Deposited by Customers: Part 1 [01:44:08]',
                          'url': 'https://www.youtube.com/watch?v=vqL3OS8Ot9o&t=6248s',
                          'relevance': 'Primary practitioner testimony on FCM public disclosure, residual '
                                       'interest, leverage window dressing and NFA BASIC.'},
                         {'title': 'CFTC — Open Commission Meeting to Consider a Supplemental Proposal to '
                                   'Automated Trading Regulation [00:33:25]',
                          'url': 'https://www.youtube.com/watch?v=ec9Mk3slriY&t=2005s',
                          'relevance': 'Primary practitioner testimony on automated-trading registration '
                                       'thresholds, risk controls and source-code access.'},
                         {'title': 'CFTC — CFTC’s Innovation Task Force to Host the Inaugural Frontier '
                                   'Forum on Super Intelligence [00:07:26]',
                          'url': 'https://www.youtube.com/watch?v=Ckw1w5mSMIQ&t=446s',
                          'relevance': 'Primary practitioner testimony on know-your-agent, AI agent '
                                       'liability, kill switches and operator IDs.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'ZEPjpgVSavY',
                       'title': 'Presentation on Perpetual Futures’ Funding Rate Mechanism, July 29 AAC '
                                'Meeting',
                       'channel': 'CFTC',
                       'author': 'CFTC',
                       'text': "It's a derivative contract with no expiration.",
                       'tip': "It's a derivative contract with no expiration.",
                       'timestamp': 160,
                       'timestamp_seconds': 160,
                       'timestamp_label': '[00:02:40]',
                       'url': 'https://www.youtube.com/watch?v=ZEPjpgVSavY&t=160s',
                       'markdown': '[00:02:40](https://www.youtube.com/watch?v=ZEPjpgVSavY&t=160s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CIinXD9tbVo',
                       'title': 'The CFTC Explained 2026: Who Polices US Futures, Swaps and Retail Forex',
                       'channel': 'Brokerchampion',
                       'author': 'Brokerchampion',
                       'text': 'The RFED must hold at least $20 million in capital.',
                       'tip': 'The RFED must hold at least $20 million in capital.',
                       'timestamp': 166,
                       'timestamp_seconds': 166,
                       'timestamp_label': '[00:02:46]',
                       'url': 'https://www.youtube.com/watch?v=CIinXD9tbVo&t=166s',
                       'markdown': '[00:02:46](https://www.youtube.com/watch?v=CIinXD9tbVo&t=166s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CIinXD9tbVo',
                       'title': 'The CFTC Explained 2026: Who Polices US Futures, Swaps and Retail Forex',
                       'channel': 'Brokerchampion',
                       'author': 'Brokerchampion',
                       'text': 'If either registration is missing, walk away.',
                       'tip': 'If either registration is missing, walk away.',
                       'timestamp': 370,
                       'timestamp_seconds': 370,
                       'timestamp_label': '[00:06:10]',
                       'url': 'https://www.youtube.com/watch?v=CIinXD9tbVo&t=370s',
                       'markdown': '[00:06:10](https://www.youtube.com/watch?v=CIinXD9tbVo&t=370s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'l76_21x9yFQ',
                       'title': 'Understanding the Commodity Futures Trading Commission (CFTC) - A Quick '
                                'Guide',
                       'channel': 'The Brief',
                       'author': 'The Brief',
                       'text': "The CFTC's mission is to protect against fraud, manipulation and abusive "
                               'practices.',
                       'tip': "The CFTC's mission is to protect against fraud, manipulation and abusive "
                              'practices.',
                       'timestamp': 33,
                       'timestamp_seconds': 33,
                       'timestamp_label': '[00:00:33]',
                       'url': 'https://www.youtube.com/watch?v=l76_21x9yFQ&t=33s',
                       'markdown': '[00:00:33](https://www.youtube.com/watch?v=l76_21x9yFQ&t=33s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Osx2O3SjlCA',
                       'title': 'What Is an Introducing Broker?',
                       'channel': 'Simple Explain',
                       'author': 'Simple Explain',
                       'text': 'Futures introducing brokers are registered with the Commodity Futures '
                               'Trading Commission CFTC and regulated by the National Futures Association '
                               'NFA.',
                       'tip': 'Futures introducing brokers are registered with the Commodity Futures '
                              'Trading Commission CFTC and regulated by the National Futures Association '
                              'NFA.',
                       'timestamp': 72,
                       'timestamp_seconds': 72,
                       'timestamp_label': '[00:01:12]',
                       'url': 'https://www.youtube.com/watch?v=Osx2O3SjlCA&t=72s',
                       'markdown': '[00:01:12](https://www.youtube.com/watch?v=Osx2O3SjlCA&t=72s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'BO0iMB23sU4',
                       'title': 'CFTC SWAP DEALER CCO ANNUAL REPORT for Foreign Swap Dealers',
                       'channel': 'A Lawyer In Finance Explains  1.1M views',
                       'author': 'A Lawyer In Finance Explains  1.1M views',
                       'text': "You can't do anything in the middle.",
                       'tip': "You can't do anything in the middle.",
                       'timestamp': 279,
                       'timestamp_seconds': 279,
                       'timestamp_label': '[00:04:39]',
                       'url': 'https://www.youtube.com/watch?v=BO0iMB23sU4&t=279s',
                       'markdown': '[00:04:39](https://www.youtube.com/watch?v=BO0iMB23sU4&t=279s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jx5ZryxlRsI',
                       'title': 'Part I: CFTC Staff Roundtable on Position Limits for Physical Commodity '
                                'Derivatives, 06/19/14',
                       'channel': 'CFTC',
                       'author': 'CFTC',
                       'text': 'Complexity demands flexibility because these markets are complex.',
                       'tip': 'Complexity demands flexibility because these markets are complex.',
                       'timestamp': 4144,
                       'timestamp_seconds': 4144,
                       'timestamp_label': '[01:09:04]',
                       'url': 'https://www.youtube.com/watch?v=jx5ZryxlRsI&t=4144s',
                       'markdown': '[01:09:04](https://www.youtube.com/watch?v=jx5ZryxlRsI&t=4144s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jx5ZryxlRsI',
                       'title': 'Part I: CFTC Staff Roundtable on Position Limits for Physical Commodity '
                                'Derivatives, 06/19/14',
                       'channel': 'CFTC',
                       'author': 'CFTC',
                       'text': 'You are not reducing your total risk exposure.',
                       'tip': 'You are not reducing your total risk exposure.',
                       'timestamp': 6542,
                       'timestamp_seconds': 6542,
                       'timestamp_label': '[01:49:02]',
                       'url': 'https://www.youtube.com/watch?v=jx5ZryxlRsI&t=6542s',
                       'markdown': '[01:49:02](https://www.youtube.com/watch?v=jx5ZryxlRsI&t=6542s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ec9Mk3slriY',
                       'title': 'Open Commission Meeting to Consider a Supplemental Proposal to Automated '
                                'Trading Regulation',
                       'channel': 'CFTC',
                       'author': 'CFTC',
                       'text': 'Automated trading now dominates the markets we oversee, more than seventy '
                               'percent of trading in futures is now automated.',
                       'tip': 'Automated trading now dominates the markets we oversee, more than seventy '
                              'percent of trading in futures is now automated.',
                       'timestamp': 38,
                       'timestamp_seconds': 38,
                       'timestamp_label': '[00:00:38]',
                       'url': 'https://www.youtube.com/watch?v=ec9Mk3slriY&t=38s',
                       'markdown': '[00:00:38](https://www.youtube.com/watch?v=ec9Mk3slriY&t=38s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yUqRhv7w9Vs',
                       'title': 'Day 1: Roundtable to Discuss Additional Customer Collateral Protections',
                       'channel': 'CFTC',
                       'author': 'CFTC',
                       'text': 'As a DCO, we cannot wait five business days to see whether or not that '
                               'call is met or not.',
                       'tip': 'As a DCO, we cannot wait five business days to see whether or not that call '
                              'is met or not.',
                       'timestamp': 1443,
                       'timestamp_seconds': 1443,
                       'timestamp_label': '[00:24:03]',
                       'url': 'https://www.youtube.com/watch?v=yUqRhv7w9Vs&t=1443s',
                       'markdown': '[00:24:03](https://www.youtube.com/watch?v=yUqRhv7w9Vs&t=1443s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yUqRhv7w9Vs',
                       'title': 'Day 1: Roundtable to Discuss Additional Customer Collateral Protections',
                       'channel': 'CFTC',
                       'author': 'CFTC',
                       'text': '75% of client funds left 5 days prior to its default.',
                       'tip': '75% of client funds left 5 days prior to its default.',
                       'timestamp': 6604,
                       'timestamp_seconds': 6604,
                       'timestamp_label': '[01:50:04]',
                       'url': 'https://www.youtube.com/watch?v=yUqRhv7w9Vs&t=6604s',
                       'markdown': '[01:50:04](https://www.youtube.com/watch?v=yUqRhv7w9Vs&t=6604s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'vqL3OS8Ot9o',
                       'title': 'CFTC Roundtable on Enhancing Protections Afforded Customers and Funds '
                                'Deposited by Customers: Part 1',
                       'channel': 'CFTC',
                       'author': 'CFTC',
                       'text': 'Liquidity is the lifeline of broker dealers and FCMs.',
                       'tip': 'Liquidity is the lifeline of broker dealers and FCMs.',
                       'timestamp': 6777,
                       'timestamp_seconds': 6777,
                       'timestamp_label': '[01:52:57]',
                       'url': 'https://www.youtube.com/watch?v=vqL3OS8Ot9o&t=6777s',
                       'markdown': '[01:52:57](https://www.youtube.com/watch?v=vqL3OS8Ot9o&t=6777s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kkkaudUCNSQ',
                       'title': 'CFTC to Hold an Open Commission Meeting on March 25',
                       'channel': 'CFTC',
                       'author': 'CFTC',
                       'text': 'Under no circumstances can an unlimited quantity of swaps be a de minimis '
                               'quantity.',
                       'tip': 'Under no circumstances can an unlimited quantity of swaps be a de minimis '
                              'quantity.',
                       'timestamp': 5152,
                       'timestamp_seconds': 5152,
                       'timestamp_label': '[01:25:52]',
                       'url': 'https://www.youtube.com/watch?v=kkkaudUCNSQ&t=5152s',
                       'markdown': '[01:25:52](https://www.youtube.com/watch?v=kkkaudUCNSQ&t=5152s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dvFmfWlkYq0',
                       'title': 'What Is the CFTC? The US Regulator Behind Futures, Swaps and Retail Forex '
                                '(2026)',
                       'channel': 'Brokerchampion',
                       'author': 'Brokerchampion',
                       'text': 'Offshore brokers commonly advertise 500 to1 leverage.',
                       'tip': 'Offshore brokers commonly advertise 500 to1 leverage.',
                       'timestamp': 275,
                       'timestamp_seconds': 275,
                       'timestamp_label': '[00:04:35]',
                       'url': 'https://www.youtube.com/watch?v=dvFmfWlkYq0&t=275s',
                       'markdown': '[00:04:35](https://www.youtube.com/watch?v=dvFmfWlkYq0&t=275s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fGEHMyG3ktY',
                       'title': 'What is the CFTC and What Does it Do?',
                       'channel': 'Earn2Trade',
                       'author': 'Earn2Trade',
                       'text': "If you don't listen to the CFTC, that is the first and foremost way that "
                               'they get you.',
                       'tip': "If you don't listen to the CFTC, that is the first and foremost way that "
                              'they get you.',
                       'timestamp': 941,
                       'timestamp_seconds': 941,
                       'timestamp_label': '[00:15:41]',
                       'url': 'https://www.youtube.com/watch?v=fGEHMyG3ktY&t=941s',
                       'markdown': '[00:15:41](https://www.youtube.com/watch?v=fGEHMyG3ktY&t=941s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ckw1w5mSMIQ',
                       'title': 'CFTC’s Innovation Task Force to Host the Inaugural Frontier Forum on '
                                'Super Intelligence',
                       'channel': 'CFTC',
                       'author': 'CFTC',
                       'text': 'There should be a fundamental way to turn off the agents if things go '
                               'wrong.',
                       'tip': 'There should be a fundamental way to turn off the agents if things go '
                              'wrong.',
                       'timestamp': 8031,
                       'timestamp_seconds': 8031,
                       'timestamp_label': '[02:13:51]',
                       'url': 'https://www.youtube.com/watch?v=Ckw1w5mSMIQ&t=8031s',
                       'markdown': '[02:13:51](https://www.youtube.com/watch?v=Ckw1w5mSMIQ&t=8031s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bsDlbXqvPok',
                       'title': "AI Trading Agents: The CFTC's Know Your Agent Question",
                       'channel': 'AI in Regulated Industries',
                       'author': 'AI in Regulated Industries',
                       'text': "That's know your agent in everything but name.",
                       'tip': "That's know your agent in everything but name.",
                       'timestamp': 120,
                       'timestamp_seconds': 120,
                       'timestamp_label': '[00:02:00]',
                       'url': 'https://www.youtube.com/watch?v=bsDlbXqvPok&t=120s',
                       'markdown': '[00:02:00](https://www.youtube.com/watch?v=bsDlbXqvPok&t=120s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'}]}
