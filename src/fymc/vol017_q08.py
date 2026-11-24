from __future__ import annotations

CHAPTER_8 = {'id': 'Q8',
 'chapter_id': 'Q8',
 'chapter_number': 8,
 'question_number': 8,
 'slug': 'marketplace-listings-afternic-sedo-atom',
 'question_prompt': "How do you list domains on Afternic, Sedo, and Atom so they sell through GoDaddy's "
                    'distribution network?',
 'kicker': 'Q8 / THE BIG MONEY PLAYBOOKS',
 'title': 'Marketplace Listings: Afternic, Sedo, and Atom',
 'subtitle': 'Step-by-step Afternic listing and payment setup, Fast Transfer and the GoDaddy integration, '
             'Afternic masterclass tips and criticisms, Sedo Buy Now vs Make Offer settings, listing '
             'DropCatch and NameBright purchases, and Atom listing tutorials',
 'layout_template': 'legal_compliance_callout',
 'reading_time_minutes': 15,
 'executive_summary': 'Sellers working Afternic, Sedo, and Atom converge on one playbook: list once on '
                      'Afternic to syndicate across a network of 120-plus reseller partners, put a Buy Now '
                      'price on everything possible, opt into fast transfer, and run a for-sale lander so '
                      "brokers can work inbound leads. Afternic's sales team reports over 60% of "
                      'sub-$10,000 sales close within 48 hours, and says a 1,500-name sample climbs from '
                      'about 2 to 10-13 sales a year once it is priced, fast-transfer enabled, and '
                      'bannered. Sedo says Buy Now listings sell three times more often than make-offer '
                      'listings. Commission math splits the field: Afternic drops from 25% to 15% on its '
                      'nameservers, while Atom charges 7.5% standard. Reza Taheri moved every name to Atom '
                      'after an Afternic transfer sat pending for 12 days.',
 'key_metrics': [{'label': 'Afternic Commission With Afternic Nameservers',
                  'metric': 'Afternic Commission With Afternic Nameservers',
                  'value': '15% instead of the standard 25%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Afternic dashboard warning shown while pricing a newly added domain: '
                             'pointing to Afternic nameservers reduces the commission rate.',
                  'source': 'Web Whizz ([UPcwro2bxDg @ 00:04:02])'},
                 {'label': 'Atom Listing Commission Tiers',
                  'metric': 'Atom Listing Commission Tiers',
                  'value': '7.5% standard vs 15% Plus',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Upgrading an Atom listing from standard to Plus doubles the commission; '
                             'Premium requires Atom approval.',
                  'source': 'ReviewUP ([Tf5gRH1YWFE @ 00:00:31])'},
                 {'label': 'Priced Sub-$10,000 Sales Closing Fast',
                  'metric': 'Priced Sub-$10,000 Sales Closing Fast',
                  'value': 'Over 60% close within 48 hours',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Afternic sales team data on domains priced under $10,000; close percentage '
                             'drops significantly on day three.',
                  'source': 'GoDaddy ([PPJ8y-pwY38 @ 00:07:28])'},
                 {'label': 'Buy Now vs Make Offer Sell-Through',
                  'metric': 'Buy Now vs Make Offer Sell-Through',
                  'value': 'Buy Now listings 3x more likely to sell',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Sedo research comparing Buy Now listings with standard make-offer listings '
                             'on its marketplace.',
                  'source': 'Sedo.com, LLC ([XPj2Qjpi55Y @ 00:00:15])'}],
 'sections': [{'title': 'The Practitioner Consensus',
               'paragraphs': ['Every Afternic-side speaker frames the marketplace as the MLS of domains: '
                              'list a name once and it is distributed across a network of over 120 partner '
                              'resellers, from GoDaddy and Network Solutions to High China, with over 75 '
                              'million domain searches flowing through that network each month '
                              "[PPJ8y-pwY38 @ 00:02:51]. GoDaddy's own walkthrough pitches Afternic as the "
                              "world's biggest domain marketplace, owned and operated by GoDaddy, aimed "
                              'squarely at anyone sitting on unused names they would rather sell than let '
                              'expire and go back on the market for free [9335u-6w_ZQ @ 00:00:19]. The '
                              'integration is tight enough that Ralph of Jazzy Domainz lists a name from '
                              'the three-dot menu inside the GoDaddy dashboard and watches it appear in '
                              'their Afternic account almost instantly, already carrying the Buy It Now '
                              'price and ready for deeper edits [7r4PuUv52Pw @ 00:02:44]. ReviewUP proves '
                              'the reach from the outside in: after listing a NameBright-held domain on '
                              'Afternic and swapping nameservers, a plain GoDaddy search shows the name as '
                              'a premium domain at the exact price set on Afternic [S2dl3wpQtus @ '
                              '00:01:06]. The baseline prerequisite every one of them repeats is the same. '
                              'Get the inventory into the syndication pipe first, because buyers search at '
                              'the registrar they already use, and a name that is not listed never '
                              'surfaces there.',
                              "The second point of agreement is that unpriced inventory stalls. Afternic's "
                              'sales team reports that over 60% of sales on domains priced under $10,000 '
                              'happen within 48 hours, because domains tend to be impulse buys, and close '
                              'percentage drops significantly on day three as buyers find another name '
                              'rather than wait for a quote [PPJ8y-pwY38 @ 00:07:28]. Sedo independently '
                              'says Buy Now listings are three times more likely to sell than standard '
                              'make-offer listings, are required for its MLS premium partner network and '
                              'instant transfers, and create urgency because a hesitating buyer could lose '
                              'out, though a Buy Now set too high without research just puts buyers off '
                              '[XPj2Qjpi55Y @ 00:00:15]. The How-To Learning Academy adds that a clear Buy '
                              'It Now price is what qualifies a name for instant purchase across '
                              "Afternic's network, while a minimum offer and floor tell brokers how to "
                              'handle inquiries, all anchored to extension, length, keywords, and '
                              "comparable sales [r3zrQNCo_eU @ 00:00:39]. Wade Smith, Afternic's director "
                              'of aftermarket sales, puts the line at $2,500: names at or below that fit '
                              "Buy Now as impulse purchases that need no human involvement, and GoDaddy's "
                              'NameFind portfolio runs request-price landers on most names above it '
                              '[memimdQC7MY @ 00:23:10].',
                              'Third, everyone wires up the plumbing that turns a listing into a payout. A '
                              "for-sale lander is treated as non-negotiable: GoDaddy's Emma calls it the "
                              'free equivalent of putting a for-sale sign in front of a house, so anyone '
                              'visiting the domain sees it is on the market [9335u-6w_ZQ @ 00:01:21]. '
                              'Ralph goes further and replaces the default request-price lander with a '
                              'custom Buy It Now plus Make Offer lander, since forcing a visitor to '
                              'contact Afternic for a price is one more step in the way of a sale, and '
                              'notes GoDaddy claims a for-sale lander cuts commission by 40% and doubles '
                              'the chance of selling [7r4PuUv52Pw @ 00:05:04]. Fast transfer is the other '
                              'must-have: Todd of the Afternic sales team describes it as instant '
                              'ownership change across registrars with no pushing and no authorization '
                              'codes, and warns that several large registrars will only list fast-transfer '
                              'names at all [PPJ8y-pwY38 @ 00:11:14]. Payouts close the loop. Emma adds a '
                              'payment method under account details, chooses direct deposit or PayPal, and '
                              'completes a W9 as a United States seller, after which a sold domain '
                              'transfers to the buyer automatically and an unsold one simply stays listed '
                              '[9335u-6w_ZQ @ 00:03:17].'],
               'table': {'caption': 'Where Afternic, Sedo, and Atom sellers agree on the listing baseline',
                         'headers': ['Consensus Point',
                                     'What Practitioners Do',
                                     'Why It Matters To Sellers',
                                     'Expert Source'],
                         'rows': [['List the whole portfolio on Afternic first',
                                   'Use the 50-name form or paste thousands of names into the bulk CSV '
                                   'spreadsheet, priced or not',
                                   'Listings syndicate across 120-plus reseller partners and 75 million '
                                   'monthly domain searches',
                                   'GoDaddy ([PPJ8y-pwY38 @ 00:05:38])'],
                                  ['Put a visible price on every name possible',
                                   'Set a Buy Now price instead of leaving names unpriced for brokers to '
                                   'quote',
                                   'Over 60% of priced sub-$10,000 sales close inside the first 48 hours',
                                   'GoDaddy ([PPJ8y-pwY38 @ 00:07:28])'],
                                  ['Choose Buy Now over open make-offer on Sedo',
                                   'List researched names as Buy Now so they qualify for Sedo MLS and '
                                   'instant transfer',
                                   'Buy Now listings are three times more likely to sell than make-offer '
                                   'listings',
                                   'Sedo.com, LLC ([XPj2Qjpi55Y @ 00:00:15])'],
                                  ['Always switch on the free for-sale landing page',
                                   'Tick the for-sale landing page box before publishing the GoDaddy '
                                   'listing',
                                   'Works like a for-sale sign so every visitor sees the domain is '
                                   'available',
                                   'GoDaddy Help Center ([9335u-6w_ZQ @ 00:01:03])'],
                                  ['Enroll every eligible name in fast transfer',
                                   'Follow the opt-in prompts after publishing and approve the registrar '
                                   'authorization',
                                   'Commission drops to 15% and the domain moves to the buyer the moment '
                                   'payment completes',
                                   'The How-To Learning Academy ([r3zrQNCo_eU @ 00:01:37])'],
                                  ['Verify ownership by pointing nameservers at the marketplace',
                                   'Replace registrar nameservers at NameBright with the two Afternic '
                                   'nameservers provided',
                                   'Afternic auto-verifies ownership and the name shows as premium in '
                                   'GoDaddy search',
                                   'ReviewUP ([S2dl3wpQtus @ 00:00:49])'],
                                  ['Configure payouts before any sale lands',
                                   'Add direct deposit, PayPal, or wire details and file the W9 tax form',
                                   'Sold domains transfer automatically so the money needs a working '
                                   'destination ready',
                                   'GoDaddy Help Center ([9335u-6w_ZQ @ 00:03:17])']]}},
              {'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Afternic runs three price fields, and operators set all of them. Buy Now is '
                              'the price a buyer sees on any site in the network and the one required for '
                              'fast transfer; minimum offer is required for Afternic.com and unpriced '
                              'GoDaddy auction listings; floor price is visible only to the sales team as '
                              "the lowest number they may close at [PPJ8y-pwY38 @ 00:16:30]. Todd's rule "
                              'is to set the floor at the number you are happy selling for and put Buy Now '
                              '25 to 30% higher so brokers have room to negotiate; on a name bought for '
                              '$200 in GoDaddy expired auctions and valued at $1,000, that means floor '
                              '$1,000, Buy Now around $1,500, and minimum offer $500 [PPJ8y-pwY38 @ '
                              '00:17:56]. Ralph shows the auto-close mechanic: on a $200 Buy Now name they '
                              'set both minimum offer and floor at $150, so any offer of $150 or more goes '
                              'through automatically, whereas a $175 floor against a $150 offer kicks the '
                              'deal back to Afternic for negotiation [7r4PuUv52Pw @ 00:03:25]. Ralph also '
                              'prices at wholesale, listing a name GoDaddy appraises at $635 for $200 and '
                              'one appraised at $2,119 for $700 so a reseller can still flip it, while '
                              'retail pricing means doing extra marketing through social media, YouTube, '
                              'email, or phone outreach [7r4PuUv52Pw @ 00:08:51].',
                              'Lease-to-own is the second lever. Ralph notes it only unlocks once Buy Now '
                              'is at least $495 and that GoDaddy says it lifts sale rate by around 35%, so '
                              'they switch it on for every higher-priced name that qualifies [7r4PuUv52Pw '
                              '@ 00:03:45]. Wade recommends LTO on all domains up to the current $100,000 '
                              'threshold, with NameFind testing showing a 24-to-36-month sweet spot where '
                              'buyers have enough skin in the game to keep cancellations down, while a '
                              '60-month term makes walking away too cheap [memimdQC7MY @ 00:25:22]. The '
                              'money tweak is setting terms at 13 or 25 months instead of 12 or 24: the '
                              'extra fee GoDaddy collects is split with the seller and reduces commission, '
                              'many buyers check out at the displayed term, and Andrew Allemann cites a '
                              'large investor who sees about half of buyers stick with 13 [memimdQC7MY @ '
                              '00:26:39]. Fast transfer has hard gates: a participating registrar, no '
                              'expiry within 30 days, no 60-day lock, a passed integrity check, and a Buy '
                              'Now between $50 and $25,000, after which the registrar emails an opt-in '
                              'approval within 24 hours; Afternic says the average customer gains 10 to '
                              '15% in sales, with one GoDaddy-registered portfolio jumping 20% '
                              '[PPJ8y-pwY38 @ 00:13:13].',
                              "Commission math decides where names get pointed. Afternic's own warning "
                              'reads that using its nameservers cuts commission from the standard 25% to '
                              '15% [UPcwro2bxDg @ 00:04:02]. For names held elsewhere, verification is a '
                              'nameserver swap: ReviewUP bought a domain on DropCatch for $13, gave it a '
                              "$490 Buy Now because the name is not very strong, then pasted Afternic's "
                              'two nameservers into NameBright, the registrar DropCatch uses, and '
                              'confirmed the listing showed on GoDaddy at the set prices [m0396LLUymU @ '
                              '00:00:51]. Atom keeps it leaner: paste the domain with the price appended '
                              'after it, choose standard at 7.5% commission or Plus at 15%, request '
                              "Premium only for strong names because it needs Atom's approval, and verify "
                              'by nameservers or a TXT record that cleared in a few minutes for ReviewUP '
                              '[Tf5gRH1YWFE @ 00:00:31]. Sedo pays a reduced commission when a parked Buy '
                              'Now listing sells, and its make-offer format accepts any offer over 20 '
                              'pounds, euros, or dollars; adding a minimum offer and asking price filters '
                              'out low offers you were never interested in, every offer above minimum '
                              'arrives by email, and the seller is not obliged to sell even at the asking '
                              'price [XPj2Qjpi55Y @ 00:02:29]. Each marketplace rewards a seller who '
                              'commits to a visible price.'],
               'table': {'caption': 'Exact pricing levers, thresholds, and commission settings '
                                    'practitioners use',
                         'headers': ['Lever',
                                     'Exact Number Or Setting',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Floor-to-Buy-Now negotiation spread',
                                   'Buy Now set 25 to 30 percent above the floor price',
                                   'Gives Afternic brokers room to negotiate toward Buy Now while closing '
                                   'quickly',
                                   'GoDaddy ([PPJ8y-pwY38 @ 00:17:21])'],
                                  ['Automatic offer acceptance setting',
                                   'Minimum offer and floor both $150 on a $200 Buy Now',
                                   'Any offer at $150 or above closes without a negotiation round',
                                   'Jazzy Domainz ([7r4PuUv52Pw @ 00:03:25])'],
                                  ['Lease-to-own eligibility and claimed lift',
                                   'Buy Now of at least $495 with roughly 35 percent higher sale rate',
                                   'Turn on lease-to-own for every higher-priced name that clears the '
                                   'minimum',
                                   'Jazzy Domainz ([7r4PuUv52Pw @ 00:04:04])'],
                                  ['Lease-to-own term length sweet spot',
                                   '24 to 36 months, listed at 13 or 25 months',
                                   'Keeps buyer skin in the game and shaves commission through the extra '
                                   'month',
                                   'Andrew Allemann ([memimdQC7MY @ 00:25:37])'],
                                  ['Request-price lander versus Buy Now cutoff',
                                   'Buy Now at $2,500 and below; request-price lander shows Buy Now under '
                                   '$2,000',
                                   'Capture the lead and still expose an instant purchase price after the '
                                   'survey',
                                   'Andrew Allemann ([memimdQC7MY @ 00:23:25])'],
                                  ['Fast transfer eligibility price band',
                                   'Buy Now between $50 and $25,000, no 30-day expiry, no 60-day lock',
                                   'Keep prices inside the band so the name reaches fast-transfer-only '
                                   'registrars',
                                   'GoDaddy ([PPJ8y-pwY38 @ 00:13:13])'],
                                  ['Atom listing tier selection',
                                   '7.5 percent standard, 15 percent Plus, Premium by approval',
                                   'Stay on standard unless the name is strong enough to justify the '
                                   'upgrade',
                                   'ReviewUP ([Tf5gRH1YWFE @ 00:00:31])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Squeezing More Net Out Of Every Listing',
                           'body': 'Four field-tested moves sellers use to protect margin, revive stale '
                                   'offers, and reprice on real demand signals.',
                           'items': ['Mark up for the fee: Reza prices names up to 20% higher on Afternic '
                                     'than elsewhere because Afternic takes around 20% commission, versus '
                                     "Atom's 7.5% standard [Reza Taheri — 2jfssBvnbfw @ 00:03:33]",
                                     'Flip stale make-offer names to Buy Now: Sedo automatically emails '
                                     'every previous bidder that the name is no longer under negotiation '
                                     'and can be bought at a fixed price [Sedo.com, LLC — XPj2Qjpi55Y @ '
                                     '00:01:25]',
                                     'Reprice on demand signals, not on a whim: Wade says avoid frequent '
                                     'changes, but when an offer lands, recheck the signals behind the '
                                     "original price, such as whether the keyword's TLD registration count "
                                     'has risen [Andrew Allemann — memimdQC7MY @ 00:22:42]',
                                     'Use a two-month tripwire on new portfolios: if a freshly acquired '
                                     'portfolio gets no inquiries or sales in the first two months, review '
                                     'pricing; seasoned sellers tweaking prices should give it a '
                                     'three-to-four-month window [GoDaddy — PPJ8y-pwY38 @ 00:34:44]']},
               'sop_steps': [{'step': 1,
                              'title': 'Load The Inventory',
                              'action': 'Bulk-upload every name to Afternic with at least a minimum offer.',
                              'detail': 'Download the Afternic spreadsheet, paste in domains with minimum '
                                        'offers, save as CSV, and upload; names usually clear the '
                                        'integrity check and go live within 24 hours [GoDaddy — '
                                        'PPJ8y-pwY38 @ 00:06:22]'},
                             {'step': 2,
                              'title': 'Build The Price Ladder',
                              'action': 'Set floor, Buy Now, and minimum offer for each name.',
                              'detail': 'Floor at the number you are happy with, Buy Now about 50% above '
                                        'it, minimum offer near half the floor, as in the $1,000 floor, '
                                        '$1,500 Buy Now, $500 minimum offer example [GoDaddy — PPJ8y-pwY38 '
                                        '@ 00:17:38]'},
                             {'step': 3,
                              'title': 'Verify And Enroll Fast Transfer',
                              'action': 'Point nameservers to the marketplace and opt eligible names into '
                                        'fast transfer.',
                              'detail': "Swap NameBright nameservers for Afternic's to auto-verify "
                                        '[ReviewUP — S2dl3wpQtus @ 00:00:49], then confirm fast transfer '
                                        'so commission drops to 15% and the name transfers instantly on '
                                        'purchase [The How-To Learning Academy — r3zrQNCo_eU @ 00:01:37]'},
                             {'step': 4,
                              'title': 'Switch On Lander And Payouts',
                              'action': 'Replace the request-price default with a Buy Now plus Make Offer '
                                        'lander and set up payment.',
                              'detail': 'Edit lander settings to a custom Buy It Now plus Make Offer page '
                                        '[Jazzy Domainz — 7r4PuUv52Pw @ 00:05:04], then add direct deposit '
                                        'or PayPal and file the W9 under account details [GoDaddy Help '
                                        'Center — 9335u-6w_ZQ @ 00:03:17]'}]},
              {'id': 'section_3',
               'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Reza Taheri ran an accidental head-to-head on payout friction. Two of his '
                              'names sold on almost the same date, one on Atom and one on Afternic, and '
                              'the Atom transfer closed in two days and two hours while the Afternic side '
                              'dragged for almost two weeks [2jfssBvnbfw @ 00:00:26]. His response was '
                              'blunt. He switched the name servers of his whole portfolio to Atom. On any '
                              'name still listed at Afternic, he prices up to 20% higher to absorb what he '
                              "calls roughly 20% commission, against Atom's 7.5% standard rate, which he "
                              "calls awesome [2jfssBvnbfw @ 00:03:08]. ReviewUP flags the catch on Atom's "
                              'side: upgrading a listing from standard to Plus pushes the commission to '
                              "15% instead of 7.5%, and the Premium tier only opens with Atom's approval "
                              'for strong names [Tf5gRH1YWFE @ 00:00:31]. The GoDaddy aftermarket team '
                              'argues the opposite trade. In their pitch, Afternic behaves like a '
                              'real-estate MLS, syndicating one listing across more than 120 partner '
                              'resellers such as GoDaddy and Network Solutions, with over 75 million '
                              'domain searches a month running through that network [PPJ8y-pwY38 @ '
                              "00:02:51]. The operator read is simple: in Taheri's ledger, Atom wins on "
                              "fee and payout speed, while Afternic's case rests entirely on distribution "
                              'reach inside registrar search results.',
                              "How the price is displayed to buyers is the sharpest split. Sedo's own "
                              'research says Buy Now listings are three times more likely to sell than '
                              "standard Make Offer listings. Buy Now is also required to enter Sedo's MLS "
                              'premium partner network and get instant domain transfers [XPj2Qjpi55Y @ '
                              '00:00:15]. Sedo then carves out the exception. Buy Now is the wrong call if '
                              "you haven't researched the name, because a price that's too high just puts "
                              'buyers off. Make Offer lets you test whether any interest exists at all, '
                              'with offers accepted above 20 pounds, euros or dollars [XPj2Qjpi55Y @ '
                              "00:01:42]. Jazzy Domainz refuses Afternic's default Request Price lander "
                              'outright, calling it one more step in the way of getting a sale. He '
                              'switches names to a custom lander showing Buy It Now plus Make Offer '
                              "[7r4PuUv52Pw @ 00:04:44]. Wade Smith, who runs Afternic's inbound sales "
                              'teams, draws a dollar line instead. Names at $2,500 or below fit BIN as '
                              'impulse purchases that need no human involvement. Namefind runs Request '
                              'Price on most inventory above that line. A newer hybrid shows the BIN price '
                              'at the end of the post-inquiry survey on Request Price landers for names '
                              'under $2,000 [memimdQC7MY @ 00:23:10]. Andrew Allemann admits most of his '
                              'own landers are Request Price, so the Afternic brokers work every inquiry.',
                              'On price level, Jazzy Domainz deliberately sells wholesale. His Sai Young '
                              'Award domain, appraised by GoDaddy at $635, went up at $200. Columbus '
                              'History, appraised at $2,119, sits at $700. That leaves room for another '
                              'investor to flip at $300 to $400, while retail pricing is reserved for '
                              'sellers willing to grind through social media, YouTube, email and phone '
                              "outreach to leads [7r4PuUv52Pw @ 00:06:06]. Afternic's inbound sales "
                              'manager structures the spread differently. Set the floor at the number '
                              "you're happy selling for and put the BIN 25 to 30% higher. Under that rule, "
                              'a $200 expired-auction buy valued at $1,000 becomes a $1,000 floor, a '
                              'roughly $1,500 BIN and a $500 minimum offer [PPJ8y-pwY38 @ 00:17:05]. '
                              'Lease-to-own splits them too. Jazzy can only switch it on at a $495 BIN and '
                              'above. Wade Smith recommends it on everything up to the $100,000 threshold, '
                              'with a 24-to-36-month sweet spot, and suggests setting 13 or 25 months '
                              "instead of 12 or 24 to cut the seller's commission [memimdQC7MY @ "
                              '00:25:07]. For website projects, bytecash has sold a lot more sites on Sedo '
                              'than on Afternic, though his Afternic sales were fairly high priced. He '
                              "also notes that Afternic's $250 minimum on any domain or website rules out "
                              'quick turnkey flips [Hw6wg0dsANM @ 00:08:45].'],
               'table': {'caption': 'Competing marketplace playbooks: who argues which side and on what '
                                    'numbers',
                         'headers': ['Decision Point',
                                     'Playbook A (Who Argues It)',
                                     'Playbook B (Counter-Play)',
                                     'Expert Source'],
                         'rows': [['Which marketplace gets your name servers and inventory',
                                   'Atom at 7.5% standard commission, with one sale transferred in two '
                                   'days and two hours',
                                   'Afternic syndication to 120-plus reseller partners and 75 million '
                                   'monthly searches at 15% to 25%',
                                   'Reza Taheri ([2jfssBvnbfw @ 00:02:24]) vs GoDaddy ([PPJ8y-pwY38 @ '
                                   '00:02:51])'],
                                  ['Fixed Buy Now price versus open Make Offer listing',
                                   'Buy Now is three times more likely to sell and is required for Sedo '
                                   'MLS premium',
                                   "Make Offer when the domain's value hasn't been researched or interest "
                                   'is untested',
                                   'Sedo.com, LLC ([XPj2Qjpi55Y @ 00:00:15]) and Sedo.com, LLC '
                                   '([XPj2Qjpi55Y @ 00:01:42])'],
                                  ['Request Price lander versus a priced Buy It Now lander',
                                   'Kill the Request Price default and run a custom Buy It Now plus Make '
                                   'Offer lander',
                                   'BIN at $2,500 and below; Namefind uses Request Price on most names '
                                   'above that line',
                                   'Jazzy Domainz ([7r4PuUv52Pw @ 00:04:44]) vs Andrew Allemann '
                                   '([memimdQC7MY @ 00:23:10])'],
                                  ['Wholesale pricing versus retail pricing on hand-registered names',
                                   'List far under the GoDaddy appraisal, such as $200 against $635, for '
                                   'faster turnover',
                                   'Hold retail prices but commit to social media, YouTube, email and '
                                   'phone outreach',
                                   'Jazzy Domainz ([7r4PuUv52Pw @ 00:07:33])'],
                                  ['How wide the floor-to-BIN negotiation spread should be',
                                   'Floor at your happy number with BIN 25 to 30% higher so brokers can '
                                   'negotiate',
                                   'Price a little under the suggested GoDaddy value, hoping the name '
                                   'sells faster',
                                   'GoDaddy ([PPJ8y-pwY38 @ 00:17:05]) vs GoDaddy Help Center '
                                   '([9335u-6w_ZQ @ 00:01:03])'],
                                  ['Where to list developed website projects rather than bare domains',
                                   'Sedo project sale template seeded early, since buyers need 30 days of '
                                   'traffic stats',
                                   'Afternic website content button with a $250 minimum; fewer but '
                                   'higher-priced sales',
                                   'bytecash ([Hw6wg0dsANM @ 00:02:51]) and bytecash ([Hw6wg0dsANM @ '
                                   '00:08:45])'],
                                  ['Lease-to-own term length and which names qualify for it',
                                   'LTO on all names up to $100,000 with a 24-to-36-month term sweet spot',
                                   'Higher-priced sellers prefer shorter terms so the buyer invests more '
                                   'up front',
                                   'Andrew Allemann ([memimdQC7MY @ 00:25:07])']]}},
              {'id': 'section_4',
               'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["The costliest trap is money stuck after the sale. Reza Taheri's Afternic "
                              'payment landed on 23 March 2025, yet on 2 April the dashboard still read '
                              'transfer pending. By then the domain had already left his own registrar '
                              "account and was sitting at the buyer's registrar [2jfssBvnbfw @ 00:01:12]. "
                              'Customer service kept answering that it can take five to seven business '
                              'days; he counted at least ten [2jfssBvnbfw @ 00:02:00]. Andrew Allemann hit '
                              'the broker-side version. A buyer agreed a price on a '
                              "two-to-three-thousand-dollar name, the purchase link didn't go out for "
                              'three days, and the buyer never paid. On another lead, a rep engaged and '
                              'then set the next follow-up 12 or 14 days out [memimdQC7MY @ 00:19:18]. '
                              "Wade Smith's defense is that the gap covers checking the buyer's funding "
                              "and authority to purchase, and that once engagement happens there's no "
                              "fixed cadence. GoDaddy's own numbers show why delay hurts. Over 60% of "
                              'sales on names priced under $10,000 close within 48 hours, and the close '
                              'percentage drops significantly on day three as buyers find another name '
                              '[PPJ8y-pwY38 @ 00:08:37]. Speed of fulfilment, not list price, is the '
                              'economics that decides whether a hot lead actually turns into cash in your '
                              'account.',
                              'Leaving names unpriced is the second firsthand loss. One Afternic seller '
                              'with three or four years on the platform refused to price, afraid a $5,000 '
                              "BIN would forfeit an $8,000 deal. After pricing, the seller's sales "
                              'velocity rose enough to quadruple revenue [PPJ8y-pwY38 @ 00:09:23]. '
                              "GoDaddy's sample 1,500-name portfolio sells about two names a year unpriced "
                              'and five to six once priced. That rises to six to eight with fast transfer, '
                              'and to ten to thirteen once the for-sale banner and sales team are added. '
                              'The opposite error is overpricing on gut: Sedo warns that a Buy Now price '
                              "that's too high just puts off potential buyers [XPj2Qjpi55Y @ 00:01:42]. "
                              'Appraisal anchoring cuts both ways. Allemann hears sellers complain that Go '
                              'Value tells buyers a six-figure name is worth $20,000, while investors '
                              "anchor on the above-25,000 readout. Wade Smith concedes the tool hasn't "
                              'been updated in a while and does a poor job on ultra-premium names, while '
                              'holding up in the $2,000-to-$5,000 average range and even at $10,000 to '
                              '$15,000 [memimdQC7MY @ 00:29:17]. When a seller with zero sales asked why, '
                              'the Afternic team found minimal inquiries and traffic. They routed him to a '
                              'GoDaddy Premier service rep to rework how he acquires names, because the '
                              'portfolio was the problem [PPJ8y-pwY38 @ 00:35:56].',
                              'Operational traps are mostly self-inflicted. GoDaddy says fast transfer '
                              'lifts sales 10 to 15% on average, but the program silently excludes three '
                              'groups: names expiring within 30 days, names under a 60-day lock, and '
                              'anything without a BIN between $50 and $25,000. The seller still has to '
                              'approve the opt-in notice their registrar sends within 24 hours '
                              "[PPJ8y-pwY38 @ 00:12:51]. bytecash warns that pointing a live website's "
                              "name servers at Sedo or Afternic parking means the site won't work anymore, "
                              'and he calls their domain parking terrible [Hw6wg0dsANM @ 00:09:26]. He '
                              'also had to shut down a 2,000-member forum after spammers overran it while '
                              'it went unchecked. Sedo kicks off projects without traffic, and nobody buys '
                              'a site there until they see stats. He flags autosurf and traffic-exchange '
                              'stat inflation as worthless traffic that will eventually get a seller sued '
                              'if it is claimed as organic. He works around the short, no-HTML, no-picture '
                              'descriptions on Sedo and Afternic by uploading screenshots and an appraisal '
                              'to his own server [Hw6wg0dsANM @ 00:13:36]. On lease-to-own, Wade Smith '
                              "warns that on a 60-month term the buyer's initial investment is small and "
                              'walking away is easy, so cancellations climb [memimdQC7MY @ 00:25:07].'],
               'table': {'caption': 'Firsthand failures on Afternic, Sedo and Atom with the economics '
                                    'check each one forces',
                         'headers': ['Failure Mode',
                                     'What Went Wrong Firsthand',
                                     'Economics Check / Countermove',
                                     'Expert Source'],
                         'rows': [['Afternic payout stuck in transfer pending after the sale',
                                   'Payment received 23 March 2025, still pending 2 April after the domain '
                                   'had moved',
                                   'Moved all portfolio name servers to Atom and priced remaining Afternic '
                                   'listings 20% higher',
                                   'Reza Taheri ([2jfssBvnbfw @ 00:01:12])'],
                                  ['Broker lag after the buyer agrees on a price',
                                   'Checkout link went out three days late on a $2,000 to $3,000 name and '
                                   'the buyer never paid',
                                   'Over 60% of sub-$10,000 sales close within 48 hours, so delays kill '
                                   'deals',
                                   'Andrew Allemann ([memimdQC7MY @ 00:19:18])'],
                                  ['Holding inventory unpriced out of fear of underselling',
                                   'Seller feared losing an $8,000 deal by setting a $5,000 Buy Now price',
                                   "Pricing raised sales velocity enough to quadruple the seller's total "
                                   'revenue',
                                   'GoDaddy ([PPJ8y-pwY38 @ 00:09:23])'],
                                  ['Go Value appraisal anchoring buyers and sellers alike',
                                   'Six-figure names shown near $20,000 and investors anchoring on the '
                                   'above-25,000 readout',
                                   'Use it to rank-stack expired inventory; it holds up in the $2,000 to '
                                   '$15,000 range',
                                   'Andrew Allemann ([memimdQC7MY @ 00:28:43])'],
                                  ['Names silently excluded from the fast transfer network',
                                   'Expiring within 30 days, under a 60-day lock, or BIN outside $50 to '
                                   '$25,000',
                                   'Renew early, price inside the band, and approve the registrar opt-in '
                                   'within 24 hours',
                                   'GoDaddy ([PPJ8y-pwY38 @ 00:13:13])'],
                                  ["Pointing a live website's name servers at marketplace parking",
                                   'The website stops working once name servers change, and the parking '
                                   'pays poorly',
                                   'Keep the site on its own hosting and paste the Sedo tracker code in '
                                   'the footer',
                                   'bytecash ([Hw6wg0dsANM @ 00:09:26])'],
                                  ['Lease-to-own terms stretched out to 60 months',
                                   'A small initial buyer investment makes walking away easy and '
                                   'cancellations climb',
                                   'Set 24 to 36 months, and use shorter terms on higher-value assets',
                                   'Andrew Allemann ([memimdQC7MY @ 00:25:22])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Listing Checks Before Any Name Goes Live',
                           'body': 'Each check below comes from a loss or bottleneck a practitioner hit '
                                   'firsthand. Clear all four before a name is exposed to buyers or a sale '
                                   'is routed through a marketplace.',
                           'items': ["Never repoint a live website's name servers to Afternic or Sedo "
                                     'parking just to list it, because bytecash reports the site stops '
                                     'working and the parking is terrible [bytecash — Hw6wg0dsANM @ '
                                     '00:09:26].',
                                     'Budget cash flow for Afternic transfer-pending delays: Reza Taheri '
                                     'waited 12 days against a quoted five to seven business days while '
                                     'the buyer already held the domain [Reza Taheri — 2jfssBvnbfw @ '
                                     '00:02:00].',
                                     'Confirm fast-transfer eligibility before relying on the 10 to 15% '
                                     'lift: no expiry within 30 days, no 60-day lock, and a BIN between '
                                     '$50 and $25,000 [GoDaddy — PPJ8y-pwY38 @ 00:12:51].',
                                     'Research value before setting a Buy Now price, because Sedo warns a '
                                     "Buy Now price that's too high just puts off potential buyers "
                                     '[Sedo.com, LLC — XPj2Qjpi55Y @ 00:01:42].']}}],
 'pull_quote': '"I put a higher price, up to 20% higher, in Afternic because it will take around 20% '
               'commission... in Atom the standard commission is 7.5%, which is awesome." — Reza Taheri '
               '(2jfssBvnbfw @ 00:03:08).',
 'diagram_id': 'diag-04',
 'action_checklist': ["Bulk-list the whole portfolio through Afternic's downloadable Excel sheet: paste "
                      'the domains, fill in minimum offers, save as CSV and upload, and expect names to '
                      'clear the integrity check within 24 hours [GoDaddy — PPJ8y-pwY38 @ 00:05:22].',
                      "Set the floor at the number you're happy selling for, put the Buy Now price 25 to "
                      '30% higher, and set the minimum offer near half the floor, as in the $1,000 floor, '
                      '$1,500 BIN and $500 minimum offer example [GoDaddy — PPJ8y-pwY38 @ 00:17:21].',
                      "Switch Afternic's default Request Price lander to a custom Buy It Now plus Make "
                      'Offer lander so visitors see a price without contacting the sales team [Jazzy '
                      'Domainz — 7r4PuUv52Pw @ 00:05:04].',
                      "For names held at NameBright, copy Afternic's two name servers into the registrar's "
                      'DNS settings, then search the name on GoDaddy to confirm it shows as premium at '
                      'your price [ReviewUP — S2dl3wpQtus @ 00:00:49].',
                      'On Atom, keep the standard 7.5% listing unless the name justifies Plus at 15%, and '
                      'verify ownership with Atom name servers or a TXT record holding the verification ID '
                      '[ReviewUP — Tf5gRH1YWFE @ 00:00:50].',
                      'Set the Afternic payout method (direct deposit, PayPal or another option) and '
                      'complete the W-9 form before a sale lands, so a sold name settles without delay '
                      '[GoDaddy Help Center — 9335u-6w_ZQ @ 00:02:36].'],
 'statutory_citations': [{'title': 'Reza Taheri — Afternic Review: Why It’s Killing Your Domain Sales '
                                   '[00:00:26]',
                          'url': 'https://www.youtube.com/watch?v=2jfssBvnbfw&t=26s',
                          'relevance': 'Primary practitioner testimony on Atom versus Afternic transfer '
                                       'speed, payout delays and the 7.5% versus 20% commission gap.'},
                         {'title': 'Andrew Allemann — Selling domains through Afternic - DNW Podcast #561 '
                                   '[00:21:59]',
                          'url': 'https://www.youtube.com/watch?v=memimdQC7MY&t=1319s',
                          'relevance': 'Primary practitioner testimony on Afternic broker follow-up, '
                                       'lander selection thresholds, lease-to-own terms and Go Value '
                                       'anchoring.'},
                         {'title': 'GoDaddy — On The Dot! | Domain Aftermarket | Episode 1 - Afternic '
                                   'Integration with GoDaddy | GoDaddy Hangout [00:07:11]',
                          'url': 'https://www.youtube.com/watch?v=PPJ8y-pwY38&t=431s',
                          'relevance': 'Primary practitioner testimony on pricing velocity, fast transfer '
                                       'eligibility and floor-to-BIN spread mechanics.'},
                         {'title': 'Sedo.com, LLC — What Sales Settings to Choose When Selling Domains - '
                                   'Buy Now VS Make Offer [00:00:15]',
                          'url': 'https://www.youtube.com/watch?v=XPj2Qjpi55Y&t=15s',
                          'relevance': 'Primary practitioner testimony on Sedo Buy Now versus Make Offer '
                                       'conversion and MLS premium eligibility.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '7r4PuUv52Pw',
                       'title': 'How I List Domains for Sale on Afternic (Step-by-Step Example)',
                       'channel': 'Jazzy Domainz',
                       'author': 'Jazzy Domainz',
                       'text': 'Right now the default is request price, so somebody who comes to your page '
                               'has to contact GoDaddy Afternic to get the price, and this is just one '
                               'more step in the way of getting a sale, so I like to use a custom lander.',
                       'tip': 'Right now the default is request price, so somebody who comes to your page '
                              'has to contact GoDaddy Afternic to get the price, and this is just one more '
                              'step in the way of getting a sale, so I like to use a custom lander.',
                       'timestamp': 284,
                       'timestamp_seconds': 284,
                       'timestamp_label': '[00:04:44]',
                       'url': 'https://www.youtube.com/watch?v=7r4PuUv52Pw&t=284s',
                       'markdown': '[00:04:44](https://www.youtube.com/watch?v=7r4PuUv52Pw&t=284s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9335u-6w_ZQ',
                       'title': 'How to Sell Your Godaddy Domain Step-By-Step on Afternic',
                       'channel': 'GoDaddy Help Center',
                       'author': 'GoDaddy Help Center',
                       'text': "Set your buy now price; I'm gonna price mine a little under the suggested "
                               'price hoping it will sell faster.',
                       'tip': "Set your buy now price; I'm gonna price mine a little under the suggested "
                              'price hoping it will sell faster.',
                       'timestamp': 63,
                       'timestamp_seconds': 63,
                       'timestamp_label': '[00:01:03]',
                       'url': 'https://www.youtube.com/watch?v=9335u-6w_ZQ&t=63s',
                       'markdown': '[00:01:03](https://www.youtube.com/watch?v=9335u-6w_ZQ&t=63s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'r3zrQNCo_eU',
                       'title': 'How to Sell Your GoDaddy Domain on Afternic [2026 Guide]',
                       'channel': 'The How-To Learning Academy',
                       'author': 'The How-To Learning Academy',
                       'text': 'When eligible and enrolled, fast transfer reduces commissions to 15% and '
                               'enables an automatic transfer to the buyer the moment a purchase is '
                               'completed.',
                       'tip': 'When eligible and enrolled, fast transfer reduces commissions to 15% and '
                              'enables an automatic transfer to the buyer the moment a purchase is '
                              'completed.',
                       'timestamp': 97,
                       'timestamp_seconds': 97,
                       'timestamp_label': '[00:01:37]',
                       'url': 'https://www.youtube.com/watch?v=r3zrQNCo_eU&t=97s',
                       'markdown': '[00:01:37](https://www.youtube.com/watch?v=r3zrQNCo_eU&t=97s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '53UqsOGx89Q',
                       'title': '💸 How to Sell Your GoDaddy Domain Step-by-Step on Afternic (2025 Complete '
                                'Guide)',
                       'channel': 'Tutorials With Alen',
                       'author': 'Tutorials With Alen',
                       'text': "If you're looking for a quick sale, you might want to price competitively, "
                               "and use Afternic's pricing tools or consult other domains in your niche to "
                               'see what similar domains are going for.',
                       'tip': "If you're looking for a quick sale, you might want to price competitively, "
                              "and use Afternic's pricing tools or consult other domains in your niche to "
                              'see what similar domains are going for.',
                       'timestamp': 70,
                       'timestamp_seconds': 70,
                       'timestamp_label': '[00:01:10]',
                       'url': 'https://www.youtube.com/watch?v=53UqsOGx89Q&t=70s',
                       'markdown': '[00:01:10](https://www.youtube.com/watch?v=53UqsOGx89Q&t=70s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2jfssBvnbfw',
                       'title': 'Afternic Review: Why It’s Killing Your Domain Sales',
                       'channel': 'Reza Taheri',
                       'author': 'Reza Taheri',
                       'text': 'On Atom the process of transfer took about two days and two hours, but on '
                               'the other hand for Afternic it took almost two weeks.',
                       'tip': 'On Atom the process of transfer took about two days and two hours, but on '
                              'the other hand for Afternic it took almost two weeks.',
                       'timestamp': 26,
                       'timestamp_seconds': 26,
                       'timestamp_label': '[00:00:26]',
                       'url': 'https://www.youtube.com/watch?v=2jfssBvnbfw&t=26s',
                       'markdown': '[00:00:26](https://www.youtube.com/watch?v=2jfssBvnbfw&t=26s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2jfssBvnbfw',
                       'title': 'Afternic Review: Why It’s Killing Your Domain Sales',
                       'channel': 'Reza Taheri',
                       'author': 'Reza Taheri',
                       'text': 'I put a higher price, up to 20% higher, in Afternic because it will take '
                               'around 20% commission, and in Atom the standard commission is 7.5%, which '
                               'is awesome.',
                       'tip': 'I put a higher price, up to 20% higher, in Afternic because it will take '
                              'around 20% commission, and in Atom the standard commission is 7.5%, which '
                              'is awesome.',
                       'timestamp': 213,
                       'timestamp_seconds': 213,
                       'timestamp_label': '[00:03:33]',
                       'url': 'https://www.youtube.com/watch?v=2jfssBvnbfw&t=213s',
                       'markdown': '[00:03:33](https://www.youtube.com/watch?v=2jfssBvnbfw&t=213s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Hw6wg0dsANM',
                       'title': 'Selling Websites on SEDO and AFTERNIC',
                       'channel': 'bytecash',
                       'author': 'bytecash',
                       'text': 'On Afternic you have a minimum price of 250 for any domain name or '
                               "website, so this isn't going to be the best place to sell quick turnkey "
                               'solutions.',
                       'tip': 'On Afternic you have a minimum price of 250 for any domain name or website, '
                              "so this isn't going to be the best place to sell quick turnkey solutions.",
                       'timestamp': 525,
                       'timestamp_seconds': 525,
                       'timestamp_label': '[00:08:45]',
                       'url': 'https://www.youtube.com/watch?v=Hw6wg0dsANM&t=525s',
                       'markdown': '[00:08:45](https://www.youtube.com/watch?v=Hw6wg0dsANM&t=525s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'I1_LrdnHVvo',
                       'title': 'Unlock More Domain Sales Today: Secrets from the Afternic Masterclass',
                       'channel': 'GoDaddy Domain Academy',
                       'author': 'GoDaddy Domain Academy',
                       'text': 'You may want to learn how you would set up a for sale lander or the best '
                               'thing to do with lease to own, and we have AI powered pricing insights.',
                       'tip': 'You may want to learn how you would set up a for sale lander or the best '
                              'thing to do with lease to own, and we have AI powered pricing insights.',
                       'timestamp': 99,
                       'timestamp_seconds': 99,
                       'timestamp_label': '[00:01:39]',
                       'url': 'https://www.youtube.com/watch?v=I1_LrdnHVvo&t=99s',
                       'markdown': '[00:01:39](https://www.youtube.com/watch?v=I1_LrdnHVvo&t=99s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'memimdQC7MY',
                       'title': 'Selling domains through Afternic - DNW Podcast #561',
                       'channel': 'Andrew Allemann',
                       'author': 'Andrew Allemann',
                       'text': "Anybody that has something that's 2500 or below is really a good fit for "
                               "bin; those could be impulse purchases, and you don't typically need human "
                               'involvement to make that sale happen.',
                       'tip': "Anybody that has something that's 2500 or below is really a good fit for "
                              "bin; those could be impulse purchases, and you don't typically need human "
                              'involvement to make that sale happen.',
                       'timestamp': 1390,
                       'timestamp_seconds': 1390,
                       'timestamp_label': '[00:23:10]',
                       'url': 'https://www.youtube.com/watch?v=memimdQC7MY&t=1390s',
                       'markdown': '[00:23:10](https://www.youtube.com/watch?v=memimdQC7MY&t=1390s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'memimdQC7MY',
                       'title': 'Selling domains through Afternic - DNW Podcast #561',
                       'channel': 'Andrew Allemann',
                       'author': 'Andrew Allemann',
                       'text': "We've found with Namefind that the sweet spot is probably between 24 "
                               'months and 36 months, where you have enough investment from a buyer that '
                               "they've got skin in the game.",
                       'tip': "We've found with Namefind that the sweet spot is probably between 24 months "
                              "and 36 months, where you have enough investment from a buyer that they've "
                              'got skin in the game.',
                       'timestamp': 1522,
                       'timestamp_seconds': 1522,
                       'timestamp_label': '[00:25:22]',
                       'url': 'https://www.youtube.com/watch?v=memimdQC7MY&t=1522s',
                       'markdown': '[00:25:22](https://www.youtube.com/watch?v=memimdQC7MY&t=1522s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PPJ8y-pwY38',
                       'title': 'On The Dot! | Domain Aftermarket | Episode 1 - Afternic Integration with '
                                'GoDaddy | GoDaddy Hangout',
                       'channel': 'GoDaddy',
                       'author': 'GoDaddy',
                       'text': 'The majority of our sales, over 60% of them on domains that are priced '
                               'under $10,000, are going to happen within 48 hours.',
                       'tip': 'The majority of our sales, over 60% of them on domains that are priced '
                              'under $10,000, are going to happen within 48 hours.',
                       'timestamp': 431,
                       'timestamp_seconds': 431,
                       'timestamp_label': '[00:07:11]',
                       'url': 'https://www.youtube.com/watch?v=PPJ8y-pwY38&t=431s',
                       'markdown': '[00:07:11](https://www.youtube.com/watch?v=PPJ8y-pwY38&t=431s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UPcwro2bxDg',
                       'title': 'How to Sell Domain on Afternic | Afternic Payment Setup Tutorial (2026)',
                       'channel': 'Web Whizz',
                       'author': 'Web Whizz',
                       'text': 'When you use Afternic name servers, the commission rate will be reduced '
                               'from the standard rate of 25% to 15%.',
                       'tip': 'When you use Afternic name servers, the commission rate will be reduced '
                              'from the standard rate of 25% to 15%.',
                       'timestamp': 225,
                       'timestamp_seconds': 225,
                       'timestamp_label': '[00:03:45]',
                       'url': 'https://www.youtube.com/watch?v=UPcwro2bxDg&t=225s',
                       'markdown': '[00:03:45](https://www.youtube.com/watch?v=UPcwro2bxDg&t=225s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XPj2Qjpi55Y',
                       'title': 'What Sales Settings to Choose When Selling Domains - Buy Now VS Make '
                                'Offer',
                       'channel': 'Sedo.com, LLC',
                       'author': 'Sedo.com, LLC',
                       'text': 'Sedo recommends that you list your domains as buy now, as our research '
                               'shows that domains listed as buy now are three times more likely to sell '
                               'than those listed as a standard make offer listing.',
                       'tip': 'Sedo recommends that you list your domains as buy now, as our research '
                              'shows that domains listed as buy now are three times more likely to sell '
                              'than those listed as a standard make offer listing.',
                       'timestamp': 15,
                       'timestamp_seconds': 15,
                       'timestamp_label': '[00:00:15]',
                       'url': 'https://www.youtube.com/watch?v=XPj2Qjpi55Y&t=15s',
                       'markdown': '[00:00:15](https://www.youtube.com/watch?v=XPj2Qjpi55Y&t=15s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'S2dl3wpQtus',
                       'title': 'How to Sell a Domain Name On GoDaddy in 2026  Goddady & Afternic Domain '
                                'Flipping Tutorial',
                       'channel': 'ReviewUP',
                       'author': 'ReviewUP',
                       'text': 'Set the floor price, which is the minimum price Afternic brokers can '
                               'negotiate and sell the domain for.',
                       'tip': 'Set the floor price, which is the minimum price Afternic brokers can '
                              'negotiate and sell the domain for.',
                       'timestamp': 17,
                       'timestamp_seconds': 17,
                       'timestamp_label': '[00:00:17]',
                       'url': 'https://www.youtube.com/watch?v=S2dl3wpQtus&t=17s',
                       'markdown': '[00:00:17](https://www.youtube.com/watch?v=S2dl3wpQtus&t=17s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'm0396LLUymU',
                       'title': 'How to Sell Any Domain Name on GoDaddy in 2026 (Using DropCatch & '
                                'NameBright with Afternic Tutorial)',
                       'channel': 'ReviewUP',
                       'author': 'ReviewUP',
                       'text': "Since this domain isn't very strong, I'm going to set bin price $490.",
                       'tip': "Since this domain isn't very strong, I'm going to set bin price $490.",
                       'timestamp': 51,
                       'timestamp_seconds': 51,
                       'timestamp_label': '[00:00:51]',
                       'url': 'https://www.youtube.com/watch?v=m0396LLUymU&t=51s',
                       'markdown': '[00:00:51](https://www.youtube.com/watch?v=m0396LLUymU&t=51s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mj3WifuqDM8',
                       'title': 'How to Sell Domain on Afternic | Afternic Payment Setup Tutorial (2025)',
                       'channel': 'Twoguysfinance',
                       'author': 'Twoguysfinance',
                       'text': "Gain wider exposure for your domain names by opting into Afternic's fast "
                               'transfer network.',
                       'tip': "Gain wider exposure for your domain names by opting into Afternic's fast "
                              'transfer network.',
                       'timestamp': 72,
                       'timestamp_seconds': 72,
                       'timestamp_label': '[00:01:12]',
                       'url': 'https://www.youtube.com/watch?v=mj3WifuqDM8&t=72s',
                       'markdown': '[00:01:12](https://www.youtube.com/watch?v=mj3WifuqDM8&t=72s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Tf5gRH1YWFE',
                       'title': 'How to List a Domain for Sale on Atom (Atom Domain Flipping Step-by-Step '
                                'Tutorial )',
                       'channel': 'ReviewUP',
                       'author': 'ReviewUP',
                       'text': 'You can choose to keep the listing standard or upgrade it to plus, but '
                               'keep in mind the commission increases to 15% instead of 7.5%.',
                       'tip': 'You can choose to keep the listing standard or upgrade it to plus, but keep '
                              'in mind the commission increases to 15% instead of 7.5%.',
                       'timestamp': 31,
                       'timestamp_seconds': 31,
                       'timestamp_label': '[00:00:31]',
                       'url': 'https://www.youtube.com/watch?v=Tf5gRH1YWFE&t=31s',
                       'markdown': '[00:00:31](https://www.youtube.com/watch?v=Tf5gRH1YWFE&t=31s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YRldRVYasrU',
                       'title': 'How to Sell Domain on atom (atom.com) - Full Tutorial',
                       'channel': 'CyberTech',
                       'author': 'CyberTech',
                       'text': 'Choose your registration here, and from this option add your API token and '
                               'import your domains.',
                       'tip': 'Choose your registration here, and from this option add your API token and '
                              'import your domains.',
                       'timestamp': 38,
                       'timestamp_seconds': 38,
                       'timestamp_label': '[00:00:38]',
                       'url': 'https://www.youtube.com/watch?v=YRldRVYasrU&t=38s',
                       'markdown': '[00:00:38](https://www.youtube.com/watch?v=YRldRVYasrU&t=38s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'}]}
