from __future__ import annotations

CHAPTER_2 = {'id': 'Q2',
 'chapter_id': 'Q2',
 'chapter_number': 2,
 'question_number': 2,
 'slug': 'registrars-dns-infrastructure-domain-portfolio',
 'question_prompt': 'Which registrar should a domain investor use, and how do you connect domains to '
                    'Cloudflare DNS?',
 'kicker': 'Q2 / THE BIG MONEY PLAYBOOKS',
 'title': 'Registrars and DNS Infrastructure for the Domain Portfolio',
 'subtitle': 'Porkbun vs Cloudflare vs Dynadot vs Namecheap comparisons (free privacy, SSL, refunds, '
             'renewals), reseller margins (GoDaddy vs Domain Name API), Cloudflare caveats, nameserver and '
             'DNS record setup, and BigRock fast-transfer for Afternic/Sedo',
 'layout_template': 'executive_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners agree on three rules for a domain portfolio: register at a dedicated '
                      'registrar rather than a host, require free WHOIS privacy, and price every name on '
                      'its renewal rate instead of first-year bait. The cheapest published .com figures '
                      "sit close together: Cloudflare Registrar at $11.17 (Utke's cart showed $10.46), "
                      'Porkbun at $11.81, Dynadot at $10.88, and Spaceship at $8.88 renewing at $9.98. '
                      "Namecheap's Beast Mode handles bulk searches of up to 5,000 names. Cloudflare's "
                      'free plan is the default DNS layer. The workflow is to quick-scan records, swap in '
                      'two nameservers, disable DNSSEC at the old registrar first, set MX and TXT records '
                      'to gray-cloud, and wait anywhere from minutes to 48 hours. The disagreements are '
                      'sharp. Cloudflare is non-refundable and locks nameservers. One reviewer reports a '
                      '4-day Porkbun refund window and another reports none. Luka Knows has demoted both '
                      'Porkbun and Dynadot over support problems and domain-snatching reports.',
 'key_metrics': [{'label': 'Cloudflare Registrar .com At-Cost Price',
                  'metric': 'Cloudflare Registrar .com At-Cost Price',
                  'value': '$11.17 to register, renew, or transfer in',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Design Guy's published-price comparison put Cloudflare 64 cents under "
                             "Porkbun's $11.81 on all three .com price rounds.",
                  'source': 'Design Guy ([mMGvtO-bkPI @ 00:00:59])'},
                 {'label': 'Porkbun .com Flat Registration and Renewal',
                  'metric': 'Porkbun .com Flat Registration and Renewal',
                  'value': 'Approximately $11.81 per year including the ICANN fee',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'SEARCHLIGHT HQ reported that registration and renewal are generally the same '
                             'price, so there is no jump after year one.',
                  'source': 'SEARCHLIGHT HQ ([RClpPcLHviU @ 00:00:30])'},
                 {'label': 'Spaceship .com Register vs Renew',
                  'metric': 'Spaceship .com Register vs Renew',
                  'value': '$8.88 to register, $9.98 to renew',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "David Utke's live cart check on Spaceship, the Namecheap-run brand, with "
                             'WHOIS protection included.',
                  'source': 'David Utke ([UkMYRY9wDN0 @ 00:10:42])'},
                 {'label': 'Reseller Margin Scaling Example',
                  'metric': 'Reseller Margin Scaling Example',
                  'value': '$5 gross margin x 10,000 registrations = $50,000',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "The Domain Reseller channel's hypothetical volume math, stated as figures "
                             'before taxes, payment fees, and operating costs.',
                  'source': 'Domain Reseller ([72rBKTbIECI @ 00:03:27])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every operator who covered registrar selection starts from the same rule. '
                              'The registrar, the DNS layer, and the web host are three separate jobs, and '
                              'the domain should never be held hostage by the host. David Utke tells '
                              'viewers in every long-form tutorial to register at a dedicated domain '
                              'registrar rather than at a web host or site builder. Those platforms have '
                              'to mark the name up to make a profit, while registrars compete hard to keep '
                              'costs low [UkMYRY9wDN0 @ 00:00:30]. Luka Knows goes further and puts '
                              'Hostinger and web hosting providers on a never-use list for domains. '
                              'Bundling creates a single point of failure: if the host goes down, the '
                              'domain goes down with it. Bundles also still charge for WHOIS privacy and '
                              'make migrating away far harder [oi-pZAGrrhQ @ 00:05:17]. Craylor draws the '
                              'same line from the DNS side, warning that Cloudflare is not web hosting. '
                              'The domain points to Cloudflare, Cloudflare manages the records and sends '
                              'visitors on, and a real server still has to sit at the end of that chain '
                              '[IXpvUD5SDzA @ 00:00:12]. Create a Pro Website frames it for people who '
                              'just want to sit on a name. A domain is the address, not the house, so '
                              'owning one does not mean you own a website. Anyone who only wants to secure '
                              'a URL can simply search, add it to the cart, and check out [08Ekqe45IH0 @ '
                              '00:03:31].',
                              'The second hard line is free WHOIS privacy, and nobody in the lineup treats '
                              'it as optional. David Utke calls domain privacy non-negotiable because '
                              'registration forces you to submit your name, email, address, and phone '
                              'number. Utke lists GoDaddy, Hover, Hostinger, Bluehost, Network Solutions, '
                              'Squarespace, and Shopify as too expensive, partly because some of them sell '
                              'privacy as an upsell [UkMYRY9wDN0 @ 00:14:00]. Luka Knows flags domain.com '
                              'for charging extra for WHOIS privacy and calls it a complete red flag in '
                              '2026 and beyond. Without it, scammers pull your contact details from the '
                              'public database for automated outreach, non-stop calls, and resale of your '
                              'data [oi-pZAGrrhQ @ 00:03:01]. Design Guy notes that some registrars charge '
                              'an extra $10 or $12 just to keep that spam inbox quiet. Cloudflare '
                              'Registrar and Dynadot both include redaction or privacy at zero dollars '
                              "with no upsell [chataozFYGw @ 00:01:46]. Jake's Tech Lab built an entire "
                              'five-way ranking on the same baseline: free privacy, free SSL, free email '
                              'forwarding, and built-in DNSSEC. The channel cut Ionos simply because the '
                              'company does not publish whether privacy is free [ul52eFQneY0 @ 00:01:07]. '
                              'For a portfolio, a registrar that bills privacy per name is disqualified on '
                              'that point alone, because the charge repeats on every domain every year.',
                              'The third consensus point is that the first-year sticker is bait and the '
                              'renewal line is the real price. Luka Knows opens with the classic trap: a '
                              '1-cent GoDaddy deal, followed a year later by a renewal bill. According to '
                              'Luka Knows, GoDaddy often runs two or three times the cost of competitors '
                              'and hides that behind flashy first-year promos and promo pricing '
                              '[oi-pZAGrrhQ @ 00:01:46]. Create a Pro Website describes the same headache '
                              "from the buyer's seat: registrars advertise a 1-cent domain and then "
                              'quietly charge $40 [08Ekqe45IH0 @ 00:00:00]. SEARCHLIGHT HQ singles out '
                              'Porkbun precisely because registration and renewal for a .com both run at '
                              'roughly $11.81, including the ICANN fee. That keeps budgeting predictable '
                              'because there is no price spike after year one [RClpPcLHviU @ 00:00:48]. '
                              'The Domain Reseller channel applies the same discipline at wholesale. Do '
                              'not compare first-year prices; compare renewal costs, fixed program fees, '
                              'integration costs, and lifetime value. A program fee lands every year '
                              'regardless of sales volume [72rBKTbIECI @ 00:04:03]. For anyone carrying a '
                              'portfolio, the renewal rate is the cost that compounds every year. A cheap '
                              'entry price on a registrar with an inflated renewal will cost more over '
                              'time than a flat at-cost rate from day one.'],
               'table': {'caption': 'Baseline rules every practitioner applies before choosing where '
                                    'portfolio names live',
                         'headers': ['Consensus Rule',
                                     'What The Practitioner Reports',
                                     'Portfolio Operator Move',
                                     'Expert Source'],
                         'rows': [['Register domains at a dedicated registrar, not a host',
                                   'Web hosts and site builders must mark domain names up to profit, while '
                                   'registrars keep costs low',
                                   'Buy every portfolio name at a pure registrar and keep it off hosting '
                                   'accounts',
                                   'David Utke ([UkMYRY9wDN0 @ 00:00:30])'],
                                  ['Bundling domain and host creates a single point of failure',
                                   'If the host has problems the domain goes down too, and migrating away '
                                   'becomes far harder',
                                   'Hold domains and hosting at separate companies because it is cheaper '
                                   'and safer',
                                   'Luka Knows ([oi-pZAGrrhQ @ 00:05:37])'],
                                  ['Free WHOIS privacy is non-negotiable on every registration',
                                   'Registration requires your name, email, address, and phone number, so '
                                   'privacy must be included free forever',
                                   'Reject any registrar that sells privacy as a per-domain upsell at '
                                   'checkout',
                                   'David Utke ([UkMYRY9wDN0 @ 00:04:17])'],
                                  ['Judge registrars on renewal rates, never on first-year promos',
                                   "GoDaddy often runs two or three times competitors' cost, hidden behind "
                                   'flashy first-year promotional deals',
                                   'Model every name on its long-term renewal cost before adding it to the '
                                   'cart',
                                   'Luka Knows ([oi-pZAGrrhQ @ 00:01:46])'],
                                  ['Cloudflare manages DNS records but is not web hosting',
                                   'The domain points to Cloudflare, which manages DNS and sends visitors '
                                   'to the final destination',
                                   'Treat Cloudflare as the DNS and CDN layer that sits in front of a real '
                                   'server',
                                   'Craylor ([IXpvUD5SDzA @ 00:00:26])'],
                                  ['Privacy, SSL, forwarding, and DNSSEC should come free',
                                   'These extras are free at some registrars but paid add-ons at others, '
                                   'which gets frustrating fast',
                                   'Shortlist only registrars that publish all four extras as included at '
                                   'zero cost',
                                   "Jake's Tech Lab ([ul52eFQneY0 @ 00:00:00])"],
                                  ['The Cloudflare free plan is enough for most operators',
                                   'Paid plans target advanced and enterprise users, and most users get no '
                                   'advantage from upgrading',
                                   'Scroll past the paid columns during signup and select the free plan '
                                   'box',
                                   'Craylor ([IXpvUD5SDzA @ 00:01:54])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The Cloudflare onboarding sequence is the same in every walkthrough. '
                              "Easytorial's version: log in, click Add a Site or Onboard a Domain, enter "
                              'the real domain, and pick a plan, which for most people is the free one. '
                              'Cloudflare then scans for existing A, CNAME, and MX records so nothing gets '
                              'lost in a migration. Review every imported record before touching the '
                              'nameservers, especially the root record pointing to the server IP and the '
                              'www CNAME [sx83eEm6nk4 @ 00:00:34]. George Basics runs the same flow from '
                              'Account Home. Choose the recommended quick scan for DNS records, pick the '
                              'free plan, scroll down to Continue to Activation, and copy the two assigned '
                              'nameservers. At Dynadot, go to Manage Domains, open the domain, then DNS '
                              'Settings and Name Servers, and select enter new or existing name servers. '
                              'Paste both, then click Save Name Servers [aeqNGnkQgbA @ 00:01:06]. Porkbun '
                              'is shorter still: open Domain Management, click the NS button under the '
                              'domain, paste both nameservers, click Submit, and wait a few hours while '
                              'Cloudflare checks them [OuQbsdwFTA0 @ 00:01:13]. PMN Online adds a step '
                              'most tutorials skip. Turn DNSSEC off at the registrar before the swap, '
                              'because it can cause DNS failures during the nameserver transition '
                              "[AKtcv_vFlSY @ 00:01:13]. Easytorial's assigned nameservers looked like "
                              'alice and bob under ns.cloudflare.com, and Cloudflare emails you when the '
                              'domain goes live.',
                              'Inside the DNS tab, every record is built from the same five fields. PMN '
                              'Online lays them out. Type is A, AAAA, CNAME, MX, or TXT. Name is the @ '
                              'symbol for the root or a subdomain like www or mail. Content is an IP '
                              'address, a hostname, or a verification value. TTL is left on Auto. Proxy '
                              'status applies only to A, AAAA, and CNAME records [piq0yLKq_SE @ 00:02:05]. '
                              'The proxy toggle is where setups break. Easytorial explains that the orange '
                              'cloud routes traffic through Cloudflare for performance and attack '
                              'protection and should be on for most web traffic. MX and verification '
                              'records must be switched to the gray DNS-only cloud, or those services will '
                              'not work correctly [sx83eEm6nk4 @ 00:03:23]. Craylor recommends proxying A '
                              'records and CNAMEs in most cases. Craylor cites a network in over 300 '
                              'cities that serves cached files from the node closest to each visitor, and '
                              'notes that Cloudflare shows a CAPTCHA to traffic from IP addresses it '
                              'already knows belong to bad actors [IXpvUD5SDzA @ 00:03:35]. Craylor also '
                              'uses Cloudflare to avoid paying for SSL certificates entirely. Craylor '
                              "reports Cloudflare's email forwarding as instant, after other forwarders "
                              'held mail for an extra hour or two. Propagation estimates run from a few '
                              'minutes up to 48 hours worldwide, so check back rather than panic '
                              '[AKtcv_vFlSY @ 00:03:03].',
                              'The per-name price gaps are small, but they add up across a portfolio. '
                              'Design Guy compared published .com pricing. Cloudflare Registrar charges '
                              '$11.17 to register, renew, or transfer in, and Porkbun charges $11.81 for '
                              'all three. That 64-cent gap per name gave Cloudflare a clean sweep of the '
                              "three price rounds [mMGvtO-bkPI @ 00:01:54]. David Utke's live cart checks "
                              'came in as follows. Namecheap was $6.49 for the first year for new '
                              'customers, or $9.98 for existing customers, renewing at $14.98. Porkbun was '
                              '$11 flat. Dynadot was $10.88 flat with a free one-page site. Spaceship was '
                              '$8.88, renewing at $9.98. Cloudflare was $10.46 flat. Namecheap, Porkbun, '
                              'and Cloudflare all allow registrations of up to 10 years [UkMYRY9wDN0 @ '
                              "00:10:42]. For bulk work, Utke points domainers to Namecheap's Beast Mode, "
                              'which searches up to 5,000 domains or keywords at once [UkMYRY9wDN0 @ '
                              '00:03:23]. On the wholesale side, the Domain Reseller channel prices '
                              "GoDaddy's Basic reseller plan (up to 25 customers) at $53.88 for the first "
                              'year, renewing at $107.88. The Pro plan is $89.88, renewing at $179.88. '
                              'Domain Name API has no activation fee and sells a .com at $11.99 to '
                              "register and $12.29 to renew. The channel's volume math: a $5 margin across "
                              '10,000 registrations is $50,000 gross [72rBKTbIECI @ 00:03:27].'],
               'table': {'caption': 'Stated .com economics and bundled terms by registrar and reseller '
                                    'program',
                         'headers': ['Registrar Or Program',
                                     'Stated .com Economics',
                                     'Bundled Extras And Terms',
                                     'Expert Source'],
                         'rows': [['Cloudflare Registrar, sold at cost to pull buyers into its ecosystem',
                                   '$11.17 to register, renew, or transfer a standard .com',
                                   'Free WHOIS redaction and SSL, but new registrations are strictly '
                                   'non-refundable with zero window',
                                   'Design Guy ([mMGvtO-bkPI @ 00:03:17])'],
                                  ['Porkbun, known for transparent flat pricing on a standard .com',
                                   'Approximately $11.81 to register and renew, including the ICANN fee',
                                   'Free WHOIS privacy, SSL, DNS management, URL forwarding, and up to 20 '
                                   'email forwards',
                                   'SEARCHLIGHT HQ ([RClpPcLHviU @ 00:01:02])'],
                                  ['Spaceship, the sleeker budget brand run by Namecheap',
                                   '$8.88 to register and $9.98 to renew on a live cart check',
                                   'WHOIS protection included, plus Beast Mode bulk search just like the '
                                   'parent Namecheap',
                                   'David Utke ([UkMYRY9wDN0 @ 00:10:42])'],
                                  ["Namecheap, the main registrar used and recommended in Utke's tutorials",
                                   '$6.49 first year for new customers; $9.98 for existing customers, '
                                   'renewing at $14.98',
                                   'Privacy free forever, light upsells you can ignore, and registrations '
                                   'of up to 10 years',
                                   'David Utke ([UkMYRY9wDN0 @ 00:02:41])'],
                                  ['Dynadot, a registrar focused squarely on domain names and domain '
                                   'services',
                                   '$10.88 to register and $10.88 to renew per year',
                                   'Free privacy plus a free one-page site usable as a coming-soon or '
                                   'buy-this-domain page',
                                   'David Utke ([UkMYRY9wDN0 @ 00:09:27])'],
                                  ['GoDaddy Reseller, a hosted white-label storefront program',
                                   'Basic $53.88 first year, renewing at $107.88; Pro $89.88, renewing at '
                                   '$179.88',
                                   'Up to 20 percent off retail on Basic and up to 40 percent on Pro; API '
                                   'access requires calling their team',
                                   'Domain Reseller ([72rBKTbIECI @ 00:01:08])'],
                                  ['Domain Name API, an ICANN-accredited reseller platform with a REST API',
                                   '$11.99 to register and $12.29 to renew a .com at the reseller tier',
                                   'No activation fee, minimum deposit, or monthly cost, with wholesale '
                                   'pricing on more than 800 extensions',
                                   'Domain Reseller ([72rBKTbIECI @ 00:02:11])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Field Notes From The Nameserver Swap',
                           'body': 'These are the small operational details that decide whether a '
                                   'portfolio domain resolves on the first try or goes dark during '
                                   'migration.',
                           'items': ['Turn off DNSSEC at the current registrar before pasting in the '
                                     'Cloudflare nameservers. Leaving it on risks DNS failures and '
                                     'downtime mid-transition [PMN Online — AKtcv_vFlSY @ 00:01:13].',
                                     'Never proxy MX or TXT verification records. Set them to the gray '
                                     'DNS-only cloud, or email and verification services will not work '
                                     'correctly [Easytorial — sx83eEm6nk4 @ 00:03:23].',
                                     'Domains registered at Cloudflare cannot have their nameservers '
                                     'changed. Utke calls this a dealbreaker with dedicated shared hosts '
                                     'but a perfect match for Amazon AWS [David Utke — UkMYRY9wDN0 @ '
                                     '00:13:15].',
                                     "Register at Spaceship for the full 10 years to lock in today's price "
                                     'for a decade, for what two years would cost at a host like '
                                     'SiteGround [Luka Knows — oi-pZAGrrhQ @ 00:13:45].']},
               'sop_steps': [{'step': 1,
                              'title': 'Onboard the domain in Cloudflare',
                              'action': 'From Account Home, enter the domain, choose the quick scan for '
                                        'DNS records, select the free plan, and click Continue to '
                                        'Activation.',
                              'detail': 'Quick scan is the option Cloudflare itself recommends. The free '
                                        'plan sits below the paid columns, so scroll all the way down '
                                        'before continuing [George Basics — OuQbsdwFTA0 @ 00:00:37].'},
                             {'step': 2,
                              'title': 'Audit imported records, then swap nameservers',
                              'action': 'Check the root record and the www CNAME against the real server, '
                                        'disable DNSSEC at the registrar, and replace the old nameservers '
                                        "with Cloudflare's two.",
                              'detail': 'Do not just click through the imported records. Double-check the '
                                        'root A record and the www CNAME like the shipping address on a '
                                        'critical package, then hand DNS control from the registrar to '
                                        'Cloudflare [Easytorial — sx83eEm6nk4 @ 00:01:08].'},
                             {'step': 3,
                              'title': 'Build the record set',
                              'action': 'Add the A or CNAME records for the root (@) and www, set TTL to '
                                        'Auto, keep web records orange-clouded, and set MX and TXT records '
                                        'to gray.',
                              'detail': 'Fill in Type, Name, Content, TTL, and proxy status for each '
                                        'record, then save. Allow a few minutes for propagation and verify '
                                        'accuracy before saving [PMN Online — piq0yLKq_SE @ 00:02:05].'},
                             {'step': 4,
                              'title': 'Opt sellable names into marketplace fast transfer',
                              'action': 'At BigRock, go to Manage, click Revert to Old Look, then Manage '
                                        'Orders, Fast Transfer, and Opt In, and confirm with the emailed '
                                        'verification code.',
                              'detail': 'If the code has not arrived, resend it. After you click Confirm '
                                        'Opt In, select Afternic or Sedo to enable the domain listing for '
                                        'fast transfer [PG Tech Help — 0QCYIFcFO7A @ 00:00:33].'}]},
              {'section_number': 3,
               'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Porkbun is the sharpest split in this registrar field. The Lone Crater '
                              'pitches it as incredibly competitive and transparent on price, with free '
                              'Whois privacy on all registrations, a remarkably user-friendly interface, '
                              'and customer support that often receives five-star reviews [hdvK17zvRgk @ '
                              '00:01:11]. Luka Knows tells the opposite story from his own testing: '
                              'Porkbun used to be one of his top recommendations, but he now calls the '
                              'experience dated, says connecting a domain to a website takes way longer '
                              'than it should, labels support unreliable, and reports that one of '
                              "Porkbun's own suggested help questions failed when he tried it [oi-pZAGrrhQ "
                              '@ 00:10:52]. The refund question is contested just as hard. Design Guy '
                              "reads Porkbun's published terms as a four-day, 96-hour refund window on new "
                              'registrations and hands Porkbun that round outright against Cloudflare '
                              'Registrar, calling it breathing room for an honest typo [mMGvtO-bkPI @ '
                              '00:03:01]. David Utke states the reverse on camera: Porkbun does not offer '
                              'refunds on domain registration, all sales are final, and support is a '
                              'ticket queue answered within 24 hours instead of a round-the-clock desk '
                              '[UkMYRY9wDN0 @ 00:06:26]. Design Guy himself tells buyers to double check '
                              'both sites before purchasing, because prices and plans move.',
                              "Cloudflare Registrar draws the widest spread of verdicts. Jake's Tech Lab "
                              'ranks it the cleanest overall winner for free extras, citing free WHOIS '
                              'redaction, free SSL, free email routing, and one-click DNSSEC without a '
                              'single nickel in upsells [ul52eFQneY0 @ 00:01:22]. Design Guy backs the '
                              'price case with published numbers: $11.17 for a .com registration, renewal, '
                              "and transfer against Porkbun's $11.81, a 64-cent gap that hands Cloudflare "
                              'a three-round sweep on raw cost [mMGvtO-bkPI @ 00:01:36]. David Utke likes '
                              'the at-cost model and quotes $10.46 to register and renew, but calls one '
                              'catch a dealbreaker for him: you cannot change the name servers of a domain '
                              'registered with Cloudflare, which he says turns pairing it with a dedicated '
                              'shared web host into a hassle, even though it is a perfect match for '
                              'something like Amazon AWS [UkMYRY9wDN0 @ 00:13:15]. Luka Knows reserves '
                              'Cloudflare for complete professionals buying for clients or big '
                              'organizations who need to save every cent, rates it the least '
                              'beginner-friendly option on his entire list, notes that everything is '
                              'manual, and argues the savings over his best budget pick are negligible '
                              'anyway [oi-pZAGrrhQ @ 00:12:44]. Builders chasing the lowest recurring cost '
                              'and holders who need free name-server control land on opposite sides.',
                              'The question of where to park a portfolio splits into three camps. David '
                              'Utke and Luka Knows both crown Namecheap: Utke uses it in every long-form '
                              'tutorial and quotes $6.49 first year for new customers, or $9.98 first year '
                              'renewing at $14.98 for existing accounts, plus Beast Mode for domainers '
                              'searching up to 5,000 names at once [UkMYRY9wDN0 @ 00:02:41]; Luka keeps '
                              'all his most important domains there and names its sister brand Spaceship '
                              'the budget pick, with .com renewal under $10 and ten-year registration that '
                              "locks today's price for a decade [oi-pZAGrrhQ @ 00:13:23]. Create a Pro "
                              'Website runs a different playbook for builders, sending domain-only buyers '
                              'to Namecheap but steering site builders to Hostinger, where the '
                              '12-to-48-month plans include a free custom domain and hosting starts at as '
                              'little as $3 a month [08Ekqe45IH0 @ 00:04:43]. Luka rejects that bundle '
                              'outright, calling hosting-plus-domain a single point of failure that tends '
                              'to cost more, still charges for WHOIS privacy, and makes migration far '
                              "harder. On the resale side, Domain Reseller contrasts GoDaddy's annual-fee "
                              "white-label storefront with Domain Name API's model of no activation fee, "
                              'no minimum deposit, no monthly cost, and wholesale pricing across more than '
                              '800 extensions [72rBKTbIECI @ 00:01:40].'],
               'table': {'caption': 'Registrar and DNS playbooks where named practitioners take opposite '
                                    'positions',
                         'headers': ['Battleground', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Porkbun refund policy on brand new registrations',
                                   'Design Guy reads a four-day, 96-hour refund window covering honest '
                                   'typos',
                                   'David Utke says Porkbun offers no registration refunds and all sales '
                                   'are final',
                                   'Design Guy ([mMGvtO-bkPI @ 00:03:01]); David Utke ([UkMYRY9wDN0 @ '
                                   '00:06:26])'],
                                  ['Porkbun usability and support quality for daily management',
                                   'The Lone Crater calls the interface remarkably user-friendly with '
                                   'five-star support reviews',
                                   'Luka Knows calls it dated, slow to connect, unreliable on support, not '
                                   'beginner-friendly',
                                   'The Lone Crater ([hdvK17zvRgk @ 00:01:11]); Luka Knows ([oi-pZAGrrhQ @ '
                                   '00:10:52])'],
                                  ['Cloudflare Registrar as the home for a portfolio',
                                   "Jake's Tech Lab ranks it cleanest overall winner on free privacy, SSL, "
                                   'routing, DNSSEC',
                                   'David Utke calls locked name servers a dealbreaker when using a shared '
                                   'web host',
                                   "Jake's Tech Lab ([ul52eFQneY0 @ 00:01:22]); David Utke ([UkMYRY9wDN0 @ "
                                   '00:13:15])'],
                                  ['Dynadot risk profile for buying and holding names',
                                   'Design Guy credits a five-day grace deletion refunded as account '
                                   'credit, not cash',
                                   'Luka Knows flags pricier TLDs like .ai and an online domain snatching '
                                   'report he has not personally experienced',
                                   'Design Guy ([chataozFYGw @ 00:01:15]); Luka Knows ([oi-pZAGrrhQ @ '
                                   '00:09:33])'],
                                  ['Buying the domain bundled together with web hosting',
                                   'Create a Pro Website pushes Hostinger 12-to-48-month plans that '
                                   'include a free custom domain',
                                   'Luka Knows calls bundling a single point of failure that makes '
                                   'migration far harder',
                                   'Create a Pro Website ([08Ekqe45IH0 @ 00:04:43]); Luka Knows '
                                   '([oi-pZAGrrhQ @ 00:05:17])'],
                                  ['Cloudflare proxy status across different record types',
                                   'Craylor recommends enabling the orange-cloud proxy on A records and '
                                   'CNAMEs in most cases',
                                   'Easytorial switches MX and verification records to grey-cloud DNS only '
                                   'or they break',
                                   'Craylor ([IXpvUD5SDzA @ 00:03:20]); Easytorial ([sx83eEm6nk4 @ '
                                   '00:03:23])'],
                                  ['Reseller model for selling domains under your own brand',
                                   'GoDaddy storefront hosts the store and payments but charges an annual '
                                   'program fee every year',
                                   'Domain Name API charges no activation fee, no minimum deposit, and no '
                                   'monthly cost',
                                   'Domain Reseller ([72rBKTbIECI @ 00:00:46]); Domain Reseller '
                                   '([72rBKTbIECI @ 00:01:40])']]}},
              {'section_number': 4,
               'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The first-year sticker is where most buyers get burned. Create a Pro '
                              'Website opens with the classic trap of a registrar advertising a domain at '
                              '1 cent and then secretly charging $40 [08Ekqe45IH0 @ 00:00:14], and Luka '
                              'Knows describes the same pattern from the buyer side: grab a 1-cent GoDaddy '
                              'deal, then open the account a year later and find the renewal bill. Luka '
                              'puts GoDaddy at often two or three times more expensive than competitors '
                              'behind flashy first-year promos, says he has seen a basic Hover .com '
                              'renewal run $50 plus for one year after the intro period expires, and warns '
                              'that domain.com stuffs the cart with three trials by default, where an '
                              'email add-on can quietly cost $36 a year once its trial ends and compound '
                              'into hundreds of dollars on a domain held for years [oi-pZAGrrhQ @ '
                              '00:04:56]. David Utke lists GoDaddy, Hover, Hostinger, Blue Host, Network '
                              'Solutions, Squarespace, and Shopify as too expensive, citing high markups, '
                              'higher renewal rates, and WHOIS protection sold as an upsell [UkMYRY9wDN0 @ '
                              '00:13:45]. SEARCHLIGHT HQ shows the same cliff on hosting sold by a '
                              "registrar: Porkbun's starter WordPress plan is $30 for the first year and "
                              'renews at $120 per year [RClpPcLHviU @ 00:01:40].',
                              'The nameserver cutover is the operational bottleneck where practitioners '
                              'report breakage. PMN Online warns that DNSSEC must be turned off at the '
                              "registrar before swapping in Cloudflare's two name servers, because leaving "
                              'it on during the transition risks DNS failures and disruptions to site '
                              'availability, and puts worldwide propagation at up to 48 hours [AKtcv_vFlSY '
                              '@ 00:01:13]. Easytorial tells operators not to just click through '
                              "Cloudflare's automated record import: review every record, especially the "
                              'root record pointing at the server IP and the www CNAME, and flip MX and '
                              'verification records to the grey-cloud DNS-only setting, otherwise those '
                              'services will not work correctly [sx83eEm6nk4 @ 00:03:23]. Luka Knows '
                              "reports that GoDaddy's built-in integrations with platforms like Google "
                              'Sites break constantly and may have already partially imported records '
                              'without telling you, forcing manual cleanup that frustrates beginners '
                              '[oi-pZAGrrhQ @ 00:02:25]. Craylor adds two beginner traps: Cloudflare is '
                              'not web hosting, so you still need a server for it to point at, and the '
                              'free plan box sits underneath the paid columns, which makes new users '
                              'message him thinking Cloudflare expects $20 a month; he also admits '
                              'first-timers may make mistakes and need troubleshooting before everything '
                              'works [IXpvUD5SDzA @ 00:01:25].',
                              'Irreversible purchases and fixed overhead are the economics checks. Design '
                              'Guy is blunt that new Cloudflare Registrar registrations are completely '
                              "non-refundable, so a mistyped name means the fee is gone, whereas Dynadot's "
                              'five-day grace deletion returns money only as account credit rather than '
                              'cash [chataozFYGw @ 00:01:15]. Domain Reseller warns that a reseller '
                              'program fee is paid every year regardless of sales volume, lays out '
                              "GoDaddy's Basic plan at $53.88 the first year renewing at $107.88 for up to "
                              '25 customers and Pro at $89.88 renewing at $179.88, and runs a hypothetical '
                              '$5 gross margin where 1,000 registrations yields $5,000 before taxes, '
                              'payment fees, and operating costs [72rBKTbIECI @ 00:03:47]. Luka Knows '
                              'flags the information trap behind every recommendation: creators earn '
                              'bigger affiliate commissions on pricier products, so cheap, high-quality '
                              'registrars like Spaceship get pushed less by reviewers [oi-pZAGrrhQ @ '
                              '00:06:13]. On the exit side, PG Tech Help shows that selling through '
                              'Afternic or Sedo from BigRock requires reverting to the old dashboard look, '
                              'opting into Fast Transfer under manage orders, and entering an emailed '
                              'verification code, with a resend option if it never arrived, and the '
                              'verification code for such domains must be submitted [0QCYIFcFO7A @ '
                              '00:00:16].'],
               'table': {'caption': 'Firsthand traps, what broke, and the counter-move practitioners use',
                         'headers': ['Trap',
                                     'What Practitioners Reported',
                                     'Counter-Move Taught',
                                     'Expert Source'],
                         'rows': [['One-cent introductory domain pricing',
                                   'An advertised 1-cent domain secretly carries a $40 charge at checkout',
                                   'Compare renewal costs, fixed fees, and lifetime value instead of '
                                   'first-year prices',
                                   'Create a Pro Website ([08Ekqe45IH0 @ 00:00:14]); Domain Reseller '
                                   '([72rBKTbIECI @ 00:04:03])'],
                                  ['Default trial add-ons stuffed into the cart',
                                   'domain.com loads three trials by default and an email add-on later '
                                   'costs $36 a year',
                                   'Inspect the cart before checkout and strip every trial you did not ask '
                                   'for',
                                   'Luka Knows ([oi-pZAGrrhQ @ 00:04:56])'],
                                  ['DNSSEC left enabled during the nameserver switch',
                                   'Leaving DNSSEC on at the registrar risks DNS failures and site '
                                   'availability disruptions',
                                   'Turn DNSSEC off at the registrar before pasting in Cloudflare name '
                                   'servers',
                                   'PMN Online ([AKtcv_vFlSY @ 00:01:13])'],
                                  ['Mail and verification records left proxied',
                                   'MX and verification records behind the orange cloud stop working '
                                   'correctly',
                                   'Switch those records to grey-cloud DNS only and keep web records '
                                   'proxied',
                                   'Easytorial ([sx83eEm6nk4 @ 00:03:23])'],
                                  ['Locked name servers on Cloudflare-registered domains',
                                   'Name servers cannot be changed, creating friction with dedicated '
                                   'shared web hosts',
                                   'Use Cloudflare Registrar with setups like Amazon AWS, register '
                                   'elsewhere for shared hosting',
                                   'David Utke ([UkMYRY9wDN0 @ 00:13:15])'],
                                  ['Typo on a non-refundable registration',
                                   'Cloudflare Registrar gives zero grace period, so a mistyped name burns '
                                   'the fee',
                                   'Double check spelling, or use Dynadot for its five-day grace deletion '
                                   'as credit',
                                   'Design Guy ([chataozFYGw @ 00:01:00])'],
                                  ['Slow third-party email forwarding services',
                                   'Craylor saw forwarded emails stuck for an extra hour or two with other '
                                   'services',
                                   'Run forwarding through Cloudflare, where he reports emails are '
                                   'forwarded instantly',
                                   'Craylor ([IXpvUD5SDzA @ 00:05:06])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Checkout and Pre-Cutover Gate',
                           'body': 'Clear all four checks before buying, moving, or repointing a single '
                                   'name in the portfolio.',
                           'items': ["Turn DNSSEC off at the registrar before pasting Cloudflare's two "
                                     'name servers, and allow up to 48 hours for worldwide propagation '
                                     '[PMN Online — AKtcv_vFlSY @ 00:01:13].',
                                     'Review every record Cloudflare imports, especially the root A record '
                                     'and the www CNAME, and keep MX and verification records on '
                                     'grey-cloud DNS only [Easytorial — sx83eEm6nk4 @ 00:01:08].',
                                     'Confirm the exact spelling before buying at Cloudflare Registrar, '
                                     'because new registrations are completely non-refundable with no '
                                     'grace period [Design Guy — chataozFYGw @ 00:01:00].',
                                     'Walk away from any registrar that charges for WHOIS privacy, which '
                                     'David Utke calls non-negotiable and Luka Knows calls a complete red '
                                     'flag [David Utke — UkMYRY9wDN0 @ 00:04:17].']}}],
 'pull_quote': '"The best practice in this space is always keep your web hosting and domain name separate. '
               'It is cheaper and also safer." — Luka Knows (oi-pZAGrrhQ @ 00:05:37).',
 'diagram_id': 'diag-04',
 'action_checklist': ['Register portfolio names at a dedicated registrar rather than a web host, keeping '
                      'hosting and domains separate to avoid a single point of failure [Luka Knows — '
                      'oi-pZAGrrhQ @ 00:05:37].',
                      'Onboard each domain in Cloudflare through Account Home, choose quick scan for DNS '
                      'records, pick the free plan, and click continue to activation [George Basics — '
                      'aeqNGnkQgbA @ 00:00:34].',
                      'At Dynadot, open the domain, go to DNS settings, select name servers, tick enter '
                      'new or existing name servers, paste both Cloudflare name servers, and click save '
                      'name servers [George Basics — aeqNGnkQgbA @ 00:01:06].',
                      'At Porkbun, click the NS button under the domain, paste the first and second '
                      'Cloudflare name servers, click submit, then return to Cloudflare and wait a few '
                      'hours [George Basics — OuQbsdwFTA0 @ 00:01:13].',
                      'Add each record by choosing the type, setting the name to @ for the root or www for '
                      'a subdomain, entering the content destination, leaving TTL on auto, and setting '
                      'proxy status [PMN Online — piq0yLKq_SE @ 00:02:05].',
                      'Before listing a BigRock domain on Afternic or Sedo, revert to the old look, open '
                      'manage orders, opt in to Fast Transfer, and enter the emailed verification code [PG '
                      'Tech Help — 0QCYIFcFO7A @ 00:00:16].'],
 'statutory_citations': [{'title': 'David Utke — The 5 BEST Domain Registrars in 2026: Where to Buy Your '
                                   'Domain Name [00:13:15]',
                          'url': 'https://www.youtube.com/watch?v=UkMYRY9wDN0&t=795s',
                          'relevance': 'Primary practitioner testimony on the locked name server catch at '
                                       'Cloudflare Registrar and registrar pricing benchmarks.'},
                         {'title': 'Design Guy — Porkbun or Cloudflare Registrar? Domain Registration '
                                   'Service Compared for 2026 [00:03:01]',
                          'url': 'https://www.youtube.com/watch?v=mMGvtO-bkPI&t=181s',
                          'relevance': 'Primary practitioner testimony on refund windows, renewal pricing, '
                                       'and transfer costs between Porkbun and Cloudflare Registrar.'},
                         {'title': 'PMN Online — How to Set Cloudflare DNS Easily 2026 [00:01:13]',
                          'url': 'https://www.youtube.com/watch?v=AKtcv_vFlSY&t=73s',
                          'relevance': 'Primary practitioner testimony on disabling DNSSEC before a '
                                       'nameserver switch and propagation timing.'},
                         {'title': "Luka Knows — Where to Buy a Domain in 2026? (Don't choose WRONG!) "
                                   '[00:05:17]',
                          'url': 'https://www.youtube.com/watch?v=oi-pZAGrrhQ&t=317s',
                          'relevance': 'Primary practitioner testimony on bundling risk, renewal traps, '
                                       'and registrar tiering.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'IXpvUD5SDzA',
                       'title': '5 Things to Know BEFORE Using Cloudflare!',
                       'channel': 'Craylor',
                       'author': 'Craylor',
                       'text': 'You still need a hosting account with a provider of your choice to get '
                               'started with Cloudflare.',
                       'tip': 'You still need a hosting account with a provider of your choice to get '
                              'started with Cloudflare.',
                       'timestamp': 85,
                       'timestamp_seconds': 85,
                       'timestamp_label': '[00:01:25]',
                       'url': 'https://www.youtube.com/watch?v=IXpvUD5SDzA&t=85s',
                       'markdown': '[00:01:25](https://www.youtube.com/watch?v=IXpvUD5SDzA&t=85s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'piq0yLKq_SE',
                       'title': 'How to Add DNS Records on Cloudflare Easily 2026',
                       'channel': 'PMN Online',
                       'author': 'PMN Online',
                       'text': "Here you decide whether to enable Cloudflare's proxy feature, which is "
                               'denoted by an orange cloud, or to set it as DNS only, indicated by a gray '
                               'cloud.',
                       'tip': "Here you decide whether to enable Cloudflare's proxy feature, which is "
                              'denoted by an orange cloud, or to set it as DNS only, indicated by a gray '
                              'cloud.',
                       'timestamp': 174,
                       'timestamp_seconds': 174,
                       'timestamp_label': '[00:02:54]',
                       'url': 'https://www.youtube.com/watch?v=piq0yLKq_SE&t=174s',
                       'markdown': '[00:02:54](https://www.youtube.com/watch?v=piq0yLKq_SE&t=174s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RClpPcLHviU',
                       'title': 'Porkbun Review 2026 | Is Porkbun Worth It for Domain Registration?',
                       'channel': 'SEARCHLIGHT HQ',
                       'author': 'SEARCHLIGHT HQ',
                       'text': 'Instead of relying heavily on extremely cheap introductory offers followed '
                               'by expensive renewals, Porkbun aims to keep domain prices competitive and '
                               'transparent.',
                       'tip': 'Instead of relying heavily on extremely cheap introductory offers followed '
                              'by expensive renewals, Porkbun aims to keep domain prices competitive and '
                              'transparent.',
                       'timestamp': 30,
                       'timestamp_seconds': 30,
                       'timestamp_label': '[00:00:30]',
                       'url': 'https://www.youtube.com/watch?v=RClpPcLHviU&t=30s',
                       'markdown': '[00:00:30](https://www.youtube.com/watch?v=RClpPcLHviU&t=30s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ul52eFQneY0',
                       'title': 'Best Domain Registrars for Free Extras: 5 Compared on the Specs That '
                                'Matter',
                       'channel': "Jake's Tech Lab",
                       'author': "Jake's Tech Lab",
                       'text': 'At number one, your cleanest overall winner is Cloudflare Registrar.',
                       'tip': 'At number one, your cleanest overall winner is Cloudflare Registrar.',
                       'timestamp': 82,
                       'timestamp_seconds': 82,
                       'timestamp_label': '[00:01:22]',
                       'url': 'https://www.youtube.com/watch?v=ul52eFQneY0&t=82s',
                       'markdown': '[00:01:22](https://www.youtube.com/watch?v=ul52eFQneY0&t=82s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sx83eEm6nk4',
                       'title': 'How to Set Up and Manage Domain and DNS on Cloudflare [In 3 steps]',
                       'channel': 'Easytorial',
                       'author': 'Easytorial',
                       'text': "If you're setting up records for email like MX or verification values, "
                               "switch to DNS only grey cloud. Otherwise, those services won't work "
                               'correctly.',
                       'tip': "If you're setting up records for email like MX or verification values, "
                              "switch to DNS only grey cloud. Otherwise, those services won't work "
                              'correctly.',
                       'timestamp': 203,
                       'timestamp_seconds': 203,
                       'timestamp_label': '[00:03:23]',
                       'url': 'https://www.youtube.com/watch?v=sx83eEm6nk4&t=203s',
                       'markdown': '[00:03:23](https://www.youtube.com/watch?v=sx83eEm6nk4&t=203s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '08Ekqe45IH0',
                       'title': "Don't Buy a Domain Until You Watch This! (Best Domain Name Registrars "
                                '2026)',
                       'channel': 'Create a Pro Website',
                       'author': 'Create a Pro Website',
                       'text': 'They say that the domain name costs 1 cent, but they secretly charge $40.',
                       'tip': 'They say that the domain name costs 1 cent, but they secretly charge $40.',
                       'timestamp': 14,
                       'timestamp_seconds': 14,
                       'timestamp_label': '[00:00:14]',
                       'url': 'https://www.youtube.com/watch?v=08Ekqe45IH0&t=14s',
                       'markdown': '[00:00:14](https://www.youtube.com/watch?v=08Ekqe45IH0&t=14s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oi-pZAGrrhQ',
                       'title': "Where to Buy a Domain in 2026? (Don't choose WRONG!)",
                       'channel': 'Luka Knows',
                       'author': 'Luka Knows',
                       'text': 'The best practice in this space is always keep your web hosting and domain '
                               'name separate. It is cheaper and also safer.',
                       'tip': 'The best practice in this space is always keep your web hosting and domain '
                              'name separate. It is cheaper and also safer.',
                       'timestamp': 337,
                       'timestamp_seconds': 337,
                       'timestamp_label': '[00:05:37]',
                       'url': 'https://www.youtube.com/watch?v=oi-pZAGrrhQ&t=337s',
                       'markdown': '[00:05:37](https://www.youtube.com/watch?v=oi-pZAGrrhQ&t=337s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '72rBKTbIECI',
                       'title': 'Stop Overpaying for Domain Reselling! GoDaddy vs. Domain Name API',
                       'channel': 'Domain Reseller',
                       'author': 'Domain Reseller',
                       'text': 'A program fee is something you pay every year, whatever your sales volume.',
                       'tip': 'A program fee is something you pay every year, whatever your sales volume.',
                       'timestamp': 227,
                       'timestamp_seconds': 227,
                       'timestamp_label': '[00:03:47]',
                       'url': 'https://www.youtube.com/watch?v=72rBKTbIECI&t=227s',
                       'markdown': '[00:03:47](https://www.youtube.com/watch?v=72rBKTbIECI&t=227s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mMGvtO-bkPI',
                       'title': 'Porkbun or Cloudflare Registrar? Domain Registration Service Compared for '
                                '2026',
                       'channel': 'Design Guy',
                       'author': 'Design Guy',
                       'text': 'Pork Bun officially gives you a refund window of 4 days, that is 96 hours '
                               'on a new registration.',
                       'tip': 'Pork Bun officially gives you a refund window of 4 days, that is 96 hours '
                              'on a new registration.',
                       'timestamp': 181,
                       'timestamp_seconds': 181,
                       'timestamp_label': '[00:03:01]',
                       'url': 'https://www.youtube.com/watch?v=mMGvtO-bkPI&t=181s',
                       'markdown': '[00:03:01](https://www.youtube.com/watch?v=mMGvtO-bkPI&t=181s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'AKtcv_vFlSY',
                       'title': 'How to Set Cloudflare DNS Easily 2026',
                       'channel': 'PMN Online',
                       'author': 'PMN Online',
                       'text': 'You must ensure that DNSSEC, which stands for Domain Name System Security '
                               'Extensions, is turned off at your registrar.',
                       'tip': 'You must ensure that DNSSEC, which stands for Domain Name System Security '
                              'Extensions, is turned off at your registrar.',
                       'timestamp': 73,
                       'timestamp_seconds': 73,
                       'timestamp_label': '[00:01:13]',
                       'url': 'https://www.youtube.com/watch?v=AKtcv_vFlSY&t=73s',
                       'markdown': '[00:01:13](https://www.youtube.com/watch?v=AKtcv_vFlSY&t=73s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'aeqNGnkQgbA',
                       'title': 'How To Setup Cloudflare With Dynadot Domain - Full Guide',
                       'channel': 'George Basics',
                       'author': 'George Basics',
                       'text': 'Paste the first name server we just copied from Cloudflare. Then copy the '
                               'second one and paste it in the second row. Then click save name servers.',
                       'tip': 'Paste the first name server we just copied from Cloudflare. Then copy the '
                              'second one and paste it in the second row. Then click save name servers.',
                       'timestamp': 84,
                       'timestamp_seconds': 84,
                       'timestamp_label': '[00:01:24]',
                       'url': 'https://www.youtube.com/watch?v=aeqNGnkQgbA&t=84s',
                       'markdown': '[00:01:24](https://www.youtube.com/watch?v=aeqNGnkQgbA&t=84s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'OuQbsdwFTA0',
                       'title': 'How To Setup Cloudflare With Porkbun Domain (Step By Step)',
                       'channel': 'George Basics',
                       'author': 'George Basics',
                       'text': 'You need to click on it and we need to paste our name servers right here. '
                               "First one and then the second one. Click submit and that's all.",
                       'tip': 'You need to click on it and we need to paste our name servers right here. '
                              "First one and then the second one. Click submit and that's all.",
                       'timestamp': 73,
                       'timestamp_seconds': 73,
                       'timestamp_label': '[00:01:13]',
                       'url': 'https://www.youtube.com/watch?v=OuQbsdwFTA0&t=73s',
                       'markdown': '[00:01:13](https://www.youtube.com/watch?v=OuQbsdwFTA0&t=73s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hdvK17zvRgk',
                       'title': 'Cloudflare vs Porkbun Domain - 2025 Comparison',
                       'channel': 'The Lone Crater',
                       'author': 'The Lone Crater',
                       'text': 'Opt for Porkbun if your main focus is cost-effective domain registration, '
                               'a vast array of unique domain extensions, and a straightforward, '
                               'user-friendly management experience.',
                       'tip': 'Opt for Porkbun if your main focus is cost-effective domain registration, a '
                              'vast array of unique domain extensions, and a straightforward, '
                              'user-friendly management experience.',
                       'timestamp': 122,
                       'timestamp_seconds': 122,
                       'timestamp_label': '[00:02:02]',
                       'url': 'https://www.youtube.com/watch?v=hdvK17zvRgk&t=122s',
                       'markdown': '[00:02:02](https://www.youtube.com/watch?v=hdvK17zvRgk&t=122s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UkMYRY9wDN0',
                       'title': 'The 5 BEST Domain Registrars in 2026: Where to Buy Your Domain Name',
                       'channel': 'David Utke',
                       'author': 'David Utke',
                       'text': 'The catch is that you cannot change the name servers of a domain name '
                               'registered with Cloudflare.',
                       'tip': 'The catch is that you cannot change the name servers of a domain name '
                              'registered with Cloudflare.',
                       'timestamp': 795,
                       'timestamp_seconds': 795,
                       'timestamp_label': '[00:13:15]',
                       'url': 'https://www.youtube.com/watch?v=UkMYRY9wDN0&t=795s',
                       'markdown': '[00:13:15](https://www.youtube.com/watch?v=UkMYRY9wDN0&t=795s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UkMYRY9wDN0',
                       'title': 'The 5 BEST Domain Registrars in 2026: Where to Buy Your Domain Name',
                       'channel': 'David Utke',
                       'author': 'David Utke',
                       'text': "Then you get domain name privacy included and it's free forever. And you "
                               'need domain name privacy. This is non-negotiable.',
                       'tip': "Then you get domain name privacy included and it's free forever. And you "
                              'need domain name privacy. This is non-negotiable.',
                       'timestamp': 257,
                       'timestamp_seconds': 257,
                       'timestamp_label': '[00:04:17]',
                       'url': 'https://www.youtube.com/watch?v=UkMYRY9wDN0&t=257s',
                       'markdown': '[00:04:17](https://www.youtube.com/watch?v=UkMYRY9wDN0&t=257s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'chataozFYGw',
                       'title': 'Cloudflare Registrar vs Dynadot — Which Wins for Domain Registration in '
                                '2026?',
                       'channel': 'Design Guy',
                       'author': 'Design Guy',
                       'text': 'With Cloudflare registrar, the policy is absolute. Brand new domain '
                               'registrations are completely non-refundable.',
                       'tip': 'With Cloudflare registrar, the policy is absolute. Brand new domain '
                              'registrations are completely non-refundable.',
                       'timestamp': 60,
                       'timestamp_seconds': 60,
                       'timestamp_label': '[00:01:00]',
                       'url': 'https://www.youtube.com/watch?v=chataozFYGw&t=60s',
                       'markdown': '[00:01:00](https://www.youtube.com/watch?v=chataozFYGw&t=60s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0QCYIFcFO7A',
                       'title': 'How To Enable Fast Transfer In BigRock and Sell Your Domain To Afternic '
                                'or Sedo?',
                       'channel': 'PG Tech Help',
                       'author': 'PG Tech Help',
                       'text': 'Click on manage orders and then you need to click on fast transfer and '
                               'click on opt in option.',
                       'tip': 'Click on manage orders and then you need to click on fast transfer and '
                              'click on opt in option.',
                       'timestamp': 16,
                       'timestamp_seconds': 16,
                       'timestamp_label': '[00:00:16]',
                       'url': 'https://www.youtube.com/watch?v=0QCYIFcFO7A&t=16s',
                       'markdown': '[00:00:16](https://www.youtube.com/watch?v=0QCYIFcFO7A&t=16s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'}]}
