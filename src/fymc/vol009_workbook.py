from __future__ import annotations

def build_volume_009_workbook() -> dict:
    return {'workbook_id': 'wb-009-million-dollar-lead-generation',
 'volume_id': 'vol-009-million-dollar-lead-generation',
 'title': 'Million-Dollar Lead Generation — Practitioner Testimony Operator Workbook',
 'subtitle': 'Field worksheets for defining the buyer by the pain you fix, building the account-based '
             'operating system, running warm enterprise plays, wiring signal-led outbound, publishing '
             'executive thought leadership, and sourcing proprietary M&A deal flow',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Buyer Definition and the ABM Operating System',
                 'purpose': 'Define the buyer by the pain you fix, cut the market down to accounts with '
                            'active, budgeted, urgent pain, and decide whether a joint sales-and-marketing '
                            'ABM operating system fits your deal size before spending on campaigns, lists, '
                            'or advertising.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Start from the problem and the outcome, never from the product or a job '
                                  "title, and write every answer in the buyer's own words.",
                                  'Apply company-level filters before persona work, then score open deals '
                                  'so the scorecard actually disqualifies pipeline instead of validating '
                                  'it.',
                                  'Keep lists small and segmented: hold segments to manageable sizes, '
                                  'contact more than one person per account, and cap daily sends per box.',
                                  'Test ABM fit against contract value, CFO sign-off, and list length, and '
                                  'walk away when any walk-away condition applies.',
                                  'Review progress weekly at the account level with sales and marketing '
                                  'together, and diagnose every stall as either a distribution or a '
                                  'content problem.'],
                 'fields': [{'name': 'problem_statement',
                             'type': 'textarea',
                             'prompt': "Write the core problem your offer fixes in the buyer's own "
                                       'language, not as a product feature or job title. Name the '
                                       'measurable burden, such as tools juggled or hours lost each month, '
                                       'and state who carries it daily.',
                             'example': 'A social-reporting SaaS stopped targeting a job title and '
                                        "redefined its buyer as someone 'juggling 10 tools… 20 hours a "
                                        "month.' The product did not change; the definition of who needed "
                                        'it did. That shift produced a reported 32% conversion lift and a '
                                        '20% shorter sales cycle [OGONJO Workbooks — ZSqgCrydlAo @ '
                                        '00:04:50].'},
                            {'name': 'five_whys_chain',
                             'type': 'textarea',
                             'prompt': "Run the Five Whys on your problem statement. Ask 'why does that "
                                       "matter?' five times in sequence, record each answer on its own "
                                       'line, and stop only when you reach the emotional reason the buyer '
                                       'will finally act.',
                             'example': 'Why 1: the team juggles 10 tools. Why 2: reports take 20 hours a '
                                        'month. Why 3: those hours come out of client work. Why 4: '
                                        'deadlines slip. Why 5: the manager looks unprepared in front of '
                                        'leadership. That last answer is the emotional trigger to build '
                                        'messaging on [OGONJO Workbooks — ZSqgCrydlAo @ 00:08:35].'},
                            {'name': 'company_level_icp_filter',
                             'type': 'textarea',
                             'prompt': 'List the company-level filters that must be true before any '
                                       'persona work begins. Include the pain signal, budget evidence, and '
                                       'urgency marker for each filter, and explain why you are not '
                                       'jumping straight into personas or titles.',
                             'example': "Myk Pono warns that 'very often companies just jump in to create "
                                        "personas and an ideal customer profile, and I think it's wrong' "
                                        '[Myk Pono — Y1u-ngsyH60 @ 00:00:47]. Filter first: active pain, '
                                        'budget, urgency. Only accounts passing all three move to persona '
                                        'mapping. Note that revenue data is unreliable for companies that '
                                        'do not publish it [Hunter — 35H3HVb8ymw @ 00:28:02].'},
                            {'name': 'icp_scorecard_criteria',
                             'type': 'textarea',
                             'prompt': 'Define 5 to 7 scorecard criteria for your ICP, assign each a point '
                                       'value, and set the cutoff score. Then run the scorecard against '
                                       'every open deal and record what percentage falls below the cutoff '
                                       'and gets disqualified.',
                             'example': 'Score 5 to 7 criteria and expect to disqualify 20 to 30% of open '
                                        'deals. If the scorecard cuts nothing, it is validating pipeline '
                                        'rather than filtering it. A strong ICP shows roughly a '
                                        'three-times win-rate gap between high and low scorers, so check '
                                        'both bands against closed outcomes [OGONJO Workbooks — '
                                        '4S63IHiDhTk @ 00:07:53].'},
                            {'name': 'list_size_and_segmentation',
                             'type': 'textarea',
                             'prompt': 'State your total target list size and how you will split it. Name '
                                       'the one or two levers used to segment, the size of each segment, '
                                       'and the daily sending cap per box you will enforce from day one.',
                             'example': 'Never push one message to a 10,000-lead list. Split it into 10 '
                                        'segments of 1,000 using one or two levers and keep each sending '
                                        'box at 50 or fewer per day [Hunter — 35H3HVb8ymw @ 00:48:20]. '
                                        'Lists of 100 leads or fewer more than double replies across 31M '
                                        'outreach emails [Hunter — 35H3HVb8ymw @ 00:09:28].'},
                            {'name': 'multi_contact_plan',
                             'type': 'textarea',
                             'prompt': 'For each target company, list every person you will email, their '
                                       'role, and the personalized element in each message body. Explain '
                                       'how editing templates and body-level personalization will differ '
                                       'between contacts at the same target account.',
                             'example': 'Email more than one person per target company: outreach data '
                                        'shows almost +50% replies, and editing templates plus body '
                                        'personalization adds about another +50% [Hunter — 35H3HVb8ymw @ '
                                        '00:10:21]. Timing also matters, since only 2-8% of a market is '
                                        'actively looking at any time, so hiring and funding signals guide '
                                        'who gets contacted first [Hunter — 35H3HVb8ymw @ 00:29:38].'},
                            {'name': 'route_to_market',
                             'type': 'textarea',
                             'prompt': 'Choose your route to market: sales-led, marketing-led, or a '
                                       'federal notice-and-teaming path. Justify the choice with your '
                                       'customer lifetime value and deal size, and note any partner rates '
                                       'or gap-analysis scores that must be settled first.',
                             'example': 'Prairie Founders Club draws the sales-led versus marketing-led '
                                        'line at $10K LTV. On the federal path, prime a bid only when the '
                                        'requirements gap analysis averages 4, and talk rates before '
                                        'signing the teaming agreement, because a partner charging $200 '
                                        'against your $100 breaks the bid [Neil McDonnell — d_oQ5UhlC0k @ '
                                        '00:24:39].'},
                            {'name': 'abm_fit_gate',
                             'type': 'text',
                             'prompt': 'Record your average contract value, whether CFO sign-off is '
                                       'required, and your planned account count. State plainly whether '
                                       'the program clears the ABM entry floor or whether self-service, '
                                       'low-ticket economics make ABM overkill for your business.',
                             'example': 'An account requiring CFO sign-off clears the roughly $20,000 ACV '
                                        'floor [AdConversion — FPPnVM3_KPk @ 00:18:13]. Walk away if ACV '
                                        'sits below 30K, the team chases MQLs, the list is 1,000 accounts, '
                                        'or leadership expects $1M in 30 days [Fullfunnel io — glV72-awJAU '
                                        '@ 01:17:37]. Self-service credit-card SaaS where users just sign '
                                        'up and swipe a card may find ABM overkill.'},
                            {'name': 'abm_sequence_and_air_cover',
                             'type': 'textarea',
                             'prompt': 'Map your ABM operating sequence from ICP through messaging, a '
                                       'Dream 100, personalization, and sales outbound. Name the paid and '
                                       'organic air cover running underneath, and describe how pre-SDR '
                                       'campaigns are timed before the first rep touch lands.',
                             'example': 'Fire pre-SDR campaigns 2 days to 2 weeks before outreach; at one '
                                        'CPG client this lifted connect rates, meetings and target account '
                                        'pipeline [LinkedIn for Marketing — Co22pd-mVlk @ 01:00:37]. Do '
                                        'not run demo ads at accounts that do not know who you are '
                                        '[AdConversion — FPPnVM3_KPk @ 00:01:12]. Answer the top 10 sales '
                                        'objections with targeted ads [AdConversion — FPPnVM3_KPk @ '
                                        '00:06:48].'},
                            {'name': 'weekly_account_review',
                             'type': 'textarea',
                             'prompt': 'Describe the weekly account-level meeting where sales and '
                                       'marketing review progress together. List who attends, which '
                                       'metrics you review, and the red flags that trigger a diagnosis of '
                                       'distribution problems versus content problems before the pilot '
                                       'stalls.',
                             'example': "Treat sales saying 'not sure' at two months as a red flag. "
                                        'Diagnose no impressions as a distribution problem and no '
                                        'engagement as a content problem [AdConversion — LbEgZ7SpArs @ '
                                        '00:08:08]. Never ask for a budget increase to rescue a weak '
                                        "pilot, because that 'puts the gun in front of your head' "
                                        '[Fullfunnel io — glV72-awJAU @ 01:23:19].'}],
                 'completion_gate': 'Complete only when the problem statement survives the Five Whys, the '
                                    'scorecard disqualifies 20 to 30% of open deals with roughly a '
                                    'three-times win-rate gap, no segment exceeds 1,000 leads, each '
                                    'sending box stays at 50 or fewer per day, and ACV clears the ABM '
                                    'floor.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Enterprise Account Plays and Signal-Led Outbound',
                 'purpose': 'Size enterprise plays to deal value and rep capacity, run warm gifting and '
                            'one-to-one experiences with tracked follow-up, and build a signal-led '
                            'outbound engine in Clay where timing beats targeting and targeting beats '
                            'copy.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Confirm the deal-size floor and rep capacity before choosing any '
                                  'account, gift, or executive experience.',
                                  'Warm every account or confirm intent before a gift ships, and tie each '
                                  'send to automated follow-up and a BDR cadence.',
                                  'Pick narrow timing signals with a specific role, event, and window '
                                  'rather than static wide-net lists.',
                                  'Build the enrichment waterfall with run conditions, an LLM relevance '
                                  'filter, and clear routing destinations for every qualified lead.',
                                  'Protect credits and keys: test small, confirm every spend, and never '
                                  'scale an untested update.'],
                 'fields': [{'name': 'deal_size_floor',
                             'type': 'text',
                             'prompt': 'Write the minimum annual deal value that justifies an enterprise '
                                       'account play in your business. Explain how that floor carries the '
                                       'cost of gifting, direct mail, and one-to-one experiences, and '
                                       'which accounts fall below it today.',
                             'example': 'Practitioners set the floor anywhere from roughly $10K a year to '
                                        'deals of 50,000-100,000 or more. You do not need a robust ABM '
                                        'platform to start, nor 60, 80 or 100,000 a year in software '
                                        '[Growth Business Templates — aDOxVzIz_Hk @ 00:08:42]. Spread your '
                                        'risk and run ABM on three accounts first [Growth Manifesto '
                                        'Podcast — Vdq5ROPgQzw @ 00:19:28].'},
                            {'name': 'rep_capacity_list_sizing',
                             'type': 'text',
                             'prompt': 'Calculate how many target accounts your sales team can genuinely '
                                       'work. Record accounts per rep, the share selected for enterprise '
                                       'plays, and the total list size, treating rep capacity rather than '
                                       'marketing ambition as the deciding factor.',
                             'example': "Snowflake's Casey Patterson targets 10 of a rep's 100 accounts. "
                                        'The sales team is the bottleneck and the deciding factor on '
                                        'account count [Exit Five — uWRminjpXsE @ 00:40:10]. For '
                                        'one-to-one executive experiences, build the list at 2-3x the '
                                        'desired contact count, since 11 of 30 contacts became meetings '
                                        '[Steve Armenti — Mv1ZTzPcy5A @ 00:07:56].'},
                            {'name': 'warm_signal_before_gift',
                             'type': 'textarea',
                             'prompt': 'For every account slated to receive a gift or direct mail, record '
                                       'the warming touch or confirmed intent signal that came first. '
                                       'Accounts with no prior engagement or intent evidence must be '
                                       'pulled from the send list before anything ships.',
                             'example': 'No gift goes to a cold account as the first touch; warm the '
                                        'account or confirm intent first [B2B Fusion — 4kdiiYL17XU @ '
                                        "00:23:20]. Rocket SaaS is blunt: 'I wouldn't do a cold direct "
                                        "mail campaign' [Rocket SaaS — 5XU6PUsdwEM @ 00:40:07]. Armenti "
                                        "adds that experience recipients 'aren't like hand-raisers,' so "
                                        'the research has to earn attention.'},
                            {'name': 'five_to_nine_research',
                             'type': 'textarea',
                             'prompt': "Research each priority buyer's 'five to nine,' meaning what they "
                                       'care about outside work. Record the source of that insight, the '
                                       'gift or experience matched to it, and any seasonal or practical '
                                       'risk that could spoil the send.',
                             'example': "Gift to the buyer's passions outside work, not to the job title "
                                        "[B2B Fusion — 4kdiiYL17XU @ 00:20:55]. Armenti's "
                                        'agent-researched, human-validated offers included a private chef, '
                                        'a yoga retreat and golf [Steve Armenti — Mv1ZTzPcy5A @ 00:07:56]. '
                                        "Check practical risks too: 'you shouldn't send chocolate in the "
                                        "summer' [AI Marketers Guild — v0lXcZYhFXc @ 00:42:06]."},
                            {'name': 'send_and_follow_up_trigger',
                             'type': 'textarea',
                             'prompt': 'Document exactly how the offer is sent and what follows it. Name '
                                       'the sending inbox, the automated marketing follow-up, and the BDR '
                                       'cadence steps tied to ship, deliver, and landing-page visit events '
                                       'for every recipient on the list.',
                             'example': "Send manually from the rep's or an executive's own inbox, not a "
                                        "sequencer; Armenti's opens and engagement ran above 50% [Steve "
                                        "Armenti — Mv1ZTzPcy5A @ 00:08:16]. Wrike's locked acrylic candy "
                                        'box triggered BDR outreach on ship, deliver and visit events, and '
                                        'at least 41% clicked to learn more [AI Marketers Guild — '
                                        'v0lXcZYhFXc @ 00:28:14].'},
                            {'name': 'phone_list_scoring',
                             'type': 'textarea',
                             'prompt': 'Describe how you will score and prioritize your phone list before '
                                       'dialing. Record the starting list size, the scoring method, the '
                                       'conversation rate before and after scoring, and how anyone who '
                                       'answered once gets moved into a priority callback bucket.',
                             'example': 'Ronen Pessar re-scored a 2,245-number list with Phone Ready '
                                        'Leads, now TitanX, and conversations rose from 1.6% (1 per 60 '
                                        'dials) to 39.6% (21 from 53 dials) [Ronen Pessar — dpDcjwreO8o @ '
                                        '00:08:10]. Anyone who answered once goes into a priority callback '
                                        'bucket, where 20-40% convert [Ronen Pessar — dpDcjwreO8o @ '
                                        '00:09:06].'},
                            {'name': 'signal_trigger_definition',
                             'type': 'textarea',
                             'prompt': 'Define the narrow timing signal that will trigger outreach, '
                                       'including the exact role, event, and time window. Explain why it '
                                       'beats a static wide-net list and whether the signal is overused by '
                                       'competitors already targeting the same accounts.',
                             'example': 'One client targeting US companies with 50-500 employees switched '
                                        "from a static list to 'hired head of data in last 90 days' and "
                                        'replies moved from about 1% to 11% with the same offer [Hlib '
                                        'Storchak — Iy92NakD7e4 @ 00:08:25]. Wide-net lists of 10,000+ '
                                        'contacts stall at 2-4% while spearhead campaigns hit 15-25% [Hlib '
                                        'Storchak — Iy92NakD7e4 @ 00:02:00].'},
                            {'name': 'clay_enrichment_waterfall',
                             'type': 'textarea',
                             'prompt': 'Map your Clay enrichment build step by step: tiered dream '
                                       'accounts, signal tables, the LLM relevance filter, the email and '
                                       'mobile waterfall providers in order, and the destination each '
                                       'qualified lead routes to after enrichment completes.',
                             'example': 'One email provider found 5 of 10 CEO emails; the full waterfall '
                                        'found 9 or 10 of 10 [GTM Partner — NCH5pSCJcCU @ 00:06:28]. Set '
                                        "run conditions so 'if it finds the emails with this provider then "
                                        "it's not going to run the rest' [James Praise #realjaymes — "
                                        'S9IhjTPQRTA @ 00:05:42]. Route results to Slack, Smartlead, '
                                        'Instantly or HeyReach.'},
                            {'name': 'archetype_reason_timestamp',
                             'type': 'textarea',
                             'prompt': 'For each lead entering outreach, record its archetype, the reason '
                                       'it qualifies, and the timestamp of the triggering signal. Set the '
                                       'archetype threshold that must be reached before outreach fires, '
                                       'and describe how irrelevant signal articles are filtered out.',
                             'example': "'If a lead doesn't have an archetype, plus a reason, plus a time "
                                        "stamp, it doesn't get touched' [Blue Pencil — 5CV9o_tOrgg @ "
                                        '00:05:41]. Run an LLM relevant-or-not checkbox and a why-relevant '
                                        'briefing on every Clay Signals article before it reaches an AE '
                                        'Slack channel, because these plays carry heavy noise [GTM Partner '
                                        '— NCH5pSCJcCU @ 00:03:23].'},
                            {'name': 'credit_and_safety_controls',
                             'type': 'textarea',
                             'prompt': 'List the controls protecting your enrichment budget and data '
                                       'security. Note how every credit spend gets confirmed, how many '
                                       'records you test before scaling an update, where tone and banned '
                                       'words are configured, and how API keys stay hidden.',
                             'example': 'Confirm every credit spend through the Apollo MCP and never run '
                                        'an untested update at scale [ColdIQ — lSM-6GschOc @ 00:25:44]. '
                                        'Fill the Apollo AI Context Center with tone and banned words, the '
                                        'setting operators most often forget [ColdIQ — lSM-6GschOc @ '
                                        '00:13:32]. Keep API keys off screen when recording or sharing '
                                        'workflows [Cold Outbound Clips — _l5HU1yQjdM @ 00:01:26].'}],
                 'completion_gate': 'Complete only when every target account has a warming touch logged, '
                                    'the list is sized to rep capacity, every send has a ship, deliver, '
                                    'and visit-triggered BDR cadence, every lead carries an archetype, '
                                    'reason, and timestamp, and every credit-spending update has passed a '
                                    'small test.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Thought Leadership, Podcast Business Development, and Proprietary M&A Sourcing',
                 'purpose': "Extract the principal's point of view live, publish it consistently so "
                            'content pre-sells deals, open executive doors through podcast invitations, '
                            'and build a verified, scored outbound machine for proprietary M&A deal flow '
                            'that replaces Rolodex and referral dependence.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ["Extract the executive's point of view on a live call before any post "
                                  'goes out under their name.',
                                  'Hold a steady publishing cadence for six months and report qualified '
                                  'leads and revenue, not likes.',
                                  'Apply hard kill rules to thought leader ads and vet every paid podcast '
                                  'slot before money moves.',
                                  'Define acquisition criteria, verify every lead, re-verify catch-alls, '
                                  'and cut low-scoring targets before a single email is sent.',
                                  'Route every reply through an intent screen and a CRM before it ever '
                                  'reaches the closer.'],
                 'fields': [{'name': 'executive_pov_extraction',
                             'type': 'textarea',
                             'prompt': 'Schedule and document the live extraction session with your '
                                       'principal. Record the date, length, and cadence of each session, '
                                       'the strongest point of view captured, and the proprietary data or '
                                       'customer conversation that backs it up.',
                             'example': 'Run a 45-minute extraction every six weeks, and never publish '
                                        "under the executive's name until insights are pulled on a live "
                                        'call; anything else is guessing [Social-Hire.com — VesCkYBJkFA @ '
                                        "00:01:04]. Concurate gets on a call 'every week to hear what's "
                                        "coming up in a customer conversation' [Concurate — 3_gHjeAdeNE @ "
                                        '00:01:03].'},
                            {'name': 'idea_mining_sources',
                             'type': 'textarea',
                             'prompt': 'List where your post ideas come from each week. Record the comment '
                                       'threads you mine, the strategic comments you leave before posting, '
                                       'your daily connection-request target, and which proprietary data '
                                       'supports each point of view you publish.',
                             'example': 'Comments produce 3x more ideas than brainstorming, and '
                                        'proprietary data should back each POV [ZenPilot — -zNdXXrY9lU @ '
                                        '00:33:17]. Strategic comments likely earn more exposure than your '
                                        'own posts, paired with 10 connection requests a day [Impactable - '
                                        'B2B LinkedIn Ads Agency — s0wOPmHvpWM @ 00:14:20]. Less than 2% '
                                        'of LinkedIn members post at all [Executive Resume Writers — '
                                        'Vi-DPWAY1C0 @ 00:01:36].'},
                            {'name': 'publishing_cadence',
                             'type': 'text',
                             'prompt': 'Set your publishing cadence for the next six months. State posts '
                                       'per week, lead magnets per week, and the minimum consistency you '
                                       'will hold, explaining how you will avoid short bursts of activity '
                                       'followed by long silences.',
                             'example': 'Operators run four posts weekly and two lead magnets per client '
                                        "per week. Justin Row says it is 'way better for you to post once "
                                        "or twice a week consistently for 6 months' than to go crazy for "
                                        'three or four weeks and drop off the map [Impactable - B2B '
                                        'LinkedIn Ads Agency — s0wOPmHvpWM @ 00:13:43].'},
                            {'name': 'dm_ladder',
                             'type': 'textarea',
                             'prompt': 'Write the direct-message ladder that follows engagement with your '
                                       'content. Draft each of the three to five messages, state the '
                                       'trigger that starts the sequence, and describe how you move a warm '
                                       'prospect toward a booked call.',
                             'example': 'Run three-to-five-message DM ladders off content engagement, and '
                                        "remember 'you nurture enough relationships and conversions "
                                        "happen' [ZenPilot — -zNdXXrY9lU @ 00:22:52]. Prospects exposed to "
                                        'thought leadership before booking arrive 60 or 70% sold at the '
                                        'first sales call [Impactable - B2B LinkedIn Ads Agency — '
                                        's0wOPmHvpWM @ 00:07:22], so the ladder should invite '
                                        'conversation, not pitch.'},
                            {'name': 'thought_leader_ad_kill_rule',
                             'type': 'text',
                             'prompt': 'Define the click-through and landing-page thresholds that keep a '
                                       'thought leader ad running. Record current CTR, the share of social '
                                       'actions that become landing-page clicks, and the exact rule you '
                                       'apply to kill underperforming ads each week.',
                             'example': 'Adam Holmgren reports thought leader ads at 13% or more CTR '
                                        'versus about 1% for image ads, credited with 300+ customers in 15 '
                                        'months [Adam Holmgren — eFSMGI_UK38 @ 00:00:14]. Kill any ad '
                                        'under 10% CTR or where landing-page clicks fall below 10% of '
                                        'social actions [Adam Holmgren — eFSMGI_UK38 @ 00:11:39].'},
                            {'name': 'results_reporting',
                             'type': 'textarea',
                             'prompt': 'Choose the business metrics you will report before raising cadence '
                                       'or budget. List net-new ICP engagement, qualified leads, clients, '
                                       'and recurring revenue tied to content, and explain why likes and '
                                       'impressions alone will not justify more spend.',
                             'example': 'Report net-new ICP engagement, qualified leads and MRR, not likes '
                                        "[ZenPilot — -zNdXXrY9lU @ 00:15:15]. Garret Caudle's best founder "
                                        'POV post earned 64,000 impressions and 623 likes, but the number '
                                        'that mattered was 10+ qualified leads, 3 clients and over $20k '
                                        'MRR [ZenPilot — -zNdXXrY9lU @ 00:17:16]. ZenPilot adds that the '
                                        'CEO should not manage their own LinkedIn account.'},
                            {'name': 'podcast_trojan_horse',
                             'type': 'textarea',
                             'prompt': 'Design your podcast-led business development play. List the ICP '
                                       'executives you will invite, how you will find them through '
                                       'conference credentials or attendee lists, who receives the pitch, '
                                       'and how each paid slot gets vetted before money moves.',
                             'example': 'Podcast invites to ICP executives draw 25 to 45% responses versus '
                                        '1 to 3% for cold email [Dylan Conroy — yja0j6pWgP0 @ 00:20:04]. '
                                        'Use conference press credentials and Vendelux attendee lists, and '
                                        'pitch comms or PR people instead of the executive [Dylan Conroy — '
                                        'ttPyddAq19E @ 00:20:41]. Vet paid slots with the STAGE score and '
                                        'a 30-day posting check.'},
                            {'name': 'acquisition_criteria_and_list',
                             'type': 'textarea',
                             'prompt': 'Write your acquisition criteria or total addressable market '
                                       'definition for proprietary deal sourcing. Record sector, size, and '
                                       'geography filters, the raw lead count pulled, the verified '
                                       'sendable count after catch-all re-verification, and the AI score '
                                       'cutoff applied.',
                             'example': "Do not launch on raw counts: Nico Holloman's 6,000-lead pull "
                                        'shrank to 1,324 sendable leads after verification and '
                                        're-verifying catch-alls [Nico Holloman | Hologram Agency — '
                                        "PauebGoMxEw @ 00:09:52]. 'Anyone who's under a five out of 10 "
                                        "gets automatically cut from the list' [Nico Holloman | Hologram "
                                        'Agency — PauebGoMxEw @ 00:08:17].'},
                            {'name': 'outreach_angle_and_inbox',
                             'type': 'textarea',
                             'prompt': 'Draft your outbound angle for owners and the inbox you will '
                                       'target. Name the hook, such as a past closed deal or market '
                                       'interest, the first-line personalization, the compliance footer, '
                                       'and whether generic company inboxes beat named executive '
                                       'addresses.',
                             'example': "Peakstone's Schmidt Electric to MC Corp deal anchored a campaign "
                                        'the agency never held, booking $15M, $25M and $30M companies '
                                        'within seven days at around 1% replies [Ephraim Austin — '
                                        'esA2m5IlLT8 @ 00:01:39]. For blue-collar targets, email the '
                                        'generic inquiry inbox [Willem — Gi8lgR2IK40 @ 00:03:39]. Add an '
                                        'opt-out and signature under CAN-SPAM.'},
                            {'name': 'reply_screen_and_crm',
                             'type': 'textarea',
                             'prompt': 'Describe how replies are screened and tracked before reaching the '
                                       'closer. Name the CRM holding every opportunity, the behavioral '
                                       'triggers that create sales tasks, and the email or short screener '
                                       'call used to confirm real intent to sell.',
                             'example': 'Screen every reply for real intent to sell, by email or a hired '
                                        '10-minute screener call, before it reaches the closer [Willem — '
                                        'Gi8lgR2IK40 @ 00:10:10]. No CRM, no campaign: one CRM-less client '
                                        'turned 400+ opportunities into zero closings [Exxcelerate — '
                                        'TE99yv49oy4 @ 00:25:56]. Repeat visits to a sell-a-business page '
                                        'should fire sales tasks automatically.'}],
                 'completion_gate': 'Complete only when every published insight comes from a live '
                                    'extraction call, thought leader ads clear 10% CTR with landing-page '
                                    'clicks at 10% of social actions, every M&A target scores 5 or above '
                                    'after verification, and a CRM is live before the first send.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Deal Process Control and Solar Appointment Flow',
                 'purpose': 'Turn an M&A opportunity into a controlled competitive process with protected '
                            'LOI terms, verified fees and tested earnout math, then apply the same '
                            'discipline to solar lead flow so every appointment is exclusive, qualified '
                            'and likely to show.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Start with the buyer funnel and hold every stage to written bid '
                                  'instructions and buyer-only deadlines, even when only one serious buyer '
                                  'remains at the table.',
                                  'Lock escrow, R&W insurance, caps and baskets into the LOI before '
                                  'accepting exclusivity, a no-shop clause or a notice duty that ends your '
                                  'competitive leverage.',
                                  'Run a worked fee calculation and answer the four earnout questions in '
                                  'writing before any adviser engagement letter or earnout clause is '
                                  'signed.',
                                  'Rebuild your solar acquisition math from cost per lead to cost per '
                                  'customer, and reject any vendor that cannot state fall-off percentages '
                                  'and lead exclusivity.',
                                  'Complete the site-visit checklist on every commercial lead and the '
                                  'show-rate plan on every residential booking before you scale spend or '
                                  'add lead sources.'],
                 'fields': [{'name': 'buyer_funnel_targets',
                             'type': 'textarea',
                             'prompt': 'Write the sell-side funnel targets for your next mandate: how many '
                                       'buyers you will contact, how many signed NDAs you expect, how many '
                                       'IOIs, approved bidders and final bids, and the four-to-eight-month '
                                       'calendar you will hold every stage against.',
                             'example': 'Distribute to 35 PE firms plus 8 strategics, aiming for 30-50 '
                                        'signed NDAs. Treat 10 IOIs from 50 NDAs as a really good day '
                                        '[POTOMAC M&A — 8jBQ3jZnNvY @ 00:39:45]. Cut to 5 approved '
                                        'bidders, then 3 final bids, with one winner by month seven. Every '
                                        'stage gets written bid instructions and a buyer-only deadline, '
                                        'never a seller deadline.'},
                            {'name': 'single_buyer_process',
                             'type': 'textarea',
                             'prompt': 'Describe how you will run the process if only one serious buyer '
                                       'shows up. List the bid instructions, iterative stages and '
                                       'deadlines you will keep identical to a multi-buyer auction so the '
                                       'buyer cannot read a thin field from your behavior.',
                             'example': 'One strategic acquirer remains after round one. Keep the same bid '
                                        'template, the same first-round and final-round stages and a '
                                        'Friday deadline, because sophisticated buyers read the field from '
                                        'how you act, not from what you say [POTOMAC M&A — f7d2hP31YB8 @ '
                                        '00:06:09]. Leverage factors such as their time pressure get '
                                        'gathered over dinner first [POTOMAC M&A — f7d2hP31YB8 @ '
                                        '00:12:43].'},
                            {'name': 'loi_protection_terms',
                             'type': 'textarea',
                             'prompt': 'List the LOI terms you will require before signing or '
                                       'countersigning: escrow amount, R&W insurance, indemnity caps and '
                                       'baskets. Note which exclusivity, no-shop and notice clauses you '
                                       'will accept only after those terms are locked in writing for this '
                                       'deal.',
                             'example': 'LOI draft holds a 10% escrow for 18 months, R&W insurance paid by '
                                        'the buyer, a cap at 10% of price and a 0.5% basket. Exclusivity '
                                        'runs 60 days only after those lines are written in, because '
                                        'exclusivity, a no-shop clause and a notice duty end the '
                                        'competition that was the leverage [POTOMAC M&A — 8jBQ3jZnNvY @ '
                                        '01:01:56].'},
                            {'name': 'earnout_four_questions',
                             'type': 'textarea',
                             'prompt': 'If an earnout is on the table, answer the four questions in '
                                       'writing: what is measured, who influences performance, how it is '
                                       'verified and when it is paid. Then value the conditional amount '
                                       'separately from cash at closing.',
                             'example': 'Measured: gross profit of the acquired division, not EBITDA after '
                                        'buyer overhead. Influence: the seller keeps pricing authority for '
                                        '24 months. Verified: audited accounts with a seller review right. '
                                        'Paid: within 90 days of each year end. The EUR 2M conditional '
                                        'amount is valued apart from cash today [Saverio Canepa — '
                                        'ZlseQf6dS1g @ 00:02:43].'},
                            {'name': 'adviser_fee_calculation',
                             'type': 'textarea',
                             'prompt': 'Build a worked fee calculation for every adviser you are '
                                       'considering. Cover the triggering event, the fee base (enterprise '
                                       'value or equity), any retainer and whether it is credited, fees '
                                       'due on a failed deal and the tail period.',
                             'example': 'Adviser A and Adviser B both quote 2%. On a EUR 10M EV, EUR 8M '
                                        'equity deal, the gap reaches EUR 60K, EUR 160K versus EUR 220K: '
                                        'EUR 40K from the EV fee base and EUR 20K from an uncredited '
                                        'retainer [Saverio Canepa — kIcxjlHfa74 @ 00:01:46]. Both tails '
                                        'run 12 months.'},
                            {'name': 'sourcing_lane_choice',
                             'type': 'text',
                             'prompt': 'State whether this acquisition will be sourced through a '
                                       'banker-run auction or through proprietary, relationship-driven '
                                       'origination, and name the lawyers, accountants or other referral '
                                       "sources you will cultivate to hear about owners before a banker's "
                                       'book exists.',
                             'example': 'Proprietary lane. Cultivate four estate lawyers and two regional '
                                        'accounting partners who know when clients are about to sell and '
                                        'tip off before the deal reaches a banker [Mink Learning with '
                                        'Steve Balaban, CFA — iTj-KQOCZhY @ 00:00:42]. Avoid '
                                        'banker-shopped flow, since overpaying means you have just paid '
                                        'the seller for the value creation [POTOMAC M&A — RLr8PdCZ6U0 @ '
                                        '00:41:11].'},
                            {'name': 'solar_lead_economics',
                             'type': 'textarea',
                             'prompt': 'Write your current solar customer acquisition math: cost to '
                                       'generate one lead, leads needed per sale, resulting cost per '
                                       'customer, and whether your leads are exclusive or shared with '
                                       'direct competitors. Compare it with the cost of an exclusive, '
                                       'pre-qualified flow.',
                             'example': 'Bought leads cost about $200 each and take five to ten to produce '
                                        'one sale, landing at $1,000 to $2,000 per customer, often resold '
                                        'to direct competitors [David Sugrue — vmJD-cz6rdc @ 00:00:54]. '
                                        'Cold calling converts 1% to appointments, and ten appointments '
                                        'make one commercial sale [Phaibion Royal — rhgUISy29oc @ '
                                        '00:01:20]. Target: exclusive Meta flow under $20 per lead.'},
                            {'name': 'residential_meta_launch',
                             'type': 'textarea',
                             'prompt': 'Plan the residential Meta launch sequence: how many days of '
                                       'warm-up content go on the page first, what share is video, the '
                                       'cost-per-lead ceiling you will hold, your instant callback method '
                                       'and the ad-copy claims you will keep out.',
                             'example': 'Publish seven days of page content, about 70% video, before spend '
                                        '[Nazir Yakubu — FGU8xAz-R1U @ 00:04:37]. Hold cost per lead under '
                                        '$20, with an AI agent calling back instantly. Ad copy leads with '
                                        "the state's rising energy costs and lower bills, never '$0 down', "
                                        'which triggers a special ad category [Leadbase — mb1j52sTZX0 @ '
                                        '00:04:31].'},
                            {'name': 'show_rate_plan',
                             'type': 'textarea',
                             'prompt': 'Describe how you will protect appointment show rates after '
                                       'booking: the retargeting creative shown only to booked prospects, '
                                       'the daily retargeting budget, how confirmations and reschedules '
                                       'are handled, and the priority callback rule for anyone who '
                                       'answered once.',
                             'example': 'Film three short homeowner interviews on install day and run them '
                                        'only to people who just booked, with spend around $20, pushing '
                                        'show rates toward 60% [Nazir Yakubu — FGU8xAz-R1U @ 00:07:09]. AI '
                                        'agents confirm and reschedule. Anyone who picked up once enters a '
                                        'priority callback bucket, where 20-40% convert [Ronen Pessar — '
                                        'dpDcjwreO8o @ 00:09:06].'},
                            {'name': 'commercial_site_visit_gate',
                             'type': 'textarea',
                             'prompt': 'Write the qualification checklist a commercial solar lead must '
                                       'pass before you book a site visit or buy it from a vendor, '
                                       'including competing installer status, supply details, system size '
                                       'and the vendor answers you require before signing.',
                             'example': 'Prospect confirms no other installer has a DNO submission in '
                                        'flight, states phase supply and a rough system size before any '
                                        'trip is booked [Roman Love — oZ_jg6mmZEE @ 00:05:39]. Any lead '
                                        'vendor must state fall-off percentages, lead exclusivity and how '
                                        'its strategy differs from everyone else [Solar Boss — E_z3wa2X4Pw '
                                        '@ 00:04:32]. Fresh leads get a phone call first.'}],
                 'completion_gate': 'Worksheet 4 is complete when the funnel targets, LOI protections, '
                                    'earnout answers and adviser fee math are written for the live deal, '
                                    'and the solar plan shows a cost-per-lead ceiling, a show-rate tactic '
                                    'and a commercial site-visit checklist with every item answered.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Property Opportunity Screens and Legal Intake Controls',
                 'purpose': 'Screen land, roofs and liens for the value that sits below the surface, then '
                            'build legal lead acquisition around speed to lead, verified case inventory, '
                            'honest cost benchmarks and retainers that only close with qualified clients.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Price power before acreage: record voltage, megawatt letters, zoning '
                                  'and re-use demand before pitching any parcel as data-center land to an '
                                  'end user.',
                                  'On every flat-roof hail claim, clean the surface, mark test squares, '
                                  'rule out look-alikes and bring the manufacturer rep out before any core '
                                  'is taken.',
                                  'Run a UCC search on yourself and on the seller, and read every security '
                                  'agreement for all-assets language, before an acquisition or financing '
                                  'moves forward.',
                                  'Set intake speed rules and secondary QC so no mass tort case counts as '
                                  'inventory until it clears background, database and facility treatment '
                                  'checks.',
                                  'Judge every legal campaign against stated cost benchmarks, and sign '
                                  'retainers only with clients who meet at least 5 of the 6 qualification '
                                  'criteria.'],
                 'fields': [{'name': 'powered_land_screen',
                             'type': 'textarea',
                             'prompt': 'For each parcel you plan to pitch as data-center land, record the '
                                       'nearest transmission line voltage, any utility megawatt letter, '
                                       'zoning status and expected rezoning time, and whether you can show '
                                       'a realistic and deliverable path to energization.',
                             'example': 'Parcel 7 sits beside a 230 kV line, the stated minimum, with 500 '
                                        'kV better [Saunders Real Estate — j0rQ27ZfIcU @ 00:11:32]. The '
                                        'utility megawatt letter is requested. Zoning is agricultural, so '
                                        'rezoning could take 3 to 6 months [LandApp by LandGate — '
                                        'UqoyFfPDAmA @ 00:02:04]. Adjacent solar alone is not counted as '
                                        'power.'},
                            {'name': 'reuse_demand_check',
                             'type': 'text',
                             'prompt': 'Name the market where the site or building sits and state the '
                                       'evidence of data-center re-use demand there. Note the obsolescence '
                                       'risk if the facility cannot be repurposed and the qualification '
                                       'odds you are assuming for this parcel.',
                             'example': 'Richmond, Virginia shows re-use demand; the remote alternate site '
                                        'does not, so it is dropped [Industrial Real Estate Show — '
                                        'jak1MCZd_UQ @ 00:11:46]. Assume only about 1% of candidate land '
                                        'is conducive [Industrial Real Estate Show — jak1MCZd_UQ @ '
                                        '00:24:12], and remember a data center costs four times as much to '
                                        'build and is not meant to be repurposed.'},
                            {'name': 'land_price_negotiation',
                             'type': 'textarea',
                             'prompt': 'Write your landowner negotiation position: the farmland value per '
                                       'acre, the data-center value per acre you will anchor to, why you '
                                       "will refuse the first offer, and how land's share of total "
                                       'development cost supports a higher ask.',
                             'example': 'Farmland trades at a couple thousand dollars per acre, while '
                                        'qualifying data-center land can command about $1M per acre '
                                        '[Industrial Real Estate Show — jak1MCZd_UQ @ 00:23:06]. Land is '
                                        '6% of the overall development deal, so moving from $100k to $150k '
                                        'per acre barely registers; the first offer is declined [Saunders '
                                        'Real Estate — j0rQ27ZfIcU @ 00:36:22].'},
                            {'name': 'hail_inspection_kit',
                             'type': 'textarea',
                             'prompt': 'List the inspection kit and sequence for a flat-roof hail claim: '
                                       'surface cleaning, magnification, test squares, coring or cutting '
                                       'the membrane, and who must be on the roof before any core is taken '
                                       'or patched for the carrier.',
                             'example': 'Clean aging PVC with Windex or solvent so the carrier cannot call '
                                        'it deterioration [Jansen/Adjusters International — oAK4wMoYcMA @ '
                                        '00:18:52]. Carry a $9.99 magnifying glass to read divot color. '
                                        'Mark 10x10 test squares. Bring the manufacturer rep before '
                                        'coring, and use a licensed roofer for a warrantied patch '
                                        '[Jansen/Adjusters International — oAK4wMoYcMA @ 00:08:16].'},
                            {'name': 'hail_evidence_log',
                             'type': 'textarea',
                             'prompt': 'Record the evidence for each test square: hit count, divot color '
                                       'under magnification, facing color on the ISO, cracked ISO or split '
                                       'backing found when cored, and any marks ruled out as bird '
                                       'droppings or other look-alikes before being logged as hail.',
                             'example': 'Square B: about 20 circled hits, the count that got one flat roof '
                                        'bought [Jansen/Adjusters International — oAK4wMoYcMA @ 00:27:18]. '
                                        'Divots read black like tar, so newer; ISO facing is not yellow or '
                                        'orange [Jansen/Adjusters International — oAK4wMoYcMA @ 00:13:18]. '
                                        'Core shows cracked ISO. Two TPO marks were bird droppings and '
                                        'excluded [Digital Roofing Innovations — GciwM0T3IPE @ 00:04:58].'},
                            {'name': 'ucc_lien_search',
                             'type': 'textarea',
                             'prompt': 'Before any acquisition or financing, document the UCC search you '
                                       'ran on yourself and on the seller, every security agreement '
                                       'reviewed for all-assets language, and how existing liens could '
                                       'block the financing you are planning to close.',
                             'example': 'UCC search run on our entity and the seller before the LOI '
                                        "[BizNick — 22cx7DJjhTY @ 00:22:54]. The seller's equipment lender "
                                        'holds a filing backed by a signed security agreement with '
                                        'all-assets language, so the lien is public notice that blocks new '
                                        'financing until released. Remember a UCC-1 financing statement '
                                        'does not create a security interest [BizNick — 22cx7DJjhTY @ '
                                        '00:16:09].'},
                            {'name': 'speed_to_lead_intake',
                             'type': 'textarea',
                             'prompt': 'Set your legal intake speed and coverage rules: the maximum '
                                       'seconds or minutes to call a new lead, who answers overflow, how '
                                       'missed and abandoned calls are tagged daily, and how intake staff '
                                       'are coached to sell rather than receive.',
                             'example': 'Web leads get a call within 60 seconds, five minutes maximum '
                                        '[Loudr Media — TJJfmZiIGW4 @ 00:01:34]. LSA calls ring through AI '
                                        'pickup inside 30 seconds, with overflow to a backup call service '
                                        'and every missed call tagged on a daily disposition sheet [Local '
                                        'Service Ads — abdd1rgCZ90 @ 00:03:00]. Intake staff are treated '
                                        'like salesmen, not receptionists.'},
                            {'name': 'mass_tort_qc',
                             'type': 'textarea',
                             'prompt': 'Define the secondary QC every signed mass tort case must clear '
                                       'before it counts as inventory: background check, internal database '
                                       'search for dual representation and known frauds, facility call '
                                       'confirming treatment, and the viability score with reason required '
                                       'on each file.',
                             'example': 'No case is inventory until background check, dual-representation '
                                        'and known-fraud search, and a facility treatment call clear [IMG '
                                        '— dxqvZPB25eo @ 00:00:37]. Every file carries a viability score '
                                        'and reason so nonviable cases release on ingestion and the source '
                                        'is shut down [IMG — dxqvZPB25eo @ 00:03:43]. Frauds always '
                                        'answer, so a quick pickup proves nothing.'},
                            {'name': 'legal_cpl_benchmarks',
                             'type': 'textarea',
                             'prompt': 'Write the cost benchmarks you will judge each legal campaign '
                                       'against: blended Meta cost per lead, practice-area cost per lead, '
                                       'signed-case conversion, realistic weekly case volume and the '
                                       'per-case floor for hard torts, plus lead exclusivity terms.',
                             'example': 'Blended Meta benchmark is $42 CPL across 4,600+ leads, with '
                                        'personal injury at $64 [SMB Team — WZ82yYgND3M @ 00:27:56]. Depo '
                                        'cases are hard to land under $10,000 or above 1 to 3 a week, so a '
                                        '30-case order at $5,000 is refused [IMG — dxqvZPB25eo @ '
                                        '00:06:32]. Only exclusive live transfers are bought, never shared '
                                        'leads.'},
                            {'name': 'retainer_qualification',
                             'type': 'textarea',
                             'prompt': 'Score the prospective retainer client against the six criteria: '
                                       'recurring problem, measurable value, inside your moat, outcome '
                                       'owner, capacity to pay and trust earned. Then set the fee as a '
                                       'share of 12-month value, the minimum term and the single '
                                       'recommended option.',
                             'example': 'Client meets 5 of 6 criteria; trust is still being earned, which '
                                        'is the floor [Ana Leiman — ngCxldTE3UI @ 00:06:36]. Value over 12 '
                                        'months is $400K, so the fee lands at 10 to 20%, shown without '
                                        'hours, with one recommended option [Ana Leiman — ngCxldTE3UI @ '
                                        '00:05:08]. The term opens at one year; paying upfront earns two '
                                        'months free.'}],
                 'completion_gate': 'Worksheet 5 is complete when every pitched parcel shows voltage, '
                                    'zoning and re-use evidence, every hail claim has a test-square '
                                    'evidence log, UCC searches are on file, and the legal intake plan '
                                    'states speed rules, secondary QC, cost benchmarks and a scored '
                                    'retainer client.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Attribution Discipline and Commercial Guardrails',
                 'purpose': 'Commit to one attribution model matched to the real sales cycle, automate the '
                            'CRM data that feeds it, and package lead generation into risk-shared, '
                            'recurring deals that stay inside non-circumvention, filing and FINRA '
                            'trip-wires.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Pick one attribution model, match its influence window to your real '
                                  'sales cycle, and stay consistent rather than hiding inside blended CAC '
                                  'numbers.',
                                  'Automate campaign membership and audit lifecycle workflows so no rep '
                                  'touches attribution data and no non-deal signup fires as a customer '
                                  'conversion.',
                                  'Run the weekly pipeline hygiene report and test every AI agent on a '
                                  'small batch before full automation or any proposal leaves the building.',
                                  'Write the hybrid pricing terms, resale split and credit rules into the '
                                  'contract before pitching, and protect every introduction with '
                                  'non-circumvention language.',
                                  'Map each finance-sector campaign against retail communication '
                                  'thresholds, Form D timing, pre-ODD limits and Reg BI rules before a '
                                  'single message goes out.'],
                 'fields': [{'name': 'attribution_model_choice',
                             'type': 'textarea',
                             'prompt': 'Name the attribution model you will commit to and justify it '
                                       'against your real sales cycle length. State the influence window '
                                       'you will set, how it matches that cycle, and what share of revenue '
                                       'a short ad-platform click window would miss.',
                             'example': 'With an 84-day average cycle, a 30-day click window captures only '
                                        '5-15% of revenue [GrowthSpree - AI Native B2B Marketing Agency — '
                                        'fdPFLXFJlwo @ 00:00:18]. So the model is even distribution in '
                                        'Salesforce with a 180-day influence window matched to the cycle. '
                                        'Last touch only fits hyper-fast cycles near nine days [Chris '
                                        'Walker — wkcuqfylydw @ 00:01:29].'},
                            {'name': 'utm_campaign_automation',
                             'type': 'textarea',
                             'prompt': 'Describe how campaign membership will be captured without any rep '
                                       'touching it: where the campaign ID lives in each UTM, which hidden '
                                       'form field stores it, which automated flow creates the campaign '
                                       'member record, and who audits it monthly.',
                             'example': 'Every UTM carries the Salesforce campaign ID, captured in a '
                                        "hidden 'SF campaign' form field, and a Flow creates the campaign "
                                        'member automatically [SalesLabX — JkmlKUCHcmA @ 00:56:16]. '
                                        'Marketing owns this, because campaign membership should be '
                                        'automated, not dependent on anyone adding members manually '
                                        '[SalesLabX — JkmlKUCHcmA @ 00:18:25]. Marketing ops audits '
                                        'mismatches monthly.'},
                            {'name': 'lifecycle_workflow_audit',
                             'type': 'textarea',
                             'prompt': 'List every HubSpot workflow that can set lifecycle stage to '
                                       'Customer and confirm each requires a real closed deal. Note which '
                                       'non-deal signups were firing false customer conversions into '
                                       'branded or retargeting campaigns and how you stopped them.',
                             'example': "Workflow 'Product signup to Customer' auto-moved an IT signup to "
                                        'Customer, firing false conversions in branded and retargeting '
                                        'campaigns [Cole Furrh | B2B SaaS PPC Pro — WOpqbZNyqNE @ '
                                        '00:03:29]. It now requires a closed deal; Opportunity remains the '
                                        'first stage with a value attached to the lead [Cole Furrh | B2B '
                                        'SaaS PPC Pro — WOpqbZNyqNE @ 00:02:40]. Two workflows passed.'},
                            {'name': 'multi_touch_scope',
                             'type': 'textarea',
                             'prompt': 'Scope your multi-touch model: the number of baseline channels, the '
                                       'workflows and fields required, how data accrues forward and gets '
                                       'backfilled, and how you will prove that revenue rolls up to '
                                       'exactly 100 percent for the board.',
                             'example': 'HubSpot Pro build with 12 baseline channels, 7 workflows and '
                                        '80-some fields, accruing forward with manual backfill of the last '
                                        'two quarters [Value-First — NZUqq5BtQuU @ 00:14:17]. The board '
                                        'gets non-squishy numbers that total 100 percent [Value-First — '
                                        'NZUqq5BtQuU @ 00:10:58]. If 90 percent shows organic during event '
                                        'spend, the missing channel is found first.'},
                            {'name': 'pipeline_hygiene_report',
                             'type': 'textarea',
                             'prompt': 'Design the weekly pipeline hygiene report: which opportunities it '
                                       'flags, how they are grouped, which deal sizes trigger a challenge, '
                                       'and the closed-won share of pipeline you will treat as healthy '
                                       'versus a sign opportunities open too late.',
                             'example': 'Monday exception report lists opportunities with no contact '
                                        'roles, grouped by rep, and any $60k-$100k deal carrying a single '
                                        'contact gets challenged [SalesLabX — JkmlKUCHcmA @ 00:28:18]. '
                                        'Healthy closed-won share of pipeline sits near 30%; at 51% or '
                                        '70-80%, opportunities are being opened too late [SalesLabX — '
                                        'JkmlKUCHcmA @ 00:21:55]. Reps fix flags by Wednesday.'},
                            {'name': 'ai_outreach_guardrails',
                             'type': 'textarea',
                             'prompt': 'Set the guardrails for AI-drafted outreach and proposals: email '
                                       'length, the test batch size before full automation, the facts '
                                       'every proposal must check against a quoted source line, and the '
                                       'promises the agent is never allowed to make.',
                             'example': 'n8n agent emails stay at 4-7 sentences and run on 8 test leads '
                                        'before full automation [AI Automation Official — bQPaiBg-cWs @ '
                                        '00:01:20]. No agent-drafted proposal ships until site counts, '
                                        'entities and dates match a quoted source line, and the agent '
                                        'never promises discounts or dates [Ambilio — oWWC4Sj-SjA @ '
                                        '00:06:57]. A human reviewer signs off each proposal.'},
                            {'name': 'hybrid_pricing_terms',
                             'type': 'textarea',
                             'prompt': 'Write the hybrid lead-gen deal you will offer: base retainer '
                                       'versus full retainer, who funds ad spend, who owns the ad account '
                                       'and pixel, the paid-result definition, the resale split on '
                                       'unqualified leads, and credit pricing and expiry.',
                             'example': 'Retainer drops from $5K to $2K a month; the client funds ad spend '
                                        'and pays more only per delivered appointment [Rafael Hernandez ⚡️ '
                                        '— XPcFTfp7i8E @ 00:05:05]. The contract names ad and pixel '
                                        'ownership, defines a paid appointment, sets the fifty-fifty '
                                        'resale split and prices credits with a 90-day expiry [Rafael '
                                        'Hernandez ⚡️ — XPcFTfp7i8E @ 00:05:42].'},
                            {'name': 'performance_vs_flat',
                             'type': 'text',
                             'prompt': 'Decide whether this client gets performance pay, a flat fee or a '
                                       'hybrid. Explain how the retainer level changes with performance '
                                       'pay and which retention rate you need across your book before the '
                                       'business earns a real exit multiple.',
                             'example': 'Hybrid. Performance deals usually come coupled with an abnormally '
                                        'lower retainer, so clients that barely produce get dropped rather '
                                        'than carried [Daniel Fazio Highlights — bQCztTB4VbQ @ 00:04:19]. '
                                        'Recurring $200-a-month maintenance plans replace one-off builds, '
                                        'and the target is 80 percent plus yearly retention for a six-plus '
                                        'multiple [Alex Hormozi — O1As2zxy0es @ 00:10:50].'},
                            {'name': 'introduction_protection',
                             'type': 'textarea',
                             'prompt': 'Describe how you will protect capital introductions and '
                                       'allocations: the non-circumvention clause covering each '
                                       'introduction, the in-person meeting rule before a large allocation '
                                       'is accepted, and how trust and risk understanding are built before '
                                       'money moves.',
                             'example': 'Every introduction is locked with a signed non-circumvention '
                                        'clause before names are shared. No large allocation is accepted '
                                        'until the investor meets the manager in person; a 10 million '
                                        'dollar check that skipped the handshake redeemed after one bad '
                                        'month inside seven months [Centimillionaire Strategies — '
                                        'N8Z0FPf2yLw @ 00:08:33]. Capital moves because trust is built '
                                        '[Centimillionaire Strategies — N8Z0FPf2yLw @ 00:02:22].'},
                            {'name': 'regulatory_tripwires',
                             'type': 'textarea',
                             'prompt': 'List the regulatory trip-wires on your finance-sector campaigns: '
                                       'the retail communication threshold that triggers principal '
                                       'pre-approval, the Form D and blue sky filing deadline and date of '
                                       'first sale, pre-ODD content limits, and Reg BI rules on contests '
                                       'and quotas.',
                             'example': 'Any piece reaching more than 25 retail investors in 30 calendar '
                                        'days goes to principal pre-approval [Financial Regulation Courses '
                                        '— CmOezPFI5ew @ 00:00:28]. Form D plus blue skies file within 15 '
                                        'days of close, with first sale dated to countersigned '
                                        'subscriptions [All Things SPVs — F1OsgcF_bhg @ 00:09:49]. Pre-ODD '
                                        'emails carry no performance figures or security names. Sales '
                                        'contests are banned.'}],
                 'completion_gate': 'Worksheet 6 is complete when one attribution model and influence '
                                    'window are committed in writing, campaign membership and lifecycle '
                                    'workflows are automated and audited, AI guardrails are tested on a '
                                    'small batch, and every commercial deal and finance-sector campaign '
                                    'clears its pricing, protection and regulatory trip-wires.'}]}
