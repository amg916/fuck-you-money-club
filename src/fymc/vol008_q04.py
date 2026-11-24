from __future__ import annotations

CHAPTER_4 = {'id': 'Q4',
 'chapter_id': 'Q4',
 'chapter_number': 4,
 'question_number': 4,
 'slug': 'clay-enrichment-and-outbound-workflows',
 'question_prompt': 'How do practitioners use Clay to enrich prospect records, identify relevant '
                    'companies, and assemble outbound workflows?',
 'kicker': 'Q4 / THE BIG MONEY PLAYBOOKS',
 'title': 'Clay Enrichment and Outbound Workflows',
 'subtitle': 'Beginner setup, email and phone waterfalls, company enrichment, topic intent, Claygent '
             'research, AI-assisted prospecting, and practical platform reviews',
 'layout_template': 'comparison_matrix',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners running Clay at agency scale agree that single-database lists leak '
                      "coverage. AJ Cassata sees Apollo 'valids' verify at only 40%, and traditional "
                      'databases supply emails for 40-50% of a list, while a stacked waterfall lifts that '
                      'to 60-80%. The street mechanics are consistent: import from Apollo, AI Ark, '
                      'LinkedIn or Google Maps, exclude a DNC table, run a cheapest-first email waterfall '
                      'capped around four steps, validate, classify with forced yes/no AI outputs, gate '
                      'every column with run conditions, test on 10 rows, then push to Smartlead or '
                      "Instantly. Using your own API keys avoids Clay's markup. The disagreements center "
                      'on waterfall depth (Cassata cuts at four, Matt Lucero runs 11 providers, Romain '
                      'Osman skips the waterfall for Prospeo alone) and on whether Clay replaces ZoomInfo '
                      'or only complements it.',
 'key_metrics': [{'label': "Apollo 'Valid' Email Verification Rate",
                  'metric': "Apollo 'Valid' Email Verification Rate",
                  'value': "Only 40% of 'valid' emails verify",
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Of 5,000 Apollo leads, even the emails marked valid often verify at only '
                             '40%; mailing invalids burns inboxes and domains.',
                  'source': 'AJ Cassata ([6l8CThrSJEY @ 00:03:00])'},
                 {'label': 'Waterfall Email Coverage vs Single Database',
                  'metric': 'Waterfall Email Coverage vs Single Database',
                  'value': '60-80% with a waterfall vs 40-50% from traditional databases',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Stacking providers in a Clay waterfall gets 'up to 60 to 80% of your list to "
                             "have an email,' almost double a single database.",
                  'source': 'AJ Cassata ([12s-u4y1VF0 @ 00:04:38])'},
                 {'label': '11-Provider Work-Email Waterfall Hit Rate',
                  'metric': '11-Provider Work-Email Waterfall Hit Rate',
                  'value': '9 of 10 valid emails found',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Work-email waterfall across 11 providers with validation between each step, '
                             'Prospeo and LeadMagic moved to the front.',
                  'source': 'Matt Lucero ([jEkDgA8hPmo @ 00:25:01])'},
                 {'label': 'Clay Credit Cost per Action',
                  'metric': 'Clay Credit Cost per Action',
                  'value': '1-3 credits per email lookup; 5-10 credits per AI research run',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Caffrey tells builders to think of credits 'as tokens' when sizing a plan "
                             'and budgeting a table.',
                  'source': 'Xavier Caffrey GTM ([kY5E4wl8wlA @ 00:06:54])'}],
 'sections': [{'heading': 'The Practitioner Consensus',
               'paragraphs': ['Every operator here starts from the same premise: no single database holds '
                              'your whole market. AJ Cassata, co-founder of the outbound agency Revenue '
                              "Boost, reports that of 5,000 Apollo leads, even the 'valid' emails often "
                              'verify at only 40%. Cassata warns that mailing invalids triggers bounces, '
                              'spam placement, and burned inboxes and domains [6l8CThrSJEY @ 00:03:00]. '
                              'Mark Colgan puts it plainly for non-technical users: Apollo will not have '
                              'every email, some of the ones it does have will not be valid, so you '
                              "cross-check against other providers [N-15SMLSc3c @ 00:00:12]. Matt Lucero's "
                              'agency sends hundreds of thousands of cold emails a month. In one demo '
                              'Lucero worked an Apollo export that carried emails for only about half the '
                              'rows before any enrichment [HqdvpIGiOz4 @ 00:03:36]. The fix they converge '
                              'on is the waterfall: ping providers in sequence, stop at the first accurate '
                              'hit, and pay only when something is found. Cassata puts the upside at '
                              'moving from the 40-50% coverage that traditional databases deliver to '
                              "60-80% of a list, 'almost double' [12s-u4y1VF0 @ 00:04:38]. That gap is the "
                              'whole business case. More reachable contacts per account means more of the '
                              'target market gets touched before a list has to be recycled, and fewer '
                              'bounces eat through the sending domains that every campaign depends on.',
                              "The second point of agreement is what Clay actually is. Clay's own channel "
                              'pitches it as a data aggregator rather than a data provider. It plugs into '
                              '80-plus sources and bills per use, so you pay only for data successfully '
                              'returned [v31hKg-WSCc @ 00:02:00]. Matt Lucero runs over 1M cold emails a '
                              'month through Clay and reports just under 5,000 sales meetings. Lucero '
                              "calls it a 'data orchestrator,' a canvas that stitches the GTM stack "
                              "together, and adds that 'the best tools are usually specialist tools' "
                              '[jEkDgA8hPmo @ 00:01:40]. Patrick Spychalski spells out the economics: Clay '
                              "has no data warehouse of its own and resells providers' data for credits, "
                              'which is why a waterfall charges only the provider that hits [YLXzWpknuJk @ '
                              "00:19:22]. AJ Cassata describes the role the same way: 'It does not replace "
                              "outreach tools. It sits in the middle of everything we already use.' Apollo "
                              'and D7 feed in, and Instantly and HeyReach sit on the other end '
                              '[AtF_XaOE3As @ 00:11:48]. The shared operating model is Find, Enrich, '
                              'Transform, Export. You import lists, layer enrichments, turn the output '
                              'into scores, tags and copy, then push to a sequencer, CRM, or dialer. None '
                              'of these practitioners treats Clay as the sender. It is the research and '
                              'routing layer that sits in front of the sender.',
                              'Third, the qualification layer is where the money is made. AJ Cassata notes '
                              'there is no database filter for B2B versus B2C, for commercial versus '
                              'residential contractors, or for whether a company actually sells data. '
                              'Instead, AI scans websites and third-party sources and returns a yes/no '
                              'answer or a 1-10 score that routes top leads to the best reps [12s-u4y1VF0 '
                              "@ 00:05:33]. Matt Lucero forces prompts to 'only output B2B or b2c' so the "
                              "column can be filtered, and runs work in small chunks so mistakes don't "
                              'burn credits [HqdvpIGiOz4 @ 00:23:16]. The guardrails are near-universal. '
                              'Romain Osman, credited with over 1,000 B2B appointments from cold email and '
                              "LinkedIn, puts it bluntly: add a condition every time, 'otherwise it's just "
                              "going to run for all of your rows and so you're going to lose a lot of "
                              "credits' [RodU66qhDeY @ 00:10:37]. GTM With Deepika's rule is 'for testing "
                              "just run two to three rows,' and each funding and tech-stack waterfall only "
                              'fires when the input fields are present [1AB3H7aWJ0Q @ 00:10:15]. The '
                              'baseline every serious builder shares has five parts: a do-not-contact '
                              'exclusion table, conditional run logic on every paid column, forced binary '
                              'AI outputs, a test batch before the full run, and validation before '
                              'anything touches a sending inbox.'],
               'table': {'caption': 'Where Clay operators agree: the baseline prerequisites before any '
                                    'campaign launches',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Single-database exports leak valid email coverage',
                                   'Of 5,000 Apollo leads, even the valids often verify at only 40%',
                                   'Never send straight from a database export without re-verifying every '
                                   'email first',
                                   'AJ Cassata ([6l8CThrSJEY @ 00:03:00])'],
                                  ['Waterfalls nearly double reachable contacts on a list',
                                   'Traditional databases give emails for 40-50%; a waterfall reaches '
                                   '60-80% of the list',
                                   'Stack providers in sequence instead of paying for one bigger annual '
                                   'data contract',
                                   'AJ Cassata ([12s-u4y1VF0 @ 00:04:38])'],
                                  ['Cross-check every provider because none has complete data',
                                   "Apollo won't have all emails, and some it does have won't be valid",
                                   "Treat any single provider's email as unconfirmed until another source "
                                   'or validator agrees',
                                   'Mark Colgan | Outbound & Pipeline for B2B SaaS ([N-15SMLSc3c @ '
                                   '00:00:12])'],
                                  ['Clay bills only for data that actually returns',
                                   'Per-use waterfall billing means you pay only for data successfully '
                                   'returned by a provider',
                                   'Deep waterfalls cost nothing extra on misses, so the price is set by '
                                   'hits',
                                   'Clay ([v31hKg-WSCc @ 00:02:15])'],
                                  ["Own API keys beat paying Clay's credit markup",
                                   'Use your own Findymail API key because Clay charges a markup on '
                                   'provider credits',
                                   'Once a provider proves itself, connect its key directly and stop '
                                   'paying resale rates',
                                   'AJ Cassata ([12s-u4y1VF0 @ 00:15:36])'],
                                  ['Run conditions must gate every paid enrichment column',
                                   'Without a condition a column runs for all rows and you lose a lot of '
                                   'credits',
                                   "Add an 'only run if' rule before enabling any column that spends "
                                   'credits',
                                   'Romain Osman Lead Generation ([RodU66qhDeY @ 00:10:37])'],
                                  ['Test a small batch before running the full table',
                                   'Ran 10 rows first as a test before the full 50-lead B2B check',
                                   'Validate prompt logic and provider order on ten rows before committing '
                                   'the credit budget',
                                   'Matt Lucero ([jEkDgA8hPmo @ 00:17:57])']]}},
              {'heading': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Start with the price sheet. Xavier Caffrey runs the OneWay agency and '
                              'claims more than $100M in generated pipeline. Caffrey lays out the tiers '
                              'this way. Free gives 100 credits. Starter costs $149 for 2,000 credits, '
                              '5,000 searches, phone data and your own API keys. Explorer costs $349 for '
                              '10,000 credits plus HTTP API, webhooks and exclusions, and Caffrey '
                              'recommends it for most users. Pro costs $800 for 50,000 credits and CRM '
                              'sync [kY5E4wl8wlA @ 00:04:22]. Caffrey says to think of credits as tokens: '
                              'an email lookup runs 1-3 credits and AI research runs 5-10. Sales Feed, a '
                              "self-described non-technical seller, judged Starter worth it: 'the 149 I "
                              "think is about what I pay for Sales Navigator a month anyway' [Z9xzPDRrQHw "
                              '@ 00:07:54]. On the AI side, Matt Lucero priced a GPT-4o Mini call at about '
                              "$0.00126, 'a tenth of a penny.' Premium models cost 'a penny 2 pennies 5 "
                              "pennies 10 pennies' per row, so the cheap model writes a reusable summary "
                              'and Claude 3.5 Sonnet is used only for interpretation [HqdvpIGiOz4 @ '
                              "00:19:33]. Provider prices vary widely. GTM With Deepika's tech-stack "
                              'waterfall ordered tools at 1, 2, 4 and 18 credits per row, cheapest first, '
                              'and the waterfall only fired when domain and funding were already present '
                              '[1AB3H7aWJ0Q @ 00:07:26].',
                              "The email waterfall is the core build. Mark Colgan's demonstrated order "
                              'runs Findymail, then LeadMagic, then Prospeo, then Dropcontact, checking '
                              'each provider in turn until all have been checked [N-15SMLSc3c @ 00:00:29]. '
                              "AJ Cassata's minimum inputs are full name plus company domain, or the "
                              'LinkedIn profile alone. Cassata finds that valid emails usually come from '
                              'the first two or three columns, puts the cheapest provider first, and caps '
                              'waterfalls at about four steps because returns diminish [6l8CThrSJEY @ '
                              '00:13:17]. Matt Lucero runs the opposite extreme: 11 providers with '
                              'validation between each step and Prospeo and LeadMagic moved to the front, '
                              'which returned 9 of 10 valid emails [jEkDgA8hPmo @ 00:21:30]. Romain Osman '
                              "pitches an eight-step 'basic workflow' as covering 90% of campaigns, and it "
                              'adds deliverability checks before any spend. First comes a DNC lookup on '
                              'company domain. Next is an MX provider check through a free LeadMagic HTTP '
                              'API that skips Microsoft 365 rows for low deliverability. Then come '
                              'Debounce validation and Prospeo enrichment. Finally, a merge column sends '
                              'risky, unknown and catch-all emails to Enrich.so for a second verdict '
                              "[RodU66qhDeY @ 00:05:09]. Osman's 'master email' column merges Debounce "
                              'safe-to-send, Prospeo valid, and Enrich.so valid results into one field '
                              'that feeds Instantly or Smartlead.',
                              "Once the email is found, AI turns raw rows into routing and copy. Clay's "
                              'own CRE dinner campaign chains several steps. A LinkedIn import feeds a '
                              'company-description enrichment, Claygent finds the office address, and '
                              'OpenAI writes a blurb on what the company does. A casualization step '
                              "follows, because a full street address makes it 'obvious that a robot is "
                              "sending that email.' Then come a Yelp lookup for dinner near HQ and an "
                              'Instantly push with variables [tbe8LBJOSSc @ 00:06:05]. Xavier Caffrey runs '
                              "a Claygent website-design template that rates each site. A 'Hey {first "
                              "name}, saw that you guys...' opener only runs if the design rating is 7 or "
                              'higher [UpSWlkeuUqs @ 00:10:43]. AJ Cassata generates a first line that '
                              "opens with 'I found you from your work on...', maps it as an Instantly "
                              'variable, and connects a personal ChatGPT or Claude key to cut cost '
                              '[12s-u4y1VF0 @ 00:19:11]. Matt Lucero pushes to Smartlead only if the row '
                              "is B2B, and toggles 'allow leads that exist in other campaigns' and "
                              "'community bounce list' on the way out [HqdvpIGiOz4 @ 00:25:17]. The "
                              'pattern repeats across all of these builds. Every AI column outputs '
                              'something filterable, every paid column carries a condition, and only '
                              'qualified, validated rows reach the sequencer.'],
               'table': {'caption': 'Street-level Clay tooling, plan pricing and per-row credit math as '
                                    'taught by the operators',
                         'headers': ['Tool or Step',
                                     'Exact Mechanic Taught',
                                     'Number or Price Stated',
                                     'Expert Source'],
                         'rows': [['Clay Starter plan for first paid builds',
                                   'Includes 5,000 searches, scheduling, phone data, your own API keys and '
                                   'signals',
                                   '$149 per month for 2,000 credits',
                                   'Xavier Caffrey GTM ([kY5E4wl8wlA @ 00:03:19])'],
                                  ['Clay Explorer plan recommended for most users',
                                   'Adds HTTP API, webhooks, sequencing and exclusions; webhooks are '
                                   "Caffrey's favorite feature",
                                   '$349 for 10,000 credits and 10,000 searches',
                                   'Xavier Caffrey GTM ([kY5E4wl8wlA @ 00:04:22])'],
                                  ['Provider pruning inside the email waterfall',
                                   'Delete providers costing over 10 credits per row and move the cheapest '
                                   'to the front',
                                   'Some providers cost 20-25 credits per row',
                                   'AJ Cassata ([6l8CThrSJEY @ 00:11:35])'],
                                  ['AI column cost on Clay credits',
                                   'Run an AI column on Clay credits or plug in your own OpenAI key',
                                   '1.1 credits per AI column; one run cost about 2 cents',
                                   'Matt Lucero ([jEkDgA8hPmo @ 00:15:14])'],
                                  ['Company-level research before people-level lookup',
                                   'Run research once per company, then look it up from the people table',
                                   'Running research per lead costs 2-3 times as much',
                                   'Xavier Caffrey GTM ([kY5E4wl8wlA @ 00:22:10])'],
                                  ['Claygent as a cheaper funding-data alternative',
                                   'Use Claygent instead of a multi-tool funding waterfall; it errored '
                                   'when social links were unmapped',
                                   'Around one credit per row',
                                   'GTM With Deepika ([1AB3H7aWJ0Q @ 00:06:21])'],
                                  ['Mobile-number waterfall after email is secured',
                                   'Run the mobile waterfall as a separate step after the work-email '
                                   'waterfall finishes',
                                   '14 mobile providers in the waterfall',
                                   'Matt Lucero ([jEkDgA8hPmo @ 00:24:10])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Credit Discipline Moves the Operators Swear By',
                           'body': 'These are the small switches and ordering rules that separate a table '
                                   'that burns its whole monthly budget from one that runs on a fraction '
                                   'of it.',
                           'items': ['Delete any waterfall provider charging over 10 credits per row and '
                                     'put the cheapest first; valid emails usually land in the first 2-3 '
                                     'columns anyway [AJ Cassata — 6l8CThrSJEY @ 00:11:35]',
                                     "Turn auto-update off so Clay 'won't run the entire table by "
                                     "accident' and you keep your credits [Xavier Caffrey GTM — "
                                     'kY5E4wl8wlA @ 00:19:24]',
                                     'Skip the mobile lookup whenever the email waterfall comes back '
                                     "empty: 'I don't want their mobile phone if I don't get their email' "
                                     '[The AI Ops Guy — nRh4F859Xjo @ 00:19:15]',
                                     'Use formulas for cleanup and logic wherever possible, because '
                                     'formulas are free and never touch your credit balance [Patrick '
                                     'Spychalski — YLXzWpknuJk @ 00:25:57]']},
               'sop_steps': [{'step': 1,
                              'title': 'Build the List and Strip Do-Not-Contacts',
                              'action': 'Import leads, clean the domain, then run a multi-row lookup '
                                        'against a DNC table before any paid column.',
                              'detail': "Run 'look up multiple rows in other table' against a DNC table "
                                        'that holds clients and opt-outs, with target column company '
                                        "domain and filter operator 'equals'. Every downstream column then "
                                        'skips the row if a record is found [Romain Osman Lead Generation '
                                        '— RodU66qhDeY @ 00:02:04].'},
                             {'step': 2,
                              'title': 'Qualify with a Forced True/False AI Column',
                              'action': 'Use the meta-prompter to write a B2B true/false check, set a max '
                                        'cost, and test 10 rows first.',
                              'detail': 'Lucero used the meta-prompter to build a B2B true/false column, '
                                        "chose the model, set a max cost, added 'run only if' logic and "
                                        'tested 10 rows. In the full run, 33 of the 50 leads came back B2B '
                                        '[Matt Lucero — jEkDgA8hPmo @ 00:13:47].'},
                             {'step': 3,
                              'title': 'Run a Capped, Cheapest-First Email Waterfall',
                              'action': 'Order providers by cost, cap at about four steps, and gate '
                                        'fallbacks on an empty work email.',
                              'detail': "Set the fallback run condition to 'only run if work email is "
                                        "empty'. Use Claygent to 'visit their website and find me an "
                                        "email', and search other job titles at companies that still have "
                                        'no valid address [AJ Cassata — 6l8CThrSJEY @ 00:16:35].'},
                             {'step': 4,
                              'title': 'Normalize, Personalize and Push to the Sequencer',
                              'action': 'Normalize company names, generate variables, and push only '
                                        'qualified, validated rows to Instantly.',
                              'detail': 'Find founders, CEOs and presidents, run the work-email waterfall, '
                                        'normalize the company name, then push to Instantly with the '
                                        'enriched fields mapped as variables [Clay — tbe8LBJOSSc @ '
                                        '00:07:18].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split among operators is how long the email waterfall should '
                              'run. AJ Cassata of Revenue Boost says valid emails usually surface in the '
                              'first two or three provider columns, so the waterfall gets capped at about '
                              'four steps because returns diminish fast after that [6l8CThrSJEY @ '
                              "00:13:17]. The Clay channel's own demo, by contrast, runs a work-email "
                              'waterfall across six different data providers off nothing more than a name '
                              'and a company domain [tbe8LBJOSSc @ 00:02:23]. Matt Lucero goes further '
                              'still, chaining eleven providers with validation between each step and '
                              'pulling Prospeo and LeadMagic to the front, which returned nine valid '
                              'emails out of ten test rows [jEkDgA8hPmo @ 00:21:30]. Romain Osman sits at '
                              'the opposite extreme: in a workflow built to cover most campaigns, Osman '
                              "runs no waterfall at all because Prospeo's coverage is good enough on its "
                              'own, with LeadMagic, TryKitt and ICPs held back as an optional chain '
                              "[RodU66qhDeY @ 00:06:32]. Cassata's case for short chains is cost: anything "
                              'not found after four or five providers is unlikely to appear later, so the '
                              "tail providers get cancelled. Lucero's long chain leans on validation "
                              'between every hop rather than on a short provider list.',
                              'Practitioners also split on whether Clay replaces the data stack or simply '
                              'sits on top of it. Xavier Caffrey, who runs the OneWay agency, pitches '
                              "Clay's 105-plus data sources as enough to replace Apollo, ZoomInfo and "
                              'Lusha outright [kY5E4wl8wlA @ 00:01:07]. Patrick Spychalski pushes back: '
                              'Clay complements ZoomInfo and is probably not a replacement, and Clay holds '
                              "no data warehouse of its own, reselling providers' data for credits "
                              '[YLXzWpknuJk @ 00:10:28]. Mark Colgan takes the specialist line, paying '
                              'separately for LeadMagic as the main finder and validator, running it on '
                              "non-Clay projects, and warning that you don't have to use Clay for "
                              'everything [N-15SMLSc3c @ 00:01:14]. The economics follow the philosophy. '
                              'Caffrey recommends testing providers inside Clay at a discount and then '
                              'buying directly from the winner, and AJ Cassata uses Clay credits to trial '
                              'tools such as Semrush before switching to direct API keys because credits '
                              'carry a markup, arguing that used right, Clay can actually save you money '
                              '[AtF_XaOE3As @ 00:16:38]. The Clay channel concedes the same point from its '
                              'side: once your own API key is connected, that waterfall step is not '
                              'charged. Matt Lucero, who calls Clay a data orchestrator, sums up the camp: '
                              'the best tools are usually specialist tools.',
                              'How much AI belongs in the workflow is the third fault line. Romain Osman '
                              'opens with a deliberately basic build, no AI personalization, and claims it '
                              'covers ninety percent of campaigns, leaning on DNC lookups, MX checks, '
                              'validation and a clean master email column instead [RodU66qhDeY @ '
                              '00:00:00]. AJ Cassata runs the opposite shop: AI is ninety percent of '
                              "Revenue Boost's Clay usage, from picking an e-commerce store's dominant "
                              'traffic channel to dropping its top-selling product into the subject line '
                              '[AtF_XaOE3As @ 00:11:05]. Patrick Spychalski splits the difference, '
                              'describing their own outbound copy as roughly half human and half AI '
                              '[YLXzWpknuJk @ 00:04:31]. The Clay channel frames the tool as the opposite '
                              "of a volume cannon, stating that Clay isn't a plug-and-play AI tool looking "
                              'to 10x the volume of outreach to customer spam folders [v31hKg-WSCc @ '
                              "00:03:58]. Cassata's stated reason for heavy AI is that reply rates are "
                              'lower now because outreach is saturated, and Cassata answers it with '
                              'variables like other business types, role focus and an AI-picked case '
                              "study. Osman's build answers with plumbing rather than prose, merging "
                              'Debounce safe-to-send, Prospeo valid and Enrich.so valid results into one '
                              'master email column before anything reaches Instantly or Smartlead, and '
                              'using AI only to strip LLC, Ltd and Inc from company names.'],
               'table': {'caption': 'Competing Clay playbooks: who runs what, and why',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Email waterfall depth per row',
                                   'Cap the chain near four steps because valid emails usually land in the '
                                   'first two or three columns',
                                   'Chain six to eleven providers, with Lucero validating between every '
                                   'step and front-loading Prospeo and LeadMagic',
                                   'AJ Cassata ([6l8CThrSJEY @ 00:13:17]); Matt Lucero ([jEkDgA8hPmo @ '
                                   '00:21:30])'],
                                  ['Waterfall versus a single strong finder',
                                   'Skip the waterfall entirely because Prospeo coverage is strong enough '
                                   'for most campaigns',
                                   'Rerun the 40 percent that fail NeverBounce through another finder to '
                                   'lift contact coverage',
                                   'Romain Osman Lead Generation ([RodU66qhDeY @ 00:06:32]); AJ Cassata '
                                   '([AtF_XaOE3As @ 00:05:12])'],
                                  ['Clay as stack replacement or orchestration layer',
                                   "Replace Apollo, ZoomInfo, Lusha and even Sales Navigator with Clay's "
                                   'aggregated data sources',
                                   'Keep ZoomInfo and specialist accounts like LeadMagic, using Clay to '
                                   'orchestrate rather than replace them',
                                   'Xavier Caffrey GTM ([kY5E4wl8wlA @ 00:01:07]); Sales Feed '
                                   '([Z9xzPDRrQHw @ 00:07:54]); Patrick Spychalski ([YLXzWpknuJk @ '
                                   '00:10:28])'],
                                  ['Where the list build starts',
                                   'Start with a company search because it is a lot more specific, then '
                                   'find people',
                                   'Start with a people search via Sculptor, such as new CMOs at 11 to 200 '
                                   'employee firms',
                                   'Xavier Caffrey GTM ([UpSWlkeuUqs @ 00:00:29]); Matt Lucero '
                                   '([jEkDgA8hPmo @ 00:07:09])'],
                                  ['Primary lead database feeding the Clay table',
                                   'Import from AI Ark after dropping Apollo, merging Google Maps scrapers '
                                   'for local businesses',
                                   'Import straight from Apollo, then clean full names and domains with '
                                   'formulas before enrichment',
                                   'AJ Cassata ([12s-u4y1VF0 @ 00:14:17]); Romain Osman Lead Generation '
                                   '([RodU66qhDeY @ 00:00:33])'],
                                  ['How much AI runs inside the workflow',
                                   'Basic build with no AI personalization, claimed to cover 90 percent of '
                                   'campaigns',
                                   'AI drives 90 percent of usage: research, scoring, channel routing and '
                                   'subject lines',
                                   'Romain Osman Lead Generation ([RodU66qhDeY @ 00:00:00]); AJ Cassata '
                                   '([AtF_XaOE3As @ 00:11:05])'],
                                  ['Where sequencing happens at high volume',
                                   "Clay's Campaigns feature, a white-labeled Smartlead, keeps sending "
                                   'inside the Clay canvas',
                                   'Standalone Smartlead or Instantly once volume reaches 1,000 to 10,000 '
                                   'cold emails a day',
                                   'Matt Lucero ([jEkDgA8hPmo @ 00:28:48]); Patrick Spychalski '
                                   '([YLXzWpknuJk @ 00:37:07])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The first trap every practitioner reports is trusting a single database. AJ '
                              'Cassata says that out of 5,000 Apollo leads, even the emails flagged as '
                              'valid often verify at only forty percent, and that mailing invalids drives '
                              'bounces, spam placement and burned inboxes and domains [6l8CThrSJEY @ '
                              '00:03:00]. Matt Lucero saw the same pattern in a live build, where an '
                              'Apollo export carried emails for only about half the rows, and warns that '
                              'skipping validation produces high bounce rates [HqdvpIGiOz4 @ 00:05:40]. '
                              'Romain Osman adds an infrastructure filter most beginners miss: an MX check '
                              'through a free LeadMagic HTTP call flags Microsoft 365 domains, which Osman '
                              'skips for low deliverability [RodU66qhDeY @ 00:04:25]. Volume makes it '
                              'worse. Cassata warns that the more you scale cold email, the more you are '
                              'going to land in spam, which is why the local-restaurant opener in the '
                              'Revenue Boost demo doubles as a deliverability play [AtF_XaOE3As @ '
                              '00:22:47]. Cassata also ties coverage to TAM math, describing improved '
                              'coverage of a 100,000-contact market from a 40,000 baseline as more than '
                              'doubling revenue potential, with better coverage also delaying lead '
                              'recycling. That upside only lands if every added address clears validation '
                              'before it touches a sending inbox.',
                              'Credit burn is the second recurring loss, and it hits from several '
                              'directions. Cassata warns that a waterfall provider can find an email that '
                              'then fails validation, and Clay still charges for the find, which is one '
                              'reason to delete providers costing over ten credits a row and put the '
                              'cheapest first [6l8CThrSJEY @ 00:13:30]. Romain Osman calls run conditions '
                              'non-negotiable: without one, a column runs for all rows and you lose a lot '
                              'of credits [RodU66qhDeY @ 00:10:37]. Xavier Caffrey flags a structural '
                              'leak: running research per lead instead of once at the company level and '
                              'looking it up from the people table costs two to three times as much, and '
                              'leaving auto-update on lets Clay run the entire table by accident '
                              '[kY5E4wl8wlA @ 00:22:10]. Hamza Sakib, The AI Ops Guy, found a quieter '
                              'drain in Topic Intent: topics Clay auto-adds produce weak signals that lead '
                              'to the wrong people and use up a lot of credits, so only high and medium '
                              'intent stays in the run [nRh4F859Xjo @ 00:05:32]. Caffrey prices an email '
                              'lookup at one to three credits and AI research at five to ten, and tells '
                              'operators to think of credits as tokens.',
                              'AI research fails quietly, and practitioners show it on camera. Sales Feed '
                              'tried to find software companies with Glassdoor complaints about HR, '
                              'benefits or payroll for a Rippling-style pitch, and the search came back '
                              'empty: no companies were found, and the reviews it did surface lacked the '
                              'specific details requested [Z9xzPDRrQHw @ 00:03:57]. The fix, recorded '
                              'later, was defining multiple outputs such as yes/no and turnover percentage '
                              "and using the AI formula builder to force a true/false answer. Deepika's "
                              'funding waterfall showed a different break: Claygent was the cheap path at '
                              'about one credit per row, but it errored when social links were not mapped '
                              "as inputs [1AB3H7aWJ0Q @ 00:06:05]. Matt Lucero says AI output isn't "
                              'perfect, so the B2B classifier ran on ten rows before the full pull, and 33 '
                              'of 50 leads came back B2B [jEkDgA8hPmo @ 00:17:57]. Then there is the '
                              'learning curve. Patrick Spychalski calls Clay a hard tool and tells '
                              'operators to expect it [YLXzWpknuJk @ 00:32:10], while Sales Feed, months '
                              'into using Clay and partnered with it, still finds the APIs intimidating '
                              'and advises delegating the build to ops, an agency or a freelancer because '
                              'competitors will win otherwise.'],
               'table': {'caption': 'Firsthand traps and the fixes practitioners applied',
                         'headers': ['Failure Mode',
                                     'What Practitioners Hit',
                                     'Fix They Applied',
                                     'Expert Source'],
                         'rows': [['Trusting database valid emails at face value',
                                   'Of 5,000 Apollo leads, even the valids often verify at only 40 percent',
                                   'Run a waterfall, then validate every address before it touches a '
                                   'sender',
                                   'AJ Cassata ([6l8CThrSJEY @ 00:03:00]); Matt Lucero ([HqdvpIGiOz4 @ '
                                   '00:05:40])'],
                                  ['Paying for finds that later fail validation',
                                   'A provider returns an email that then fails validation and the credit '
                                   'is still charged',
                                   'Cap waterfalls near four steps and keep validation inside the chain',
                                   'AJ Cassata ([6l8CThrSJEY @ 00:13:30])'],
                                  ['Expensive providers sitting early in the chain',
                                   'Some providers cost 20 to 25 credits per row; one tech-stack source '
                                   'ran 18',
                                   'Delete providers above 10 credits and order every waterfall cheapest '
                                   'first',
                                   'AJ Cassata ([6l8CThrSJEY @ 00:11:35]); GTM With Deepika ([1AB3H7aWJ0Q '
                                   '@ 00:07:26])'],
                                  ['Paid columns running across the whole table',
                                   'No run condition, or auto-update left on, fires every row and drains '
                                   'credits',
                                   'Add a run condition to every paid column and switch auto-update off',
                                   'Romain Osman Lead Generation ([RodU66qhDeY @ 00:10:37]); Xavier '
                                   'Caffrey GTM ([kY5E4wl8wlA @ 00:19:24])'],
                                  ['Per-lead research instead of per-company research',
                                   'Researching each lead separately costs two to three times as much '
                                   'credit',
                                   'Research once at company level, then look it up from the people table',
                                   'Xavier Caffrey GTM ([kY5E4wl8wlA @ 00:22:10])'],
                                  ['Weak auto-added Topic Intent topics',
                                   'Topics Clay auto-adds lead to the wrong people and use up a lot of '
                                   'credits',
                                   'Review added topics, keep high and medium intent only, rerun on a '
                                   'weekly schedule',
                                   'The AI Ops Guy ([nRh4F859Xjo @ 00:05:32])'],
                                  ['Robotic personalization tells in the copy',
                                   'A full street address in the email makes it obvious a robot is sending '
                                   'it',
                                   'Casualize the address with AI before pushing variables into Instantly',
                                   'Clay ([tbe8LBJOSSc @ 00:06:05])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Clear These Four Before Any Full-Table Run',
                           'body': 'Each gate comes from a loss or near-miss practitioners hit on their '
                                   'own Clay tables. Clear all four before pushing a full list into a '
                                   'sequencer.',
                           'items': ['Validate before sending: merge only Debounce safe-to-send, Prospeo '
                                     'valid and Enrich.so valid results into one master email column, and '
                                     'route risky, unknown and catch-all rows to a second verifier [Romain '
                                     'Osman Lead Generation — RodU66qhDeY @ 00:09:16].',
                                     'Test on a slice first: run ten rows before the full pull, or just '
                                     'two to three rows when testing a new waterfall [Matt Lucero — '
                                     'jEkDgA8hPmo @ 00:17:57] [GTM With Deepika — 1AB3H7aWJ0Q @ 00:10:15].',
                                     "Gate every fallback with a run condition such as 'only run if work "
                                     "email is empty' so paid columns never re-run on rows that already "
                                     'hit [AJ Cassata — 6l8CThrSJEY @ 00:16:35].',
                                     'Do not treat tech-stack presence as buying intent: using Salesforce '
                                     'does not mean a company needs help, so layer topic intent and '
                                     'Claygent opportunity ratings before finding contacts [The AI Ops Guy '
                                     '— nRh4F859Xjo @ 00:01:02].']}}],
 'pull_quote': "So it's very important to every time add a condition otherwise it's just going to run for "
               "all of your rows and so you're going to lose a lot of credits. — Romain Osman Lead "
               'Generation (RodU66qhDeY @ 00:10:37)',
 'diagram_id': 'diag-07',
 'action_checklist': ["Build a DNC table of clients and opt-outs, then run 'look up multiple rows in other "
                      "table' on company domain with the equals operator and skip any row where a record "
                      'is found [Romain Osman Lead Generation — RodU66qhDeY @ 00:02:04].',
                      'Order the email waterfall cheapest first, delete providers costing over 10 credits '
                      'per row, and cap the chain at about four steps [AJ Cassata — 6l8CThrSJEY @ '
                      '00:11:35].',
                      "Connect your own Findymail, ChatGPT or Claude API keys so Clay's markup stops "
                      'applying to your highest-volume steps [AJ Cassata — 12s-u4y1VF0 @ 00:15:36].',
                      'Force AI qualification columns to output yes or no only so the results can be '
                      'filtered and used as run conditions downstream [AJ Cassata — 12s-u4y1VF0 @ '
                      '00:17:24].',
                      'Run Claygent research once at the company level and pull it into the people table '
                      'by lookup instead of paying two to three times per lead [Xavier Caffrey GTM — '
                      'kY5E4wl8wlA @ 00:22:10].',
                      "Add 'run only if' logic and test on 10 rows before running the full table, then "
                      'push only qualified rows to the sequencer [Matt Lucero — jEkDgA8hPmo @ 00:17:57].'],
 'statutory_citations': [{'title': 'AJ Cassata — How to Get Unlimited Leads Using Clay Enrichment '
                                   'Waterfall | clay.com Tutorial [00:06:46]',
                          'url': 'https://www.youtube.com/watch?v=6l8CThrSJEY&t=406s',
                          'relevance': 'Primary practitioner testimony on waterfall sequencing, Apollo '
                                       'validity rates, provider cost cutoffs and paying for finds that '
                                       'fail validation.'},
                         {'title': 'Romain Osman Lead Generation — Clay.com Tutorial - Best Workflow For '
                                   'Your Outbound Campaign [00:09:16]',
                          'url': 'https://www.youtube.com/watch?v=RodU66qhDeY&t=556s',
                          'relevance': 'Primary practitioner testimony on DNC lookups, MX filtering, '
                                       'multi-verifier master email columns and run-condition discipline.'},
                         {'title': 'Xavier Caffrey GTM — The ONLY Clay Tutorial You Need in 2025 (For '
                                   'Beginners) [00:22:10]',
                          'url': 'https://www.youtube.com/watch?v=kY5E4wl8wlA&t=1330s',
                          'relevance': 'Primary practitioner testimony on Clay plan pricing, credit costs '
                                       'per action, auto-update leaks and company-level research '
                                       'economics.'},
                         {'title': 'The AI Ops Guy — How to Find High-Intent B2B Leads with Clay | Topic '
                                   'Intent + Claygent Tutorial [00:05:32]',
                          'url': 'https://www.youtube.com/watch?v=nRh4F859Xjo&t=332s',
                          'relevance': 'Primary practitioner testimony on Topic Intent configuration, weak '
                                       'auto-added topics and intent-gated contact finding.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '6l8CThrSJEY',
                       'title': 'How to Get Unlimited Leads Using Clay Enrichment Waterfall | clay.com '
                                'Tutorial',
                       'channel': 'AJ Cassata',
                       'author': 'AJ Cassata',
                       'text': 'A provider can find an email that then fails validation, and you are still '
                               'charged for it.',
                       'tip': 'A provider can find an email that then fails validation, and you are still '
                              'charged for it.',
                       'timestamp': 810,
                       'timestamp_seconds': 810,
                       'timestamp_label': '[00:13:30]',
                       'url': 'https://www.youtube.com/watch?v=6l8CThrSJEY&t=810s',
                       'markdown': '[00:13:30](https://www.youtube.com/watch?v=6l8CThrSJEY&t=810s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HqdvpIGiOz4',
                       'title': 'Clay.com Beginner Walkthrough 2026 - Step-by-Step Guide',
                       'channel': 'Matt Lucero',
                       'author': 'Matt Lucero',
                       'text': "Run it in small chunks so that mistakes don't burn through your credits.",
                       'tip': "Run it in small chunks so that mistakes don't burn through your credits.",
                       'timestamp': 1452,
                       'timestamp_seconds': 1452,
                       'timestamp_label': '[00:24:12]',
                       'url': 'https://www.youtube.com/watch?v=HqdvpIGiOz4&t=1452s',
                       'markdown': '[00:24:12](https://www.youtube.com/watch?v=HqdvpIGiOz4&t=1452s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tbe8LBJOSSc',
                       'title': 'The Easiest Way To Get B2B Clients In 2025 [Clay.com Tutorial]',
                       'channel': 'Clay',
                       'author': 'Clay',
                       'text': 'Casualize the address, because a full street address makes it obvious that '
                               'a robot is sending that email.',
                       'tip': 'Casualize the address, because a full street address makes it obvious that '
                              'a robot is sending that email.',
                       'timestamp': 365,
                       'timestamp_seconds': 365,
                       'timestamp_label': '[00:06:05]',
                       'url': 'https://www.youtube.com/watch?v=tbe8LBJOSSc&t=365s',
                       'markdown': '[00:06:05](https://www.youtube.com/watch?v=tbe8LBJOSSc&t=365s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '12s-u4y1VF0',
                       'title': 'The Top 3 Ways We Use Clay.com + AI To Get Leads & Clients [Tutorial]',
                       'channel': 'AJ Cassata',
                       'author': 'AJ Cassata',
                       'text': 'Now typically this will allow you to get up to 60 to 80% of your list to '
                               'have an email.',
                       'tip': 'Now typically this will allow you to get up to 60 to 80% of your list to '
                              'have an email.',
                       'timestamp': 278,
                       'timestamp_seconds': 278,
                       'timestamp_label': '[00:04:38]',
                       'url': 'https://www.youtube.com/watch?v=12s-u4y1VF0&t=278s',
                       'markdown': '[00:04:38](https://www.youtube.com/watch?v=12s-u4y1VF0&t=278s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'N-15SMLSc3c',
                       'title': 'What Does "Waterfall Enrichment" Even Mean?  (Clay.com For Non-Technical '
                                'Users)',
                       'channel': 'Mark Colgan | Outbound & Pipeline for B2B SaaS',
                       'author': 'Mark Colgan | Outbound & Pipeline for B2B SaaS',
                       'text': 'So looks at one provider, goes to the next provider, goes to the next '
                               'provider until all providers have been checked, which increases the '
                               'likelihood that you will find the data.',
                       'tip': 'So looks at one provider, goes to the next provider, goes to the next '
                              'provider until all providers have been checked, which increases the '
                              'likelihood that you will find the data.',
                       'timestamp': 88,
                       'timestamp_seconds': 88,
                       'timestamp_label': '[00:01:28]',
                       'url': 'https://www.youtube.com/watch?v=N-15SMLSc3c&t=88s',
                       'markdown': '[00:01:28](https://www.youtube.com/watch?v=N-15SMLSc3c&t=88s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kY5E4wl8wlA',
                       'title': 'The ONLY Clay Tutorial You Need in 2025 (For Beginners)',
                       'channel': 'Xavier Caffrey GTM',
                       'author': 'Xavier Caffrey GTM',
                       'text': "This way Clay won't run the entire table by accident and then you get to "
                               'save credits.',
                       'tip': "This way Clay won't run the entire table by accident and then you get to "
                              'save credits.',
                       'timestamp': 1164,
                       'timestamp_seconds': 1164,
                       'timestamp_label': '[00:19:24]',
                       'url': 'https://www.youtube.com/watch?v=kY5E4wl8wlA&t=1164s',
                       'markdown': '[00:19:24](https://www.youtube.com/watch?v=kY5E4wl8wlA&t=1164s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kY5E4wl8wlA',
                       'title': 'The ONLY Clay Tutorial You Need in 2025 (For Beginners)',
                       'channel': 'Xavier Caffrey GTM',
                       'author': 'Xavier Caffrey GTM',
                       'text': 'Run the research at the company level and look it up from the people '
                               'table, because running it per lead costs two to three times as much.',
                       'tip': 'Run the research at the company level and look it up from the people table, '
                              'because running it per lead costs two to three times as much.',
                       'timestamp': 1330,
                       'timestamp_seconds': 1330,
                       'timestamp_label': '[00:22:10]',
                       'url': 'https://www.youtube.com/watch?v=kY5E4wl8wlA&t=1330s',
                       'markdown': '[00:22:10](https://www.youtube.com/watch?v=kY5E4wl8wlA&t=1330s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Z9xzPDRrQHw',
                       'title': 'Did This AI Tool Just Change Sales Forever? (Clay AI Review)',
                       'channel': 'Sales Feed',
                       'author': 'Sales Feed',
                       'text': 'So from that search no companies were found; some reviews mentioned bad HR '
                               'and negative manager experience, but they lack the specific details '
                               'requested.',
                       'tip': 'So from that search no companies were found; some reviews mentioned bad HR '
                              'and negative manager experience, but they lack the specific details '
                              'requested.',
                       'timestamp': 237,
                       'timestamp_seconds': 237,
                       'timestamp_label': '[00:03:57]',
                       'url': 'https://www.youtube.com/watch?v=Z9xzPDRrQHw&t=237s',
                       'markdown': '[00:03:57](https://www.youtube.com/watch?v=Z9xzPDRrQHw&t=237s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nWnc3cZ1nFs',
                       'title': "I Tried Clay AI for 9 Months, Here’s What I Learned (Beginner's Guide)",
                       'channel': 'Sales Feed',
                       'author': 'Sales Feed',
                       'text': "And that will save you a ton of credits using Clay's preferred partners.",
                       'tip': "And that will save you a ton of credits using Clay's preferred partners.",
                       'timestamp': 441,
                       'timestamp_seconds': 441,
                       'timestamp_label': '[00:07:21]',
                       'url': 'https://www.youtube.com/watch?v=nWnc3cZ1nFs&t=441s',
                       'markdown': '[00:07:21](https://www.youtube.com/watch?v=nWnc3cZ1nFs&t=441s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nRh4F859Xjo',
                       'title': 'How to Find High-Intent B2B Leads with Clay | Topic Intent + Claygent '
                                'Tutorial',
                       'channel': 'The AI Ops Guy',
                       'author': 'The AI Ops Guy',
                       'text': "But just because a company uses Salesforce doesn't mean it needs our help "
                               'or that it is even considering hiring a consultancy.',
                       'tip': "But just because a company uses Salesforce doesn't mean it needs our help "
                              'or that it is even considering hiring a consultancy.',
                       'timestamp': 62,
                       'timestamp_seconds': 62,
                       'timestamp_label': '[00:01:02]',
                       'url': 'https://www.youtube.com/watch?v=nRh4F859Xjo&t=62s',
                       'markdown': '[00:01:02](https://www.youtube.com/watch?v=nRh4F859Xjo&t=62s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'v31hKg-WSCc',
                       'title': 'What is Clay?',
                       'channel': 'Clay',
                       'author': 'Clay',
                       'text': "Clay isn't a plug-and-play AI tool looking to 10x the volume of outreach "
                               'to your customer spam folders.',
                       'tip': "Clay isn't a plug-and-play AI tool looking to 10x the volume of outreach to "
                              'your customer spam folders.',
                       'timestamp': 238,
                       'timestamp_seconds': 238,
                       'timestamp_label': '[00:03:58]',
                       'url': 'https://www.youtube.com/watch?v=v31hKg-WSCc&t=238s',
                       'markdown': '[00:03:58](https://www.youtube.com/watch?v=v31hKg-WSCc&t=238s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jEkDgA8hPmo',
                       'title': 'FREE Clay.com Crash Course For 2026',
                       'channel': 'Matt Lucero',
                       'author': 'Matt Lucero',
                       'text': "If you're trying to do like 10,000 cold emails a day or 5,000 cold emails "
                               "a day or 1,000 cold emails a day, I'd recommend you probably just use your "
                               'own sequencer like Smartlead or Instantly.',
                       'tip': "If you're trying to do like 10,000 cold emails a day or 5,000 cold emails a "
                              "day or 1,000 cold emails a day, I'd recommend you probably just use your "
                              'own sequencer like Smartlead or Instantly.',
                       'timestamp': 1728,
                       'timestamp_seconds': 1728,
                       'timestamp_label': '[00:28:48]',
                       'url': 'https://www.youtube.com/watch?v=jEkDgA8hPmo&t=1728s',
                       'markdown': '[00:28:48](https://www.youtube.com/watch?v=jEkDgA8hPmo&t=1728s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UpSWlkeuUqs',
                       'title': 'The Fastest Way To Get B2B Clients In 2025 [Clay.com Tutorial]',
                       'channel': 'Xavier Caffrey GTM',
                       'author': 'Xavier Caffrey GTM',
                       'text': 'Now the phone number data is always a lot more expensive.',
                       'tip': 'Now the phone number data is always a lot more expensive.',
                       'timestamp': 445,
                       'timestamp_seconds': 445,
                       'timestamp_label': '[00:07:25]',
                       'url': 'https://www.youtube.com/watch?v=UpSWlkeuUqs&t=445s',
                       'markdown': '[00:07:25](https://www.youtube.com/watch?v=UpSWlkeuUqs&t=445s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YLXzWpknuJk',
                       'title': 'How to Use Clay.com (1 Hour Tutorial)',
                       'channel': 'Patrick Spychalski',
                       'author': 'Patrick Spychalski',
                       'text': 'The waterfall only charges the provider that hits, so here we are only '
                               'going to spend two credits.',
                       'tip': 'The waterfall only charges the provider that hits, so here we are only '
                              'going to spend two credits.',
                       'timestamp': 1303,
                       'timestamp_seconds': 1303,
                       'timestamp_label': '[00:21:43]',
                       'url': 'https://www.youtube.com/watch?v=YLXzWpknuJk&t=1303s',
                       'markdown': '[00:21:43](https://www.youtube.com/watch?v=YLXzWpknuJk&t=1303s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RodU66qhDeY',
                       'title': 'Clay.com Tutorial - Best Workflow For Your Outbound Campaign',
                       'channel': 'Romain Osman Lead Generation',
                       'author': 'Romain Osman Lead Generation',
                       'text': "We're not doing any waterfall enrichment right now because we found that "
                               "Prospeo has very good coverage and so we don't need to use other tools.",
                       'tip': "We're not doing any waterfall enrichment right now because we found that "
                              "Prospeo has very good coverage and so we don't need to use other tools.",
                       'timestamp': 392,
                       'timestamp_seconds': 392,
                       'timestamp_label': '[00:06:32]',
                       'url': 'https://www.youtube.com/watch?v=RodU66qhDeY&t=392s',
                       'markdown': '[00:06:32](https://www.youtube.com/watch?v=RodU66qhDeY&t=392s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RodU66qhDeY',
                       'title': 'Clay.com Tutorial - Best Workflow For Your Outbound Campaign',
                       'channel': 'Romain Osman Lead Generation',
                       'author': 'Romain Osman Lead Generation',
                       'text': "So it's very important to every time add a condition otherwise it's just "
                               "going to run for all of your rows and so you're going to lose a lot of "
                               'credits.',
                       'tip': "So it's very important to every time add a condition otherwise it's just "
                              "going to run for all of your rows and so you're going to lose a lot of "
                              'credits.',
                       'timestamp': 637,
                       'timestamp_seconds': 637,
                       'timestamp_label': '[00:10:37]',
                       'url': 'https://www.youtube.com/watch?v=RodU66qhDeY&t=637s',
                       'markdown': '[00:10:37](https://www.youtube.com/watch?v=RodU66qhDeY&t=637s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'AtF_XaOE3As',
                       'title': 'How to use Clay.com for outbound: Clay 101 Complete Guide',
                       'channel': 'AJ Cassata',
                       'author': 'AJ Cassata',
                       'text': "The more that you scale your cold email, the more that you're going to "
                               'land in spam.',
                       'tip': "The more that you scale your cold email, the more that you're going to land "
                              'in spam.',
                       'timestamp': 1367,
                       'timestamp_seconds': 1367,
                       'timestamp_label': '[00:22:47]',
                       'url': 'https://www.youtube.com/watch?v=AtF_XaOE3As&t=1367s',
                       'markdown': '[00:22:47](https://www.youtube.com/watch?v=AtF_XaOE3As&t=1367s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1AB3H7aWJ0Q',
                       'title': 'CLAY Company Waterfall Enrichment | Explained in simple way',
                       'channel': 'GTM With Deepika',
                       'author': 'GTM With Deepika',
                       'text': 'For testing just run two to three rows.',
                       'tip': 'For testing just run two to three rows.',
                       'timestamp': 615,
                       'timestamp_seconds': 615,
                       'timestamp_label': '[00:10:15]',
                       'url': 'https://www.youtube.com/watch?v=1AB3H7aWJ0Q&t=615s',
                       'markdown': '[00:10:15](https://www.youtube.com/watch?v=1AB3H7aWJ0Q&t=615s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'}]}
