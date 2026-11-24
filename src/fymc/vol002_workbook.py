from __future__ import annotations

def build_volume_002_workbook() -> dict:
    return {'workbook_id': 'wb-002-surplus-funds-recovery',
 'volume_id': 'vol-002-surplus-funds-recovery',
 'title': 'Surplus Funds Recovery — Practitioner Testimony Operator Workbook',
 'subtitle': 'Surplus Funds Recovery: Find Tax-Sale Excess Proceeds, Verify Owners and Competing Debt, and '
             'Prepare Mortgage, Heir, and Estate Cases for Recovery',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Define Your Recovery Model and Qualify Your First Market',
                 'purpose': 'Build a practical starting plan that connects auction records, eligible '
                            'claimants, agreements, and claim processing. Separate apparent surplus from '
                            'verified availability, and distinguish contracted expectations from collected '
                            'fees before committing research time or outreach money.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Choose one county to investigate and describe its records and filing '
                                  'process before expanding into additional markets.',
                                  'Complete every field using a specific record, a clearly labeled '
                                  'planning assumption, or an unresolved question requiring verification.',
                                  'Keep auction proceeds, potential owner recovery, business fees, '
                                  'expenses, and collected cash in separate entries throughout your '
                                  'planning.',
                                  'Resolve identity, current availability, existing claims, and filing '
                                  'requirements before treating an owner agreement as a workable recovery.',
                                  'Finish with a written next action for every unresolved item; do not '
                                  'replace missing evidence with confidence or projected earnings.'],
                 'fields': [{'name': 'recovery_business_definition',
                             'type': 'textarea',
                             'prompt': 'Describe how auction proceeds become a potential recovery '
                                       'opportunity and explain your role in connecting records, the '
                                       'intended claimant, agreements, and filing. Separate this service '
                                       'from buying the property, and identify what the initial '
                                       'subtraction does not establish.',
                             'example': 'Overage Acquisition illustrates a $100,000 auction against '
                                        '$10,000 in back taxes, producing a $90,000 difference. My role is '
                                        'to investigate the records, locate the intended claimant, and '
                                        'move an appropriate claim forward. I will not label the entire '
                                        "difference an owner's confirmed payout or my business revenue. "
                                        '[Overage Acquisition — zed9ZTbgUfI @ 00:00:50]'},
                            {'name': 'accessible_county_selection',
                             'type': 'textarea',
                             'prompt': 'Name your initial county and explain how you will locate published '
                                       'sale results, claim instructions, and existing claim information. '
                                       'Record which parts you understand already and which remain '
                                       'unresolved before you spend money locating owners or preparing '
                                       'agreements.',
                             'example': 'I will start with a county where I can explain the results page, '
                                        'the claim filing route, and the existing claim lookup. A '
                                        'downloadable balance alone will not qualify the market. Any '
                                        'missing filing instruction stays on my research checklist before '
                                        'I purchase contact data or prepare outreach. [Money Making '
                                        'Juggernaut — _vsvjD8JvgU @ 00:02:11]'},
                            {'name': 'county_search_and_request',
                             'type': 'textarea',
                             'prompt': 'Write the exact search phrases you will try for your selected '
                                       'county, including alternative names for surplus records. Describe '
                                       'how you will distinguish an unsuccessful search from an '
                                       'unavailable list and what clarification you will request from '
                                       'county staff.',
                             'example': 'My search checklist includes the county name followed by surplus '
                                        'funds list, then the same county followed by excess proceeds '
                                        'list. I will save the relevant results and record which '
                                        'terminology the office actually uses. A failed first search means '
                                        'trying the alternative wording, not abandoning the county '
                                        'immediately. [Alfred Taren — 8-8koApqnYA @ 00:08:18]'},
                            {'name': 'list_age_and_available_balance',
                             'type': 'textarea',
                             'prompt': 'Record the list date, the date you checked the entry, and the '
                                       'evidence that money remains available. Explain how an old entry '
                                       'could survive after recovery and specify the unresolved status '
                                       'that would stop you from working the lead.',
                             'example': 'I will mark an undated list entry as unverified rather than '
                                        'current. Before researching contact details, I will check whether '
                                        'the owner or another recovery operator already claimed the '
                                        'balance. My working file must distinguish the amount printed on '
                                        'the list from the availability actually established during '
                                        'review. [SurplusFundsRiches — 4W8c0I28pxQ @ 00:18:26]'},
                            {'name': 'claimant_identity_match',
                             'type': 'textarea',
                             'prompt': 'Explain how you will establish that the person you contact and '
                                       'eventually sign is the intended claimant. Identify name '
                                       'similarities, generational suffixes, or conflicting ownership '
                                       'information that require additional review, and describe the '
                                       'evidence still needed before proceeding.',
                             'example': 'A matching surname and telephone response will not close my '
                                        'identity review. If the file could refer to senior while the '
                                        'person answering is junior, I will keep the agreement pending '
                                        'until the ownership record and intended claimant match. Diamond '
                                        'identifies mistaken claimant identity as a recurring team '
                                        "failure. [Bob Diamond - America's Tax Sale Attorney — 1Pp-cjYnY2k "
                                        '@ 00:06:19]'},
                            {'name': 'claim_instructions_and_identification',
                             'type': 'textarea',
                             'prompt': "List the county's stated requirements for originals, notarization, "
                                       'and claimant identification. Record what the claimant can '
                                       'currently provide, what remains missing, and the next practical '
                                       'step for each gap before you describe the file as ready for '
                                       'submission.',
                             'example': 'Identification availability belongs in my intake notes, not at '
                                        "the end of packet preparation. Anthony's case needed family "
                                        'assistance and DMV paperwork before submission because '
                                        'identification was missing. I will record that condition as an '
                                        'active dependency and keep the case separate from files whose '
                                        'submission requirements are already satisfied. [Money Making '
                                        'Juggernaut — gB8lD75eL5I @ 00:10:44]'},
                            {'name': 'research_and_mail_budget',
                             'type': 'textarea',
                             'prompt': 'Build a small research and mailing budget with separate entries '
                                       'for locating data, postage, envelopes, paper, and ink. Label '
                                       'practitioner prices as reported examples rather than guaranteed '
                                       'current costs, and keep campaign spending separate from any hoped '
                                       'for monthly deal income.',
                             'example': "The webinar student's reported mailing cost totals $0.85 per "
                                        'letter: $0.20 tracing, $0.58 postage, $0.05 envelope, and $0.01 '
                                        'each for paper and ink. Their 1,000 letter example therefore '
                                        'costs $850. I will use that as a comparison worksheet, not assume '
                                        'it guarantees a deal or a particular monthly income. [Money '
                                        'Making Juggernaut — vs2o6Zz48Oc @ 00:18:26]'},
                            {'name': 'pipeline_and_cash_separation',
                             'type': 'textarea',
                             'prompt': 'Define separate tracking categories for identified opportunities, '
                                       'signed agreements, expected fees, recovered funds, and collected '
                                       'business fees. Explain what evidence moves a file between '
                                       'categories and how you will prevent a promising contracted '
                                       'pipeline from being reported as spendable earnings.',
                             'example': "Matthew's eight contracted files and roughly $60,000 expected "
                                        'belong in a pipeline column, not a cash received column. My '
                                        'tracker will retain the agreement milestone while leaving '
                                        'collection unconfirmed. If a file stalls, the signed agreement '
                                        'remains a documented event without turning the anticipated fee '
                                        'into money already earned and received. [Nick Fullmer- Overage '
                                        'Syndicate — vd__NHmQYgM @ 00:03:28]'},
                            {'name': 'partner_net_allocation',
                             'type': 'textarea',
                             'prompt': 'Describe how you will separate the recovery check, owner '
                                       'allocation, attorney expense, and researcher compensation in a '
                                       'partnered file. Specify whether each percentage applies to gross '
                                       'recovery or net proceeds, and mark unsettled charges before '
                                       'calculating any projected partner payment.',
                             'example': "Bougie's researcher example uses 40% of net, with approximately "
                                        '$14,000 or more expected while final attorney charges remain '
                                        'unsettled. I will not multiply that percentage by the entire '
                                        'recovery check. My allocation sheet will show the recovery, owner '
                                        'allocation, expenses, and the remaining basis for the '
                                        "researcher's projected share separately. [SurplusFundsRiches — "
                                        'fzvvdAGwCBM @ 00:01:45]'},
                            {'name': 'weekly_file_management',
                             'type': 'textarea',
                             'prompt': 'Design a repeatable weekly file review that preserves prior calls, '
                                       'texts, letters, agreements, and unresolved tasks. Explain how a '
                                       'returned call will connect immediately to the correct history, and '
                                       'identify the next action that keeps each active case moving '
                                       'without overstating progress.',
                             'example': 'I will organize files into visible working sections and keep each '
                                        'contact attempt with its case. When someone returns a call, I '
                                        'should immediately see the earlier calls, texts, and letters '
                                        'rather than reconstruct the conversation. Matthew uses Evernote '
                                        'sections this way; my chosen system must preserve the same '
                                        'continuity. [Nick Fullmer- Overage Syndicate — vd__NHmQYgM @ '
                                        '00:14:56]'}],
                 'completion_gate': 'Complete all ten fields and select one county whose results, claim '
                                    'instructions, and claim lookup you can explain. Do not advance a '
                                    'candidate to agreement preparation while claimant identity, existing '
                                    'claims, available funds, or essential submission requirements remain '
                                    'unresolved. Keep every projected fee outside collected cash.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Build a Verified Lead File and Reconcile Competing Debt',
                 'purpose': 'Turn public lists and auction results into documented research files. Connect '
                            'each candidate to its parcel, sale, ownership, claim history, and competing '
                            'debt while preserving the difference between a preliminary spread and an '
                            'estimated remainder available for an owner claim.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Work through one candidate from its original list or auction record '
                                  'rather than combining unrelated facts into a single apparent case.',
                                  'Save the source location for every amount, case identifier, sale date, '
                                  'ownership record, and claim status you enter.',
                                  'Keep preliminary arithmetic visible, then record additional taxes, '
                                  'competing debts, and amounts already paid as separate research '
                                  'findings.',
                                  'Treat missing lien amounts, incomplete document review, and uncertain '
                                  'ownership as open tasks rather than assuming favorable answers.',
                                  'Finish by classifying the candidate as ready for further qualification, '
                                  'held for specific evidence, or excluded because the opportunity is '
                                  'unavailable.'],
                 'fields': [{'name': 'search_location_and_record_source',
                             'type': 'textarea',
                             'prompt': 'Document your county and state search, including whether adding '
                                       'PDF reveals a downloadable record. Record the actual source '
                                       'location and explain how you confirmed that a similarly named '
                                       'county did not lead you to the wrong jurisdiction or sale records.',
                             'example': 'I will search the county together with its state and add PDF when '
                                        'looking for a direct download. Each saved result will retain its '
                                        'source location so I can return to the original document. A '
                                        'convenient file name alone will not establish that I found the '
                                        "intended county's records. [Next Level VA — 2e4YGOesnUY @ "
                                        '00:15:20]'},
                            {'name': 'lead_spreadsheet_structure',
                             'type': 'textarea',
                             'prompt': 'Create the working entry for this lead with its case number, '
                                       'displayed amount, property address, and previous owner. Explain '
                                       'how these identifiers will remain connected as you add supporting '
                                       'documents, and identify any missing value that prevents reliable '
                                       'research.',
                             'example': 'My first spreadsheet row will preserve the case number, listed '
                                        "amount, property address, and previous owner's name together. If "
                                        'the address is missing, I will flag that gap instead of merging '
                                        'the entry with a similar name. The row becomes the reference '
                                        'point for subsequent ownership and claim research. [Overage '
                                        'Acquisition — Tv7CWg8qUb0 @ 00:03:38]'},
                            {'name': 'parcel_to_owner_connection',
                             'type': 'textarea',
                             'prompt': 'Record the parcel number and trace how it connects the sale entry '
                                       "to the property's address and former owner. Describe each "
                                       'unresolved mismatch, and state which original record you need '
                                       'before relying on a name discovered through a separate search.',
                             'example': 'I will begin with the parcel identifier from the sale record and '
                                        'use it to locate the address and ownership information. A name '
                                        'found elsewhere stays tentative until it connects to that '
                                        'property. The research file should show the connection rather '
                                        'than merely contain a plausible owner name and phone number. '
                                        '[Overage Acquisition — 6UiKunbtUa0 @ 00:04:54]'},
                            {'name': 'sold_status_and_bid_screen',
                             'type': 'textarea',
                             'prompt': 'Describe the sale status filter you used and compare the base bid '
                                       'with the highest bid for the candidate. Explain why that '
                                       'comparison selects a file for investigation rather than proving an '
                                       'owner payout, and retain the underlying auction result.',
                             'example': 'I will filter the auction results to sold entries and compare the '
                                        'base bid with the highest bid. A substantial difference earns '
                                        'further investigation, not a confirmed recovery label. I will '
                                        'retain the result page and carry the candidate forward for '
                                        'ownership, claim status, and competing debt research before '
                                        'outreach. [Tax Deed Surplus & Lien-Research Records — y94Ncg0WHn0 '
                                        '@ 00:01:30]'},
                            {'name': 'preliminary_proceeds_adjustment',
                             'type': 'textarea',
                             'prompt': 'Show the preliminary sale calculation and list additional taxes or '
                                       'other unresolved deductions separately. Identify which amounts are '
                                       'established and which still require research, then explain how a '
                                       'smaller remainder could change your decision to spend more time on '
                                       'this candidate.',
                             'example': "Mark's $17,933 entry is a preliminary sale minus minimum bid "
                                        'figure, not a final available balance. I will preserve that '
                                        'starting calculation while researching other taxes that could '
                                        'reduce it. Until those amounts are established, the candidate '
                                        'remains under review and its apparent size does not justify a '
                                        'promised owner recovery. [Texas FundFinding — 8UHfSY8oKfQ @ '
                                        '00:08:14]'},
                            {'name': 'existing_application_review',
                             'type': 'textarea',
                             'prompt': 'Record the current application or claim status and the record used '
                                       'to establish it. Explain how you will handle a large displayed '
                                       'balance when an application already exists, and distinguish an '
                                       'unchecked status from affirmative evidence that no claim has been '
                                       'filed.',
                             'example': "Richardson's $47,000 example is excluded because an application "
                                        'has already been filed, despite the attractive displayed amount. '
                                        'I will record both facts in my review. An empty claim status note '
                                        'means I have not checked; it does not mean the opportunity is '
                                        'open or ready for another owner agreement. [Money Making '
                                        'Juggernaut — ZU8-PRxVeCg @ 00:03:15]'},
                            {'name': 'complete_document_review',
                             'type': 'textarea',
                             'prompt': 'Describe the document collection you reviewed and how you checked '
                                       'for later correspondence, completed claims, and supporting '
                                       'material. Identify where your review ended, and explain why seeing '
                                       'blank claim forms alone does not establish that a case remains '
                                       'untouched or available.',
                             'example': 'For a Citrus file, I will continue scrolling after the blank '
                                        'forms because the same document can accumulate emails, letters, '
                                        'completed claims, and supporting records. My notes will identify '
                                        'what I actually reviewed. Stopping at an unused application page '
                                        'would leave the later claim history unresolved, even when the '
                                        'opening pages look routine. [Tax Deed Surplus & Lien-Research '
                                        'Records — bmmWj7_LTrw @ 00:03:09]'},
                            {'name': 'owner_name_lien_search',
                             'type': 'textarea',
                             'prompt': "Record the former owner's name used in lien research and describe "
                                       'how each resulting document connects to the asset under review. '
                                       'Identify possible name matches that remain unresolved, and explain '
                                       'why searching only the street address could leave your debt review '
                                       'incomplete.',
                             'example': "I will search recorded liens using the previous owner's name and "
                                        'then inspect the asset described in each document. A search '
                                        'result is not automatically a debt against this case. My notes '
                                        'will separate documents connected to the property from unresolved '
                                        'matches rather than treating an address search as the complete '
                                        'review. [Money Making Juggernaut — q95klfFm9mE @ 00:02:04]'},
                            {'name': 'missing_lien_balance_resolution',
                             'type': 'textarea',
                             'prompt': 'List every recorded lien whose current amount or outstanding '
                                       'status remains unknown. Write the question you will ask its '
                                       'recording entity, include the case number or property reference, '
                                       'and explain what decision must wait until the missing balance has '
                                       'been established.',
                             'example': 'My unresolved lien note will ask whether the lien remains '
                                        'outstanding and what amount is due. I will provide the case '
                                        'number or property address when contacting the recording entity. '
                                        'A renewal document without a balance does not let me calculate '
                                        'the owner remainder or classify the file as economically '
                                        'workable. [Nick Fullmer- Overage Syndicate — KOYBZFn2k7w @ '
                                        '00:03:47]'},
                            {'name': 'estimated_remainder_and_disposition',
                             'type': 'textarea',
                             'prompt': 'Reconcile the listed surplus with documented competing debts and '
                                       'calculate the current estimated remainder. State whether the file '
                                       'should proceed, remain on hold, or be excluded, and preserve any '
                                       'unresolved payoff or payment question instead of presenting your '
                                       'arithmetic as a guaranteed distribution.',
                             'example': "Taren's illustration starts with $180,000 and subtracts a $95,000 "
                                        'second mortgage, $8,000 HOA debt, and $22,000 judgment, leaving '
                                        '$55,000. I will show each deduction separately rather than call '
                                        "the original balance the owner's money. The remaining figure "
                                        'stays estimated while the actual file, payment history, and '
                                        'outstanding balances receive their necessary review. [Alfred '
                                        'Taren — SzfjJzM76ls @ 00:01:26]'}],
                 'completion_gate': 'Advance only when the sale record, parcel, former owner, and case '
                                    'identifier form one coherent file; current claim status has been '
                                    'checked; and competing debt has been investigated. Every unknown '
                                    'balance must have a specific follow-up task. Describe any remainder '
                                    'as estimated, not guaranteed, and exclude already claimed '
                                    'opportunities.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Route Mortgage Recoveries and Resolve Complex Claimant Authority',
                 'purpose': 'Identify the mortgage-sale records and money holder, distinguish distribution '
                            'requests from collected fees, and prepare difficult claimant files without '
                            'confusing contact with entitlement. Address company ownership, deceased '
                            'owners, estate authority, overseas communication, and changes that occur '
                            'before final documentation.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Identify whether the candidate involves a mortgage foreclosure, company '
                                  'owner, deceased owner, overseas claimant, or multiple overlapping '
                                  'complications.',
                                  'Use the actual sale and debt records to investigate proceeds; do not '
                                  'substitute an opening bid for the amount actually owed.',
                                  'Record the money holder, distribution evidence, ownership proof, and '
                                  'claimant authority as distinct parts of the file.',
                                  'Adapt communication and document delivery to the claimant while keeping '
                                  'identity, entitlement, and required estate papers unresolved until '
                                  'supported.',
                                  'Recheck the file whenever ownership information, claimant '
                                  'circumstances, deductions, or payment instructions change before '
                                  'submission or distribution.'],
                 'fields': [{'name': 'mortgage_sale_candidate_screen',
                             'type': 'textarea',
                             'prompt': 'Record the mortgage sale outcome and explain how you distinguished '
                                       'foreclosure opportunities from bank owned properties. Identify the '
                                       'evidence of an actual sale result you still need, and describe why '
                                       'a property listing alone cannot establish that recovery funds '
                                       'exist.',
                             'example': "In Richardson's Georgia workflow, I will select foreclosure homes "
                                        'rather than bank owned listings and retain the resulting sale '
                                        "evidence for further review. The property's appearance on a "
                                        'search page is only a research starting point. I still need to '
                                        'connect the outcome with the debt and available proceeds before '
                                        'approaching a claimant. [Money Making Juggernaut — FJj3hN2KbIg @ '
                                        '00:09:08]'},
                            {'name': 'actual_mortgage_debt_record',
                             'type': 'textarea',
                             'prompt': 'Identify the final judgment or final writ that establishes what '
                                       'was actually due, and compare it with the opening bid. Explain any '
                                       'unresolved difference and state which surplus calculation must '
                                       'remain preliminary until the relevant debt record has been '
                                       'reviewed.',
                             'example': 'I will not subtract the opening bid and call the result available '
                                        'surplus. Richardson explains that the bid can reflect appraisal '
                                        'or judgment fractions rather than the amount owed. My worksheet '
                                        'will identify the final judgment or writ and leave the recovery '
                                        'calculation unconfirmed until that record supports the debt '
                                        'figure. [Money Making Juggernaut — 0pjP-Sr15PA @ 00:00:39]'},
                            {'name': 'trustee_contact_recovery',
                             'type': 'textarea',
                             'prompt': 'Record the trustee information available in the auction record and '
                                       'describe your next research step if that information disappears '
                                       'after foreclosure. Keep the property and case identifiers '
                                       'connected to the contact, and distinguish locating a trustee from '
                                       'confirming funds remain available.',
                             'example': 'If the completed auction page no longer identifies the trustee, I '
                                        'will record that missing contact and investigate PropertyRadar as '
                                        'Richardson describes. Finding the trustee solves the routing '
                                        'problem, not the balance question. My file will still need the '
                                        'sale information and distribution evidence before I describe an '
                                        'owner recovery as available. [Money Making Juggernaut — '
                                        'XNxo6xvEJBg @ 00:01:13]'},
                            {'name': 'trustee_disbursement_reconciliation',
                             'type': 'textarea',
                             'prompt': "Draft the request for the trustee's disbursement breakdown and "
                                       'list the creditor payments you need to verify. Explain how the '
                                       "response will distinguish a creditor's asserted priority from an "
                                       'actual payment, and identify the remaining balance question that '
                                       'controls further work.',
                             'example': 'My request will ask for the disbursement history showing what was '
                                        'paid after the sale. If the trustee says another creditor '
                                        'consumed the surplus, I will seek the payment evidence rather '
                                        'than stop at a statement of priority. The file remains unresolved '
                                        'until that history explains whether any money remains for further '
                                        'recovery. [Money Making Juggernaut — 0pjP-Sr15PA @ 00:02:30]'},
                            {'name': 'mortgage_distribution_and_fee_status',
                             'type': 'textarea',
                             'prompt': "Separate the mortgage case's requested distribution, agreed fee, "
                                       'estimated business compensation, and actual receipt of money. '
                                       'Label each amount by its milestone, and explain what confirmation '
                                       'you need before treating a trustee message or a fee calculation as '
                                       'collected revenue.',
                             'example': 'Richardson reads a trustee message requesting a $16,609 check for '
                                        'distribution to the client. I will record that as a distribution '
                                        'request, not automatically as money received or a business fee. '
                                        'My file will keep the agreement terms and collection evidence '
                                        'separate so a processing milestone does not become a cash receipt '
                                        'by assumption. [Money Making Juggernaut — 7AHHRIbWG80 @ '
                                        '00:03:09]'},
                            {'name': 'company_owner_lookup',
                             'type': 'textarea',
                             'prompt': 'For a company owner, record the state business search findings, '
                                       'including entity status, formation information, and address. '
                                       'Describe what those findings establish and what remains unresolved '
                                       "about the person you can contact, the property's ownership, and "
                                       'authority to pursue the recovery.',
                             'example': 'I will begin the company research with the free business search '
                                        'and record filing date, active or inactive status, entity type, '
                                        'formation location, and address. These details organize the next '
                                        'inquiry rather than prove that any reachable individual can claim '
                                        'the funds. Ownership and the appropriate claimant still need '
                                        'their own supporting review. [William Whitman, Esquire — '
                                        '0xk7lNvAgn0 @ 00:01:06]'},
                            {'name': 'deceased_owner_contact_path',
                             'type': 'textarea',
                             'prompt': 'Map the contact routes for a deceased owner, including existing '
                                       'mobile numbers and potential family connections. Record what each '
                                       'response actually establishes, and explain how you will avoid '
                                       'treating a successful conversation with a relative as proof of '
                                       'entitlement to the funds.',
                             'example': "I will not discard the deceased owner's existing mobile number "
                                        'without considering whether family retained it. Church reports '
                                        'reaching relatives through those numbers after a death. A '
                                        'successful connection becomes a contact lead in my notes, while '
                                        "the person's relationship, ownership connection, and claim "
                                        'authority remain separate questions requiring their own '
                                        'verification. [Surplus Institute / David Church / Unclaimed Funds '
                                        '— hA6VJ_GqGyc @ 00:00:39]'},
                            {'name': 'estate_submission_requirements',
                             'type': 'textarea',
                             'prompt': 'Write the questions you will ask the holding office about an '
                                       "heir's submission requirements. Separate the death certificate "
                                       'from probate papers or a court order, and identify which documents '
                                       'remain missing before the estate file can proceed beyond '
                                       'preliminary family contact.',
                             'example': 'I will ask the holding office what the heir must submit before '
                                        'assembling the filing packet. A death certificate alone will not '
                                        'be treated as sufficient without that answer. Overages Overflow '
                                        'describes offices requiring probate papers or a court order, so '
                                        'the file will explicitly track any missing estate documentation '
                                        'before submission. [Overages Overflow — XTbc1Dz6dxY @ 00:01:32]'},
                            {'name': 'overseas_recovery_amount_revision',
                             'type': 'textarea',
                             'prompt': 'For an overseas claimant, record the current recovery estimate and '
                                       'any deductions that changed the earlier amount. Explain how you '
                                       'will keep the fee discussion connected to the revised recovery '
                                       'rather than an obsolete figure, while tracking unresolved '
                                       'communication and document needs.',
                             'example': "Danielle reports that back taxes reduced the overseas owner's "
                                        'recovery from $97,000 to $87,000 before the fee discussion. My '
                                        'worksheet will preserve both figures and identify the deduction '
                                        'rather than continue presenting the larger amount. Any fee '
                                        'projection must clearly identify the recovery figure it uses and '
                                        'remain separate from a collected payment. [Money Making '
                                        'Juggernaut — WEohyFOyk2M @ 00:01:14]'},
                            {'name': 'claimant_death_change_control',
                             'type': 'textarea',
                             'prompt': 'Describe the actions required if the claimant dies while final '
                                       'documents are being prepared or signed. Identify which assumptions '
                                       'about signing and estate handling must be revisited, and explain '
                                       'why earlier progress cannot justify continuing the file as though '
                                       'nothing changed.',
                             'example': 'If a claimant dies at the final document stage, I will stop '
                                        'treating the existing signing plan as current. Bucci stopped the '
                                        'hospital signing and revisited the estate issue. My case notes '
                                        'will preserve the earlier progress but reopen the authority and '
                                        'documentation questions instead of marking the pending packet '
                                        'complete under unchanged assumptions. [SurplusFundsRiches — '
                                        'EPNAIRsvIHQ @ 00:01:39]'}],
                 'completion_gate': 'Complete all ten fields, marking genuinely inapplicable claimant '
                                    'complications explicitly. Do not advance a mortgage file without '
                                    'actual debt research and an explained distribution history. Do not '
                                    'advance an estate or company file merely because someone is '
                                    'reachable. Resolve claimant authority, required documents, and '
                                    'changed circumstances; keep requested distributions, projected fees, '
                                    'and collected money separate.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Claimant Contact, Evidence, and Follow-Up Planner',
                 'purpose': 'Prepare an evidence-led claimant conversation, address distrust without '
                            'pressure, and track the difference between successful contact, requested '
                            'paperwork, signed agreements, and recovered funds. Keep contact restrictions '
                            'and unresolved debts visible throughout the outreach process.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Complete one worksheet for each claimant conversation, connecting every '
                                  'contact detail to the corresponding property and case.',
                                  "Check DNC filtering, the recipient's local time, and previous stop "
                                  'requests before preparing the next call.',
                                  'Gather concrete records before rehearsing an introduction; describe '
                                  'possible funds without promising the listed surplus as a payout.',
                                  'Practice the introduction, listening pauses, fee explanation, and '
                                  'request for an email or mailing address before calling.',
                                  'After every conversation, record the actual outcome, unresolved '
                                  'questions, delivery preference, and next permitted follow-up action.'],
                 'fields': [{'name': 'contact_data_and_locating_clues',
                             'type': 'textarea',
                             'prompt': "Record the claimant's contact details and explain how each was "
                                       'connected to the case. Include deed information, tax mailing '
                                       'addresses, possible relatives, and returned envelopes. Separate a '
                                       'useful locating clue from confirmation that the intended claimant '
                                       'has actually been reached.',
                             'example': 'The returned envelope stays with the case because the expired '
                                        'forwarding notice may reveal another address. I will inspect the '
                                        'bottom of the envelope and record that address as a locating '
                                        'clue, not proof that the claimant currently lives there or has '
                                        'received our explanation. [SurplusFundsRiches — bt6FqwHwtBY @ '
                                        '00:03:12]'},
                            {'name': 'calling_restrictions_and_stop_log',
                             'type': 'textarea',
                             'prompt': 'Document how DNC filtering was checked, whether the number was '
                                       "excluded, and the recipient's local time before calling. Record "
                                       'any explicit stop request and the same-day list update. Leave the '
                                       'next call blocked when the screening result remains unresolved.',
                             'example': 'Calling status is blocked until the DNC filtering result is '
                                        'recorded. Richardson describes excluding listed contacts after a '
                                        'lawsuit rather than assuming the data provider checked them. A '
                                        'previous request to stop also remains visible in the contact '
                                        'record, so another calling session does not restart unwanted '
                                        'outreach. [Money Making Juggernaut — Zh5fus4SGzc @ 00:02:21]'},
                            {'name': 'proof_packet_and_estimated_funds',
                             'type': 'textarea',
                             'prompt': 'List the records you will use to explain the possible recovery, '
                                       'including auction information and any unsuccessful county notice. '
                                       'Identify unresolved second mortgages or liens. Write an '
                                       'owner-facing explanation that distinguishes the displayed surplus '
                                       'from the amount potentially available after competing debts.',
                             'example': 'My conversation notes say possible funds, not a guaranteed owner '
                                        'payment. Before calling, I will check whether a second mortgage '
                                        'or other lien could absorb part of the balance. The records may '
                                        'support discussing an opportunity, but the listed surplus alone '
                                        'does not establish what the claimant receives. [Money Making '
                                        'Juggernaut — rJjMD-YvK30 @ 00:05:13]'},
                            {'name': 'first_call_structure',
                             'type': 'textarea',
                             'prompt': 'Draft a short first-call outline covering your introduction, '
                                       'verification, explanation of the opportunity, and request for an '
                                       'email or mailing address. State the immediate objective clearly. '
                                       'Avoid treating the initial conversation as a requirement to obtain '
                                       'a signed agreement immediately.',
                             'example': 'The outline is introduction, verification, a brief explanation of '
                                        "how we can help, and a request for the claimant's preferred "
                                        'delivery address. My objective is to send information they can '
                                        'review, not deliver a long pitch. Richardson describes this first '
                                        'conversation as taking five minutes or less. [Money Making '
                                        'Juggernaut — JJObKyLY5YY @ 00:00:27]'},
                            {'name': 'listening_and_rehearsal_notes',
                             'type': 'textarea',
                             'prompt': 'Write the question that invites the claimant to review the auction '
                                       'results, then mark where you will stop speaking. Record your '
                                       'rehearsal practice and listening reminders. Include space for the '
                                       "claimant's explanation instead of scripting uninterrupted "
                                       'statements about the recovery.',
                             'example': 'After asking whether we can review the auction results, I will '
                                        'pause rather than fill the silence with another pitch. Taren '
                                        'describes waiting three to five seconds for a response. My '
                                        "rehearsal notes leave room for the claimant's answer before I "
                                        'explain the next part of the process. [Alfred Taren — CqlbwGPmv64 '
                                        '@ 00:02:01]'},
                            {'name': 'contingency_fee_explanation',
                             'type': 'textarea',
                             'prompt': 'Write the fee explanation you will actually use, stating whether '
                                       'compensation comes from recovered funds rather than being added to '
                                       'them. Connect the explanation to the proposed agreement. Identify '
                                       'any wording that could confuse the claimant about their remaining '
                                       'share.',
                             'example': 'The explanation will identify the agreed percentage and say '
                                        'whether it comes out of the recovered funds. I will not describe '
                                        'ten percent in a way that sounds like an additional payment on '
                                        'top of the recovery. Church specifically corrects that ambiguity '
                                        'while reviewing a fee conversation. [Surplus Institute / David '
                                        'Church / Unclaimed Funds — MsxVzoHQCNk @ 00:07:30]'},
                            {'name': 'distrust_and_objection_response',
                             'type': 'textarea',
                             'prompt': "Record the claimant's actual concern, the record that answers it, "
                                       'and a brief response using only information you can support. '
                                       'Distinguish questions about legitimacy from refusal. Remove '
                                       'fabricated connections, pressure, or unsupported stories from the '
                                       'explanation before making another contact.',
                             'example': 'If the claimant asks why they should believe the call, I will '
                                        'return to the case information and offer the supporting records. '
                                        'I will not invent a mutual friend or another personal connection '
                                        "to gain attention. Church's instruction is to stick to true data "
                                        'rather than fabricate a story. [Surplus Institute / David Church '
                                        '/ Unclaimed Funds — jNXoU7Ep1vY @ 00:03:07]'},
                            {'name': 'document_delivery_and_callback',
                             'type': 'textarea',
                             'prompt': 'Record whether the claimant wants email or mailed information, the '
                                       'address supplied, and the agreed next contact. Prepare a clear '
                                       'callback message with a slowly delivered number. Keep successful '
                                       'delivery separate from an assumption that the claimant has read or '
                                       'accepted everything.',
                             'example': 'The callback message will give the number slowly and repeat it so '
                                        'the claimant can write it down. Church reports complaints about '
                                        'speaking too quickly and recommends repeating the number two or '
                                        'three times. My contact record will separately show the delivery '
                                        'address and whether any response arrives. [Surplus Institute / '
                                        'David Church / Unclaimed Funds — xqpLsq3JVlU @ 00:34:45]'},
                            {'name': 'unfinished_paperwork_follow_up',
                             'type': 'textarea',
                             'prompt': 'Set the next follow-up action after documents are sent, noting '
                                       'what question or missing item the contact should resolve. If '
                                       'promised paperwork remains outstanding, include a fresh '
                                       'claim-status check. Do not assume friendly conversations mean the '
                                       'opportunity is still available to your business.',
                             'example': 'When the promised documents do not return, the next action '
                                        'includes checking whether a claim has already been filed. Church '
                                        'describes a friendly claimant who filed directly after paperwork '
                                        'had been prepared. I will update availability before continuing '
                                        'to treat this unsigned file as an active recovery opportunity for '
                                        'the business. [Surplus Institute / David Church / Unclaimed Funds '
                                        '— jNXoU7Ep1vY @ 00:07:49]'},
                            {'name': 'conversation_outcome_and_stage',
                             'type': 'textarea',
                             'prompt': 'Record the precise outcome of the conversation using separate '
                                       'descriptions for contact, permission to send information, verbal '
                                       'agreement, signed paperwork, and recovered funds. Identify what '
                                       'evidence supports the current stage and which event must occur '
                                       'before the case can advance.',
                             'example': 'The outcome is verbal agreement with contracts still unsigned, '
                                        'not collected revenue. Church describes a day with $16,000 in '
                                        'verbal commissions while acknowledging that signatures remained '
                                        'outstanding. My case record will preserve that distinction and '
                                        'name returned signed paperwork as the next event, rather than '
                                        'marking the recovery complete. [Surplus Institute / David Church '
                                        '/ Unclaimed Funds — ieI6zKICpKo @ 00:00:31]'}],
                 'completion_gate': 'Complete only when contact restrictions have been checked, the '
                                    'conversation uses supportable records and estimated amounts, the fee '
                                    'explanation is clear, and the actual outcome and next action are '
                                    'recorded. An unresolved screening result blocks calling; a verbal '
                                    'agreement does not complete the claim.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Claim Packet, Local Requirements, and Submission Control',
                 'purpose': 'Turn a signed agreement into a claim packet matched to the actual money '
                            'holder, claimant situation, and local instructions. Track missing documents, '
                            'competing debt, timing, and delivery without confusing a submitted claim with '
                            'an approved or paid recovery.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Identify the fund type, holding office, filing destination, and '
                                  'deadline before assembling forms or scheduling signatures.',
                                  'Read the applicable instructions again rather than copying another '
                                  "county's packet or assuming your preferred assignment form is accepted.",
                                  'Compare claimant and property identifiers across the agreement, '
                                  'ownership evidence, claim form, and payment direction.',
                                  'Resolve required originals, certified copies, notarization, estate '
                                  'evidence, and signing details before treating the packet as ready.',
                                  'Retain mailing and filing confirmations, tell the claimant what happens '
                                  'next, and schedule a receipt check with the holding office.'],
                 'fields': [{'name': 'holding_office_and_filing_route',
                             'type': 'textarea',
                             'prompt': 'Identify who currently holds the money, which office receives the '
                                       'claim, and the documents that office requires for release. Record '
                                       'the filing deadline separately from expected processing time. Mark '
                                       'unanswered questions for resolution before selecting forms or '
                                       'promising the claimant a submission date.',
                             'example': 'The routing entry has three unresolved items: money holder, '
                                        'release requirements, and time remaining to file. I will answer '
                                        'those questions before assembling a packet from earlier work. '
                                        'Taren frames the process around those exact questions, so a '
                                        'signed agreement alone does not establish where or how this claim '
                                        'proceeds. [Alfred Taren — ouYE5P3UJdQ @ 00:00:46]'},
                            {'name': 'claim_and_property_identifiers',
                             'type': 'textarea',
                             'prompt': 'Transcribe the exact tax deed or case number, parcel or real '
                                       'estate number, and sale date from the relevant records. Compare '
                                       'those entries across the packet. Document any discrepancy and its '
                                       'correction before asking the claimant to sign the final version.',
                             'example': 'The identifier review compares the tax deed number, parcel '
                                        'number, and specific sale date across the claim materials. I will '
                                        'not substitute a general auction month for the recorded sale '
                                        'date. The notary walkthrough emphasizes these exact entries, '
                                        'making identifier matching a separate check before the packet '
                                        'moves to signing. [Noble Notary & Legal Document Preparers — '
                                        'DM0kjEZlbSk @ 00:03:07]'},
                            {'name': 'agreement_review_with_claimant',
                             'type': 'textarea',
                             'prompt': 'Plan the agreement walkthrough with the claimant, identifying the '
                                       'compensation terms, when compensation is earned, and each required '
                                       'signature. Record questions answered during the review. Keep '
                                       'sending the agreement separate from confirming that the claimant '
                                       'understands and has completed the required signing.',
                             'example': 'The agreement review happens while the claimant is at the '
                                        'computer, with the document open. I will point to the '
                                        'compensation terms and required signatures rather than merely '
                                        'asking whether the email arrived. Church describes reading the '
                                        'agreement together so the claimant can follow what they owe and '
                                        'what needs signing. [Surplus Institute / David Church / Unclaimed '
                                        'Funds — A47AbsTHlkY @ 00:05:44]'},
                            {'name': 'ownership_evidence_and_deed_copy',
                             'type': 'textarea',
                             'prompt': 'Identify the ownership document connecting the claimant to the '
                                       'property before the sale. State whether an ordinary copy or '
                                       "certified copy is required. Distinguish the former owner's deed "
                                       "from the tax deed showing the auction purchaser's acquisition when "
                                       'preparing the evidence list.',
                             'example': "The ownership attachment should be the former owner's grant deed, "
                                        "not the tax deed issued for the buyer's acquisition after "
                                        'auction. Greg makes that distinction when describing the next '
                                        "steps after a returned contract. I will check the document's "
                                        'parties and purpose before marking ownership evidence complete '
                                        'for the filing packet. [Overage Acquisition — X_Oq8vv4j_c @ '
                                        '00:00:42]'},
                            {'name': 'originals_notarization_and_signing',
                             'type': 'textarea',
                             'prompt': 'Create the signing checklist for originals, certified documents, '
                                       'notarization, requested ink color, and separate claimant packets. '
                                       'Assign responsibility for obtaining each item. Record the planned '
                                       'return method so completed documents reach the correct destination '
                                       'without assuming every county accepts the same execution method.',
                             'example': 'The packet remains incomplete until the instructions establish '
                                        'whether originals or certified documents are needed and whether '
                                        'each claimant must submit separately. Taren identifies those '
                                        'distinctions as recurring reasons claims come back. I will write '
                                        'the requirement beside each attachment instead of treating '
                                        "another county's accepted packet as the default here. [Alfred "
                                        'Taren — ouYE5P3UJdQ @ 00:07:39]'},
                            {'name': 'deceased_claimant_document_blockers',
                             'type': 'textarea',
                             'prompt': 'List the deceased-owner evidence required for this claimant '
                                       'situation and mark every missing document explicitly. Identify who '
                                       'will obtain each item and the next follow-up. Do not describe the '
                                       'file as ready merely because the recovery amount is substantial or '
                                       'an agreement is signed.',
                             'example': 'A missing death certificate is a blocking item, not a minor note '
                                        "beneath the expected fee. Richardson describes Christian's "
                                        '$138,000 deal remaining stalled for more than a year because one '
                                        'death certificate was missing. My checklist gives that document '
                                        'its own responsible person, next action, and outstanding status '
                                        'before submission readiness. [Money Making Juggernaut — '
                                        'MVCNlj7HQBQ @ 00:12:31]'},
                            {'name': 'current_balance_and_competing_payoffs',
                             'type': 'textarea',
                             'prompt': 'Record the evidence that funds remain available and identify each '
                                       'competing lien or deduction still under review. Request written '
                                       'payoff information where needed. Compare recorded amounts and '
                                       'added fees before updating the estimated owner remainder or '
                                       'describing a deduction as final.',
                             'example': 'The competing-lien entry stays estimated until a written payoff '
                                        'can be compared with the recorded amount and added fees. Overage '
                                        'Acquisition calls for that comparison before accepting the '
                                        'deduction as final. I will keep the listed surplus, proposed '
                                        'deductions, and resulting owner estimate separate rather than '
                                        'collapse them into one promised payout. [Overage Acquisition — '
                                        'V0TgTN8wjyM @ 00:04:09]'},
                            {'name': 'filing_review_and_payment_timeline',
                             'type': 'textarea',
                             'prompt': 'Build a timeline separating the filing deadline, submission date, '
                                       'review waiting period, and expected payment interval. Identify the '
                                       'event that starts each period. Attribute practitioner timing '
                                       'examples without converting them into a guaranteed schedule for a '
                                       'different county or claim type.',
                             'example': 'For the Florida tax-deed example, the timeline starts the 120-day '
                                        'review waiting period from the notice of surplus funds. '
                                        'Richardson says claims can be submitted during that period '
                                        'although review waits. I will therefore record submission and '
                                        'review eligibility separately, without treating the waiting '
                                        'period as a reason to postpone preparing documents. [Money Making '
                                        'Juggernaut — FIgAVvrCcC8 @ 00:05:08]'},
                            {'name': 'state_model_and_compensation_check',
                             'type': 'textarea',
                             'prompt': 'Identify whether the proposed arrangement is a recovery service or '
                                       'an assignment purchase, and connect it to the specific fund type. '
                                       'Record applicable fee or capital questions for verification. Keep '
                                       'proposed legislation and practitioner descriptions distinct from '
                                       'confirmed requirements for this file.',
                             'example': 'The Texas tax-assignment model is not entered as an ordinary '
                                        'contingency recovery. Overage Acquisition describes paying at '
                                        'least 80% of the claim on assignment day. My model review '
                                        'therefore asks whether that upfront purchase can actually be '
                                        'funded before proceeding, rather than relying on the eventual '
                                        'recovery to supply the purchase money. [Overage Acquisition — '
                                        'F9-rceUCqYE @ 00:03:45]'},
                            {'name': 'submission_receipt_and_next_action',
                             'type': 'textarea',
                             'prompt': 'Record the submission method, tracking or filing confirmation, '
                                       'claimant update, and planned receipt check. After delivery, ask '
                                       'whether additional documents are needed. Assign the next action '
                                       'and follow-up date without treating a delivery scan as '
                                       'confirmation that the claim has been approved.',
                             'example': 'The submission record will include the USPS tracking number '
                                        'provided to the claimant and a call to the county after delivery. '
                                        'Greg recommends confirming receipt and asking about additional '
                                        'documents. I will record those answers separately from the '
                                        "carrier's delivery result, leaving approval and payment pending "
                                        'until those events actually occur. [Overage Acquisition — '
                                        'X_Oq8vv4j_c @ 00:03:18]'}],
                 'completion_gate': 'Mark the packet ready only after the filing route, deadline, claimant '
                                    'identifiers, required evidence, signing mechanics, and compensation '
                                    'model have been checked. Missing required documents remain blockers. '
                                    'After submission, retain proof, confirm receipt, and record the next '
                                    'action; submission alone is not approval or payment.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Fund-Type Routing and Repeatable Recovery Operations',
                 'purpose': 'Separate state property, foreclosure surplus, and bankruptcy recoveries while '
                            'building a repeatable operating record. Connect availability checks, claimant '
                            'authority, local agreements, case stages, attorney handoffs, and actual fee '
                            'economics before expanding or delegating the work.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Choose the fund type first and identify its actual holder rather than '
                                  'assuming every recovery follows the state-property process.',
                                  'Verify availability, existing claims, and claimant authority before '
                                  'preparing outreach, agreements, or a paid processing handoff.',
                                  'Keep state-specific agreement checks and bankruptcy evidence in '
                                  'separate sections so requirements are not transferred between unrelated '
                                  'claim types.',
                                  'Track contacted, signed, filed, accepted, and paid cases distinctly; '
                                  'update tasks and claimant communications as each event occurs.',
                                  'Review actual deductions and collected fees, then document a process '
                                  'you have repeatedly completed before assigning it to an assistant.'],
                 'fields': [{'name': 'fund_type_and_holder_map',
                             'type': 'textarea',
                             'prompt': 'Classify the opportunity as state unclaimed property, foreclosure '
                                       'surplus, or bankruptcy funds. Identify the actual holder and '
                                       "research route for that category. Explain why another category's "
                                       'agreement, evidence, or processing expectations cannot '
                                       'automatically be reused for the file you are evaluating.',
                             'example': 'This routing entry separates foreclosure surplus from state '
                                        'unclaimed property before selecting a claim process. Unclaimed '
                                        'Funds Finder explains that foreclosure money may be held by a '
                                        'court, sheriff, trustee, or county office rather than the state '
                                        'program. I will identify that holder instead of starting with a '
                                        'state-property agreement by default. [Unclaimed Funds Finder — '
                                        'NDXBOlfVC5E @ 00:01:06]'},
                            {'name': 'availability_and_existing_claim_review',
                             'type': 'textarea',
                             'prompt': 'Record how the funds arose, whether they remain available, and '
                                       'what existing claims or payments appear in the records. For '
                                       'bankruptcy funds, distinguish an apparent prior claim from '
                                       'confirmed payment. Document unresolved questions before either '
                                       'discarding the lead or beginning a new recovery.',
                             'example': 'An existing bankruptcy claim triggers review rather than an '
                                        'automatic rejection or a fresh filing. Richardson and Whitman '
                                        'describe encountering a false claim and checking payment and '
                                        'partial recovery. My review notes will distinguish the claim '
                                        'entry, any confirmed payment, and the amount still potentially '
                                        'available before deciding whether to proceed. [Money Making '
                                        'Juggernaut — NxCoaATrtq4 @ 00:15:32]'},
                            {'name': 'state_finder_agreement_controls',
                             'type': 'textarea',
                             'prompt': 'Create a state-specific agreement checklist covering timing, fee, '
                                       "disclosures, notarized signatures, and the claimant's current "
                                       'payment address where relevant. Attribute each practitioner '
                                       'example to its state and fund type. Leave unverified requirements '
                                       'open instead of combining different states into one universal '
                                       'agreement.',
                             'example': 'For the North Carolina example, the checklist flags the first 24 '
                                        'months after delivery to the state before an agreement is '
                                        'prepared. Pierce Law Group describes a general restriction during '
                                        'that period and an attorney-related exception. I will keep the '
                                        'timing question visible rather than assume a willing claimant '
                                        'makes the agreement usable. [Pierce Law Group — Uxc6KOSzdLc @ '
                                        '00:00:29]'},
                            {'name': 'bankruptcy_proof_and_explanation',
                             'type': 'textarea',
                             'prompt': 'Identify the bankruptcy records needed to explain the opportunity, '
                                       'including the notice of deposit when available. Write a short '
                                       'explanation connecting those records to the possible recovery. '
                                       'Distinguish a closed bankruptcy case from the separate question of '
                                       'whether an undelivered payment remains.',
                             'example': 'The proof packet will include the bankruptcy notice of deposit so '
                                        'the conversation can explain why funds may remain even though the '
                                        'case is closed. Richardson uses that notice as concrete evidence. '
                                        'I will connect the document to the recipient and claimed amount '
                                        'instead of relying on a vague statement about found money. [Money '
                                        'Making Juggernaut — NxCoaATrtq4 @ 00:12:04]'},
                            {'name': 'corporate_recipient_and_signing_authority',
                             'type': 'textarea',
                             'prompt': 'For an entity recipient, record the company connection and '
                                       'identify the person who may sign on its behalf. Separate a '
                                       'reachable business contact from established authority. List the '
                                       'remaining entity research needed before presenting paperwork as '
                                       'ready for a corporate claimant.',
                             'example': 'The entity research entry identifies the company recipient first, '
                                        'then investigates its president, CEO, or authorized members as '
                                        'possible signers. Richardson highlights that research skill for '
                                        'corporate bankruptcy recipients. I will not treat the first '
                                        'person who answers a company number as automatically authorized '
                                        'to complete the recovery paperwork for the business. [Money '
                                        'Making Juggernaut — 7WZONOtYbjc @ 00:06:58]'},
                            {'name': 'pipeline_stages_and_payment_evidence',
                             'type': 'textarea',
                             'prompt': 'Define separate case stages for filing, acceptance, and payment, '
                                       'with the evidence needed to enter each stage. Record expected fees '
                                       'separately from collected funds. Use practitioner outcomes to test '
                                       'whether your reporting would mistakenly count unresolved claims as '
                                       'successful paid recoveries.',
                             'example': 'The bankruptcy results entry shows four filings but only one '
                                        "payout, matching the guest's reported distinction. Texas delays "
                                        'and an Illinois claim awaiting anticipated money remain '
                                        'unresolved rather than counted as paid. My dashboard will '
                                        'therefore show filing activity, acceptance where established, and '
                                        'collected recovery as separate events with separate supporting '
                                        'evidence. [Money Making Juggernaut — waps0YmW8BI @ 00:02:30]'},
                            {'name': 'crm_tasks_and_claimant_updates',
                             'type': 'textarea',
                             'prompt': 'Describe how the case record connects outreach, documents, tasks, '
                                       'and claimant updates. Name the next responsible person and action '
                                       'for each active file. Specify when the client-facing status '
                                       'changes so a portal update reflects a real event rather than an '
                                       'optimistic internal expectation.',
                             'example': 'The CRM record will keep the next task beside the document and '
                                        'case status, while the client portal receives the corresponding '
                                        'factual update. Surplus Funds List demonstrates updating portal '
                                        'status so the homeowner can search for the case. I will not label '
                                        'a file paid merely because paperwork has moved to processing. '
                                        '[Surplus Funds List — lOnYUxDdOdI @ 00:04:10]'},
                            {'name': 'screening_and_paid_handoff_gate',
                             'type': 'textarea',
                             'prompt': 'List the checks required before a paid attorney handoff, including '
                                       'actual debt, second mortgages, liens, claimant information, and '
                                       'remaining surplus. Record unresolved contradictions explicitly. '
                                       'Explain how the handoff decision changes when the attorney '
                                       'retainer is payable even if the submitted case proves unworkable.',
                             'example': 'The attorney handoff stays blocked while claimant information and '
                                        "the team's findings remain unchecked. Full Circle's host explains "
                                        'that a retainer is paid even on a bad case. My screening record '
                                        'therefore requires verification before transfer, rather than '
                                        "using the attorney's paid review as the first test of whether the "
                                        'file is viable. [Surplus Funds Secrets — c2vik3KCA5g @ 00:33:15]'},
                            {'name': 'fee_allocation_and_cash_readiness',
                             'type': 'textarea',
                             'prompt': 'Separate the recovery amount, gross business fee, attorney '
                                       'expense, partner allocations, and remaining business share. State '
                                       'whether each amount is projected or collected. Include payment '
                                       'timing in your operating plan rather than treating signed cases or '
                                       'large listed balances as immediately available income.',
                             'example': "Jordan's living-case illustration starts with a $10,000 fee, "
                                        'subtracts $2,500 for the lawyer, and leaves $7,500 before the '
                                        'partner split. The closer receives $2,250 and the '
                                        'appointment-setting partner $5,250. I will enter that as an '
                                        'allocation example, not a guarantee, and keep collection status '
                                        'separate from the arithmetic when planning operating cash. '
                                        '[Jordan Tejeda Marketing — -bhX4mtOKPs @ 00:26:24]'},
                            {'name': 'repeatability_and_assistant_training',
                             'type': 'textarea',
                             'prompt': 'Choose one operating process to prove repeatedly before delegating '
                                       'it. Describe the records, decisions, and completed outcomes an '
                                       'assistant must understand. Plan supervised practice and a daily '
                                       'reference, then identify what evidence will show the assistant can '
                                       'repeat the process without unexplained assumptions.',
                             'example': 'The first assistant assignment will follow a process I have '
                                        'already completed repeatedly, with training alongside me rather '
                                        'than an unexplained handoff. Joe describes spending without '
                                        'results before changing that approach. The training record will '
                                        'show the steps demonstrated, questions resolved, and the next '
                                        'supervised repetition before the assistant works through that '
                                        'process independently. [Unclaimed CEO — XdU7CVOntKk @ 00:03:57]'}],
                 'completion_gate': 'Complete when the fund type and holder are identified, availability '
                                    'and authority checks are recorded, agreement questions remain '
                                    'visible, and the case stages distinguish activity from payment. Do '
                                    'not release an unchecked paid handoff or delegate an unproven '
                                    'process. Keep projected allocations separate from collected operating '
                                    'cash.'}]}
