from __future__ import annotations

CHAPTER_1 = {'id': 'Q1',
 'chapter_id': 'Q1',
 'chapter_number': 1,
 'question_number': 1,
 'slug': 'the-var-business-model',
 'question_prompt': 'What is a value-added reseller, how does it differ from an MSP, and what separates '
                    'VARs that win from those that stall?',
 'kicker': 'Q1 / THE BIG MONEY PLAYBOOKS',
 'title': 'The VAR Business Model',
 'subtitle': 'VAR vs. MSP roles, choosing an ERP or vendor partner, ISV engagement asks from VARs, carrier '
             'and TMS reseller programs, customer success hand-offs, customer case studies, and what '
             'high-performing resellers do before marketing',
 'layout_template': 'opportunity_overview',
 'reading_time_minutes': 15,
 'executive_summary': 'VAR operators agree the license is a thin-margin entry ticket and the money sits in '
                      'implementation, training, customization and support layered on top. Positive '
                      'Results says most software providers push over 80 percent of sales through VARs and '
                      'pay the VAR directly, while Phil Morettini warns VARs will not create demand for a '
                      "vendor. Steve Preda's XAPT case shows the upside of verticalizing a commodity "
                      'Microsoft ERP: $24 million in revenue and $14 million pre-tax profit, near 60 '
                      "percent margin. TC2's Ben Fox details how markups hide in shaved OEM discounts and "
                      'buried fees, and Stuart Sutton lays out a full license stack of setup fees, monthly '
                      'minimums, usage pricing and per-hour customization. The friction points: Scott Alan '
                      "Miller says a VAR's sales incentive overrides any advisory role, and Sheldon Needle "
                      'flags small, high-turnover VARs.',
 'key_metrics': [{'label': 'Share of software sales routed through VARs',
                  'metric': 'Share of software sales routed through VARs',
                  'value': 'Over 80 percent',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Positive Results states most software providers do over 80 percent of their '
                             'sales through value-added resellers, which compensate the VAR directly '
                             'instead of raising client monthly user fees.',
                  'source': 'Positive Results ([z6rVTIy-FOg @ 00:02:59])'},
                 {'label': 'XAPT pre-tax margin as a niche Microsoft ERP VAR',
                  'metric': 'XAPT pre-tax margin as a niche Microsoft ERP VAR',
                  'value': '$14 million pre-tax profit on $24 million revenue (almost 60 percent), 2015 '
                           'financials',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Steve Preda reports a Hungarian VAR that customized Navision for Caterpillar '
                             'and heavy-equipment dealers posted near-60 percent margins on a commodity '
                             'Microsoft ERP.',
                  'source': 'Steve Preda ([5n6g3xVFV88 @ 00:04:18])'},
                 {'label': 'Price lift from verticalized Salesforce customization',
                  'metric': 'Price lift from verticalized Salesforce customization',
                  'value': '25 per seat generic versus 250 per month customized (10x)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Preda, shopping for an investment-banking CRM around 2010, paid attention to '
                             'a firm that customized Salesforce for investment banks and charged ten times '
                             'the vanilla seat price for the same basic package.',
                  'source': 'Steve Preda ([5n6g3xVFV88 @ 00:05:29])'},
                 {'label': 'OEM discount shaved as the VAR markup',
                  'metric': 'OEM discount shaved as the VAR markup',
                  'value': '60 percent OEM discount passed through as 58 percent',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Ben Fox of TC2 explains that some VARs take their fee by reducing the OEM '
                             'discount a point or two instead of adding a percentage over net cost of '
                             'goods.',
                  'source': 'Staying Connected ([BJPNVL1CIiM @ 00:04:10])'}],
 'sections': [{'title': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['The operators converge on one blunt definition: a VAR resells someone '
                              "else's platform bundled with the labor that makes it work. Jim Ward, CEO of "
                              'BrainSell, says his firm sells software platforms and adds value by '
                              'supplying training, implementation, development and business-application '
                              'know-how, because vendors build good software but are not on the ground day '
                              'to day with its hard parts [Y3mGiwmy2l0 @ 00:01:19]. His line: software is '
                              'stupid and needs to be told what to do, so the VAR maps it onto people and '
                              'process. Jillian Craig of Eye on Tech lists the add-on forms as '
                              'customization, additional offerings, installation, and consulting or '
                              'design, and warns that small VARs often get pushed into buying through a '
                              'two-tier distribution model instead of direct [WEqXH4PuF8c @ 00:00:20]. '
                              'Sheldon Needle of CTS Guides frames VARs as independent companies reselling '
                              "a vendor's software under license, becoming the party that sells, installs "
                              'and trains the user [2tRDmrgGASk @ 00:00:00]. Steve Preda traces the model '
                              'to the early 90s, when SAP, Microsoft and Oracle dominated, smaller '
                              'developers struggled to sell, and system integrators began earning money by '
                              'customizing, training and consulting around those platforms, taking a small '
                              'margin on the license and bundling all services on top [5n6g3xVFV88 @ '
                              '00:02:09].',
                              'Everyone who touches the money agrees the license itself is thin and the '
                              'services are the profit engine. Preda says the original VARs made a small '
                              'margin on the software and sold their bundled services alongside it '
                              '[5n6g3xVFV88 @ 00:02:09]. Ben Fox of TC2 calls resale good for revenue but '
                              'a low-margin business, and says systems integrators and telecom carriers '
                              'wax and wane on VAR services depending on whether they are chasing revenue '
                              'growth or healthy margin that year [BJPNVL1CIiM @ 00:03:05]. Phil Morettini '
                              'of PTM Consulting tells vendors that VARs will not be motivated solely by '
                              'high product margins; what they market and sell very actively is their own '
                              'high-margin services, so a product that enables those services puts the '
                              'vendor in great shape with the channel [L1YsH5QkIus @ 00:01:22]. The flip '
                              'side is leverage over vendors: Positive Results claims most software '
                              'providers do over 80 percent of their sales through VARs, that the VAR is '
                              'compensated by the software company, and that it never charges the client '
                              'more on monthly user fees [z6rVTIy-FOg @ 00:02:59]. Fox adds that OEMs such '
                              'as Cisco run channel strategies and prefer to transact through partners '
                              'rather than directly, which makes VARs practically inevitable for '
                              'enterprise buyers sourcing from many manufacturers at once [BJPNVL1CIiM @ '
                              '00:01:16].',
                              'The third point of agreement is that winners pick a narrow lane and vet the '
                              'vendor hard before selling it. Ridge Consulting says low performers grab a '
                              'technology, sprint into multiple segments without checking long-term fit '
                              'and run short-term marketing, then scramble to survive when business and '
                              'technology cycles turn; high performers run a full strategic review with '
                              'vendor support, identify one segment with high strategic fit and build '
                              "tactics to dominate it [NbukIA2E8Nw @ 00:00:50]. Preda's XAPT story proves "
                              'the payoff: a Hungarian Microsoft ERP implementer customized Navision for '
                              'one Caterpillar dealer, got referred to another, and turned heavy-equipment '
                              'dealers into a global niche that Microsoft embraced, putting the firm on '
                              'stage with Steve Ballmer [5n6g3xVFV88 @ 00:03:26]. Positive Results screens '
                              'every partner on six factors: true cloud access from any device, '
                              'functionality tested against real customer use cases rather than developer '
                              'claims, easy integrations, simple user experience, a mobile-first build and '
                              'world-class security [z6rVTIy-FOg @ 00:00:42]. Morettini insists the '
                              'vendor, not the VAR, must position the product and create demand, and must '
                              'have sold it successfully direct first so it has best practices to hand '
                              'partners, because VARs will not create demand or spearhead a new '
                              'marketplace for anyone [L1YsH5QkIus @ 00:02:38].'],
               'table': {'caption': 'Where the VAR operators line up on the core business model',
                         'headers': ['Consensus Point',
                                     'What Practitioners Say',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['The value add is the services layer, not the box',
                                   'BrainSell sells platforms, then supplies training, implementation, '
                                   'development and business-application understanding',
                                   'Staff and price the services practice as the real product you sell',
                                   'BrainSell ([Y3mGiwmy2l0 @ 00:00:37])'],
                                  ['Vendors cannot implement their own software well in the field',
                                   'Vendors build good software but are not on the ground day to day with '
                                   'its hard parts',
                                   'Pitch hands-on implementation expertise as the reason buyers should '
                                   'skip going direct',
                                   'BrainSell ([Y3mGiwmy2l0 @ 00:01:19])'],
                                  ['License margin is thin while bundled services carry the profit',
                                   'Original VARs made a small margin on SAP or Microsoft software and '
                                   'bundled services on top',
                                   'Never build the P&L on license margin alone; services must carry the '
                                   'profit',
                                   'Steve Preda ([5n6g3xVFV88 @ 00:02:09])'],
                                  ['Software vendors depend heavily on the reseller channel for revenue',
                                   'Most software providers do over 80 percent of their sales through '
                                   'value-added resellers',
                                   'Use that channel dependence as leverage when negotiating vendor '
                                   'partnership terms and support',
                                   'Positive Results ([z6rVTIy-FOg @ 00:02:59])'],
                                  ['VARs fulfill demand but will not create it for vendors',
                                   'Vendors must position the product and create demand; VARs sell into '
                                   'existing customer bases',
                                   'Favor vendors that already generate demand and pull buyers toward your '
                                   'services',
                                   'Phil Morettini ([L1YsH5QkIus @ 00:01:04])'],
                                  ['One high-fit segment beats spraying across many markets at once',
                                   'High performers complete a strategic review and choose one segment '
                                   'they can dominate',
                                   'Commit to a single vertical before launching any short-term marketing '
                                   'activity at all',
                                   'Ridge Consulting ([NbukIA2E8Nw @ 00:00:50])'],
                                  ["Vet the vendor's product hard before adding it to the line",
                                   'Test functionality against real customer use cases, not developer '
                                   'claims, across six screening factors',
                                   'Run your own use-case tests before any product earns a spot on your '
                                   'line card',
                                   'Positive Results ([z6rVTIy-FOg @ 00:00:42])']]}},
              {'title': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["Ben Fox of TC2 breaks down exactly how the VAR's cut gets taken, and it is "
                              'rarely one clean number. The markup is the charge for VAR services, applied '
                              'either as a percentage over net cost of goods or by shaving the OEM '
                              'discount: if the OEM gives 60 percent off, the VAR passes through 58 '
                              '[BJPNVL1CIiM @ 00:04:10]. Fox stresses that a one percent markup on cost '
                              'and a one percent cut to the discount sound identical but land very '
                              'differently on the final price, and that the least transparent model simply '
                              'quotes a net discount per OEM so nobody sees the margin [BJPNVL1CIiM @ '
                              '00:04:42]. Markups also float by country, by OEM, and by whether a '
                              'distributor sits between VAR and manufacturer, which lines up with Eye on '
                              "Tech's point that small VARs get routed through two-tier distribution and "
                              "only mark up the distributor's product a small amount [WEqXH4PuF8c @ "
                              "00:01:33]. Fox's checklist of fees that get buried includes import duties, "
                              'customs clearance, import broker fees, exchange-rate hedging, extra '
                              'logistics layers and management fees; only shipping and sales tax should '
                              'ride on top [BJPNVL1CIiM @ 00:05:51]. On recurring cloud licenses, Positive '
                              'Results says the vendor pays the VAR, leaving client per-user fees '
                              'untouched [z6rVTIy-FOg @ 00:02:59].',
                              "Stuart Sutton's Full Circle TMS walkthrough lays out the most granular VAR "
                              'license structure of any operator. Applicants must be non-transportation '
                              'entities so subscribers trust their data stays away from competitors, they '
                              'get a geographic area or vertical, their office must sit inside that '
                              'territory, and the product is rebranded to look like theirs; the license is '
                              'kept only by generating sufficient business within the first two years '
                              '[yasPH-UlTQo @ 00:03:43]. The vendor bills the VAR a one-time setup and '
                              'training cost, a monthly VAR fee, a wholesale price on subscriber usage, '
                              'on-demand support charges above a threshold, and cost-plus-management-fee '
                              'pay for any dedicated developer, who stays a Full Circle employee that the '
                              'VAR cannot poach [yasPH-UlTQo @ 00:07:26]. The VAR earns back through a '
                              'setup and training fee, a minimum monthly charge, module-based usage fees, '
                              'paid extra training and per-hour customization work [yasPH-UlTQo @ '
                              '00:08:10]. Preda shows what customization does to price: generic Salesforce '
                              'ran 25 per seat, while a firm that tailored it for investment banks charged '
                              '250 a month for the same basic package and he judged it clearly better '
                              '[5n6g3xVFV88 @ 00:05:29]. XAPT later spun off its customization arm into a '
                              'US-headquartered company of 450 employees, three times the original '
                              'business [5n6g3xVFV88 @ 00:07:04].',
                              'The day-to-day motion runs on fast qualification, joint deals and adoption '
                              'follow-through. VAR panelists at Channel Marketing Academy want vendors to '
                              'hand them ballpark tiers, such as entry, medium and hard implementations at '
                              'roughly a month and a half, six months and two years, because a customer '
                              'who will spend $5,000 may balk at $50,000 and the VAR will not risk the '
                              'embarrassment of presenting an unpriced product [vLO0gA3TgxE @ 00:02:14]. '
                              'They want a 15-minute pitch and a one-page cheat sheet, not an hour-long '
                              'demo. Brian Tanney of GetWireless, grown from two people in a basement to '
                              'over 90 team members in 25 years, describes a VAR-led program being '
                              'architected with AT&T where VARs bring deals in and either bill the '
                              'hardware on their own paper or run it on AT&T paper with the buy-down '
                              "showing on the customer's bill [-gG3jIROESw @ 00:03:27], alongside six "
                              'state and local contracts and a GSA federal contract [-gG3jIROESw @ '
                              "00:02:42]. Atlassian's partner customer-success program checks deployment "
                              'after purchase and again four months before license expiry; one quarter it '
                              'flagged 20 at-risk high-volume customers, remediated eight, saved over '
                              '250,000 in revenue and lifted renewals 5 percent, and it names failure to '
                              'go live in production as the top reason customers do not renew [4qYKEjVIAjc '
                              '@ 00:00:57].'],
               'table': {'caption': 'VAR pricing, fee and pipeline mechanics with the exact numbers '
                                    'operators quote',
                         'headers': ['Mechanic / Tool',
                                     'Exact Number or Rule',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Discount-shave markup taken off the OEM discount',
                                   'A 60 percent OEM discount passed through to the customer as 58 percent',
                                   'Know whether markup sits on cost or off discount; the net effect '
                                   'differs',
                                   'Staying Connected ([BJPNVL1CIiM @ 00:04:10])'],
                                  ['Fee containment on resale quotes and contracts',
                                   'Only hardware shipping and sales tax should sit above product cost '
                                   'plus markup',
                                   'Strip import duties, broker, hedging, logistics and management fees '
                                   'out of every quote',
                                   'Staying Connected ([BJPNVL1CIiM @ 00:05:51])'],
                                  ['Vendor-side cost stack on a VAR license',
                                   'One-time setup and training, monthly VAR fee, wholesale usage price, '
                                   'overage support, cost-plus developer',
                                   'Model every vendor charge before setting the subscriber fee structure '
                                   'and margins',
                                   'Stuart Sutton ([yasPH-UlTQo @ 00:07:26])'],
                                  ['VAR-side revenue stack charged to subscribers',
                                   'Setup and training fee, minimum monthly, module usage fees, extra '
                                   'training, hourly customization',
                                   'Mirror the vendor cost stack and set a floor so tiny accounts stay '
                                   'profitable',
                                   'Stuart Sutton ([yasPH-UlTQo @ 00:08:10])'],
                                  ['Vertical customization premium on a commodity platform',
                                   'Generic Salesforce at 25 per seat versus 250 per month customized for '
                                   'investment banks',
                                   'Customize one platform for one niche, the way the investment-bank '
                                   'specialist hit 10x pricing',
                                   'Steve Preda ([5n6g3xVFV88 @ 00:05:29])'],
                                  ['Implementation ballpark tiers requested from every vendor',
                                   'Entry, medium and hard tiers at about a month and a half, six months '
                                   'and two years',
                                   'Demand ballpark tiers from vendors before ever presenting their '
                                   'product to a customer',
                                   'Channel Marketing Academy ([vLO0gA3TgxE @ 00:01:38])'],
                                  ["Adoption checkpoints run jointly with the vendor's success team",
                                   'Check deployment after purchase and again four months before the '
                                   'license expires',
                                   'Catch at-risk renewals early; Atlassian saved over 250,000 and gained '
                                   '5 percent renewals',
                                   'Summer Zaldivar ([4qYKEjVIAjc @ 00:00:36])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Margin and Pipeline Moves Operators Actually Run',
                           'body': 'Small levers the practitioners pull to protect margin, qualify vendors '
                                   'fast and turn happy customers into sales assets.',
                           'items': ["Force every VAR quote to break out whatever is lumped under 'taxes'; "
                                     'Fox has seen importation and customs fees disguised as taxes, and '
                                     'logistics and tax variance between VARs can exceed markup variance '
                                     '[Staying Connected — BJPNVL1CIiM @ 00:08:17].',
                                     'Charge a minimum monthly amount so a subscriber whose usage fees '
                                     'fall below the cost of cutting an invoice still pays its way [Stuart '
                                     'Sutton — yasPH-UlTQo @ 00:08:10].',
                                     'If a vendor refuses a budgetary number until it talks to the client, '
                                     'do not present it; a $50,000 surprise on a $5,000 buyer embarrasses '
                                     'the VAR [Channel Marketing Academy — vLO0gA3TgxE @ 00:02:14].',
                                     'Record customer case-study calls on Riverside.fm for separate '
                                     'per-person video and audio tracks plus a transcript, edit in CapCut, '
                                     'and book at least an hour, with 90 minutes better [Tom Bruining — '
                                     'meEqyWq6yX0 @ 00:07:33].']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock a niche and vet the platform',
                              'action': 'Choose one segment with high strategic fit and test the vendor '
                                        'against real customer use cases before signing.',
                              'detail': 'High performers complete a full strategic review and pick a '
                                        'segment they can dominate [Ridge Consulting — NbukIA2E8Nw @ '
                                        '00:00:50]; Positive Results builds use cases from its customers '
                                        'and tests function and completeness instead of trusting developer '
                                        'claims [Positive Results — z6rVTIy-FOg @ 00:00:42].'},
                             {'step': 2,
                              'title': 'Extract the vendor cheat sheet and ballparks',
                              'action': 'Get a 15-minute pitch, a one-page cheat sheet and entry, medium '
                                        'and hard implementation ballparks before presenting.',
                              'detail': 'The sheet should list products the vendor works and does not work '
                                        'with, industry sweet spots, minimum requirements and customer '
                                        'examples [Channel Marketing Academy — vLO0gA3TgxE @ 00:03:22], '
                                        'with tiered timelines of roughly a month and a half, six months '
                                        'and two years [Channel Marketing Academy — vLO0gA3TgxE @ '
                                        '00:01:38].'},
                             {'step': 3,
                              'title': 'Build the fee stack against vendor costs',
                              'action': 'Price setup and training, a monthly minimum, module usage and '
                                        'hourly customization so they cover every vendor charge.',
                              'detail': 'Sutton tells VARs to understand their own costs and set fee '
                                        'structures to hit their profitability goals [Stuart Sutton — '
                                        'yasPH-UlTQo @ 00:05:17], billing per-hour customization to offset '
                                        'the dedicated programming resource [Stuart Sutton — yasPH-UlTQo @ '
                                        '00:08:25].'},
                             {'step': 4,
                              'title': 'Drive adoption through to renewal',
                              'action': 'Set up and train new subscribers, follow up hard in the first '
                                        'months, and re-check deployment four months before license '
                                        'expiry.',
                              'detail': 'Sutton calls initial setup, training and the first few months '
                                        'critical to long-term subscriber success [Stuart Sutton — '
                                        'yasPH-UlTQo @ 00:04:31]; Atlassian checks deployment after '
                                        'purchase and again four months before the license expires [Summer '
                                        'Zaldivar — 4qYKEjVIAjc @ 00:00:36].'}]},
              {'title': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The money question splits the field. Positive Results tells buyers flatly '
                              'that value-added resellers never charge more for monthly user fees because '
                              'the VAR is compensated by the software company, and claims most software '
                              'providers do over 80 percent of their sales through VARs [z6rVTIy-FOg @ '
                              '00:02:59]. Eye on Tech frames it the other way: VARs mark up the '
                              "distributor's product a small amount and cannot control the cost of what "
                              'they sell [WEqXH4PuF8c @ 00:01:33]. Ben Fox of TC2, speaking on Staying '
                              'Connected, treats the markup as the actual charge for VAR services and '
                              'splits it into two mechanics: a straight percentage on the net cost of '
                              'goods, or a quiet haircut to the OEM discount, where a 60 percent OEM '
                              'discount becomes 58 percent by the time it reaches the buyer [BJPNVL1CIiM @ '
                              '00:04:10]. Fox stresses that the two sound identical yet hit the invoice '
                              'differently, and that the least transparent VARs simply quote a net '
                              'discount per OEM with no visible markup. Full Circle TMS, pitched by Stuart '
                              'Sutton, runs a fourth model: the vendor bills the VAR a wholesale price and '
                              'expects the VAR to mark up what it sells [yasPH-UlTQo @ 00:07:26].',
                              'On margins, the practitioners report opposite worlds. Steve Preda pulled '
                              'the last public financials of XAPT, the Hungarian Microsoft ERP reseller '
                              'founded by Zoltan Schwartz: 24 million dollars in revenue and 14 million '
                              'dollars profit before tax, almost a 60 percent net margin, earned by '
                              'customizing a commodity Microsoft ERP for Caterpillar and heavy equipment '
                              "dealers [5n6g3xVFV88 @ 00:04:18]. Preda's read is that the margin came from "
                              'inventing the customization, not the license. A second data point comes '
                              "from Preda's investment banking days: a plain Salesforce seat at 25 a month "
                              'versus a niche firm charging 250 a month for the same base package '
                              'customized for investment banks, a 10x price point purely from vertical '
                              'tailoring [5n6g3xVFV88 @ 00:05:29]. Ben Fox describes resale as the '
                              'opposite: good for revenue but a low margin business, which is why systems '
                              'integrators and telecom carriers wax and wane on pushing it depending on '
                              'whether they are chasing growth or margin [BJPNVL1CIiM @ 00:03:05]. Eye on '
                              'Tech goes further, reporting that VARs are finding it harder to stay in the '
                              'market as margins, revenue and competitive positions shift, and are '
                              'migrating toward an MSP role [WEqXH4PuF8c @ 00:02:13].',
                              'Identity and territory are the third fault line. Scott Alan Miller of SAM '
                              'IT holds a hard line: once a VAR, always a VAR, any MSP work is just part '
                              'of the value add, and a reseller presenting itself purely as an MSP is '
                              'misleading to the point of being questionably ethical or legal, because the '
                              'sales side is paid to represent the vendor, not the customer [bek-1YEtW80 @ '
                              '00:03:15]. Eye on Tech treats the MSP shift as a survival move rather than '
                              'a disclosure problem. On customization ownership, the playbooks diverge '
                              'sharply. XAPT built its own NAXT vertical layer and eventually spun the '
                              'customization business into a United States company with 450 employees, '
                              'roughly three times the size of the original business, per Steve Preda '
                              '[5n6g3xVFV88 @ 00:07:04]. Full Circle TMS closes that path off: any '
                              'dedicated developer must be a Full Circle employee or contractor billed to '
                              'the VAR at cost plus a management fee, the vendor owns all IP, and the VAR '
                              'cannot recruit vendor staff, though it keeps prioritization control '
                              '[yasPH-UlTQo @ 00:05:49]. Ridge Consulting adds the segment question: high '
                              'performers pick one segment with high strategic fit and, with vendor '
                              'support, plan tactics to dominate it [NbukIA2E8Nw @ 00:01:06].'],
               'table': {'caption': 'Competing VAR playbooks side by side',
                         'headers': ['Fault Line', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Who pays the VAR on software subscriptions',
                                   'Vendor compensates the VAR; customer pays no more on monthly user fees',
                                   'VAR marks up the distributor product a small amount and cannot control '
                                   'cost',
                                   'Positive Results ([z6rVTIy-FOg @ 00:02:59]); Eye on Tech ([WEqXH4PuF8c '
                                   '@ 00:01:33])'],
                                  ['How the resale markup is actually calculated',
                                   'Straight percentage markup applied to the net cost of goods sold',
                                   'Shave the OEM discount, for example a 60 percent discount cut to 58 '
                                   'percent',
                                   'Staying Connected ([BJPNVL1CIiM @ 00:04:10])'],
                                  ['Margin profile of the VAR business model',
                                   'Vertical customization of Microsoft ERP produced almost 60 percent net '
                                   'margin',
                                   'Resale is good for revenue but runs as a low margin business',
                                   'Steve Preda ([5n6g3xVFV88 @ 00:04:18]); Staying Connected '
                                   '([BJPNVL1CIiM @ 00:03:05])'],
                                  ['VAR versus MSP positioning and disclosure',
                                   'Once a VAR always a VAR; MSP work sits inside the value add',
                                   'VARs squeezed on margins are transitioning toward more of an MSP role',
                                   'samit ([bek-1YEtW80 @ 00:01:34]); Eye on Tech ([WEqXH4PuF8c @ '
                                   '00:02:13])'],
                                  ['Who owns the customization and the developers',
                                   'Build your own vertical layer, then spin it off as a standalone '
                                   'company',
                                   'Vendor employs dedicated developers, bills the VAR cost plus a '
                                   'management fee, keeps all IP',
                                   'Steve Preda ([5n6g3xVFV88 @ 00:07:04]); Stuart Sutton ([yasPH-UlTQo @ '
                                   '00:05:49])'],
                                  ['Market focus: one niche segment versus broad coverage',
                                   'Pick one segment with high strategic fit and dominate it with vendor '
                                   'support',
                                   'Low performers grab multiple segments without checking long-term fit '
                                   'and later scramble',
                                   'Ridge Consulting ([NbukIA2E8Nw @ 00:01:06])'],
                                  ['Whose paper the hardware deal is written on',
                                   'VAR builds the hardware deal independently on its own paper',
                                   'Deal goes down AT&T paper and the customer still sees the hardware '
                                   'buy-down on the bill',
                                   'AT&T Business ([-gG3jIROESw @ 00:03:41])']]}},
              {'title': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['Phil Morettini says many software management teams get off on the wrong '
                              'foot with the VAR channel, and in the worst cases it ends in failure of the '
                              'company. The core trap: VARs will not create demand, will not spearhead a '
                              'new marketplace, and will not be motivated solely by high product margins; '
                              'they push their own high-margin services, so the product has to be the '
                              "enabler of those services. Morettini's rule is that no one can sell your "
                              'product if you cannot, so sell directly and successfully first, never take '
                              'a sale direct to grab a few extra points, and never over-distribute by '
                              'assigning too many VARs in one local area, because brutal competition '
                              'strips out the profit margin and the incentive to sell [L1YsH5QkIus @ '
                              '00:03:16]. Ridge Consulting documents the reseller-side version: low '
                              'performers pick a technology, grab multiple market segments without '
                              'checking long-term fit, and launch short-term marketing, which works until '
                              'later business and technology cycles leave them in a painful scramble to '
                              'survive, if not outright disaster [NbukIA2E8Nw @ 00:00:15]. On the Channel '
                              'Marketing Academy panel, a VAR states they will not even present a vendor '
                              'that refuses budgetary numbers, because a 50,000 dollar surprise to a 5,000 '
                              'dollar client is embarrassing [vLO0gA3TgxE @ 00:02:14].',
                              'Operational traps hit both buyers and VARs. Sheldon Needle of CTS Guides '
                              'warns that VARs are often small organizations with heavy turnover, may lack '
                              'experience in your industry or in applications like EDI, CRM or HR, and '
                              'some vendors will not back you up by assigning another VAR when one '
                              'underperforms [2tRDmrgGASk @ 00:00:38]. The worst case is a staff change '
                              'mid-project that leaves the customer high and dry. Ben Fox lists the fee '
                              'leakage: import duties, customs clearance fees, import broker fees, '
                              'exchange rate hedging, extra logistics layers and extra management fees, '
                              'when the only costs above product plus markup should be hardware shipping '
                              'and sales taxes [BJPNVL1CIiM @ 00:05:51]. Fox has seen the variation in '
                              'logistics, shipping and even taxes between VARs exceed the variation in the '
                              'markup itself, and has caught importation and customs fees disguised as '
                              'taxes in quotes. Geographic coverage is the other trap: without an '
                              'in-country entity licensed to sell the product, the customer ends up as '
                              'importer of record, which defeats the purpose of hiring a VAR. Stuart '
                              "Sutton's Full Circle model adds on-demand support charges once a VAR "
                              'exceeds a support threshold, and pulls the license from VARs that fail to '
                              'generate sufficient business within two years [yasPH-UlTQo @ 00:03:59].',
                              "Adoption is where renewals die. Atlassian's customer success team, "
                              'presented by Summer Zaldivar, reports that the primary reason customers do '
                              'not renew is failing to go live into production; last quarter they flagged '
                              '20 high-volume customers at risk, remediated 8 by connecting them with '
                              'premier support, saved over 250,000 in revenue and lifted the renewal rate '
                              'by 5 percent [4qYKEjVIAjc @ 00:00:36]. Their ask of partners is to collect '
                              'feedback at purchase: deployed into production, active users, more to add, '
                              'business requirements met, blockers, documentation needs; Atlassian then '
                              'checks back four months before the license expires. Stuart Sutton reaches '
                              'the same conclusion from the VAR seat: initial setup and training are '
                              'critical to long-term subscriber success, the first few months are '
                              'critical, and the VAR must keep following up until the customer runs their '
                              'entire business on the platform [yasPH-UlTQo @ 00:04:31]. Sutton also tells '
                              'VARs to charge a minimum monthly amount in case usage fees fall below the '
                              'cost of cutting an invoice. Positive Results claims the payoff of '
                              'process-first implementation: never more than a quarter percent annual '
                              "attrition in over 25 years [z6rVTIy-FOg @ 00:03:18]. AT&T's Shiraz Asan "
                              'reports the same pattern: when the partners work well together, customers '
                              'stay much longer and do not turn away [-gG3jIROESw @ 00:02:10].'],
               'table': {'caption': 'Firsthand VAR failure modes and the economics check for each',
                         'headers': ['Failure Mode',
                                     'What Practitioners Saw Or Warn',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Expecting VARs to create demand for a new product',
                                   'VARs will not create demand or spearhead a new marketplace for the '
                                   'vendor',
                                   'Sell directly and successfully first, then hand proven best practices '
                                   'to partners',
                                   'Phil Morettini ([L1YsH5QkIus @ 00:01:04])'],
                                  ['Over-distributing with too many VARs in one local area',
                                   'Brutal competition between channel partners strips the profit margin '
                                   'out of the sale',
                                   'Limit VAR count per local area so partners keep their incentive to '
                                   'sell',
                                   'Phil Morettini ([L1YsH5QkIus @ 00:03:16])'],
                                  ['Launching marketing before strategy on the reseller side',
                                   'Low performers launch short-term campaigns, then face a painful '
                                   'scramble to survive',
                                   'Complete a full strategic review and pick one high-fit segment before '
                                   'spending',
                                   'Ridge Consulting ([NbukIA2E8Nw @ 00:00:15])'],
                                  ['Hidden fees stacked on top of the agreed markup',
                                   'Import duties, broker fees, hedging and management fees appear beyond '
                                   'the markup',
                                   'Only shipping and sales taxes should sit above product cost plus '
                                   'markup',
                                   'Staying Connected ([BJPNVL1CIiM @ 00:05:51])'],
                                  ['Small VAR with staff turnover in the middle of a project',
                                   'A staff change during the project leaves the customer high and dry',
                                   'Vet the VAR separately from the software because vendors may not '
                                   'reassign you',
                                   'Sheldon Needle ([2tRDmrgGASk @ 00:01:43])'],
                                  ['Customers never going live into production after purchase',
                                   'Primary reason customers do not renew; 20 flagged at risk and 8 '
                                   'remediated',
                                   'Remediation saved over 250,000 and lifted the renewal rate by 5 '
                                   'percent',
                                   'Summer Zaldivar ([4qYKEjVIAjc @ 00:00:57])'],
                                  ['Usage fees too small to justify cutting an invoice',
                                   "Low-usage subscribers can bill below the VAR's own cost of invoicing "
                                   'them',
                                   'Charge a minimum monthly amount plus one-time setup and training fees',
                                   'Stuart Sutton ([yasPH-UlTQo @ 00:08:10])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Kill Switches Before You Scale the Channel',
                           'body': 'Each gate comes straight from a practitioner-reported loss; fail any '
                                   'one and the channel bleeds margin, presentations, or renewals.',
                           'items': ['Do not launch a VAR channel until the product sells direct, because '
                                     'no one can sell your product if you cannot [Phil Morettini — '
                                     'L1YsH5QkIus @ 00:02:18].',
                                     'Publish entry, medium and heavy implementation ballparks, such as a '
                                     'month and a half, six months and two years, or VARs will not put you '
                                     'in front of clients [Channel Marketing Academy — vLO0gA3TgxE @ '
                                     '00:01:38].',
                                     'Demand a written markup definition and a broken-out tax line on '
                                     'every quote so customs and import fees cannot hide under taxes '
                                     '[Staying Connected — BJPNVL1CIiM @ 00:08:32].',
                                     'Track go-live into production and active users for every customer '
                                     'from purchase, since failing to go live is the primary non-renewal '
                                     'driver [Summer Zaldivar — 4qYKEjVIAjc @ 00:00:57].']}}],
 'pull_quote': '"Software is stupid. It needs to be told what to do." — Jim Ward, BrainSell (Y3mGiwmy2l0 @ '
               '00:01:36).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Build a one-page partner cheat sheet listing products you work with, products you '
                      'do not, industry sweet spots, minimum requirements and sample customers [Channel '
                      'Marketing Academy — vLO0gA3TgxE @ 00:03:22].',
                      'Cap the vendor intro at a 15-minute elevator pitch covering who uses it, why, and '
                      'what problem it solves instead of an hour-long demo [Channel Marketing Academy — '
                      'vLO0gA3TgxE @ 00:02:55].',
                      'Send potential VARs a matrix of every OEM and country you need and make them fill '
                      'in their specific in-country coverage [Staying Connected — BJPNVL1CIiM @ 00:07:17].',
                      'Solicit quotes from multiple VARs on each transaction even after a master '
                      'agreement, comparing logistics, shipping and tax lines, not just markup [Staying '
                      'Connected — BJPNVL1CIiM @ 00:08:02].',
                      'Vet every vendor against six filters before signing: true cloud, functionality '
                      'tested on real customer use cases, integrations, user experience, mobility and '
                      'security [Positive Results — z6rVTIy-FOg @ 00:00:23].',
                      'Pick a single industry niche and customize the base platform for it, the way XAPT '
                      'turned Microsoft ERP into a Caterpillar dealer solution [Steve Preda — 5n6g3xVFV88 '
                      '@ 00:03:26].'],
 'statutory_citations': [{'title': 'Steve Preda — Value-Added Reseller | The ProfServ Traction Podcast '
                                   '[00:04:18]',
                          'url': 'https://www.youtube.com/watch?v=5n6g3xVFV88&t=258s',
                          'relevance': 'Primary practitioner testimony on the XAPT vertical customization '
                                       'play producing almost 60 percent net margin on 24 million dollars '
                                       'of revenue.'},
                         {'title': 'Staying Connected — Get the Most Value from Value Added Resellers '
                                   '[00:04:10]',
                          'url': 'https://www.youtube.com/watch?v=BJPNVL1CIiM&t=250s',
                          'relevance': 'Primary practitioner testimony on VAR markup mechanics, discount '
                                       'reduction, hidden fees and multi-VAR quoting.'},
                         {'title': 'Phil Morettini — Selling and Marketing Software Through the VAR '
                                   'Channel -Morettini on Management Video Edition [00:03:16]',
                          'url': 'https://www.youtube.com/watch?v=L1YsH5QkIus&t=196s',
                          'relevance': 'Primary practitioner testimony on vendor-side channel failures, '
                                       'demand creation and over-distribution.'},
                         {'title': 'Stuart Sutton — Value Added Reseller Overview [00:07:26]',
                          'url': 'https://www.youtube.com/watch?v=yasPH-UlTQo&t=446s',
                          'relevance': 'Primary practitioner testimony on VAR license terms, wholesale '
                                       'pricing, cost-plus developers and revenue streams.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'z6rVTIy-FOg',
                       'title': 'Value Added Reseller Explained - Should You Utilize One?',
                       'channel': 'Positive Results',
                       'author': 'Positive Results',
                       'text': 'Value-added resellers never charge you more for monthly user fees of the '
                               "services you buy; we're compensated by the software company, and most "
                               'software providers do over 80 percent of their sales through value-added '
                               'resellers.',
                       'tip': 'Value-added resellers never charge you more for monthly user fees of the '
                              "services you buy; we're compensated by the software company, and most "
                              'software providers do over 80 percent of their sales through value-added '
                              'resellers.',
                       'timestamp': 179,
                       'timestamp_seconds': 179,
                       'timestamp_label': '[00:02:59]',
                       'url': 'https://www.youtube.com/watch?v=z6rVTIy-FOg&t=179s',
                       'markdown': '[00:02:59](https://www.youtube.com/watch?v=z6rVTIy-FOg&t=179s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tn0y9__lnqY',
                       'title': 'VAR Talk: Finding the Right ERP Partner',
                       'channel': 'GoldFinch Cloud Solutions',
                       'author': 'GoldFinch Cloud Solutions',
                       'text': 'As an ERP VAR, in addition to taking care of your clients, one of your '
                               'goals is profitability, so partner with a vendor offering simple pricing '
                               'models for transparency and ease of quoting.',
                       'tip': 'As an ERP VAR, in addition to taking care of your clients, one of your '
                              'goals is profitability, so partner with a vendor offering simple pricing '
                              'models for transparency and ease of quoting.',
                       'timestamp': 144,
                       'timestamp_seconds': 144,
                       'timestamp_label': '[00:02:24]',
                       'url': 'https://www.youtube.com/watch?v=tn0y9__lnqY&t=144s',
                       'markdown': '[00:02:24](https://www.youtube.com/watch?v=tn0y9__lnqY&t=144s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WEqXH4PuF8c',
                       'title': 'What is a VAR (Value-Added Reseller)?',
                       'channel': 'Eye on Tech',
                       'author': 'Eye on Tech',
                       'text': 'VARs are finding it more difficult to continue in the market due to '
                               'changes in their margins, revenue and competitive positions and as a '
                               'result are transitioning to more of an MSP role.',
                       'tip': 'VARs are finding it more difficult to continue in the market due to changes '
                              'in their margins, revenue and competitive positions and as a result are '
                              'transitioning to more of an MSP role.',
                       'timestamp': 133,
                       'timestamp_seconds': 133,
                       'timestamp_label': '[00:02:13]',
                       'url': 'https://www.youtube.com/watch?v=WEqXH4PuF8c&t=133s',
                       'markdown': '[00:02:13](https://www.youtube.com/watch?v=WEqXH4PuF8c&t=133s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5n6g3xVFV88',
                       'title': 'Value-Added Reseller | The ProfServ Traction Podcast',
                       'channel': 'Steve Preda',
                       'author': 'Steve Preda',
                       'text': 'Their net profit before tax was 14 million dollars, almost 60 percent net '
                               'profit margin, and they are a value-added reseller.',
                       'tip': 'Their net profit before tax was 14 million dollars, almost 60 percent net '
                              'profit margin, and they are a value-added reseller.',
                       'timestamp': 258,
                       'timestamp_seconds': 258,
                       'timestamp_label': '[00:04:18]',
                       'url': 'https://www.youtube.com/watch?v=5n6g3xVFV88&t=258s',
                       'markdown': '[00:04:18](https://www.youtube.com/watch?v=5n6g3xVFV88&t=258s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bek-1YEtW80',
                       'title': 'What Is the Difference Between an MSP and a VAR',
                       'channel': 'samit',
                       'author': 'samit',
                       'text': "It doesn't matter how much they are your MSP and represent you; they are "
                               'also your VAR and are paid to not represent you but to represent the '
                               'vendor.',
                       'tip': "It doesn't matter how much they are your MSP and represent you; they are "
                              'also your VAR and are paid to not represent you but to represent the '
                              'vendor.',
                       'timestamp': 195,
                       'timestamp_seconds': 195,
                       'timestamp_label': '[00:03:15]',
                       'url': 'https://www.youtube.com/watch?v=bek-1YEtW80&t=195s',
                       'markdown': '[00:03:15](https://www.youtube.com/watch?v=bek-1YEtW80&t=195s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4qYKEjVIAjc',
                       'title': 'Customer Success Video for Channel Partner ver 1',
                       'channel': 'Summer Zaldivar',
                       'author': 'Summer Zaldivar',
                       'text': 'Last quarter 20 high-volume customers were identified at risk, eight of '
                               'which were remediated by connecting these customers with our premier '
                               'support teams, saving over 250,000 and increasing our renewal rate by 5 '
                               'percent.',
                       'tip': 'Last quarter 20 high-volume customers were identified at risk, eight of '
                              'which were remediated by connecting these customers with our premier '
                              'support teams, saving over 250,000 and increasing our renewal rate by 5 '
                              'percent.',
                       'timestamp': 36,
                       'timestamp_seconds': 36,
                       'timestamp_label': '[00:00:36]',
                       'url': 'https://www.youtube.com/watch?v=4qYKEjVIAjc&t=36s',
                       'markdown': '[00:00:36](https://www.youtube.com/watch?v=4qYKEjVIAjc&t=36s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'vLO0gA3TgxE',
                       'title': 'Ask a VAR: How Can an ISV Get Better Engagement and Build a Partnership?',
                       'channel': 'Channel Marketing Academy',
                       'author': 'Channel Marketing Academy',
                       'text': "If you won't tell me how much it costs at all until you talk to the "
                               "client, then I'm not even going to present you because I don't want to be "
                               'embarrassed.',
                       'tip': "If you won't tell me how much it costs at all until you talk to the client, "
                              "then I'm not even going to present you because I don't want to be "
                              'embarrassed.',
                       'timestamp': 134,
                       'timestamp_seconds': 134,
                       'timestamp_label': '[00:02:14]',
                       'url': 'https://www.youtube.com/watch?v=vLO0gA3TgxE&t=134s',
                       'markdown': '[00:02:14](https://www.youtube.com/watch?v=vLO0gA3TgxE&t=134s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-gG3jIROESw',
                       'title': 'AT&T Value Added Reseller Program: Empowering VAR Growth and Success',
                       'channel': 'AT&T Business',
                       'author': 'AT&T Business',
                       'text': 'The VAR partners bring deals in to your team, and then they can either '
                               'build the hardware independently on their own paper or go down AT&T paper, '
                               'and that end customer will still see that hardware buy-down on their bill.',
                       'tip': 'The VAR partners bring deals in to your team, and then they can either '
                              'build the hardware independently on their own paper or go down AT&T paper, '
                              'and that end customer will still see that hardware buy-down on their bill.',
                       'timestamp': 207,
                       'timestamp_seconds': 207,
                       'timestamp_label': '[00:03:27]',
                       'url': 'https://www.youtube.com/watch?v=-gG3jIROESw&t=207s',
                       'markdown': '[00:03:27](https://www.youtube.com/watch?v=-gG3jIROESw&t=207s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Y3mGiwmy2l0',
                       'title': 'What the Heck is... a Value-Added Reseller (VAR)?',
                       'channel': 'BrainSell',
                       'author': 'BrainSell',
                       'text': 'Software is stupid; it needs to be told what to do, and once we understand '
                               'how it affects people in process we come back to the value add.',
                       'tip': 'Software is stupid; it needs to be told what to do, and once we understand '
                              'how it affects people in process we come back to the value add.',
                       'timestamp': 96,
                       'timestamp_seconds': 96,
                       'timestamp_label': '[00:01:36]',
                       'url': 'https://www.youtube.com/watch?v=Y3mGiwmy2l0&t=96s',
                       'markdown': '[00:01:36](https://www.youtube.com/watch?v=Y3mGiwmy2l0&t=96s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yasPH-UlTQo',
                       'title': 'Value Added Reseller Overview',
                       'channel': 'Stuart Sutton',
                       'author': 'Stuart Sutton',
                       'text': 'You will also be expected to work hard to make your VAR successful and '
                               'generate sufficient business within the first two years for you to retain '
                               'your VAR license.',
                       'tip': 'You will also be expected to work hard to make your VAR successful and '
                              'generate sufficient business within the first two years for you to retain '
                              'your VAR license.',
                       'timestamp': 239,
                       'timestamp_seconds': 239,
                       'timestamp_label': '[00:03:59]',
                       'url': 'https://www.youtube.com/watch?v=yasPH-UlTQo&t=239s',
                       'markdown': '[00:03:59](https://www.youtube.com/watch?v=yasPH-UlTQo&t=239s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yasPH-UlTQo',
                       'title': 'Value Added Reseller Overview',
                       'channel': 'Stuart Sutton',
                       'author': 'Stuart Sutton',
                       'text': 'Their salary, benefits, and expenses will be paid for by you, the VAR, at '
                               'a cost plus management fee, and you cannot recruit any Full Circle TMS '
                               'employees to work for you.',
                       'tip': 'Their salary, benefits, and expenses will be paid for by you, the VAR, at a '
                              'cost plus management fee, and you cannot recruit any Full Circle TMS '
                              'employees to work for you.',
                       'timestamp': 349,
                       'timestamp_seconds': 349,
                       'timestamp_label': '[00:05:49]',
                       'url': 'https://www.youtube.com/watch?v=yasPH-UlTQo&t=349s',
                       'markdown': '[00:05:49](https://www.youtube.com/watch?v=yasPH-UlTQo&t=349s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'BJPNVL1CIiM',
                       'title': 'Get the Most Value from Value Added Resellers',
                       'channel': 'Staying Connected',
                       'author': 'Staying Connected',
                       'text': 'If the OEM provides you with a 60 percent discount, the VAR might reduce '
                               'that discount to say 58 by way of the markup for its resale services.',
                       'tip': 'If the OEM provides you with a 60 percent discount, the VAR might reduce '
                              'that discount to say 58 by way of the markup for its resale services.',
                       'timestamp': 250,
                       'timestamp_seconds': 250,
                       'timestamp_label': '[00:04:10]',
                       'url': 'https://www.youtube.com/watch?v=BJPNVL1CIiM&t=250s',
                       'markdown': '[00:04:10](https://www.youtube.com/watch?v=BJPNVL1CIiM&t=250s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'meEqyWq6yX0',
                       'title': 'How to Create a SaaS Customer Case Study',
                       'channel': 'Tom Bruining',
                       'author': 'Tom Bruining',
                       'text': "If you've got two customers and one of them is a bit larger with a legal "
                               'team you would need for sign off, you might want to go with the other '
                               "customer who's a little bit easier to work with.",
                       'tip': "If you've got two customers and one of them is a bit larger with a legal "
                              'team you would need for sign off, you might want to go with the other '
                              "customer who's a little bit easier to work with.",
                       'timestamp': 243,
                       'timestamp_seconds': 243,
                       'timestamp_label': '[00:04:03]',
                       'url': 'https://www.youtube.com/watch?v=meEqyWq6yX0&t=243s',
                       'markdown': '[00:04:03](https://www.youtube.com/watch?v=meEqyWq6yX0&t=243s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'L1YsH5QkIus',
                       'title': 'Selling and Marketing Software Through the VAR Channel -Morettini on '
                                'Management Video Edition',
                       'channel': 'Phil Morettini',
                       'author': 'Phil Morettini',
                       'text': "Don't over distribute your products by assigning way too many VARs within "
                               'a local area; all this will do is take all the product profit margin out '
                               'of the sale.',
                       'tip': "Don't over distribute your products by assigning way too many VARs within a "
                              'local area; all this will do is take all the product profit margin out of '
                              'the sale.',
                       'timestamp': 196,
                       'timestamp_seconds': 196,
                       'timestamp_label': '[00:03:16]',
                       'url': 'https://www.youtube.com/watch?v=L1YsH5QkIus&t=196s',
                       'markdown': '[00:03:16](https://www.youtube.com/watch?v=L1YsH5QkIus&t=196s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'L1YsH5QkIus',
                       'title': 'Selling and Marketing Software Through the VAR Channel -Morettini on '
                                'Management Video Edition',
                       'channel': 'Phil Morettini',
                       'author': 'Phil Morettini',
                       'text': "VARs won't create demand for your products; that's the vendor's "
                               "responsibility, and they won't be motivated solely by high product "
                               'margins.',
                       'tip': "VARs won't create demand for your products; that's the vendor's "
                              "responsibility, and they won't be motivated solely by high product margins.",
                       'timestamp': 64,
                       'timestamp_seconds': 64,
                       'timestamp_label': '[00:01:04]',
                       'url': 'https://www.youtube.com/watch?v=L1YsH5QkIus&t=64s',
                       'markdown': '[00:01:04](https://www.youtube.com/watch?v=L1YsH5QkIus&t=64s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2tRDmrgGASk',
                       'title': 'Working Successfully with Value-Added Resellers (VARs)',
                       'channel': 'Sheldon Needle',
                       'author': 'Sheldon Needle',
                       'text': "You could get a VAR who's not really very qualified, who has a change in "
                               'staff during the course of your project and leaves you high and dry.',
                       'tip': "You could get a VAR who's not really very qualified, who has a change in "
                              'staff during the course of your project and leaves you high and dry.',
                       'timestamp': 103,
                       'timestamp_seconds': 103,
                       'timestamp_label': '[00:01:43]',
                       'url': 'https://www.youtube.com/watch?v=2tRDmrgGASk&t=103s',
                       'markdown': '[00:01:43](https://www.youtube.com/watch?v=2tRDmrgGASk&t=103s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NbukIA2E8Nw',
                       'title': "What the Best Technology VAR's & Resellers Do Differently",
                       'channel': 'Ridge Consulting',
                       'author': 'Ridge Consulting',
                       'text': 'They quickly choose multiple market segments without checking long-term '
                               'fit and then quickly launch a range of short-term focused marketing '
                               'activities.',
                       'tip': 'They quickly choose multiple market segments without checking long-term fit '
                              'and then quickly launch a range of short-term focused marketing activities.',
                       'timestamp': 15,
                       'timestamp_seconds': 15,
                       'timestamp_label': '[00:00:15]',
                       'url': 'https://www.youtube.com/watch?v=NbukIA2E8Nw&t=15s',
                       'markdown': '[00:00:15](https://www.youtube.com/watch?v=NbukIA2E8Nw&t=15s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2qyZJaUnuYo',
                       'title': 'Channel Partner Program: the value for partners',
                       'channel': 'ItaltelChannel',
                       'author': 'ItaltelChannel',
                       'text': 'Italtel needs an indirect channel sales program because we see '
                               'opportunities not only in the regions that we cover directly but also in '
                               'the regions that are not covered by our direct sales force.',
                       'tip': 'Italtel needs an indirect channel sales program because we see '
                              'opportunities not only in the regions that we cover directly but also in '
                              'the regions that are not covered by our direct sales force.',
                       'timestamp': 39,
                       'timestamp_seconds': 39,
                       'timestamp_label': '[00:00:39]',
                       'url': 'https://www.youtube.com/watch?v=2qyZJaUnuYo&t=39s',
                       'markdown': '[00:00:39](https://www.youtube.com/watch?v=2qyZJaUnuYo&t=39s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'}]}
