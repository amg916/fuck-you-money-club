from __future__ import annotations

CHAPTER_11 = {'id': 'Q11',
 'chapter_id': 'Q11',
 'chapter_number': 11,
 'question_number': 11,
 'slug': 'n8n-client-delivery-scope-creep-control-white-label-ai-voice-agents',
 'question_prompt': 'How can I get started with n8n, self-host it for free, migrate workflows between '
                    'accounts, build AI lead intake automation, and deliver projects with clear client '
                    'handoffs—while managing scope creep, drafting paid change orders for human review and '
                    'sending, and white-labeling VAPI AI voice agents?',
 'kicker': 'Q11 / THE BIG MONEY PLAYBOOKS',
 'title': 'n8n Client Delivery, Scope-Creep Control & White-Label AI Voice Agents',
 'subtitle': 'Getting started with n8n, free self-hosting, cloud-to-self-hosted workflow migration, AI '
             'lead intake, professional client delivery and handoffs, scope management, AI-assisted change '
             'orders, and white-labeling VAPI voice agents.',
 'layout_template': 'chapter_opener',
 'reading_time_minutes': 15,
 'executive_summary': 'Austin Reed and Automate AI Consulting treat delivery as installed workflows, '
                      'production credentials, documentation, and defined support—not a loose JSON file. '
                      'Scott Bartnick carries scope through onboarding, named owners, and client-confirmed '
                      'strategy, while WPTuts welcomes changes through separate estimates. Nate Herk moves '
                      'workflows with two instance API keys and a Google Sheet tracking what remains to '
                      'process; credentials still need manual resetting. Quiet Client uses Notion, Claude, '
                      'and Wave to turn requests into reviewed, priced add-ons. Nomad Life Success '
                      'proposes 1.5x expansion pricing, while The Contractor AI collects change orders '
                      'upfront. Hosting preferences diverge: Reed favors self-hosting for 99% of clients, '
                      'whereas Automate AI Consulting usually chooses cloud for small businesses. Chat '
                      'Dash demonstrates branded VAPI dashboards and recurring Stripe billing.',
 'key_metrics': [{'label': 'Default workflow support window',
                  'metric': 'Default workflow support window',
                  'value': '30 days',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Automate AI Consulting offers 30 days of support on delivered work whether '
                             'or not the client has a retainer; ongoing maintenance is separate.',
                  'source': 'Automate AI Consulting ([91lw5ubtLMc @ 00:04:45])'},
                 {'label': 'Migration inventory and demonstration batch',
                  'metric': 'Migration inventory and demonstration batch',
                  'value': '512 workflows inventoried; demonstration limited to 25',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Nate Herk retrieves 512 workflow items from the cloud instance, then limits '
                             'the demonstration to 25 rather than migrating the entire inventory.',
                  'source': 'Nate Herk | AI Automation ([t1PTmpas0bg @ 00:02:39])'},
                 {'label': 'Expansion request pricing multiplier',
                  'metric': 'Expansion request pricing multiplier',
                  'value': '1.5x base rate',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Marcus Chen prices small additions extending an existing project at 1.5x the '
                             'base rate, citing interruption and context switching.',
                  'source': 'Nomad Life Success ([KdD-2pmdFZI @ 00:03:28])'},
                 {'label': 'White-label voice package pricing uplift',
                  'metric': 'White-label voice package pricing uplift',
                  'value': 'Up to 30% more',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Chat Dash says agencies should be able to charge up to 30% more for branded '
                             'voice AI packages because of higher perceived value.',
                  'source': 'Chat Dash ([1Ewf_Nq5mow @ 00:06:06])'}],
 'sections': [{'title': 'The Practitioner Consensus',
               'paragraphs': ['Austin Reed and Automate AI Consulting agree that the sale is followed by '
                              'hosting decisions, credential work, installation, documentation, and '
                              'support. Both describe clients owning their infrastructure, an '
                              'agency-managed arrangement funded through monthly maintenance, and a hybrid '
                              'where the client owns the instance while the agency maintains it. Reed '
                              'tells clients without infrastructure to open their own hosting account and '
                              'put their card on file; the builder can then deploy the server for a setup '
                              "fee. Delivery usually means logging into the client's n8n and installing "
                              'with production credentials, because API keys and responses can differ from '
                              'the test environment. Documentation identifies credential changes, service '
                              'information, webhooks, and API keys so someone else can troubleshoot after '
                              'the builder leaves. A technical client may instead accept JSON with '
                              'documentation in Notion. Reed describes a 30-day workflow guarantee; '
                              'Automate AI Consulting offers 30 days of support even without a retainer. '
                              'Ongoing maintenance costs more when it includes frequent new workflows and '
                              'improvements than when it means availability for breakages. Tom Crawshaw '
                              'supplies the business priority: solve expensive problems rather than build '
                              'impressive-looking workflows. Their highest-earning automation uses about '
                              'four or five nodes and, they report, generated over $600,000 for one '
                              'client. [mw1V2GoYHsk @ 00:01:45] [91lw5ubtLMc @ 00:02:38] [ofC4OeNjDx8 @ '
                              '00:04:28]',
                              'Scott Bartnick, WPTuts, and The Contractor AI make scope explicit before '
                              'delivery work expands. Bartnick routes a paid order into an onboarding form '
                              'containing business details and an electronic signature on the terms. '
                              'Standard packages define the work and payment terms while keeping team '
                              'expectations clear. Sales retains ownership until onboarding is complete; '
                              'the responsibility then moves to the person assigning accounts. The '
                              'onboarding call brings sales and operations together to restate scope, '
                              'timelines, and delivery expectations, followed by a strategy plan the '
                              'client confirms before work proceeds. WPTuts takes a similarly explicit but '
                              'deliberately flexible approach: the signed agreement welcomes changes where '
                              'possible, reserves the ability to decline them, and requires a separate '
                              'estimate for additional work. Technical limitations, pricing, and available '
                              'time can all prevent an addition. The Contractor AI starts with exclusions '
                              'before inclusions, attaches scope documentation, and uses a 15-minute scope '
                              'walk to explain the agreement. Customers repeat back their understanding '
                              'rather than merely receive small print. Their project managers handle '
                              'change orders because they hold the client relationship. Bartnick likewise '
                              'insists on an owner at every step instead of allowing a paid client to '
                              'disappear between sales and fulfillment. [d9zqCrUn7mY @ 00:01:41] '
                              '[UgtrG88EDhU @ 00:00:49] [J5BBjGKyoUE @ 00:12:40]',
                              'Kelsey Hastie and Quiet Client keep AI drafting separate from the human '
                              "decision to send. Hastie's starting project is one repetitive task: a "
                              'website audit request becomes an internal draft, not an automatic customer '
                              'reply. Required fields, explicit mapping, validation, and a duplicate check '
                              'precede the model. The model returns a summary, questions, and a draft '
                              'reply, asking about missing deadlines and scope rather than inventing '
                              'prices or delivery dates. A reviewer compares the Gmail draft with the '
                              'original request. Quiet Client applies the same division of work to scope '
                              'changes: Notion holds the original agreement and change log, Claude drafts '
                              'the message from real notes, and the freelancer edits and sends it. A '
                              "database label does not substitute for the client's actual response. Chat "
                              "Dash addresses the client's experience after voice-agent delivery: branded "
                              'analytics, conversation logs, transcripts, recordings, and associated '
                              'knowledge-base files are exposed through a client dashboard instead of '
                              'leaving the client in a developer-facing interface. The presenter describes '
                              'manually calculated usage and spreadsheet reporting as time-consuming, then '
                              'demonstrates a separate client account with an assigned assistant. Agency '
                              'branding and client access sit alongside the agent itself, while recurring '
                              'Stripe products handle billing through the agency interface. [cqaukVEOmJ4 @ '
                              '00:04:18] [csELc0aBrp4 @ 00:03:04] [1Ewf_Nq5mow @ 00:03:27]'],
               'table': {'caption': 'Delivery responsibilities the practitioners make explicit',
                         'headers': ['Delivery Area',
                                     'Practitioner Operating Method',
                                     'Client-Facing Result',
                                     'Expert Source'],
                         'rows': [['Infrastructure ownership is decided before the workflow is handed '
                                   'over.',
                                   'Let the client own hosting, manage it yourself, or maintain their '
                                   'instance.',
                                   'The hosting account and maintenance relationship follow the selected '
                                   'arrangement.',
                                   'Austin Reed ([mw1V2GoYHsk @ 00:01:26])'],
                                  ['Production installation includes enough documentation for someone else '
                                   'to troubleshoot.',
                                   'Install with production credentials and document credential locations '
                                   'and webhooks.',
                                   'The client receives installed work rather than an unexplained workflow '
                                   'export.',
                                   'Automate AI Consulting ([91lw5ubtLMc @ 00:02:38])'],
                                  ['Paid orders remain assigned to sales until onboarding is completed.',
                                   'Combine order details and signed terms inside the onboarding form.',
                                   'The delivery team receives business information and a restated project '
                                   'scope.',
                                   'Scott Bartnick ([d9zqCrUn7mY @ 00:01:53])'],
                                  ['Additional requests are welcomed without automatically absorbing their '
                                   'extra work.',
                                   'Specify changes where possible and issue separate estimates for '
                                   'additions.',
                                   'Clients can change direction while understanding that additional work '
                                   'costs more.',
                                   'WPTuts ([UgtrG88EDhU @ 00:01:05])'],
                                  ['AI prepares a structured response without choosing what customers '
                                   'receive.',
                                   'Generate a Gmail draft and compare it against the original request.',
                                   'A person checks scope, claims, recipient, and missing details before '
                                   'sending.',
                                   'Kelsey Hastie ([cqaukVEOmJ4 @ 00:05:20])'],
                                  ['Voice clients receive an assigned assistant inside a separate '
                                   'dashboard.',
                                   'Expose analytics, call logs, transcripts, audio, and associated '
                                   'knowledge-base files.',
                                   'Clients inspect agent activity through the dashboard created for their '
                                   'account.',
                                   'Chat Dash ([1Ewf_Nq5mow @ 00:03:58])']]}},
              {'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["Nate Herk's migration uses two manually executed workflows and a Google "
                              'Sheet. Create an API credential for the old instance and another for the '
                              "destination, using each instance's base URL followed by /api/v1 without a "
                              'duplicated slash. The first workflow retrieves the old workflows and writes '
                              "their IDs, names, and a 'to process' status into the sheet. Herk retrieves "
                              '512 items but limits the demonstration to 25. The second workflow reads '
                              "only rows marked 'to process', fetches each workflow by ID from the old "
                              'instance, and loops through destination creation one at a time. Its '
                              'workflow object contains name, nodes, connections, and settings; after '
                              "creation, the sheet status becomes 'processed'. Credentials, users, and "
                              'executions do not move with that object. For a hosted destination, Metics '
                              "Media demonstrates Hostinger's n8n template on KVM 1, describing a normal "
                              'starting price around $5 monthly. Setup includes server location, a root '
                              'password, account verification, and the n8n account. Self-hosted updates '
                              "remain the operator's responsibility through Docker Manager. Reed completes "
                              'delivery by connecting client services on a call and using Dashlane or One '
                              'Time Secret for credential exchanges rather than email or SMS. Their '
                              'HTTP-node pattern centralizes a service key in an initial edit node. '
                              '[t1PTmpas0bg @ 00:03:44] [oRI0lA-ZQ3w @ 00:04:16] [mw1V2GoYHsk @ 00:04:38]',
                              "Quiet Client's scope loop starts before anyone builds the requested extra. "
                              'Freeze the original statement of work in Notion with deliverables, '
                              'exclusions, and the date of agreement. Add a change-log row containing the '
                              'request, original-scope link, status, price, impact, decision, and '
                              'correspondence link; leave unquoted amounts blank and the decision pending. '
                              "Give Claude the real scope bullets, the client's words, current capacity, "
                              'and two or three options. Ask for a short email and revised scope bullets '
                              'without invented approvals or signatures. The freelancer edits and sends. '
                              'Once the client chooses a priced option, create a separate Wave estimate or '
                              'invoice for that add-on and link it back to Notion. Quiet Client '
                              'demonstrates a fictional $950 press kit page due on approval. Marcus Chen '
                              'at Nomad Life Success instead teaches ChatGPT classification into in scope, '
                              'expansion, or new project, returning classification, suggested_price, and '
                              'rationale as JSON. Their pricing is no charge, 1.5x base rate, or 2x–3x '
                              "base rate respectively. The Contractor AI uses the immediate script, 'Great "
                              "catch. That's a change order. I'll write it up right now.' Their voice-note "
                              'scoping tool feeds prefilled pricing calculators, and their change orders '
                              'are collected 100% upfront. [csELc0aBrp4 @ 00:01:18] [KdD-2pmdFZI @ '
                              '00:02:06] [J5BBjGKyoUE @ 00:20:55]',
                              "Chat Dash's white-label setup begins with an agency account and profile. "
                              'Add an agency logo, name, domain or default subdomain, and color theme; '
                              'select VAPI, name the agent, and bring in the private API key and assistant '
                              'ID from VAPI. Create the client subaccount with login details and language, '
                              'then assign the imported assistant. The presenter logs in as the client and '
                              'checks analytics and the conversations tab, which contains one conversation '
                              'in the demonstration. Clients can read transcripts, listen to recordings, '
                              'download audio, and inspect associated knowledge-base files. The agency '
                              'view lists clients and associated agents. Its Stripe billing area assigns a '
                              'recurring subscription product to a project. Chat Dash claims branded '
                              'packages can command up to 30% more and automated billing can save up to 15 '
                              'hours monthly. For a separate bounded n8n intake build, Hastie starts with '
                              'request ID, email, and request fields, normalizes them, checks that '
                              'required strings are nonempty, and inserts a pending row before calling the '
                              'model. A structured output parser defines summary and draft reply as '
                              'strings and questions as an array. Gmail creates a draft addressed to a '
                              'fixed reviewer; after success, the workflow records its ID and updates '
                              'status. [1Ewf_Nq5mow @ 00:02:22] [cqaukVEOmJ4 @ 00:01:04]'],
               'table': {'caption': 'Execution details, tools, and attributed commercial numbers',
                         'headers': ['Operation',
                                     'Exact Mechanic',
                                     'Number or Completion Detail',
                                     'Expert Source'],
                         'rows': [['Move existing workflows between an old and a destination instance.',
                                   'Read pending sheet rows, fetch workflow JSON, create workflows, then '
                                   'update status.',
                                   'Herk inventories 512 workflows and limits the demonstration batch to '
                                   '25.',
                                   'Nate Herk | AI Automation ([t1PTmpas0bg @ 00:02:39])'],
                                  ['Deploy the demonstrated self-hosted n8n setup on a hosted server.',
                                   'Choose Hostinger KVM 1 with the n8n template already selected.',
                                   'The presenter describes the normal starting price as $5 per month.',
                                   'Metics Media ([oRI0lA-ZQ3w @ 00:04:16])'],
                                  ['Move a priced scope addition into a separate billing document.',
                                   'Create the Wave estimate and link its URL into the Notion row.',
                                   'The fictional press kit page example is $950 due on approval.',
                                   'Quiet Client ([csELc0aBrp4 @ 00:05:27])'],
                                  ['Classify new client requests before choosing the proposed price '
                                   'treatment.',
                                   'Return JSON classification, suggested_price, and rationale using the '
                                   'base hourly rate.',
                                   'Expansion uses 1.5x; new projects use 2x to 3x base rate.',
                                   'Nomad Life Success ([KdD-2pmdFZI @ 00:03:09])'],
                                  ['Turn a field request into a written and priced change order.',
                                   'Dictate the scope and feed it into prefilled pricing calculators.',
                                   'The speaker describes five or six such orders that week in JobTread.',
                                   'The Contractor AI | AI Systems for Contractors ([J5BBjGKyoUE @ '
                                   '00:24:32])'],
                                  ['Present voice-agent activity through an agency-branded client '
                                   'dashboard and account.',
                                   'Import the VAPI assistant and assign it to the client subaccount.',
                                   'Assign recurring Stripe subscription products to projects through '
                                   'agency billing.',
                                   'Chat Dash ([1Ewf_Nq5mow @ 00:03:27]; [1Ewf_Nq5mow @ 00:05:19])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Small implementation details the practitioners emphasize',
                           'body': 'Herk tracks migration status externally; Reed simplifies repeated key '
                                   'changes; Quiet Client leaves missing facts visible; Chen reviews '
                                   'classifications weekly.',
                           'items': ["Filter the migration sheet to 'to process' and mark each created "
                                     "workflow 'processed' rather than repeatedly importing the same "
                                     'inventory. [Nate Herk | AI Automation — t1PTmpas0bg @ 00:03:55]',
                                     'For multiple HTTP nodes calling the same service, Reed places an '
                                     'edit node at the beginning so changing one API key updates their '
                                     'shared source. [Austin Reed — mw1V2GoYHsk @ 00:05:01]',
                                     'Ask Claude to leave brackets when a fact or price is missing and '
                                     'finish with a clear choice: option A, option B, or pause the add-on. '
                                     '[Quiet Client — csELc0aBrp4 @ 00:03:42]',
                                     'Store scope prompts in Notion or a text file, log every request in a '
                                     'spreadsheet, and spend 15 minutes each Friday reviewing '
                                     'classifications. [Nomad Life Success — KdD-2pmdFZI @ 00:05:09]']},
               'sop_steps': [{'step': 1,
                              'title': 'Complete the owned onboarding handoff',
                              'action': 'Collect the onboarding form and signed terms before moving the '
                                        'account from sales to the person assigning delivery '
                                        'responsibility.',
                              'detail': 'Bartnick gives sales 48 hours to obtain onboarding forms and '
                                        'gives the assignment owner 24 hours after onboarding arrives. '
                                        'Keep an owner and due date on the project-management task as '
                                        'responsibility changes. [Scott Bartnick — d9zqCrUn7mY @ 00:06:37] '
                                        '[Scott Bartnick — d9zqCrUn7mY @ 00:07:46]'},
                             {'step': 2,
                              'title': 'Migrate tracked workflows and reconnect services',
                              'action': 'Configure old and destination instance credentials, populate the '
                                        'migration sheet, and create destination workflows from pending '
                                        'rows.',
                              'detail': 'Use the workflow name, nodes, connections, and settings in the '
                                        'creation object; update each sheet row after creation. Reset '
                                        'credentials manually because credentials, users, and executions '
                                        'do not migrate with the workflow. [Nate Herk | AI Automation — '
                                        't1PTmpas0bg @ 00:05:39] [Nate Herk | AI Automation — t1PTmpas0bg '
                                        '@ 00:08:56]'},
                             {'step': 3,
                              'title': 'Log, draft, price, and send the scope addition',
                              'action': 'Record the new request against the original scope, draft the '
                                        'client message in Claude, and send the edited options.',
                              'detail': 'After the client selects a priced option, create a separate Wave '
                                        'estimate or invoice for the add-on. Link it back to Notion and '
                                        'mark the decision approved after the reply rather than treating a '
                                        'draft as agreement. [Quiet Client — csELc0aBrp4 @ 00:03:04] '
                                        '[Quiet Client — csELc0aBrp4 @ 00:04:48]'},
                             {'step': 4,
                              'title': 'Deploy the branded voice-agent client view',
                              'action': 'Set agency branding, import the VAPI assistant, create the client '
                                        'subaccount, and open the resulting dashboard as that client.',
                              'detail': 'Check analytics, conversation transcripts, recordings, and '
                                        'associated knowledge-base files. In the agency billing area, '
                                        'assign a recurring Stripe subscription product to the project. '
                                        '[Chat Dash — 1Ewf_Nq5mow @ 00:03:58] [Chat Dash — 1Ewf_Nq5mow @ '
                                        '00:05:19]'}]},
              {'title': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Austin Reed and Automate AI Consulting agree on self-hosting for serious '
                              'volume, but their everyday client defaults diverge. Reed recommends '
                              'self-hosting for 99% of their clients, pointing to infrastructure control, '
                              'larger servers, and custom nodes; cloud remains an option for clients who '
                              'prioritize security handling over price. Automate AI Consulting instead '
                              'uses cloud for most small-business clients because they prefer simplicity '
                              'and straightforwardness. Neither practitioner makes infrastructure '
                              'ownership synonymous with maintenance responsibility. Reed describes '
                              'client-owned hosting, agency-owned hosting with a monthly maintenance fee, '
                              'and a hybrid where the client owns the infrastructure while the agency '
                              'keeps it updated. Automate AI Consulting likewise has clients establish '
                              'their own accounts and payment arrangements, while offering managed '
                              'arrangements for retainer relationships. Metics Media adds a separate '
                              'distinction inside self-hosting: running locally avoids a hosting bill, but '
                              'closing the laptop stops the automations, while a home server introduces '
                              'hardware and networking work. Their preferred VPS route starts around $5 '
                              'monthly in their presentation. Kelsey Hastie separates the free community '
                              'edition from hosting, model usage, backups, and maintenance. These are '
                              'different delivery arrangements with different stated responsibilities, not '
                              'one shared recommendation that every client should run the same setup '
                              '[mw1V2GoYHsk @ 00:01:08] [91lw5ubtLMc @ 00:01:28] [oRI0lA-ZQ3w @ 00:01:18] '
                              '[cqaukVEOmJ4 @ 00:00:44].',
                              'Change-order pricing produces a sharper contrast. The Contractor AI teaches '
                              'charging for disruption: change work carries a stated 50% to 60% margin, '
                              'and their company collects 100% when the change comes up. The explanation '
                              'is operational: crews stop, schedules shift, and production is interrupted. '
                              'Nomad Life Success uses multipliers instead: included work stays free, '
                              'expansions cost 1.5 times the base rate, and new projects cost two to three '
                              'times that rate. Their mobile-app example also offers a 10% discount for a '
                              'response within 48 hours. Yet Nomad explicitly allows relationship-building '
                              'freebies and warns that charging for every tiny tweak can drive clients '
                              'away. WPTuts takes a flexible contractual approach rather than prescribing '
                              'a multiplier: welcome changes where possible, retain the ability to '
                              'decline, and issue a separate estimate for additional work. Quiet Client '
                              'offers another menu for the actual conversation: absorb the addition with a '
                              'deadline slip, charge a fixed add-on fee, or decline with a referral. '
                              'Claude drafts the language from real notes, capacity, and operator-supplied '
                              'options. The distinction is concrete: Contractor AI prioritizes immediate '
                              'paid disruption, Nomad supplies premium rate tiers with discretion, and '
                              'WPTuts and Quiet Client organize the decision around a separate estimate or '
                              'explicit choice [J5BBjGKyoUE @ 00:17:48] [KdD-2pmdFZI @ 00:03:28] '
                              '[UgtrG88EDhU @ 00:01:33] [csELc0aBrp4 @ 00:03:04].',
                              'The handoff interface also changes with the job. Scott Bartnick rejects '
                              'spreadsheets as the home for agency projects and instead assigns owners and '
                              'due dates inside a project management tool. Sales owns the account until '
                              'onboarding is complete; account assignment and the strategy plan then move '
                              'through named responsibilities. Nate Herk deliberately uses a Google sheet '
                              'for a narrower operation: migrating workflows. Their sheet holds workflow '
                              'IDs, names, and processing status so the migration can select unfinished '
                              'rows and mark completed transfers. Those positions address different work, '
                              "rather than proving that either practitioner rejects the other's entire "
                              'system. Chat Dash takes a third route for voice-agent delivery: a branded '
                              'client dashboard, connected through a VAPI private API key and assistant '
                              'ID, displays analytics, conversations, transcripts, recordings, and '
                              'associated knowledge-base files. Their agency interface can associate a '
                              "recurring Stripe subscription product with a project. Kelsey Hastie's "
                              'intake design stops much earlier: its output is a reviewed internal draft, '
                              'not a quote, contract, or automatic customer reply. The client-facing voice '
                              'portal, internal draft workflow, migration ledger, and agency project board '
                              'therefore remain distinct playbooks, each matching the specific delivery '
                              'surface its practitioner actually demonstrates rather than serving as '
                              'interchangeable handoff packages [d9zqCrUn7mY @ 00:04:34] [t1PTmpas0bg @ '
                              '00:03:55] [1Ewf_Nq5mow @ 00:05:19] [cqaukVEOmJ4 @ 00:01:04].'],
               'table': {'caption': 'Alternative delivery and scope-control playbooks, with their stated '
                                    'operating differences.',
                         'headers': ['Decision and competing approaches',
                                     'Practitioner mechanics and stated boundaries',
                                     'Expert Source'],
                         'rows': [["Choose between Reed's self-hosting default and Automate AI "
                                   "Consulting's small-business cloud default.",
                                   'Reed recommends self-hosting for 99% of clients; Automate AI '
                                   'Consulting says most of their small-business clients prefer cloud '
                                   'simplicity.',
                                   'Austin Reed ([mw1V2GoYHsk @ 00:01:08]); Automate AI Consulting '
                                   '([91lw5ubtLMc @ 00:01:28])'],
                                  ['Separate the free software edition from the machine and ongoing '
                                   'operational costs.',
                                   'Metics Media distinguishes local computers, home servers, and VPS '
                                   'hosting; Hastie separately counts hosting, models, backups, and '
                                   'maintenance.',
                                   'Metics Media ([oRI0lA-ZQ3w @ 00:01:18]); Kelsey Hastie ([cqaukVEOmJ4 @ '
                                   '00:00:44])'],
                                  ['Compare disruption margins and immediate collection with premium '
                                   'hourly-rate multipliers.',
                                   'Contractor AI describes 50% to 60% margins and full payment '
                                   'immediately; Nomad prices expansions at 1.5 times and new projects at '
                                   'two to three times.',
                                   'The Contractor AI | AI Systems for Contractors ([J5BBjGKyoUE @ '
                                   '00:17:48]); Nomad Life Success ([KdD-2pmdFZI @ 00:03:28])'],
                                  ['Allow changes through separate estimates or offer an explicit menu of '
                                   'alternatives.',
                                   'WPTuts welcomes feasible changes with separate estimates; Quiet Client '
                                   'offers deadline movement, a fixed add-on fee, or declining with a '
                                   'referral.',
                                   'WPTuts ([UgtrG88EDhU @ 00:01:33]); Quiet Client ([csELc0aBrp4 @ '
                                   '00:03:04])'],
                                  ["Distinguish a workflow migration ledger from the agency's ongoing "
                                   'project management system.',
                                   'Herk tracks migration status in Google Sheets; Bartnick assigns '
                                   'project owners and due dates rather than running agency projects in '
                                   'spreadsheets.',
                                   'Nate Herk | AI Automation ([t1PTmpas0bg @ 00:03:55]); Scott Bartnick '
                                   '([d9zqCrUn7mY @ 00:04:34])'],
                                  ['Deliver a branded voice-agent portal or prepare a reviewed internal '
                                   'intake draft.',
                                   'Chat Dash exposes calls, transcripts, and recordings to clients; '
                                   "Hastie's website-audit intake prepares an internal draft without "
                                   'automatically replying.',
                                   'Chat Dash ([1Ewf_Nq5mow @ 00:03:58]); Kelsey Hastie ([cqaukVEOmJ4 @ '
                                   '00:01:04])']]}},
              {'title': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["The Contractor AI's hardest contract lesson was not an abstract warning "
                              'about extra work. They report paying $130,000 to remove a cell tower on a '
                              '$120,000 job, then still having to complete the project because their '
                              'agreement lacked the relevant exclusion. Their contract clauses now reflect '
                              'problems they personally experienced. They also describe being a recovering '
                              'yes-person, practicing difficult conversations in the mirror, and running '
                              'millions in revenue without having much to show for nearly a decade. WPTuts '
                              'reports a different contract bottleneck: a roughly twelve-page document '
                              'became two pages after adopting a plain-English approach, and they say '
                              'conversion improved. The contrast is between accumulated exclusions and '
                              'accessible language, not a claim that either page count alone protects a '
                              'job. Scott Bartnick identifies another firsthand mismatch: sales says one '
                              'thing while operations understands something else. Their onboarding call '
                              'brings those functions together, and the strategy plan restates the work '
                              "before execution. Quiet Client's change log addresses a related operational "
                              'trap: a board marked approved when nobody replied is worse than a sticky '
                              'note. Their demonstration leaves the decision pending and price unfilled '
                              'until quoted, rather than allowing an attractive tracking system to '
                              'manufacture agreement [J5BBjGKyoUE @ 00:11:51] [UgtrG88EDhU @ 00:02:43] '
                              '[d9zqCrUn7mY @ 00:09:50] [csELc0aBrp4 @ 00:02:41].',
                              'A transferred workflow is not a transferred operating environment. Nate '
                              'Herk demonstrates copying workflow names, nodes, connections, settings, and '
                              'even visual notes, but explicitly says credentials, users, and executions '
                              'do not move through that migration. Those require manual resetting in their '
                              'account of the process. Austin Reed explains why installation with '
                              'production credentials matters: some APIs behave differently after '
                              'switching from testing to production, so a workflow that ran successfully '
                              'during development can still break at delivery. Their documentation '
                              'includes credential locations, services, webhooks, and API-key locations so '
                              'the client can troubleshoot later. Kelsey Hastie exposes a separate trap in '
                              'the intake blueprint: checking whether a request ID already exists stops a '
                              'sequential duplicate, but simultaneous requests can race. Recording pending '
                              'before the model call also creates a recovery obligation if the model then '
                              'fails. Their instruction is to investigate the pending row and retry '
                              'deliberately, not silently lose the request. Tom Crawshaw grounds the '
                              'broader debugging burden in their own history of broken workflows, '
                              'frustrated clients, and months of trial and error. Their learning advice '
                              'favors solving an actual business problem and understanding the necessary '
                              'nodes over collecting templates whose behavior the builder cannot explain '
                              '[t1PTmpas0bg @ 00:08:56] [mw1V2GoYHsk @ 00:04:05] [cqaukVEOmJ4 @ 00:03:14] '
                              '[ofC4OeNjDx8 @ 00:05:51].',
                              "Keep each practitioner's money claim attached to the thing being counted. "
                              "Kelsey Hastie's worked example assumes forty requests saving three minutes "
                              'each: two hours valued at $30 per hour produces $60 of time value. '
                              'Subtracting $15 for hosting and model costs plus $20 for maintenance and '
                              'review leaves an estimated $25 benefit. Hastie explicitly presents those '
                              'amounts as assumptions, and says saved time becomes cash only when it '
                              'avoids a cost or gets used productively. Chat Dash makes a different claim '
                              'about voice-agent packaging: a branded dashboard should support up to 30% '
                              'higher pricing, while automated billing can save up to fifteen hours '
                              'monthly. Their demonstration shows the client interface and subscription '
                              "configuration; the premium and time figures remain Chat Dash's stated "
                              'claims. Tom Crawshaw reports that their highest-earning automation has only '
                              'four or five nodes and generated over $600,000 for one client, opposing '
                              "complexity for its own sake. Quiet Client's $950 press-kit-page add-on is a "
                              'fictional demonstration, with the estimate remaining a draft until sent. '
                              'Their operating check is whether change-order emails actually leave drafts. '
                              'These examples count different things: assumed net benefit, asserted '
                              'pricing uplift, reported client revenue, and a demonstration estimate '
                              'awaiting a real sending action [cqaukVEOmJ4 @ 00:06:27] [1Ewf_Nq5mow @ '
                              '00:06:06] [ofC4OeNjDx8 @ 00:04:28] [csELc0aBrp4 @ 00:05:27].'],
               'table': {'caption': 'Reported losses, demonstrated limitations, and the checks '
                                    'practitioners attach to their economics.',
                         'headers': ['Failure mode or economics trap',
                                     'Reported experience and practitioner response',
                                     'Expert Source'],
                         'rows': [['An omitted exclusion produced an expense larger than the original job '
                                   'value.',
                                   'Contractor AI reports a $130,000 tower-removal expense on a $120,000 '
                                   'job, followed by completing the original project.',
                                   'The Contractor AI | AI Systems for Contractors ([J5BBjGKyoUE @ '
                                   '00:11:51])'],
                                  ['Workflow migration copies the build without transferring every '
                                   'operational dependency.',
                                   'Herk says credentials, users, and executions do not move; Reed warns '
                                   'that switching API environments can break previously working flows.',
                                   'Nate Herk | AI Automation ([t1PTmpas0bg @ 00:08:56]); Austin Reed '
                                   '([mw1V2GoYHsk @ 00:04:05])'],
                                  ['Sequential duplicate protection leaves simultaneous requests and '
                                   'pending failures to investigate.',
                                   'Hastie says concurrent requests can race and instructs operators to '
                                   'investigate pending rows when the model fails before deliberately '
                                   'retrying.',
                                   'Kelsey Hastie ([cqaukVEOmJ4 @ 00:03:14])'],
                                  ['Sales promises and operations expectations can diverge before the '
                                   'client receives work.',
                                   'Bartnick brings sales and operations together on onboarding, then uses '
                                   "the strategy plan to restate scope and obtain the client's agreement.",
                                   'Scott Bartnick ([d9zqCrUn7mY @ 00:09:50])'],
                                  ['Time-value calculations can shrink after hosting, models, review, and '
                                   'maintenance costs.',
                                   "Hastie's assumed $60 time value becomes $25 after stated costs; they "
                                   'say review can consume the time expected to be saved.',
                                   'Kelsey Hastie ([cqaukVEOmJ4 @ 00:06:27]); Kelsey Hastie ([cqaukVEOmJ4 '
                                   '@ 00:06:48])'],
                                  ['Presentation claims and large client-revenue examples measure '
                                   'different business outcomes.',
                                   'Chat Dash claims up to 30% higher pricing; Crawshaw reports over '
                                   '$600,000 in client revenue from four or five nodes.',
                                   'Chat Dash ([1Ewf_Nq5mow @ 00:06:06]); The AI Architects | Tom Crawshaw '
                                   '([ofC4OeNjDx8 @ 00:04:28])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Check the missing handoff, the stalled request, and the unpaid extra',
                           'body': "Use the practitioners' stated checks before calling the delivery "
                                   'complete.',
                           'items': ['After workflow migration, manually reset credentials and account for '
                                     'users and executions that Herk says do not transfer through this '
                                     'method. [Nate Herk | AI Automation — t1PTmpas0bg @ 00:08:56]',
                                     'Investigate pending intake rows after model failure, test '
                                     'simultaneous requests, and inspect failed executions before retrying '
                                     'because a timeout may already have created a draft. [Kelsey Hastie — '
                                     'cqaukVEOmJ4 @ 00:03:14] [Kelsey Hastie — cqaukVEOmJ4 @ 00:05:43]',
                                     'Do not leave all change orders for the final invoice; Contractor AI '
                                     'describes the relationship damage when the final number is 30% '
                                     'higher than the client expected. [The Contractor AI | AI Systems for '
                                     'Contractors — J5BBjGKyoUE @ 00:26:06]',
                                     'Assign an owner at every onboarding stage and track due dates; '
                                     'Bartnick warns that stalled onboarding can leave advance payments '
                                     'followed by disputes or refunds instead of completed work. [Scott '
                                     'Bartnick — d9zqCrUn7mY @ 00:06:07] [Scott Bartnick — d9zqCrUn7mY @ '
                                     '00:08:30]']}}],
 'pull_quote': '"Great catch. That\'s a change order. I\'ll write it up right now." — The Contractor AI | '
               'AI Systems for Contractors (J5BBjGKyoUE @ 00:20:55).',
 'diagram_id': 'diag-06',
 'action_checklist': ["Install the workflow in the client's n8n with production credentials, and document "
                      'credential changes, webhook locations, and the connected services. [Austin Reed — '
                      'mw1V2GoYHsk @ 00:02:35] [Austin Reed — mw1V2GoYHsk @ 00:03:14]',
                      'Track migration rows by workflow ID and status; select only rows marked to process, '
                      'then mark each completed transfer processed. [Nate Herk | AI Automation — '
                      't1PTmpas0bg @ 00:03:55]',
                      'Freeze the original scope in Notion, log each new request before starting work, and '
                      'have Claude draft options from actual notes rather than invented prices or '
                      'agreement. [Quiet Client — csELc0aBrp4 @ 00:01:18] [Quiet Client — csELc0aBrp4 @ '
                      '00:03:04]',
                      "Test Nomad's classification prompt against the last five client requests, using in "
                      'scope, expansion, and new project as the three categories. [Nomad Life Success — '
                      'KdD-2pmdFZI @ 00:02:27] [Nomad Life Success — KdD-2pmdFZI @ 00:06:51]',
                      'Keep sales responsible until onboarding is complete, pursue the form within 48 '
                      'hours, and assign the account team within the following 24-hour responsibility '
                      'window. [Scott Bartnick — d9zqCrUn7mY @ 00:06:37] [Scott Bartnick — d9zqCrUn7mY @ '
                      '00:06:54] [Scott Bartnick — d9zqCrUn7mY @ 00:07:46]',
                      'Connect the VAPI assistant in Chat Dash using its private API key and assistant ID, '
                      'create the client subaccount, then log in as that client to inspect analytics and '
                      'conversations. [Chat Dash — 1Ewf_Nq5mow @ 00:03:10] [Chat Dash — 1Ewf_Nq5mow @ '
                      '00:03:27] [Chat Dash — 1Ewf_Nq5mow @ 00:03:58]'],
 'statutory_citations': [{'title': 'Nate Herk | AI Automation — Easiest Way to Migrate n8n Workflows '
                                   'Between Accounts (cloud to self-hosted) [00:08:56]',
                          'url': 'https://www.youtube.com/watch?v=t1PTmpas0bg&t=536s',
                          'relevance': 'Primary practitioner testimony on credentials, users, and '
                                       'executions excluded from the demonstrated workflow migration.'},
                         {'title': 'The Contractor AI | AI Systems for Contractors — The $12.4K Scope '
                                   'Creep Killing Your Best Jobs (Fix Inside) [00:11:51]',
                          'url': 'https://www.youtube.com/watch?v=J5BBjGKyoUE&t=711s',
                          'relevance': 'Primary practitioner testimony on a reported $130,000 '
                                       'tower-removal expense arising during a $120,000 project.'},
                         {'title': 'Scott Bartnick — The Client Handoff System That Stops Scope Creep and '
                                   'Dropped Balls [00:09:50]',
                          'url': 'https://www.youtube.com/watch?v=d9zqCrUn7mY&t=590s',
                          'relevance': 'Primary practitioner testimony on mismatched sales and operations '
                                       'expectations and the strategy-plan handoff.'},
                         {'title': 'Chat Dash — How to Whitelabel VAPI AI Voice Agents (in 7 Minutes) '
                                   '[00:03:10]',
                          'url': 'https://www.youtube.com/watch?v=1Ewf_Nq5mow&t=190s',
                          'relevance': 'Primary practitioner testimony demonstrating the VAPI private-key '
                                       'and assistant-ID connection for a client dashboard.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 't1PTmpas0bg',
                       'title': 'Easiest Way to Migrate n8n Workflows Between Accounts (cloud to '
                                'self-hosted)',
                       'channel': 'Nate Herk | AI Automation',
                       'author': 'Nate Herk | AI Automation',
                       'text': "We're only going to pull in workflows if the status equals to process.",
                       'tip': "We're only going to pull in workflows if the status equals to process.",
                       'timestamp': 235,
                       'timestamp_seconds': 235,
                       'timestamp_label': '[00:03:55]',
                       'url': 'https://www.youtube.com/watch?v=t1PTmpas0bg&t=235s',
                       'markdown': '[00:03:55](https://www.youtube.com/watch?v=t1PTmpas0bg&t=235s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 't1PTmpas0bg',
                       'title': 'Easiest Way to Migrate n8n Workflows Between Accounts (cloud to '
                                'self-hosted)',
                       'channel': 'Nate Herk | AI Automation',
                       'author': 'Nate Herk | AI Automation',
                       'text': "The only thing that won't move over is, you know, credentials and users "
                               'and executions and things like that.',
                       'tip': "The only thing that won't move over is, you know, credentials and users and "
                              'executions and things like that.',
                       'timestamp': 536,
                       'timestamp_seconds': 536,
                       'timestamp_label': '[00:08:56]',
                       'url': 'https://www.youtube.com/watch?v=t1PTmpas0bg&t=536s',
                       'markdown': '[00:08:56](https://www.youtube.com/watch?v=t1PTmpas0bg&t=536s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mw1V2GoYHsk',
                       'title': 'How to Deliver Your n8n Project to Clients Like a PRO!',
                       'channel': 'Austin Reed',
                       'author': 'Austin Reed',
                       'text': 'All in all, I recommend the self-hosted option for 99% of our clients.',
                       'tip': 'All in all, I recommend the self-hosted option for 99% of our clients.',
                       'timestamp': 68,
                       'timestamp_seconds': 68,
                       'timestamp_label': '[00:01:08]',
                       'url': 'https://www.youtube.com/watch?v=mw1V2GoYHsk&t=68s',
                       'markdown': '[00:01:08](https://www.youtube.com/watch?v=mw1V2GoYHsk&t=68s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mw1V2GoYHsk',
                       'title': 'How to Deliver Your n8n Project to Clients Like a PRO!',
                       'channel': 'Austin Reed',
                       'author': 'Austin Reed',
                       'text': 'Some APIs are badly built and you switch from the test environment to the '
                               'production environment. Some problems might occur.',
                       'tip': 'Some APIs are badly built and you switch from the test environment to the '
                              'production environment. Some problems might occur.',
                       'timestamp': 245,
                       'timestamp_seconds': 245,
                       'timestamp_label': '[00:04:05]',
                       'url': 'https://www.youtube.com/watch?v=mw1V2GoYHsk&t=245s',
                       'markdown': '[00:04:05](https://www.youtube.com/watch?v=mw1V2GoYHsk&t=245s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ofC4OeNjDx8',
                       'title': 'Seriously, please watch this before you start learning n8n',
                       'channel': 'The AI Architects | Tom Crawshaw',
                       'author': 'The AI Architects | Tom Crawshaw',
                       'text': 'Personally, my highest earning automation is about four or five different '
                               "nodes. And it's generated one of my clients over $600,000 in revenue.",
                       'tip': 'Personally, my highest earning automation is about four or five different '
                              "nodes. And it's generated one of my clients over $600,000 in revenue.",
                       'timestamp': 268,
                       'timestamp_seconds': 268,
                       'timestamp_label': '[00:04:28]',
                       'url': 'https://www.youtube.com/watch?v=ofC4OeNjDx8&t=268s',
                       'markdown': '[00:04:28](https://www.youtube.com/watch?v=ofC4OeNjDx8&t=268s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '91lw5ubtLMc',
                       'title': 'How To Deliver Your N8N Automation To Clients Like An Expert',
                       'channel': 'Automate AI Consulting',
                       'author': 'Automate AI Consulting',
                       'text': 'For the majority of my clients who are small businesses, I use cloud. They '
                               'prefer the simplicity and straightforwardness of it.',
                       'tip': 'For the majority of my clients who are small businesses, I use cloud. They '
                              'prefer the simplicity and straightforwardness of it.',
                       'timestamp': 88,
                       'timestamp_seconds': 88,
                       'timestamp_label': '[00:01:28]',
                       'url': 'https://www.youtube.com/watch?v=91lw5ubtLMc&t=88s',
                       'markdown': '[00:01:28](https://www.youtube.com/watch?v=91lw5ubtLMc&t=88s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oRI0lA-ZQ3w',
                       'title': 'How to Use n8n for FREE in 2026 - n8n Self Hosting Setup',
                       'channel': 'Metics Media',
                       'author': 'Metics Media',
                       'text': "First, your local machine, your laptop, your desktop, whatever you're "
                               'using right now. This is the only truly free option, but it only runs when '
                               'your computer is on.',
                       'tip': "First, your local machine, your laptop, your desktop, whatever you're using "
                              'right now. This is the only truly free option, but it only runs when your '
                              'computer is on.',
                       'timestamp': 78,
                       'timestamp_seconds': 78,
                       'timestamp_label': '[00:01:18]',
                       'url': 'https://www.youtube.com/watch?v=oRI0lA-ZQ3w&t=78s',
                       'markdown': '[00:01:18](https://www.youtube.com/watch?v=oRI0lA-ZQ3w&t=78s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oRI0lA-ZQ3w',
                       'title': 'How to Use n8n for FREE in 2026 - n8n Self Hosting Setup',
                       'channel': 'Metics Media',
                       'author': 'Metics Media',
                       'text': 'When you self host you get to choose exactly when to update the software. '
                               "This also means that you're the one responsible for updating the software "
                               "periodically to make sure it's compatible with all the nodes you're using.",
                       'tip': 'When you self host you get to choose exactly when to update the software. '
                              "This also means that you're the one responsible for updating the software "
                              "periodically to make sure it's compatible with all the nodes you're using.",
                       'timestamp': 564,
                       'timestamp_seconds': 564,
                       'timestamp_label': '[00:09:24]',
                       'url': 'https://www.youtube.com/watch?v=oRI0lA-ZQ3w&t=564s',
                       'markdown': '[00:09:24](https://www.youtube.com/watch?v=oRI0lA-ZQ3w&t=564s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cqaukVEOmJ4',
                       'title': 'n8n Beginner Tutorial: AI Lead Intake Automation (Free Self-Hosted '
                                'Option)',
                       'channel': 'Kelsey Hastie',
                       'author': 'Kelsey Hastie',
                       'text': 'Two simultaneous requests can race. Production systems need stronger, '
                               'tested coordination.',
                       'tip': 'Two simultaneous requests can race. Production systems need stronger, '
                              'tested coordination.',
                       'timestamp': 194,
                       'timestamp_seconds': 194,
                       'timestamp_label': '[00:03:14]',
                       'url': 'https://www.youtube.com/watch?v=cqaukVEOmJ4&t=194s',
                       'markdown': '[00:03:14](https://www.youtube.com/watch?v=cqaukVEOmJ4&t=194s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cqaukVEOmJ4',
                       'title': 'n8n Beginner Tutorial: AI Lead Intake Automation (Free Self-Hosted '
                                'Option)',
                       'channel': 'Kelsey Hastie',
                       'author': 'Kelsey Hastie',
                       'text': 'Suppose 40 requests save 3 minutes each. That is 2 hours. At a '
                               'hypothetical $30 per hour, the time value is $60.',
                       'tip': 'Suppose 40 requests save 3 minutes each. That is 2 hours. At a hypothetical '
                              '$30 per hour, the time value is $60.',
                       'timestamp': 387,
                       'timestamp_seconds': 387,
                       'timestamp_label': '[00:06:27]',
                       'url': 'https://www.youtube.com/watch?v=cqaukVEOmJ4&t=387s',
                       'markdown': '[00:06:27](https://www.youtube.com/watch?v=cqaukVEOmJ4&t=387s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'J5BBjGKyoUE',
                       'title': 'The $12.4K Scope Creep Killing Your Best Jobs (Fix Inside)',
                       'channel': 'The Contractor AI | AI Systems for Contractors',
                       'author': 'The Contractor AI | AI Systems for Contractors',
                       'text': 'We ended up paying $130,000 to have a cell phone tower taken down on a '
                               '$120,000 job.',
                       'tip': 'We ended up paying $130,000 to have a cell phone tower taken down on a '
                              '$120,000 job.',
                       'timestamp': 711,
                       'timestamp_seconds': 711,
                       'timestamp_label': '[00:11:51]',
                       'url': 'https://www.youtube.com/watch?v=J5BBjGKyoUE&t=711s',
                       'markdown': '[00:11:51](https://www.youtube.com/watch?v=J5BBjGKyoUE&t=711s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'J5BBjGKyoUE',
                       'title': 'The $12.4K Scope Creep Killing Your Best Jobs (Fix Inside)',
                       'channel': 'The Contractor AI | AI Systems for Contractors',
                       'author': 'The Contractor AI | AI Systems for Contractors',
                       'text': "When they want to go ahead with that change work order, remember, we're "
                               'going to have a 50% to 60% margin on that.',
                       'tip': "When they want to go ahead with that change work order, remember, we're "
                              'going to have a 50% to 60% margin on that.',
                       'timestamp': 1068,
                       'timestamp_seconds': 1068,
                       'timestamp_label': '[00:17:48]',
                       'url': 'https://www.youtube.com/watch?v=J5BBjGKyoUE&t=1068s',
                       'markdown': '[00:17:48](https://www.youtube.com/watch?v=J5BBjGKyoUE&t=1068s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'csELc0aBrp4',
                       'title': 'Stop eating scope creep for free — AI stack that drafts change orders '
                                '(you still send) (2026)',
                       'channel': 'Quiet Client',
                       'author': 'Quiet Client',
                       'text': 'Feed Claude only real notes, client name, original scope bullets, the new '
                               'request in their words, your capacity this week, and two or three price '
                               'options.',
                       'tip': 'Feed Claude only real notes, client name, original scope bullets, the new '
                              'request in their words, your capacity this week, and two or three price '
                              'options.',
                       'timestamp': 184,
                       'timestamp_seconds': 184,
                       'timestamp_label': '[00:03:04]',
                       'url': 'https://www.youtube.com/watch?v=csELc0aBrp4&t=184s',
                       'markdown': '[00:03:04](https://www.youtube.com/watch?v=csELc0aBrp4&t=184s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KdD-2pmdFZI',
                       'title': "The AI Scope-Creep Shield: How to Turn 'One More Request' into a Premium "
                                'Change-Order That Pays Y...',
                       'channel': 'Nomad Life Success',
                       'author': 'Nomad Life Success',
                       'text': 'Tier two, expansion, price at 1.5 x your base rate. Why 1.5 x? Because '
                               "it's a small addition, but it interrupts your flow and requires context "
                               'switching.',
                       'tip': "Tier two, expansion, price at 1.5 x your base rate. Why 1.5 x? Because it's "
                              'a small addition, but it interrupts your flow and requires context '
                              'switching.',
                       'timestamp': 208,
                       'timestamp_seconds': 208,
                       'timestamp_label': '[00:03:28]',
                       'url': 'https://www.youtube.com/watch?v=KdD-2pmdFZI&t=208s',
                       'markdown': '[00:03:28](https://www.youtube.com/watch?v=KdD-2pmdFZI&t=208s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UgtrG88EDhU',
                       'title': 'How to Handle Scope Creep in Client Projects',
                       'channel': 'WPTuts',
                       'author': 'WPTuts',
                       'text': "I know my contract went from like 12 pages down to two pages. And it's "
                               'already a lot more accessible.',
                       'tip': "I know my contract went from like 12 pages down to two pages. And it's "
                              'already a lot more accessible.',
                       'timestamp': 163,
                       'timestamp_seconds': 163,
                       'timestamp_label': '[00:02:43]',
                       'url': 'https://www.youtube.com/watch?v=UgtrG88EDhU&t=163s',
                       'markdown': '[00:02:43](https://www.youtube.com/watch?v=UgtrG88EDhU&t=163s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'd9zqCrUn7mY',
                       'title': 'The Client Handoff System That Stops Scope Creep and Dropped Balls',
                       'channel': 'Scott Bartnick',
                       'author': 'Scott Bartnick',
                       'text': "I've seen in the past where sales says one thing and operations thinks "
                               "it's something else.",
                       'tip': "I've seen in the past where sales says one thing and operations thinks it's "
                              'something else.',
                       'timestamp': 590,
                       'timestamp_seconds': 590,
                       'timestamp_label': '[00:09:50]',
                       'url': 'https://www.youtube.com/watch?v=d9zqCrUn7mY&t=590s',
                       'markdown': '[00:09:50](https://www.youtube.com/watch?v=d9zqCrUn7mY&t=590s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1Ewf_Nq5mow',
                       'title': 'How to Whitelabel VAPI AI Voice Agents (in 7 Minutes)',
                       'channel': 'Chat Dash',
                       'author': 'Chat Dash',
                       'text': 'And I want to copy private key here. Copy ID back to chat dash. Paste it. '
                               "And now let's copy assistant ID that I want to bring in.",
                       'tip': 'And I want to copy private key here. Copy ID back to chat dash. Paste it. '
                              "And now let's copy assistant ID that I want to bring in.",
                       'timestamp': 190,
                       'timestamp_seconds': 190,
                       'timestamp_label': '[00:03:10]',
                       'url': 'https://www.youtube.com/watch?v=1Ewf_Nq5mow&t=190s',
                       'markdown': '[00:03:10](https://www.youtube.com/watch?v=1Ewf_Nq5mow&t=190s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1Ewf_Nq5mow',
                       'title': 'How to Whitelabel VAPI AI Voice Agents (in 7 Minutes)',
                       'channel': 'Chat Dash',
                       'author': 'Chat Dash',
                       'text': 'You should be able to charge up to 30% more for your voice AI packages.',
                       'tip': 'You should be able to charge up to 30% more for your voice AI packages.',
                       'timestamp': 366,
                       'timestamp_seconds': 366,
                       'timestamp_label': '[00:06:06]',
                       'url': 'https://www.youtube.com/watch?v=1Ewf_Nq5mow&t=366s',
                       'markdown': '[00:06:06](https://www.youtube.com/watch?v=1Ewf_Nq5mow&t=366s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'}]}
