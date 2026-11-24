from __future__ import annotations

CHAPTER_6 = {'id': 'Q6',
 'chapter_id': 'Q6',
 'chapter_number': 6,
 'question_number': 6,
 'slug': 'source-proprietary-ma-deals',
 'question_prompt': 'How do we build an M&A origination funnel that finds proprietary targets and turns '
                    'outreach into owner conversations?',
 'kicker': 'Q6 / THE BIG MONEY PLAYBOOKS',
 'title': 'Source Proprietary M&A Deals',
 'subtitle': 'Off-market origination, acquisition criteria, sourcing providers, MergerID, deal-flow tools, '
             'cold email, transaction-led outreach, AI sourcing, and reported deal-origination case '
             'studies',
 'layout_template': 'step_by_step_blueprint',
 'reading_time_minutes': 15,
 'executive_summary': 'Operators who source proprietary M&A deals agree that referrals and Rolodex '
                      'networking no longer produce predictable flow, so they build outbound machines: a '
                      'defined acquisition criteria list or TAM, a verified owner list, AI-driven '
                      'personalization, and disciplined sending. Willem reports 1,000+ emails a day '
                      'producing 10+ conversations daily and a healthcare bank booking 70+ qualified '
                      'appointments a month. Ephraim Austin booked calls with $15M, $25M and $30M '
                      'companies within seven days at roughly a 1% reply rate, while Nico Holloman '
                      'averages 12 interested replies per 3,000 sends. Tooling runs through Apollo, '
                      'clay.com, GodMode HQ, getleads.io, listkit.io and Email Bison. The sharpest split: '
                      'POTOMAC M&A calls cold email noise and pushes in-person lunches, and Exxcelerate '
                      'says AI should enrich data, never write copy, after spam caused the 2024 crash.',
 'key_metrics': [{'label': 'Cold Email Reply Rate on Exit-Angle Campaign',
                  'metric': 'Cold Email Reply Rate on Exit-Angle Campaign',
                  'value': 'Around 1%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Average reply rate on the Peakstone campaign that booked calls with $15M, '
                             '$25M and $30M companies in the first 7 days.',
                  'source': 'Ephraim Austin ([esA2m5IlLT8 @ 00:03:20])'},
                 {'label': 'Interested Replies per 3,000 Sends',
                  'metric': 'Interested Replies per 3,000 Sends',
                  'value': '12 interested responses per 3,000 outreaches',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Average for the 'network of a thousand plus buyers' message to electrical "
                             'business owners, sent with an opt-out and signature.',
                  'source': 'Nico Holloman | Hologram Agency ([PauebGoMxEw @ 00:05:07])'},
                 {'label': 'Buy-Side AI Analyst Daily Output',
                  'metric': 'Buy-Side AI Analyst Daily Output',
                  'value': '1,000+ emails/day booking 10+ conversations/day',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "AI 'analyst' workflow pairing a personalized first line with the acquisition "
                             'rationale for buy-side outreach.',
                  'source': 'Willem ([Gi8lgR2IK40 @ 00:06:37])'},
                 {'label': 'Sell-Side Qualified Appointments per Month',
                  'metric': 'Sell-Side Qualified Appointments per Month',
                  'value': '70+ qualified appointments/month',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Healthcare investment bank using sell-side copy that leads with market '
                             'interest instead of track record.',
                  'source': 'Willem ([Gi8lgR2IK40 @ 00:07:54])'}],
 'sections': [{'section_number': 1,
               'title': 'The Practitioner Consensus',
               'paragraphs': ['Every outbound operator here starts from the same verdict: the Rolodex is '
                              'not a pipeline. Willem, who claims $355M in syndicated volume across 100+ '
                              'PE partners and 15+ lower-middle-market investment banks, says relying on '
                              'referrals and personal networks "no longer works" [Gi8lgR2IK40 @ 00:00:43]. '
                              'Ephraim Austin, who runs 800,000 emails a month at Dorsia Labs after 15 '
                              "years in IB and PE and $1B+ closed, rejects referrals because they don't "
                              'scale and rejects content because it "takes at least 6 to9 months to get '
                              'any type of traction" [esA2m5IlLT8 @ 00:01:23]. Nico Holloman opens on the '
                              'identical complaint that referral flow is simply not predictable, and '
                              'answers it with a list-and-send machine instead of a networking calendar '
                              '[PauebGoMxEw @ 00:00:00]. Even Paul Jammore of POTOMAC M&A, who later '
                              'fights the cold-email crowd hard on execution, agrees on the diagnosis: '
                              'passive "fishers" who wait for deals to come to them may wait a decade '
                              '[T64at1dT1Zs @ 00:05:16]. The shared conclusion is that proprietary flow '
                              'has to be manufactured, not waited for. Whoever controls the first '
                              'conversation with an owner gets there before the bankers and brokers do, '
                              'and every speaker in this camp builds a repeatable outbound system '
                              'specifically to own that first conversation at volume.',
                              'The second consensus point is that the target universe gets defined on '
                              'paper before a single email goes out. Paul Jammore insists on writing an '
                              'acquisition criteria list before going to market, then shows how wildly '
                              'universes vary: lawn care may offer 500 targets that screen down to about '
                              '100, while POS software may have only 3 or 4 targets globally [T64at1dT1Zs '
                              "@ 00:03:38]. Ephraim Austin's playbook for Peakstone runs in the same "
                              'order: build infrastructure, map the TAM at $15M+ revenue in electrical '
                              'contracting or industrial services, and only then write messaging and book '
                              'calls [esA2m5IlLT8 @ 00:01:57]. Nico Holloman builds the list by cloning a '
                              "firm's best clients into an ideal customer avatar, so the new list mirrors "
                              'the companies the firm already does its best work with [PauebGoMxEw @ '
                              '00:01:12]. Exxcelerate, after roughly 700 M&A clients over 5+ years, draws '
                              'a hard size line: lower-middle-market companies with $1M+ EBITDA, not Main '
                              'Street [TE99yv49oy4 @ 00:08:14]. The practical baseline across all four is '
                              'identical. Know the sector, the size band and the ownership profile you '
                              'want, because the list, the copy and the qualification screen all inherit '
                              'from that one definition. A vague thesis produces a vague list, and every '
                              'downstream step inherits the mess.',
                              'The third shared belief is that owners are already flooded, so generic '
                              'outreach is dead on arrival. Willem warns that owners are "getting hit up '
                              '247 with inquiries about you know buying their business," can spot '
                              'automated emails, and have been burned by time-wasters [2X_myL7Ao9A @ '
                              '00:02:02]. In a follow-up build, Willem adds that generic emails fail '
                              'because founders distrust "empty inquiries," so every message has to prove '
                              'real research into that specific company [PSsr4qdwaj8 @ 00:04:07]. John '
                              'Colley pushes the same idea upstream into target refinement: look for a '
                              'concrete reason for sale such as death, disease, divorce or retirement '
                              'before anyone makes an approach, and check deal deliverability, because a '
                              'blocking minority is a risk Colley has personally run into [dZiHOJKxvoE @ '
                              '00:03:49]. M&A Synergy AI turns those triggers into scannable signals, '
                              "watching for executive departures, a founder's divorce, hiring spikes and "
                              'negative reviews [kk3kEZ_huBU @ 00:03:27]. The common thread is relevance '
                              'plus motive. The message must show why this owner, why this company and why '
                              'now, and qualification starts before the first reply, not after it. Willem '
                              'closes the loop on the back end by screening every response for genuine '
                              'intent to sell rather than tire kickers.'],
               'table': {'caption': 'Where the M&A sourcing operators agree: core principles and what they '
                                    'actually do',
                         'headers': ['Consensus Principle',
                                     'What the Practitioner Actually Does',
                                     'Reported Payoff or Warning',
                                     'Expert Source'],
                         'rows': [['Referrals and the Rolodex are no longer a pipeline',
                                   'Replaces network-driven flow with an account list, conversations, '
                                   'scale and qualification system',
                                   'Scales conversations from 20 a day toward 1,000 a day while staying '
                                   'personalized',
                                   'Willem ([Gi8lgR2IK40 @ 00:01:44])'],
                                  ['Content and referrals are too slow to rely on',
                                   'Builds sending infrastructure, maps a $15M+ revenue TAM, then writes '
                                   'messaging and books calls',
                                   'Calls with $15M, $25M and $30M companies inside the first 7 days',
                                   'Ephraim Austin ([esA2m5IlLT8 @ 00:02:51])'],
                                  ['Write the acquisition criteria list before going to market',
                                   'Defines sector and size first, then screens the whole universe before '
                                   'any outreach begins',
                                   'Lawn care shrinks from 500 targets to about 100; POS software has 3-4 '
                                   'globally',
                                   'POTOMAC M&A ([T64at1dT1Zs @ 00:03:38])'],
                                  ['Clone the best existing clients into the target profile',
                                   'Builds an ideal customer avatar from top clients and filters proxies '
                                   'for $750K+ EBITDA',
                                   'About 7,200 owners pulled for verification and AI scoring in one run',
                                   'Nico Holloman | Hologram Agency ([PauebGoMxEw @ 00:01:12])'],
                                  ['Hunt for a concrete reason the owner would sell',
                                   'Refines shortlists by checking for death, disease, divorce or '
                                   'retirement behind a potential sale',
                                   'Deliverability checks catch blocking minorities that can stop a deal '
                                   'from closing',
                                   'John Colley | The Investment Banking Practitioner ([dZiHOJKxvoE @ '
                                   '00:03:49])'],
                                  ['Generic outreach gets ignored by owners who are already flooded',
                                   'Uses AI research to write a first line complimenting two specific '
                                   'company achievements',
                                   'Owners spot automated emails and have been burned by time-wasting '
                                   'buyers',
                                   'Willem ([2X_myL7Ao9A @ 00:02:02])'],
                                  ['Track and nurture the owners who are not ready yet',
                                   'Keeps trackable multichannel follow-up running on the roughly 95 not '
                                   'ready at first pass',
                                   'Repeat visits to a sell-a-business page trigger sales tasks or '
                                   'persona-specific campaigns',
                                   'BN.Digital ([ssgz-uXMi6c @ 00:02:09])']]}},
              {'section_number': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['List building is where the operators get specific. Willem stacks Apollo, '
                              'LinkedIn and Google Maps, hires Fiverr or Upwork contractors to scrape '
                              'PitchBook, and uses Ocean to generate lookalike lists, while warning that '
                              'PitchBook cannot hold all private-company data [Gi8lgR2IK40 @ 00:03:08]. '
                              'Because revenue claims on private companies are often impossible to pin '
                              'down, Willem segments by proxy instead: 50+ or 100+ employees, or 1,000+ '
                              'reviews [Gi8lgR2IK40 @ 00:04:51]. Nico Holloman runs Claude Code against '
                              'getleads.io with proxy filters aimed at $750K+ EBITDA, pulls roughly 7,200 '
                              'owners, and verifies them through listkit.io. In one run of 6,400 leads, '
                              'only 1,900 came back valid, 2,200 were catch-alls and 2,300 were unusable, '
                              'with the catch-alls pushed through Omni Verifier for a second pass '
                              '[PauebGoMxEw @ 00:06:50]. Holloman then has AI score every company from 1 '
                              'to 10, and "anyone who\'s under a five out of 10 gets automatically cut '
                              'from the list"; a 114-employee HVAC company scored 9/10 [PauebGoMxEw @ '
                              '00:08:17]. By the time the sequence loaded into Email Bison, 1,324 leads '
                              "survived from 6,000. Holloman's own funnel shows the attrition plainly: the "
                              'raw pull has to be several times larger than the send list you actually '
                              'want, because verification and scoring each cut deep into it.',
                              "Personalization is engineered, not handwritten. Willem's $50M "
                              'marketing-services deal ran through clay.com, described as "chat jbt meets '
                              'you know a Google spreadsheet": upload a lead list, have AI pull each '
                              "company's LinkedIn description, write a first line that compliments two "
                              "specific things and ties them to the investment group's interest, add a "
                              'generic brief on the firm representing top active buyers, then layer a '
                              'second personalization mapping what the company does to investor interests '
                              '[2X_myL7Ao9A @ 00:00:51]. Willem also has AI re-label every industry, '
                              'because data platforms mislabel constantly; "medical device distributors '
                              'focused on acute care" is the kind of specific label wanted instead of a '
                              "vendor's default tag [2X_myL7Ao9A @ 00:04:01]. In the GodMode HQ build, "
                              'filters for founder, owner and CEO titles, chemical manufacturing and '
                              '$20M-$100M revenue returned 145 leads, and the research prompt hunts each '
                              'company website for awards, press, case studies, specific products and the '
                              'B2B buyer avatar, with a fallback to anything "particularly interesting" '
                              '[PSsr4qdwaj8 @ 00:04:07]. Exxcelerate draws the boundary hard: use AI for '
                              'enrichment and pre-call M&A reports, but not to "think" or write the copy '
                              'itself, and map the full process on paper before automating any piece of it '
                              '[TE99yv49oy4 @ 00:19:27].',
                              "The copy itself is short and owner-facing. Ephraim Austin's email to "
                              'Peakstone\'s TAM used the subject line "future ownership," opened with '
                              '"Have you thought about an exit at...", referenced the Schmidt Electric to '
                              'MC Corp deal, offered a complimentary valuation overview and closed on a '
                              'soft CTA, aimed only at founders, owners and CEOs holding equity '
                              '[esA2m5IlLT8 @ 00:04:20]. That campaign produced a $15M engineering firm '
                              'within 2 hours, a $30M subsidiary the same day and a $25M contractor on day '
                              '7. Nico Holloman leads with buyer depth instead, a "network of a thousand '
                              'plus buyers" for electrical businesses between 1 and 40 million, plus an '
                              'opt-out and signature, and that exact message averaged 12 interested '
                              'responses per 3,000 sends [PauebGoMxEw @ 00:05:07]. Holloman runs 3-step '
                              'sequences on a 4-day then 7-day cadence through Email Bison and reports '
                              '7-15 booked meetings a month at 1,000-2,000 sends a day [PauebGoMxEw @ '
                              '00:09:52]. On the sell side, Willem says to lead with market interest '
                              'rather than your track record; a healthcare investment bank using that '
                              'angle booked 70+ qualified appointments a month, while the buy-side AI '
                              '"analyst" workflow pushes 1,000+ emails a day and books 10+ conversations '
                              'daily [Gi8lgR2IK40 @ 00:07:54].'],
               'table': {'caption': 'The outbound M&A sourcing stack: stage by stage, with the numbers the '
                                    'operators reported',
                         'headers': ['Pipeline Stage',
                                     'Tool or Tactic Used',
                                     'Exact Numbers Reported',
                                     'Expert Source'],
                         'rows': [['Raw data pull and proxy segmentation',
                                   'Apollo, LinkedIn, Google Maps, Fiverr or Upwork PitchBook scrapes, and '
                                   'Ocean lookalike lists',
                                   'Segment by 50+ or 100+ employees, or 1,000+ reviews, when revenue is '
                                   'impossible',
                                   'Willem ([Gi8lgR2IK40 @ 00:04:51])'],
                                  ['Owner list build from the avatar',
                                   'Claude Code run against getleads.io using proxy filters for the target '
                                   'EBITDA band',
                                   '$750K+ EBITDA proxy filter with about 7,200 owners pulled in one run',
                                   'Nico Holloman | Hologram Agency ([PauebGoMxEw @ 00:01:28])'],
                                  ['Email verification and catch-all recovery',
                                   'listkit.io for the first pass, with catch-all addresses re-run through '
                                   'Omni Verifier',
                                   '6,400 leads split into 1,900 valid, 2,200 catch-all and 2,300 unusable',
                                   'Nico Holloman | Hologram Agency ([PauebGoMxEw @ 00:06:50])'],
                                  ['AI account research and list filtering',
                                   'GodMode HQ title, geography, industry and revenue filters plus a '
                                   'website research prompt',
                                   '145 leads from owner titles, chemical manufacturing and $20M-$100M '
                                   'revenue',
                                   'Willem ([PSsr4qdwaj8 @ 00:03:17])'],
                                  ['Personalized first lines at scale',
                                   'clay.com spreadsheet AI pulling LinkedIn descriptions and writing '
                                   'two-compliment opening lines',
                                   '10,000-lead list engaged within days; $50M deal with an LOI in a '
                                   'couple days',
                                   'Willem ([2X_myL7Ao9A @ 00:05:29])'],
                                  ['Exit-angle copy aimed at equity holders',
                                   "Subject 'future ownership', past deal reference, complimentary "
                                   'valuation overview and a soft CTA',
                                   'Reply rate around 1%; $60M sell-side mandate from 12 calls over 4 '
                                   'months',
                                   'Ephraim Austin ([esA2m5IlLT8 @ 00:04:20])'],
                                  ['Sequencing cadence and daily send volume',
                                   'Email Bison sender running a three-step sequence on a 4-day then 7-day '
                                   'cadence',
                                   '2,000-3,000 sends a day; 12 interested replies per 3,000 sends',
                                   'Nico Holloman | Hologram Agency ([PauebGoMxEw @ 00:09:52])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Edges the operators use that most deal teams skip',
                           'body': 'Small execution choices that the practitioners credit for getting '
                                   'owners on the phone faster.',
                           'items': ['For blue-collar targets, go after the generic or inquiry company '
                                     'inbox instead of hunting a named executive address; that is where '
                                     'owner-operated businesses actually read mail [Willem — Gi8lgR2IK40 @ '
                                     '00:03:39].',
                                     "Use a client's past closed deal as the hook even if you never held "
                                     "that mandate; Peakstone's Schmidt Electric to MC Corp deal anchored "
                                     'a campaign the agency did not win [Ephraim Austin — esA2m5IlLT8 @ '
                                     '00:01:39].',
                                     'Diversify sending platforms, data sources and domains, and buy the '
                                     'domains yourself: agency-bought domains outperformed client-bought '
                                     'domains after the 2024 crash [Exxcelerate — TE99yv49oy4 @ 00:11:13].',
                                     "Wire behavioral triggers into the CRM so repeat visits to a 'sell a "
                                     "business' page fire a sales task or a persona-specific campaign "
                                     'automatically [BN.Digital — ssgz-uXMi6c @ 00:02:54].']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock the acquisition criteria and map the TAM',
                              'action': 'Write the criteria list, then define sector, size band and '
                                        'ownership before building any list.',
                              'detail': 'Jammore writes the acquisition criteria list before going to '
                                        'market and screens universes like lawn care from 500 down to '
                                        'about 100 [POTOMAC M&A — T64at1dT1Zs @ 00:01:23]; Austin maps a '
                                        '$15M+ revenue electrical and industrial services TAM before '
                                        'writing a word of copy [Ephraim Austin — esA2m5IlLT8 @ '
                                        '00:01:57].'},
                             {'step': 2,
                              'title': 'Build, verify and score the owner list',
                              'action': 'Pull owners with proxy filters, verify emails, recover '
                                        'catch-alls, and cut anything scoring under 5/10.',
                              'detail': 'Holloman pulls about 7,200 owners via getleads.io, verifies '
                                        'through listkit.io, re-runs catch-alls in Omni Verifier, and '
                                        'auto-cuts every company scoring under five out of 10 [Nico '
                                        'Holloman | Hologram Agency — PauebGoMxEw @ 00:03:36].'},
                             {'step': 3,
                              'title': 'Run AI research and personalization on a test batch first',
                              'action': 'Run the website research prompt on the first five rows, check '
                                        'output, then queue the full list.',
                              'detail': 'Willem tests the GodMode HQ research prompt (awards, press, case '
                                        'studies, products, B2B buyer avatar) on the first five rows '
                                        'before queuing everything, then generates a two-achievement first '
                                        'line [Willem — PSsr4qdwaj8 @ 00:06:22].'},
                             {'step': 4,
                              'title': 'Send, then qualify every reply for real intent',
                              'action': 'Launch the sequence and screen responders for intent to sell '
                                        "before they reach a dealmaker's calendar.",
                              'detail': 'Willem screens out tire kickers by email or through a hired '
                                        '10-minute screener call so only owners with real intent to sell '
                                        'reach the deal team [Willem — Gi8lgR2IK40 @ 00:10:10].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ["The loudest split is volume versus intimacy. Willem runs an AI 'analyst' "
                              'workflow that pushes 1,000+ personalized emails a day and books 10+ owner '
                              'conversations daily, framing the jump from 20 to 1,000 conversations a day '
                              'as the whole game [Gi8lgR2IK40 @ 00:06:37]. Nico Holloman of Hologram '
                              'Agency runs even hotter, sending 2,000 to 3,000 emails a day and calling 12 '
                              "interested replies per 3,000 sends 'very strong' [PauebGoMxEw @ 00:05:26]. "
                              'Paul Jammore of POTOMAC M&A rejects the premise outright. Jammore calls '
                              "cold emails 'noise' and tells buyers to sit the owner down for a personal "
                              "lunch or a diner meeting instead [T64at1dT1Zs @ 00:09:42]. Jammore's "
                              'verdict on buy-side brokers hits the same nerve: their mass email is '
                              "'highly efficient' but 'not very effective,' fishers can wait a decade, and "
                              'an in-house sourcing capability beats both. John Colley stakes out a middle '
                              'lane. Colley approaches targets on a no-names basis, works LinkedIn and '
                              'Twitter to engineer warm introductions, and only then picks up the phone '
                              'for cold calls [dZiHOJKxvoE @ 00:05:15]. So the same owner can be hit three '
                              'ways: a personalized email at machine scale, a warm intro brokered through '
                              'social platforms, or a buyer who shows up in person and skips the inbox '
                              'entirely.',
                              'Practitioners split hard on how to define the target universe. Willem says '
                              'PitchBook cannot hold all private-company data and that revenue claims are '
                              'often impossible to verify, so Willem segments by headcount, 50+ or 100+ '
                              'employees, or by review volume, 1,000+ reviews, and hires Fiverr or Upwork '
                              'contractors for PitchBook scrapes [Gi8lgR2IK40 @ 00:04:51]. Nico Holloman '
                              'goes the other way, cloning the best existing clients into an ideal '
                              'customer avatar and running Claude Code with getleads.io on proxy filters '
                              'aimed at $750K+ EBITDA, then letting AI score every company 1 to 10 '
                              '[PauebGoMxEw @ 00:01:28]. Marco Palmero warns that leaning on any single '
                              'data provider caps results and demands multi-layered data from anyone '
                              "sourcing for you [p5BRxk-zVCA @ 00:05:22]. Willem's own AI build adds a "
                              'twist: data platforms routinely mislabel industries, so the workflow has AI '
                              're-label each company, turning vague tags into specifics such as medical '
                              'device distributors focused on acute care [2X_myL7Ao9A @ 00:04:01]. The '
                              'result is three competing philosophies. One trusts observable proxies like '
                              'headcount and reviews, one trusts an engineered EBITDA proxy plus an AI '
                              "score, and one refuses to bet on any single database. Willem's verdict on "
                              'raw vendor labels is blunt: do not trust the lead source.',
                              'The sharpest live argument is how much thinking to hand to AI. Willem '
                              'claims AI now replaces research teams, cold callers, and emailers, and '
                              'scales outreach to 10,000 companies a day [PSsr4qdwaj8 @ 00:01:05]. '
                              'Exxcelerate, after roughly 700 M&A clients, draws the line much tighter: '
                              "use AI for enrichment and pre-call M&A reports, but never let it 'think' or "
                              'write copy, and map the full process on paper before automating anything '
                              "[TE99yv49oy4 @ 00:19:27]. That puts Exxcelerate directly against Willem's "
                              'clay.com build, where AI writes the first line, the second personalization '
                              'layer, and the industry re-labels. Inside the banks, the fight continues. '
                              'Jan Pörschmann of atares warns about AI overuse, makes staff explain models '
                              'cell by cell, and has new joiners build first models by hand [rOwXkmrMljc @ '
                              '00:38:10]. Michael Drill of Lincoln International predicts execution '
                              'becomes a commodity and 2030 teams shrink to six people with one analyst '
                              "and one associate, and Pörschmann says outright that they 'would take a bet "
                              "against' it [rOwXkmrMljc @ 00:52:09]. The two even prescribe different "
                              'moats: Pörschmann bets on proprietary knowledge pulled through MCPs and '
                              'good prompts, while Drill bets on winning the war for talent. Both already '
                              "run AI daily, from Pörschmann's morning deal alert to Drill's "
                              'two-to-three-minute meeting briefings.'],
               'table': {'caption': 'Competing M&A sourcing playbooks, side by side',
                         'headers': ['Fault Line', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Outreach channel used for first contact with business owners',
                                   'Willem runs an AI analyst workflow sending 1,000+ emails daily and '
                                   'booking 10+ conversations',
                                   'Jammore calls cold emails noise and pushes a personal lunch or diner '
                                   'meeting instead',
                                   'Willem ([Gi8lgR2IK40 @ 00:06:37]); POTOMAC M&A ([T64at1dT1Zs @ '
                                   '00:09:42])'],
                                  ['Who runs sourcing: an online platform or an in-house team',
                                   'WallStreetMojo says online matchmaking platforms run cheaper than '
                                   'staffing full in-house teams',
                                   'Jammore ranks building in-house capability above buy-side brokers and '
                                   'passive fishing',
                                   'WallStreetMojo ([x21Z365qRBM @ 00:05:53]); POTOMAC M&A ([T64at1dT1Zs @ '
                                   '00:06:20])'],
                                  ['Single-channel versus multichannel outreach sequencing from day one',
                                   'Palmero starts single-channel early, then layers multichannel outreach '
                                   'for compounding results',
                                   'BN.Digital integrates email, phone, LinkedIn, and snail mail at the '
                                   'top of funnel',
                                   'Marco Palmero ([p5BRxk-zVCA @ 00:02:47]); BN.Digital ([ssgz-uXMi6c @ '
                                   '00:00:34])'],
                                  ['How to size targets when private-company financials stay hidden',
                                   'Willem segments by 50+ or 100+ employees or 1,000+ reviews instead of '
                                   'revenue',
                                   'Holloman runs proxy filters for $750K+ EBITDA and AI scores each '
                                   'company 1 to 10',
                                   'Willem ([Gi8lgR2IK40 @ 00:04:51]); Nico Holloman | Hologram Agency '
                                   '([PauebGoMxEw @ 00:01:28])'],
                                  ['Whether AI should be allowed to write the outreach copy',
                                   'Willem has clay.com write a first line complimenting two achievements '
                                   'tied to buyer interest',
                                   'Exxcelerate uses AI only for enrichment and pre-call reports, never to '
                                   'think or write copy',
                                   'Willem ([2X_myL7Ao9A @ 00:02:29]); Exxcelerate ([TE99yv49oy4 @ '
                                   '00:19:27])'],
                                  ['Sell-side hook placed in the very first owner email',
                                   'Willem leads with live market interest from buyers rather than the '
                                   "bank's track record",
                                   'Ephraim Austin leads with a past deal reference plus a complimentary '
                                   'valuation overview',
                                   'Willem ([Gi8lgR2IK40 @ 00:07:54]); Ephraim Austin ([esA2m5IlLT8 @ '
                                   '00:04:20])'],
                                  ['Shape and moat of the 2030 M&A deal team',
                                   'Drill expects execution to commoditize and teams of six with one '
                                   'analyst, one associate',
                                   'Pörschmann would take a bet against that and leans on proprietary '
                                   'knowledge through MCPs',
                                   'SS&C Intralinks ([rOwXkmrMljc @ 00:52:09]); SS&C Intralinks '
                                   '([rOwXkmrMljc @ 00:55:31])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failure on record is the deliverability crash. '
                              'Exxcelerate says spam is what caused the 2024 crash, and the lessons were '
                              'bought the hard way: diversify sending platforms, data sources, and '
                              'domains, and buy domains at the agency level because agency-bought domains '
                              'outperform client-bought ones [TE99yv49oy4 @ 00:11:13]. Exxcelerate is '
                              'equally clear that cold email itself is not dead and that most people '
                              'simply run it wrong. Ephraim Austin of Dorsia Labs, sending 800,000 emails '
                              'a month, gives the same warning from the volume side: scaling requires '
                              'avoiding spam and following CAN-SPAM [esA2m5IlLT8 @ 00:06:04]. List rot is '
                              "the second leak. Nico Holloman's run started at about 6,400 leads and "
                              'verification split them into 1,900 valid, 2,200 catch-all, and 2,300 '
                              'unusable, with catch-alls pushed through Omni Verifier for a second pass '
                              '[PauebGoMxEw @ 00:06:50]. By the time the sequence launched in Email Bison, '
                              'just 1,324 leads had survived from 6,000 [PauebGoMxEw @ 00:09:52]. That is '
                              'roughly a fifth of the raw pull, so a meeting forecast built on the raw '
                              "lead count overstates the real list more than fourfold. Holloman's own "
                              'starting figures drift between 7,200, 6,400, and 6,000, so only '
                              'post-verification survivors belong in the send, reply, and booked-call '
                              'math.',
                              'The second trap is assuming owners are waiting for your email. Willem says '
                              "owners are 'getting hit up 24/7' with inquiries about buying their "
                              'business, can spot automated emails, and have already been burned by '
                              'time-wasters [2X_myL7Ao9A @ 00:02:02]. In the GodMode HQ build, Willem '
                              'names the failure directly: generic emails die because founders distrust '
                              "'empty inquiries,' which is why the research prompt hunts awards, press, "
                              'case studies, products, and the B2B buyer avatar before a first line is '
                              'written [PSsr4qdwaj8 @ 00:04:07]. The mirror-image failure sits on the '
                              "reply side, after an owner finally answers. Willem's qualification step "
                              'screens for real intent to sell rather than tire kickers, either over email '
                              "or through a hired screener running 10-minute calls, so the closer's "
                              'calendar is not eaten by curiosity [Gi8lgR2IK40 @ 00:10:10]. Marco Palmero '
                              'adds a vendor-side trap: watch for marketers disguised as M&A providers, '
                              'because most campaign problems are strategic rather than technical and '
                              "selling a company is 'a life-changing decision' [p5BRxk-zVCA @ 00:01:06]. "
                              'Stack those warnings together and the failure chain is clear. Lazy '
                              'personalization kills the open, unscreened replies kill the calendar, and a '
                              'provider without M&A experience kills the positioning long before a mandate '
                              'is in sight.',
                              'The economics checks are blunt. Exxcelerate compared two clients: one with '
                              'a CRM closed its third deal from roughly 200 to 300 opportunities, while '
                              'one without a CRM generated 400+ opportunities and closed none [TE99yv49oy4 '
                              '@ 00:25:56]. More leads did not rescue the client with no system. Ephraim '
                              'Austin shows how long the cycle runs even when the top of funnel works: a '
                              '$60M sell-side mandate came from 12 calls spread over 4 months, on a reply '
                              'rate Ephraim pegs at around 1% [esA2m5IlLT8 @ 00:06:19]. Paul Jammore of '
                              "POTOMAC M&A flags the diligence trap on small add-ons: messy 'cigar box' "
                              'books may simply not be worth the effort on a $1M deal, and paying too much '
                              'for even the best company still makes it a bad investment [T64at1dT1Zs @ '
                              '00:00:36]. John Colley warns from personal experience that a blocking '
                              'minority can sink deal deliverability, which is why the refining stage '
                              'checks whether a deal can actually close and summarizes each target in a '
                              'SWOT before approach [dZiHOJKxvoE @ 00:04:27]. Those four checks frame the '
                              'real P&L. Each one marks a point where a funded pipeline dies: a CRM gap, a '
                              'cigar box ledger, a minority holder who blocks the sale, or a 4-month cycle '
                              'nobody budgeted for.'],
               'table': {'caption': 'Firsthand traps, what broke, and the fix each practitioner applied',
                         'headers': ['Trap',
                                     'What Went Wrong Firsthand',
                                     'Fix the Practitioner Applied',
                                     'Expert Source'],
                         'rows': [['Spam-driven cold email sending collapse during 2024',
                                   'Exxcelerate traced the 2024 cold email crash directly back to spam',
                                   'Diversify sending platforms, data sources, and domains across every '
                                   'client campaign',
                                   'Exxcelerate ([TE99yv49oy4 @ 00:17:24])'],
                                  ['Sending from domains purchased by the client',
                                   'Domains bought by clients underperformed domains bought and managed by '
                                   'the agency',
                                   'Have the agency buy and control the sending domains for each campaign',
                                   'Exxcelerate ([TE99yv49oy4 @ 00:11:13])'],
                                  ['Launching on unverified business owner email lists',
                                   'Of 6,400 pulled leads, only 1,900 were valid while 2,300 were unusable',
                                   'Verify with listkit.io, then push the 2,200 catch-alls through Omni '
                                   'Verifier',
                                   'Nico Holloman | Hologram Agency ([PauebGoMxEw @ 00:06:50])'],
                                  ['Running a deal pipeline with no CRM behind it',
                                   'A client without a CRM generated 400+ opportunities and closed zero '
                                   'deals',
                                   'The client running a CRM closed a third deal from 200 to 300 '
                                   'opportunities',
                                   'Exxcelerate ([TE99yv49oy4 @ 00:25:56])'],
                                  ['Blocking minority shareholder discovered too late in process',
                                   'Colley has personally seen a blocking minority threaten whether a deal '
                                   'could close',
                                   'Check deal deliverability during refining and summarize every target '
                                   'with a SWOT',
                                   'John Colley | The Investment Banking Practitioner ([dZiHOJKxvoE @ '
                                   '00:04:27])'],
                                  ['Underpaying for an outside deal sourcing provider',
                                   'Palmero says below a certain price threshold you get 100% less in '
                                   'results',
                                   'Weigh fees against deal size; $15K versus $30K on a $5M deal does not '
                                   'matter',
                                   'Marco Palmero ([p5BRxk-zVCA @ 00:16:12]); Marco Palmero ([p5BRxk-zVCA '
                                   '@ 00:14:31])'],
                                  ['AI time savings that quietly vanish into process',
                                   'Drill says clients use AI too, so saved hours get absorbed by more '
                                   'process interactions',
                                   'Run the extra mile with additional advice and added value beyond the '
                                   'AI baseline',
                                   'SS&C Intralinks ([rOwXkmrMljc @ 00:30:28])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Kill Switches Before Any Sequence Goes Live',
                           'body': 'Every gate below comes from a list that shrank, a pipeline that closed '
                                   'nothing, or a calendar flooded with tire kickers [Exxcelerate — '
                                   'TE99yv49oy4 @ 00:25:56].',
                           'items': ['Do not launch on raw counts: verify every lead and re-verify '
                                     "catch-alls, because Holloman's 6,000-lead pull shrank to 1,324 "
                                     'sendable leads [Nico Holloman | Hologram Agency — PauebGoMxEw @ '
                                     '00:09:52].',
                                     'Cut every target the AI scores under 5 out of 10 before a single '
                                     'email is sent [Nico Holloman | Hologram Agency — PauebGoMxEw @ '
                                     '00:08:17].',
                                     'No CRM, no campaign: the CRM-less client turned 400+ opportunities '
                                     'into zero closings [Exxcelerate — TE99yv49oy4 @ 00:25:56].',
                                     'Screen every reply for real intent to sell, by email or a hired '
                                     '10-minute screener call, before it reaches the closer [Willem — '
                                     'Gi8lgR2IK40 @ 00:10:10].']}}],
 'pull_quote': 'Remember, in M&A, your sourcing strategy literally is your valuation strategy. — One '
               'Minute Finance (id39IYEm-oQ @ 00:09:06).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Write a full acquisition criteria list before going to market, then size the real '
                      'target universe after screening [POTOMAC M&A — T64at1dT1Zs @ 00:01:23].',
                      'Clone your best clients into an ideal customer avatar and build the list with proxy '
                      'filters such as $750K+ EBITDA [Nico Holloman | Hologram Agency — PauebGoMxEw @ '
                      '00:01:12].',
                      'Run the account research prompt for awards, press, case studies, and products on '
                      'the first five rows, then queue the full list [Willem — PSsr4qdwaj8 @ 00:06:22].',
                      "Use a past deal as the hook with a 'future ownership' subject line, a complimentary "
                      'valuation overview, and a soft CTA aimed at equity-holding founders [Ephraim Austin '
                      '— esA2m5IlLT8 @ 00:04:20].',
                      'Diversify sending platforms, data sources, and domains, and have the agency buy the '
                      'sending domains [Exxcelerate — TE99yv49oy4 @ 00:11:13].',
                      'Keep nurturing the owners not ready on the first pass and fire sales tasks when '
                      'someone repeatedly visits the sell-a-business page [BN.Digital — ssgz-uXMi6c @ '
                      '00:02:54].'],
 'statutory_citations': [{'title': 'POTOMAC M&A — Acquisition Criteria & Proprietary Deal Flow | Buy-Side '
                                   'Masterclass Moment [00:09:42]',
                          'url': 'https://www.youtube.com/watch?v=T64at1dT1Zs&t=582s',
                          'relevance': 'Primary practitioner testimony on rejecting cold email noise in '
                                       'favor of in-person owner meetings and in-house sourcing.'},
                         {'title': 'Exxcelerate — How We Actually Source M&A Deals: Cold Email, AI, and '
                                   'Tech Stacks [00:11:13]',
                          'url': 'https://www.youtube.com/watch?v=TE99yv49oy4&t=673s',
                          'relevance': 'Primary practitioner testimony on the 2024 spam crash, domain '
                                       'diversification, AI limits, and CRM-driven close rates.'},
                         {'title': 'Ephraim Austin — We Turned an M&A Firm’s Past Deal Into Calls With '
                                   '$15M, $25M & $30M Companies in the First 7 Days [00:06:19]',
                          'url': 'https://www.youtube.com/watch?v=esA2m5IlLT8&t=379s',
                          'relevance': 'Primary practitioner testimony on past-deal hooks, 1% reply rates, '
                                       'and a $60M mandate from 12 calls over 4 months.'},
                         {'title': 'Nico Holloman | Hologram Agency — The New Way to Source M&A Deals in '
                                   '2027 [00:06:50]',
                          'url': 'https://www.youtube.com/watch?v=PauebGoMxEw&t=410s',
                          'relevance': 'Primary practitioner testimony on list verification losses, AI '
                                       'scoring cutoffs, and send-to-meeting benchmarks.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'Gi8lgR2IK40',
                       'title': 'Full Guide on M&A Deal Origination',
                       'channel': 'Willem',
                       'author': 'Willem',
                       'text': 'Relying on your Rolodex or referrals no longer works.',
                       'tip': 'Relying on your Rolodex or referrals no longer works.',
                       'timestamp': 43,
                       'timestamp_seconds': 43,
                       'timestamp_label': '[00:00:43]',
                       'url': 'https://www.youtube.com/watch?v=Gi8lgR2IK40&t=43s',
                       'markdown': '[00:00:43](https://www.youtube.com/watch?v=Gi8lgR2IK40&t=43s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'esA2m5IlLT8',
                       'title': 'We Turned an M&A Firm’s Past Deal Into Calls With $15M, $25M & $30M '
                                'Companies in the First 7 Days',
                       'channel': 'Ephraim Austin',
                       'author': 'Ephraim Austin',
                       'text': 'The problem with that is it takes at least 6 to 9 months to get any type '
                               'of traction.',
                       'tip': 'The problem with that is it takes at least 6 to 9 months to get any type of '
                              'traction.',
                       'timestamp': 83,
                       'timestamp_seconds': 83,
                       'timestamp_label': '[00:01:23]',
                       'url': 'https://www.youtube.com/watch?v=esA2m5IlLT8&t=83s',
                       'markdown': '[00:01:23](https://www.youtube.com/watch?v=esA2m5IlLT8&t=83s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'esA2m5IlLT8',
                       'title': 'We Turned an M&A Firm’s Past Deal Into Calls With $15M, $25M & $30M '
                                'Companies in the First 7 Days',
                       'channel': 'Ephraim Austin',
                       'author': 'Ephraim Austin',
                       'text': 'The average reply rate is around like 1%.',
                       'tip': 'The average reply rate is around like 1%.',
                       'timestamp': 200,
                       'timestamp_seconds': 200,
                       'timestamp_label': '[00:03:20]',
                       'url': 'https://www.youtube.com/watch?v=esA2m5IlLT8&t=200s',
                       'markdown': '[00:03:20](https://www.youtube.com/watch?v=esA2m5IlLT8&t=200s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PauebGoMxEw',
                       'title': 'The New Way to Source M&A Deals in 2027',
                       'channel': 'Nico Holloman | Hologram Agency',
                       'author': 'Nico Holloman | Hologram Agency',
                       'text': 'And then we just do an opt-out and a signature based on cold email '
                               'CAN-SPAM sending laws, and just like that this exact messaging averaged 12 '
                               'interested responses for every 3,000 outreaches that we sent, which is '
                               'very strong.',
                       'tip': 'And then we just do an opt-out and a signature based on cold email CAN-SPAM '
                              'sending laws, and just like that this exact messaging averaged 12 '
                              'interested responses for every 3,000 outreaches that we sent, which is very '
                              'strong.',
                       'timestamp': 307,
                       'timestamp_seconds': 307,
                       'timestamp_label': '[00:05:07]',
                       'url': 'https://www.youtube.com/watch?v=PauebGoMxEw&t=307s',
                       'markdown': '[00:05:07](https://www.youtube.com/watch?v=PauebGoMxEw&t=307s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PauebGoMxEw',
                       'title': 'The New Way to Source M&A Deals in 2027',
                       'channel': 'Nico Holloman | Hologram Agency',
                       'author': 'Nico Holloman | Hologram Agency',
                       'text': "And anyone who's under a five out of 10 gets automatically cut from the "
                               'list.',
                       'tip': "And anyone who's under a five out of 10 gets automatically cut from the "
                              'list.',
                       'timestamp': 497,
                       'timestamp_seconds': 497,
                       'timestamp_label': '[00:08:17]',
                       'url': 'https://www.youtube.com/watch?v=PauebGoMxEw&t=497s',
                       'markdown': '[00:08:17](https://www.youtube.com/watch?v=PauebGoMxEw&t=497s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'D8UMfxaORrU',
                       'title': 'How it works: Middle Market M&A Deal Sourcing Tool',
                       'channel': 'MergerID',
                       'author': 'MergerID',
                       'text': 'The adviser enters a project anonymously, the system matches buyers by '
                               'sector and size, the adviser shares a teaser, and contacts are exchanged.',
                       'tip': 'The adviser enters a project anonymously, the system matches buyers by '
                              'sector and size, the adviser shares a teaser, and contacts are exchanged.',
                       'timestamp': 40,
                       'timestamp_seconds': 40,
                       'timestamp_label': '[00:00:40]',
                       'url': 'https://www.youtube.com/watch?v=D8UMfxaORrU&t=40s',
                       'markdown': '[00:00:40](https://www.youtube.com/watch?v=D8UMfxaORrU&t=40s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ssgz-uXMi6c',
                       'title': 'What tools should I use for M&A deal sourcing and my deal flow funnel? '
                                "Here's our process.",
                       'channel': 'BN.Digital',
                       'author': 'BN.Digital',
                       'text': 'Repeat visits to a sell-a-business page trigger sales tasks or '
                               'persona-specific campaigns.',
                       'tip': 'Repeat visits to a sell-a-business page trigger sales tasks or '
                              'persona-specific campaigns.',
                       'timestamp': 174,
                       'timestamp_seconds': 174,
                       'timestamp_label': '[00:02:54]',
                       'url': 'https://www.youtube.com/watch?v=ssgz-uXMi6c&t=174s',
                       'markdown': '[00:02:54](https://www.youtube.com/watch?v=ssgz-uXMi6c&t=174s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'p5BRxk-zVCA',
                       'title': 'How Do You Choose the Right Deal Sourcing Provider?',
                       'channel': 'Marco Palmero',
                       'author': 'Marco Palmero',
                       'text': 'Selling a company is a life-changing decision, so look for M&A-specific '
                               'case studies.',
                       'tip': 'Selling a company is a life-changing decision, so look for M&A-specific '
                              'case studies.',
                       'timestamp': 591,
                       'timestamp_seconds': 591,
                       'timestamp_label': '[00:09:51]',
                       'url': 'https://www.youtube.com/watch?v=p5BRxk-zVCA&t=591s',
                       'markdown': '[00:09:51](https://www.youtube.com/watch?v=p5BRxk-zVCA&t=591s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'id39IYEm-oQ',
                       'title': 'M&A Sourcing & Valuation Explained: Proprietary Deals to EBITDA Multiples',
                       'channel': 'One Minute Finance',
                       'author': 'One Minute Finance',
                       'text': 'Remember, in M&A, your sourcing strategy literally is your valuation '
                               'strategy.',
                       'tip': 'Remember, in M&A, your sourcing strategy literally is your valuation '
                              'strategy.',
                       'timestamp': 546,
                       'timestamp_seconds': 546,
                       'timestamp_label': '[00:09:06]',
                       'url': 'https://www.youtube.com/watch?v=id39IYEm-oQ&t=546s',
                       'markdown': '[00:09:06](https://www.youtube.com/watch?v=id39IYEm-oQ&t=546s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dZiHOJKxvoE',
                       'title': 'Mergers and Acquisitions Explained: M&A Deal Origination Secrets',
                       'channel': 'John Colley | The Investment Banking Practitioner',
                       'author': 'John Colley | The Investment Banking Practitioner',
                       'text': 'Look for a reason for sale, such as death, disease, divorce, or '
                               'retirement.',
                       'tip': 'Look for a reason for sale, such as death, disease, divorce, or retirement.',
                       'timestamp': 229,
                       'timestamp_seconds': 229,
                       'timestamp_label': '[00:03:49]',
                       'url': 'https://www.youtube.com/watch?v=dZiHOJKxvoE&t=229s',
                       'markdown': '[00:03:49](https://www.youtube.com/watch?v=dZiHOJKxvoE&t=229s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TE99yv49oy4',
                       'title': 'How We Actually Source M&A Deals: Cold Email, AI, and Tech Stacks',
                       'channel': 'Exxcelerate',
                       'author': 'Exxcelerate',
                       'text': 'A client with a CRM closed a third deal from about 200 to 300 '
                               'opportunities, while a client without one got 400 plus and closed none.',
                       'tip': 'A client with a CRM closed a third deal from about 200 to 300 '
                              'opportunities, while a client without one got 400 plus and closed none.',
                       'timestamp': 1556,
                       'timestamp_seconds': 1556,
                       'timestamp_label': '[00:25:56]',
                       'url': 'https://www.youtube.com/watch?v=TE99yv49oy4&t=1556s',
                       'markdown': '[00:25:56](https://www.youtube.com/watch?v=TE99yv49oy4&t=1556s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kk3kEZ_huBU',
                       'title': 'AI Deal Sourcing Explained: How to Find Off-Market Deals',
                       'channel': 'M&A Synergy AI',
                       'author': 'M&A Synergy AI',
                       'text': "We're talking about going from a typical 40 hours down to just 10.",
                       'tip': "We're talking about going from a typical 40 hours down to just 10.",
                       'timestamp': 297,
                       'timestamp_seconds': 297,
                       'timestamp_label': '[00:04:57]',
                       'url': 'https://www.youtube.com/watch?v=kk3kEZ_huBU&t=297s',
                       'markdown': '[00:04:57](https://www.youtube.com/watch?v=kk3kEZ_huBU&t=297s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'x21Z365qRBM',
                       'title': 'Deal Origination Sourcing | Approaches to Deal Origination',
                       'channel': 'WallStreetMojo',
                       'author': 'WallStreetMojo',
                       'text': 'Online matchmaking platforms are a cheaper option than building in-house '
                               'teams.',
                       'tip': 'Online matchmaking platforms are a cheaper option than building in-house '
                              'teams.',
                       'timestamp': 353,
                       'timestamp_seconds': 353,
                       'timestamp_label': '[00:05:53]',
                       'url': 'https://www.youtube.com/watch?v=x21Z365qRBM&t=353s',
                       'markdown': '[00:05:53](https://www.youtube.com/watch?v=x21Z365qRBM&t=353s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Za2avmXv1RE',
                       'title': 'Deal Origination',
                       'channel': 'Tao Solutions Inc',
                       'author': 'Tao Solutions Inc',
                       'text': 'Deal origination in the LeaseSpark module runs from quotes and '
                               'amortization through the credit approval workflow.',
                       'tip': 'Deal origination in the LeaseSpark module runs from quotes and amortization '
                              'through the credit approval workflow.',
                       'timestamp': 6,
                       'timestamp_seconds': 6,
                       'timestamp_label': '[00:00:06]',
                       'url': 'https://www.youtube.com/watch?v=Za2avmXv1RE&t=6s',
                       'markdown': '[00:00:06](https://www.youtube.com/watch?v=Za2avmXv1RE&t=6s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'T64at1dT1Zs',
                       'title': 'Acquisition Criteria & Proprietary Deal Flow | Buy-Side Masterclass '
                                'Moment',
                       'channel': 'POTOMAC M&A',
                       'author': 'POTOMAC M&A',
                       'text': "You can buy the best company in the world, but if you overpay for it, it's "
                               'still a bad investment.',
                       'tip': "You can buy the best company in the world, but if you overpay for it, it's "
                              'still a bad investment.',
                       'timestamp': 111,
                       'timestamp_seconds': 111,
                       'timestamp_label': '[00:01:51]',
                       'url': 'https://www.youtube.com/watch?v=T64at1dT1Zs&t=111s',
                       'markdown': '[00:01:51](https://www.youtube.com/watch?v=T64at1dT1Zs&t=111s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rOwXkmrMljc',
                       'title': 'Building the AI-Powered M&A Deal Team of 2030 | SS&C Intralinks '
                                '#dealmaking #mergersandacquisitions',
                       'channel': 'SS&C Intralinks',
                       'author': 'SS&C Intralinks',
                       'text': 'And more and more you need to run the extra mile, you know, to come up '
                               'with some additional advice and added value.',
                       'tip': 'And more and more you need to run the extra mile, you know, to come up with '
                              'some additional advice and added value.',
                       'timestamp': 1828,
                       'timestamp_seconds': 1828,
                       'timestamp_label': '[00:30:28]',
                       'url': 'https://www.youtube.com/watch?v=rOwXkmrMljc&t=1828s',
                       'markdown': '[00:30:28](https://www.youtube.com/watch?v=rOwXkmrMljc&t=1828s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2X_myL7Ao9A',
                       'title': 'I Sourced a $50 Million M&A Deal Using AI!',
                       'channel': 'Willem',
                       'author': 'Willem',
                       'text': "They're getting hit up 24/7 with inquiries about, you know, buying their "
                               'business.',
                       'tip': "They're getting hit up 24/7 with inquiries about, you know, buying their "
                              'business.',
                       'timestamp': 122,
                       'timestamp_seconds': 122,
                       'timestamp_label': '[00:02:02]',
                       'url': 'https://www.youtube.com/watch?v=2X_myL7Ao9A&t=122s',
                       'markdown': '[00:02:02](https://www.youtube.com/watch?v=2X_myL7Ao9A&t=122s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PSsr4qdwaj8',
                       'title': 'How AI is Revolutionizing Deal Origination in M&A',
                       'channel': 'Willem',
                       'author': 'Willem',
                       'text': 'We could scale this up to reaching out to 10,000 companies that fit your '
                               'criteria a day.',
                       'tip': 'We could scale this up to reaching out to 10,000 companies that fit your '
                              'criteria a day.',
                       'timestamp': 81,
                       'timestamp_seconds': 81,
                       'timestamp_label': '[00:01:21]',
                       'url': 'https://www.youtube.com/watch?v=PSsr4qdwaj8&t=81s',
                       'markdown': '[00:01:21](https://www.youtube.com/watch?v=PSsr4qdwaj8&t=81s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'}]}
