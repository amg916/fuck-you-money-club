from __future__ import annotations

CHAPTER_1 = {'id': 'Q1',
 'chapter_id': 'Q1',
 'chapter_number': 1,
 'question_number': 1,
 'slug': 'funding-architecture-fully-insured-self-funded-level-funded',
 'question_prompt': 'How do fully insured, self-funded, and level-funded health plans actually differ in '
                    "how an employer's premium dollars flow, who carries the risk, and where the savings "
                    'come from?',
 'kicker': 'Q1 / THE BIG MONEY PLAYBOOKS',
 'title': 'Fully Insured vs. Self-Funded vs. Level-Funded: The Funding Architecture',
 'subtitle': 'Premium mechanics, claims funds, fixed admin costs, surplus refunds, and why double-digit '
             'renewals push small and mid-size employers off fully insured plans',
 'layout_template': 'opportunity_overview',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners across benefits brokerages, stop-loss carriers and healthcare finance '
                      'channels converge on one architecture map: fully insured is guaranteed cost where '
                      'the carrier keeps every unspent claims dollar, self-funded is pay-as-you-go with '
                      'stop-loss backstops, and level-funded is the hybrid that bills a fixed monthly '
                      'amount split into admin, stop-loss and a claims fund with surplus refunds. Street '
                      'numbers include 60-70% of self-funded spend landing in claims, carriers loading '
                      'level-funded rates roughly 25% above expected cost, surplus splits of 50-80%, and '
                      'level-funded penetration jumping from 10% to 45% of lives in 50-500 employee '
                      'groups. Disagreements center on where the size cutoffs sit (25, 30, 45, 100 lives), '
                      'whether carriers quietly keep level-funded surpluses, and how hard medical '
                      'underwriting, lasers and renewal spikes bite after a bad claims year.',
 'key_metrics': [{'label': 'Level-Funded Share of Lives in 50-500 Employee Groups',
                  'metric': 'Level-Funded Share of Lives in 50-500 Employee Groups',
                  'value': 'About 10% ten years ago to 45% today',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Dr. Eric Bricker describes level funding as having more than quadrupled in '
                             'the mid-market, concentrated in the Midwest and South.',
                  'source': 'AHealthcareZ - Healthcare Finance Explained ([wshiRRBh4Gs @ 00:05:06])'},
                 {'label': 'Level-Funded Surplus Refund Split',
                  'metric': 'Level-Funded Surplus Refund Split',
                  'value': '50% to 80% of the leftover claims fund',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Share of an unused claims fund returned as cash or lower next-year rates, '
                             'depending on the specific contract.',
                  'source': 'Tyler Dutchover ([ExcUj28jzzc @ 00:03:47])'},
                 {'label': 'Carrier Load on Level-Funded Premium',
                  'metric': 'Carrier Load on Level-Funded Premium',
                  'value': 'About 25% above expected cost',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Matt Roy says carriers price admin, ISL, ASL and claims, then usually charge '
                             'about 25% more and present one flat number.',
                  'source': 'Blue Ocean Benefits & Consulting ([D23XjGg7o_g @ 00:05:15])'},
                 {'label': 'Self-Funded Plan Spend Going to Claims',
                  'metric': 'Self-Funded Plan Spend Going to Claims',
                  'value': '60% to 70% of total plan spend',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Spencer Smith's estimate for small to midsize self-funded employers; fixed "
                             'costs drop to roughly 25% to 30% of budget.',
                  'source': 'Self-Funded ([VPeObJ32l7M @ 00:01:40])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner starts from the same baseline: fully insured is a '
                              'guaranteed-cost product where the carrier owns the upside. Spencer Smith of '
                              'Self-Funded frames it as prepaid cost, with the carrier projecting claims, '
                              'calculating administrative charges, collecting taxes and baking its desired '
                              'profit margin into one premium, so the employer spends that full amount no '
                              'matter what happens in the claims bucket unless enrollment drops '
                              'significantly [VPeObJ32l7M @ 00:00:49]. Matt Roy of Blue Ocean Benefits & '
                              'Consulting puts it bluntly: you pay a premium, 100% of it goes to the '
                              'carrier, and the carrier keeps it regardless of what the claims are '
                              '[D23XjGg7o_g @ 00:00:58]. Tyler Dutchover runs the street version of that '
                              'math: a business paying $300,000 in premium whose young workforce only '
                              'burns $100,000 of care watches the carrier keep every penny of the $200,000 '
                              'difference, gets no refund or thank-you, and then gets higher rates the '
                              'next year [ExcUj28jzzc @ 00:01:16]. Brian Calvert of Health Insurance '
                              "Doesn't Have to Suck sums up the trade as maximum predictability, maximum "
                              'cost, noting the model works as a starting point under 50 employees but '
                              'starts leaving money on the table as a group gets larger and more stable '
                              '[y9n2wYoPMYw @ 00:01:46].',
                              'The second point of consensus is what level funding actually is under the '
                              'hood. Dr. Eric Bricker of AHealthcareZ calls it a crossbreed: a fixed '
                              'monthly premium to the carrier, like fully insured, that funds claims plus '
                              'stop-loss insurance plus an administrative fee plus the PBM, with a refund '
                              'or credit possible if claims come in low and stop-loss covering the year if '
                              'claims run hot [wshiRRBh4Gs @ 00:00:20]. Tyler Dutchover and Brian Calvert '
                              'describe the identical three-bucket split, admin fee, stop-loss premium and '
                              'a claims fund that pays everyday doctor visits and prescriptions, with '
                              'leftover money coming back as a refund or credit [ExcUj28jzzc @ 00:02:16] '
                              '[y9n2wYoPMYw @ 00:04:06]. The practitioners also agree that self-funding is '
                              'less of a cliff than its name suggests. Matt Roy repeats a line from an old '
                              'rep that a self-funded plan is really a fully reinsured self-funded plan, '
                              'because individual and aggregate stop-loss cap exposure, and only very big '
                              'companies take 100% of the risk, something Roy says you will not see under '
                              'a thousand lives [D23XjGg7o_g @ 00:00:30]. That shared stop-loss floor is '
                              'why most speakers treat the three models as points on one dial, trading '
                              'predictability against how much unspent claims money the employer keeps.',
                              'Speakers also line up on who belongs in which model, and the real dividing '
                              'line is claims risk. Bricker says the number one driver of claims is age, '
                              'so young groups sitting in fully insured should generally go level funded, '
                              'while older, high-claims groups are left holding the bag; brokers now '
                              'describe the fully insured market as essentially a high-risk pool, and '
                              "Bricker warns that if you don't know who the sucker at the poker table is, "
                              "it's probably you [wshiRRBh4Gs @ 00:08:05]. Tyler Dutchover calls the same "
                              'dynamic a death spiral, healthy groups exit, the community pool gets '
                              'sicker, rates rise again, and points to Connecticut as a place where it has '
                              'already happened [m5BLhBDIZZ4 @ 00:07:13]. Olivia of Allstate Benefits adds '
                              'that four out of five years groups perform better than expected, so the '
                              'self-funded or level-funded employer reaps that margin instead of the fully '
                              'insured carrier, which also hands the group very little data on providers, '
                              'claims spend or drug usage [hqPZ5l67B4A @ 00:05:35]. Jennifer Shafer of JS '
                              'Benefits Group turns that into the baseline prerequisite: the question is '
                              "not whether level funding is cheaper but whether it fits the group's "
                              'demographics, claims history and risk profile [qE34fv4L2qU @ 00:01:13].'],
               'table': {'caption': 'The three funding architectures as the practitioners define them',
                         'headers': ['Funding Model',
                                     'How the Money Flows',
                                     'Who Keeps Unspent Claims Dollars',
                                     'Expert Source'],
                         'rows': [['Fully insured as guaranteed, prepaid cost',
                                   'Carrier bakes projected claims, administrative charges, taxes and its '
                                   'desired profit margin into one premium',
                                   'Carrier keeps every unspent dollar; employer pays full premium unless '
                                   'enrollment drops significantly',
                                   'Self-Funded ([VPeObJ32l7M @ 00:01:06])'],
                                  ['Where one fully insured dollar goes',
                                   'About 2 cents premium tax, about 5 cents commission, a carrier '
                                   'retention slice, 70 to 75 cents claims',
                                   'Retention stays with the carrier, a shell game the speaker says can '
                                   'hide kickbacks',
                                   'Self Insured Reporting ([5PxkF9WUCd0 @ 00:01:28])'],
                                  ['Level funded as a carrier-built hybrid',
                                   'Fixed monthly premium pays claims, stop-loss insurance, an '
                                   "administrative fee and the carrier's own PBM",
                                   'Low-claims year may earn a credit or refund, but the carrier makes '
                                   'that call',
                                   'AHealthcareZ - Healthcare Finance Explained ([wshiRRBh4Gs @ '
                                   '00:01:54])'],
                                  ['Level funded three-bucket payment split',
                                   'Admin fee to the third-party administrator, stop-loss premium, and a '
                                   'claims fund belonging to the plan',
                                   'Leftover claims fund is split, 50 to 80% back as cash or lower rates',
                                   'Tyler Dutchover ([ExcUj28jzzc @ 00:03:47])'],
                                  ['Traditional self-funded, pay as you go',
                                   'Employer pays admin fees and stop-loss premium, then pays claims only '
                                   'as they actually occur',
                                   'Claims that never happen never leave the bank account, so the employer '
                                   'keeps the savings',
                                   'The Difference Card ([iT4htd_Aqag @ 00:01:24])'],
                                  ['Self-funded reinsurance layer under 1,000 lives',
                                   "Individual stop-loss caps any one member's claims; aggregate stop-loss "
                                   'caps the pile-up of smaller claims',
                                   'Nobody under a thousand lives runs 100% self-funded; it is a fully '
                                   'reinsured plan',
                                   'Blue Ocean Benefits & Consulting ([D23XjGg7o_g @ 00:01:15])'],
                                  ['Headcount fit across all three models',
                                   'Under 10 employees fully insured, 10 or 15 to 100 level funded, over '
                                   '100 self-funded',
                                   'Larger groups with stable claims history can absorb volatility and '
                                   'keep the savings upside',
                                   "Health Insurance Doesn't Have to Suck ([y9n2wYoPMYw @ 00:06:49])"]]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The level-funded rate is built, not guessed, and the speakers expose the '
                              'formula. Matt Roy says the carrier calculates what it needs for admin, '
                              'individual stop-loss, aggregate stop-loss and claims, then usually charges '
                              'about 25% more than it expects the plan to cost and hands over one flat '
                              'number that looks like a fully insured premium, with some or all of the '
                              'overage split back at year end depending on the contract [D23XjGg7o_g @ '
                              '00:05:15]. Olivia of Allstate Benefits mirrors that figure from the '
                              'stop-loss side: the aggregate is set around 125% of expected claims, spread '
                              'over 12 months, and if a major claim hits in January before the fund is '
                              'built, Allstate advances the money and recoups it as the fund fills '
                              "[hqPZ5l67B4A @ 00:16:41]. Tyler Dutchover's 40-employee model runs $30,000 "
                              'a month, $6,000 to admin, $8,000 to stop-loss and $16,000 to the claims '
                              'fund, totaling $192,000 a year; a healthy year using $92,000 leaves '
                              '$100,000, of which the employer gets 50 to 80% back [ExcUj28jzzc @ '
                              '00:03:06]. In the Mediocre Corp case, a $500,000 fully insured quote '
                              'becomes a $470,000 level-funded cap at $39,000 monthly, with $120,000 for '
                              'admin and stop-loss and $350,000 in claims reserve that technically belongs '
                              'to the company [m5BLhBDIZZ4 @ 00:02:13].',
                              'Stop-loss is the engine every architecture except fully insured runs on, '
                              'and the attachment points decide how much risk the employer actually '
                              "carries. Matt Roy's worked example: with a $30,000 individual stop-loss, a "
                              '$100,000 hospital claim costs the employer the first $30,000 and the '
                              'carrier the next $70,000, and even a $2 million claim only costs the '
                              'employer $30,000 [D23XjGg7o_g @ 00:02:49]. Aggregate stop-loss is the '
                              'second layer, adding up every claim below the individual cap, so a $5,000, '
                              'a $10,000 and a $50,000 claim capped at 30 total $45,000 toward the '
                              'aggregate; Roy notes a group can hit the aggregate with nobody hitting the '
                              'individual layer, though it rarely happens [D23XjGg7o_g @ 00:04:09]. Olivia '
                              "says the specific deductible is the employer's choice, as low as 10 or 20 "
                              'thousand or as high as 40, 50 or 100 thousand, with the aggregate '
                              'deductible capping total group spend [hqPZ5l67B4A @ 00:07:12]. Marc Combs '
                              'of Self Insured Reporting frames the same two risks in plain terms: '
                              'specific risk is one employee hit by a bus with a half-million-dollar '
                              'claim, reinsured at 50,000 up to 500,000 depending on size, and aggregate '
                              'risk is everybody getting the bird flu at five grand apiece [5PxkF9WUCd0 @ '
                              '00:07:44].',
                              'The vendor stack is where level-funded and self-funded split hardest. '
                              "Bricker says level-funded buyers are stuck with the carrier's PBM, Cigna "
                              'means Express Scripts, Aetna means CVS Caremark, United means OptumRx, and '
                              "the carrier's stop-loss, while a self-funded group can carve out the PBM or "
                              'buy stop-loss from Berkeley or Tokio Marine [wshiRRBh4Gs @ 00:01:18]. '
                              'Olivia says Allstate runs bundled level-funded and traditional self-funded '
                              'deals through Allied Benefits as TPA on about 95% of groups, with Meritain '
                              'in some regions, quotes level-funded as three line items, admin, stop-loss '
                              'premium and claims funding, and will sell standalone stop-loss to very '
                              'large groups that want their own TPA and PBM [hqPZ5l67B4A @ 00:11:13]. '
                              'Getting a level-funded quote at all means underwriting: Warp reports some '
                              'carriers require every employee to complete an Individual Medical '
                              'Questionnaire taking three to five minutes each, non-IMQ options leave '
                              'rates a shot in the dark, and brokers dodge level funding because chasing '
                              'every IMQ is more work for the same job [XHSDGFk6y94 @ 00:02:08]. Marc '
                              'Combs pushes the last lever: commissions run around 5% of the fully insured '
                              'dollar, and after about 15 years teaching this Combs argues brokers should '
                              'be fee-based, paid by the hour like accountants and attorneys for known, '
                              'visible work [5PxkF9WUCd0 @ 00:05:13].'],
               'table': {'caption': 'Street-level numbers, attachment points and vendor locks quoted by '
                                    'the practitioners',
                         'headers': ['Mechanic',
                                     'Exact Number or Tool',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Carrier load baked into the level-funded rate',
                                   'Roughly 25% above what the carrier expects admin, ISL, ASL and claims '
                                   'to cost',
                                   'Flat bill looks like a fully insured premium; the overcollection is '
                                   'what can come back',
                                   'Blue Ocean Benefits & Consulting ([D23XjGg7o_g @ 00:05:15])'],
                                  ['Aggregate deductible and claims funding schedule',
                                   'Aggregate set around 125% of expected claims, funded in equal slices '
                                   'over 12 months',
                                   'Employer knows the worst-case spend up front; Allstate advances cash '
                                   'if January claims spike',
                                   'Maximize Asset Protection ([hqPZ5l67B4A @ 00:16:41])'],
                                  ['Specific deductible chosen by the employer',
                                   'As low as 10 or 20 thousand, or 40, 50 or 100 thousand per member',
                                   'Sets the most the plan pays on any one member before stop-loss takes '
                                   'over',
                                   'Maximize Asset Protection ([hqPZ5l67B4A @ 00:07:12])'],
                                  ['40-employee level-funded monthly split',
                                   '$30,000 a month: $6,000 admin, $8,000 stop-loss, $16,000 into the '
                                   'claims fund',
                                   '$192,000 annual fund; using $92,000 leaves $100,000 surplus for the '
                                   'refund split',
                                   'Tyler Dutchover ([ExcUj28jzzc @ 00:03:06])'],
                                  ['Renewal laser on a high-cost employee',
                                   "Stop-loss carrier pushes one sick employee's specific attachment up to "
                                   '$200,000 in claims',
                                   'Fallback is the fully insured community pool, which must take the '
                                   'group back at 10%-plus higher',
                                   'Tyler Dutchover ([m5BLhBDIZZ4 @ 00:06:25])'],
                                  ['Individual Medical Questionnaire underwriting burden',
                                   'Three to five minutes per employee, and every enrolling employee has '
                                   'to complete it',
                                   'Non-IMQ plans exist with some carriers, but rates become a shot in the '
                                   'dark',
                                   'Warp ([XHSDGFk6y94 @ 00:02:27])'],
                                  ['Carrier-locked pharmacy benefit manager',
                                   'Cigna forces Express Scripts, Aetna forces CVS Caremark, United forces '
                                   'OptumRx',
                                   'Level-funded buyers cannot carve out the PBM; self-funded groups can '
                                   'swap PBM and stop-loss',
                                   'AHealthcareZ - Healthcare Finance Explained ([wshiRRBh4Gs @ '
                                   '00:01:32])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Moves the Renewal Broker Will Not Volunteer',
                           'body': 'These are the leverage plays the practitioners use to stop the carrier '
                                   "from quietly pocketing a healthy group's claims margin and to move up "
                                   'the funding ladder on their own terms.',
                           'items': ['Run the loss-ratio math on your own renewal: a 120-employee Dallas '
                                     'group at a 60% loss ratio got a flat renewal and no refund, leaving '
                                     'roughly $560,000 of about $1.4 million in premium with the carrier '
                                     '[AHealthcareZ - Healthcare Finance Explained — wshiRRBh4Gs @ '
                                     '00:03:45]',
                                     'Use a level-funded year as a data harvest: Allstate will look at '
                                     'traditional self-funding for groups under 100 lives when they arrive '
                                     'with level-funded claims data proving they run well [Maximize Asset '
                                     'Protection — hqPZ5l67B4A @ 00:09:05]',
                                     'Convert broker pay from roughly 5% commission to a fee you can see, '
                                     'paid like an accountant or attorney for known work [Self Insured '
                                     'Reporting — 5PxkF9WUCd0 @ 00:05:13]',
                                     'Hunt a broker willing to grind the IMQ paperwork: Warp says typical '
                                     'brokers skip level funding because of the extra work, while Warp has '
                                     'produced quotes showing 60% plus savings [Warp — XHSDGFk6y94 @ '
                                     '00:00:48]']},
               'sop_steps': [{'step': 1,
                              'title': 'Strip the premium dollar',
                              'action': 'Break the current fully insured renewal into premium tax, '
                                        'commission, carrier retention and claims before shopping '
                                        'alternatives.',
                              'detail': 'Marc Combs maps a fully insured dollar at about 2 cents premium '
                                        'tax, about 5 cents commission, a carrier retention slice and 70 '
                                        'to 75 cents in medical and pharmacy claims, and says '
                                        'self-insuring shrinks tax and commission while cutting into '
                                        'carrier profit [Self Insured Reporting — 5PxkF9WUCd0 @ 00:01:28]. '
                                        'Brian Calvert pegs carrier overhead, margin and profit at 15 to '
                                        "20 cents of every fully insured dollar [Health Insurance Doesn't "
                                        'Have to Suck — y9n2wYoPMYw @ 00:03:04].'},
                             {'step': 2,
                              'title': 'Size-match the architecture',
                              'action': 'Place the group on the headcount ladder before requesting any '
                                        'level-funded or self-funded quote.',
                              'detail': "Calvert's ladder: under 10 employees fully insured, 10 or 15 to "
                                        '100 the level-funded sweet spot, over 100 self-funded [Health '
                                        "Insurance Doesn't Have to Suck — y9n2wYoPMYw @ 00:06:49]. "
                                        'Allstate sends traditional self-funded deals to underwriting at '
                                        '100 lives, going smaller only with level-funded claims data in '
                                        'hand [Maximize Asset Protection — hqPZ5l67B4A @ 00:08:46].'},
                             {'step': 3,
                              'title': 'Run the underwriting sprint',
                              'action': 'Push every enrolling employee through the medical questionnaire '
                                        'fast and screen the census for high-cost conditions.',
                              'detail': 'Warp clocks the IMQ at three to five minutes per employee, with '
                                        'everyone required to finish it on IMQ carriers [Warp — '
                                        'XHSDGFk6y94 @ 00:02:08]. Tyler Dutchover warns underwriters can '
                                        'decline an older group with conditions like rheumatoid arthritis '
                                        'or hemophilia, or set the claims reserve so high the plan costs '
                                        'more than fully insured [Tyler Dutchover — m5BLhBDIZZ4 @ '
                                        '00:05:13].'},
                             {'step': 4,
                              'title': 'Lock stop-loss terms and refund mechanics',
                              'action': 'Set the specific deductible, confirm the aggregate corridor, and '
                                        'read the surplus split and renewal provisions before signing.',
                              'detail': 'Olivia sets the specific deductible anywhere from 10 or 20 '
                                        'thousand up to 100 thousand, with the aggregate around 125% of '
                                        'expected claims as the hard ceiling [Maximize Asset Protection — '
                                        'hqPZ5l67B4A @ 00:07:43]. Jennifer Shafer insists on knowing the '
                                        'contract, stop-loss coverage, renewal provisions and financial '
                                        'exposure, and says never renew automatically [JS Benefits Group — '
                                        'UhT4cGnMRpY @ 00:01:12].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over where level funding sits on the ladder. Dr. Eric '
                              'Bricker treats it as a halfway house the carrier still milks: he has run '
                              'self-funded groups as small as 45 employees and says self-funding '
                              '120-employee groups is fairly common in the South and Midwest [wshiRRBh4Gs '
                              '@ 00:04:30]. Olivia of Allstate Benefits pitches level funding as the '
                              'stepping stone, with traditional self-funded only going to her underwriters '
                              'at 100 lives unless a smaller group arrives with clean claims data from a '
                              'prior level-funded year [hqPZ5l67B4A @ 00:08:46]. Brian Calvert draws the '
                              'cleanest map: under 10 employees start fully insured, 10 or 15 to 100 is '
                              'the level-funded sweet spot, and past 100 self-funding becomes worth '
                              'exploring once claims history is stable [y9n2wYoPMYw @ 00:07:03]. Floors '
                              'drift by seller. Matt Roy says Cigna, Aetna and UnitedHealthcare write '
                              'level-funded contracts down to 25 lives depending on state, while noting '
                              'nobody under 1,000 lives carries 100 percent of the risk alone [D23XjGg7o_g '
                              '@ 00:03:05]. Jennifer Shafer flags roughly 30 employees as the evaluation '
                              'trigger, and David at Imago Dei opens the conversation at 10. Across the '
                              "four, the floor moves with whoever is selling, and Olivia's rule holds: "
                              'prior level-funded claims data is what earns a sub-100 group a self-funded '
                              'look.',
                              'Nobody agrees on the size of the prize. Warp says its own level-funded '
                              'quotes have produced 60 percent plus cost savings [XHSDGFk6y94 @ 00:00:48], '
                              'while Bricker cites a Milliman study pegging level-funded savings at about '
                              "6 to 12 percent of overall cost [wshiRRBh4Gs @ 00:06:23]. Tyler Dutchover's "
                              'Mediocre Corp model sits at the low end: a $500,000 fully insured quote '
                              'against a $470,000 level-funded cap, paid at $39,000 a month [m5BLhBDIZZ4 @ '
                              '00:02:13]. Olivia flatly refuses to throw out a number, saying it depends '
                              'on coverage, network and what the group wants, and frames the move as a '
                              'strategy play more than a dollar play [hqPZ5l67B4A @ 00:13:08]. The surplus '
                              "split is just as contested. Dutchover's other walkthrough says the carrier "
                              'hands back anywhere from 50 to 80 percent of unused claims money depending '
                              'on contract, as cash or lower rates. Matt Roy says the carrier pads its '
                              'flat price about 25 percent above expected cost and then returns some or '
                              "all of the leftover. Bricker's live Dallas case got neither: a 60 percent "
                              'loss ratio, no credit, no refund, flat renewal. Read every contract for the '
                              'split, because three practitioners report three different refund realities '
                              'on the same product.',
                              'Practitioners even disagree on what self-funded means. PeopleKeep defines '
                              'it as the employer assuming total financial risk and forgoing stop-loss '
                              'entirely, citing KFF data that 20 percent of covered workers at small '
                              'organizations sat in self-insured plans in 2024 [o5eOH2AXJAs @ 00:01:46]. '
                              'Matt Roy says the opposite: no medical group plan is truly self-funded '
                              'because it is always reinsured, a fully reinsured self-funded plan in his '
                              "old rep's words [D23XjGg7o_g @ 00:00:30], and Calvert says self-funded "
                              'plans almost always carry stop-loss. The control argument splits too. '
                              "Bricker warns level funding locks you into the carrier's stop-loss and PBM, "
                              'so Cigna means Express Scripts, Aetna means CVS Caremark and United means '
                              'OptumRx, while true self-funding lets you shop stop-loss with Berkeley or '
                              "Tokio Marine and carve out pharmacy [wshiRRBh4Gs @ 00:01:18]. Olivia's "
                              'Allstate sells standalone stop-loss to groups that want their own TPA and '
                              'PBM, but she says that appetite rarely shows up below a couple hundred to '
                              'thousands of lives [hqPZ5l67B4A @ 00:12:38]. PeopleKeep pushes a fourth '
                              'exit altogether, a standalone HRA with a fixed monthly allowance that rolls '
                              'over and reimburses more than 200 expense types, and Imago Dei says the '
                              'right answer for some employers is a different strategy altogether, such as '
                              'direct primary care.'],
               'table': {'caption': 'Funding Architecture Fault Lines: Who Argues What',
                         'headers': ['Fault Line Between Practitioners',
                                     'Position A',
                                     'Position B',
                                     'Expert Source'],
                         'rows': [['Where level funding sits on the graduation ladder',
                                   'A carrier halfway house; self-fund groups of 45 to 120 employees '
                                   'directly',
                                   'The stepping stone; traditional self-funded underwriting starts at '
                                   'about 100 lives',
                                   'AHealthcareZ - Healthcare Finance Explained ([wshiRRBh4Gs @ '
                                   '00:04:30]); Maximize Asset Protection ([hqPZ5l67B4A @ 00:08:46])'],
                                  ['Minimum headcount for moving off fully insured coverage',
                                   'Under 10 fully insured, 10 or 15 to 100 level funded, over 100 '
                                   'self-funded',
                                   'Carriers write level funded down to 25 lives; evaluate at roughly 30 '
                                   'employees',
                                   "Health Insurance Doesn't Have to Suck ([y9n2wYoPMYw @ 00:07:03]); Blue "
                                   'Ocean Benefits & Consulting ([D23XjGg7o_g @ 00:03:05]); JS Benefits '
                                   'Group ([UhT4cGnMRpY @ 00:01:29])'],
                                  ['How big the level-funded savings actually get in practice',
                                   'Warp reports 60 percent plus savings on some of its produced quotes',
                                   'Milliman study cited at roughly 6 to 12 percent overall cost reduction',
                                   'Warp ([XHSDGFk6y94 @ 00:00:48]); AHealthcareZ - Healthcare Finance '
                                   'Explained ([wshiRRBh4Gs @ 00:06:23])'],
                                  ['How much of the unused claims surplus comes back',
                                   'Carrier returns 50 to 80 percent as a cash refund or lower rates',
                                   'Carrier prices about 25 percent above expected cost, then returns some '
                                   'or all',
                                   'Tyler Dutchover ([ExcUj28jzzc @ 00:03:47]); Blue Ocean Benefits & '
                                   'Consulting ([D23XjGg7o_g @ 00:05:15])'],
                                  ['Whether a self-funded plan carries stop-loss protection at all',
                                   'Self-funded means total employer risk and forgoing a stop-loss policy '
                                   'entirely',
                                   'No medical group plan is truly self-funded; it is always reinsured',
                                   'PeopleKeep ([o5eOH2AXJAs @ 00:01:46]); Blue Ocean Benefits & '
                                   'Consulting ([D23XjGg7o_g @ 00:00:30])'],
                                  ['Control over the PBM and the stop-loss vendor',
                                   'Level funding locks the carrier PBM: Cigna to Express Scripts, Aetna '
                                   'to CVS Caremark, United to OptumRx',
                                   'Standalone stop-loss with your own TPA and PBM mostly fits groups in '
                                   'the hundreds or thousands',
                                   'AHealthcareZ - Healthcare Finance Explained ([wshiRRBh4Gs @ '
                                   '00:01:32]); Maximize Asset Protection ([hqPZ5l67B4A @ 00:12:38])'],
                                  ['What a fully insured premium is really buying the employer',
                                   'Peace of mind that the plan can absorb a larger volume of medical '
                                   'claims',
                                   'Maximum predictability at maximum cost, leaving money on the table as '
                                   'groups grow',
                                   "WPS Health ([g_TZcndr5ds @ 00:00:23]); Health Insurance Doesn't Have "
                                   'to Suck ([y9n2wYoPMYw @ 00:02:03])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["The most expensive trap is assuming a good year pays you. Bricker's Dallas "
                              'broker had a 120-employee, 240-member group run a 60 percent loss ratio on '
                              'roughly $1.4 million in premium at about $15,000 per subscriber; the '
                              'carrier refused any credit or refund and simply held the renewal flat, '
                              'pocketing about $560,000 that a self-funded group would have largely kept '
                              "[wshiRRBh4Gs @ 00:04:09]. The bad year is worse. Dutchover's Mediocre Corp "
                              'blows through its $350,000 claims reserve to $430,000, stop-loss covers the '
                              '$80,000 overage, and total spend stays capped at $470,000, but the next '
                              'renewal lands with a significant increase and possibly a laser that pushes '
                              "one sick employee's specific stop-loss attachment to $200,000 [m5BLhBDIZZ4 "
                              '@ 00:06:25]. Warp confirms that a significant medical claims year will hit '
                              'level-funded renewal rates hard and that the group must actively manage its '
                              "stop-loss [XHSDGFk6y94 @ 00:01:04]. Dutchover's escape hatch costs money: "
                              'the fully insured community pool must take the group back with no health '
                              'questions, but at 10 percent or more above the old rate, so $500,000 '
                              'becomes roughly $550,000 [m5BLhBDIZZ4 @ 00:06:50]. Price that fallback '
                              'before signing year one, since neither the good-year refund nor the '
                              'bad-year renewal is locked in.',
                              'The second wall is underwriting friction before you ever see savings. Warp '
                              'reports some carriers require every employee to complete an Individual '
                              'Medical Questionnaire that takes three to five minutes each, a grind across '
                              'hundreds of employees, while non-IMQ quotes leave rates a shot in the dark; '
                              'level funding is also unavailable in some states [XHSDGFk6y94 @ 00:02:08]. '
                              'Warp says that workload is exactly why many brokers never raise the option. '
                              'Dutchover adds that an older workforce with a few chronic cases such as '
                              'rheumatoid arthritis or hemophilia can get a group declined outright, or '
                              'quoted with a claims reserve so high that level funding costs more than '
                              'staying fully insured [m5BLhBDIZZ4 @ 00:05:25]. On traditional self-funded, '
                              'the danger is liquidity. Olivia warns that a couple of massive claims early '
                              'in the year can force the employer to pay the full aggregate amount within '
                              'a couple of months, which is why the route skews to larger groups with cash '
                              'on hand [hqPZ5l67B4A @ 00:17:30]. Level funding softens that, since '
                              'Allstate advances money when the claims fund runs short in month one and '
                              'recoups it over later deposits. Matt Roy adds a back-end trap: when a '
                              'self-funded contract ends, somebody still has to pay the claims that arrive '
                              'afterward [D23XjGg7o_g @ 00:06:56].',
                              'The structural failure is the fully insured death spiral. Bricker says '
                              'brokers now describe the fully insured market as essentially a high-risk '
                              'pool, with one broker facing an 80 percent renewal and another relieved to '
                              'take 30 percent, because young, low-claim groups keep leaving for level '
                              'funding [wshiRRBh4Gs @ 00:08:30]. Dutchover reports the same spiral and '
                              'says it has already played out in Connecticut [m5BLhBDIZZ4 @ 00:07:25]. If '
                              "you are fully insured and cannot spot the sucker at the table, Bricker's "
                              'line is that it is probably you. The overpay is real on the ground: Mario '
                              'of Maximize Asset Protection paid UnitedHealthcare about $1,200 a month for '
                              'a healthy family of four that he says never used the plan once, a $64,000 '
                              'lesson he blames on buying out of fear instead of knowledge [hqPZ5l67B4A @ '
                              '00:20:45]. Marc Combs of Self Insured Reporting closes the loop: no one '
                              'pays your claims but you. A fully insured group that pays $1 million in '
                              'premium and runs $2 million in claims gets that money clawed back at '
                              'renewal, and he calls post-ACA loss-ratio optics a shell game where a '
                              '75-cent payout can hide money flowing back to the carrier [5PxkF9WUCd0 @ '
                              '00:09:30].'],
               'table': {'caption': 'Firsthand Failure Modes and the Dollars Behind Them',
                         'headers': ['Failure Mode Reported',
                                     'What Happened on the Ground',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Good claims year with zero refund from the carrier',
                                   '120-employee group ran a 60 percent loss ratio; carrier held renewal '
                                   'flat with no credit',
                                   'About $560,000 of roughly $1.4 million in premium retained by the '
                                   'carrier',
                                   'AHealthcareZ - Healthcare Finance Explained ([wshiRRBh4Gs @ '
                                   '00:04:09])'],
                                  ['Renewal laser placed on one sick employee after a bad year',
                                   'Stop-loss carrier renews the plan but carves out one specific '
                                   'high-cost employee',
                                   'Specific stop-loss for that employee does not kick in until $200,000 '
                                   'in claims',
                                   'Tyler Dutchover ([m5BLhBDIZZ4 @ 00:06:25])'],
                                  ['Retreating to the fully insured community pool after a bad renewal',
                                   'Group exits a punishing level-funded renewal and returns with no '
                                   'health questions asked',
                                   'Community rate runs 10 percent or more higher, $500,000 becoming about '
                                   '$550,000',
                                   'Tyler Dutchover ([m5BLhBDIZZ4 @ 00:06:50])'],
                                  ['Individual Medical Questionnaire drag during the quoting process',
                                   'Some carriers require every single employee to complete an IMQ before '
                                   'final rates',
                                   'Three to five minutes per employee; non-IMQ rates are a shot in the '
                                   'dark',
                                   'Warp ([XHSDGFk6y94 @ 00:02:08])'],
                                  ['Underwriting decline for an older or chronically ill workforce',
                                   'Older group with conditions like rheumatoid arthritis or hemophilia '
                                   'gets reviewed by underwriters',
                                   'Carrier may decline to quote or set a claims reserve above fully '
                                   'insured cost',
                                   'Tyler Dutchover ([m5BLhBDIZZ4 @ 00:05:25])'],
                                  ['Cash-flow shock from early massive claims on traditional self-funding',
                                   'A couple of large claims land in the first months of the plan year',
                                   'Employer may have to pay the full aggregate amount within a couple of '
                                   'months',
                                   'Maximize Asset Protection ([hqPZ5l67B4A @ 00:17:30])'],
                                  ['Fear-driven overpaying for coverage a healthy household never touched',
                                   'Healthy family of four paid UnitedHealthcare about $1,200 a month and '
                                   'never used the plan',
                                   'Roughly $64,000 paid in premium with nothing coming back',
                                   'Maximize Asset Protection ([hqPZ5l67B4A @ 00:20:45])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Kill Switches Before Moving a Group Off Fully Insured',
                           'body': 'Every gate below comes from a loss, a laser, or a cash squeeze a '
                                   'practitioner described firsthand. Clear all four before signing a '
                                   'level-funded or self-funded contract.',
                           'items': ['Get the surplus-split and renewal language in writing before '
                                     'signing, because a 120-employee group with a 60 percent loss ratio '
                                     'still got no credit, no refund, and a flat renewal [AHealthcareZ - '
                                     'Healthcare Finance Explained — wshiRRBh4Gs @ 00:04:09].',
                                     'Model the year-two downside: a renewal laser that pushes one '
                                     "employee's specific attachment to $200,000, plus the 10 percent or "
                                     'higher fully insured fallback rate [Tyler Dutchover — m5BLhBDIZZ4 @ '
                                     '00:06:25].',
                                     'On traditional self-funded, prove the business can write a check for '
                                     'the full aggregate amount within a couple of months if big claims '
                                     'hit early [Maximize Asset Protection — hqPZ5l67B4A @ 00:17:42].',
                                     'Never pick a level-funded plan just because the initial quote looks '
                                     'cheaper; check demographics, claims history, expected utilization, '
                                     'and the stop-loss protection first [JS Benefits Group — qE34fv4L2qU '
                                     '@ 00:00:54].']}}],
 'pull_quote': "If you're a fully insured group and you don't know who the sucker is, it's probably you. - "
               'AHealthcareZ - Healthcare Finance Explained (wshiRRBh4Gs @ 00:08:05).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Pull every scrap of claims data you can before renewal, because fully insured '
                      'carriers are very stingy with the data they release to groups [Maximize Asset '
                      'Protection — hqPZ5l67B4A @ 00:09:36].',
                      'Compare fully insured, level-funded, and self-funded quotes side by side before '
                      'renewal and do not automatically renew [JS Benefits Group — UhT4cGnMRpY @ '
                      '00:01:47].',
                      'Map headcount to structure: under 10 employees fully insured, 10 or 15 to 100 level '
                      'funded, more than 100 self-funded with stable claims history [Health Insurance '
                      "Doesn't Have to Suck — y9n2wYoPMYw @ 00:07:03].",
                      'Set the specific deductible per member, anywhere from 10,000 or 20,000 up to '
                      '100,000, and confirm the aggregate sits near 125 percent of expected claims '
                      '[Maximize Asset Protection — hqPZ5l67B4A @ 00:07:43].',
                      'Budget the IMQ workload of three to five minutes per employee and demand a broker '
                      'who will drive completion fast instead of skipping level funding [Warp — '
                      'XHSDGFk6y94 @ 00:02:08].',
                      'Convert broker compensation to a fee-based arrangement so you know exactly what '
                      'work you are paying for once you self-insure [Self Insured Reporting — 5PxkF9WUCd0 '
                      '@ 00:05:13].'],
 'statutory_citations': [{'title': 'AHealthcareZ - Healthcare Finance Explained — Level-Funded Health '
                                   'Plans Explained [00:04:09]',
                          'url': 'https://www.youtube.com/watch?v=wshiRRBh4Gs&t=249s',
                          'relevance': 'Primary practitioner testimony on a 60 percent loss ratio group '
                                       'losing about $560,000 to carrier retention under level funding.'},
                         {'title': 'Tyler Dutchover — Fully Insured vs Level Funded: Health Insurance '
                                   'Explained [00:06:25]',
                          'url': 'https://www.youtube.com/watch?v=m5BLhBDIZZ4&t=385s',
                          'relevance': 'Primary practitioner testimony on renewal lasers, underwriting '
                                       'declines, and the cost of retreating to the fully insured pool.'},
                         {'title': 'Maximize Asset Protection — Group Health Insurance Explained: Fully '
                                   'Funded vs. Self-Funded vs. Level Funded Plans [00:17:30]',
                          'url': 'https://www.youtube.com/watch?v=hqPZ5l67B4A&t=1050s',
                          'relevance': 'Primary practitioner testimony on aggregate exposure, cash-flow '
                                       'risk, and claims-fund advances in self-funded and level-funded '
                                       'plans.'},
                         {'title': 'Blue Ocean Benefits & Consulting — Basics of Self-Funded & '
                                   'Level-Funded Group Plans [00:05:15]',
                          'url': 'https://www.youtube.com/watch?v=D23XjGg7o_g&t=315s',
                          'relevance': 'Primary practitioner testimony on how carriers price level-funded '
                                       'contracts about 25 percent above expected cost.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'wshiRRBh4Gs',
                       'title': 'Level-Funded Health Plans Explained',
                       'channel': 'AHealthcareZ - Healthcare Finance Explained',
                       'author': 'AHealthcareZ - Healthcare Finance Explained',
                       'text': 'Not crediting back to the employer, is $560,000. So, just keep in mind '
                               'that if this group had been self-funded with 120 employees, they could '
                               'have kept, maybe not all of that 560,000, but they would have kept a huge '
                               'chunk of it.',
                       'tip': 'Not crediting back to the employer, is $560,000. So, just keep in mind that '
                              'if this group had been self-funded with 120 employees, they could have '
                              'kept, maybe not all of that 560,000, but they would have kept a huge chunk '
                              'of it.',
                       'timestamp': 249,
                       'timestamp_seconds': 249,
                       'timestamp_label': '[00:04:09]',
                       'url': 'https://www.youtube.com/watch?v=wshiRRBh4Gs&t=249s',
                       'markdown': '[00:04:09](https://www.youtube.com/watch?v=wshiRRBh4Gs&t=249s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wshiRRBh4Gs',
                       'title': 'Level-Funded Health Plans Explained',
                       'channel': 'AHealthcareZ - Healthcare Finance Explained',
                       'author': 'AHealthcareZ - Healthcare Finance Explained',
                       'text': "So, if you're using Cigna, you got to use Express Scripts. If you're using "
                               "Aetna, you got to use CVS Caremark. If you're using United, you got to use "
                               "OptumRx. You can't choose somebody else.",
                       'tip': "So, if you're using Cigna, you got to use Express Scripts. If you're using "
                              "Aetna, you got to use CVS Caremark. If you're using United, you got to use "
                              "OptumRx. You can't choose somebody else.",
                       'timestamp': 92,
                       'timestamp_seconds': 92,
                       'timestamp_label': '[00:01:32]',
                       'url': 'https://www.youtube.com/watch?v=wshiRRBh4Gs&t=92s',
                       'markdown': '[00:01:32](https://www.youtube.com/watch?v=wshiRRBh4Gs&t=92s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XHSDGFk6y94',
                       'title': 'Level Funded vs. Fully Insured Health Plans: What Every Employer Needs to '
                                'Know',
                       'channel': 'Warp',
                       'author': 'Warp',
                       'text': 'Some carriers require that every employee fills out a number of questions '
                               'called an Individual Medical Questionnaire, an IMQ, and that can take '
                               'three to five minutes per employee.',
                       'tip': 'Some carriers require that every employee fills out a number of questions '
                              'called an Individual Medical Questionnaire, an IMQ, and that can take three '
                              'to five minutes per employee.',
                       'timestamp': 128,
                       'timestamp_seconds': 128,
                       'timestamp_label': '[00:02:08]',
                       'url': 'https://www.youtube.com/watch?v=XHSDGFk6y94&t=128s',
                       'markdown': '[00:02:08](https://www.youtube.com/watch?v=XHSDGFk6y94&t=128s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'VPeObJ32l7M',
                       'title': 'Self-Funded vs. Fully-Insured Health Insurance, EXPLAINED | The '
                                'Self-Funded Sketchbook',
                       'channel': 'Self-Funded',
                       'author': 'Self-Funded',
                       'text': 'If I go self-funded, about 60 to 70% of my plan is now variable and '
                               'therefore manageable and I can do something about it.',
                       'tip': 'If I go self-funded, about 60 to 70% of my plan is now variable and '
                              'therefore manageable and I can do something about it.',
                       'timestamp': 216,
                       'timestamp_seconds': 216,
                       'timestamp_label': '[00:03:36]',
                       'url': 'https://www.youtube.com/watch?v=VPeObJ32l7M&t=216s',
                       'markdown': '[00:03:36](https://www.youtube.com/watch?v=VPeObJ32l7M&t=216s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ExcUj28jzzc',
                       'title': 'Level Funded Health Plans Explained - in Plain English',
                       'channel': 'Tyler Dutchover',
                       'author': 'Tyler Dutchover',
                       'text': 'The insurance company actually splits that surplus with you. Depending on '
                               'your specific contract, you get anywhere between 50 to 80% of that money '
                               'back in a cash refund or with lower rates the next year.',
                       'tip': 'The insurance company actually splits that surplus with you. Depending on '
                              'your specific contract, you get anywhere between 50 to 80% of that money '
                              'back in a cash refund or with lower rates the next year.',
                       'timestamp': 227,
                       'timestamp_seconds': 227,
                       'timestamp_label': '[00:03:47]',
                       'url': 'https://www.youtube.com/watch?v=ExcUj28jzzc&t=227s',
                       'markdown': '[00:03:47](https://www.youtube.com/watch?v=ExcUj28jzzc&t=227s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'o5eOH2AXJAs',
                       'title': 'Level funded vs. self funded health plans',
                       'channel': 'PeopleKeep',
                       'author': 'PeopleKeep',
                       'text': 'KFF found that 20% of covered workers at small organizations were enrolled '
                               'in self-insured health plans in 2024.',
                       'tip': 'KFF found that 20% of covered workers at small organizations were enrolled '
                              'in self-insured health plans in 2024.',
                       'timestamp': 106,
                       'timestamp_seconds': 106,
                       'timestamp_label': '[00:01:46]',
                       'url': 'https://www.youtube.com/watch?v=o5eOH2AXJAs&t=106s',
                       'markdown': '[00:01:46](https://www.youtube.com/watch?v=o5eOH2AXJAs&t=106s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'g_TZcndr5ds',
                       'title': 'Self funded vs fully insured health plans | WPS explains',
                       'channel': 'WPS Health',
                       'author': 'WPS Health',
                       'text': 'Self-funded plans are often more flexible because they are subject to '
                               'fewer state regulations or requirements.',
                       'tip': 'Self-funded plans are often more flexible because they are subject to fewer '
                              'state regulations or requirements.',
                       'timestamp': 75,
                       'timestamp_seconds': 75,
                       'timestamp_label': '[00:01:15]',
                       'url': 'https://www.youtube.com/watch?v=g_TZcndr5ds&t=75s',
                       'markdown': '[00:01:15](https://www.youtube.com/watch?v=g_TZcndr5ds&t=75s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'D23XjGg7o_g',
                       'title': 'Basics of Self-Funded & Level-Funded Group Plans',
                       'channel': 'Blue Ocean Benefits & Consulting',
                       'author': 'Blue Ocean Benefits & Consulting',
                       'text': "When you do a level funded plan the carrier calculates what they're going "
                               'to need for admin, ISL, ASL and claims, they then usually charge you about '
                               '25% more than they expect it to cost and they give you a flat number.',
                       'tip': "When you do a level funded plan the carrier calculates what they're going "
                              'to need for admin, ISL, ASL and claims, they then usually charge you about '
                              '25% more than they expect it to cost and they give you a flat number.',
                       'timestamp': 315,
                       'timestamp_seconds': 315,
                       'timestamp_label': '[00:05:15]',
                       'url': 'https://www.youtube.com/watch?v=D23XjGg7o_g&t=315s',
                       'markdown': '[00:05:15](https://www.youtube.com/watch?v=D23XjGg7o_g&t=315s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hqPZ5l67B4A',
                       'title': 'Group Health Insurance Explained: Fully Funded vs. Self-Funded vs. Level '
                                'Funded Plans',
                       'channel': 'Maximize Asset Protection',
                       'author': 'Maximize Asset Protection',
                       'text': 'You could potentially from a cash flow perspective need to pay that full '
                               'aggregate amount up front within a couple months.',
                       'tip': 'You could potentially from a cash flow perspective need to pay that full '
                              'aggregate amount up front within a couple months.',
                       'timestamp': 1050,
                       'timestamp_seconds': 1050,
                       'timestamp_label': '[00:17:30]',
                       'url': 'https://www.youtube.com/watch?v=hqPZ5l67B4A&t=1050s',
                       'markdown': '[00:17:30](https://www.youtube.com/watch?v=hqPZ5l67B4A&t=1050s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5PxkF9WUCd0',
                       'title': 'Fully Insured VS Self Insured',
                       'channel': 'Self Insured Reporting',
                       'author': 'Self Insured Reporting',
                       'text': "No one's gonna pay your claims but you. There are no free lunches, period.",
                       'tip': "No one's gonna pay your claims but you. There are no free lunches, period.",
                       'timestamp': 555,
                       'timestamp_seconds': 555,
                       'timestamp_label': '[00:09:15]',
                       'url': 'https://www.youtube.com/watch?v=5PxkF9WUCd0&t=555s',
                       'markdown': '[00:09:15](https://www.youtube.com/watch?v=5PxkF9WUCd0&t=555s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'm5BLhBDIZZ4',
                       'title': 'Fully Insured vs Level Funded: Health Insurance Explained',
                       'channel': 'Tyler Dutchover',
                       'author': 'Tyler Dutchover',
                       'text': "We're going to renew your plan, but we're putting in a laser on that one "
                               "specific employee. The specific stop-loss safety net won't kick in for "
                               'them until they hit 200,000 in claims.',
                       'tip': "We're going to renew your plan, but we're putting in a laser on that one "
                              "specific employee. The specific stop-loss safety net won't kick in for them "
                              'until they hit 200,000 in claims.',
                       'timestamp': 385,
                       'timestamp_seconds': 385,
                       'timestamp_label': '[00:06:25]',
                       'url': 'https://www.youtube.com/watch?v=m5BLhBDIZZ4&t=385s',
                       'markdown': '[00:06:25](https://www.youtube.com/watch?v=m5BLhBDIZZ4&t=385s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'i5hi-x9Pdxw',
                       'title': 'Understanding Your Self-Funded Health Plan | McGohan Brabender',
                       'channel': 'McGohan Brabender',
                       'author': 'McGohan Brabender',
                       'text': 'Employers and employees have more control over health care costs, can '
                               'manage claims costs through tailored clinical or wellness programs and '
                               'guide employees towards fair price providers.',
                       'tip': 'Employers and employees have more control over health care costs, can '
                              'manage claims costs through tailored clinical or wellness programs and '
                              'guide employees towards fair price providers.',
                       'timestamp': 146,
                       'timestamp_seconds': 146,
                       'timestamp_label': '[00:02:26]',
                       'url': 'https://www.youtube.com/watch?v=i5hi-x9Pdxw&t=146s',
                       'markdown': '[00:02:26](https://www.youtube.com/watch?v=i5hi-x9Pdxw&t=146s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iT4htd_Aqag',
                       'title': 'Self Funded vs Fully Insured Health Plans',
                       'channel': 'The Difference Card',
                       'author': 'The Difference Card',
                       'text': 'Self-funded plans have significantly reduced fixed costs because premiums '
                               'do not include projected claims costs, pooling charges or taxes.',
                       'tip': 'Self-funded plans have significantly reduced fixed costs because premiums '
                              'do not include projected claims costs, pooling charges or taxes.',
                       'timestamp': 66,
                       'timestamp_seconds': 66,
                       'timestamp_label': '[00:01:06]',
                       'url': 'https://www.youtube.com/watch?v=iT4htd_Aqag&t=66s',
                       'markdown': '[00:01:06](https://www.youtube.com/watch?v=iT4htd_Aqag&t=66s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Zej6tYKTOgE',
                       'title': 'Level-Funded Health Plans Explained Simply for Christian Employers',
                       'channel': 'Imago Dei Insurance Advisors',
                       'author': 'Imago Dei Insurance Advisors',
                       'text': 'A low first-year rate is not helpful if the strategy is not sustainable.',
                       'tip': 'A low first-year rate is not helpful if the strategy is not sustainable.',
                       'timestamp': 182,
                       'timestamp_seconds': 182,
                       'timestamp_label': '[00:03:02]',
                       'url': 'https://www.youtube.com/watch?v=Zej6tYKTOgE&t=182s',
                       'markdown': '[00:03:02](https://www.youtube.com/watch?v=Zej6tYKTOgE&t=182s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UhT4cGnMRpY',
                       'title': 'Level Funded Health Plans  What Employers Need to Know 1080p caption',
                       'channel': 'JS Benefits Group',
                       'author': 'JS Benefits Group',
                       'text': "Don't automatically renew. Understand your options first.",
                       'tip': "Don't automatically renew. Understand your options first.",
                       'timestamp': 107,
                       'timestamp_seconds': 107,
                       'timestamp_label': '[00:01:47]',
                       'url': 'https://www.youtube.com/watch?v=UhT4cGnMRpY&t=107s',
                       'markdown': '[00:01:47](https://www.youtube.com/watch?v=UhT4cGnMRpY&t=107s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'y9n2wYoPMYw',
                       'title': 'Fully Insured vs. Self-Funded vs. Level-Funded Explained',
                       'channel': "Health Insurance Doesn't Have to Suck",
                       'author': "Health Insurance Doesn't Have to Suck",
                       'text': 'The monthly payment structure is manageable, the stop loss protection is '
                               'meaningful, and the potential year end refund can be significant if your '
                               'group stays healthy. So this is the sweet spot for level funding.',
                       'tip': 'The monthly payment structure is manageable, the stop loss protection is '
                              'meaningful, and the potential year end refund can be significant if your '
                              'group stays healthy. So this is the sweet spot for level funding.',
                       'timestamp': 423,
                       'timestamp_seconds': 423,
                       'timestamp_label': '[00:07:03]',
                       'url': 'https://www.youtube.com/watch?v=y9n2wYoPMYw&t=423s',
                       'markdown': '[00:07:03](https://www.youtube.com/watch?v=y9n2wYoPMYw&t=423s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qE34fv4L2qU',
                       'title': 'Is Level Funding Right for Your Company',
                       'channel': 'JS Benefits Group',
                       'author': 'JS Benefits Group',
                       'text': "The right question isn't whether level funding is cheaper; the better "
                               "question is whether level funding makes sense for our company's risk "
                               'profile and long-term benefit strategy.',
                       'tip': "The right question isn't whether level funding is cheaper; the better "
                              "question is whether level funding makes sense for our company's risk "
                              'profile and long-term benefit strategy.',
                       'timestamp': 73,
                       'timestamp_seconds': 73,
                       'timestamp_label': '[00:01:13]',
                       'url': 'https://www.youtube.com/watch?v=qE34fv4L2qU&t=73s',
                       'markdown': '[00:01:13](https://www.youtube.com/watch?v=qE34fv4L2qU&t=73s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'}]}
