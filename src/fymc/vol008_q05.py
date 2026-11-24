from __future__ import annotations

CHAPTER_5 = {'id': 'Q5',
 'chapter_id': 'Q5',
 'chapter_number': 5,
 'question_number': 5,
 'slug': 'email-infrastructure-and-deliverability',
 'question_prompt': 'How do operators configure sending infrastructure and diagnose the setup failures '
                    'that prevent outreach emails from reaching inboxes?',
 'kicker': 'Q5 / THE BIG MONEY PLAYBOOKS',
 'title': 'Email Infrastructure and Deliverability',
 'subtitle': 'Domains, DNS, SPF, DKIM, DMARC, mailbox providers, warm-up, Google Workspace and Microsoft '
             '365 configuration, GoHighLevel setup, and deliverability troubleshooting',
 'layout_template': 'case_study',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners converge on one operating model: never cold-email from the main brand '
                      'domain, buy lookalike secondary domains, put two or three Google Workspace or '
                      'Outlook mailboxes on each, publish SPF, DKIM, DMARC, and MX, and warm every inbox '
                      'two to four weeks before launch. The numbers cluster tightly: 15 to 50 cold sends '
                      'per inbox per day, warmup ramps starting at two to ten emails, 50/50 cold-to-warmup '
                      'splits, and automatic campaign pauses at 4 to 5 percent bounce. Smartlead operators '
                      'report 49 percent of Gmail inboxes burning overnight and reply rates crashing below '
                      '0.5 percent on static copy until spintax went in. Disagreements are real: Damien of '
                      'MailReach tolerates up to 100 sends per address, Kyle Dickson rotates half the '
                      'fleet into rest monthly, and Coldbot insists authentication and warmup are '
                      'prerequisites that guarantee nothing.',
 'key_metrics': [{'label': 'Gmail inboxes burned overnight',
                  'metric': 'Gmail inboxes burned overnight',
                  'value': 'Over 49% of Gmail inboxes dead in one night',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Agency operator woke up to nearly half their Gmail sending inboxes burned '
                             'and spent hundreds of dollars on replacement domains to keep client '
                             'campaigns running.',
                  'source': 'Smartlead ([GZEdhosrYRc @ 00:00:00])'},
                 {'label': 'Reply-rate collapse on static copy',
                  'metric': 'Reply-rate collapse on static copy',
                  'value': 'Below 0.5% versus a normal floor of about 2%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Client campaigns using identical static copy in every email dropped under '
                             '0.5% replies; the fix was AI spintax variation inside Smartlead.',
                  'source': 'Smartlead ([GZEdhosrYRc @ 00:02:09])'},
                 {'label': 'Inbox rate with always-on background warmup',
                  'metric': 'Inbox rate with always-on background warmup',
                  'value': 'Between 95% and 97% inbox rate month after month',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Team sending 2 million cold emails a year credits never switching off '
                             'low-level background warmup, even during campaign pauses.',
                  'source': 'Smartlead ([DIUObYQih3s @ 00:09:29])'},
                 {'label': 'Catch-all bounce share',
                  'metric': 'Catch-all bounce share',
                  'value': 'Around 23% of catch-all addresses bounce',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'MailReach data on risky/catch-all verifier results; drives the rule of '
                             'capping catch-alls at 20% of each list.',
                  'source': 'Damien - MailReach ([8EaKo_iAiPE @ 00:06:42])'}],
 'sections': [{'title': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every operator in this set treats the main brand domain as untouchable for '
                              "cold outreach. Smartlead's agency operator frames it with coca-cola.com: "
                              'blast from that domain and it is only a matter of time before it gets '
                              'flagged, and then mail to friends, family, colleagues, investors, and '
                              'partners starts landing in spam too [GZEdhosrYRc @ 00:04:45]. TechSales '
                              'opens with the same nightmare in story form: cold emails go out from the '
                              'company domain, replies stop within a week, and finance reports that '
                              'customer invoices are hitting spam [aa7B2gisZdU @ 00:00:01]. CRMOZ puts a '
                              'number on the trigger, warning that 5,000 cold marketing emails from '
                              'yourcompany.com plus a wave of spam reports gets the domain blacklisted and '
                              'real clients stop receiving invoices; the fix is a lookalike secondary '
                              'domain such as yourcompany.net [T9cn3UyRkR8 @ 00:04:01]. Ethan Fleming paid '
                              'for this lesson directly: a Zapier automation sending lead data from their '
                              "main email wrecked their domain reputation, their proposal hit a prospect's "
                              'spam filter, and they lost a $2,000-a-month client [TB1PQrXx5s8 @ '
                              '00:08:53]. The shared rule is operational separation: buy close-to-brand '
                              'sending domains, keep them clean of hyphens and numbers, and let the '
                              'primary domain handle invoices, support, and partner mail only.',
                              'The second point of agreement is provider choice and spreading load thin. '
                              'Smartlead\'s operator calls SMTP inboxes "absolute rubbish" after three '
                              'years of daily outreach, says they were the first setups wiped out when '
                              'Gmail and Microsoft tightened filters, and calls Google and Outlook the '
                              'Nike and Adidas of infrastructure [GZEdhosrYRc @ 00:01:20]. Damien of '
                              'MailReach rates Google Workspace or Office 365 mailboxes an absolute game '
                              'changer and names a custom SMTP server the worst possible setup for landing '
                              'in the inbox [8EaKo_iAiPE @ 00:02:42]. On density, the numbers converge: '
                              'two to three mailboxes per domain from Kyle Dickson, who warns that if the '
                              'domain gets destroyed every inbox on it dies with it [drsocawArfo @ '
                              '00:04:41]. Coldbot frames the domain as the building and mailboxes as '
                              'rooms, so one hundred addresses on one new domain is still concentrated '
                              "risk, and argues that Google Workspace's technical ceiling is not a "
                              "cold-outreach target; Instantly's documentation recommends around thirty "
                              'campaign emails per day for regular mailboxes [fM-ywBq8yoU @ 00:03:43]. The '
                              'working rule that falls out: when more volume is needed, add healthy '
                              'inboxes and domains rather than turning one inbox into a fire hose.',
                              'Authentication and warmup are the table stakes nobody skips, and nobody '
                              "oversells. Smartlead's team, claiming 2 million cold emails sent in a year "
                              'and more than 300 campaigns reviewed, lists four non-negotiables before '
                              'warmup even begins, with SPF, DKIM, DMARC, and MX records all set up and '
                              'verified at the top of the list [DIUObYQih3s @ 00:02:27]. TechSales '
                              'compresses the trio into three questions an operator can remember: SPF '
                              'answers who can send, DKIM answers whether the message is really from you, '
                              'and DMARC decides what to do if it does not check out [aa7B2gisZdU @ '
                              "00:05:26]. Kyle Dickson's version is the bluntest of all: warm every inbox "
                              'two to three weeks minimum before a single cold send, keep warmup running '
                              'forever, and never shut it off [drsocawArfo @ 00:00:15]. Coldbot supplies '
                              'the necessary cold water: you can have SPF, DKIM, and DMARC and still get '
                              'poor placement, because authentication proves identity but does not force '
                              'Gmail or Outlook to like your sending behavior, and a warmed inbox can '
                              'still be damaged by bad data, complaints, or sudden volume spikes '
                              '[fM-ywBq8yoU @ 00:05:42]. The consensus position is that both are '
                              'prerequisites, not guarantees, and the infrastructure has to be monitored '
                              'after launch rather than treated as a one-time checklist.'],
               'table': {'caption': 'Infrastructure rules multiple practitioners agree on before the first '
                                    'cold send',
                         'headers': ['Consensus Rule',
                                     'What the Practitioner Says',
                                     'Operator Takeaway',
                                     'Expert Source'],
                         'rows': [['Never send cold email from the main brand domain',
                                   'Cold sends from coca-cola.com eventually push friends, investors, and '
                                   'partners mail into spam',
                                   'Buy lookalike secondary domains and keep the primary domain for daily '
                                   'business',
                                   'Smartlead ([GZEdhosrYRc @ 00:04:45])'],
                                  ['Send only from Google Workspace or Office 365 mailboxes',
                                   'A custom SMTP server is named the worst setup for landing in the inbox',
                                   'Skip cheap SMTP inboxes even though they cost roughly half as much',
                                   'Damien - MailReach ([8EaKo_iAiPE @ 00:02:42])'],
                                  ['Cap each sending domain at two or three mailboxes',
                                   'If the domain gets destroyed, every inbox sitting on that domain dies '
                                   'too',
                                   'Scale volume by adding domains, not by stacking more inboxes per '
                                   'domain',
                                   'Kyle Dickson ([drsocawArfo @ 00:04:41])'],
                                  ['Publish SPF, DKIM, and DMARC on every sending domain',
                                   'SPF says who can send, DKIM proves origin, DMARC sets the failure '
                                   'rules',
                                   'Start DMARC at none and tighten once reports show everything works',
                                   'TechSales ([aa7B2gisZdU @ 00:05:26])'],
                                  ['Warm every new inbox before the first cold campaign',
                                   'Start at five to ten per day and increase slowly over two to three '
                                   'weeks',
                                   'Leave low-level background warmup running indefinitely, even during '
                                   'campaign pauses',
                                   'Smartlead ([DIUObYQih3s @ 00:01:37])'],
                                  ['Keep daily cold sends per inbox deliberately low',
                                   'Stay under about 40 emails per day from each warmed inbox',
                                   'Need more volume? Add another warmed inbox for roughly 40 more daily '
                                   'sends',
                                   'Justin Davis ([35rkCLq5LC4 @ 00:01:45])'],
                                  ['Treat authentication and warmup as prerequisites, not guarantees',
                                   'Fully authenticated domains can still see poor inbox placement from '
                                   'sending behavior',
                                   'Seed-test Gmail and Outlook accounts you control before launching any '
                                   'harder',
                                   'Coldbot ([fM-ywBq8yoU @ 00:05:42])']]}},
              {'title': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["The DNS work is mechanical once you know the traps. Stewart Gauld's Google "
                              'Workspace walkthrough: in the Admin console go to Apps, Gmail, Authenticate '
                              'email, generate a new DKIM record, keep the 2048-bit key length rather than '
                              '1024 because it is more secure, keep the google prefix, paste the host name '
                              'and TXT value into DNS, then click start authentication and allow up to 48 '
                              'hours to propagate [fsZaEce18FE @ 00:03:43]. For Microsoft 365, SalesBlink '
                              'points to the Defender portal instead: open Email authentication settings, '
                              'the DKIM tab, add the two CNAME records selector1 and selector2, then '
                              'switch on DKIM signing, while the SPF value swaps Google for '
                              'spf.protection.outlook.com [8sprCYGSnpI @ 00:01:33]. CRMOZ, drawing on '
                              'their audits, says never create two SPF records, because it is like handing '
                              'the bouncer two different guest lists, and that one extra space or typo '
                              'kills delivery outright; they also want a separate DKIM for every sending '
                              'tool [T9cn3UyRkR8 @ 00:01:24]. On DMARC, Frankee Muryan runs p=none for the '
                              'first 6 to 12 months unless the brand is big enough to attract spoofing, '
                              'roughly 300k monthly website visitors, and pastes the zipped daily reports '
                              'into ChatGPT to read them [YWsrDI9jLXk @ 00:05:40].',
                              'Warmup settings are where the numbers get specific. Kyle Dickson sets '
                              "Instantly's ramp at two warmup emails per day per inbox, climbing two, "
                              'four, six, eight up to a cap of 30, with a warmup reply rate somewhere '
                              'between 65 and 95 percent but never 100, because a perfect reply rate '
                              'followed by a normal cold campaign looks suspicious; their hard ceiling is '
                              '50 sends per inbox per day, split 20 cold and 30 warm [drsocawArfo @ '
                              "00:04:20]. Smartlead's agency operator starts bulk warmup at five per day "
                              'with a daily ramp of five and a 20 percent reply rate, then runs a 50/50 '
                              'split once campaigns go live, for example 15 cold plus 15 warmup per day '
                              '[GZEdhosrYRc @ 00:10:25]. The other Smartlead presenter publishes a '
                              'week-by-week curve: 5 to 10 warmup emails in week one, 20 to 30 in week '
                              'two, 30 to 40 from week three on, warmup reply rate at 30 to 40 percent, '
                              'and at least four weeks before launch if you can afford the wait '
                              '[DIUObYQih3s @ 00:06:10]. For sizing, TechSales does the arithmetic: 500 '
                              'people a day at 40 per mailbox is 13 mailboxes, which at two or three per '
                              'domain is five domains [aa7B2gisZdU @ 00:02:28].',
                              "Content and campaign settings carry their own hard rules. Smartlead's "
                              'operator calls HTML the single biggest deliverability killer, turns on '
                              'plain text mode under delivery optimization, switches off open and click '
                              'tracking because the pixel forces HTML and Apple devices skew the stats '
                              'anyway, and sets high bounce rate auto-protection to 5 so the campaign '
                              'pauses itself at a 5 percent bounce rate [GZEdhosrYRc @ 00:14:23]. Kyle '
                              'Dickson runs the same kill switch tighter, pausing at 4 percent, and claims '
                              'images or links in the first email cut deliverability roughly in half, so '
                              'any link or image goes in the last email of the sequence [drsocawArfo @ '
                              '00:11:25]. Both push spintax hard: Kyle wants variations on nearly every '
                              'sentence for 50 or 60 possible combinations, while the Smartlead operator '
                              'watched reply rates collapse below 0.5 percent on static copy against a '
                              'normal floor of 2 percent before adding AI spintax through an OpenAI key '
                              '[GZEdhosrYRc @ 00:02:09]. On lists, Damien of MailReach says roughly 23 '
                              'percent of catch-all addresses bounce, so cap catch-alls at 20 percent of '
                              'every list instead of burning through valid addresses first and then going '
                              'all in on catch-alls [8EaKo_iAiPE @ 00:07:24].'],
               'table': {'caption': 'Exact settings, numbers, and tools practitioners run in production',
                         'headers': ['Mechanic',
                                     'Exact Setting or Number',
                                     'Why It Matters',
                                     'Expert Source'],
                         'rows': [['Warmup ramp configuration inside the Instantly dashboard',
                                   'Start at two per day, add two daily, cap at 30',
                                   'Reply rate set between 65 and 95 percent, never a suspicious 100',
                                   'Kyle Dickson ([drsocawArfo @ 00:01:32])'],
                                  ['Cold plus warmup split once live campaigns run',
                                   'A 50/50 split, for example 15 cold and 15 warmup per day',
                                   'Keeps domains and mailboxes alive longer instead of burning them '
                                   'overnight',
                                   'Smartlead ([GZEdhosrYRc @ 00:10:25])'],
                                  ['Bounce auto-pause kill switch in campaign protection settings',
                                   'High bounce rate auto-protection toggled on and set to 5 percent',
                                   'Campaign pauses itself before bounces damage long-term domain and '
                                   'mailbox health',
                                   'Smartlead ([GZEdhosrYRc @ 00:14:23])'],
                                  ['Domain sizing calculator for monthly prospect volume planning',
                                   '3,000 prospects times 3 emails needs about 15 mailboxes and 7 domains',
                                   'Assumes 25 emails per domain per day; the sheet is free to copy',
                                   'Smartlead ([GZEdhosrYRc @ 00:08:01])'],
                                  ['Catch-all ratio control during every list preparation pass',
                                   'Cap catch-all addresses at 20 percent of each campaign list',
                                   'Roughly 23 percent of catch-alls bounce, so uncontrolled use spikes '
                                   'bounce rate',
                                   'Damien - MailReach ([8EaKo_iAiPE @ 00:07:24])'],
                                  ['DKIM key generation inside the Google Workspace Admin console',
                                   'Keep the 2048-bit key length and the default google prefix',
                                   'More secure key; allow up to 48 hours for DNS propagation',
                                   'Stewart Gauld ([fsZaEce18FE @ 00:04:03])'],
                                  ['Domain cost and naming rules for new sending domains',
                                   'Roughly $15 per domain; avoid hyphens, numbers, and exotic extensions',
                                   'Cheap enough that spreading risk across many domains always pays off',
                                   'Damien - MailReach ([8EaKo_iAiPE @ 00:02:18])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Small moves the operators swear by',
                           'body': 'Low-cost habits that catch problems before prospects see them and keep '
                                   'links from torching the first touch.',
                           'items': ['Put two of your own email addresses at the top of every campaign '
                                     'list so the first sends hit you; check formatting, links, and inbox '
                                     'versus spam before a single prospect sees it [Justin Davis — '
                                     '35rkCLq5LC4 @ 00:00:00].',
                                     'Never put the resource link in email one: ask the prospect to reply '
                                     'a trigger word like "pink," then fire a subsequence that delivers '
                                     'the link only to people who replied with that word [Smartlead — '
                                     'GZEdhosrYRc @ 00:12:47].',
                                     'Set up a custom tracking domain in your sending tool; without it '
                                     'your emails carry the same tracking domain as every other user of '
                                     'that tool, which multiplies spam risk [Damien - MailReach — '
                                     '8EaKo_iAiPE @ 00:04:47].',
                                     'Redirect every new sending domain to your main website; a prospect '
                                     'who searches the lookalike domain and hits an error page loses '
                                     'trust, which Kidous Mahteme names as a big reason cold email fails '
                                     '[Kidous Mahteme - Inframail Cold Email Inboxes — EN_hwXy6LyU @ '
                                     '00:02:10].']},
               'sop_steps': [{'step': 1,
                              'title': 'Buy and size the sending domains',
                              'action': 'Purchase close-to-brand .com lookalike domains and size mailbox '
                                        'count from monthly volume.',
                              'detail': 'Use names like getexample.com or examplehq.com, avoid hyphens and '
                                        'numbers, point each domain to the main website, and run the math: '
                                        '500 people a day at 40 per mailbox is 13 mailboxes across five '
                                        'domains at two or three mailboxes each [TechSales — aa7B2gisZdU @ '
                                        '00:01:44].'},
                             {'step': 2,
                              'title': 'Authenticate every domain',
                              'action': 'Publish one SPF record, a DKIM record from the mailbox provider, '
                                        'a DMARC record, and MX.',
                              'detail': 'In Google Admin go to Apps, Gmail, Authenticate email, generate a '
                                        '2048-bit DKIM key, paste the TXT host and value into DNS, add a '
                                        '_dmarc TXT record with your report email, then confirm with '
                                        'Google Admin Toolbox Check MX [Stewart Gauld — fsZaEce18FE @ '
                                        '00:04:03].'},
                             {'step': 3,
                              'title': 'Warm before the first cold send',
                              'action': 'Turn on warmup for every inbox and let it ramp for 14 to 21 days.',
                              'detail': 'Ramp two warmup emails per day up to a 30 cap, set the warmup '
                                        'reply rate between 65 and 95 percent, then ramp cold sends the '
                                        'same way to 15 to 20 per day while keeping total sends at 50 or '
                                        'fewer per inbox [Kyle Dickson — drsocawArfo @ 00:01:32].'},
                             {'step': 4,
                              'title': 'Launch with guardrails on',
                              'action': 'Enable plain text mode, disable open and click tracking, and set '
                                        'bounce auto-protection.',
                              'detail': 'Inside campaign protection and limits, switch on high bounce rate '
                                        'auto-protection at 5 so the campaign pauses itself once 5 percent '
                                        'of sends bounce, and keep warmup running alongside live campaigns '
                                        '[Smartlead — GZEdhosrYRc @ 00:14:23].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Nobody agrees on a single daily ceiling, so the cap is a dial each operator '
                              "sets. Smartlead's agency operator plugs 25 emails per domain per day into a "
                              'free sending-volume calculator and insists on a 50/50 split once campaigns '
                              'go live: 15 cold sends matched by 15 warm-up sends per inbox, so domains '
                              'and mailboxes keep a healthier longevity [GZEdhosrYRc @ 00:10:25]. '
                              "Smartlead's 2-million-email team keeps each inbox under 30 to 40 daily "
                              'sends, randomizes slightly, and ramps warm-up into that same 30 to 40 band '
                              '[DIUObYQih3s @ 00:03:33]. Kyle Dickson caps total traffic at 50 per inbox, '
                              'split as 20 cold and 30 warm, and ramps the cold side 2, 4, 6, 8, 10 over a '
                              'week or two after the 14-to-21-day warm-up ends [drsocawArfo @ 00:04:20]. '
                              'Damien of MailReach sits at the aggressive end: up to 100 cold emails per '
                              'day per address, but only on Google Workspace or Office 365, dropping to 50 '
                              'or fewer on any other provider because results come in lower [8EaKo_iAiPE @ '
                              '00:05:05]. The common thread is scaling horizontally. When one inbox hits '
                              'its ceiling, every one of these operators adds mailboxes and domains rather '
                              'than pushing the same account harder, because the risk of burning a single '
                              'overloaded inbox multiplies with every extra send.',
                              "The sharpest split is over cheap SMTP. Smartlead's agency operator calls "
                              'SMTP inboxes most of the time absolute rubbish after three years of daily '
                              'outreach, says they were the first setups wiped out when Gmail and '
                              'Microsoft tightened their filters, and tells operators to buy only Google '
                              'or Outlook even though SMTP runs half the price [GZEdhosrYRc @ 00:01:20]. '
                              'Damien backs that hard line: a custom SMTP or custom mail server is the '
                              'worst setup for landing in the inbox, because Workspace and Office 365 own '
                              'most of the mailbox market and nothing enters a Google or Microsoft home '
                              'better than another Google or Microsoft mailbox [8EaKo_iAiPE @ 00:03:26]. '
                              "Smartlead's own SmartSenders launch argues the opposite hedge: which "
                              'provider delivers best changes every other week, so a diverse email '
                              'infrastructure is the biggest defensibility metric, and the shopping cart '
                              'sells Google, Outlook, and SMTP through Mail Reef side by side [GYd8Y73SCGE '
                              '@ 00:02:05]. Digitellix runs a different lane entirely, pairing an email '
                              'app with Amazon SES, SendGrid, or Mailgun, warning that running your own '
                              'SMTP server means owning every reputation problem, and keeping a shared IP '
                              'rather than a dedicated one under roughly 100,000 emails a month '
                              '[iM8vOv1pK8g @ 00:02:01].',
                              'Domain architecture splits along two lines. Ethan Fleming uses a mail. '
                              'subdomain for nurtures and newsletters inside GoHighLevel, but tells most '
                              'beginners to buy a burner domain such as contactyourbrand.com, so a '
                              'reputation blow-up stays isolated from the Gmail and Outlook mail the '
                              'business runs on its root domain [TB1PQrXx5s8 @ 00:08:34]. Digitellix goes '
                              'the other way for small senders, mailing from a subdomain like '
                              "news.yourdomain.com so the main domain's everyday mail stays safe, and "
                              'authenticating the exact domain used in the from address [iM8vOv1pK8g @ '
                              '00:03:05]. The second fight is links versus unsubscribe. Kyle Dickson '
                              'strips every image and link from the first email, saying either one can cut '
                              'deliverability roughly in half, explains that open tracking is itself a '
                              'one-by-one pixel image that Google and Outlook caught on to, and saves any '
                              'link or image for the last email of the sequence [drsocawArfo @ 00:11:07]. '
                              'Damien demands an easy-to-spot, working unsubscribe link in every email, '
                              'warning that without one the spam complaint rate skyrockets and destroys '
                              'sender reputation in no time, and that asking prospects to reply '
                              'unsubscribe does not count [8EaKo_iAiPE @ 00:10:40]. On the opening email, '
                              'those two rules are in direct conflict.'],
               'table': {'caption': 'Competing playbooks on daily caps, warm-up settings, providers, '
                                    'domain structure, and links',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Cold sends per mailbox per day',
                                   'Keep each inbox under 30 to 40 daily sends and randomize slightly',
                                   'Push up to 100 per address, but only on Workspace or Office 365',
                                   'Smartlead ([DIUObYQih3s @ 00:03:33]); Damien - MailReach ([8EaKo_iAiPE '
                                   '@ 00:05:05])'],
                                  ['Cold-to-warm ratio once campaigns are live',
                                   'Run a strict 50/50 split of 15 cold and 15 warm per inbox',
                                   'Cap at 50 total sends per inbox, split 20 cold and 30 warm',
                                   'Smartlead ([GZEdhosrYRc @ 00:10:25]); Kyle Dickson ([drsocawArfo @ '
                                   '00:04:20])'],
                                  ['Warm-up reply rate setting inside the sending tool',
                                   'Set warm-up replies near 20% with a five-per-day daily ramp-up',
                                   'Pick a random figure between 65 and 95% like 83, never 100%',
                                   'Smartlead ([GZEdhosrYRc @ 00:08:54]); Kyle Dickson ([drsocawArfo @ '
                                   '00:02:05])'],
                                  ['Warm-up length before the first cold campaign',
                                   'Hold 14 to 21 days minimum and never switch warm-up off',
                                   'Stay at least four weeks, holding 30 to 40 daily through weeks five '
                                   'and six',
                                   'Kyle Dickson ([drsocawArfo @ 00:00:50]); Smartlead ([DIUObYQih3s @ '
                                   '00:06:10])'],
                                  ['Sending domain structure for outbound volume',
                                   'Buy a burner lookalike domain for most beginners to isolate any damage',
                                   'Send from a subdomain like news.yourdomain.com to protect everyday '
                                   'mail',
                                   'Ethan Fleming Marketing ([TB1PQrXx5s8 @ 00:08:34]); Digitellix '
                                   '([iM8vOv1pK8g @ 00:03:05])'],
                                  ['Inbox provider mix for the sending fleet',
                                   'Buy only Google or Outlook because SMTP inboxes are mostly rubbish',
                                   'Diversify across Google, Outlook, and SMTP because the winner changes '
                                   'every other week',
                                   'Smartlead ([GZEdhosrYRc @ 00:01:20]); Smartlead ([GYd8Y73SCGE @ '
                                   '00:00:04])'],
                                  ['Links and unsubscribe handling in the opening email',
                                   'Zero links or images in email one, moving any link to the final email',
                                   'Put an easy-to-spot working unsubscribe link in every email; '
                                   'reply-to-unsubscribe does not count',
                                   'Kyle Dickson ([drsocawArfo @ 00:11:07]); Damien - MailReach '
                                   '([8EaKo_iAiPE @ 00:10:40])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["The most expensive failures are burned assets. Smartlead's agency operator "
                              'woke up to over 49% of their Gmail inboxes completely dead overnight and '
                              'had to drop hundreds of dollars on brand-new domains just to keep client '
                              'campaigns running [GZEdhosrYRc @ 00:00:00]. Ethan Fleming lost a '
                              '$2,000-a-month client because a Zapier automation was sending lead data '
                              'from their main email; the damaged reputation pushed a proposal into the '
                              "prospect's spam filter, and those two spam-foldered emails cost the deal. "
                              'Another Fleming client fired 10,000 cold emails through one automation and '
                              'tanked not only the CRM domain but the main Gmail and Outlook sending as '
                              'well, which a separate burner domain would have isolated [TB1PQrXx5s8 @ '
                              '00:08:53]. TechSales opens on the same pattern: the first cold emails go '
                              "out from the company's own domain, replies stop a week later, then finance "
                              'reports that customer invoices are landing in spam [aa7B2gisZdU @ '
                              '00:00:01]. CRMOZ adds the volume-spike trap, where a domain silent for '
                              'months suddenly jumps to 10,000 sends on a random Tuesday, Google reads it '
                              'as a hacked account and blocks the domain instantly, and the fix is '
                              'starting at 10 to 15 daily sends to highly engaged users and raising the '
                              'number slowly [T9cn3UyRkR8 @ 00:04:42].',
                              "Content failures show up as silent reply collapse. Smartlead's agency "
                              'operator watched client reply rates fall below 0.5%, against a usual floor '
                              'of 2%, purely because identical static copy went to every prospect; the fix '
                              'was AI spintax inside Smartlead, connected through an OpenAI API key to '
                              'GPT-4, so each recipient receives a different variation of the same message '
                              '[GZEdhosrYRc @ 00:02:09]. Kyle Dickson pushes spintax into nearly every '
                              'sentence to reach 50 or 60 combinations, and warns that one image or one '
                              'link in the first cold email will probably cut deliverability in half, with '
                              'half as many emails actually going out [drsocawArfo @ 00:11:25]. '
                              "Smartlead's 2-million-email team reports the slow-burn version of the same "
                              'trap: images and links can post strong first-week numbers, then most mail '
                              'slides into spam by week two or three, so after testing they stopped '
                              'sending images, while conceding that anyone consistently booking more '
                              'meetings with them should keep going [DIUObYQih3s @ 00:07:19]. Damien calls '
                              'links one of the top causes of content-related spam, says a single link can '
                              'destroy deliverability and that MailReach sees it every day, and lists '
                              'attachments among the top deliverability killers because they are used for '
                              'phishing and hacking [8EaKo_iAiPE @ 00:09:00].',
                              'List quality is where bounce math kills domains. Damien measures catch-all '
                              'addresses bouncing around 23%, and calls the worst move sending to valid '
                              'addresses first, then going all-in on catch-alls once the valids run out; '
                              'the fix is building every list with only 20% catch-alls so the bounce rate '
                              'stays controlled [8EaKo_iAiPE @ 00:06:42]. Kyle Dickson calls bounces the '
                              'enemy of domain and inbox reputation, runs an automation that pauses '
                              'campaigns at a 4% bounce rate, and warns that once bounces pile up the only '
                              'options are buying new inboxes and domains or letting them warm up for '
                              "months [drsocawArfo @ 00:06:33]. Smartlead's agency operator sets the "
                              'high-bounce auto-protection toggle to 5% so a campaign pauses itself, '
                              'because past that line long-term domain and mailbox health starts taking '
                              "real damage [GZEdhosrYRc @ 00:14:23]. Coldbot's diagnostic for a sudden "
                              'placement drop runs in layers: did volume change, was a new domain added, '
                              'did bounce rate rise, did the list source change, did tracking links '
                              'appear, did one mailbox behave differently? Run seed tests by provider and '
                              'compare domains instead of trusting campaign-wide averages, because '
                              'authentication and warm-up are prerequisites, not guarantees [fM-ywBq8yoU @ '
                              '00:06:02].'],
               'table': {'caption': 'Firsthand losses, measured thresholds, and unit-cost checks reported '
                                    'by operators',
                         'headers': ['Failure Mode or Cost Line',
                                     'What Happened or the Number',
                                     'Practitioner Fix',
                                     'Expert Source'],
                         'rows': [['Burned Gmail inbox fleet overnight',
                                   'Over 49% of Gmail inboxes dead overnight, with hundreds spent on '
                                   'replacement domains',
                                   'Drop SMTP, run a 50/50 cold-to-warm split, and keep warm-up running',
                                   'Smartlead ([GZEdhosrYRc @ 00:00:00])'],
                                  ['Main-domain contamination from automations',
                                   'A Zapier lead-data automation from the main email cost a '
                                   '$2,000-a-month client',
                                   'Send all outbound from burner domains and never from the root domain',
                                   'Ethan Fleming Marketing ([TB1PQrXx5s8 @ 00:08:53])'],
                                  ['Static identical copy across a whole campaign',
                                   'Reply rates fell below 0.5% against a usual floor of 2%',
                                   'Add AI spintax variation through an OpenAI key inside Smartlead',
                                   'Smartlead ([GZEdhosrYRc @ 00:02:09])'],
                                  ['Catch-all overload once valid addresses run out',
                                   'Catch-all addresses bounce around 23% when sent to all at once',
                                   'Cap catch-all addresses at 20% of every prepared list',
                                   'Damien - MailReach ([8EaKo_iAiPE @ 00:06:42])'],
                                  ['Bounce spiral that downgrades the sender',
                                   'Hard bounce rate over 5% gets the sender downgraded instantly by '
                                   'algorithms',
                                   'Auto-pause campaigns at a 4 to 5% bounce rate and clean the list',
                                   'CRMOZ ([T9cn3UyRkR8 @ 00:06:02]); Kyle Dickson ([drsocawArfo @ '
                                   '00:06:33])'],
                                  ['Domain unit cost and replacement budget',
                                   'Lookalike sending domains cost roughly $13 to $15 per year each',
                                   'Buy one or two new domains every month as burn insurance and keep them '
                                   'warming',
                                   'Smartlead ([GZEdhosrYRc @ 00:06:41]); Damien - MailReach ([8EaKo_iAiPE '
                                   '@ 00:02:18]); Kyle Dickson ([drsocawArfo @ 00:05:57])'],
                                  ['Capacity math before buying infrastructure',
                                   '3,000 prospects at three emails is 9,000 monthly, needing about 15 '
                                   'mailboxes and 7 domains',
                                   'Size the fleet with a volume calculator at 25 sends per domain per day',
                                   'Smartlead ([GZEdhosrYRc @ 00:08:01])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Checks Before Any Cold Campaign Goes Live',
                           'body': 'Every item below comes from a loss, a burned asset, or a measured '
                                   'threshold an operator hit firsthand. Clear all four before the first '
                                   'send.',
                           'items': ['Keep cold volume off the root domain: a main-email automation cost '
                                     'one operator a $2,000-a-month client, and a 10,000-email blast '
                                     "tanked a client's main Gmail and Outlook sending [Ethan Fleming "
                                     'Marketing — TB1PQrXx5s8 @ 00:08:53].',
                                     'Arm the high-bounce auto-protection at 5% so the campaign pauses '
                                     'itself before long-term domain and mailbox health takes damage '
                                     '[Smartlead — GZEdhosrYRc @ 00:14:23].',
                                     'Build every list with no more than 20% catch-all addresses, since '
                                     'catch-alls bounce around 23% when sent all at once [Damien - '
                                     'MailReach — 8EaKo_iAiPE @ 00:07:24].',
                                     'Send seed tests to Gmail and Outlook accounts you control first; if '
                                     'everything goes to spam, do not launch harder, stop and diagnose '
                                     '[Coldbot — fM-ywBq8yoU @ 00:05:21].']}}],
 'pull_quote': '"Authentication proves identity. It does not force Gmail or Outlook to like your sending '
               'behavior." — Coldbot (fM-ywBq8yoU @ 00:05:42)',
 'diagram_id': 'diag-05',
 'action_checklist': ['Buy lookalike sending domains close to your brand name, with no hyphens or numbers, '
                      'and point every one back to your main website [TechSales — aa7B2gisZdU @ 00:01:44].',
                      'Put two to three Google or Outlook mailboxes on each sending domain, or just two if '
                      'you want to be super safe [Smartlead — GZEdhosrYRc @ 00:07:21].',
                      'Publish SPF, a 2048-bit DKIM key generated in Google Workspace admin, and a _dmarc '
                      'TXT record, then confirm with Google Admin Toolbox Check MX [Stewart Gauld — '
                      'fsZaEce18FE @ 00:03:43].',
                      'Turn on warm-up for 14 to 21 days before any cold send and never shut it off '
                      'afterward [Kyle Dickson — drsocawArfo @ 00:00:32].',
                      'Switch on plain text mode and leave open tracking and link click tracking disabled, '
                      'trusting only reply rates [Smartlead — GZEdhosrYRc @ 00:13:25].',
                      'Load two of your own email addresses at the top of every campaign list to check '
                      'formatting, links, and inbox placement before prospects see anything [Justin Davis '
                      '— 35rkCLq5LC4 @ 00:05:02].'],
 'statutory_citations': [{'title': 'Smartlead — The New Rules of Cold Email Deliverability in 2026 '
                                   '[00:00:00]',
                          'url': 'https://www.youtube.com/watch?v=GZEdhosrYRc&t=0s',
                          'relevance': 'Primary practitioner testimony on a 49% overnight Gmail inbox '
                                       'burn, SMTP failure, spintax recovery, and 5% bounce auto-pause.'},
                         {'title': 'Damien - MailReach — Cold Email Deliverability: The 17 Actions To '
                                   'Always Land in Inbox (Real Advice From Real Pros) [00:02:42]',
                          'url': 'https://www.youtube.com/watch?v=8EaKo_iAiPE&t=162s',
                          'relevance': 'Primary practitioner testimony on Workspace and Office 365 '
                                       'mailboxes, 100-per-day caps, catch-all control, and link-driven '
                                       'spam.'},
                         {'title': 'Ethan Fleming Marketing — GoHighLevel Email Deliverability 2025: SPF, '
                                   'DKIM, DMARC + Warmup (No Spam) [00:08:53]',
                          'url': 'https://www.youtube.com/watch?v=TB1PQrXx5s8&t=533s',
                          'relevance': 'Primary practitioner testimony on losing a $2,000-a-month client '
                                       'to main-domain reputation damage and the burner-domain fix.'},
                         {'title': 'Coldbot — Cold Email Infrastructure 2026: Domains, DNS, Mailboxes & '
                                   'Warmup [00:05:42]',
                          'url': 'https://www.youtube.com/watch?v=fM-ywBq8yoU&t=342s',
                          'relevance': 'Primary practitioner testimony on layered diagnosis when placement '
                                       'drops despite valid authentication and warm-up.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'GZEdhosrYRc',
                       'title': 'The New Rules of Cold Email Deliverability in 2026',
                       'channel': 'Smartlead',
                       'author': 'Smartlead',
                       'text': 'Ideally you want to be warming up your email inboxes anywhere from 2 weeks '
                               'to 3 weeks to start with, and as soon as you start any email campaigns, '
                               'you still want to be warming up the mailboxes at the same time.',
                       'tip': 'Ideally you want to be warming up your email inboxes anywhere from 2 weeks '
                              'to 3 weeks to start with, and as soon as you start any email campaigns, you '
                              'still want to be warming up the mailboxes at the same time.',
                       'timestamp': 611,
                       'timestamp_seconds': 611,
                       'timestamp_label': '[00:10:11]',
                       'url': 'https://www.youtube.com/watch?v=GZEdhosrYRc&t=611s',
                       'markdown': '[00:10:11](https://www.youtube.com/watch?v=GZEdhosrYRc&t=611s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GZEdhosrYRc',
                       'title': 'The New Rules of Cold Email Deliverability in 2026',
                       'channel': 'Smartlead',
                       'author': 'Smartlead',
                       'text': 'I recommend you to add 5% over here so that your campaign automatically '
                               'pauses as soon as your bounce rate reaches 5%.',
                       'tip': 'I recommend you to add 5% over here so that your campaign automatically '
                              'pauses as soon as your bounce rate reaches 5%.',
                       'timestamp': 879,
                       'timestamp_seconds': 879,
                       'timestamp_label': '[00:14:39]',
                       'url': 'https://www.youtube.com/watch?v=GZEdhosrYRc&t=879s',
                       'markdown': '[00:14:39](https://www.youtube.com/watch?v=GZEdhosrYRc&t=879s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'DIUObYQih3s',
                       'title': 'The Ultimate Guide to Cold Email Deliverability in 2026',
                       'channel': 'Smartlead',
                       'author': 'Smartlead',
                       'text': 'Our recommendation is to use two mailboxes per domain, and keep your daily '
                               'limit under 30 to 40 emails per inbox and randomize sometimes slightly.',
                       'tip': 'Our recommendation is to use two mailboxes per domain, and keep your daily '
                              'limit under 30 to 40 emails per inbox and randomize sometimes slightly.',
                       'timestamp': 213,
                       'timestamp_seconds': 213,
                       'timestamp_label': '[00:03:33]',
                       'url': 'https://www.youtube.com/watch?v=DIUObYQih3s&t=213s',
                       'markdown': '[00:03:33](https://www.youtube.com/watch?v=DIUObYQih3s&t=213s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GYd8Y73SCGE',
                       'title': 'SmartSenders Full Demo : Setting up Cold Email Infrastructure in Seconds '
                                'within Smartlead',
                       'channel': 'Smartlead',
                       'author': 'Smartlead',
                       'text': 'Which email provider has the best deliverability, is it Gmail, is it '
                               'Outlook, or is it any of these SMTPs; the thing is it changes every other '
                               'week, so having a diverse email infrastructure is the biggest '
                               'defensibility metric you can have.',
                       'tip': 'Which email provider has the best deliverability, is it Gmail, is it '
                              'Outlook, or is it any of these SMTPs; the thing is it changes every other '
                              'week, so having a diverse email infrastructure is the biggest defensibility '
                              'metric you can have.',
                       'timestamp': 4,
                       'timestamp_seconds': 4,
                       'timestamp_label': '[00:00:04]',
                       'url': 'https://www.youtube.com/watch?v=GYd8Y73SCGE&t=4s',
                       'markdown': '[00:00:04](https://www.youtube.com/watch?v=GYd8Y73SCGE&t=4s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EN_hwXy6LyU',
                       'title': 'Cold Email Setup: SPF, DKIM, and DMARC (2 minute setup for 10+ inboxes)',
                       'channel': 'Kidous Mahteme - Inframail Cold Email Inboxes',
                       'author': 'Kidous Mahteme - Inframail Cold Email Inboxes',
                       'text': 'When you are sending emails with these domains you need to redirect every '
                               "single one back to your main domain, and a lot of people don't do that.",
                       'tip': 'When you are sending emails with these domains you need to redirect every '
                              "single one back to your main domain, and a lot of people don't do that.",
                       'timestamp': 144,
                       'timestamp_seconds': 144,
                       'timestamp_label': '[00:02:24]',
                       'url': 'https://www.youtube.com/watch?v=EN_hwXy6LyU&t=144s',
                       'markdown': '[00:02:24](https://www.youtube.com/watch?v=EN_hwXy6LyU&t=144s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YWsrDI9jLXk',
                       'title': 'How To Setup SPF DKIM DMARC Super Easy 2025',
                       'channel': 'Frankee Muryan',
                       'author': 'Frankee Muryan',
                       'text': 'You want to have this set for none for the first 6 to 12 months, '
                               "especially if you don't have a global brand yet.",
                       'tip': 'You want to have this set for none for the first 6 to 12 months, especially '
                              "if you don't have a global brand yet.",
                       'timestamp': 340,
                       'timestamp_seconds': 340,
                       'timestamp_label': '[00:05:40]',
                       'url': 'https://www.youtube.com/watch?v=YWsrDI9jLXk&t=340s',
                       'markdown': '[00:05:40](https://www.youtube.com/watch?v=YWsrDI9jLXk&t=340s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4N2eWwb-eo4',
                       'title': 'The Best Cold Email Setup: SPF, DKIM, DMARC & Inbox Warmup Explained',
                       'channel': 'Best Lifetime Deal',
                       'author': 'Best Lifetime Deal',
                       'text': 'Before you send a single cold email, your inbox needs a reputation; '
                               'otherwise, even great copy goes straight to spam.',
                       'tip': 'Before you send a single cold email, your inbox needs a reputation; '
                              'otherwise, even great copy goes straight to spam.',
                       'timestamp': 26,
                       'timestamp_seconds': 26,
                       'timestamp_label': '[00:00:26]',
                       'url': 'https://www.youtube.com/watch?v=4N2eWwb-eo4&t=26s',
                       'markdown': '[00:00:26](https://www.youtube.com/watch?v=4N2eWwb-eo4&t=26s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TB1PQrXx5s8',
                       'title': 'GoHighLevel Email Deliverability 2025: SPF, DKIM, DMARC + Warmup (No '
                                'Spam)',
                       'channel': 'Ethan Fleming Marketing',
                       'author': 'Ethan Fleming Marketing',
                       'text': 'I lost a $2,000 a month client because I was using the Zapier automation '
                               'that was basically sending from my main email to a client for basically '
                               'sending lead data.',
                       'tip': 'I lost a $2,000 a month client because I was using the Zapier automation '
                              'that was basically sending from my main email to a client for basically '
                              'sending lead data.',
                       'timestamp': 533,
                       'timestamp_seconds': 533,
                       'timestamp_label': '[00:08:53]',
                       'url': 'https://www.youtube.com/watch?v=TB1PQrXx5s8&t=533s',
                       'markdown': '[00:08:53](https://www.youtube.com/watch?v=TB1PQrXx5s8&t=533s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fsZaEce18FE',
                       'title': 'How To Set Up Google Workspace SPF, DKIM & DMARC | Improve Email '
                                'Deliverability',
                       'channel': 'Stewart Gauld',
                       'author': 'Stewart Gauld',
                       'text': "It's recommended that you keep 2048 selected, which is more secure, then "
                               'keep google down here for the prefix and then click generate.',
                       'tip': "It's recommended that you keep 2048 selected, which is more secure, then "
                              'keep google down here for the prefix and then click generate.',
                       'timestamp': 223,
                       'timestamp_seconds': 223,
                       'timestamp_label': '[00:03:43]',
                       'url': 'https://www.youtube.com/watch?v=fsZaEce18FE&t=223s',
                       'markdown': '[00:03:43](https://www.youtube.com/watch?v=fsZaEce18FE&t=223s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'drsocawArfo',
                       'title': 'Cold Email Deliverability MASTERCLASS – Inbox Every Time! (Full Guide)',
                       'channel': 'Kyle Dickson',
                       'author': 'Kyle Dickson',
                       'text': "It's just more likely to cause domain reputation problems by having a lot "
                               'of inboxes sending cold emails on one domain; if the domain gets '
                               'destroyed, all the inboxes get destroyed.',
                       'tip': "It's just more likely to cause domain reputation problems by having a lot "
                              'of inboxes sending cold emails on one domain; if the domain gets destroyed, '
                              'all the inboxes get destroyed.',
                       'timestamp': 301,
                       'timestamp_seconds': 301,
                       'timestamp_label': '[00:05:01]',
                       'url': 'https://www.youtube.com/watch?v=drsocawArfo&t=301s',
                       'markdown': '[00:05:01](https://www.youtube.com/watch?v=drsocawArfo&t=301s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'aa7B2gisZdU',
                       'title': 'Cold Email Infrastructure: Domains, SPF, DKIM, DMARC and Warm Up | Cold '
                                'Outreach Academy 03',
                       'channel': 'TechSales',
                       'author': 'TechSales',
                       'text': "The golden rule: if the numbers get worse, don't increase volume; stop, "
                               'find the cause, then continue.',
                       'tip': "The golden rule: if the numbers get worse, don't increase volume; stop, "
                              'find the cause, then continue.',
                       'timestamp': 499,
                       'timestamp_seconds': 499,
                       'timestamp_label': '[00:08:19]',
                       'url': 'https://www.youtube.com/watch?v=aa7B2gisZdU&t=499s',
                       'markdown': '[00:08:19](https://www.youtube.com/watch?v=aa7B2gisZdU&t=499s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8sprCYGSnpI',
                       'title': 'SPF, DKIM and DMARC Setup for Cold Email (Google Workspace & Microsoft '
                                '365) | SalesBlink',
                       'channel': 'SalesBlink',
                       'author': 'SalesBlink',
                       'text': "A failed check hurts where your emails land, but it doesn't stop sending; "
                               'only a broken sending connection does.',
                       'tip': "A failed check hurts where your emails land, but it doesn't stop sending; "
                              'only a broken sending connection does.',
                       'timestamp': 18,
                       'timestamp_seconds': 18,
                       'timestamp_label': '[00:00:18]',
                       'url': 'https://www.youtube.com/watch?v=8sprCYGSnpI&t=18s',
                       'markdown': '[00:00:18](https://www.youtube.com/watch?v=8sprCYGSnpI&t=18s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iM8vOv1pK8g',
                       'title': 'Email Deliverability for Small Businesses: SPF, DKIM, DMARC + Warm-Up',
                       'channel': 'Digitellix',
                       'author': 'Digitellix',
                       'text': 'Running your own SMTP server means you own every reputation problem, and '
                               'under roughly 100,000 emails a month, a shared IP is usually better than a '
                               'dedicated one.',
                       'tip': 'Running your own SMTP server means you own every reputation problem, and '
                              'under roughly 100,000 emails a month, a shared IP is usually better than a '
                              'dedicated one.',
                       'timestamp': 121,
                       'timestamp_seconds': 121,
                       'timestamp_label': '[00:02:01]',
                       'url': 'https://www.youtube.com/watch?v=iM8vOv1pK8g&t=121s',
                       'markdown': '[00:02:01](https://www.youtube.com/watch?v=iM8vOv1pK8g&t=121s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '35rkCLq5LC4',
                       'title': 'SPF, DKIM and DMARC Explained for Link Building Outreach Email '
                                'Deliverability',
                       'channel': 'Justin Davis',
                       'author': 'Justin Davis',
                       'text': 'Once an inbox is warmed up, I generally stay under 40 emails per day; need '
                               'to send more, add more inboxes.',
                       'tip': 'Once an inbox is warmed up, I generally stay under 40 emails per day; need '
                              'to send more, add more inboxes.',
                       'timestamp': 105,
                       'timestamp_seconds': 105,
                       'timestamp_label': '[00:01:45]',
                       'url': 'https://www.youtube.com/watch?v=35rkCLq5LC4&t=105s',
                       'markdown': '[00:01:45](https://www.youtube.com/watch?v=35rkCLq5LC4&t=105s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8EaKo_iAiPE',
                       'title': 'Cold Email Deliverability: The 17 Actions To Always Land in Inbox (Real '
                                'Advice From Real Pros)',
                       'channel': 'Damien - MailReach',
                       'author': 'Damien - MailReach',
                       'text': "For the catch-all ones you don't know if they are valid or not, so a "
                               "significant proportion of this will bounce, and it's around 23%.",
                       'tip': "For the catch-all ones you don't know if they are valid or not, so a "
                              "significant proportion of this will bounce, and it's around 23%.",
                       'timestamp': 402,
                       'timestamp_seconds': 402,
                       'timestamp_label': '[00:06:42]',
                       'url': 'https://www.youtube.com/watch?v=8EaKo_iAiPE&t=402s',
                       'markdown': '[00:06:42](https://www.youtube.com/watch?v=8EaKo_iAiPE&t=402s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'T9cn3UyRkR8',
                       'title': 'SPF DKIM DMARC Setup + 5 Mistakes Killing Your Deliverability',
                       'channel': 'CRMOZ',
                       'author': 'CRMOZ',
                       'text': 'Start at none just to monitor the traffic, then over a few weeks move to a '
                               'quarantine at 10%, and slowly scale it up to 100.',
                       'tip': 'Start at none just to monitor the traffic, then over a few weeks move to a '
                              'quarantine at 10%, and slowly scale it up to 100.',
                       'timestamp': 160,
                       'timestamp_seconds': 160,
                       'timestamp_label': '[00:02:40]',
                       'url': 'https://www.youtube.com/watch?v=T9cn3UyRkR8&t=160s',
                       'markdown': '[00:02:40](https://www.youtube.com/watch?v=T9cn3UyRkR8&t=160s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fM-ywBq8yoU',
                       'title': 'Cold Email Infrastructure 2026: Domains, DNS, Mailboxes & Warmup',
                       'channel': 'Coldbot',
                       'author': 'Coldbot',
                       'text': 'You can have SPF, you can have DKIM, you can have DMARC, and still have '
                               'poor inbox placement; authentication proves identity, it does not force '
                               'Gmail or Outlook to like your sending behavior.',
                       'tip': 'You can have SPF, you can have DKIM, you can have DMARC, and still have '
                              'poor inbox placement; authentication proves identity, it does not force '
                              'Gmail or Outlook to like your sending behavior.',
                       'timestamp': 342,
                       'timestamp_seconds': 342,
                       'timestamp_label': '[00:05:42]',
                       'url': 'https://www.youtube.com/watch?v=fM-ywBq8yoU&t=342s',
                       'markdown': '[00:05:42](https://www.youtube.com/watch?v=fM-ywBq8yoU&t=342s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'}]}
