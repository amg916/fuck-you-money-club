from __future__ import annotations

CHAPTER_3 = {'id': 'Q3',
 'chapter_id': 'Q3',
 'chapter_number': 3,
 'question_number': 3,
 'slug': 'oil-gas-lease-pooling-owner-bargaining-power',
 'question_prompt': 'What does my oil and gas lease say, how does it stay alive, and how do pooling and '
                    'negotiation leverage affect my royalty?',
 'kicker': 'Q3 / THE BIG MONEY PLAYBOOKS',
 'title': 'The Oil and Gas Lease, Pooling and Owner Bargaining Power',
 'subtitle': 'Granting clause, royalty rate, shut-in and constructive production, cessation, dry-hole and '
             'continuous-operations clauses, Pugh clauses, pooling and unitization mechanics, landowner '
             'bargaining power, and listener Q&A on lease management',
 'layout_template': 'financial_analysis',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners converge on one rule: the lease is negotiated before signing or not '
                      'at all. No standard form exists, leases run for decades, and royalty terms outweigh '
                      'the bonus. Matt Sands prices a fair bonus at mineral value divided by 2 or 3 and '
                      'calls trading royalty rate for bonus short-sighted, while the Energy Law Professor '
                      'treats a zero or low bonus as a sign the operator is not serious about drilling. '
                      "Leverage scales with acreage: Steven Hatcher's 5,000-acre owners command 1/4 "
                      'cost-free royalties, while 5-acre owners in 1,280-acre units get pooled or '
                      'excluded. Street mechanics cover tract participation math, 300% force-pool '
                      'penalties, $300-per-acre deemed leases and Pugh audits. The sharpest split: holding '
                      "out for better terms versus Hatcher's Haynesville holdouts who lost "
                      'multi-million-dollar offers.',
 'key_metrics': [{'label': 'Fair Lease Bonus Rule of Thumb',
                  'metric': 'Fair Lease Bonus Rule of Thumb',
                  'value': 'Mineral value divided by 2 or 3 ($3,000/NMA minerals supports about '
                           '$1,000/acre bonus)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Matt Sands' benchmark for judging a lease bonus offer, given while answering "
                             'a Nacogdoches County Haynesville offer of $300/NMA on 14.3 net mineral '
                             'acres.',
                  'source': 'Matt Sands ([xiP5PiaaYKE @ 00:06:17])'},
                 {'label': 'Force-Pooling Risk Penalty',
                  'metric': 'Force-Pooling Risk Penalty',
                  'value': '300% ($18M of production on a $6M well before payout)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Alice Hog's second election option for a force-pooled owner; reworks reset "
                             'the penalty, and the default if no election is made is a deemed lease at '
                             '$300/acre and 1/8.',
                  'source': 'behoge13 ([le24nqd0H0M @ 00:35:49])'},
                 {'label': 'Small-Tract Pooled Royalty Dilution',
                  'metric': 'Small-Tract Pooled Royalty Dilution',
                  'value': "3/16 x 5/40 = .0234375 ('really 2% rather than 18%')",
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Allocation math showing what a 3/16 royalty owner with 5 acres in a 40-acre '
                             'pooled unit actually receives.',
                  'source': 'behoge13 ([le24nqd0H0M @ 00:13:55])'},
                 {'label': 'Haynesville Peak Lease Bonus',
                  'metric': 'Haynesville Peak Lease Bonus',
                  'value': '$20,000 per acre across six parishes',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Steven Hatcher's example of bonus levels during the Haynesville rush, where "
                             'some holdouts lost multi-million-dollar offers after delineation drilling '
                             'proved their acreage worthless.',
                  'source': 'Steven Hatcher | Minerals Guy ([hZZNvuvGfkc @ 00:02:04])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner who works lease paper opens with the same warning: there '
                              'is no standard lease, and the form the landman hands over is a starting '
                              "point, not a final deal. The Energy Law Professor flags the Producer's 88 "
                              'as an oil-company-friendly form and points owners toward bank trusts and '
                              'landowners associations for landowner-friendly paper [WBGDgooXnq8 @ '
                              '00:03:11]. Steven Hatcher of Minerals Guy frames the stakes in time, not '
                              "dollars: a lease can run 20, 30 or 50 years, so the owner's kids may end up "
                              'living with whatever gets signed, which is why the first pro tip is to '
                              "refuse to simply sign the landman's form [b97Q2qy5uEo @ 00:02:33]. Tracy "
                              'Lenz, an engineer reading decades of recorded leases from Utah to Ohio, '
                              'adds that leases are hard to exit once signed and that no universal '
                              'standard lease exists across counties or eras [HGUBxgz_6Ak @ 00:01:36]. The '
                              'professor also notes the one structural edge owners keep after signing: '
                              'courts read ambiguities against the lessee and imply covenants into the '
                              'deal [WBGDgooXnq8 @ 00:06:22]. The operator takeaway is blunt. The '
                              'negotiation happens before the ink dries, because the document then governs '
                              'royalty, deductions, term and release rights for as long as a well keeps '
                              'producing in paying quantities.',
                              'The second point of agreement is that royalty rate and deduction language '
                              'matter more than the check at signing. Matt Sands calls trading royalty '
                              "rate for a bigger bonus 'short-sighted,' because mineral value moves in "
                              'direct proportion to the royalty rate and that rate sets every future '
                              'check; the biggest single win, especially in gas plays, is no '
                              'post-production deduction or marketable-product language [xiP5PiaaYKE @ '
                              "00:06:37]. Steven Hatcher shows the same split on the page: an 'at the "
                              "well' royalty lets the operator deduct processing, treating, marketing and "
                              'transportation, while a cost-free royalty bars gathering, processing and '
                              'transportation deductions [b97Q2qy5uEo @ 00:10:30]. Tracy Lenz tracks the '
                              'rate history across recorded leases: 1/8 dominated in the 1980s and '
                              'earlier, then later paper in McMullen County, Texas reached 25% and a '
                              'Monroe County, Ohio addendum set 19% over the printed 12.5% [HGUBxgz_6Ak @ '
                              '00:06:39]. The Energy Law Professor does not dismiss the bonus entirely, '
                              'though. A zero or low bonus signals the company is not serious about '
                              "drilling, and the professor's worked example pairs a $1.5M bonus with a 25% "
                              'royalty for a $16.5M total to the owner [WBGDgooXnq8 @ 00:22:32]. '
                              'Consensus: negotiate rate and deductions first, then use the bonus as a '
                              'seriousness test on the operator.',
                              'Practitioners also agree that bargaining power is a function of acreage and '
                              'the pooling threat. Steven Hatcher splits owners into two classes: a '
                              'roughly 5,000-acre tract can command a 1/4 gross cost-free royalty, '
                              'top-of-market bonus, depth severance, a well commitment and possibly a '
                              'continuous drilling clause, while a 5-acre owner inside a 1,280-acre unit '
                              'has little leverage because the operator can force pool the tract or simply '
                              "exclude it [hZZNvuvGfkc @ 00:01:07]. The small owner's move is to benchmark "
                              'terms against neighbors rather than bluff. Alice Hog of the behoge13 '
                              'pooling webinar confirms the threat is real almost everywhere: 39 of 50 '
                              'states have forced pooling, aimed at unleased owners, unlocatable owners '
                              'and non-participating royalty interest owners, though Texas applies it '
                              "'very rarely' [le24nqd0H0M @ 00:28:31]. The Energy Law Professor explains "
                              'why Texas is different: the Mineral Interest Pooling Act only reaches '
                              'fields discovered after 1961, and the operator must exhaust voluntary '
                              "efforts and make 'fair and reasonable offers' before going to the Railroad "
                              'Commission [W5PjbHVyvWU @ 00:00:59]. The professor adds that fracking '
                              'flipped the incentives, so drillers are now the ones seeking force pooling '
                              '[W5PjbHVyvWU @ 00:11:45]. Net result: large tracts dictate terms, small '
                              'tracts price off the neighborhood.'],
               'table': {'caption': 'Where the practitioners line up on lease negotiation and owner '
                                    'leverage',
                         'headers': ['Consensus Point',
                                     'What the Practitioner Reports',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['There is no standard oil and gas lease',
                                   "The Producer's 88 form favors oil companies; landowner-friendly forms "
                                   'come from bank trusts and landowners associations',
                                   "Treat the landman's printed form as an opening offer, never the final "
                                   'document',
                                   'Energy Law Professor ([WBGDgooXnq8 @ 00:03:11])'],
                                  ["Never just sign the landman's form",
                                   "Leases can last 20, 30 or 50 years and the owner's kids may live with "
                                   'the document',
                                   'Negotiate every term before signing because the lease outlives the '
                                   'signer',
                                   'Steven Hatcher | Minerals Guy ([b97Q2qy5uEo @ 00:02:33])'],
                                  ['Royalty rate beats a bigger bonus',
                                   'Trading royalty rate for bonus is short-sighted because mineral value '
                                   'tracks the royalty rate directly',
                                   'Push for no post-production deductions or marketable-product language, '
                                   'especially in gas plays',
                                   'Matt Sands ([xiP5PiaaYKE @ 00:06:37])'],
                                  ['Cost-free royalty language blocks deductions',
                                   'An at-the-well royalty allows processing, treating, marketing and '
                                   'transportation deductions; cost-free bars GP&T',
                                   'Read the royalty clause and Exhibit A for deduction wording before '
                                   'accepting the rate',
                                   'Steven Hatcher | Minerals Guy ([b97Q2qy5uEo @ 00:10:30])'],
                                  ['A low bonus is a warning sign',
                                   'A zero or low bonus signals the company is not serious about drilling '
                                   'the acreage',
                                   'Use the bonus as a seriousness test even while prioritizing the '
                                   'royalty rate',
                                   'Energy Law Professor ([WBGDgooXnq8 @ 00:22:32])'],
                                  ['Acreage size determines bargaining leverage',
                                   'Around 5,000 acres earns a 1/4 gross cost-free royalty, top bonus, '
                                   'depth severance and a well commitment',
                                   'Large owners can demand terms while small owners benchmark against '
                                   'neighboring leases',
                                   'Steven Hatcher | Minerals Guy ([hZZNvuvGfkc @ 00:00:23])'],
                                  ['Forced pooling caps small-owner holdout power',
                                   '39 of 50 states have forced pooling targeting unleased, unlocatable '
                                   'and NPRI owners; Texas very rarely applies it',
                                   "Know your state's pooling regime before deciding whether to hold out",
                                   'behoge13 ([le24nqd0H0M @ 00:28:31])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["Execution starts with the recorded instrument. Steven Hatcher's workflow "
                              'pulls the lease and any assignments from county or parish records, then '
                              'reads it as who, what, when and how much: lessor and lessee in the first '
                              'paragraph, where an ancestor in title may appear as lessor, the land in '
                              'paragraph 2 and possibly Exhibit A, the habendum clause usually in the '
                              'third paragraph, and the royalty rate under how much. On term math, a lease '
                              'executed January 1, 2020 with a 3-year primary term expires January 1, 2023 '
                              'unless held, and paid-up leases carry no rentals [b97Q2qy5uEo @ 00:07:22]. '
                              "Alex Ottewell's field version: operators typically get about a 3-year "
                              'window to start drilling, production has to continue monthly, and after 90 '
                              'days without paying quantities the lease can be lost and the wells must be '
                              'plugged [VTx53sL4jRk @ 00:00:39]. The savings clauses get read literally. '
                              'The Energy Law Professor walks through Freeman v. Magnolia, where a late '
                              "shut-in payment terminated the lease because 'while royalty is so paid' "
                              'created a condition [7sPTlHr4F7A @ 00:03:56], and Rogers v. Osborne, where '
                              'a second well failed because the end-of-term sentence lacked the word '
                              "'additional,' making it only a well-completion clause [aPa6sCIUG-M @ "
                              '00:04:46].',
                              "The money math is simple enough to run on a napkin. Matt Sands' bonus rule "
                              'of thumb: a fair bonus is the mineral value divided by 2 or 3, so minerals '
                              'worth $3,000 per net mineral acre support a targeted bonus near $1,000 an '
                              'acre; on a Nacogdoches County Haynesville offer of $300 per NMA across 14.3 '
                              "net mineral acres, Sands says Mitsubishi's $8B purchase of Aethon's assets "
                              "will not move bonus rates, and Mitsubishi's capital spending is the real "
                              'question [xiP5PiaaYKE @ 00:06:17]. Alice Hog shows why pooled small tracts '
                              'disappoint: a 3/16 royalty (.1875) times a 5/40 tract share (.125) yields '
                              ".0234375, 'really 2% rather than 18%' [le24nqd0H0M @ 00:13:55]. On Texas "
                              'allocation wells, Sands computes the tract participation factor as '
                              'productive lateral length divided by total length, first take point to last '
                              'take point, so 5,000 feet of a 10,000-foot well is one half, then applies '
                              'net acres in the 640-acre half of a 1,280-acre unit times the royalty rate '
                              '[5Cx7zTkAJdw @ 00:14:23]. Lengths come off the permit plat and the '
                              "as-drilled plat at the Railroad Commission, a check that works '99% of the "
                              "time' [5Cx7zTkAJdw @ 00:17:06].",
                              'Two audits separate owners who get paid from owners who get diluted. '
                              'Michele Johnson of LMJ Land Services runs the Pugh clause check: an acreage '
                              'Pugh means the unit holds only land inside it, a depth Pugh holds only down '
                              'to a stated depth, often 100 feet below the deepest producing formation, '
                              "and 'a lease can be alive and still be much smaller than the lease form "
                              "says' [sLCs9xQypFE @ 00:00:40]. In the demo, an 80-acre lease on the S/2 "
                              'SE/4 of Section 59 has only 40 acres in the unit, so the other 40 may no '
                              'longer be held. The second audit is the force-pooling election. Alice Hog '
                              'lays out three options: pay a fair share of costs, take a 300% risk penalty '
                              'under which the operator recovers $18M of production on a $6M well before '
                              'payout, with reworks resetting it, or accept a deemed lease at $300 per '
                              'acre and 1/8, which becomes the default if the owner fails to elect '
                              "[le24nqd0H0M @ 00:35:49]. The Energy Law Professor's Carson case shows "
                              'where small owners win: an acreage-basis offer made only after drilling on '
                              "the owner's land, cutting a 1/8 royalty to 1/24, was not fair and "
                              "reasonable judged from the offeree's standpoint at the time of the offer "
                              '[W5PjbHVyvWU @ 00:07:12].'],
               'table': {'caption': 'Exact formulas, thresholds and dollar figures taught by the '
                                    'practitioners',
                         'headers': ['Mechanic',
                                     'Exact Number or Formula',
                                     'How the Practitioner Applies It',
                                     'Expert Source'],
                         'rows': [['Fair lease bonus benchmark',
                                   'Mineral value divided by 2 or 3; $3,000/NMA minerals supports about '
                                   '$1,000/acre',
                                   'Test any per-acre bonus offer against estimated mineral value before '
                                   'countering',
                                   'Matt Sands ([xiP5PiaaYKE @ 00:06:17])'],
                                  ['Allocation well tract participation factor',
                                   'Productive lateral length divided by total length, first take point to '
                                   'last take point',
                                   'Multiply the factor by net acres in the unit half and the royalty rate',
                                   'Matt Sands ([5Cx7zTkAJdw @ 00:14:23])'],
                                  ['Pooled small-tract royalty dilution',
                                   '3/16 times 5/40 equals .0234375, really 2% rather than 18%',
                                   'Convert the lease royalty into a unit decimal before valuing a pooled '
                                   'tract',
                                   'behoge13 ([le24nqd0H0M @ 00:13:55])'],
                                  ['Force-pooling risk penalty election',
                                   '300% penalty means $18M of production on a $6M well before payout',
                                   'Weigh the carried option against paying costs or taking the deemed '
                                   'lease',
                                   'behoge13 ([le24nqd0H0M @ 00:35:49])'],
                                  ['Default deemed lease for non-electing owners',
                                   '$300 per acre bonus and a 1/8 royalty if the owner fails to elect',
                                   'File the election on time or the agency default terms apply '
                                   'automatically',
                                   'behoge13 ([le24nqd0H0M @ 00:37:31])'],
                                  ['Depth Pugh clause cutoff',
                                   'Often 100 feet below the deepest producing formation in the unit',
                                   'Pull completion depths from Railroad Commission forms and map them '
                                   'against the lease',
                                   'LMJ Land Services ([sLCs9xQypFE @ 00:00:40])'],
                                  ['Continuous operations and cessation window',
                                   'No gap of more than 60 consecutive days in the sample clause',
                                   'Track operational gaps at the end of the primary term to spot a lapsed '
                                   'lease',
                                   'Energy Law Professor ([aPa6sCIUG-M @ 00:03:31])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'What the lease paper hides',
                           'body': 'Practitioners repeatedly found the real terms in strike-outs, addenda '
                                   'and clause wording that owners skim past.',
                           'items': ['On a post-1990 lease that shows 1/8, check for strike-outs and '
                                     'addenda; a 1998 Jim Wells County lease had 1/8 struck and replaced '
                                     "with 1/5, and a 2012 Ohio addendum's 19% overrode the printed 12.5% "
                                     '[Tracy Lenz — HGUBxgz_6Ak @ 00:22:21]',
                                     'A recorded memorandum of lease hides the terms; ask the operator or '
                                     'back-calculate the royalty from 3 of the 4 variables on the check '
                                     '[Tracy Lenz — HGUBxgz_6Ak @ 00:13:01]',
                                     'Compare competing offers through the Lease Price Report, discounted '
                                     'for NARO members, and the Mineral Rights Forum; county clerk records '
                                     'show royalty rates but a memorandum does not [Matt Sands — '
                                     'xiP5PiaaYKE @ 00:09:06]',
                                     "A 'gas well' or 'gas only' shut-in clause does not cover oil wells "
                                     "or low oil prices: 'If it's actually an oil well, no, you can't shut "
                                     "it in' [Energy Law Professor — 7sPTlHr4F7A @ 00:12:56]"]},
               'sop_steps': [{'step': 1,
                              'title': 'Pull the recorded paper',
                              'action': 'Retrieve the lease, assignments and any memorandum from county or '
                                        'parish records.',
                              'detail': 'Leases and their assignments are recorded in county or parish '
                                        'records; read who, what, when and how much, checking Exhibit A '
                                        'for the land description and royalty overrides [Steven Hatcher | '
                                        'Minerals Guy — b97Q2qy5uEo @ 00:03:23]'},
                             {'step': 2,
                              'title': 'Price the offer',
                              'action': 'Benchmark the bonus at mineral value divided by 2 or 3, then rank '
                                        'royalty rate and deduction language above the bonus.',
                              'detail': 'A $3,000/NMA mineral value targets about a $1,000/acre bonus, and '
                                        'giving up royalty rate for bonus is short-sighted because royalty '
                                        'rate drives every future check [Matt Sands — xiP5PiaaYKE @ '
                                        '00:06:17]'},
                             {'step': 3,
                              'title': 'Run your unit decimal',
                              'action': 'Convert gross acres to net acres, then apply tract share or tract '
                                        'participation factor and royalty rate.',
                              'detail': '160 gross acres at a 50% mineral interest equals 80 net acres; '
                                        'multiply by tract share and royalty to get the decimal the '
                                        'division order should show [behoge13 — le24nqd0H0M @ 00:17:46]'},
                             {'step': 4,
                              'title': 'Audit Pugh release and pooling elections',
                              'action': 'Map units and wells against the lease, pull completion depths, '
                                        'and file any force-pool election on time.',
                              'detail': 'Read every word of the Pugh clause, find its effective date, map '
                                        'units and wells, and pull completion depths from Railroad '
                                        'Commission forms; the deliverable is a Pugh column on the lease '
                                        'schedule [LMJ Land Services — sLCs9xQypFE @ 00:00:40]'}]},
              {'title': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split on lease economics is how hard to push bonus versus '
                              'royalty. Energy Law Professor models a $1.5M bonus stacked on a 25% royalty '
                              'for a $16.5M landowner take, and flags that a zero or low bonus signals the '
                              'company is not serious about drilling [WBGDgooXnq8 @ 00:22:32]. Matt Sands '
                              'comes at it from the other direction: target a bonus of roughly the mineral '
                              'value divided by 2 or 3, so $3,000 per net mineral acre in value points to '
                              'about $1,000 an acre in bonus, but never trade royalty rate away to fatten '
                              'that check [xiP5PiaaYKE @ 00:06:17]. Sands calls that swap short-sighted '
                              'because mineral value moves in direct proportion to the royalty rate, and '
                              'ranks no post-production deduction, marketable-product language as the '
                              'biggest single win, especially in gas plays [xiP5PiaaYKE @ 00:06:37]. '
                              'Steven Hatcher | Minerals Guy sets the ceiling for big blocks: on roughly '
                              '5,000 acres, a 1/4 gross, cost-free royalty is about as good as it gets, '
                              'paired with top-of-market bonus, depth severance, a well commitment, and '
                              'possibly a continuous drilling clause [hZZNvuvGfkc @ 00:00:23]. The '
                              'operator read: bonus is a seriousness signal and a one-time payday, while '
                              'royalty rate and deduction language compound for the life of the wells.',
                              'Leverage depends on tract size, and practitioners disagree on whether '
                              'holding out pays. Steven Hatcher | Minerals Guy says an 800lb gorilla can '
                              'sit tight and wait for the landman to come back, but a 5-acre owner inside '
                              'a 1,280-acre unit has little leverage because the operator can force pool '
                              'the tract or exclude it, so that owner should benchmark terms against '
                              'neighbors [hZZNvuvGfkc @ 00:01:50]. Energy Law Professor reads Texas law as '
                              'tilted toward the small owner: in Carson v. Railroad Commission, the Texas '
                              'Supreme Court judged fairness from the standpoint of the offeree at the '
                              'time of the offer, favored small tracts, and allowed more than an acreage '
                              'share [W5PjbHVyvWU @ 00:08:46]. Other states run zoning-like pooling with '
                              'no small-tract exception, which strips that edge away [W5PjbHVyvWU @ '
                              '00:12:47]. Alice Hog of behoge13 counts 39 of 50 states with force pooling, '
                              'notes Texas applies it very rarely, and flips the leasing math: an unleased '
                              'owner who stands in as the fourth working-interest owner gets 25% versus '
                              '18% as a lessor [le24nqd0H0M @ 00:38:59]. The alternative playbook is to '
                              'skip the lease entirely, but that only works for an owner who can carry '
                              'well costs or swallow the penalty that comes with being carried.',
                              'Where the royalty is measured is the next fault line. Steven Hatcher | '
                              'Minerals Guy separates at-the-well royalties, which let the lessee deduct '
                              'processing, treating, marketing, and transportation, from a cost-free '
                              'royalty that bars gathering, processing, and transportation deductions '
                              '[b97Q2qy5uEo @ 00:10:30]. Tracy Lenz shows the old-form version in a 1970 '
                              'Weld County, Colorado lease from Beaver Mesa: 1/8 at the mouth of the well, '
                              'with post-production costs applied [HGUBxgz_6Ak @ 00:08:05]. Energy Law '
                              'Professor shows that even the value base splits by state: in a 2001 Texas '
                              'case the contract price was $8 per mcf, market value was $2, and the '
                              'landowner got $2; Kansas, Montana, North Dakota, and West Virginia follow '
                              "that majority rule while Oklahoma's Tara (1981) sits in the minority "
                              '[dM8LufO_Emg @ 00:16:19]. The same professor maps a parallel split on what '
                              'holds a lease: Oklahoma lets capability of production hold it so the '
                              "shut-in payment is for the lessor's benefit, Louisiana keeps it alive "
                              'pending written notice, and Texas under Stanolind says capability alone '
                              'does not hold [7sPTlHr4F7A @ 00:09:00]. Read the state and the measuring '
                              'point together before comparing any two royalty rates.'],
               'table': {'caption': 'Contested lease and pooling playbooks, side by side',
                         'headers': ['Contested Question', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How much weight to put on bonus versus royalty',
                                   'Demand a real bonus because zero or low bonus signals no serious '
                                   'drilling intent',
                                   'Target value divided by 2 or 3 and never trade royalty rate for bonus',
                                   'Energy Law Professor ([WBGDgooXnq8 @ 00:22:32]) vs Matt Sands '
                                   '([xiP5PiaaYKE @ 00:06:37])'],
                                  ['Whether a holdout owner should wait out the landman',
                                   'An 800lb gorilla on a large block can wait for the landman to return',
                                   'Haynesville holdouts lost multi-million-dollar offers after '
                                   'delineation drilling proved acreage worthless',
                                   'Steven Hatcher | Minerals Guy ([hZZNvuvGfkc @ 00:01:50]) and Steven '
                                   'Hatcher | Minerals Guy ([hZZNvuvGfkc @ 00:02:04])'],
                                  ['Lease the tract or stay unleased under force pooling',
                                   'Lease for bonus plus royalty; the deemed-lease default pays $300 per '
                                   'acre and 1/8',
                                   'Stay unleased as fourth working-interest owner for 25% versus 18% as '
                                   'lessor',
                                   'behoge13 ([le24nqd0H0M @ 00:37:31]) and behoge13 ([le24nqd0H0M @ '
                                   '00:38:59])'],
                                  ['Whether small tracts get protection in compulsory pooling',
                                   'Texas Carson rule favors small tracts and allows more than an acreage '
                                   'share',
                                   'Other states run zoning-like pooling with no small-tract exception at '
                                   'all',
                                   'Energy Law Professor ([W5PjbHVyvWU @ 00:08:46]) and Energy Law '
                                   'Professor ([W5PjbHVyvWU @ 00:12:47])'],
                                  ['Where the royalty gets measured and what gets deducted',
                                   'At-the-well royalty lets lessee deduct processing, treating, '
                                   'marketing, and transportation costs',
                                   'Cost-free royalty bars gathering, processing, and transportation '
                                   'deductions from the owner check',
                                   'Steven Hatcher | Minerals Guy ([b97Q2qy5uEo @ 00:10:30]) and Tracy '
                                   'Lenz ([HGUBxgz_6Ak @ 00:08:05])'],
                                  ['Whether a capable but shut-in well holds the lease',
                                   'Oklahoma lets capability hold it; Louisiana continues pending written '
                                   'notice',
                                   'Texas under Stanolind says capability alone does not hold the lease',
                                   'Energy Law Professor ([7sPTlHr4F7A @ 00:09:00])'],
                                  ['How steep the risk penalty should be on carried owners',
                                   'Bennion v. ANR upheld no first-well penalty and 175% on the second '
                                   'well',
                                   'A 300% penalty is called quite common in commission-ordered pooling '
                                   'elections',
                                   'Energy Law Professor ([W5PjbHVyvWU @ 00:21:47]) and Energy Law '
                                   'Professor ([W5PjbHVyvWU @ 00:21:28])']]}},
              {'title': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['Termination traps are the costliest failures. Energy Law Professor walks '
                              'through Freeman v. Magnolia (Texas, 1943), where a late shut-in payment '
                              "killed the lease because the words 'while royalty is so paid' created a "
                              "condition, and a 'covenants aren't conditions' clause did not rescue the "
                              "lessee: 'because the royalty wasn't paid, that condition's not met, the "
                              "lease expires' [7sPTlHr4F7A @ 00:07:22]. The same professor warns that "
                              'gas-well or gas-only shut-in language does not cover oil wells or low oil '
                              "prices: 'If it's actually an oil well, no, you can't shut it in' "
                              '[7sPTlHr4F7A @ 00:12:56]. In Rogers v. Osborne (Texas 1953), a well that '
                              'never produced and was not a dry hole fell between both savings clauses, '
                              'could not carry shut-in royalty because it was not capable of production, '
                              'and the second well failed because the end-of-term sentence lacked the word '
                              "'additional'; the professor adds that courts read these clauses literally "
                              'and harshly [aPa6sCIUG-M @ 00:04:46]. Alex Ottewell puts the field version '
                              'bluntly: production must continue monthly, and after 90 days without paying '
                              'quantities the lease can be lost and the wells must be plugged [VTx53sL4jRk '
                              '@ 00:00:39]. Check the calendar before the lessee does.',
                              'Pooling arithmetic burns owners who read only the royalty fraction. Alice '
                              'Hog of behoge13 runs it: a 3/16 royalty (.1875) times a 5/40 tract share '
                              "(.125) yields .0234375, 'really 2% rather than 18%' [le24nqd0H0M @ "
                              '00:13:55]. Hog also flags how pooling breaks: in Amoco v. Underwood (1977), '
                              'carving a sliver of a 2,252-acre lease into a 643-acre unit was bad faith, '
                              'a lease without a pooling clause does not hold, and when Sunoco pooled for '
                              'gas and found oil the lease was not held [le24nqd0H0M @ 00:24:00]. The '
                              'force-pooled owner who sits on the election paper gets the default, a '
                              'deemed lease at $300 per acre and 1/8, while choosing to be carried means a '
                              '300% penalty, $18M of production on a $6M well before payout, with reworks '
                              'resetting the clock [le24nqd0H0M @ 00:37:31]. Michele Johnson of LMJ Land '
                              'Services catches the reverse trap in acquisitions: a Pugh clause limits '
                              'what a well or unit can hold, so lease three covering the S/2 SE/4 of '
                              'Section 59, 80 acres, may keep only the 40 acres inside the unit, because '
                              "'a lease can be alive and still be much smaller than the lease form says' "
                              '[sLCs9xQypFE @ 00:00:40]. Buyers assuming the whole lease is held are '
                              'pricing acreage that may already be released.',
                              'Paper traps and outright scams round out the failures. Steven Hatcher | '
                              "Minerals Guy warns against just signing the landman's form because leases "
                              'can run 20, 30, or 50 years and your kids may live with the document '
                              '[b97Q2qy5uEo @ 00:02:33]. Tracy Lenz shows why the paper matters: a 1999 '
                              'memorandum of lease hides the terms, a 2012 Monroe County, Ohio addendum at '
                              '19% overrides the printed 12.5%, and any post-1990 lease showing 1/8 needs '
                              'a check for strike-outs and addenda [HGUBxgz_6Ak @ 00:22:21]. Matt Sands '
                              'fields a caller whose number traced to a hospital and warns of fake term '
                              'royalty deeds that convey all future royalties just before wells are '
                              'drilled, at cents on the dollar, such as $3,000 offered against $50 a year '
                              "in checks: 'if it seems too good to be true, it probably is' [xiP5PiaaYKE @ "
                              '00:12:49]. On the operator side, Sands describes a landman fraud case where '
                              "the operator kept title to elderly investors' interests and paid only "
                              'distribution reports; the fix was a litigator rather than a general oil and '
                              'gas attorney, often on contingency at a 30% cut of recovered damages, with '
                              "'trust but verify' as the standing rule [5Cx7zTkAJdw @ 00:11:11]. Every one "
                              'of these losses started with paper nobody pulled and read.'],
               'table': {'caption': 'Firsthand traps, the mechanism that bit, and the economics check',
                         'headers': ['Trap', 'What Went Wrong', 'Economics Check', 'Expert Source'],
                         'rows': [['Late shut-in royalty payment on a Texas lease',
                                   "'While royalty is so paid' made payment a condition and the lease "
                                   'expired',
                                   'Calendar every annual shut-in payment date and confirm the payment '
                                   'actually posted',
                                   'Energy Law Professor ([7sPTlHr4F7A @ 00:03:56])'],
                                  ["End-of-term operations sentence missing the word 'additional'",
                                   'Rogers v. Osborne second well failed because the clause covered only '
                                   'well completion',
                                   'Read savings clauses literally because courts read them literally and '
                                   'harshly',
                                   'Energy Law Professor ([aPa6sCIUG-M @ 00:04:46])'],
                                  ['Gas-only shut-in clause applied to an oil well',
                                   'Shut-in language does not cover oil wells or periods of low oil prices',
                                   'Confirm whether the clause says gas well or gas only before relying on '
                                   'it',
                                   'Energy Law Professor ([7sPTlHr4F7A @ 00:12:56])'],
                                  ['Reading the royalty fraction as the actual pooled payout',
                                   '3/16 times 5/40 equals .0234375, really 2% rather than 18% of '
                                   'production',
                                   'Multiply royalty rate by tract share before valuing any pooled '
                                   'interest',
                                   'behoge13 ([le24nqd0H0M @ 00:13:55])'],
                                  ['Ignoring the force-pooling election deadline entirely',
                                   'Failure to elect defaults the owner into a deemed lease at $300 per '
                                   'acre and 1/8',
                                   'Compare participation, the 300% carried penalty, and the deemed lease '
                                   'before the deadline',
                                   'behoge13 ([le24nqd0H0M @ 00:37:31])'],
                                  ['Assuming one unit holds the entire leased tract',
                                   'Pugh clause left 40 of 80 acres in S/2 SE/4 of Section 59 possibly '
                                   'unheld',
                                   'Map units and wells against the lease and pull completion depths from '
                                   'Railroad Commission forms',
                                   'LMJ Land Services ([sLCs9xQypFE @ 00:01:04])'],
                                  ['Selling to an unsolicited term royalty deed buyer',
                                   'Fake deeds convey all future royalties just before drilling at cents '
                                   'on the dollar',
                                   'Weigh $3,000 offered against $50 a year in checks only after pulling '
                                   'deeds and leases',
                                   'Matt Sands ([xiP5PiaaYKE @ 00:15:00])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before the lease, the election, or the sale',
                           'body': 'Each gate below maps to a loss a practitioner watched happen: a lease '
                                   'expiring on a late payment, a pooled decimal far below the headline '
                                   'fraction, a default election, and a cents-on-the-dollar deed.',
                           'items': ['Confirm every shut-in royalty payment lands on time, because a late '
                                     "payment under 'while royalty is so paid' language terminated the "
                                     'lease in Freeman v. Magnolia [Energy Law Professor — 7sPTlHr4F7A @ '
                                     '00:07:22].',
                                     'Run royalty rate times tract share before valuing a pooled interest; '
                                     '3/16 on a 5/40 tract is really 2% rather than 18% [behoge13 — '
                                     'le24nqd0H0M @ 00:13:55].',
                                     'Make the force-pooling election in writing before the deadline, or '
                                     'default into a deemed lease at $300 per acre and 1/8 [behoge13 — '
                                     'le24nqd0H0M @ 00:37:31].',
                                     'Pull deeds, leases, and assignments before answering any unsolicited '
                                     'term royalty deed offer, since these convey all future royalties '
                                     'just before drilling at cents on the dollar [Matt Sands — '
                                     'xiP5PiaaYKE @ 00:12:49].']}}],
 'pull_quote': '"So, a lease can be alive and still be much smaller than the lease form says." Michele '
               'Johnson, LMJ Land Services (sLCs9xQypFE @ 00:00:40).',
 'diagram_id': 'diag-03',
 'action_checklist': ['Pull the base lease and every recorded assignment from county or parish records, '
                      'then read the granting, habendum, and royalty paragraphs before signing anything '
                      '[Steven Hatcher | Minerals Guy — b97Q2qy5uEo @ 00:03:23].',
                      'Set the target bonus at mineral value divided by 2 or 3 and refuse to trade royalty '
                      'rate for a bigger bonus check [Matt Sands — xiP5PiaaYKE @ 00:06:17].',
                      'Benchmark the offer against the Lease Price Report, the Mineral Rights Forum, and '
                      'county clerk records, knowing a recorded memorandum of lease will not show the '
                      'royalty rate [Matt Sands — xiP5PiaaYKE @ 00:09:06].',
                      'Verify an allocation-well decimal by dividing your productive lateral length by '
                      'total length, first take point to last take point, using the permit plat and '
                      'as-drilled plat [Matt Sands — 5Cx7zTkAJdw @ 00:17:06].',
                      'Build a Pugh column on the lease schedule: read every word of the clause, find its '
                      'effective date, map units and wells, and pull completion depths [LMJ Land Services '
                      '— sLCs9xQypFE @ 00:00:40].',
                      'When force pooled, choose between paying a fair share of costs, a 300% carried '
                      'penalty, or the deemed lease before the default election kicks in [behoge13 — '
                      'le24nqd0H0M @ 00:35:49].'],
 'statutory_citations': [{'title': 'behoge13 — Pooling & Unitization Webinar [00:35:49]',
                          'url': 'https://www.youtube.com/watch?v=le24nqd0H0M&t=2149s',
                          'relevance': 'Primary practitioner testimony on force-pooled owner elections, '
                                       'the 300% carried penalty, and the deemed-lease default.'},
                         {'title': 'Energy Law Professor — Oil & Gas 06: Intro to Pooling [00:07:12]',
                          'url': 'https://www.youtube.com/watch?v=W5PjbHVyvWU&t=432s',
                          'relevance': 'Primary practitioner testimony on the Carson fair-and-reasonable '
                                       'offer standard and small-tract owner leverage.'},
                         {'title': 'Matt Sands — MRP 328:  Listener Questions April 2026 [00:06:17]',
                          'url': 'https://www.youtube.com/watch?v=xiP5PiaaYKE&t=377s',
                          'relevance': 'Primary practitioner testimony on bonus pricing at value divided '
                                       'by 2 or 3 and holding royalty rate over bonus.'},
                         {'title': 'LMJ Land Services — The Pugh Clause in an Acquisition | LMJ Chalk Talk '
                                   '[00:00:40]',
                          'url': 'https://www.youtube.com/watch?v=sLCs9xQypFE&t=40s',
                          'relevance': 'Primary practitioner testimony on Pugh clause review and acreage '
                                       'released outside a pooled unit.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '5Cx7zTkAJdw',
                       'title': 'MRP 358: Listener Questions November 2026',
                       'channel': 'Matt Sands',
                       'author': 'Matt Sands',
                       'text': 'And in Texas, you do have to sign and return that division order in order '
                               'to get paid royalties.',
                       'tip': 'And in Texas, you do have to sign and return that division order in order '
                              'to get paid royalties.',
                       'timestamp': 412,
                       'timestamp_seconds': 412,
                       'timestamp_label': '[00:06:52]',
                       'url': 'https://www.youtube.com/watch?v=5Cx7zTkAJdw&t=412s',
                       'markdown': '[00:06:52](https://www.youtube.com/watch?v=5Cx7zTkAJdw&t=412s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5Cx7zTkAJdw',
                       'title': 'MRP 358: Listener Questions November 2026',
                       'channel': 'Matt Sands',
                       'author': 'Matt Sands',
                       'text': 'They might be able to do it on a contingency fee basis.',
                       'tip': 'They might be able to do it on a contingency fee basis.',
                       'timestamp': 671,
                       'timestamp_seconds': 671,
                       'timestamp_label': '[00:11:11]',
                       'url': 'https://www.youtube.com/watch?v=5Cx7zTkAJdw&t=671s',
                       'markdown': '[00:11:11](https://www.youtube.com/watch?v=5Cx7zTkAJdw&t=671s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WBGDgooXnq8',
                       'title': 'Oil & Gas 09A: Intro to the Oil & Gas Lease',
                       'channel': 'Energy Law Professor',
                       'author': 'Energy Law Professor',
                       'text': 'A $1.5M bonus plus a 25% royalty yields $16.5M, and a zero or low bonus '
                               'signals the company is not serious about drilling.',
                       'tip': 'A $1.5M bonus plus a 25% royalty yields $16.5M, and a zero or low bonus '
                              'signals the company is not serious about drilling.',
                       'timestamp': 1352,
                       'timestamp_seconds': 1352,
                       'timestamp_label': '[00:22:32]',
                       'url': 'https://www.youtube.com/watch?v=WBGDgooXnq8&t=1352s',
                       'markdown': '[00:22:32](https://www.youtube.com/watch?v=WBGDgooXnq8&t=1352s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'b97Q2qy5uEo',
                       'title': 'Mineral Rights Management 101: EP 3 | 4 Questions About Your Oil & Gas '
                                'Lease',
                       'channel': 'Steven Hatcher | Minerals Guy',
                       'author': 'Steven Hatcher | Minerals Guy',
                       'text': "Do not just sign the landman's form, because leases can last 20, 30, or 50 "
                               'years and your kids may live with the document.',
                       'tip': "Do not just sign the landman's form, because leases can last 20, 30, or 50 "
                              'years and your kids may live with the document.',
                       'timestamp': 153,
                       'timestamp_seconds': 153,
                       'timestamp_label': '[00:02:33]',
                       'url': 'https://www.youtube.com/watch?v=b97Q2qy5uEo&t=153s',
                       'markdown': '[00:02:33](https://www.youtube.com/watch?v=b97Q2qy5uEo&t=153s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7sPTlHr4F7A',
                       'title': 'Oil & Gas 12A: Constructive Production & Shut-In Royalties',
                       'channel': 'Energy Law Professor',
                       'author': 'Energy Law Professor',
                       'text': "And so because the royalty wasn't paid, that condition's not met, the "
                               'lease expires.',
                       'tip': "And so because the royalty wasn't paid, that condition's not met, the lease "
                              'expires.',
                       'timestamp': 442,
                       'timestamp_seconds': 442,
                       'timestamp_label': '[00:07:22]',
                       'url': 'https://www.youtube.com/watch?v=7sPTlHr4F7A&t=442s',
                       'markdown': '[00:07:22](https://www.youtube.com/watch?v=7sPTlHr4F7A&t=442s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dM8LufO_Emg',
                       'title': 'Introduction to Royalties (Oil & Gas 14.1)',
                       'channel': 'Energy Law Professor',
                       'author': 'Energy Law Professor',
                       'text': 'Oil royalty paid in kind keeps the oil and gas company honest, though '
                               'division orders usually convert it to proceeds.',
                       'tip': 'Oil royalty paid in kind keeps the oil and gas company honest, though '
                              'division orders usually convert it to proceeds.',
                       'timestamp': 308,
                       'timestamp_seconds': 308,
                       'timestamp_label': '[00:05:08]',
                       'url': 'https://www.youtube.com/watch?v=dM8LufO_Emg&t=308s',
                       'markdown': '[00:05:08](https://www.youtube.com/watch?v=dM8LufO_Emg&t=308s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hZZNvuvGfkc',
                       'title': 'Landman vs. Landowner: Who Really Has the Power?',
                       'channel': 'Steven Hatcher | Minerals Guy',
                       'author': 'Steven Hatcher | Minerals Guy',
                       'text': 'Haynesville holdouts lost multi-million-dollar offers after delineation '
                               "drilling proved their acreage worthless, so don't cut your nose off to "
                               'spite your face.',
                       'tip': 'Haynesville holdouts lost multi-million-dollar offers after delineation '
                              "drilling proved their acreage worthless, so don't cut your nose off to "
                              'spite your face.',
                       'timestamp': 124,
                       'timestamp_seconds': 124,
                       'timestamp_label': '[00:02:04]',
                       'url': 'https://www.youtube.com/watch?v=hZZNvuvGfkc&t=124s',
                       'markdown': '[00:02:04](https://www.youtube.com/watch?v=hZZNvuvGfkc&t=124s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'W5PjbHVyvWU',
                       'title': 'Oil & Gas 06: Intro to Pooling',
                       'channel': 'Energy Law Professor',
                       'author': 'Energy Law Professor',
                       'text': 'A pooling offer is judged fair and reasonable from the standpoint of the '
                               'offeree at the time of the offer, with good-faith negotiation required of '
                               'both sides.',
                       'tip': 'A pooling offer is judged fair and reasonable from the standpoint of the '
                              'offeree at the time of the offer, with good-faith negotiation required of '
                              'both sides.',
                       'timestamp': 432,
                       'timestamp_seconds': 432,
                       'timestamp_label': '[00:07:12]',
                       'url': 'https://www.youtube.com/watch?v=W5PjbHVyvWU&t=432s',
                       'markdown': '[00:07:12](https://www.youtube.com/watch?v=W5PjbHVyvWU&t=432s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'le24nqd0H0M',
                       'title': 'Pooling & Unitization Webinar',
                       'channel': 'behoge13',
                       'author': 'behoge13',
                       'text': 'A 3/16 royalty times a 5/40 tract share comes to .0234375, which is really '
                               '2% rather than 18%.',
                       'tip': 'A 3/16 royalty times a 5/40 tract share comes to .0234375, which is really '
                              '2% rather than 18%.',
                       'timestamp': 835,
                       'timestamp_seconds': 835,
                       'timestamp_label': '[00:13:55]',
                       'url': 'https://www.youtube.com/watch?v=le24nqd0H0M&t=835s',
                       'markdown': '[00:13:55](https://www.youtube.com/watch?v=le24nqd0H0M&t=835s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'le24nqd0H0M',
                       'title': 'Pooling & Unitization Webinar',
                       'channel': 'behoge13',
                       'author': 'behoge13',
                       'text': 'A force-pooled owner who takes the 300% penalty sees $18M of production on '
                               'a $6M well before payout, and reworks reset it.',
                       'tip': 'A force-pooled owner who takes the 300% penalty sees $18M of production on '
                              'a $6M well before payout, and reworks reset it.',
                       'timestamp': 2149,
                       'timestamp_seconds': 2149,
                       'timestamp_label': '[00:35:49]',
                       'url': 'https://www.youtube.com/watch?v=le24nqd0H0M&t=2149s',
                       'markdown': '[00:35:49](https://www.youtube.com/watch?v=le24nqd0H0M&t=2149s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'aPa6sCIUG-M',
                       'title': 'Cessation, Dry Hole, & Continuous Operations Clauses (Oil & Gas 12.2)',
                       'channel': 'Energy Law Professor',
                       'author': 'Energy Law Professor',
                       'text': "So the lease doesn't immediately terminate because production ceases.",
                       'tip': "So the lease doesn't immediately terminate because production ceases.",
                       'timestamp': 83,
                       'timestamp_seconds': 83,
                       'timestamp_label': '[00:01:23]',
                       'url': 'https://www.youtube.com/watch?v=aPa6sCIUG-M&t=83s',
                       'markdown': '[00:01:23](https://www.youtube.com/watch?v=aPa6sCIUG-M&t=83s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sLCs9xQypFE',
                       'title': 'The Pugh Clause in an Acquisition | LMJ Chalk Talk',
                       'channel': 'LMJ Land Services',
                       'author': 'LMJ Land Services',
                       'text': 'So, a lease can be alive and still be much smaller than the lease form '
                               'says.',
                       'tip': 'So, a lease can be alive and still be much smaller than the lease form '
                              'says.',
                       'timestamp': 40,
                       'timestamp_seconds': 40,
                       'timestamp_label': '[00:00:40]',
                       'url': 'https://www.youtube.com/watch?v=sLCs9xQypFE&t=40s',
                       'markdown': '[00:00:40](https://www.youtube.com/watch?v=sLCs9xQypFE&t=40s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XvpPKXAYhlQ',
                       'title': 'Oil and Gas Leases by Mark Sokolow',
                       'channel': 'Tips from Mark Sokolow',
                       'author': 'Tips from Mark Sokolow',
                       'text': 'Under the most-favored clause the city gets the greater of its own rate or '
                               "any other owner's rate, and the highest was $300 per net mineral acre per "
                               'year.',
                       'tip': 'Under the most-favored clause the city gets the greater of its own rate or '
                              "any other owner's rate, and the highest was $300 per net mineral acre per "
                              'year.',
                       'timestamp': 226,
                       'timestamp_seconds': 226,
                       'timestamp_label': '[00:03:46]',
                       'url': 'https://www.youtube.com/watch?v=XvpPKXAYhlQ&t=226s',
                       'markdown': '[00:03:46](https://www.youtube.com/watch?v=XvpPKXAYhlQ&t=226s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'USmNwOWurpk',
                       'title': 'Oil & Gas 09B: The Granting Clause',
                       'channel': 'Energy Law Professor',
                       'author': 'Energy Law Professor',
                       'text': 'Under the obstruction doctrine, six months of exclusion or denying title '
                               'may extend the primary term.',
                       'tip': 'Under the obstruction doctrine, six months of exclusion or denying title '
                              'may extend the primary term.',
                       'timestamp': 574,
                       'timestamp_seconds': 574,
                       'timestamp_label': '[00:09:34]',
                       'url': 'https://www.youtube.com/watch?v=USmNwOWurpk&t=574s',
                       'markdown': '[00:09:34](https://www.youtube.com/watch?v=USmNwOWurpk&t=574s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'DcdI-1zyjQo',
                       'title': 'Mineral Rights Management 101 | How to Manage Your Mineral Rights Like '
                                "the Pro's",
                       'channel': 'Steven Hatcher | Minerals Guy',
                       'author': 'Steven Hatcher | Minerals Guy',
                       'text': 'You have to know what you own, otherwise you are flying blind.',
                       'tip': 'You have to know what you own, otherwise you are flying blind.',
                       'timestamp': 141,
                       'timestamp_seconds': 141,
                       'timestamp_label': '[00:02:21]',
                       'url': 'https://www.youtube.com/watch?v=DcdI-1zyjQo&t=141s',
                       'markdown': '[00:02:21](https://www.youtube.com/watch?v=DcdI-1zyjQo&t=141s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HGUBxgz_6Ak',
                       'title': "Oil & Gas Lease Royalties: Beginner's Guide for Mineral Owners (with "
                                'examples!)',
                       'channel': 'Tracy Lenz',
                       'author': 'Tracy Lenz',
                       'text': "Usually if it's 1980s or earlier, it's one eighth.",
                       'tip': "Usually if it's 1980s or earlier, it's one eighth.",
                       'timestamp': 399,
                       'timestamp_seconds': 399,
                       'timestamp_label': '[00:06:39]',
                       'url': 'https://www.youtube.com/watch?v=HGUBxgz_6Ak&t=399s',
                       'markdown': '[00:06:39](https://www.youtube.com/watch?v=HGUBxgz_6Ak&t=399s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'VTx53sL4jRk',
                       'title': 'How does an oil and gas lease work?',
                       'channel': 'Alex Ottewell',
                       'author': 'Alex Ottewell',
                       'text': "Once they've got that lease in place, they're typically given a 3-year "
                               'period to start drilling.',
                       'tip': "Once they've got that lease in place, they're typically given a 3-year "
                              'period to start drilling.',
                       'timestamp': 13,
                       'timestamp_seconds': 13,
                       'timestamp_label': '[00:00:13]',
                       'url': 'https://www.youtube.com/watch?v=VTx53sL4jRk&t=13s',
                       'markdown': '[00:00:13](https://www.youtube.com/watch?v=VTx53sL4jRk&t=13s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xiP5PiaaYKE',
                       'title': 'MRP 328:  Listener Questions April 2026',
                       'channel': 'Matt Sands',
                       'author': 'Matt Sands',
                       'text': 'And the reason for that is because that royalty rate will determine the '
                               'amount of royalties you get paid in the future.',
                       'tip': 'And the reason for that is because that royalty rate will determine the '
                              'amount of royalties you get paid in the future.',
                       'timestamp': 484,
                       'timestamp_seconds': 484,
                       'timestamp_label': '[00:08:04]',
                       'url': 'https://www.youtube.com/watch?v=xiP5PiaaYKE&t=484s',
                       'markdown': '[00:08:04](https://www.youtube.com/watch?v=xiP5PiaaYKE&t=484s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'}]}
