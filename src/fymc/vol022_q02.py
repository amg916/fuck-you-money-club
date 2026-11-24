from __future__ import annotations

CHAPTER_2 = {'id': 'Q2',
 'chapter_id': 'Q2',
 'chapter_number': 2,
 'question_number': 2,
 'slug': 'sourcing-shipping-selling-medical-equipment-across-borders',
 'question_prompt': 'How do resellers vet refurbishers, move equipment safely across borders, and sell '
                    'into international markets?',
 'kicker': 'Q2 / THE BIG MONEY PLAYBOOKS',
 'title': 'Sourcing, Shipping, and Selling Across Borders',
 'subtitle': 'Questions to ask refurbishment providers, biomed savings from used gear, data erasure before '
             'resale, imaging data and HIPAA, specialized medical freight, U.S. import steps, UAE/MOHAP '
             'trading licenses, China NMPA exports, FDA vs. Health Canada, Latin American market outlooks, '
             'distributor licensing, and supplier bookkeeping',
 'layout_template': 'executive_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners working the resale lane agree that the money sits in the gap between '
                      'OEM pricing and the secondary market. A Dutch refurbisher exhibiting with ARABLAB '
                      'resells five-to-six-year-old pharma lab systems at more than 50% below new, and a '
                      'hospital biomed documents eBay buys of $200-$300 replacing $1,200-$2,200 OEM parts '
                      'and repairs, plus a camera-head trade-in loop that saved $10,000-plus. The shared '
                      'prerequisites are ISO-certified refurbishing, documented HIPAA data removal, '
                      'internal decontamination, and air-ride, climate-controlled freight with insurance '
                      'matched to cargo value. Across borders, Latin American buyers want to see and touch '
                      'equipment, reject tier-3 gear and cluster in major cities, so Global Health '
                      'Intelligence filters for private hospitals above 100 beds. Disagreements center on '
                      'entering Canada or the US first, free-zone versus mainland setup in Dubai, and '
                      'whether hospital purchasing will ever approve used units bought for parts.',
 'key_metrics': [{'label': 'Refurbished Lab System Discount vs New',
                  'metric': 'Refurbished Lab System Discount vs New',
                  'value': 'More than 50% less than buying new',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Refurbisher buying five-to-six-year-old HPLC, GC and GCMS units from big '
                             'pharmaceutical companies, rebuilding, testing and reselling with a test '
                             'report',
                  'source': 'EXPO NEWS ([U-LBQwafIo8 @ 00:01:38])'},
                 {'label': 'Camera-Head Trade-In Savings',
                  'metric': 'Camera-Head Trade-In Savings',
                  'value': '$10,000-plus saved from an ~$800 eBay box against $2,500 credit per head',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Storz offered one-for-one trade credit; the hospital held 3-4 heads but was '
                             'buying 10, so used heads from eBay filled the gap',
                  'source': 'Better Biomed Channel ([sgJKIx288kY @ 00:15:38])'},
                 {'label': 'Average Latin American Hospital Size',
                  'metric': 'Average Latin American Hospital Size',
                  'value': '44 beds vs more than 160 in the US and Europe',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Chile is the only market above 100 beds; small size limits investment in '
                             'robotics, linacs, CT, MRI and even x-ray',
                  'source': 'Global Health Intelligence ([8l8Q1Q45u1s @ 00:06:17])'},
                 {'label': 'Brazil Private Hospital Prospect Filter',
                  'metric': 'Brazil Private Hospital Prospect Filter',
                  'value': '195 targets from 1,800-plus private institutions at 100-plus beds',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'HospiScope filter on a database of more than 19,000 profiles, exported to '
                             'Excel and loaded into the CRM',
                  'source': 'Global Health Intelligence ([FzWeG7sw7qk @ 00:01:46])'}],
 'sections': [{'heading': '1. The Practitioner Consensus',
               'paragraphs': ['The core engine every resale operator describes is the same: buy aged '
                              'equipment from institutions that are dumping it, restore it, and sell it '
                              'far under OEM list. The Dutch refurbisher exhibiting with ARABLAB at Expo '
                              'News Dubai buys five-to-six-year-old HPLC, GC and GCMS systems directly '
                              'from big pharmaceutical companies, brings them into its own facility, '
                              "rebuilds them 'like new,' runs a test, issues a test report and pushes them "
                              'back to market [U-LBQwafIo8 @ 00:00:59]. The pitch to buyers is simple: '
                              'refurbished costs more than 50% less than a new system [U-LBQwafIo8 @ '
                              '00:01:38]. The Better Biomed Channel host runs the buy side of the same '
                              'arbitrage from inside a hospital. Used units get bought either as parts '
                              'donors or as whole replacements, and a used unit off eBay or DotMed is '
                              "frequently cheaper than the OEM's flat-rate repair on the broken one "
                              '[sgJKIx288kY @ 00:01:56] [sgJKIx288kY @ 00:05:45]. That host frames the '
                              "savings bluntly as 'free money for the hospital' and free money for the "
                              'biomed shop, with the instruction not to spend every dollar the budget '
                              'allows. The shared baseline is that the margin lives in the spread between '
                              'OEM pricing on parts, repairs and new systems and what the secondary market '
                              'actually clears at, and both operators build their whole workflow around '
                              'capturing that spread rather than around new-unit list prices.',
                              'The second point of agreement is that buyers only trust refurbished gear '
                              'that arrives with a paper trail. Block Imaging lays out the vetting script: '
                              'confirm the refurbishment process is ISO-certified, demand process '
                              'documentation, verify a HIPAA data-removal step so the buyer is not fined '
                              'for holding information it should not have, and insist on internal '
                              'decontamination because dust clogs fans and is a biohazard [xvO7-DA6X2w @ '
                              '00:00:35] [xvO7-DA6X2w @ 00:01:37]. DES Technologies pushes the data line '
                              "harder, calling erasure 'a compliance necessity' under FDA, GDPR and "
                              "'HIPPA' (as spoken), with methods running from software wiping to physical "
                              'destruction, backed by audit reports that make the erasure verifiable '
                              '[xzb3hv6fB4g @ 00:01:19]. The hospital buy side confirms the certification '
                              'requirement from the purchasing desk: Better Biomed Channel notes an '
                              'ISO-certified vendor is required before the hospital can pay, which is the '
                              'entire reason the FOBI middleman exists [sgJKIx288kY @ 00:09:20]. Block '
                              'Imaging adds two proof demands before money moves: an unedited '
                              'functionality video and QA results showing the system runs within the '
                              "original manufacturer's specifications. The operator takeaway is consistent "
                              'across all three channels: certification, wipe records, decontamination and '
                              'test evidence are the price of entry, not optional upsells, and a seller '
                              'who cannot produce them is cut out of institutional deals.',
                              'Once gear crosses a border or a state line, the practitioners converge on '
                              'two rules: ship it like the fragile instrument it is, and sell it where the '
                              'buyer can touch it. Ntwdequiptrans warns that treating CT scanners, beds or '
                              "imaging systems as a standard load leads to delays, damage and 'thousands "
                              "of dollars lost,' because stacking and rough handling throw calibration "
                              'off, so loads need air-ride trailers, climate control and carriers who have '
                              'moved medical loads before [LXOka69hkxs @ 00:00:18] [LXOka69hkxs @ '
                              '00:00:53]. ISF Customs Broker echoes the experienced-carrier point for '
                              'imports into the USA and adds that CBP wants an accurate invoice, proof of '
                              'FDA compliance and payment of duties [r84DBdhhg1k @ 00:00:57]. On the '
                              'selling end, Thomas Gibson of Med Global Group tells Healthcare Direct USA '
                              "that Latin American buyers are 'show me don't tell me,' the physician is "
                              'often the purchaser, the market is price-driven, and parts plus support are '
                              "what build loyalty [09hrQ3SQK3E @ 00:04:21]. Gibson's prescription is a "
                              'physical presence in Monterrey, Guadalajara or Mexico City so buyers can '
                              'see, touch and feel the equipment before committing. Nobody in this group '
                              'argues for blind, unsupported cross-border drops; the consensus model is '
                              'protected freight, clean paperwork and a reachable local footprint.'],
               'table': {'caption': 'Where the resale practitioners line up on the same baseline mechanics',
                         'headers': ['Consensus Point',
                                     'What Practitioners Do',
                                     'Why It Matters',
                                     'Expert Source'],
                         'rows': [['Buy aged gear from large institutions',
                                   'Source five-to-six-year-old HPLC, GC and GCMS units from big pharma',
                                   'Refurbished resale lands more than 50% under new pricing',
                                   'EXPO NEWS ([U-LBQwafIo8 @ 00:00:42])'],
                                  ['Used unit beats OEM flat-rate repair',
                                   'Pull replacement units from eBay or DotMed instead of OEM repair',
                                   'A whole used unit often costs less than one repair',
                                   'Better Biomed Channel ([sgJKIx288kY @ 00:05:45])'],
                                  ['ISO-certified refurbishment process is the entry ticket',
                                   'Ask the refurbisher for ISO certification and written process '
                                   'documentation',
                                   'Undocumented refurbishing gives buyers no proof of consistent quality',
                                   'Block Imaging ([xvO7-DA6X2w @ 00:00:35])'],
                                  ['Patient data must be wiped and proven',
                                   'Run software wiping or physical destruction backed by audit reports',
                                   'Verifiable erasure protects patients and cuts seller liability '
                                   'exposure',
                                   'DES Technologies ([xzb3hv6fB4g @ 00:01:19])'],
                                  ['Medical freight is never treated as regular freight',
                                   'Use air-ride trailers, climate control and experienced medical '
                                   'carriers',
                                   'Stacking and rough handling throw calibration off and cost thousands',
                                   'Ntwdequiptrans ([LXOka69hkxs @ 00:00:53])'],
                                  ['Latin American buyers must see the gear first',
                                   'Set up stock in Monterrey, Guadalajara or Mexico City locations',
                                   "Buyers are show-me-don't-tell-me and the physician often buys",
                                   'Healthcare Direct USA ([09hrQ3SQK3E @ 00:06:56])'],
                                  ['Tier-three equipment no longer moves south of the border',
                                   'Stock Olympus 180/190 endoscopy systems rather than older 160 units',
                                   'Buyer demand shifted upward over the last five to six years',
                                   'Healthcare Direct USA ([09hrQ3SQK3E @ 00:10:03])']]}},
              {'heading': '2. Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Better Biomed Channel supplies the most granular unit economics, and nearly '
                              'every number runs through eBay. A Steris 3080 table bought for $3,000 total '
                              'became a parts donor whose castings, shrouds, tops and control board saved '
                              "'thousands' [sgJKIx288kY @ 00:03:11]. When the Belmont rapid infuser's OEM "
                              'touch panel priced at about $1,200, the host bought two whole Belmonts on '
                              'eBay at $200-$300 each, roughly $500 total; both arrived in better shape '
                              'than the inventory units and turned one working infuser into two in service '
                              '[sgJKIx288kY @ 00:04:07]. A Storz HD Connect runs $200-$300 on eBay, so one '
                              'flat-rate repair buys three units, one deployed and two shelved. A Sony '
                              'UP-DR80MD printer that Storz quoted at $2,200 sells for $200-$300, and a '
                              'Stryker recorder at $200 is treated as a consumable: retire the dead unit '
                              'and drop the eBay unit straight into service [sgJKIx288kY @ 00:13:48]. '
                              'Those spreads run far deeper than the more-than-50% discount the Dutch lab '
                              'refurbisher at Expo News Dubai quotes on rebuilt HPLC and GC systems, which '
                              'still come with a test report and software for add-ons like the Swiss CTC '
                              'autosampler that fits any brand of GC [U-LBQwafIo8 @ 00:01:38]. The '
                              'operating rule is to price the whole used unit first and treat the OEM '
                              'quote as the ceiling, not the benchmark.',
                              'The sharpest street move is the trade-in loop. Storz offered $2,500 credit '
                              'per old camera head on a one-for-one basis, but the hospital only held '
                              'three or four heads against a purchase of ten, so the Better Biomed host '
                              'bought a box of used heads on eBay for about $800, fed them in as trade-ins '
                              "and saved $10,000-plus; in the host's words, 'all you need is a camera and "
                              "a serial number' [sgJKIx288kY @ 00:15:38]. ESUs run the same math, with "
                              'used units at $200-$500 against a $2-3K trade credit [sgJKIx288kY @ '
                              '00:16:10]. Because the hospital needs an ISO-certified vendor on the '
                              'invoice, the workaround is FOBI: the biomed sends FOBI the online listing, '
                              "FOBI buys it and invoices the hospital with a 'slight markup' [sgJKIx288kY "
                              '@ 00:10:24]. On the cross-border sell side, the Healthcare Direct USA '
                              'platform applies the same friction-removal logic: a shipping API shows '
                              'buyers carrier options and costs, sellers must post warranties, and the '
                              'platform mediates disputes because buyers balk at wiring money to strangers '
                              "or spending 'two or three grand' on a US trip to inspect a unit "
                              '[09hrQ3SQK3E @ 00:13:27]. Each tactic strips one specific objection out of '
                              'the transaction, whether it comes from purchasing, the OEM rep or a buyer '
                              'sitting in another country.',
                              'For prospecting abroad, Global Health Intelligence runs a repeatable filter '
                              'in HospiScope: start with private institutions because they decide faster, '
                              'pick Brazil as the largest market, set minimum beds to 100 with an open '
                              "upper bound, and a database of more than 19,000 profiles narrows Brazil's "
                              '1,800-plus private institutions to 195 targets, exported to Excel and '
                              'loaded into the CRM [FzWeG7sw7qk @ 00:01:46]. The bed cutoff matters '
                              'because Latin American hospitals average 44 beds versus more than 160 in '
                              'the US and Europe, Chile is the only market above 100, and small size caps '
                              'investment in CT, MRI, robotics and even x-ray [8l8Q1Q45u1s @ 00:06:17]. '
                              "The same team's tactic is to target major cities rather than chase "
                              'countrywide coverage, with Panama and Costa Rica standing out [e1ChWLjN_6Q '
                              '@ 00:29:52]. Once a deal closes, Ntwdequiptrans sets the freight spec: no '
                              'stacking, air-ride, climate control, a carrier with prior medical loads, a '
                              'plan for hospitals with timed or restricted access, and, for six-figure '
                              "machines, carrier insurance verified against freight value 'before the "
                              "wheels ever start turning' [LXOka69hkxs @ 00:01:55]. The stated goal on "
                              "every load is to be 'right,' not cheapest or fastest."],
               'table': {'caption': 'Street prices and trade math reported by the operators',
                         'headers': ['Item or Move',
                                     'Street Price or Number',
                                     'Comparison Point',
                                     'Expert Source'],
                         'rows': [['Belmont rapid infuser whole units bought on eBay',
                                   'Two units at $200-$300 each, about $500 total',
                                   'OEM touch panel alone costs about $1,200',
                                   'Better Biomed Channel ([sgJKIx288kY @ 00:04:07])'],
                                  ['Storz HD Connect bought as used spares',
                                   '$200-$300 each on eBay listings',
                                   'One flat-rate repair buys three, two go on shelf',
                                   'Better Biomed Channel ([sgJKIx288kY @ 00:11:02])'],
                                  ['Sony UP-DR80MD printer replacement from eBay',
                                   '$200-$300 per unit on eBay',
                                   'Storz quoted $2,200 for the same printer',
                                   'Better Biomed Channel ([sgJKIx288kY @ 00:12:54])'],
                                  ['Spy Elite navigation system complete tower replacement',
                                   '$2,500 for tower, computer, camera, arm and chassis',
                                   'Leased unit valued around $30-40K at full replacement',
                                   'Better Biomed Channel ([sgJKIx288kY @ 00:08:04])'],
                                  ['Used camera heads fed into OEM trade-ins',
                                   'About $800 for a box of heads on eBay',
                                   'Storz credited $2,500 per head, saving $10K-plus total',
                                   'Better Biomed Channel ([sgJKIx288kY @ 00:15:38])'],
                                  ['Used ESUs bought to capture trade credit',
                                   '$200-$500 per used ESU purchased',
                                   'Trade credit worth $2-3K per unit offered',
                                   'Better Biomed Channel ([sgJKIx288kY @ 00:16:10])'],
                                  ['HospiScope Brazil private hospital prospect filter run',
                                   '195 targets at 100-plus beds with open ceiling',
                                   'Pulled from more than 19,000 hospital profiles in database',
                                   'Global Health Intelligence ([FzWeG7sw7qk @ 00:01:46])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Moves the operators actually run',
                           'body': 'These are the specific levers the practitioners pull to widen margin, '
                                   'prove quality and keep cross-border buyers from walking [Better Biomed '
                                   'Channel — sgJKIx288kY @ 00:16:42].',
                           'items': ['Price a whole used unit on eBay or DotMed before approving any OEM '
                                     'flat-rate repair; the used unit often comes in under the repair '
                                     'quote [Better Biomed Channel — sgJKIx288kY @ 00:05:45]',
                                     'Demand an unedited functionality video and pre-ship QA results '
                                     "proving the system runs within the original manufacturer's "
                                     'specifications [Block Imaging — xvO7-DA6X2w @ 00:03:05]',
                                     "On six-figure machines, verify the carrier's insurance lines up with "
                                     'the freight value before pickup [Ntwdequiptrans — LXOka69hkxs @ '
                                     '00:01:55]',
                                     'Route unanswered buyer messages to email after about 15 minutes and '
                                     'send Spanish-speaking buyers to Spanish-speaking reps so no lead is '
                                     'lost [Healthcare Direct USA — 09hrQ3SQK3E @ 00:20:15]']},
               'sop_steps': [{'step': 1,
                              'title': 'Source below OEM',
                              'action': 'Buy aged systems from large institutions or pull whole units from '
                                        'eBay and DotMed.',
                              'detail': 'Target five-to-six-year-old HPLC, GC and GCMS units from big '
                                        'pharma [EXPO NEWS — U-LBQwafIo8 @ 00:00:42], and price whole used '
                                        'units against OEM repair quotes, buying extras as shelf spares '
                                        '[Better Biomed Channel — sgJKIx288kY @ 00:11:02].'},
                             {'step': 2,
                              'title': 'Refurbish and document',
                              'action': 'Run an ISO-certified process with HIPAA data removal, internal '
                                        'decontamination and a test report.',
                              'detail': 'Document each step, wipe patient data, clear dust from fans, and '
                                        'hold QA results plus an unedited functionality video ready for '
                                        'the buyer before shipping [Block Imaging — xvO7-DA6X2w @ '
                                        '00:01:14].'},
                             {'step': 3,
                              'title': 'Ship as medical freight',
                              'action': 'Book air-ride, climate-controlled transport with an experienced '
                                        'medical carrier.',
                              'detail': 'Ban stacking, plan for timed or restricted hospital access, and '
                                        'match carrier insurance to freight value [Ntwdequiptrans — '
                                        'LXOka69hkxs @ 00:01:08]; on US imports, carry an accurate invoice '
                                        'and proof of FDA compliance for CBP [ISF Customs Broker — '
                                        'r84DBdhhg1k @ 00:00:57].'},
                             {'step': 4,
                              'title': 'Target and list abroad',
                              'action': 'Filter for private hospitals above 100 beds in major cities and '
                                        'list with warranties on a buyer-facing platform.',
                              'detail': 'Run the HospiScope private, Brazil, 100-plus-bed filter and load '
                                        'results into the CRM [Global Health Intelligence — FzWeG7sw7qk @ '
                                        '00:02:05]; list on the Healthcare Direct USA platform, where the '
                                        '90-day premium trial allows 1,200 listings of equipment, parts or '
                                        'services [Healthcare Direct USA — 09hrQ3SQK3E @ 00:16:59].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is how much process you buy along with the hardware. '
                              'Better Biomed Channel runs a raw secondary-market play: an OEM Belmont '
                              'rapid infuser touch panel costs about $1,200, while two whole Belmont units '
                              'off eBay at $200 to $300 each came to roughly $500 and put two infusers in '
                              'service instead of one [sgJKIx288kY @ 00:04:07]. The same biomed argues a '
                              'used unit from eBay or DotMed is often cheaper than the OEM flat-rate '
                              'repair, and because an ISO-certified vendor is required, FOBI buys the '
                              'online listing and invoices the hospital at a slight markup [sgJKIx288kY @ '
                              '00:05:45] [sgJKIx288kY @ 00:10:24]. Block Imaging pushes the opposite '
                              'discipline: demand an ISO-certified refurbishment process, written process '
                              'documentation, an unedited functionality video and QA results before the '
                              'system ships, treating that QA as proof the unit functions within the '
                              "original manufacturer's specifications [xvO7-DA6X2w @ 00:00:35] "
                              '[xvO7-DA6X2w @ 00:03:05]. The Dutch lab-resale exhibitor on EXPO NEWS sits '
                              'between the two, pulling five-to-six-year-old HPLC, GC and GCMS units from '
                              'big pharmaceutical companies, refurbishing them like new, testing them, '
                              'issuing a test report, and selling at more than 50% under new [U-LBQwafIo8 '
                              '@ 00:01:38]. Better Biomed Channel goes further still, treating a $200 '
                              'Stryker recorder as a consumable to retire and replace straight off eBay '
                              '[sgJKIx288kY @ 00:13:48].',
                              'Where to plant the regulatory flag first splits operators too. Quality '
                              'Smart Solutions reports some companies enter Canada first because the '
                              'process is more predictable and generates postmarket data, while others go '
                              'to the US first for market size and reimbursement; the catch on the '
                              'Canadian side is that ISO 13485 through an MDSAP registrar is required '
                              'before licensing, which the speaker calls a big hurdle [4ICxQIfTktg @ '
                              '00:03:12] [4ICxQIfTktg @ 00:02:51]. In the Gulf, A&A Associate LLC lays out '
                              'a mainland-versus-free-zone fork: mainland setup is needed to bid DHA, DoH '
                              'and MOH tenders and to run a showroom, while free zones such as Dubai '
                              'Healthcare City, RAKEZ and SRTIP are cheaper for re-export and still sell '
                              'into the mainland through local distributors or registered agents '
                              '[PoaIdM80c3c @ 00:00:49] [PoaIdM80c3c @ 00:01:22]. For China, Intertek '
                              "describes the route itself changing under the operator's feet: the "
                              'traditional path forced government-lab testing inside China with no '
                              'exemption, while Announcement 126, published October 2021, allows '
                              'self-testing reports from an internal lab meeting the QMS requirement or a '
                              'CMA-accredited third party [NTlv6-PNAuI @ 00:05:36]. The trade-off is lab '
                              'scarcity, with only 63 CMA labs, about 50 of them government-run, and three '
                              'accredited international labs, Intertek among them [NTlv6-PNAuI @ '
                              '00:09:07].',
                              'On Latin America, both camps agree the demand is real, but they split hard '
                              'on how to sell into it. Thomas Gibson of Med Global Group, interviewed by '
                              "host Sean on Healthcare Direct USA, describes a show-me-don't-tell-me buyer "
                              'who wants to see, touch and feel equipment, where the physician is often '
                              'the purchaser and price drives the deal, and advises locating in Monterrey, '
                              'Guadalajara or Mexico City [09hrQ3SQK3E @ 00:04:21] [09hrQ3SQK3E @ '
                              '00:06:56]. Sean adds that tier 3 equipment cannot move there at all '
                              'anymore; buyers now want Olympus 180 and 190 endoscopy systems rather than '
                              'the 160 [09hrQ3SQK3E @ 00:10:03]. Global Health Intelligence works top-down '
                              'from data instead: filter HospiScope to private institutions because they '
                              'decide faster, start in Brazil as the largest market, and set a 100-bed '
                              'floor for more sophisticated purchasing, which returned 195 prospects '
                              '[FzWeG7sw7qk @ 00:00:39] [FzWeG7sw7qk @ 00:01:46]. GHI also tells sellers '
                              'to hit major cities rather than chase countrywide coverage, and flags '
                              'Chile, at about 400 hospitals, as easy to test in [e1ChWLjN_6Q @ 00:29:52] '
                              '[8l8Q1Q45u1s @ 00:48:14]. Healthcare Direct USA counters with a '
                              'smaller-hospital reality: private hospitals across the region run just 15 '
                              'to 20 beds, against roughly 60% public healthcare covering about 80% of the '
                              'population, with Mexico itself near 50/50 public and private [09hrQ3SQK3E @ '
                              '00:11:36].'],
               'table': {'caption': 'Competing playbooks for sourcing, proving, registering and selling '
                                    'medical equipment across borders',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Sourcing replacement and spare hospital units',
                                   'Buy whole used units off eBay or DotMed when they undercut OEM '
                                   'flat-rate repair',
                                   'Demand ISO-certified refurbishment, written process documentation and '
                                   'pre-ship QA results',
                                   'Better Biomed Channel ([sgJKIx288kY @ 00:05:45]); Block Imaging '
                                   '([xvO7-DA6X2w @ 00:00:35])'],
                                  ['Getting used gear past hospital procurement',
                                   'FOBI, an ISO-certified middleman, buys the listing and invoices at '
                                   'slight markup',
                                   'Cash in OEM trade-ins: Storz paid $2,500 credit per old camera head',
                                   'Better Biomed Channel ([sgJKIx288kY @ 00:10:24]); Better Biomed '
                                   'Channel ([sgJKIx288kY @ 00:15:38])'],
                                  ['Proving condition to the buyer',
                                   'Refurbisher tests the instrument and issues its own test report before '
                                   'resale',
                                   'Buyer demands an unedited functionality video plus QA results before '
                                   'shipping',
                                   'EXPO NEWS ([U-LBQwafIo8 @ 00:00:59]); Block Imaging ([xvO7-DA6X2w @ '
                                   '00:02:36])'],
                                  ['First regulated market for a device',
                                   'Canada first for predictability and postmarket data, despite the MDSAP '
                                   'hurdle',
                                   'US first for market size and reimbursement via 510(k) or PMA',
                                   'Quality Smart Solutions ([4ICxQIfTktg @ 00:03:12]); Quality Smart '
                                   'Solutions ([4ICxQIfTktg @ 00:01:25])'],
                                  ['Dubai company structure for equipment trade',
                                   'Mainland setup to bid DHA, DoH and MOH tenders and run showrooms',
                                   'Free zone such as Dubai Healthcare City, RAKEZ or SRTIP, cheaper for '
                                   're-export',
                                   'A&A Associate LLC ([PoaIdM80c3c @ 00:00:49]); A&A Associate LLC '
                                   '([PoaIdM80c3c @ 00:01:22])'],
                                  ['China type testing route under NMPA',
                                   'Old route: government-lab testing inside China with no exemption '
                                   'allowed',
                                   'Announcement 126 self-testing through a QMS-compliant internal lab or '
                                   'CMA third party',
                                   'Intertek ([NTlv6-PNAuI @ 00:05:36]); Intertek ([NTlv6-PNAuI @ '
                                   '00:09:07])'],
                                  ['Latin America go-to-market motion',
                                   'Physical presence in Monterrey, Guadalajara or Mexico City for show-me '
                                   'buyers',
                                   'HospiScope filter on private, Brazil, 100-plus beds, then export to '
                                   'Excel and CRM',
                                   'Healthcare Direct USA ([09hrQ3SQK3E @ 00:06:56]); Global Health '
                                   'Intelligence ([FzWeG7sw7qk @ 00:02:05])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['Freight and customs are where margin evaporates fastest on cross-border '
                              'deals. Ntwdequiptrans warns that treating CT scanners, hospital beds or '
                              'imaging systems like a standard load leads to delays, damage and thousands '
                              'of dollars lost, and that stacking or rough handling can throw calibration '
                              "off [LXOka69hkxs @ 00:00:18] [LXOka69hkxs @ 00:00:35]. The operator's fix "
                              'is air-ride trailers, climate control, and only carriers who have moved '
                              "medical loads before, plus a hard check that the carrier's insurance lines "
                              'up with the freight value on six-figure machines before the wheels turn; '
                              'hospital deliveries also land in timed or restricted access windows '
                              '[LXOka69hkxs @ 00:00:53] [LXOka69hkxs @ 00:01:55]. ISF Customs Broker, '
                              'which also tells importers to use experienced carriers, stacks the '
                              'paperwork trap on top: CBP wants an accurate invoice, proof of FDA '
                              'compliance and duties paid, FDA classification decides whether premarket '
                              'approval or registration applies, and post-import record-keeping and '
                              'postmarket surveillance follow the unit [r84DBdhhg1k @ 00:00:57] '
                              '[r84DBdhhg1k @ 00:01:36]. Better Biomed Channel shows the downstream cost '
                              'of damage on a lease: a Spy Elite navigation system worth about $30,000 to '
                              '$40,000 had its arm cracked through user abuse, could not be returned, and '
                              'total replacement value was demanded, even though a whole replacement tower '
                              'sat on eBay for $2,500 [sgJKIx288kY @ 00:07:22] [sgJKIx288kY @ 00:08:04].',
                              'Data left on a resold unit is the trap that turns into fines. Block Imaging '
                              'asks every refurbisher whether a HIPAA data-removal step is built into the '
                              'process, because it keeps the buyer from being fined for holding '
                              'information they are not supposed to have, and separately whether internal '
                              'decontamination happens, since dust clogs fans and is a biohazard '
                              '[xvO7-DA6X2w @ 00:01:14] [xvO7-DA6X2w @ 00:01:37]. DES Technologies frames '
                              'erasure as a compliance necessity under FDA, GDPR and HIPAA, ranging from '
                              'software wiping to physical destruction, backed by documentation and '
                              'verifiable audit reports, though its own narration muddles the point by '
                              'claiming information remains intact and confidential after destruction '
                              '[xzb3hv6fB4g @ 00:00:40] [xzb3hv6fB4g @ 00:01:19]. On the data-monetization '
                              'side, Gareth Hoile of Sell My Data To AI flags the deeper traps: disclosing '
                              'a re-identification code counts as disclosing PHI, the linkage key for '
                              'follow-up studies must stay out of the package, de-identification has to '
                              'cover header attributes, burned-in pixel text and anatomy, which matters '
                              'for head CT and MRI, and DICOM Part 15 Annex E does not guarantee full '
                              'removal, so buyers expect a re-identification test on a sample [K2WVBO_rnnA '
                              '@ 00:01:34] [K2WVBO_rnnA @ 00:02:29]. Chain of title is the last landmine: '
                              'a radiology or teleradiology group may hold rights in the reports '
                              '[K2WVBO_rnnA @ 00:02:46].',
                              'The rest of the losses come from people, paperwork and process, not '
                              'hardware. Better Biomed Channel reports many hospitals refuse the '
                              'used-parts play because purchasing will not buy used units for parts, that '
                              'dropping service contracts only works if manpower is added to absorb the '
                              'extra work, and that even an approved $2,500 eBay replacement for the '
                              'cracked Spy Elite stalled on snags [sgJKIx288kY @ 00:02:54] [sgJKIx288kY @ '
                              '00:01:34] [sgJKIx288kY @ 00:09:00]. On the cross-border buyer side, '
                              'Healthcare Direct USA says wiring money to strangers is risky and a US trip '
                              'costs two or three grand, which is why the platform requires seller '
                              'warranties and mediates disputes [09hrQ3SQK3E @ 00:13:27] [09hrQ3SQK3E @ '
                              '00:14:15]. Global Health Intelligence adds the macro brakes: financing '
                              'slows private purchases in Latin America, and trained staff is a bottleneck '
                              'even where robotics has room for several hundred more units, with patient '
                              'flow, savvy, financing and leasing named as barriers [e1ChWLjN_6Q @ '
                              "00:32:11] [8l8Q1Q45u1s @ 00:46:28]. Intertek's China numbers show the time "
                              'cost of the old route: an average of 6 months just to schedule '
                              'government-lab testing and 18 months to complete it, with most documents '
                              'and the test report required in Chinese, and the manufacturer, not the lab, '
                              'files the submission to NMPA [NTlv6-PNAuI @ 00:11:07] [NTlv6-PNAuI @ '
                              '00:16:30].'],
               'table': {'caption': 'Firsthand traps and the economics check each practitioner runs '
                                    'against them',
                         'headers': ['Trap',
                                     'What Practitioners Report',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Shipping medical gear as standard freight',
                                   'Stacking and rough handling throw calibration off, causing delays and '
                                   'damage',
                                   'Losses run to thousands; match carrier insurance to six-figure freight '
                                   'value',
                                   'Ntwdequiptrans ([LXOka69hkxs @ 00:00:35]); Ntwdequiptrans '
                                   '([LXOka69hkxs @ 00:01:55])'],
                                  ['Incomplete import paperwork at the US border',
                                   'CBP requires an accurate invoice, proof of FDA compliance and paid '
                                   'duties',
                                   'FDA classification decides premarket approval versus registration '
                                   'before the shipment lands',
                                   'ISF Customs Broker ([r84DBdhhg1k @ 00:00:57]); ISF Customs Broker '
                                   '([r84DBdhhg1k @ 00:00:38])'],
                                  ['Paying OEM flat-rate repair by default',
                                   'Storz wanted $2,200 to handle a Sony UP-DR80MD medical printer',
                                   'eBay sells the same Sony printers for roughly $200 to $300 each',
                                   'Better Biomed Channel ([sgJKIx288kY @ 00:12:54])'],
                                  ['Damaged leased capital equipment on the floor',
                                   'Cracked Spy Elite arm blocked return; total replacement value demanded '
                                   'on $30-40K unit',
                                   'Whole replacement tower sat on eBay for $2,500, then stalled on snags',
                                   'Better Biomed Channel ([sgJKIx288kY @ 00:07:22]); Better Biomed '
                                   'Channel ([sgJKIx288kY @ 00:09:00])'],
                                  ['Patient data left on resold systems',
                                   'A missing HIPAA data-removal step exposes the equipment holder to '
                                   'fines',
                                   'Require documented erasure backed by verifiable audit reports before '
                                   'the unit lists',
                                   'Block Imaging ([xvO7-DA6X2w @ 00:01:37]); DES Technologies '
                                   '([xzb3hv6fB4g @ 00:01:19])'],
                                  ["Lab scarcity under China's NMPA testing regime",
                                   'Only 63 CMA labs exist, and about 50 of them are government-run',
                                   'Old route averaged 6 months to schedule and 18 months to complete '
                                   'testing',
                                   'Intertek ([NTlv6-PNAuI @ 00:09:07]); Intertek ([NTlv6-PNAuI @ '
                                   '00:11:07])'],
                                  ['Untracked rental, warranty and maintenance costs in the books',
                                   'Supplier bookkeeping covers rental income, delivery, installation, '
                                   'warranty and maintenance costs',
                                   'Reconcile AR/AP and inventory cost records in QuickBooks Online, Xero '
                                   'or Wave',
                                   'Cloud Accounting World ([ll03lU-_2LM @ 00:02:05]); Cloud Accounting '
                                   'World ([ll03lU-_2LM @ 00:03:14])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Clear These Four Checks Before a Unit Crosses a Border',
                           'body': 'Each check maps to a loss, stall or fine a practitioner reported '
                                   'firsthand: damaged freight, blocked purchasing, leftover patient data, '
                                   'and missed licensing windows.',
                           'items': ['Confirm the carrier has moved medical loads before and that its '
                                     'insurance lines up with the freight value before the wheels start '
                                     'turning [Ntwdequiptrans — LXOka69hkxs @ 00:01:55].',
                                     "Clear purchasing's stance on used units for parts and route the buy "
                                     'through an ISO-certified vendor such as FOBI before promising '
                                     'savings [Better Biomed Channel — sgJKIx288kY @ 00:02:54].',
                                     'Get the HIPAA data-removal step, internal decontamination and '
                                     'pre-ship QA results confirmed by the refurbisher before payment '
                                     '[Block Imaging — xvO7-DA6X2w @ 00:01:37].',
                                     'For an FDA-licensed 3PL, file the new-location application no later '
                                     'than 90 calendar days before operations and complete annual '
                                     'reporting between January 1 and March 31 [U.S. Food and Drug '
                                     'Administration — an4G9gKy9wE @ 00:31:50].']}}],
 'pull_quote': '"I only work with experienced carriers who\'ve moved medical loads before because the cost '
               'of inexperience is just too high." — Ntwdequiptrans (LXOka69hkxs @ 00:01:08)',
 'diagram_id': 'diag-04',
 'action_checklist': ['Price every OEM flat-rate repair against a whole used unit on eBay or DotMed before '
                      'approving it [Better Biomed Channel — sgJKIx288kY @ 00:05:45].',
                      'Buy old camera heads and ESUs cheaply on eBay to cash in OEM trade-in credits, '
                      'since all you need is a camera and a serial number [Better Biomed Channel — '
                      'sgJKIx288kY @ 00:15:38].',
                      'Run the seven-question refurbisher screen: ISO process, documentation, HIPAA '
                      'removal, decontamination, unedited video, QA results and project management [Block '
                      'Imaging — xvO7-DA6X2w @ 00:00:35].',
                      'Build Latin America prospect lists in HospiScope filtered to private, Brazil and '
                      '100-plus beds, then export to Excel and load into the CRM [Global Health '
                      'Intelligence — FzWeG7sw7qk @ 00:02:05].',
                      'Book air-ride, climate-controlled carriers experienced with medical loads and '
                      'schedule around hospital timed or restricted access [Ntwdequiptrans — LXOka69hkxs @ '
                      '00:01:25].',
                      'Before any US import, lock the FDA classification, an accurate invoice, proof of '
                      'FDA compliance and duties for CBP [ISF Customs Broker — r84DBdhhg1k @ 00:00:57].'],
 'statutory_citations': [{'title': 'Better Biomed Channel — Save Major Dollars with Used Medical Equipment '
                                   '[00:08:04]',
                          'url': 'https://www.youtube.com/watch?v=sgJKIx288kY&t=484s',
                          'relevance': 'Primary practitioner testimony on eBay sourcing, OEM repair '
                                       'arbitrage, ISO-certified middlemen and trade-in credit plays.'},
                         {'title': 'Ntwdequiptrans — Don’t Ship Medical Equipment Like Regular '
                                   'Freight—Here’s Why [00:01:55]',
                          'url': 'https://www.youtube.com/watch?v=LXOka69hkxs&t=115s',
                          'relevance': 'Primary practitioner testimony on medical freight handling, '
                                       'carrier experience and insurance-to-value checks.'},
                         {'title': 'Intertek — Medical Compliance With Clarissa - Episode 16 - NMPA '
                                   'Process & Exporting Medical Devices to China [00:05:36]',
                          'url': 'https://www.youtube.com/watch?v=NTlv6-PNAuI&t=336s',
                          'relevance': 'Primary practitioner testimony on NMPA testing routes, '
                                       'Announcement 126 self-testing and CMA lab scarcity.'},
                         {'title': 'Healthcare Direct USA — Selling Medical Equipment Into Latin America '
                                   '[00:10:03]',
                          'url': 'https://www.youtube.com/watch?v=09hrQ3SQK3E&t=603s',
                          'relevance': 'Primary practitioner testimony on Latin American buyer behavior, '
                                       'equipment tiers and cross-border payment risk.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'U-LBQwafIo8',
                       'title': 'LAB RESALE | New, Used, Refurbished, Medical Equipment for SALE | ARABLAB '
                                '| Expo News Dubai 2020',
                       'channel': 'EXPO NEWS',
                       'author': 'EXPO NEWS',
                       'text': "Refurbished it's more than 50% less than when you buy a new system.",
                       'tip': "Refurbished it's more than 50% less than when you buy a new system.",
                       'timestamp': 98,
                       'timestamp_seconds': 98,
                       'timestamp_label': '[00:01:38]',
                       'url': 'https://www.youtube.com/watch?v=U-LBQwafIo8&t=98s',
                       'markdown': '[00:01:38](https://www.youtube.com/watch?v=U-LBQwafIo8&t=98s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sgJKIx288kY',
                       'title': 'Save Major Dollars with Used Medical Equipment',
                       'channel': 'Better Biomed Channel',
                       'author': 'Better Biomed Channel',
                       'text': 'I found a replacement unit off of eBay for 2,500, a whole unit, the whole '
                               'entire tower, the computer, the camera, the arm, the chassis, everything.',
                       'tip': 'I found a replacement unit off of eBay for 2,500, a whole unit, the whole '
                              'entire tower, the computer, the camera, the arm, the chassis, everything.',
                       'timestamp': 484,
                       'timestamp_seconds': 484,
                       'timestamp_label': '[00:08:04]',
                       'url': 'https://www.youtube.com/watch?v=sgJKIx288kY&t=484s',
                       'markdown': '[00:08:04](https://www.youtube.com/watch?v=sgJKIx288kY&t=484s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sgJKIx288kY',
                       'title': 'Save Major Dollars with Used Medical Equipment',
                       'channel': 'Better Biomed Channel',
                       'author': 'Better Biomed Channel',
                       'text': 'We use those for trade-ins for the rest of the 10 that they were buying '
                               'and we saved ten thousand dollars plus.',
                       'tip': 'We use those for trade-ins for the rest of the 10 that they were buying and '
                              'we saved ten thousand dollars plus.',
                       'timestamp': 938,
                       'timestamp_seconds': 938,
                       'timestamp_label': '[00:15:38]',
                       'url': 'https://www.youtube.com/watch?v=sgJKIx288kY&t=938s',
                       'markdown': '[00:15:38](https://www.youtube.com/watch?v=sgJKIx288kY&t=938s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xzb3hv6fB4g',
                       'title': 'How to Legally Sell Used Medical Equipment | Compliance & Data Security '
                                'Explained!',
                       'channel': 'DES Technologies',
                       'author': 'DES Technologies',
                       'text': 'Incorporating audit reports guarantees that your data erasure efforts are '
                               'verifiable, adding another layer of protection.',
                       'tip': 'Incorporating audit reports guarantees that your data erasure efforts are '
                              'verifiable, adding another layer of protection.',
                       'timestamp': 79,
                       'timestamp_seconds': 79,
                       'timestamp_label': '[00:01:19]',
                       'url': 'https://www.youtube.com/watch?v=xzb3hv6fB4g&t=79s',
                       'markdown': '[00:01:19](https://www.youtube.com/watch?v=xzb3hv6fB4g&t=79s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'K2WVBO_rnnA',
                       'title': 'Selling medical imaging data to AI: HIPAA and DICOM explained',
                       'channel': 'Sell My Data To AI',
                       'author': 'Sell My Data To AI',
                       'text': 'Our first two vetting checks are authority to sign and chain of title, and '
                               'no buyer sees a sample until both are clear.',
                       'tip': 'Our first two vetting checks are authority to sign and chain of title, and '
                              'no buyer sees a sample until both are clear.',
                       'timestamp': 184,
                       'timestamp_seconds': 184,
                       'timestamp_label': '[00:03:04]',
                       'url': 'https://www.youtube.com/watch?v=K2WVBO_rnnA&t=184s',
                       'markdown': '[00:03:04](https://www.youtube.com/watch?v=K2WVBO_rnnA&t=184s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'an4G9gKy9wE',
                       'title': 'National Standards for the Licensure of Wholesale Drug '
                                'Distributors&Third-Party Logistics Providers',
                       'channel': 'U.S. Food and Drug Administration',
                       'author': 'U.S. Food and Drug Administration',
                       'text': 'A key distinction for 3PLs is that if a 3PL is licensed by FDA and ships '
                               "interstate, it's not required to have a license from any state into which "
                               'the 3PL ships.',
                       'tip': 'A key distinction for 3PLs is that if a 3PL is licensed by FDA and ships '
                              "interstate, it's not required to have a license from any state into which "
                              'the 3PL ships.',
                       'timestamp': 723,
                       'timestamp_seconds': 723,
                       'timestamp_label': '[00:12:03]',
                       'url': 'https://www.youtube.com/watch?v=an4G9gKy9wE&t=723s',
                       'markdown': '[00:12:03](https://www.youtube.com/watch?v=an4G9gKy9wE&t=723s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4ICxQIfTktg',
                       'title': 'FDA vs Health Canada: Medical Device Regulations Explained (510k, PMA & '
                                'MDL)',
                       'channel': 'Quality Smart Solutions',
                       'author': 'Quality Smart Solutions',
                       'text': 'So again in Canada ISO 13485 and MDSAP is required before licensing.',
                       'tip': 'So again in Canada ISO 13485 and MDSAP is required before licensing.',
                       'timestamp': 171,
                       'timestamp_seconds': 171,
                       'timestamp_label': '[00:02:51]',
                       'url': 'https://www.youtube.com/watch?v=4ICxQIfTktg&t=171s',
                       'markdown': '[00:02:51](https://www.youtube.com/watch?v=4ICxQIfTktg&t=171s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '09hrQ3SQK3E',
                       'title': 'Selling Medical Equipment Into Latin America',
                       'channel': 'Healthcare Direct USA',
                       'author': 'Healthcare Direct USA',
                       'text': 'You cannot move tier three stuff really down there at all anymore.',
                       'tip': 'You cannot move tier three stuff really down there at all anymore.',
                       'timestamp': 603,
                       'timestamp_seconds': 603,
                       'timestamp_label': '[00:10:03]',
                       'url': 'https://www.youtube.com/watch?v=09hrQ3SQK3E&t=603s',
                       'markdown': '[00:10:03](https://www.youtube.com/watch?v=09hrQ3SQK3E&t=603s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'e1ChWLjN_6Q',
                       'title': 'The Market Outlook for Medical Equipment in Latin America',
                       'channel': 'Global Health Intelligence',
                       'author': 'Global Health Intelligence',
                       'text': 'Panama and Costa Rica stand out, and the play is to target the major '
                               'cities rather than countrywide coverage.',
                       'tip': 'Panama and Costa Rica stand out, and the play is to target the major cities '
                              'rather than countrywide coverage.',
                       'timestamp': 1792,
                       'timestamp_seconds': 1792,
                       'timestamp_label': '[00:29:52]',
                       'url': 'https://www.youtube.com/watch?v=e1ChWLjN_6Q&t=1792s',
                       'markdown': '[00:29:52](https://www.youtube.com/watch?v=e1ChWLjN_6Q&t=1792s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8l8Q1Q45u1s',
                       'title': '2022 Latin America Medical Equipment Market',
                       'channel': 'Global Health Intelligence',
                       'author': 'Global Health Intelligence',
                       'text': 'Brazil and Mexico lead on volume, Colombia and Chile lead on specialized '
                               'equipment, and Chile with about 400 hospitals is easy to test in.',
                       'tip': 'Brazil and Mexico lead on volume, Colombia and Chile lead on specialized '
                              'equipment, and Chile with about 400 hospitals is easy to test in.',
                       'timestamp': 2894,
                       'timestamp_seconds': 2894,
                       'timestamp_label': '[00:48:14]',
                       'url': 'https://www.youtube.com/watch?v=8l8Q1Q45u1s&t=2894s',
                       'markdown': '[00:48:14](https://www.youtube.com/watch?v=8l8Q1Q45u1s&t=2894s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'FzWeG7sw7qk',
                       'title': 'Increasing Sales of Medical Equipment in Latin America',
                       'channel': 'Global Health Intelligence',
                       'author': 'Global Health Intelligence',
                       'text': 'Set the minimum beds to 100 and leave the upper bound open, and the filter '
                               'returns 195 private institutions in Brazil.',
                       'tip': 'Set the minimum beds to 100 and leave the upper bound open, and the filter '
                              'returns 195 private institutions in Brazil.',
                       'timestamp': 106,
                       'timestamp_seconds': 106,
                       'timestamp_label': '[00:01:46]',
                       'url': 'https://www.youtube.com/watch?v=FzWeG7sw7qk&t=106s',
                       'markdown': '[00:01:46](https://www.youtube.com/watch?v=FzWeG7sw7qk&t=106s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LXOka69hkxs',
                       'title': 'Don’t Ship Medical Equipment Like Regular Freight—Here’s Why',
                       'channel': 'Ntwdequiptrans',
                       'author': 'Ntwdequiptrans',
                       'text': "That's why I make sure the carrier's insurance lines up with the freight "
                               'value before the wheels ever start turning.',
                       'tip': "That's why I make sure the carrier's insurance lines up with the freight "
                              'value before the wheels ever start turning.',
                       'timestamp': 115,
                       'timestamp_seconds': 115,
                       'timestamp_label': '[00:01:55]',
                       'url': 'https://www.youtube.com/watch?v=LXOka69hkxs&t=115s',
                       'markdown': '[00:01:55](https://www.youtube.com/watch?v=LXOka69hkxs&t=115s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'll03lU-_2LM',
                       'title': 'Medical Equipment Suppliers Bookkeeping Services | Inventory, Accounting '
                                '& Financial Management',
                       'channel': 'Cloud Accounting World',
                       'author': 'Cloud Accounting World',
                       'text': 'Bookkeeping for medical equipment suppliers also tracks rental income '
                               'along with delivery, installation, warranty and maintenance costs.',
                       'tip': 'Bookkeeping for medical equipment suppliers also tracks rental income along '
                              'with delivery, installation, warranty and maintenance costs.',
                       'timestamp': 125,
                       'timestamp_seconds': 125,
                       'timestamp_label': '[00:02:05]',
                       'url': 'https://www.youtube.com/watch?v=ll03lU-_2LM&t=125s',
                       'markdown': '[00:02:05](https://www.youtube.com/watch?v=ll03lU-_2LM&t=125s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xvO7-DA6X2w',
                       'title': 'Seven Questions to Ask Your Provider for Refurbished Medical Equipment',
                       'channel': 'Block Imaging',
                       'author': 'Block Imaging',
                       'text': 'Making sure that your refurbishment has this step in their process can '
                               "help you avoid being fined for having information you're not supposed to.",
                       'tip': 'Making sure that your refurbishment has this step in their process can help '
                              "you avoid being fined for having information you're not supposed to.",
                       'timestamp': 97,
                       'timestamp_seconds': 97,
                       'timestamp_label': '[00:01:37]',
                       'url': 'https://www.youtube.com/watch?v=xvO7-DA6X2w&t=97s',
                       'markdown': '[00:01:37](https://www.youtube.com/watch?v=xvO7-DA6X2w&t=97s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'r84DBdhhg1k',
                       'title': 'How to Import Medical Equipment to the USA: A Comprehensive Guide',
                       'channel': 'ISF Customs Broker',
                       'author': 'ISF Customs Broker',
                       'text': 'CBP requires an accurate invoice, proof of FDA compliance, and payment of '
                               'duties on imported medical equipment.',
                       'tip': 'CBP requires an accurate invoice, proof of FDA compliance, and payment of '
                              'duties on imported medical equipment.',
                       'timestamp': 57,
                       'timestamp_seconds': 57,
                       'timestamp_label': '[00:00:57]',
                       'url': 'https://www.youtube.com/watch?v=r84DBdhhg1k&t=57s',
                       'markdown': '[00:00:57](https://www.youtube.com/watch?v=r84DBdhhg1k&t=57s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PoaIdM80c3c',
                       'title': 'How to Start a Medical Equipment Business in Dubai (MOHAP Guide)',
                       'channel': 'A&A Associate LLC',
                       'author': 'A&A Associate LLC',
                       'text': 'You can still sell inside the mainland through local distributors or '
                               'registered agents.',
                       'tip': 'You can still sell inside the mainland through local distributors or '
                              'registered agents.',
                       'timestamp': 82,
                       'timestamp_seconds': 82,
                       'timestamp_label': '[00:01:22]',
                       'url': 'https://www.youtube.com/watch?v=PoaIdM80c3c&t=82s',
                       'markdown': '[00:01:22](https://www.youtube.com/watch?v=PoaIdM80c3c&t=82s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NTlv6-PNAuI',
                       'title': 'Medical Compliance With Clarissa - Episode 16 - NMPA Process & Exporting '
                                'Medical Devices to China',
                       'channel': 'Intertek',
                       'author': 'Intertek',
                       'text': 'Under the old process the wait averaged about 6 months just to schedule '
                               'testing and about 18 months to complete it.',
                       'tip': 'Under the old process the wait averaged about 6 months just to schedule '
                              'testing and about 18 months to complete it.',
                       'timestamp': 667,
                       'timestamp_seconds': 667,
                       'timestamp_label': '[00:11:07]',
                       'url': 'https://www.youtube.com/watch?v=NTlv6-PNAuI&t=667s',
                       'markdown': '[00:11:07](https://www.youtube.com/watch?v=NTlv6-PNAuI&t=667s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'}]}
