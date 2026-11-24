from __future__ import annotations

def build_volume_020_workbook() -> dict:
    return {'workbook_id': 'wb-020-government-contract-brokering',
 'volume_id': 'vol-020-government-contract-brokering',
 'title': 'Government Contract Brokering — Practitioner Testimony Operator Workbook',
 'subtitle': 'Middleman bid mechanics, the registration stack, simplified acquisition targeting, first-win '
             'pricing, set-aside and state and local lanes, and incumbent-anchored cost buildup drawn from '
             'street-level government contract brokers and former contracting insiders',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Middleman Bid Readiness and Registration Stack',
                 'purpose': 'Pressure-test a middleman bid against the legal line practitioners draw '
                            'between a managed prime and a pass-through toll booth, while confirming the '
                            'registration stack that lets an award be signed and paid. Every field forces '
                            'a sourced vendor quote, a documented management role, a cash float plan, and '
                            'a verified SAM.gov, UEI, and CAGE status before anything reaches a '
                            'contracting officer.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Open every attachment on the solicitation before filling a single '
                                  'field, because practitioners call middleman bidding a game of reading '
                                  '[Kizzy Parks — iOVkNIsRYV4 @ 00:23:28].',
                                  'Collect three vendor quotes from large providers before drafting, then '
                                  'pull prior award history from the point of contact, USA Spending, or '
                                  'FPDS to anchor your price.',
                                  'Check whether FAR 52.219-14 is marked and whether the set-aside is a '
                                  'plain small business set-aside under the simplified acquisition '
                                  'threshold before assuming you may subcontract the work.',
                                  'Confirm pay-after-paid terms, a backup sub at the same price, and 60 to '
                                  '90 days of float before submitting anything to the contracting officer.',
                                  'Finish the registration stack with exact IRS name matching, never pay '
                                  'anyone for a CAGE code, and log in at least weekly because SAM.gov '
                                  'typically sends zero reminder emails [Kizzy Parks — eIFlVzfusWo @ '
                                  '00:02:23].'],
                 'fields': [{'name': 'target_set_aside',
                             'type': 'text',
                             'prompt': 'Name the specific SAM.gov small business set-aside you are '
                                       'targeting, its agency, and its structure, then state whether it is '
                                       'a plain small business set-aside or a subcategory such as 8(a), '
                                       'HUBZone, or SDVOSB, and why that distinction matters.',
                             'example': 'VA waste-removal small business set-aside priced as a base year '
                                        'plus four option years and worth $500 to $2,000 a month to the '
                                        'prime. Parks rates middleman odds at 50% to 55% [Kizzy Parks — '
                                        'kejmg4Gzuuc @ 00:10:01]. It is a plain small business set-aside, '
                                        'not 8(a), HUBZone, or SDVOSB, so subcontracting limits may not '
                                        'apply [Kizzy Parks — R-2hdJLvKUM @ 00:03:22].'},
                            {'name': 'three_vendor_quotes',
                             'type': 'textarea',
                             'prompt': 'List the three vendor price quotes you collected before writing a '
                                       'single word of the proposal, naming each vendor, its quoted '
                                       'monthly price, and why you approached large national providers '
                                       'rather than small local rivals who might bid themselves.',
                             'example': 'Quote one: WM. Quote two: Republic. Quote three: a third large '
                                        'provider at comparable scale. All three were gathered before the '
                                        'Word document opened, because Parks insists you need three price '
                                        'quotes first [Kizzy Parks — kejmg4Gzuuc @ 00:09:45]. Small '
                                        'competitors were skipped on purpose, since they will just bid the '
                                        'job themselves [Kizzy Parks — kejmg4Gzuuc @ 00:12:46].'},
                            {'name': 'prior_contract_amount',
                             'type': 'text',
                             'prompt': 'Record the prior contract amount for this requirement and where '
                                       'you found it, whether from the point of contact, USA Spending, or '
                                       'FPDS, and explain how that history caps the price you are willing '
                                       'to submit.',
                             'example': 'Prior award history pulled from FPDS and confirmed by emailing '
                                        'the point of contact before any pricing began. The history reads '
                                        '$40,000, so a $120,000 number is off the table; Parks warns '
                                        'against exactly that mismatch [Kizzy Parks — 2GThNGqMOJQ @ '
                                        "00:05:57]. Markup will stay inside Parks's 20% to 100% range over "
                                        'the lowest credible vendor quote.'},
                            {'name': 'subcontracting_clause_check',
                             'type': 'text',
                             'prompt': 'State whether FAR 52.219-14 is checked on the solicitation, quote '
                                       'the set-aside type and estimated value, and decide whether the '
                                       'limitations-on-subcontracting exemption under the simplified '
                                       'acquisition threshold applies or whether you must self-perform a '
                                       'meaningful share.',
                             'example': 'Clause box for 52.219-14 is unchecked, and Fisher says an '
                                        'unchecked box means the limit does not apply [Dr. Wes Fisher — '
                                        '7NhHddZW0kE @ 00:02:18]. The estimated value sits below both the '
                                        '$350,000 threshold attorney Steve cites [Kizzy Parks — '
                                        'R-2hdJLvKUM @ 00:20:50] and the roughly $250,000 figure Humam '
                                        'cites, so the exemption holds either way.'},
                            {'name': 'management_value',
                             'type': 'textarea',
                             'prompt': 'Describe the real management value you add as prime beyond passing '
                                       'work through, including oversight hours, quality checks, and how '
                                       'you will document management with an org chart, defined roles, and '
                                       'Gantt charts so the paperwork proves it happened.',
                             'example': 'A couple hours of monthly oversight: confirming pickups and '
                                        "reconciling the hauler's invoices. Org chart names the owner as "
                                        'program manager and the hauler as performing sub, with a Gantt '
                                        "chart for the base year. Theo's warning drives the file: if the "
                                        'paperwork is not right, it did not happen [GovCon Empire with '
                                        'Derrick Green “Theo” — h72zKiJRBe4 @ 00:26:52].'},
                            {'name': 'float_capacity',
                             'type': 'text',
                             'prompt': 'Show how you will float subcontractor payroll and vendor invoices '
                                       'for 60 to 90 days, naming the line of credit or cash reserve, its '
                                       'dollar amount, and what happens if the agency pays months late '
                                       'after an invoicing change.',
                             'example': 'Cash reserve covers 90 days of hauler invoices, with a business '
                                        'line of credit as second layer, because revenue is not cash flow '
                                        '[GovCon TechLab — uYFWvLCSDgA @ 00:07:27]. Stephanie won four '
                                        'contracts with this model yet carried $30,000 of sub costs when a '
                                        'net-30 agency paid months late after an invoicing-method change '
                                        '[GovCon TechLab — uYFWvLCSDgA @ 00:00:00].'},
                            {'name': 'pay_after_paid_terms',
                             'type': 'textarea',
                             'prompt': 'Write the exact pay-after-paid question you asked the vendor '
                                       "before submitting, record the vendor's answer, and draft the "
                                       'stop-work clause your service agreement will carry if the '
                                       'government has not yet paid you as the prime contractor.',
                             'example': 'Question asked before submission: is it okay if I pay you after '
                                        "I've been paid [Kizzy Parks — 386MNSeLv9E @ 00:34:38]. The vendor "
                                        'agreed in writing. Agreement language: if the prime has not '
                                        'received government payment, the subcontractor may stop work. '
                                        'Backup hauler lined up at the same quoted price [J. White - The '
                                        'Federal Code — LWdgQS6TyHg @ 00:01:20].'},
                            {'name': 'legal_line_position',
                             'type': 'textarea',
                             'prompt': 'Explain where your arrangement sits on the legal line between a '
                                       'managed middleman and a paper prime, citing the 100% pass-through '
                                       'risk on set-asides and the penalties practitioners name, including '
                                       'jail, fines, restitution, and debarment warnings from former '
                                       'contracting officers.',
                             'example': 'We win and sign as prime, carrying full performance liability, '
                                        'and no one else holds that role [Fed Biz Exchange — kgPkC78OKzs @ '
                                        '00:07:16]. The hauler performs; we schedule, inspect, invoice, '
                                        'and answer for every missed pickup. A pure 100% pass-through on a '
                                        'set-aside is the line that draws jail, fines, and restitution. '
                                        'Theo calls paper primes fraud.'},
                            {'name': 'bid_volume_plan',
                             'type': 'text',
                             'prompt': 'Set your monthly proposal volume and timeline expectations, given '
                                       'the reported ratio of proposals written per middleman award and '
                                       'the months a new firm may wait before its first win, and state how '
                                       'you will sustain that pace.',
                             'example': 'Plan assumes 20 to 50 proposals per win and 6 to 18 months before '
                                        'the first award, the ratio middlemen privately admitted to '
                                        'GovClose [GovClose | DoD Contract Academy — GSss1UvHnQg @ '
                                        '00:00:13]. Target is four proposals a month, every attachment '
                                        'opened and read, because this is a game of reading [Kizzy Parks — '
                                        'iOVkNIsRYV4 @ 00:23:28].'},
                            {'name': 'registration_stack_log',
                             'type': 'textarea',
                             'prompt': 'Log each registration milestone in order, Login.gov, IRS name '
                                       'match, SAM.gov entity validation, UEI receipt, DLA follow-up '
                                       'email, and CAGE assignment, with dates, plus who holds access to '
                                       'the account that stores your banking details for every payment.',
                             'example': 'Taxpayer name matched to the IRS letter character for character, '
                                        "since a stray period broke Kizzy's passcode verification [Kizzy "
                                        'Parks — wNMt73DArFc @ 00:07:15]. UEI appeared three minutes into '
                                        'validation [Kizzy Parks — FWfV2m3K4jY @ 00:05:56]. DLA email '
                                        'answered inside three business days [Kizzy Parks — FWfV2m3K4jY @ '
                                        '00:23:47]. Only the owner holds the login.'}],
                 'completion_gate': 'Complete only when three written vendor quotes, a prior-award figure, '
                                    'a recorded 52.219-14 decision, written pay-after-paid consent, a '
                                    'named backup sub at the quoted price, a funded 60-to-90-day float, a '
                                    'management org chart with Gantt schedule, and an active SAM.gov '
                                    'registration with an assigned CAGE code are all on file.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Simplified Acquisition Targeting and First-Win Pricing',
                 'purpose': 'Turn micro-purchases and simplified acquisitions into a repeatable first-win '
                            'engine. Practitioners quote micro ceilings anywhere from $2,500 to $10,000 '
                            'and split on lowest price versus best value, so these fields force you to '
                            'document filters, buyer calls, markup logic, funding, and records against '
                            'named first-win case studies before you quote a single job.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Read FAR 13.203 yourself before pricing a micro buy; Coffie notes it is '
                                  'four paragraphs and shows price reasonableness need not be verified '
                                  '[Eric Coffie — JVBkE6J1jPc @ 00:05:47].',
                                  'Remember that micro-purchases are rarely advertised, so pair every '
                                  'SAM.gov search with buyer phone calls and card-holder outreach rather '
                                  'than waiting for postings.',
                                  'Benchmark every quote against FPDS action obligations on comparable '
                                  'simplified awards and keep markup inside the middle band unless the bid '
                                  'is upfront-cash, unusual, or overseas.',
                                  'Match supplier terms to government terms before bidding and confirm '
                                  'cash runway for payment delays of up to 90 days after invoicing.',
                                  'Treat micro-purchases as legitimate work, not a loophole [Federal '
                                  'Contracts Lab — NUKVGhkCHbg @ 00:02:36], and log every small job as '
                                  'past performance.'],
                 'fields': [{'name': 'dollar_lane',
                             'type': 'text',
                             'prompt': 'Define the dollar lane you will hunt, micro-purchase under $10,000 '
                                       'or simplified acquisition under $250,000, and explain why that '
                                       'lane fits your capital, noting the small-business share '
                                       'practitioners report for simplified acquisition work versus '
                                       'traditional contracts.',
                             'example': 'Lane: simplified acquisitions under $250,000, the line SamSearch '
                                        'uses to define the category [SamSearch - AI for Government '
                                        'Contracting — e7wypJIJZpw @ 00:02:00]. The case rests on 65% of '
                                        'simplified acquisition contracts going to small businesses versus '
                                        '26% of traditional spending [SamSearch - AI for Government '
                                        'Contracting — e7wypJIJZpw @ 00:05:43]. Micro buys are worked by '
                                        'phone in parallel.'},
                            {'name': 'fpds_filter_chain',
                             'type': 'textarea',
                             'prompt': 'Document the exact FPDS filter chain you ran, including action '
                                       'obligation, simplified procedures, date signed, and keyword, '
                                       'recording the record count after each filter so a teammate can '
                                       'repeat the search and benchmark comparable simplified award '
                                       'prices.',
                             'example': 'Contracting, then advanced search [GovCon with Humam — '
                                        'IEV3HAgB8jA @ 00:07:44]. A $20,000 action obligation returned 86 '
                                        'million records; simplified procedures plus date signed from '
                                        'March 1 cut it to 30,000; the keyword cleaning cut it to 535 '
                                        '[GovCon with Humam — IEV3HAgB8jA @ 00:10:26]. Action obligations '
                                        'on those 535 become the pricing benchmark before quoting.'},
                            {'name': 'card_buyer_outreach',
                             'type': 'textarea',
                             'prompt': 'List the purchase-card holders and buyers you will call this '
                                       'month, the question you will ask about their budget, and how your '
                                       'payment setup accepts Visa or Mastercard directly with the '
                                       'SmartPay logo displayed on your website.',
                             'example': 'Ten percent of weekly hours go to Dialing for Dollars [Kizzy '
                                        'Parks — Ac9lYLwR6QQ @ 00:04:37]. Each card holder hears one '
                                        'question: what is your budget, since card holders may simply tell '
                                        'you [Sheenapreneur — B6uLsI5zZTQ @ 00:07:57]. Card payments run '
                                        'through a direct Visa and Mastercard merchant account, never '
                                        'PayPal, which reads as high-risk [TendersPage Corp. — xobcboYBB6w '
                                        '@ 00:03:10].'},
                            {'name': 'notice_screen',
                             'type': 'text',
                             'prompt': 'For each notice you screened this week, record the solicitation '
                                       'number, its dollar range, whether it demands government past '
                                       'performance, and whether it is lowest price or best value, then '
                                       'mark it pursue or skip with a reason.',
                             'example': 'Skipped one notice demanding prior government past performance, '
                                        'since Coffie says that requirement is not standard [Eric Coffie — '
                                        'AOa0-iEhmks @ 00:20:07]. Pursued a cleaning RFQ where the award '
                                        'goes to best value, not just the cheapest quote [SamSearch - AI '
                                        'for Government Contracting — xeEO2U-Vy38 @ 00:04:58], so the '
                                        'response leads with a short technical approach before price.'},
                            {'name': 'markup_band',
                             'type': 'text',
                             'prompt': 'State the markup percentage you will apply and justify it against '
                                       'the contracting-officer middle band, the gravel sweet spot, and '
                                       'the specialized-item ranges practitioners report, noting whether '
                                       'competition is heavy or you face a single player.',
                             'example': 'Markup set at 15%, inside the 7 to 25 percent middle band a '
                                        'contracting officer described, where gravel cleared at 10 to 13 '
                                        "percent [Kizzy Parks — etvo2gL7_Cs @ 00:02:23]. Coffie's ranges "
                                        'would justify 30-40% on specialized items, dropping to 5-10% '
                                        'under heavy competition [Eric Coffie — AOa0-iEhmks @ 00:30:07]; '
                                        'this part is commodity, so 15% holds.'},
                            {'name': 'first_win_model',
                             'type': 'textarea',
                             'prompt': 'Pick one practitioner first-win case to model, summarize its '
                                       'contract value, margin, and outreach effort, and explain which '
                                       'part of that engine, finding a live solicitation, phoning subs for '
                                       'quotes, or pricing in the middle, you will copy first.',
                             'example': "Model: James Walk's VA Dallas cooling-tower parts win, about $42K "
                                        'at a 15% markup, landed on three phone calls and 10 emails under '
                                        'LPTA even though Walk was not the lowest bidder [Kizzy Parks — '
                                        'AHQVro9N9HM @ 00:08:02]. First copy: phone distributors for '
                                        'quotes. Walk also added eight subs from a site visit for later '
                                        'bids [Kizzy Parks — AHQVro9N9HM @ 00:33:59].'},
                            {'name': 'funding_and_execution',
                             'type': 'textarea',
                             'prompt': 'Lay out the funding and execution plan for your target award, '
                                       'matching supplier payment terms to government payment terms, '
                                       'sizing the cash outlay against expected profit, and stating '
                                       'whether primes or subs get paid first at your dollar level.',
                             'example': 'Supplier terms are net 30 to mirror government net 30, the '
                                        'pairing James Walk used to bid within means [Kizzy Parks — '
                                        'AHQVro9N9HM @ 00:11:31]. Winning is easy; funding is hard, as '
                                        'with a $155,000 outlay for $10,000 in profit [Kizzy Parks — '
                                        'WR8VA1o3VMU @ 00:12:00]. Under $10K, primes pay subs upfront '
                                        'while primes wait 30 days [Sheenapreneur — MB8IFp5mwWc @ '
                                        '00:03:48].'},
                            {'name': 'sources_sought_cadence',
                             'type': 'text',
                             'prompt': 'Record your monthly sources-sought and outreach cadence, including '
                                       'the number of responses submitted, late responses you still sent, '
                                       'capability briefs requested, and the two-week follow-up schedule '
                                       'you keep with each assigned contracting officer on file.',
                             'example': 'Six responses this month, above the floor of five, since fewer is '
                                        'business faking [Kizzy Parks — ITZqqfI1Eig @ 00:12:55]. One went '
                                        'in after the deadline with a procurement-strategy question and a '
                                        'capability brief request [Kizzy Parks — ITZqqfI1Eig @ 00:08:52]. '
                                        'Capability statement emailed to each contracting officer every '
                                        'two weeks, the cadence Harvey used for the Colorado Air Force '
                                        'Base deal.'},
                            {'name': 'parts_sourceability',
                             'type': 'text',
                             'prompt': 'For any DIBBS or parts opportunity, record the NSN, quantity, due '
                                       'date, and approved-source status, then answer plainly whether you '
                                       'can still profit after sourcing, and note any IDIQ or BPA awardee '
                                       'count that affects profit.',
                             'example': 'NSN, quantity, and due date logged from DIBBS; the item lists an '
                                        'approved source, so it is flagged for caution, and profit after '
                                        'sourcing is confirmed before quoting [Federal Contracts Lab — '
                                        'NUKVGhkCHbg @ 00:18:36]. On the BPA, the contracting officer was '
                                        'asked how many awardees there will be, because that is going to '
                                        'impact profit [Kizzy Parks — DAbMwnUtgfI @ 00:06:04].'},
                            {'name': 'records_and_runway',
                             'type': 'textarea',
                             'prompt': 'Describe the accounting records and cash runway you keep for each '
                                       'simplified award, including how you will carry the job through 30, '
                                       '60, or 90 days of payment lag and support a '
                                       'termination-for-convenience claim if one arises.',
                             'example': 'Runway assumes the agency may take 30, 60, or even 90 days to pay '
                                        'after invoicing [Government Contract Blueprint — ZL3JyvzdhyE @ '
                                        '00:05:50]. Job-level ledgers track labor, materials, and sub '
                                        'invoices weekly, because a termination-for-convenience claim '
                                        'failed on rudimentary records [How To Sell To & Win Federal '
                                        'Government Contracts — CbeDp1nctog @ 00:11:33]. Even a $500 job '
                                        'is logged as past performance.'}],
                 'completion_gate': 'Complete only when an FPDS benchmark, a named dollar lane, a '
                                    'card-ready payment rail, a markup justified against the 7 to 25 '
                                    'percent band, a funding match between supplier and government terms, '
                                    'at least five monthly sources-sought responses, and job-level '
                                    'accounting records are documented for every active pursuit.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Set-Aside, SLED, and Cooperative Targeting with Price Buildup',
                 'purpose': 'Point outreach at the set-aside, state, local, school, and cooperative '
                            'markets practitioners call softer ground, then build a defensible price from '
                            'incumbent award history and a line-by-line cost buildup. Fields capture '
                            'filters, team campaigns, co-op positioning, recompete intelligence, and '
                            'wrap-rate math so no number reaches a contracting officer unsupported.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Treat certification as a filter, not a pipeline, because the SBA is not '
                                  'going to be bringing you contracts [GovKidMethod — xXM1cyLQ_jY @ '
                                  '00:07:09].',
                                  'Run set-aside and portal filters first, record result counts, and '
                                  'choose one lane before spending money on certifications or bid '
                                  'subscriptions.',
                                  'Below the formal threshold on state and local work, aim to get called '
                                  'for quotes, and attend every mandatory pre-bid meeting [Win the Bid — '
                                  'roNNP4jeQpc @ 00:00:55].',
                                  'Never price a recompete blind: email the POC, pull modification 0, and '
                                  'pull the old solicitation before touching the wrap calculator.',
                                  'Build costs from fringe, overhead, G&A, and fee upward, then check the '
                                  'result against FPDS history and the competitive G&A band before '
                                  'submitting.'],
                 'fields': [{'name': 'set_aside_market_research',
                             'type': 'text',
                             'prompt': 'Run the SAM.gov set-aside filter with your NAICS code and record '
                                       'result counts for each set-aside type, then decide whether any '
                                       'certification is worth time or money now, or after your first '
                                       'prime federal win.',
                             'example': 'Set-aside search treated as market research before any '
                                        'certification decision [GovKidMethod — nRXCetmIWUs @ 00:02:27]. '
                                        'An SDVOSB search narrowed from 61 to 14 results with a Sources '
                                        'Sought filter. FY2023 context: 11,152 SDVOSB awards, 2,845 WOSB, '
                                        '1,534 HUBZone, and 872 8(a) against 5,413,622 total actions [Neil '
                                        'McDonnell — 4poj2n7iLrs @ 00:00:58]. Decision: certify after the '
                                        'first prime win.'},
                            {'name': 'sources_sought_team',
                             'type': 'textarea',
                             'prompt': 'Describe your sources-sought campaign, naming the size of the '
                                       'partner team, the single set-aside tag each firm will request, the '
                                       'number of notices you will answer this quarter, and the questions '
                                       'you will submit before solicitations drop.',
                             'example': 'A 12-firm team, each requesting one set-aside tag only, ignoring '
                                        'the rule of two [Neil McDonnell — 4poj2n7iLrs @ 00:25:19]. Goal: '
                                        "25 sources-sought responses this quarter, which McDonnell's ratio "
                                        'puts at 5 to 10 RFP responses. Scope questions go in now, because '
                                        'contracting officers avoid one-on-one questions after release '
                                        '[GovClose | DoD Contract Academy — Qij-5QQmwc8 @ 01:08:51].'},
                            {'name': 'sled_portals',
                             'type': 'textarea',
                             'prompt': 'List the state, county, city, and school bid portals you will '
                                       'monitor, the filter you apply on each to isolate live '
                                       'opportunities, the resulting page or listing count, and the single '
                                       'lane you have chosen instead of chasing everything.',
                             'example': 'Texas SmartBuy: single keyword, status set to posted, cutting '
                                        '20,000 pages to 27 [SamSearch - AI for Government Contracting — '
                                        'OmEqzgzoKlc @ 00:03:13]. Each city portal is logged separately, '
                                        'since every city has its own site and process [SamSearch - AI for '
                                        'Government Contracting — RY7zan9X3oY @ 00:02:30]. Lane chosen: '
                                        "janitorial priced per service point; don't chase the map."},
                            {'name': 'cooperative_contract',
                             'type': 'text',
                             'prompt': 'Identify a cooperative purchasing vehicle such as Sourcewell that '
                                       'fits your offering, explain how a co-op award would replace a '
                                       'year-long RFP with a priced quote, and state how you will pitch it '
                                       'without implying a procurement workaround.',
                             'example': 'Sourcewell is the target vehicle; co-op buying is estimated at '
                                        'about 20-30% of US purchases, yet salespeople and city officials '
                                        "often don't know it exists [Foley Equipment — Hlnggncm3KQ @ "
                                        '00:00:00]. Pitch to agencies: you choose a distributor and skip a '
                                        'year-long RFP. Never framed as a way to get around procurement '
                                        '[Provident — V3qc9e4w-4M @ 00:19:43].'},
                            {'name': 'prebid_and_bid_tabs',
                             'type': 'textarea',
                             'prompt': 'Record whether the bid has a mandatory pre-bid meeting and your '
                                       'attendance plan, the plan-holder list contents, and the bid tabs '
                                       'and last award letter you pulled, then explain how that history '
                                       'sets your number.',
                             'example': 'Mandatory pre-bid confirmed and attended, since missing it means '
                                        "you cannot submit [D'S Construction — yxjYYFbCa5E @ 00:02:56]. "
                                        'Plan-holder list saved as the gold: it shows which GCs receive '
                                        "our number [D'S Construction — yxjYYFbCa5E @ 00:02:08]. Bid tabs "
                                        'and the last award letter pulled, so pricing tracks history '
                                        'instead of guesses [Government Contracting Strategist & Host — '
                                        'iTD46ZpHbdI @ 00:10:32].'},
                            {'name': 'incumbent_value',
                             'type': 'textarea',
                             'prompt': 'Record the incumbent name, contract number, and contract value you '
                                       'requested from the point of contact, plus modification 0 totals '
                                       'from FPDS sorted by date signed, and note any gap between the '
                                       'latest action and the full award.',
                             'example': 'POC emailed for incumbent, contract number, and value, because '
                                        'Parks once assumed an Army award was at least $250K and it came '
                                        'in near $35K [Kizzy Parks — L0SM3XAM3IE @ 00:05:28]. FPDS sorted '
                                        'by date signed: modification 0 showed $1,686,566.88 over three '
                                        'years, while the latest action alone showed 348k [Fox Wade — '
                                        'Z2ZeI5rayvk @ 00:02:50].'},
                            {'name': 'old_solicitation_scope',
                             'type': 'text',
                             'prompt': 'Pull the prior solicitation for this recompete using an '
                                       'exact-phrase SAM.gov search with status set to inactive, then '
                                       'compare the old scope and staffing to the new one and record how '
                                       'the change shifts your price.',
                             'example': 'Exact-phrase search with Status set to Inactive returned the '
                                        'prior solicitation; staffing grew from 2 people to 10, the same '
                                        'jump FedAccess warns about [FedAccess — GrYP5KyxBho @ 00:05:33]. '
                                        'The old award value is therefore not a ceiling. Scope questions '
                                        'go to the email address listed in every solicitation [FedAccess — '
                                        'GrYP5KyxBho @ 00:07:51].'},
                            {'name': 'wrap_rate_buildup',
                             'type': 'textarea',
                             'prompt': 'Build your wrap rate line by line, entering fringe, overhead, G&A, '
                                       'and fee percentages, the resulting multiplier on direct pay, and '
                                       'the maximum pay a target bill rate allows, then flag any rate '
                                       'outside the competitive band.',
                             'example': 'Fringe 30%, overhead 3%, G&A 8%, fee 7%, for a client-site wrap '
                                        'near 1.5, so $50/hr pay bills about $75/hr; competitors may '
                                        'target 1.45 [Solvability — lOumu-Dk0Jw @ 00:40:51]. A $75 bill '
                                        'rate caps pay near $48, and G&A stays inside the 8-15% norm, far '
                                        'from the 60% that is out of the game [Solvability — lOumu-Dk0Jw @ '
                                        '00:42:07].'},
                            {'name': 'cost_allocation',
                             'type': 'textarea',
                             'prompt': 'Explain where each gray-area cost lands, overhead or G&A, how you '
                                       'keep unallowable costs out of every pool, and how you will support '
                                       'reasonableness with records, knowing that spending money alone '
                                       'does not prove an amount reasonable.',
                             'example': 'Gray-area items go to overhead, not G&A, or the G&A rate goes '
                                        'through the roof [Solvability — lOumu-Dk0Jw @ 00:27:28]. '
                                        'Unallowable items are tagged and excluded from every pool. Each '
                                        'allocation carries a receipt and rationale, since under FAR '
                                        '31.201-3 spending the money creates no presumption of '
                                        'reasonableness [Win Government Contracts with GovSuccess — '
                                        'i7_rrrRpotk @ 00:01:30].'},
                            {'name': 'recompete_pipeline',
                             'type': 'text',
                             'prompt': 'Size your recompete pipeline against your revenue target, listing '
                                       'the FPDS query URL you saved, the total opportunity value it '
                                       'surfaces, the export format you used, and the year you must win '
                                       'work to book future revenue.',
                             'example': 'Target $5M of 2027 revenue, so $25-100M in recompetes must be in '
                                        'the pipeline during 2026 [Neil McDonnell — 17foq325L5w @ '
                                        '00:10:33]. The FPDS query URL is copied and sent to the teammate '
                                        'instead of rebuilding filters [Neil McDonnell — 17foq325L5w @ '
                                        '00:25:07]. Export goes to Excel for a pivot table, never PDF '
                                        '[Neil McDonnell — 0cGdQvymmvY @ 00:28:22].'}],
                 'completion_gate': 'Complete only when set-aside result counts, a chosen lane, a '
                                    'sources-sought team plan, a pre-bid attendance record, incumbent '
                                    "value with modification 0, the prior solicitation's scope, a "
                                    'wrap-rate table with G&A inside 8-15%, documented cost allocations, '
                                    'and a saved FPDS query URL are all recorded and cross-checked against '
                                    'award history.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Compliant Proposals and Prime-Sub Teaming Agreements',
                 'purpose': 'Turn a live solicitation into a compliant, scorable response and a written '
                            'prime-sub structure. Responsiveness is unforgiving, so this worksheet forces '
                            'a compliance matrix, a logged amendment trail, disciplined written questions, '
                            'a deliberate prime-or-sub decision backed by capital math, and teaming terms '
                            'that exist on paper rather than in handshakes.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Pull the full solicitation package, open every attachment, and read '
                                  'Sections L and M before writing a single sentence of the response.',
                                  'Build the compliance matrix before kickoff and key every row to a PWS '
                                  'section number, an owner, a status, and an evaluation factor.',
                                  'Submit questions in writing only, during the question window, and '
                                  'assume every answer will be published to all competing bidders.',
                                  'Choose prime or sub based on upfront capital and liability, then put '
                                  'every workshare floor and sub price in writing.',
                                  'Have an independent checker open every page reference in the matrix, '
                                  'and upload a full day before the deadline.'],
                 'fields': [{'name': 'solicitation_type_and_naics_check',
                             'type': 'text',
                             'prompt': 'Identify whether the notice is an RFI, RFQ, or RFP, record the '
                                       'solicitation number and posted NAICS code, and confirm that exact '
                                       'NAICS code already sits on your SAM registration before any '
                                       'writing time is spent on the response.',
                             'example': 'Notice type: solicitation for the Bardwell Lake job, NAICS '
                                        '721211. Before drafting, open the SAM entity record and confirm '
                                        '721211 is listed; GovKidMethod warns the award cannot be made '
                                        'without it [GovKidMethod — wot0JsK9qCc @ 00:02:06]. Status: '
                                        '721211 missing, added today, registration resubmitted. Drafting '
                                        'holds until the updated record shows active, and the check is '
                                        'logged in the matrix header.'},
                            {'name': 'compliance_matrix_build',
                             'type': 'textarea',
                             'prompt': 'List every shall, must, and will statement pulled from Sections L '
                                       'and M and the PWS, then map each requirement to a volume and page, '
                                       'a named owner, a status, and the Section M evaluation factor it '
                                       'supports in scoring.',
                             'example': "Row 14: PWS 3.2.1 'contractor shall provide weekly floor care' "
                                        'maps to Technical Volume page 6, owner: operations lead, status: '
                                        'drafted, Section M Factor 1. Rows are keyed to PWS section '
                                        'numbers because PWS documents often lack page numbers [THE '
                                        'FEDERAL PROPOSAL EXPERTS — zeJUuxLmj6s @ 00:08:42]. Budget four '
                                        'to ten hours for the full build.'},
                            {'name': 'amendment_and_clarification_log',
                             'type': 'textarea',
                             'prompt': 'Record every amendment and written clarification received since '
                                       'release, the date each arrived, the matrix rows it changed, and '
                                       'the version label now on the matrix, so writers never work from '
                                       'superseded requirements or outdated instructions during drafting.',
                             'example': 'Amendment 002 arrived Tuesday and moved the page limit for the '
                                        'technical volume. Changes were redlined into rows 9 through 12 '
                                        'that same day, following the rule to add every clarification the '
                                        'day it arrives [Bid and Comply — c73xWsLDDhc @ 00:03:26]. Matrix '
                                        "header now reads 'up-to-date through amendment 002' and the old "
                                        'version is archived.'},
                            {'name': 'written_question_strategy',
                             'type': 'textarea',
                             'prompt': 'Draft the written questions you will submit before the question '
                                       'deadline, and for each one note why it is needed and confirm it '
                                       'does not reveal any unique advantage, since every answer is '
                                       'published to all bidders in an addendum.',
                             'example': 'Question 1: Section L sets a 20-page limit but the PWS lists six '
                                        'task areas; please confirm whether resumes count toward the '
                                        'limit. This exposes nothing proprietary. Questions go in writing '
                                        'only and answers reach every bidder by addendum, so the staffing '
                                        'approach stays out of it [CHCEDC — 46vBsddH6zQ @ 00:12:11]. '
                                        'Submit through the solicitation email address.'},
                            {'name': 'page_budget_and_formatting',
                             'type': 'textarea',
                             'prompt': 'Allocate the page limit across sections in proportion to the '
                                       'Section M evaluation weights, and record the required font, '
                                       'margins, file format, and submission deadline, because bids are '
                                       'rejected at the first gate review for format non-compliance well '
                                       'before price matters.',
                             'example': 'DFO RFP weighted 70/30 technical to price, so roughly 70% of '
                                        'pages go to the technical approach. Pricing followed the '
                                        'all-inclusive daily model: $1,850/day for 90 days plus $1,925/day '
                                        'for 30 days, about $224K [Point2Pivot — LmEpAxUzd94 @ 00:38:35]. '
                                        'Upload target is a full day early, because 12:01 for a noon '
                                        'deadline is rejected.'},
                            {'name': 'ai_draft_verification',
                             'type': 'textarea',
                             'prompt': 'Describe how AI tools were used to draft or check the response, '
                                       'which sections they touched, and how every figure, claim, and '
                                       'requirement in the AI output was verified against the solicitation '
                                       'before it entered the final proposal volume.',
                             'example': 'Claude and ChatGPT drafted the technical narrative side by side; '
                                        "the ChatGPT version came back very light, so Claude's draft "
                                        'became the base. Every invented figure was struck and replaced '
                                        'with a number traced to the RFP, because automation is no '
                                        'substitute for accuracy [APMP — MSvfidBACFs @ 00:00:59]. A second '
                                        'reviewer re-checked all pricing references.'},
                            {'name': 'prime_or_sub_decision',
                             'type': 'textarea',
                             'prompt': 'State whether you will pursue this opportunity as the prime or as '
                                       'a subcontractor, naming who the contracting officer would actually '
                                       'sign with, who carries full performance liability, and how much '
                                       'upfront capital each path would require you to fund.',
                             'example': 'On a $2M-per-year set-aside task order, priming at 55% means '
                                        'roughly $80K a month in costs, a 70-80 day payment wait, and '
                                        '$275,000-$300,000 upfront, versus about $80,000 for a $400K sub '
                                        'slice [ELINT Capital — EpUc9OVjb4g @ 00:13:32]. Decision: sub on '
                                        'this one, because cash on hand cannot carry the roughly $175K '
                                        'payroll reserve.'},
                            {'name': 'partner_target_list',
                             'type': 'textarea',
                             'prompt': 'Build a target list of potential teaming partners with past '
                                       'performance at this agency, showing the search source, filters '
                                       'applied, number of results before and after deduplication, and the '
                                       'outreach method planned for each firm on the list.',
                             'example': "SAM.gov Contract Awards search for 'help desk' returned about "
                                        '2,000 results, filtered to 149 woman-owned, then 87 unique '
                                        'companies after removing 62 duplicates by UEI [Neil McDonnell — '
                                        'zqg5q_pZvdc @ 00:24:05]. Top five with agency past performance '
                                        'get phone calls, not email; three of five should say yes, and '
                                        'silent ones get a spam-folder check.'},
                            {'name': 'workshare_and_agreement_terms',
                             'type': 'textarea',
                             'prompt': 'Write the workshare, exclusivity, duration, and survival terms for '
                                       'the teaming agreement in exact language, stating the minimum '
                                       'percentage as a floor, the end date, what survives termination, '
                                       'and whether the agreement can terminate during source selection '
                                       'for the proposal.',
                             'example': 'Workshare: sub receives no less than 30% of labor dollars, not '
                                        "'approximately' [GovCon TechLab — JYbjE63rG-Y @ 00:14:55]. "
                                        'Exclusivity applies at the task-order level only and does not '
                                        'survive termination; confidentiality and employee '
                                        'non-solicitation do survive. Agreement ends at award plus 12 '
                                        'months or on loss notice, and cannot terminate while the proposal '
                                        'sits in source selection.'},
                            {'name': 'sub_pricing_paper_trail',
                             'type': 'text',
                             'prompt': 'Record where each subcontractor price quote lives in writing, the '
                                       'date it was received, the named contact who sent it, and the '
                                       'backup sub you have lined up at the same price in case the primary '
                                       'contact disappears.',
                             'example': 'Janitorial sub quote received by text on March 4 from the '
                                        'operations manager, screenshot saved to the bid folder; written '
                                        'pricing matters more than an NDA, and one winner had to give a '
                                        'contract back after the sub contact left [Kizzy Parks — '
                                        'F6Hwh89ornQ @ 00:07:00]. Backup sub confirmed by email at the '
                                        'identical price.'}],
                 'completion_gate': 'Worksheet 4 is complete when every matrix row has an owner, status, '
                                    'and page reference verified by an independent checker, the NAICS code '
                                    'is confirmed on SAM, all amendments are logged, and every sub price '
                                    'and workshare floor exists in writing.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Limitations on Subcontracting, Affiliation Risk, and Contract Administration '
                          'Controls',
                 'purpose': 'Keep a set-aside award legally defensible after the win. This worksheet sets '
                            'the subcontracting cap, runs per-period self-performance math, vets similarly '
                            'situated subs, screens affiliation exposure, and builds the contract '
                            'administration controls that stop COR-directed changes, missed notice '
                            'windows, clause confusion, and unpriced wage determination lines.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Check whether 52.219-14 is checked on the solicitation and identify the '
                                  'work category before running any self-performance math.',
                                  'Compute the limitation on subcontracting per base period, option '
                                  'period, or task order, never averaged across the whole contract.',
                                  'Verify every similarly situated sub against first-tier status, program '
                                  'status, and size under the subcontract NAICS code.',
                                  'Search the contract for every 52.2 clause, read local clauses closely, '
                                  'and flow down only the mandatory lists to subs.',
                                  'Route every scope change through the warranted contracting officer in '
                                  'writing and log notice dates against your changes clause.'],
                 'fields': [{'name': 'los_category_and_cap',
                             'type': 'text',
                             'prompt': 'Identify the work category for this award as services, supplies, '
                                       'general construction, or specialty trade, record the matching cap '
                                       'on dollars paid to non-similarly-situated subs, and note whether '
                                       'the 52.219-14 clause box is checked on the solicitation before '
                                       'pricing.',
                             'example': 'Services task order; 52.219-14 is checked, so the subcontracting '
                                        'limit applies [Dr. Wes Fisher — 7NhHddZW0kE @ 00:02:18]. Cap: no '
                                        'more than 50% of amount paid may go to non-similarly-situated '
                                        'subs, with supplies also 50%, general construction 85%, and '
                                        'specialty trade 75%. Planning target is 47-49% subcontracted to '
                                        'keep wiggle room below the services cap.'},
                            {'name': 'self_performance_math',
                             'type': 'textarea',
                             'prompt': 'Calculate the dollar amount your firm must self-perform for each '
                                       'base and option period, showing contract value per period, '
                                       'materials excluded, the applicable percentage, and the resulting '
                                       'self-performance requirement, with no averaging across periods or '
                                       'across task orders.',
                             'example': 'A $1M-per-month services contract with $100K in materials leaves '
                                        '$900K subject to the rule, producing a $450K monthly '
                                        'self-performance requirement [PilieroMazza PLLC — i9prjadeAyM @ '
                                        '00:32:49]. Base year and each option year are tested separately. '
                                        'Falling short in year one cannot be made up later, so the '
                                        'shortfall plan below triggers on any monthly miss.'},
                            {'name': 'similarly_situated_entity_check',
                             'type': 'textarea',
                             'prompt': 'List every subcontractor you plan to count as similarly situated, '
                                       'and for each confirm it is first tier, holds the same program '
                                       'status as your firm, and is small under the NAICS code assigned to '
                                       'the subcontract rather than yours.',
                             'example': 'WOSB prime teaming with a WOSB electrical sub: first tier, '
                                        "current WOSB status, small under the subcontract's NAICS, not the "
                                        "prime's [Theodore Watson — 28K_7987r8w @ 00:04:26]. Its work "
                                        "counts as the prime's own. Keep class deviation 0003 from "
                                        'December 2018 in the file, since contracting officers have asked '
                                        'Eric Coffie to explain SSE pooling.'},
                            {'name': 'monthly_payment_tracking',
                             'type': 'textarea',
                             'prompt': 'Set up a monthly tracker of dollars paid to each subcontractor, '
                                       'flagging silent drift toward the cap and any lapsed sub '
                                       'certification, so problems are caught and corrected inside the '
                                       'measurement period rather than discovered at the end of it.',
                             'example': 'October close: Sub A paid $210K, Sub B $35K, against $500K '
                                        'invoiced, so non-similarly-situated share sits at 49%, inside the '
                                        "buffer but drifting. Sub B's SDVOSB status lapsed September 30 "
                                        'and now counts against the cap. Monthly tracking exists to catch '
                                        'exactly this drift [Vet GovCon Blueprint — go1eoNNgFRM @ '
                                        '00:05:58]. Action: shift two tasks in-house.'},
                            {'name': 'affiliation_risk_screen',
                             'type': 'textarea',
                             'prompt': 'Screen your firm for affiliation and ostensible contractor risk by '
                                       'recording revenue concentration from any single company in the '
                                       'prior year, reliance on a large sub to manage the work, and any '
                                       'plan to hire an incumbent workforce.',
                             'example': 'Prior-year revenue from the largest customer was 62%, under the '
                                        '70% economic-dependence trigger cited under 13 CFR 121.103 '
                                        '[Theodore Watson — k1ZkyITmwWM @ 00:02:49]. The large sub '
                                        'performs field tasks only; our program manager runs the contract. '
                                        'Incumbent hires limited to four technicians, no managers, '
                                        "following Watson's warning against hiring an incumbent workforce "
                                        'en masse.'},
                            {'name': 'authority_and_warrant_map',
                             'type': 'textarea',
                             'prompt': 'Name the warranted contracting officer, the COR, and any other '
                                       'government contacts on this contract, recording what each person '
                                       'is authorized to direct, and write down the rule your team follows '
                                       'when a non-warranted person requests a scope change.',
                             'example': 'Contracting officer holds the warrant and alone binds the '
                                        'government; the COR has no warrant and cannot alter the scope of '
                                        'work [Contract Warrior — pktnZU4AWIE @ 00:06:55]. Team rule: any '
                                        'COR direction, like moving ductwork 6 ft north, is logged, '
                                        'paused, and emailed to the contracting officer for written '
                                        'confirmation before crews touch anything.'},
                            {'name': 'clause_inventory',
                             'type': 'textarea',
                             'prompt': 'Search the contract for every clause beginning with 52.2, list '
                                       'each clause number with its date, flag local clauses for close '
                                       'reading, and note which clauses must flow down to subcontractors '
                                       'under 52.244-6 or 52.212-5(e) rather than flowing down all of '
                                       'them.',
                             'example': "Ctrl-F on '52.2' returned 41 clauses. Two local clauses on site "
                                        'access skipped public comment, so each gets a close read. '
                                        'Flow-downs limited to the mandatory lists in 52.244-6 and '
                                        '52.212-5(e), not all of 52.2 [Public Contracting Institute (PCI) '
                                        '— UV6zJLRHfHw @ 00:56:54]. Blank fill-ins are treated as blank, '
                                        'and nothing self-deletes.'},
                            {'name': 'change_notice_and_rea_log',
                             'type': 'textarea',
                             'prompt': 'Log every potential change with the date it was directed, who '
                                       'directed it, the notice window stated in your changes clause, the '
                                       'date notice reached the contracting officer, and whether the cost '
                                       'impact is heading toward an REA or claim.',
                             'example': 'Change 03: additional floor scope directed May 6. Notice window '
                                        'is typically 30 days, but our clause was read for the exact '
                                        'period [How To Sell To & Win Federal Government Contracts — '
                                        'h1yszOmFw3w @ 00:14:08]. Notice sent May 9. Estimated impact '
                                        '$64K, so an REA comes first; anything over $100,000 would need '
                                        'certification as a claim.'},
                            {'name': 'protest_and_claim_separation',
                             'type': 'text',
                             'prompt': 'Describe how protest files and claim files are kept separate, '
                                       'listing the deadline type that governs each, the submission period '
                                       'versus the appeal period, and who on your team owns each file so '
                                       'deadlines are never mixed up.',
                             'example': 'Two folders, two owners. Protest file: proposal manager, '
                                        'debriefing request sent even on wins. Claim file: contracts lead, '
                                        'six-year limit, CDA interest applies to claims but not REAs. '
                                        'Protest deadlines are never imported into the claim file, and '
                                        'submission and appeal periods are tracked on separate calendars '
                                        '[Win Government Contracts with GovSuccess — -smvR-8_v1M @ '
                                        '00:01:14].'},
                            {'name': 'wage_determination_pricing_check',
                             'type': 'textarea',
                             'prompt': 'Before submission, list every SCA wage determination line and paid '
                                       'vacation requirement attached to the solicitation, confirm each is '
                                       'priced into your labor rates, and note the reviewer who checked '
                                       'the pricing against the attachment line by line.',
                             'example': 'Wage determination attached as Exhibit 4 lists custodial rates '
                                        'plus paid vacation after one year of service. Both are now built '
                                        'into the hourly rate, and the reviewer initialed each line. A '
                                        'firm lost money by missing the SCA paid vacation line [FedAccess '
                                        '— T_cRpZF2IUo @ 00:06:57], so this check runs before the price '
                                        'volume is locked.'}],
                 'completion_gate': 'Worksheet 5 is complete when the subcontracting cap and per-period '
                                    'self-performance dollars are calculated, every similarly situated sub '
                                    'is verified, the monthly payment tracker is live, the warrant map and '
                                    'clause inventory are filed, and every wage determination line is '
                                    'priced.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'DIBBS Brokering Workflow and Contract Funding, Invoicing, and Collections',
                 'purpose': 'Run a disciplined DLA parts brokering lane on DIBBS and convert awards into '
                            'cash in the bank. This worksheet covers FSC selection, RFQ screening, origin '
                            'and technical-data checks, supplier calls, margin-anchored pricing, gap '
                            'funding, supplier confidentiality, WAWF invoicing, weekly status follow-up, '
                            'and the thin-margin rebid trap.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Register on SAM and DIBBS, choose three to five FSCs, and sort RFQs by '
                                  'newest posted every working day.',
                                  'Screen each RFQ for approved-source CAGE restrictions, origin rules, '
                                  'and JCP technical data before calling any supplier.',
                                  'Call suppliers with the manufacturer part number in hand, lock pricing, '
                                  'and anchor every bid against procurement history.',
                                  'Fund the gap between paying suppliers and getting paid, and price any '
                                  'financing fee into the bid from the start.',
                                  'Match the WAWF document type and DoDAAC to the contract, then check '
                                  'invoice status every Friday until paid.'],
                 'fields': [{'name': 'fsc_lane_selection',
                             'type': 'text',
                             'prompt': 'Name the three to five FSCs you will work on DIBBS, explain why '
                                       'each fits your supplier access, and describe the daily quoting '
                                       'routine you will follow to keep bid volume high inside that narrow '
                                       'lane of parts.',
                             'example': 'Four FSCs selected where two distributors already answer phone '
                                        'calls. Routine: sort by newest posted each morning, since a '
                                        'contracting officer just entered those, then quote at least 15 '
                                        'RFQs before noon. Bid count tracks award count, and there is a '
                                        'direct correlation between bids submitted and awards won [Tris10 '
                                        '@ MeND — v4ulUMKE5xA @ 00:15:55].'},
                            {'name': 'rfq_screening_data',
                             'type': 'textarea',
                             'prompt': 'For each RFQ, extract the NSN, quantity, required delivery, due '
                                       'date, and any approved-source CAGE listed in the PID, then record '
                                       'whether a new solicitation is open, since DLA often cancels and '
                                       'reissues the same requirement many times.',
                             'example': 'NSN screened, quantity 40, due date nine days out, '
                                        'approved-source CAGE listed in the PID, so the part must come '
                                        'from that source, though buying it through a distributor is '
                                        'allowed [Tris10 @ MeND — JE_OOJ3NAVk @ 00:08:55]. Full '
                                        'solicitation read on DIBBS before quoting, with packaging terms '
                                        'noted. Still open: confirmed this morning.'},
                            {'name': 'origin_and_tech_data_check',
                             'type': 'textarea',
                             'prompt': 'Confirm the country of origin for the quoted part, document that '
                                       'it does not come from a non-qualifying country, and record whether '
                                       'JCP technical data is involved and whether the receiving '
                                       'manufacturer is also certified to hold it.',
                             'example': 'Supplier confirmed in writing that the fitting is made '
                                        'domestically, not in China or Afghanistan, which would disqualify '
                                        'the quote [Tris10 @ MeND — v4ulUMKE5xA @ 00:12:48]. Drawings '
                                        'carry JCP restrictions, and the machine shop holds its own '
                                        'certification, so the data package can be shared. A non-certified '
                                        'shop would have been dropped, because passing that data is not '
                                        'legal.'},
                            {'name': 'supplier_quote_call_log',
                             'type': 'textarea',
                             'prompt': 'Log each supplier you called for this NSN, including the '
                                       'manufacturer part number you mapped beforehand, the contact name, '
                                       'quoted unit cost, lead time, payment terms, and freight or FOB '
                                       'terms affecting your final delivered cost before you price the '
                                       'quote.',
                             'example': 'NSN mapped to the manufacturer part number using nsn-now before '
                                        'dialing, because suppliers often have no idea what an NSN is '
                                        '[Tris10 @ MeND — JE_OOJ3NAVk @ 00:04:05]. Distributor quoted $212 '
                                        'per unit, 120-day lead time, Net 30, FOB origin with freight '
                                        'added. Calling beat email: saying no over the phone is harder.'},
                            {'name': 'dla_bid_price_and_margin',
                             'type': 'textarea',
                             'prompt': 'Build the DLA bid price from supplier cost, freight, tariffs, and '
                                       'packaging, anchor it against procurement history for the NSN, '
                                       'state the margin percentage, and record the lead time you will '
                                       'quote, using your real lead time rather than the requested one.',
                             'example': 'Supplier cost $212, freight $9, landed cost $221. Procurement '
                                        'history shows the last two awards at $250 and $258, so the bid is '
                                        '$248, about 12% margin, inside the 10-15% sweet spot; asking '
                                        '20-30% gets you underbid [Secureframe — v7nJCLRc0uo @ 00:38:03]. '
                                        "Quoted lead time is the supplier's real 120 days, not the "
                                        'requested 45.'},
                            {'name': 'cash_gap_funding_plan',
                             'type': 'textarea',
                             'prompt': 'Map the cash gap from the date you pay your supplier or crew to '
                                       'the date the government pays you, then name the funding source '
                                       'that covers it, its cost as a percentage, and whether your margin '
                                       'can absorb that fee.',
                             'example': 'Services task order: crews paid biweekly, about 30 days of work '
                                        'before invoicing, then roughly 30 more days waiting for payment. '
                                        'Funding: invoice factoring at 3% to 5%, with any factor above 5% '
                                        'rejected [Debra Smith — NusotbSsCa4 @ 00:02:56]. Margin is 18%, '
                                        'so a 4% fee fits and is priced into the bid from the start.'},
                            {'name': 'supplier_confidentiality_terms',
                             'type': 'text',
                             'prompt': 'Write the exact language you will use when a prospective supplier '
                                       'asks for the agency name or point of contact before the purchase '
                                       'order is in hand, and name the backup supplier you will move to if '
                                       'they insist.',
                             'example': "Script: 'The end customer and contact are confidential under our "
                                        'terms and conditions until the purchase order issues; we can '
                                        "share NSN, quantity, and delivery.' A sub once used that request "
                                        'to try to undercut and bid directly, so insistence means moving '
                                        'on [Debra Smith — NusotbSsCa4 @ 00:12:21]. Backup: second '
                                        'distributor already quoted.'},
                            {'name': 'wawf_invoice_setup',
                             'type': 'textarea',
                             'prompt': 'Record the WAWF document type required by the payment instructions '
                                       'clause, the ship-to and admin DoDAAC codes copied from the '
                                       'contract, and the final-shipment indicator plan, so the invoice '
                                       'qualifies as proper and the prompt payment clock starts.',
                             'example': 'Supply contract, so the document type is combo, not Invoice '
                                        '2-in-1, which is for services [Acquisition Pro Tips — WXCymE9NjBg '
                                        '@ 00:05:10]. Ship-to DoDAAC verified against the contract and '
                                        'confirmed different from the admin DoDAAC. This is the last '
                                        'shipment, so the Z final-shipment marker goes on. Payment is due '
                                        'within 30 days of a proper invoice.'},
                            {'name': 'invoice_status_followup',
                             'type': 'textarea',
                             'prompt': 'Describe your weekly invoice status routine, including the day you '
                                       'check My Invoice, how each rejection or remark code is handled, '
                                       'which office you call for quantity versus accounting problems, and '
                                       'the delivery evidence you keep on file.',
                             'example': "Every Friday, open My Invoice; any 'See reason and remark code' "
                                        'status is ours to fix, calling DLA on quantity and DFAS on '
                                        'accounting [Tris10 @ MeND — yXqp5I7wQK0 @ 00:15:10]. Rejected '
                                        'invoices are copied, only the failed field is corrected, then '
                                        'resubmitted. Every unit and container is photographed, and FedEx '
                                        'or UPS proof of delivery is downloaded.'},
                            {'name': 'margin_and_rebid_risk',
                             'type': 'textarea',
                             'prompt': 'Compare the gross margin on this award against the financing cost, '
                                       'payment lag, and the price you would need on the rebid, and '
                                       'explain whether you are buying the door at a margin too thin to '
                                       'sustain the work.',
                             'example': 'Gross margin on the planned bid is 6%, inside the 5% to 7% '
                                        'low-bid trap, while rebids need 20% to 40% [Business Cash Now — '
                                        '4V1zq5q3VuQ @ 00:00:53]. A 4% factoring fee would leave 2%, so '
                                        'financing is off the table. Decision: pass on this bid unless the '
                                        'price can carry a margin that covers funding and execution.'}],
                 'completion_gate': 'Worksheet 6 is complete when the FSC lane and daily routine are set, '
                                    'every quoted part passes the source, origin, and tech-data checks, '
                                    'the funding source and fee are priced into the bid, and the WAWF '
                                    'setup and Friday status routine are documented.'}]}
