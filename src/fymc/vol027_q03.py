from __future__ import annotations

CHAPTER_3 = {'id': 'Q3',
 'chapter_id': 'Q3',
 'chapter_number': 3,
 'question_number': 3,
 'slug': 'search-funds-self-funded-search-running-the-search',
 'question_prompt': 'How do traditional search funds and self-funded searchers raise capital, run a '
                    'search, and get a deal to close?',
 'kicker': 'Q3 / THE BIG MONEY PLAYBOOKS',
 'title': 'Search Funds and Self-Funded Search: Running the Search',
 'subtitle': 'Traditional vs. self-funded search models, investor-backed searcher economics, the Harvard '
             "professors' buyer playbook, convincing owners to sell, favored searcher industries, "
             "search-fund financial projections, Booth's search and deal-structuring sessions, legal "
             'guidance for small-business buyers, the 8-stage M&A process, and an ETA reality check on SBA '
             'lending and deal killers',
 'layout_template': 'financial_analysis',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners running and backing searches agree the job is a high-volume '
                      "relationship grind: Pete Seligman's funnel ran 200 companies to 50 IMs to 20 "
                      'conversations to 5 offers to 1 purchase, and Coley Andrews describes thousands of '
                      'outreaches for one deal. Targets are healthy, cash-generative, recurring-revenue '
                      'businesses priced around 4-6x cash flow, financed with roughly half bank debt plus '
                      'seller notes and equity. Traditional funds raise about $400-700K of search capital '
                      'for a two-year runway and hand the searcher 20-30% equity in thirds; self-funded '
                      'searchers keep 60-73% but carry the runway themselves. The sharpest split is Robert '
                      "Graham versus Greg Geronimus on whether traditional capital is a win-win or 'more "
                      "expensive than a payday loan,' while Peter and Garrett reject mass broker spam in "
                      'favor of authentic follow-ups every couple of weeks.',
 'key_metrics': [{'label': 'Search-to-purchase funnel',
                  'metric': 'Search-to-purchase funnel',
                  'value': 'About 200 companies to 50 IMs to 20 conversations to 5 offers to 1 purchase',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Pete Seligman's own sourcing funnel before buying SRO, worked through online "
                             'and offline brokers.',
                  'source': 'David Nazeem Aboud ([_exEOi-Wxuk @ 00:15:24])'},
                 {'label': 'Median search capital raise',
                  'metric': 'Median search capital raise',
                  'value': '$500-550K median; $400-700K typical; $800-900K for two searchers',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Peter Harris on traditional search capital covering about two years of '
                             'salary, interns, legal, travel, bankers and diligence.',
                  'source': 'VCPete ([i_Ownd9smbk @ 00:02:31])'},
                 {'label': 'LOIs per closed self-funded acquirer',
                  'metric': 'LOIs per closed self-funded acquirer',
                  'value': '6.9 LOIs submitted, 2.4 executed',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Robert Graham and Jordan Carter's survey of 270+ self-funded searchers; "
                             'median find-to-close time was 4-6 months.',
                  'source': 'Acquiring Minds ([KT5T3j2jVQ4 @ 00:45:01])'},
                 {'label': 'Lender DSCR floor',
                  'metric': 'Lender DSCR floor',
                  'value': 'At least 1.25; sample model shows 4.64 in year one',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Adam of ProjectionHub on the debt service coverage ratio lenders expect in a '
                             'search fund acquisition model.',
                  'source': 'ProjectionHub ([uXEbfHnDSes @ 00:01:53])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every operator who has actually closed describes the search as a volume '
                              'business that only converts through relationships. Pete Seligman and a '
                              'partner each pitched the other five business ideas every Sunday night, then '
                              'worked a funnel of roughly 200 companies down to 50 IMs read, 20 owners '
                              "spoken to, five offers and one purchase: 'we probably spoke to 20, put in "
                              "five offers, and bought one' [_exEOi-Wxuk @ 00:15:42]. Peter and Garrett, "
                              "who closed an HVAC business after 13 months, put it bluntly: 'it's simple "
                              "but it's a numbers game,' with Garrett grinding 15-20 broker calls a day "
                              '[Hh83Lc7sWf4 @ 00:22:15]. Coley Andrews of Pacific Lake Partners scales the '
                              'same math upward: thousands of outreaches, hundreds of conversations and '
                              'tens of meetings to buy one company, with about 90% of each day spent '
                              "absorbing rejection [_rMBWgqtfUI @ 00:05:47]. Brian O'Connor of NextGen "
                              'Growth Partners lands in the same place after building trade-show target '
                              "lists: 'at the end of the day, I think it is a numbers game in this path' "
                              '[ccaGmVeLcto @ 00:36:46]. The volume only matters because the close itself '
                              "is relational; Peter called it 'not a finance game' but a trust game, with "
                              'the seller still dropping in about three times a week after the contract '
                              'ended.',
                              'The buy box is remarkably consistent across funded and self-funded '
                              'operators: healthy, cash-generative, boring businesses that nobody needs to '
                              'rescue. Tim Ludwig wants industry growth at least at GDP, recurring or '
                              "'actuarially recurring' revenue, gross margins of 50% or higher, and growth "
                              "already underway, because 'it's hard enough as it is why not why try and "
                              "make it any harder than you have to' [AWJaRrNXru8 @ 00:01:24]. Coley "
                              'Andrews frames the same rule as risk control for inexperienced CEOs: buy '
                              "companies that are 'unlikely to be broken' and sold by owners in their 60s "
                              "or 70s with no successor child [_rMBWgqtfUI @ 00:01:17]. Brian O'Connor's "
                              'preferred list reads like a checklist: recurring revenue, mission-critical '
                              'product, low share of wallet, B2B over B2C, asset-light, and negative '
                              'working capital [ccaGmVeLcto @ 00:42:07]. Pete Seligman screened for no '
                              'customer or product concentration, stable earnings and good cash '
                              'conversion, and specifically wanted blue-chip customers issuing purchase '
                              "orders directly rather than sitting 'five layers down' a supply chain "
                              "[_exEOi-Wxuk @ 00:17:28]. Peter and Garrett's HVAC search ran almost the "
                              'identical filter: recurring revenue, low customer concentration, stable '
                              'margin, stable EBITDA and a non-cyclical industry.',
                              'The baseline prerequisite is runway. Greg Geronimus describes traditional '
                              'search capital as money that covers salary and operating costs for two '
                              'years before a second raise funds the deal, and Robert Graham states flatly '
                              'that self-funded search does not fit anyone who cannot fund two years of '
                              'searching [0lg8Gh_uAPU @ 00:54:24]. Peter Harris prices that runway at a '
                              'typical $400-700K raise with a median of $500-550K, of which $100-200K is '
                              'searcher salary and the remaining $300K-plus goes to interns, legal, '
                              'travel, bankers and diligence [i_Ownd9smbk @ 00:02:13]. Lenders demand the '
                              'same staying power at the closing table: Jared Johnson, billed as the top '
                              'SBA lender in the country, looks for liquidity well beyond the 10% down '
                              'payment, experience mapped against the target, other income, and personal '
                              'saving habits [pqmsev-3MPY @ 00:11:43]. The last shared conviction is how a '
                              'searcher actually wins. Steve Divitikos, who closed in Toronto after just '
                              "under two years, won over father-and-son founders who had developed 'a high "
                              "distaste for private Equity' by presenting as 'a succession plan that's "
                              "looking for the right business to succeed,' with a portfolio of one, a "
                              'promise to keep the company name, and 99.9% of personal net worth riding on '
                              'the deal [GYvpRW21sSY @ 00:00:59]. Price and structure only had to be good '
                              'enough; the qualitative factors closed it.'],
               'table': {'caption': 'Where searchers, investors and lenders line up on running the search',
                         'headers': ['Consensus Point',
                                     'What Practitioners Do',
                                     'Why It Matters',
                                     'Expert Source'],
                         'rows': [['High-volume outreach is the core daily search activity',
                                   'Funnel roughly 200 companies into 50 IMs, 20 conversations, 5 offers',
                                   'Only sheer volume reliably produces a single closed acquisition at the '
                                   'end',
                                   'David Nazeem Aboud ([_exEOi-Wxuk @ 00:15:24])'],
                                  ['Buy healthy businesses that are unlikely to be broken',
                                   'Target owners in their 60s or 70s with no successor child',
                                   "Healthy targets offset the searcher's lack of operating experience as "
                                   'CEO',
                                   'Stanford Graduate School of Business ([_rMBWgqtfUI @ 00:01:17])'],
                                  ['Screen for growth, recurring revenue and fat gross margins',
                                   'Require GDP-plus industry growth, recurring revenue, 50% or higher '
                                   'gross margin',
                                   'No bonus points for degree of difficulty; turnarounds are harder to '
                                   'run',
                                   'POWERS Pod ([AWJaRrNXru8 @ 00:00:34])'],
                                  ['Avoid concentration and demand clean cash conversion in targets',
                                   'Reject customer or product concentration; want direct blue-chip '
                                   'purchase orders',
                                   'Stable earnings and cash conversion fund debt service and working '
                                   'capital',
                                   'David Nazeem Aboud ([_exEOi-Wxuk @ 00:17:01])'],
                                  ['Fund roughly two full years of search runway up front',
                                   'Traditional raises pay salary and costs; self-funders cover it '
                                   'personally',
                                   'Self-funded search does not fit anyone who cannot fund two years',
                                   'Acquiring Minds ([0lg8Gh_uAPU @ 00:54:24])'],
                                  ['Price the business off a multiple of cash flow',
                                   'Use about 4x cash flow, maybe 5x for larger firms',
                                   'Value comes from cash flow, not from what the seller wants',
                                   'Built to Sell ([004ptgWQ2TE @ 00:05:24])'],
                                  ['Win the seller on relationship, not on top bid',
                                   'Pitch as a succession plan once price and structure clear the bar',
                                   'Searchers rarely win as highest bidder; sellers choose them '
                                   'relationally',
                                   'The University of Chicago Booth School of Business ([kKwXdeUVNOw @ '
                                   '00:24:22])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Sourcing runs on two engines: brokers and proprietary lists. Peter and '
                              'Garrett split the labor, with Garrett making 15-20 broker calls a day while '
                              'Peter systematized a deal tracker that took six to seven months to refine '
                              '[Hh83Lc7sWf4 @ 00:22:01]. Their broker list snowballed from about 10 to '
                              '500, and instead of blasting thousands of brokers they followed up with '
                              "every broker every couple of weeks in emails that 'sounded authentic'; "
                              '40-50 brokers ended up knowing them by name, which matters because brokers '
                              'filter buyers too [Hh83Lc7sWf4 @ 00:23:59]. The proprietary engine is cheap '
                              'labor plus lists. Peter Harris describes intern armies at $10-15 an hour '
                              "'smiling and dialing,' or a sector thesis such as personal care or an HVAC "
                              "roll-up [i_Ownd9smbk @ 00:03:55]. Brian O'Connor works trade-show exhibitor "
                              'lists of about 1,000 companies, uses interns for research, and narrows to '
                              '200-400 targets after scoring roughly three industry spaces on a weighted '
                              'attribute scorecard covering growth, fragmentation, cyclicality, a TAM of '
                              'about $1B per niche, and low operational complexity [ccaGmVeLcto @ '
                              "00:36:46]. Once deal flow is running, the cadence compounds: Peter's team "
                              'read about five SIMs a week early, saw the first LOI die after about three '
                              'months, and after six months always had one or two deals under contract.',
                              "The pricing and capital-stack math is standardized. Built to Sell's Harvard "
                              "guest values targets at 'somewhere around four times' cash flow, maybe five "
                              'for larger firms, so a $10M company carries roughly $2-2.5M of cash flow. '
                              'On that $10M deal, the bank lends about 50%, or about $5M repaid over '
                              'roughly seven years, usually without a personal guarantee at that size; a '
                              'seller note of $1-2.5M sits subordinated and pays over about four years '
                              'with interest; and investors supply about $3M of equity [004ptgWQ2TE @ '
                              "00:06:38]. Brian O'Connor benchmarks purchase prices at 4-6x TTM EBITDA "
                              'with $5-10M of acquisition equity [ccaGmVeLcto @ 00:45:37]. In the SBA '
                              'lane, Jared Johnson requires 10% down on the total project, meaning price '
                              'plus working capital, closing and diligence costs; a seller can carry half '
                              'of that on full standby, typically no payments for 10 years, but the buyer '
                              'still needs at least 5% [pqmsev-3MPY @ 00:06:14]. Adam of ProjectionHub '
                              'models the coverage test: lenders want a DSCR of at least 1.25, and the '
                              "template's example, built from a $5M SBA 7(a) loan, a $500K seller note and "
                              '$5M of search-fund equity with $500K earmarked for working capital, reaches '
                              'a $10M purchase price and shows 4.64 in year one [uXEbfHnDSes @ 00:01:53].',
                              'After the LOI, the clock and the paperwork take over. The Harvard guest on '
                              'Built to Sell signs the LOI before financing is lined up, budgets 2-4 weeks '
                              'of business diligence, 1-3 weeks to collect bank proposals and about six '
                              "weeks for the bank's own process, and stresses that the no-shop clause, "
                              "usually 90 days, is 'in fact the only binding part of the agreement' "
                              '[004ptgWQ2TE @ 00:16:54]. Laura D. Franchesco of Dean Street Law adds that '
                              "confidentiality and deposits bind too, so an LOI is 'not entirely "
                              "non-binding' [ScOjsEfBwZQ @ 00:22:50]. Josh Dennis and Brian O'Connor close "
                              "in 60-90 days, 'typically 75 days on average,' 30-45 when rushed and "
                              '120-plus when it drags, and they negotiate buffer into exclusivity, such as '
                              'a 60-day close under 90-day exclusivity [kKwXdeUVNOw @ 00:45:15]. They '
                              'issue the data-request list the moment the LOI is signed, run good cop/bad '
                              "cop, insist on 'the power of the pen' by drafting the purchase agreement, "
                              'and do business diligence in-house before hiring a QoE firm to keep '
                              'dead-deal costs near zero. Robert Graham and Jordan Carter put real prices '
                              'on that work: typical QoE runs $10-25K and legal $25-30K, 85% of surveyed '
                              'self-funded acquirers spent under $30K on QoE, 68% spent under $50K on '
                              'legal, and 75% ate under $25K in dead-deal costs [KT5T3j2jVQ4 @ 00:51:02].'],
               'table': {'caption': 'Search-phase mechanics, price points and timelines operators actually '
                                    'use',
                         'headers': ['Mechanic',
                                     'Exact Number or Tool',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Traditional search capital raise sized for two years',
                                   '$400-700K typical; $500-550K median; $800-900K for two searchers',
                                   'Funds $100-200K salary plus interns, legal, travel, bankers, diligence',
                                   'VCPete ([i_Ownd9smbk @ 00:02:31])'],
                                  ['Intern-powered proprietary dialing operation for outreach',
                                   'Intern armies paid $10-15 per hour smiling and dialing',
                                   'Cheap labor pushes outreach volume against a defined sector thesis',
                                   'VCPete ([i_Ownd9smbk @ 00:03:55])'],
                                  ['Trade-show target list construction method',
                                   'Mine exhibitor lists of about 1,000 companies down to 200-400',
                                   'Interns research the list after scoring about three industry spaces',
                                   'The University of Chicago Booth School of Business ([ccaGmVeLcto @ '
                                   '00:36:46])'],
                                  ['Senior bank debt in a $10M deal',
                                   'About 50% of price, roughly $5M, repaid over about seven years',
                                   'Usually no personal guarantee at this size; seller note subordinated '
                                   'behind',
                                   'Built to Sell ([004ptgWQ2TE @ 00:06:38])'],
                                  ['SBA equity injection on the total project',
                                   '10% down on price plus working capital, closing and diligence costs',
                                   'Seller can carry half on full standby; buyer still needs 5%',
                                   'Before You Buy or Sell a Business Podcast ([pqmsev-3MPY @ 00:06:14])'],
                                  ['Lender debt service coverage floor in projections',
                                   'DSCR of at least 1.25; sample model shows 4.64 in year one',
                                   'Five-year monthly model proves the debt is serviceable before lenders '
                                   'see it',
                                   'ProjectionHub ([uXEbfHnDSes @ 00:01:53])'],
                                  ['LOI-to-close timeline and exclusivity buffer',
                                   '60-90 days, about 75 on average; 120-plus when deals drag',
                                   'Negotiate 90-day exclusivity around a 60-day target close for slack',
                                   'The University of Chicago Booth School of Business ([kKwXdeUVNOw @ '
                                   '00:45:15])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'What closers do that the Twitter playbooks skip',
                           'body': 'Four moves operators credit for getting deals sourced, won and papered '
                                   'on their terms.',
                           'items': ['Skip the mass broker blast: follow up with every broker every couple '
                                     'of weeks in emails that sound authentic, and let the list snowball '
                                     'from 10 to 500 [Before You Buy or Sell a Business Podcast — '
                                     'Hh83Lc7sWf4 @ 00:23:59]',
                                     'Sell yourself as the succession plan: a portfolio of one, a promise '
                                     'to keep the company name, and 99.9% of your net worth tied to the '
                                     'outcome won founders who distrusted private equity [Built to Sell — '
                                     'GYvpRW21sSY @ 00:01:13]',
                                     'Take the power of the pen by drafting the purchase agreement '
                                     'yourself, and do not be afraid to blame your service providers to '
                                     'keep data requests moving [The University of Chicago Booth School of '
                                     'Business — kKwXdeUVNOw @ 00:26:05]',
                                     'Hunt for sellers still growing without a salesperson; hiring the '
                                     'right one is the easy upside lever [POWERS Pod — AWJaRrNXru8 @ '
                                     '00:01:50]']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock the thesis and build the target list',
                              'action': 'Score industries on a weighted attribute scorecard, pick about '
                                        'three spaces, and turn trade-show exhibitor lists into 200-400 '
                                        'targets.',
                              'detail': 'Filter for growing, fragmented, non-cyclical niches with no '
                                        '800-pound gorilla and about $1B TAM, then use interns to research '
                                        'roughly 1,000 exhibitors down to the target list [The University '
                                        'of Chicago Booth School of Business — ccaGmVeLcto @ 00:15:59]'},
                             {'step': 2,
                              'title': 'Run the daily broker and outreach cadence',
                              'action': 'Make 15-20 broker calls a day while a partner systematizes the '
                                        'deal tracker.',
                              'detail': 'Peter and Garrett refined their tracker over six to seven months, '
                                        'reviewed about five SIMs a week early, and after six months '
                                        'always had one or two deals under contract [Before You Buy or '
                                        'Sell a Business Podcast — Hh83Lc7sWf4 @ 00:22:01]'},
                             {'step': 3,
                              'title': 'Model the deal before the LOI',
                              'action': 'Build a five-year monthly projection with the full capital stack '
                                        'and confirm DSCR clears 1.25.',
                              'detail': 'Match the projection start year to the acquisition year because '
                                        'date handling is finicky, edit only the blue assumption cells, '
                                        'and hold expenses at a percentage of revenue for a conservative '
                                        'case [ProjectionHub — uXEbfHnDSes @ 00:06:02]'},
                             {'step': 4,
                              'title': 'Sign the LOI with buffer and fire the data request',
                              'action': 'Negotiate exclusivity longer than the target close and send the '
                                        'data-request list the moment the LOI is signed.',
                              'detail': 'Target a 60-day close under 90-day exclusivity, expect about 75 '
                                        'days on average, and set data expectations immediately to blunt '
                                        'deal fatigue [The University of Chicago Booth School of Business '
                                        '— kKwXdeUVNOw @ 00:45:15]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split in search is who owns the equity. In the live Acquiring '
                              'Minds debate, Greg Geronimus laid out the traditional deal: the searcher '
                              'earns 25 percent in thirds, with one third at close, one vesting over about '
                              'four years, and one tied to performance hurdles [0lg8Gh_uAPU @ 00:10:12]. '
                              'Robert Graham attacked that last tranche, arguing a searcher has to return '
                              "25 to 35 percent IRR to earn it, a hurdle 'over four times higher' than "
                              'what LPs expect from a private equity firm, and adding that they have never '
                              'been able to deposit a percentage of common equity in the bank [0lg8Gh_uAPU '
                              "@ 00:17:15]. Robert's counter-numbers: Sig searchers average 73 percent "
                              'ownership of businesses with $2.6M average EBITDA, while traditional '
                              'searchers hold 10 percent or less at close of a median $1.8M EBITDA '
                              'business [0lg8Gh_uAPU @ 00:12:55]. The wider self-funded survey shows 86 '
                              'percent keeping more than 60 percent of the common equity [KT5T3j2jVQ4 @ '
                              '00:24:04]. The Harvard view lands in the same place: funded searchers carry '
                              'up to 30 percent, more likely 20, while unfunded searchers may hold 60 to '
                              "70 percent [004ptgWQ2TE @ 00:11:26]. Greg's rebuttal is scale, with 46 "
                              'percent of traditional deals above $12M TEV against a $3M to $8M '
                              'self-funded range [0lg8Gh_uAPU @ 00:08:43].',
                              'Sourcing splits into volume machines versus relationship plays. Pete '
                              'Seligman tried wining and dining brokers and found it failed because '
                              'brokers were not proactive [_exEOi-Wxuk @ 00:14:26], while noting that some '
                              'current searchers source 2,000 businesses a month and make hundreds of '
                              'calls a week [_exEOi-Wxuk @ 00:15:24]. Peter Harris describes the '
                              "hired-volume version: intern armies at $10 to $15 an hour 'smiling and "
                              "dialing,' or a sector thesis such as personal care or an HVAC roll-up "
                              "[i_Ownd9smbk @ 00:03:55]. Brian O'Connor at Booth runs the thesis version, "
                              'working trade-show exhibitor lists of about 1,000 companies down to 200 to '
                              "400 targets and calling it 'a numbers game in this path' [ccaGmVeLcto @ "
                              '00:36:46]. Peter and Garrett, who closed an HVAC deal after 13 months, '
                              'explicitly reject spamming thousands of brokers. Their list snowballed from '
                              '10 to 500, and every broker got a follow-up every couple of weeks in emails '
                              'written to sound authentic [Hh83Lc7sWf4 @ 00:23:27], while Garrett made 15 '
                              'to 20 broker calls a day and Peter systematized the tracker [Hh83Lc7sWf4 @ '
                              '00:22:01]. The payoff was 40 to 50 brokers who came to know them, and those '
                              'brokers filter buyers too [Hh83Lc7sWf4 @ 00:25:20]. The real fork is not '
                              'volume versus no volume; it is automated blast versus personal cadence.',
                              'Practitioners also split on what a buyer must bring before day one. Coley '
                              "Andrews of Pacific Lake Partners says flatly, 'We believe in backing smarts "
                              "and hustle, not experience' [_rMBWgqtfUI @ 00:00:54], and offsets the gap "
                              'by buying healthy businesses that are unlikely to be broken [_rMBWgqtfUI @ '
                              '00:01:17]. Jared Johnson, billed as the top SBA lender in the country, '
                              'wants the opposite profile: someone who has worked in consulting, PE, IB, '
                              'or up through a company, managed people, saved money, and targets an '
                              'adjacent industry [pqmsev-3MPY @ 00:05:02]. The Harvard buyer profile sits '
                              'between them, with 7 to 15 years of management experience that is usually '
                              'outside the target industry [004ptgWQ2TE @ 00:01:33]. The two debaters even '
                              'agree on who each model excludes. Greg Geronimus concedes traditional '
                              'search does not fit narrow-geography searchers or anyone weighing a startup '
                              '[0lg8Gh_uAPU @ 00:51:39], after earlier conceding a narrow Milwaukee search '
                              'will not work in the traditional model [0lg8Gh_uAPU @ 00:30:14]. Robert '
                              'Graham concedes self-funded search does not fit anyone who cannot fund two '
                              "years of searching [0lg8Gh_uAPU @ 00:54:24]. Coley's investor math frames "
                              'the trade from the other side: $30K to $50K per searcher buys two years of '
                              "runway, and even with some chance of losing that small amount, '75 out of a "
                              "100 is still pretty good' [_rMBWgqtfUI @ 00:05:15]."],
               'table': {'caption': 'Traditional, Self-Funded and Hybrid Playbooks Side by Side',
                         'headers': ['Decision Point',
                                     'Playbook A (Who Argues It)',
                                     'Playbook B (Who Argues It)',
                                     'Expert Source'],
                         'rows': [['Searcher equity and how it gets earned',
                                   'Greg Geronimus: 25 percent in thirds, one at close, one vesting about '
                                   'four years, one on hurdles',
                                   'Robert Graham: Sig searchers average 73 percent ownership; the hurdle '
                                   'tranche needs 25 to 35 percent IRR',
                                   'Acquiring Minds ([0lg8Gh_uAPU @ 00:10:12]); Acquiring Minds '
                                   '([0lg8Gh_uAPU @ 00:17:15])'],
                                  ['Leverage and purchase multiple on the deal',
                                   'Traditional model: Stanford median purchase multiple of six times with '
                                   '50 to 60 percent debt',
                                   'Self-funded model: four times at 90 percent LTV yields the same DSCR, '
                                   'per Robert Graham',
                                   'Acquiring Minds ([0lg8Gh_uAPU @ 00:36:08])'],
                                  ['Broker coverage strategy during the search',
                                   'Volume searchers source 2,000 businesses a month and make hundreds of '
                                   'calls every week',
                                   'Peter and Garrett reject spamming: a 10-to-500 list with authentic '
                                   'follow-ups every couple weeks',
                                   'David Nazeem Aboud ([_exEOi-Wxuk @ 00:15:24]); Before You Buy or Sell '
                                   'a Business Podcast ([Hh83Lc7sWf4 @ 00:23:27])'],
                                  ['Deferred seller consideration at close',
                                   'Seller note: 45 percent of acquirers used one, and 56 percent of notes '
                                   'charge six percent or more',
                                   'Jordan Carter used an 18-month escrow instead of any seller note at '
                                   'all',
                                   'Acquiring Minds ([KT5T3j2jVQ4 @ 00:56:34]); Acquiring Minds '
                                   '([KT5T3j2jVQ4 @ 01:01:09])'],
                                  ['Search vehicle without a top-school credential',
                                   'Accelerators like Broadtree and NextGen Growth train you and source '
                                   'deals, but keep a strong say',
                                   'Peter Harris: lacking the credential, go the SBA loan or personal '
                                   'savings route instead',
                                   'VCPete ([i_Ownd9smbk @ 00:09:13]); VCPete ([i_Ownd9smbk @ 00:07:47])'],
                                  ['Debt flavor used to fund the acquisition',
                                   'NextGen prefers flexible debt with no amortization and looser '
                                   'covenants, at a higher cash interest cost',
                                   'SBA route: 10 percent down, seller may carry half on full standby, '
                                   'buyer still needs five percent',
                                   'The University of Chicago Booth School of Business ([kKwXdeUVNOw @ '
                                   '00:53:13]); Before You Buy or Sell a Business Podcast ([pqmsev-3MPY @ '
                                   '00:05:56])'],
                                  ['What the buyer must bring on day one',
                                   'Coley Andrews backs smarts and hustle, not experience, and buys '
                                   'healthy businesses unlikely to be broken',
                                   'Jared Johnson wants consulting, PE, IB or operating experience aimed '
                                   'at an adjacent industry',
                                   'Stanford Graduate School of Business ([_rMBWgqtfUI @ 00:00:54]); '
                                   'Before You Buy or Sell a Business Podcast ([pqmsev-3MPY @ '
                                   '00:05:02])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The first economics check is attrition. One of the Sig study presenters, '
                              "drawing on time at a PE firm, said an executed LOI there carried 'north of "
                              "a 75 percent chance' of closing, and 'that's just not the case here' "
                              '[KT5T3j2jVQ4 @ 00:40:09]. The self-funded survey shows the average acquirer '
                              'submitted 6.9 LOIs to get 2.4 executed [KT5T3j2jVQ4 @ 00:45:01]. Pete '
                              "Seligman's own funnel ran about 200 companies, 50 IMs read, 20 "
                              'conversations, five offers, and one purchase [_exEOi-Wxuk @ 00:15:42]. '
                              "Peter and Garrett's first LOI landed at about three months and died a week "
                              'later; only after roughly six months did they hold one or two deals under '
                              'contract at all times [Hh83Lc7sWf4 @ 00:20:17], and the partners tell '
                              "searchers to expect to 'fail about 200 times' [Hh83Lc7sWf4 @ 00:27:36]. "
                              "Jared Johnson watches searchers drift toward 'junk' deals eight or nine "
                              "months in and refuses to finance them with a blunt 'I forbid you' "
                              "[Hh83Lc7sWf4 @ 00:28:05]. Brian O'Connor names the two behavioral traps "
                              'around that curve: sitting on your hands early in the search [ccaGmVeLcto @ '
                              '00:28:59] and tunnel vision once a deal is under LOI [ccaGmVeLcto @ '
                              "00:30:36]. Brian's reason: 'time when you're doing this, you'll find is "
                              "your most scarce resource' [ccaGmVeLcto @ 00:25:54].",
                              'The second check is whether the numbers and the seller are real. Jared '
                              "Johnson says the biggest deal-killer is usually that 'the cash flow doesn't "
                              "work,' followed by red flags such as broker numbers that exceed tax returns "
                              "or the QoE, low buyer cash, remote operators who show up 'once a month for "
                              "a week,' and one or two customers dominating revenue [pqmsev-3MPY @ "
                              "00:09:02]. Jared's own first deal shows the cost of a prior owner's "
                              'behavior: the bankrupt manufacturer had pre-collected customer payments, so '
                              'the buying group put in $700,000 just to finish products for customers who '
                              "had already paid [pqmsev-3MPY @ 00:25:33]. Robert Graham's first Pillar "
                              'deal was the exception to a 78 percent positive seller-relationship rate, '
                              'ending in an IRS fines letter, police involvement, and a lawsuit '
                              "[KT5T3j2jVQ4 @ 01:04:14]. Tim Ludwig's rule: a gut red flag about the "
                              'seller usually means problems elsewhere in the organization too '
                              '[AWJaRrNXru8 @ 00:03:03]. Laura D. Franchesco adds the legal traps: an LOI '
                              "is 'not entirely non-binding,' because exclusivity, confidentiality, and "
                              'deposits bind [ScOjsEfBwZQ @ 00:22:50], and a waste-management acquisition '
                              'must be a stock purchase with license transfer checked [ScOjsEfBwZQ @ '
                              "00:22:34]. Jared's adviser fix is to hire an acquisition specialist whose "
                              'career this is, not a family-law or real-estate attorney [pqmsev-3MPY @ '
                              '00:19:28].',
                              'The third check is the first year after close, where practitioners report '
                              'self-inflicted wounds. Pete Seligman ran an icebreaker at a strategy day '
                              "that caused the owner to walk out, concluding 'application is everything' "
                              "[_exEOi-Wxuk @ 00:29:30]. Pete's travel business lost to online wholesalers "
                              "and exited around 2019 without a loss, summed up as 'can't fight a market' "
                              '[_exEOi-Wxuk @ 00:42:22]. The Harvard list of failure modes covers external '
                              'shocks, fixing broken businesses, mistiming cyclical bottoms, due diligence '
                              "mistakes, and growth plays that amount to 'bolting a startup' onto the "
                              'company [004ptgWQ2TE @ 00:48:45]; the counter is to avoid big, '
                              'hard-to-reverse decisions in year one [004ptgWQ2TE @ 00:50:29]. Coley '
                              "Andrews compresses the transition plan into 'do nothing,' holding off on a "
                              'sales force, new segments, or senior hires until 12 to 18 months in '
                              '[_rMBWgqtfUI @ 00:04:07]. Peak Frameworks puts the downside in aggregate: '
                              '31 percent of searchers never acquire and 29 percent of acquirers sustain a '
                              'loss, which the speaker combines into roughly a 50 percent failure rate, '
                              'alongside single-company idiosyncratic risk [0KhOZrLBMVQ @ 00:03:12]. The '
                              "same speaker flags the timing collision with family plans in a searcher's "
                              'late 20s or early 30s [0KhOZrLBMVQ @ 00:04:52].'],
               'table': {'caption': 'Firsthand Failure Modes and the Economics Check Each One Demands',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Economics Check Practitioners Apply',
                                     'Expert Source'],
                         'rows': [['Prior owner pre-collected customer cash before the sale',
                                   "Jared's group bought a bankrupt manufacturer and put in $700,000 to "
                                   'finish already-paid products',
                                   'Never skip due diligence and quality of earnings; the buyer-mistakes '
                                   'list starts there',
                                   'Before You Buy or Sell a Business Podcast ([pqmsev-3MPY @ 00:25:33]); '
                                   'Before You Buy or Sell a Business Podcast ([pqmsev-3MPY @ 00:18:48])'],
                                  ['Search fatigue pushes buyers into junk deals',
                                   'Searchers drift to junk deals eight to nine months in, and Jared '
                                   'refuses to finance them',
                                   'Expect to fail about 200 times rather than lowering the bar on '
                                   'criteria',
                                   'Before You Buy or Sell a Business Podcast ([Hh83Lc7sWf4 @ 00:28:05]); '
                                   'Before You Buy or Sell a Business Podcast ([Hh83Lc7sWf4 @ 00:27:36])'],
                                  ['Dead-deal costs bleed the search budget dry',
                                   '75 percent of self-funded acquirers kept dead-deal costs under $25K; '
                                   'QoE typically runs $10-25K',
                                   'Do the business diligence yourself before hiring QoE; repeat providers '
                                   'discount or defer fees',
                                   'Acquiring Minds ([KT5T3j2jVQ4 @ 00:50:03]); The University of Chicago '
                                   'Booth School of Business ([kKwXdeUVNOw @ 00:07:50])'],
                                  ['Working capital swallows the first months of cash',
                                   "SRO's first-month revenue of $138,000 went straight back out as "
                                   'working capital',
                                   'Model receivables days, inventory as a percent of sales, and payables '
                                   'days before close',
                                   'David Nazeem Aboud ([_exEOi-Wxuk @ 00:21:17]); ProjectionHub '
                                   '([uXEbfHnDSes @ 00:06:52])'],
                                  ['Seller relationship turns hostile after the close',
                                   "Robert's first Pillar deal brought an IRS fines letter, police "
                                   'involvement and a lawsuit',
                                   'Tim Ludwig requires an honest seller; one gut red flag signals '
                                   'problems elsewhere',
                                   'Acquiring Minds ([KT5T3j2jVQ4 @ 01:04:14]); POWERS Pod ([AWJaRrNXru8 @ '
                                   '00:03:03])'],
                                  ['Negotiating leverage evaporates once exclusivity starts',
                                   'Most deals die or get repriced at the LOI and exclusivity stage of the '
                                   'process',
                                   'Negotiate a buffer, for example a 60-day close inside 90-day '
                                   'exclusivity',
                                   'THE M&A DESK ([MvN2Q7SWbgY @ 00:06:06]); The University of Chicago '
                                   'Booth School of Business ([kKwXdeUVNOw @ 00:45:15])'],
                                  ['Thin debt coverage once the owner salary comes out',
                                   "Without other income, lenders deduct the buyer's salary straight from "
                                   'business cash flow',
                                   'Hold DSCR at or above 1.25; the sample model showed 4.64 in year one',
                                   'Before You Buy or Sell a Business Podcast ([pqmsev-3MPY @ 00:13:14]); '
                                   'ProjectionHub ([uXEbfHnDSes @ 00:01:53])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Kill-or-Proceed Checks Before You Sign',
                           'body': 'Every check below comes from a deal that blew up, nearly blew up, or '
                                   'got repriced on these operators. Clear all four before the LOI or '
                                   'walk.',
                           'items': ['Run cash flow after deducting your own salary and kill the deal if '
                                     'coverage falls below the 1.25 DSCR lenders expect [Before You Buy or '
                                     'Sell a Business Podcast — pqmsev-3MPY @ 00:13:14] [ProjectionHub — '
                                     'uXEbfHnDSes @ 00:01:53].',
                                     'Ask the seller why they are selling, again and again, and walk on '
                                     'any gut red flag about honesty [Before You Buy or Sell a Business '
                                     'Podcast — pqmsev-3MPY @ 00:18:48] [POWERS Pod — AWJaRrNXru8 @ '
                                     '00:03:03].',
                                     'Treat LOI exclusivity, confidentiality and deposits as binding, and '
                                     'negotiate exclusivity longer than the planned close [Dean Street Law '
                                     '— ScOjsEfBwZQ @ 00:22:50] [The University of Chicago Booth School of '
                                     'Business — kKwXdeUVNOw @ 00:45:15].',
                                     'Freeze big, hard-to-reverse changes in year one and hold the '
                                     "transition to 'do nothing' for 12 to 18 months [Built to Sell — "
                                     '004ptgWQ2TE @ 00:50:29] [Stanford Graduate School of Business — '
                                     '_rMBWgqtfUI @ 00:04:07].']}}],
 'pull_quote': "'This isn't VC, you don't have to knock it out of the park, you just have to not let it go "
               "off a cliff.' — Acquiring Minds (KT5T3j2jVQ4 @ 00:30:45)",
 'diagram_id': 'diag-03',
 'action_checklist': ['Before committing, talk to successful buyers first and then a trusted lender '
                      '[Before You Buy or Sell a Business Podcast — pqmsev-3MPY @ 00:23:20].',
                      'Pick about three spaces using a weighted scorecard: growing, fragmented, '
                      'non-cyclical, roughly $1B TAM, low operational complexity [The University of '
                      'Chicago Booth School of Business — ccaGmVeLcto @ 00:15:59].',
                      'Build a broker list and follow up with every broker every couple of weeks in emails '
                      'that sound authentic [Before You Buy or Sell a Business Podcast — Hh83Lc7sWf4 @ '
                      '00:23:59].',
                      'Build a five-year monthly projection with DSCR of at least 1.25 and a start year '
                      'matching the acquisition year [ProjectionHub — uXEbfHnDSes @ 00:06:02].',
                      'Set data-request expectations right after the LOI is signed and run good cop/bad '
                      'cop with your service providers [The University of Chicago Booth School of Business '
                      '— kKwXdeUVNOw @ 00:21:07].',
                      'Pitch the founder as a succession plan: a portfolio of one, the company name kept, '
                      'and your net worth tied to the asset [Built to Sell — GYvpRW21sSY @ 00:00:59].'],
 'statutory_citations': [{'title': 'Acquiring Minds — The Self Funded Search Model | Robert Graham & '
                                   'Jordan carter [00:22:42]',
                          'url': 'https://www.youtube.com/watch?v=KT5T3j2jVQ4&t=1362s',
                          'relevance': 'Primary practitioner testimony on self-funded search outcomes, LOI '
                                       'attrition, deal costs and seller notes.'},
                         {'title': 'Acquiring Minds — Self-Funded Search vs. Traditional Search Funds '
                                   '[00:10:12]',
                          'url': 'https://www.youtube.com/watch?v=0lg8Gh_uAPU&t=612s',
                          'relevance': 'Primary practitioner testimony on the traditional versus '
                                       'self-funded equity, leverage and control debate.'},
                         {'title': 'Before You Buy or Sell a Business Podcast — ETA Reality Check: SBA '
                                   'Lending, Buyer Mistakes, Deal Killers, and the Truth About Buying a '
                                   'Business [00:09:02]',
                          'url': 'https://www.youtube.com/watch?v=pqmsev-3MPY&t=542s',
                          'relevance': 'Primary practitioner testimony on SBA lending mechanics, deal '
                                       'killers and buyer mistakes.'},
                         {'title': 'The University of Chicago Booth School of Business — Structuring the '
                                   'Acquisition Deal - Entrepreneurship Through Acquisition Event Series '
                                   '[00:45:15]',
                          'url': 'https://www.youtube.com/watch?v=kKwXdeUVNOw&t=2715s',
                          'relevance': 'Primary practitioner testimony on dead-deal costs, earn-outs, '
                                       'exclusivity buffers and escrow structure.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '_exEOi-Wxuk',
                       'title': 'How to Buy and Scale Businesses (ETA Explained) | Pete Seligman x David '
                                'Aboud [Part 1]',
                       'channel': 'David Nazeem Aboud',
                       'author': 'David Nazeem Aboud',
                       'text': 'We probably spoke to 20, put in five offers, and bought one.',
                       'tip': 'We probably spoke to 20, put in five offers, and bought one.',
                       'timestamp': 942,
                       'timestamp_seconds': 942,
                       'timestamp_label': '[00:15:42]',
                       'url': 'https://www.youtube.com/watch?v=_exEOi-Wxuk&t=942s',
                       'markdown': '[00:15:42](https://www.youtube.com/watch?v=_exEOi-Wxuk&t=942s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '004ptgWQ2TE',
                       'title': 'Inside the Mind of an Acquirer: The Harvard Playbook for Buying Your '
                                'Business',
                       'channel': 'Built to Sell',
                       'author': 'Built to Sell',
                       'text': 'Finding the business is often not the hard part.',
                       'tip': 'Finding the business is often not the hard part.',
                       'timestamp': 803,
                       'timestamp_seconds': 803,
                       'timestamp_label': '[00:13:23]',
                       'url': 'https://www.youtube.com/watch?v=004ptgWQ2TE&t=803s',
                       'markdown': '[00:13:23](https://www.youtube.com/watch?v=004ptgWQ2TE&t=803s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Hh83Lc7sWf4',
                       'title': 'Navigating Entrepreneurship Through Acquisition | Ep. 43 Part 1 | Before '
                                'You Buy or Sell a Business',
                       'channel': 'Before You Buy or Sell a Business Podcast',
                       'author': 'Before You Buy or Sell a Business Podcast',
                       'text': "It's simple but it's a numbers game.",
                       'tip': "It's simple but it's a numbers game.",
                       'timestamp': 1335,
                       'timestamp_seconds': 1335,
                       'timestamp_label': '[00:22:15]',
                       'url': 'https://www.youtube.com/watch?v=Hh83Lc7sWf4&t=1335s',
                       'markdown': '[00:22:15](https://www.youtube.com/watch?v=Hh83Lc7sWf4&t=1335s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'pqmsev-3MPY',
                       'title': 'ETA Reality Check: SBA Lending, Buyer Mistakes, Deal Killers, and the '
                                'Truth About Buying a Business',
                       'channel': 'Before You Buy or Sell a Business Podcast',
                       'author': 'Before You Buy or Sell a Business Podcast',
                       'text': "I would say the biggest one is usually that the cash flow doesn't work on "
                               'a business.',
                       'tip': "I would say the biggest one is usually that the cash flow doesn't work on a "
                              'business.',
                       'timestamp': 542,
                       'timestamp_seconds': 542,
                       'timestamp_label': '[00:09:02]',
                       'url': 'https://www.youtube.com/watch?v=pqmsev-3MPY&t=542s',
                       'markdown': '[00:09:02](https://www.youtube.com/watch?v=pqmsev-3MPY&t=542s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KT5T3j2jVQ4',
                       'title': 'The Self Funded Search Model | Robert Graham & Jordan carter',
                       'channel': 'Acquiring Minds',
                       'author': 'Acquiring Minds',
                       'text': 'If you submitted an LOI and it got executed there was probably north of a '
                               "75 percent chance of the deal closing; that's just not the case here.",
                       'tip': 'If you submitted an LOI and it got executed there was probably north of a '
                              "75 percent chance of the deal closing; that's just not the case here.",
                       'timestamp': 2409,
                       'timestamp_seconds': 2409,
                       'timestamp_label': '[00:40:09]',
                       'url': 'https://www.youtube.com/watch?v=KT5T3j2jVQ4&t=2409s',
                       'markdown': '[00:40:09](https://www.youtube.com/watch?v=KT5T3j2jVQ4&t=2409s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KT5T3j2jVQ4',
                       'title': 'The Self Funded Search Model | Robert Graham & Jordan carter',
                       'channel': 'Acquiring Minds',
                       'author': 'Acquiring Minds',
                       'text': 'So 56 percent of the seller notes in the study charge an interest rate of '
                               'six percent or more.',
                       'tip': 'So 56 percent of the seller notes in the study charge an interest rate of '
                              'six percent or more.',
                       'timestamp': 3512,
                       'timestamp_seconds': 3512,
                       'timestamp_label': '[00:58:32]',
                       'url': 'https://www.youtube.com/watch?v=KT5T3j2jVQ4&t=3512s',
                       'markdown': '[00:58:32](https://www.youtube.com/watch?v=KT5T3j2jVQ4&t=3512s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0KhOZrLBMVQ',
                       'title': 'Search Funds: How to Buy a Small Business',
                       'channel': 'Peak Frameworks',
                       'author': 'Peak Frameworks',
                       'text': 'Of the people that acquire businesses, 29 percent sustain a loss.',
                       'tip': 'Of the people that acquire businesses, 29 percent sustain a loss.',
                       'timestamp': 192,
                       'timestamp_seconds': 192,
                       'timestamp_label': '[00:03:12]',
                       'url': 'https://www.youtube.com/watch?v=0KhOZrLBMVQ&t=192s',
                       'markdown': '[00:03:12](https://www.youtube.com/watch?v=0KhOZrLBMVQ&t=192s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0lg8Gh_uAPU',
                       'title': 'Self-Funded Search vs. Traditional Search Funds',
                       'channel': 'Acquiring Minds',
                       'author': 'Acquiring Minds',
                       'text': "I've never been able to deposit a percentage of common equity in the bank.",
                       'tip': "I've never been able to deposit a percentage of common equity in the bank.",
                       'timestamp': 1108,
                       'timestamp_seconds': 1108,
                       'timestamp_label': '[00:18:28]',
                       'url': 'https://www.youtube.com/watch?v=0lg8Gh_uAPU&t=1108s',
                       'markdown': '[00:18:28](https://www.youtube.com/watch?v=0lg8Gh_uAPU&t=1108s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GYvpRW21sSY',
                       'title': 'How search fund operators convince owners to sell their business with '
                                'Steve Divitikos',
                       'channel': 'Built to Sell',
                       'author': 'Built to Sell',
                       'text': 'They liked the fact that 99.9% of my own net worth in the entirety of my '
                               'career was tied up in this one single illiquid private asset.',
                       'tip': 'They liked the fact that 99.9% of my own net worth in the entirety of my '
                              'career was tied up in this one single illiquid private asset.',
                       'timestamp': 102,
                       'timestamp_seconds': 102,
                       'timestamp_label': '[00:01:42]',
                       'url': 'https://www.youtube.com/watch?v=GYvpRW21sSY&t=102s',
                       'markdown': '[00:01:42](https://www.youtube.com/watch?v=GYvpRW21sSY&t=102s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_rMBWgqtfUI',
                       'title': 'Coley Andrews:  What it Takes to be a Search Fund Entrepreneur',
                       'channel': 'Stanford Graduate School of Business',
                       'author': 'Stanford Graduate School of Business',
                       'text': 'So the transition is really, do nothing.',
                       'tip': 'So the transition is really, do nothing.',
                       'timestamp': 247,
                       'timestamp_seconds': 247,
                       'timestamp_label': '[00:04:07]',
                       'url': 'https://www.youtube.com/watch?v=_rMBWgqtfUI&t=247s',
                       'markdown': '[00:04:07](https://www.youtube.com/watch?v=_rMBWgqtfUI&t=247s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'i_Ownd9smbk',
                       'title': 'How to Start a Search Fund from Nothing! | Funding with Peter Harris',
                       'channel': 'VCPete',
                       'author': 'VCPete',
                       'text': "One, they're selling the deal, but two they're also selling their job in "
                               'the deal.',
                       'tip': "One, they're selling the deal, but two they're also selling their job in "
                              'the deal.',
                       'timestamp': 303,
                       'timestamp_seconds': 303,
                       'timestamp_label': '[00:05:03]',
                       'url': 'https://www.youtube.com/watch?v=i_Ownd9smbk&t=303s',
                       'markdown': '[00:05:03](https://www.youtube.com/watch?v=i_Ownd9smbk&t=303s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uXEbfHnDSes',
                       'title': 'How to Create Financial Projections for a Search Fund Acquisition '
                                '(Template Walkthrough)',
                       'channel': 'ProjectionHub',
                       'author': 'ProjectionHub',
                       'text': 'Most lenders like to see at least a 1.25.',
                       'tip': 'Most lenders like to see at least a 1.25.',
                       'timestamp': 113,
                       'timestamp_seconds': 113,
                       'timestamp_label': '[00:01:53]',
                       'url': 'https://www.youtube.com/watch?v=uXEbfHnDSes&t=113s',
                       'markdown': '[00:01:53](https://www.youtube.com/watch?v=uXEbfHnDSes&t=113s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'AWJaRrNXru8',
                       'title': 'Tim Ludwig on What Industries Excite him as a Search Fund',
                       'channel': 'POWERS Pod',
                       'author': 'POWERS Pod',
                       'text': "That's going to be a red flag because typically if it's there, it's "
                               'elsewhere in the organization as well.',
                       'tip': "That's going to be a red flag because typically if it's there, it's "
                              'elsewhere in the organization as well.',
                       'timestamp': 183,
                       'timestamp_seconds': 183,
                       'timestamp_label': '[00:03:03]',
                       'url': 'https://www.youtube.com/watch?v=AWJaRrNXru8&t=183s',
                       'markdown': '[00:03:03](https://www.youtube.com/watch?v=AWJaRrNXru8&t=183s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kKwXdeUVNOw',
                       'title': 'Structuring the Acquisition Deal - Entrepreneurship Through Acquisition '
                                'Event Series',
                       'channel': 'The University of Chicago Booth School of Business',
                       'author': 'The University of Chicago Booth School of Business',
                       'text': 'You want the power of the pen.',
                       'tip': 'You want the power of the pen.',
                       'timestamp': 1565,
                       'timestamp_seconds': 1565,
                       'timestamp_label': '[00:26:05]',
                       'url': 'https://www.youtube.com/watch?v=kKwXdeUVNOw&t=1565s',
                       'markdown': '[00:26:05](https://www.youtube.com/watch?v=kKwXdeUVNOw&t=1565s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ccaGmVeLcto',
                       'title': 'The Acquisition Search Process - Entrepreneurship Through Acquisition '
                                'Event Series',
                       'channel': 'The University of Chicago Booth School of Business',
                       'author': 'The University of Chicago Booth School of Business',
                       'text': "I think that the trade off, right, is that you're probably not the only "
                               'person looking at that opportunity.',
                       'tip': "I think that the trade off, right, is that you're probably not the only "
                              'person looking at that opportunity.',
                       'timestamp': 2298,
                       'timestamp_seconds': 2298,
                       'timestamp_label': '[00:38:18]',
                       'url': 'https://www.youtube.com/watch?v=ccaGmVeLcto&t=2298s',
                       'markdown': '[00:38:18](https://www.youtube.com/watch?v=ccaGmVeLcto&t=2298s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ScOjsEfBwZQ',
                       'title': 'Entrepreneurship Through Acquisition: A Legal Guide to Buying a Small '
                                'Business // Ep 32 of DWLD',
                       'channel': 'Dean Street Law',
                       'author': 'Dean Street Law',
                       'text': "That's like buying a couple million dollar car and not actually getting "
                               'the title to it.',
                       'tip': "That's like buying a couple million dollar car and not actually getting the "
                              'title to it.',
                       'timestamp': 693,
                       'timestamp_seconds': 693,
                       'timestamp_label': '[00:11:33]',
                       'url': 'https://www.youtube.com/watch?v=ScOjsEfBwZQ&t=693s',
                       'markdown': '[00:11:33](https://www.youtube.com/watch?v=ScOjsEfBwZQ&t=693s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MvN2Q7SWbgY',
                       'title': 'How to Sell Your Business: The 8-Stage M&A Process Explained',
                       'channel': 'THE M&A DESK',
                       'author': 'THE M&A DESK',
                       'text': 'This is the stage where most deals die or get repriced.',
                       'tip': 'This is the stage where most deals die or get repriced.',
                       'timestamp': 366,
                       'timestamp_seconds': 366,
                       'timestamp_label': '[00:06:06]',
                       'url': 'https://www.youtube.com/watch?v=MvN2Q7SWbgY&t=366s',
                       'markdown': '[00:06:06](https://www.youtube.com/watch?v=MvN2Q7SWbgY&t=366s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'}]}
