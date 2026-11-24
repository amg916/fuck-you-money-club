from __future__ import annotations

CHAPTER_10 = {'id': 'Q10',
 'chapter_id': 'Q10',
 'chapter_number': 10,
 'question_number': 10,
 'slug': 'procure-to-pay-vendor-onboarding',
 'question_prompt': 'How do buyer procurement systems onboard vendors and process purchases, and what must '
                    'a reseller fit into?',
 'kicker': 'Q10 / THE BIG MONEY PLAYBOOKS',
 'title': 'Procure-to-Pay and Vendor Onboarding',
 'subtitle': 'Supplier payment-term negotiation, SAP Business Network, NetSuite procure-to-pay and RFQ, '
             'Business Central and Zoho procurement, no-code and DocuSign onboarding automation, Peakflo, '
             'a 30-entity D365 vendor master case, and procurement manager expectations',
 'layout_template': 'expert_commentary',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners from Gatekeeper, Charted, PROKURIA, LeadSquared, AVC-Licensing and '
                      'the NetSuite consulting bench agree that vendor onboarding is the front-end control '
                      'of procure-to-pay. Bad bank details, stale documents and duplicate records entered '
                      'at intake ripple into returned payments, failed three-way matches and messy '
                      'month-end accruals. The street mechanics replace emailed Excel forms with validated '
                      'digital intake that writes straight into the ERP. They push invoice errors back '
                      'onto suppliers through PO flips and 120-plus SAP business rules, and they earn '
                      'payment terms step by step from 100 percent upfront toward Net 60. On $50,000 of '
                      'monthly spend, that is worth roughly $100,000 of supplier financing. The '
                      'disagreements center on vendor portals versus password-free links, single-page '
                      'versus multi-step forms, and whether to negotiate contracts in parallel with vendor '
                      'checks to speed time-to-contract.',
 'key_metrics': [{'label': 'Supplier Financing Unlocked at Net 60',
                  'metric': 'Supplier Financing Unlocked at Net 60',
                  'value': 'Approximately $100,000 ($50,000 monthly purchases x 2 months)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Simplified steady-state calculation for a buyer moving a $50,000-per-month '
                             'supplier from 100 percent upfront payment to Net 60. The benefit depends on '
                             'invoice timing, shipment schedules and credit limits.',
                  'source': '10 Min For Supply Chain ([vdxHe8A6Tkk @ 00:02:11])'},
                 {'label': 'Vendor Master Consolidation Scope',
                  'metric': 'Vendor Master Consolidation Scope',
                  'value': '~8,000 records across 30 legal entities mapped to ~6,800 master accounts; 5 '
                           'rehearsals; ~4-hour cutover',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'D365 consolidation where the AP team owned every survivorship decision. Five '
                             'full rehearsals ran on copies of production before a weekend cutover.',
                  'source': 'AVC-Licensing ([8S2AXmoUSJY @ 00:00:42])'},
                 {'label': 'Onboarding Cycle Compression',
                  'metric': 'Onboarding Cycle Compression',
                  'value': '20 days reduced to 5-10 hours (Zoomcar)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'LeadSquared customer testimonial on overall vendor onboarding time after '
                             'moving the process onto the platform.',
                  'source': 'LeadSquared ([mR8B4VcLNjU @ 00:44:41])'},
                 {'label': 'Pre-AP Invoice Validation Rules',
                  'metric': 'Pre-AP Invoice Validation Rules',
                  'value': '120-plus business rules',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'SAP Business Network checks supplier invoices for errors before they hit '
                             'accounts payable. It can block altered quantities or values even when the '
                             'total is unchanged.',
                  'source': 'Spend And Procurement with Mike ([xPYn_cF6f1E @ 00:00:58])'}],
 'sections': [{'title': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every operator here treats vendor onboarding as the front door of '
                              "procure-to-pay rather than clerical paperwork. Gatekeeper's speaker opens "
                              'with the scare number: Google and Facebook have both paid over a hundred '
                              'million dollars to fraudulent vendors. The speaker blames vendors that were '
                              'never properly onboarded, and frames the whole function as a risk '
                              'mitigation play run before the contract is signed [-L_45dSkyaE @ 00:00:00]. '
                              'Marlin at Charted splits accounts payable into four buckets: vendors, '
                              'invoices, payments and accruals. Friction compounds downstream from the '
                              'vendor record. A wrong address sends the check astray, and a fat-fingered '
                              'account number triggers a returned ACH and a delayed payment. The mess '
                              'resurfaces later in three-way match and month-end accrual reconciliation '
                              "[1wlmLTmDAfc @ 00:05:03]. PROKURIA's deep dive reaches the same thesis from "
                              'the compliance side. It defines the real scope as legal documents, tax '
                              'forms, GDPR, ESG and anti-bribery checks, payment setup, risk assessment '
                              'and system access, and it claims structured programs can cut onboarding '
                              'time by over a third [_R1e9FCXKyI @ 00:01:00]. The shared takeaway for a '
                              'reseller running a supplier base is blunt: the vendor master is a control, '
                              'not a list. AVC-Licensing closes its consolidation case study on exactly '
                              'that line. Deduplication counts rows, while a vendor master is a control '
                              'the business relies on every day [8S2AXmoUSJY @ 00:03:00].',
                              'The second point of agreement is that email-and-spreadsheet onboarding '
                              'bleeds time and opens fraud exposure. Alex at PROKURIA walks through the '
                              'standard Excel or PDF supplier form, sent as an attachment with a cover '
                              'email. The predictable outcome is a long thread of reminders, follow-ups '
                              'and missing documents, because not every supplier is organized or quick to '
                              'respond [_tfz6kZ8JZo @ 00:00:42]. The PROKURIA deep dive lists the '
                              'recurring pain points: fragmented data, suppliers asked for the same thing '
                              'over and over, manual spreadsheets and email chains, compliance blind spots '
                              'such as expired insurance, and vendor data stranded in one place while the '
                              'ERP sits somewhere else [_R1e9FCXKyI @ 00:02:01]. Ashish Gupta at '
                              'LeadSquared calls the no-system version clumsy and scattered. Commitments '
                              'stay verbal, documents cannot be found, security concerns pile up, team '
                              'productivity falls, and the business ends up onboarding the wrong set of '
                              'vendors [mR8B4VcLNjU @ 00:13:50]. Marlin at Charted adds the fraud angle '
                              'directly. Informal Excel or CSV-driven vendor updates are prone to '
                              'potential fraud, incorrect formatting and missing validation, which '
                              'together create chaos that ripples straight into payments [1wlmLTmDAfc @ '
                              '00:06:22]. Each of these speakers sells or builds a fix, but the diagnosis '
                              'is identical: unstructured intake is where bad bank details, stale '
                              'documents and duplicate vendors get into the system.',
                              'Practitioners also agree the process must be lean for the supplier and '
                              "tiered for the buyer. Gatekeeper's rule is the sharpest: only ask a vendor "
                              'a question if you will take the answer and do something with it, and strip '
                              "everything else out. Automated checks such as Gatekeeper's Market IQ should "
                              'cover financial and cyber health instead of long questionnaires, because a '
                              'rigid, onerous onboarding creates tension before the relationship starts. '
                              'The same speaker then uses onboarding data to segment vendors. Strategic '
                              'suppliers are prioritized by risk, spend or criticality, and transactional '
                              'tail-spend vendors get lighter oversight [-L_45dSkyaE @ 00:05:45]. '
                              "PROKURIA's best-practice list mirrors this. Centralize on one platform as a "
                              'single source of truth, automate checks and revalidations, and segment '
                              'suppliers because not every vendor needs the same scrutiny. Focus on '
                              'supplier experience to become a customer of choice [_R1e9FCXKyI @ '
                              '00:04:15]. Marlin at Charted describes the ideal vendor experience as a '
                              'single page that is branded for legitimacy, customizable per industry, and '
                              'synced back to NetSuite as the source of truth. Vendors drop off when '
                              'forced through multiple click-through steps [1wlmLTmDAfc @ 00:11:21]. '
                              'Underneath all of it is trust in the record. After consolidating vendors '
                              'across 30 legal entities, AVC-Licensing reports that the AP team could '
                              'finally trust and navigate its vendor data [8S2AXmoUSJY @ 00:03:00].'],
               'table': {'caption': 'Where the Practitioners Agree on Vendor Onboarding and Procure-to-Pay',
                         'headers': ['Consensus Point', 'Practitioner Position', 'Expert Source'],
                         'rows': [['Onboarding is a pre-contract risk mitigation play',
                                   'Surface every present and future vendor issue before signing, after '
                                   'fraudulent vendors cost Google and Facebook over a hundred million '
                                   'dollars',
                                   'Gatekeeper Vendor & Contract Lifecycle Management ([-L_45dSkyaE @ '
                                   '00:01:20])'],
                                  ['Vendor record errors compound through invoices, payments and accruals',
                                   'A fat-fingered account number returns the ACH payment, delays '
                                   'settlement and complicates month-end accrual reconciliation',
                                   'Charted (formerly SquareWorks) ([1wlmLTmDAfc @ 00:07:23])'],
                                  ['Emailed Excel or PDF intake creates endless chase threads',
                                   'Attached onboarding forms turn into long threads of reminders, '
                                   'follow-ups and missing documents from disorganized suppliers',
                                   'PROKURIA ([_tfz6kZ8JZo @ 00:00:42])'],
                                  ['Onboarding time is the dominant operator pain point',
                                   'In a live webinar poll, 36 percent named onboarding time, 26 percent '
                                   'engagement, 18 percent verification, 15 percent identification',
                                   'LeadSquared ([mR8B4VcLNjU @ 00:19:47])'],
                                  ['Ask only questions whose answers you will act on',
                                   'Strip throwaway questions, automate financial and cyber health checks, '
                                   'and keep the onboarding flow as lean as possible',
                                   'Gatekeeper Vendor & Contract Lifecycle Management ([-L_45dSkyaE @ '
                                   '00:06:02])'],
                                  ['Segment suppliers instead of applying uniform scrutiny everywhere',
                                   'Not every vendor needs the same level of scrutiny; centralize data and '
                                   'automate revalidations on one platform',
                                   'PROKURIA ([_R1e9FCXKyI @ 00:04:15])'],
                                  ['A shared, trusted vendor master is the real control',
                                   'Each legal entity keeps its own vendor record while shared fields stay '
                                   'identical across all thirty companies',
                                   'AVC-Licensing ([8S2AXmoUSJY @ 00:02:02])']]}},
              {'title': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The core procure-to-pay chain runs the same way in every ERP shown: '
                              "purchase order, receipt, bill, payment. SuperTraining's NetSuite "
                              'walkthrough goes to Transactions, Purchases, Enter Purchase Orders, then '
                              'picks the vendor and the receiving location. The PO sublist splits into '
                              'Expense lines and Item lines. Expense lines take a flat amount, such as '
                              '$500 of marketing supplies. Item lines carry exact quantities of inventory '
                              'that will be resold. Saving the PO unlocks Receive, then Bill, which has an '
                              'approval status field for supervisor sign-off, then Make Payment by check '
                              "[EgxNMaMzml0 @ 00:01:10]. NetSuite's own Advanced Procurement demo adds "
                              'four tools for the purchasing manager role: - blanket purchase orders on '
                              'auto-generated schedules; - employee requisitions that agents group into '
                              'one PO per vendor; - requests for quotes; - purchase contracts with start '
                              'and end dates and minimum and maximum contracted amounts [5hYAlGkuizk @ '
                              '00:00:15]. Jules Holtzman of Bridgepoint Consulting runs the RFQ live. The '
                              'advice is to keep bid open and close dates strict for quick turnaround and '
                              'to set effectivity by order date or expected receipt date. Vendors respond '
                              'through the Vendor Center and can even propose their own payment terms '
                              "[KL4guXcGWDU @ 00:00:30]. For leaner shops, James and Jenna's Zoho "
                              'Procurement review puts the Premium plan at around $35 per user per month '
                              'and Enterprise at around $75. Both use requester, approver, purchaser and '
                              'admin roles [gkHpTkP_2Zg @ 00:02:04].',
                              'On vendor intake, the street mechanic is to replace the attachment with a '
                              "validated digital form that writes straight into the ERP. Marlin's Charted "
                              'AVO is a SuiteApp that lives inside NetSuite. Templates are built in the '
                              'Advanced Form Builder, and each field maps to a standard or custom NetSuite '
                              'vendor field. A W-9 upload is collected by default, and vendors can choose '
                              'check or ACH, with basic routing-number validation. The form goes out '
                              "through a private encrypted link that only the vendor's email client can "
                              'open. Returned changes show red for changed and green for unchanged before '
                              "AP applies them [1wlmLTmDAfc @ 00:15:22]. PROKURIA's no-code form restricts "
                              'free-text fields to predefined options, such as three company types. It '
                              'replaces usernames with a one-time password and routes each submission to '
                              "two assigned approvers [_tfz6kZ8JZo @ 00:01:16]. Peakflo's portal validates "
                              'GSTIN, PAN and MSME numbers, but only for Indian entities. It flags bank '
                              'verification with green or red tags, OTP-verifies contacts, and highlights '
                              'vendor edits in yellow and newly added data in blue [Y400sNeYMUw @ '
                              "00:02:00]. Agreement Automation Lab's NetSuite plus Docusign flow fills the "
                              'supplier agreement from the vendor record. The supplier contact adds only '
                              'the legal name, federal tax ID, entity type and founding year, and those '
                              'details write back to NetSuite with nobody retyping them [A91pl3huL6s @ '
                              '00:01:10].',
                              'Downstream, the practitioners push error-catching onto the supplier and '
                              "negotiate cash terms deliberately. Mike's SAP Business Network demo shows "
                              'suppliers performing a PO flip, which copies every purchase order detail '
                              'onto the invoice. The invoice then runs against 120-plus business rules '
                              'that can block submission if quantities or values were changed, even when '
                              'the total is unaffected. Bad invoices die at source, and supplier calls to '
                              'AP drop because invoice status is visible on the network [xPYn_cF6f1E @ '
                              '00:00:58]. On terms, 10 Min For Supply Chain lays out a ladder for a buyer '
                              'spending $50,000 a month under 100 percent upfront. First, move to 30 '
                              'percent upfront and 70 percent before shipment for a few orders. Then go to '
                              'Net 30, then Net 60. The levers are predictable volume, credit and trade '
                              'references, and consolidated orders. At steady state, the ladder is worth '
                              'roughly $100,000 of supplier financing [vdxHe8A6Tkk @ 00:00:56]. The deal '
                              'closes in writing, with the payment trigger, credit limit, invoice '
                              'requirements and late-payment consequences spelled out. For multi-entity '
                              'groups, AVC-Licensing ran five full rehearsals on copies of production and '
                              'cut over in about four hours during a planned weekend, with point-in-time '
                              'restore as the fallback. Afterwards, AP had to search one list by name, tax '
                              'ID, email or phone before creating any vendor [8S2AXmoUSJY @ 00:01:42].'],
               'table': {'caption': 'Procure-to-Pay and Onboarding Tools, Settings and Numbers Taught by '
                                    'Practitioners',
                         'headers': ['Tool / Mechanic',
                                     'Exact Setting or Number',
                                     'Operator Use',
                                     'Expert Source'],
                         'rows': [['SAP Business Network PO flip with invoice rules',
                                   '120-plus business rules check every invoice before accounts payable',
                                   'Blocks altered quantities or values even when the invoice total is '
                                   'unchanged',
                                   'Spend And Procurement with Mike ([xPYn_cF6f1E @ 00:00:58])'],
                                  ['Supplier payment term ladder from upfront terms',
                                   '30 percent upfront, 70 percent before shipment, then Net 30, then Net '
                                   '60',
                                   'Earn longer credit on $50,000 monthly spend through proven on-time '
                                   'payment history',
                                   '10 Min For Supply Chain ([vdxHe8A6Tkk @ 00:00:56])'],
                                  ['Charted AVO automated vendor follow-up scheduler',
                                   'Reminder emails scheduled every seven days or every three days',
                                   'Chase critical missing vendor information without manual email threads '
                                   'clogging inboxes',
                                   'Charted (formerly SquareWorks) ([1wlmLTmDAfc @ 00:27:12])'],
                                  ['Zoho Procurement subscription pricing tiers',
                                   'Premium around $35 and Enterprise around $75 per user per month',
                                   'Run purchase requests, approvals, purchase orders, bills, payments and '
                                   'budgets in one place',
                                   "James And Jenna's Tutorials ([gkHpTkP_2Zg @ 00:02:04])"],
                                  ['NetSuite purchase contracts from awarded RFQ bids',
                                   'Start and end dates, minimum and maximum contracted amounts, quantity '
                                   'pricing levels',
                                   'Convert winning RFQ bids into contracts applied to eligible purchase '
                                   'order lines',
                                   'NetSuite ([5hYAlGkuizk @ 00:03:23])'],
                                  ['D365 cross-entity vendor master consolidation project',
                                   'About 8,000 records, 30 entities, about 6,800 masters, four-hour '
                                   'cutover',
                                   'Rehearse five full times on production copies until zero known '
                                   'exceptions remain',
                                   'AVC-Licensing ([8S2AXmoUSJY @ 00:00:42])'],
                                  ['Peakflo vendor tax registration validation checks',
                                   'GSTIN, PAN and MSME validation available only for Indian entities',
                                   'Auto-verify tax registrations; a green tick confirms valid '
                                   'vendor-entered data',
                                   'Peakflo ([Y400sNeYMUw @ 00:02:17])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Speed Moves the Operators Actually Use',
                           'body': 'Small process choices compress time-to-contract and time-to-pay more '
                                   'than any single tool. These are the moves the practitioners call out '
                                   'by name.',
                           'items': ['Keep RFQ bid open and close dates strict to force quick vendor '
                                     'turnaround. You can always extend the close date or add more vendors '
                                     'to the RFQ later [Bridgepoint Consulting — KL4guXcGWDU @ 00:00:30].',
                                     'Have legal start negotiating contract terms while vendor checks are '
                                     'still running. If the checks fail, the review time is wasted, but '
                                     'done in parallel the two tracks massively speed up time-to-contract '
                                     '[Gatekeeper Vendor & Contract Lifecycle Management — -L_45dSkyaE @ '
                                     '00:03:02].',
                                     'Cut field KYC turnaround by capturing details progressively across '
                                     'meetings and running OCR on document snaps. The OCR auto-extracts '
                                     'name, phone and email and flags unclear images [LeadSquared — '
                                     'mR8B4VcLNjU @ 00:50:02].',
                                     'Before accepting Net 60, check whether the supplier raised prices or '
                                     'removed discounts in exchange. Recalculate whether the cash-flow '
                                     'benefit still beats the higher total cost [10 Min For Supply Chain — '
                                     'vdxHe8A6Tkk @ 00:02:42].']},
               'sop_steps': [{'step': 1,
                              'title': 'Screen Before You Sign',
                              'action': 'Run pre-qualification: sanctions screening, credit checks, '
                                        'initial ESG checks, and tech-rated financial and cyber health.',
                              'detail': 'PROKURIA puts sanctions-list screening, credit checks and initial '
                                        'ESG checks at step one of its six-step blueprint, to weed out '
                                        "problems early [PROKURIA — _R1e9FCXKyI @ 00:02:44]. Gatekeeper's "
                                        'seven activities add due diligence questionnaires, tech-rated '
                                        'financial and cyber health, a risk register, price finalization '
                                        'and an NDA [Gatekeeper Vendor & Contract Lifecycle Management — '
                                        '-L_45dSkyaE @ 00:02:02].'},
                             {'step': 2,
                              'title': 'Send a Validated Digital Intake Form',
                              'action': 'Create a lightweight vendor record with an email and subsidiary, '
                                        'then send a branded form through a secure link.',
                              'detail': 'In Charted AVO, a new vendor needs only an email address and a '
                                        'subsidiary before the template goes out. The private encrypted '
                                        'link can only be opened by the email client tied to that address '
                                        '[Charted (formerly SquareWorks) — 1wlmLTmDAfc @ 00:18:17]. '
                                        'Alternatively, a Docusign agreement prefilled from NetSuite '
                                        'collects the legal name and tax ID at signature [Agreement '
                                        'Automation Lab — A91pl3huL6s @ 00:00:24].'},
                             {'step': 3,
                              'title': 'Verify Bank and Tax Data, Then Apply Changes',
                              'action': 'Check the bank and tax verification tags and accept or decline '
                                        'each vendor change before it touches the master.',
                              'detail': 'Peakflo shows a green tag when bank account verification succeeds '
                                        'and a red tag when it fails. AP accepts or declines, and the '
                                        'vendor is notified automatically so they can resubmit [Peakflo — '
                                        'Y400sNeYMUw @ 00:05:10]. Before creating any vendor, '
                                        'AVC-Licensing has AP search the shared list by name, tax ID, '
                                        'email or phone [AVC-Licensing — 8S2AXmoUSJY @ 00:02:21].'},
                             {'step': 4,
                              'title': 'Run the First Transaction End to End',
                              'action': 'Push a first order through PO, receipt, bill and payment, with '
                                        'invoice rules catching supplier errors at source.',
                              'detail': 'SuperTraining generates the receipt from the PO, bills against '
                                        'the vendor invoice, and records the check payment without '
                                        "re-keying data [SuperTraining — EgxNMaMzml0 @ 00:03:11]. SAP's PO "
                                        'flip and 120-plus rules make the supplier fix bad invoices before '
                                        'submission [Spend And Procurement with Mike — xPYn_cF6f1E @ '
                                        '00:01:38].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over how the supplier gets in the door. Peakflo runs '
                              'the credentialed model: the vendor receives an invitation email plus a '
                              'second email with login credentials, lands on a dashboard tagged pending '
                              'verification, then works through info, address, bank and contact tabs '
                              "before hitting send to customer [Y400sNeYMUw @ 00:00:17]. Charted's Marlin "
                              'attacks that model head-on, saying vendors do not love managing credential '
                              'information, get locked out, forget passwords, and that a vendor paid by '
                              'hundreds or thousands of companies faces an impossible exercise juggling a '
                              'thousand logins [1wlmLTmDAfc @ 00:06:04]. Their replacement is a private '
                              "encrypted link pulled from the vendor record's email address that cannot be "
                              'shared with anyone else, pitched as the sweet spot between a heavy portal '
                              "and an informal spreadsheet. PROKURIA's Alex lands in the same middle "
                              'ground on a different build: no username or password, just an email the '
                              'vendor manager adds to the system and a one-time code the supplier '
                              'retrieves from their inbox [_tfz6kZ8JZo @ 00:02:07]. SAP Ariba flips the '
                              'problem entirely with one network login where the supplier sees RFPs, '
                              'questionnaires, contracts, opportunities and orders for every connected '
                              'customer, with hundreds of Ariba employees on hand to connect them '
                              '[xPYn_cF6f1E @ 00:00:19].',
                              "Form depth is the second fault line. LeadSquared's Shivam demos a six-tab "
                              'vendor onboarding form covering company details, eligibility, agreement, '
                              'bank details and certification, plus dynamic forms that swap the entire '
                              'field set depending on whether the field agent is signing an electronics '
                              "vendor or an office-products vendor [mR8B4VcLNjU @ 00:29:00]. Charted's "
                              'Marlin wants the opposite: a single page, little dynamic-form complexity '
                              'and few steps to click through, because that is where vendors drop off and '
                              'just do not want to deal with it [1wlmLTmDAfc @ 00:11:21]. Gatekeeper '
                              'applies a ruthless filter: only ask a question if you will take the answer '
                              'and do something with it, strip every question asked for the sake of it, '
                              'and let automated tools such as Market IQ check financial and cyber health '
                              "so the vendor is never asked [-L_45dSkyaE @ 00:06:02]. LeadSquared's Ashish "
                              'counters for field-led onboarding: capture basic information in the first '
                              'meeting and the rest progressively, then let an OCR integration pull names, '
                              'numbers and IDs from a single snap of each KYC document [mR8B4VcLNjU @ '
                              '00:50:02]. Both camps still insist on configurability, with Charted letting '
                              'admins add required or optional fields mapped to NetSuite custom fields and '
                              'LeadSquared configuring every tab per vendor type.',
                              'Sequencing splits the room too. Gatekeeper lists seven onboarding '
                              'activities, with price finalization sixth and the NDA seventh, admitting '
                              'some people will not want the NDA step; the bonus tip is to have legal '
                              'start negotiating contract terms while checks are still running, accepting '
                              'that a failed check wastes all that review time in exchange for massively '
                              'speeding up time to contract [-L_45dSkyaE @ 00:03:02]. PROKURIA keeps it '
                              'linear, placing approval and contract alignment fifth, after '
                              'pre-qualification, document collection, data verification and system '
                              "registration, with internal sign-offs checking that the T's and C's match "
                              'the paperwork [_R1e9FCXKyI @ 00:03:34]. Payment terms show the same '
                              'tension. 10 Min For Supply Chain treats terms as something the buyer earns '
                              'in phases: for a supplier demanding 100% upfront, propose 30% upfront and '
                              '70% before shipment, move to net 30 after a reliable payment history, and '
                              'request net 60 only after consistent volumes and on-time payments, giving '
                              'the supplier evidence that extending credit is a manageable risk '
                              "[vdxHe8A6Tkk @ 00:00:56]. Bridgepoint's Jules Holtzman shows the reverse "
                              "flow inside NetSuite's request for quote, where the responding vendor can "
                              'change the payment terms they want for the contract they are bidding on, so '
                              'the supplier opens the terms conversation [KL4guXcGWDU @ 00:02:25].'],
               'table': {'caption': 'Competing playbooks for vendor access, data capture, contracting, '
                                    'terms and invoice control',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How the supplier logs in to onboard',
                                   'Credentialed vendor portal with invitation email, separate login '
                                   'credentials and tabbed self-service submission',
                                   'Credential-free private encrypted link or one-time passcode tied to '
                                   'the vendor email address',
                                   'Peakflo ([Y400sNeYMUw @ 00:00:17]); Charted (formerly SquareWorks) '
                                   '([1wlmLTmDAfc @ 00:18:17])'],
                                  ['How deep the onboarding form should go',
                                   'LeadSquared six-tab multi-step form with dynamic fields switching by '
                                   'vendor type',
                                   'Charted single-page form because multi-step click-throughs drive '
                                   'vendor drop-off',
                                   'LeadSquared ([mR8B4VcLNjU @ 00:29:00]); Charted (formerly SquareWorks) '
                                   '([1wlmLTmDAfc @ 00:11:21])'],
                                  ['How many questions to ask the vendor',
                                   'Strip any question whose answer you will not act on and automate '
                                   'financial and cyber checks',
                                   'Collect progressively across field meetings and let OCR read each KYC '
                                   'document snap',
                                   'Gatekeeper Vendor & Contract Lifecycle Management ([-L_45dSkyaE @ '
                                   '00:06:02]); LeadSquared ([mR8B4VcLNjU @ 00:50:02])'],
                                  ['When contract negotiation starts',
                                   'Negotiate contract terms in parallel with vendor checks to massively '
                                   'speed up time to contract',
                                   'Align contract and internal sign-offs only after verification and '
                                   'system registration are complete',
                                   'Gatekeeper Vendor & Contract Lifecycle Management ([-L_45dSkyaE @ '
                                   '00:03:02]); PROKURIA ([_R1e9FCXKyI @ 00:03:34])'],
                                  ['Who sets the payment terms',
                                   'Buyer earns terms in phases from a 30/70 split to net 30 then net 60',
                                   'Vendor enters its own preferred payment terms inside the NetSuite RFQ '
                                   'bid response',
                                   '10 Min For Supply Chain ([vdxHe8A6Tkk @ 00:00:56]); Bridgepoint '
                                   'Consulting ([KL4guXcGWDU @ 00:02:25])'],
                                  ['How hard the invoice gets policed',
                                   'SAP Ariba 120-plus business rules block a PO-flip invoice with changed '
                                   'quantities or values',
                                   'NetSuite walkthrough marks the bill approved and skips the approval '
                                   'step entirely',
                                   'Spend And Procurement with Mike ([xPYn_cF6f1E @ 00:00:58]); '
                                   'SuperTraining ([EgxNMaMzml0 @ 00:03:46])'],
                                  ['How vendor data lands in the ERP',
                                   'Docusign workflow writes the signed legal name and tax ID back to '
                                   'NetSuite with zero retyping',
                                   'Reviewer sees red and green field changes and accepts or denies before '
                                   'applying to the record',
                                   'Agreement Automation Lab ([A91pl3huL6s @ 00:02:05]); Charted (formerly '
                                   'SquareWorks) ([1wlmLTmDAfc @ 00:20:19])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['Gatekeeper opens with the headline loss: both Google and Facebook paid over '
                              'a hundred million dollars to fraudulent vendors, which the speaker pins on '
                              'one simple truth, that those vendors were never properly onboarded '
                              "[-L_45dSkyaE @ 00:00:00]. Charted's Marlin traces the cheaper, more "
                              'frequent version of the same failure: informal Excel or CSV vendor updates '
                              'are prone to potential fraud, carry incorrect formatting and lack '
                              'validation, and a vendor who fat-fingers one extra digit into an ACH '
                              'account number triggers a returned payment and a delayed payment, while a '
                              'wrong address sends the check to the wrong place and the error ripples into '
                              'three-way match, month-end reconciliation and accruals until it delays the '
                              'close [1wlmLTmDAfc @ 00:07:23]. PROKURIA names the blind spots underneath: '
                              'fragmented data, suppliers asked for the same thing over and over, '
                              'spreadsheet-and-email workflows that are slow and error-prone, expired '
                              'insurance nobody catches, and vendor data stuck in one place while the ERP '
                              "sits somewhere else [_R1e9FCXKyI @ 00:02:17]. Peakflo's counter is "
                              'verification at entry, showing a green tick when tax and bank details '
                              'validate and a red tag when bank account verification fails so the vendor '
                              'must re-enter, but it warns that its GSTIN, PAN and MSME validation is only '
                              'available for entities in India [Y400sNeYMUw @ 00:02:17].',
                              "AVC-Licensing's D365 consolidation is the most candid failure ledger any "
                              'speaker offers. Across 30 legal entities, nearly 8,000 vendor records '
                              'mapped to about 6,800 master accounts, and the trap was not duplicates but '
                              'duplicates that disagreed: a survivor record on hold, a retired record '
                              'holding a tax ID the survivor lacked, two records of one supplier paying '
                              'into different bank accounts, and legitimate differences such as default '
                              'ledger accounts that had to stay local [8S2AXmoUSJY @ 00:01:03]. The team '
                              'ran five full rehearsals on a copy of production, cut over in about 4 hours '
                              'inside a planned weekend window with a point-in-time restore as fallback, '
                              'and still found Fabric and Power BI reports pointing at old vendor '
                              'references, fixed at the source and resynced in about a day; they refuse to '
                              "claim an ROI they never measured [8S2AXmoUSJY @ 00:02:41]. LeadSquared's "
                              'Ashish describes the no-system version of the mess: details on Excel or '
                              'paper in the field, verbal commitments nobody records, documents nobody can '
                              'find, security concerns, falling productivity and, ultimately, onboarding '
                              'the wrong set of vendors [mR8B4VcLNjU @ 00:14:28]. When Shivani polled the '
                              'webinar audience, 36% named onboarding time as their top challenge, the '
                              'stage where the most time goes [mR8B4VcLNjU @ 00:19:28].',
                              'The economics traps sit on both sides of the table. 10 Min For Supply Chain '
                              'runs the working-capital math on $50,000 of monthly purchases: moving from '
                              'upfront payment to net 60 is worth roughly $100,000 of supplier financing '
                              'under a simplified steady-state assumption, but only if the full monthly '
                              'purchases qualify and the payment cycle is established, with invoice '
                              'timing, shipment schedules and credit limits moving the real number '
                              '[vdxHe8A6Tkk @ 00:02:11]. The same speaker flags the two ways that gain '
                              'evaporates: a volume commitment that forces you to buy unnecessary '
                              'inventory, and a supplier who raises prices or removes discounts in '
                              'exchange for longer terms, so the total cost has to be recalculated; '
                              'jumping straight from upfront to net 60 with a supplier who has little '
                              'experience with your business is the named mistake [vdxHe8A6Tkk @ '
                              "00:02:42]. Finconvo Animation's interview guide adds the credibility check "
                              'every buyer gets tested on: explain the original quotation, the action '
                              'taken and the final result, and do not claim savings without supporting '
                              'figures [JEqCIJmR4Mg @ 00:04:46]. Gatekeeper prices in the relationship '
                              'cost: an onerous, rigid, frustrating onboarding upsets the vendor and '
                              'creates friction and tension up front, so the process should stay as lean '
                              'as possible [-L_45dSkyaE @ 00:05:24].'],
               'table': {'caption': 'Firsthand failure modes and the economics check each practitioner '
                                    'applied',
                         'headers': ['Failure Mode', 'What Happened', 'Economics Check', 'Expert Source'],
                         'rows': [['Vendors paid without proper onboarding',
                                   'Google and Facebook paid over a hundred million dollars to fraudulent '
                                   'vendors',
                                   'Run due diligence plus financial and cyber health scoring before '
                                   'signing the contract',
                                   'Gatekeeper Vendor & Contract Lifecycle Management ([-L_45dSkyaE @ '
                                   '00:00:00])'],
                                  ['Fat-fingered ACH bank details',
                                   'One extra digit in the account number returns the payment and delays '
                                   'it',
                                   'Validate routing and account format at capture and review changes '
                                   'before applying them',
                                   'Charted (formerly SquareWorks) ([1wlmLTmDAfc @ 00:07:23])'],
                                  ['Duplicate vendor records that disagree',
                                   'Survivor on hold, retired record held the tax ID, two bank accounts '
                                   'for one supplier',
                                   'Five full rehearsals on a production copy reached zero known '
                                   'exceptions before cutover',
                                   'AVC-Licensing ([8S2AXmoUSJY @ 00:01:03]); AVC-Licensing ([8S2AXmoUSJY '
                                   '@ 00:02:02])'],
                                  ['Hidden downstream report dependency',
                                   'Fabric and Power BI reports kept showing old vendor references after '
                                   'consolidation',
                                   'Fixed at the source and resynced in about a day with no ROI claimed',
                                   'AVC-Licensing ([8S2AXmoUSJY @ 00:02:41])'],
                                  ['Longer terms that cost more than they save',
                                   'Supplier raises prices or removes discounts in exchange for longer '
                                   'payment terms',
                                   '$50,000 monthly at net 60 equals about $100,000 financing only if '
                                   'purchases fully qualify',
                                   '10 Min For Supply Chain ([vdxHe8A6Tkk @ 00:02:42]); 10 Min For Supply '
                                   'Chain ([vdxHe8A6Tkk @ 00:02:11])'],
                                  ['Onboarding run through email attachments',
                                   'Emailed form turns into a long thread of reminders, follow-ups and '
                                   'missing documents',
                                   'Zoomcar cut its onboarding cycle from 20 days to 5 to 10 hours on a '
                                   'system',
                                   'PROKURIA ([_tfz6kZ8JZo @ 00:00:42]); LeadSquared ([mR8B4VcLNjU @ '
                                   '00:44:41])'],
                                  ['Validation coverage gaps by country',
                                   'GSTIN, PAN and MSME validation only works for entities based in India',
                                   'Bank account verification failures show a red tag and force vendor '
                                   're-entry',
                                   'Peakflo ([Y400sNeYMUw @ 00:02:17]); Peakflo ([Y400sNeYMUw @ '
                                   '00:05:10])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four stops before a vendor gets paid or a master gets merged',
                           'body': 'Each stop below is lifted from a loss, reversal or bottleneck a '
                                   'practitioner reported firsthand. Clear all four before releasing '
                                   'payment, extending terms or cutting over a vendor master.',
                           'items': ['Do not jump straight from upfront payment to net 60 with a supplier '
                                     'that has little experience working with your business; earn the '
                                     'terms in phases and price any discount removal against the cash '
                                     'benefit [10 Min For Supply Chain — vdxHe8A6Tkk @ 00:02:56].',
                                     'Hold ACH payment release until the routing and account numbers pass '
                                     'validation and the submitted changes are reviewed, because one '
                                     'fat-fingered digit returns the payment and delays it [Charted '
                                     '(formerly SquareWorks) — 1wlmLTmDAfc @ 00:07:23].',
                                     'Before consolidating vendor masters, rehearse on a copy of '
                                     'production until execution starts with zero known exceptions, and '
                                     'keep a point-in-time restore as the fallback [AVC-Licensing — '
                                     '8S2AXmoUSJY @ 00:02:21].',
                                     'Automate reminders for expiring insurance, tax and compliance '
                                     'documents so expired coverage never becomes a compliance blind spot '
                                     '[PROKURIA — _R1e9FCXKyI @ 00:03:00].']}}],
 'pull_quote': '"Deduplication counts rows. A vendor master is a control the business relies on." — '
               'AVC-Licensing (8S2AXmoUSJY @ 00:03:00).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Pre-qualify every new supplier before onboarding starts by screening against '
                      'sanctions lists, running credit checks and doing initial ESG checks [PROKURIA — '
                      '_R1e9FCXKyI @ 00:02:44].',
                      'Replace the Excel or PDF onboarding form with a structured online form that '
                      'restricts fields such as company type to predefined options and embeds a document '
                      'upload subgrid [PROKURIA — _tfz6kZ8JZo @ 00:01:16].',
                      "Verify the vendor's mobile number with an OTP so the onboarding form only submits "
                      'once the number is confirmed genuine [LeadSquared — mR8B4VcLNjU @ 00:30:34].',
                      'Schedule automated follow-ups every seven or three days for required vendor '
                      'information so requests do not get lost in the inbox [Charted (formerly '
                      'SquareWorks) — 1wlmLTmDAfc @ 00:27:12].',
                      'Before creating any vendor, search one shared list by name, tax ID, email or phone '
                      'to stop new duplicates at the source [AVC-Licensing — 8S2AXmoUSJY @ 00:02:21].',
                      'Put negotiated payment terms in writing, confirming the payment trigger, credit '
                      'limit, invoice requirements, due date and consequences of late payment [10 Min For '
                      'Supply Chain — vdxHe8A6Tkk @ 00:02:42].'],
 'statutory_citations': [{'title': 'AVC-Licensing — One Vendor Master Across 30 D365 Legal Entities: The '
                                   'Win Was Trust (Case Study) [00:01:03]',
                          'url': 'https://www.youtube.com/watch?v=8S2AXmoUSJY&t=63s',
                          'relevance': 'Primary practitioner testimony on consolidating disagreeing '
                                       'duplicate vendor records across 30 legal entities, rehearsals and '
                                       'cutover fallout.'},
                         {'title': 'Charted (formerly SquareWorks) — The modern way to work with vendors '
                                   'in NetSuite: Faster onboarding, smoother invoices [00:07:23]',
                          'url': 'https://www.youtube.com/watch?v=1wlmLTmDAfc&t=443s',
                          'relevance': 'Primary practitioner testimony on how bad onboarding data causes '
                                       'returned ACH payments and ripples into matching, reconciliation '
                                       'and accruals.'},
                         {'title': 'Gatekeeper Vendor & Contract Lifecycle Management — What is Vendor '
                                   'Onboarding? [00:00:00]',
                          'url': 'https://www.youtube.com/watch?v=-L_45dSkyaE&t=0s',
                          'relevance': 'Primary practitioner testimony on vendor fraud losses, the seven '
                                       'onboarding activities and keeping onboarding lean.'},
                         {'title': '10 Min For Supply Chain — How to Negotiate Supplier Payment Terms | '
                                   'Upfront to Net 60 Explained [00:02:11]',
                          'url': 'https://www.youtube.com/watch?v=vdxHe8A6Tkk&t=131s',
                          'relevance': 'Primary practitioner testimony on phased payment-term negotiation '
                                       'and the working-capital math of moving to net 60.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'vdxHe8A6Tkk',
                       'title': 'How to Negotiate Supplier Payment Terms | Upfront to Net 60 Explained',
                       'channel': '10 Min For Supply Chain',
                       'author': '10 Min For Supply Chain',
                       'text': 'Using a simplified steady state assumption, $50,000 monthly purchases '
                               'times 2 months equals $100,000.',
                       'tip': 'Using a simplified steady state assumption, $50,000 monthly purchases times '
                              '2 months equals $100,000.',
                       'timestamp': 131,
                       'timestamp_seconds': 131,
                       'timestamp_label': '[00:02:11]',
                       'url': 'https://www.youtube.com/watch?v=vdxHe8A6Tkk&t=131s',
                       'markdown': '[00:02:11](https://www.youtube.com/watch?v=vdxHe8A6Tkk&t=131s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xPYn_cF6f1E',
                       'title': 'SAP Business Network for Procurement - Demo',
                       'channel': 'Spend And Procurement with Mike',
                       'author': 'Spend And Procurement with Mike',
                       'text': 'Through the 120 plus business rules that SAP Ariba offers, we can check '
                               'the invoice for errors before it hits accounts payable.',
                       'tip': 'Through the 120 plus business rules that SAP Ariba offers, we can check the '
                              'invoice for errors before it hits accounts payable.',
                       'timestamp': 58,
                       'timestamp_seconds': 58,
                       'timestamp_label': '[00:00:58]',
                       'url': 'https://www.youtube.com/watch?v=xPYn_cF6f1E&t=58s',
                       'markdown': '[00:00:58](https://www.youtube.com/watch?v=xPYn_cF6f1E&t=58s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_R1e9FCXKyI',
                       'title': 'Vendor Onboarding Made Simple: Supplier Compliance and Management Tools',
                       'channel': 'PROKURIA',
                       'author': 'PROKURIA',
                       'text': 'Structured programs slash third-party risks significantly and can cut '
                               'onboarding time by over a third.',
                       'tip': 'Structured programs slash third-party risks significantly and can cut '
                              'onboarding time by over a third.',
                       'timestamp': 93,
                       'timestamp_seconds': 93,
                       'timestamp_label': '[00:01:33]',
                       'url': 'https://www.youtube.com/watch?v=_R1e9FCXKyI&t=93s',
                       'markdown': '[00:01:33](https://www.youtube.com/watch?v=_R1e9FCXKyI&t=93s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'IpCHEJpOqrE',
                       'title': 'Purchasing and Payables in Business Central | Vendor, Orders, Invoices & '
                                'Payments Explained',
                       'channel': 'INFOC',
                       'author': 'INFOC',
                       'text': 'Vendor ledger entries give finance teams visibility into posted supplier '
                               'transactions, open balances, and due amounts.',
                       'tip': 'Vendor ledger entries give finance teams visibility into posted supplier '
                              'transactions, open balances, and due amounts.',
                       'timestamp': 196,
                       'timestamp_seconds': 196,
                       'timestamp_label': '[00:03:16]',
                       'url': 'https://www.youtube.com/watch?v=IpCHEJpOqrE&t=196s',
                       'markdown': '[00:03:16](https://www.youtube.com/watch?v=IpCHEJpOqrE&t=196s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-L_45dSkyaE',
                       'title': 'What is Vendor Onboarding?',
                       'channel': 'Gatekeeper Vendor & Contract Lifecycle Management',
                       'author': 'Gatekeeper Vendor & Contract Lifecycle Management',
                       'text': 'For any question you need to ask the vendor, you only want to ask that '
                               "question if you're going to take the data that you get from that question "
                               'and do something with it.',
                       'tip': 'For any question you need to ask the vendor, you only want to ask that '
                              "question if you're going to take the data that you get from that question "
                              'and do something with it.',
                       'timestamp': 362,
                       'timestamp_seconds': 362,
                       'timestamp_label': '[00:06:02]',
                       'url': 'https://www.youtube.com/watch?v=-L_45dSkyaE&t=362s',
                       'markdown': '[00:06:02](https://www.youtube.com/watch?v=-L_45dSkyaE&t=362s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-L_45dSkyaE',
                       'title': 'What is Vendor Onboarding?',
                       'channel': 'Gatekeeper Vendor & Contract Lifecycle Management',
                       'author': 'Gatekeeper Vendor & Contract Lifecycle Management',
                       'text': 'Both Google and Facebook have paid over a hundred million dollars to '
                               'fraudulent vendors.',
                       'tip': 'Both Google and Facebook have paid over a hundred million dollars to '
                              'fraudulent vendors.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=-L_45dSkyaE&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=-L_45dSkyaE&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EgxNMaMzml0',
                       'title': 'NetSuite Procure to Pay Example',
                       'channel': 'SuperTraining',
                       'author': 'SuperTraining',
                       'text': "We've received their invoice and we're going to generate a bill that "
                               'matches that invoice.',
                       'tip': "We've received their invoice and we're going to generate a bill that "
                              'matches that invoice.',
                       'timestamp': 191,
                       'timestamp_seconds': 191,
                       'timestamp_label': '[00:03:11]',
                       'url': 'https://www.youtube.com/watch?v=EgxNMaMzml0&t=191s',
                       'markdown': '[00:03:11](https://www.youtube.com/watch?v=EgxNMaMzml0&t=191s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5hYAlGkuizk',
                       'title': 'NetSuite Procurement',
                       'channel': 'NetSuite',
                       'author': 'NetSuite',
                       'text': 'The order requisition screen allows purchasing agents to view all approved '
                               'purchase requisitions, select the vendor, group these vendors and create '
                               'one purchase order to fulfill each of these requisitions.',
                       'tip': 'The order requisition screen allows purchasing agents to view all approved '
                              'purchase requisitions, select the vendor, group these vendors and create '
                              'one purchase order to fulfill each of these requisitions.',
                       'timestamp': 118,
                       'timestamp_seconds': 118,
                       'timestamp_label': '[00:01:58]',
                       'url': 'https://www.youtube.com/watch?v=5hYAlGkuizk&t=118s',
                       'markdown': '[00:01:58](https://www.youtube.com/watch?v=5hYAlGkuizk&t=118s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_tfz6kZ8JZo',
                       'title': 'Automate Supplier Onboarding | No-Code Procurement Tools',
                       'channel': 'PROKURIA',
                       'author': 'PROKURIA',
                       'text': 'For security, we use a one-time password system.',
                       'tip': 'For security, we use a one-time password system.',
                       'timestamp': 143,
                       'timestamp_seconds': 143,
                       'timestamp_label': '[00:02:23]',
                       'url': 'https://www.youtube.com/watch?v=_tfz6kZ8JZo&t=143s',
                       'markdown': '[00:02:23](https://www.youtube.com/watch?v=_tfz6kZ8JZo&t=143s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KL4guXcGWDU',
                       'title': 'NetSuite Procurement Module: Request for Quote Demo',
                       'channel': 'Bridgepoint Consulting',
                       'author': 'Bridgepoint Consulting',
                       'text': 'You can always go out and extend the bid closed date, but in order to get '
                               'some quick turnaround and responses it is good to keep these dates kind of '
                               'strict.',
                       'tip': 'You can always go out and extend the bid closed date, but in order to get '
                              'some quick turnaround and responses it is good to keep these dates kind of '
                              'strict.',
                       'timestamp': 30,
                       'timestamp_seconds': 30,
                       'timestamp_label': '[00:00:30]',
                       'url': 'https://www.youtube.com/watch?v=KL4guXcGWDU&t=30s',
                       'markdown': '[00:00:30](https://www.youtube.com/watch?v=KL4guXcGWDU&t=30s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mR8B4VcLNjU',
                       'title': 'Vendor Onboarding Process - What is Vendor Onboarding and How to Build an '
                                'Optimal Process?',
                       'channel': 'LeadSquared',
                       'author': 'LeadSquared',
                       'text': 'In terms of Zoomcar, they have reduced their overall cycle of onboarding '
                               'time from 20 days to 5 to 10 hours.',
                       'tip': 'In terms of Zoomcar, they have reduced their overall cycle of onboarding '
                              'time from 20 days to 5 to 10 hours.',
                       'timestamp': 2681,
                       'timestamp_seconds': 2681,
                       'timestamp_label': '[00:44:41]',
                       'url': 'https://www.youtube.com/watch?v=mR8B4VcLNjU&t=2681s',
                       'markdown': '[00:44:41](https://www.youtube.com/watch?v=mR8B4VcLNjU&t=2681s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8S2AXmoUSJY',
                       'title': 'One Vendor Master Across 30 D365 Legal Entities: The Win Was Trust (Case '
                                'Study)',
                       'channel': 'AVC-Licensing',
                       'author': 'AVC-Licensing',
                       'text': 'Deduplication counts rows. A vendor master is a control the business '
                               'relies on.',
                       'tip': 'Deduplication counts rows. A vendor master is a control the business relies '
                              'on.',
                       'timestamp': 180,
                       'timestamp_seconds': 180,
                       'timestamp_label': '[00:03:00]',
                       'url': 'https://www.youtube.com/watch?v=8S2AXmoUSJY&t=180s',
                       'markdown': '[00:03:00](https://www.youtube.com/watch?v=8S2AXmoUSJY&t=180s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8S2AXmoUSJY',
                       'title': 'One Vendor Master Across 30 D365 Legal Entities: The Win Was Trust (Case '
                                'Study)',
                       'channel': 'AVC-Licensing',
                       'author': 'AVC-Licensing',
                       'text': 'Duplicates were the visible part. The harder part was that duplicates '
                               'disagreed.',
                       'tip': 'Duplicates were the visible part. The harder part was that duplicates '
                              'disagreed.',
                       'timestamp': 63,
                       'timestamp_seconds': 63,
                       'timestamp_label': '[00:01:03]',
                       'url': 'https://www.youtube.com/watch?v=8S2AXmoUSJY&t=63s',
                       'markdown': '[00:01:03](https://www.youtube.com/watch?v=8S2AXmoUSJY&t=63s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gkHpTkP_2Zg',
                       'title': 'Zoho Procurement Demo, Tutorial & Review | Purchase Orders & Vendor '
                                'Management (2026)',
                       'channel': "James And Jenna's Tutorials",
                       'author': "James And Jenna's Tutorials",
                       'text': 'We have the premium plan which is going to cost around $35 per month per '
                               'user and the enterprise plan which is going to cost around $75 per user '
                               'per month.',
                       'tip': 'We have the premium plan which is going to cost around $35 per month per '
                              'user and the enterprise plan which is going to cost around $75 per user per '
                              'month.',
                       'timestamp': 124,
                       'timestamp_seconds': 124,
                       'timestamp_label': '[00:02:04]',
                       'url': 'https://www.youtube.com/watch?v=gkHpTkP_2Zg&t=124s',
                       'markdown': '[00:02:04](https://www.youtube.com/watch?v=gkHpTkP_2Zg&t=124s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1wlmLTmDAfc',
                       'title': 'The modern way to work with vendors in NetSuite: Faster onboarding, '
                                'smoother invoices',
                       'channel': 'Charted (formerly SquareWorks)',
                       'author': 'Charted (formerly SquareWorks)',
                       'text': "If you gather the wrong information, let's say they fat finger and add an "
                               'additional account number, then that payment gets returned and that '
                               'results in a delayed payment.',
                       'tip': "If you gather the wrong information, let's say they fat finger and add an "
                              'additional account number, then that payment gets returned and that results '
                              'in a delayed payment.',
                       'timestamp': 443,
                       'timestamp_seconds': 443,
                       'timestamp_label': '[00:07:23]',
                       'url': 'https://www.youtube.com/watch?v=1wlmLTmDAfc&t=443s',
                       'markdown': '[00:07:23](https://www.youtube.com/watch?v=1wlmLTmDAfc&t=443s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Y400sNeYMUw',
                       'title': 'Vendor Onboarding Management | Peakflo',
                       'channel': 'Peakflo',
                       'author': 'Peakflo',
                       'text': 'The GSTIN, PAN and MSME validation is only available for entities in '
                               'India.',
                       'tip': 'The GSTIN, PAN and MSME validation is only available for entities in India.',
                       'timestamp': 137,
                       'timestamp_seconds': 137,
                       'timestamp_label': '[00:02:17]',
                       'url': 'https://www.youtube.com/watch?v=Y400sNeYMUw&t=137s',
                       'markdown': '[00:02:17](https://www.youtube.com/watch?v=Y400sNeYMUw&t=137s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'A91pl3huL6s',
                       'title': 'Supplier Onboarding with Zero Retyping | NetSuite + Docusign',
                       'channel': 'Agreement Automation Lab',
                       'author': 'Agreement Automation Lab',
                       'text': 'The legal name and the tax ID are exactly what Marcus entered, and nobody '
                               'typed them in.',
                       'tip': 'The legal name and the tax ID are exactly what Marcus entered, and nobody '
                              'typed them in.',
                       'timestamp': 125,
                       'timestamp_seconds': 125,
                       'timestamp_label': '[00:02:05]',
                       'url': 'https://www.youtube.com/watch?v=A91pl3huL6s&t=125s',
                       'markdown': '[00:02:05](https://www.youtube.com/watch?v=A91pl3huL6s&t=125s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JEqCIJmR4Mg',
                       'title': 'Procurement & Vendor Manager Interview Questions and Answers',
                       'channel': 'Finconvo Animation',
                       'author': 'Finconvo Animation',
                       'text': 'Explain the original quotation, the action you took, and the final result. '
                               'Do not claim savings without supporting figures.',
                       'tip': 'Explain the original quotation, the action you took, and the final result. '
                              'Do not claim savings without supporting figures.',
                       'timestamp': 286,
                       'timestamp_seconds': 286,
                       'timestamp_label': '[00:04:46]',
                       'url': 'https://www.youtube.com/watch?v=JEqCIJmR4Mg&t=286s',
                       'markdown': '[00:04:46](https://www.youtube.com/watch?v=JEqCIJmR4Mg&t=286s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'}]}
