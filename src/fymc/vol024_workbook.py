from __future__ import annotations

def build_volume_024_workbook() -> dict:
    return {'workbook_id': 'wb-024-tax-lien-investing',
 'volume_id': 'vol-024-tax-lien-investing',
 'title': 'Tax Lien Investing — Practitioner Testimony Operator Workbook',
 'subtitle': 'A Field Workbook for Reading Lien Foundations, State Rulebooks, Auction Yields, Online '
             'Sales, and Over-the-Counter Leftovers Before Any Dollar Moves',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Foundations and Model Selection Ledger',
                 'purpose': 'Turn the core lien trade into written commitments: one county, a measured '
                            'competition ratio, a known rate ceiling, honest redemption math, a chosen '
                            'model between liens, deeds and redeemable deeds, a budget path, and an exit '
                            'logged before the first bid.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Complete every field for a single county only; spreading research '
                                  'across several counties before learning one auction defeats the purpose '
                                  'of this ledger.',
                                  'Call the county treasurer before filling the competition and rate '
                                  'fields, and write the answers exactly as the county gives them, with '
                                  'the date of the call.',
                                  'Show your arithmetic in every return field, including face amount, bid '
                                  'rate, months held, and dollars collected, so a reviewer can check each '
                                  'figure.',
                                  'Treat ownership as the rare outcome: plan around redemption first, then '
                                  'write how you would handle the parcel if the certificate never pays '
                                  'off.',
                                  'Leave no field blank; if a number is unknown, write what is missing and '
                                  'who will supply it before the auction.'],
                 'fields': [{'name': 'target_county_profile',
                             'type': 'text',
                             'prompt': 'Name the single county you will study first, the state it sits in, '
                                       'and whether it sells liens, deeds, or redeemable deeds. Record why '
                                       'you chose one county instead of spreading across several, and what '
                                       'you still do not know about its auction.',
                             'example': 'Duval County, Florida, a lien state with certificates capped at '
                                        "18 percent. Lien Ledger's rule drives the choice: start small in "
                                        'one county and learn how its auction works [Lien Ledger — '
                                        "H9fPhqUYPfc @ 00:08:00]. Still unknown: last year's lien count, "
                                        'attendance, and how many certificates went unsold to the county.'},
                            {'name': 'competition_ratio_check',
                             'type': 'textarea',
                             'prompt': 'Write down the number of liens the county sold last year and how '
                                       'many bidders attended that sale. Divide one by the other, compare '
                                       "the result to the ratio test, and decide whether this county's "
                                       'crowd leaves room for a newcomer.',
                             'example': "Called the treasurer using Dustin Hahn's phone script: 240 liens "
                                        'sold last year with about 20 people in the room, roughly 12 liens '
                                        'per bidder. That sits inside the 200 to 500 liens with 20 '
                                        'attendees target, far from the 30 liens with 50 attendees trap '
                                        '[Dustin Hahn — eNKIUQC6io0 @ 00:05:44]. County passes the '
                                        'competition screen.'},
                            {'name': 'statutory_rate_ceiling',
                             'type': 'text',
                             'prompt': 'Record the statutory interest ceiling for your target state and '
                                       'note that it is only a maximum, not a promise. List two other '
                                       'state ceilings for comparison so you can see where your state '
                                       'ranks before setting any bidding expectations.',
                             'example': 'Florida ceiling: 18 percent. Comparison ceilings from Ted '
                                        "Thomas's list: Arizona 16 percent, Iowa 24 percent, Illinois 36 "
                                        'percent, with Florida offering roughly one million certificates a '
                                        'year [Gerald Harris — nMj50Itu21Q @ 00:03:13]. Note to self: 18 '
                                        'percent is where bidding starts, and the crowd decides how far '
                                        'below it the winning rate lands.'},
                            {'name': 'minimum_return_floor_math',
                             'type': 'textarea',
                             'prompt': "Work one redemption scenario using your state's minimum return "
                                       'rule. Show the lien face amount, your bid rate, the months until '
                                       'redemption, and the dollars collected, then state whether a zero '
                                       'percent bid would forfeit the minimum entirely.',
                             'example': '$1,000 lien bid at 0.25 percent, redeemed in 3 months. Interest '
                                        'at a quarter percent would be under $1, but the 5 percent floor '
                                        'pays $50, roughly 20 percent annualized [Lien Ledger — '
                                        'H9fPhqUYPfc @ 00:05:06]. A flat 0 percent bid gets no minimum at '
                                        'all, so my floor bid is 0.25, never zero [Lien Ledger — '
                                        'H9fPhqUYPfc @ 00:04:40].'},
                            {'name': 'redemption_expectation',
                             'type': 'textarea',
                             'prompt': 'State the redemption rate you are planning around and the outcome '
                                       'you expect on most certificates. Explain in your own words why '
                                       'that rate makes you a lender rather than a cheap-house buyer, and '
                                       'what share might end in foreclosure.',
                             'example': 'Planning at 95 percent redemption: most of the time the owner '
                                        'comes back and pays the back taxes [Red Lotus Chic — ehSkuiHT060 '
                                        '@ 00:05:21]. The D.C. review of 9,395 properties showed 70 '
                                        'percent redeemed, 16 percent canceled, 13 percent in progress, '
                                        'and only 1 percent foreclosure [Lien Ledger — H9fPhqUYPfc @ '
                                        '00:03:33]. I am a lender first.'},
                            {'name': 'model_choice_lien_deed_redeemable',
                             'type': 'textarea',
                             'prompt': 'Choose between a tax lien, a tax deed, and a redeemable deed for '
                                       'your first purchase. Describe what each model actually buys you, '
                                       'how often each converts to ownership, and which one fits your '
                                       'budget, patience, and appetite for work.',
                             'example': 'Liens buy a claim plus interest and redeem about 95 percent of '
                                        'the time; redemption deeds redeem about 50 percent or less, so '
                                        'they convert to ownership far more often [Tax Sale Secrets — '
                                        '0adTzNpuLtk @ 00:11:13]. Deeds pay more but mean possession right '
                                        'away [Tax Sale Academy — oKQjnGAQlGs @ 00:09:12]. Choice: liens '
                                        'first, deeds after learning.'},
                            {'name': 'budget_path',
                             'type': 'text',
                             'prompt': 'Write your starting budget in dollars and match it to a path. Note '
                                       'which practitioner rule applies to that budget, whether '
                                       'over-the-counter deeds or small liens, and what you would need to '
                                       'add before the other path becomes realistic.',
                             'example': 'Budget: $15,000. The split runs from Dustin Hahn pushing anyone '
                                        'under $20,000 toward over-the-counter deeds to Casey Deon '
                                        'steering tiny budgets into liens. Ted Thomas sets a $20,000 to '
                                        '$25,000 floor and says $500 is not enough [REtipster — '
                                        'jDYlxXpw-e4 @ 00:36:45]. Path: small liens while reserving two to '
                                        'five grand per file [Tax Sale Secrets — fIPCLCdZlAU @ 00:08:59].'},
                            {'name': 'penalty_vs_interest',
                             'type': 'textarea',
                             'prompt': 'Compare a penalty-style return with an interest-style return on '
                                       'the same dollar amount. Show what each pays if the owner redeems '
                                       'after one month and after twelve months, and note which structure '
                                       'rewards fast redemptions more heavily.',
                             'example': "$1,500 at Georgia's flat 20 percent pays $300 whether redemption "
                                        'comes the next day or in month twelve [Cecil Jones — Yq9tyhYQJGY '
                                        '@ 00:03:41]. An 18 percent lien redeemed in month one nets only '
                                        'about 1.5 percent. That is why Cecil Jones prefers '
                                        'redeemable-deed states over interest-rate liens [Cecil Jones — '
                                        'Yq9tyhYQJGY @ 00:04:13].'},
                            {'name': 'cushion_and_all_in_number',
                             'type': 'textarea',
                             'prompt': 'Size the cushion between what the property is worth and what is '
                                       'owed, then run the all-in number. Add the purchase price and '
                                       'estimated attorney foreclosure cost, and confirm the total sits '
                                       'well under resale value for this parcel.',
                             'example': 'Parcel worth roughly $60,000 with $2,000 owed: a big cushion, '
                                        'which is safety as a lien buyer and profit as a deed buyer [Lien '
                                        'Ledger — ul1onF24UbM @ 00:06:33]. All-in: $2,000 lien plus about '
                                        '$2,500 attorney foreclosure cost equals $4,500, well under '
                                        'resale. A landlocked lot would turn this negative [Tax Sale '
                                        'Academy — FgLt0Zd5dxo @ 00:04:14].'},
                            {'name': 'exit_and_deadline_log',
                             'type': 'textarea',
                             'prompt': 'Before bidding, write the exit you would use if the certificate '
                                       'never redeems, and log every redemption and expiration date on the '
                                       'day you buy. Note the action deadline that, if missed, would cost '
                                       'you the right to collect.',
                             'example': 'Exit: if no redemption, foreclose and sell using big ugly signs '
                                        'and Craigslist [Gerald Harris — nMj50Itu21Q @ 00:10:08]. No bid '
                                        'without looking at the parcel and holding an exit [Ted Thomas — '
                                        'JcAwqIfK0vo @ 00:12:26]. Calendar: Florida certificate expires if '
                                        'no deed application is filed within seven years [Lien Ledger — '
                                        'H9fPhqUYPfc @ 00:05:50].'}],
                 'completion_gate': 'Do not register for any auction until all ten fields are complete, '
                                    'the all-in number sits well under resale value, every redemption and '
                                    'expiration date is logged, and an exit is written for each parcel you '
                                    'might bid on.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'State Rulebook and Real Yield Calculator',
                 'purpose': "Replace the idea of a national playbook with your state's actual rulebook, "
                            'then convert statutory ceilings into the yield the auction format will really '
                            'pay, stress-testing low bids, premiums, and paperwork deadlines before you '
                            'raise your hand.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ["Pull the county's published terms and bidding rules first, and fill the "
                                  'rulebook field from those documents rather than from memory or general '
                                  'state summaries.',
                                  'Write your walk-away rate in ink before the sale and do not edit it '
                                  'during the auction for any reason.',
                                  'For every yield calculation, show both a fast-redemption case and a '
                                  'no-redemption case held at least two years.',
                                  'Put every recording, notice, and foreclosure deadline on a calendar the '
                                  'same day you buy, since one day late has gotten entire foreclosures '
                                  'thrown out.',
                                  'Sort the county list by face amount and review past auction results '
                                  'before deciding which property types to chase.'],
                 'fields': [{'name': 'state_rulebook_essentials',
                             'type': 'textarea',
                             'prompt': 'List the four essentials for your target state: the interest rate, '
                                       'the bidding procedure, the redemption period, and the life of the '
                                       "lien. Mark any item you could not confirm from the county's own "
                                       'published terms.',
                             'example': 'Arizona: 16 percent maximum, interest bid down with no penalty '
                                        'floor. TaxLienLady names the four essentials as interest rate, '
                                        'bidding procedure, redemption period, and life of the lien '
                                        '[TaxLienLady — 7ybooMbrE58 @ 00:07:10]. Unconfirmed: whether this '
                                        'county runs proxy or direct bidding, which changes what a lone '
                                        'low bid wins [Realauction — cleRXY7vybQ @ 00:02:43].'},
                            {'name': 'minimum_rate_walkaway',
                             'type': 'text',
                             'prompt': 'Write your minimum acceptable rate on the list before the auction '
                                       'opens. Note the exact number at which you will stop bidding, and '
                                       'describe the ego-driven moment you expect to feel when someone '
                                       'bids one notch below you.',
                             'example': 'Minimum: 8.5 percent, written at the top of the list. The moment '
                                        "bidding hits 8.49 percent, I walk, following Bob Diamond's rule "
                                        "against ego-based auction fever [Bob Diamond - America's Tax Sale "
                                        'Attorney — B0WBR5swuac @ 00:05:05]. Expected trigger: watching a '
                                        'competitor win a clean single-family lien I had researched for a '
                                        'week.'},
                            {'name': 'neighborhood_redemption_variance',
                             'type': 'textarea',
                             'prompt': 'Record the overall redemption rate for your county and any '
                                       'area-level difference you can find. Explain how a lower-redeeming '
                                       'neighborhood changes the odds that you end up owning the parcel, '
                                       'and whether you want that outcome.',
                             'example': 'Cook County: 96 percent redeem overall, but about 70 percent on '
                                        "Chicago's south and west sides, where bidders are far more likely "
                                        "to end up owning [Bob Diamond - America's Tax Sale Attorney — "
                                        'B0WBR5swuac @ 00:03:17]. Decision: stay in high-redeeming areas '
                                        'for yield until an exit for owned parcels is proven.'},
                            {'name': 'subsequent_tax_plan',
                             'type': 'textarea',
                             'prompt': "Describe how you will handle the following year's unpaid taxes on "
                                       'a lien you already hold. Note the rate subsequent taxes earn in '
                                       'your state, who else can buy them, and how that offsets a low '
                                       'first-year rate.',
                             'example': "Illinois plan: hold the first lien and pay each following year's "
                                        'unpaid taxes at 12 percent with no competing bidders, which can '
                                        "make up for a near-zero first-year rate [Bob Diamond - America's "
                                        'Tax Sale Attorney — bFO7QIn_w3U @ 00:02:28]. Budget an extra year '
                                        'of taxes per certificate so the 12 percent layer is funded on '
                                        'time.'},
                            {'name': 'paperwork_deadlines',
                             'type': 'textarea',
                             'prompt': 'List every recording and notice deadline that decides whether your '
                                       'lien holds in this state. Give the number of days or months, the '
                                       'office that receives the filing, and who will prepare and serve it '
                                       'on your behalf.',
                             'example': 'New Jersey: record the tax certificate with the county clerk '
                                        'within 90 days to keep it valid [Tax Lien Bestie | Sabrina — '
                                        'G8iotxNSgRg @ 00:06:08]. Illinois: the 22-5 notice is due four '
                                        'months and 15 days from the sale, prepared and served by '
                                        "experienced tax sale counsel [Bob Diamond - America's Tax Sale "
                                        'Attorney — bFO7QIn_w3U @ 00:03:36].'},
                            {'name': 'lien_position_check',
                             'type': 'text',
                             'prompt': 'Confirm that the certificate you plan to buy is the '
                                       'first-position, first-year lien that carries the right to '
                                       'foreclose. Note whether this county restricts foreclosure to '
                                       'second- or third-year holders, and how you verified it with the '
                                       'county.',
                             'example': 'Verified first-position status, because that priority is what '
                                        'lets the holder foreclose [Dustin Hahn — rYcTmrny9JQ @ 00:04:41]. '
                                        'Confirmed this is the first-year lien, not a second or third, '
                                        'since a third-year buyer cannot foreclose [Dustin Hahn — '
                                        'tXVBp8vbkT4 @ 00:05:34]. Asked the county directly whether '
                                        'foreclosure is limited to later-year holders: it is not.'},
                            {'name': 'auction_format_identification',
                             'type': 'textarea',
                             'prompt': 'Identify the auction format your county uses: interest bid-down, '
                                       'premium or overbid, ownership-interest bid-down, or a hybrid that '
                                       'flips from rate to premium. Explain what you are actually '
                                       'competing on and what fixed rate, if any, survives.',
                             'example': 'New Jersey hybrid: liens go to whoever accepts the lowest rate, '
                                        'and once bidding passes 0 percent, to whoever pays the highest '
                                        'premium [Realauction — hKsLdKqVOE0 @ 00:01:12]. Large investors '
                                        'routinely bid it to 0 percent [Tax Lien School Highlights - '
                                        'Dustin Hahn — mHvzzGVcYdI @ 00:01:53]. I am competing on premium '
                                        'dollars, not rate.'},
                            {'name': 'sub_one_percent_stress_test',
                             'type': 'textarea',
                             'prompt': 'Price any bid below 1 percent against a no-redemption scenario. '
                                       'Show the yield if the owner redeems quickly and the yield if the '
                                       'lien sits unredeemed for two years, then decide whether the '
                                       'quick-redemption payoff justifies the risk.',
                             'example': 'Florida quarter-point fast-five: 0.25 percent wins, and the 5 '
                                        'percent penalty applies even on a next-day redemption [Tax Sale '
                                        'Resources — XbThUArmcIE @ 00:01:24]. Stress case: never redeemed '
                                        'and held two years, the return drops to about 2.5 percent a year '
                                        '[Tax Sale Resources — XbThUArmcIE @ 00:02:11]. Cap: no more than '
                                        'a small slice at quarter-point.'},
                            {'name': 'premium_overbid_math',
                             'type': 'textarea',
                             'prompt': 'If your state auctions a premium above face value, confirm whether '
                                       'the overbid is returned and whether it earns interest. Estimate '
                                       'how many months of interest must accrue to cover the premium, '
                                       "using the county's own redemption timing statistics.",
                             'example': 'Called the county for stats on how long most liens take to '
                                        'redeem, as a starting number [Tax Sale Academy — cnd7EM15dyk @ '
                                        '00:00:40]. Overpaying the face value without enough months of '
                                        'interest to cover the overbid loses money [Tax Sale Academy — '
                                        '0I_mhnrF0So @ 00:02:27]. Colorado alternative: fixed payoff '
                                        'around 13 percent under premium bidding [Tax Sale Secrets — '
                                        'stFlmSmpP3Q @ 00:01:09].'},
                            {'name': 'where_the_crowd_is_not',
                             'type': 'textarea',
                             'prompt': "Review the county's past auction results and its full lien list "
                                       'sorted by face amount. Identify the property types bid to near '
                                       'zero, the types clearing at double-digit rates, and any liens too '
                                       'large for most bidders to fund.',
                             'example': 'Pattern checked: downtown condo liens bid near zero while '
                                        'single-family liens cleared double digits [Smart Capital — '
                                        'TL6AIsoe5m0 @ 00:14:44]. The Montezuma list opens with $25 liens, '
                                        'and the $900 to $128,000 liens start about 11 pages in [Tax Sale '
                                        'Secrets — stFlmSmpP3Q @ 00:04:24], including a $128,000 lien on a '
                                        'Best Western valued at 5.7 million [Tax Sale Secrets — '
                                        'stFlmSmpP3Q @ 00:10:01].'}],
                 'completion_gate': 'Bidding is cleared only when the walk-away rate is written, the '
                                    'auction format and proxy-or-direct rule are confirmed, the '
                                    'no-redemption yield is acceptable, the lien is verified as first '
                                    'position, and every paperwork deadline is calendared with an assigned '
                                    'preparer.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Online Sale and Over-the-Counter Verification Checklist',
                 'purpose': "Walk a single parcel from the online sale list or the county's leftover list "
                            'to a funded purchase, verifying identity by parcel ID, condition by current '
                            'image, usability by access and utilities, and price against a written maximum '
                            'and a proven exit.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Work one parcel per copy of this checklist and attach the parcel ID to '
                                  'every page.',
                                  'Verify on the property appraiser site and county records; never rely on '
                                  'a vendor listing photo, an undated image, or a street address alone.',
                                  'Fund deposits early enough that they are received on time, and confirm '
                                  "the platform's payment rules before registration closes.",
                                  'On over-the-counter lists, assume most parcels are rejects and record '
                                  'your reason for every rejection.',
                                  'Stop after your first-buy cap and sell what you own before adding more '
                                  'parcels.'],
                 'fields': [{'name': 'platform_registration',
                             'type': 'text',
                             'prompt': 'Name the online platform your county uses and record its '
                                       'registration deadline, deposit size, deposit method, and final '
                                       'payment method. Note how many working days each payment method '
                                       'needs so no deposit arrives late on sale day.',
                             'example': 'Florida county on RealAuction: free registration, roughly 10 '
                                        'percent deposit. Deposit goes in at the county counter by 4 pm '
                                        'the day prior; ACH is used only for the final payment, because '
                                        'ACH needs four working days [Loren Brown - The 5am Reinvention '
                                        'Project — gamhQuWz38o @ 00:06:56]. Deposits must be received on '
                                        'time, not just sent [Ted Thomas — sXKw09ndbYg @ 00:14:54].'},
                            {'name': 'parcel_id_verification',
                             'type': 'textarea',
                             'prompt': 'Take the parcel ID from the sale list and click through to the '
                                       'property appraiser site. Record the usage and description shown '
                                       'there, and note any mismatch between the parcel ID, the street '
                                       "address, and the vendor's listing.",
                             'example': 'Appraiser site lists usage as vacant residential, matching the '
                                        "description, so the vendor's listing photo and assessed value "
                                        'were ignored [The Jackie Jackson | Tax Deed & Real Estate Coach — '
                                        'Pz2ZCMuIox4 @ 00:12:04]. Matched by parcel ID, never by street '
                                        'address [Dustin Hahn — YVYW5E5cTUI @ 00:03:22]. No mismatch '
                                        'found, so the parcel moves to imagery checks.'},
                            {'name': 'current_image_check',
                             'type': 'textarea',
                             'prompt': 'Document the most current image you have of the parcel, its date, '
                                       'and its source. If county or Street View images are stale, record '
                                       'who you will send for fresh photos, what it will cost, and when '
                                       'they will report back.',
                             'example': 'Street View image is years old, and county shots run stale, so no '
                                        'bid without a current photo [Tax Sale Secrets — IMGzMnzQiZQ @ '
                                        '01:29:27]. First pass on Google Earth, then a wegowlook.com visit '
                                        'for $20 to $50 in pictures, or a Craigslist gig driver for about '
                                        '$50 [Dustin Hahn — uiH28IFKgC4 @ 00:06:06]. Report due Thursday.'},
                            {'name': 'access_and_utilities_screen',
                             'type': 'textarea',
                             'prompt': 'Screen the parcel for access, size, and utilities before paying '
                                       'anything. Note whether it is landlocked, where the nearest power '
                                       'and sewer connections are, and what it would cost to bring them to '
                                       'the lot, and whether that cost erases the deal.',
                             'example': 'Not landlocked; landlocked lots are among the first eliminated '
                                        'because of the use factor, even when cheap [Tax Sale Secrets — '
                                        'RgLErVu5_Kk @ 00:29:54]. Power poles sit at the lot line. Saen '
                                        'Higgins once found power at the end of the street, costing '
                                        '$20,000 to bring to a $1,500 lot [Saen Higgins — nbHUraglUQo @ '
                                        '00:07:11]. Sewer confirmed with the county.'},
                            {'name': 'max_bid_and_exit',
                             'type': 'textarea',
                             'prompt': 'Fix your exit and your maximum bid before the auction opens. State '
                                       'whether you will quiet title or wholesale as-is, show the '
                                       'comparable sales behind your ceiling, and write the number you '
                                       'will not exceed online.',
                             'example': 'Exit: as-is wholesale. CMA built from the cheapest comps; ceiling '
                                        'written at $4,000 before registration [Tax Sale Secrets — '
                                        'RgLErVu5_Kk @ 00:48:38]. Once the bottom line is set and research '
                                        'done, there is no getting emotionally involved [Tax Sale Secrets '
                                        '— AO4ZqaMio7s @ 00:27:24]. Expect losses: one Florida run lost '
                                        'seven or eight properties before winning one [Tax Sale Secrets — '
                                        'IMGzMnzQiZQ @ 01:30:17].'},
                            {'name': 'diligence_timing',
                             'type': 'text',
                             'prompt': 'Set the calendar window for your heavy due diligence relative to '
                                       'the auction date. Note how many days before the sale you will '
                                       'finish research, and why that timing keeps the parcel likely to '
                                       'still be available.',
                             'example': 'Heavy diligence runs one to two weeks before the auction, so the '
                                        'parcel is still likely to be available on sale day [Tax Sale '
                                        'Secrets — AO4ZqaMio7s @ 01:41:13]. Also watching for sales whose '
                                        'registration closes months in advance, which is very rare and '
                                        'thins the bidder pool [Tax Lien School Highlights - Dustin Hahn — '
                                        'M8AxkDXoffk @ 00:03:08].'},
                            {'name': 'find_leftover_list',
                             'type': 'textarea',
                             'prompt': 'Ask the county what happens to properties that did not sell, and '
                                       'record the name the county uses for its leftover list. Note when '
                                       'the list posts, how it is delivered, and whether a paid or hidden '
                                       'version exists.',
                             'example': 'County calls it the strike off list; other states use scavenger, '
                                        'lands available, forfeited lands, or repository. It posts about '
                                        '30 days after the sale [Saen Higgins — G44d74hIS_0 @ 00:09:40]. A '
                                        'paid version costs 15 cents a page, roughly $30 total, the list '
                                        'nobody else bothers to buy [Dustin Hahn — YVYW5E5cTUI @ '
                                        '00:16:14].'},
                            {'name': 'otc_screening_yield',
                             'type': 'textarea',
                             'prompt': 'Screen the full leftover list and record how many parcels you '
                                       'reviewed, how many looked decent, and how many looked great. '
                                       'Compare your hit rate to the practitioner benchmark and note the '
                                       'most common reason you rejected parcels.',
                             'example': 'Reviewed 1,000 parcels: 96 decent, 4 great, close to the 100 '
                                        'decent and 5 great benchmark [Tax Sale Support — 5t3VbtPlElc @ '
                                        '00:39:46]. Most common rejection: minimum bid that made no sense '
                                        'against value [Dustin Hahn — YVYW5E5cTUI @ 00:03:22]. Dustin Hahn '
                                        'concedes most of it will be crap [Dustin Hahn — uiH28IFKgC4 @ '
                                        '00:03:46], so the screen did its job.'},
                            {'name': 'otc_price_and_clock',
                             'type': 'textarea',
                             'prompt': 'Record the over-the-counter price as a share of value and the '
                                       'redemption clock that applies. Note whether the clock runs from '
                                       'the original auction date or your purchase date, and when the '
                                       'earliest foreclosure or deed action becomes possible.',
                             'example': 'Maryland OTC lien paying 20 percent. The six-month redemption '
                                        'counts from the auction date, not the purchase date, so this one '
                                        'is foreclosable the day I buy [Tax Lien School Highlights - '
                                        'Dustin Hahn — Ayjol9fgpNg @ 00:02:15]. For OTC land, target 10 '
                                        'percent of value or less; students buy at 5 to 15 percent [Tax '
                                        'Sale Secrets — RgLErVu5_Kk @ 00:23:45].'},
                            {'name': 'first_buy_cap_and_encumbrances',
                             'type': 'textarea',
                             'prompt': 'Set a hard cap on your first over-the-counter purchases and list '
                                       'the encumbrance checks each parcel must pass. Include IRS liens, '
                                       'buried tanks, municipal liens, and chain-of-title notice failures, '
                                       'and state when you will sell before buying more.',
                             'example': 'Cap: one or two liens and one deed, sold before buying more, '
                                        'after a student stacked 40 unsold properties [Ted Thomas — '
                                        'XLUuBoGUOj8 @ 00:09:47]. Each parcel screened for IRS liens, '
                                        'buried gas tanks, and chain-of-title notification failures before '
                                        'money moves [Dustin Hahn — uiH28IFKgC4 @ 00:04:31]. Title search '
                                        'covers hidden and municipal liens too [Ted Thomas — 41UuQtBLiBo @ '
                                        '00:03:04].'}],
                 'completion_gate': 'No money moves on this parcel until the parcel ID matches the '
                                    'appraiser record, a current image is in hand, access and utilities '
                                    'are confirmed, encumbrance checks are clear, the redemption clock is '
                                    'known, and the maximum bid and exit are written down.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Pre-Bid Research Ledger and Foreclosure-to-Clean-Title Plan',
                 'purpose': 'Turn every parcel on the county list into a verified, valued, and '
                            'title-mapped file before a single dollar moves. Then carry the non-redeeming '
                            'lien through foreclosure, notice, and title cure, with costs and timelines '
                            'budgeted before the bid.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Work one parcel per copy of this worksheet and identify it by parcel or '
                                  'account number, never by street address, so every later step points at '
                                  'the same asset.',
                                  'Treat research as elimination scaled to cost: a small lien earns a '
                                  'lighter pass, while a deed or a lien likely to end in ownership earns '
                                  'the full ledger.',
                                  'Date every image, record, and phone call you rely on, because stale '
                                  'photos and undated county pictures are the most common reason a parcel '
                                  'is misjudged.',
                                  'Fix your maximum bid only after the valuation, land screen, and lien '
                                  'search are complete, and write it down before the sale opens so it '
                                  'cannot drift upward.',
                                  'Complete the foreclosure and title-cure fields before you buy, not '
                                  'after the redemption window closes, so counsel, notice, cost, and carry '
                                  'time are already planned.'],
                 'fields': [{'name': 'parcel_id_gis_verification',
                             'type': 'text',
                             'prompt': 'Record the parcel number exactly as printed on the county list, '
                                       'then confirm its location inside the county GIS or parcel viewer. '
                                       'Note whether this county even runs a GIS, and log any mismatch '
                                       'between the parcel number and the situs address.',
                             'example': 'Parcel 14-22-0318 located by account number in the county parcel '
                                        'viewer, not by the Google pin, following the rule to verify '
                                        'location by parcel number [Jason Porter — bnQAJL9-zo0 @ '
                                        '00:00:17]. The county does run a GIS, which only about half of '
                                        'counties do [Tax Sale Academy — 2B3hCb362oA @ 00:04:44]. No '
                                        'address listed, so the account number was copied directly.'},
                            {'name': 'structure_imagery_check',
                             'type': 'textarea',
                             'prompt': 'Describe how you confirmed the structure still stands using dated '
                                       'Street View and historical aerial imagery. Record the capture date '
                                       'of every image, flag anything older than a few years, and note '
                                       'signs of long vacancy, fire, or demolition.',
                             'example': 'Street View on the target home is six years old, and Ted Thomas '
                                        'warns that photos five to ten years old are unreliable [Ted '
                                        'Thomas — a81g1szr71Y @ 00:02:30]. Historical aerials show the '
                                        'roof intact but an overgrown lot. Because a property vacant for '
                                        '10 to 20 years means serious issues [Tax Sale Academy — '
                                        'yUKmyPRuIsY @ 00:01:24], a drive-by is scheduled before bidding.'},
                            {'name': 'land_usability_screen',
                             'type': 'textarea',
                             'prompt': 'Screen the land itself before valuing any structure. Record lot '
                                       'size in acres, flood exposure, buildability, road access, and HOA '
                                       'status, and state plainly whether the parcel clears the '
                                       'minimum-size rule or should be eliminated before more research '
                                       'time is spent.',
                             'example': 'Lot measures 0.08 acre, below the rule to skip anything under 0.1 '
                                        'acre and to call the HOA before bidding [Tax Sale Secrets — '
                                        'GxMaS0YFT1Y @ 00:46:21]. A second candidate is landlocked, and '
                                        'landlocked parcels are among the first eliminated even when cheap '
                                        'because of the use factor [Tax Sale Secrets — RgLErVu5_Kk @ '
                                        '00:29:54]. Both parcels are struck from the list.'},
                            {'name': 'opening_bid_screen',
                             'type': 'text',
                             'prompt': 'Enter the opening bid, the assessed value, and the ratio between '
                                       'them as a percentage. State whether the parcel passes a first-pass '
                                       'screen before you spend time pulling comps, maps, and owner '
                                       'records on it.',
                             'example': 'Opening bid $6,200 against an assessed value of $48,000, about 13 '
                                        'percent, inside the quick-glance screen of 10 to 15 percent of '
                                        'assessed value, up to 20 percent [onlinetaxsales — OU-LqZt4nCs @ '
                                        '00:47:15]. Passes to full research. Address split on paste into '
                                        'Zillow, so it was re-entered by hand [onlinetaxsales — '
                                        'OU-LqZt4nCs @ 00:48:08].'},
                            {'name': 'cma_valuation',
                             'type': 'textarea',
                             'prompt': 'Build a comparative market analysis from the cheapest credible '
                                       'comps. Record square footage, comp prices, the resulting price per '
                                       'square foot, and your valuation range, keeping the estimate within '
                                       'plus or minus ten percent of what the property would realistically '
                                       'sell for.',
                             'example': 'Subject is 1,800 square feet. The cheapest comps sold at $105,000 '
                                        'to $110,000, which works out to $55 to $62 per square foot, '
                                        "matching the worked example and its warning, 'Don't cheat "
                                        "yourself' [Tax Sale Secrets — GxMaS0YFT1Y @ 00:34:52]. Valuation "
                                        'range set at $99,000 to $111,600, with the low end used for the '
                                        'maximum bid.'},
                            {'name': 'government_lien_owner_search',
                             'type': 'textarea',
                             'prompt': 'List every court and county record search run on the current '
                                       "owner's name, including government liens, municipal liens, and "
                                       'code violations. Note which liens would survive a sale and record '
                                       'the final re-confirmation that the parcel remains on the county '
                                       'list.',
                             'example': 'Owner name run through court records the week of the sale, the '
                                        'parcel re-confirmed on the county list, and the maximum bid fixed '
                                        '[Tax Sale Secrets — GxMaS0YFT1Y @ 00:05:41]. One open '
                                        'code-violation file found; municipal liens and code violations '
                                        'survive to the new buyer [The Residential Buyer — 2S4mkxCrOhM @ '
                                        '00:03:06]. Counties never refund, so the file is flagged.'},
                            {'name': 'lien_priority_foreclosure_right',
                             'type': 'text',
                             'prompt': 'Confirm the certificate is the first-year lien that carries the '
                                       'right to foreclose, not a second- or third-year lien. Record the '
                                       'redemption expiration date and the earliest date you can file, and '
                                       'note whether it came from county inventory.',
                             'example': 'Certificate verified as the first-year lien; Dustin Hahn warns '
                                        'that a third-year buyer cannot foreclose [Dustin Hahn — '
                                        'tXVBp8vbkT4 @ 00:05:34]. Bought from county inventory already '
                                        'past redemption, so foreclosure can start immediately, which Saen '
                                        'Higgins likens to taking 20 shots on goal now instead of waiting '
                                        'two years [Saen Higgins — EXkUbWWenl0 @ 00:08:53]. Filing opens '
                                        'this month.'},
                            {'name': 'defendant_net_chain_of_title',
                             'type': 'textarea',
                             'prompt': 'Build the full chain of title and list every undischarged interest '
                                       'holder who must be named and served, including mortgage lenders, '
                                       'junior lienholders, heirs, and trustees. Record the service method '
                                       'and date for each party so no claimant is missed.',
                             'example': 'Chain of title shows the record owner, a first mortgage, a '
                                        'home-equity lender, and one judgment creditor, each named and '
                                        'served by certified mail. One missed claimant forces the whole '
                                        'suit to restart just to remove that interest [Quiet Title '
                                        'Michigan — kJRxvYeK_eU @ 00:03:19]. Once foreclosed, the '
                                        "lienholder holds the county's strength to extinguish encumbrances "
                                        '[Saen Higgins — EXkUbWWenl0 @ 00:06:28].'},
                            {'name': 'title_cure_path_and_budget',
                             'type': 'textarea',
                             'prompt': 'Choose between a suit to quiet title and a tax foreclosure '
                                       'certification, and explain why. Record the quoted fee, expected '
                                       'timeline, counsel name, and whether an entity owner rules out '
                                       'filing pro se before any rehab or resale is scheduled.',
                             'example': 'Certification quoted at $1,950 to $3,000 with a three-to-six-week '
                                        'turn [Tax Sale Academy — 7BP12s9Jn2c @ 00:15:10], versus a suit '
                                        'to quiet title planned at $3,000 to $5,000 over three to six '
                                        'months [Ted Thomas — MzL0xEaYnUI @ 00:01:31]. The parcel sits in '
                                        'an LLC, so pro se filing is off the table [Tax Sale Academy — '
                                        'vMMozg0xaSA @ 00:02:46].'},
                            {'name': 'carry_cost_stress_test',
                             'type': 'textarea',
                             'prompt': 'Stress-test the hold from foreclosure judgment to clean title. '
                                       'List monthly taxes, heat, snow removal, security, insurance, and '
                                       'attorney fees across a long hold, then confirm the resale margin '
                                       "survives a timeline far longer than the attorney's first estimate.",
                             'example': 'Underwriting assumes a 13-month hold, mirroring the quiet title '
                                        'that took 13 months of diligent work before the judge would issue '
                                        'it [Ted Thomas — O8MWhOJE6Oc @ 00:07:42]. Taxes, heat, snow '
                                        'removal, and security are carried every month because buyers '
                                        'cannot get a mortgage until title clears [Ted Thomas — '
                                        'O8MWhOJE6Oc @ 00:08:01]. Margin still clears after the full '
                                        'hold.'}],
                 'completion_gate': 'Do not bid until the parcel is matched by number in the GIS, the '
                                    'structure is confirmed on dated imagery, the land passes the size and '
                                    'access screen, a CMA-based maximum is written down, and the '
                                    'first-year lien status, defendant list, title-cure path, and 13-month '
                                    'carry budget are all recorded.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Title Trap Audit and Federal Lien Redemption Defense',
                 'purpose': 'Expose the hidden liabilities that turn a cheap parcel into a loss, from '
                            'burned structures and unrecorded municipal fines to supplemental taxes and '
                            'HOA claims, then protect any foreclosure purchase against the federal right '
                            'of redemption that can follow a property past the auction.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Get physical eyes on the property through your own visit or a hired '
                                  'local, because satellite imagery misses fires, floods, and demolitions '
                                  'that change the entire deal.',
                                  'Pull a title report before bidding and follow it with a human search of '
                                  'municipal and utility departments, since a large share of title '
                                  'problems never reach the record.',
                                  'Write down the strongest argument against the purchase and name the one '
                                  'condition that must hold for you to proceed; if that condition fails, '
                                  'drop the parcel.',
                                  'When a federal tax lien appears, verify pre-sale notice to the IRS, '
                                  'mark the sale date as day zero, and freeze every cosmetic dollar until '
                                  'the window closes.',
                                  'Keep every preservation receipt organized from day one, and calendar '
                                  'each IRS letter deadline and county release confirmation the moment the '
                                  'related document arrives.'],
                 'fields': [{'name': 'physical_inspection_record',
                             'type': 'textarea',
                             'prompt': 'Record who physically viewed the property, when, and what they '
                                       'saw. Note any fire damage, flood damage, demolition, environmental '
                                       'hazards such as underground tanks, or conditions that satellite '
                                       'imagery could have missed, and attach the dated photographs.',
                             'example': 'A local driver photographed the house on Tuesday and found the '
                                        'rear half burned out, damage Google Earth never showed; a '
                                        'burned-down house has sold four times at auction [Dustin Hahn — '
                                        'vA4ImBMyenY @ 00:06:09]. The neighboring lot is a former gas '
                                        'station, and environmental sites are avoided outright [Dustin '
                                        'Hahn — vA4ImBMyenY @ 00:02:08]. Both parcels dropped.'},
                            {'name': 'title_report_pull',
                             'type': 'text',
                             'prompt': 'Record the title report order date, cost per report, and every IRS '
                                       'or government lien it revealed. Size each lien against the '
                                       'property value and state whether the parcel stays on the bid list '
                                       'or is removed.',
                             'example': 'Title reports pulled at $20 to $30 each, roughly $2,000 to $3,000 '
                                        'across 100 deeds, with IRS and government liens flagged and sized '
                                        'against value [Dustin Hahn — vA4ImBMyenY @ 00:07:24]. This parcel '
                                        'shows a federal tax lien near half its value, so it moves to the '
                                        'IRS redemption fields below before any bid is allowed.'},
                            {'name': 'unrecorded_municipal_lien_search',
                             'type': 'textarea',
                             'prompt': 'Document the human search for unrecorded municipal, utility, and '
                                       'code-enforcement liens that a recorded title report would miss. '
                                       'List each department contacted, the daily fine rate on open '
                                       'violations, and the running balance projected through your '
                                       'expected closing date.',
                             'example': 'Building and water departments called directly, since a quarter '
                                        'of title issues trace to unrecorded municipal liens and Arizona '
                                        'code fines can run $100 per day [Alex Goldovsky — O6HhpnnQADM @ '
                                        '00:16:00]. One open permit violation found, accruing daily. '
                                        'Silence is what turns a small problem into a large one [HOA '
                                        'Insights — YD_WDRyFt4Q @ 00:05:53], so the fine is priced in.'},
                            {'name': 'hoa_and_supplemental_tax_check',
                             'type': 'textarea',
                             'prompt': 'List any HOA dues, HOA liens, supplemental tax bills, and '
                                       'subsequent-year taxes attached to the parcel. Record who is '
                                       'responsible for each, the payment deadline, and how paying '
                                       'subsequent taxes changes the capital required to keep the '
                                       'position.',
                             'example': 'A supplemental tax bill arrived after the sale and is logged as '
                                        "the buyer's burden: 'If you don't pay the supplemental, that's "
                                        "your fault' [Premier Wealth Builders — AYiTxfuCWHk @ 00:01:36]. "
                                        "Next year's taxes are reserved too, since new liens take over old "
                                        'liens and subsequent liens require more capital [Rent To '
                                        'Retirement — iOoZ743spRo @ 00:02:02]. HOA statement requested.'},
                            {'name': 'four_essentials_and_odds',
                             'type': 'textarea',
                             'prompt': 'Write down the four essentials for this county: interest rate, '
                                       'bidding procedure, redemption period, and life of the lien. Then '
                                       'estimate how many liens you would need to buy to land one '
                                       'property, given realistic redemption rates.',
                             'example': 'Interest rate, bidding procedure, redemption period, and life of '
                                        'the lien recorded for the county, the four essentials named by '
                                        'TaxLienLady [TaxLienLady — 7ybooMbrE58 @ 00:07:10]. With about 95 '
                                        'percent of liens redeeming and the bank the biggest redeemer '
                                        '[Dustin Hahn — iCR-rdsQrUg @ 00:02:31], $50,000 spread across 100 '
                                        'liens is modeled to produce about 5 properties.'},
                            {'name': 'skeptic_counterweight',
                             'type': 'textarea',
                             'prompt': 'Write the strongest case against this purchase. Record the '
                                       'skeptical view you take most seriously, the specific failure it '
                                       'predicts for this parcel, and the single condition that would have '
                                       'to be true for you to proceed anyway.',
                             'example': 'Counterweight: a host who has owned about 2,000 properties bought '
                                        "two of these and called it 'a freaking nightmare, never again' "
                                        '[The Ramsey Show Highlights — KytTy1-RC5I @ 00:05:35]. Predicted '
                                        'failure here is a contested title costing far more than budget. '
                                        'Proceed only if quiet title stays uncontested, near a grand or '
                                        'two rather than $100K+ disputed [Jose Luiz Morales — B0yvMIdmaaQ '
                                        '@ 00:23:16].'},
                            {'name': 'irs_presale_notice_check',
                             'type': 'text',
                             'prompt': 'Confirm the foreclosing party sent written notice to the IRS at '
                                       'least 25 days before the sale, and that the case went to an actual '
                                       'sale rather than a deed in lieu. Record the notice date and its '
                                       'proof.',
                             'example': 'Notice to the IRS confirmed 31 days before the sale, clearing the '
                                        '25-day pre-sale requirement [Global Estate Hub LLC — q4Kqh7Vleyg '
                                        '@ 00:06:35]. The case went to an actual sale, not a deed in lieu '
                                        '[LCO Law LLC | Estate Planning & Real Estate Law — GoBskUnMJ5k @ '
                                        '00:01:19]. The federal lien is discharged, and the redemption '
                                        'clock starts on sale day.'},
                            {'name': 'redemption_window_calendar',
                             'type': 'text',
                             'prompt': 'Enter the sale date as day zero, the 120-day IRS redemption '
                                       'deadline, and any longer state-law period that applies. List the '
                                       'cosmetic spending you will freeze until that window fully closes '
                                       'or a redemption waiver issues.',
                             'example': 'Sale date logged as day zero; the IRS has exactly 120 days to '
                                        'decide whether to redeem [Global Estate Hub LLC — q4Kqh7Vleyg @ '
                                        '00:03:17]. Cabinets, granite, and hardwood floors are frozen, '
                                        'because a redemption wipes out every cent spent on upgrades '
                                        '[Global Estate Hub LLC — q4Kqh7Vleyg @ 00:05:23]. Thin equity '
                                        'here, so a redemption waiver request is filed.'},
                            {'name': 'preservation_receipts_ledger',
                             'type': 'textarea',
                             'prompt': 'Log every preservation expense that would be reimbursed if the IRS '
                                       'redeems, such as insurance, locks, superior-position property '
                                       'taxes, and roof repairs. Record the date, amount, and receipt '
                                       'location so the full claim can ship within fifteen days.',
                             'example': 'Paid delinquent prior-year property taxes and a roof patch, both '
                                        'preserving the asset and outranking the IRS [LCO Law LLC | Estate '
                                        'Planning & Real Estate Law — GoBskUnMJ5k @ 00:02:37]. '
                                        'Reimbursement on redemption would be the bid plus 6 percent '
                                        'annual interest plus qualifying expenses [LCO Law LLC | Estate '
                                        'Planning & Real Estate Law — GoBskUnMJ5k @ 00:01:38].'},
                            {'name': 'irs_letter_and_release_followup',
                             'type': 'textarea',
                             'prompt': 'Record the date any IRS redemption letter or Letter 3172 arrives, '
                                       'the response deadline you calculated, the mailing date and proof '
                                       'of mailing, and confirmation that any Certificate of Release '
                                       'actually posted with the county recorder.',
                             'example': 'IRS redemption letter logged on arrival, and the 15-day deadline '
                                        'for receipts and senior-lien release proof calendared immediately '
                                        '[LCO Law LLC | Estate Planning & Real Estate Law — GoBskUnMJ5k @ '
                                        '00:03:16]. After a payoff on a prior file, the recorder was '
                                        'checked directly, because nobody calls to say the release posted '
                                        '[Clarity Tax Relief — oPKD4zP1XUQ @ 00:07:18].'}],
                 'completion_gate': 'Do not bid or begin any rehab until the property has been physically '
                                    'viewed, the title report and municipal search are sized against '
                                    'value, supplemental and HOA charges are reserved, the skeptic '
                                    'condition is met, and any federal lien has a verified IRS notice, a '
                                    'day-zero calendar, and a receipts ledger.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Legal Exposure Check and Funding-to-Scale Blueprint',
                 'purpose': 'Shield each certificate from surplus-equity claims, defective notice, '
                            'uncertain deed issuance, and bankruptcy stays, then design the capital stack, '
                            'retirement-account plumbing, entity wrappers, and exit channels that let a '
                            'lien book grow without one missed deadline erasing a year of returns.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Measure the equity above the taxes owed on every parcel, because '
                                  'surplus rulings now shape how certificates are challenged, compensated, '
                                  'and reviewed by the court.',
                                  "Get the county's deed-issuance practice in writing and document every "
                                  'notice step to every interest holder, since a verbal answer or a missed '
                                  'trustee can unwind the deal.',
                                  'Check for an owner bankruptcy filing right up to the minute of sale, '
                                  'and keep redemption proof ticklers running long after each payoff '
                                  'closes.',
                                  'Size your bankroll honestly against institutional competition, then '
                                  'route retirement money, entities, and borrowed funds through structures '
                                  'set up well before sale season.',
                                  'Prove your exit channel before you buy in high-foreclosure states, lock '
                                  'the maximum bid to that exit, and hand every foreclosure to a tax '
                                  'attorney.'],
                 'fields': [{'name': 'surplus_equity_exposure',
                             'type': 'textarea',
                             'prompt': 'Estimate the equity sitting above the taxes owed on this parcel '
                                       'and describe how a post-Tyler surplus claim could affect your '
                                       'position. Record the assessed value, amount owed, and expected '
                                       'sale price, and note whether the court form asks about equity.',
                             'example': 'Benchmark: in Tyler, a $40,000 sale on roughly $15,000 owed left '
                                        'Hennepin keeping about $25,000 [The Deed | Real Estate — '
                                        'sb6T0Xe5siY @ 00:01:27]. This parcel shows heavy equity over a '
                                        'small tax debt, and the court application form now asks whether '
                                        'there is equity in the property [The Devine Law Group — '
                                        'qAoyeFTuxms @ 00:15:05], so counsel reviews before purchase.'},
                            {'name': 'deed_issuance_confirmation',
                             'type': 'text',
                             'prompt': 'Confirm in writing how this county actually handles deed issuance '
                                       'after the redemption period expires. Record the official '
                                       'contacted, the written answer received, and your fallback remedy '
                                       'if the county refuses or stalls on issuing the deed.',
                             'example': 'Nebraska county treasurer emailed a written answer, because a '
                                        'verbal answer from a clerk is not proof [The Deed | Real Estate — '
                                        'sb6T0Xe5siY @ 00:06:20]. Counties there are split between issuing '
                                        'deeds, requiring foreclosure, and staying undecided, so the '
                                        'fallback is a mandamus action or judicial foreclosure followed by '
                                        'suing the county [Tax Sale Resources — d67aVfAEUxg @ 00:25:05].'},
                            {'name': 'notice_audit',
                             'type': 'textarea',
                             'prompt': 'Audit notice to every interest holder, including trustees, heirs, '
                                       'and lenders. For each, record the certified mail result, any '
                                       'returned envelopes, and the additional reasonable steps taken '
                                       'afterward, so a defective-notice appeal cannot unwind your deed '
                                       'later.',
                             'example': 'Certified mail to the trustee came back unclaimed, so a posted '
                                        'notice and a second address were documented as additional '
                                        'reasonable steps [Florida Trust, Real Estate, Probate, & '
                                        'Foreclosure — RlQwxNYiqok @ 00:15:33]. Every notice is dated with '
                                        'proof of delivery, since one or two misses can derail a full '
                                        "year's returns [Kevin Bupp - Cash Flow Investor — UyiZp8ocowM @ "
                                        '00:39:08].'},
                            {'name': 'bankruptcy_stay_check',
                             'type': 'text',
                             'prompt': 'Record the time you last checked for a bankruptcy filing by the '
                                       'owner before the sale, the case number if one exists, and the '
                                       'steps you will take to halt collection activity if a filing '
                                       'appears.',
                             'example': 'Bankruptcy search rerun at 9:55 a.m. for a 10:00 a.m. auction, '
                                        'because a 9:48 a.m. filing halts the sale and voids it [Behind '
                                        'The Servicing — au90-c2Pwvo @ 00:00:17]. Bankruptcy freezes the '
                                        'sale but never erases property taxes. If a filing appears, the '
                                        'case number is kept on hand for every caller [Bankruptcy '
                                        'Explained — m1B_j8n-b9E @ 00:02:11].'},
                            {'name': 'redemption_proof_tickler',
                             'type': 'text',
                             'prompt': 'Set tickler dates two and three weeks after every redemption '
                                       'closing. Record the certificate number, the redemption date, the '
                                       'date actual proof of payment arrived, and who confirmed it, so no '
                                       'payoff rests on an assumption.',
                             'example': 'Illinois certificate redeemed on the 3rd; ticklers set for the '
                                        "17th and 24th, because 'Bob thought Stan sent the check' is how "
                                        'certificates go sideways [The Devine Law Group — qAoyeFTuxms @ '
                                        '00:16:45]. Actual proof of redemption received in writing on the '
                                        '18th. A slow payout only drags a few months, already expected '
                                        'with liens [Tax Sale Secrets — qEuYpfZ_Qgg @ 00:01:42].'},
                            {'name': 'starting_bankroll_and_capital_plan',
                             'type': 'textarea',
                             'prompt': 'State your total starting bankroll, how much stays in reserve for '
                                       'attorney and title-clearing costs, and the yield you realistically '
                                       'expect at that size given institutional competition. Note whether '
                                       'your capital is large enough to chase bank-level returns.',
                             'example': "Bankroll is $25,000, meeting Ted Thomas's floor of $20,000 to "
                                        '$25,000, since $500 is not enough [REtipster — jDYlxXpw-e4 @ '
                                        '00:36:45]. Reserve set at $5,000 for the clear-title attorney '
                                        '[REtipster — jDYlxXpw-e4 @ 00:41:33]. Bank-level 15 to 18 percent '
                                        'yields take six to seven figures [Kevin Bupp - Cash Flow Investor '
                                        '— UyiZp8ocowM @ 00:14:17], so expectations stay modest.'},
                            {'name': 'self_directed_ira_setup',
                             'type': 'textarea',
                             'prompt': 'Describe how retirement money will flow into liens. Record the '
                                       'custodian, fee schedule, the exact name the IRA bids under, its '
                                       'TIN, any entity bank account required by bidding sites, and the '
                                       'transfer start date relative to sale season.',
                             'example': 'Custodian charges $325 per asset per year [Next Generation — '
                                        "l9-Us7KWWPM @ 00:16:30]. Bids go in the IRA's exact name with its "
                                        'own TIN and an entity bank account, since bidding sites now '
                                        'require one [CamaPlan Self Directed IRA — U08uLxrDVE4 @ '
                                        '00:36:29]. Transfer starts in August, well before the October '
                                        'Illinois sales.'},
                            {'name': 'entity_structure',
                             'type': 'text',
                             'prompt': 'Decide whether liens and deeds will be held individually, jointly, '
                                       'or through LLCs before you bid. Record the entity names, which '
                                       'assets each entity holds, and whether any title insurance '
                                       'endorsement is needed before transferring property into an entity.',
                             'example': "Following Clint Coons's pattern, one Wyoming LLC holds all liens "
                                        'and each deed gets its own LLC. Entity chosen before bidding, '
                                        'since re-deeding afterward can trigger tax uncapping or gift '
                                        'conveyance issues [Quiet Title Michigan — 7yD_brKdgXk @ '
                                        '00:13:04]. A title insurance endorsement is ordered before any '
                                        'transfer, after one entity transfer voided coverage [Jose Luiz '
                                        'Morales — B0yvMIdmaaQ @ 00:29:12].'},
                            {'name': 'opm_and_ladder_plan',
                             'type': 'textarea',
                             'prompt': "Describe any other people's money you will use, the rate you will "
                                       'pay lenders, and the rate the lien or redeemable deed earns. '
                                       'Explain how you will ladder maturities and reinvest redemptions so '
                                       'capital keeps working without crowding your deadlines.',
                             'example': 'Friends lend to the LLC on unsecured notes at 10 percent while '
                                        'Georgia redeemable deeds earn the 20 percent penalty, with '
                                        'lenders refunded if a bid strikes out [Ross Budrakey — '
                                        'VmzztAnZ71w @ 01:24:13]. Florida liens are allowed to run up to '
                                        'five years at 18 percent and are reinvested on a ladder [CamaPlan '
                                        'Self Directed IRA — U08uLxrDVE4 @ 00:44:40].'},
                            {'name': 'reo_exit_and_scaling_rule',
                             'type': 'textarea',
                             'prompt': 'Name your proven channel for selling any property you end up '
                                       'owning, and the scaling rule you will follow. Record the maximum '
                                       'bid tied to that exit, the foreclosure attorney you will use, and '
                                       'the costs you will carry after year one.',
                             'example': 'Exit channel proven with two wholesale sales before entering '
                                        'Georgia and Texas, where REO rates run at least 60 percent '
                                        '[Platinum Investment Properties Group - Tax Liens — AcKbZeNuPr4 @ '
                                        '00:21:38]. Maximum bid set only after the exit was locked [Ross '
                                        'Budrakey — VmzztAnZ71w @ 00:36:42]. A tax attorney handles every '
                                        'foreclosure, and post-day-365 costs are budgeted [Advanta IRA — '
                                        'c3YDDPR5wVo @ 00:44:29].'}],
                 'completion_gate': 'Do not commit new capital until equity exposure is measured, deed '
                                    'issuance is confirmed in writing, every notice is documented, the '
                                    'bankruptcy check is timed to the sale, redemption ticklers are set, '
                                    'the bankroll and reserve are sized, retirement and entity plumbing is '
                                    'live, and a proven exit channel is locked to the maximum bid.'}]}
