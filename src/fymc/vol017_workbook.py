from __future__ import annotations

def build_volume_017_workbook() -> dict:
    return {'workbook_id': 'wb-017-domain-investing',
 'volume_id': 'vol-017-domain-investing',
 'title': 'Domain Investing — Practitioner Testimony Operator Workbook',
 'subtitle': 'A Field Worksheet Series for Flipping Cheap Names, Building Registrar and DNS '
             'Infrastructure, Hunting Expired Inventory, Auditing Aged Domains, and Valuing Exact-Match '
             'and One-Word Assets',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'The Buy-Low Flip and Registrar Setup Ledger',
                 'purpose': 'Turn the beginner flip loop into a written, repeatable routine: pick '
                            'extensions, screen out weak names, mine AI brainstorms, price against real '
                            'comps, run the buy math, choose a registrar on renewal cost and free privacy, '
                            'cut DNS over cleanly, and list every name so renewals never quietly eat the '
                            'profit.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Work one candidate name at a time from brainstorm to listing, and fill '
                                  'every field before spending money on the next name.',
                                  'Write actual dollar figures for registration, renewal, appraisal, '
                                  'comps, and exit price; never leave a field as a vague estimate.',
                                  'Run the reject filter before checking availability so dashes, '
                                  'misspellings, dates, and numbers never reach the cart.',
                                  'Verify registrar prices and policies on the live cart page, and record '
                                  'the renewal price beside the first-year price every time.',
                                  'Revisit this ledger every 90 days to relist unsold names at a new price '
                                  'and decide which names to renew or drop.'],
                 'fields': [{'name': 'extension_rule',
                             'type': 'textarea',
                             'prompt': 'Write the extension rule you will follow before any name enters '
                                       'the cart. State which extension comes first, which alternates you '
                                       'accept, and the share-of-sales figure that justifies the order, '
                                       'then explain why country extensions rank lower on your list.',
                             'example': '.com goes first because Thinking Blueprint puts it at about 75% '
                                        'of all domain sales [Thinking Blueprint — 12ohlClK0g8 @ '
                                        '00:02:27]. Alternates are .ai and .io only, the two alternates '
                                        'practitioners rank as hot. Country extensions wait until a .com '
                                        'and an .ai version have both been checked, and every candidate '
                                        'still has to be short, memorable, and free of hyphens.'},
                            {'name': 'reject_filter',
                             'type': 'text',
                             'prompt': 'List the disqualifiers that knock a candidate name out before it '
                                       'reaches the cart. Cover dashes, spelling tricks, dates, and '
                                       'numbers, and describe the exact moment in your workflow when you '
                                       'run this screen so nothing slips through.',
                             'example': 'Any name with a dash, a creative misspelling, or a date dies '
                                        'before checkout [Make Money with Stacy La — SuiwtFN2AO8 @ '
                                        '00:04:48]. Numbers and odd spellings are cut on the same pass, '
                                        'matching the consensus on short, memorable names. The screen runs '
                                        'after each AI or keyword brainstorm and again before payment, so '
                                        'a tempting typo never survives a search session.'},
                            {'name': 'ai_name_hunt',
                             'type': 'textarea',
                             'prompt': 'Record one AI-assisted brainstorm session. Paste the raw seed '
                                       'list, the word swaps you tried, which combinations were available '
                                       'and at what price, and how you judged whether each combination '
                                       'reads as natural phrasing rather than a forced mashup.',
                             'example': 'Seed: FleetVision.ai from a ChatGPT list. Swapping Fleet for '
                                        'Gaming landed GamingVision.ai, available at $90, and swapping '
                                        'Forecast for Weather surfaced WeatherVision [KT Blogger — '
                                        'yz0jUQvunAI @ 00:35:43]. Each combination was treated as raw ore '
                                        'and kept only if it read as a sensible phrase that Google NLP '
                                        'would parse cleanly; anything clunky went straight to the discard '
                                        'column.'},
                            {'name': 'comps_and_pricing',
                             'type': 'textarea',
                             'prompt': 'For your strongest candidate, write the GoDaddy appraisal figure '
                                       'beside at least two NameBio comparable sales, then set your list '
                                       'price. Note how far you discount the automated number and the date '
                                       'you will relist if it stays unsold.',
                             'example': 'The appraisal is paired with NameBio comps before any price is '
                                        'set, and the name is relisted at a new price if 90 days pass '
                                        'without a sale [David Utke — A6-lVEeaHEs @ 00:05:02]. Tim Verdouw '
                                        'trusts AI output but discounts a $5,000 to $10,000 call to a '
                                        'realistic $2,500 to $3,000 [Tim Verdouw — ehERSgNWmRc @ '
                                        '00:13:01]; the same haircut applies here.'},
                            {'name': 'buy_math',
                             'type': 'text',
                             'prompt': 'Write the buy math for this name: registration cost, renewal cost, '
                                       'your per-name spending cap, and the realistic exit price. Then '
                                       'state the margin you lock in at purchase and whether a single '
                                       'renewal would erase it.',
                             'example': 'Profit is made on the buy, not the sale: a name worth $4,000 '
                                        'bought for $80 has the gain locked in [Thinking Blueprint — '
                                        '12ohlClK0g8 @ 00:05:29]. The warning case is Andrey Verevko, who '
                                        'bought at $10, renewed at $15, and sold at $20, ending five '
                                        'dollars in the hole [Andrey Verevko — bVQnMN-Qrd8 @ 00:07:32]. '
                                        'This name stays under a $50 cap.'},
                            {'name': 'portfolio_size_plan',
                             'type': 'textarea',
                             'prompt': 'Decide how many names your first batch will hold and what hit rate '
                                       'you expect. Write the batch size, the number of winners you need '
                                       'to break even, and the pace at which you will add names after the '
                                       'first purchases.',
                             'example': 'First batch: 20 names, expecting 2 to 3 winners, with two right '
                                        'domains projected to bring $7,000 or $15,000 [Thinking Blueprint '
                                        '— 12ohlClK0g8 @ 00:05:29]. Pace stays deliberate because '
                                        "GoDaddy's guidance is to start slow, calling the alternative one "
                                        'of the biggest mistakes [GoDaddy — qJ6o0aD4Msg @ 00:07:30]. New '
                                        'names are added only after the first sales land.'},
                            {'name': 'registrar_choice',
                             'type': 'textarea',
                             'prompt': 'Choose the registrar that will hold this portfolio. Record the '
                                       '.com registration and renewal price you verified, whether WHOIS '
                                       'privacy is free, the refund policy, and any nameserver restriction '
                                       'that could block your listing or hosting plans later.',
                             'example': 'Cloudflare Registrar lists .com at $11.17 to register, renew, or '
                                        "transfer, 64 cents under Porkbun's $11.81 [Design Guy — "
                                        'mMGvtO-bkPI @ 00:00:59]. But new Cloudflare registrations are '
                                        'non-refundable and nameservers cannot be changed [David Utke — '
                                        'UkMYRY9wDN0 @ 00:13:15], so flip inventory goes to Spaceship at '
                                        '$8.88, renewing at $9.98, with WHOIS protection included.'},
                            {'name': 'privacy_and_separation',
                             'type': 'text',
                             'prompt': 'State your two non-negotiables for registrar selection: how you '
                                       'handle WHOIS privacy charges and whether domains and hosting live '
                                       'at the same company. Explain the cost and safety reasoning behind '
                                       'each rule in your own words.',
                             'example': 'Any registrar that charges for WHOIS privacy is dropped, a rule '
                                        'David Utke calls non-negotiable and Luka Knows calls a complete '
                                        'red flag [David Utke — UkMYRY9wDN0 @ 00:04:17]. Domains and '
                                        'hosting stay at separate companies because that setup is cheaper '
                                        'and safer [Luka Knows — oi-pZAGrrhQ @ 00:05:37], which also '
                                        'guards against one-cent bait that quietly becomes a $40 charge.'},
                            {'name': 'dns_cutover_checklist',
                             'type': 'textarea',
                             'prompt': 'Write your DNS cutover checklist for moving a name onto '
                                       "Cloudflare's free DNS layer. Include the DNSSEC step, the records "
                                       'you review after the import, how you treat email and verification '
                                       'records, and your propagation waiting window.',
                             'example': 'Step one: turn DNSSEC off at the current registrar before pasting '
                                        "Cloudflare's two nameservers, then allow up to 48 hours [PMN "
                                        'Online — AKtcv_vFlSY @ 00:01:13]. Step two: review the root A '
                                        'record and the www CNAME. Step three: set MX and TXT records to '
                                        'the gray DNS-only cloud, or email breaks [Easytorial — '
                                        'sx83eEm6nk4 @ 00:03:23].'},
                            {'name': 'listing_and_renewal_plan',
                             'type': 'textarea',
                             'prompt': 'Describe how each finished name gets listed and how you protect it '
                                       'at renewal time. Note the marketplace and nameserver setup, the '
                                       'commission you expect, your auto-renew setting for keepers, and '
                                       'the date you review dead weight.',
                             'example': 'Namecheap-registered names point their nameservers to Afternic, '
                                        'cutting commission from 25% to 15% and unlocking fast transfer '
                                        'plus a for-sale lander [David Utke — A6-lVEeaHEs @ 00:10:27]. '
                                        'Auto-renew is switched on for every keeper, and unsold dead '
                                        'weight is dropped before the bill arrives [Andrey Verevko — '
                                        'bVQnMN-Qrd8 @ 00:09:05], avoiding the forgotten-renewal trap '
                                        'Verevko describes.'}],
                 'completion_gate': 'Complete only when every candidate has passed the dash, misspelling, '
                                    'and date screen; the list price is backed by an appraisal plus '
                                    'NameBio comps; the registrar offers free WHOIS privacy and a known '
                                    'renewal price; DNSSEC, MX, and TXT handling is documented; and '
                                    'auto-renew or a drop date is set for every name held.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Expired Domain Hunt and Aged-Domain Due Diligence Log',
                 'purpose': 'Run every expired or aged target through the same clock and the same evidence '
                            'trail: map the drop cycle, filter the raw list, pick the cheapest acquisition '
                            'route, arm alerts, fix a hidden bid ceiling, then audit referring domains, '
                            'live links, cross-tool counts, and archive history before any money moves.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Start with the drop clock and confirm the date on the WHOIS status tab '
                                  'before planning any bid or backorder.',
                                  'Apply filters to the raw expiring list first and record the remaining '
                                  'count, treating unfiltered inventory as mostly trash.',
                                  'Write the maximum bid before the auction opens and never raise it after '
                                  'bidding starts.',
                                  'Judge backlinks at page level and history level; never let a domain '
                                  'score alone approve a purchase.',
                                  'Log any site you cannot reach as unverified, and walk away whenever the '
                                  'archive shows redirects or spam in the final year.'],
                 'fields': [{'name': 'drop_cycle_map',
                             'type': 'textarea',
                             'prompt': 'Map the expiry clock for one target name. Write the day its '
                                       'auction opens, the Closeout window, registry release, and expected '
                                       'public drop, then confirm the drop date from a WHOIS status check '
                                       'before planning any bid or backorder.',
                             'example': 'GoDaddy cycle: a 10-day auction from day 26, a 5-day declining '
                                        'Closeout from day 36, registry release on day 43, and a public '
                                        'drop around day 75 to 80. The drop date is confirmed on the '
                                        'freewhois.com Status tab, and no drop backorder goes in less than '
                                        '2 hours before the drop [GoDaddy — OM_5VESPepY @ 00:22:17].'},
                            {'name': 'list_filters',
                             'type': 'textarea',
                             'prompt': 'Record the exact filter settings you apply to the raw expiring '
                                       'list before reading a single name. Include extension, language, '
                                       'character rules, and any minimum authority or trust metrics, plus '
                                       'the count of names left after filtering.',
                             'example': 'The unfiltered GoDaddy list on expireddomains.net usually runs '
                                        'over 400,000 names a week [ReviewUP — LqUB5Dr0vrE @ 00:00:14]. '
                                        'Filters strip numbers and hyphens and lock English .com. For SEO '
                                        'targets, the DomCop minimums are page rank two, domain authority '
                                        '30, and Majestic trust flow 15 [DomCop — r5xkDG4-mvo @ 00:00:42], '
                                        'since Jamie Lewis calls expired lists 99% trash.'},
                            {'name': 'acquisition_route',
                             'type': 'textarea',
                             'prompt': 'Choose the acquisition route for this name: live auction, Closeout '
                                       'buy-now, registrar backorder, or drop-catch service. Write the fee '
                                       'or opening price for that route, what happens if the catch fails, '
                                       'and why this route beats the alternatives.',
                             'example': 'A GoDaddy backorder credit costs just under $21, bundling a $10 '
                                        'opening bid and a .com registration worth about $15 [GoDaddy — '
                                        'OM_5VESPepY @ 00:15:23]. The Closeout buy-now starts at $11, '
                                        'drops $1 a day, then hits $5 on the final day [GoDaddy — '
                                        '0f-o9p0h6u8 @ 00:09:23]. SnapNames runs about 79 per domain, with '
                                        'refund or rollover on a failed catch.'},
                            {'name': 'alerts_watchlist',
                             'type': 'text',
                             'prompt': 'List every alert and watch-list setting you have switched on for '
                                       'your target names. Note which events trigger a notification, where '
                                       'you confirmed the setting saved, and what action each alert type '
                                       'tells you to take next.',
                             'example': 'Alerts are set for auction start, registrant changes, and '
                                        'nameserver changes, since a nameserver change can signal a seller '
                                        'newly open to offers [GoDaddy — OM_5VESPepY @ 00:11:46]. Auction '
                                        'alerts run through Domains, Auctions for domains, Settings, with '
                                        'the save and phone number double-checked [Tutorialjake — '
                                        'P82q-S2X978 @ 00:01:54]. Contested names sit on the watch list '
                                        'instead of drawing early bids.'},
                            {'name': 'bid_ceiling',
                             'type': 'text',
                             'prompt': 'Fix your maximum price for this name before the auction opens. '
                                       'Write the number, the evidence behind it, whether you will use a '
                                       'proxy bid or a last-moment backorder, and how you keep the ceiling '
                                       'hidden from rival bidders.',
                             'example': 'GoDaddy staff favor proxy bids, noting a $7,000 proxy against '
                                        'bids of $10 and $15 only bids up to $20 [GoDaddy — OM_5VESPepY @ '
                                        '00:24:01]. Affiliate Credo refuses any visible maximum or '
                                        'auto-bid and skips obviously great names without a $5,000 budget '
                                        '[Affiliate Credo — 9vU7vtxcYuc @ 00:07:48]. This ceiling: $60, '
                                        'placed late through a watch-list backorder.'},
                            {'name': 'referring_domain_trend',
                             'type': 'textarea',
                             'prompt': 'Read the referring-domain history for this name in your backlink '
                                       'tool and describe its shape. Note the starting and ending counts, '
                                       'the time span, any traffic spike or crash, and whether the domain '
                                       'rating alone would have misled you.',
                             'example': 'Frey Chu passed on DR59 magpress.com after its referring domains '
                                        'doubled from 1,900 to 4,000 in roughly nine to ten months, '
                                        'followed by a traffic spike and crash [Frey Chu — mHkLfhpVYqc @ '
                                        '00:09:08]. His best links carried zero traffic. Any profile '
                                        'showing that doubling-then-crash pattern is passed regardless of '
                                        'DR [Frey Chu — mHkLfhpVYqc @ 00:09:24].'},
                            {'name': 'link_quality_audit',
                             'type': 'textarea',
                             'prompt': 'Audit the backlinks themselves rather than the domain score. '
                                       'Record anchor types, country mix, page-level traffic, follow '
                                       'status from sampled pages, and how many links you could actually '
                                       'verify live versus those you logged as unverified.',
                             'example': 'SearchGAPMethod found 44 of 49 free-list entries passed DR, but '
                                        'only 15 passed six live checks, a 31% rate [SearchGAPMethod — '
                                        'UXycltw74Bw @ 00:05:05]. Each 403 is opened in a real browser and '
                                        'logged as unverified, never dead or passed. The Ahrefs or Moz '
                                        'review rejects keyword anchors and foreign links off the target '
                                        'country [Ecommerce FM — N8NOW92hCY4 @ 00:13:31].'},
                            {'name': 'tool_crosscheck',
                             'type': 'text',
                             'prompt': 'Run the same domain through at least two backlink checkers and '
                                       "record each tool's total. Write the spread between the lowest and "
                                       'highest count, the toxicity or spam score shown, and which source '
                                       'you treat as final authority.',
                             'example': 'Edvido ran one site through 11 free checkers and got 14.9K '
                                        'backlinks at SE Ranking versus 65.62K at SEO Review Tools, '
                                        'roughly a 4x spread, with Majestic near 21.8K and Ahrefs at 35K '
                                        '[Edvido — XjoQwN4FcDU @ 00:01:32]. When third-party tools and '
                                        'Google disagree, Google wins [Edvido — XjoQwN4FcDU @ 00:08:19], '
                                        'so Search Console data settles ties.'},
                            {'name': 'wayback_review',
                             'type': 'textarea',
                             'prompt': 'Review the archive history from the earliest snapshot to the final '
                                       'months before the drop. Record whether an archive index exists, '
                                       'any redirects and their type, gaps containing green redirect days, '
                                       'and any casino, pharma, or spam content.',
                             'example': '302 redirects are ignored as temporary, but a 301 held during the '
                                        'final year is a skip [Affiliate Credo — S8e33kDoWhQ @ 00:04:00]. '
                                        'No archive index or spam content in the last months is fatal '
                                        '[Affiliate Credo — S8e33kDoWhQ @ 00:03:54]. Green redirect days '
                                        'inside a scan gap pointing to a third-party site mean walk away '
                                        '[Shawna Newman (Skipblast) — wkwOl5VePMM @ 00:02:11].'},
                            {'name': 'rebuild_and_compliance',
                             'type': 'textarea',
                             'prompt': 'Decide how you will use the domain after purchase and check that '
                                       'plan against compliance risk. Note whether you will restore '
                                       'archived content, rebuild on-topic, or redirect, how you screen '
                                       'for duplicates, and the policy concern you weighed.',
                             'example': 'A 301 redirect is fast but spammy if overdone, so the plan is an '
                                        'on-topic rebuild linking back with brand mentions [Ecommerce FM — '
                                        'N8NOW92hCY4 @ 00:08:42]. Archived phrases are checked in quotes '
                                        'on Google or through Copyscape first [Affiliate Credo — '
                                        'S8e33kDoWhQ @ 00:03:18]. SERPSUPPORT warns that rebuilding purely '
                                        "for links breaks Google's expired domain abuse policy, so the "
                                        'rebuild stays on-topic.'}],
                 'completion_gate': 'Complete only when the drop date is confirmed on the WHOIS status '
                                    'tab, a hidden maximum bid is written down, the backlink profile shows '
                                    'no keyword anchors, off-target foreign links, or referring-domain '
                                    'spike, every unreachable site is logged as unverified, and the '
                                    'archive shows an index with no final-year 301, redirect gaps, or spam '
                                    'content.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Exact-Match Valuation and Portfolio Pricing Room',
                 'purpose': 'Value generic exact-match and one-word names on evidence instead of automated '
                            'appraisals: measure exact-phrase demand, convert clicks into money, build the '
                            "end user's business case, price through three frames, cap buys by liquidity, "
                            'set asks on realistic sell-through, test repricing, and lock lease and '
                            'trademark terms in writing.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Use exact-match search volume and real advertiser cost per click; '
                                  'ignore broad and phrase match numbers entirely.',
                                  'Name at least one identifiable end user for whom the domain is an '
                                  'obvious upgrade before assigning any value.',
                                  "Treat online appraisals as a buyer's talking point to answer with "
                                  'comps, never as your own pricing anchor.',
                                  'Write the acquisition ceiling as a percentage of expected resale before '
                                  'negotiating, based on whether the name is liquid or illiquid.',
                                  'Put down payments, default penalties, and trademark bid caps in writing '
                                  'before offering any lease-to-own deal.'],
                 'fields': [{'name': 'exact_match_demand',
                             'type': 'textarea',
                             'prompt': 'Measure demand for the exact phrase this domain matches. Record '
                                       'the monthly exact-match search volume, the cost per click, whether '
                                       'the intent is booking or research, and what the live Google '
                                       'results show beyond any keyword-difficulty score.',
                             'example': "Andrew Rosener's floor for traffic-based value is more than 1,000 "
                                        'exact-match searches a month; some buyers accept 200 to 300 '
                                        '[domainsherpa — HfWOYwPZ1HU @ 00:11:38]. Broad and phrase match '
                                        'carry zero use for this purpose [domainsherpa — HfWOYwPZ1HU @ '
                                        '00:07:40]. The live results are read directly and booking intent '
                                        'confirmed [Launch with Bryan — ASaM7hIMKVI @ 00:03:28].'},
                            {'name': 'click_value_model',
                             'type': 'textarea',
                             'prompt': 'Convert search volume into estimated visits and value. Write the '
                                       'click-capture rate you assign to the top organic spot, the CPC you '
                                       'use and how you sourced it, and the yearly traffic value that '
                                       'results from your calculation.',
                             'example': 'Rosener assigns 75 to 90% of clicks, roughly 85%, to the number '
                                        'one organic spot, with sponsored links getting far fewer '
                                        '[domainsherpa — HfWOYwPZ1HU @ 00:13:01]. The CPC comes from '
                                        'advertisers paying for the keyword, never a placeholder, because '
                                        'assigning a one dollar CPC is silly [domainsherpa — J6_UP-VNOco @ '
                                        '00:56:33]. The finish is the cost per click [domainsherpa — '
                                        'KYAHTsYNIPI @ 00:21:06].'},
                            {'name': 'emd_leverage_case',
                             'type': 'textarea',
                             'prompt': 'Write the business case an end user would make for owning this '
                                       'exact-match name. Cover trust and click-through advantages, any '
                                       'spend leverage claimed by owners of similar names, and where SEO '
                                       'practitioners say rankings really come from.',
                             'example': 'Michael Gargiulo claims a dollar of vpn.com spend equals ten '
                                        'dollars for a non-exact-match brand, alongside 3 to 5x '
                                        "competitors' click-through rate [domainsherpa — J6_UP-VNOco @ "
                                        '00:14:45]. SEO operators still credit content, links, and reviews '
                                        'with ranking, and PPC Better says EMDs lost their SEO benefit in '
                                        '2012, so the pitch leans on consumer trust, not algorithm '
                                        'favoritism.'},
                            {'name': 'three_frame_price',
                             'type': 'textarea',
                             'prompt': 'Price this name through three frames instead of anchoring on a '
                                       'single comparable sale. Write the likely buyer type, the raw, '
                                       'brand, or perceived equity the name carries, and where its '
                                       'industry trend currently sits in its phase.',
                             'example': 'Chris Zuiker prices through buyer type, raw/brand/perceived '
                                        "equity, and the industry trend's phase rather than one comp "
                                        '[Chris Zuiker - Domain Name Broker — veILle9et0o @ 00:00:58]. '
                                        'Rosener treats $25K as table stakes for payments, crypto, and AI '
                                        'names. Zuiker also warns passing on a top offer means waiting '
                                        'years [Chris Zuiker - Domain Name Broker — veILle9et0o @ '
                                        '00:02:37].'},
                            {'name': 'buy_ceiling_liquidity',
                             'type': 'text',
                             'prompt': 'Classify this name as liquid or illiquid and set your acquisition '
                                       'ceiling as a share of expected resale. Write the expected resale '
                                       'figure, the percentage you will pay, and how many active bidders '
                                       'or buyers you can identify today.',
                             'example': 'Rosener pays no more than 10% of expected resale for illiquid '
                                        'names and 30 to 50% for liquid ones, so Diagnose.com, worth about '
                                        '$100K to $150K retail, draws a bid near $30K to $35K '
                                        '[domainsherpa — KZqosumnXfg @ 01:09:57]. Names with 2 to 3 active '
                                        'bidders imply liquidity within 10 to 20% of cost [domainsherpa — '
                                        'KYAHTsYNIPI @ 00:39:42].'},
                            {'name': 'end_user_pool',
                             'type': 'textarea',
                             'prompt': 'Identify the end-user pool for this name. Count the potential '
                                       'buyers, the advertisers already paying for the keyword, and the '
                                       'registrations of the same term across other extensions, then '
                                       'explain who gets an obvious upgrade by owning it.',
                             'example': 'Adam Dicker counts potential buyers and paying advertisers, and '
                                        'Andrew Allemann bulk-checks DotDB for registrations across TLDs '
                                        'and live companies. The standard is an obvious end user for whom '
                                        'this is an upgrade, or a strategic acquisition with significant '
                                        'proof [domainsherpa — OzWsYhxMiCE @ 01:42:37]. Names without that '
                                        'buyer get cut, however clever.'},
                            {'name': 'appraisal_vs_comps',
                             'type': 'text',
                             'prompt': 'Compare any automated appraisal on this name against real '
                                       'comparable sales and buyer evidence. Write the appraisal figure, '
                                       'the comps you found, the gap between them, and how you would '
                                       'answer a buyer who quotes a low appraisal.',
                             'example': 'On BainbridgeBuilders.com, Michael Cyger countered a $1,655 '
                                        'GoDaddy valuation with NameBio comps, cut $200 so the buyer felt '
                                        'they won, and closed on Dan.com at a 5% fee [domainsherpa — '
                                        'R695oEH1bvA @ 00:13:08]. appraise.net figures are quoted '
                                        'constantly in valuation reviews, yet Adam Dicker puts zero value '
                                        'on online appraisals, so comps lead every reply.'},
                            {'name': 'ask_price_rule',
                             'type': 'textarea',
                             'prompt': 'Set the asking price for each name you hold using an explicit '
                                       'sell-through assumption. Write the share of your portfolio you '
                                       'expect to sell over its life, the multiplier that implies, and the '
                                       'resulting ask for your best name.',
                             'example': "About 10% of a portfolio sells in an investor's lifetime, so asks "
                                        'carry roughly 10x; Rosener applied that rule to set about a $250K '
                                        'ask on Timeless.com [domainsherpa — cb-n0okmiuw @ 00:17:23]. The '
                                        'mindset matches the panel line that the highest price comes from '
                                        'wanting not to sell your names [domainsherpa — R695oEH1bvA @ '
                                        '00:40:35].'},
                            {'name': 'repricing_test',
                             'type': 'textarea',
                             'prompt': 'Plan a repricing test on names that have drawn recent inquiries. '
                                       'List which names move up, which move down, the size of each '
                                       'change, the inquiry window that qualifies a name, and how long you '
                                       'wait before judging results.',
                             'example': 'About 50 names that had Afternic inquiries or offers in the prior '
                                        '60 to 90 days were repriced: most rose 10 to 15%, and 15 to 20 '
                                        'were lowered. In under a month, one lowered-price name sold '
                                        'against three raised-price names [domainsherpa — DLZJeUWhf3I @ '
                                        '00:52:42]. Timing is more important than price [domainsherpa — '
                                        'sekhN8zuNlU @ 00:59:52].'},
                            {'name': 'lease_and_risk_terms',
                             'type': 'textarea',
                             'prompt': 'Write the deal terms you will offer for lease-to-own and '
                                       'trademark-exposed names. Include the down payment percentage, the '
                                       'default penalty written into the contract, and the bid ceiling you '
                                       'apply to any name carrying trademark takedown risk.',
                             'example': 'Shane Cultra now requires 20 to 30% down on every Atom '
                                        'lease-to-own after a meme-coin buyer defaulted [domainsherpa — '
                                        'OzWsYhxMiCE @ 00:41:29]. Drew Rosener charges two extra monthly '
                                        'payments on default after waiving the penalty once [domainsherpa '
                                        '— CKvIo_PJEQI @ 00:36:11]. Trademark-exposed bids cap at takedown '
                                        'cost, like $2,500 on WordPresstutorials.com [domainsherpa — '
                                        '4a5oAIneDaA @ 00:44:22].'}],
                 'completion_gate': 'Complete only when exact-match volume and real advertiser CPC are '
                                    'recorded, at least one obvious end user is named, any appraisal has '
                                    'been answered with comps, the buy ceiling is set as a percentage of '
                                    'resale by liquidity class, and every lease-to-own offer carries a '
                                    'written down payment, default penalty, and trademark bid cap.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Outbound Pitches, Broker Terms, and Marketplace Listings',
                 'purpose': 'Turn the outbound and marketplace playbooks into a working sales sheet: '
                            'identify obvious end users, script first contact and follow-ups, decide on '
                            'brokers, and set Afternic, Sedo, Atom, and Dan listings with commission math, '
                            'Buy Now prices, and fast-transfer eligibility checked before launch.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Pick one domain from the current portfolio and complete every field for '
                                  'that single name before moving to the next.',
                                  'Write the end-user identification fields first, because brokers and '
                                  'outbound sellers both screen for an obvious buyer before pitching.',
                                  'Record commission rates for every venue in percent and compute net '
                                  'proceeds before setting any Buy Now price.',
                                  'Cite the operator benchmark you are measuring against in each answer '
                                  'using the channel, video ID, and timestamp format.',
                                  'Revisit the pricing and follow-up fields after two months if the name '
                                  'has drawn no inquiries or sales.'],
                 'fields': [{'name': 'obvious_end_user_test',
                             'type': 'textarea',
                             'prompt': 'Name the single most obvious end-user business for one domain you '
                                       'plan to pitch, and write the one sentence you would say to its CEO '
                                       'explaining why the name matters to their revenue. If you cannot '
                                       'write it with conviction, record the pass decision.',
                             'example': 'SawSells frames the screen bluntly: if you cannot tell a CEO with '
                                        'conviction that they need the name for their business, pass on it '
                                        '[SawSells — EA8QZJvkKP4 @ 00:00:18]. Chris Zuiker adds that you '
                                        'have to understand who your buyer is [Chris Zuiker - Domain Name '
                                        'Broker — DBqMibOXGo8 @ 00:03:38], so the entry lists one named '
                                        'company and one sentence.'},
                            {'name': 'prospect_list_sources',
                             'type': 'textarea',
                             'prompt': 'List every source you will mine for prospective buyers of this '
                                       'name, how many search result pages you will work through, and '
                                       'which contact doors you will try for each owner, including email, '
                                       'WHOIS, and social channels.',
                             'example': 'Yogi Solanki mines Google pages 1 to 20 for end users. Reach '
                                        'owners through every door: info@, a scraped owner email, WHOIS, a '
                                        'Facebook DM with an image, and a comment tagging their pinned '
                                        'post [kickstartcommerce — gQJxEyrhqec @ 01:02:16]. Log each '
                                        'prospect with the door used and the date of first contact.'},
                            {'name': 'first_email_draft',
                             'type': 'textarea',
                             'prompt': 'Draft the first outreach email for this name, keeping the price '
                                       'out of the opening message, and note the subject line you will '
                                       'use. Explain how the draft avoids the one sentence that could kill '
                                       'the deal before a reply arrives.',
                             'example': 'Yogi Solanki withholds price in the first email. A domainsherpa '
                                        'guest warns that one sentence may not sell a domain but one '
                                        'sentence can certainly kill a domain [domainsherpa — 3C8uYmkV_aE '
                                        "@ 00:35:23]. The draft names the buyer's business, states the "
                                        'domain is available, invites a reply, and leaves every number out '
                                        'until they ask.'},
                            {'name': 'follow_up_cadence',
                             'type': 'text',
                             'prompt': 'Set the follow-up schedule for recipients who open the first '
                                       'email: the day interval, the maximum number of follow-ups, and the '
                                       'date you will relist and re-pitch the name if the sequence ends '
                                       'without a sale.',
                             'example': 'Follow up every third day, no more than three times, and only '
                                        'with recipients who opened the first email [kickstartcommerce — '
                                        'gQJxEyrhqec @ 00:38:36]. After the third touch, list the name '
                                        'everywhere and re-pitch after about three months. Yogi Solanki '
                                        'also warns that sending a thousand emails a day will not sell a '
                                        'domain.'},
                            {'name': 'price_question_response',
                             'type': 'textarea',
                             'prompt': 'Write your response for when a prospect replies asking how much. '
                                       'State whether you will quote a figure or ask the buyer to name a '
                                       'range first, and record the reasoning behind that choice for this '
                                       'particular name.',
                             'example': 'Jason Eisler reports about 80% of outbound replies are simply how '
                                        'much, so let the buyer raise price first and never negotiate '
                                        'against yourself [kickstartcommerce — gQJxEyrhqec @ 01:06:01]. '
                                        'Chris Zuiker takes the opposite line and gives a price when '
                                        "asked. Rosener wants the buyer's range up front without jumping "
                                        'straight to its top.'},
                            {'name': 'objection_and_discount_rules',
                             'type': 'textarea',
                             'prompt': 'Define how you will handle repeated no replies and discount '
                                       'requests on this name: how many refusals you will absorb, the '
                                       'diagnostic question you will ask, and the maximum discount you '
                                       'will grant and under what closing condition.',
                             'example': 'Ignore the first three or four no replies, then ask whether the '
                                        'objection is the domain, the price or the timing '
                                        '[kickstartcommerce — 5UOGADHB0l0 @ 00:51:15]. Hold the integrity '
                                        'line: no fake offers, and give 10% off only if it closes, never '
                                        '20%. Alex Verdea likewise caps discounts at 10% and offers '
                                        'installments instead.'},
                            {'name': 'broker_decision',
                             'type': 'textarea',
                             'prompt': 'Decide whether this name goes to a broker or stays in your own '
                                       'outbound pipeline. Record the commission you would pay, whether '
                                       'the broker requires an exclusive contract, and how a broker sale '
                                       'changes your net proceeds.',
                             'example': "MarkUpgrade's broker guidance is to refuse brokers who skip an "
                                        'exclusive contract or compete on rock-bottom commission, because '
                                        'if you pay peanuts you get monkeys [MarkUpgrade — 8mDbRg8x4DA @ '
                                        '00:57:38]. Brooks Conkle notes a $1,000 sale could carry a $300 '
                                        'commission. Chandler Bolt tells buyers never to hire brokers that '
                                        "GoDaddy's Joe recommends."},
                            {'name': 'venue_commission_math',
                             'type': 'textarea',
                             'prompt': 'Compare net proceeds for this name across Afternic, Sedo, Atom, '
                                       'and Dan at your target price. Show each commission rate, any '
                                       'nameserver condition that changes it, and the markup you will '
                                       'apply on higher-fee venues to protect your net.',
                             'example': 'Afternic drops from the standard 25% to 15% on Afternic '
                                        'nameservers [Web Whizz — UPcwro2bxDg @ 00:04:02], while Atom '
                                        'charges 7.5% standard and 15% Plus. Reza Taheri prices up to 20% '
                                        'higher on Afternic to cover its fee. Dan runs about 9% versus '
                                        "GoDaddy's 20% on Yogi Solanki's outbound closes. Write the net "
                                        'figure beside each venue.'},
                            {'name': 'buy_now_and_fast_transfer',
                             'type': 'textarea',
                             'prompt': 'Set the Buy Now price for this name and confirm fast-transfer '
                                       'eligibility line by line: expiry date, transfer lock status, and '
                                       'whether the price sits inside the allowed range. Note the research '
                                       'you used to keep the price from deterring buyers.',
                             'example': 'Fast transfer requires no expiry within 30 days, no 60-day lock, '
                                        'and a BIN between $50 and $25,000 [GoDaddy — PPJ8y-pwY38 @ '
                                        '00:12:51]. Sedo reports Buy Now listings sell three times more '
                                        'often than make-offer listings, but warns that a Buy Now price '
                                        'set too high just puts off potential buyers. Over 60% of priced '
                                        'sub-$10,000 Afternic sales close within 48 hours.'},
                            {'name': 'lander_and_reprice_trigger',
                             'type': 'textarea',
                             'prompt': 'Describe the for-sale lander this name will use and the condition '
                                       'that triggers a price review. Include whether the lander shows a '
                                       'price or a request-price form, and the number of months without '
                                       'inquiries before you reprice.',
                             'example': 'Jazzy Domainz avoids the default request-price page because it '
                                        'adds one more step in the way of a sale and uses a custom lander '
                                        'instead [Jazzy Domainz — 7r4PuUv52Pw @ 00:04:44]. On a freshly '
                                        'acquired portfolio, review pricing after two months with no '
                                        'inquiries or sales; seasoned sellers give tweaks a '
                                        'three-to-four-month window.'}],
                 'completion_gate': 'Complete only when the name has a named end user with a conviction '
                                    'sentence, a first email without a price, a cadence of no more than '
                                    'three follow-ups, a written 10% discount ceiling, net proceeds '
                                    'calculated for every venue, and fast-transfer eligibility confirmed.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Escrow Closings, Lease-to-Own Terms, and Parking Economics',
                 'purpose': 'Build a closing and monetization sheet: run every sale through verified '
                            'escrow, structure lease-to-own and holding terms with cure periods and '
                            'penalties, screen scam signals, and decide whether each idle name earns its '
                            'renewal through parking or should be rotated or sold.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Complete the closing fields before accepting any offer, so the escrow '
                                  'route and transfer conditions are settled in advance.',
                                  'Write lease-to-own terms in full, including down payment, cure period, '
                                  'default penalty, and content restrictions, before any DNS change.',
                                  'Treat any request for the seller to pay first as a scam signal and stop '
                                  'the deal on that field.',
                                  'Fill the parking fields with monthly revenue per name and compare each '
                                  "figure against that name's renewal cost.",
                                  'Cite the operator benchmark behind every decision using the channel, '
                                  'video ID, and timestamp format.'],
                 'fields': [{'name': 'escrow_route',
                             'type': 'textarea',
                             'prompt': 'Name the escrow service for this sale, who funds it, and the exact '
                                       'step at which you will begin the transfer. Note the deal size at '
                                       'which you will add a separate paper contract beyond the escrow '
                                       "platform's standard terms.",
                             'example': "Do not start the transfer until escrow confirms the buyer's funds "
                                        'as verified [Domains No Broker — FSQ0uJ1Ul9Q @ 00:00:36]. Name '
                                        'Experts say the escrow.com terms are enough on smaller deals, but '
                                        'above six digits a paper contract is used. Brian Tharp puts the '
                                        'Escrow.com fee as low as 0.89% with no chargeback exposure.'},
                            {'name': 'scam_signal_screen',
                             'type': 'textarea',
                             'prompt': 'List every request in this negotiation that would require you to '
                                       'pay money before the buyer does, such as appraisals, refunds, or '
                                       'renewal invoices. Record the reply you will send and the '
                                       'verification step you will run yourself.',
                             'example': 'Kill any deal where the seller pays first; money flowing the '
                                        'wrong way is the universal scam signal [Domain Value Estimator — '
                                        'zNcj1gwZsso @ 00:04:43]. When a buyer demands a paid appraisal, '
                                        'reply: order the appraisal yourself and pay for it and send me '
                                        'the escrow transaction number and I will verify it at escrow.com '
                                        'myself.'},
                            {'name': 'transfer_deadline_clause',
                             'type': 'text',
                             'prompt': 'Write the cancellation-and-refund clause for this deal, including '
                                       'the number of days the transfer may take before the buyer can '
                                       'cancel, and note how you will budget cash flow if a marketplace '
                                       'transfer sits pending longer than quoted.',
                             'example': 'Make Money Anthony writes a cancellation-and-refund clause into '
                                        'the terms if the transfer does not happen within about 7 days '
                                        '[Make Money Anthony — -3yBZKLuJnU @ 00:02:37], after having '
                                        '$3,600 frozen for a month when a seller went silent. Reza Taheri '
                                        'waited 12 days on an Afternic transfer quoted at five to seven '
                                        'business days.'},
                            {'name': 'lease_to_own_structure',
                             'type': 'textarea',
                             'prompt': 'Set the lease-to-own structure for this particular domain name: '
                                       'platform, term length in months, any discount tied to the term, '
                                       'the down payment percentage, and whether the buyer may exercise '
                                       'the purchase early with remaining payments forgiven.',
                             'example': "Afternic's 14-month custom term carries a 5% discount [GoDaddy "
                                        'Domain Academy — Osg5qiW8qYI @ 00:01:24], and Dan runs plans from '
                                        '2 to 60 months. Shane now takes 20 to 30% down on every Atom deal '
                                        'after a meme-coin buyer defaulted. Tharp writes the purchase '
                                        'option so the lessee can exercise early with remaining payments '
                                        'forgiven.'},
                            {'name': 'default_and_cure_terms',
                             'type': 'textarea',
                             'prompt': 'Define what happens when a lessee misses a payment on this name: '
                                       'the cure period in business days, any late fee, and the default '
                                       'penalty written into the agreement. Explain why you chose each '
                                       'figure against the reported default data.',
                             'example': "Escrow.com's default cure period is 5 business days, adjustable "
                                        'to windows such as 15 days or paired with late fees '
                                        '[kickstartcommerce — IJ9lx010Yps @ 00:24:58]. Drew now charges '
                                        'two monthly payments on top after waiving a penalty once and '
                                        'regretting it. DNH reports about a 3.6% default rate across '
                                        'roughly 3,000 deals.'},
                            {'name': 'content_bans_and_outside_agreement',
                             'type': 'textarea',
                             'prompt': 'List the content restrictions a lessee must accept before any DNS '
                                       'change goes live on this leased name, and describe in full the '
                                       'outside agreement that will carry terms the escrow platform cannot '
                                       'enforce on its own.',
                             'example': 'Agree content bans and the cure period in the holding agreement '
                                        'before any DNS changes are made, because Escrow.com cannot '
                                        'enforce terms that were never written in [kickstartcommerce — '
                                        "IJ9lx010Yps @ 00:17:24]. Tharp's broader rule is to always use an "
                                        'outside agreement. Adam Dicker adds that a lease without an '
                                        'option to buy is even better.'},
                            {'name': 'lowball_offer_log',
                             'type': 'textarea',
                             'prompt': 'Log every offer received on this name, including lowballs, with '
                                       'date, amount, and contact. Write the monthly lease counteroffer '
                                       'you will send to each lowball bidder and the date you will reach '
                                       'back out if they stay silent.',
                             'example': 'Adam Dicker logs every offer, including lowballs, and counters '
                                        'with a $500 to $1,000 per month lease, noting that buyers come '
                                        'back even after four or more years [Adam Dicker — DnnSbpJm2ZI @ '
                                        '00:13:33]. Efty adds that lease-to-own can significantly increase '
                                        'your sale through rate, so the counter keeps the conversation '
                                        'open instead of ending it.'},
                            {'name': 'parking_setup',
                             'type': 'textarea',
                             'prompt': 'Record the parking service, the pointing method, and the DNS '
                                       'configuration for this name. Confirm the nameserver setting '
                                       'matches what the chosen service requires, and note how you will '
                                       'verify ownership without waiting on a manual review.',
                             'example': 'Point the domain to the Bodis name servers at your registrar and '
                                        'the park page shows within 24 hours [DomCop — im4LjoyOxPE @ '
                                        '00:02:35]. Namecheap parking requires BasicDNS, and custom name '
                                        "servers break the park page. Utke skips Sedo's multi-day manual "
                                        'review by adding a TXT record on host @ holding a private ID.'},
                            {'name': 'parking_revenue_vs_renewal',
                             'type': 'textarea',
                             'prompt': 'Enter the monthly parking revenue for this name, its normalized '
                                       'RPM, and its annual renewal cost. State whether the name clears '
                                       'the per-domain monthly target, and whether you will keep parking '
                                       'it, rotate services, or sell it.',
                             'example': 'Utke sets a $5 monthly floor per domain, so 100 names at $5 '
                                        'yields $500 a month; otherwise rotate the service or sell the '
                                        'name [David Utke — ck1VMki_11Q @ 00:02:24]. Gilmour judges '
                                        'performance only on normalized RPM, revenue divided by raw '
                                        'traffic times 1,000, and notes the best single provider wins just '
                                        '25% of traffic.'},
                            {'name': 'parking_traffic_integrity',
                             'type': 'textarea',
                             'prompt': 'Confirm the traffic sources reaching this parked name and the '
                                       'safeguards you keep in place. State whether any traffic is pushed, '
                                       'redirected, or purchased, and how you prevent clicks from your own '
                                       'devices and IP addresses.',
                             'example': 'Keep traffic organic type-in only; pushed, redirected or '
                                        'purchased arbitrage traffic risks a DRID ban at Google and '
                                        'clawbacks [HostMaria — SE1nkvW6rGw @ 01:45:24]. Domain Notebook '
                                        'warns the owning IP is tracked and blocked after the first '
                                        'self-click. USENIX researchers classified about 45% of parking '
                                        'traffic as click fraud, so audit sources before each payout.'}],
                 'completion_gate': 'Complete only when escrow verification precedes transfer, every '
                                    'seller-pays-first request is rejected in writing, lease terms carry a '
                                    'down payment, cure period, and default penalty, and every parked name '
                                    'either clears the $5 monthly target against renewal or is marked for '
                                    'rotation or sale.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Trademark Defense, Extension Bets, and Portfolio Capital Plan',
                 'purpose': 'Protect and fund the portfolio: clear trademark exposure before buying, '
                            'prepare a response plan for UDRP complaints, weigh extension bets against '
                            '.com, and model sell-through, renewal ceilings, lease income, and bad-year '
                            'losses before committing more capital to new acquisitions.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Run the trademark fields on every new candidate before it reaches the '
                                  'cart, and record the databases you checked.',
                                  'Complete the dispute response field now, while no complaint is pending, '
                                  'so a filing never goes unanswered.',
                                  "Use the portfolio's actual name count, renewal totals, and sales "
                                  'history when completing the capital fields.',
                                  'Model the bad year before the good year, including a dispute cost, and '
                                  'keep both scenarios on the sheet.',
                                  'Cite the operator benchmark behind each figure using the channel, video '
                                  'ID, and timestamp format.'],
                 'fields': [{'name': 'trademark_clearance_stack',
                             'type': 'textarea',
                             'prompt': 'Record the trademark checks run on this candidate name: each '
                                       'database searched, the date, and any match found. State whether '
                                       'the term is tied to one major company and whether you will buy, '
                                       'skip, or cap the bid.',
                             'example': 'Stack three checks before buying any brandable: a basic Google '
                                        'search, the EU trademark and design view, and the WIPO global '
                                        'brands database, and skip terms tied to one major company [live '
                                        'NDDCamp — PdwE4T9wmMo @ 00:33:12]. Carter Law Firm credits the '
                                        'USPTO with a usable trademark database worth adding as a fourth '
                                        'check.'},
                            {'name': 'generic_vs_trademark_term',
                             'type': 'text',
                             'prompt': 'Classify this name as a generic term, a descriptive phrase, a '
                                       "brandable, or a term containing someone else's mark. Explain the "
                                       'classification and estimate the dispute exposure in dollars it '
                                       'creates for the rest of the portfolio.',
                             'example': 'POWERS Pod buys generic terms only, because trademark terms '
                                        'invite UDRP filings against the portfolio [POWERS Pod — '
                                        'S9SNhuYObsA @ 00:30:09]. Brooks Conkle separately notes a UDRP '
                                        'filing costs $5,000 and a holder can sue and take the name. Drew '
                                        'caps bids on trademark-exposed names at $2,500 on '
                                        'WordPresstutorials.com, the cost of a UDRP-style takedown.'},
                            {'name': 'udrp_response_plan',
                             'type': 'textarea',
                             'prompt': 'Write the plan you will follow if a UDRP complaint lands on any '
                                       'descriptive or brandable name: who you will hire, the documents '
                                       'you will gather, and the registration-date evidence you will '
                                       "compare against the complainant's rights.",
                             'example': 'A Serbian investor lost kerosoft.co by default after filing no '
                                        'response to a $1,330 Forum complaint, so answer every complaint '
                                        '[live NDDCamp — PdwE4T9wmMo @ 00:04:24]. Steven Rinehart says to '
                                        'hire counsel experienced in domain disputes specifically and '
                                        "check whether the complainant's use-based rights predate your "
                                        'registration date. Rinehart quotes 34 to 44 days for a UDRP.'},
                            {'name': 'udrp_vs_acpa_exposure',
                             'type': 'textarea',
                             'prompt': 'Estimate the time and cost a complainant would face to pursue this '
                                       'name through UDRP versus a court action, and compare that cost '
                                       'with what the complainant might otherwise pay to buy the name '
                                       'outright. Record both figures side by side.',
                             'example': 'Doug Isenberg clocks a typical UDRP at about 60 days versus 259 '
                                        'days for the Debevoise ACPA final judgment [GigaLaw - Doug '
                                        'Isenberg — GI9Us2WWsAo @ 00:06:31], and notes the UDRP offers no '
                                        "injunctive relief. NDDCamp panelists price a complainant's run at "
                                        'about $5,000 in lawyer fees plus a $1,500 filing fee, against '
                                        '50,000 to 100,000 euros to buy outright.'},
                            {'name': 'extension_bet',
                             'type': 'textarea',
                             'prompt': 'If this name uses an extension other than .com, record why you are '
                                       "holding it, the matching .com's status, and the registry terms you "
                                       'have read. State the maximum you will spend and the exit if the '
                                       'extension stalls.',
                             'example': 'James Booth reports two-word .ai names bought at $200 to $300 and '
                                        'sold at $50,000 to $100,000, yet a one-word .com is still worth '
                                        'about 4 to 5 times the one-word .ai [domainsherpa — 35YUAM-dUn0 @ '
                                        '00:21:41]. Read ccTLD terms first: .si includes moral type '
                                        'clauses, and Afnic deletes portfolios after a two-week reply '
                                        'deadline.'},
                            {'name': 'sell_through_model',
                             'type': 'textarea',
                             'prompt': 'Using your current name count, project how many names will sell '
                                       'this year at a realistic sell-through rate, the average sale price '
                                       'you expect, and the venue mix through which you expect those sales '
                                       'to close.',
                             'example': 'A typical portfolio sells 1 to 3% a year, roughly 2 of every 100 '
                                        'names, which Ownerly frames as a lottery ticket business with a '
                                        'holding cost [Ownerly — xPtTNJU_OGE @ 00:02:01]. Andrew Allemann '
                                        'logged 21 of 25 sales through Afternic for about 60% of revenue, '
                                        'with Sedo, Spaceship and saw.com splitting the rest.'},
                            {'name': 'renewal_ceiling_vs_cash',
                             'type': 'textarea',
                             'prompt': 'Total the annual renewal bill for the full portfolio and compare '
                                       'it with cash on hand plus projected sales. Identify how many dry '
                                       'months the portfolio can survive and which names you will drop '
                                       'first if sales stall.',
                             'example': 'One challenge investor put about $100K into 260 to 270 names, '
                                        'collected $28K on the first three sales, then hit three dry '
                                        'months [GoDaddy Domain Academy — d1VjM9-Tyig @ 00:41:30]. Brooks '
                                        'Conkle notes a thousand domains carry about $15,000 in yearly '
                                        'overhead, and Andrey Verevko warns a $10 buy renewed at $15 and '
                                        'sold for $20 loses money.'},
                            {'name': 'bad_year_model',
                             'type': 'textarea',
                             'prompt': 'Model a bad year for this portfolio: the fewest sales you could '
                                       'plausibly close, total revenue, total renewals and fees, and one '
                                       'unexpected legal or dispute cost. Show the resulting profit or '
                                       'loss and how you would cover it.',
                             'example': 'Ownerly models the bad year first: three sales totaling $9,400 '
                                        'left $900 profit, and a $4,000 trademark dispute turned it into a '
                                        'roughly $3,000 loss [Ownerly — xPtTNJU_OGE @ 00:17:49]. On Tim '
                                        'Ferriss, the survival floor is framed as making $250 every day '
                                        'minimum so the business survives. Write both figures beside your '
                                        'own projection.'},
                            {'name': 'lease_income_ladder',
                             'type': 'textarea',
                             'prompt': 'Identify which names in the portfolio suit lease or lease-to-own '
                                       'income, the monthly rate you will ask for each, and the share of '
                                       'annual sales you expect lease-to-own deals to contribute toward a '
                                       'steadier revenue stream.',
                             'example': 'On Tim Ferriss, lease pricing runs a 5 to 10% option fee credited '
                                        'to the strike plus 0.5 to 1 point per month, so a $100K name '
                                        'yields $500 to $1,000 monthly [Tim Ferriss — ApCGeST90RA @ '
                                        '01:03:55]. Andrew Allemann reports eight of 25 sales this year '
                                        'were LTOs, alongside $5,000 to $7,000 in monthly lease-to-own '
                                        'income.'},
                            {'name': 'sourcing_and_pricing_discipline',
                             'type': 'textarea',
                             'prompt': 'Describe your sourcing routine for the coming quarter: where you '
                                       'will hunt, at what time of day, your maximum bid per name, and the '
                                       'safeguard that stops you from raising that maximum or pricing '
                                       'finished names too low.',
                             'example': 'Mike Zigger searches $1 to $50 GoDaddy closeouts in the middle of '
                                        'the day, every day, and newsletter names often sell before 5 a.m. '
                                        'Pacific [GoDaddy Domain Academy — d1VjM9-Tyig @ 00:44:08]. '
                                        "Allemann's bidding bot bids late and cannot raise its max later. "
                                        'The same challenge warns that pricing everything too low left '
                                        'money on the table.'}],
                 'completion_gate': 'Complete only when every candidate shows a dated three-database '
                                    'trademark check, a written UDRP response plan exists, any non-.com '
                                    'bet has a spending cap, and the capital model shows sell-through, '
                                    'renewal ceiling, dry-month runway, and a bad-year scenario that '
                                    'includes a dispute cost.'}]}
