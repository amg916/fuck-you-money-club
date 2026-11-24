from __future__ import annotations

CHAPTER_6 = {'id': 'Q6',
 'chapter_id': 'Q6',
 'chapter_number': 6,
 'question_number': 6,
 'slug': 'smartlead-ai-cold-email-campaigns',
 'question_prompt': 'How do practitioners launch and operate cold email campaigns, choose sending '
                    'software, and automate copy and reply handling?',
 'kicker': 'Q6 / THE BIG MONEY PLAYBOOKS',
 'title': 'Run Cold Email Campaigns with Smartlead and AI',
 'subtitle': 'Smartlead setup and full-platform tutorials, campaign scaling, AI copywriting, Claude Code '
             'experiments, n8n reply automation, agency startup, and Instantly and EmailBison comparisons',
 'layout_template': 'step_by_step_blueprint',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners running Smartlead at 20,000 to 1M+ emails a month converge on the '
                      'same skeleton: secondary lookalike domains, two to five inboxes per domain, 10 to '
                      '25 sends per inbox per day, constant warm-up, verified-only lists, plain-text copy '
                      "with tracking off, and short two-to-three-touch sequences. Smartlead's own agency "
                      'operators run lead math backward from volume, where 100K emails means roughly 35K '
                      'leads and 200 inboxes on a one-month plan, while Matt Lucero pins benchmarks at '
                      'about 1% reply and under 3% bounce, with auto-pause at 5%. Costs stay lean: the $94 '
                      'Pro plan, $4.5 fresh mailboxes, $39 Smart Servers. The fights are over '
                      'burn-and-replace versus protect-the-domain, one follow-up versus three, AI copy '
                      'versus hand-written copy, and whether agencies should graduate to Email Bison or '
                      'Plus Vibe.',
 'key_metrics': [{'label': 'Per-inbox daily send cap',
                  'metric': 'Per-inbox daily send cap',
                  'value': '25 messages per inbox per day, 2 inboxes per domain, 50 sends per domain per '
                           'day',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Capacity rule for a 100,000-email build, excluding warm-up; sending more per '
                             'inbox gets domains flagged.',
                  'source': 'Smartlead ([C2lkX09G4h4 @ 00:02:20])'},
                 {'label': 'Campaign health benchmarks',
                  'metric': 'Campaign health benchmarks',
                  'value': 'About 1% reply rate and under 3% bounce rate',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Troubleshooting benchmarks from an agency operator who reports sending more '
                             'than 10 million emails.',
                  'source': 'Matt Lucero ([_iGjRSCPXuA @ 02:10:45])'},
                 {'label': 'Claude Code 30-day campaign result',
                  'metric': 'Claude Code 30-day campaign result',
                  'value': '~15,000 sent, ~8,000 net-new leads, ~500 replies, ~250 interested, 57 calls',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Day-27 results of a Smartlead campaign driven by Claude Code, with copy '
                             "written manually, on a friend's account running about a year.",
                  'source': 'Smartlead ([NWEL3WNYDhg @ 00:09:43])'},
                 {'label': 'High-volume Smartlead pricing',
                  'metric': 'High-volume Smartlead pricing',
                  'value': '$800 per month for 1M emails, versus $3,000+ before the repricing',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'New volume-based billing with unlimited contacts on the higher plan, as '
                             'reported by a 1M+ emails-per-month agency.',
                  'source': 'Matt Lucero ([_iGjRSCPXuA @ 00:14:19])'}],
 'sections': [{'title': 'Section 1: The Practitioner Consensus',
               'paragraphs': ["Every high-volume sender in this group refuses to mail from the company's "
                              "primary domain. Wesley, running Smartlead's 20,000-email Claude Code "
                              'experiment, buys lookalike secondary domains such as gofish.com and '
                              'hellofish.com and hangs three to five inboxes on each one [NWEL3WNYDhg @ '
                              "00:01:36]. Smartlead's 100,000-email tutorial sends only from secondary "
                              'names like richflowsuccess.com, forwards each sending domain to the main '
                              'website, adds profile pictures, and explains the stakes in one line: cold '
                              "email 'will always get some spam complaints, always' [C2lkX09G4h4 @ "
                              '00:07:20]. Matt Lucero, who runs 4,000 email accounts for an agency, '
                              'repeats the rule without qualification: never send from your main domain '
                              '[J8lvEnIHcLk @ 01:03:01]. The second shared law is distribution. Sergio '
                              'Perea of Boost Hero calls low volume per inbox spread across a high inbox '
                              "count the only safe model and says everything else is 'just burning domain "
                              "slowly' [lvp7ODzi7I8 @ 00:00:32]. In practice that means nobody scales by "
                              'cranking one mailbox from 50 to 100 to 150 sends a day. They scale by '
                              'buying more domains and more inboxes, keeping each one boring and '
                              'low-volume, and letting Smartlead rotate sends across the whole pool. The '
                              'infrastructure is treated as a replaceable layer sitting in front of the '
                              'real brand, never as the brand itself.',
                              'The second consensus block is warm-up plus list hygiene, and both are '
                              'treated as permanent operating costs rather than launch chores. Gabriel '
                              'Martinez of ReachFlow, speaking on the Smartlead channel, says having '
                              "warm-up running constantly 'is not optional' [vQSB7GXedMM @ 00:02:02]. "
                              "Smartlead's 100,000-email build keeps warm-up live on every inbox at all "
                              'times and walks fresh mailboxes from 5 to 20 sends a day in week one to '
                              'full volume around day 30 [C2lkX09G4h4 @ 00:09:16]. Matt Lucero backs the '
                              "habit but kills the fantasy around it: warm-up 'doesn't cure everything' "
                              'and cannot rescue a sender from spam reports [J8lvEnIHcLk @ 00:48:57]. On '
                              "data, the shared rule is verified-only. Smartlead's operator does the math "
                              'out loud: a list that is 95% accurate still throws well over 1,000 bounces '
                              'across 35,000 leads, so every address gets verified, which lands a 0.3% '
                              'bounce rate [C2lkX09G4h4 @ 00:10:20]. Matt likewise sends only to verified '
                              'contacts and turns on the import toggle that ignores leads already sitting '
                              'in other campaigns. In one walkthrough, re-uploading the same CSV stripped '
                              '153 duplicate leads automatically, so overlapping lists never double-tap a '
                              'prospect from two campaigns. Verification happens before import, not after '
                              'the damage.',
                              'On copy, the consensus is short, plain, and stripped of anything a filter '
                              'can grab. Tim of Unlock GTME, teaching on the Smartlead channel, says '
                              'sequences have shrunk from five emails in 2018 and 2019 to two or three, '
                              "insists on three net-new templates rather than 'just checking in,' and "
                              'draws a hard line: never send more than three emails per cold sequence '
                              "[doR2rhof6CM @ 01:29:20]. Michael Saruggia keeps every message 'painfully "
                              "short, under 100 words,' rotates the angle every 30 to 90 days across "
                              'value, lead magnets, CTAs and video, and pastes URLs as plain text in '
                              'parentheses rather than hyperlinks [qWuvWm5Zcz0 @ 00:12:04]. Matt Lucero '
                              "recommends the 'optimize email delivery' setting for 90% of people because "
                              "links, images 'or any weird stuff' make spam placement more likely, and "
                              'pairs it with plain text and no open or click tracking [J8lvEnIHcLk @ '
                              '01:48:04]. Vincent Robin builds the same way from scratch: no bold, no '
                              'italics, no images, no links, then spintax on greetings like hi, hello and '
                              "hey plus 'I saw' versus 'I noticed' so batches never look uniform to the "
                              'provider [7Sq3Ger8D3A @ 00:09:16]. The common thread is that identical, '
                              'decorated, link-heavy email gets flagged, while varied plain text from a '
                              'real-looking sender gets read.'],
               'table': {'caption': 'Consensus rules multiple Smartlead operators run before a single cold '
                                    'email goes out',
                         'headers': ['Consensus Rule',
                                     'What The Operator Actually Does',
                                     'Stated Reason Or Number',
                                     'Expert Source'],
                         'rows': [['Never send from the primary company domain',
                                   'Buy lookalike secondary domains like gofish.com and hellofish.com, '
                                   'three to five inboxes each',
                                   'Keeps cold-email reputation damage off the main brand domain entirely',
                                   'Smartlead ([NWEL3WNYDhg @ 00:01:36])'],
                                  ['Spread low volume across many inboxes',
                                   'Cap each inbox low and add inboxes instead of raising per-inbox sends',
                                   'Everything else is described as burning domains slowly over time',
                                   'Sergio Perea | Boost Hero ([lvp7ODzi7I8 @ 00:00:32])'],
                                  ['Split mailboxes across multiple email providers',
                                   'Run roughly 67 Google, 67 Outlook and the rest SMTP across 200 inboxes',
                                   'Agencies have been seen losing every single inbox overnight on one '
                                   'provider',
                                   'Smartlead ([C2lkX09G4h4 @ 00:08:16])'],
                                  ['Keep warm-up running permanently on every inbox',
                                   'Leave warm-up switched on for every connected inbox on every plan',
                                   'Described flatly as not optional for any serious outbound sender',
                                   'Smartlead ([vQSB7GXedMM @ 00:02:02])'],
                                  ['Send only to verified email addresses',
                                   'Verify every lead before import instead of trusting a 95% accurate '
                                   'list',
                                   'Full verification across 35K leads brought the bounce rate to 0.3%',
                                   'Smartlead ([C2lkX09G4h4 @ 00:10:20])'],
                                  ['Keep sequences at three touches or fewer',
                                   "Write three net-new templates and never send a bare 'just checking in'",
                                   'Sequences shrank from five emails in 2018 to two or three today',
                                   'Smartlead ([doR2rhof6CM @ 01:29:20])'],
                                  ['Send plain text with tracking switched off',
                                   'Enable optimize delivery, force plain text, disable open and click '
                                   'tracking',
                                   'Links, images and weird formatting make landing in spam more likely',
                                   'Smartlead ([J8lvEnIHcLk @ 01:48:04])']]}},
              {'title': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["Execution starts with backward math, not with copy. Smartlead's "
                              '100,000-email operator runs a three-email sequence, one opener plus two '
                              'follow-ups, so 100,000 sends equals about 33,000 people, rounded up to '
                              '35,000 to absorb replies and bounces [C2lkX09G4h4 @ 00:01:00]. Capacity is '
                              'capped at 25 messages per inbox per day excluding warm-up, two inboxes per '
                              'domain, and 20 working days a month with weekends off. Hitting the volume '
                              'in one month needs 5,000 sends a day across 200 inboxes on 100 domains; '
                              'spreading it over three months drops that to roughly 1,700 a day on 67 '
                              'inboxes and 34 domains [C2lkX09G4h4 @ 00:03:17]. The warm-up ramp stretches '
                              'both plans, turning one month into about two and three months into about '
                              'four. Wesley runs tighter: 10 sends per inbox per day out of a stated 10 to '
                              '15 ceiling, so 1,000 a day means 100 inboxes divided by three per domain, '
                              'or 34 domains, and Claude itself recommended buying 34 new inboxes after a '
                              "13-minute sufficiency check [NWEL3WNYDhg @ 00:03:02]. Tim's calculator uses "
                              '15 per mailbox per day, two mailboxes per domain, and 22 sending days a '
                              'month [doR2rhof6CM @ 02:03:33]. Pick the per-inbox number first; everything '
                              'else is division.',
                              'The buy list is specific. Through Smart Senders, fresh mailboxes run $4.5 '
                              'each per month on Google, Outlook or SMTP at a two-to-one mailbox-to-domain '
                              'ratio, so 67 mailboxes cost about $300 a month; the first month lands near '
                              '$700 once roughly $400 of domains are added, then drops back to $300 '
                              '[C2lkX09G4h4 @ 00:04:43]. Pre-warmed is the expensive shortcut at $18 a '
                              'year per domain and $9 a month per inbox, ready in 24 to 48 hours. Matt '
                              'Lucero split-tested pre-warmed against custom-named fresh boxes and says '
                              "'it does not affect performance in our experience at all'; the trade is "
                              'cost and unchosen sender names versus a 14 to 21-plus day wait, with fresh '
                              'domains at $13 a year and up to 20 per order [_iGjRSCPXuA @ 00:32:29]. Matt '
                              'recommends the $94 Pro plan for most operators, roughly 30,000 contacts and '
                              '90,000 emails a month, plus Smart Servers at $39 each sized for 80,000 to '
                              '100,000 emails per server [_iGjRSCPXuA @ 01:18:34]. Tim diversifies harder, '
                              'buying through Prime Forge, Mail Forge or Infraforge instead of GoDaddy and '
                              'splitting mailboxes 40% Google, 30% Microsoft 365 and 30% SMTP [doR2rhof6CM '
                              '@ 02:01:55].',
                              "Matt Lucero's campaign rule is that the most conservative number always "
                              'wins. A 20-minute gap between sends inside a 9am-to-5pm window yields 21 '
                              'slots a day, but a mailbox capped at 15 still sends 15, and an 8-to-10am '
                              'window with the same gap gives only six; max new leads per day should be '
                              'set very high, because 100 means 100 new leads, not 100 sends [_iGjRSCPXuA '
                              '@ 01:44:05]. Vincent Robin sets max new leads to 10,000, turns on '
                              'stop-on-reply, optimize delivery and plain text, kills open and click '
                              'tracking, and sets bounce auto-protection to five, which pauses the '
                              'campaign once bounces exceed 5% [7Sq3Ger8D3A @ 00:13:34]. When interested '
                              'replies land, Matt pushes them into a subsequence: manual reply first, then '
                              "a threaded 'Are you still interested? Let me know either way' after three "
                              'days and a last email two days later, with the subsequence allowed to '
                              'override inbox caps [_iGjRSCPXuA @ 01:54:30]. Hoani Taylor automates triage '
                              'with n8n: a reply webhook fires, GPT-4o mini classifies the reply against '
                              "examples, Smartlead's lead category updates, and a second webhook triggers "
                              'an auto-reply or Slack alert within a minute, sorting 27 categories in '
                              'tiers rather than one pass [7360Lif0HLQ @ 00:03:08].'],
               'table': {'caption': 'Exact numbers, prices and Smartlead settings operators quote for '
                                    'running cold email at volume',
                         'headers': ['Mechanic',
                                     'Exact Number Or Setting',
                                     'Operator Note',
                                     'Expert Source'],
                         'rows': [['Lead math for a 100K-email push',
                                   'Three-touch sequence means about 33,000 people, rounded up to 35,000 '
                                   'leads',
                                   'Extra headroom absorbs replies and bounces before the volume target '
                                   'lands',
                                   'Smartlead ([C2lkX09G4h4 @ 00:01:00])'],
                                  ['Per-inbox daily sending cap',
                                   '25 per inbox, two inboxes per domain, 50 per domain daily',
                                   'Pushing more per inbox gets sending domains flagged by providers',
                                   'Smartlead ([C2lkX09G4h4 @ 00:02:20])'],
                                  ['Fresh versus pre-warmed mailbox cost',
                                   'Fresh $4.5 per mailbox monthly; pre-warmed $9 monthly plus $18 yearly '
                                   'domains',
                                   'Pre-warmed inboxes go live in 24 to 48 hours instead',
                                   'Smartlead ([C2lkX09G4h4 @ 00:09:37])'],
                                  ['Smartlead plan and high-volume pricing',
                                   '$94 Pro plan; 1M emails monthly now costs $800 instead of $3,000-plus',
                                   'Billing now runs on sending volume with unlimited contacts on higher '
                                   'plan',
                                   'Matt Lucero ([_iGjRSCPXuA @ 00:14:19])'],
                                  ['Warm-up settings for live inboxes',
                                   '30 warm-up emails daily, randomized 20 to 30, about 40% reply rate',
                                   'Ramp goes 5, 10, 15, 20, 25, then 30 per day',
                                   'Matt Lucero ([_iGjRSCPXuA @ 00:51:01])'],
                                  ['Bounce auto-protection threshold setting',
                                   'Set to five so the campaign pauses once bounces exceed 5%',
                                   'Protects account deliverability like pulling over on a flat tire',
                                   'Smartlead ([J8lvEnIHcLk @ 01:52:30])'],
                                  ['Mailbox provider mix and vendor pricing',
                                   '40% Google, 30% Microsoft 365, 30% SMTP; mailboxes $2.50 up to $7 '
                                   'monthly',
                                   'Buy through Prime Forge, Mail Forge or Infraforge rather than GoDaddy',
                                   'Smartlead ([doR2rhof6CM @ 02:01:55])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Settings And Copy Moves The Operators Swear By',
                           'body': 'Small configuration and copy details that practitioners say keep '
                                   'sequences threaded, natural-looking and out of spam.',
                           'items': ['Leave the follow-up subject line blank so it stays in the same '
                                     'thread as email one, which looks more natural and is easier to read '
                                     '[Vincent Robin — 7Sq3Ger8D3A @ 00:11:09]',
                                     'Wrap first names in a liquid conditional so if 50 of 100 leads lack '
                                     "a name they get 'Hi there' instead of an awkward gap [Matt Lucero — "
                                     '_iGjRSCPXuA @ 01:58:52]',
                                     "Ask for a reply keyword like 'report', then fire a Smartlead "
                                     'subsequence on a text-contains trigger with a 0-day delay that sends '
                                     'the resource and steers toward a 15-minute call [Smartlead — '
                                     'doR2rhof6CM @ 00:31:44]',
                                     'Put links in the message as non-hyperlinked URLs in parentheses, '
                                     'because hyperlinks hurt deliverability [Michael Saruggia - GTM '
                                     'Engineering — qWuvWm5Zcz0 @ 00:09:25]']},
               'sop_steps': [{'step': 1,
                              'title': 'Reverse-engineer volume into inboxes and domains',
                              'action': 'Divide the monthly send target by sequence length, then by the '
                                        'per-inbox cap and inboxes per domain.',
                              'detail': 'For 100K emails on a three-touch sequence, plan 35,000 leads; at '
                                        '25 per inbox and two inboxes per domain, a one-month push needs '
                                        '200 inboxes on 100 domains and a three-month push needs 67 '
                                        'inboxes on 34 domains [Smartlead — C2lkX09G4h4 @ 00:03:17].'},
                             {'step': 2,
                              'title': 'Buy split infrastructure and ramp warm-up',
                              'action': 'Buy secondary domains, split mailboxes across Google, Outlook and '
                                        'SMTP, then ramp warm-up before cold sends.',
                              'detail': 'Run about 67 Google, 67 Outlook and the rest SMTP out of 200 '
                                        'inboxes; ramp 5-20 a day in week one, 25-55 in week two, 65-125 '
                                        'in week three, reaching full volume around day 30 [Smartlead — '
                                        'C2lkX09G4h4 @ 00:09:16].'},
                             {'step': 3,
                              'title': 'Build, verify and import the list',
                              'action': 'Pull ICP-filtered leads, keep verified addresses only, and import '
                                        'with dedupe toggles on.',
                              'detail': 'Define the ICP from past customers, filter Smart Prospect by '
                                        'industry, keywords, headcount and titles, run find-emails, send '
                                        "to verified only, and enable 'ignore leads in other campaigns' on "
                                        'import [Matt Lucero — _iGjRSCPXuA @ 00:26:33].'},
                             {'step': 4,
                              'title': 'Launch in batches with a bounce kill switch',
                              'action': 'Start on a fraction of the inbox pool and stop the moment bounces '
                                        'cross 2%.',
                              'detail': 'Start with 50 of 200 inboxes on batches of about 5,000 leads, '
                                        'stop and fix the list if bounces exceed 2%, read near-zero '
                                        'replies with low bounces as an offer or copy problem, and add '
                                        'inboxes in groups of 50 over one to two weeks [Smartlead — '
                                        'C2lkX09G4h4 @ 00:13:23].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Per-inbox volume is the loudest split on the floor. The Smartlead agency '
                              'operator behind the 100,000-email tutorial runs 25 messages per inbox per '
                              'day, excluding warmup, with two inboxes per domain, which works out to 50 '
                              'sends per domain daily, and warns that pushing more per inbox gets domains '
                              'flagged [C2lkX09G4h4 @ 00:02:20]. Tim from the Smartlead copywriting course '
                              'runs tighter: 15 emails per mailbox per day, two mailboxes per domain, and '
                              'a 22-day sending month with weekends dark [doR2rhof6CM @ 02:03:33]. Wesley, '
                              'sending 20,000 emails in 30 days through Claude Code, goes more '
                              'conservative still at 10 per inbox per day, but stacks three to five '
                              'inboxes on each lookalike domain, landing on 100 inboxes across 34 domains '
                              'for 1,000 sends daily [NWEL3WNYDhg @ 00:02:37]. Jim Fung frames it at the '
                              'domain level instead, saying you can safely send between 50 and 100 emails '
                              'per domain and that 1,500 a day beats 50 a day because volume negates luck '
                              '[B-xnx1pQQKY @ 00:06:06]. Every camp runs the same physics, many inboxes at '
                              'low individual load, yet the daily ceiling ranges from 10 to 25 per inbox '
                              'depending on whose risk tolerance you adopt, and the domain count you buy '
                              'moves with that choice.',
                              'The second fault line is whether domains are assets or consumables. Michael '
                              'Saruggia re-hits one 10,000-lead ICP list, adding a new step whenever a '
                              "sequence finishes, and treats reputation damage as a line item: 'If they "
                              "block me, my deliverability goes down, I buy new addresses' [qWuvWm5Zcz0 @ "
                              '00:14:26]. The Smartlead 100,000-email operator runs the opposite playbook, '
                              'sending a three-touch sequence across 35,000 fresh verified leads, '
                              'splitting inboxes across Google, Outlook and SMTP, and halting the moment '
                              'bounce rate crosses 2% to fix the list before another email leaves '
                              '[C2lkX09G4h4 @ 00:13:23]. Matt Lucero sits between the two: settings stay '
                              'disciplined, but when accounts still fail after copy and infrastructure '
                              'check out, the move is to crash the car and get a new car by buying fresh '
                              'accounts [J8lvEnIHcLk @ 01:34:27]. Sergio Perea of Boost Hero calls the '
                              'slow-burn approach a trap, describing operators who raise per-inbox volume '
                              'from 50 to 100 to 150 and find two months later that domains are burned, '
                              'spam is up and replies are down, with no warning light along the way '
                              '[lvp7ODzi7I8 @ 00:01:54]. Burn-and-replace runs on a standing budget for '
                              'new addresses; the protect model runs on verification, secondary domains '
                              'and a hard bounce kill switch.',
                              'Sequence length and who writes the copy also split the room. Tim from the '
                              'Smartlead copywriting course says sequences shrank from five emails in 2018 '
                              'and 2019 to two or three, and sets a hard cap: never send more than three '
                              "emails per sequence, with a fresh template for each touch and never a 'just "
                              "checking in' [doR2rhof6CM @ 01:29:20]. Vincent Robin goes leaner, running "
                              'one email and one follow-up because more touches trigger spam reports, yet '
                              "defends a bare 'just quick follow-up' line, saying hundreds still go out "
                              'daily and answers still come back every day despite LinkedIn claims that '
                              'bare follow-ups fail [7Sq3Ger8D3A @ 00:10:51]. On copy production, Tim '
                              'leans on AI personalization tools like Twain.ai, Octave and Autobound, '
                              'while Wesley built an entire Claude Code send machine but wrote the copy '
                              "manually, saying 'that's something that I didn't use AI to do' [NWEL3WNYDhg "
                              '@ 00:09:08]. The Smartlead 200,000-email operator splits the difference, '
                              'running deep research in Claude Code trained on five to ten manually '
                              'written emails before pushing personalized lines into Smartlead through the '
                              'MCP [CAJAVLQEQ88 @ 00:05:51]. The one point Tim and Vincent share: nobody '
                              'here still runs the five-email sequences of 2018.'],
               'table': {'caption': 'Competing Playbooks: Volume, Domain Risk, Sequences and Platform '
                                    'Choice',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Daily sends per individual inbox',
                                   '25 per inbox per day with two inboxes per domain, giving 50 sends per '
                                   'domain daily',
                                   '10 per inbox per day with three to five inboxes per lookalike domain '
                                   'to stay conservative',
                                   'Smartlead ([C2lkX09G4h4 @ 00:02:20]); Smartlead ([NWEL3WNYDhg @ '
                                   '00:02:37])'],
                                  ['Domain reputation stance and list model',
                                   'Accept lower deliverability, re-hit the same 10,000-lead list and buy '
                                   'new addresses when blocked',
                                   'Stop at a 2% bounce rate, use secondary domains only and split '
                                   'providers to protect every inbox',
                                   'Michael Saruggia - GTM Engineering ([qWuvWm5Zcz0 @ 00:14:26]); '
                                   'Smartlead ([C2lkX09G4h4 @ 00:13:23])'],
                                  ['Number of follow-ups per sequence',
                                   'Three net-new emails maximum, emails one and two threaded, email three '
                                   'as a new thread',
                                   'One email plus one blank-subject follow-up after two days because more '
                                   'touches trigger spam reports',
                                   'Smartlead ([doR2rhof6CM @ 01:25:33]); Vincent Robin ([7Sq3Ger8D3A @ '
                                   '00:11:42])'],
                                  ['Pre-warmed versus fresh mailboxes',
                                   'Pre-warmed mailboxes send on day one with no performance difference in '
                                   'split tests but cost more',
                                   'Fresh mailboxes at $4.50 per month need a warmup ramp reaching full '
                                   'volume around day 30',
                                   'Matt Lucero ([_iGjRSCPXuA @ 00:32:29]); Smartlead ([C2lkX09G4h4 @ '
                                   '00:09:16])'],
                                  ['Community bounce list import setting',
                                   'Keep the default exclusion on even though shared community bounce data '
                                   'could be false',
                                   'Leave the global bounce list ignored because data from other users may '
                                   'not be accurate',
                                   'Smartlead ([J8lvEnIHcLk @ 01:37:46]); Matt Lucero ([nWq972pdw00 @ '
                                   '00:07:24])'],
                                  ['Sending platform for agency-scale operators',
                                   'Smartlead for multi-client workspaces, white-label, unlimited inboxes '
                                   'and API depth suiting most operators',
                                   'Email Bison at $500 to $600 monthly or Plus Vibe at $415 for '
                                   'agency-scale volume',
                                   'George Vlasyev ([S8imkVkGoZw @ 00:00:48]); Lead Gen Jay ([u6rzEjXQdmo '
                                   '@ 00:13:28])'],
                                  ['First tool for a beginner sender',
                                   'Instantly because it makes starting cold email campaigns as easy as '
                                   'possible for newcomers',
                                   'Smartlead wins at volume and for anyone who already has contacts to '
                                   'load and send',
                                   'Lead Gen Jay ([u6rzEjXQdmo @ 00:21:38]); Software Scope ([00esG7HsVNs '
                                   '@ 00:07:34])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failure is infrastructure collapse. The Smartlead '
                              '100,000-email operator warns that high-volume senders typically land in '
                              'spam within two weeks, and has watched agencies lose every inbox overnight '
                              'by parking them all on one provider, which is why 200 inboxes get split 67 '
                              'Google, 67 Outlook and the rest SMTP [C2lkX09G4h4 @ 00:08:16]. Matt Lucero '
                              'adds that Google and Microsoft can suspend accounts pushing around 10,000 a '
                              'day, that SMTP through Mail Reef has no built-in cap but more variance, and '
                              'that warm-up is not a cure-all because it cannot save you from spam reports '
                              '[J8lvEnIHcLk @ 00:48:57]. Sergio Perea of Boost Hero pins the root cause on '
                              'per-inbox greed, the 50-to-150 creep that burns domains with no warning '
                              'light, and insists no sequencer fixes a bad list, weak offer or wrong ICP '
                              "[lvp7ODzi7I8 @ 00:03:36]. Recipient-side landmines matter too: Wesley's "
                              'Claude Code build excluded Zoho recipients outright after the Zoho '
                              'apocalypse and can filter the list down to Google inboxes only [NWEL3WNYDhg '
                              '@ 00:06:56]. The operator check is simple: count providers, count inboxes '
                              'per domain, and confirm warm-up stays running on every inbox at all times, '
                              'exactly as the 100,000-email build demands.',
                              'Dirty data is the second silent killer. At 35,000 leads, a list that is 95% '
                              'accurate still throws well over 1,000 bounces, which is why the Smartlead '
                              '100,000-email operator verifies every address, reaches a 0.3% bounce rate, '
                              'and kills the campaign above 2% [C2lkX09G4h4 @ 00:10:20]. Tim treats 1.27% '
                              'to 2% as fine and 4% to 5% as a warning that demands re-verification '
                              'through a second tool, and notes single providers only find 40% to 60% of '
                              'emails, so out of 10 people you find six [doR2rhof6CM @ 02:07:27]. Gabriel '
                              'Martinez of ReachFlow, on the Smartlead channel, warns that data decays at '
                              '2% to 3% per month, that Apollo revenue and funding fields are unreliable '
                              "with 15% stale inside six months, and that Apollo's own sequencer is fine "
                              'under 40 to 50 emails a day but not above 100 [vQSB7GXedMM @ 00:15:49]. '
                              "Matt Lucero's own pull shows the attrition in real numbers: 469 leads "
                              'yielded 107 verified and 67 catch-all, and only the 153 verified plus '
                              'catch-all-verified leads went out [J8lvEnIHcLk @ 00:26:46]. Lists shrink '
                              'hard between scrape and send, so the 35,000-lead target has to be met after '
                              'verification, not before it.',
                              'The last layer of traps lives inside settings and seat economics. Matt '
                              'Lucero says 99% of low-volume complaints trace to triggers per day, max new '
                              'leads per day, the mailbox daily limit or a time gap set too high, and that '
                              '100% follow-up priority starves new leads, the exact mistake behind '
                              'campaigns that send mostly follow-ups [_iGjRSCPXuA @ 02:56:27]. The same '
                              'tutorial flags that a stopped campaign cannot simply be resumed, only '
                              'restarted through final review, a fix that took a couple of years to figure '
                              'out, and that removing a mailbox mid-sequence strands its leads without '
                              'later steps [J8lvEnIHcLk @ 02:08:33]. On the reply side, Hoani Taylor calls '
                              'a high-volume master inbox a nightmare where mistakes cost calls, and found '
                              'that asking GPT-4o mini to pick from 27 categories in one pass gets it '
                              'wrong far more often than a tiered three-bucket first pass [7360Lif0HLQ @ '
                              "00:03:08]. Lead Gen Jay's economics check on Instantly: the $47 plan caps "
                              'at 1,000 contacts, 125,000 contacts runs almost $1,000 a month, and leads '
                              'must be deleted after campaigns, wiping history [u6rzEjXQdmo @ 00:05:31]. '
                              'Audit those four sending limits and the platform bill before rewriting a '
                              'single line of copy.'],
               'table': {'caption': 'Firsthand Failure Modes and the Fixes Practitioners Applied',
                         'headers': ['Failure Mode', 'What Happened', 'Practitioner Fix', 'Expert Source'],
                         'rows': [['Single-provider inbox concentration',
                                   'Agencies lost every inbox overnight when all mailboxes sat on one '
                                   'provider',
                                   'Split 200 inboxes into 67 Google, 67 Outlook and the remaining on SMTP',
                                   'Smartlead ([C2lkX09G4h4 @ 00:08:16])'],
                                  ['Bounce spike from an unverified list',
                                   'A 95% accurate list at 35,000 leads produced well over 1,000 bounces',
                                   'Verify every address and stop the campaign once bounces exceed 2%',
                                   'Smartlead ([C2lkX09G4h4 @ 00:13:23])'],
                                  ['Per-inbox volume creep over two months',
                                   'Raising sends from 50 to 100 to 150 burned domains while replies fell',
                                   'Add more inboxes, lower per-inbox volume and keep warm-up running '
                                   'constantly',
                                   'Sergio Perea | Boost Hero ([lvp7ODzi7I8 @ 00:03:53])'],
                                  ['Campaign stuck at low daily volume',
                                   'Triggers per day, max new leads, mailbox cap or time gap throttled '
                                   'real sends',
                                   'Lower the time gap and raise the maximum limits so the campaign sends '
                                   'through',
                                   'Matt Lucero ([_iGjRSCPXuA @ 02:56:27])'],
                                  ['Burned accounts despite clean settings',
                                   'Copy and infrastructure both checked out yet the accounts still failed '
                                   'to land',
                                   'Crash the car and get a new car by buying fresh email accounts',
                                   'Smartlead ([J8lvEnIHcLk @ 01:34:27])'],
                                  ['AI reply misclassification in the inbox',
                                   'One-pass classification across 27 categories got replies wrong far '
                                   'more often',
                                   'Tier into interested, not interested and automated, then feed '
                                   'misclassified replies back as examples',
                                   'Hoani Taylor ([7360Lif0HLQ @ 00:03:08])'],
                                  ['Overpersonalized cold email openers',
                                   'Stuffing personalization snippets made some prospects reply that the '
                                   'email was too much',
                                   'Cap personalization at two to seven snippets per email and lead with '
                                   'relevance',
                                   'Smartlead ([doR2rhof6CM @ 00:20:50])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Scale Gate: Clear These Before Adding Inboxes',
                           'body': 'Every item below is a pitfall a named practitioner hit or guarded '
                                   'against in live sending. Do not add the next batch of 50 inboxes until '
                                   'all four are confirmed.',
                           'items': ['Bounce protection armed at 5 in campaign settings, with a manual '
                                     'stop and list fix the moment bounce rate passes 2% [Vincent Robin — '
                                     '7Sq3Ger8D3A @ 00:13:34].',
                                     'Inboxes split across Google, Outlook and SMTP so a single provider '
                                     'action cannot wipe the whole fleet overnight [Smartlead — '
                                     'C2lkX09G4h4 @ 00:08:16].',
                                     'Triggers per day, max new leads per day, mailbox daily limit and '
                                     'minimum time gap audited before blaming copy for low volume [Matt '
                                     'Lucero — _iGjRSCPXuA @ 02:56:27].',
                                     'Optimize delivery and plain text switched on with no links, images, '
                                     'open tracking or click tracking in the sequence [Smartlead — '
                                     'J8lvEnIHcLk @ 01:48:04].']}}],
 'pull_quote': '"Low volume per inbox is spread across a high inbox count. Everything else is just burning '
               'domain slowly." Sergio Perea | Boost Hero (lvp7ODzi7I8 @ 00:00:32).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Size infrastructure from lead math: a three-email sequence means 100,000 sends '
                      'needs about 35,000 leads, run at 25 per inbox per day with two inboxes per domain '
                      '(Smartlead, C2lkX09G4h4 @ 00:01:00).',
                      'Buy secondary lookalike domains, never send from the primary domain, and redirect '
                      'each sending domain to the main site (Smartlead, NWEL3WNYDhg @ 00:01:36).',
                      'Warm up fresh mailboxes for at least 14 days at 30 per day randomized between 20 '
                      'and 30, weekdays only, and keep warm-up running after launch (Matt Lucero, '
                      '_iGjRSCPXuA @ 00:51:01).',
                      'Send only to verified leads and enable ignore leads in other campaigns so '
                      'overlapping lists dedupe on import (Matt Lucero, _iGjRSCPXuA @ 00:26:33).',
                      'Launch on 50 of 200 inboxes while the rest keep warming, add inboxes in groups of '
                      '50 over one to two weeks, and stop above a 2% bounce rate (Smartlead, C2lkX09G4h4 @ '
                      '00:12:45).',
                      'Automate reply triage: Smartlead reply webhook into n8n, tiered GPT-4o mini '
                      'classification, category update in Smartlead, then auto-reply or Slack alert (Hoani '
                      'Taylor, 7360Lif0HLQ @ 00:01:01).'],
 'statutory_citations': [{'title': "Smartlead — If I Wanted to Send 100,000 Cold Emails, I'd Do This "
                                   '(Tutorial) [00:13:23]',
                          'url': 'https://www.youtube.com/watch?v=C2lkX09G4h4&t=803s',
                          'relevance': 'Primary practitioner testimony on the 2% bounce kill switch, batch '
                                       'launch and multi-provider inbox splits.'},
                         {'title': 'Matt Lucero — How To Use Smartlead.ai 2026 - Full Cold Email Tutorial '
                                   '[02:56:27]',
                          'url': 'https://www.youtube.com/watch?v=_iGjRSCPXuA&t=10587s',
                          'relevance': 'Primary practitioner testimony on the four sending limits behind '
                                       'low-volume campaigns.'},
                         {'title': 'Sergio Perea | Boost Hero — Smartlead vs EmailBison: The Best Cold '
                                   'Email Tools for 2026 [00:00:32]',
                          'url': 'https://www.youtube.com/watch?v=lvp7ODzi7I8&t=32s',
                          'relevance': 'Primary practitioner testimony on low per-inbox volume and the '
                                       'domain-burning volume creep trap.'},
                         {'title': 'Smartlead — Complete B2B Cold Email Copywriting Course Using AI (2026) '
                                   '[01:29:20]',
                          'url': 'https://www.youtube.com/watch?v=doR2rhof6CM&t=5360s',
                          'relevance': 'Primary practitioner testimony on the three-email sequence cap and '
                                       'bounce re-verification thresholds.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'qWuvWm5Zcz0',
                       'title': 'How I Am Sending 50K Cold Emails Per Month with Smartlead AI (Full Guide)',
                       'channel': 'Michael Saruggia - GTM Engineering',
                       'author': 'Michael Saruggia - GTM Engineering',
                       'text': 'If they block me, my deliverability goes down, I buy new addresses.',
                       'tip': 'If they block me, my deliverability goes down, I buy new addresses.',
                       'timestamp': 866,
                       'timestamp_seconds': 866,
                       'timestamp_label': '[00:14:26]',
                       'url': 'https://www.youtube.com/watch?v=qWuvWm5Zcz0&t=866s',
                       'markdown': '[00:14:26](https://www.youtube.com/watch?v=qWuvWm5Zcz0&t=866s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'C2lkX09G4h4',
                       'title': "If I Wanted to Send 100,000 Cold Emails, I'd Do This (Tutorial)",
                       'channel': 'Smartlead',
                       'author': 'Smartlead',
                       'text': 'The first is the bounce rate and if that goes above 2%, I stop and fix the '
                               'list before I send another email.',
                       'tip': 'The first is the bounce rate and if that goes above 2%, I stop and fix the '
                              'list before I send another email.',
                       'timestamp': 803,
                       'timestamp_seconds': 803,
                       'timestamp_label': '[00:13:23]',
                       'url': 'https://www.youtube.com/watch?v=C2lkX09G4h4&t=803s',
                       'markdown': '[00:13:23](https://www.youtube.com/watch?v=C2lkX09G4h4&t=803s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'C2lkX09G4h4',
                       'title': "If I Wanted to Send 100,000 Cold Emails, I'd Do This (Tutorial)",
                       'channel': 'Smartlead',
                       'author': 'Smartlead',
                       'text': 'So with 200 inboxes, I do about 67 on Google, 67 on Outlook, and the rest '
                               'on SMTP.',
                       'tip': 'So with 200 inboxes, I do about 67 on Google, 67 on Outlook, and the rest '
                              'on SMTP.',
                       'timestamp': 496,
                       'timestamp_seconds': 496,
                       'timestamp_label': '[00:08:16]',
                       'url': 'https://www.youtube.com/watch?v=C2lkX09G4h4&t=496s',
                       'markdown': '[00:08:16](https://www.youtube.com/watch?v=C2lkX09G4h4&t=496s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_iGjRSCPXuA',
                       'title': 'How To Use Smartlead.ai 2026 - Full Cold Email Tutorial',
                       'channel': 'Matt Lucero',
                       'author': 'Matt Lucero',
                       'text': 'When in doubt, lower your email send time, like the gap, and uh raise the '
                               'maximum limits and it will send through.',
                       'tip': 'When in doubt, lower your email send time, like the gap, and uh raise the '
                              'maximum limits and it will send through.',
                       'timestamp': 10587,
                       'timestamp_seconds': 10587,
                       'timestamp_label': '[02:56:27]',
                       'url': 'https://www.youtube.com/watch?v=_iGjRSCPXuA&t=10587s',
                       'markdown': '[02:56:27](https://www.youtube.com/watch?v=_iGjRSCPXuA&t=10587s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'doR2rhof6CM',
                       'title': 'Complete B2B Cold Email Copywriting Course Using AI (2026)',
                       'channel': 'Smartlead',
                       'author': 'Smartlead',
                       'text': 'And in total, never send more than three emails per cold email sequence.',
                       'tip': 'And in total, never send more than three emails per cold email sequence.',
                       'timestamp': 5360,
                       'timestamp_seconds': 5360,
                       'timestamp_label': '[01:29:20]',
                       'url': 'https://www.youtube.com/watch?v=doR2rhof6CM&t=5360s',
                       'markdown': '[01:29:20](https://www.youtube.com/watch?v=doR2rhof6CM&t=5360s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NWEL3WNYDhg',
                       'title': 'I Sent 20,000 Cold Emails With Claude Code in 30 Days (Results)',
                       'channel': 'Smartlead',
                       'author': 'Smartlead',
                       'text': "So, that's something that I didn't use AI to do.",
                       'tip': "So, that's something that I didn't use AI to do.",
                       'timestamp': 548,
                       'timestamp_seconds': 548,
                       'timestamp_label': '[00:09:08]',
                       'url': 'https://www.youtube.com/watch?v=NWEL3WNYDhg&t=548s',
                       'markdown': '[00:09:08](https://www.youtube.com/watch?v=NWEL3WNYDhg&t=548s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'S8imkVkGoZw',
                       'title': 'Instantly AI vs Smartlead 2026: Which Cold Email Tool Is Right for You?',
                       'channel': 'George Vlasyev',
                       'author': 'George Vlasyev',
                       'text': 'SmartLead adds structure and control for scale.',
                       'tip': 'SmartLead adds structure and control for scale.',
                       'timestamp': 82,
                       'timestamp_seconds': 82,
                       'timestamp_label': '[00:01:22]',
                       'url': 'https://www.youtube.com/watch?v=S8imkVkGoZw&t=82s',
                       'markdown': '[00:01:22](https://www.youtube.com/watch?v=S8imkVkGoZw&t=82s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'J8lvEnIHcLk',
                       'title': 'Full Smartlead.ai Tutorial 2026 (Best Cold Email Software)',
                       'channel': 'Smartlead',
                       'author': 'Smartlead',
                       'text': "Now again, warm-up doesn't cure everything.",
                       'tip': "Now again, warm-up doesn't cure everything.",
                       'timestamp': 2937,
                       'timestamp_seconds': 2937,
                       'timestamp_label': '[00:48:57]',
                       'url': 'https://www.youtube.com/watch?v=J8lvEnIHcLk&t=2937s',
                       'markdown': '[00:48:57](https://www.youtube.com/watch?v=J8lvEnIHcLk&t=2937s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '00esG7HsVNs',
                       'title': 'Smartlead Vs Instantly (2026) | Which Cold Email Tool Is Better?',
                       'channel': 'Software Scope',
                       'author': 'Software Scope',
                       'text': 'So instantly is not a cheap tool.',
                       'tip': 'So instantly is not a cheap tool.',
                       'timestamp': 263,
                       'timestamp_seconds': 263,
                       'timestamp_label': '[00:04:23]',
                       'url': 'https://www.youtube.com/watch?v=00esG7HsVNs&t=263s',
                       'markdown': '[00:04:23](https://www.youtube.com/watch?v=00esG7HsVNs&t=263s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7Sq3Ger8D3A',
                       'title': 'How To Setup Your Smartlead.ai Cold Email Campaign',
                       'channel': 'Vincent Robin',
                       'author': 'Vincent Robin',
                       'text': "I'm still sending hundreds of this kind of follow-up every day and I still "
                               'have answer every day.',
                       'tip': "I'm still sending hundreds of this kind of follow-up every day and I still "
                              'have answer every day.',
                       'timestamp': 651,
                       'timestamp_seconds': 651,
                       'timestamp_label': '[00:10:51]',
                       'url': 'https://www.youtube.com/watch?v=7Sq3Ger8D3A&t=651s',
                       'markdown': '[00:10:51](https://www.youtube.com/watch?v=7Sq3Ger8D3A&t=651s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CAJAVLQEQ88',
                       'title': 'How I Send 200,000+ Cold Emails Per Month With AI',
                       'channel': 'Smartlead',
                       'author': 'Smartlead',
                       'text': 'So, as you can see on the screen now, if email provider A does not find '
                               'the email, we go to email provider B, then email provider C, and so on.',
                       'tip': 'So, as you can see on the screen now, if email provider A does not find the '
                              'email, we go to email provider B, then email provider C, and so on.',
                       'timestamp': 455,
                       'timestamp_seconds': 455,
                       'timestamp_label': '[00:07:35]',
                       'url': 'https://www.youtube.com/watch?v=CAJAVLQEQ88&t=455s',
                       'markdown': '[00:07:35](https://www.youtube.com/watch?v=CAJAVLQEQ88&t=455s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'B-xnx1pQQKY',
                       'title': 'How To ACTUALLY Start A Lead Generation Agency In 2026 (For Beginners)',
                       'channel': 'Jim Fung',
                       'author': 'Jim Fung',
                       'text': 'Now the general rule of thumb is you can safely send somewhere between 50 '
                               'and 100 emails per one domain.',
                       'tip': 'Now the general rule of thumb is you can safely send somewhere between 50 '
                              'and 100 emails per one domain.',
                       'timestamp': 366,
                       'timestamp_seconds': 366,
                       'timestamp_label': '[00:06:06]',
                       'url': 'https://www.youtube.com/watch?v=B-xnx1pQQKY&t=366s',
                       'markdown': '[00:06:06](https://www.youtube.com/watch?v=B-xnx1pQQKY&t=366s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7360Lif0HLQ',
                       'title': 'How To Use n8n To Automate Cold Email Replies in Smartlead',
                       'channel': 'Hoani Taylor',
                       'author': 'Hoani Taylor',
                       'text': "So, it's going to be far more accurate if there's only three options with "
                               "10 examples each than if there's 30 options with one example each.",
                       'tip': "So, it's going to be far more accurate if there's only three options with "
                              "10 examples each than if there's 30 options with one example each.",
                       'timestamp': 548,
                       'timestamp_seconds': 548,
                       'timestamp_label': '[00:09:08]',
                       'url': 'https://www.youtube.com/watch?v=7360Lif0HLQ&t=548s',
                       'markdown': '[00:09:08](https://www.youtube.com/watch?v=7360Lif0HLQ&t=548s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'u6rzEjXQdmo',
                       'title': 'This Changes Everything for Cold Email Agencies',
                       'channel': 'Lead Gen Jay',
                       'author': 'Lead Gen Jay',
                       'text': 'So, this $600 per month comes with 500,000 emails per month.',
                       'tip': 'So, this $600 per month comes with 500,000 emails per month.',
                       'timestamp': 808,
                       'timestamp_seconds': 808,
                       'timestamp_label': '[00:13:28]',
                       'url': 'https://www.youtube.com/watch?v=u6rzEjXQdmo&t=808s',
                       'markdown': '[00:13:28](https://www.youtube.com/watch?v=u6rzEjXQdmo&t=808s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nWq972pdw00',
                       'title': 'Smartlead.ai Beginner Tutorial 2026',
                       'channel': 'Matt Lucero',
                       'author': 'Matt Lucero',
                       'text': 'I usually leave this on to ignore it because it takes data from all kinds '
                               'of different users on the platform which may or may not be accurate.',
                       'tip': 'I usually leave this on to ignore it because it takes data from all kinds '
                              'of different users on the platform which may or may not be accurate.',
                       'timestamp': 444,
                       'timestamp_seconds': 444,
                       'timestamp_label': '[00:07:24]',
                       'url': 'https://www.youtube.com/watch?v=nWq972pdw00&t=444s',
                       'markdown': '[00:07:24](https://www.youtube.com/watch?v=nWq972pdw00&t=444s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'vQSB7GXedMM',
                       'title': 'The Best Cold Email Tools in 2026 (Complete Guide)',
                       'channel': 'Smartlead',
                       'author': 'Smartlead',
                       'text': 'Data decays at a rate of 2-3% per month.',
                       'tip': 'Data decays at a rate of 2-3% per month.',
                       'timestamp': 949,
                       'timestamp_seconds': 949,
                       'timestamp_label': '[00:15:49]',
                       'url': 'https://www.youtube.com/watch?v=vQSB7GXedMM&t=949s',
                       'markdown': '[00:15:49](https://www.youtube.com/watch?v=vQSB7GXedMM&t=949s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lvp7ODzi7I8',
                       'title': 'Smartlead vs EmailBison: The Best Cold Email Tools for 2026',
                       'channel': 'Sergio Perea | Boost Hero',
                       'author': 'Sergio Perea | Boost Hero',
                       'text': 'Low volume per inbox is spread across a high inbox count.',
                       'tip': 'Low volume per inbox is spread across a high inbox count.',
                       'timestamp': 32,
                       'timestamp_seconds': 32,
                       'timestamp_label': '[00:00:32]',
                       'url': 'https://www.youtube.com/watch?v=lvp7ODzi7I8&t=32s',
                       'markdown': '[00:00:32](https://www.youtube.com/watch?v=lvp7ODzi7I8&t=32s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'}]}
