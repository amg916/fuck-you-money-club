from __future__ import annotations

CHAPTER_4 = {'id': 'Q4',
 'chapter_id': 'Q4',
 'chapter_number': 4,
 'question_number': 4,
 'slug': 'auction-formats-and-the-real-yield',
 'question_prompt': 'How do tax lien auction formats work, and how do bid-downs and premiums change my '
                    'actual return?',
 'kicker': 'Q4 / THE BIG MONEY PLAYBOOKS',
 'title': 'Auction Formats and the Real Yield',
 'subtitle': 'Interest Bid-Downs to 0.25%, Premium and Overbid States, Ownership-Interest Bidding, '
             "Interest Versus Penalty Rates, Premium Formulas, Colorado's 13%, and the Worst States for "
             'Returns',
 'layout_template': 'comparison_matrix',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners agree the statutory rate is only a ceiling and the auction format '
                      'decides the real yield. Florida and Arizona bid interest down from 18% and 16%; New '
                      'Jersey runs 18% to 0% and then flips into dollar premiums at 0% interest; Colorado '
                      'and other overbid states fix the rate and auction the premium; Louisiana and Utah '
                      'bid down ownership percentage instead. Institutional money and online platforms '
                      'grind popular counties toward zero, yet a 0.25% Florida bid still collects a 5% '
                      'penalty on fast redemption, Colorado pays about 13%, and Arizona proxy engines can '
                      'award the full 16% to a lone bidder. Operators split on whether quarter-point '
                      'fast-five plays and 1% ownership bids are smart bets or traps when liens sit '
                      'unredeemed for years, and on whether to fight New Jersey institutions or pivot '
                      'elsewhere.',
 'key_metrics': [{'label': 'Florida quarter-point penalty floor',
                  'metric': 'Florida quarter-point penalty floor',
                  'value': '5% penalty collected even on a 0.25% winning bid',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Brian Seinsticker explains the 'fast five' model: the 5% penalty applies "
                             'even if the lien redeems the next day, so quarter-point bidders still earn '
                             '5% on quick redemptions.',
                  'source': 'Tax Sale Resources ([XbThUArmcIE @ 00:01:24])'},
                 {'label': 'Colorado redemption payoff',
                  'metric': 'Colorado redemption payoff',
                  'value': 'About 13% in 2026 (9% above the federal discount rate)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Colorado liens carry a 3-year redemption period and are sold under a premium '
                             'bid system; the payoff on redemption runs 9% over the federal discount rate.',
                  'source': 'Tax Sale Secrets ([stFlmSmpP3Q @ 00:01:09])'},
                 {'label': 'Arizona proxy-bid win rate',
                  'metric': 'Arizona proxy-bid win rate',
                  'value': '16% maximum awarded when a lone 5% bid wins under proxy',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'In proxy bid counties the engine wins at the closest increment, so an '
                             'uncontested 5% bid clears at 16%; in direct bid counties the same bid locks '
                             'in 5%.',
                  'source': 'Realauction ([cleRXY7vybQ @ 00:02:20])'},
                 {'label': 'Louisiana redemption rate under ownership bid-down',
                  'metric': 'Louisiana redemption rate under ownership bid-down',
                  'value': '95% to 97% of liens redeem',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Brian Seinsticker says the ownership bid method has nothing to do with what '
                             'you earn on redemption, and 95% to 97% of Louisiana liens still redeem.',
                  'source': 'Tax Sale Resources ([3thEKo1DOwU @ 00:03:36])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner on this beat agrees on one thing first: the statutory '
                              'rate printed in the law is a ceiling, and the auction format decides how '
                              'much of it survives to your pocket. Casey Demmon of Tax Sale Academy lays '
                              'out the bid-down engine plainly: the sale opens at the highest allowable '
                              'rate set by statute, bidders call it down in steps, and whoever accepts the '
                              'lowest rate takes the lien, with Florida opening at 18% and sliding through '
                              '16, 14, 12, 10, nine, eight [0XlgBwC8tog @ 00:00:49]. Julia M. Spencer '
                              'frames it against a normal auction: the price is set and does not change, '
                              'so competitors are not bidding the price up, they are bidding the interest '
                              'down to the lowest number they can live with [NAHQ-7eWR_c @ 00:01:25]. '
                              'Olivia at Smart Capital hammers the same point from the yield side, calling '
                              'the 18%, 16%, and 24% headlines ceilings set by law rather than promises, '
                              'because in a competitive county the 18% routinely gets bid down to a small '
                              "fraction of the ceiling [TL6AIsoe5m0 @ 00:07:14]. Realauction's New Jersey "
                              'walkthrough shows the extreme version: interest bids run from 18% to 0%, '
                              'and once bidding passes zero it flips into dollar premiums tied to 0% '
                              'interest [hKsLdKqVOE0 @ 00:00:54].',
                              'The second consensus point: premium, or overbid, formats invert the auction '
                              'while freezing the rate. Casey Demmon describes premium states as ones '
                              'where the interest rate is set by state statute and never changes, and the '
                              'lien goes to whoever pays the most above the face value of the back taxes, '
                              'with the gap between what is owed and what is paid called the premium or '
                              'overbid [0I_mhnrF0So @ 00:01:05]. Brian Seinsticker of Tax Sale Resources '
                              'says that whatever the local label, high bid premium, true bid premium, bid '
                              'up, it is the traditional auction most people already picture, live or '
                              'online, outbidding the other bidders in dollars [6hRZuHmCM0M @ 00:01:10]. '
                              'The Tax Sale Secrets hosts put Colorado in this camp: a 3-year redemption '
                              'under a premium bid system where a $1,200 lien gets bid to 1,201, 1,202, '
                              '1,203, and paying $5 or $10 over is effectively how you bid down your '
                              "interest [stFlmSmpP3Q @ 00:01:43]. Smart Capital's Olivia adds that some "
                              'counties run round-robin or rotational systems instead, and insists you '
                              'know which system your county uses before you show up, because the winning '
                              'strategy is completely different under each [TL6AIsoe5m0 @ 00:17:46]. '
                              'Misread the format and you misread the yield before placing a single bid.',
                              'The third agreement is about who is on the other side of the paddle. Josh, '
                              "on Dustin Hahn's Tax Lien School panel, says New Jersey makes their "
                              'worst-states list because large investors scoop up everything and are '
                              'willing to bid it down to 0%, which makes it very hard for anyone to be '
                              'scrappy when institutions or hedge funds show up [mHvzzGVcYdI @ 00:01:36]. '
                              'Julia M. Spencer reports the same pattern: institutional investors like '
                              'banks bid the interest down to almost zero or half a percent because they '
                              'do not care about keeping properties and have a very high amount of money '
                              'to park in liens on valuable properties [NAHQ-7eWR_c @ 00:02:17]. The SKW '
                              'Central trainer quotes an article on Pima County, Arizona, where banks '
                              'bought nearly 6,000 tax liens totaling at least $15.8 million after the '
                              '2008 bailout, earning up to 16% with a three-year foreclosure trigger, and '
                              'concludes that if they recognize the value, so should individual investors '
                              "[e-CuINE8x-g @ 00:00:48]. Smart Capital's Olivia names the mechanism behind "
                              'the compression: online platforms like Real Auction opened the market to '
                              'out-of-state money, which increased competition and pushed winning rates '
                              'down in popular counties [TL6AIsoe5m0 @ 00:16:39]. Big money and easy '
                              'access both grind the rate toward the floor.'],
               'table': {'caption': 'Auction formats and how each one sets the real yield',
                         'headers': ['Auction Format',
                                     'How the Winner Is Picked',
                                     'Yield Consequence',
                                     'Expert Source'],
                         'rows': [['Interest rate bid-down auction as run in Florida',
                                   'Opens at the 18% statutory maximum; lowest accepted rate takes the '
                                   'lien',
                                   'Liens seen selling at 1% or 1.5% plus a five or six percent penalty',
                                   'Tax Sale Academy ([0XlgBwC8tog @ 00:00:49])'],
                                  ['New Jersey bid-down that rolls into dollar premiums',
                                   'Interest bids from 18% down to 0%, then highest dollar premium wins',
                                   'Every premium bid carries 0% interest when the lien redeems',
                                   'Realauction ([hKsLdKqVOE0 @ 00:01:12])'],
                                  ['Arizona whole-percent bid-down on the Realauction platform',
                                   'Whole percent bids between zero and 16; lowest rate wins the lien',
                                   'Proxy or direct bid engine changes the rate you actually clear at',
                                   'Realauction ([cleRXY7vybQ @ 00:01:18])'],
                                  ['Premium or overbid format with a statutory fixed rate',
                                   'Rate never changes; whoever pays most above face value becomes lien '
                                   'holder',
                                   'Premium may or may not be reimbursed and may or may not earn interest',
                                   'Tax Sale Academy ([0I_mhnrF0So @ 00:01:05])'],
                                  ['Colorado premium bid on a 3-year redemption certificate',
                                   'Bidders push a $1,200 lien to 1,201, 1,202, 1,203 above face',
                                   'Payoff runs 9% above the federal discount rate, about 13% in 2026',
                                   'Tax Sale Secrets ([stFlmSmpP3Q @ 00:01:09])'],
                                  ['Ownership interest bid-down used in Louisiana and Utah',
                                   'Rate and price stay fixed; bidders shave ownership percentage down '
                                   'from 100%',
                                   'You still earn the automatic maximum statutory interest; ownership '
                                   'bites only at foreclosure',
                                   'Tax Sale Resources ([3thEKo1DOwU @ 00:02:31])'],
                                  ['Round-robin or rotational allocation used in some counties',
                                   'County spreads certificates among registered bidders rather than pure '
                                   'competitive bidding',
                                   'Winning strategy is completely different, so identify the system '
                                   'before arriving',
                                   'Smart Capital ([TL6AIsoe5m0 @ 00:17:46])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["The mechanics start inside the bidding software. Realauction's New Jersey "
                              'walkthrough runs the click path: Place Bids on the left, the batch summary '
                              'screen, click a batch number, then work the bid menu where each ADV number '
                              'opens item details and the face amount sits in the center; a page-fill tool '
                              'drops one rate across every item, but you still must click Bid or Submit '
                              'Bids, and it only covers the page you are looking at, not later pages in '
                              'the batch [hKsLdKqVOE0 @ 00:02:10]. The Arizona module adds the setting '
                              'that silently changes your yield: in a proxy bid county, if you bid 5% and '
                              'nobody else bids, the engine wins you the 16% maximum, while in a direct '
                              'bid county 5% is what you get even as the only bidder [cleRXY7vybQ @ '
                              "00:02:20]. Smart Capital's Olivia layers on session discipline: big online "
                              'sales run in batches with hundreds of liens each over several days, bidders '
                              'in every batch make worse decisions in the last one, and experienced '
                              'bidders pre-rank targets and set automated maximums so the plan executes '
                              "when attention fades [TL6AIsoe5m0 @ 00:18:18]. They also flag Florida's "
                              'cash clock: 10% at the auction and the balance within 48 hours, or you can '
                              'lose the deposit and the certificate [TL6AIsoe5m0 @ 00:17:12].',
                              'Real yield math splits into interest and penalty. Dustin Hahn explains '
                              'interest states accrue monthly, so a 12% certificate pays 1% a month, and a '
                              "lien redeemed one month after sale returns 1.33% at Arizona's 16% or 1.5% "
                              'in Florida at the full rate, adding that much again for every month it sits '
                              '[Ip2V3ixjk4k @ 00:03:52]. Penalty states charge the full amount on day one: '
                              "Hahn's Texas example has the owner owing 25% on top of what you paid "
                              'whether they redeem on day one or day 179, and Georgia charges 20% the day '
                              'after the sale plus another 10% past the one-year mark [Ip2V3ixjk4k @ '
                              "00:02:28]. Brian Seinsticker connects the two inside Florida: the 'fast "
                              "five' model works because a 5% penalty applies even if the lien redeems the "
                              'next day, so a bidder at a quarter percent technically still earns 5% '
                              '[XbThUArmcIE @ 00:01:24]. Seinsticker frames it as a way of deploying '
                              'capital for a quick 5% and moving it somewhere else, not a strategy for '
                              'earning interest over a multi-year period. Casey Demmon reports seeing '
                              'liens sell at 1% or 1.5% for exactly that reason, since many states add a '
                              'penalty of maybe five or six percent on top [0XlgBwC8tog @ 00:01:38]. The '
                              'bid rate and the realized rate are two different numbers.',
                              'For pricing, Casey Demmon refuses a one-size premium formula for '
                              'individuals, noting institutions with tens of millions in liens can run one '
                              'because everything averages out; instead, call the county for redemption '
                              'stats, get a figure like 1.8 years or two years, and model a fake $1,000 '
                              'lien with a given premium against the return you need [cnd7EM15dyk @ '
                              '00:00:40]. The stacking angle changes that math: in some states, Casey '
                              'Demmon says, the first-year holder gets first option on years two, three, '
                              'and four, so a bidder can take year one at 1% and buy the later liens at '
                              '15% or 16% [0XlgBwC8tog @ 00:01:55]. Dustin Hahn confirms the New Jersey '
                              'version, where you bid the rate down but subsequent liens added on top earn '
                              'the full interest rate amount, calling it very powerful if done right '
                              "[Ip2V3ixjk4k @ 00:04:58]. Smart Capital's Olivia runs a straight interest "
                              'play for scale: an $8,000 lien won at a 12% bid-down rate with a two-year '
                              'redemption collects roughly $1,900, about 24% total over two years, with a '
                              '$200,000 house as collateral the whole time [TL6AIsoe5m0 @ 00:21:03]. Every '
                              'model starts from expected hold time, not from the auction-day rate.'],
               'table': {'caption': 'Bidding engine settings, payoff math, and cash rules operators work '
                                    'with',
                         'headers': ['Mechanic or Number',
                                     'Exact Figure Reported',
                                     'Operator Use',
                                     'Expert Source'],
                         'rows': [['Arizona proxy bid engine versus direct bid engine',
                                   'Lone 5% bid wins at 16% under proxy; direct bid locks 5%',
                                   'Check the county bidding rules before entering any rate at all',
                                   'Realauction ([cleRXY7vybQ @ 00:02:20])'],
                                  ['Florida quarter-point bid backed by the penalty floor',
                                   'A 0.25% winning bid still collects the 5% penalty on quick redemption',
                                   'Deploy capital for a fast 5%, then move it somewhere else',
                                   'Tax Sale Resources ([XbThUArmcIE @ 00:01:24])'],
                                  ['Monthly interest accrual in Arizona and Florida interest states',
                                   '16% Arizona works out to 1.33% monthly; Florida full rate pays 1.5% '
                                   'monthly',
                                   'Model the yield per month held instead of the annual headline rate',
                                   'Dustin Hahn ([Ip2V3ixjk4k @ 00:03:52])'],
                                  ['Texas and Georgia flat penalty on redeemable deeds',
                                   'Texas 25% any day in six months; Georgia 20% plus 10% after one year',
                                   'Penalty pays the full amount even on a next-day redemption',
                                   'Dustin Hahn ([Ip2V3ixjk4k @ 00:02:28])'],
                                  ['Colorado statutory payoff on redeemed certificates of purchase',
                                   '9% above the federal discount rate, about 13% in 2026',
                                   'Expect premium bidding to push effective returns toward about 10%',
                                   'Tax Sale Secrets ([stFlmSmpP3Q @ 00:01:09])'],
                                  ['Overbid example from a live premium state sale',
                                   '$293.57 face value certificate won with a $28.82 premium on top',
                                   'Confirm whether the premium is refunded and whether it earns interest',
                                   'Tax Sale Academy ([0I_mhnrF0So @ 00:01:50])'],
                                  ['Florida winning bidder payment clock after the auction closes',
                                   '10% paid at the auction and the remaining balance within 48 hours',
                                   'Stage funds before bidding or lose both deposit and certificate',
                                   'Smart Capital ([TL6AIsoe5m0 @ 00:17:12])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Where the yield hides from the crowd',
                           'body': 'Operators find rate where the institutional bidders and auction-day '
                                   'tourists are not looking.',
                           'items': ['Sort big lien lists by face amount: the Montezuma County, Colorado '
                                     'list opens with $25 and $26 liens on lots and acreage, and the '
                                     'well-secured $900 to $128,000 liens on homes and hotels only start '
                                     'showing about 11 pages in [Tax Sale Secrets — stFlmSmpP3Q @ '
                                     '00:04:24].',
                                     "Pull the county's past auction results first: if downtown condo "
                                     'liens get bid to near zero while suburban single-family liens clear '
                                     'at double-digit rates, the market is telling you where the crowd is '
                                     'not [Smart Capital — TL6AIsoe5m0 @ 00:14:44].',
                                     'Chase liens too big for most bidders: the hosts flagged a $128,000 '
                                     'lien on a Best Western valued at 5.7 million and about $250,000 in '
                                     'liens tied to one hotel operator, noting only so many people have '
                                     'that money to bid against you and you could probably still get them '
                                     'close to 10% [Tax Sale Secrets — stFlmSmpP3Q @ 00:10:01].',
                                     'In New Jersey, dodge the institutions by sticking to '
                                     'smaller-population counties, or pivot to Pennsylvania and New York '
                                     'where Josh says you will find better opportunities [Dustin Hahn — '
                                     'I9YP4P0-OM0 @ 00:00:44].']},
               'sop_steps': [{'step': 1,
                              'title': 'Identify the format and the engine',
                              'action': 'Confirm bid-down, premium, ownership, or rotational format and '
                                        'whether the county runs proxy or direct bidding.',
                              'detail': 'Open the county or municipality bidding rules to see whether a '
                                        'proxy auction will win you the maximum rate or a direct auction '
                                        'will lock in exactly what you typed [Realauction — cleRXY7vybQ @ '
                                        '00:02:43].'},
                             {'step': 2,
                              'title': "Get the county's redemption timeline",
                              'action': 'Call the county for redemption stats and build a personal premium '
                                        'or rate formula off that hold period.',
                              'detail': "Use the county's figure, such as 1.8 years or two years, then run "
                                        'a fake $1,000 lien with a given premium against the return you '
                                        'need, adjusting as you go [Tax Sale Academy — cnd7EM15dyk @ '
                                        '00:00:40].'},
                             {'step': 3,
                              'title': 'Separate penalty from interest',
                              'action': 'Know whether the state pays a flat penalty on early redemption '
                                        'before deciding how low to bid.',
                              'detail': 'In Florida a quarter-point bid still earns the 5% penalty if the '
                                        'lien redeems the next day, which is the whole basis of the '
                                        'fast-five model [Tax Sale Resources — XbThUArmcIE @ 00:01:41].'},
                             {'step': 4,
                              'title': 'Set the walk-away cap and load the platform',
                              'action': 'Pre-rank targets, write down a maximum, and set automated '
                                        'maximums where the platform allows.',
                              'detail': 'Start from a conservative value, multiply by a 60 to 70% safety '
                                        'factor, subtract surviving liens, quiet title costs, and holding '
                                        'costs, and stop when bidding passes that number [Smart Capital — '
                                        'TL6AIsoe5m0 @ 00:18:51].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The first fault line is whether a bid cap should come from a fixed formula '
                              'at all. Olivia at Smart Capital teaches a hard walk-away number set before '
                              'the gavel drops: conservative value times 0.65, minus every surviving lien, '
                              'minus quiet title costs, minus holding costs, with no exceptions once '
                              'bidding passes it. On a $200,000 Florida house carrying an $8,000 lien, '
                              'that math lands at $115,000 of maximum total exposure [TL6AIsoe5m0 @ '
                              '00:19:24]. Casey at Tax Sale Academy refuses to hand out a one-size formula '
                              'for individuals, conceding only that institutions sitting on tens of '
                              'millions of dollars in liens can run one because they play the long average '
                              "and everything evens out [cnd7EM15dyk @ 00:00:15]. Casey's alternative is a "
                              'personal formula: call the county for redemption stats, take the typical '
                              '1.8 or 2 years as the starting number, model a fake $1,000 lien at a given '
                              'premium, and solve for the return required, folding in suit and quiet title '
                              'costs whenever foreclosure is on the table [cnd7EM15dyk @ 00:00:40]. Brian '
                              'Seinsticker of Tax Sale Resources adds that high bid premium, true bid '
                              'premium and bid up are all names for the same traditional bid-up auction, '
                              'so the formula fight is really about how far to chase a familiar price war '
                              '[6hRZuHmCM0M @ 00:01:10].',
                              'The second split is whether a near-zero rate is a smart play or a slow '
                              "bleed. Brian Seinsticker explains the Florida 'fast five': bidders drive "
                              'the rate to a quarter point because a 5% penalty pays even if the lien '
                              'redeems the next day, which turns the certificate into a way to deploy '
                              'capital, grab a quick 5%, and move the money somewhere else [XbThUArmcIE @ '
                              '00:01:24]. Casey at Tax Sale Academy reports liens selling at 1% or 1.5% '
                              'for the same reason, because many states stack a penalty of five or six '
                              'percent on top, and lays out a second angle: take the first-year lien at 1% '
                              'to hold the first option on years two, three and four, then buy those later '
                              "liens at 15% or 16% [0XlgBwC8tog @ 00:01:38]. Dustin Hahn's crew runs "
                              'identical logic in New Jersey, where the initial lien gets bid down but '
                              'subsequent liens bought on top carry the full interest rate, a move Dustin '
                              'calls very powerful when done right [Ip2V3ixjk4k @ 00:04:58]. Julia M. '
                              'Spencer reads the floor differently: banks and other institutions bid '
                              'toward zero or half a percent because they do not care about keeping '
                              'properties and have huge sums to park against high-value collateral '
                              '[NAHQ-7eWR_c @ 00:02:17].',
                              'The third split is about which arena to enter in the first place. Josh, on '
                              "Dustin Hahn's panel, ranks New Jersey among the worst states because hedge "
                              'funds and large institutions sweep the sale and bid it to zero, so a '
                              'scrappy buyer should stick to smaller-population areas or pivot to '
                              "Pennsylvania's over-the-counter tax deeds or to New York [I9YP4P0-OM0 @ "
                              '00:00:44]. The Tax Sale Secrets hosts argue the opposite end of the size '
                              'curve in Colorado: a $128,000 lien on a Best Western valued near $5.7 '
                              'million, and roughly $250,000 in liens tied to one hotel operator, are buys '
                              'for a millionaire because few bidders can bring that cash, and even '
                              'rate-minded big fish might leave them close to 10% [stFlmSmpP3Q @ '
                              '00:10:01]. On ownership bid-down sales, Brian Seinsticker says the '
                              'ownership percentage is irrelevant to redemption earnings in Louisiana, '
                              'where 95 to 97 percent of liens redeem, so the odd format alone is no '
                              'reason to stay away [3thEKo1DOwU @ 00:03:36]. Casey treats the same format '
                              'as a co-ownership fight waiting to happen: a 30% winner who forecloses must '
                              'negotiate a buyout with the 70% delinquent owner or sue to force a '
                              'partition sale, usually with a hired attorney [YMBhKuuupDc @ 00:03:07].'],
               'table': {'caption': 'Competing auction playbooks reported by practitioners across '
                                    'bid-down, premium and ownership formats',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How to set the maximum bid before the auction',
                                   'Fixed walk-away cap: conservative value times 0.65 minus surviving '
                                   'liens, quiet title and holding costs',
                                   'Personal formula built from county redemption stats, because no single '
                                   'formula fits every individual investor',
                                   'Smart Capital ([TL6AIsoe5m0 @ 00:35:11]); Tax Sale Academy '
                                   '([cnd7EM15dyk @ 00:00:40])'],
                                  ['Bidding Florida liens down to a quarter point',
                                   'Collect the 5% penalty on fast redemptions and recycle the capital '
                                   'into the next deployment',
                                   'Avoid for multi-year holds, because a two-year lien drops to roughly '
                                   '2.5% a year',
                                   'Tax Sale Resources ([XbThUArmcIE @ 00:01:41]); Tax Sale Resources '
                                   '([XbThUArmcIE @ 00:02:11])'],
                                  ['Whether to compete in New Jersey lien sales at all',
                                   'Skip it: institutions bid to 0%, so move to smaller counties, '
                                   'Pennsylvania or New York',
                                   'Win the first lien low, then buy subsequent liens that pay the full '
                                   'statutory interest rate',
                                   'Dustin Hahn ([I9YP4P0-OM0 @ 00:00:44]); Dustin Hahn ([Ip2V3ixjk4k @ '
                                   '00:04:58])'],
                                  ['How to play Colorado premium bid auctions',
                                   'Bid dollars over face, such as $1,201 then $1,202, and chase big '
                                   'commercial liens few can fund',
                                   'Expect the premium itself to earn only a modest return once the '
                                   'certificate redeems',
                                   'Tax Sale Secrets ([stFlmSmpP3Q @ 00:01:43]); Smart Capital '
                                   '([TL6AIsoe5m0 @ 00:17:46])'],
                                  ['Bidding ownership percentage down in Louisiana-style sales',
                                   'Bid low freely, since 95 to 97 percent redeem and ownership bids never '
                                   'touch interest earned',
                                   'Plan the exit first: buyout negotiations or a partition sale lawsuit '
                                   'against the delinquent co-owner',
                                   'Tax Sale Resources ([3thEKo1DOwU @ 00:03:36]); Tax Sale Academy '
                                   '([YMBhKuuupDc @ 00:03:07])'],
                                  ['Preferred redemption speed for the capital being deployed',
                                   'Fast-redeeming states let investors recycle capital, while long '
                                   'lockups favor compounding the statutory rate',
                                   'Most liens that redeem do it within the first year, and each later '
                                   'year raises deed odds',
                                   'Smart Capital ([TL6AIsoe5m0 @ 00:24:03]); Tax Sale Secrets '
                                   '([stFlmSmpP3Q @ 00:07:05])'],
                                  ['Which statutory ceilings apply in Florida and Arizona',
                                   'Florida bidding starts at 18% and Arizona bids run between zero and '
                                   '16% whole percents',
                                   "Dustin Hahn's deck says Florida 16% and Arizona 18%, then computes "
                                   'Arizona at 1.33% monthly',
                                   'Smart Capital ([TL6AIsoe5m0 @ 00:17:29]); Dustin Hahn ([Ip2V3ixjk4k @ '
                                   '00:03:33])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive trap the practitioners report is a cheap rate or a fat '
                              'premium colliding with the wrong redemption clock. Brian Seinsticker warns '
                              'that the quarter-point Florida play burns the buyer who lands a lien that '
                              'never redeems: hold it two years and the effective return falls to about '
                              'two and a half percent a year, a figure Brian says does not even keep pace '
                              'with inflation [XbThUArmcIE @ 00:02:11]. Casey at Tax Sale Academy walks '
                              'through the premium-side version using a real certificate with a $293.57 '
                              'face value and a $28.82 overbid: in states where the overbid is not '
                              'reimbursed or earns no interest, paying too much and getting redeemed '
                              'before enough months accrue to cover the premium means losing money '
                              'outright [0I_mhnrF0So @ 00:02:27]. Olivia at Smart Capital lists the same '
                              'timing wound from the opposite direction, budgeting for a two-year hold '
                              'only to watch the owner redeem in month three at a pro-rated minimum return '
                              'while the capital sat idle [TL6AIsoe5m0 @ 00:28:49]. The Realauction New '
                              'Jersey walkthrough shows why premium pain lands so hard there: once bidding '
                              'moves past rate and into dollars above face, every premium bid associates '
                              'with 0% interest on redemption [hKsLdKqVOE0 @ 00:02:28]. The economics '
                              'check is identical across all four: the redemption timeline, not the '
                              'headline rate, decides whether the bid made money.',
                              'The second failure pattern is showing up where the capital in the room is '
                              'far bigger than yours. Josh, on the Tax Lien School panel, says most New '
                              'Jersey sales get scooped up by large investors willing to bid to 0%, '
                              'leaving more competition there than even in big California cities '
                              '[mHvzzGVcYdI @ 00:01:53]. The host adds that desirable California counties '
                              'such as Santa Barbara, San Luis Obispo and Ventura see little action at '
                              'all, because a bank carrying a million-dollar mortgage will simply pay '
                              'several thousand in back taxes rather than risk getting eliminated '
                              '[mHvzzGVcYdI @ 00:00:15]. The SKW Central trainer reads an article '
                              'reporting that bailed-out banks bought nearly 6,000 Pima County liens '
                              'totaling at least $15.8 million, chasing up to 16% with a three-year path '
                              'to foreclosure, and turns the initial anger into a signal that the asset '
                              'class is worth pursuing [e-CuINE8x-g @ 00:00:48]. Olivia at Smart Capital '
                              'explains why the crowd keeps growing: online platforms opened the market to '
                              'out-of-state investors, which increased competition and pushed winning '
                              'rates down in popular counties, the trade-off of convenience [TL6AIsoe5m0 @ '
                              '00:16:55]. The fix the practitioners report is geographic rather than '
                              'tactical: smaller counties, over-the-counter leftovers, and states where '
                              'the heavy money is not parked.',
                              'The third cluster is pure execution failure, where the bid or the paperwork '
                              'breaks rather than the deal itself. The Realauction New Jersey tutorial '
                              'flags that the fill tool types a number only across the page being viewed, '
                              'not every item in a multi-page batch, and that bids still need the bid key '
                              'or the submit bids click to register at all [hKsLdKqVOE0 @ 00:02:10]. '
                              'Olivia at Smart Capital names fatigue as a real cost in multi-day batch '
                              'auctions, noting that investors who bid in every batch make worse decisions '
                              'in the last one, so experienced bidders pre-rank targets and set automated '
                              'maximums wherever the platform allows it [TL6AIsoe5m0 @ 00:18:18]. Olivia '
                              'also calls missed notices the single most common way investors lose a valid '
                              'claim: a wrong address or a filing one day late has led courts to throw out '
                              'entire foreclosures, taking the legal fees, the time, and sometimes the '
                              'investment position with them [TL6AIsoe5m0 @ 00:25:09]. Brian Seinsticker '
                              'supplies the endgame trap for ownership bid-down states: bid ownership down '
                              'to 1% and a foreclosure leaves the investor sharing the property with a 99% '
                              'previous owner who is unhappy about it, a setup Brian expects to breed '
                              'confusion and disputes [3thEKo1DOwU @ 00:02:48]. Every one of these losses '
                              'hit after the hard work of finding the lien was already done.'],
               'table': {'caption': 'Firsthand failure modes and the economics check each one demands',
                         'headers': ['Failure Mode', 'What Happens', 'Economics Check', 'Expert Source'],
                         'rows': [['Quarter-point Florida lien that never redeems',
                                   'The 0.25% bid relied on the 5% penalty, but the hold stretches past '
                                   'two years',
                                   'Effective return drops to roughly 2.5% a year, below the pace of '
                                   'inflation',
                                   'Tax Sale Resources ([XbThUArmcIE @ 00:02:11])'],
                                  ['Unreimbursed overbid in a premium state',
                                   'A $28.82 premium sits on a $293.57 face certificate in a non-refund '
                                   'state',
                                   'Redemption before interest covers the premium turns the certificate '
                                   'into a straight loss',
                                   'Tax Sale Academy ([0I_mhnrF0So @ 00:02:27])'],
                                  ['Low ownership bid that fails to redeem',
                                   'The foreclosing investor becomes a minority co-owner alongside the '
                                   'original delinquent owner',
                                   'Getting money out requires a negotiated buyout or a partition sale '
                                   'lawsuit with counsel',
                                   'Tax Sale Academy ([YMBhKuuupDc @ 00:03:07])'],
                                  ['Tiny lien sitting on a very low-value lot',
                                   'A $300 lien on a $5,000 lot heads toward foreclosure legal work',
                                   'Thousands of dollars in foreclosure costs destroy the economics of the '
                                   'entire deal',
                                   'Smart Capital ([TL6AIsoe5m0 @ 00:22:15])'],
                                  ['Missed Florida payment deadline after winning',
                                   'Winning bidder must pay 10% at the auction and the balance within 48 '
                                   'hours',
                                   'Miss the window and both the deposit and the certificate can be lost',
                                   'Smart Capital ([TL6AIsoe5m0 @ 00:17:12])'],
                                  ['Page-only bid fill on a multi-page batch',
                                   'The fill tool populates only the visible page, not every item in the '
                                   'batch',
                                   'Items on the other pages carry no bid until entered and submitted '
                                   'separately',
                                   'Realauction ([hKsLdKqVOE0 @ 00:02:10])'],
                                  ['Lowball rate entered in an Arizona direct-bid county',
                                   'Bidder enters 5% as the only bidder where the county runs direct '
                                   'bidding',
                                   'The lien is won at 5%, not the 16% maximum a proxy engine would award',
                                   'Realauction ([cleRXY7vybQ @ 00:02:43])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Checks Before Any Bid Goes In',
                           'body': 'Every loss the practitioners reported traces back to a format rule, a '
                                   'redemption clock, or a deadline the bidder did not price in. Clear all '
                                   'four gates before entering a rate, a premium, or an ownership '
                                   'percentage.',
                           'items': ['Price every sub-1% bid against a no-redemption scenario, because a '
                                     'quarter-point lien held two years yields only about 2.5% a year [Tax '
                                     'Sale Resources — XbThUArmcIE @ 00:02:11]',
                                     'Confirm whether the state returns the overbid and pays interest on '
                                     'it before bidding any premium above face value [Tax Sale Academy — '
                                     '0I_mhnrF0So @ 00:02:42]',
                                     'Read the county bidding rules for proxy versus direct bid before '
                                     'entering a low rate as a possible sole bidder [Realauction — '
                                     'cleRXY7vybQ @ 00:02:43]',
                                     'Calendar every foreclosure notice and filing deadline, since one day '
                                     'late has gotten entire foreclosures thrown out [Smart Capital — '
                                     'TL6AIsoe5m0 @ 00:25:09]']}}],
 'pull_quote': 'If you pay too much money for the face value of that certificate and not enough months '
               'pass by where that interest will accumulate to cover your over bid, then guess what, '
               "you're gonna lose money. — Tax Sale Academy (0I_mhnrF0So @ 00:02:27).",
 'diagram_id': 'diag-07',
 'action_checklist': ['Call the county for its average redemption time, such as 1.8 or 2 years, and build '
                      'a personal premium formula from that starting number [Tax Sale Academy — '
                      'cnd7EM15dyk @ 00:00:40]',
                      'Write down a walk-away cap before the auction: conservative value times 0.65 minus '
                      'surviving liens, quiet title costs and holding costs [Smart Capital — TL6AIsoe5m0 @ '
                      '00:35:11]',
                      'In New Jersey, accept a low rate on the initial lien, then buy subsequent liens '
                      'that carry the full interest rate [Dustin Hahn — Ip2V3ixjk4k @ 00:04:58]',
                      'In Florida, reserve quarter-point bids for capital meant to come back fast through '
                      'the 5% penalty, not for multi-year holds [Tax Sale Resources — XbThUArmcIE @ '
                      '00:01:41]',
                      'When institutions sweep a New Jersey sale, shift to smaller-population counties or '
                      'pivot to Pennsylvania or New York [Dustin Hahn — I9YP4P0-OM0 @ 00:00:44]',
                      'Sort Colorado lien lists by face amount and target the large commercial liens few '
                      'bidders have the cash to chase [Tax Sale Secrets — stFlmSmpP3Q @ 00:04:24]'],
 'statutory_citations': [{'title': 'Tax Sale Resources — Why Do Investors Bid Down Florida Tax Lien '
                                   'Interest Rate To 0.25? [00:01:24]',
                          'url': 'https://www.youtube.com/watch?v=XbThUArmcIE&t=84s',
                          'relevance': 'Primary practitioner testimony on the Florida fast-five penalty '
                                       'play and how a non-redeeming quarter-point lien burns the buyer.'},
                         {'title': 'Tax Sale Academy — Tax Lien Overbid Auction Process [00:02:07]',
                          'url': 'https://www.youtube.com/watch?v=0I_mhnrF0So&t=127s',
                          'relevance': 'Primary practitioner testimony on unreimbursed overbids and how '
                                       'premium bidders lose money on early redemption.'},
                         {'title': 'Tax Sale Academy — Tax Lien Ownership Interest Bid Down [00:02:06]',
                          'url': 'https://www.youtube.com/watch?v=YMBhKuuupDc&t=126s',
                          'relevance': 'Primary practitioner testimony on co-ownership after foreclosure, '
                                       'buyouts and forced partition sales in ownership bid-down states.'},
                         {'title': 'Smart Capital — Tax Lien Investing for Beginners: 8-18% Interest? '
                                   'Risks & Auction Mistakes [00:19:24]',
                          'url': 'https://www.youtube.com/watch?v=TL6AIsoe5m0&t=1164s',
                          'relevance': 'Primary practitioner testimony on the 0.65 maximum bid cap formula '
                                       'and its worked Florida example.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'hKsLdKqVOE0',
                       'title': 'Bidding: Tax Lien New Jersey',
                       'channel': 'Realauction',
                       'author': 'Realauction',
                       'text': 'Within the state of New Jersey, all items are sold to the investor who is '
                               'willing to accept the lowest interest rate or, should the bidding proceed '
                               'beyond interest rate, the one willing to accept the highest premium.',
                       'tip': 'Within the state of New Jersey, all items are sold to the investor who is '
                              'willing to accept the lowest interest rate or, should the bidding proceed '
                              'beyond interest rate, the one willing to accept the highest premium.',
                       'timestamp': 72,
                       'timestamp_seconds': 72,
                       'timestamp_label': '[00:01:12]',
                       'url': 'https://www.youtube.com/watch?v=hKsLdKqVOE0&t=72s',
                       'markdown': '[00:01:12](https://www.youtube.com/watch?v=hKsLdKqVOE0&t=72s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6hRZuHmCM0M',
                       'title': 'What is tax deed and tax lien premium bidding',
                       'channel': 'Tax Sale Resources',
                       'author': 'Tax Sale Resources',
                       'text': 'A bid up for a premium auction is really the traditional auction style '
                               'that most people are familiar with.',
                       'tip': 'A bid up for a premium auction is really the traditional auction style that '
                              'most people are familiar with.',
                       'timestamp': 100,
                       'timestamp_seconds': 100,
                       'timestamp_label': '[00:01:40]',
                       'url': 'https://www.youtube.com/watch?v=6hRZuHmCM0M&t=100s',
                       'markdown': '[00:01:40](https://www.youtube.com/watch?v=6hRZuHmCM0M&t=100s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cnd7EM15dyk',
                       'title': 'Formula for Tax Lien Premiums (Viewer Question)',
                       'channel': 'Tax Sale Academy',
                       'author': 'Tax Sale Academy',
                       'text': 'Call the county and see if they have any stats, see how long it takes most '
                               'tax liens to get redeemed, and that gives you a starting number for your '
                               'calculations.',
                       'tip': 'Call the county and see if they have any stats, see how long it takes most '
                              'tax liens to get redeemed, and that gives you a starting number for your '
                              'calculations.',
                       'timestamp': 40,
                       'timestamp_seconds': 40,
                       'timestamp_label': '[00:00:40]',
                       'url': 'https://www.youtube.com/watch?v=cnd7EM15dyk&t=40s',
                       'markdown': '[00:00:40](https://www.youtube.com/watch?v=cnd7EM15dyk&t=40s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0I_mhnrF0So',
                       'title': 'Tax Lien Overbid Auction Process',
                       'channel': 'Tax Sale Academy',
                       'author': 'Tax Sale Academy',
                       'text': 'If you pay too much money for the face value of that certificate and not '
                               'enough months pass by where that interest will accumulate to cover your '
                               "over bid, then you're gonna lose money.",
                       'tip': 'If you pay too much money for the face value of that certificate and not '
                              'enough months pass by where that interest will accumulate to cover your '
                              "over bid, then you're gonna lose money.",
                       'timestamp': 147,
                       'timestamp_seconds': 147,
                       'timestamp_label': '[00:02:27]',
                       'url': 'https://www.youtube.com/watch?v=0I_mhnrF0So&t=147s',
                       'markdown': '[00:02:27](https://www.youtube.com/watch?v=0I_mhnrF0So&t=147s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3thEKo1DOwU',
                       'title': 'What is the Bid Down Ownership Bidding Process?',
                       'channel': 'Tax Sale Resources',
                       'author': 'Tax Sale Resources',
                       'text': 'In the case of Louisiana, where still 95 to 97 percent of all liens '
                               "redeem, the bid method has nothing to do with what you're going to earn on "
                               'that redemption.',
                       'tip': 'In the case of Louisiana, where still 95 to 97 percent of all liens redeem, '
                              "the bid method has nothing to do with what you're going to earn on that "
                              'redemption.',
                       'timestamp': 216,
                       'timestamp_seconds': 216,
                       'timestamp_label': '[00:03:36]',
                       'url': 'https://www.youtube.com/watch?v=3thEKo1DOwU&t=216s',
                       'markdown': '[00:03:36](https://www.youtube.com/watch?v=3thEKo1DOwU&t=216s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mHvzzGVcYdI',
                       'title': 'The Worst States for Tax Liens and Tax Deeds - and Where To Go Instead',
                       'channel': 'Tax Lien School Highlights - Dustin Hahn',
                       'author': 'Tax Lien School Highlights - Dustin Hahn',
                       'text': "Most of the New Jersey tax sales, there's large investors that go in and "
                               "they just scoop up everything and they're willing to bid it down to 0%.",
                       'tip': "Most of the New Jersey tax sales, there's large investors that go in and "
                              "they just scoop up everything and they're willing to bid it down to 0%.",
                       'timestamp': 113,
                       'timestamp_seconds': 113,
                       'timestamp_label': '[00:01:53]',
                       'url': 'https://www.youtube.com/watch?v=mHvzzGVcYdI&t=113s',
                       'markdown': '[00:01:53](https://www.youtube.com/watch?v=mHvzzGVcYdI&t=113s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cleRXY7vybQ',
                       'title': 'Bidding: Tax Lien Arizona',
                       'channel': 'Realauction',
                       'author': 'Realauction',
                       'text': 'You bid 5% and no one else bids, you would win at the maximum interest '
                               'rate, which is 16% in Arizona.',
                       'tip': 'You bid 5% and no one else bids, you would win at the maximum interest '
                              'rate, which is 16% in Arizona.',
                       'timestamp': 140,
                       'timestamp_seconds': 140,
                       'timestamp_label': '[00:02:20]',
                       'url': 'https://www.youtube.com/watch?v=cleRXY7vybQ&t=140s',
                       'markdown': '[00:02:20](https://www.youtube.com/watch?v=cleRXY7vybQ&t=140s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XbThUArmcIE',
                       'title': 'Why Do Investors Bid Down Florida Tax Lien Interest Rate To 0.25?',
                       'channel': 'Tax Sale Resources',
                       'author': 'Tax Sale Resources',
                       'text': 'You buy that lien at a quarter percent and it never redeems, and now '
                               "you've owned that lien for two years, and technically you've got a two and "
                               'a half percent yearly return.',
                       'tip': "You buy that lien at a quarter percent and it never redeems, and now you've "
                              "owned that lien for two years, and technically you've got a two and a half "
                              'percent yearly return.',
                       'timestamp': 131,
                       'timestamp_seconds': 131,
                       'timestamp_label': '[00:02:11]',
                       'url': 'https://www.youtube.com/watch?v=XbThUArmcIE&t=131s',
                       'markdown': '[00:02:11](https://www.youtube.com/watch?v=XbThUArmcIE&t=131s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'e-CuINE8x-g',
                       'title': 'SKW Central | Tax Lien investing part 3',
                       'channel': 'skwcentraltraining',
                       'author': 'skwcentraltraining',
                       'text': 'Since the bank bailout in 2008, major banks have bought nearly 6,000 tax '
                               'liens in Pima County that total at least 15.8 million.',
                       'tip': 'Since the bank bailout in 2008, major banks have bought nearly 6,000 tax '
                              'liens in Pima County that total at least 15.8 million.',
                       'timestamp': 48,
                       'timestamp_seconds': 48,
                       'timestamp_label': '[00:00:48]',
                       'url': 'https://www.youtube.com/watch?v=e-CuINE8x-g&t=48s',
                       'markdown': '[00:00:48](https://www.youtube.com/watch?v=e-CuINE8x-g&t=48s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'I9YP4P0-OM0',
                       'title': 'Can You Really Earn 0% Interest on Tax Liens?',
                       'channel': 'Dustin Hahn',
                       'author': 'Dustin Hahn',
                       'text': 'The best way to combat that is to go to smaller counties, or you could '
                               'just simply pivot over to Pennsylvania because Pennsylvania has some of '
                               'the best over-the-counter tax deeds in the country.',
                       'tip': 'The best way to combat that is to go to smaller counties, or you could just '
                              'simply pivot over to Pennsylvania because Pennsylvania has some of the best '
                              'over-the-counter tax deeds in the country.',
                       'timestamp': 44,
                       'timestamp_seconds': 44,
                       'timestamp_label': '[00:00:44]',
                       'url': 'https://www.youtube.com/watch?v=I9YP4P0-OM0&t=44s',
                       'markdown': '[00:00:44](https://www.youtube.com/watch?v=I9YP4P0-OM0&t=44s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TL6AIsoe5m0',
                       'title': 'Tax Lien Investing for Beginners: 8-18% Interest? Risks & Auction '
                                'Mistakes',
                       'channel': 'Smart Capital',
                       'author': 'Smart Capital',
                       'text': 'Set your maximum cap before the auction using the formula conservative '
                               'value times 0.65 minus surviving liens minus quiet title costs minus '
                               'holding costs.',
                       'tip': 'Set your maximum cap before the auction using the formula conservative '
                              'value times 0.65 minus surviving liens minus quiet title costs minus '
                              'holding costs.',
                       'timestamp': 2111,
                       'timestamp_seconds': 2111,
                       'timestamp_label': '[00:35:11]',
                       'url': 'https://www.youtube.com/watch?v=TL6AIsoe5m0&t=2111s',
                       'markdown': '[00:35:11](https://www.youtube.com/watch?v=TL6AIsoe5m0&t=2111s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TL6AIsoe5m0',
                       'title': 'Tax Lien Investing for Beginners: 8-18% Interest? Risks & Auction '
                                'Mistakes',
                       'channel': 'Smart Capital',
                       'author': 'Smart Capital',
                       'text': 'Miss a required notice, serve the wrong address, or file a day late, and '
                               'courts have thrown out entire foreclosures.',
                       'tip': 'Miss a required notice, serve the wrong address, or file a day late, and '
                              'courts have thrown out entire foreclosures.',
                       'timestamp': 1509,
                       'timestamp_seconds': 1509,
                       'timestamp_label': '[00:25:09]',
                       'url': 'https://www.youtube.com/watch?v=TL6AIsoe5m0&t=1509s',
                       'markdown': '[00:25:09](https://www.youtube.com/watch?v=TL6AIsoe5m0&t=1509s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0XlgBwC8tog',
                       'title': 'Tax Lien Interest Bid Down Auctions',
                       'channel': 'Tax Sale Academy',
                       'author': 'Tax Sale Academy',
                       'text': 'You might accept the first lien the first year at 1% and then you might '
                               'buy years 2, 3 and 4 at 15 or 16 percent.',
                       'tip': 'You might accept the first lien the first year at 1% and then you might buy '
                              'years 2, 3 and 4 at 15 or 16 percent.',
                       'timestamp': 115,
                       'timestamp_seconds': 115,
                       'timestamp_label': '[00:01:55]',
                       'url': 'https://www.youtube.com/watch?v=0XlgBwC8tog&t=115s',
                       'markdown': '[00:01:55](https://www.youtube.com/watch?v=0XlgBwC8tog&t=115s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YMBhKuuupDc',
                       'title': 'Tax Lien Ownership Interest Bid Down',
                       'channel': 'Tax Sale Academy',
                       'author': 'Tax Sale Academy',
                       'text': 'You can sue them and force a partition sale, and that is going to be the '
                               "only way that you can get your money out if they won't negotiate with you.",
                       'tip': 'You can sue them and force a partition sale, and that is going to be the '
                              "only way that you can get your money out if they won't negotiate with you.",
                       'timestamp': 187,
                       'timestamp_seconds': 187,
                       'timestamp_label': '[00:03:07]',
                       'url': 'https://www.youtube.com/watch?v=YMBhKuuupDc&t=187s',
                       'markdown': '[00:03:07](https://www.youtube.com/watch?v=YMBhKuuupDc&t=187s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'stFlmSmpP3Q',
                       'title': "Colorado Tax Liens Pay 13% | Here's How It Works!",
                       'channel': 'Tax Sale Secrets',
                       'author': 'Tax Sale Secrets',
                       'text': "If you're a millionaire, these are some liens to buy, because there are "
                               'only so many people that are going to have that money to bid against you.',
                       'tip': "If you're a millionaire, these are some liens to buy, because there are "
                              'only so many people that are going to have that money to bid against you.',
                       'timestamp': 601,
                       'timestamp_seconds': 601,
                       'timestamp_label': '[00:10:01]',
                       'url': 'https://www.youtube.com/watch?v=stFlmSmpP3Q&t=601s',
                       'markdown': '[00:10:01](https://www.youtube.com/watch?v=stFlmSmpP3Q&t=601s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NAHQ-7eWR_c',
                       'title': "What does 'Bid Down the Interest' Mean in Tax Foreclosure Investing",
                       'channel': 'Julia M. Spencer',
                       'author': 'Julia M. Spencer',
                       'text': 'In some states institutional investors like banks invest in tax '
                               'foreclosures and they bid down the interest to almost like zero percent or '
                               "half a percent, because they really don't care about keeping the "
                               'properties.',
                       'tip': 'In some states institutional investors like banks invest in tax '
                              'foreclosures and they bid down the interest to almost like zero percent or '
                              "half a percent, because they really don't care about keeping the "
                              'properties.',
                       'timestamp': 137,
                       'timestamp_seconds': 137,
                       'timestamp_label': '[00:02:17]',
                       'url': 'https://www.youtube.com/watch?v=NAHQ-7eWR_c&t=137s',
                       'markdown': '[00:02:17](https://www.youtube.com/watch?v=NAHQ-7eWR_c&t=137s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ip2V3ixjk4k',
                       'title': 'Interest Rates VS Penalty Rates (TLTV Ep 23)',
                       'channel': 'Dustin Hahn',
                       'author': 'Dustin Hahn',
                       'text': 'In New Jersey you can bid the interest rate down, but if you buy the '
                               'subsequent liens on top of that you actually get the full interest rate '
                               'amount on those liens.',
                       'tip': 'In New Jersey you can bid the interest rate down, but if you buy the '
                              'subsequent liens on top of that you actually get the full interest rate '
                              'amount on those liens.',
                       'timestamp': 298,
                       'timestamp_seconds': 298,
                       'timestamp_label': '[00:04:58]',
                       'url': 'https://www.youtube.com/watch?v=Ip2V3ixjk4k&t=298s',
                       'markdown': '[00:04:58](https://www.youtube.com/watch?v=Ip2V3ixjk4k&t=298s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'}]}
