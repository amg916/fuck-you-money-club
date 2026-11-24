from __future__ import annotations

CHAPTER_4 = {'id': 'Q4',
 'chapter_id': 'Q4',
 'chapter_number': 4,
 'question_number': 4,
 'slug': 'aws-marketplace-seller-setup-private-offers',
 'question_prompt': 'How does a software seller list on AWS Marketplace and create, renew, and manage '
                    'private offers?',
 'kicker': 'Q4 / THE BIG MONEY PLAYBOOKS',
 'title': 'Selling Through AWS Marketplace: Seller Setup and Private Offers',
 'subtitle': 'Seller registration and first listings, private marketplace curation, SaaS contract private '
             'offers, future-dated and agreement-based offers, renewals and upgrades, buyer subscription '
             'flow, re:Invent custom-pricing updates, and Ops Squad best practices',
 'layout_template': 'comparison_matrix',
 'reading_time_minutes': 15,
 'executive_summary': 'AWS Marketplace practitioners agree the private offer is the enterprise closing '
                      "tool: a custom contract pinned to a buyer's AWS account ID, with AWS invoicing, "
                      'collecting, and disbursing the money. Setup is free and requires an eligible '
                      'jurisdiction for paid listings, a paid listing, management portal access, and '
                      'ideally a dedicated seller of record account. Mechanics: a five-step offer wizard, '
                      'up to 23 buyers per SaaS contract offer, durations up to five years, installment '
                      'schedules, and a worked example where an $80 discounted price nets the ISV $72 '
                      'after a 10 percent listing fee. Renewals run through agreement-based offers that '
                      'replace the live subscription. Speakers diverge on pace and packaging: AWS staff '
                      'push standard contracts, CRM API integration, and future dated agreements, while '
                      'PartnerCloud argues against bucketing everything under one company-name listing.',
 'key_metrics': [{'label': 'ISV Net Revenue After Listing Fee',
                  'metric': 'ISV Net Revenue After Listing Fee',
                  'value': '$72 net on an $80 private offer price (10 percent listing fee)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Worked example: $100 list price, 20 percent private offer discount to $80, '
                             'AWS charges the customer $80 and disburses to the ISV minus a 10 percent '
                             'listing fee.',
                  'source': 'Amazon Web Services ([qWl-wamuA-Q @ 00:10:25])'},
                 {'label': 'Reported Vendor Deal Outcomes',
                  'metric': 'Reported Vendor Deal Outcomes',
                  'value': '80% bigger deals, 81% ROI, 27% higher win rates, 40% higher deal sizes',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Stats cited at re:Invent 2024 for software vendors selling through AWS '
                             'Marketplace.',
                  'source': 'AWS Events ([K-GonrtXvKA @ 00:02:05])'},
                 {'label': 'Maximum Buyers Per SaaS Contract Private Offer',
                  'metric': 'Maximum Buyers Per SaaS Contract Private Offer',
                  'value': 'Up to 23 buyer AWS account IDs',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Buyer targeting step of the SaaS contract private offer creation demo in the '
                             'Management Portal.',
                  'source': 'Amazon Web Services ([2qDBJ9lxIdQ @ 00:03:53])'},
                 {'label': 'Agreement-Based Offer Generation Time',
                  'metric': 'Agreement-Based Offer Generation Time',
                  'value': 'Up to 45 minutes',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Time to allow after creating an upgrade or renewal agreement-based offer '
                             'before the new offer ID and URL appear in the Offers tab.',
                  'source': 'Amazon Web Services ([KzcE0ZWyjzk @ 00:02:52])'}],
 'sections': [{'title': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every speaker who touches the mechanic lands on the same definition: a '
                              'private offer is a custom contract created from a listing and pinned to a '
                              'specific buyer AWS account. Prunal, CEO and co-founder of Clazar, frames it '
                              'as customized contracts carrying special pricing or terms for specific '
                              'customers, all inside the AWS Marketplace ecosystem, with AWS still '
                              'handling billing and payments so no separate invoicing is required '
                              '[h7liwzzA_-I @ 00:00:20]. The AWS ISV operations walkthrough states it the '
                              'same way: the customer receives pricing that is not publicly available, '
                              'negotiates terms with the seller, and the partner creates the offer for the '
                              'AWS account the customer designates, with each offer carrying its own '
                              'pricing, licensing terms, and a set expiration date [qWl-wamuA-Q @ '
                              '00:01:04]. David, presenting at re:Invent 2024, boils it down further: '
                              'partners can write custom quotes to their customers through private offers, '
                              'covering volume discounts, custom contractual terms, and specific payment '
                              'schedules [K-GonrtXvKA @ 00:02:50]. Tyler from the AWS Marketplace team '
                              'positions the same feature as the white glove lane, distinct from '
                              'self-service click-to-subscribe, where sellers control contract terms and '
                              'payment schedules as they see fit [HU_SJTFHcGU @ 00:02:20]. The shared '
                              'takeaway for an operator is simple: negotiate the deal directly with the '
                              'buyer, then let the offer and AWS billing carry the paperwork and '
                              'collections.',
                              'The baseline prerequisites are short and repeated across sources. The ISV '
                              'operations walkthrough lists three: the partner must have a paid listing in '
                              'AWS Marketplace, must have access to the AWS Marketplace Management Portal, '
                              "and the buyer must be an AWS customer [qWl-wamuA-Q @ 00:05:26]. Tyler's "
                              'registration walkthrough states there is no charge or fee to register as a '
                              'seller and recommends a fresh AWS account as the seller of record, because '
                              'every Marketplace interaction ties to that account; sellers told AWS that '
                              'separating production accounts from the seller of record account simplifies '
                              'management, separates disbursements, and adds a security layer [w6XECzZOfXY '
                              "@ 00:01:44]. David's re:Invent sequence matches the onboarding order: sign "
                              'in with an AWS account, agree to the terms and conditions, set up the '
                              'seller profile and banking info, create the first product listing, '
                              'integrate with the Billing API for contract or usage consumption, then '
                              'start selling [K-GonrtXvKA @ 00:04:52]. On the profile side, the '
                              'PartnerCloud host walked the horizontal tabs live: a public profile needing '
                              'only a 300 by 150 logo file, display name, URL, and a 600 character max '
                              'description, then tax information, bank account, KYC with extra '
                              'requirements in EMEA and South Korea, service link roles for resale '
                              'authorizations, and notifications [qXei9F9hLNU @ 00:02:35].',
                              'The commercial case is consistent across the speakers: buyers want to '
                              'consolidate third-party spend onto the AWS bill, and sellers ride that '
                              'procurement path. Tyler reports the most common customer feedback is love '
                              'for consolidating third-party software expenses into the AWS bill, plus '
                              'pay-as-you-go consumption and flexible payment terms, and on the seller '
                              'side some sellers shared they accelerated sales cycles upwards of 50 '
                              'percent because the heavy lifting of working with procurement teams and '
                              'approving software purchases gets eliminated [HU_SJTFHcGU @ 00:05:22]. '
                              'David layers on vendor outcomes of 80 percent bigger deals, 81 percent '
                              'return on investment, 27 percent higher win rates, and 40 percent higher '
                              'deal sizes, and notes customers often buy through Marketplace to meet AWS '
                              'commitments [K-GonrtXvKA @ 00:02:05]. Prunal pitches private offers as one '
                              'of the best ways to accelerate enterprise transactions, specifically for '
                              'enterprise customers needing tailored pricing and contract terms, '
                              'multi-year or volume deals, and channel motions through CPPO [h7liwzzA_-I @ '
                              '00:01:15]. The PartnerCloud host adds a field-level angle: a professional '
                              "services purchase through Marketplace burns down the buyer's Marketplace "
                              'commit, which becomes a selling point written straight into the listing '
                              'copy [qXei9F9hLNU @ 00:14:47].'],
               'table': {'caption': 'Where AWS Marketplace practitioners agree: private offer fundamentals '
                                    'and seller prerequisites',
                         'headers': ['Consensus Point',
                                     'What Practitioners Say',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Private offers are custom contracts tied to one buyer account',
                                   'Seller defines buyer account ID, custom pricing, duration, and terms; '
                                   'AWS generates a secure offer URL',
                                   'Collect the buyer AWS account ID before building any offer in the '
                                   'portal',
                                   'Clazar ([h7liwzzA_-I @ 00:00:38])'],
                                  ['Three hard prerequisites must exist before any private offer',
                                   'Paid listing in AWS Marketplace, Management Portal access, and the '
                                   'buyer must be an AWS customer',
                                   'Without a paid listing live, no private offer can be extended to '
                                   'anyone',
                                   'Amazon Web Services ([qWl-wamuA-Q @ 00:05:26])'],
                                  ['Eligible jurisdictions gate who can sell paid software licenses',
                                   'Paid sellers must be a resident, citizen, or entity incorporated in an '
                                   'eligible jurisdiction',
                                   'Free-only publishers skip the jurisdiction check and the payment '
                                   'information requirement entirely',
                                   'Amazon Web Services ([w6XECzZOfXY @ 00:00:17])'],
                                  ['Use a dedicated seller of record AWS account from day one',
                                   'New account recommended because all Marketplace interactions are tied '
                                   'to that account moving forward',
                                   'Separates disbursements from production accounts and adds a '
                                   'permissions security layer across teams',
                                   'Amazon Web Services ([w6XECzZOfXY @ 00:01:44])'],
                                  ['AWS owns invoicing, collections, and distribution of buyer funds',
                                   'AWS collects funds from the customer and distributes to the ISV, '
                                   'sending reports on accepted offers',
                                   'Seller skips separate invoicing; cash arrives through the normal AWS '
                                   'disbursement cycle',
                                   'Amazon Web Services ([qWl-wamuA-Q @ 00:07:34])'],
                                  ['Marketplace puts the listing in front of a large buyer pool',
                                   'About 5,000 partners, over 20,000 products, about 300,000 active '
                                   'customers, over 2.5 million subscriptions',
                                   'Listing places offers in front of buyers already procuring through '
                                   'their AWS accounts',
                                   'AWS Events ([K-GonrtXvKA @ 00:01:00])'],
                                  ['SaaS provisioning stays entirely with the seller after subscription',
                                   'AWS does not provision SaaS products; buyers register on the seller '
                                   'website after subscribing',
                                   'Seller needs a working registration page live before the first deal '
                                   'closes',
                                   'Amazon Web Services ([PVL4069oqC0 @ 00:02:32])']]}},
              {'title': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The build path is identical across demos. Log into the AWS Marketplace '
                              'Management Portal, open the Offers tab, and hit the orange Create Private '
                              'Offer button; David describes a five-step wizard covering pricing details, '
                              "duration, terms, legal documents, and the customer's AWS ID [K-GonrtXvKA @ "
                              '00:05:38]. The SaaS contract demo runs the same order in practice: select '
                              'product type, pick the product, wait up to 30 seconds for the offer ID to '
                              'generate, set offer name, description, renewal flag and expiration date, '
                              'then configure pricing and duration, add the buyer account ID, and attach '
                              'legal terms such as the Standard Contract for AWS Marketplace [2qDBJ9lxIdQ '
                              '@ 00:01:42]. That same demo caps targeting at up to 23 buyers on a single '
                              'private offer and treats an Active status as the signal the offer is '
                              'published and available for the buyer to accept [2qDBJ9lxIdQ @ 00:03:53]. '
                              'The earlier generic demo shows the payload: dimensions are the features, '
                              'services, and usage amounts of the software; the seller can let customers '
                              'pick quantity, designate price, select zero dollar pricing, and add service '
                              'agreement details, then copy the offer URL and email it straight to the '
                              'buyer [PVL4069oqC0 @ 00:01:11].',
                              'Pricing structure is where the deal gets shaped. David splits private offer '
                              'pricing into four basic structures: contract pricing with an upfront fee '
                              'for a set term, usage pay-as-you-go, installment payment schedules where '
                              'AWS invoices on dates the two sides agree, and hybrids where a contract '
                              'converts into overage once the customer hits the max; installment dates '
                              'themselves often become a negotiation lever [K-GonrtXvKA @ 00:03:34]. The '
                              'ISV walkthrough lists standard SaaS contract durations of one month, one '
                              'year, two years, or three years, with custom contracts for any number of '
                              'months up to five years [qWl-wamuA-Q @ 00:02:17]. Its worked unit '
                              'economics: a $100 list product discounted 20 percent becomes an $80 private '
                              'offer price, AWS charges the customer $80, and after a 10 percent listing '
                              'fee the ISV nets $72, with VAT or other taxes added on top of the customer '
                              'price at invoicing [qWl-wamuA-Q @ 00:10:25]. In the installment demo, the '
                              'seller starts the contract on acceptance with a 12 month duration, picks '
                              'dimensions, applies a bulk unit price to usage dimensions, enters total '
                              'contract price and number of installments, sets the first invoice date, '
                              'generates the plan, and can manually edit each invoice amount or date '
                              '[2qDBJ9lxIdQ @ 00:02:43].',
                              'After signature, the money and renewal mechanics take over. Customers '
                              'receive AWS invoices on the third of the month, Marketplace purchases ride '
                              'on the monthly AWS invoice under AWS net payment terms, and buyer funds can '
                              'take one to two days to post to the sub ledger before they count toward a '
                              'disbursement [qWl-wamuA-Q @ 00:11:43]. For upgrades and renewals on SaaS '
                              'contracts, Chloe Weaver walks the agreement-based offer: open the '
                              'Agreements tab, search the active subscription by buyer AWS account ID, '
                              'click create agreement-based offer, set end date, dimensions, quantity, '
                              'usage pricing, payment schedule, and EULA, mark it as a renewal, then allow '
                              'up to 45 minutes for the new offer ID and URL to appear [KzcE0ZWyjzk @ '
                              '00:01:58]. The companion demo adds that the seller can co-term on the '
                              'existing end date, keep the current EULA or swap to standard, enterprise, '
                              'or custom terms, bill upfront by scheduling the invoice for today, and set '
                              'expiration at least two weeks out because AWS systems run on UTC '
                              '[MlboB3rLbvE @ 00:02:38]. Future dated offers let the seller pick New Offer '
                              'starting at a future date with service start and end dates; once accepted '
                              'it becomes a future dated agreement [xLqQjXa2edo @ 00:01:16].'],
               'table': {'caption': 'Exact settings, limits, and unit economics for building and renewing '
                                    'AWS Marketplace private offers',
                         'headers': ['Mechanic',
                                     'Exact Setting or Number',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Offer ID generation after starting a SaaS offer',
                                   'Up to 30 seconds after selecting the product type and the product '
                                   'offer',
                                   'Wait for the ID, then save and exit as a draft whenever details are '
                                   'missing',
                                   'Amazon Web Services ([2qDBJ9lxIdQ @ 00:01:42])'],
                                  ['Buyer accounts targeted on a single SaaS contract offer',
                                   'Up to 23 buyer AWS account IDs on one private offer',
                                   'Cover multiple buyer accounts in one build instead of duplicating '
                                   'offers',
                                   'Amazon Web Services ([2qDBJ9lxIdQ @ 00:03:53])'],
                                  ['Listing fee math on a discounted private offer',
                                   '$100 list, 20 percent discount, $80 customer price, 10 percent fee, '
                                   '$72 ISV net',
                                   'Model net revenue to the ISV before agreeing the discount with the '
                                   'buyer',
                                   'Amazon Web Services ([qWl-wamuA-Q @ 00:10:25])'],
                                  ['SaaS contract term lengths available in private offers',
                                   'Standard one month, one, two, or three years; custom up to five years',
                                   'Match the contract term to the buyer budget cycle and multi-year '
                                   'commitment',
                                   'Amazon Web Services ([qWl-wamuA-Q @ 00:02:17])'],
                                  ['Agreement-based renewal offer generation time in the portal',
                                   'Allow up to 45 minutes before the new offer ID and URL appear',
                                   'Build renewal offers well ahead of the buyer decision deadline, never '
                                   'last minute',
                                   'Amazon Web Services ([KzcE0ZWyjzk @ 00:02:52])'],
                                  ['Offer expiration buffer for agreement-based offers',
                                   'Best practice sets expiration at least two weeks out; AWS systems run '
                                   'on UTC',
                                   'Gives buyer procurement time to accept before the offer silently '
                                   'disappears',
                                   'Amazon Web Services ([MlboB3rLbvE @ 00:02:38])'],
                                  ['Local currency contract pricing for international private offers',
                                   'Euros, pounds, Japanese yen, and Australian dollar launched for '
                                   'contract pricing',
                                   'Quote international buyers without worrying about currency exchange '
                                   'rates',
                                   'AWS Events ([K-GonrtXvKA @ 00:13:00])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Speed and Renewal Levers Practitioners Actually Use',
                           'body': 'Once the first offer is live, the speakers point to four levers that '
                                   'cut build time, lift renewals, and make listings findable.',
                           'items': ['Use clone to new to replicate configurations from past offers and '
                                     'adjust them for renewals or revisions, then export any extended '
                                     'offer to PDF with one click for stakeholders and offline '
                                     'collaboration [AWS Events — K-GonrtXvKA @ 00:09:10]',
                                     'At higher volume, integrate with the Marketplace API so private '
                                     'offers go out from the CRM instead of logging into the portal every '
                                     'single time; products and agreements can be read there too [AWS '
                                     'Events — K-GonrtXvKA @ 00:14:28]',
                                     'Push future dated agreements for renewals: an Ops Squad speaker '
                                     'reports partners implementing them at scale saw their renewal rate '
                                     'go up and ended the end-of-year scramble for unclosed deals [Amazon '
                                     'Web Services — gNv2wvhYkzA @ 00:03:43]',
                                     'Avoid bucketing every deal under one company-name listing; break '
                                     'offerings into separate SKUs by product or industry so buyers and '
                                     'AWS field sellers can actually find them [PartnerCloud — qXei9F9hLNU '
                                     '@ 00:20:18]']},
               'sop_steps': [{'step': 1,
                              'title': 'Register the seller of record account',
                              'action': 'Sign into a dedicated AWS account, open the Sell in AWS '
                                        'Marketplace tab, and click Register now.',
                              'detail': 'On the registration page review the legal business name, accept '
                                        'and download the seller terms and conditions, and answer the '
                                        'questions on product types, pricing models, category, and '
                                        'industry segment before signing into the Management Portal '
                                        '[Amazon Web Services — w6XECzZOfXY @ 00:02:44]'},
                             {'step': 2,
                              'title': 'Build the seller profile and first listing',
                              'action': 'Complete the profile tabs, then create the first product with '
                                        'descriptions, highlights, support, categories, and keywords.',
                              'detail': 'Upload a 300 by 150 logo with a 600 character max description, '
                                        'add tax, bank, and KYC details, then build the product with an S3 '
                                        'URL thumbnail, short and long descriptions, three highlights, '
                                        'support details, up to three categories, and keywords '
                                        '[PartnerCloud — qXei9F9hLNU @ 00:07:43]'},
                             {'step': 3,
                              'title': 'Create and send the private offer',
                              'action': 'From the Offers tab, run the Create Private Offer wizard and '
                                        'share the URL once the offer is Active.',
                              'detail': 'Fill pricing details, duration, terms, legal documents, and the '
                                        'buyer AWS ID in the five-step wizard [AWS Events — K-GonrtXvKA @ '
                                        '00:05:38], attach the Standard Contract for AWS Marketplace, '
                                        'review, create, and monitor until status reads Active [Amazon Web '
                                        'Services — 2qDBJ9lxIdQ @ 00:04:15]'},
                             {'step': 4,
                              'title': 'Collect, then renew through agreement-based offers',
                              'action': 'Track invoicing and disbursement, then build renewals off the '
                                        'active agreement in the Agreements tab.',
                              'detail': 'Customers are invoiced on the third of the month and funds take '
                                        'one to two days to post before disbursement [Amazon Web Services '
                                        '— qWl-wamuA-Q @ 00:11:43]; renewals are created as '
                                        "agreement-based offers from the buyer's active subscription "
                                        '[Amazon Web Services — KzcE0ZWyjzk @ 00:01:15]'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The first fork is how the cash moves. The AWS SaaS-contract walkthrough '
                              'lays out two pricing tracks: contract pricing with upfront payment, where '
                              'the buyer picks quantities and AWS invoices the full amount the moment the '
                              'private offer is accepted, versus contract pricing with an installment '
                              'plan, where the seller enters a total contract price, a number of '
                              'installments and a first invoice date, then can hand-edit each invoice '
                              'amount or date [2qDBJ9lxIdQ @ 00:02:24]. David at re:Invent treats '
                              'installments as a bargaining chip rather than an admin setting: AWS sends '
                              'the invoice on the specific date seller and customer agree on, and the '
                              'installment date and distribution becomes a factor in the negotiation '
                              '[K-GonrtXvKA @ 00:03:56]. The catch surfaces on renewals. Chloe Weaver '
                              'points out that every agreement-based offer is created with scheduled '
                              'payments, which requires the buyer to be on invoicing terms with AWS '
                              '[KzcE0ZWyjzk @ 00:01:37]. The buyer-side walkthrough spells out the fix: '
                              'switch the account to invoicing terms, also called ACH direct debit, by '
                              'opening a customer service case under Account and billing support in the '
                              'Marketplace category with company name, contact name, phone, email and '
                              'mailing address attached [XvBBSBimMn4 @ 00:05:47]. Upfront billing dodges '
                              "that friction; installments demand the buyer's billing setup be sorted "
                              'first.',
                              'The second split is where offers get built. The ISV operations overview '
                              'describes the old way, manually entering deal details into a form for '
                              'customization, and the new way: the seller creates tool inside the AWS '
                              'Marketplace Management Portal, which lets the partner build the offer '
                              'independently without being in touch with the AWS team, with a direct ask '
                              'to reach out if the tool is not working on the account [qWl-wamuA-Q @ '
                              '00:06:07]. David pushes past the portal entirely once volume climbs: '
                              'integrate with the Marketplace API so private offers go out from the '
                              "seller's own CRM instead of logging onto the portal every single time, and "
                              'create products and read agreements there too, which David calls how you go '
                              'fast and go big [K-GonrtXvKA @ 00:14:28]. Clazar CEO Prunal pitches a third '
                              'lane, working with an implementation expert to launch on AWS in a couple of '
                              'weeks or less [h7liwzzA_-I @ 00:01:50]. Inside the AWS Ops Squad, the '
                              'favorite low-tech fix is simply drafts: one team member calls saving as '
                              'drafts a game changer because folks no longer have to complete private '
                              'offer creation in one step and can walk away until they have all of the '
                              'information [gNv2wvhYkzA @ 00:04:12]. Low-volume sellers can live in the '
                              'wizard; high-volume sellers are told to wire the API.',
                              'Packaging is the third fault line. The PartnerCloud host, listing '
                              'professional services, skipped tiered dimensions like platinum, gold and '
                              'silver, kept a single monthly dimension and chose to shoehorn everyone into '
                              'that one option, pushing differentiation into private pricing; by default '
                              'the whole listing routes through private pricing, and the host is still '
                              'curious what showing a public price for the assessment would look and feel '
                              'like [qXei9F9hLNU @ 00:17:19]. David argues for a different emphasis: tap '
                              'product-led growth with self-service click-to-buy, free trials, request for '
                              'demo and request for private offer so customers start on Marketplace, '
                              'become leads and get access to larger private-offer deals [K-GonrtXvKA @ '
                              '00:12:16]. Tyler from the AWS Marketplace team frames the same split as two '
                              'purchase paths, self-service subscription with little to no intervention '
                              'versus private offers as a white glove experience where sellers control '
                              'contract terms and payment schedules as they see fit [HU_SJTFHcGU @ '
                              '00:02:20]. The PartnerCloud host also takes a swing at big partners who '
                              'bucket every transaction under one company-named listing, arguing that '
                              'separate SKUs per offering and per industry, healthcare versus education '
                              'versus automotive, make the seller findable by buyers and AWS field sellers '
                              'alike [qXei9F9hLNU @ 00:20:51]. The trade is reach through a public price '
                              'versus control through a custom quote.'],
               'table': {'caption': 'Competing playbooks for pricing, building, renewing and packaging AWS '
                                    'Marketplace private offers',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Billing structure for a new SaaS contract private offer',
                                   'Upfront contract pricing where the buyer picks quantities and AWS '
                                   'invoices the full amount on acceptance',
                                   'Installment plan with total contract price, number of installments, '
                                   'first invoice date and editable invoices',
                                   'Amazon Web Services ([2qDBJ9lxIdQ @ 00:02:24])'],
                                  ['Where private offers get built as deal volume grows',
                                   'Five-step wizard in the Management Portal Offers tab, with drafts '
                                   'saved and resumed later',
                                   'Marketplace API integration so offers, products and agreement reads '
                                   'run from your own CRM',
                                   'AWS Events ([K-GonrtXvKA @ 00:14:28])'],
                                  ['How to handle renewals and expansions of in-flight agreements',
                                   'Agreement-based offer copies the active agreement, then cancels and '
                                   'replaces it once accepted',
                                   'Future dated agreement delivers entitlement at a predetermined date, '
                                   'decoupled from transaction close date',
                                   'AWS Events ([K-GonrtXvKA @ 00:14:49])'],
                                  ['Agreement end date when amending an existing customer subscription',
                                   'Co-term the agreement-based offer and keep the current agreement end '
                                   'date unchanged',
                                   'Choose a brand new agreement end date for the replacement offer going '
                                   'forward',
                                   'Amazon Web Services ([MlboB3rLbvE @ 00:01:07])'],
                                  ['Contract paper attached to the private offer for the buyer',
                                   'Adopt the Standard Contract for AWS Marketplace so buyers avoid '
                                   'renegotiating terms from scratch',
                                   'Keep the current EULA, pick public, standard or enterprise EULAs, or '
                                   'upload a custom EULA',
                                   'AWS Events ([K-GonrtXvKA @ 00:14:09]); Amazon Web Services '
                                   '([MlboB3rLbvE @ 00:02:14])'],
                                  ['Listing structure for discovery by buyers and AWS field sellers',
                                   'One listing with one monthly dimension, differentiation pushed '
                                   'entirely into private pricing',
                                   'Separate SKUs per product and per industry instead of bucketing under '
                                   'one company name',
                                   'PartnerCloud ([qXei9F9hLNU @ 00:17:19]); PartnerCloud ([qXei9F9hLNU @ '
                                   '00:20:51])'],
                                  ['Route to market for larger and strategic enterprise deals',
                                   'Direct seller private offer negotiated between ISV and buyer '
                                   'independently outside of AWS',
                                   'Channel Partner Private Offer, with resell authorizations letting '
                                   'channel partners create offers on your behalf',
                                   'Clazar ([h7liwzzA_-I @ 00:01:15]); AWS Events ([K-GonrtXvKA @ '
                                   '00:12:36])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most common dead deal is a link that stops working. The ISV operations '
                              'overview is blunt: every private offer carries a set expiration date, and '
                              'if the customer does not accept by then the offer is no longer available, '
                              'leaving the partner to either extend the expiration date or create a new '
                              'offer [qWl-wamuA-Q @ 00:01:43]. The agreement-based offer walkthrough adds '
                              'the clock detail that trips sellers: AWS systems run in UTC time, and best '
                              'practice is to set the expiration date for at least two weeks [MlboB3rLbvE '
                              '@ 00:02:38]. When the buyer clicks and hits a 404, the AWS troubleshooting '
                              'list runs in order: confirm the buyer is logged in to the correct account '
                              'ID, confirm with the ISV or channel partner that the offer was created for '
                              'that account ID, and check whether it expired, which the seller fixes by '
                              'modifying the expiration date in the Offers tab [XvBBSBimMn4 @ 00:06:43]. '
                              'Two quieter blockers follow: a buyer running a private marketplace needs '
                              'the product on its allow list, and ISVs using limited listings, products '
                              "not available on the public Marketplace, must allow the customer's account "
                              'to view it; only after that does the advice drop to clearing cache and '
                              'cookies, incognito windows or a different browser, never Internet Explorer '
                              '[XvBBSBimMn4 @ 00:07:16].',
                              'Renewals and SaaS fulfillment carry their own landmines. Chloe Weaver warns '
                              'that when a buyer subscribes to an agreement-based offer it completely '
                              'replaces the current subscription: invoices already generated stay '
                              'untouched, but invoices from the original deal that have not been generated '
                              'yet are replaced by the new payment schedule, and no cancellation of the '
                              'previous subscription is necessary [KzcE0ZWyjzk @ 00:02:16]. Timing is not '
                              'instant either; the agreement-based offer walkthrough says the offer is '
                              'created within 45 minutes and only then becomes available to send from the '
                              'Offers tab, so the link is not ready the instant the offer is submitted '
                              '[MlboB3rLbvE @ 00:03:17]. On SaaS, the create-offer demo stresses that AWS '
                              'does not provision SaaS products: after subscribing, the buyer must '
                              "register on the seller's website, and if the product includes consumption, "
                              'additional usage is billed on top of the upfront amount [PVL4069oqC0 @ '
                              "00:02:32]. The buyer-side walkthrough ties that overage to the seller's "
                              'plumbing, since additional usage is billed on the third of the following '
                              'month provided the ISV sends AWS metering records [XvBBSBimMn4 @ 00:04:25]. '
                              'Skip the registration page or the metering feed and the deal closes on '
                              'paper while the product access or the overage revenue never lands.',
                              'Run the economics check before granting the discount. The ISV overview '
                              'walks the math: a $100 list price with a 20 percent negotiated discount '
                              'lands the customer at $80, and when the customer pays the AWS invoice, AWS '
                              'disburses that $80 minus applicable listing fees, which at the 10 percent '
                              'fee used in the example nets the ISV $72 [qWl-wamuA-Q @ 00:10:25]. The cash '
                              'lag is structural: customers receive invoices on the third of the month, '
                              'AWS invoice net payment terms apply, and once a payment is received it can '
                              'take one to two days to post to the sub-ledger, which must happen at time '
                              'of disbursement for the funds to be included [qWl-wamuA-Q @ 00:12:05]. The '
                              'PartnerCloud host hit a different wall during setup: the listing review got '
                              'hung up because the website had no support section, a professional-services '
                              'shop with no support component to point to, so the host added one and went '
                              'back under review with the company profile still limited to private '
                              'visibility [qXei9F9hLNU @ 00:07:08]. The Ops Squad team describes the '
                              'year-end failure mode future dated agreements were built to kill: running '
                              'around last minute at Christmas asking whether a deal is done with '
                              "everyone's hair on fire, with some partners implementing future dated "
                              'agreements at scale and seeing renewal rates go up [gNv2wvhYkzA @ '
                              '00:03:43].'],
               'table': {'caption': 'Firsthand traps on AWS Marketplace private offers and the fixes '
                                    'practitioners used',
                         'headers': ['Failure Mode',
                                     'What Happened Or Was Warned',
                                     'Fix Practitioners Used',
                                     'Expert Source'],
                         'rows': [['Private offer expires before the buyer accepts it',
                                   'Offer becomes unavailable after the expiration date; partner must '
                                   'extend it or rebuild a new offer',
                                   'Set expiration at least two weeks out, remembering AWS systems run on '
                                   'UTC time',
                                   'Amazon Web Services ([qWl-wamuA-Q @ 00:01:43]); Amazon Web Services '
                                   '([MlboB3rLbvE @ 00:02:38])'],
                                  ['Buyer hits a 404 error opening the private offer link',
                                   'Wrong account ID, expired offer, private marketplace block, or limited '
                                   'listing not allow-listed for the account',
                                   'Verify account ID, extend expiration in the Offers tab, allow-list the '
                                   'account, then clear cache',
                                   'Amazon Web Services ([XvBBSBimMn4 @ 00:06:27])'],
                                  ['Buyer cannot accept a scheduled-payment or agreement-based private '
                                   'offer',
                                   'Offers with one or more scheduled payments require the buyer account '
                                   'to be on AWS invoicing terms',
                                   'Buyer opens a customer service case asking to switch the account to '
                                   'invoicing terms',
                                   'Amazon Web Services ([XvBBSBimMn4 @ 00:05:47])'],
                                  ["Agreement-based offer overwrites the existing deal's future invoices",
                                   'Invoices from the original subscription that were not generated yet '
                                   'get replaced by the new schedule',
                                   'Build the new payment schedule knowing billed invoices stay intact and '
                                   'unbilled ones are replaced',
                                   'Amazon Web Services ([KzcE0ZWyjzk @ 00:02:35])'],
                                  ['SaaS buyer subscribes but never gets access to the product',
                                   'AWS does not provision SaaS products, so buyers must register on the '
                                   "seller's own website",
                                   'Buyers who forgot registration find the website links under their '
                                   'Marketplace software later',
                                   'Amazon Web Services ([XvBBSBimMn4 @ 00:08:27])'],
                                  ['Listing stuck in review and company profile stuck on private',
                                   'PartnerCloud had no support section on its website for a '
                                   'professional-services listing',
                                   'Added a support section to the website, resubmitted, and waited on the '
                                   'Marketplace review',
                                   'PartnerCloud ([qXei9F9hLNU @ 00:10:28])'],
                                  ['Consumption overage revenue never gets billed to the buyer',
                                   'AWS bills additional usage on the third of the month only after the '
                                   'ISV sends metering records',
                                   'ISV sends metering records through the AWS Marketplace Metering '
                                   'Service every billing cycle',
                                   'Amazon Web Services ([XvBBSBimMn4 @ 00:02:40])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before any private offer URL leaves your hands',
                           'body': 'Every item below maps to a failure the AWS Marketplace team or a '
                                   'working seller hit or warned about directly. Clear all four before the '
                                   'buyer clicks.',
                           'items': ['Confirm the offer status reads Active, meaning it is published and '
                                     'available for the buyer to accept, and allow up to 45 minutes for '
                                     'agreement-based offers to generate [Amazon Web Services — '
                                     '2qDBJ9lxIdQ @ 00:04:15].',
                                     'Set the expiration date at least two weeks out and remember AWS '
                                     'systems run in UTC time [Amazon Web Services — MlboB3rLbvE @ '
                                     '00:02:38].',
                                     "Verify the buyer's AWS account ID and, for any scheduled payments, "
                                     'that the buyer account is already on invoicing terms [Amazon Web '
                                     'Services — XvBBSBimMn4 @ 00:05:47].',
                                     'For SaaS with consumption, have the registration website live and '
                                     'metering records flowing, since overage bills on the third of the '
                                     'following month only when the ISV sends them [Amazon Web Services — '
                                     'XvBBSBimMn4 @ 00:04:25].']}}],
 'pull_quote': "We're not having to run around last minute the end of the year when it's Christmas and say "
               "hey where's this deal, is it done, and everyone's freaking out, everyone's hair is on "
               'fire. Attributed to Amazon Web Services (gNv2wvhYkzA @ 00:03:43).',
 'diagram_id': 'diag-07',
 'action_checklist': ['Register as a seller from a brand new AWS account used only as the seller of '
                      'record, keeping disbursements and permissions separate from production [Amazon Web '
                      'Services — w6XECzZOfXY @ 00:01:44].',
                      'Build the public profile with a 300 by 150 logo, display name, URL and a '
                      '600-character description, then finish tax, bank and KYC tabs [PartnerCloud — '
                      'qXei9F9hLNU @ 00:02:35].',
                      'Publish a support section on your website before submitting the listing so the '
                      'Marketplace review does not stall [PartnerCloud — qXei9F9hLNU @ 00:07:08].',
                      'Open the Offers tab, hit Create Private Offer, select product type and product, and '
                      'walk the five-step wizard, saving drafts as needed [AWS Events — K-GonrtXvKA @ '
                      '00:05:38].',
                      'Set the offer expiration at least two weeks out in UTC, then copy the offer URL and '
                      'send it to the buyer [Amazon Web Services — MlboB3rLbvE @ 00:02:38].',
                      "For renewals, search the buyer's AWS account ID in the Agreements tab, select the "
                      'active agreement, choose Create agreement-based offer and mark it as a renewal '
                      '[Amazon Web Services — KzcE0ZWyjzk @ 00:01:37].'],
 'statutory_citations': [{'title': "AWS Events — AWS re:Invent 2024 - Custom pricing: What's new with AWS "
                                   'Marketplace private offers (PEX113) [00:14:49]',
                          'url': 'https://www.youtube.com/watch?v=K-GonrtXvKA&t=889s',
                          'relevance': 'Primary practitioner testimony on agreement-based offers, future '
                                       'dated agreements, API-driven offer creation and channel resell '
                                       'authorizations.'},
                         {'title': 'Amazon Web Services — AWS Marketplace Private Offers overview for ISVs '
                                   '[00:10:25]',
                          'url': 'https://www.youtube.com/watch?v=qWl-wamuA-Q&t=625s',
                          'relevance': 'Primary practitioner testimony on discount math, listing fees, '
                                       'invoicing dates and disbursement timing for private offers.'},
                         {'title': 'Amazon Web Services — Subscribing to SaaS Contract Private Offers - '
                                   'AWS Marketplace [00:06:27]',
                          'url': 'https://www.youtube.com/watch?v=XvBBSBimMn4&t=387s',
                          'relevance': 'Primary practitioner testimony on buyer-side 404 troubleshooting, '
                                       'invoicing terms and metering-dependent overage billing.'},
                         {'title': 'PartnerCloud — AWS Marketplace 101  Building a Profile and My First '
                                   'Listing! [00:07:08]',
                          'url': 'https://www.youtube.com/watch?v=qXei9F9hLNU&t=428s',
                          'relevance': 'Primary practitioner testimony on seller profile setup, listing '
                                       'review friction and SKU packaging strategy.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'h7liwzzA_-I',
                       'title': 'How Private Offers work on AWS Marketplace explained step by step',
                       'channel': 'Clazar',
                       'author': 'Clazar',
                       'text': 'Private offers are useful for enterprise customers requiring tailored '
                               'pricing and contract terms, multi-year or volume based deals, or channel '
                               'partner motions through CPPO.',
                       'tip': 'Private offers are useful for enterprise customers requiring tailored '
                              'pricing and contract terms, multi-year or volume based deals, or channel '
                              'partner motions through CPPO.',
                       'timestamp': 75,
                       'timestamp_seconds': 75,
                       'timestamp_label': '[00:01:15]',
                       'url': 'https://www.youtube.com/watch?v=h7liwzzA_-I&t=75s',
                       'markdown': '[00:01:15](https://www.youtube.com/watch?v=h7liwzzA_-I&t=75s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iROp007IYLs',
                       'title': 'AWS Private Marketplace Overview',
                       'channel': 'Amazon Web Services',
                       'author': 'Amazon Web Services',
                       'text': 'End users with existing subscriptions can continue using products that '
                               "have been removed from the private Marketplace catalog, however they won't "
                               'be able to change or renew their subscriptions until the product is '
                               'approved in the private marketplace.',
                       'tip': 'End users with existing subscriptions can continue using products that have '
                              "been removed from the private Marketplace catalog, however they won't be "
                              'able to change or renew their subscriptions until the product is approved '
                              'in the private marketplace.',
                       'timestamp': 357,
                       'timestamp_seconds': 357,
                       'timestamp_label': '[00:05:57]',
                       'url': 'https://www.youtube.com/watch?v=iROp007IYLs&t=357s',
                       'markdown': '[00:05:57](https://www.youtube.com/watch?v=iROp007IYLs&t=357s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PVL4069oqC0',
                       'title': 'Create Private Offer in AWS Marketplace | Amazon Web Services',
                       'channel': 'Amazon Web Services',
                       'author': 'Amazon Web Services',
                       'text': 'Once the buyer subscribes they are billed upfront for the amount that they '
                               'subscribe to, and AWS does not provision SaaS products to buyers, so '
                               "buyers must register the SaaS product on the seller's website.",
                       'tip': 'Once the buyer subscribes they are billed upfront for the amount that they '
                              'subscribe to, and AWS does not provision SaaS products to buyers, so buyers '
                              "must register the SaaS product on the seller's website.",
                       'timestamp': 152,
                       'timestamp_seconds': 152,
                       'timestamp_label': '[00:02:32]',
                       'url': 'https://www.youtube.com/watch?v=PVL4069oqC0&t=152s',
                       'markdown': '[00:02:32](https://www.youtube.com/watch?v=PVL4069oqC0&t=152s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2qDBJ9lxIdQ',
                       'title': 'Create AWS Marketplace Private Offers for SaaS Contracts | Amazon Web '
                                'Services',
                       'channel': 'Amazon Web Services',
                       'author': 'Amazon Web Services',
                       'text': "The next step is to specify the buyer's AWS account ID so we can target "
                               'the offer, and we can add up to 23 buyers to this private offer.',
                       'tip': "The next step is to specify the buyer's AWS account ID so we can target the "
                              'offer, and we can add up to 23 buyers to this private offer.',
                       'timestamp': 233,
                       'timestamp_seconds': 233,
                       'timestamp_label': '[00:03:53]',
                       'url': 'https://www.youtube.com/watch?v=2qDBJ9lxIdQ&t=233s',
                       'markdown': '[00:03:53](https://www.youtube.com/watch?v=2qDBJ9lxIdQ&t=233s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xLqQjXa2edo',
                       'title': 'Create an AWS Marketplace Future Dated Private Offer | Amazon Web '
                                'Services',
                       'channel': 'Amazon Web Services',
                       'author': 'Amazon Web Services',
                       'text': 'The private offer has been created, and once the buyer accepts the offer, '
                               'it will become a future dated agreement.',
                       'tip': 'The private offer has been created, and once the buyer accepts the offer, '
                              'it will become a future dated agreement.',
                       'timestamp': 138,
                       'timestamp_seconds': 138,
                       'timestamp_label': '[00:02:18]',
                       'url': 'https://www.youtube.com/watch?v=xLqQjXa2edo&t=138s',
                       'markdown': '[00:02:18](https://www.youtube.com/watch?v=xLqQjXa2edo&t=138s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qWl-wamuA-Q',
                       'title': 'AWS Marketplace Private Offers overview for ISVs',
                       'channel': 'Amazon Web Services',
                       'author': 'Amazon Web Services',
                       'text': 'AWS first takes out eighty dollars, the discounted price to the customer, '
                               'to disburse to the ISV minus any applicable listing fees, and with a 10 '
                               'percent listing fee the net revenue to the ISV is $72.',
                       'tip': 'AWS first takes out eighty dollars, the discounted price to the customer, '
                              'to disburse to the ISV minus any applicable listing fees, and with a 10 '
                              'percent listing fee the net revenue to the ISV is $72.',
                       'timestamp': 625,
                       'timestamp_seconds': 625,
                       'timestamp_label': '[00:10:25]',
                       'url': 'https://www.youtube.com/watch?v=qWl-wamuA-Q&t=625s',
                       'markdown': '[00:10:25](https://www.youtube.com/watch?v=qWl-wamuA-Q&t=625s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qWl-wamuA-Q',
                       'title': 'AWS Marketplace Private Offers overview for ISVs',
                       'channel': 'Amazon Web Services',
                       'author': 'Amazon Web Services',
                       'text': 'If the customer does not accept the private offer by the expiration date '
                               'the offer will no longer be available, and the partner will either have to '
                               'extend the offer expiration date or create a new offer.',
                       'tip': 'If the customer does not accept the private offer by the expiration date '
                              'the offer will no longer be available, and the partner will either have to '
                              'extend the offer expiration date or create a new offer.',
                       'timestamp': 103,
                       'timestamp_seconds': 103,
                       'timestamp_label': '[00:01:43]',
                       'url': 'https://www.youtube.com/watch?v=qWl-wamuA-Q&t=103s',
                       'markdown': '[00:01:43](https://www.youtube.com/watch?v=qWl-wamuA-Q&t=103s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'K-GonrtXvKA',
                       'title': "AWS re:Invent 2024 - Custom pricing: What's new with AWS Marketplace "
                                'private offers (PEX113)',
                       'channel': 'AWS Events',
                       'author': 'AWS Events',
                       'text': 'Integrate with Marketplace API so that you can actually extend those '
                               'private offers from your own CRM environment rather than logging onto the '
                               'portal every single time.',
                       'tip': 'Integrate with Marketplace API so that you can actually extend those '
                              'private offers from your own CRM environment rather than logging onto the '
                              'portal every single time.',
                       'timestamp': 868,
                       'timestamp_seconds': 868,
                       'timestamp_label': '[00:14:28]',
                       'url': 'https://www.youtube.com/watch?v=K-GonrtXvKA&t=868s',
                       'markdown': '[00:14:28](https://www.youtube.com/watch?v=K-GonrtXvKA&t=868s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KzcE0ZWyjzk',
                       'title': 'Renew SaaS Contract Private Offers - AWS Marketplace | Amazon Web '
                                'Services',
                       'channel': 'Amazon Web Services',
                       'author': 'Amazon Web Services',
                       'text': 'When a buyer subscribes to an agreement-based offer it completely replaces '
                               "the buyer's current subscription, and any invoices already generated for "
                               'the buyer will not be modified.',
                       'tip': 'When a buyer subscribes to an agreement-based offer it completely replaces '
                              "the buyer's current subscription, and any invoices already generated for "
                              'the buyer will not be modified.',
                       'timestamp': 136,
                       'timestamp_seconds': 136,
                       'timestamp_label': '[00:02:16]',
                       'url': 'https://www.youtube.com/watch?v=KzcE0ZWyjzk&t=136s',
                       'markdown': '[00:02:16](https://www.youtube.com/watch?v=KzcE0ZWyjzk&t=136s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gNv2wvhYkzA',
                       'title': 'AWS Marketplace Ops Squad | Amazon Web Services',
                       'channel': 'Amazon Web Services',
                       'author': 'Amazon Web Services',
                       'text': "We've seen some partners actually implement future dated agreements at "
                               "scale and they've seen their renewal rate go up as a result.",
                       'tip': "We've seen some partners actually implement future dated agreements at "
                              "scale and they've seen their renewal rate go up as a result.",
                       'timestamp': 237,
                       'timestamp_seconds': 237,
                       'timestamp_label': '[00:03:57]',
                       'url': 'https://www.youtube.com/watch?v=gNv2wvhYkzA&t=237s',
                       'markdown': '[00:03:57](https://www.youtube.com/watch?v=gNv2wvhYkzA&t=237s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MlboB3rLbvE',
                       'title': 'Create an Agreements Based Offer - AWS Marketplace Private Offers',
                       'channel': 'Amazon Web Services',
                       'author': 'Amazon Web Services',
                       'text': 'AWS systems are in UTC time and best practice is to set the expiration '
                               'date for at least two weeks.',
                       'tip': 'AWS systems are in UTC time and best practice is to set the expiration date '
                              'for at least two weeks.',
                       'timestamp': 158,
                       'timestamp_seconds': 158,
                       'timestamp_label': '[00:02:38]',
                       'url': 'https://www.youtube.com/watch?v=MlboB3rLbvE&t=158s',
                       'markdown': '[00:02:38](https://www.youtube.com/watch?v=MlboB3rLbvE&t=158s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qXei9F9hLNU',
                       'title': 'AWS Marketplace 101  Building a Profile and My First Listing!',
                       'channel': 'PartnerCloud',
                       'author': 'PartnerCloud',
                       'text': "Maybe it makes more sense, and maybe it's how people would find you more "
                               'efficiently, if you industrialized your products and created different '
                               'SKUs for your different products.',
                       'tip': "Maybe it makes more sense, and maybe it's how people would find you more "
                              'efficiently, if you industrialized your products and created different SKUs '
                              'for your different products.',
                       'timestamp': 1251,
                       'timestamp_seconds': 1251,
                       'timestamp_label': '[00:20:51]',
                       'url': 'https://www.youtube.com/watch?v=qXei9F9hLNU&t=1251s',
                       'markdown': '[00:20:51](https://www.youtube.com/watch?v=qXei9F9hLNU&t=1251s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'w6XECzZOfXY',
                       'title': 'How to register as an AWS Marketplace seller | Amazon Web Services',
                       'channel': 'Amazon Web Services',
                       'author': 'Amazon Web Services',
                       'text': 'We recommend creating a new AWS account because all AWS Marketplace '
                               'interactions will be tied to this account moving forward.',
                       'tip': 'We recommend creating a new AWS account because all AWS Marketplace '
                              'interactions will be tied to this account moving forward.',
                       'timestamp': 104,
                       'timestamp_seconds': 104,
                       'timestamp_label': '[00:01:44]',
                       'url': 'https://www.youtube.com/watch?v=w6XECzZOfXY&t=104s',
                       'markdown': '[00:01:44](https://www.youtube.com/watch?v=w6XECzZOfXY&t=104s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HU_SJTFHcGU',
                       'title': 'Introduction to AWS Marketplace | Amazon Web Services',
                       'channel': 'Amazon Web Services',
                       'author': 'Amazon Web Services',
                       'text': "We have a number of sellers who have shared that they've accelerated their "
                               'sales cycles, some upwards of 50 percent, just by selling through AWS '
                               'Marketplace.',
                       'tip': "We have a number of sellers who have shared that they've accelerated their "
                              'sales cycles, some upwards of 50 percent, just by selling through AWS '
                              'Marketplace.',
                       'timestamp': 322,
                       'timestamp_seconds': 322,
                       'timestamp_label': '[00:05:22]',
                       'url': 'https://www.youtube.com/watch?v=HU_SJTFHcGU&t=322s',
                       'markdown': '[00:05:22](https://www.youtube.com/watch?v=HU_SJTFHcGU&t=322s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XvBBSBimMn4',
                       'title': 'Subscribing to SaaS Contract Private Offers - AWS Marketplace',
                       'channel': 'Amazon Web Services',
                       'author': 'Amazon Web Services',
                       'text': 'Some ISVs use limited listings, which are products not available on the '
                               'public Marketplace for private offer transactions, so ask the ISV if the '
                               "product is a limited listing and if they have allowed the customer's "
                               'account to view it.',
                       'tip': 'Some ISVs use limited listings, which are products not available on the '
                              'public Marketplace for private offer transactions, so ask the ISV if the '
                              "product is a limited listing and if they have allowed the customer's "
                              'account to view it.',
                       'timestamp': 436,
                       'timestamp_seconds': 436,
                       'timestamp_label': '[00:07:16]',
                       'url': 'https://www.youtube.com/watch?v=XvBBSBimMn4&t=436s',
                       'markdown': '[00:07:16](https://www.youtube.com/watch?v=XvBBSBimMn4&t=436s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RxCRHsAqiWs',
                       'title': 'AWS Marketplace: Seller Private Offers',
                       'channel': 'Amazon Web Services',
                       'author': 'Amazon Web Services',
                       'text': 'Purchases made by linked accounts will be reported under your master payer '
                               'account and broken out by the account that subscribed to the product.',
                       'tip': 'Purchases made by linked accounts will be reported under your master payer '
                              'account and broken out by the account that subscribed to the product.',
                       'timestamp': 68,
                       'timestamp_seconds': 68,
                       'timestamp_label': '[00:01:08]',
                       'url': 'https://www.youtube.com/watch?v=RxCRHsAqiWs&t=68s',
                       'markdown': '[00:01:08](https://www.youtube.com/watch?v=RxCRHsAqiWs&t=68s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4obiejTAlFQ',
                       'title': 'What is AWS Marketplace | Amazon Web Services',
                       'channel': 'Amazon Web Services',
                       'author': 'Amazon Web Services',
                       'text': 'When ready for a bigger investment, save money with long-term contracts, '
                               'bring your own license or negotiate custom pricing and terms with private '
                               'offers.',
                       'tip': 'When ready for a bigger investment, save money with long-term contracts, '
                              'bring your own license or negotiate custom pricing and terms with private '
                              'offers.',
                       'timestamp': 62,
                       'timestamp_seconds': 62,
                       'timestamp_label': '[00:01:02]',
                       'url': 'https://www.youtube.com/watch?v=4obiejTAlFQ&t=62s',
                       'markdown': '[00:01:02](https://www.youtube.com/watch?v=4obiejTAlFQ&t=62s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'}]}
