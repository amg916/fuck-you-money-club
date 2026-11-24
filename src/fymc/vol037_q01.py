from __future__ import annotations

CHAPTER_1 = {'id': 'Q1',
 'chapter_id': 'Q1',
 'chapter_number': 1,
 'question_number': 1,
 'slug': 'microsoft-channel-partner-center-mpn-csp-resale-models',
 'question_prompt': 'How do I get set up as a Microsoft partner and pick the right CSP resale model so I '
                    'can legally buy and resell Microsoft cloud licenses?',
 'kicker': 'Q1 / THE BIG MONEY PLAYBOOKS',
 'title': 'Entering the Microsoft Channel: Partner Center, MPN Enrollment, and CSP Resale Models',
 'subtitle': 'Partner Center account and company-profile setup, MPN/AI Cloud Partner Program enrollment, '
             'CSP Direct vs Indirect Provider vs Indirect Reseller, partner levels and benefits packages, '
             'CSP licensing rules, and transacting NCE through a distributor marketplace',
 'layout_template': 'opportunity_overview',
 'reading_time_minutes': 15,
 'executive_summary': 'Operators entering the Microsoft channel converge on one route: register a Partner '
                      'Center account under a domain email and primary Entra tenant, clear business '
                      'verification, join the free AI Cloud Partner Program, then link an MPN ID to an '
                      'indirect provider such as Ingram Micro, Pax8, TD Synnex or Sherweb. More than 90% '
                      'of partners run indirect because direct bill now demands $1M trailing revenue, a '
                      'designation and paid support. License margin is thin, 8-15% or $18 cost against $20 '
                      'MSRP, so practitioners bundle services and chase back-end incentives that stack to '
                      '25.75% on M365, 26% on Azure and 34.75% on Dynamics, paid 60% rebate and 40% co-op. '
                      'Benefits packages run $345 to $4,730 a year. Disagreements center on who owns '
                      'first-line support, whether indirect layers add cost, and package pricing.',
 'key_metrics': [{'label': 'Direct Bill Revenue Threshold',
                  'metric': 'Direct Bill Revenue Threshold',
                  'value': '$1,000,000 per year (up from roughly $300,000)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Microsoft raised the direct bill bar effective October; Pax8 APAC expects up '
                             'to two-thirds of direct partners to move under indirect providers',
                  'source': 'Pax8 APAC ([Xywyds1IfvM @ 00:04:31])'},
                 {'label': 'CSP License Margin',
                  'metric': 'CSP License Margin',
                  'value': '8-15% on the license',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Margin earned on resold Microsoft licenses before any service bundling, '
                             'which is why the partner earns on the service layer',
                  'source': 'm365 Show | M365, Azure Cloud, Power Platform & AI ([LGgw20GtaDQ @ '
                            '00:03:47])'},
                 {'label': 'Stacked M365 Incentive Ceiling',
                  'metric': 'Stacked M365 Incentive Ceiling',
                  'value': 'Up to 25.75% stacked',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Core 3.75% plus Tier 1 5%, Tier 2 7%, PSTN 20% and customer-add 15% for 12 '
                             'months; Azure stacks to 26% and Dynamics to 34.75%',
                  'source': 'Inside Microsoft AI Cloud Partner Program ([jz1cE7UYBO4 @ 00:15:48])'},
                 {'label': 'NCE Monthly-Term Premium',
                  'metric': 'NCE Monthly-Term Premium',
                  'value': '20% ($100 seat becomes $120)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Premium for monthly NCE terms versus annual; annual paid monthly adds 5% and '
                             'triennial saves 12-18%',
                  'source': 'm365 Show | M365, Azure Cloud, Power Platform & AI ([LGgw20GtaDQ @ '
                            '00:04:45])'}],
 'sections': [{'title': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['The channel runs as a wholesale chain, and every operator who walks through '
                              'it describes the same ladder. Microsoft sells licenses at bulk prices, '
                              'partners layer services on top and resell Microsoft 365, Azure, Dynamics '
                              '365 and EMS, and the partner owns billing, support and provisioning for the '
                              'end customer [LGgw20GtaDQ @ 00:00:26]. The m365 Show breakdown draws the '
                              'chain as Microsoft to indirect provider to reseller to customer, with three '
                              'partner types sitting on it: direct bill, indirect provider and indirect '
                              'reseller [uiVjifpxK38 @ 00:04:51]. Microsoft Helps engineers Halima and '
                              'Sachin map the same structure to tiers, calling direct bill Tier 1 and the '
                              'indirect provider plus indirect reseller pairing Tier 2, and they note that '
                              'only providers and direct bill partners can create customer tenants, while '
                              "resellers send a relationship link the customer's global admin must accept "
                              "[9Q30FhN41LI @ 00:03:43]. Pax8 APAC's Kristen Farenbach and Chris Sharp "
                              'report the direct threshold jumped from roughly $300,000 a year to $1 '
                              'million, and they expect up to two-thirds of current direct partners to '
                              'move under indirect providers [Xywyds1IfvM @ 00:04:31]. The same m365 Show '
                              'breakdown puts more than 90% of partners in the indirect lane with no '
                              'revenue minimum, which makes indirect reseller the default entry point.',
                              'Enrollment prerequisites are identical across every walkthrough. Sub-Zero '
                              'To Wealth lists a registered legal entity, a domain email with no Gmail or '
                              'Yahoo, a verifiable address and phone number, and a live website before '
                              'touching partner.microsoft.com, then runs a seven-step path from tenant '
                              'creation through profile, validation, free MCPP enrollment, product '
                              'selection and a CSP distributor [VP4hPTXkPIs @ 00:01:07]. Validation is '
                              "where, in that speaker's words, most people get stuck. Technical Support "
                              'Online walks the same signup, choosing Partner and Resell, building the '
                              'account under a domain email, then clearing email, employment and business '
                              'verification before a decision lands [tlmDeX5UBJs @ 00:06:42]. Their '
                              'company-profile walkthrough adds two-step verification, shows a global and '
                              'a location MPN ID under Legal Info, and clocks verification at two to three '
                              'business days [wjgyQO9jIAM @ 00:05:22]. Mirko Peters at m365 Show insists '
                              'the account be built under the primary Entra tenant, warning that the '
                              'viral-user problem otherwise spawns duplicate or orphaned accounts '
                              '[by9BiS2U7xo @ 00:05:03]. Sub-Zero To Wealth names the profile killers '
                              'outright: personal email, inaccurate details, missing website, no niche and '
                              'ignoring compliance. Get the legal entity, domain email and Entra tenant '
                              'right first, and the rest of the reseller chain moves cleanly.',
                              'On economics, the consensus is that the license itself pays almost nothing. '
                              'The m365 Show CSP breakdown puts license margin at 8 to 15% and argues the '
                              'partner earns on the service layer, not the software, illustrating with '
                              'Business Premium at $22 plus $8 of identity, device management and help '
                              'desk to land a $30 seat [LGgw20GtaDQ @ 00:03:47]. The Crancer Group frames '
                              'the distributor spread as a $20 MSRP license bought at $18, which the '
                              'speaker dismisses as pennies on the dollar, and points operators toward a '
                              'Solutions Partner Designation in Modern Work plus Azure or Security, then '
                              'an advanced specialization, where the money reaches thousands and hundreds '
                              'of thousands [-zF8JCzzp8w @ 00:00:43]. Ana Stranaghan of TD SYNNEX confirms '
                              'the back end is where the stack lives, with M365 incentives running core '
                              '3.75%, Tier 1 at 5%, Tier 2 at 7%, PSTN at 20% and customer-add at 15% for '
                              'twelve months, up to 25.75% stacked, and warns that holding a package or '
                              'designation does not start the money until you enroll in Microsoft Commerce '
                              'Incentives [jz1cE7UYBO4 @ 00:15:48]. Sub-Zero To Wealth closes the loop: do '
                              'not just sell a license, sell a complete solution [VP4hPTXkPIs @ '
                              '00:05:49].'],
               'table': {'caption': 'Where Microsoft channel practitioners agree before the first seat is '
                                    'sold',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Indirect reseller is the default entry lane',
                                   'More than 90% of partners run indirect through Ingram Micro, Pax8 or '
                                   'Rhipe with no revenue minimum',
                                   'Start under a distributor instead of chasing direct bill status on day '
                                   'one',
                                   'm365 Show | M365, Azure Cloud, Power Platform & AI ([LGgw20GtaDQ @ '
                                   '00:02:15])'],
                                  ['Direct bill bar was raised sharply in October',
                                   'Threshold moved from roughly $300,000 a year to $1 million plus kept '
                                   'designations',
                                   'Up to two-thirds of existing direct partners may need an indirect '
                                   'provider home',
                                   'Pax8 APAC ([Xywyds1IfvM @ 00:04:31])'],
                                  ['Domain email and verifiable business identity are mandatory',
                                   'Legal entity, domain email, verifiable address, phone and a live '
                                   'website are required',
                                   'Gmail or Yahoo signups stall at validation, where most people get '
                                   'stuck',
                                   'Sub-Zero To Wealth ([VP4hPTXkPIs @ 00:01:07])'],
                                  ['Build the account under the primary Entra tenant',
                                   'Mixed email domains trigger the viral-user problem with duplicate or '
                                   'orphaned tenants',
                                   'Lock the tenant choice before creating the Partner Center account, not '
                                   'after',
                                   'm365 Show | M365, Azure Cloud, Power Platform & AI ([uiVjifpxK38 @ '
                                   '00:06:04])'],
                                  ['License margin alone is thin through a distributor',
                                   'Distributor spread runs a $20 MSRP license bought at roughly $18 cost',
                                   'Treat the license as pennies on the dollar and push designations and '
                                   'specializations',
                                   'The Crancer Group ([-zF8JCzzp8w @ 00:00:43])'],
                                  ['Service bundling carries the profit on every seat',
                                   'Business Premium at $22 plus $8 identity, device management and help '
                                   'desk equals $30',
                                   'Price every deal as a complete solution rather than a bare license '
                                   'line',
                                   'm365 Show | M365, Azure Cloud, Power Platform & AI ([LGgw20GtaDQ @ '
                                   '00:04:01])'],
                                  ['Incentives require separate enrollment beyond packages and '
                                   'designations',
                                   'Benefits packages and Solutions Partner status do not automatically '
                                   'start incentive earnings',
                                   'Enroll in Microsoft Commerce Incentives before expecting any rebate or '
                                   'co-op payout',
                                   'Inside Microsoft AI Cloud Partner Program ([jz1cE7UYBO4 @ '
                                   '00:21:41])']]}},
              {'title': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Execution starts inside Partner Center, and the m365 Show setup walkthrough '
                              'is precise about the fields that break: the phone box accepts ten '
                              'characters maximum with no spaces, dashes or country code, verification '
                              'runs hours to days, and access should be split with role-based access '
                              'control plus a break-glass global admin account [uiVjifpxK38 @ 00:11:01]. '
                              "Horror FM's walkthrough, voiced by a speaker who identifies as technical "
                              'support online, shows the reseller step: link the existing partner ID to a '
                              'CSP indirect reseller account, and if the status comes back rejected, hit '
                              'Fix now and upload company documents [jUFbUlIkcm0 @ 00:07:50]. Once the '
                              'reseller ID is live, Ingram Micro Cloud runs the first order in five steps: '
                              'search nce in the marketplace, open the Microsoft NCE tile, pick NCE '
                              'Microsoft 365 Commercial, add the plan to cart, select or create the '
                              'customer, then enter the Microsoft Partner Number and indirect reseller '
                              'domain until the reseller screen shows status ready [W-fGvHNBEiM @ '
                              '00:02:09]. Ingram Micro is explicit that the MPN ID and tenant ID are '
                              'required to place an order, and the final screen forces Microsoft Customer '
                              'Agreement acceptance before Buy returns an order number for Track Order.',
                              'Term selection is where the per-seat math moves. The m365 Show CSP '
                              'breakdown lays out the NCE structure that arrived in 2022: a monthly term '
                              'carries a 20% premium, so $100 becomes $120, annual paid monthly adds 5%, '
                              'triennial saves 12 to 18%, and every order has a seven-day window to change '
                              'your mind or adjust quantities, after which seats can only be added, never '
                              'reduced [LGgw20GtaDQ @ 00:04:45]. Lapsed subscriptions now roll into an '
                              'extended term billed at the monthly rate plus 3% once the grace period '
                              "ended in May 2026. MicroAge's Avery Shaller and Jason confirm NCE sits "
                              'nested inside CSP with three payment terms and the 20% monthly premium '
                              'unchanged, and they log the April 1, 2025 increases on Power BI Pro and '
                              'PPU, Teams Phone, plus a 5% surcharge on annual-commit-paid-monthly that '
                              'hits Copilot too [Ap8gUtRq32o @ 00:05:46]. Their playbook: renew before '
                              'April 1, use CSP-to-CSP transfers that keep dates and agreements, and run '
                              'license optimization because customers are often over-provisioned. On the '
                              'API side, Mirko Peters flags that 429 errors need exponential back-off and '
                              'that every app-plus-user API call must carry an MFA token by April 2026, or '
                              'automation breaks [by9BiS2U7xo @ 00:14:31].',
                              'The back-end numbers decide whether the channel pays. Ana Stranaghan of TD '
                              'SYNNEX prices the Core benefits package at $895 a year for about $62,000 in '
                              'value, sized for 5, 15 and 35 users, and Solutions Partner at $4,730 a year '
                              'with incremental benefits per designation; packages stack, but no '
                              'incentives are tied to them [jz1cE7UYBO4 @ 00:04:08]. Stacked ceilings run '
                              'up to 25.75% on M365, 26% on Azure and 34.75% on Dynamics, paid 60% as '
                              'monthly cash rebate and 40% as co-op, with co-op under $10K converted to a '
                              'rebate lump sum. The Crancer Group describes the same split in practice: '
                              'under $10K, Microsoft mails a check every six months; above it, payouts '
                              'break 60/40, for example $6,000 cash against a $4,000 MDF bucket that is '
                              'clawed back if unused within six months [-zF8JCzzp8w @ 00:03:34]. '
                              'Designation math is a points game: 70 of 100 points with at least one point '
                              'in every metric, fed by CSP, CPOR, PAL and DPOR associations. On the '
                              'package side, PKF Attest reports roughly $30,000 in value from a $4,000 '
                              'package and a 15 to 25x return, calling it a no brainer and running every '
                              'tool it sells internally [RQe8RvOAGRw @ 00:02:54].'],
               'table': {'caption': 'Exact settings, prices and rates practitioners use to run CSP resale',
                         'headers': ['Mechanic',
                                     'Exact Number or Setting',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['NCE monthly term premium over annual commitment',
                                   '20% premium, so a $100 seat bills at $120',
                                   'Reserve monthly terms for seasonal headcount like the 80/30-person '
                                   'landscaper example',
                                   'm365 Show | M365, Azure Cloud, Power Platform & AI ([LGgw20GtaDQ @ '
                                   '00:04:45])'],
                                  ['NCE cancellation and quantity adjustment window',
                                   'Seven days after the order, then seats can only be added',
                                   'Confirm headcount inside the window; the speaker still advises '
                                   'overbuying slightly',
                                   'm365 Show | M365, Azure Cloud, Power Platform & AI ([LGgw20GtaDQ @ '
                                   '00:05:42])'],
                                  ['Extended term billing on lapsed subscriptions',
                                   'Monthly rate plus 3% after the May 2026 grace period ended',
                                   'Renew on time so seats never drift into extended-term billing',
                                   'm365 Show | M365, Azure Cloud, Power Platform & AI ([LGgw20GtaDQ @ '
                                   '00:06:24])'],
                                  ['Partner Center phone field formatting rule',
                                   'Ten characters maximum with no spaces, dashes or country code',
                                   'Enter digits only to avoid verification stalls that drag for days',
                                   'm365 Show | M365, Azure Cloud, Power Platform & AI ([uiVjifpxK38 @ '
                                   '00:11:01])'],
                                  ['M365 stacked incentive rates by component',
                                   'Core 3.75%, Tier 1 5%, Tier 2 7%, PSTN 20%, customer-add 15%',
                                   'Stack customer-add and PSTN earnings to approach the 25.75% ceiling',
                                   'Inside Microsoft AI Cloud Partner Program ([jz1cE7UYBO4 @ 00:15:48])'],
                                  ['Benefits package annual pricing tiers',
                                   'Core $895 for about $62,000 value; Solutions Partner $4,730 per year',
                                   'Buy Core early; E3 and E5 benefits only come with Solutions Partner',
                                   'Inside Microsoft AI Cloud Partner Program ([jz1cE7UYBO4 @ 00:04:08])'],
                                  ['Azure Global versus Azure plan offer IDs',
                                   'MS-AZR-0145P versus 0017G, which cannot be added side by side',
                                   'Run the transition workflow instead of adding 0017G to a 0145P tenant',
                                   'Microsoft Helps ([9Q30FhN41LI @ 00:16:50])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Operator shortcuts from the channel floor',
                           'body': 'Small habits practitioners use to protect margin, keep tickets moving '
                                   'and pick the right provider.',
                           'items': ['Always check the benefits tab before buying another security '
                                     'license; internal-use rights may already cover it [m365 Show | M365, '
                                     'Azure Cloud, Power Platform & AI — by9BiS2U7xo @ 00:08:21]',
                                     'For API failures, send Microsoft the request and response logs plus '
                                     'the MS-CorrelationID, not your code; pull a SPOCK file with '
                                     'Ctrl+Alt+D for portal issues [Microsoft Helps — 9Q30FhN41LI @ '
                                     '00:35:20]',
                                     'Trace unexplained deposits such as $8,000 in the earnings report, '
                                     'and on any billing discrepancy wait 24 hours and check again before '
                                     'filing [m365 Show | M365, Azure Cloud, Power Platform & AI — '
                                     'uiVjifpxK38 @ 00:13:33]',
                                     'Pick an indirect provider on marketplace strength, instant '
                                     'provisioning and tickets closed in-house rather than escalated [Pax8 '
                                     'APAC — Xywyds1IfvM @ 00:09:05]']},
               'sop_steps': [{'step': 1,
                              'title': 'Stand up the entity, domain and tenant',
                              'action': 'Secure a legal entity, domain email, verifiable address and '
                                        'phone, and a live website, then create the account under the '
                                        'primary Entra tenant.',
                              'detail': 'Gmail or Yahoo addresses, missing websites and inaccurate details '
                                        'are the named mistakes, and validation is where most people get '
                                        'stuck [Sub-Zero To Wealth — VP4hPTXkPIs @ 00:01:07]'},
                             {'step': 2,
                              'title': 'Enroll and clear verification',
                              'action': 'Select Partner, Reseller and Integrate, enable two-step '
                                        'verification, and finish the company profile in Partner Center.',
                              'detail': 'Legal Info shows a global and a location MPN ID, and verification '
                                        'takes two to three business days [Technical Support Online — '
                                        'wjgyQO9jIAM @ 00:06:17]'},
                             {'step': 3,
                              'title': 'Link the reseller ID to an indirect provider',
                              'action': 'Connect the existing partner ID to a CSP indirect reseller '
                                        'account under a distributor such as Ingram Micro, Pax8, TD Synnex '
                                        'or Sherweb.',
                              'detail': 'If the status shows rejected, use Fix now and upload company '
                                        'documents to clear the reseller step [Horror FM — jUFbUlIkcm0 @ '
                                        '00:07:50]'},
                             {'step': 4,
                              'title': 'Place the first NCE order and switch on incentives',
                              'action': 'Search nce on the provider marketplace, add the plan, attach the '
                                        'customer with MPN ID and tenant ID, accept the Microsoft Customer '
                                        'Agreement and click Buy.',
                              'detail': 'Track the order number from the Track Order button, then enroll '
                                        'in Microsoft Commerce Incentives because packages and '
                                        'designations do not start earnings on their own [Ingram Micro '
                                        'Cloud — W-fGvHNBEiM @ 00:03:35]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is whether to chase direct-bill status or live '
                              "permanently under a distributor. Spyglass MTG's Keith Tiller argues against "
                              'the indirect layer outright: an extra vendor in the chain raises cost and '
                              'complexity, and his shop sells as a direct partner pricing customers '
                              '"typically below retail" [yNBOfW1MoPs @ 00:00:35]. The m365 Show counters '
                              'with the gatekeeping math: direct bill demands $1M in trailing-twelve-month '
                              'revenue, twelve months already logged as an indirect reseller, a solutions '
                              'partner designation and a paid support plan, with only about 30 such '
                              'partners in the US, while more than 90% of partners run indirect with no '
                              "revenue minimum [LGgw20GtaDQ @ 00:01:47]. Pax8 APAC's Kristen Farenbach and "
                              'Chris Sharp frame the same wall as a migration event: the direct threshold '
                              'jumped from roughly $300,000 a year to $1 million, and they expect up to '
                              'two-thirds of current direct partners to find a new home with indirect '
                              'providers [Xywyds1IfvM @ 00:05:09]. Their counter-pitch is that "your value '
                              'hasn\'t diminished," and they tell operators to screen indirect providers '
                              'for a strong marketplace, instant provisioning, account management that '
                              'drives growth rather than QBRs, and support tickets closed in-house rather '
                              'than escalated [Xywyds1IfvM @ 00:09:05].',
                              'Who carries the support burden is a flat contradiction between channels. '
                              'Tiller says the indirect reseller is not responsible for support and that '
                              'tickets fall back to the provider [yNBOfW1MoPs @ 00:00:50]. The m365 Show '
                              'states the opposite: first-line support is mandatory for every CSP partner, '
                              'ASfP runs about $15,000 a year minimum before it ends in January 2027, and '
                              'the support services designation under the incoming FY27 program offers up '
                              'to 50% off [LGgw20GtaDQ @ 00:11:05]. On margin, the same split repeats. The '
                              'm365 Show pegs license margin at 8-15% and treats the license as the entry '
                              'ticket for a service wrapper, bundling Business Premium at $22 with $8 of '
                              'identity, device management and help desk to reach $30 per seat, because '
                              '"the partner earns the margin on the service layer, not the software" '
                              '[LGgw20GtaDQ @ 00:04:18]. The Crancer Group is blunter about base-tier '
                              'economics: a $20 MSRP seat bought from a distributor at $18 is "pennies on '
                              'the dollar," and the real money sits in advanced specializations worth '
                              '"thousands and hundreds of thousands" [-zF8JCzzp8w @ 00:04:18]. Operators '
                              'picking between a service-wrapper playbook and an incentive-chasing '
                              'playbook are picking between those two camps, and MicroAge sides with '
                              'services, calling CSP "commoditized" across 300,000-plus resellers.',
                              'Benefits-package pricing and payout timing come out differently depending '
                              'on who is talking. PKF Attest, featured by the Microsoft AI Cloud Partner '
                              'Program, describes the package as an annual investment of "somewhere around '
                              '$345," calls the 15-25x ROI "a no brainer," and says they pulled about '
                              '$30,000 in value from a $4,000 package against roughly $150,000 a year in '
                              'licensing they would otherwise pay [RQe8RvOAGRw @ 00:02:54]. Ana Stranaghan '
                              'of TD SYNNEX quotes Core at $895 a year for about $62,000 in value and '
                              'Solutions Partner at $4,730, and warns that the packages are stackable but '
                              'carry no incentives tied to them [jz1cE7UYBO4 @ 00:05:00]. Payout cadence '
                              'splits too. The Crancer Group says under $10K in earnings Microsoft cuts a '
                              'check every six months, while over $10K the money divides 60/40 into cash '
                              'and an MDF bucket, so $10K yields "basically 6,000" in hand [-zF8JCzzp8w @ '
                              '00:03:34]. Stranaghan instead describes the 60% rebate as monthly cash and '
                              'says co-op under $10K is converted into a rebate lump sum [jz1cE7UYBO4 @ '
                              "00:20:01]. PKF Attest's own figures pair the $345 annual cost with a "
                              '"$4,000 package," so the exact tier behind their ROI claim is never pinned '
                              "down, and Stranaghan's $895 and $4,730 price points sit well above the $345 "
                              'number.'],
               'table': {'caption': 'Competing playbooks on channel model, support, margin, packages and '
                                    'payouts',
                         'headers': ['Fault Line', 'Position A', 'Position B', 'Expert Source'],
                         'rows': [['Direct bill versus indirect provider as the operating model',
                                   'Go direct because the extra vendor layer adds cost and complexity; '
                                   'price typically below retail',
                                   'Go indirect because the direct bar rose to $1 million and two-thirds '
                                   'of direct partners may move',
                                   'Spyglass MTG ([yNBOfW1MoPs @ 00:00:35]); Pax8 APAC ([Xywyds1IfvM @ '
                                   '00:05:09])'],
                                  ['Who owns first-line customer support in the indirect chain',
                                   'The indirect reseller is not responsible for support and tickets fall '
                                   'back to the provider',
                                   'First-line support is mandatory for all partners, with ASfP costing '
                                   'about $15,000 per year minimum',
                                   'Spyglass MTG ([yNBOfW1MoPs @ 00:00:50]); m365 Show | M365, Azure '
                                   'Cloud, Power Platform & AI ([LGgw20GtaDQ @ 00:11:05])'],
                                  ['Where the real margin actually lives for a new reseller',
                                   'Service layer: $22 Business Premium plus $8 of identity, device and '
                                   'help desk equals $30',
                                   'Incentive layer: base resale is pennies on the dollar, advanced '
                                   'specializations pay thousands to hundreds of thousands',
                                   'm365 Show | M365, Azure Cloud, Power Platform & AI ([LGgw20GtaDQ @ '
                                   '00:04:01]); The Crancer Group ([-zF8JCzzp8w @ 00:04:18])'],
                                  ['Benefits package cost and the value it returns each year',
                                   'About $345 per year, with roughly $30,000 in value pulled from a '
                                   '$4,000 package',
                                   'Core at $895 for about $62,000 in value; Solutions Partner at $4,730 '
                                   'per year',
                                   'Microsoft AI Cloud Partner Program ([RQe8RvOAGRw @ 00:01:38]); Inside '
                                   'Microsoft AI Cloud Partner Program ([jz1cE7UYBO4 @ 00:04:08])'],
                                  ['Incentive payout cadence and the $10K co-op threshold',
                                   'Under $10K earnings Microsoft sends a check every six months; over '
                                   '$10K splits 60/40',
                                   'The 60% rebate pays monthly cash; co-op under $10K converts into a '
                                   'rebate lump sum',
                                   'The Crancer Group ([-zF8JCzzp8w @ 00:03:04]); Inside Microsoft AI '
                                   'Cloud Partner Program ([jz1cE7UYBO4 @ 00:20:01])'],
                                  ['Which CSP distributors make the indirect shortlist',
                                   'Ingram Micro, Pax8 and Rhipe named, with an alternate cut swapping '
                                   'Tech Data for Pax8',
                                   'Ingram Micro, TD Synnex, Sherweb and Pax8 named as the CSP '
                                   'distributors to approach',
                                   'm365 Show | M365, Azure Cloud, Power Platform & AI ([rD2YxxfsOa4 @ '
                                   '00:03:23]); Sub-Zero To Wealth ([VP4hPTXkPIs @ 00:04:15])'],
                                  ['CSP versus Enterprise Agreement and the commoditization of seat resale',
                                   'Under 300 seats use CSP; EA runs 20-35% cheaper above 500 users, so '
                                   'run the numbers',
                                   'CSP is becoming commoditized across 300,000-plus CSPs, so lead with '
                                   'services rather than seats',
                                   'm365 Show | M365, Azure Cloud, Power Platform & AI ([LGgw20GtaDQ @ '
                                   '00:07:59]); MicroAge ([Ap8gUtRq32o @ 00:20:35])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['Most onboarding failures happen before a single seat is sold. Sub-Zero To '
                              'Wealth flags business validation as the step where "most people get stuck" '
                              'and lists the self-inflicted killers: a personal Gmail or Yahoo address, '
                              'inaccurate company information, no website, no niche and ignoring '
                              'compliance [VP4hPTXkPIs @ 00:05:49]. Technical Support Online walks through '
                              'what happens when the application bounces: the status flips to rejected, '
                              'and the only path forward is clicking "Fix now" and uploading company '
                              'documents before the email, employment, business and decision checks clear '
                              '[tlmDeX5UBJs @ 00:11:52]. The m365 Show adds the silent traps. Sign up '
                              'under anything other than the primary Entra tenant and the "viral user" '
                              'problem spawns duplicate or orphaned accounts, while the phone field '
                              'accepts ten characters maximum with no spaces, dashes or country code, and '
                              'verification itself takes hours to days [uiVjifpxK38 @ 00:11:01]. Older '
                              'partners got hit by the Partner Membership Center migration itself, which '
                              'lost historical records and displayed paid designations as wrongly expired '
                              "[by9BiS2U7xo @ 00:01:47]. The same channel's operational order of battle: "
                              'set up role-based access control and a break-glass global admin account '
                              'first, because "don\'t jump straight into customer management."',
                              'The commercial traps sit inside NCE commitments. The m365 Show spells out '
                              'the lock-in: the monthly term carries a 20% premium, annual paid monthly '
                              'adds 5%, and orders get "just 7 days to change your mind or adjust '
                              'quantities," after which seats can be added but never reduced [LGgw20GtaDQ '
                              '@ 00:05:42]. Their example is a customer who plans 100 seats, needs 80 and '
                              'pays for 20 idle licenses, and since the grace period ended in May 2026, '
                              'lapsed subscriptions roll into an extended term billed at the monthly rate '
                              "plus 3% [LGgw20GtaDQ @ 00:06:24]. MicroAge's Avery Shaller and Jason "
                              'describe the transfer minefield around Teams unbundling: Microsoft "sprung" '
                              'the CSP-to-CSP transfer process on partners, will not arbitrate disputes '
                              'short of malfeasance or bankruptcy, lets the incumbent refuse, and some '
                              'distributors simply do not participate [Ap8gUtRq32o @ 00:15:13]. If the '
                              'transfer dies, the customer buys new unbundled licenses plus Teams at about '
                              '$5.30. From the Microsoft Helps side, Halima and Sachin report a quieter '
                              'blocker in Azure: you cannot add Azure plan 0017G to a tenant already '
                              'holding MS-AZR-0145P, and must run the transition workflow instead of '
                              'forcing the new offer onto the customer [9Q30FhN41LI @ 00:16:50].',
                              'The final economics check is whether the incentive engine actually pays. '
                              'Stranaghan warns that "just because you have a benefits package or you\'ve '
                              'earned the solutions partner designation does not mean that you '
                              'automatically start earning the incentives"; enrollment in Microsoft '
                              'Commerce Incentives is its own step [jz1cE7UYBO4 @ 00:21:41]. Designations '
                              'need 70 of 100 points with points in every metric, and churn compounds the '
                              'math: "if you lose a customer you need to gain two customers to offset that '
                              'one loss" [jz1cE7UYBO4 @ 00:34:52]. The Crancer Group adds that MDF left '
                              'unused inside six months is clawed back, so the 40% bucket is only real if '
                              'it gets spent [-zF8JCzzp8w @ 00:04:05]. On the operations side, the m365 '
                              'Show warns that automation breaks without MFA: by April 2026 every '
                              'app-plus-user API call must carry an MFA token, 429 throttling errors need '
                              'exponential back-off, unexplained deposits such as $8,000 must be traced in '
                              'the earnings report, billing mismatches should sit 24 hours before a ticket '
                              'goes in, and on-premises Windows Server and SQL keys are gone from the '
                              'benefits stack [uiVjifpxK38 @ 00:15:23]. Anyone who leaned on partner '
                              'benefits for those server licenses hears it plainly: "those days are '
                              'over."'],
               'table': {'caption': 'Firsthand failure modes with their mechanism and the economic or '
                                    'operational hit',
                         'headers': ['Failure Mode',
                                     'Mechanism Reported',
                                     'Economics or Operational Hit',
                                     'Expert Source'],
                         'rows': [['Over-committing seats on an NCE annual order',
                                   'Customer planned 100 seats, needed 80, and quantities locked after the '
                                   '7-day window',
                                   'Pays for 20 unused seats because NCE seats can only be added, never '
                                   'reduced',
                                   'm365 Show | M365, Azure Cloud, Power Platform & AI ([LGgw20GtaDQ @ '
                                   '00:06:10])'],
                                  ['Failing the Partner Center Security Score',
                                   'MFA and the secure application model are not in place on the partner '
                                   'tenant',
                                   'Partner loses the ability to transact for customers until the score is '
                                   'fixed',
                                   'm365 Show | M365, Azure Cloud, Power Platform & AI ([LGgw20GtaDQ @ '
                                   '00:11:45])'],
                                  ['Incumbent refuses a CSP-to-CSP transfer request',
                                   'Microsoft will not arbitrate disputes and some distributors do not '
                                   'participate in transfers',
                                   'Customer must buy new unbundled licenses plus Teams at about $5.30 per '
                                   'seat',
                                   'MicroAge ([Ap8gUtRq32o @ 00:20:13])'],
                                  ['Global admin cannot see the Customers tab',
                                   'Global admin is a partner organization role, so customer access is '
                                   'withheld by design',
                                   'Customer work stalls until admin agent or helpdesk agent roles are '
                                   'assigned properly',
                                   'Microsoft Helps ([9Q30FhN41LI @ 00:37:59])'],
                                  ['Geography mismatch or insufficient credit limit on an order',
                                   'EU customer attached to a US partner, or distributor credit ceiling '
                                   'already reached',
                                   'Both rank among the most common Partner Center errors that stop '
                                   'customer transactions',
                                   'Microsoft Helps ([9Q30FhN41LI @ 00:39:10]); Microsoft Helps '
                                   '([9Q30FhN41LI @ 00:41:01])'],
                                  ['Missing MPN ID or tenant ID on a marketplace order',
                                   'Ingram Micro Cloud checkout requires the Microsoft Partner Number and '
                                   'indirect reseller domain',
                                   'The NCE order cannot be placed until both identifiers are entered and '
                                   'show ready',
                                   'Ingram Micro Cloud ([W-fGvHNBEiM @ 00:02:09])'],
                                  ['Redeeming package benefits without a usage plan',
                                   "Each benefit's 12-month clock starts the moment that specific benefit "
                                   'is redeemed',
                                   'Redemption timing sets when each benefit window expires, independent '
                                   'of the package renewal',
                                   'Inside Microsoft AI Cloud Partner Program ([jz1cE7UYBO4 @ '
                                   '00:27:25])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before you transact a single seat',
                           'body': 'Each gate below maps to a loss, lockout or stalled payout the speakers '
                                   'reported firsthand. Clear all four before onboarding paying customers.',
                           'items': ['Enroll in Microsoft Commerce Incentives separately; a benefits '
                                     'package or solutions partner designation does not start incentive '
                                     'earnings on its own [Inside Microsoft AI Cloud Partner Program — '
                                     'jz1cE7UYBO4 @ 00:21:41].',
                                     'Make every API automation MFA-ready before the April 2026 cutoff, '
                                     'because non-compliant automation will break [m365 Show | M365, Azure '
                                     'Cloud, Power Platform & AI — by9BiS2U7xo @ 00:14:31].',
                                     'Lock seat counts and term choice inside the 7-day NCE window, since '
                                     'quantities can only go up after that [m365 Show | M365, Azure Cloud, '
                                     'Power Platform & AI — LGgw20GtaDQ @ 00:05:42].',
                                     'Before removing a customer, suspend subscriptions and cancel '
                                     'reservations first; a reseller stays blocked until the provider '
                                     'removes its own relationship [Microsoft Helps — 9Q30FhN41LI @ '
                                     '00:30:55].']}}],
 'pull_quote': '"If you lose a customer you need to gain two customers to offset that one loss." — Ana '
               'Stranaghan of TD SYNNEX, Inside Microsoft AI Cloud Partner Program (jz1cE7UYBO4 @ '
               '00:34:52).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Stand up a legal entity, a domain email (no Gmail or Yahoo), a verifiable address '
                      'and phone, and a live website before applying [Sub-Zero To Wealth — VP4hPTXkPIs @ '
                      '00:01:07].',
                      'Create the Partner Center account under your primary Entra tenant to avoid '
                      'viral-user duplicate or orphaned accounts [m365 Show | M365, Azure Cloud, Power '
                      'Platform & AI — by9BiS2U7xo @ 00:05:03].',
                      'Select Partner, Reseller and Integrate during signup, then enable two-step '
                      'verification on the account [Technical Support Online — wjgyQO9jIAM @ 00:01:44].',
                      'Link your existing partner ID to the CSP indirect reseller account, and use Fix now '
                      'with company documents if the status shows rejected [Horror FM — jUFbUlIkcm0 @ '
                      '00:07:50].',
                      'Place the first NCE order on Ingram Micro Cloud with the MPN ID and indirect '
                      'reseller domain, accept the Microsoft Customer Agreement, then use Track Order '
                      '[Ingram Micro Cloud — W-fGvHNBEiM @ 00:02:09].',
                      'Bundle services on every seat, for example $22 Business Premium plus $8 of '
                      'identity, device management and help desk for $30 [m365 Show | M365, Azure Cloud, '
                      'Power Platform & AI — LGgw20GtaDQ @ 00:04:01].'],
 'statutory_citations': [{'title': 'Pax8 APAC — Microsoft CSP Direct vs Indirect: Which Model Saves You '
                                   'More? [00:05:09]',
                          'url': 'https://www.youtube.com/watch?v=Xywyds1IfvM&t=309s',
                          'relevance': 'Primary practitioner testimony on the direct-bill threshold jump '
                                       'from $300,000 to $1 million and the expected shift of direct '
                                       'partners to indirect providers.'},
                         {'title': 'Inside Microsoft AI Cloud Partner Program — Unlock Microsoft AI Cloud '
                                   'Partner Program Benefits [00:21:41]',
                          'url': 'https://www.youtube.com/watch?v=jz1cE7UYBO4&t=1301s',
                          'relevance': 'Primary practitioner testimony on package pricing, stacked '
                                       'incentive rates, the 60/40 rebate and co-op split, and separate '
                                       'incentive enrollment.'},
                         {'title': 'MicroAge — Everything you need to know about Microsoft licensing for '
                                   'CSP in 2025 | Tech Instinct Podcast Ep.2 [00:15:13]',
                          'url': 'https://www.youtube.com/watch?v=Ap8gUtRq32o&t=913s',
                          'relevance': 'Primary practitioner testimony on CSP-to-CSP transfer refusals, '
                                       'Teams unbundling and CSP commoditization.'},
                         {'title': 'm365 Show | M365, Azure Cloud, Power Platform & AI — Microsoft Cloud '
                                   'Solution Provider (CSP) - Simply Explained [00:05:42]',
                          'url': 'https://www.youtube.com/watch?v=LGgw20GtaDQ&t=342s',
                          'relevance': 'Primary practitioner testimony on NCE term premiums, the 7-day '
                                       'cancel window, seat lock-in and direct-bill prerequisites.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'LGgw20GtaDQ',
                       'title': 'Microsoft Cloud Solution Provider (CSP) - Simply Explained',
                       'channel': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
                       'author': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
                       'text': 'Just 7 days to change your mind or adjust quantities.',
                       'tip': 'Just 7 days to change your mind or adjust quantities.',
                       'timestamp': 342,
                       'timestamp_seconds': 342,
                       'timestamp_label': '[00:05:42]',
                       'url': 'https://www.youtube.com/watch?v=LGgw20GtaDQ&t=342s',
                       'markdown': '[00:05:42](https://www.youtube.com/watch?v=LGgw20GtaDQ&t=342s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LGgw20GtaDQ',
                       'title': 'Microsoft Cloud Solution Provider (CSP) - Simply Explained',
                       'channel': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
                       'author': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
                       'text': 'The partner earns the margin on the service layer, not the software.',
                       'tip': 'The partner earns the margin on the service layer, not the software.',
                       'timestamp': 258,
                       'timestamp_seconds': 258,
                       'timestamp_label': '[00:04:18]',
                       'url': 'https://www.youtube.com/watch?v=LGgw20GtaDQ&t=258s',
                       'markdown': '[00:04:18](https://www.youtube.com/watch?v=LGgw20GtaDQ&t=258s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-zF8JCzzp8w',
                       'title': 'Which Microsoft Partner Level Unlocks the Most Incentives? (AI Cloud '
                                'Explained)',
                       'channel': 'The Crancer Group',
                       'author': 'The Crancer Group',
                       'text': "Basically, 6,000 because it's always a 60/40 split.",
                       'tip': "Basically, 6,000 because it's always a 60/40 split.",
                       'timestamp': 214,
                       'timestamp_seconds': 214,
                       'timestamp_label': '[00:03:34]',
                       'url': 'https://www.youtube.com/watch?v=-zF8JCzzp8w&t=214s',
                       'markdown': '[00:03:34](https://www.youtube.com/watch?v=-zF8JCzzp8w&t=214s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'VP4hPTXkPIs',
                       'title': '✅Affiliate Series Guide 1| Become a Microsoft Partner in 2026| Sell '
                                'Microsoft Products & Solutions',
                       'channel': 'Sub-Zero To Wealth',
                       'author': 'Sub-Zero To Wealth',
                       'text': "Don't just sell a license, sell a complete solution.",
                       'tip': "Don't just sell a license, sell a complete solution.",
                       'timestamp': 349,
                       'timestamp_seconds': 349,
                       'timestamp_label': '[00:05:49]',
                       'url': 'https://www.youtube.com/watch?v=VP4hPTXkPIs&t=349s',
                       'markdown': '[00:05:49](https://www.youtube.com/watch?v=VP4hPTXkPIs&t=349s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'by9BiS2U7xo',
                       'title': 'Microsoft Partner Center - Simply Explained',
                       'channel': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
                       'author': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
                       'text': "If your automation isn't MFA-ready, it will break.",
                       'tip': "If your automation isn't MFA-ready, it will break.",
                       'timestamp': 871,
                       'timestamp_seconds': 871,
                       'timestamp_label': '[00:14:31]',
                       'url': 'https://www.youtube.com/watch?v=by9BiS2U7xo&t=871s',
                       'markdown': '[00:14:31](https://www.youtube.com/watch?v=by9BiS2U7xo&t=871s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9Q30FhN41LI',
                       'title': 'Overview of Microsoft Partner Center Portal, new features, & common '
                                'scenario discussion | Microsoft',
                       'channel': 'Microsoft Helps',
                       'author': 'Microsoft Helps',
                       'text': 'As global Admin is a partner organization role, they will not have access '
                               'to customers tab and it is by design.',
                       'tip': 'As global Admin is a partner organization role, they will not have access '
                              'to customers tab and it is by design.',
                       'timestamp': 2279,
                       'timestamp_seconds': 2279,
                       'timestamp_label': '[00:37:59]',
                       'url': 'https://www.youtube.com/watch?v=9Q30FhN41LI&t=2279s',
                       'markdown': '[00:37:59](https://www.youtube.com/watch?v=9Q30FhN41LI&t=2279s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rD2YxxfsOa4',
                       'title': 'Microsoft Cloud Solution Provider CSP   Simply Explained',
                       'channel': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
                       'author': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
                       'text': 'Indirect partners buy through distributors such as Ingram Micro, Tech Data '
                               'and Rhipe.',
                       'tip': 'Indirect partners buy through distributors such as Ingram Micro, Tech Data '
                              'and Rhipe.',
                       'timestamp': 203,
                       'timestamp_seconds': 203,
                       'timestamp_label': '[00:03:23]',
                       'url': 'https://www.youtube.com/watch?v=rD2YxxfsOa4&t=203s',
                       'markdown': '[00:03:23](https://www.youtube.com/watch?v=rD2YxxfsOa4&t=203s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yNBOfW1MoPs',
                       'title': 'Difference Between CSP Direct Partner, Indirect Provider & Indirect '
                                'Reseller',
                       'channel': 'Spyglass MTG',
                       'author': 'Spyglass MTG',
                       'text': 'The indirect reseller is not responsible for support; support falls back '
                               'to the provider.',
                       'tip': 'The indirect reseller is not responsible for support; support falls back to '
                              'the provider.',
                       'timestamp': 50,
                       'timestamp_seconds': 50,
                       'timestamp_label': '[00:00:50]',
                       'url': 'https://www.youtube.com/watch?v=yNBOfW1MoPs&t=50s',
                       'markdown': '[00:00:50](https://www.youtube.com/watch?v=yNBOfW1MoPs&t=50s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ap8gUtRq32o',
                       'title': 'Everything you need to know about Microsoft licensing for CSP in 2025 | '
                                'Tech Instinct Podcast Ep.2',
                       'channel': 'MicroAge',
                       'author': 'MicroAge',
                       'text': 'CSP is becoming commoditized.',
                       'tip': 'CSP is becoming commoditized.',
                       'timestamp': 1235,
                       'timestamp_seconds': 1235,
                       'timestamp_label': '[00:20:35]',
                       'url': 'https://www.youtube.com/watch?v=Ap8gUtRq32o&t=1235s',
                       'markdown': '[00:20:35](https://www.youtube.com/watch?v=Ap8gUtRq32o&t=1235s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jUFbUlIkcm0',
                       'title': 'Create Microsoft Partner account | Microsoft Partner Center | Partner MPN '
                                'account setup | MPN | CSP',
                       'channel': 'Horror FM',
                       'author': 'Horror FM',
                       'text': 'Link the existing partner ID to the CSP indirect reseller account.',
                       'tip': 'Link the existing partner ID to the CSP indirect reseller account.',
                       'timestamp': 470,
                       'timestamp_seconds': 470,
                       'timestamp_label': '[00:07:50]',
                       'url': 'https://www.youtube.com/watch?v=jUFbUlIkcm0&t=470s',
                       'markdown': '[00:07:50](https://www.youtube.com/watch?v=jUFbUlIkcm0&t=470s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wjgyQO9jIAM',
                       'title': 'Microsoft Partner Center: How to Setup Your Company Profile Correctly',
                       'channel': 'Technical Support Online',
                       'author': 'Technical Support Online',
                       'text': 'Verification takes two to three business days.',
                       'tip': 'Verification takes two to three business days.',
                       'timestamp': 377,
                       'timestamp_seconds': 377,
                       'timestamp_label': '[00:06:17]',
                       'url': 'https://www.youtube.com/watch?v=wjgyQO9jIAM&t=377s',
                       'markdown': '[00:06:17](https://www.youtube.com/watch?v=wjgyQO9jIAM&t=377s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tlmDeX5UBJs',
                       'title': 'I will help to join the Microsoft Partner Program | Join the Microsoft AI '
                                'Cloud Partner Program',
                       'channel': 'Technical Support Online',
                       'author': 'Technical Support Online',
                       'text': 'If the status shows rejected, click Fix now and upload the company '
                               'documents.',
                       'tip': 'If the status shows rejected, click Fix now and upload the company '
                              'documents.',
                       'timestamp': 712,
                       'timestamp_seconds': 712,
                       'timestamp_label': '[00:11:52]',
                       'url': 'https://www.youtube.com/watch?v=tlmDeX5UBJs&t=712s',
                       'markdown': '[00:11:52](https://www.youtube.com/watch?v=tlmDeX5UBJs&t=712s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'W-fGvHNBEiM',
                       'title': 'Tutorial To Transact Microsoft NCE on Ingram Micro Cloud Marketplace',
                       'channel': 'Ingram Micro Cloud',
                       'author': 'Ingram Micro Cloud',
                       'text': 'Please note that mpn id and tenant id is required to place an order.',
                       'tip': 'Please note that mpn id and tenant id is required to place an order.',
                       'timestamp': 129,
                       'timestamp_seconds': 129,
                       'timestamp_label': '[00:02:09]',
                       'url': 'https://www.youtube.com/watch?v=W-fGvHNBEiM&t=129s',
                       'markdown': '[00:02:09](https://www.youtube.com/watch?v=W-fGvHNBEiM&t=129s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uiVjifpxK38',
                       'title': 'Microsoft Partner Center Explained: FY26 Benefits & CSP Guide',
                       'channel': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
                       'author': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
                       'text': "If you're automating anything, every app plus user API call must include "
                               'an MFA token.',
                       'tip': "If you're automating anything, every app plus user API call must include an "
                              'MFA token.',
                       'timestamp': 923,
                       'timestamp_seconds': 923,
                       'timestamp_label': '[00:15:23]',
                       'url': 'https://www.youtube.com/watch?v=uiVjifpxK38&t=923s',
                       'markdown': '[00:15:23](https://www.youtube.com/watch?v=uiVjifpxK38&t=923s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jz1cE7UYBO4',
                       'title': 'Unlock Microsoft AI Cloud Partner Program Benefits',
                       'channel': 'Inside Microsoft AI Cloud Partner Program',
                       'author': 'Inside Microsoft AI Cloud Partner Program',
                       'text': "Just because you have a benefits package or you've earned the solutions "
                               'partner designation does not mean that you automatically start earning the '
                               'incentives.',
                       'tip': "Just because you have a benefits package or you've earned the solutions "
                              'partner designation does not mean that you automatically start earning the '
                              'incentives.',
                       'timestamp': 1301,
                       'timestamp_seconds': 1301,
                       'timestamp_label': '[00:21:41]',
                       'url': 'https://www.youtube.com/watch?v=jz1cE7UYBO4&t=1301s',
                       'markdown': '[00:21:41](https://www.youtube.com/watch?v=jz1cE7UYBO4&t=1301s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jz1cE7UYBO4',
                       'title': 'Unlock Microsoft AI Cloud Partner Program Benefits',
                       'channel': 'Inside Microsoft AI Cloud Partner Program',
                       'author': 'Inside Microsoft AI Cloud Partner Program',
                       'text': 'So if you lose a customer you need to gain two customers to offset that '
                               'one loss.',
                       'tip': 'So if you lose a customer you need to gain two customers to offset that one '
                              'loss.',
                       'timestamp': 2092,
                       'timestamp_seconds': 2092,
                       'timestamp_label': '[00:34:52]',
                       'url': 'https://www.youtube.com/watch?v=jz1cE7UYBO4&t=2092s',
                       'markdown': '[00:34:52](https://www.youtube.com/watch?v=jz1cE7UYBO4&t=2092s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RQe8RvOAGRw',
                       'title': 'Microsoft Partner Benefits Packages: Turn Benefits into Profitability and '
                                'Growth',
                       'channel': 'Microsoft AI Cloud Partner Program',
                       'author': 'Microsoft AI Cloud Partner Program',
                       'text': "I think we're about $30,000 in value that we got with the $4,000 package.",
                       'tip': "I think we're about $30,000 in value that we got with the $4,000 package.",
                       'timestamp': 174,
                       'timestamp_seconds': 174,
                       'timestamp_label': '[00:02:54]',
                       'url': 'https://www.youtube.com/watch?v=RQe8RvOAGRw&t=174s',
                       'markdown': '[00:02:54](https://www.youtube.com/watch?v=RQe8RvOAGRw&t=174s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Xywyds1IfvM',
                       'title': 'Microsoft CSP Direct vs Indirect: Which Model Saves You More?',
                       'channel': 'Pax8 APAC',
                       'author': 'Pax8 APAC',
                       'text': 'So going from 300,000 to a million really means that we might see upwards '
                               'of 2/3 of these partners having to find a new home or moving over to these '
                               'indirect providers.',
                       'tip': 'So going from 300,000 to a million really means that we might see upwards '
                              'of 2/3 of these partners having to find a new home or moving over to these '
                              'indirect providers.',
                       'timestamp': 309,
                       'timestamp_seconds': 309,
                       'timestamp_label': '[00:05:09]',
                       'url': 'https://www.youtube.com/watch?v=Xywyds1IfvM&t=309s',
                       'markdown': '[00:05:09](https://www.youtube.com/watch?v=Xywyds1IfvM&t=309s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'}]}
