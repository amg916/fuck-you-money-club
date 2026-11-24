from __future__ import annotations

CHAPTER_7 = {'id': 'Q7',
 'chapter_id': 'Q7',
 'chapter_number': 7,
 'question_number': 7,
 'slug': 'linkedin-outreach-appointment-setting-systems',
 'question_prompt': 'How do practitioners book meetings through LinkedIn outreach, appointment-setting '
                    'teams, and automated lead conversations?',
 'kicker': 'Q7 / THE BIG MONEY PLAYBOOKS',
 'title': 'LinkedIn Outreach and Appointment-Setting Systems',
 'subtitle': 'HeyReach and alternative DM tools, LinkedIn messaging workflows, pay-per-appointment sales '
             'teams, AI voice speed-to-lead, mortgage SMS booking, and automated sales follow-up',
 'layout_template': 'thirty_day_roadmap',
 'reading_time_minutes': 15,
 'executive_summary': 'LinkedIn outreach operators agree the list and the offer decide results before any '
                      'tool does: target active posters and post engagers, segment beyond job title, send '
                      'blank connection requests, and open with a no-pitch, value-first message that asks '
                      'one easy question. LinkedIn caps each account at roughly 100 to 200 connection '
                      'requests per week, so operators scale by stacking sender accounts, timing sends to '
                      "the prospect's time zone, and auto-stopping sequences on reply. Amon measures 27% "
                      'acceptance on blank requests versus 22% with text and tests variants in 150/150 '
                      'splits. Appointment-setting operators add speed-to-lead AI agents that contact '
                      'leads within five minutes and pay-per-qualified-appointment pricing. Practitioners '
                      'split on daily ceilings, from 20 to 40 per account, on follow-up length, on '
                      'rotating versus static IPs, and on whether connection notes help or hurt.',
 'key_metrics': [{'label': 'Blank vs. written connection request acceptance',
                  'metric': 'Blank vs. written connection request acceptance',
                  'value': 'About 27% blank vs. 22% with text',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Amon's measured acceptance gap between empty connection requests and "
                             'requests carrying a note, sent through HeyReach.',
                  'source': 'HeyReach ([Cgx8HVnGOdY @ 00:30:30])'},
                 {'label': 'Reply-rate decay by connection batch',
                  'metric': 'Reply-rate decay by connection batch',
                  'value': '12% first 50, 6% next 100, 2% next 200',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Reply rates falling as connection volume climbs, drawn from roughly 100K '
                             'HeyReach campaigns.',
                  'source': 'HeyReach ([RYTMEUD8-FQ @ 00:01:40])'},
                 {'label': 'Weekly connection request cap per account',
                  'metric': 'Weekly connection request cap per account',
                  'value': 'About 100 per week, roughly 10 to 15 per day',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Per-account LinkedIn ceiling with a weekly reset; scale comes from adding '
                             'sender accounts.',
                  'source': 'HeyReach ([5JAMkYMtvhw @ 00:07:28])'},
                 {'label': 'Interested-to-booked conversion floor',
                  'metric': 'Interested-to-booked conversion floor',
                  'value': 'At least 35% of interested leads should book',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Inbox-management audit line; ten interested leads producing one booking '
                             'signals a problem.',
                  'source': 'Matt Harriman ([hm5isqC1d74 @ 00:06:18])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every serious LinkedIn operator starts the same place: the list and the '
                              'offer, not the software. Matt Harriman calls starting with LinkedIn itself '
                              'the biggest mistake, and makes operators answer who to target, why that '
                              'person would want to talk, and what to say before a single request goes out '
                              "[hm5isqC1d74 @ 00:00:12]. Harriman's math is blunt: a $50,000 client does "
                              "not need 10,000 leads, only the right 300, and the 'posted on LinkedIn' "
                              'filter in Sales Navigator is the most important part of the build. '
                              "HeyReach's Amon, who credits LinkedIn outreach with over $5M for the agency "
                              "and its clients across five years, puts it as 'your LinkedIn Outreach is "
                              "only as strong as your offer' and defines a strong offer as a clear "
                              'outcome, credibility through proof, a guarantee or derisking, and easy to '
                              'buy [Cgx8HVnGOdY @ 00:07:34]. The HeyReach team pushes hyper-specific '
                              'segments so the copy speaks to one person, warning that title-only lists '
                              'are a mistake because a job title at a 20-person company means something '
                              'completely different at a 500-person one; getting prospecting right moved '
                              'reply rates from 20% to 40% [5JAMkYMtvhw @ 00:01:04]. Their demo names poor '
                              'lists as a key reason campaigns fail [3o3gecljGlE @ 00:00:12].',
                              'On the connection request itself, the consensus is close to unanimous: no '
                              'pitch. Amon measured blank requests at roughly 27% acceptance against 22% '
                              'with text, then frames the opener as an observation followed by a question, '
                              'using a direct ask only when the offer is strong, such as an insurance '
                              "client's guaranteed 30 to 50% savings [Cgx8HVnGOdY @ 00:30:30]. HeyReach's "
                              'team says they always advise leaving requests empty, citing a 5% lift over '
                              'personalized notes, then sends a 3-to-5-sentence value-first first message '
                              "with no pitch and the smallest possible ask, with the standing rule: 'Never "
                              "reword your first message' [5JAMkYMtvhw @ 00:04:50]. Harry Long sends "
                              "requests blank because a blank invite 'spikes curiosity' and raises "
                              'acceptance, yet still tells operators to test both versions before locking '
                              'anything in [DgzklijTLzE @ 00:06:00]. lemlist lands on the same line with '
                              "sharper language: 'If you pitch in the connection request, you're dead,' "
                              "LinkedIn 'isn't about pitching,' and the message should run Socratic, an "
                              'observation that sparks curiosity rather than a feature dump or a calendar '
                              'link dropped cold [-LtGmHnpioI @ 00:06:20]. Across all four, the first '
                              'touch earns a conversation and nothing more; the meeting gets asked for '
                              'later, once the prospect has replied and qualified.',
                              'The appointment-setting operators converge on two baselines: speed and '
                              'qualification. Tommy Chryst sells speed-to-lead voice systems on the claim '
                              'that calling within 5 minutes makes a company 8x more likely to get a '
                              'response while the average company takes over 2 hours, backed by 400K+ '
                              "automated calls [YQbr_FhZTo8 @ 00:00:14]. Zenscape's Alice bot rests on the "
                              "same 5-minute rationale [HeluxMYTT0o @ 00:06:55], and Genesys Digital's "
                              "mortgage setter books the next available slot with 'absolutely no human "
                              "interaction' from the broker's side [I-riwAqQ3us @ 00:04:28]. On the buying "
                              'side, ViB opens with 90% of B2B marketers calling appointment setting '
                              "effective while only 21% prioritize it, and the 'one thing you must take "
                              "away' is a clear targeting and qualification process; the pricing warning "
                              "is to refuse vendors who charge per appointment set 'whatever the quality' "
                              'and to pay per qualified appointment instead [w2J3Ou1jTR4 @ 00:02:43]. '
                              "Typical vendors in ViB's account stack big onboarding fees, long-term "
                              'contracts and hourly or retainer billing regardless of results, which is '
                              'why operators on both sides tie payment to a booked, qualified meeting '
                              'rather than to activity or raw appointment counts that may never show up.'],
               'table': {'caption': 'Practitioner consensus on LinkedIn outreach and appointment setting',
                         'headers': ['Consensus Point',
                                     'What Practitioners Do',
                                     'Why It Matters',
                                     'Expert Source'],
                         'rows': [['Fix the offer and targeting before touching any software',
                                   'Answer who to target, why they talk, and what to say',
                                   'Automation comes last; a $50,000 client needs only the right 300',
                                   'Matt Harriman ([hm5isqC1d74 @ 00:00:12])'],
                                  ['Blank connection requests beat requests carrying a written note',
                                   'Send the invite empty, then open with value and a question',
                                   "Roughly 27% acceptance blank versus 22% with text in Amon's accounts",
                                   'HeyReach ([Cgx8HVnGOdY @ 00:30:30])'],
                                  ['Hyper-specific segments outperform broad job-title-only prospect lists',
                                   'Segment by company size or industry niche, not title alone',
                                   'Getting prospecting right moved reply rates from 20% up to 40%',
                                   'HeyReach ([5JAMkYMtvhw @ 00:01:04])'],
                                  ['Active posters and post engagers carry the real buying intent',
                                   'Pull likes, comments and reposts from posts targeting your ICP',
                                   'One post URL produced about 700 leads already active on-platform',
                                   'Aimfox ([O8VBEriCr60 @ 00:03:04])'],
                                  ["Messages land inside the prospect's working hours, never the sender's",
                                   "Schedule sends 9 to 5 in the target's own time zone",
                                   'Outreach arrives when prospects are actually working and reading '
                                   'messages',
                                   'Aimfox ([O8VBEriCr60 @ 00:08:38])'],
                                  ['Sequences stop automatically the moment a prospect replies back',
                                   'Replies unenroll prospects from the campaign, so threads move to '
                                   'manual handling',
                                   'Put 10 to 15 minutes aside each morning for positive replies',
                                   'Harry Long ([DgzklijTLzE @ 00:12:12])'],
                                  ['Speed to lead decides whether inbound appointments ever get booked',
                                   'Call or message new leads within five minutes using AI agents',
                                   'Five-minute contact claimed 8x more likely to get a response',
                                   'Tommy Chryst ([YQbr_FhZTo8 @ 00:00:14])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Volume on LinkedIn is capped per account, so scale comes from stacking '
                              "senders. HeyReach's team puts the ceiling at about 100 connection requests "
                              'per week per account, roughly 10 to 15 a day with a weekly reset, and their '
                              'reply-decay data from about 100K campaigns shows reply rates falling as '
                              'volume climbs: 12% on the first 50 connections, 6% on the next 100, 2% on '
                              'the next 200 [RYTMEUD8-FQ @ 00:01:40]. Their answer is 6 to 20 sender '
                              'accounts, a range they say gets the highest reply rates across all their '
                              'campaign data. Amon runs 100 to 200 requests per week, about 20 to 40 per '
                              'day, with the counter resetting Monday at 2 p.m. Pacific and a cap of 200 '
                              'actions per day; six accounts at 40 a day yields 240 daily or 1,200 weekly, '
                              'and accounts can be borrowed from friends, family or team members '
                              '[Cgx8HVnGOdY @ 00:53:13]. Cold accounts stay at 20 or fewer per day while '
                              "Amon's own runs 35 to 40. Aimfox pushes weekly interaction limits to "
                              '200/200 but keeps new or cold accounts at 100 or on the warm-up button '
                              '[O8VBEriCr60 @ 00:01:16], and lemlist defaults to 20 per day, with free '
                              'accounts at about 20 invites daily and paid accounts up to 30 [-LtGmHnpioI '
                              '@ 00:01:37].',
                              'Sequence mechanics are where the craft lives. Harry Long warms the prospect '
                              'first: view the profile, like a post the next day, connect the day after, '
                              'then layer personalization tokens and voice notes, either one recording '
                              "with tokens or a cloned voice, which Long credits with '10x' reply rates "
                              '[DgzklijTLzE @ 00:05:20]. Long also prefers a scorecard or quiz CTA over a '
                              "direct booking link, but says to test it. Amon's cadence after acceptance: "
                              "wait 1 day, send message 1; 2 days later ask 'is this a priority'; 4 days "
                              "after that send 'name?' or a micro case study; re-ping at 30 days; then "
                              "treat the lead as cold for 90 days, because 'the money is in the followup' "
                              "[Cgx8HVnGOdY @ 00:54:44]. HeyReach's lazy-booking playbook cuts it shorter, "
                              '1 to 2 follow-ups plus a humorous breakup message and no 7-step sequences '
                              '[5JAMkYMtvhw @ 00:06:29]. Matt Harriman runs day 1, a case study 2 days '
                              "later, then a one-line check-in 2 days after that, insisting 'you never say "
                              "just bumping this' and that the first message does most of the work "
                              '[hm5isqC1d74 @ 00:05:09].',
                              'The numbers that decide whether the machine pays come from testing and '
                              "pricing. Amon's benchmarks: about 30% acceptance on average, under 20% for "
                              'Ecom, 35 to 45% for SaaS and agencies; 1,000 requests yields about 300 '
                              'accepted, split 150/150 between variants, with about 100 messages enough to '
                              'call a winner; test the offer first, then the pain point, then the lead '
                              'source, and optimize for booked calls, not replies [Cgx8HVnGOdY @ '
                              "01:10:19]. Matt Harriman's inbox audit says at least 35% of interested "
                              'leads should book, and ten interested with one booking signals a problem '
                              '[hm5isqC1d74 @ 00:06:18]. On the sell side, Melvin Mendoza prices roofing '
                              'appointments at $250 each, adds $250 of free appointments for urgency, and '
                              'sells a six-pack for $2,000 up front with the cash funding ads, then '
                              'ascends buyers into 10, 20, 30 and 50-pack bundles to pull cash forward '
                              '[OJFNkb_PwS4 @ 00:08:15]. Tommy Chryst bills an AI voice speed-to-lead '
                              'build at $3,500 one-time or $400 a month with 250 minutes and $0.20 per '
                              'minute overage, and reports about $650K billed through Chat Dash '
                              '[YQbr_FhZTo8 @ 00:53:41].'],
               'table': {'caption': 'Street mechanics, settings and unit numbers practitioners run',
                         'headers': ['Mechanic',
                                     'Exact Setting or Number',
                                     'Execution Detail',
                                     'Expert Source'],
                         'rows': [['Weekly connection-request ceiling for a single LinkedIn account',
                                   'About 100 per week, roughly 10 to 15 per day',
                                   'Count resets weekly; add sender accounts to scale volume',
                                   'HeyReach ([5JAMkYMtvhw @ 00:07:28])'],
                                  ['Multi-account rotation math for scaling daily outbound volume',
                                   'Six accounts at 40 per day equals 240 daily',
                                   'Borrow accounts from friends, family or team members to stack',
                                   'HeyReach ([Cgx8HVnGOdY @ 00:53:13])'],
                                  ['Blank versus written connection request acceptance rate test',
                                   'Roughly 27% acceptance blank versus 22% with text',
                                   'Send blank through HeyReach or any tool for higher acceptance',
                                   'HeyReach ([Cgx8HVnGOdY @ 00:30:30])'],
                                  ["Post-engager lead import from a same-ICP creator's post",
                                   'About 700 leads pulled from a single post URL',
                                   'Paste URL to import likes, comments and reposts, then stack sources',
                                   'Aimfox ([O8VBEriCr60 @ 00:03:04])'],
                                  ['Follow-up cadence after a prospect accepts the connection',
                                   'Day 1, plus 2 days, plus 4 days, then 30',
                                   'Then treat the lead as cold for 90 days before re-contact',
                                   'HeyReach ([Cgx8HVnGOdY @ 00:57:07])'],
                                  ['AI message quality threshold before trusting automated copy at scale',
                                   'More than 10% needing manual fixes triggers prompt rework',
                                   'Send request with no pitch, then value message with one easy question',
                                   'HeyReach ([RYTMEUD8-FQ @ 00:05:37])'],
                                  ['Per-account pricing between two LinkedIn automation tools compared',
                                   '$59 per account Sendable versus $79 per account HeyReach',
                                   'Sendable offers a 7-day free trial and claims full stack replacement',
                                   'Sendable ([BWyoFA5VHTE @ 00:04:06])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Small Settings That Move Acceptance and Reply Rates',
                           'body': 'Four list and timing adjustments practitioners run before scaling '
                                   'sender accounts.',
                           'items': ["Turn on the 'posted on LinkedIn' filter in Sales Navigator; Amon "
                                     'says it lifts acceptance rates by 2 to 4X because requests reach '
                                     'people who actually use the platform and will see them [HeyReach — '
                                     'Cgx8HVnGOdY @ 00:24:08].',
                                     'Let location drive both send time and greeting, down to a '
                                     "'Buongiorno' opener for Italian prospects [HeyReach — 5JAMkYMtvhw @ "
                                     '00:01:20].',
                                     "Like and comment on a prospect's post the day before sending the "
                                     'request; lemlist reports an 18% acceptance lift [lemlist — '
                                     '-LtGmHnpioI @ 00:08:45].',
                                     'Validate company websites in Clay before launch, because 30% of any '
                                     'Sales Navigator list is inaccurate, if not more [Matt Harriman — '
                                     'hm5isqC1d74 @ 00:02:33].']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock the Offer and Build the List',
                              'action': 'Answer who to target, why they would talk, and what to say, then '
                                        "build a Sales Navigator list filtered on 'posted on LinkedIn'.",
                              'detail': 'Example filters: staffing and recruiting, 11 to 200 employees, '
                                        'United States, CEO/owner/founder/managing partner/managing '
                                        "director, plus 'posted on LinkedIn' [Matt Harriman — hm5isqC1d74 "
                                        '@ 00:02:10].'},
                             {'step': 2,
                              'title': 'Import and Clean Leads',
                              'action': 'Import by link from LinkedIn, Sales Navigator, Clay or HubSpot, '
                                        'then strip mismatches and prior contacts.',
                              'detail': 'Import takes about a minute; Claude connected to HeyReach removes '
                                        'mismatches and previously contacted leads are auto-excluded '
                                        '[HeyReach — 5JAMkYMtvhw @ 00:03:47].'},
                             {'step': 3,
                              'title': 'Build the Warm-Up Sequence',
                              'action': 'View profile, like a post the next day, send a blank connection '
                                        'request the day after, then message with tokens and voice notes.',
                              'detail': 'Sequence runs profile view, post like, then connect, with '
                                        'personalization tokens and voice notes layered after acceptance '
                                        '[Harry Long — DgzklijTLzE @ 00:05:20].'},
                             {'step': 4,
                              'title': 'Scale Senders and Triage the Inbox',
                              'action': 'Run 6 to 20 sender accounts, auto-stop on reply, and work '
                                        'AI-tagged replies in Unibox daily.',
                              'detail': 'AI tags replies as interested, generic or negative inside Unibox, '
                                        'with Claude integration drafting responses [HeyReach — '
                                        'RYTMEUD8-FQ @ 00:08:36].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Volume ceilings are where the operators split hardest. Harry Long hands the '
                              "throttle to HeyReach, which reads each account's LinkedIn and SSI score and "
                              'stays inside it, quoting roughly 45 connection requests a day and applying '
                              'the same logic to profile visits and messages [DgzklijTLzE @ 00:02:12]. '
                              "HeyReach's own booking playbook sets a tighter line of about 100 requests "
                              'per account per week, which it translates to 10 to 15 a day with a weekly '
                              'reset, and the answer to more volume is more sender accounts, not a hotter '
                              'single profile [5JAMkYMtvhw @ 00:07:28]. Aimfox pushes the other way: raise '
                              'weekly interaction limits to 200/200, then lean on free InMails once the '
                              '200 cap is hit, while keeping new or cold accounts at 100 or running the '
                              'warm-up button before maxing out [O8VBEriCr60 @ 00:01:16]. lemlist sits at '
                              'the conservative end with about 20 invites a day on free accounts, up to 30 '
                              'on paid, a default of 20, and a flat "Don\'t push more than that" '
                              '[-LtGmHnpioI @ 00:02:55]. In practice the same LinkedIn seat gets run '
                              'anywhere from 20 a day to 200 a week depending on whose stack is driving '
                              'it.',
                              "Connection notes split the room the same way. Amon's numbers in the "
                              'HeyReach masterclass show blank requests at about 27% acceptance versus 22% '
                              'with text, and he treats the blank request as the default [Cgx8HVnGOdY @ '
                              '00:30:30]. lemlist counters with acceptance by note type: compliments at '
                              '75%, simple networking at 60%, referrals at 50% or more, and attention or '
                              'ebook notes at 40%, plus a rule to skip the note entirely when you share '
                              'three to five mutual connections [-LtGmHnpioI @ 00:07:06]. The same '
                              'breakdown credits liking and commenting on a post the day before with an '
                              'extra 18% acceptance. That pre-warm logic is where Harry Long lands: view '
                              'the profile, like a post the next day, connect the day after, and send the '
                              'request blank because it spikes curiosity, while still telling operators to '
                              'test both versions [DgzklijTLzE @ 00:05:20]. Aimfox flips the order, '
                              'connecting first with no note and only reacting to a post with insightful '
                              'or celebration if the request sits unaccepted for a day, then running note '
                              'versus no note for about two weeks before deleting the loser and doubling '
                              'down on the winner [O8VBEriCr60 @ 00:05:50]. Every camp agrees on one '
                              'thing: no pitch inside the request.',
                              "Follow-up depth is the third fault line. HeyReach's booking playbook caps "
                              'the sequence at one or two follow-ups plus a humorous breakup message, says '
                              'never reword the first message, and tells operators to stop after the '
                              'second follow-up rather than build seven-step sequences [5JAMkYMtvhw @ '
                              '00:06:44]. Amon in the HeyReach masterclass runs a longer tail because, in '
                              'his words, the money is in the followup: message one after a one-day wait, '
                              'an "is this a priority" nudge two days later, a "name?" line or micro case '
                              'study four days after that, a re-ping at 30 days, then 90 days on ice as a '
                              'cold lead [Cgx8HVnGOdY @ 00:57:07]. Matt Harriman compresses it to day one, '
                              'a case study two days later, and a one-line check-in two days after that, '
                              'insisting the first message does most of the work and that you never say '
                              'just bumping this [hm5isqC1d74 @ 00:05:09]. Harry Long sits at the opposite '
                              "pole from HeyReach's own playbook, stacking many follow-up steps and "
                              'recording voice notes with personalization tokens or a cloned voice, which '
                              'he credits with 10x reply rates [DgzklijTLzE @ 00:09:01]. Inbox scope '
                              "splits too: in Long's HeyReach setup the Unibox shows campaign threads "
                              'only, while Aimfox pulls normal LinkedIn conversations into the same '
                              'inbox.'],
               'table': {'caption': 'Side-by-side playbook splits on volume, infrastructure, notes, '
                                    'sequencing, inbox, and appointment pricing',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Daily and weekly connection volume per account',
                                   "Long runs about 45 requests a day inside HeyReach's SSI-based safe "
                                   'limits',
                                   'lemlist caps free accounts near 20 invites a day and paid at 30',
                                   'Harry Long ([DgzklijTLzE @ 00:02:12]); lemlist ([-LtGmHnpioI @ '
                                   '00:01:37])'],
                                  ['Proxy and IP setup for automation tools',
                                   'Amon warns rotating proxies and VPNs get accounts banned; HeyReach '
                                   'uses a static residential IP',
                                   'lemlist says good tools delete cookies, rotate IP addresses, and match '
                                   'your location',
                                   'HeyReach ([Cgx8HVnGOdY @ 00:50:11]); lemlist ([-LtGmHnpioI @ '
                                   '00:02:55])'],
                                  ['Connection request with a note or sent blank',
                                   'Blank requests hit about 27% acceptance versus 22% for requests with '
                                   'text',
                                   'Compliment notes report 75%, networking 60%, referral 50% plus, ebook '
                                   '40%',
                                   'HeyReach ([Cgx8HVnGOdY @ 00:30:30]); lemlist ([-LtGmHnpioI @ '
                                   '00:07:06])'],
                                  ['Post engagement timing around the connection request',
                                   'Long views the profile, likes a post next day, connects the day after',
                                   'Aimfox reacts to one post only after a full day without acceptance',
                                   'Harry Long ([DgzklijTLzE @ 00:05:20]); Aimfox ([O8VBEriCr60 @ '
                                   '00:05:50])'],
                                  ['Follow-up sequence length after the request is accepted',
                                   'Stop after the second follow-up, add a humorous breakup, skip '
                                   'seven-step sequences',
                                   'Amon waits 1 day, then 2, then 4, then re-pings at 30 days',
                                   'HeyReach ([5JAMkYMtvhw @ 00:06:44]); HeyReach ([Cgx8HVnGOdY @ '
                                   '00:57:07])'],
                                  ['Unibox scope for daily reply management workflows',
                                   "Long's HeyReach Unibox shows campaign threads only, so replies get "
                                   'handled each morning',
                                   'Aimfox Unibox pulls in both Aimfox and normal LinkedIn conversations '
                                   'together',
                                   'Harry Long ([DgzklijTLzE @ 00:11:20]); Aimfox ([O8VBEriCr60 @ '
                                   '00:09:39])'],
                                  ['Appointment-setting pricing and who carries the risk',
                                   'ViB says pay per qualified appointment and start with a half-price '
                                   'trial campaign',
                                   'Mendoza sells a six-pack of roofing appointments for $2,000 up front '
                                   'into ads',
                                   'ViB ([w2J3Ou1jTR4 @ 00:03:46]); Melvin Mendoza ([OJFNkb_PwS4 @ '
                                   '00:08:15])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["Tommy Chryst's live voice-agent build doubles as a catalogue of wiring "
                              'misses: an agent left unpublished before assignment, a function missing '
                              'speak after execution, one webhook shared across functions when each needs '
                              'its own, and an agent asking broad availability questions instead of '
                              'proposing a specific time [YQbr_FhZTo8 @ 00:44:26]. He grinds through to V4 '
                              'in about 45 minutes, but he is clear the build is a V1 against an average '
                              'client project length of four to 12 weeks, and he even admits he is unsure '
                              'where the under-60-second response data comes from. On collections he is '
                              'blunt: clients who have not paid get locked out through Chat Dash billing. '
                              'Harry Long flags the automation trap on LinkedIn: a reply unenrolls the '
                              'prospect from the sequence, so somebody has to spend 10 to 15 minutes every '
                              'morning in the Unibox answering positive replies by hand [DgzklijTLzE @ '
                              '00:12:12]. Matt Harriman calls starting with LinkedIn itself the biggest '
                              'mistake, and pushes automation to the last step, after targeting, the '
                              'reason to talk, and the message are answered [hm5isqC1d74 @ 00:06:47]. '
                              "Genesys Digital's mortgage bot shows the other edge: it books the next "
                              "available slot with no human involvement, so the broker's only touchpoint "
                              'before the call is the emailed summary [I-riwAqQ3us @ 00:04:28].',
                              "Bad lists sink campaigns before a single message goes out. HeyReach's demo "
                              'names poor lists as a key reason campaigns fail and pushes qualified '
                              'imports plus exclusion of anyone already contacted [3o3gecljGlE @ '
                              '00:00:12]. Matt Harriman says 30% of any Sales Navigator list is '
                              'inaccurate, if not more, so he validates company websites in Clay before '
                              'anything gets sent, and he reminds operators that a $50,000 client only '
                              'needs the right 300 leads, not 10,000 [hm5isqC1d74 @ 00:02:33]. Amon caught '
                              'the same rot inside Sales Navigator filters: the personal-industry filter '
                              'matched only 125 of 281 leads, so he tells operators to skip it and lean on '
                              'account lists, headcount as a revenue proxy, and person location instead of '
                              "company HQ [Cgx8HVnGOdY @ 00:22:41]. HeyReach's booking playbook calls "
                              'title-only lists a mistake outright, because a job title at a 20-person '
                              'company means something completely different at a 500-person one, reports '
                              'reply rates moving from 20% to 40% once targeting was tightened, and says '
                              'getting prospecting right is more than half the job [5JAMkYMtvhw @ '
                              '00:01:04]. Skip the cleaning and every downstream metric, from acceptance '
                              'to booked calls, is measured on the wrong people.',
                              "The economics checks start with decay. HeyReach's 2026 strategy data from "
                              'about 100K campaigns shows reply rates of 12% on the first 50 connections, '
                              '6% on the next 100, and 2% on the next 200, and the same video calls raw '
                              'volume commoditized and points to signals like a new role seven to 10 '
                              'months in [RYTMEUD8-FQ @ 00:01:40]. Downstream, Matt Harriman wants at '
                              'least 35% of interested leads booking, and treats ten interested with one '
                              'booking as an inbox-management problem [hm5isqC1d74 @ 00:06:18]. On the buy '
                              'side, ViB warns that some providers bill per appointment set whatever the '
                              'quality and whether or not the lead shows, and that typical vendors stack '
                              'big onboarding fees, long-term contracts, and hourly or retainer billing '
                              'regardless of results; the counter is paying per qualified appointment and '
                              'starting with a trial campaign [w2J3Ou1jTR4 @ 00:03:46]. On the sell side, '
                              'Melvin Mendoza lists the prerequisites for pay-per-appointment as a good '
                              'market, dialed-in back-end systems, cheap cost per booked appointment, and '
                              'a willingness to eat the risk, and he cut the setter-to-closer handoff '
                              'because one side underperforming cascades into the other [OJFNkb_PwS4 @ '
                              '00:06:48]. His low-ticket offer keeps the scoreboard simple: cash collected '
                              'or not.'],
               'table': {'caption': 'Firsthand failure modes with the fix each practitioner applied',
                         'headers': ['Failure Mode',
                                     'What Went Wrong',
                                     'Practitioner Fix',
                                     'Expert Source'],
                         'rows': [['Voice agent never fires on live leads',
                                   'Agent was left unpublished before being assigned to the phone number',
                                   'Publish the agent first, then assign it and buy the 561 number',
                                   'Tommy Chryst ([YQbr_FhZTo8 @ 00:11:40])'],
                                  ['Booking functions collide during the live AI call',
                                   'One webhook was shared across check availability and calendar booking '
                                   'functions',
                                   'Give each custom function its own webhook and enable speak after '
                                   'execution',
                                   'Tommy Chryst ([YQbr_FhZTo8 @ 00:44:26])'],
                                  ['Positive replies silently drop out of the automation',
                                   'A reply unenrolls the prospect and the sequence stops sending entirely',
                                   'Block 10 to 15 minutes every morning to answer positive Unibox replies',
                                   'Harry Long ([DgzklijTLzE @ 00:12:12])'],
                                  ['Reply rates collapse as connection volume climbs',
                                   'Replies fall from 12% to 6% to 2% across successive connection tiers',
                                   'Score signals like new roles, hiring sprees, and recent funding before '
                                   'sending',
                                   'HeyReach ([RYTMEUD8-FQ @ 00:01:40])'],
                                  ['Interested leads that never convert into a booked call',
                                   'Ten interested leads producing one booking signals a broken inbox '
                                   'process',
                                   'Hold inbox management to at least 35% of interested leads booking',
                                   'Matt Harriman ([hm5isqC1d74 @ 00:06:18])'],
                                  ['Cold or new account banned after maxing out volume',
                                   'Cheap tools rotating proxies and VPNs, plus cold accounts sending at '
                                   'full volume',
                                   'Keep cold accounts at 20 or fewer daily on a static residential IP',
                                   'HeyReach ([Cgx8HVnGOdY @ 00:53:59]); Aimfox ([O8VBEriCr60 @ '
                                   '00:01:16])'],
                                  ['Paying for appointments that never show up or qualify',
                                   'Providers bill per appointment set whatever the quality or attendance',
                                   'Pay only per qualified appointment and run a small trial campaign '
                                   'first',
                                   'ViB ([w2J3Ou1jTR4 @ 00:03:46])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Launch Kill Switches',
                           'body': 'Four practitioner-tested checks to clear before any LinkedIn campaign '
                                   'or AI booking agent touches a live lead.',
                           'items': ['Do not launch until the offer is clear in 5 seconds, the targeting '
                                     'is right, and the first message starts a conversation instead of a '
                                     'lecture [Matt Harriman — hm5isqC1d74 @ 00:06:18].',
                                     'Run cold accounts at 20 or fewer connection requests a day before '
                                     'moving toward the 35 to 40 a day Amon runs on his own account '
                                     '[HeyReach — Cgx8HVnGOdY @ 00:53:59].',
                                     'If more than 10% of AI-written messages need manual fixes, stop and '
                                     'rework the prompt before sending more [HeyReach — RYTMEUD8-FQ @ '
                                     '00:05:37].',
                                     'Test every AI booking function end to end with a published agent, '
                                     'its own webhook per function, and a specific proposed time before a '
                                     'client lead hits it [Tommy Chryst — YQbr_FhZTo8 @ 00:44:26].']}}],
 'pull_quote': '"A $50,000 client doesn\'t need 10,000 leads, it only needs the right 300." — Matt '
               'Harriman (hm5isqC1d74 @ 00:01:31).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Build a Sales Navigator account list first, then search leads inside it using '
                      'person location and the posted on LinkedIn filter, and paste the search URL '
                      'straight into HeyReach [HeyReach — Cgx8HVnGOdY @ 00:15:14].',
                      'Validate company websites in Clay before launch, because roughly 30% of any Sales '
                      'Navigator list is inaccurate [Matt Harriman — hm5isqC1d74 @ 00:02:33].',
                      'Pull post engagers from a creator who targets your exact ICP by pasting the post '
                      'URL into Aimfox to import likes, comments, and reposts [Aimfox — O8VBEriCr60 @ '
                      '00:03:04].',
                      'Send the connection request blank, then a 3 to 5 sentence value-first first message '
                      'with no pitch and the smallest possible ask [HeyReach — 5JAMkYMtvhw @ 00:05:23].',
                      'Split 1,000 requests into variants of about 150 accepted each, decide on roughly '
                      '100 messages, and test offer first, then pain point, then lead source [HeyReach — '
                      'Cgx8HVnGOdY @ 01:10:19].',
                      'Fire an AI voice call within minutes of a form fill by POSTing name, phone, and '
                      'email in E.164 format to the outbound agent webhook [Tommy Chryst — YQbr_FhZTo8 @ '
                      '00:14:05].'],
 'statutory_citations': [{'title': 'HeyReach — How I made $5 Million with LinkedIn Outreach (1 Hour '
                                   'Masterclass) [00:49:13]',
                          'url': 'https://www.youtube.com/watch?v=Cgx8HVnGOdY&t=2953s',
                          'relevance': 'Primary practitioner testimony on connection request limits, '
                                       'account rotation, static residential IPs, and follow-up cadence.'},
                         {'title': 'HeyReach — The Laziest Way to Book Meetings on LinkedIn [00:06:44]',
                          'url': 'https://www.youtube.com/watch?v=5JAMkYMtvhw&t=404s',
                          'relevance': 'Primary practitioner testimony on short follow-up sequences, blank '
                                       'connection requests, and weekly sending limits.'},
                         {'title': 'Matt Harriman — The LinkedIn Outbound System That Actually Books '
                                   'Meetings (2026) [00:06:18]',
                          'url': 'https://www.youtube.com/watch?v=hm5isqC1d74&t=378s',
                          'relevance': 'Primary practitioner testimony on the outbound audit checklist and '
                                       'the 35% interested-to-booked benchmark.'},
                         {'title': 'Tommy Chryst — RAW Build: Complete AI Voice Agent Speed-to-Lead System '
                                   '[00:44:26]',
                          'url': 'https://www.youtube.com/watch?v=YQbr_FhZTo8&t=2666s',
                          'relevance': 'Primary practitioner testimony on AI voice agent build failures '
                                       'and webhook-per-function wiring.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'w2J3Ou1jTR4',
                       'title': 'Pay Per Appointment: The RIGHT Way To Do It For B2B Lead Generation',
                       'channel': 'ViB',
                       'author': 'ViB',
                       'text': 'This lets you book a handful of high quality meetings at half price.',
                       'tip': 'This lets you book a handful of high quality meetings at half price.',
                       'timestamp': 265,
                       'timestamp_seconds': 265,
                       'timestamp_label': '[00:04:25]',
                       'url': 'https://www.youtube.com/watch?v=w2J3Ou1jTR4&t=265s',
                       'markdown': '[00:04:25](https://www.youtube.com/watch?v=w2J3Ou1jTR4&t=265s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'OJFNkb_PwS4',
                       'title': 'How To Build A Low Ticket Sales Team (pay per appointment)',
                       'channel': 'Melvin Mendoza',
                       'author': 'Melvin Mendoza',
                       'text': 'I like to be at anywhere between 7 to 12 pitches a day for my team, and '
                               'then I need to make sure that each person is at least putting out three '
                               'offers a day.',
                       'tip': 'I like to be at anywhere between 7 to 12 pitches a day for my team, and '
                              'then I need to make sure that each person is at least putting out three '
                              'offers a day.',
                       'timestamp': 1281,
                       'timestamp_seconds': 1281,
                       'timestamp_label': '[00:21:21]',
                       'url': 'https://www.youtube.com/watch?v=OJFNkb_PwS4&t=1281s',
                       'markdown': '[00:21:21](https://www.youtube.com/watch?v=OJFNkb_PwS4&t=1281s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YQbr_FhZTo8',
                       'title': 'RAW Build: Complete AI Voice Agent Speed-to-Lead System',
                       'channel': 'Tommy Chryst',
                       'author': 'Tommy Chryst',
                       'text': 'Four to 12 weeks is my average project length.',
                       'tip': 'Four to 12 weeks is my average project length.',
                       'timestamp': 3121,
                       'timestamp_seconds': 3121,
                       'timestamp_label': '[00:52:01]',
                       'url': 'https://www.youtube.com/watch?v=YQbr_FhZTo8&t=3121s',
                       'markdown': '[00:52:01](https://www.youtube.com/watch?v=YQbr_FhZTo8&t=3121s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'I-riwAqQ3us',
                       'title': 'Mortgage Broker AI Appointment setter - Get Qualified Appointments On '
                                'Autopilot',
                       'channel': 'Genesys Digital',
                       'author': 'Genesys Digital',
                       'text': 'This is really important because there has been absolutely no human '
                               "interaction at this point from the mortgage broker's side.",
                       'tip': 'This is really important because there has been absolutely no human '
                              "interaction at this point from the mortgage broker's side.",
                       'timestamp': 268,
                       'timestamp_seconds': 268,
                       'timestamp_label': '[00:04:28]',
                       'url': 'https://www.youtube.com/watch?v=I-riwAqQ3us&t=268s',
                       'markdown': '[00:04:28](https://www.youtube.com/watch?v=I-riwAqQ3us&t=268s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KocD1S0Auvo',
                       'title': 'Set Up AI Agents for Faster Appointments',
                       'channel': 'Thelaywala',
                       'author': 'Thelaywala',
                       'text': 'Speed to lead matters when Facebook leads come in.',
                       'tip': 'Speed to lead matters when Facebook leads come in.',
                       'timestamp': 22,
                       'timestamp_seconds': 22,
                       'timestamp_label': '[00:00:22]',
                       'url': 'https://www.youtube.com/watch?v=KocD1S0Auvo&t=22s',
                       'markdown': '[00:00:22](https://www.youtube.com/watch?v=KocD1S0Auvo&t=22s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HeluxMYTT0o',
                       'title': 'AI Appointment Setting   The Future of Lead Gen for Marketing Agencies',
                       'channel': 'Zenscape',
                       'author': 'Zenscape',
                       'text': 'You want to contact your leads within 5 minutes.',
                       'tip': 'You want to contact your leads within 5 minutes.',
                       'timestamp': 415,
                       'timestamp_seconds': 415,
                       'timestamp_label': '[00:06:55]',
                       'url': 'https://www.youtube.com/watch?v=HeluxMYTT0o&t=415s',
                       'markdown': '[00:06:55](https://www.youtube.com/watch?v=HeluxMYTT0o&t=415s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RYTMEUD8-FQ',
                       'title': 'The Best AI LinkedIn Lead Generation Strategy for 2026',
                       'channel': 'HeyReach',
                       'author': 'HeyReach',
                       'text': "Across all our campaign data, that's the range that gets the highest reply "
                               'rates.',
                       'tip': "Across all our campaign data, that's the range that gets the highest reply "
                              'rates.',
                       'timestamp': 459,
                       'timestamp_seconds': 459,
                       'timestamp_label': '[00:07:39]',
                       'url': 'https://www.youtube.com/watch?v=RYTMEUD8-FQ&t=459s',
                       'markdown': '[00:07:39](https://www.youtube.com/watch?v=RYTMEUD8-FQ&t=459s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3o3gecljGlE',
                       'title': '10x Your LinkedIn Outbound With HeyReach [Demo Video]',
                       'channel': 'HeyReach',
                       'author': 'HeyReach',
                       'text': 'I recommend you go for the infinite login because it will give you maximum '
                               'performance.',
                       'tip': 'I recommend you go for the infinite login because it will give you maximum '
                              'performance.',
                       'timestamp': 12,
                       'timestamp_seconds': 12,
                       'timestamp_label': '[00:00:12]',
                       'url': 'https://www.youtube.com/watch?v=3o3gecljGlE&t=12s',
                       'markdown': '[00:00:12](https://www.youtube.com/watch?v=3o3gecljGlE&t=12s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'DgzklijTLzE',
                       'title': 'How I Automate My LinkedIn DM Outreach (Step By Step)',
                       'channel': 'Harry Long',
                       'author': 'Harry Long',
                       'text': 'So, you can just every morning put 10 to 15 minutes aside going through '
                               'your uni box and replying to the positive replies.',
                       'tip': 'So, you can just every morning put 10 to 15 minutes aside going through '
                              'your uni box and replying to the positive replies.',
                       'timestamp': 732,
                       'timestamp_seconds': 732,
                       'timestamp_label': '[00:12:12]',
                       'url': 'https://www.youtube.com/watch?v=DgzklijTLzE&t=732s',
                       'markdown': '[00:12:12](https://www.youtube.com/watch?v=DgzklijTLzE&t=732s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5JAMkYMtvhw',
                       'title': 'The Laziest Way to Book Meetings on LinkedIn',
                       'channel': 'HeyReach',
                       'author': 'HeyReach',
                       'text': 'Stop after the second follow-up.',
                       'tip': 'Stop after the second follow-up.',
                       'timestamp': 404,
                       'timestamp_seconds': 404,
                       'timestamp_label': '[00:06:44]',
                       'url': 'https://www.youtube.com/watch?v=5JAMkYMtvhw&t=404s',
                       'markdown': '[00:06:44](https://www.youtube.com/watch?v=5JAMkYMtvhw&t=404s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'O8VBEriCr60',
                       'title': 'The LinkedIn DM System That Gets Paying Clients in 2026 (Full Tutorial)',
                       'channel': 'Aimfox',
                       'author': 'Aimfox',
                       'text': 'Test it for about two weeks, see which one has better results, and then '
                               "you can go ahead and delete the one that doesn't work as well and double "
                               'down the one that does.',
                       'tip': 'Test it for about two weeks, see which one has better results, and then you '
                              "can go ahead and delete the one that doesn't work as well and double down "
                              'the one that does.',
                       'timestamp': 336,
                       'timestamp_seconds': 336,
                       'timestamp_label': '[00:05:36]',
                       'url': 'https://www.youtube.com/watch?v=O8VBEriCr60&t=336s',
                       'markdown': '[00:05:36](https://www.youtube.com/watch?v=O8VBEriCr60&t=336s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Cgx8HVnGOdY',
                       'title': 'How I made $5 Million with LinkedIn Outreach (1 Hour Masterclass)',
                       'channel': 'HeyReach',
                       'author': 'HeyReach',
                       'text': 'The money is in the followup.',
                       'tip': 'The money is in the followup.',
                       'timestamp': 3284,
                       'timestamp_seconds': 3284,
                       'timestamp_label': '[00:54:44]',
                       'url': 'https://www.youtube.com/watch?v=Cgx8HVnGOdY&t=3284s',
                       'markdown': '[00:54:44](https://www.youtube.com/watch?v=Cgx8HVnGOdY&t=3284s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Cgx8HVnGOdY',
                       'title': 'How I made $5 Million with LinkedIn Outreach (1 Hour Masterclass)',
                       'channel': 'HeyReach',
                       'author': 'HeyReach',
                       'text': 'Your LinkedIn Outreach is only as strong as your offer.',
                       'tip': 'Your LinkedIn Outreach is only as strong as your offer.',
                       'timestamp': 454,
                       'timestamp_seconds': 454,
                       'timestamp_label': '[00:07:34]',
                       'url': 'https://www.youtube.com/watch?v=Cgx8HVnGOdY&t=454s',
                       'markdown': '[00:07:34](https://www.youtube.com/watch?v=Cgx8HVnGOdY&t=454s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hm5isqC1d74',
                       'title': 'The LinkedIn Outbound System That Actually Books Meetings (2026)',
                       'channel': 'Matt Harriman',
                       'author': 'Matt Harriman',
                       'text': 'Something with LinkedIn Sales Navigator that you have to know is that 30% '
                               "of the list, doesn't matter what list, is always going to be inaccurate, "
                               'if not more.',
                       'tip': 'Something with LinkedIn Sales Navigator that you have to know is that 30% '
                              "of the list, doesn't matter what list, is always going to be inaccurate, if "
                              'not more.',
                       'timestamp': 153,
                       'timestamp_seconds': 153,
                       'timestamp_label': '[00:02:33]',
                       'url': 'https://www.youtube.com/watch?v=hm5isqC1d74&t=153s',
                       'markdown': '[00:02:33](https://www.youtube.com/watch?v=hm5isqC1d74&t=153s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-LtGmHnpioI',
                       'title': 'The Only LinkedIn Outreach Video You Will Ever Need',
                       'channel': 'lemlist',
                       'author': 'lemlist',
                       'text': "If you pitch in the connection request, you're dead.",
                       'tip': "If you pitch in the connection request, you're dead.",
                       'timestamp': 380,
                       'timestamp_seconds': 380,
                       'timestamp_label': '[00:06:20]',
                       'url': 'https://www.youtube.com/watch?v=-LtGmHnpioI&t=380s',
                       'markdown': '[00:06:20](https://www.youtube.com/watch?v=-LtGmHnpioI&t=380s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'BWyoFA5VHTE',
                       'title': 'The Best Heyreach Alternatives for LinkedIn Outreach Automation (2026)',
                       'channel': 'Sendable',
                       'author': 'Sendable',
                       'text': 'And finally, regarding the pricing, on Sendable we are at $59 per account '
                               "and on HeyReach it's $79 per LinkedIn account.",
                       'tip': 'And finally, regarding the pricing, on Sendable we are at $59 per account '
                              "and on HeyReach it's $79 per LinkedIn account.",
                       'timestamp': 246,
                       'timestamp_seconds': 246,
                       'timestamp_label': '[00:04:06]',
                       'url': 'https://www.youtube.com/watch?v=BWyoFA5VHTE&t=246s',
                       'markdown': '[00:04:06](https://www.youtube.com/watch?v=BWyoFA5VHTE&t=246s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kNseUbJwaA0',
                       'title': 'AI Sales Automation for B2B Teams: Lead Follow-Up, Quotes & Orders | '
                                'iTechnoLabs',
                       'channel': 'iTechnoLabs - Best App Development Company',
                       'author': 'iTechnoLabs - Best App Development Company',
                       'text': 'Nobody on your team has to follow up.',
                       'tip': 'Nobody on your team has to follow up.',
                       'timestamp': 34,
                       'timestamp_seconds': 34,
                       'timestamp_label': '[00:00:34]',
                       'url': 'https://www.youtube.com/watch?v=kNseUbJwaA0&t=34s',
                       'markdown': '[00:00:34](https://www.youtube.com/watch?v=kNseUbJwaA0&t=34s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'}]}
