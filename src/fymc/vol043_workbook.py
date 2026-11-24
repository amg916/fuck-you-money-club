from __future__ import annotations

def build_volume_043_workbook() -> dict:
    return {'workbook_id': 'wb-043-live-event-super-bowl-and-vip-ticket-brokering',
 'volume_id': 'vol-043-live-event-super-bowl-and-vip-ticket-brokering',
 'title': 'Live-Event, Super Bowl & VIP Ticket Brokering — Practitioner Testimony Operator Workbook',
 'subtitle': "A Broker's Field Workbook for Super Bowl Resale Reads, Allotment Sourcing, Premium "
             'Hospitality Packages, Paddock Club Access, Marquee-Event Badges and Personal Seat License '
             'Economics',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Super Bowl Resale Market Read and Seat Sourcing Ledger',
                 'purpose': 'Build a disciplined read of the Super Bowl resale curve before committing '
                            'capital, then trace every seat back to the allocation door it came through. '
                            'This ledger turns face-value spreads, commission drag, buyer geography, '
                            'timing windows and fraud screens into one written buy-or-pass decision.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Start with the face-value floor and the cheapest live resale listing, '
                                  'because every later margin calculation depends on knowing that spread '
                                  'in writing.',
                                  'Fill the timing and collapse fields before buying anything, so the exit '
                                  'price exists before emotion and game-week noise arrive.',
                                  'Map the allocation and supplier channels next, naming the specific '
                                  'roster segment, team door or hospitality partner behind each seat you '
                                  'pursue.',
                                  'Run every inbound offer through the fraud screen field, rejecting '
                                  'below-market listings, physical tickets for a mobile-only game and '
                                  'unverified private sellers.',
                                  'Review the completed ledger against the completion gate, and do not '
                                  'wire money until every field carries a dated figure and a named '
                                  'reference.'],
                 'fields': [{'name': 'face_value_vs_resale_floor',
                             'type': 'text',
                             'prompt': 'Record the face-value floor for the target game alongside the '
                                       'cheapest live resale listing and the game-day average listing, '
                                       'then state the multiple between face and resale so every later '
                                       'pricing decision starts from a documented spread rather than '
                                       'memory.',
                             'example': 'Face value floor sits at $950 while the cheapest resale listing '
                                        'reads about $4,950, a spread above five times face. Game-day '
                                        'resale listings averaged about $8,100, so any seat bought near '
                                        'face is a rare allotment, not a market buy [Overtime Economics — '
                                        'C_QtPWHCo_U @ 00:01:58]. Logged spread: 5.2x floor, 8.5x '
                                        'average.'},
                            {'name': 'commission_and_fee_drag',
                             'type': 'text',
                             'prompt': 'Enter the marketplace commission or fee you expect to absorb on '
                                       'each trade, name the platform, and estimate what share of the '
                                       'stadium crowd buys through that channel so your net margin '
                                       'reflects the real cost of reaching buyers.',
                             'example': 'StubHub takes an average 25% commission on secondary trades, and '
                                        'interim president Noah Goldberg estimated 10 to 15% of the Super '
                                        'Bowl stadium crowd buys through the site [CBS Mornings — '
                                        'RGn3Hcnvklg @ 00:02:26]. On a $5,000 listing that commission '
                                        'removes roughly $1,250, so the break-even purchase price must sit '
                                        'near $3,750 or lower.'},
                            {'name': 'matchup_and_buyer_geography',
                             'type': 'textarea',
                             'prompt': 'Describe the matchup and the traveling fan bases behind it, '
                                       'identify which buyer markets are driving demand, and note whether '
                                       'fatigue or a single regional surge is bending the curve before you '
                                       'commit capital to inventory this week.',
                             'example': 'A single traveling fan base can carry the whole market: '
                                        'Philadelphia buyers kept StubHub sales running 30 to 40% ahead of '
                                        'the prior year even after the hometown team was knocked out [AP '
                                        'Archive — NwYrOSq9-5Q @ 00:00:15]. Contrast that with a '
                                        'Patriots-fatigue year, when a New York broker sat holding a '
                                        'backpack of slow-moving tickets.'},
                            {'name': 'buy_window_timing',
                             'type': 'text',
                             'prompt': 'Set your planned buy window in hours before kickoff, name which '
                                       'timing camp you follow, and write the trigger that would make you '
                                       'abandon the plan, such as a conference-championship spike that '
                                       'refuses to burn off on schedule.',
                             'example': 'Planned window: 48 to 72 hours out, the sweet spot where prices '
                                        'dip before game-day purchases pop them again [NBC10 Boston — '
                                        '-GwKaOFdk_M @ 00:01:24]. Counter-view logged: watch early, wait a '
                                        'few days to a week for the dip, and stay out of the final rush, '
                                        'when desperation pushes prices back up [N.F.L Podcast — '
                                        'Aj09Nv4kg04 @ 00:03:31].'},
                            {'name': 'week_of_collapse_scenario',
                             'type': 'textarea',
                             'prompt': 'Model the downside case for the final week by recording a '
                                       'documented price collapse, the leftover supply you expect on game '
                                       'day, and the exit price at which you would cut inventory rather '
                                       'than carry it into kickoff.',
                             'example': 'In one week, 50-yard-line seats fell from $56,000 to $23,000 and '
                                        'the cheapest tickets fell from $6,400 to $4,600, a 58% drop '
                                        '[Valuetainment Short Clips — jQCA_9sgdpM @ 00:00:52]. StubHub '
                                        'noted downward movement depends on how much inventory is left on '
                                        'game day [AP Archive — NxbqrXeuWTI @ 00:00:38], so the exit price '
                                        'is set before that supply read.'},
                            {'name': 'soft_year_exit_plan',
                             'type': 'textarea',
                             'prompt': 'Write the exit plan for unsold inventory in a soft-matchup week, '
                                       'including the floor you will accept, the perk or bundle you could '
                                       'attach to move seats, and the date by which any remaining tickets '
                                       'must be liquidated.',
                             'example': 'Warning case: one broker sat on a backpack of tickets as the '
                                        'average slid to just over $4,400 and the low hit $1,900 [CBS '
                                        'Boston — hhJFZEqMUpQ @ 00:01:16]. Perk play from the same market: '
                                        'a pop-up near NRG Stadium threw a tailgate bash for anyone who '
                                        'bought from that operation [CBS Boston — hhJFZEqMUpQ @ '
                                        '00:01:02].'},
                            {'name': 'allocation_map',
                             'type': 'textarea',
                             'prompt': 'Map where face-value seats originate for this game, listing each '
                                       "competing team's share, the host allocation, the other clubs, and "
                                       'the hospitality partner block, so you know which doors exist '
                                       'before approaching any single supplier or broker.',
                             'example': 'Each competing team gets 17.5 percent, about 11,375 seats on a '
                                        '65,000-ticket assumption; the host takes about 5 percent and the '
                                        'other 29 clubs 1.2 percent each [thumbsuprun — O-Sq4DDGKAY @ '
                                        '00:00:27]. The remaining 25.2 percent routes to hospitality '
                                        'partners such as NFL On Location and Prime Sport, selling at '
                                        'market value.'},
                            {'name': 'supplier_channel_log',
                             'type': 'textarea',
                             'prompt': 'List every supplier channel you are working, such as players, '
                                       'coaches, agents, season holders or front-door team deals, and note '
                                       'which roster segment is most likely to sell and what cash offer '
                                       'has opened conversations before.',
                             'example': 'About 80 percent of listed seats that week came from players, '
                                        'coaches and agents, starting at $3,500 apiece [24H SPORT — '
                                        'pAU7eEVgp1A @ 00:00:40]. Roster players 35 through 53, not the '
                                        'multimillion-dollar names, are the likeliest sellers [24H SPORT — '
                                        'pAU7eEVgp1A @ 00:02:14], and brokers open with an offer of $2,500 '
                                        'cash at pre-game parties.'},
                            {'name': 'fraud_screen',
                             'type': 'textarea',
                             'prompt': 'Document the fraud screen applied to every inbound offer: the '
                                       'verified marketplace used, the ticket format required, the '
                                       'below-market threshold that triggers rejection, and any location '
                                       'rule that governs in-person game-day transactions in the host '
                                       'city.',
                             'example': 'Kill any listing sitting $1,000 to $2,000 under the going resale '
                                        'market, because a set market price exists for Super Bowl seats '
                                        '[thumbsuprun — O-Sq4DDGKAY @ 00:06:51]. Reject physical tickets '
                                        'offered for a mobile-only game [N.F.L Podcast — Aj09Nv4kg04 @ '
                                        '00:04:00], and in Glendale transact only inside the designated '
                                        'resale corral.'},
                            {'name': 'price_alert_and_seat_rights',
                             'type': 'text',
                             'prompt': 'Set a price alert target below the current listed floor, choose '
                                       'the seating level, and record any early-season seat-rights gamble '
                                       'you are weighing, including the rights cost, the total outlay, and '
                                       'what you lose if your team misses.',
                             'example': 'Alert set under the listed floor so the app pings the moment '
                                        'seats drop below target [TickPick — tY7hYkxsK3k @ 00:00:41]. '
                                        'Seat-rights benchmark: Ray Pena paid nearly $4,300 for rights, '
                                        '$11,300 total for two seats then trading above $12,000 apiece, '
                                        'money that would have been lost had the 49ers missed [ABC7 News '
                                        'Bay Area — YZ3TuDNRcvw @ 00:00:54].'}],
                 'completion_gate': 'Do not buy or list a single seat until the face-to-resale spread, '
                                    'commission drag, buy window, collapse scenario and soft-year exit '
                                    'price are written with figures, every supplier is tied to a named '
                                    'allocation door, and every offer has cleared the fraud screen on '
                                    'verified digital rails.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Premium Hospitality, Suite and Paddock Club Underwriting Sheet',
                 'purpose': 'Underwrite premium hospitality as an access product rather than a seat. This '
                            'sheet prices the full ladder from lower-bowl seats to suites and Paddock Club '
                            'rooms, protects license-backed inventory, splits client invoices correctly, '
                            'and maps race-day logistics so premium guests never lose time or value.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Lay out the complete price ladder first, then mark the rung your client '
                                  'can afford and the rung you can realistically source.',
                                  'Check official hospitality launch and sellout timing before deciding '
                                  'whether to hold or release premium inventory during game week.',
                                  'Split every suite invoice into separate ticket and food lines and send '
                                  'the hosting and clientele email before each event.',
                                  'For motorsport hospitality, build the access timeline from stand '
                                  'opening through pit lane, garage tour and the exit route out.',
                                  'Strip networking from any pitch unless introductions are staffed, and '
                                  'verify the seat count behind every premium ticket before quoting.'],
                 'fields': [{'name': 'hospitality_ladder',
                             'type': 'textarea',
                             'prompt': 'Lay out the full premium price ladder for the target event, from '
                                       'lower-bowl seats through club tables to suites, and note which '
                                       'rung your client can afford and which rung you can actually source '
                                       'this cycle.',
                             'example': 'Allegiant Super Bowl ladder: $20,000 to $50,000 lower-bowl seats, '
                                        'a $700,000 Wynn Field Club table, and suites from $300,000 to '
                                        '$2.5 million [GQ — nT-DpxVmqC0 @ 00:07:04]. Client brief targets '
                                        'the lower-bowl rung; suite inventory is logged as out of reach '
                                        'this cycle unless a corporate host co-funds the room.'},
                            {'name': 'sellout_timing',
                             'type': 'text',
                             'prompt': 'Record when the official hospitality program launched and when it '
                                       'sold out, then decide whether to hold or release premium inventory '
                                       'during game week, noting any early softness you are reading as '
                                       'choice rather than collapse.',
                             'example': 'On Location launched Super Bowl LX premium hospitality in May and '
                                        'sold out its best seating long before game week [Front Office '
                                        'Sports News — 6ufb5u4PcIQ @ 00:05:16]. Paul Caine read early '
                                        'game-week softness as too much choice and expected demand to '
                                        'climb into the weekend [Front Office Sports News — 6ufb5u4PcIQ @ '
                                        '00:06:06]. Decision: hold, no midweek dump.'},
                            {'name': 'matchup_venue_pricing',
                             'type': 'text',
                             'prompt': 'Note how matchup and venue are shaping average and cheapest prices '
                                       'for this edition, compare against a documented record year, and '
                                       'state whether your premium quotes should lean above or below that '
                                       'benchmark when the teams are set.',
                             'example': 'Benchmark year: Super Bowl 58 in Las Vegas averaged over $9,000 a '
                                        'ticket, with some secondary seats at $12,000 and the cheapest at '
                                        '$5,000 to $7,000, roughly tripling the $3,000 minimum of recent '
                                        'years [Bloomberg Television — zXgujuB9yXw @ 00:01:31]. Quotes for '
                                        'a less hyped venue lean below that benchmark until the matchup '
                                        'confirms demand.'},
                            {'name': 'suite_tax_split',
                             'type': 'textarea',
                             'prompt': 'For every client suite outing, break the invoice into separate '
                                       'ticket and food lines, record who is hosting and who the clientele '
                                       'is, and confirm staff have been briefed on whether the room is '
                                       'closing business or celebrating.',
                             'example': 'Invoice split into ticket and food lines, since an all-inclusive '
                                        'suite with meals not separately stated kills the meal deduction '
                                        '[David Fiene — QPC4K8A6GJg @ 00:05:16]. Two-field email sent '
                                        'before the event asking who is hosting and who the clientele is, '
                                        'so staff know whether the suite is closing a $2 million deal or '
                                        'partying [ALSD — ImKo957VLSo @ 00:02:32].'},
                            {'name': 'per_game_suite_math',
                             'type': 'text',
                             'prompt': 'Convert a per-game suite price into an equivalent number of '
                                       'standard tickets for the same week, note what the suite excludes '
                                       'such as alcohol, and judge whether the conversion makes the suite '
                                       'pitch stronger or weaker for this client.',
                             'example': 'A SoFi terrace suite ran $41,000 per game with no alcohol '
                                        'included, equal to 221 top-section tickets at $185 for the same '
                                        'week against the 49ers [Morning Brew — ow9KXpcvvEg @ 00:04:56]. '
                                        'For a client hosting twelve guests, the per-head suite cost still '
                                        'dwarfs standard seats, so the pitch rests on privacy and hosting, '
                                        'not price.'},
                            {'name': 'psl_resale_route',
                             'type': 'text',
                             'prompt': 'Name the resale route for any PSL-backed premium seats, record the '
                                       'transaction fee percentage on a secondary license sale, and '
                                       'confirm the annual season-ticket purchase is current so the '
                                       'license cannot be revoked or sold out from under you.',
                             'example': 'Allegiant secondary PSL fee is 10% of the negotiated price, so '
                                        'four seats at $16,000 each ($64,000) carry a $6,400 fee [Power '
                                        'Raider — o_WpoJl9phM @ 00:04:19]. Game resales route through '
                                        'Ticketmaster even though it charges more, because a bad buyer '
                                        'from a cheaper site can get the PSL revoked [Power Raider — '
                                        'o_WpoJl9phM @ 00:20:53].'},
                            {'name': 'seat_selection_and_dead_games',
                             'type': 'textarea',
                             'prompt': 'Identify the specific seat location you are targeting for resale '
                                       'perception, such as a last-row lower level priced against a club '
                                       'tier, and list which games on the schedule you expect to give away '
                                       'or sell below cost.',
                             'example': 'Target the last row of the 100 level: casual buyers see 100 and '
                                        'assume they are closer, while the pricier 200 club level makes '
                                        '100-level listings look like a deal [Dave Chung — CpHB_gOGYSs @ '
                                        '00:04:22]. Weak-opponent dates are budgeted as giveaways or '
                                        'below-cost dumps even with a winning roster [Dave Chung — '
                                        'CpHB_gOGYSs @ 00:06:30].'},
                            {'name': 'paddock_club_buyer_profile',
                             'type': 'textarea',
                             'prompt': 'Profile the likely Paddock Club buyer for this race, recording the '
                                       'seat price ceiling, the share of guests who attend company-paid or '
                                       'free, and whether your pitch should target corporate hosts or '
                                       'individual enthusiasts paying their own way.',
                             'example': 'Seats run up to $15,000 per race weekend, with most guests '
                                        'company-paid, against 65,000 guests and over $450M in revenue '
                                        '[Pit Stop Lab — qjr3BHunOxo @ 00:00:00]. Kayvan Goes estimates '
                                        'about 30% of the room pays nothing [Kayvan Goes — 2UDtC8EP8GA @ '
                                        '00:21:38], so the pitch targets the corporate host funding the '
                                        'table.'},
                            {'name': 'access_and_logistics',
                             'type': 'textarea',
                             'prompt': 'Map the access timeline for the race day, including stand opening '
                                       'against track opening, pit lane opening before lights out, garage '
                                       'tour timing, and the exit route out of the venue, so no premium '
                                       'guest loses time or the race.',
                             'example': 'Pit lane opens to ticket holders about 90 minutes before lights '
                                        'out [SOL - Supercars of London — rQvPQuH1YXw @ 00:05:16]. An 8:30 '
                                        'track with a 9:30 stand cost one premium buyer a race [Global '
                                        'Nomads — ePgxCdmE8o8 @ 00:14:58], and a one-gate exit funnel '
                                        'stretched a Silverstone McLaren hospitality day to about 12 hours '
                                        '[LawVS — 0KKYkQr1SBk @ 00:15:22].'},
                            {'name': 'value_and_tier_choice',
                             'type': 'textarea',
                             'prompt': 'Choose the hospitality tier for this client by comparing entry and '
                                       'upgrade prices at the chosen circuit, verifying the seat count '
                                       'behind each ticket, and stating honestly whether networking is '
                                       'staffed or should be dropped from the pitch.',
                             'example': 'Melbourne spread runs from a $600 Champions Club to a $6,000 Red '
                                        'Bull Pit Lane, and about $6,000 per person bought a run at '
                                        'roughly 40 available seats [Global Nomads — ePgxCdmE8o8 @ '
                                        '00:31:34]. Networking scored 1 out of 10 when left unassisted '
                                        '[Kayvan Goes — 2UDtC8EP8GA @ 00:24:42], so it stays out of the '
                                        'pitch.'}],
                 'completion_gate': 'No premium quote leaves the desk until the full price ladder is '
                                    'priced, the sellout timing is logged, suite invoices are split into '
                                    'ticket and food lines, PSL resales are routed through Ticketmaster '
                                    'with renewals current, and every race-day access window and exit '
                                    'route is mapped in writing.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Marquee-Event Access and Personal Seat License Deal Sheet',
                 'purpose': 'Separate official-channel lockboxes from resale-driven marquee events, then '
                            'underwrite personal seat licenses as obligations rather than assets. This '
                            'sheet covers Masters ballots and badge risk, championship listing reads, UFC '
                            'and tennis access, and the full fee, financing and exit math behind every '
                            'license purchase.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Classify each event first as an official-channel-only lockbox or a '
                                  'resale market, because that single call decides every later step.',
                                  'For the Masters, file one ballot per household address and price '
                                  'gate-level voiding risk before touching any third-party badge.',
                                  'Treat every championship listing as an ask, buy only on verified sites, '
                                  'and keep proof of purchase for every order.',
                                  'For any personal seat license, confirm the full renewal obligation and '
                                  'financing terms before discussing price with a seller.',
                                  'Net out both marketplace fees and any loan payoff, then stress-test the '
                                  'exit against a losing season before signing anything.'],
                 'fields': [{'name': 'masters_ballot_plan',
                             'type': 'textarea',
                             'prompt': 'Record your Masters ballot plan for the household, including the '
                                       'application window, the single address used, the days and ticket '
                                       'count requested, and the odds you are assuming, so nobody else at '
                                       'the address files a duplicate.',
                             'example': 'One application per household inside the June 1-20 window; '
                                        'duplicate entries from roommates get both disqualified [Gameday '
                                        'Guides — LtTBm2wHjoE @ 00:01:03]. Requested two tickets for every '
                                        'day, since a winner is only offered one day anyway [Sports Travel '
                                        'Tom — iKAz6YJRTXI @ 00:02:35]. Assumed odds: under 1%, against '
                                        'the 3-5% optimistic read.'},
                            {'name': 'masters_resale_risk',
                             'type': 'textarea',
                             'prompt': 'Before touching any third-party Masters badge, write down the '
                                       'enforcement risk at the gate, the rental price you are being '
                                       'quoted per day, and whether a package route with guaranteed '
                                       'attendance is the safer use of client money.',
                             'example': 'Augusta is voiding tickets at the gate with RFID tracking to '
                                        'catch brokers and permanently revoking lifetime badges [Gameday '
                                        'Guides — LtTBm2wHjoE @ 00:01:59]. Brokers still rent badges for '
                                        'up to four grand a day. Packages run from $4,000 upwards of '
                                        '$10,000 but secure attendance [Sports Travel Tom — iKAz6YJRTXI @ '
                                        '00:04:58], so the package wins.'},
                            {'name': 'lodging_arbitrage',
                             'type': 'text',
                             'prompt': 'Identify a lodging base outside the host city that avoids '
                                       'event-week markups, record the nightly rate against the in-town '
                                       'rate, and set the date you will book, ideally the moment lottery '
                                       'or allocation results are released.',
                             'example': 'Base set in Columbia, South Carolina at $100 to $200 a night '
                                        "instead of Augusta's 5 to 10x markups, saving $300 to $800 per "
                                        'night [Gameday Guides — LtTBm2wHjoE @ 00:06:02]. Booking fires as '
                                        'soon as lottery results drop in July. The same logic applies at '
                                        'the Super Bowl: look outside the city for the best price.'},
                            {'name': 'championship_listing_read',
                             'type': 'textarea',
                             'prompt': 'For a college or tennis championship, separate listed asking '
                                       'prices from completed sales, record the floor and premium seat '
                                       'asks, and note whether you expect prices to fall toward the event '
                                       'or hold because supply is thin.',
                             'example': 'IU vs Miami listings started above $3,000 in the nosebleeds and '
                                        'reached $20,000 at the 50-yard line [WTHR — OSa-CK_qebs @ '
                                        '00:00:01]. Those are asks, not sales; an IU economist says nine '
                                        'times out of ten prices come down near game time because most '
                                        'sellers never clear at those numbers [WTHR — OSa-CK_qebs @ '
                                        '00:01:13].'},
                            {'name': 'ufc_vip_package',
                             'type': 'textarea',
                             'prompt': 'Price the UFC VIP option under review, listing the pair cost, the '
                                       'inclusions such as weigh-in access or transportation, and a '
                                       'sightline check for any cheaper seat, so the client compares the '
                                       'full experience rather than headline price.',
                             'example': 'Front-row cage-side pair at T-Mobile Arena cost 46,747.22 '
                                        'Canadian, roughly $35,000 American, with weigh-in stage access '
                                        'and private transportation [Troydan — 0jqhQFvHHcc @ 00:00:32]. '
                                        'Cheaper alternative flagged: a $470 last-section seat put a metal '
                                        'pillar between the buyer and the cage [MMALeaked — 2vauuB_YXFc @ '
                                        '00:04:26]. Sightline photos required before quoting.'},
                            {'name': 'tennis_and_festival_access',
                             'type': 'textarea',
                             'prompt': 'Document the access route for tennis or festival inventory, '
                                       'including any debenture or tradable seat asset, free pre-event '
                                       'days worth using, and the checkout tactics you will run if the '
                                       'purchase queue crashes or restarts mid-sale.',
                             'example': 'Wimbledon Center Court debentures for 2026-2030 cost more than '
                                        '$275,000, a 75% profit on previous prices [Firstpost — '
                                        'R9QNsXzjvxU @ 00:02:22]. US Open fan week offers free qualifying '
                                        'and uncrowded practice courts [BAG & TRAVEL — B2P9oIBqq5Q @ '
                                        '00:01:37]. For Coachella crashes: cycle tabs, go incognito, '
                                        'switch Chrome profiles [Courtney Willis — f5hPIW3U13c @ '
                                        '00:01:20].'},
                            {'name': 'psl_obligation_check',
                             'type': 'textarea',
                             'prompt': 'Confirm you understand the license buys zero tickets, then record '
                                       'the one-time PSL fee, the annual season-ticket bill it obligates, '
                                       'any financing terms, and whether your cash flow can cover every '
                                       'renewal before the license is forfeited.',
                             'example': 'A PSL holder must purchase and renew season tickets each year, or '
                                        'the PSL is forfeited and sold to someone else [JCFB — Dl5FeuC7tUA '
                                        '@ 00:03:05]. The Bills contract forfeits on non-payment [9NEWS — '
                                        'w0cU0-OiMB8 @ 00:03:26]. Financing modeled at 10% over ten years, '
                                        'with every future renewal budgeted before signing.'},
                            {'name': 'psl_market_and_why',
                             'type': 'text',
                             'prompt': 'Record the price range for licenses in the target market and the '
                                       'gross the team raised, then note why the owner prefers PSLs over '
                                       "higher ticket prices, so you understand the seller's incentive "
                                       'before negotiating any purchase.',
                             'example': 'Buffalo sold over 53,000 licenses priced from $750 to $50,000 for '
                                        'approximately $262 million gross, beating a $225 million target '
                                        '[THE MARKUP FILES — rT4gQkoEVDI @ 00:01:40]. Owners prefer PSLs '
                                        'because 34% of ticket revenue is shared with other teams while '
                                        'PSL revenue is not, and the cash arrives early [9NEWS — '
                                        's4p8gnL-WFw @ 00:01:12].'},
                            {'name': 'psl_offer_strategy',
                             'type': 'textarea',
                             'prompt': 'Write your offer ladder for resale licenses: the asking price, '
                                       'your opening lowball, the counter you expect, the number of '
                                       'sellers you will approach in parallel, and how you will verify any '
                                       'counterparty found in social media groups.',
                             'example': 'Answer a $3,500 two-seat ask with $2,800 and expect a counter '
                                        'near $3,100 [TicketWire — hlfwsoMBQS0 @ 00:02:11]. Lowballs go to '
                                        'several sellers at once; the route saved roughly $3,000 to $4,000 '
                                        '[TicketWire — M80btlo7xJc @ 00:01:48]. Facebook sellers are '
                                        'checked as real people with legit offers, since scams happen '
                                        'every day there.'},
                            {'name': 'psl_flip_and_exit',
                             'type': 'textarea',
                             'prompt': 'Net out a planned license flip by subtracting both marketplace '
                                       'fees and any loan payoff, list which games you will sell '
                                       'individually to recoup costs, and stress-test the exit against a '
                                       'losing season with few willing buyers.',
                             'example': 'A $10,000 Raiders license sale nets the seller $8,800 and costs '
                                        'the buyer $11,200 after 12% fees on each side [THE MARKUP FILES — '
                                        'rT4gQkoEVDI @ 00:13:14]. Unwanted games go to the secondary '
                                        'market to recover part of the investment, and the exit is tested '
                                        'against Falcons-style defaults around 2020 [9NEWS — w0cU0-OiMB8 @ '
                                        '00:03:41].'}],
                 'completion_gate': 'Close the deal sheet only when every marquee event is classified as '
                                    'lockbox or resale market, the Masters ballot is filed once per '
                                    'household, championship prices are logged as asks versus sales, and '
                                    'every license purchase shows renewal coverage, both-side fees, loan '
                                    'payoff and a losing-season exit plan.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'World Cup Orders and Ticketmaster Delivery Control',
                 'purpose': 'Price World Cup seats match by match, choose hospitality on value, screen out '
                            'scam channels, and carry every order through a verified Ticketmaster or FIFA '
                            'app transfer so the buyer ends up inside the stadium instead of stranded in '
                            'the security line.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Work through the fields in order, because channel screening and pricing '
                                  'must be settled before any transfer is attempted.',
                                  'Cite the practitioner source for every figure you record, using the '
                                  'channel name, clip ID and timestamp.',
                                  'Price every seat from completed sales and all-in totals, never from '
                                  'asking prices or teaser listings.',
                                  'Confirm the ticket is visible in the official app days before kickoff, '
                                  'not on game day.',
                                  'Stop and escalate any order where a paper ticket, an unverified seller '
                                  'or a missing barcode appears.'],
                 'fields': [{'name': 'match_premium_tier_map',
                             'type': 'textarea',
                             'prompt': 'List every World Cup fixture you are considering and sort each '
                                       'into a premium tier or an opening-price tier. Note which nations '
                                       'or star players drive the demand, and record the cheapest listing '
                                       'you can actually see today for each match.',
                             'example': 'Premium tier: Portugal, Argentina and Mexico fixtures plus any '
                                        'Messi match, because brokers set price match by match and those '
                                        'nations command the top of the board. Opening tier: San Francisco '
                                        'and some Kansas City games with sub-$300 openings. The Houston '
                                        'broker treats the tournament like a Super Bowl and says buy now '
                                        '[KPRC 2 Click2Houston — UVUOSv2U_BM @ 00:02:47].'},
                            {'name': 'fee_load_comparison',
                             'type': 'textarea',
                             'prompt': 'Compare the all-in cost of buying the same seat through a '
                                       'secondary site versus a local broker. Write the listed price, the '
                                       'buyer fee, the seller fee the broker avoids, and the final number '
                                       "that leaves the client's account on each route.",
                             'example': 'Secondary route: StubHub and similar sites charge the buyer a fee '
                                        'and charge the seller a fee, about 15 to 20 percent on each side '
                                        '[KPRC 2 Click2Houston — UVUOSv2U_BM @ 00:05:31]. Broker route: '
                                        'the Houston broker pitches local inventory as the way to save the '
                                        'client those fees. Record both totals side by side before quoting '
                                        'a price.'},
                            {'name': 'hospitality_package_selection',
                             'type': 'textarea',
                             'prompt': 'Choose a hospitality level for the client and justify it against '
                                       'general admission. Record the package price, what food, drink and '
                                       'lounge time are included, when it was purchased, and whether the '
                                       'client cares more about the teams or the experience itself.',
                             'example': 'Entry packages start at $1,400 across all three host nations '
                                        '[Adventure & Sports — qSTxMUdp-ro @ 00:00:16]. One buyer took the '
                                        'VIP level, second most expensive of four, nine months out for '
                                        '$2,900 [Travel with Frodo — 3jMjNVjPzTo @ 00:00:46]. Another '
                                        'pre-bought FIFA Pavilion before the draw because the teams did '
                                        'not matter [Landon Kissell — 76zFs7tuCJw @ 00:00:40].'},
                            {'name': 'lounge_capacity_check',
                             'type': 'textarea',
                             'prompt': 'Before arrival, assess whether the hospitality lounge is likely to '
                                       'be oversold. Note the seating plan, food service timing, and your '
                                       'on-arrival routine for securing a seat, and list any in-lounge '
                                       'services such as merchandise that beat the outside queues.',
                             'example': 'An oversold $2,000 Champions Club ran out of seating and guests '
                                        'ate off bins until chairs freed up after desserts were pulled '
                                        '[AwayDays — Hl-tVhzYfsw @ 00:20:50]. Grab and hold a seat on '
                                        'arrival. The outside FIFA shop queued massively an hour before '
                                        'kickoff while the in-lounge store had little queue [Travel with '
                                        'Frodo — 3jMjNVjPzTo @ 00:06:29].'},
                            {'name': 'transfer_visibility_check',
                             'type': 'text',
                             'prompt': 'Record the date and time you confirmed the ticket was actually '
                                       'transferred and visible in the official FIFA app under the '
                                       "client's account. Note how many days remained before kickoff and "
                                       "who on your team verified it on the client's phone.",
                             'example': 'Confirmed visible in the FIFA app five days out, verified on the '
                                        "client's phone by the account lead. The failure case to avoid: a "
                                        'buyer learned in the security line, 20 minutes before kickoff, '
                                        'that the only option was a refund, with two 16-year-olds '
                                        'expecting to attend since January [CBS Boston — QRxTlhb8Bt4 @ '
                                        '00:02:01].'},
                            {'name': 'counterfeit_and_channel_screen',
                             'type': 'textarea',
                             'prompt': 'List every channel where the client has been offered seats and '
                                       'mark each as approved or rejected. Flag paper or in-hand tickets, '
                                       'prices far under the online market, and any platform that offers '
                                       'no buyer guarantee while barcodes remain unreleased.',
                             'example': 'Rejected: a paper ticket offered in hand well under the online '
                                        'price, since FIFA issues only mobile tickets [KPRC 2 '
                                        'Click2Houston — UVUOSv2U_BM @ 00:06:17]. Rejected: Facebook '
                                        'Marketplace, social media sellers and Craigslist, which offer no '
                                        'buyer protection while barcodes stay unreleased [WFAA — '
                                        'OSbD9xp5Dw4 @ 00:01:26]. Approved: a marketplace with a written '
                                        'guarantee.'},
                            {'name': 'completed_sales_pricing',
                             'type': 'textarea',
                             'prompt': "Price the client's seat from completed sales rather than active "
                                       'listings. Record the recent average final sale price, the average '
                                       'active listing, and the gap between them, then explain which '
                                       'number you quoted and why the other one misleads.',
                             'example': "Final-week snapshot: SeatGeek's seven-day average final sale "
                                        'price sat above $11,000 while average active listings ran above '
                                        '$18,000, with a few FIFA-platform listings near $32,000 [Lessons '
                                        'Untold — Je00xGIU3m0 @ 00:00:22]. Quote the $11,000 sale figure, '
                                        'because anyone can list at any number and an unsold listing is '
                                        'not the market rate [NBC New York — -NeAkVXcsP4 @ 00:03:38].'},
                            {'name': 'transfer_execution_log',
                             'type': 'textarea',
                             'prompt': 'Log each Ticketmaster transfer step for the order: event selected '
                                       'in My Events, seats chosen, verification code passed, recipient '
                                       'address confirmed, and the moment the buyer accepted. Note whether '
                                       'the transfer button was live and whether you used website or app.',
                             'example': 'Transfer button confirmed live; no delivery delay, hard stock or '
                                        'will call block [thumbsuprun — MP1aH4hgG70 @ 00:01:35]. Four '
                                        'seats sent from the Ticketmaster website on a phone, '
                                        'multi-selected to one email instead of one at a time in the app '
                                        '[Poolarity - Life Hacks — IENQeieAOCo @ 00:00:00]. Buyer '
                                        'accepted; sender barcodes died on acceptance.'},
                            {'name': 'recipient_address_confirmation',
                             'type': 'text',
                             'prompt': 'On mobile transfers, record exactly how you confirmed the '
                                       "recipient's email before sending, since no confirmation email "
                                       'arrives afterward. Note the address shown on the confirmation '
                                       "screen and whether it matched the buyer's order record character "
                                       'for character.',
                             'example': "Pasted the buyer's email into the Last Name field before hitting "
                                        'transfer, so the confirmation screen displayed the exact address '
                                        'that received the seats [thumbsuprun — MP1aH4hgG70 @ 00:04:41]. '
                                        'Screen matched the order record exactly. No screenshot or Apple '
                                        'Wallet copy was sent, because entry scanners reject copies of '
                                        'dynamic barcodes [Nexustech — lBLVmAx5wkQ @ 00:02:13].'},
                            {'name': 'barcode_and_refund_contingency',
                             'type': 'textarea',
                             'prompt': 'Write the contingency plan for barcode timing and event changes. '
                                       'Record when barcodes should appear, the transfer deadline, what '
                                       'happens if the event is postponed or cancelled, and which refund '
                                       'or credit lane applies to how the seats were purchased.',
                             'example': 'Barcodes typically surface 24 to 48 hours out [Helpful Solutions '
                                        '— hNlTOy1daSA @ 00:00:19]; transfer cutoff assumed at 72 hours '
                                        '[Gadget Tune — 8yXxF_U1uek @ 00:01:13]. If postponed, old '
                                        'barcodes scan at the new date because they tie to the event '
                                        'manifest [thumbsuprun — MP1aH4hgG70 @ 00:05:39]. Seats bought '
                                        'into an already-postponed event generally get no refund lane.'}],
                 'completion_gate': 'Do not mark this worksheet complete until every World Cup order shows '
                                    'a completed-sales price, an approved channel with a buyer guarantee, '
                                    'a confirmed recipient address, a written barcode and refund '
                                    'contingency, and tickets verified as visible in the official app days '
                                    'before kickoff.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'AXS Back Office and Resale Compliance Ledger',
                 'purpose': 'Keep AXS and back-office inventory clean from purchase email to door scan, '
                            'and keep every buy and listing on the legal side of the BOTS Act, the FTC fee '
                            'rule and the refund guarantees your operation publishes.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Complete the AXS audit fields before listing any inventory on a '
                                  'marketplace.',
                                  'Record every account used in an on-sale and the real, provable person '
                                  'it belongs to.',
                                  'Move tickets only through platform transfers that cancel the original '
                                  'QR code and issue a new one.',
                                  'Show the all-in price first on every listing and keep the published '
                                  'guarantee attached to each order.',
                                  'Cite the channel, clip ID and timestamp for every rule or figure you '
                                  'rely on.'],
                 'fields': [{'name': 'axs_credential_and_email_audit',
                             'type': 'textarea',
                             'prompt': 'Audit each AXS order before listing it. Record the purchase email '
                                       'tied to the order, whether the tickets appear in the phone app, '
                                       'the delivery method the venue predetermined, and whether a '
                                       'delivery change is still needed through live chat.',
                             'example': 'Purchase email matches the account; tickets display digitally on '
                                        'mobile after booking [Web Mind — RDQeHkadlqk @ 00:00:59]. '
                                        'Delivery method was predetermined by the venue, and the one '
                                        'change requested went through a live chat agent who took a while '
                                        'to respond, so it was locked early [Simply Finance — s7E1Yc3RoQc '
                                        '@ 00:00:19]. If the app misbehaves, reinstall it completely.'},
                            {'name': 'cross_platform_exit_route',
                             'type': 'textarea',
                             'prompt': 'For every AXS seat headed to a buyer on another platform, write '
                                       'the exit route before you sell. Note whether a direct transfer '
                                       'exists, which resale marketplace you will list on instead, and the '
                                       'fallback if the buyer insists on Ticketmaster delivery.',
                             'example': 'Buyer wants Ticketmaster delivery, but direct cross-platform '
                                        'transfers between AXS and Ticketmaster are generally not '
                                        'supported [AidensGotGuides — xEM0K5YLBZk @ 00:02:09]. Route: list '
                                        'the AXS seats on StubHub or SeatGeek and let the buyer purchase '
                                        'there. Guide Gurus describes an AXS-to-SeatGeek claim-code '
                                        'transfer, so confirm it works for this event before promising '
                                        'it.'},
                            {'name': 'qr_reissue_transfer_record',
                             'type': 'text',
                             'prompt': 'Record how each ticket was moved to its new owner and confirm the '
                                       'original QR code was canceled. Note the platform used, the new '
                                       "registered owner's name, and the date you confirmed that a fresh "
                                       'QR code was issued to them.',
                             'example': 'Moved by platform transfer, never by emailed PDF. The original QR '
                                        'code was canceled and a new one generated and issued to the new '
                                        'registered owner, so the old code is dead at the door [PromoTix — '
                                        "IdHpcPxQTfU @ 00:21:49]. Confirmed the reissue on the buyer's "
                                        'account two days before the event and logged the owner name.'},
                            {'name': 'comp_and_will_call_controls',
                             'type': 'textarea',
                             'prompt': 'List every guest-list comp and contest-winner ticket for the event '
                                       'and how each was issued. Note whether it was set to will call, '
                                       'what identification the guest must show, and how you prevent free '
                                       'tickets from undercutting your paid inventory.',
                             'example': 'All comps and contest-winner tickets issued as will call, so each '
                                        'guest is notified without a QR code and must show ID or another '
                                        'form of identification for a manual check-in [PromoTix — '
                                        'IdHpcPxQTfU @ 00:33:47]. Royall says this stops free tickets '
                                        "being resold and flooding the market against the organizer's own "
                                        'sales.'},
                            {'name': 'promotix_fee_and_tier_setup',
                             'type': 'textarea',
                             'prompt': 'Document the event setup before the on-sale: shared inventory '
                                       'caps, the order of daisy-chained price tiers, and any organizer '
                                       'percentage added on top. Record exactly how that percentage '
                                       'appears to the buyer at checkout and the all-in total shown.',
                             'example': 'Organizer fee set at 10% on top of ticket price; buyers see it '
                                        'only inside a single service fees line, so a $20 ticket clears '
                                        'above face value [PromoTix — IdHpcPxQTfU @ 00:10:46]. Because the '
                                        'all-in price must be shown first, the total including that fee '
                                        'leads the listing rather than appearing at checkout [The Fine '
                                        'Print Audit — SdsGfL0IdKk @ 00:06:48].'},
                            {'name': 'marketplace_mapping_check',
                             'type': 'textarea',
                             'prompt': 'Before leaving the event detail page in your inventory tool, check '
                                       'every marketplace icon. Record which icons are mapped and active, '
                                       'which are grayed out, what mapping is still missing, and whether '
                                       'all flagged edits were published to the marketplaces.',
                             'example': 'Three marketplace icons active blue; one grayed out, meaning no '
                                        'mapping exists for that event yet, so inventory will not '
                                        'broadcast there until mapping is in place and the group is '
                                        'activated [Logitix — YaZpToURgBk @ 00:01:20]. Mass edit applied '
                                        'the new price to every section, and all flagged edits were '
                                        'published before closing the page.'},
                            {'name': 'door_scan_and_box_office_protocol',
                             'type': 'textarea',
                             'prompt': 'Write the door and box office protocol for event night. Explain '
                                       'how staff answer the check-in prompt on walk-up sales, how a split '
                                       'party with a missing seat is admitted, and how every door phone '
                                       'stays synchronized during entry.',
                             'example': 'Box office: answer no to check-in when the buyer enters later so '
                                        'items stay checked out for scanning, yes only when they walk '
                                        'straight in [PromoTix — IdHpcPxQTfU @ 00:29:26]. Split party: tap '
                                        'the missing seat to leave it out and admit the rest; the rescan '
                                        'shows amber, and the list updates every few seconds [Brian Jones '
                                        '— 4Ddm_7kF3nc @ 00:04:26].'},
                            {'name': 'purchase_limit_compliance',
                             'type': 'textarea',
                             'prompt': 'For every on-sale you entered, record the posted per-person '
                                       'purchase limit, the number of accounts used, and the real, '
                                       'provable person behind each account. Explain why your method does '
                                       'not depend on beating any limit the seller set.',
                             'example': 'Six-ticket limit; one account, one named buyer, six tickets. '
                                        "Methods that depend on beating a seller's limit, whether bots, "
                                        'checkout scripts or armies of accounts, are what the BOTS Act '
                                        'punishes at over $53,000 per violation [Hustle Audit — '
                                        'NOBp14Qcy_8 @ 00:06:47]. Discovery will ask the operator to show '
                                        'the human behind every account [NBC News — BOIfCHick7o @ '
                                        '00:04:05].'},
                            {'name': 'enforcement_case_lessons',
                             'type': 'textarea',
                             'prompt': 'Summarize two enforcement cases that shape your own buying rules. '
                                       'For each, record the alleged conduct, the account or ticket counts '
                                       'involved, the money at stake, and the specific rule you adopted so '
                                       'your operation never repeats that pattern.',
                             'example': 'Key Investment Group allegedly used 49 accounts for 273 Eras Tour '
                                        'tickets against a six-ticket cap; it says no bots were used '
                                        '[Hustle Audit — NOBp14Qcy_8 @ 00:05:27]. REPS allegedly ran up to '
                                        '40 accounts per name to spend $1.3 billion; it denies this and no '
                                        'court has ruled [Dot Detective — 7SSPFtppfGE @ 00:00:17]. Rule '
                                        'adopted: one verified person per account.'},
                            {'name': 'listing_disclosure_and_guarantee',
                             'type': 'textarea',
                             'prompt': 'Write the listing and guarantee policy your operation publishes. '
                                       'Confirm the all-in price appears first on every listing, state the '
                                       'refund owed on a canceled event, and state what the buyer receives '
                                       'if a promised ticket is never delivered.',
                             'example': 'All-in total first: a listing showing $299 then $422.45 at '
                                        'checkout is the practice the FTC fee rule bans [The Fine Print '
                                        'Audit — SdsGfL0IdKk @ 00:06:48]. Full refund when the promoter '
                                        'refunds a canceled event; 200% guarantee on any undelivered '
                                        'ticket [BBB National Programs — 111H45dtJsI @ 00:07:47]. No '
                                        'selling unheld seats, the move that collapsed Ticket Secrets.'}],
                 'completion_gate': 'Do not mark this worksheet complete until every AXS seat has a '
                                    'confirmed exit route, every transfer shows a reissued QR code, every '
                                    'marketplace icon is mapped or deliberately excluded, every account '
                                    'maps to a provable person within the posted limit, and every listing '
                                    'leads with the all-in price.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Concert Pricing and Flip Underwriting Sheet',
                 'purpose': 'Underwrite each concert or season-seat flip against real availability, '
                            'platinum conversion, fee drag and sell-through, so capital goes only to '
                            'events where demand outruns seats and the exit is confirmed before any '
                            'payment is made.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Screen the event and run the inventory math before entering any queue.',
                                  'Re-verify the price on the final payment screen and record the all-in '
                                  'ratio for every order.',
                                  'Check for face-value caps and single-platform resale rules before '
                                  'buying to flip.',
                                  'Stay inside every posted purchase limit with one real person per '
                                  'account; volume never justifies crossing it.',
                                  'Log cost, comparable listing and spread for every buy, citing the '
                                  'channel, clip ID and timestamp.'],
                 'fields': [{'name': 'inventory_availability_reality',
                             'type': 'textarea',
                             'prompt': "Before planning a buy, estimate how much of the event's inventory "
                                       'will actually reach public sale. Record insider holds, presale '
                                       'share, and the presales you personally qualify for, including card '
                                       'programs, so you know what remains after early waves.',
                             'example': 'Benchmark: 54% of major-event tickets never reach the public, 16% '
                                        'in insider holds and 38% in presales, with presales alone up to '
                                        '70% at some top shows [Follow The Why — cmeE4rZAlVk @ 00:00:52]. '
                                        'Qualifying presales: Amex, plus Citi Entertainment and Mastercard '
                                        'through Citi Strata; check every presale available [The Credit '
                                        'Nerd — JS9sO0Fx9A0 @ 00:02:23].'},
                            {'name': 'presale_entry_and_platinum_watch',
                             'type': 'textarea',
                             'prompt': 'Record when you entered the first presale waiting room, your queue '
                                       'number, and whether any seats in your target section had converted '
                                       'to Official Platinum or higher face values. Explain why click '
                                       'speed was not part of your plan.',
                             'example': 'Entered the very first presale wave, before the platform gathered '
                                        'demand data to convert seats to Official Platinum or raise face '
                                        'values [thumbsuprun — TpXJCfuFf4o @ 00:06:35]. Platinum '
                                        'conversion can turn a $299 floor seat into $799 mid-checkout. '
                                        'Queue positions are handed out essentially by lottery, so even '
                                        'the fastest fiber can draw number 80,000 [Follow The Why — '
                                        'cmeE4rZAlVk @ 00:02:53].'},
                            {'name': 'final_screen_price_check',
                             'type': 'text',
                             'prompt': 'Record the price shown in your cart and the price shown on the '
                                       'final payment screen for every order. Note the difference in '
                                       'dollars and as a percentage, and whether you completed or '
                                       'abandoned the purchase after seeing it.',
                             'example': 'Cart showed $227 each; the payment screen showed $291 apiece, a '
                                        '30% bump on the last step [Scott Cramer — kFsH01UthzA @ '
                                        '00:11:23]. On a Rolling Stones general admission sale, prices '
                                        'jumped $50, $70 or $90 between cart and checkout [thumbsuprun — '
                                        'TpXJCfuFf4o @ 00:09:44]. Abandoned the order because the margin '
                                        'no longer cleared target.'},
                            {'name': 'all_in_fee_ratio',
                             'type': 'textarea',
                             'prompt': 'Add every line on the order, every fee included, and divide the '
                                       'total by face value. Compare that all-in ratio across sites and '
                                       'note whether the fees scale with ticket price or are rebated to '
                                       'the venue. Then record the single number you will underwrite.',
                             'example': 'Every line added, then divided by face value, and only that '
                                        'all-in total compared across sites, because it is the only number '
                                        'that leaves the account [Business Made Simple — VBp4zpS7F3o @ '
                                        '00:09:17]. Benchmarks: a 27% average primary fee in the GAO '
                                        "sample, and 40% to 50% in a touring band's testimony, with one "
                                        'show hitting 82% [Scott Cramer — kFsH01UthzA @ 00:08:46].'},
                            {'name': 'resale_restriction_screen',
                             'type': 'textarea',
                             'prompt': 'Before buying any tour to resell, check whether resale is capped '
                                       "at face value or restricted to one platform. Record the artist's "
                                       'resale model, who absorbs the original fees, and whether any '
                                       'markup survives once those rules are applied.',
                             'example': "Noah Kahan's model allows resale only on Ticketmaster at base "
                                        'price, so the seller eats the original fees and the markup '
                                        'disappears [Scott Cramer — kFsH01UthzA @ 00:23:58]. Verdict: skip '
                                        'the tour as a flip. Also logged that weak demand can leave '
                                        "resellers with losses, as Beyonce's $35 resale floor showed, so "
                                        'caps are not the only risk.'},
                            {'name': 'event_selection_screen',
                             'type': 'textarea',
                             'prompt': 'Score each candidate event on venue size, day of the week, '
                                       'hometown appeal, and artist streaming audience. Explain why each '
                                       'event is or is not a case where demand outruns seats, and how it '
                                       'compares with headline stadium acts.',
                             'example': 'Small-venue Saturday hometown show with a strong Spotify listener '
                                        'count scores high; a headline stadium act scores low, because '
                                        'both Ticket Flipping and Emmanuel Ak steer operators toward small '
                                        'venues, weekend dates and hometown shows where demand outruns '
                                        'seats. Target: a 25% margin on every ticket, with 9 of 10 selling '
                                        'well [Ticket Flipping — JwHo6if-9Wo @ 00:09:05].'},
                            {'name': 'sell_through_trend_tracker',
                             'type': 'textarea',
                             'prompt': 'Track remaining tickets for the event each day and divide by venue '
                                       'capacity. Record every count, note any jump caused by held '
                                       'inventory being released, and state whether you have seen two or '
                                       'three large drops before trusting the trend.',
                             'example': 'Day one 500 remaining, day two back up to 700 after a release, so '
                                        'no trend yet [Ticket Flipping — hw92haJDs9Y @ 00:11:21]. Waiting '
                                        'for two or three large drops relative to capacity and a real '
                                        'daily downtrend. Flare drop and price alerts are set so each '
                                        'release or price move is logged the moment it happens.'},
                            {'name': 'price_break_and_cart_check',
                             'type': 'textarea',
                             'prompt': 'Identify the price breaks in the section you are buying and choose '
                                       'seats just behind a break. Before paying, check the resale market '
                                       'while seats sit in your cart, and record your cost, the comparable '
                                       'listing, and the projected spread.',
                             'example': '$89 seats behind a 113 break list at 110 to 115, so buy the row '
                                        'where the price drops, not the front row [Ticket Flipping — '
                                        'GORTWFnPPt0 @ 00:04:15]. Cart check: Rush seats at about $300 '
                                        'cost against about $570 listed on StubHub, roughly $270 profit '
                                        'per ticket, confirmed before paying [Emmanuel Ak — RsyNgibgVJY @ '
                                        '00:24:33].'},
                            {'name': 'season_ticket_resale_plan',
                             'type': 'textarea',
                             'prompt': 'Plan how your season seats will be resold across the year. Record '
                                       'when the schedule drops, which games you keep, which you list '
                                       'immediately, the early price per ticket, and how playoff inventory '
                                       'changes your recovery math.',
                             'example': 'List season seats as soon as the schedule drops, since holders '
                                        'know seat locations before the general sale; $75 per ticket six '
                                        'months out in Calgary [thumbsuprun — sQtHQZ6UoRM @ 00:04:57]. '
                                        'Playoffs carry the year: upper-bowl seats costing about $180 '
                                        'resold for over $1,500 by Game 6 [thumbsuprun — sQtHQZ6UoRM @ '
                                        '00:08:00].'},
                            {'name': 'liquidity_and_timing_gate',
                             'type': 'textarea',
                             'prompt': 'Before committing capital, confirm you have time to receive, list, '
                                       'sell and transfer out, and decide whether you are buying late on '
                                       'confirmed scarcity or at release. Record how much cash stays free '
                                       'for the next buy.',
                             'example': 'Timing check passed: tickets arrive in time to receive, list, '
                                        'sell and transfer out before the event [Ticket Flipping — '
                                        'NGFBVOXqxpA @ 00:04:09]. Chose to buy late on confirmed scarcity, '
                                        'single account, within the posted limit. Skipped a second event '
                                        'that would tie up money in dead stock, staying liquid for the '
                                        'next buy [Emmanuel Ak — ETQnblEeP94 @ 00:32:36].'}],
                 'completion_gate': 'Do not mark this worksheet complete until each buy shows a 25% margin '
                                    'case built on completed comparables, a final-screen price check, an '
                                    'all-in fee ratio, a resale-restriction screen, a sell-through trend '
                                    'with real drops, purchases inside every posted limit, and confirmed '
                                    'time to transfer out with cash left free for the next buy.'}]}
