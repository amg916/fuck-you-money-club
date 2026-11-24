from __future__ import annotations

CHAPTER_5 = {'id': 'Q5',
 'chapter_id': 'Q5',
 'chapter_number': 5,
 'question_number': 5,
 'slug': 'ping-post-lead-and-call-distribution',
 'question_prompt': 'How does ping-post work for leads and calls, and how do I configure it in lead '
                    'distribution software?',
 'kicker': 'Q5 / THE BIG MONEY PLAYBOOKS',
 'title': 'Ping-Post Lead and Call Distribution',
 'subtitle': 'Ping-post definitions, partial-data pings and buyer bids, ping-post for calls, boberdoo '
             'demos and webinars, ping-post lead type specs, buyer API setup via Lead Prosper, and selling '
             'calls through boberdoo',
 'layout_template': 'case_study',
 'reading_time_minutes': 15,
 'executive_summary': "boberdoo's Scott Hoffman, Brett and the Lead Prosper team describe ping post as an "
                      'exclusionary auction: a non-contact ping is fired simultaneously to every buyer '
                      'with an active account, funds and a matching filter set, the best bid minus your '
                      'margin goes back to the seller, and the PII post only lands after the buyer returns '
                      'success. Street numbers recur: $10 bid minus $2 margin returns $8; variable margin '
                      'tiers of 10-50%; 15s/30s or 20s/60s ping/post timeouts; a 15% refund cap over 30 '
                      "days; call minutes at 10 cents down to 6 cents. Operators split on 'yes' versus "
                      "'yes but sold non-exclusively' fallback and on exclusive versus shared scenarios, "
                      'and the call desk warns that a $50 duration-gated buyer can lose on earnings per '
                      'call to a $30 no-duration buyer.',
 'key_metrics': [{'label': 'Static Ping Post Margin Math',
                  'metric': 'Static Ping Post Margin Math',
                  'value': '$10 bid - $2 margin = $8 offer returned to the seller',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Fixed-dollar margin carved off a static buyer bid before the price offer is '
                             'passed back to the lead seller; a $3 margin drops the bid to $7.',
                  'source': 'boberdoo.com ([yCAVYNpSdZI @ 00:28:04])'},
                 {'label': 'Typical Ping/Post Timeout Windows',
                  'metric': 'Typical Ping/Post Timeout Windows',
                  'value': '15 seconds on the ping, 30 seconds on the post',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Typical windows quoted for ping post sources; lagging buyers are excluded so '
                             'the seller always gets a bid back.',
                  'source': 'boberdoo.com ([yCAVYNpSdZI @ 00:15:39])'},
                 {'label': 'Buyer Refund Cap',
                  'metric': 'Buyer Refund Cap',
                  'value': '15% of leads over a 30-day window',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Refund limit set on buyer accounts to stop a buyer from refunding 90 of 100 '
                             'leads.',
                  'source': 'boberdoo.com ([yCAVYNpSdZI @ 00:22:50])'},
                 {'label': 'Call Routing Minute Pricing',
                  'metric': 'Call Routing Minute Pricing',
                  'value': '10 cents down to 6 cents per minute, both legs; first block 30,000 minutes, '
                           'blocks never expire',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Per-minute pricing for routed calls covering both legs of the call, sold in '
                             'non-expiring minute blocks.',
                  'source': 'boberdoo.com ([I3MdV-IDLRk @ 00:49:12])'}],
 'sections': [{'title': 'Section 1: The Practitioner Consensus - Exclusionary Auctions, Success-Gated '
                        'Responses and One Rulebook for Leads and Calls',
               'paragraphs': ['Every boberdoo trainer frames ping post the same way: a lead seller fires '
                              'partial, non-contact data at buyers so they can bid before ever seeing a '
                              'name or phone number [vNu0tV99Lnw @ 00:00:00]. The basics walkthrough '
                              'reduces it to three moves - ping the lead without personal information to '
                              'all eligible buyers at the same time, compare the bids, and post to the '
                              "winner or winners 'in a matter of seconds' - running fully automated across "
                              "'thousands of pings a day' [o5v8ME_4M_M @ 00:00:38]. The engine is pitched "
                              'as handling both inbound and outbound ping post. The trainers hammer that '
                              "the fire is simultaneous, not a waterfall: 'we fire that out to the same "
                              "time to every possible matching buyer' [lpWTQpnduYo @ 00:38:29]. The "
                              'selection logic is exclusionary rather than additive. The system first '
                              'strips out inactive accounts, accounts without funds, and accounts without '
                              'a matching filter set, and only then sorts whoever survives by best revenue '
                              '[BvWILZyxIIA @ 00:00:46]. That ordering is the whole consensus in one '
                              'sentence: a buyer who has not funded, has no live filter set, or is '
                              'switched off simply does not exist to the auction. Everything else in the '
                              'stack is built on that filter.',
                              'The second point of agreement is that nothing goes back to the seller until '
                              'the buyer has actually taken the lead. boberdoo only returns a response to '
                              "a lead seller 'once we receive the success response from the buyer' "
                              "[BvWILZyxIIA @ 00:01:22]. The 'What Is Ping Post?' explainer spells out "
                              "why: processing is sequential, the system 'waits for that success response "
                              "before returning the Matched response to your vendor,' and any break in "
                              'that chain produces post rejects [vNu0tV99Lnw @ 00:05:06]. The ping carries '
                              'the bid-relevant fields - incident dates for legal, income for health, ZIP '
                              'and age - while name, address, phone and email ride the post. The trainers '
                              'treat post rejects as the enemy, not a cost of doing business. Their line '
                              "is blunt: 'you never want to have post rejects,' and a duplicate is the "
                              'only valid reason to throw one, because on a reject the buyer still got the '
                              'full lead posted to them without being charged for it [EKrBDZYFq2A @ '
                              '00:34:50]. Underneath all of this sits a discipline the overview demo '
                              'repeats: every submitted lead gets a response - matched, unmatched or error '
                              '- which reduces seller-versus-buyer discrepancies on every single post '
                              '[yCAVYNpSdZI @ 00:05:28].',
                              'Calls are treated as the same machine with a dial tone attached. Scott '
                              "Hoffman's pitch is that web leads and calls run through the same business "
                              'rules, routing and billing [d1FxjZ5ukI4 @ 00:01:00], and the demand logic '
                              "is simple: buyers like calls because of a 'virtually 100% contact rate,' "
                              "and that contact rate plus higher closing is why calls 'typically go for "
                              "more money than what the corresponding web lead will' [d1FxjZ5ukI4 @ "
                              '00:01:37]. On the call side the ping post runs in three steps - ping, a '
                              "post that expects a 'success' response, then the call to the terminating "
                              'Twilio number - on a different API action from the data-lead flow '
                              '[CSGuZ-Sping @ 00:02:19]. Whatever the channel, the baseline prerequisites '
                              'never change: an active account, available funds and a filter set, which '
                              "the demo calls 'the most important page in the whole system because these "
                              'are those custom business rules that Define exactly what the lead buyer can '
                              "purchase' [I3MdV-IDLRk @ 00:22:50]. Matching priority defaults to five, and "
                              'buyers on the same priority rotate round robin, so priority is the '
                              "tiebreaker rather than the main sort. Hoffman's strategic framing is that "
                              'calls add a revenue stream so the business is not pigeon-holed into one '
                              'method.'],
               'table': {'caption': 'Where the practitioners agree: the non-negotiable mechanics of a ping '
                                    'post desk',
                         'headers': ['Consensus Point',
                                     'What The Practitioners Say',
                                     'Operator Takeaway',
                                     'Expert Source'],
                         'rows': [['Exclusionary routing comes before any bid sorting',
                                   'Inactive, unfunded and unmatched-filter accounts are removed before '
                                   'sorting by best revenue',
                                   'An unfunded buyer never sees your ping, regardless of bid size',
                                   'boberdoo.com ([BvWILZyxIIA @ 00:00:46])'],
                                  ['Pings fire simultaneously to every matching buyer',
                                   'Pings go out at the same time to every possible matching buyer',
                                   'Bids are compared in parallel, then the lead posts within seconds',
                                   'boberdoo.com ([lpWTQpnduYo @ 00:38:29])'],
                                  ['Seller response is gated on buyer success',
                                   'Matched only returns to the vendor after the buyer sends success',
                                   'Any break in the sequential chain shows up as post rejects',
                                   'boberdoo.com ([vNu0tV99Lnw @ 00:05:06])'],
                                  ['Post rejects are treated as toxic to the desk',
                                   'Duplicates are the only valid post-reject reason; avoid rejects '
                                   'entirely',
                                   'Rejecting buyers still received the full lead without being charged',
                                   'boberdoo.com ([EKrBDZYFq2A @ 00:34:50])'],
                                  ['The filter set is the core of the system',
                                   'Filter set is the most important page, defining exactly what buyers '
                                   'purchase',
                                   'Build buyer business rules here before a single ping goes live',
                                   'boberdoo.com ([I3MdV-IDLRk @ 00:22:50])'],
                                  ['Calls command a premium over web leads',
                                   'Near 100% contact rate makes calls sell above the corresponding web '
                                   'lead',
                                   'Run the same rules, routing and billing for calls and leads',
                                   'boberdoo.com ([d1FxjZ5ukI4 @ 00:01:17])'],
                                  ['The ping carries no contact data at all',
                                   'Ping fields vary by vertical; name, address, phone and email ride the '
                                   'post',
                                   'Let buyers request extra ping fields or have vendors set defaults',
                                   'boberdoo.com ([vNu0tV99Lnw @ 00:02:38])']]}},
              {'title': 'Section 2: Exact Street Mechanics, Tools & Numbers - Vendor Kits, Margin Carves, '
                        'Timeouts and Call Economics',
               'paragraphs': ["Wiring a seller takes three items: the posting specs, the vendor's unique "
                              'API key and their unique SRC [IG4BgI8XMPA @ 00:05:14]. The SRC is the main '
                              'tracking variable and is never passed to buyers, so there is no need to '
                              'mask it; static vendors get a flat lead cost such as $5 that feeds profit '
                              'reports, while dynamic vendors sit at lead cost 0 with return best price '
                              "switched on [lpWTQpnduYo @ 00:02:41]. The ping post spec adds 'four extra "
                              "fields that need to be passed which aren't used with straight posts': key, "
                              "api action with the static value 'ping post lead', mode set to ping or "
                              "post, and lead id, which goes on the post only and echoes the ping's ID "
                              '[P79C92BNJHs @ 00:00:41]. A test lead parameter covers integration testing, '
                              'and the XML posting URL is mandatory for the match-with-partner hashes '
                              "features. Lead Prosper's buyer-side build mirrors it exactly: POST with a "
                              'JSON payload to one URL, Mode distinguishing ping from post, '
                              'Return_Best_Price=1 for a dynamic vendor, success mapped to '
                              '/response/status = Matched, the live bid read from /response/price, and the '
                              'post pulling Lead_ID from {{lp_ping_response:/response/lead_id}} - because '
                              "price was set on the ping, 'there's no need to set it on the POST' "
                              '[Ma1kH51odZ0 @ 00:02:24].',
                              'The money is made in the margin carve. On a static buyer the math is flat: '
                              "a $15 buyer minus a $2 margin replies to the vendor 'matched with a price "
                              "offer of $13' [W03nRhCi63A @ 00:11:08], and the Acme Insurance Agent "
                              'example runs Illinois at $10 minus $2 for an $8 bid and Wisconsin at $15 '
                              'minus $3 for $12. Dynamic wholesalers sit at price 0 with a custom delivery '
                              'and a variable matrix - 30% on bids up to $10, 40% on $10.01-20, 50% above '
                              '$20 - and the lead log proves it out: lead 9 came in at $25, the 50% margin '
                              "offered $12.50 back against a rival's $12, and 'it sold for 25' "
                              '[IG4BgI8XMPA @ 00:25:49]. A second layer sits on the vendor: a premium '
                              'vendor margin adds or subtracts a dollar, turning an $8 offer into $9 or '
                              '$7, and adding money back is how operators win top-quality vendors '
                              '[EKrBDZYFq2A @ 00:13:09]. The ceiling matters as much as the floor. Max '
                              "best price offer exists because 'Maybe you put a lead buyer in to purchase "
                              "leads at $1,000 and carving out a 10% profit margin' - a typo that would "
                              'otherwise pass straight through to the seller [yCAVYNpSdZI @ 00:17:57].',
                              'Clock and billing settings decide whether the auction actually clears. The '
                              "recommended default is '20 on the Ping 60 on the post,' though 'many cases "
                              "vendors will require shorter timeouts' [W03nRhCi63A @ 00:29:02]; at the "
                              'cutoff the system drops lagging buyers and returns the best bid it holds, '
                              'so the seller always gets an answer. On calls, a ping locks the buyer, with '
                              'the lock defaulting to 300 seconds and adjustable per client. Duration is '
                              'read in minutes, and clients have typed 120 thinking it meant seconds, '
                              "'when in return it was returning 120 minute duration' [CSGuZ-Sping @ "
                              '00:17:10]. Local numbers are cheaper both monthly and per minute, so the '
                              'pro move is ordering local numbers for ping post call vendors. The call '
                              'desk ranks buyers by earnings per call - revenue divided by attempts - so a '
                              '$50 buyer with a one-minute minimum converting 50 of 100 calls nets $25, '
                              'and a $30 buyer with no duration wins [CSGuZ-Sping @ 00:33:26]. Hard costs '
                              'are posted openly: call routing runs 10 cents down to 6 cents per minute '
                              'covering both legs, the first block is 30,000 minutes and blocks never '
                              'expire, while web distribution starts at $575 per month for up to 1,500 '
                              'leads per day [I3MdV-IDLRk @ 00:49:12].'],
               'table': {'caption': 'Street settings and numbers the trainers configure live on the desk',
                         'headers': ['Setting Or Mechanic',
                                     'Exact Number Or Value',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Static fixed-dollar margin on a buyer',
                                   '$10 bid minus $2 margin returns $8 to the seller',
                                   'Raise to a $3 margin and the bid drops to $7',
                                   'boberdoo.com ([yCAVYNpSdZI @ 00:28:24])'],
                                  ['Variable margin matrix on a dynamic buyer',
                                   '30% up to $10, 40% on $10.01-20, 50% above $20',
                                   'Dynamic buyer price stays at 0 so the matrix carves each live bid',
                                   'boberdoo.com ([W03nRhCi63A @ 00:17:24])'],
                                  ['Ping and post timeout windows',
                                   '15 seconds on the ping and 30 seconds on the post typical',
                                   'Lagging buyers are excluded so the seller always receives a bid',
                                   'boberdoo.com ([yCAVYNpSdZI @ 00:15:39])'],
                                  ['Buyer refund percentage cap',
                                   '15% refund limit measured over a 30-day window',
                                   'Stops a buyer from refunding 90 out of 100 delivered leads',
                                   'boberdoo.com ([yCAVYNpSdZI @ 00:22:50])'],
                                  ['Automated buyer rebilling trigger',
                                   'Authorize.net CIM rebills $500 when the balance falls below $50',
                                   'Keeps buyer balances funded so they stay eligible to bid on pings',
                                   'boberdoo.com ([I3MdV-IDLRk @ 00:21:20])'],
                                  ['Call routing minute pricing',
                                   '10 cents down to 6 cents per minute covering both call legs',
                                   'First block is 30,000 minutes and purchased blocks never expire',
                                   'boberdoo.com ([I3MdV-IDLRk @ 00:49:12])'],
                                  ['Call minimum duration on the filter set',
                                   '0.3-minute call cleared a 0.17 minimum; a 0.32-minute call failed 1.25',
                                   'Enter duration in minutes, never seconds, on every call buyer',
                                   'boberdoo.com ([CSGuZ-Sping @ 00:14:17])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Desk-level moves the boberdoo trainers flag on live builds',
                           'body': 'Small configuration choices the trainers single out for cutting cost, '
                                   'catching broken pings and testing bids without torching volume.',
                           'items': ['Order local numbers when dealing with a ping post call vendor, '
                                     'because they are cheaper on both the monthly and the per-minute cost '
                                     '[boberdoo.com — CSGuZ-Sping @ 00:06:49]',
                                     'Treat Show Lead Log as your best friend on the leads page: read it '
                                     "bottom-up to see raw buyer responses and run down 'price is missing' "
                                     'errors [boberdoo.com — EKrBDZYFq2A @ 00:27:08]',
                                     'Use JavaScript number display to hide the phone number when no buyer '
                                     'is available, such as at 1 a.m., and let the phone duplicity check '
                                     'route repeat callers back to the original buyer [boberdoo.com — '
                                     'I3MdV-IDLRk @ 00:12:24]',
                                     'Run bid experiments in quarantine on a specific percentage of pings '
                                     "'so as not to cannibalize all of the traffic', with significance "
                                     'reporting on the results [boberdoo.com — BvWILZyxIIA @ 00:15:16]']},
               'sop_steps': [{'step': 1,
                              'title': 'Build the dynamic vendor kit',
                              'action': 'Create the vendor account and SRC, set lead cost to 0, and switch '
                                        "return best price to 'yes'.",
                              'detail': "Dynamic vendors run at lead cost 0 with 'allow using return best "
                                        "price parameter' set to yes or 'yes but sold non exclusively'; "
                                        "Brett recommends sending it to 'yes' first, then hand over specs, "
                                        'API key and SRC [boberdoo.com — lpWTQpnduYo @ 00:04:03]'},
                             {'step': 2,
                              'title': 'Configure buyer filter sets and margins',
                              'action': 'Give static buyers a fixed-dollar margin and dynamic wholesalers '
                                        'a 0 price with a percentage matrix.',
                              'detail': 'Static buyer example runs Illinois at $10 minus $2 for $8 and '
                                        'Wisconsin at $15 minus $3 for $12, while the dynamic buyer sits '
                                        'at price 0 with tiered percentage margins on a custom delivery '
                                        '[boberdoo.com — W03nRhCi63A @ 00:15:00]'},
                             {'step': 3,
                              'title': 'Set timeouts and the max offer ceiling',
                              'action': 'Keep the ping timeout shorter than the post timeout and cap the '
                                        'best-price offer.',
                              'detail': 'The ping timeout is shorter so buyer bids can be collected first, '
                                        'and the maximum best-price offer caps the bid, for example at '
                                        '$45, when margin plus bid would exceed the value you set '
                                        '[boberdoo.com — YLw0lKsOayk @ 00:11:18]'},
                             {'step': 4,
                              'title': 'Ramp on one geo and audit the ratios',
                              'action': 'Launch on one small geo with a low daily cap, run for a few days, '
                                        'then check pings against posts.',
                              'detail': "Run it for a few days because 'one success does not equal a "
                                        "campaign that is live and troubleshooted', and question any "
                                        'vendor showing 10,000 pings against 5 posts [boberdoo.com — '
                                        'CSGuZ-Sping @ 00:29:22]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split on the boberdoo bench is what happens when the top '
                              "bidder post-rejects. Under plain 'Yes,' the deal runs one-to-one: the "
                              'system calculates the best bid among buyers, passes it to the seller, and '
                              'if that buyer rejects the post the seller gets a reject [yCAVYNpSdZI @ '
                              "00:16:56]. 'Yes but sold non-exclusively' keeps the lead alive by retrying "
                              'the next bidder, and the presenters frame that risk differently. One '
                              'walkthrough shotguns a ping to 10 buyers, collects three bids of $12, $10 '
                              "and $8 at a 10% margin, warns that the fallback means 'you could in theory "
                              "end up with a lead selling at a loss,' and closes with 'I would recommend "
                              "sending it to yes first' [EKrBDZYFq2A @ 00:23:24]. The Scott-and-Brett "
                              'session describes the same fallback as retrying only buyers whose offer '
                              'exceeds the $13 cost, so the lead is never sold below what was paid for it '
                              '[IG4BgI8XMPA @ 00:12:17]. The overview demo reconciles the two readings: '
                              'the fall-through targets the next buyer priced above cost while ignoring '
                              'margin [yCAVYNpSdZI @ 00:17:17]. For an operator, that means the '
                              'non-exclusive fallback protects the principal, not the spread, and the '
                              "conservative starting point the presenters name is plain 'Yes.'",
                              'Margin design has no single house formula; every presenter builds a '
                              'different ladder. One webinar runs a dynamic wholesaler at price 0 with a '
                              'variable margin of 30% on bids up to $10, 40% on $10.01 to $20, and 50% '
                              'above $20 [W03nRhCi63A @ 00:17:24]. The March 2015 session advises '
                              'percentage margins for dynamic buyers and shows a gentler matrix of 10% on '
                              '$0 to $10, 20% on $10.01 to $25, and a 30% default [lpWTQpnduYo @ '
                              '00:06:22]. Another session stacks four tiers at 15%, 20%, 25% and a 30% '
                              'default, then layers a second margin at the vendor level: the buyer filter '
                              'set turns a $10 bid into $8, a premium vendor adjustment of plus $1 pushes '
                              'the offer to $9 and minus $1 drops it to $7, and adding money back is the '
                              'move for winning top-quality vendors [EKrBDZYFq2A @ 00:13:09]. The overview '
                              'demo runs yet another curve, 10% on $0 to $10, 15% on $10 to $25 and 25% '
                              'above $25, and frames the per-seller plus or minus $1 as a way to reward '
                              'high quality or high volume lead sellers [DSbDVWpyXUI @ 00:19:22]. The '
                              'constant across sessions is structure: static buyers usually get a fixed '
                              'dollar margin, while percentage ladders are the recommended tool for '
                              'dynamic buyers.',
                              'Exclusive versus shared gets settled by arithmetic, not doctrine. The '
                              'scenarios engine compares one exclusive buyer against the sum of '
                              'non-exclusive buyers and picks the higher total: sell it twice at $12 and '
                              "'you're going to make 24 compared to 20' [W03nRhCi63A @ 00:31:46]. The same "
                              'contrarian ranking shows up on calls. A dynamic call buyer has duration '
                              'ignored and gets the call on best price, but earnings per call, revenue '
                              'divided by attempts, can flip the obvious winner: a $50 buyer demanding a '
                              '1-minute duration who converts only 50 of 100 calls yields $25, so a $30 '
                              'buyer with no duration requirement takes the traffic [CSGuZ-Sping @ '
                              '00:33:26]. The calls webinar also gives the dynamic buyer defaults for that '
                              'setup: minimum duration 0 and no ring timeout. Revenue sharing draws an '
                              'outright split between sessions. The general demo pays vendors on all '
                              'leads, sold leads only, revenue splits or revenue buckets, and shows a 25% '
                              'vendor revenue share inside ROI tracking, with UTM fields added through '
                              'custom reports [I3MdV-IDLRk @ 00:54:35]. The overview presenter refuses to '
                              "mix the two models: 'if you're going to do rev sharing models, I would "
                              "recommend it not being in a ping post fashion' [yCAVYNpSdZI @ 00:25:13]."],
               'table': {'caption': 'Competing ping-post playbooks taught side by side by the boberdoo and '
                                    'Lead Prosper presenters',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Post-reject fallback setting on a dynamic vendor source',
                                   "'Yes' runs one-to-one; a top-bidder reject sends the seller a reject",
                                   "'Yes but sold non-exclusively' retries the next bidder above cost, "
                                   'ignoring margin',
                                   'boberdoo.com ([EKrBDZYFq2A @ 00:23:24]); boberdoo.com ([yCAVYNpSdZI @ '
                                   '00:17:17])'],
                                  ['Ping and post timeout windows for buyer auctions',
                                   '20 seconds on the ping and 60 on the post when sellers do not specify',
                                   'Typical 15-second ping and 30-second post, with lagging buyers '
                                   'excluded from the auction',
                                   'boberdoo.com ([W03nRhCi63A @ 00:29:02]); boberdoo.com ([yCAVYNpSdZI @ '
                                   '00:15:39])'],
                                  ['Variable margin ladder applied to dynamic wholesale buyers',
                                   '30% up to $10, 40% from $10.01 to $20, 50% above $20',
                                   '10% on $0 to $10, 20% on $10.01 to $25, 30% default tier',
                                   'boberdoo.com ([W03nRhCi63A @ 00:17:24]); boberdoo.com ([lpWTQpnduYo @ '
                                   '00:12:57])'],
                                  ['Exclusive sale versus shared sale on the same lead',
                                   'One exclusive buyer at $20 wins only when shared totals fall short',
                                   'Two shared sales at $12 each produce $24, beating the $20 exclusive',
                                   'boberdoo.com ([IG4BgI8XMPA @ 00:31:19])'],
                                  ['Static price ping post versus dynamic bid pricing per lead',
                                   'Static-price ping post only checks coverage and sells at the fixed '
                                   'filter-set price',
                                   'Dynamic pricing is called more common, with payouts like $1, $10 or '
                                   '$7.36',
                                   'boberdoo.com ([o5v8ME_4M_M @ 00:01:28]); boberdoo.com ([EKrBDZYFq2A @ '
                                   '00:08:00])'],
                                  ['TrustedForm or Jornaya token placement across ping and post',
                                   'Some companies send the token on the ping because buyers want it early',
                                   'Others hold it for the post; masked values are offered as an option',
                                   'boberdoo.com ([vNu0tV99Lnw @ 00:03:05])'],
                                  ['Call buyer type ranked by earnings per call attempt',
                                   '$50 buyer with 1-minute duration converting 50 of 100 calls yields $25',
                                   '$30 buyer with no duration requirement wins on revenue divided by '
                                   'attempts',
                                   'boberdoo.com ([CSGuZ-Sping @ 00:33:26])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["Post rejects are the leak the presenters attack hardest. 'You never want to "
                              "have post rejects,' one webinar states, adding that a duplicate is the only "
                              "valid reason to reject a post, and that otherwise the buyer 'got the full "
                              "lead posted to them but they're not charged for it' [EKrBDZYFq2A @ "
                              "00:34:50]. The 'What Is Ping Post?' explainer lists the causes operators "
                              'actually hit: vendors sending additional fields that cause the filter set '
                              "to exclude, which it calls 'very common,' plus duplicates, outside "
                              'lead-scoring and DNC checks, and errors from a missing lead ID or '
                              'misconfiguration [vNu0tV99Lnw @ 00:07:35]. Because processing is sequential '
                              "and the system waits for the buyer's success response before returning "
                              'Matched to the vendor, any break in that chain lands as a reject. The '
                              'volume check is blunt: 10,000 pings against 5 posts means it is time to '
                              "question the vendor [EKrBDZYFq2A @ 00:32:42]. The overview demo's ping-post "
                              'reports show outgoing pings versus accepted for both lead sellers and '
                              'partners, which is where that ratio surfaces [DSbDVWpyXUI @ 00:40:20]. For '
                              'the forensic pass, the show lead log, which the same webinar calls your '
                              'best friend on the leads page, exposes the raw buyer responses behind each '
                              'ping.',
                              'Call campaigns break in ways web leads never do. The calls webinar reports '
                              'clients typing 120 into a filter set or response field thinking it meant '
                              'seconds, when the system read it as a 120-minute duration, because duration '
                              'defaults to minutes and support can handle the correction through a ticket '
                              'or chat [CSGuZ-Sping @ 00:17:10]. Cadence kills call campaigns too: the '
                              'data has to be submitted before the call comes in, and the ramp-up rule is '
                              "one small geo, a low daily cap and a few days of testing, because 'one "
                              "success does not equal a campaign that is live and troubleshooted' "
                              '[CSGuZ-Sping @ 00:29:22]. The cautionary tale is a single 99999 test zip '
                              "that produced '30 calls promised day one' complaints [CSGuZ-Sping @ "
                              '00:31:03]. Billing buffers bite on the general demo as well: on a 60-second '
                              'buffer a 59-second call is declined, and the JavaScript number display '
                              'exists to hide the phone number when no buyer is available, such as at 1 '
                              'a.m. [I3MdV-IDLRk @ 00:26:48]. Repeat callers get routed back to the '
                              'original buyer through a phone duplicity check, and the internal Do Not '
                              "Call list 'is not hooked up with any state or federal databases.'",
                              'The money traps sit with buyers, not traffic. Without a refund-percentage '
                              'limit a buyer can refund 90% of leads, which is why the general demo builds '
                              'the guard in, alongside commission calculated on gross margin [I3MdV-IDLRk '
                              '@ 00:19:21]. The overview presenter names capping a refund limit as a '
                              'personal favorite, with an example of 15% over 30 days, warning that a '
                              'buyer could otherwise refund 90 of 100 leads [yCAVYNpSdZI @ 00:22:50]. '
                              "Typos are the second bleed: 'Maybe you put a lead buyer in to purchase "
                              "leads at $1,000 and carving out a 10% profit margin,' which is exactly what "
                              'the max best price offer ceiling is built to stop [yCAVYNpSdZI @ 00:17:57]. '
                              'Credit risk runs upstream too: the general demo warns that unpaid bills '
                              'from one large client can sink call-tracking firms [I3MdV-IDLRk @ '
                              '00:52:52]. Funding is the operational gate. Buyers need an active account, '
                              'available funds and a filter set before they match, and the authorize.net '
                              'CIM example rebills $500 the moment the balance falls below $50. Source '
                              'pricing gets the same discipline, with paid search set at $20 against $10 '
                              'for display, and about 30 source switches control each source.'],
               'table': {'caption': 'Firsthand failure modes and the checks the presenters attach to each '
                                    'one',
                         'headers': ['Failure Mode',
                                     'What Happened Or Was Warned',
                                     'Operator Check Taught',
                                     'Expert Source'],
                         'rows': [['Seconds-versus-minutes confusion in call duration fields',
                                   'Clients entered 120 thinking seconds; the system returned a 120-minute '
                                   'duration',
                                   'Remember duration defaults to minutes; support corrects it through '
                                   'ticket or chat',
                                   'boberdoo.com ([CSGuZ-Sping @ 00:17:10])'],
                                  ['Launching a call campaign off a single test zip',
                                   "One 99999 test zip led to '30 calls promised day one' complaints",
                                   'Start with one small geo, a low daily cap, and days of testing',
                                   'boberdoo.com ([CSGuZ-Sping @ 00:31:03])'],
                                  ['Uncapped buyer refunds draining sold lead revenue',
                                   'A buyer could refund 90 of 100 leads without any refund limit',
                                   'Cap refunds, for example at 15% over a 30-day window',
                                   'boberdoo.com ([DSbDVWpyXUI @ 00:23:05])'],
                                  ['Fat-finger buyer price pushing outsized offers to vendors',
                                   'A buyer entered at $1,000 with a 10% margin carved out',
                                   'Set the maximum best price offer ceiling, for example capping at $45',
                                   'boberdoo.com ([yCAVYNpSdZI @ 00:17:57]); boberdoo.com ([YLw0lKsOayk @ '
                                   '00:11:18])'],
                                  ['Ping volume that never converts into real posts',
                                   'A vendor sending 10,000 pings while only 5 posts ever arrive',
                                   'Question the vendor and filter the leads page down to pings only',
                                   'boberdoo.com ([EKrBDZYFq2A @ 00:32:42])'],
                                  ['Partner hash matching failing on shared lead sales',
                                   'No industry standard for passed fields, so mismatched field names '
                                   'break matching',
                                   'Agree on fields up front and use the XML post method for hashes',
                                   'boberdoo.com ([W03nRhCi63A @ 00:36:20]); boberdoo.com ([W03nRhCi63A @ '
                                   '00:38:12])'],
                                  ['Email delivery choking on hosting provider sending limits',
                                   'GoDaddy SMTP carries daily limits, and email-open tracking is not '
                                   'exact science',
                                   'Supply your own SMTP; most people opt for a third-party service such '
                                   'as srid',
                                   'boberdoo.com ([lpWTQpnduYo @ 00:32:55])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Checks Before Live Ping-Post Traffic',
                           'body': 'Each gate below comes straight from a loss, complaint, or warning the '
                                   'boberdoo presenters reported on lead and call auctions [boberdoo.com — '
                                   'EKrBDZYFq2A @ 00:34:50].',
                           'items': ['Verify every call duration field is entered in minutes, after '
                                     'clients typed 120 believing it meant seconds and got a 120-minute '
                                     'duration [boberdoo.com — CSGuZ-Sping @ 00:17:10].',
                                     'Hold new call campaigns at one small geo and a low daily cap for a '
                                     'few days, because one success does not equal a live, troubleshooted '
                                     'campaign [boberdoo.com — CSGuZ-Sping @ 00:29:22].',
                                     "Start every dynamic source on 'Yes' before enabling 'yes but sold "
                                     "non-exclusively,' since the fallback can sell a lead at a loss "
                                     '[boberdoo.com — EKrBDZYFq2A @ 00:23:24].',
                                     'Install a refund cap such as 15% over 30 days before onboarding '
                                     'buyers who could otherwise refund 90 of 100 leads [boberdoo.com — '
                                     'yCAVYNpSdZI @ 00:22:50].']}}],
 'pull_quote': "'One success does not equal a campaign that is live and troubleshooted.' — boberdoo.com "
               '(CSGuZ-Sping @ 00:29:22).',
 'diagram_id': 'diag-05',
 'action_checklist': ['Hand each vendor three items before the first ping: the ping post specs, their '
                      'unique API key, and their unique SRC [boberdoo.com — IG4BgI8XMPA @ 00:05:14].',
                      'Set dynamic vendor sources to a lead cost of 0 and enable the return best price '
                      "parameter on 'Yes' or 'yes but sold non exclusively' [boberdoo.com — lpWTQpnduYo @ "
                      '00:04:03].',
                      'Run 20 seconds on the ping and 60 on the post unless the vendor requires shorter '
                      'timeouts [boberdoo.com — W03nRhCi63A @ 00:29:02].',
                      'On a Lead Prosper buyer setup, send POST JSON with Mode=ping, Return_Best_Price=1 '
                      'for dynamic vendors, and map /response/status to Matched and /response/price as the '
                      'real-time price [Lead Prosper — Ma1kH51odZ0 @ 00:01:13].',
                      'Turn on scenarios so the system compares one exclusive buyer against the sum of '
                      'non-exclusive buyers and picks the higher total [boberdoo.com — yCAVYNpSdZI @ '
                      '00:14:59].',
                      'Watch closes daily: raise bids when nothing closes all day, and pause accounts when '
                      'the phones go down [boberdoo.com — lpWTQpnduYo @ 00:22:07].'],
 'statutory_citations': [{'title': 'boberdoo.com — boberdoo Ping Post Webinar | Ping Post Software Experts '
                                   '[00:23:24]',
                          'url': 'https://www.youtube.com/watch?v=EKrBDZYFq2A&t=1404s',
                          'relevance': "Primary practitioner testimony on choosing 'Yes' over "
                                       'non-exclusive fallback and eliminating post rejects.'},
                         {'title': 'boberdoo.com — Ping Post For Calls Webinar [00:29:22]',
                          'url': 'https://www.youtube.com/watch?v=CSGuZ-Sping&t=1762s',
                          'relevance': 'Primary practitioner testimony on call campaign ramp-up, duration '
                                       'units, and earnings-per-call buyer ranking.'},
                         {'title': 'boberdoo.com — Ping Post Lead Distribution | boberdoo Ping Post '
                                   'Software [00:16:56]',
                          'url': 'https://www.youtube.com/watch?v=yCAVYNpSdZI&t=1016s',
                          'relevance': 'Primary practitioner testimony on return best price modes, refund '
                                       'caps, typo ceilings, and rev-share limits.'},
                         {'title': 'boberdoo.com — Ping Post Webinar | boberdoo Ping Options Software '
                                   '[00:12:17]',
                          'url': 'https://www.youtube.com/watch?v=IG4BgI8XMPA&t=737s',
                          'relevance': 'Primary practitioner testimony on non-exclusive resale fallback, '
                                       'margin math, and lead log diagnostics.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'I3MdV-IDLRk',
                       'title': 'Lead Distribution Software Demo With Call Routing by boberdoo',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': 'Matching priority, everything defaults to a five and clients on the same '
                               'priority just go into a round robin.',
                       'tip': 'Matching priority, everything defaults to a five and clients on the same '
                              'priority just go into a round robin.',
                       'timestamp': 1448,
                       'timestamp_seconds': 1448,
                       'timestamp_label': '[00:24:08]',
                       'url': 'https://www.youtube.com/watch?v=I3MdV-IDLRk&t=1448s',
                       'markdown': '[00:24:08](https://www.youtube.com/watch?v=I3MdV-IDLRk&t=1448s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YLw0lKsOayk',
                       'title': 'Ping Post Webinar 11/12/13 | boberdoo Ping/Post System',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': "If I'm a seller and I ping your system, if I don't get a response back in "
                               '20 seconds, the system is automatically going to return back just a '
                               'generic unmatched.',
                       'tip': "If I'm a seller and I ping your system, if I don't get a response back in "
                              '20 seconds, the system is automatically going to return back just a generic '
                              'unmatched.',
                       'timestamp': 591,
                       'timestamp_seconds': 591,
                       'timestamp_label': '[00:09:51]',
                       'url': 'https://www.youtube.com/watch?v=YLw0lKsOayk&t=591s',
                       'markdown': '[00:09:51](https://www.youtube.com/watch?v=YLw0lKsOayk&t=591s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CSGuZ-Sping',
                       'title': 'Ping Post For Calls Webinar',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': 'Run it for a few days; one success does not equal a campaign that is live '
                               'and troubleshooted.',
                       'tip': 'Run it for a few days; one success does not equal a campaign that is live '
                              'and troubleshooted.',
                       'timestamp': 1762,
                       'timestamp_seconds': 1762,
                       'timestamp_label': '[00:29:22]',
                       'url': 'https://www.youtube.com/watch?v=CSGuZ-Sping&t=1762s',
                       'markdown': '[00:29:22](https://www.youtube.com/watch?v=CSGuZ-Sping&t=1762s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'd1FxjZ5ukI4',
                       'title': 'How To Sell Calls | boberdoo Call Routing Software',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': "Lead buyers like calls because it's virtually 100% contact rate; the more "
                               'people they talk to, the more they close.',
                       'tip': "Lead buyers like calls because it's virtually 100% contact rate; the more "
                              'people they talk to, the more they close.',
                       'timestamp': 77,
                       'timestamp_seconds': 77,
                       'timestamp_label': '[00:01:17]',
                       'url': 'https://www.youtube.com/watch?v=d1FxjZ5ukI4&t=77s',
                       'markdown': '[00:01:17](https://www.youtube.com/watch?v=d1FxjZ5ukI4&t=77s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'W03nRhCi63A',
                       'title': 'Ping Post Webinar | boberdoo Ping Post Software',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': "Sell it twice at $12, you're going to make 24 compared to 20, and that's "
                               'what the scenarios does.',
                       'tip': "Sell it twice at $12, you're going to make 24 compared to 20, and that's "
                              'what the scenarios does.',
                       'timestamp': 1906,
                       'timestamp_seconds': 1906,
                       'timestamp_label': '[00:31:46]',
                       'url': 'https://www.youtube.com/watch?v=W03nRhCi63A&t=1906s',
                       'markdown': '[00:31:46](https://www.youtube.com/watch?v=W03nRhCi63A&t=1906s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lpWTQpnduYo',
                       'title': 'Ping Post Webinar 3/2015 | boberdoo Ping Post Software',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': 'It is then up to the vendor if they accept that $8 offer to then send the '
                               'post through.',
                       'tip': 'It is then up to the vendor if they accept that $8 offer to then send the '
                              'post through.',
                       'timestamp': 343,
                       'timestamp_seconds': 343,
                       'timestamp_label': '[00:05:43]',
                       'url': 'https://www.youtube.com/watch?v=lpWTQpnduYo&t=343s',
                       'markdown': '[00:05:43](https://www.youtube.com/watch?v=lpWTQpnduYo&t=343s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'vNu0tV99Lnw',
                       'title': 'What Is Ping Post?',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': "They sent additional fields that cause the filter set to exclude; that's "
                               'very common.',
                       'tip': "They sent additional fields that cause the filter set to exclude; that's "
                              'very common.',
                       'timestamp': 455,
                       'timestamp_seconds': 455,
                       'timestamp_label': '[00:07:35]',
                       'url': 'https://www.youtube.com/watch?v=vNu0tV99Lnw&t=455s',
                       'markdown': '[00:07:35](https://www.youtube.com/watch?v=vNu0tV99Lnw&t=455s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EKrBDZYFq2A',
                       'title': 'boberdoo Ping Post Webinar | Ping Post Software Experts',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': 'You could in theory end up with a lead selling at a loss.',
                       'tip': 'You could in theory end up with a lead selling at a loss.',
                       'timestamp': 1368,
                       'timestamp_seconds': 1368,
                       'timestamp_label': '[00:22:48]',
                       'url': 'https://www.youtube.com/watch?v=EKrBDZYFq2A&t=1368s',
                       'markdown': '[00:22:48](https://www.youtube.com/watch?v=EKrBDZYFq2A&t=1368s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EKrBDZYFq2A',
                       'title': 'boberdoo Ping Post Webinar | Ping Post Software Experts',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': 'You never want to have post rejects.',
                       'tip': 'You never want to have post rejects.',
                       'timestamp': 2090,
                       'timestamp_seconds': 2090,
                       'timestamp_label': '[00:34:50]',
                       'url': 'https://www.youtube.com/watch?v=EKrBDZYFq2A&t=2090s',
                       'markdown': '[00:34:50](https://www.youtube.com/watch?v=EKrBDZYFq2A&t=2090s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'BvWILZyxIIA',
                       'title': 'boberdoo Demo',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': 'Each experiment can be set up in quarantine with a specific percentage of '
                               'pings so as not to cannibalize all of the traffic.',
                       'tip': 'Each experiment can be set up in quarantine with a specific percentage of '
                              'pings so as not to cannibalize all of the traffic.',
                       'timestamp': 916,
                       'timestamp_seconds': 916,
                       'timestamp_label': '[00:15:16]',
                       'url': 'https://www.youtube.com/watch?v=BvWILZyxIIA&t=916s',
                       'markdown': '[00:15:16](https://www.youtube.com/watch?v=BvWILZyxIIA&t=916s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ma1kH51odZ0',
                       'title': 'Boberdoo Ping Post Buyer Setup',
                       'channel': 'Lead Prosper',
                       'author': 'Lead Prosper',
                       'text': 'The next field, Mode, is very important.',
                       'tip': 'The next field, Mode, is very important.',
                       'timestamp': 55,
                       'timestamp_seconds': 55,
                       'timestamp_label': '[00:00:55]',
                       'url': 'https://www.youtube.com/watch?v=Ma1kH51odZ0&t=55s',
                       'markdown': '[00:00:55](https://www.youtube.com/watch?v=Ma1kH51odZ0&t=55s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'P79C92BNJHs',
                       'title': 'How To Ping Post Specifications | boberdoo Ping/Post Software',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': "Finally there's lead id which shouldn't be sent on the ping, only on the "
                               'post.',
                       'tip': "Finally there's lead id which shouldn't be sent on the ping, only on the "
                              'post.',
                       'timestamp': 77,
                       'timestamp_seconds': 77,
                       'timestamp_label': '[00:01:17]',
                       'url': 'https://www.youtube.com/watch?v=P79C92BNJHs&t=77s',
                       'markdown': '[00:01:17](https://www.youtube.com/watch?v=P79C92BNJHs&t=77s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yCAVYNpSdZI',
                       'title': 'Ping Post Lead Distribution | boberdoo Ping Post Software',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': "So if you're going to do rev sharing models, I would recommend it not "
                               'being in a ping post fashion.',
                       'tip': "So if you're going to do rev sharing models, I would recommend it not being "
                              'in a ping post fashion.',
                       'timestamp': 1513,
                       'timestamp_seconds': 1513,
                       'timestamp_label': '[00:25:13]',
                       'url': 'https://www.youtube.com/watch?v=yCAVYNpSdZI&t=1513s',
                       'markdown': '[00:25:13](https://www.youtube.com/watch?v=yCAVYNpSdZI&t=1513s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CLgSYIHZ_GY',
                       'title': 'How To Ping Post Specifications | boberdoo Ping Post Software',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': 'Lead ID is sent on the post only, echoing the ID returned in the '
                               'successful ping response so the post matches its ping.',
                       'tip': 'Lead ID is sent on the post only, echoing the ID returned in the successful '
                              'ping response so the post matches its ping.',
                       'timestamp': 75,
                       'timestamp_seconds': 75,
                       'timestamp_label': '[00:01:15]',
                       'url': 'https://www.youtube.com/watch?v=CLgSYIHZ_GY&t=75s',
                       'markdown': '[00:01:15](https://www.youtube.com/watch?v=CLgSYIHZ_GY&t=75s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'o5v8ME_4M_M',
                       'title': 'How To Ping Post Basics | boberdoo Lead Distribution Software',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': 'To sell shared leads, raise partners-per-lead in the source, select yes '
                               'but sold non exclusively, and set buyer exclusivity to none.',
                       'tip': 'To sell shared leads, raise partners-per-lead in the source, select yes but '
                              'sold non exclusively, and set buyer exclusivity to none.',
                       'timestamp': 54,
                       'timestamp_seconds': 54,
                       'timestamp_label': '[00:00:54]',
                       'url': 'https://www.youtube.com/watch?v=o5v8ME_4M_M&t=54s',
                       'markdown': '[00:00:54](https://www.youtube.com/watch?v=o5v8ME_4M_M&t=54s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'DSbDVWpyXUI',
                       'title': 'boberdoo.com Overview Demo With Ping Post | Lead Software',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': 'The vendor premium margin lets you reward high quality or high volume lead '
                               'sellers.',
                       'tip': 'The vendor premium margin lets you reward high quality or high volume lead '
                              'sellers.',
                       'timestamp': 1162,
                       'timestamp_seconds': 1162,
                       'timestamp_label': '[00:19:22]',
                       'url': 'https://www.youtube.com/watch?v=DSbDVWpyXUI&t=1162s',
                       'markdown': '[00:19:22](https://www.youtube.com/watch?v=DSbDVWpyXUI&t=1162s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'IG4BgI8XMPA',
                       'title': 'Ping Post Webinar | boberdoo Ping Options Software',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': 'We look at the two offers from this account, 25 after the margin was set '
                               'to 50 percent, we offered 12.50 back to the vendor compared to this '
                               'particular account that offered 15 and after margin was only 12.',
                       'tip': 'We look at the two offers from this account, 25 after the margin was set to '
                              '50 percent, we offered 12.50 back to the vendor compared to this particular '
                              'account that offered 15 and after margin was only 12.',
                       'timestamp': 1528,
                       'timestamp_seconds': 1528,
                       'timestamp_label': '[00:25:28]',
                       'url': 'https://www.youtube.com/watch?v=IG4BgI8XMPA&t=1528s',
                       'markdown': '[00:25:28](https://www.youtube.com/watch?v=IG4BgI8XMPA&t=1528s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'}]}
