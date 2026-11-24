from __future__ import annotations

def build_volume_008_workbook() -> dict:
    return {'workbook_id': 'wb-008-commercial-lead-generation',
 'volume_id': 'vol-008-commercial-lead-generation',
 'title': 'Commercial Lead Generation — Practitioner Testimony Operator Workbook',
 'subtitle': 'Pricing commercial leads, building verified prospect lists, and sending cold email that '
             'lands, worked from operator numbers on pay-per-lead margins, Clay waterfalls, and Smartlead '
             'deliverability',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Lead Business Model and Unit Economics',
                 'purpose': 'Lock the niche, billing unit, lead price, buyer return, payment terms, and '
                            'credit policy for a commercial lead business before any media is spent, using '
                            'the arbitrage math operators report from pay-per-lead, pay-per-appointment, '
                            'and retainer books.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Fill the fields in order, because each later number depends on the '
                                  'niche value and billing unit chosen first.',
                                  'Write every price and cost as a single committed dollar figure rather '
                                  'than a range once the plan is set.',
                                  'Run the margin check in the cost-per-lead field before drafting the '
                                  'twenty-client profit and loss.',
                                  'Cite the operator claim behind each number in the same bracketed format '
                                  'the examples use.',
                                  'Revisit the credit and payment fields after the first prepaid pilot '
                                  'closes and adjust the caps to match real returns.'],
                 'fields': [{'name': 'niche_and_lead_value',
                             'type': 'text',
                             'prompt': 'Name the single commercial niche you will serve and state what one '
                                       'closed customer is worth to the buyer. Confirm that each lead '
                                       'clears the $100 value line before you copy any operator blueprint, '
                                       'and record the ticket size you used.',
                             'example': 'Niche: truck insurance, where one policy is worth thousands. Each '
                                        'lead clears the $100 line, so the blueprint is safe to copy [My '
                                        'First Million — Poc5H6aVTlw @ 00:03:24]. Max Conversion runs this '
                                        'niche on Google Ads at about $35 to $36 per lead on roughly '
                                        '$10,000 monthly spend [Max Conversion — kPWKWbOFwUo @ 00:00:27].'},
                            {'name': 'billing_unit',
                             'type': 'text',
                             'prompt': 'Choose your billing unit: pay-per-lead, pay-per-appointment, or '
                                       'retainer. Write the reason for your choice, the operator position '
                                       'that supports it, and the specific risk that the opposing camp '
                                       'warns about, so the trade-off stays visible while you build.',
                             'example': 'Unit: pay-per-appointment, priced at $250 per booked appointment '
                                        'with a delivery cost of $125. Ruben Frederic states their firm is '
                                        'not a custom agency [Ruben Frederic — B6M6968u10c @ 00:12:52]. '
                                        'Risk noted: Snovio warns that per-lead pricing overwhelms '
                                        'beginners with volume and pushes fixed monthly fees instead '
                                        '[Snovio — MmWpOeG5GW4 @ 00:02:29].'},
                            {'name': 'cost_per_lead_and_resale',
                             'type': 'text',
                             'prompt': 'Record your expected cost to generate one lead and your planned '
                                       'resale price. Show the multiple between them, which operators set '
                                       'at 1.5x to 3x, and confirm the sale price beats generation cost '
                                       'before you spend another dollar scaling.',
                             'example': 'Generation cost $25 per lead, resale $60, a 2.4x multiple. Kelly '
                                        'Joseph shows $1k of spend buying 40 leads sold at $60 for $2,400 '
                                        'revenue and $1,400 profit [Kelly Joseph — muQkzU3fXJY @ '
                                        '00:05:53]. Margin check passes; Rafael Hernandez warns a $30 sale '
                                        'on a $40 lead loses ten dollars every time [Rafael Hernandez ⚡️ — '
                                        'ngsR38BAFbc @ 00:06:33].'},
                            {'name': 'buyer_roas_floor',
                             'type': 'text',
                             'prompt': 'Work your lead price backward from the return your buyer must '
                                       "earn. Enter the buyer's close rate, average customer value, and "
                                       'resulting ROAS, and confirm the buyer clears at least 2x to 3x so '
                                       'they keep reordering from you.',
                             'example': 'Hunter Ceroy sets a floor of a 2 to 3x ROAS for every client '
                                        "[Hunter Ceroy — 0Cfp-Fc0sag @ 00:00:27]. Smart Capital's warning "
                                        'applies: at $250 per appointment and one in three converting, a '
                                        'client pays $750 to win an $800 patient, which is too tight '
                                        '[Smart Capital — ozWkxUTBug4 @ 00:05:28]. My price stays below '
                                        'that line.'},
                            {'name': 'twenty_client_pnl',
                             'type': 'textarea',
                             'prompt': 'Draft a monthly profit and loss for twenty clients. List revenue '
                                       'and each cost line, including media, AI tools, CRM software, a '
                                       'closer, and a developer, then state the profit you keep and '
                                       'whether the model survives heavy client churn.',
                             'example': 'Revenue $75K a month. Costs: media $25K, AI $500, GHL $300, '
                                        'closer $12,500, developer $700, just under $40K total, leaving '
                                        '$35K profit. Billy Robinson claims this pay-per-lead model works '
                                        'even at 100% churn [Billy Robinson — -_uHG2CwBjA @ 00:10:09]. '
                                        'Robinson also scaled from an $80K-a-month retainer agency to '
                                        '$250K a month in lead sales [Billy Robinson — NStq42nosUk @ '
                                        '00:06:09].'},
                            {'name': 'speed_to_lead_delivery',
                             'type': 'textarea',
                             'prompt': 'Map how each lead reaches your buyer and gets contacted. Name the '
                                       'tools that fire first contact, the target response window in '
                                       'minutes, the text and email sequence behind it, and who owns a '
                                       'lead that nobody answers.',
                             'example': 'Round-robin assignment and auto-call transfer touch every lead '
                                        'inside 1 to 5 minutes, backed by a 5-to-7-day text and email '
                                        'sequence [Nato Guajardo | Insurance Agency Growth — VSivqJQ89ow @ '
                                        '00:20:16]. Guajardo ties that window to 400% to 1,000% higher '
                                        'conversion. Robinson frames retention plainly: it is a '
                                        'speed-to-lead problem [Billy Robinson — -_uHG2CwBjA @ 00:01:30].'},
                            {'name': 'payment_terms',
                             'type': 'text',
                             'prompt': 'Set the payment terms for a new buyer. State whether they prepay, '
                                       'how long the prepaid pilot runs before you offer net 7 terms, and '
                                       'the exact day you pause delivery when an invoice goes unpaid past '
                                       'its due date.',
                             'example': 'New buyers prepay for a pilot batch; net 7 terms open only after '
                                        'that pilot delivers, and delivery pauses when payment is 7 days '
                                        "late [Kelly Joseph — muQkzU3fXJY @ 00:40:30]. Robinson's minimum "
                                        "order sits at $3,750, and prospects see the AI agent's SMS before "
                                        'the sales call, which closes one in three [Billy Robinson — '
                                        '-_uHG2CwBjA @ 00:07:18].'},
                            {'name': 'credit_policy',
                             'type': 'text',
                             'prompt': 'Write your credit and refund policy for bad leads or no-show '
                                       'appointments. State the cap as a share of delivery, the time '
                                       'window it covers, and the dollar damage one extra credit does to '
                                       'your margin on a single unit.',
                             'example': 'Credits capped at 10% of delivery, because one credited $250 '
                                        'appointment that cost $125 to produce wipes the margin [Ruben '
                                        'Frederic — B6M6968u10c @ 00:15:31]. Buyer refunds are also capped '
                                        'at 15% over the past 30 days, set before the first invoice goes '
                                        'out [boberdoo.com — yCAVYNpSdZI @ 00:22:50]. Anything above that '
                                        'cap is declined.'},
                            {'name': 'qualification_signal',
                             'type': 'textarea',
                             'prompt': 'Describe which event tells your ad platforms a lead counted. Name '
                                       'the qualifying answer or sales-accepted status that fires the '
                                       'conversion, how sold leads and billable calls post back '
                                       'server-side, and what you do when cost per lead spikes.',
                             'example': 'Conversions fire only on qualified answers, never thank-you page '
                                        'views [reachmarketingllc — M0v6X1EjkRM @ 00:04:17]. Sold leads '
                                        'and billable calls post back through the Conversions API on '
                                        'Stape.io [Kelly Joseph — muQkzU3fXJY @ 00:26:39]. On a spike, '
                                        'apply event matching and bid caps, the fixes after finance CPL '
                                        'jumped from $35 to $55 [Billy Robinson — NStq42nosUk @ '
                                        '00:05:55].'},
                            {'name': 'client_acquisition_channel',
                             'type': 'textarea',
                             'prompt': 'Plan how you will win your own buyers. State the outbound channel, '
                                       'daily send volume, expected booked calls, the price you quote per '
                                       'appointment, and any signal you use to time outreach, so '
                                       'acquisition runs on predictable math rather than hope.',
                             'example': 'Channel: cold email through Smartlead, 20 inboxes sending 20 a '
                                        'day for about 400 emails daily and 1 to 2 booked calls per day '
                                        '[Harry Latos — IPwP5tUojE4 @ 00:07:03]. Timing signal: CFOs new '
                                        'to the seat in the last 90 days, which won a $100,000 retained '
                                        'deal [Harry Latos — z85zvw9drj8 @ 00:12:18]. Appointments quoted '
                                        'inside $150 to $600.'}],
                 'completion_gate': 'Do not launch media until the niche clears the $100 lead-value line, '
                                    'resale price beats generation cost, the buyer clears a 2x to 3x ROAS, '
                                    'credits are capped at 10% of delivery, and every new buyer has '
                                    'prepaid a pilot.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Prospect List Build and Clay Enrichment Plan',
                 'purpose': 'Build a commercial prospect list that is precise, verified, and affordable by '
                            'stacking LinkedIn, Apollo, and Google Maps sources, checking match flags and '
                            'email match rates, and running a cheapest-first Clay waterfall that never '
                            'mails an unvalidated address.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Define the buyer profile before opening any scraper, database, or '
                                  'enrichment table.',
                                  'Start every pull at 100 or 200 results, and every new waterfall at two '
                                  'to ten rows, before scaling.',
                                  'Log result counts, match rates, and bounce figures for each source so '
                                  'weak sources can be cut.',
                                  'Keep auto-update off and gate every paid column with a run condition '
                                  'before importing records.',
                                  'Hand the validated master email column to the infrastructure worksheet '
                                  'only after every gate below is passed.'],
                 'fields': [{'name': 'icp_definition',
                             'type': 'textarea',
                             'prompt': 'Define the exact buyer profile for this list. Record industry, '
                                       'company size, title, geography, and tenure, and explain why fifty '
                                       'matched prospects beat five hundred random names for your offer '
                                       'before you spend a single enrichment credit.',
                             'example': 'Target: owners of heating companies across five New Jersey '
                                        'cities, pulled city by city. Alex Vacca favors 50 matched '
                                        'prospects over 500 random names, and starts every scrape at 100 '
                                        'or 200 results to test before scaling [Alex Vacca — Ouq5ayjDmmI @ '
                                        '00:05:55]. Off-criteria rows get flagged and removed, never '
                                        'mailed.'},
                            {'name': 'source_stack',
                             'type': 'textarea',
                             'prompt': 'List every source you will pull from, such as Sales Navigator, '
                                       'Apollo, Google Maps, or Apify. Note which buyer types each source '
                                       'misses, the cost per thousand records, and whether you split '
                                       'searches by city or zip code.',
                             'example': 'Apollo and Sales Navigator miss hotel, farm, and wholesale '
                                        'buyers, so Google Maps scrapes run city by city through Apify at '
                                        'about $4 per thousand places. Georgey Tishin pulled 887 unique '
                                        'heating leads across five New Jersey cities, versus 92 rows from '
                                        'Edison alone on a free extension [Georgey Tishin — p1rfyeLoS2s @ '
                                        '00:06:19].'},
                            {'name': 'search_terms',
                             'type': 'text',
                             'prompt': 'Write the keyword you will enter in the Google Maps scraper and '
                                       'the broader alternatives you tested. Record the result count for '
                                       'each term so you can prove which phrasing returns the widest list '
                                       'for the same market.',
                             'example': 'Term: heating, not HVAC, because the broader word returns more '
                                        'results [Georgey Tishin — p1rfyeLoS2s @ 00:05:00]. Tishin puts '
                                        'the gap between a city-by-city build and a single HVAC in New '
                                        'Jersey search at roughly 500 results versus 5,000 [Georgey Tishin '
                                        '— p1rfyeLoS2s @ 00:00:53]. Result counts logged per term and per '
                                        'city.'},
                            {'name': 'sales_nav_filters',
                             'type': 'textarea',
                             'prompt': 'Record the Sales Navigator filters for your saved search. Include '
                                       'title, company size, and activity filters such as posted on '
                                       'LinkedIn or changed jobs, and state whether the search excludes '
                                       'people you have already viewed or messaged.',
                             'example': 'Saved search filtered to people not yet viewed or messaged, so '
                                        'the list self-clears every week [Marcus Chan — HL8AeTPufLU @ '
                                        '00:07:24]. Change jobs in the last 90 days sits under activities '
                                        'and shared experiences [Sell Better — 3Y7sW7ob3hY @ 00:03:09], '
                                        'but Chan finds that filter a little hit or miss, so it runs as a '
                                        'test segment only.'},
                            {'name': 'match_flag_check',
                             'type': 'text',
                             'prompt': 'Run a match-filter check on your Sales Navigator export before '
                                       'sequencing. Record how many rows carry the wrong company size, '
                                       'tenure, or title, the share that missed the search criteria, and '
                                       'what you did with the flagged rows.',
                             'example': "Evaboot's match-filter column flagged an intern inside a "
                                        'head-of-sales search, and at least 20% of results missed the '
                                        'criteria [JB - Evaboot — rryPKFY2BRI @ 00:05:44]. To reach '
                                        'decision makers, companies went to an account list, a lead search '
                                        'ran on that list with CEO in current job title, then exported '
                                        'with emails [JB - Evaboot — rryPKFY2BRI @ 00:09:31].'},
                            {'name': 'email_match_rate',
                             'type': 'text',
                             'prompt': 'Run a test pull and record the email match rate before scaling the '
                                       'list. Compare the result to the 20 to 25 percent healthy benchmark '
                                       'and note whether your market uses business domains or personal '
                                       'inboxes like Gmail.',
                             'example': 'Test audience: 2,000 people. Match rate came back at 2%, far '
                                        'under the 20 to 25% healthy benchmark, because most Philippine '
                                        'buyers use Gmail rather than business domains [Lead Gen PH — '
                                        'i-oQ5e48OF8 @ 00:06:57]. A second run sat at 7%, so the list was '
                                        'not scaled [Lead Gen PH — i-oQ5e48OF8 @ 00:13:51].'},
                            {'name': 'email_waterfall',
                             'type': 'textarea',
                             'prompt': 'List the providers in your Clay email waterfall in run order. Note '
                                       'the credit cost of each step, the run condition that stops paid '
                                       'columns from re-running on rows that already hit, and the total '
                                       'number of steps.',
                             'example': 'Four steps, cheapest first, with any provider over 10 credits per '
                                        'row deleted, since valid emails usually land in the first two or '
                                        'three columns [AJ Cassata — 6l8CThrSJEY @ 00:11:35]. Each '
                                        'fallback carries the run condition only run if work email is '
                                        'empty [AJ Cassata — 6l8CThrSJEY @ 00:16:35]. Expected coverage: '
                                        '60 to 80% of the list.'},
                            {'name': 'validation_routing',
                             'type': 'textarea',
                             'prompt': 'Describe how found emails are validated before any send. Name the '
                                       'verifiers you trust, which statuses merge into the master email '
                                       'column, where risky, unknown, and catch-all rows go next, and why '
                                       'a verified label alone is not proof.',
                             'example': 'Only Debounce safe-to-send, Prospeo valid, and Enrich.so valid '
                                        'results merge into one master column; risky, unknown, and '
                                        'catch-all rows route to a second verifier [Romain Osman Lead '
                                        'Generation — RodU66qhDeY @ 00:09:16]. Verified labels are not '
                                        'trusted alone: 1,000 verified Apollo leads still delivered only '
                                        '73% email accuracy, with over 270 bounces [Prospeo — QnSW0B2oztg '
                                        '@ 00:09:46].'},
                            {'name': 'credit_budget',
                             'type': 'text',
                             'prompt': 'Estimate the Clay credits this table will consume. Count credits '
                                       'per email lookup and per AI research run, state whether research '
                                       'runs at the company or lead level, and confirm auto-update is off '
                                       'before importing any rows.',
                             'example': 'Budget: 1 to 3 credits per email lookup and 5 to 10 per AI '
                                        'research run, treated as tokens [Xavier Caffrey GTM — kY5E4wl8wlA '
                                        '@ 00:06:54]. Research runs at the company level and is looked up '
                                        'from the people table, since per-lead runs cost two to three '
                                        'times as much. Auto-update is off. Cleanup uses free formulas '
                                        'only.'},
                            {'name': 'intent_and_test_run',
                             'type': 'textarea',
                             'prompt': 'Record how you will qualify accounts for real need and how you '
                                       'will test the table. Name the intent signals you layer beyond tech '
                                       'stack, the forced yes or no AI outputs, and the row count of your '
                                       'first test run.',
                             'example': 'Using Salesforce is not treated as need; topic intent and '
                                        'Claygent opportunity ratings come first [The AI Ops Guy — '
                                        'nRh4F859Xjo @ 00:01:02]. Hiring intent is sourced by checking '
                                        'company pages for roles unfilled over two months [Prospeo — '
                                        'QnSW0B2oztg @ 00:04:10]. First run covers ten rows before the '
                                        'full pull [Matt Lucero — jEkDgA8hPmo @ 00:17:57].'}],
                 'completion_gate': 'Do not push a list to sequencing until the test pull clears a 20 to '
                                    '25% email match rate, Sales Navigator match flags are checked, only '
                                    'safe-to-send and valid emails sit in the master column, and the table '
                                    'ran cleanly on ten rows.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Sending Infrastructure and Smartlead Campaign Launch',
                 'purpose': 'Stand up a cold email fleet that protects the primary domain, spreads risk '
                            'across providers, warms every inbox, and launches short plain-text Smartlead '
                            'sequences with bounce protection armed, so commercial outreach reaches '
                            'inboxes and books calls at predictable rates.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Buy and redirect secondary domains before creating a single mailbox on '
                                  'any provider.',
                                  'Publish SPF, DKIM, DMARC, and MX, then start warm-up two to three weeks '
                                  'ahead of launch.',
                                  'Load only lists that passed the verification gates from the prospect '
                                  'list worksheet.',
                                  'Arm bounce protection and confirm tracking settings before the first '
                                  'prospect is added to a campaign.',
                                  'Review bounce, reply, and interested-to-call figures weekly, and fix '
                                  'the list before adjusting copy.'],
                 'fields': [{'name': 'secondary_domains',
                             'type': 'text',
                             'prompt': 'List the secondary lookalike domains you will send from and '
                                       'confirm none of them is your primary brand domain. Note how each '
                                       'name keeps the brand recognizable and confirm every domain '
                                       'redirects to your main website before warm-up starts.',
                             'example': 'Domains: getstar.com, trystar.com, and starhq.com, each '
                                        'redirected to the main site [Smartlead — dTLQCIO7Tf0 @ 00:01:46]. '
                                        'No cold send touches the root domain; one main-email Zapier '
                                        'automation cost an operator a $2,000-a-month client [Ethan '
                                        'Fleming Marketing — TB1PQrXx5s8 @ 00:08:53]. A prospect who hits '
                                        'an error page on a lookalike domain loses trust.'},
                            {'name': 'mailbox_plan',
                             'type': 'textarea',
                             'prompt': 'Plan the mailbox fleet. State the number of inboxes per domain, '
                                       'the split across Google, Outlook, and SMTP providers, the daily '
                                       'cold send cap per inbox, and the backup domains and inboxes '
                                       'warming in reserve so one provider action cannot wipe the fleet.',
                             'example': 'Two inboxes per domain at 25 sends each, 50 per domain per day '
                                        '[Smartlead — C2lkX09G4h4 @ 00:02:20]. Fleet split for 200 '
                                        'inboxes: about 67 Google, 67 Outlook, and the rest SMTP '
                                        '[Smartlead — C2lkX09G4h4 @ 00:08:16]. With five domains and 10 '
                                        'mailboxes live, another five domains and 10 mailboxes warm as '
                                        'backup [Smartlead — dTLQCIO7Tf0 @ 00:15:06].'},
                            {'name': 'dns_authentication',
                             'type': 'text',
                             'prompt': 'Record the authentication records published on each sending '
                                       'domain. Confirm SPF, DKIM, DMARC, and MX are live, note the DMARC '
                                       'policy you chose for the first months, and state why '
                                       'authentication alone does not guarantee inbox placement.',
                             'example': 'SPF, DKIM, DMARC, and MX published on every domain. DMARC policy '
                                        'set to none for the first 6 to 12 months while the brand is not '
                                        'global [Frankee Muryan — YWsrDI9jLXk @ 00:05:40]. Coldbot treats '
                                        'authentication and warmup as prerequisites that guarantee '
                                        'nothing, so seed tests still run before launch [Coldbot — '
                                        'fM-ywBq8yoU @ 00:05:21].'},
                            {'name': 'warmup_schedule',
                             'type': 'text',
                             'prompt': 'Set the warm-up schedule for every new inbox on each domain. '
                                       'Record the start date, the number of weeks before launch, the '
                                       'starting daily warm-up volume, and whether background warm-up '
                                       'keeps running after campaigns begin or even during pauses.',
                             'example': 'Warm-up runs two to three weeks before the first campaign and '
                                        'continues once sending starts [Smartlead — GZEdhosrYRc @ '
                                        '00:10:11]. Low-level background warm-up never switches off, even '
                                        'during pauses; the team behind 2 million cold emails a year '
                                        'credits it for 95% to 97% inbox rates month after month '
                                        '[Smartlead — DIUObYQih3s @ 00:09:29].'},
                            {'name': 'list_hygiene',
                             'type': 'text',
                             'prompt': 'State the list rules that protect bounce rate. Record the maximum '
                                       'share of catch-all addresses allowed, the verification statuses '
                                       'accepted, and the two internal addresses placed at the top of '
                                       'every campaign list for first-send checks.',
                             'example': 'Catch-alls capped at 20% of each list, since around 23% of '
                                        'catch-all addresses bounce when sent all at once [Damien - '
                                        'MailReach — 8EaKo_iAiPE @ 00:07:24]. Two of my own addresses sit '
                                        'at the top of every list, so the first sends land with me for '
                                        'formatting, link, and inbox-versus-spam checks [Justin Davis — '
                                        '35rkCLq5LC4 @ 00:00:00].'},
                            {'name': 'bounce_protection',
                             'type': 'text',
                             'prompt': 'Configure bounce protection in your sending tool. Record the '
                                       'auto-pause threshold, the manual stop line where you fix the list '
                                       'yourself, and the health benchmarks for reply and bounce rates you '
                                       'will hold every campaign against.',
                             'example': 'High-bounce auto-protection armed at 5%, so the campaign pauses '
                                        'itself before domain health takes damage [Smartlead — GZEdhosrYRc '
                                        '@ 00:14:23]. Manual stop at 2%: fix the list before sending '
                                        'another email [Smartlead — C2lkX09G4h4 @ 00:13:23]. Benchmarks '
                                        'held: about 1% reply rate and under 3% bounce rate [Matt Lucero — '
                                        '_iGjRSCPXuA @ 02:10:45].'},
                            {'name': 'tracking_and_format',
                             'type': 'text',
                             'prompt': 'List the delivery settings applied to the sequence. Note whether '
                                       'plain text and optimize delivery are on, whether open and click '
                                       'tracking are off, how links appear in the copy, and whether a '
                                       'custom tracking domain is configured.',
                             'example': 'Optimize delivery and plain text on, with no links, images, open '
                                        'tracking, or click tracking in the sequence [Smartlead — '
                                        'J8lvEnIHcLk @ 01:48:04]. Where a URL is unavoidable, it sits as a '
                                        'non-hyperlinked address in parentheses [Michael Saruggia - GTM '
                                        'Engineering — qWuvWm5Zcz0 @ 00:09:25]. A custom tracking domain '
                                        'replaces the shared one every other user carries.'},
                            {'name': 'sequence_structure',
                             'type': 'textarea',
                             'prompt': 'Outline the sequence. State the number of emails, the delay '
                                       'between them, how follow-ups thread under the first message, how '
                                       'first names fall back when missing, and how spintax keeps copy '
                                       'from repeating word for word.',
                             'example': 'Three emails maximum, because most positive replies come from '
                                        'email one [Smartlead — dTLQCIO7Tf0 @ 00:07:58]. Follow-up subject '
                                        'lines stay blank to keep the thread [Vincent Robin — 7Sq3Ger8D3A '
                                        "@ 00:11:09]. A liquid conditional sends 'Hi there' when a name is "
                                        'missing [Matt Lucero — _iGjRSCPXuA @ 01:58:52]. Spintax varies '
                                        'copy after static versions fell below 0.5% replies.'},
                            {'name': 'reply_trigger_offer',
                             'type': 'textarea',
                             'prompt': 'Describe the offer and how resources reach interested prospects. '
                                       'Name the reply keyword you ask for, the subsequence trigger and '
                                       'delay that fires on it, and the short call the follow-up steers '
                                       'toward instead of placing a link in email one.',
                             'example': 'Email one asks prospects to reply with the word report; no link '
                                        'appears. A Smartlead subsequence fires on a text-contains trigger '
                                        'with a 0-day delay, sends the resource, and steers toward a '
                                        '15-minute call [Smartlead — doR2rhof6CM @ 00:31:44]. Another '
                                        'variant uses a trigger word like pink, delivering the link only '
                                        'to those who replied [Smartlead — GZEdhosrYRc @ 00:12:47].'},
                            {'name': 'volume_troubleshooting',
                             'type': 'textarea',
                             'prompt': 'Write the checklist you run when a campaign sends less than '
                                       'planned or replies drop. Include triggers per day, max new leads '
                                       'per day, mailbox daily limits, minimum time gap, and seed '
                                       'placement in Gmail and Outlook accounts you control.',
                             'example': 'Before blaming copy, audit triggers per day, max new leads per '
                                        'day, mailbox daily limit, and minimum time gap; when in doubt, '
                                        'lower the gap and raise the limits [Matt Lucero — _iGjRSCPXuA @ '
                                        '02:56:27]. Seed tests go to controlled Gmail and Outlook '
                                        'accounts, and if everything lands in spam, sending stops for '
                                        'diagnosis [Coldbot — fM-ywBq8yoU @ 00:05:21].'}],
                 'completion_gate': 'Do not launch until no cold send touches the primary domain, every '
                                    'inbox has warmed at least two weeks, catch-alls sit at 20% or less, '
                                    'bounce auto-pause is armed at 5%, and seed tests land in the inbox on '
                                    'Gmail and Outlook.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'LinkedIn Outreach, Appointment Setting, and Cold Email Agency Compliance '
                          'Planner',
                 'purpose': 'Build a LinkedIn outreach and appointment-setting system that respects '
                            'per-account connection caps, tests blank requests against written notes, '
                            'books interested leads at a measurable rate, and launches a cold email agency '
                            'on secondary domains with physical-address footers, same-day opt-outs, and '
                            'centralized suppression.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Inventory every LinkedIn sender account and mailbox before writing a '
                                  'single message, because volume comes from stacking accounts, not from '
                                  'raising limits.',
                                  'Run every targeting, connection, and messaging decision as a measured '
                                  'test, with sample sizes and expected acceptance or reply benchmarks '
                                  'written down first.',
                                  'Wire speed-to-lead and booking functions end to end, then audit the '
                                  'interested-to-booked rate before adding new sender volume.',
                                  'Price the first three clients on fixed monthly fees and itemize the '
                                  'tool stack so margin is visible from day one.',
                                  'Complete the compliance controls last but treat them as a launch '
                                  'blocker: no campaign goes live without a footer address, opt-out path, '
                                  'and global block list.'],
                 'fields': [{'name': 'sender_account_inventory',
                             'type': 'textarea',
                             'prompt': 'List every LinkedIn sender account you will run, its age, its '
                                       'current daily connection-request ceiling, and the weekly cap it '
                                       'must respect. Explain how many accounts you need to stack to reach '
                                       'your monthly conversation target without pushing any single '
                                       'account past safe limits.',
                             'example': 'Three sender accounts: two new, one aged. Each LinkedIn account '
                                        'sits near 100 connection requests per week, roughly 10 to 15 per '
                                        'day, so the two new accounts start at 10 daily and scale only by '
                                        'adding senders, not by raising limits [HeyReach — 5JAMkYMtvhw @ '
                                        '00:07:28]. Combined fleet output is about 300 requests weekly, '
                                        'reviewed every Monday after the weekly reset.'},
                            {'name': 'targeting_filters',
                             'type': 'textarea',
                             'prompt': 'Define the Sales Navigator filters for your first LinkedIn '
                                       'campaign beyond job title alone. Name the activity filter, the '
                                       'segment rules, and how you will validate company data before '
                                       'launch so inaccurate rows never reach a sender account or a '
                                       'sequence.',
                             'example': 'Filter: operations directors at facility management firms, with '
                                        "'posted on LinkedIn' switched on, which Amon says lifts "
                                        'acceptance 2 to 4X because the request reaches active users '
                                        '[HeyReach — Cgx8HVnGOdY @ 00:24:08]. Before launch, every company '
                                        'website is validated in Clay, since 30% of any Sales Navigator '
                                        'list is inaccurate, if not more [Matt Harriman — hm5isqC1d74 @ '
                                        '00:02:33].'},
                            {'name': 'connection_request_test',
                             'type': 'textarea',
                             'prompt': 'Design a split test for your connection request. State whether '
                                       'each variant is blank or carries a note, the sample size per arm, '
                                       'the acceptance rate you expect, and the warm-up touch you will '
                                       'perform on each prospect before the request goes out.',
                             'example': 'Arm A sends 150 blank requests, Arm B sends 150 requests with a '
                                        'short note. Benchmark: about 27% acceptance blank versus 22% with '
                                        'text [HeyReach — Cgx8HVnGOdY @ 00:30:30]. The day before each '
                                        'request, the sender likes and comments on one recent prospect '
                                        'post, a step lemlist reports lifts acceptance 18% [lemlist — '
                                        '-LtGmHnpioI @ 00:08:45].'},
                            {'name': 'first_message_script',
                             'type': 'textarea',
                             'prompt': 'Write the first message a newly accepted connection receives. Keep '
                                       'it free of any pitch, lead with value, ask one easy question, and '
                                       'confirm the offer reads clearly in five seconds. Note the '
                                       'localized greeting and send-time rule tied to prospect location.',
                             'example': "For Milan prospects the message opens with 'Buongiorno' and sends "
                                        'during Italian morning hours, since location drives both greeting '
                                        'and timing [HeyReach — 5JAMkYMtvhw @ 00:01:20]. Body: one '
                                        "sentence of value, then 'Are you still handling facility vendors "
                                        "in-house?' Gate check: offer clear in 5 seconds, targeting right, "
                                        'message starts a conversation instead of a lecture [Matt Harriman '
                                        '— hm5isqC1d74 @ 00:06:18].'},
                            {'name': 'reply_decay_and_ai_qc',
                             'type': 'textarea',
                             'prompt': 'Plan how you will monitor reply-rate decay as connection volume '
                                       'grows and how you will quality-check AI-written messages. Record '
                                       'the batch checkpoints, the reply rate expected at each, and the '
                                       'manual-fix threshold that forces you to stop and rework the '
                                       'prompt.',
                             'example': 'Checkpoints follow the HeyReach decay curve: 12% replies on the '
                                        'first 50 connections, 6% on the next 100, 2% on the next 200 '
                                        '[HeyReach — RYTMEUD8-FQ @ 00:01:40]. A fresh segment launches '
                                        'when replies hit 2%. Every AI message batch is sampled; if more '
                                        'than 10% need manual fixes, sending stops and the prompt is '
                                        'rebuilt [HeyReach — RYTMEUD8-FQ @ 00:05:37].'},
                            {'name': 'speed_to_lead_agent',
                             'type': 'textarea',
                             'prompt': 'Describe the speed-to-lead system that contacts every inbound or '
                                       'interested lead. Specify the contact window in minutes, the '
                                       'channel used first, and the end-to-end test you will run on each '
                                       'AI booking function before any client lead touches it.',
                             'example': 'An AI voice agent calls each new Facebook lead inside 5 minutes, '
                                        'the window Zenscape sets [Zenscape — HeluxMYTT0o @ 00:06:55]. '
                                        'Before go-live, the agent is published, every booking function '
                                        'gets its own webhook, and a test call proposes a specific time '
                                        'such as Tuesday 2 p.m. to confirm the calendar writes correctly '
                                        '[Tommy Chryst — YQbr_FhZTo8 @ 00:44:26].'},
                            {'name': 'booking_conversion_audit',
                             'type': 'text',
                             'prompt': 'Set your inbox-management audit line. Record interested leads and '
                                       'booked meetings for the last 30 days, calculate the '
                                       'interested-to-booked rate, and define the daily pitch and offer '
                                       'quotas each appointment setter on your team must hit before adding '
                                       'any new sender volume.',
                             'example': 'Last 30 days: 40 interested, 11 booked, a 27.5% rate, below the '
                                        '35% floor, so inbox handling gets audited first; ten interested '
                                        'producing one booking signals a problem [Matt Harriman — '
                                        'hm5isqC1d74 @ 00:06:18]. Setter quota follows Mendoza: 7 to 12 '
                                        'pitches a day across the team, with each person making at least '
                                        'three offers daily [Melvin Mendoza — OJFNkb_PwS4 @ 00:21:21].'},
                            {'name': 'agency_pricing_and_stack',
                             'type': 'textarea',
                             'prompt': 'Set the pricing for your first three cold email clients and '
                                       'itemize the monthly tool stack that delivers the work. Justify '
                                       'fixed fees versus per-lead billing, list deliverables included in '
                                       'the fee, and name the trigger for raising your price.',
                             'example': "Fixed retainer of $2,000 per month, inside Snovio's $1,500 to "
                                        '$3,000 starter band, covering 1,500 to 2,000 verified contacts, '
                                        'one sequence, weekly report; price rises to $4,000 to $6,000 once '
                                        'case studies exist [Snovio — MmWpOeG5GW4 @ 00:02:46]. Stack runs '
                                        'about $105 monthly: five outreach domains, 10 outreach emails, '
                                        'hosting and Elementor Pro [Michael Gardiner - B2B Strategies — '
                                        'H_dWU8gzLA4 @ 00:10:04].'},
                            {'name': 'sending_domain_plan',
                             'type': 'textarea',
                             'prompt': 'Map the secondary sending domains and mailboxes for your agency '
                                       'launch. Give the domain naming pattern, the redirect target, '
                                       'mailboxes per domain, daily cold sends per mailbox, and the backup '
                                       'pool warming in reserve for when active domains burn out.',
                             'example': "Brand 'star' uses getstar.com, trystar.com and starhq.com, each "
                                        'redirected to the main site [Smartlead — dTLQCIO7Tf0 @ 00:01:46]. '
                                        'Two mailboxes per domain at 25 cold emails each, so 500 daily '
                                        'sends need about 10 accounts on five domains. A second set of '
                                        'five domains and 10 mailboxes warms continuously as backup '
                                        '[Smartlead — dTLQCIO7Tf0 @ 00:15:06].'},
                            {'name': 'compliance_checklist',
                             'type': 'textarea',
                             'prompt': 'Document the compliance controls attached to every cold email you '
                                       'send. Cover the physical address in the footer, the opt-out '
                                       'method, removal speed, centralized suppression across reps and '
                                       'accounts, and the per-email penalty exposure that justifies '
                                       'treating these controls as mandatory.',
                             'example': 'Footer carries a real street address on every touch [Cold '
                                        "Pipeline — tfCx05hBH78 @ 00:03:23]. Prospects reply 'stop' to opt "
                                        'out; each opt-out goes to a global block list the same day, '
                                        'before any lead list is deleted [Namit Jindal | Aerosend — '
                                        'OhSoUY7K_dU @ 00:05:30]. Exposure noted: up to $51,000 per '
                                        'incorrect US email [Namit Jindal | Aerosend — OhSoUY7K_dU @ '
                                        '00:00:00].'}],
                 'completion_gate': 'Do not launch until every sender account has a documented cap, the '
                                    'connection-request split test has a 150-per-arm plan, the booking '
                                    'functions pass an end-to-end test, the interested-to-booked rate is '
                                    'tracked against a 35% floor, and every cold email carries a footer '
                                    'address with opt-outs routed to a global block list.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Google Maps, Local Services Ads, and Rank-and-Rent Asset Builder',
                 'purpose': 'Turn Google Business Profiles, Local Services Ads, and exact-match '
                            'rank-and-rent sites into owned lead assets by locking profile data, '
                            'engineering photo reviews, comparing LSA against shared leads, valuing free '
                            'Maps traffic, scoring niches by per-lead value, and tracking every call by '
                            'source before funding any channel.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Lock name, address, phone, and primary category on every profile before '
                                  'any optimization work, and record who holds edit rights.',
                                  'Price every paid lead source against owned assets, including the true '
                                  'cost of shared leads sold to several companies at once.',
                                  'Back each added profile with a real staffed office, a DBA modifier, and '
                                  'its own phone number, and record the risk position you accept.',
                                  'Run the commission and ticket-size math and check exact-match domain '
                                  'availability before building any rank-and-rent site.',
                                  'Confirm call tracking and CRM source logging work before a single buyer '
                                  'is pitched or a single paid dollar is spent.'],
                 'fields': [{'name': 'gbp_nap_lock',
                             'type': 'text',
                             'prompt': 'Record the locked name, address, phone number, and primary '
                                       'category for each Google Business Profile you manage. State who '
                                       'holds edit rights, how changes are blocked on ranking profiles, '
                                       'and what you will do if a suspension notice arrives.',
                             'example': 'Profile: Northside Plumbing, primary category Plumber. Name, '
                                        'address and phone were set once and are never edited, because an '
                                        'edit on a ranking profile risks suspension [Steve Hunsaker | Home '
                                        'Service Accelerator — PlZ43ZKMk34 @ 00:13:28]. If suspended, the '
                                        'staffed office, lease and signage support an appeal; appeals '
                                        'restored profiles in 3 days [Austin Parker — BVNOmeAp7mg @ '
                                        '00:14:07].'},
                            {'name': 'review_engine',
                             'type': 'textarea',
                             'prompt': 'Describe the review collection engine for each profile. Name the '
                                       'physical tool used at the job site, the CRM automation that '
                                       'follows up, how you will add photos to existing reviews, and which '
                                       'details you want reviewers to mention.',
                             'example': 'Technicians tap a review card at job completion; CRM automation '
                                        'follows up. Past reviewers are asked to edit photos into existing '
                                        'reviews; a profile with 30 reviews, about half with photos, '
                                        'ranked #1-2 [Steve Hunsaker | Home Service Accelerator — '
                                        'wdo4cRHVxXA @ 00:07:15]. Reviewers are prompted to mention price '
                                        'ranges like $8k-$15k so bad-fit callers self-select out '
                                        '[PushLeads — vWdPlgxdJUA @ 00:06:16].'},
                            {'name': 'lsa_cost_comparison',
                             'type': 'textarea',
                             'prompt': 'Compare the cost per lead of Local Services Ads against shared '
                                       'lead marketplaces for your trade. Calculate the true cost of a '
                                       'shared lead after accounting for how many companies receive it, '
                                       'then decide where your next paid dollar should go.',
                             'example': 'LSA leads run $30-40 against $80-150 for shared Angi leads, and '
                                        'one fence client paid $34 per lead across 236 leads [Surge '
                                        'Digital Marketing — pZ9P9Hmof3g @ 00:03:04]. A $60 shared lead '
                                        'sold to four companies effectively costs $240 [Brayden Bass — '
                                        'QnqQKoCeYa8 @ 00:01:05]. Decision: next dollar goes to LSA, while '
                                        'owned profile and review assets get built in parallel.'},
                            {'name': 'lsa_migration_controls',
                             'type': 'textarea',
                             'prompt': 'List the controls you will apply while Local Services Ads migrate '
                                       'into Google Ads. Cover account ownership, performance history '
                                       'capture, profile edit freezes, the bidding approach you will use, '
                                       'and how you will rate leads to retrain targeting.',
                             'example': 'Admin email confirmed as LSA owner, performance history '
                                        'screenshotted, and all GBP edits frozen for migration week, since '
                                        'name or category edits trigger a 24 to 48 hour review [Surge '
                                        'Digital Marketing — pZ9P9Hmof3g @ 00:10:54]. Bidding uses target '
                                        'CPL, because a maximum is a wall and a target is an average. '
                                        "Out-of-area calls are rated 'not relevant' [Local View — "
                                        'bzWbX2kyAhg @ 00:02:21].'},
                            {'name': 'multi_profile_expansion',
                             'type': 'textarea',
                             'prompt': 'Plan any additional business profiles for new service areas. For '
                                       'each location, document the real staffed office, monthly cost, DBA '
                                       'name modifier, dedicated phone number, and the risk position you '
                                       'accept given practitioner disagreement over whether multiple '
                                       'profiles are legitimate.',
                             'example': 'Satellite office in a second suburb at $300-500 a month, staffed, '
                                        'leased and signed, with a DBA modifier and its own local number; '
                                        'forwarding is allowed but a shared number gets the main profile '
                                        'suspended [Andy Walker — FcZZMpjLVNo @ 00:09:14]. Benchmark: '
                                        'three added profiles brought a San Antonio plumber $120K in 60 '
                                        'days [Austin Parker — BVNOmeAp7mg @ 00:00:24].'},
                            {'name': 'maps_traffic_valuation',
                             'type': 'text',
                             'prompt': 'Value the free traffic your Maps profile produced over a recent '
                                       'period. Pull views, calls, and website clicks, assign a dollar '
                                       'value per conversion, state your assumed click-to-conversion rate, '
                                       'and total the figure you would otherwise pay for advertising.',
                             'example': 'Model from Hunsaker, August to December 2025: 53,466 views, 168 '
                                        'calls valued at $100 each for $16,800, and 1,192 website clicks '
                                        'at an assumed 10% conversion, about 119 conversions worth '
                                        '$11,920. Total free traffic value: about $28K [Steve Hunsaker | '
                                        'Home Service Accelerator — PlZ43ZKMk34 @ 00:13:53]. Our profile '
                                        'gets the same calculation each quarter.'},
                            {'name': 'rank_rent_niche_math',
                             'type': 'textarea',
                             'prompt': 'Score a rank-and-rent niche and city before building anything. '
                                       'Record the average customer value, the commission percentage you '
                                       'can negotiate, the calculated value per lead, the exact-match '
                                       'domain availability, and the monthly running cost per site in your '
                                       'portfolio.',
                             'example': 'Ten leads at a 30% close rate on a $2,000 ticket yield $6,000; a '
                                        '7% commission is $420, about $42 per lead [Ippei - Rank and Rent '
                                        "SEO — JuyXW9x-QMs @ 00:08:51]. The city's .com exact-match domain "
                                        'is open, so the build proceeds; a taken domain means skipping the '
                                        'city [Saravanan Ganesh — GHgraINYcOU @ 00:09:34]. Running cost: '
                                        'about $30 monthly.'},
                            {'name': 'buyer_precall_list',
                             'type': 'textarea',
                             'prompt': 'Build the buyer list for your rank-and-rent site before the build '
                                       'begins. Name the businesses you will call, the evidence they '
                                       'already pay for growth, the commission you will propose, and how '
                                       'you will prove lead flow before pitching.',
                             'example': 'Buyers: roofers already running Google Ads with broken landing '
                                        'pages, pitched that one call beats $20 to $40 of clicks [Digital '
                                        'Real Estate Secrets — cSXYPhrwhwo @ 00:08:45]. Handymen are added '
                                        'after asking ChatGPT which businesses do the work, with a roughly '
                                        '7% kickback agreed first [Ippei - Rank and Rent SEO — raunmaNfU1o '
                                        '@ 00:17:25]. Free leads go out before any pitch.'},
                            {'name': 'call_tracking_setup',
                             'type': 'text',
                             'prompt': 'Specify the call tracking setup for each rented or ranked site. '
                                       'Record the tracking number cost, the whisper message buyers hear, '
                                       'how lead source is logged in the CRM, and what happens if the CRM '
                                       'cannot track source at all.',
                             'example': 'Each site routes through a $10 tracking number with a whisper '
                                        "message for the buyer. The buyer's CRM logs every call by source; "
                                        'if a CRM cannot track lead source, no channel gets funded '
                                        '[ProLine — XH8rj3P6nIs @ 00:06:08]. Organic ranking keeps cost '
                                        'near $10 to $20 monthly [Ippei - Rank and Rent SEO — Lr9XDVpYZ8M '
                                        '@ 00:01:11].'},
                            {'name': 'commercial_followup_cadence',
                             'type': 'textarea',
                             'prompt': 'Define the follow-up cadence for commercial roofing leads and the '
                                       'single paid channel you will test. Include same-day response '
                                       'rules, how long old leads stay in rotation, how to handle '
                                       'prospects who go dark, and the monthly test budget.',
                             'example': 'Every lead gets same-day contact; American WeatherStar still '
                                        'follows leads going back 15 years. When a commercial prospect '
                                        'goes dark, voicemails stop, calls continue, the receptionist is '
                                        'asked to page them, and a nearby salesman stops by unannounced '
                                        '[American WeatherStar — sY92btEz6VQ @ 00:02:33]. One channel '
                                        'tested at $3,000 to $10,000 monthly [The STRONG Roofer w/ Adam '
                                        'Bensman — eQNS1yN6pQM @ 00:10:37].'}],
                 'completion_gate': 'Do not fund any channel or pitch any buyer until every profile has '
                                    'locked name, address, and phone with a dedicated number, the '
                                    'LSA-versus-shared-lead math is written down, each rank-and-rent site '
                                    'clears the per-lead value and exact-match domain checks, and the CRM '
                                    'logs lead source on every tracked call.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'TCPA Consent Capture, Lead Distribution, and Follow-Up Control Sheet',
                 'purpose': 'Rebuild lead capture around one-to-one consent, take possession of '
                            'TrustedForm certificates before dialing, classify every contact technology, '
                            'honor revocations fast, and run ping-post distribution with timeouts, price '
                            'ceilings, refund caps, clean buyer integrations, call-duration billing, and a '
                            'follow-up sequence that fires within seconds.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Start with every form that collects a phone number and redesign it so '
                                  'each seller is named and individually selected.',
                                  'Document where the consent certificate lives and confirm the caller '
                                  'holds it before any regulated call or text is placed.',
                                  'Classify every dialer, voice agent, voice drop, and SMS tool as '
                                  'regulated or manual, and write the revocation rules beside it.',
                                  'Configure ping-post timeouts, price ceilings, refund caps, and resale '
                                  'rules before the first buyer receives a live lead.',
                                  'Finish with the integration checklist, call billing rules, and '
                                  'automated follow-up, then test each in sequence before go-live.'],
                 'fields': [{'name': 'consent_form_design',
                             'type': 'textarea',
                             'prompt': 'Redesign every lead form that collects a phone number for '
                                       'one-to-one consent. Specify how each seller is named and '
                                       'individually selected, the checkbox size, CTA wording alignment, '
                                       'contrast standards for disclosure text, and how sellers are '
                                       'ordered on the form.',
                             'example': 'One 24px checkbox per brand, so someone actually checks a box for '
                                        'each brand [LeadCaptureIO — 4hypirM3lEg @ 00:09:48]. CTA text '
                                        'matches the disclosure word for word, in dark text, never light '
                                        'gray on an ashen background. Sellers appear ordered by bid, with '
                                        'no select-all button, which risks being treated as a dark pattern '
                                        '[Lead Generation World — 6VtW3u8e6WE @ 00:17:15].'},
                            {'name': 'trustedform_capture',
                             'type': 'text',
                             'prompt': 'Document how the consent certificate is captured, stored, and '
                                       'handed to the caller. Name the hidden field label, the certificate '
                                       'provider, the retention period, and the point in the workflow '
                                       'where the caller takes possession before any regulated contact '
                                       'happens.',
                             'example': "A hidden field labeled exactly 'XX trusted form cert' captures "
                                        'the TrustedForm URL [LeadCaptureIO — WXqAR94YqtU @ 00:05:24]. '
                                        'Records are stored securely for at least four years '
                                        '[LeadCaptureIO — Zrihem0vYcU @ 00:19:42]. The certificate is '
                                        'claimed by the calling agency before the dialer fires, since the '
                                        'caller cannot rely on the third party to hold it [Lead Generation '
                                        'World — 6VtW3u8e6WE @ 00:25:30].'},
                            {'name': 'regulated_tech_audit',
                             'type': 'textarea',
                             'prompt': 'Inventory every contact technology your team uses and classify '
                                       'each as regulated or manual. Include autodialers, preview dialers, '
                                       'AI voice agents, voice drops, and automated SMS, and note the '
                                       'state-specific dialer interpretation you rely on for each tool.',
                             'example': 'AI voice agent, voice drops and automated SMS are classed '
                                        'regulated and fire only with one-to-one consent on file. The '
                                        'preview dialer is treated as regulated: outside PA, DE and NJ, '
                                        'Troutman says preview dial is likely an ATDS, judged by capacity '
                                        '[Seasalt AI — KBFaRW7QmVQ @ 00:50:43]. Exposure: $500 to $2,000 '
                                        'per violation [Seasalt AI — KBFaRW7QmVQ @ 00:14:15].'},
                            {'name': 'consent_intent_tradeoff',
                             'type': 'text',
                             'prompt': 'Estimate how one-to-one consent changes your form economics. '
                                       'Record current form conversion, the projected conversion loss, the '
                                       'expected contact-rate lift from treating checkboxes as an intent '
                                       'filter, and the resulting change in cost per lead and per '
                                       'contacted lead.',
                             'example': 'Worst case planned at a 10%, 15% or 20% conversion loss, which '
                                        'pushes CPL up [LeadCaptureIO — Zrihem0vYcU @ 00:02:10]. Target '
                                        'case follows the top 10% of LeadCapture users: a 1-3% conversion '
                                        'drop traded for a 10-20% contact-rate lift [LeadCaptureIO — '
                                        'Hd19AToxex4 @ 00:07:03]. Cost per contacted lead becomes the '
                                        'headline number reviewed weekly, replacing raw CPL.'},
                            {'name': 'revocation_and_dnc',
                             'type': 'textarea',
                             'prompt': 'Define how revocations and Do Not Call obligations are honored '
                                       'across every channel. State the honoring deadline you commit to, '
                                       'how clarification texts are worded and tested, when text '
                                       'automation ends on inquiry leads, and which lists are scrubbed '
                                       'before manual calls.',
                             'example': 'Revocations are honored within 24 hours, not at the '
                                        '10-business-day maximum [Lead Generation World — OgyCXKzIJM4 @ '
                                        '00:24:16]. Clarification texts carry no persuasion and opt-out '
                                        'rates are tracked [Troutman Amin, LLP — 9KGQa-Oon7o @ 00:40:40]. '
                                        'Text automation stops at day 90; from day 91 calls are manual '
                                        'after national and state DNC scrubs [Lauro Herrera — tRO0J70WjKA '
                                        '@ 00:13:21].'},
                            {'name': 'ping_post_configuration',
                             'type': 'textarea',
                             'prompt': 'Configure your ping-post auction for each lead vertical. Specify '
                                       'which fields travel in the ping, how bids are compared, the margin '
                                       'you carve out, the ping and post timeout windows, and how the lead '
                                       'ID links the ping to the post.',
                             'example': 'The ping goes out without personal information to all eligible '
                                        'buyers, with non-required fields stripped [Lead Prosper — '
                                        'Ma1kH51odZ0 @ 00:00:23]. Timeouts sit at 15 seconds for the ping '
                                        'and 30 for the post, so lagging servers drop out [boberdoo.com — '
                                        'DSbDVWpyXUI @ 00:15:43]. The lead ID travels on the post only, '
                                        "echoing the ping's ID [boberdoo.com — CLgSYIHZ_GY @ 00:00:39]."},
                            {'name': 'buyer_price_controls',
                             'type': 'textarea',
                             'prompt': 'Set the financial guardrails on every buyer in your distribution '
                                       'system. Record the max best price ceiling for dynamic bidders, the '
                                       'refund cap and its lookback window, the resale rule for rejected '
                                       'leads, and your policy on revenue-share buyers.',
                             'example': 'Every dynamic buyer gets a max best price ceiling so a $1,000 '
                                        'typo bid cannot pass $900 back to a seller [boberdoo.com — '
                                        'DSbDVWpyXUI @ 00:17:44]. Refunds are capped at 15% over the past '
                                        '30 days [boberdoo.com — yCAVYNpSdZI @ 00:22:50]. Rejected leads '
                                        "resell as 'yes but sold non-exclusively' while price stays above "
                                        'cost. Rev-share buyers stay outside ping post.'},
                            {'name': 'buyer_integration_checklist',
                             'type': 'textarea',
                             'prompt': 'Write the integration checklist for onboarding a new buyer '
                                       'endpoint. Cover payload type selection, required field '
                                       'confirmation with the buyer, test flags on ping and post, the '
                                       'steps you take to strip test parameters, and the final go-live '
                                       'handoff.',
                             'example': 'Step one: set payload type to JSON before editing, since '
                                        'switching later resets the builder [Lead Prosper — gX0fjRlg1lg @ '
                                        '00:01:33]. Step two: confirm wanted fields with Phonexa buyers, '
                                        'because most are optional. Step three: run with lp_test set to 1 '
                                        'on ping and post [Lead Prosper — _1N3fncM-Ss @ 00:00:21]. Step '
                                        'four: strip lp_action test, then copy all to the buyer.'},
                            {'name': 'call_qualification_rules',
                             'type': 'text',
                             'prompt': 'Define the billing rules for pay-per-call traffic. State the price '
                                       'per qualified call, the minimum duration that qualifies a call, '
                                       'how calls under that threshold are handled, and how many networks '
                                       'you will sell through to avoid single-network dependence.',
                             'example': 'Calls sell at $100 each [Local SEO Made Easy — Bu_9XhXpDSs @ '
                                        '00:02:33]. A call qualifies at 90 seconds; anything shorter, like '
                                        'the 47-second call in the network example, never bills and never '
                                        'gets paid [Local SEO Made Easy — Bu_9XhXpDSs @ 01:03:07]. Traffic '
                                        'is split across at least two networks, following the warning not '
                                        'to stay on just one limited network.'},
                            {'name': 'followup_automation',
                             'type': 'textarea',
                             'prompt': 'Map the automated follow-up that fires when a new lead enters your '
                                       'CRM. Include the voice AI callback window, the SMS sequence '
                                       'length, the hand-off to a human rep, and the check you will run on '
                                       'lifetime value before adding ad platforms.',
                             'example': "Voice AI agent 'Alex' calls every new sign-up within 60 seconds "
                                        'inside the GoHighLevel sequence [Jason Grossman — Ot93upK_YX4 @ '
                                        '00:52:38], followed by a three-step SMS sequence and a hand-off '
                                        'to a rep on reply. Before any ad platform is added, lifetime '
                                        'value is reviewed, since the business might be fine and just need '
                                        'to tweak the LTV [MoreMozi — 94mDeuLH24c @ 00:02:29].'}],
                 'completion_gate': 'Do not route a live lead until every phone-capturing form has '
                                    'per-brand checkboxes, the TrustedForm certificate is claimed before '
                                    'dialing, every contact tool is classified, revocations clear within '
                                    '24 hours, each buyer has a price ceiling and refund cap, test flags '
                                    'are stripped, calls bill only past the duration qualifier, and voice '
                                    'AI follow-up fires within 60 seconds.'}]}
