from __future__ import annotations

CHAPTER_4 = {'id': 'Q4',
 'chapter_id': 'Q4',
 'chapter_number': 4,
 'question_number': 4,
 'slug': 'section-301-adcvd-bond-exposure-refund-paths',
 'question_prompt': 'How do Section 301, AD/CVD, forced-labor and other tariff regimes create refund '
                    'opportunities and open liability, and how do bonds and liquidation status affect '
                    'recovery?',
 'kicker': 'Q4 / THE BIG MONEY PLAYBOOKS',
 'title': 'Section 301, AD/CVD and Bond Exposure: Refund Paths and Liability Traps',
 'subtitle': 'Section 301 refunds via protest or post summary correction, refund litigation and new 301 '
             'actions, forced-labor tariffs, antidumping and countervailing duty basics and best '
             'practices, EAPA evasion allegations, customs bonds and open bond liability, and the '
             'liquidated versus unliquidated refund trap',
 'layout_template': 'comparison_matrix',
 'reading_time_minutes': 15,
 'executive_summary': 'Customs refund operators agree that liquidation status decides everything. '
                      'Unliquidated entries move through PSC or CAPE, and liquidated entries get a protest '
                      'inside 180 days. Older liquidated IEEPA entries need entry-specific court orders, '
                      'while CBP processes $80B on the unliquidated side. Section 301 drawback recovers up '
                      'to 99% through ACE-only filing, but AD/CVD goods sit outside drawback entirely. '
                      'AD/CVD scope language also overrides the HTS code, which exposes importers to '
                      'retroactive 250% bills after clean 0% clearances. Bond specialists treat the bond '
                      'as a revenue guarantee, not insurance. They size it at 10% of trailing annual '
                      'duties, taxes and fees, with a $50K floor, and warn that one-size bumps fail nine '
                      'times out of 10. Practitioners split on refund odds: Great Lakes Customs Law '
                      'reports very successful protests, while CSIS panelists say small importers lose and '
                      'DOJ is banking on fatigue.',
 'key_metrics': [{'label': 'Section 301 Drawback Recovery Ceiling',
                  'metric': 'Section 301 Drawback Recovery Ceiling',
                  'value': 'Up to 99% of duties paid',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Refund of Section 301 duties on China-origin goods that were exported, '
                             'destroyed under customs supervision, or used as components in exports, with '
                             'each import linked to its export in the records',
                  'source': 'USA Customs Clearance ([khfmXSwD3DE @ 00:01:40])'},
                 {'label': 'Continuous Bond Sufficiency Formula',
                  'metric': 'Continuous Bond Sufficiency Formula',
                  'value': 'Annual duties, taxes and fees x 10%, $50K minimum',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Measured on a rolling 365-day window, regardless of liquidation status; a '
                             '$50K bond covers $500K of DTF',
                  'source': 'Trade Risk Guaranty ([M68ZVWdgp9I @ 00:02:15])'},
                 {'label': 'CAPE Refunds Paid vs. Estimated Pool',
                  'metric': 'CAPE Refunds Paid vs. Estimated Pool',
                  'value': '$100B paid of about $166B by July 31',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'IEEPA refund flow through the CAPE portal, with Cato estimating about $130B '
                             'total; refunds go to the importer of record with no legal duty to pass them '
                             'on',
                  'source': 'Trade Winds Report ([xJrKO4dLXJ4 @ 00:02:34])'},
                 {'label': 'AD/CVD Penalty Duty Range',
                  'metric': 'AD/CVD Penalty Duty Range',
                  'value': '50% to over 300% of value',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Example given: a $50K aluminum container draws a $150K duty bill',
                  'source': 'Ask The Customs Manager ([Ze1pOvT4KsI @ 00:01:18])'}],
 'sections': [{'title': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every refund operator in this lineup keys the play to one variable: '
                              'liquidation status. Jason Wapanik of Great Lakes Customs Law lays out the '
                              'two classic Section 301 exclusion routes. The first is a post summary '
                              'correction, filed through the licensed broker (usually the original filer) '
                              'inside roughly 300 days of entry and before liquidation. The second is a '
                              'protest within 180 days after liquidation, which lands about 310 days after '
                              'import [kBvWPMXLLgs @ 00:01:41]. Ask The Customs Manager runs the same '
                              'status triage for IEEPA money. Unliquidated entries wait for CAPE because '
                              'PSCs are now "completely forbidden." Liquidated entries inside 180 days get '
                              'a protest on a hard deadline. Anything older generally needs legal action '
                              'because CBP cannot refund it [xq8bHfr9ke8 @ 00:05:19]. Freightos describes '
                              "liquidation as CBP's audit of duties paid. It reports CBP processing $80B "
                              'for unliquidated entries while demanding an entry-specific court order for '
                              'liquidated ones, which may push importers into trade court [cIMBwZ9J60I @ '
                              '00:00:58]. CSIS pegs liquidation at 312 days and notes about $20B paid '
                              'against an estimated $166B, with electronic funds transfer enrollment a '
                              'prerequisite for getting paid at all [PJpF0M_rjYs @ 00:23:04]. The shared '
                              'lesson: map every entry to its liquidation date before choosing a weapon.',
                              'The second consensus point is that AD/CVD exposure hides outside the tariff '
                              'schedule and outside the refund machinery. Ask The Customs Manager warns '
                              'that orders follow a written scope description, not the HS code. A broker '
                              'sees a 0% rate and clears goods that later draw a retroactive 250% bill, '
                              'plus interest and false-declaration fines, in a post-clearance audit about '
                              'a year out [Ze1pOvT4KsI @ 00:01:41]. Lisa Gelino and Alexander Amdur at the '
                              'NCBFAA Educational Institute make the same point: HTS numbers are guidance '
                              'only, and the written scope is dispositive. AD origin can also differ from '
                              'CBP origin, so Chinese cells inside Mexican panels stay subject. Because '
                              'there is no drawback on AD/CVD, goods an importer refuses to pay on should '
                              'never be entered for consumption [CGsvr1SDN8s @ 00:29:04]. USA Customs '
                              'Clearance independently flags that goods subject to AD/CVD may be '
                              'ineligible for Section 301 drawback, which kills the up-to-99% recovery '
                              'play on those lines [khfmXSwD3DE @ 00:01:59]. Tyler Zaichkin of Trade Risk '
                              'Guaranty closes the loop: posted rates of 30%, 50% or 100% are deposits, '
                              'not final duties. If nobody requests an administrative review in the '
                              'anniversary month, the deposit rate becomes final [38zRYvMd5Ps @ 00:18:04]. '
                              'The rate on the entry summary is a placeholder.',
                              'Bond specialists agree the customs bond is a revenue guarantee, not a '
                              'shield. Trade Risk Guaranty describes the C1, or Activity Code One, bond as '
                              'a mandatory three-party contract with a Treasury-listed surety. Goods do '
                              'not clear without it, the surety pays up to the bond amount, and the '
                              'importer stays liable to the surety for every dollar paid out [P-dHB1oQLCI '
                              '@ 00:01:55]. Freight & Trade makes the same point: a bond is not payment of '
                              'duties, it protects the government\'s revenue stream, and "it is not '
                              'insurance that eliminates the importer\'s responsibility." The channel '
                              'lists five rookie errors, including assuming the broker absorbs '
                              'responsibility and confusing bond amount with premium [ez065LeX6vE @ '
                              '00:04:37]. Yuri Starikov frames the CBP-importer-surety triangle as '
                              'protection of revenue and compliance rather than punishment. The bond is '
                              'posted on CBP Form 301 across consumption, AD/CVD, IT, I&E and drawback '
                              'entry types, and poor customs credit can trigger a cash deposit requirement '
                              '[d6omeUFeZfA @ 00:04:54]. Travis Smith of Trade Risk Guaranty ties this to '
                              'the refund era. The surety is exposed for the bond amount plus the '
                              'unliquidated tail, so a steady bond stacks to twice its face. AD/CVD '
                              'liquidation stretching 2 to 8 years then drives full collateral demands '
                              '[M68ZVWdgp9I @ 00:21:40].'],
               'table': {'caption': 'Consensus Positions on Refund Routes, AD/CVD Scope and Bond Liability',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Liquidation status picks the refund route',
                                   'Unliquidated entries ride PSC or CAPE; liquidated entries need a '
                                   'protest within 180 days',
                                   'Build an entry-level liquidation calendar before filing any refund '
                                   'claim',
                                   'Ask The Customs Manager ([xq8bHfr9ke8 @ 00:06:00])'],
                                  ['Section 301 exclusion refunds run on two clocks',
                                   'PSC inside about 300 days before liquidation; protest within 180 days '
                                   'after liquidation',
                                   'Push the original filing broker to submit PSCs well before day 300',
                                   'Great Lakes Customs Law ([kBvWPMXLLgs @ 00:01:41])'],
                                  ['Liquidated IEEPA entries need entry-specific court orders',
                                   'CBP processes $80B unliquidated but demands a court order for each '
                                   'liquidated entry',
                                   'Budget for trade court litigation on older liquidated entry '
                                   'populations',
                                   'Freightos ([cIMBwZ9J60I @ 00:00:58])'],
                                  ['AD/CVD written scope beats the HTS code',
                                   'Written scope is dispositive; HTS numbers are provided for guidance '
                                   'purposes only',
                                   'Read every order scope manually instead of trusting a 0% rate',
                                   'NCBFAA Educational Institute ([CGsvr1SDN8s @ 00:24:39])'],
                                  ['AD/CVD goods sit outside drawback recovery',
                                   'Goods subject to AD/CVD may be ineligible for the Section 301 drawback '
                                   'refund',
                                   'Strip AD/CVD lines out of drawback claims before you file',
                                   'USA Customs Clearance ([khfmXSwD3DE @ 00:01:59])'],
                                  ['The bond is a guarantee, not insurance',
                                   'Surety pays up to the bond amount, and the importer stays liable to '
                                   'the surety',
                                   'Treat every surety payout as debt coming straight back to you',
                                   'Trade Risk Guaranty ([P-dHB1oQLCI @ 00:02:12])'],
                                  ['AD/CVD deposit rates are not final duties',
                                   'Rates of 30%, 50% or 100% stay deposits until reviews finalize the '
                                   'duty',
                                   'Request administrative reviews in the anniversary month, or the '
                                   'deposit rate becomes final',
                                   'Trade Risk Guaranty ([38zRYvMd5Ps @ 00:17:12])']]}},
              {'title': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['USA Customs Clearance runs Section 301 drawback as a four-move workflow. It '
                              'covers China-origin goods that were exported, destroyed under customs '
                              'supervision, or used as components in exports, with recovery up to 99% once '
                              'each import is linked to its export in the records. The sequence is: pull '
                              'CBP Form 7501 entries, match imports to exports, build the claim including '
                              'the Chapter 99 code, and file through ACE, because paper claims are not '
                              'accepted [khfmXSwD3DE @ 00:03:46]. Substitution drawback requires '
                              'commercially interchangeable goods under the same HTS and is called '
                              'especially powerful for mixed inventory. First-time filers wait 6 to '
                              '12-plus months, while accelerated payment lands in about 4 weeks. The named '
                              'killers are the five-year filing deadline, HTS mismatch and weak '
                              'documentation, and the parting order is not to write off 301 costs '
                              '[khfmXSwD3DE @ 00:04:20]. For exclusion refunds, Wapanik stresses that '
                              'protests are entry-by-entry: one protest can cover multiple entries, but '
                              'there is no blanket claim. The filer must also prove the exclusion applies, '
                              'with the entry paperwork in hand [kBvWPMXLLgs @ 00:03:29]. Ask The Customs '
                              'Manager adds the record-pull tactic: screen entry summaries for Chapter 99 '
                              'headings, and keep one ethical broker who hands over entry copies so the '
                              'audit trail stays complete [xq8bHfr9ke8 @ 00:02:32].',
                              'Travis Smith gives the sizing formula Trade Risk Guaranty underwrites '
                              'against. Annual duties, taxes and fees times 10% equals the minimum bond. '
                              'The floor is $50K, sizes rise in $10K steps to $100K, and then in $100K '
                              'steps: "there\'s no $25,000 import bond" [M68ZVWdgp9I @ 00:02:15]. The DTF '
                              'window is a rolling 365 days, and liquidation status is ignored. A $50K '
                              'bond covers $500K of DTF, and a new bond does not reset sufficiency. Going '
                              'up only one size fails within 12 months "nine times out of 10." The '
                              'forecast should therefore run at the IEEPA-level rate of about 25% plus '
                              'standard duties, with a 5% buffer on top [M68ZVWdgp9I @ 00:15:06]. '
                              'Insufficiency letters state only the minimum increase and give 30 days to '
                              'act. The old bond must be terminated at least 15 days before that mark. '
                              'Reason one, DTF exceeded, drives 98% of letters. Mid-term jumps from $5M to '
                              '$7M to $10M stack $22M of exposure plus wasted premium, so the best move is '
                              'to start at $10M and the second best is to skip $7M. Freight & Trade sets '
                              'single-entry bonds at entered value plus duties, taxes and fees, separate '
                              'from premium [ez065LeX6vE @ 00:03:07]. Starikov pegs other-agency bonds at '
                              '3x total entered value, excluding duties, taxes and fees [d6omeUFeZfA @ '
                              '00:09:41].',
                              'On AD/CVD, the NCBFAA panel treats ACE as the system of record and the '
                              'ES-15 Active Case report as the bulk download of public case data. That '
                              'data spans more than 325 orders and 140-plus commodities, which produced '
                              '$1.2B in cash deposits, double the prior year [CGsvr1SDN8s @ 00:12:54]. The '
                              "panel's operating rules: classify by scope, check for both AD and CVD "
                              'orders on the same merchandise, track rates by exporter/producer case '
                              'number, and correct errors through PSC or prior disclosure. ABI queries at '
                              '10 digits miss 8-digit flags. Ask The Customs Manager tells importers to '
                              "distrust the supplier and the forwarder's software. They should manually "
                              'check the AD registers for metal, wood, paper, plastics and chemicals, and '
                              'get a binding scope ruling before shipping anything ambiguous [Ze1pOvT4KsI '
                              '@ 00:03:04]. The panel notes that only Commerce issues those rulings. On '
                              "offense, CBP's own walkthrough shows competitors filing EAPA evasion "
                              'allegations through the TVR tool. The filer enters the AD/CVD number, '
                              'describes the merchandise and scheme, and names the violating importer. '
                              'They then upload trade data, market research, first-hand accounts and '
                              'emails, and supply a public version of any confidential document '
                              '[CXFkPqsyXnI @ 00:04:07]. Informants who provide original information can '
                              'claim moiety compensation if a net amount is recovered [CXFkPqsyXnI @ '
                              '00:06:02].'],
               'table': {'caption': 'Street Mechanics: Refund Windows, Bond Math, Tools and Pricing',
                         'headers': ['Mechanic or Tool',
                                     'Exact Number or Window',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Section 301 drawback filed through ACE',
                                   'Up to 99% recovery; 6-12+ months first time, about 4 weeks accelerated',
                                   'Pull 7501s, match exports, add the Chapter 99 code, and file '
                                   'electronically',
                                   'USA Customs Clearance ([khfmXSwD3DE @ 00:04:05])'],
                                  ['Continuous bond sufficiency formula',
                                   'Annual DTF times 10%, $50K floor, rolling 365-day measurement window',
                                   'Size the new bond off the trailing twelve months plus a forecast '
                                   'buffer',
                                   'Trade Risk Guaranty ([M68ZVWdgp9I @ 00:02:15])'],
                                  ['Insufficiency letter response clock',
                                   '30 days to act; terminate the old bond 15 days before the deadline',
                                   'Jump past the stated minimum increase to avoid repeat letters within '
                                   'months',
                                   'Trade Risk Guaranty ([M68ZVWdgp9I @ 00:11:07])'],
                                  ['AD/CVD collateral release timing',
                                   'Released after all entries liquidate plus 120 days; AD/CVD liquidation '
                                   'runs 2-8 years',
                                   'Price multi-year collateral lockup into AD/CVD import product margins',
                                   'Trade Risk Guaranty ([M68ZVWdgp9I @ 00:45:33])'],
                                  ['Eagle Eye ACE monitoring subscription',
                                   '$300 to $1,000 per 12 months after a three-month free trial',
                                   'Track entries and liquidation status, knowing the tool does not show '
                                   'HTSUS codes',
                                   'Trade Risk Guaranty ([M68ZVWdgp9I @ 00:42:41])'],
                                  ['$50K continuous bond pricing',
                                   'Typical bonds cost $475-$525; TRG multi-year term at $225 per year',
                                   'Shop multi-year terms on the standard $50K bond size',
                                   'Trade Risk Guaranty ([38zRYvMd5Ps @ 00:24:13])'],
                                  ['ES-15 Active Case report download',
                                   'Pulls all public case data across 325+ orders and 140+ commodities',
                                   'Screen every product against active case scope language before entry',
                                   'NCBFAA Educational Institute ([CGsvr1SDN8s @ 00:12:54])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Moves the Bond, Drawback and Protest Specialists Actually Use',
                           'body': 'These are the tactical edges practitioners teach for sizing bonds, '
                                   'stacking drawback claims, bundling protests and catching hidden AD/CVD '
                                   'flags.',
                           'items': ['Skip the one-size bump. Going up only one bond size fails within 12 '
                                     'months nine times out of 10, and a $5M-to-$7M-to-$10M mid-term path '
                                     'stacks $22M of exposure, so start at $10M or skip $7M [Trade Risk '
                                     'Guaranty — M68ZVWdgp9I @ 00:07:11]',
                                     'Lean on substitution drawback for mixed inventory. Commercially '
                                     'interchangeable goods under the same HTS qualify, and the speaker '
                                     'calls this route especially powerful [USA Customs Clearance — '
                                     'khfmXSwD3DE @ 00:02:48]',
                                     'Bundle multiple entries into one protest to save filing effort, but '
                                     'remember each entry still needs its own proof because there is no '
                                     'blanket claim [Great Lakes Customs Law — kBvWPMXLLgs @ 00:03:29]',
                                     'Do not trust 10-digit ABI queries alone, because they miss AD/CVD '
                                     'flags set at the 8-digit level [NCBFAA Educational Institute — '
                                     'CGsvr1SDN8s @ 01:19:50]']},
               'sop_steps': [{'step': 1,
                              'title': 'Pull and Tag Every Entry',
                              'action': 'Collect all CBP Form 7501 entry summaries and flag Chapter 99 '
                                        'lines by tariff program.',
                              'detail': 'Screen entry summaries for Chapter 99 HTS headings to isolate '
                                        'eligible lines [Ask The Customs Manager — xq8bHfr9ke8 @ '
                                        '00:00:20], and pull the 7501 entries as the first move of the '
                                        'drawback workflow [USA Customs Clearance — khfmXSwD3DE @ '
                                        '00:03:04].'},
                             {'step': 2,
                              'title': 'Route by Liquidation Status',
                              'action': 'Assign each entry to PSC, CAPE, protest, or court action based on '
                                        'its liquidation date.',
                              'detail': 'File PSCs within about 300 days of entry and before liquidation, '
                                        'and protests within 180 days of liquidation [Great Lakes Customs '
                                        'Law — kBvWPMXLLgs @ 00:01:41]. For liquidated IEEPA entries, '
                                        'expect CBP to require an entry-specific court order [Freightos — '
                                        'cIMBwZ9J60I @ 00:00:58].'},
                             {'step': 3,
                              'title': 'Enroll for Payment and File Electronically',
                              'action': 'Enroll in CBP electronic funds transfer and submit drawback '
                                        'claims through ACE only.',
                              'detail': 'Importers must enroll in CBP electronic funds transfer to receive '
                                        'refunds [Center for Strategic & International Studies — '
                                        'PJpF0M_rjYs @ 00:23:04], and drawback claims go through ACE '
                                        'because paper claims are not accepted [USA Customs Clearance — '
                                        'khfmXSwD3DE @ 00:03:46].'},
                             {'step': 4,
                              'title': 'Resize the Bond for Incoming 301 Layers',
                              'action': 'Forecast DTF with internal departments and size the bond at the '
                                        'tariff-loaded rate plus a buffer.',
                              'detail': 'Ask internal departments whether volume trends up, down or flat, '
                                        'then forecast at the IEEPA-level rate of about 25% plus standard '
                                        'duties with a 5% buffer, because 301 tariffs are coming [Trade '
                                        'Risk Guaranty — M68ZVWdgp9I @ 00:15:06].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Three refund lanes compete for the same Section 301 money, and '
                              'practitioners route it differently. Attorney Jason Wapanik of Great Lakes '
                              'Customs Law runs exclusion refunds two ways: a post summary correction '
                              'filed through the licensed broker, likely the original filer, within about '
                              '300 days of entry and before liquidation, or a protest due within 180 days '
                              'of liquidation, built entry by entry with proof the exclusion applies '
                              '[kBvWPMXLLgs @ 00:01:41]. USA Customs Clearance works a different clock and '
                              'pushes drawback instead: export, destroy under customs supervision, or use '
                              'the goods as components, match 7501 entries to exports, attach the Chapter '
                              '99 code, file in ACE, and recover up to 99% inside a five-year window '
                              '[khfmXSwD3DE @ 00:03:46]. Ask The Customs Manager draws a hard line on the '
                              'IEEPA side: Section 301 lines are not eligible for the IEEPA refund program '
                              "at all, and for unliquidated IEEPA entries the PSC route is now 'completely "
                              "forbidden,' so operators wait for CAPE [xq8bHfr9ke8 @ 00:05:19]. The "
                              'practical split: exclusion-driven 301 money moves through PSC or protest, '
                              'export-driven 301 money moves through drawback, and anyone trying to fold '
                              '301 lines into an IEEPA refund claim is filing in the wrong lane '
                              '[xq8bHfr9ke8 @ 00:03:20].',
                              'The sharpest split is over money already liquidated. Brightup, briefing the '
                              'International Housewares Association, reports Judge Eaton at the CIT '
                              'ordering refunds for all tariffs despite the 180-day protest statute, and '
                              'expects no clawback on phase one, where CBP accepted $90B of $127B in '
                              'claims and completed $23B [RaySaQSBqfE @ 00:02:16]. Freightos reads the '
                              'same moment as a trap: CBP is processing $80B for unliquidated entries, but '
                              'for liquidated entries it says it needs an entry-specific court order, '
                              'which means importers may need to sue in trade court [cIMBwZ9J60I @ '
                              '00:00:58]. Ask The Customs Manager draws the line at 180 days after '
                              'liquidation: inside it, file a protest as a hard deadline; beyond it, CBP '
                              'generally cannot refund and legal action is the only path [xq8bHfr9ke8 @ '
                              '00:06:00]. On CSIS, the panel flags the Justice Department arguing that '
                              'Trump v. CASA bars universal injunctions, leaving class actions as the '
                              "fallback, and warns that small importers lose because, in one panelist's "
                              "words, the department is banking on the thought that a lot of people won't "
                              'bother [PJpF0M_rjYs @ 00:26:15]. Operators reading Brightup sit tight on '
                              'phase one; operators reading Freightos and CSIS file protests inside 180 '
                              'days and prepare entry-specific trade court suits for anything already '
                              'liquidated.',
                              'Practitioners also split on how durable the new Section 301 layer is and '
                              "who pays what rate. On CSIS, Alan Wolff's constitutional argument is set "
                              'against Bill Reinsch, who expects narrower, fact-specific challenges to the '
                              "'unreasonable' finding, with Scott Miller siding with Reinsch [PJpF0M_rjYs "
                              '@ 00:18:02]. Trade Winds Report backs the durability case: Sections 232 and '
                              '301 require an investigation record, so they are slower to impose but '
                              'harder to overturn in court [xJrKO4dLXJ4 @ 00:04:47]. Cindy Allen of Simply '
                              'Trade predicts 301 will fare better in court than IEEPA but still expects '
                              'challenges [GSPaDDm0OVQ @ 00:06:30]. The rate map is where readings '
                              'collide. CSIS puts the forced-labor 301 at 12.5% for 54 economies and 10% '
                              'for the EU; Brightup calls the notice confusing and reads 16 economies, '
                              'including Canada and the EU, at 10% with the other 44 at 12.5% [RaySaQSBqfE '
                              '@ 00:22:08]. Allen counts more than 50 countries at 12.5%, dumped into '
                              "buckets, against an 'all 60' headline. Stacking is contested too: CSIS "
                              'describes the forced-labor 301 stacking on 232, turning 25% into 35% or '
                              '37.5%, while Brightup reads IEEPA and 122 exemptions carrying over with no '
                              "stacking on 232. Brightup's bottom line: cumulative 301 layers stack like a "
                              'cake and likely land between 30% and 40%.'],
               'table': {'caption': 'Competing Refund, Litigation and Exposure Playbooks Side by Side',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Recovering excluded Section 301 duties on China-origin entries',
                                   'File a post summary correction through the original broker within '
                                   'roughly 300 days, before liquidation',
                                   'File an entry-by-entry protest within 180 days of liquidation with '
                                   'proof the exclusion applies',
                                   'Great Lakes Customs Law ([kBvWPMXLLgs @ 00:01:41]); Great Lakes '
                                   'Customs Law ([kBvWPMXLLgs @ 00:02:26])'],
                                  ['Recovering 301 duties on goods that leave the country',
                                   'Unused merchandise drawback: match 7501 entries to exports and recover '
                                   'up to 99%',
                                   'Substitution drawback using commercially interchangeable goods with '
                                   'the same HTS, powerful for mixed inventory',
                                   'USA Customs Clearance ([khfmXSwD3DE @ 00:01:40]); USA Customs '
                                   'Clearance ([khfmXSwD3DE @ 00:02:33])'],
                                  ['Liquidated entries after the CIT refund order',
                                   "Brightup expects refunds to flow under Judge Eaton's order with no "
                                   'clawback expected',
                                   'CBP demands an entry-specific court order, so importers may need to '
                                   'sue in trade court',
                                   'International Housewares Association ([RaySaQSBqfE @ 00:02:16]); '
                                   'Freightos ([cIMBwZ9J60I @ 00:00:58])'],
                                  ['Unliquidated IEEPA entries waiting on a refund',
                                   'Traditional route is a post summary correction filed before the entry '
                                   'liquidates',
                                   'PSC is now completely forbidden, so wait for CAPE, still in restricted '
                                   'Stage 1',
                                   'Ask The Customs Manager ([xq8bHfr9ke8 @ 00:05:19]); Ask The Customs '
                                   'Manager ([xq8bHfr9ke8 @ 00:06:19])'],
                                  ['Legal durability of the forced-labor Section 301 layer',
                                   'Alan Wolff presses a broad constitutional argument against the '
                                   'authority itself',
                                   'Reinsch and Miller expect narrower fact-specific challenges to the '
                                   'unreasonable finding',
                                   'Center for Strategic & International Studies ([PJpF0M_rjYs @ '
                                   '00:18:02]); Center for Strategic & International Studies ([PJpF0M_rjYs '
                                   '@ 00:21:00])'],
                                  ['Reading the 10% versus 12.5% country buckets',
                                   'CSIS reads 12.5% for 54 economies and 10% for the EU',
                                   'Brightup reads 16 economies including Canada and EU at 10%, the other '
                                   '44 at 12.5%',
                                   'Center for Strategic & International Studies ([PJpF0M_rjYs @ '
                                   '00:14:59]); International Housewares Association ([RaySaQSBqfE @ '
                                   '00:22:08])'],
                                  ['Funding AD/CVD bond exposure when deposit rates can swing',
                                   'Post full and stacking collateral because AD/CVD liquidation runs 2-8 '
                                   'years',
                                   'TRG AD/CVD program swaps a higher premium for collateral for importers '
                                   'with strong financials',
                                   'Trade Risk Guaranty ([M68ZVWdgp9I @ 00:31:55]); Trade Risk Guaranty '
                                   '([M68ZVWdgp9I @ 00:34:19])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The AD/CVD failures carry the biggest dollar losses, and they start with '
                              'trusting the HTS number. Ask The Customs Manager walks through a $50K '
                              'aluminum container drawing a $150K bill, because orders follow a written '
                              'scope rather than the HS code, a broker sees 0% and clears, and a '
                              'post-clearance audit about a year later brings a retroactive 250% duty plus '
                              'interest plus false-declaration fines [Ze1pOvT4KsI @ 00:02:43]. Lisa Gelino '
                              'and Alexander Amdur at the NCBFAA Educational Institute put hard numbers on '
                              'the downside: a garlic importer hit at 367% owed $3.24M against a $50K '
                              'bond, producing a $2.8M loss, and a solar importer saw a 13.8% rate '
                              'deactivated to 238%, roughly $2.2M of exposure, a $300K sufficiency demand, '
                              'and suspected Korea transshipment [CGsvr1SDN8s @ 01:02:44]. The same '
                              'session warns that ABI queries at 10 digits miss 8-digit flags, and that AD '
                              'country of origin can differ from CBP origin, so Chinese cells in Mexican '
                              'panels stay subject [CGsvr1SDN8s @ 01:19:50]. Drawback does not rescue '
                              'these entries either: NCBFAA says there is no drawback on AD/CVD, and USA '
                              'Customs Clearance warns AD/CVD goods may be ineligible for 301 drawback '
                              "[khfmXSwD3DE @ 00:01:59]. Ask The Customs Manager's fix is manual: check "
                              'the AD registers for metal, wood, paper, plastics and chemicals, and get a '
                              'binding scope ruling before shipping.',
                              'Bond mistakes compound quietly until a letter or a claim lands. Travis '
                              'Smith of Trade Risk Guaranty warns that going up only one bond size fails '
                              'within 12 months nine times out of 10, and that a new bond does not reset '
                              "sufficiency because the past year's duties, taxes and fees still count "
                              '[M68ZVWdgp9I @ 00:07:11]. Mid-term moves are worse: stepping a bond from '
                              '$5M to $7M to $10M produces $22M of surety exposure plus wasted premium and '
                              'collateral risk, where starting at $10M was the best play and skipping $7M '
                              "the second best, and Smith's rule is not to change size mid-term unless "
                              'Customs requires it [M68ZVWdgp9I @ 00:24:31]. AD/CVD multiplies the drag, '
                              'since liquidation runs 2-8 years, deposit rates can move from 5% to 50%, '
                              'and collateral only comes back after every entry liquidates plus 120 days. '
                              'Freight & Trade flags the mindset errors behind these losses: treating the '
                              'bond as duty payment, waiting until arrival, assuming the broker takes on '
                              'responsibility, and confusing bond amount with premium, stressing the bond '
                              "is not insurance that eliminates the importer's responsibility [ez065LeX6vE "
                              "@ 00:04:37]. Trade Risk Guaranty's explainer closes the loop: the surety "
                              'pays up to the bond amount, and the importer remains liable to the surety '
                              '[P-dHB1oQLCI @ 00:02:12].',
                              'Refund cash is slower and narrower than the headline numbers suggest, and '
                              'every practitioner tracking it reports a different completion figure. '
                              'Brightup reports phase one at $90B accepted of $127B claimed with only '
                              '$23B, about 20%, completed, and phase two is exactly what the '
                              'administration is challenging [RaySaQSBqfE @ 00:45:52]. On CSIS, about $20B '
                              'had been paid against $166B estimated, importers must enroll in CBP '
                              'electronic funds transfer to get paid, and liquidation itself takes 312 '
                              'days [PJpF0M_rjYs @ 00:23:04]. Travis Smith saw the CAPE relief arrive '
                              'differently than TRG expected: instead of adjustments at liquidation, '
                              'accepted filers had all ACE entries reassessed between May 5 and May 7 to '
                              'standard duties plus 122, and Smith expects that relief to last only a '
                              'month or two before 301 arrives [M68ZVWdgp9I @ 00:18:57]. Cindy Allen adds '
                              'the operational drag: IEEPA stacking errors complicated refunds, the new '
                              '301 took effect at midnight after an end-of-day notice that left '
                              'programmers under 12 hours, and importers are now using refunds to pay the '
                              'new tariffs while class actions proceed [GSPaDDm0OVQ @ 00:10:33]. The '
                              'economics check is simple: a refund that arrives just as a new 301 layer '
                              'bills the same entries is cash recycled, not cash recovered.'],
               'table': {'caption': 'Firsthand Traps With Their Dollar Consequences',
                         'headers': ['Trap', 'What Went Wrong', 'Economics Check', 'Expert Source'],
                         'rows': [['AD/CVD scope missed because the HS code showed 0%',
                                   'Broker cleared the goods; a post-clearance audit a year later added '
                                   'retroactive 250% duty',
                                   'A $50K aluminum container turned into a $150K bill plus interest and '
                                   'fines',
                                   'Ask The Customs Manager ([Ze1pOvT4KsI @ 00:01:18]); Ask The Customs '
                                   'Manager ([Ze1pOvT4KsI @ 00:02:43])'],
                                  ['Undersized continuous bond behind a 367% garlic rate',
                                   'Importer owed $3.24M while only a $50K bond stood behind the entries',
                                   'Reported $2.8M loss on a single garlic exposure against that bond',
                                   'NCBFAA Educational Institute ([CGsvr1SDN8s @ 01:02:44])'],
                                  ['Solar deposit rate deactivated from 13.8% to 238%',
                                   'Suspected Korea transshipment pushed the entries onto the 238% rate',
                                   'About $2.2M of exposure and a $300K bond sufficiency demand followed',
                                   'NCBFAA Educational Institute ([CGsvr1SDN8s @ 01:11:34])'],
                                  ['Raising the bond only one size after an insufficiency letter',
                                   'Nine times out of 10 the new bond fails again within 12 months',
                                   "Past year's DTF still counts, so a new bond can start around 75% used",
                                   'Trade Risk Guaranty ([M68ZVWdgp9I @ 00:07:11]); Trade Risk Guaranty '
                                   '([M68ZVWdgp9I @ 00:06:32])'],
                                  ['Changing continuous bond size in the middle of the term',
                                   'Stepping $5M to $7M to $10M stacked liability across overlapping bonds',
                                   '$22M of surety exposure plus wasted premium versus starting at $10M',
                                   'Trade Risk Guaranty ([M68ZVWdgp9I @ 00:24:31]); Trade Risk Guaranty '
                                   '([M68ZVWdgp9I @ 00:27:52])'],
                                  ['Missing the 180-day protest window after liquidation',
                                   'Beyond 180 days CBP generally cannot refund, forcing legal action in '
                                   'court',
                                   'Small importers lose because DOJ is betting many will not bother suing',
                                   'Ask The Customs Manager ([xq8bHfr9ke8 @ 00:07:00]); Center for '
                                   'Strategic & International Studies ([PJpF0M_rjYs @ 00:26:56])'],
                                  ['Skipping the AD/CVD administrative review request in the anniversary '
                                   'month',
                                   'No review requested, so the deposit rate becomes the final duty',
                                   'Deposits are also owed retroactively to the preliminary date after the '
                                   'final order',
                                   'Trade Risk Guaranty ([38zRYvMd5Ps @ 00:18:04]); Trade Risk Guaranty '
                                   '([38zRYvMd5Ps @ 00:15:40])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Hold the Entry Until These Four Checks Clear',
                           'body': 'No AD/CVD-exposed or 301-stacked entry moves, and no refund dollar is '
                                   'written off, until each of these practitioner-tested checks is '
                                   'cleared.',
                           'items': ['Run AD/CVD exposure against the written scope and the AD registers '
                                     'for metal, wood, paper, plastics and chemicals, and get a binding '
                                     'scope ruling before shipping anything ambiguous [Ask The Customs '
                                     'Manager — Ze1pOvT4KsI @ 00:03:27].',
                                     'Query ABI at the 8-digit level as well as 10 digits, because '
                                     '10-digit queries miss 8-digit AD/CVD flags [NCBFAA Educational '
                                     'Institute — CGsvr1SDN8s @ 01:19:50].',
                                     'Size the bond from rolling 365-day DTF forecast at the higher tariff '
                                     'rate plus a 5% buffer, and skip intermediate sizes instead of '
                                     'stepping up one at a time [Trade Risk Guaranty — M68ZVWdgp9I @ '
                                     '00:15:06].',
                                     'Calendar every liquidation date and file protests inside 180 days, '
                                     'because past that window CBP generally cannot refund and only legal '
                                     'action remains [Ask The Customs Manager — xq8bHfr9ke8 @ '
                                     '00:06:00].']}}],
 'pull_quote': '"I think the Justice Department is banking on the thought that a lot of people won\'t '
               'bother, especially the small guys, because it\'s too much effort." Attributed to Center '
               'for Strategic & International Studies (PJpF0M_rjYs @ 00:26:15).',
 'diagram_id': 'diag-07',
 'action_checklist': ['Pull every CBP Form 7501 and sort entries by liquidation status first, because '
                      "liquidation is CBP's final determination and the refund route depends on it [Ask "
                      'The Customs Manager — xq8bHfr9ke8 @ 00:04:38].',
                      'For excluded Section 301 entries, file a PSC through the original broker within '
                      'about 300 days of entry, or a protest within 180 days of liquidation that can '
                      'bundle multiple entries but proves each one [Great Lakes Customs Law — kBvWPMXLLgs '
                      '@ 00:03:29].',
                      'For exported or destroyed 301 goods, match imports to exports, include the Chapter '
                      '99 code, file drawback in ACE within 5 years, and pursue accelerated payment of '
                      'about 4 weeks [USA Customs Clearance — khfmXSwD3DE @ 00:04:05].',
                      'Enroll in CBP electronic funds transfer before refunds release, since importers '
                      'must be enrolled to get paid [Center for Strategic & International Studies — '
                      'PJpF0M_rjYs @ 00:23:04].',
                      'On an insufficiency letter, act inside the 30 days and terminate the old bond at '
                      'least 15 days before that mark, sizing to forecast to avoid stacking liability '
                      '[Trade Risk Guaranty — M68ZVWdgp9I @ 00:11:07].',
                      'Report AD/CVD transshipment evasion through the EAPA TVR tool with the case number, '
                      'scheme description, evidence uploads and public versions of confidential files, and '
                      'claim a moiety award if net recovery occurs [U.S. Customs and Border Protection — '
                      'CXFkPqsyXnI @ 00:04:26].'],
 'statutory_citations': [{'title': 'Great Lakes Customs Law — 🆘 Section 301 Duty Refund (China Tariffs) '
                                   'via Protest or Post Summary Correction CBP/customs [00:01:41]',
                          'url': 'https://www.youtube.com/watch?v=kBvWPMXLLgs&t=101s',
                          'relevance': 'Primary practitioner testimony on PSC versus protest timing for '
                                       'Section 301 exclusion refunds.'},
                         {'title': 'Ask The Customs Manager — IEEPA Tariff Refunds: Unliquidated vs '
                                   "Liquidated Entry Status—What's the Difference? [00:06:00]",
                          'url': 'https://www.youtube.com/watch?v=xq8bHfr9ke8&t=360s',
                          'relevance': 'Primary practitioner testimony on the 180-day protest cutoff and '
                                       'liquidated-entry refund limits.'},
                         {'title': 'NCBFAA Educational Institute — Best Practices for Anti Dumping and '
                                   'Countervailing Duty AD CVD [00:24:39]',
                          'url': 'https://www.youtube.com/watch?v=CGsvr1SDN8s&t=1479s',
                          'relevance': 'Primary practitioner testimony on AD/CVD scope classification and '
                                       'bond-loss case figures.'},
                         {'title': 'Trade Risk Guaranty — Managing Open U.S. Customs Bond Liability [Full '
                                   'Webinar] [00:24:31]',
                          'url': 'https://www.youtube.com/watch?v=M68ZVWdgp9I&t=1471s',
                          'relevance': 'Primary practitioner testimony on bond sufficiency, liability '
                                       'stacking and AD/CVD collateral.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'khfmXSwD3DE',
                       'title': 'Section 301 Duty Drawback Explained',
                       'channel': 'USA Customs Clearance',
                       'author': 'USA Customs Clearance',
                       'text': 'Drawback claims generally must be filed within 5 years of the import date.',
                       'tip': 'Drawback claims generally must be filed within 5 years of the import date.',
                       'timestamp': 260,
                       'timestamp_seconds': 260,
                       'timestamp_label': '[00:04:20]',
                       'url': 'https://www.youtube.com/watch?v=khfmXSwD3DE&t=260s',
                       'markdown': '[00:04:20](https://www.youtube.com/watch?v=khfmXSwD3DE&t=260s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kBvWPMXLLgs',
                       'title': '🆘 Section 301 Duty Refund (China Tariffs) via Protest or Post Summary '
                                'Correction CBP/customs',
                       'channel': 'Great Lakes Customs Law',
                       'author': 'Great Lakes Customs Law',
                       'text': 'Protests are filed entry by entry, and while one protest can cover '
                               'multiple entries, there is no blanket claim.',
                       'tip': 'Protests are filed entry by entry, and while one protest can cover multiple '
                              'entries, there is no blanket claim.',
                       'timestamp': 209,
                       'timestamp_seconds': 209,
                       'timestamp_label': '[00:03:29]',
                       'url': 'https://www.youtube.com/watch?v=kBvWPMXLLgs&t=209s',
                       'markdown': '[00:03:29](https://www.youtube.com/watch?v=kBvWPMXLLgs&t=209s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PJpF0M_rjYs',
                       'title': "China's Retaliatory Tariffs, Section 301 Authorities, and Tariff Refund "
                                'Litigation',
                       'channel': 'Center for Strategic & International Studies',
                       'author': 'Center for Strategic & International Studies',
                       'text': 'I think the Justice Department is banking on the thought that a lot of '
                               "people won't bother, especially the small guys, because it's too much "
                               'effort.',
                       'tip': 'I think the Justice Department is banking on the thought that a lot of '
                              "people won't bother, especially the small guys, because it's too much "
                              'effort.',
                       'timestamp': 1575,
                       'timestamp_seconds': 1575,
                       'timestamp_label': '[00:26:15]',
                       'url': 'https://www.youtube.com/watch?v=PJpF0M_rjYs&t=1575s',
                       'markdown': '[00:26:15](https://www.youtube.com/watch?v=PJpF0M_rjYs&t=1575s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RaySaQSBqfE',
                       'title': 'Update on new “Forced Labor” Tariffs and other Tariff-Related '
                                'Developments',
                       'channel': 'International Housewares Association',
                       'author': 'International Housewares Association',
                       'text': 'We may have seen peak tariff that may be in our rear view mirrors now.',
                       'tip': 'We may have seen peak tariff that may be in our rear view mirrors now.',
                       'timestamp': 1808,
                       'timestamp_seconds': 1808,
                       'timestamp_label': '[00:30:08]',
                       'url': 'https://www.youtube.com/watch?v=RaySaQSBqfE&t=1808s',
                       'markdown': '[00:30:08](https://www.youtube.com/watch?v=RaySaQSBqfE&t=1808s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cIMBwZ9J60I',
                       'title': 'The $166B Refund Liquidation Trap #tariffs',
                       'channel': 'Freightos',
                       'author': 'Freightos',
                       'text': 'For liquidated entries, CBP says it needs an entry-specific court order.',
                       'tip': 'For liquidated entries, CBP says it needs an entry-specific court order.',
                       'timestamp': 58,
                       'timestamp_seconds': 58,
                       'timestamp_label': '[00:00:58]',
                       'url': 'https://www.youtube.com/watch?v=cIMBwZ9J60I&t=58s',
                       'markdown': '[00:00:58](https://www.youtube.com/watch?v=cIMBwZ9J60I&t=58s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'd6omeUFeZfA',
                       'title': 'U.S. Customs (CBP) Bonds Webcast Preview',
                       'channel': 'Law Office of Yuri Starikov, LLC',
                       'author': 'Law Office of Yuri Starikov, LLC',
                       'text': 'Poor customs credit can trigger a cash deposit requirement.',
                       'tip': 'Poor customs credit can trigger a cash deposit requirement.',
                       'timestamp': 294,
                       'timestamp_seconds': 294,
                       'timestamp_label': '[00:04:54]',
                       'url': 'https://www.youtube.com/watch?v=d6omeUFeZfA&t=294s',
                       'markdown': '[00:04:54](https://www.youtube.com/watch?v=d6omeUFeZfA&t=294s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'P-dHB1oQLCI',
                       'title': 'What is a U.S. Customs Import Bond?',
                       'channel': 'Trade Risk Guaranty',
                       'author': 'Trade Risk Guaranty',
                       'text': 'The surety pays up to the bond amount, and the importer remains liable to '
                               'the surety.',
                       'tip': 'The surety pays up to the bond amount, and the importer remains liable to '
                              'the surety.',
                       'timestamp': 132,
                       'timestamp_seconds': 132,
                       'timestamp_label': '[00:02:12]',
                       'url': 'https://www.youtube.com/watch?v=P-dHB1oQLCI&t=132s',
                       'markdown': '[00:02:12](https://www.youtube.com/watch?v=P-dHB1oQLCI&t=132s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ez065LeX6vE',
                       'title': 'What Is a Customs Bond  A Beginner’s Guide to Importing into the US',
                       'channel': 'Freight & Trade',
                       'author': 'Freight & Trade',
                       'text': "It is not insurance that eliminates the importer's responsibility.",
                       'tip': "It is not insurance that eliminates the importer's responsibility.",
                       'timestamp': 277,
                       'timestamp_seconds': 277,
                       'timestamp_label': '[00:04:37]',
                       'url': 'https://www.youtube.com/watch?v=ez065LeX6vE&t=277s',
                       'markdown': '[00:04:37](https://www.youtube.com/watch?v=ez065LeX6vE&t=277s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'M68ZVWdgp9I',
                       'title': 'Managing Open U.S. Customs Bond Liability [Full Webinar]',
                       'channel': 'Trade Risk Guaranty',
                       'author': 'Trade Risk Guaranty',
                       'text': "It is not a good idea to change your bond size mid-term unless you're "
                               'required to by customs.',
                       'tip': "It is not a good idea to change your bond size mid-term unless you're "
                              'required to by customs.',
                       'timestamp': 1672,
                       'timestamp_seconds': 1672,
                       'timestamp_label': '[00:27:52]',
                       'url': 'https://www.youtube.com/watch?v=M68ZVWdgp9I&t=1672s',
                       'markdown': '[00:27:52](https://www.youtube.com/watch?v=M68ZVWdgp9I&t=1672s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'M68ZVWdgp9I',
                       'title': 'Managing Open U.S. Customs Bond Liability [Full Webinar]',
                       'channel': 'Trade Risk Guaranty',
                       'author': 'Trade Risk Guaranty',
                       'text': "Don't forget 301's coming.",
                       'tip': "Don't forget 301's coming.",
                       'timestamp': 3575,
                       'timestamp_seconds': 3575,
                       'timestamp_label': '[00:59:35]',
                       'url': 'https://www.youtube.com/watch?v=M68ZVWdgp9I&t=3575s',
                       'markdown': '[00:59:35](https://www.youtube.com/watch?v=M68ZVWdgp9I&t=3575s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CXFkPqsyXnI',
                       'title': 'Steps to Submitting an Allegation - Enforce and Protect Act (EAPA) | '
                                'Office of Trade | CBP',
                       'channel': 'U.S. Customs and Border Protection',
                       'author': 'U.S. Customs and Border Protection',
                       'text': 'It is important to include as much information as possible pertaining to '
                               'the evasion scheme.',
                       'tip': 'It is important to include as much information as possible pertaining to '
                              'the evasion scheme.',
                       'timestamp': 266,
                       'timestamp_seconds': 266,
                       'timestamp_label': '[00:04:26]',
                       'url': 'https://www.youtube.com/watch?v=CXFkPqsyXnI&t=266s',
                       'markdown': '[00:04:26](https://www.youtube.com/watch?v=CXFkPqsyXnI&t=266s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ze1pOvT4KsI',
                       'title': 'Anti-Dumping Duties (ADD & CVD): The Hidden Customs Trap That Bankrupts '
                                'Importers',
                       'channel': 'Ask The Customs Manager',
                       'author': 'Ask The Customs Manager',
                       'text': 'A formal ruling is legally binding and protects you from surprise audits.',
                       'tip': 'A formal ruling is legally binding and protects you from surprise audits.',
                       'timestamp': 227,
                       'timestamp_seconds': 227,
                       'timestamp_label': '[00:03:47]',
                       'url': 'https://www.youtube.com/watch?v=Ze1pOvT4KsI&t=227s',
                       'markdown': '[00:03:47](https://www.youtube.com/watch?v=Ze1pOvT4KsI&t=227s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CGsvr1SDN8s',
                       'title': 'Best Practices for Anti Dumping and Countervailing Duty AD CVD',
                       'channel': 'NCBFAA Educational Institute',
                       'author': 'NCBFAA Educational Institute',
                       'text': "While HTS numbers are provided for guidance purposes, they're not "
                               'dispositive; the written scope of the order is dispositive.',
                       'tip': "While HTS numbers are provided for guidance purposes, they're not "
                              'dispositive; the written scope of the order is dispositive.',
                       'timestamp': 1479,
                       'timestamp_seconds': 1479,
                       'timestamp_label': '[00:24:39]',
                       'url': 'https://www.youtube.com/watch?v=CGsvr1SDN8s&t=1479s',
                       'markdown': '[00:24:39](https://www.youtube.com/watch?v=CGsvr1SDN8s&t=1479s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '38zRYvMd5Ps',
                       'title': 'Learn the Basics of Antidumping and Countervailing Duties [Full Webinar]',
                       'channel': 'Trade Risk Guaranty',
                       'author': 'Trade Risk Guaranty',
                       'text': 'Administrative reviews must be requested in the anniversary month, and if '
                               'no review is requested, the deposit rate becomes final.',
                       'tip': 'Administrative reviews must be requested in the anniversary month, and if '
                              'no review is requested, the deposit rate becomes final.',
                       'timestamp': 1084,
                       'timestamp_seconds': 1084,
                       'timestamp_label': '[00:18:04]',
                       'url': 'https://www.youtube.com/watch?v=38zRYvMd5Ps&t=1084s',
                       'markdown': '[00:18:04](https://www.youtube.com/watch?v=38zRYvMd5Ps&t=1084s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xJrKO4dLXJ4',
                       'title': 'After the Midterms, Can Congress Undo Tariffs? Follow One Toy',
                       'channel': 'Trade Winds Report',
                       'author': 'Trade Winds Report',
                       'text': 'Watch what gets exempted, not what gets announced.',
                       'tip': 'Watch what gets exempted, not what gets announced.',
                       'timestamp': 418,
                       'timestamp_seconds': 418,
                       'timestamp_label': '[00:06:58]',
                       'url': 'https://www.youtube.com/watch?v=xJrKO4dLXJ4&t=418s',
                       'markdown': '[00:06:58](https://www.youtube.com/watch?v=xJrKO4dLXJ4&t=418s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xq8bHfr9ke8',
                       'title': "IEEPA Tariff Refunds: Unliquidated vs Liquidated Entry Status—What's the "
                                'Difference?',
                       'channel': 'Ask The Customs Manager',
                       'author': 'Ask The Customs Manager',
                       'text': "Liquidation is CBP's final determination of duties owed on an import "
                               'entry.',
                       'tip': "Liquidation is CBP's final determination of duties owed on an import entry.",
                       'timestamp': 278,
                       'timestamp_seconds': 278,
                       'timestamp_label': '[00:04:38]',
                       'url': 'https://www.youtube.com/watch?v=xq8bHfr9ke8&t=278s',
                       'markdown': '[00:04:38](https://www.youtube.com/watch?v=xq8bHfr9ke8&t=278s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GSPaDDm0OVQ',
                       'title': 'Sad, Beautiful, Tragic: New Section 301 Tariffs | Cindy’s Version',
                       'channel': 'Simply Trade Podcast',
                       'author': 'Simply Trade Podcast',
                       'text': 'However, strictly looking at that from a customs law perspective, the '
                               'importers are the right refund recipients.',
                       'tip': 'However, strictly looking at that from a customs law perspective, the '
                              'importers are the right refund recipients.',
                       'timestamp': 651,
                       'timestamp_seconds': 651,
                       'timestamp_label': '[00:10:51]',
                       'url': 'https://www.youtube.com/watch?v=GSPaDDm0OVQ&t=651s',
                       'markdown': '[00:10:51](https://www.youtube.com/watch?v=GSPaDDm0OVQ&t=651s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'}]}
