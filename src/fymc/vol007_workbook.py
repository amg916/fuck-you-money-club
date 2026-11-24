from __future__ import annotations

def build_volume_007_workbook() -> dict:
    return {'workbook_id': 'wb-007-unclaimed-property-recovery',
 'volume_id': 'vol-007-unclaimed-property-recovery',
 'title': 'Unclaimed Property Recovery — Practitioner Testimony Operator Workbook',
 'subtitle': 'A field-tested worksheet system for locating dormant assets, launching a compliant recovery '
             'practice, working official state portals, and filing business and investigator claims inside '
             'state fee caps, registration rules, and payout deadlines',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Unclaimed Property Fundamentals, Search Entry Points, and Business Launch Plan',
                 'purpose': 'Build a working understanding of how dormant money moves from holders into '
                            'state custody, map the official search sequence that prevents false zero '
                            'results, and lock in the niche, state, fee, funding, and outreach decisions '
                            'that must be settled before the first prospect is ever contacted.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Work through the fields in order, because the asset fundamentals in the '
                                  'first half shape every launch decision made in the second half.',
                                  'Write in complete sentences with real figures, states, and dates rather '
                                  'than placeholders, so each answer can be reused as an operating note.',
                                  'Confirm every fee cap, registration rule, and claim-package requirement '
                                  'directly with the state unclaimed property office before relying on it.',
                                  'Treat any answer that involves collecting money before the claimant is '
                                  'paid as a failed answer, and rewrite it until payment follows the '
                                  'payout.',
                                  'Revisit the tracking fields after two to three weeks of outreach and '
                                  'adjust volume only from measured calls-to-pickups data, never from '
                                  'instinct.'],
                 'fields': [{'name': 'asset_class_definition',
                             'type': 'textarea',
                             'prompt': 'Describe in your own words how money becomes unclaimed property: '
                                       'who the holder is, what due diligence notice must go out, which '
                                       'dormancy clock applies to wages versus bank accounts, and why the '
                                       'state holds funds without any expiration date.',
                             'example': 'A payroll department cannot deliver a final paycheck, mails a due '
                                        'diligence notice, and remits the wages after a one-year dormancy '
                                        'clock, while a dormant bank account moves after three to five '
                                        'years. The state holds the money as custodian with no expiration, '
                                        'part of a pool Hoang Le puts above $70 billion [Hoang Le CFP, EA, '
                                        'Real Estate Agent — kZMkghcevh8 @ 00:00:00].'},
                            {'name': 'search_entry_sequence',
                             'type': 'textarea',
                             'prompt': 'List the exact order of databases you will search for each owner, '
                                       'starting with the national multistate site, then the state sites '
                                       'for California or Pennsylvania style records, then the federal '
                                       'registries that no single state portal covers.',
                             'example': 'First pass on MissingMoney.com, second pass through unclaimed.org '
                                        'to reach California and Pennsylvania directly, third pass across '
                                        'federal registries for wages, pensions, FHA refunds, failed '
                                        'banks, and bankruptcy courts. A single state portal is never the '
                                        'last word, because state databases do not hold federal assets and '
                                        'millions wrongly assume nothing is coming [This Guy Knows Tech — '
                                        '74IHdXzW4aQ @ 00:02:47].'},
                            {'name': 'dormancy_status_check',
                             'type': 'text',
                             'prompt': 'Before declaring any search empty, record whether the target asset '
                                       'has actually cleared its dormancy period and been reported, noting '
                                       'the asset type, the last activity date you know of, and the '
                                       'earliest date it could reach the state.',
                             'example': "Owner's checking account went quiet eighteen months ago, so a "
                                        'bank-account dormancy clock of three to five years means it has '
                                        'not reached the state yet. Result logged as not yet reported '
                                        'rather than zero, with a recheck scheduled, because an empty '
                                        'search may only mean nothing has been turned over [Hoang Le CFP, '
                                        'EA, Real Estate Agent — kZMkghcevh8 @ 00:02:14].'},
                            {'name': 'claim_size_reality',
                             'type': 'textarea',
                             'prompt': 'Write down the realistic size expectations you will use when '
                                       'screening records, comparing the typical median claim against the '
                                       'average claim, and explain how a few very large accounts distort '
                                       'the picture you present to owners and partners.',
                             'example': 'The typical claim sits near $100 while the average reaches '
                                        '$2,080, because a handful of huge accounts drag the mean upward. '
                                        "Illinois' record $11 million Joseph Stancak estate, which took "
                                        'five generations of research to find 119 relatives across the US, '
                                        'Poland, and Slovakia, is the outlier, not the norm [Money Missed '
                                        '— sfcrjWHv_7k @ 00:03:30].'},
                            {'name': 'first_contact_opening',
                             'type': 'textarea',
                             'prompt': 'Draft the first two sentences you will say when an owner answers, '
                                       'and describe how you will handle immediate disbelief or a scam '
                                       'accusation without pressuring them, requesting money, or '
                                       'abandoning a file that may be worth real money.',
                             'example': 'Opening: I am calling about funds the state is holding under your '
                                        'name, and nothing is owed to me unless you get paid. Invite them '
                                        'to verify the record on the official state site. Expect '
                                        "suspicion: South Carolina's treasurer reached an heir owed more "
                                        'than $763,000 who assumed the call was a scam and almost hung up '
                                        '[Money Missed — sfcrjWHv_7k @ 00:03:49].'},
                            {'name': 'fee_cap_and_payment_rule',
                             'type': 'text',
                             'prompt': 'Record the fee cap for your target state, the percentage you will '
                                       'actually charge, and your written rule on when payment is '
                                       'collected, making sure no fee, processing charge, or deposit is '
                                       'ever requested before the claimant receives funds.',
                             'example': 'Target state capped at 10 percent, charging 10 percent, collected '
                                        'only after the claimant is paid and confirms receipt. Legitimate '
                                        'locators are regulated in most states and never ask to be paid '
                                        'first. Any email promising Jake $3,400 once a $49 processing fee '
                                        'is paid is a scam [Hoang Le CFP, EA, Real Estate Agent — '
                                        'kZMkghcevh8 @ 00:07:03] [Dollar Decoded — QVgTN5Lip0o @ '
                                        '00:05:52].'},
                            {'name': 'niche_and_state_selection',
                             'type': 'textarea',
                             'prompt': 'Name the single niche and the one or two states you will work '
                                       "first, and justify each choice using the state's fee cap, whether "
                                       'it reports exact amounts, how pleasant it is to work with, and '
                                       'whether licensing partners are required.',
                             'example': 'Niche: state unclaimed funds. First state: California, because '
                                        'the state registers locators and pays the 10 percent directly, so '
                                        'there is no collecting from the client; a $20,000 claim pays '
                                        '$2,000 to the locator and $18,000 to the client. New York is '
                                        'skipped because it reports only under or over $100 [Surplus '
                                        'Institute / David Church / Unclaimed Funds — IIBKDdChS-k @ '
                                        '00:01:43].'},
                            {'name': 'claim_floor_and_filter',
                             'type': 'text',
                             'prompt': 'State the minimum claim size you will accept, the exceptions you '
                                       'allow for states that hide amounts, and the list filters you will '
                                       'apply to downloaded or purchased state records before spending any '
                                       'time or money on skip tracing.',
                             'example': 'Floor of $10,000 under a 10 percent cap, starting with roughly a '
                                        '$10,000 claim to get the first person paid. Only exception: in '
                                        'under-or-over-$100 states, pull Roth IRA and IRA accounts, which '
                                        'carry higher payouts. Filter the downloaded list by amount, '
                                        'descending, before any skip trace is ordered [Surplus Institute / '
                                        'David Church / Unclaimed Funds — RjCjrBjQF7Y @ 00:07:42].'},
                            {'name': 'outreach_channel_and_followup',
                             'type': 'textarea',
                             'prompt': 'Choose your primary outreach channel, either cold calls with '
                                       'structured follow-up or inbound social media lead flow, and write '
                                       'the follow-up count per prospect, your weekend calling plan, and '
                                       'the daily time block you will hold.',
                             'example': 'Channel: phone, with three to five follow-up calls per prospect, '
                                        'since 80 percent of sales close on the fifth to twelfth contact '
                                        'and 48 percent of salespeople never follow up. Saturdays and '
                                        'Sundays get priority for contact rates, inside a three-hour daily '
                                        "window that matches most people's mental limit [Surplus Funds 101 "
                                        '— qyRWV76TgwE @ 00:07:19] [Surplus Funds 101 — PGvJEv9Y_Go @ '
                                        '00:05:58].'},
                            {'name': 'funding_and_tracking_plan',
                             'type': 'textarea',
                             'prompt': 'Explain how you will fund the first ninety days without draining '
                                       'household savings, which free or low-cost lead and skip tracing '
                                       'sources you will use, and how you will measure calls against '
                                       'pickups before increasing volume.',
                             'example': 'No personal savings go in, since draining your own account means '
                                        "draining your family's money. Leads come from free online state "
                                        'lists, and batch skip tracing runs about $14 to $15 per 100 leads '
                                        'against four to ten hours of manual research. Calls-to-pickups '
                                        'get tracked for two to three weeks before doubling volume '
                                        '[Unclaimed CEO — i84F9CVghTA @ 00:09:25].'}],
                 'completion_gate': 'Do not contact a single prospect until the dormancy logic, the full '
                                    "search sequence, the target state's fee cap and claim-package rules, "
                                    'a minimum claim floor, a no-upfront-payment rule, and a measured '
                                    'follow-up plan are all written down and confirmed with the state '
                                    'office.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Official Portals, State Return Practices, and State-by-State Personal Searches',
                 'purpose': 'Run a disciplined, free, official search across the multistate portal and '
                            'every relevant state site, verify suspicious contacts, account for automatic '
                            'state returns and securities liquidation, and assemble a complete claim '
                            'packet that survives setoffs, finder caps, utility exceptions, and '
                            'check-cashing deadlines.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Start every owner file with the multistate sweep, then move state by '
                                  'state through each place the owner lived, worked, or rented.',
                                  'Search every name variant, old address, estate prefix, and business '
                                  'name on each portal before marking any state as clear.',
                                  'Verify every unexpected letter, check, or call against the official '
                                  'state search before replying, clicking, or paying anything at all.',
                                  'Log claim numbers, filing dates, and uploaded documents the moment they '
                                  'appear, so every follow-up call references the exact file.',
                                  'Price setoffs, finder caps, utility exceptions, and check-cashing '
                                  'deadlines into each file before counting any balance as recoverable.'],
                 'fields': [{'name': 'multistate_first_sweep',
                             'type': 'text',
                             'prompt': 'Record the results of your first sweep on the national multistate '
                                       'portal, including every name variant entered, the number of hits, '
                                       'the states each hit points to, and whether each record routes to '
                                       'an info view or a claim.',
                             'example': 'MissingMoney.com searched first because it is endorsed by the '
                                        'National Association of Unclaimed Property Administrators and the '
                                        'National Association of State Treasurers. Three name variants '
                                        'returned eleven hits across two states, each logged with its '
                                        'info-versus-claim routing and noted for follow-up on the '
                                        'individual state site, since every state runs its own process '
                                        '[Jordan Liles — lM8PdIOG7-E @ 00:02:31].'},
                            {'name': 'state_portal_map',
                             'type': 'textarea',
                             'prompt': 'List every state where the owner lived, worked, or rented, and for '
                                       'each one write the official portal address you confirmed, the '
                                       'result page size you used, and any state-specific quirk that '
                                       'changes how records display.',
                             'example': 'Owner lived in Pennsylvania and Delaware and rented in Texas. '
                                        'Delaware groups records into over-50 and under-50 bands; '
                                        'Pennsylvania shows white rows for single-owner property and gray '
                                        'rows for joint ownership; result pages set to 80 rows to avoid '
                                        'missing entries. Old addresses searched too, since a move usually '
                                        'ties money to the prior address [Michael Curtis — 0YK26E_fzYA @ '
                                        '00:03:35].'},
                            {'name': 'name_variant_matrix',
                             'type': 'textarea',
                             'prompt': 'Build a full name variant matrix covering maiden and married '
                                       'names, nicknames, common misspellings, every business or trade '
                                       'name ever used, estate prefixes, and deceased relatives, then mark '
                                       'which variants produced results on which portals during this '
                                       'search session.',
                             'example': 'Variants run: legal name, signup typo from an old utility '
                                        'account, former sole proprietorship name, and Estate of plus '
                                        'surname as a separate Maryland query, because prefix matching '
                                        'misses records filed as Estate of John Doe when only Doe is '
                                        'typed. The utility typo found a deposit the correct spelling '
                                        'never surfaced [GardenShop.Pro — 1IpkVjkkXHg @ 00:03:58].'},
                            {'name': 'suspicious_contact_verification',
                             'type': 'textarea',
                             'prompt': 'Log every unexpected letter, email, check, or phone call about '
                                       'unclaimed money, then record the holder name and amount you looked '
                                       'up on the official state search and the verdict you reached before '
                                       'replying, clicking, or paying anything.',
                             'example': 'A mailer asked for a fee to reveal a balance; the holder name and '
                                        "amount were looked up on the state's official search instead of "
                                        'replying, and the site that wanted payment before showing results '
                                        'was abandoned. An Illinois Treasurer check was confirmed genuine '
                                        "and cashed, matching the treasurer's instruction [Nobody Asked, I "
                                        'Checked — z2nZM27w4qU @ 00:06:37] [WGN News — 4abzayS6yzk @ '
                                        '00:00:54].'},
                            {'name': 'automatic_return_status',
                             'type': 'text',
                             'prompt': "Note whether the owner's state proactively mails checks, what the "
                                       'automatic ceiling is, and whether the owner should still file '
                                       'manually, so that small balances are not chased when a state check '
                                       'is already likely to arrive.',
                             'example': 'New York verifies ownership and mails checks automatically on '
                                        'claims of $250 or less, paying out about $1.5 million a day, so a '
                                        '$140 record is left to the state. Montana now matches and mails '
                                        'up to $1,000 using tax records, but manual searches remain '
                                        'worthwhile for records that do not auto-match [NBC New York — '
                                        'wCk_H4rThTo @ 00:00:38] [GardenShop.Pro — 3iluxKs2wP8 @ '
                                        '00:02:43].'},
                            {'name': 'securities_liquidation_timing',
                             'type': 'textarea',
                             'prompt': 'For any escheated stock, bond, or brokerage position, record when '
                                       'it was turned over, whether the state has likely liquidated it, '
                                       'and how the sale timing affects the value the owner can expect to '
                                       'recover today.',
                             'example': 'A brokerage account reached California two years ago. California '
                                        'law requires the state to cash out stocks and investments within '
                                        '20 months of receipt, so the owner should expect the sale price '
                                        "at liquidation, not today's market value. The claim is filed "
                                        'immediately because California waits for owners to file rather '
                                        'than returning funds automatically [CBS News Sacramento — '
                                        '1Grj5UvPLwo @ 00:02:52].'},
                            {'name': 'claim_number_log',
                             'type': 'text',
                             'prompt': 'Record each claim number the moment it appears on screen, along '
                                       'with the state, filing date, documents uploaded, and the tracking '
                                       'method the state offers, so every later follow-up call references '
                                       'the exact file without delay.',
                             'example': 'Delaware claim number written down immediately after submission, '
                                        'filed March 3, with photo ID and proof of address uploaded. Texas '
                                        'claim tracked online after hitting claim and completing the free '
                                        "application. Delaware's check is reported arriving within two "
                                        'weeks, so a recheck is calendared for day fourteen [Michael '
                                        'Curtis — JGravBgJTJo @ 00:05:29] [KHOU 11 — WdhaqcAUXBk @ '
                                        '00:00:55].'},
                            {'name': 'document_packet_checklist',
                             'type': 'textarea',
                             'prompt': "List every document in the owner's claim packet, including photo "
                                       'ID, Social Security proof, current address proof, and prior '
                                       'address documentation, and mark which items are optional but speed '
                                       "processing on the specific state's form.",
                             'example': "Packet: driver's license, Social Security card, current utility "
                                        'bill, and an old lease proving the prior address. On '
                                        "Pennsylvania's form, Social Security number and date of birth "
                                        'carry no red asterisk but are entered anyway to speed the claim, '
                                        'since incomplete files are the most common trigger for a '
                                        'six-month denial [GardenShop.Pro — 3iluxKs2wP8 @ 00:06:08] '
                                        '[Michael Curtis — 0YK26E_fzYA @ 00:07:28].'},
                            {'name': 'setoffs_and_finder_caps',
                             'type': 'textarea',
                             'prompt': 'For each state in the file, record the finder fee ceiling, any '
                                       'written or notarized contract requirement, and any setoffs the '
                                       'state can take for taxes, child support, or court fines before '
                                       'paying the net balance to the owner.',
                             'example': 'New York caps location service providers at 15 percent under a '
                                        'written, notarized contract, and the state sends the full check '
                                        'to the owner, who then pays the provider. Kansas caps at 15 '
                                        'percent but intercepts delinquent state income taxes, child '
                                        'support, and court fines, so only the net balance is counted [Как '
                                        'се прави — 9BVp_yhswZY @ 00:05:25] [GardenShop.Pro — E2EtkM2OBvI '
                                        '@ 00:07:00].'},
                            {'name': 'utility_deposit_and_cash_deadline',
                             'type': 'textarea',
                             'prompt': 'Identify any utility deposits that may sit outside the state '
                                       'portal, the provider you must contact directly, and the date by '
                                       'which the owner must cash any state check before the funds risk '
                                       'becoming abandoned all over again.',
                             'example': 'Former Colorado service address: electric and gas deposits never '
                                        'reach the state portal, so Xcel Energy gets called at '
                                        '1-800-895-4999 with the old address, service dates, and Social '
                                        'Security number ready. A New York check received in May must be '
                                        'cashed by December 31 of the following calendar year '
                                        '[GardenShop.Pro — GWa4tWyuEoA @ 00:03:32] [Как се прави — '
                                        '9BVp_yhswZY @ 00:05:56].'}],
                 'completion_gate': 'Submit no claim until every relevant state portal has been searched '
                                    'under all name variants and old addresses, suspicious contacts are '
                                    'verified against official searches, the full document packet is '
                                    'assembled, setoffs and caps are priced in, and every claim number and '
                                    'cashing deadline is logged.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Business-Name Recovery, Investigator Requirements, and State Claim Filing',
                 'purpose': 'Recover funds held under company names by searching portals correctly, '
                            'stacking name, zip, and FEIN variants, proving ownership chains for merged or '
                            'dissolved entities, and filing as a properly licensed or registered '
                            'investigator under compliant agreements, disclosures, notarization rules, and '
                            'tracked shipping.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Enter every company name in the last name field with first name blank, '
                                  'and repeat the search across all name and zip code variants.',
                                  'Run FEIN searches and secondary state databases alongside the primary '
                                  'portal, and route federal amounts outside the state system entirely.',
                                  'Assemble the full ownership chain and officer authority before filing '
                                  'any merged, acquired, or dissolved entity claim with the state.',
                                  'Confirm license or registration status, locator timing windows, and fee '
                                  'caps in each state before any outreach begins.',
                                  'Disclose the nature and value of the property, ship every packet with '
                                  "tracking, and calendar each check's void date on the day it prints."],
                 'fields': [{'name': 'business_name_search_entry',
                             'type': 'text',
                             'prompt': 'Record how you entered each company name on every state portal, '
                                       'confirming the name went into the last name field with first name '
                                       'blank, and note any commercial records that appeared only after '
                                       'correcting the field placement.',
                             'example': "On North Dakota's portal the first attempt placed the company in "
                                        'the first name field and returned nothing. Re-entered in the last '
                                        'name field, first name blank, it surfaced two commercial records. '
                                        'Legal suffixes LLC, Inc., and Corp. were dropped on the first '
                                        'pass to widen the net [Как се прави — 7MUtjq4bwU0 @ 00:02:53] '
                                        '[Как се прави — RtDPQUDYTy0 @ 00:03:17].'},
                            {'name': 'variant_and_zip_matrix',
                             'type': 'textarea',
                             'prompt': 'List every corporate name variant you searched, including prior '
                                       'names, DBAs, acronyms, truncations, dropped suffixes, and acquired '
                                       'entities, plus the zip code of every former office location, and '
                                       'mark which combination produced each hit on each portal.',
                             'example': 'Searched current legal name, two DBAs, the company acronym, and '
                                        'an acquired subsidiary, then ran zip codes for three former '
                                        'offices. A refund check misspelled by a vendor ten years ago '
                                        'appeared only under the old zip code, which was the single way to '
                                        'spot it on the state list [GardenShop.Pro — rOaTjN9BoFE @ '
                                        '00:04:31].'},
                            {'name': 'fein_and_multiportal_search',
                             'type': 'textarea',
                             'prompt': 'Record the federal employer identification number used for each '
                                       'search, every portal where you ran it, and any secondary databases '
                                       'for uncashed government checks, vendor electronic payments, or '
                                       'municipal deposits that a primary state search would miss.',
                             'example': 'Tennessee searched on claimittn.gov by FEIN, a stronger match key '
                                        'than the precise name. In South Carolina three portals were run: '
                                        'the primary database, the outstanding state-issued checks '
                                        'database for government checks over two years old, and the vendor '
                                        'electronic payment search by EIN for missing ACH deposits '
                                        '[GardenShop.Pro — bUxdjo_bs0g @ 00:02:18] [Как се прави — '
                                        'KJU4iu_xIgw @ 00:03:10].'},
                            {'name': 'federal_exempt_assets',
                             'type': 'text',
                             'prompt': 'List any amounts a federal agency or federal bankruptcy court may '
                                       'owe the business, since these never escheat to a state, and record '
                                       'the separate channel you will use to pursue each one outside the '
                                       'multistate portal.',
                             'example': 'The corporation had a pending IRS refund and a creditor '
                                        'distribution from a federal bankruptcy case. Federal agencies are '
                                        'exempt from state escheatment laws, so neither will ever appear '
                                        'on missingmoney.com; both are routed to the federal bankruptcy '
                                        'court records and the agency directly, with no state portal '
                                        'treated as a final answer [Garden Shop Pro — 7Fc0D2RuIJE @ '
                                        '00:03:14].'},
                            {'name': 'ownership_chain_proof',
                             'type': 'textarea',
                             'prompt': 'Document the full legal ownership chain for any merged, acquired, '
                                       'or dissolved entity, listing the certified articles of merger or '
                                       'dissolution, the certificate of good standing, officer authority, '
                                       'and the historical address link tying the business to the record.',
                             'example': 'Colorado claim for a merged company: certified articles of '
                                        'merger, a certificate of good standing, proof of officer '
                                        'authority, and an old lease linking the reported address. The '
                                        'calendar is set for a six to twelve month audit of the legal '
                                        'lineage, versus 90 to 150 days for standard cash claims under '
                                        '$5,000 [Как се прави — 2_XKdBsmJ5c @ 00:03:58].'},
                            {'name': 'upload_and_payout_deadlines',
                             'type': 'text',
                             'prompt': 'Record the upload rules, file formats, and session limits for each '
                                       'state where you are filing, plus the exact date each state check '
                                       'is printed and the date it voids, so no payout lapses into a full '
                                       'refiling.',
                             'example': 'Colorado packet: PDF and JPEG only, each under 10 MB, no '
                                        'encryption, uploaded in two sessions of five files under the same '
                                        'numeric claim ID. A South Carolina check printed June 2 voids at '
                                        '90 days, so the deposit deadline is calendared for August 31 to '
                                        'avoid refiling from scratch [Как се прави — 2_XKdBsmJ5c @ '
                                        '00:04:44] [Как се прави — KJU4iu_xIgw @ 00:05:43].'},
                            {'name': 'locator_timing_and_fee_cap',
                             'type': 'textarea',
                             'prompt': 'For each target state, record the locator fee cap, the window '
                                       'after remittance during which any fee agreement is void or '
                                       'unenforceable, any required power of attorney form, and whether '
                                       'the state mails the check to the owner or the locator.',
                             'example': 'Missouri voids deals made in the first 12 months; Colorado voids '
                                        'the first 24 and caps fees at 10 percent. Georgia agents need a '
                                        'notarized UP 1061 power of attorney under a 10 percent cap, '
                                        'agreements are unenforceable for 24 months, and the check goes to '
                                        'the business [Как се прави — 2_XKdBsmJ5c @ 00:07:20] [Как се '
                                        'прави — WHTvjELqLw0 @ 00:06:40].'},
                            {'name': 'license_registration_status',
                             'type': 'textarea',
                             'prompt': 'Record your license or registration status in each state before '
                                       'any outreach, including the filing method, expected approval time, '
                                       'background check or fingerprint steps, sponsorship fees, and the '
                                       'consequences of performing investigative work without proper '
                                       'credentials.',
                             'example': 'California: registration packet emailed, approval usually arrives '
                                        'by email within a few days. Texas: DPS background check and '
                                        'fingerprinting, with agency sponsorship at $295 per year in place '
                                        'of three years of experience and an in-person exam. Charging '
                                        'above a cap can count as unlicensed investigative work and bar a '
                                        'PI license permanently [Unclaimed CEO — 3_qKwnM5EUw @ 00:03:32] '
                                        '[ShadowAnyone — 5gSBjAC1g0s @ 00:06:09].'},
                            {'name': 'agreement_terms_and_disclosure',
                             'type': 'textarea',
                             'prompt': 'Write the exact percentage on your investigator agreement, the '
                                       'validity term, every spot the claimant must initial, and the '
                                       'disclosure statement describing the nature and value of the '
                                       'property that you will deliver before the claimant signs.',
                             'example': 'California agreement written at 10 percent, valid for 12 months '
                                        'from claimant signature instead of the former six, with each '
                                        'initial spot flagged. The claimant is told the property is a '
                                        '$14,000 savings account before signing, because clause three '
                                        'voids the obligation if nature and value were not disclosed '
                                        '[Surplus Institute / David Church / Unclaimed Funds — D3Fcqm3xaco '
                                        '@ 00:04:35].'},
                            {'name': 'filing_shipment_and_estate_route',
                             'type': 'textarea',
                             'prompt': 'Describe how you will assemble, notarize, and ship each claim '
                                       'packet, including your cover sheet checklist, the notarization '
                                       'threshold, tracked delivery method, and the route you will use '
                                       'when the reported owner turns out to be deceased.',
                             'example': 'State filing instructions copied into a Google doc cover sheet '
                                        'checklist; the claim affirmation form is notarized because the '
                                        'value exceeds $1,000; the packet ships overnight with tracking. '
                                        'When the owner proves deceased, power of attorney use stops and '
                                        'the claim moves through a court-appointed personal representative '
                                        '[Unclaimed CEO — 2SYC3A6apHk @ 00:05:05] [GardenShop.Pro — '
                                        'dhZB_jSn2Qg @ 00:06:01].'}],
                 'completion_gate': 'File no business or investigator claim until the company has been '
                                    'searched correctly under every name, zip, and FEIN variant, the '
                                    'ownership chain is documented, registration is confirmed, the '
                                    'agreement sits at or under the state cap with full disclosure, and '
                                    'every packet and void date is tracked.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Skip Tracing, Heir Reconstruction, and Prospect Outreach',
                 'purpose': 'Rebuild the family behind a deceased or missing owner, reach the right living '
                            'claimant with paid tracing data and relative outreach, and open contact with '
                            'a data-loaded, compliant, credible approach that survives the trust deficit '
                            'every recovery agent faces.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ["Start with the reported owner's record and assume the owner may be "
                                  'deceased, since much state-held money belongs to people who died '
                                  'decades ago.',
                                  'Run paid tracing data before free people-search sites, and map '
                                  'relatives and associates as a primary route to the claimant rather than '
                                  'an afterthought.',
                                  "Document every generational link and check the target state's heirship "
                                  'rules before you promise any relative a share of the funds.',
                                  'Complete the DNC scrub, finder registry check, and fee cap check before '
                                  'the first dial, letter, or doorstep visit goes out.',
                                  'Keep the data sheet in front of you on every contact, log every '
                                  'objection, and repair any call that goes badly before the line goes '
                                  'cold.'],
                 'fields': [{'name': 'deceased_owner_profile',
                             'type': 'textarea',
                             'prompt': "Record the reported owner's full name, last known address, "
                                       'property type, and approximate date of death if known. Note '
                                       'whether the owner may have died decades ago, and list every name '
                                       'variant you will search for heirs and estate records.',
                             'example': 'Reported owner: Walter K. Simms, last known address on Elm '
                                        'Street, dormant savings balance near $14,000, death estimated '
                                        'around 1981. Variants queued: Walt Simms, W K Simms, Simms '
                                        'Walter, plus a separate Estate of Walter Simms search, because '
                                        'prefix matching misses records filed under the estate name when '
                                        'only the surname is typed [GardenShop.Pro — 1IpkVjkkXHg @ '
                                        '00:03:58].'},
                            {'name': 'skip_trace_tool_stack',
                             'type': 'text',
                             'prompt': 'List the paid tracing services you will run on this file, the '
                                       'per-record or monthly cost of each, and why paid data beats free '
                                       'people-search sites for reaching a living heir or ex-owner on the '
                                       'first attempt. Note the expected accuracy.',
                             'example': 'Primary: Tracers at about a $10 setup plus $1.50 per skip, which '
                                        'Joe Green calls trivial once ten deals return $10,000 to $20,000 '
                                        '[Unclaimed CEO — Qf591_R7CN4 @ 00:03:36]. Backup: Skip Matrix at '
                                        'a maximum of $0.14 per matched record with misses refunded [Money '
                                        'Making Juggernaut — XEcv7z100aA @ 00:18:05]. Free sites skipped '
                                        'as first pass at 40 to 60% accuracy.'},
                            {'name': 'relatives_and_associates_map',
                             'type': 'textarea',
                             'prompt': "Map every relative and associate attached to the owner's record, "
                                       'including siblings, children, in-laws, and former neighbors. For '
                                       'each, note the newest phone number, mailing address, and why that '
                                       'person is likely to pass your message to the claimant.',
                             'example': 'Relatives found: daughter Carla Simms Ortiz, newest-dated mobile '
                                        "number first, since kids keep deceased parents' phone numbers "
                                        '[Surplus Institute / David Church / Unclaimed Funds — hA6VJ_GqGyc '
                                        "@ 00:00:39]. Aunt May Harlow gets a letter under the ex-owner's "
                                        'name, the outreach Sean Boujie credits with a 40 to 50 percent '
                                        'hit-rate lift [SurplusFundsRiches — ujbTh1In_c4 @ 00:02:37].'},
                            {'name': 'heir_chain_and_state_rules',
                             'type': 'textarea',
                             'prompt': 'Document the full generational heir chain from the reported owner '
                                       "to each living claimant, and record the target state's heirship "
                                       'rules on stepchildren, marriage at death, wills, and marriage '
                                       'duration before you promise any relative a share of the funds.',
                             'example': 'Chain: Walter Simms, died 1981, to son Robert, died 2015, to '
                                        'grandchildren Dana and Lee. Every link is documented because one '
                                        'missing generational link stalls or denies the claim '
                                        '[GardenShop.Pro — J2nto2DAwqc @ 00:04:46]. Stepdaughter Pam '
                                        'excluded in Texas, which denied a stepchild that California would '
                                        'have recognized [Surplus Institute / David Church / Unclaimed '
                                        'Funds — 2l827py8Fe8 @ 00:02:42].'},
                            {'name': 'owner_match_verification',
                             'type': 'text',
                             'prompt': 'Explain how you confirmed that the person you found is the true '
                                       "owner or heir, including whether you uploaded the prior owner's "
                                       'name plus address rather than running an address-only lookup, and '
                                       'which secondary records corroborated the match.',
                             'example': 'Sale is eight months old, so the batch upload used prior owner '
                                        'name plus address, not address alone [Money Making Juggernaut — '
                                        'aKzRVyO_gfI @ 00:29:37]. Corroboration: undeliverable mail '
                                        'returned with a forwarding order expired notice still printing '
                                        'the new Maple Court address [SurplusFundsRiches — ujbTh1In_c4 @ '
                                        '00:04:17], and the Georgia energy website shows who pays the '
                                        'utility bills there.'},
                            {'name': 'dnc_and_registration_check',
                             'type': 'text',
                             'prompt': 'Before any dial or mailer, confirm the file passed a Do Not Call '
                                       "scrub, that you appear on the state's finder registry where one "
                                       'exists, and that your proposed contingency percentage sits at or '
                                       "under the state's posted cap.",
                             'example': 'All four skip-traced numbers scrubbed against the DNC list, '
                                        'dialed one at a time on a power dialer, no voicemail drops, after '
                                        'one unscrubbed contact became a federal class action [Money '
                                        'Making Juggernaut — Zh5fus4SGzc @ 00:02:21]. Pennsylvania finder '
                                        'registry checked, since FOX43 named an unregistered finder on air '
                                        '[FOX43 News — gEVKR-AmaU0 @ 00:02:41]. Fee set at 10%.'},
                            {'name': 'data_loaded_opener',
                             'type': 'textarea',
                             'prompt': 'Write the opening lines of your first call, naming the payer, the '
                                       'property address, the dormant date, and an approximate amount. '
                                       'Keep the data sheet in front of you so you never land on the wrong '
                                       'name mid-call.',
                             'example': 'Opener: This is regarding a dormant account from First Valley '
                                        'Bank tied to 412 Elm Street, dormant since 2016, about $1,158 '
                                        'held by the state; the file was assigned to me, and it is 10% '
                                        'with no upfront cost. Church credits the data with saving every '
                                        'call [Surplus Institute / David Church / Unclaimed Funds — '
                                        'wp5vC44yQQg @ 00:05:08].'},
                            {'name': 'outreach_channel_plan',
                             'type': 'textarea',
                             'prompt': 'Choose your primary and backup outreach channels for this '
                                       'prospect, such as phone, letter, greeting card, or doorstep visit. '
                                       'State the per-piece cost, the follow-up count you commit to, and '
                                       "why that channel fits this prospect's trust level.",
                             'example': 'Primary: Stamp letter at $0.85 per piece, with postcards at '
                                        '$0.73, mailed to both skip-traced addresses [Money Making '
                                        'Juggernaut — 8hCl2lLNDrk @ 00:01:00]. Backup: the prospect lives '
                                        'inside a 20 mile radius with a sizable account, so a doorstep '
                                        'visit follows [Unclaimed CEO — WlbnzGtdoSY @ 00:04:39]. Phone '
                                        'follow-up committed at three to five calls.'},
                            {'name': 'credibility_assets',
                             'type': 'text',
                             'prompt': 'List the legitimacy assets a skeptical prospect can verify before '
                                       'handing over a Social Security card or ID, such as a live website, '
                                       'registry listing, QR-coded mailer, or business card, and confirm '
                                       'each one is working today.',
                             'example': 'Live website with registration number and contact page confirmed '
                                        'before requesting any ID, because prospects who cannot verify the '
                                        'investigator ghost after notary and shipping money is spent '
                                        '[Unclaimed CEO — 97wh_A16P2s @ 00:14:01]. Local area code number '
                                        'set up, since prospects ignore unfamiliar area codes [Unclaimed '
                                        'CEO — 97wh_A16P2s @ 00:04:33]. QR-coded mailer links to the '
                                        'site.'},
                            {'name': 'objection_and_recovery_log',
                             'type': 'textarea',
                             'prompt': 'Log each objection the prospect raised, such as denial of '
                                       'ownership, scam suspicion, or a demand to file alone, along with '
                                       'your response and the next touch. Note any call that went badly '
                                       'and how you repaired it.',
                             'example': 'Prospect denied being the owner, so the record kept coming: '
                                        'address, payer, dormant date, and the $1,158 amount; Church '
                                        'reports one heated prospect called back and signed [Surplus '
                                        'Institute / David Church / Unclaimed Funds — wp5vC44yQQg @ '
                                        '00:06:11]. Second call ran hot, an apology text followed to keep '
                                        'the line open [FundSleuth - Unclaimed Funds Info and Training — '
                                        'rQqA2wnJ9xw @ 00:04:10].'}],
                 'completion_gate': 'Do not make first contact until the heir chain has no missing '
                                    'generational link, the owner match is confirmed with name plus '
                                    'address, every number is DNC-scrubbed, your registry status and fee '
                                    'cap are verified, and a live website is ready for the prospect to '
                                    'check.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Closing Claims, Collecting Fees, and Bankruptcy Recoveries',
                 'purpose': 'Turn a willing claimant into a filed, paid claim and a collected fee by '
                            'choosing the right fee model, writing protective agreement clauses, shipping '
                            'clean packets, researching bankruptcy balances, and reconciling every payout '
                            'against its signed contract.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Never ask for money before the client is paid on contingency files; use '
                                  'flat upfront invoicing only where the county packet model applies.',
                                  'Write the approximate amount, agreed percentage, accrued interest '
                                  'treatment, and separate cost billing into the agreement before anything '
                                  'is filed.',
                                  'Send only the documents the filing instructions request, and chase '
                                  'every missing signature or notarization with a concrete, specific '
                                  'message.',
                                  'Resolve any bankruptcy balance discrepancy with the clerk, trustee, or '
                                  'courtroom deputy before quoting an amount to the owner.',
                                  'Save the contract, invoices, and every email before filing, and match '
                                  'each payout to its contract percentage before distributing funds.'],
                 'fields': [{'name': 'fee_structure_decision',
                             'type': 'textarea',
                             'prompt': 'Decide the fee model for this claim: flat packet fee, contingency '
                                       'percentage, or a higher split for paperwork-heavy estate work. '
                                       'Record the claim size, the state or county cap, and why the chosen '
                                       'structure fits the effort required.',
                             'example': 'County claim of $4,200 falls inside the $500 to $8,000 band, so a '
                                        '$150 flat packet invoiced before work begins; anything $10,000 '
                                        'and up moves to 15% to 30% contingency [Money Making Juggernaut — '
                                        'xocEKVSCJtU @ 00:08:13]. A paperwork-heavy estate overage near '
                                        '$15,000 would justify the 40% finder split Church used [Surplus '
                                        'Institute / David Church / Unclaimed Funds — V_ycS3i_CMY @ '
                                        '00:03:17].'},
                            {'name': 'agreement_clauses',
                             'type': 'textarea',
                             'prompt': 'List the clauses written into the recovery agreement, including '
                                       'the approximate amount, the agreed percentage, treatment of '
                                       'accrued interest, and separate billing for probate or lawyer '
                                       'costs. Confirm the percentage sits at or below the governing cap.',
                             'example': 'Clause 2 applies the agreed percentage to any interest accrued at '
                                        "the treasury, the structure that lifted Jay's New Jersey estate "
                                        'fee from $18,000 to $31,000 [Money Making Juggernaut — '
                                        'ZvJ4yCc9em4 @ 00:04:22]. Clause 4 bills probate costs on '
                                        'deceased-owner files separately from the 10% recovery fee [Money '
                                        'Making Juggernaut — vp2uuB23fww @ 00:34:21].'},
                            {'name': 'filing_packet_contents',
                             'type': 'textarea',
                             'prompt': 'Itemize every document going into the filing packet, such as the '
                                       'agreement form, claim form, identification, and notarized power of '
                                       'attorney. Mark anything the filing instructions do not request, '
                                       'and remove it before the packet ships with tracking.',
                             'example': 'Packet: agreement form, claim form, and proof of identification, '
                                        'the three core items for a court claim [Money Making Juggernaut — '
                                        '91o6wv-g6D0 @ 00:03:17], plus notarized power of attorney. '
                                        "Removed the client's old tax return because extras slow "
                                        'processing and delay both paydays [Unclaimed CEO — pZG8hK4VPVM @ '
                                        '00:02:23]. Shipped overnight with tracking number logged.'},
                            {'name': 'notary_and_paperwork_follow_up',
                             'type': 'textarea',
                             'prompt': 'Describe how you will get missing signatures, notarizations, or '
                                       'client documents returned, including mailed paper copies for '
                                       'clients who are not computer literate, mobile notary offers, and '
                                       "the exact follow-up message you will send when only the client's "
                                       'items remain.',
                             'example': 'Client is not computer literate, so documents went by mail with a '
                                        'scheduled notary [Surplus Institute / David Church / Unclaimed '
                                        'Funds — V_ycS3i_CMY @ 00:04:12]. Contract came back but the '
                                        'affidavit stayed unnotarized, so a covered mobile notary was '
                                        'offered [Spring Solutions, LLC — YKjd__UIhB8 @ 00:08:53]. Text '
                                        'sent: my portion is finished; your two documents are all that '
                                        'remain.'},
                            {'name': 'crm_prospect_record',
                             'type': 'text',
                             'prompt': 'Enter the CRM record for this prospect before any callback '
                                       'arrives: claim amount, quoted percentage, working phone and email, '
                                       'preferred communication method, date of last contact, and the next '
                                       'scheduled follow-up step with its due date. Never rely on memory '
                                       'alone.',
                             'example': 'Prospect: Denise Fowler, $1,117.83 Western District of Missouri '
                                        'balance, quoted 30%, mobile verified, prefers text, last contact '
                                        'November 3, follow-up November 10. Logged the same day the mailer '
                                        'went out, because Porter describes forgetting mailed prospects '
                                        "and struggling to reconstruct conversations; Porter's rule is "
                                        'simple: update your CRM [Spring Solutions, LLC — YKjd__UIhB8 @ '
                                        '00:03:26].'},
                            {'name': 'bankruptcy_balance_research',
                             'type': 'textarea',
                             'prompt': 'Record the bankruptcy district, case number, located balance, and '
                                       'entitled party for this file. Note what the docket and claims '
                                       'register show, and list every discrepancy between figures that '
                                       'must be resolved before you quote an amount to the owner.',
                             'example': 'Middle District of Alabama case shows a locator balance that does '
                                        'not match the claims register distribution. Following Porter, the '
                                        "clerk, the trustee's office, and the courtroom deputy were all "
                                        'contacted before any amount went to the owner [Spring Solutions, '
                                        'LLC — y2j1Ux0R9jY @ 00:06:02]. Docket read in full, since '
                                        'explaining entitlement requires it [Money Making Juggernaut — '
                                        'EyQovsqVOnE @ 00:02:45].'},
                            {'name': 'payout_timeline_expectation',
                             'type': 'text',
                             'prompt': 'State the payout window you will quote the client for this claim '
                                       'type, the source of that estimate, and how you will explain delays '
                                       'if the actual payout runs longer than expected or arrives in a '
                                       'different form than promised.',
                             'example': "State-level claim quoted at 16 to 120 days, Richardson's range "
                                        'across niches [Money Making Juggernaut — 7WZONOtYbjc @ 00:02:36]. '
                                        'Bankruptcy claim quoted with a caution that actual payouts have '
                                        "exceeded the 30 to 60 day expectation. Church's $54,000 state "
                                        'claim took roughly four months before the invoice went out '
                                        '[Surplus Institute / David Church / Unclaimed Funds — kb-pXZgQdoE '
                                        '@ 00:00:57].'},
                            {'name': 'invoice_and_collection',
                             'type': 'textarea',
                             'prompt': 'Describe how you will collect the fee after the client is paid, '
                                       'including the invoice format, the payment instrument you will '
                                       'request, and the exact steps you will take if the client stops '
                                       'responding or refuses to pay.',
                             'example': 'Professional invoice showing the claim amount and the 10% owed, '
                                        "payable by cashier's check, the method that returned $5,400 on a "
                                        '$54,000 claim [Surplus Institute / David Church / Unclaimed Funds '
                                        '— kb-pXZgQdoE @ 00:00:57]. If ignored: 10-day letter, then '
                                        "small-claims complaint, judgment, and garnishment; Porter's "
                                        '$1,100 holdout arranged payment once a suit was mentioned [Spring '
                                        'Solutions, LLC — 2Q7vcVR_cDs @ 00:03:53].'},
                            {'name': 'dispute_evidence_file',
                             'type': 'text',
                             'prompt': 'List the evidence you have saved in case the client goes around '
                                       'you or refuses to pay: signed contract, invoices, emails, texts, '
                                       'and call notes. Record the statute-of-limitations window for suing '
                                       'on a contract in your state.',
                             'example': 'Saved before filing: signed contract, invoice, and every email, '
                                        'the three exhibits Porter attached to a lawsuit inside a '
                                        'three-year Maryland window to sue on a contract [Spring '
                                        'Solutions, LLC — 2Q7vcVR_cDs @ 00:02:50]. Texts with photographed '
                                        "signed contract archived. Church's advice on clients who go "
                                        'around you: deal with it [Surplus Institute / David Church / '
                                        'Unclaimed Funds — RjCjrBjQF7Y @ 00:09:55].'},
                            {'name': 'payout_reconciliation',
                             'type': 'textarea',
                             'prompt': 'When multiple payouts arrive together, match each check to its '
                                       'signed contract, confirm the agreed percentage, and calculate the '
                                       "client's share and your commission before distributing anything. "
                                       'Record any mismatch between the contract terms and the amount '
                                       'received.',
                             'example': 'Two court checks arrived the same day. Western District of '
                                        'Missouri: $1,117.83 at 30% yields a $335.34 commission [Spring '
                                        'Solutions, LLC — ckzrLZgtcYI @ 00:02:52]. Each contract was '
                                        'pulled and its percentage confirmed before distribution, since '
                                        'paying a client the wrong amount breaches the arrangement [Spring '
                                        'Solutions, LLC — ckzrLZgtcYI @ 00:05:21]. Client share: '
                                        '$782.49.'}],
                 'completion_gate': 'Do not file until the agreement covers accrued interest and sits at '
                                    'or under the cap, the packet holds only requested documents, any '
                                    'balance discrepancy is resolved, the CRM record is current, and the '
                                    'signed contract, invoice, and emails are saved as dispute evidence.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Royalties, Insurance, Shares, and Holder Compliance',
                 'purpose': 'Recover specialty assets such as royalties, life insurance, shares, and '
                            'dividends with correct heirship and estate paperwork, and, on the holder '
                            'side, build a filing calendar, exposure assessment, and audit response plan '
                            'that keeps penalties and look-backs contained.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Identify the dormancy clock and custodian for each asset type before '
                                  'sizing any claim, because royalties, insurance, shares, and wages '
                                  'escheat on different timelines.',
                                  'Run every free search across each state of residence or work before any '
                                  'paid locator, and log every request ID you receive.',
                                  'Confirm the estate document names each share, royalty, or policy being '
                                  'claimed, and secure an addendum for anything it omits.',
                                  'On the holder side, map every reporting deadline, due diligence '
                                  'threshold, and exposure area, and hunt for exemptions before remitting.',
                                  'When an audit notice or VDA invitation arrives, pull participating '
                                  'states from the states themselves and decide within the stated window.'],
                 'fields': [{'name': 'royalty_dormancy_and_operator',
                             'type': 'text',
                             'prompt': 'Identify the royalty interest, the operator that issued the '
                                       'payments, the state holding the escheated funds, and the dormancy '
                                       'period that applied. Record the date the clock started: last '
                                       'contact, check issue, or payable date, whichever was most recent.',
                             'example': 'Texas mineral interest; royalties coded MI02, abandoned after 3 '
                                        'years of inactivity versus 1 year for MS01 wages [txcomptroller — '
                                        'rGLI7Ry3sF0 @ 00:01:45]. Clock started at the last check issue '
                                        'date in 2020. A Louisiana tract on the same lease runs a two-year '
                                        'dormancy [PakEnergy — fVMIbCz8s0U @ 00:19:42]. Operator letter '
                                        'queued to redirect future checks.'},
                            {'name': 'heirship_route_and_texas_cap',
                             'type': 'textarea',
                             'prompt': 'For a deceased royalty owner, size the claim against the Texas '
                                       'affidavit-of-heirship ceiling, choose between an affidavit and '
                                       'probate paperwork, and confirm any finder agreement is written, '
                                       'capped at 10%, and held by a DPS-licensed finder who does not file '
                                       'the claim.',
                             'example': 'Escheated royalties total $8,600, under the $10,000 '
                                        'affidavit-of-heirship ceiling, so the affidavit route applies '
                                        '[Royalty Clerk — 8RccEFzRtl8 @ 00:03:50]. Finder agreement is '
                                        'written, set at 10% of what is recovered with no share of '
                                        'minerals or overriding royalty, and the licensed finder does not '
                                        'file the claim [Royalty Clerk — 8RccEFzRtl8 @ 00:04:39].'},
                            {'name': 'life_insurance_trace',
                             'type': 'textarea',
                             'prompt': 'Record the order in which you will search for a lost life '
                                       'insurance policy, including free state and national locators '
                                       'before any paid service, the cost of each step, and every request '
                                       'ID you receive along the way.',
                             'example': 'Step 1: NAIC policy locator, request ID logged. Step 2: '
                                        'missingmoney.com sweep across every state of residence and work. '
                                        'Step 3, an absolute last resort: MIB at $75, covering policies '
                                        'after 1995 [Garden Shop Pro — HMzGGSvJ104 @ 00:04:40]. Anyone '
                                        'demanding fees up front is refused, and each request ID is logged '
                                        '[Garden Shop Pro — HMzGGSvJ104 @ 00:05:43].'},
                            {'name': 'share_and_dividend_recovery',
                             'type': 'textarea',
                             'prompt': 'For unclaimed shares or dividends, record the registrar, the '
                                       'custodial fund holding the money, the dormancy rule that moved it, '
                                       'and the exact amount due as confirmed by the registrar rather than '
                                       'a broker before any recovery spending.',
                             'example': "Indian shares: only the specific unpaid year's dividend transfers "
                                        "to the IEPFA, so encashing the 2022 dividend stops that year's "
                                        'transfer [Mint — Y4d3T6BNtEg @ 00:02:24]. Nigerian holding: '
                                        'amount due requested from the registrar, not the broker, because '
                                        'taking two naira to collect one naira is unwise [Broadstreet '
                                        'Radio — ykLXSnb1CRE @ 00:45:47].'},
                            {'name': 'estate_document_coverage',
                             'type': 'text',
                             'prompt': 'Confirm the letter of administration or will names every share, '
                                       'royalty, or policy being claimed. List each asset, whether it '
                                       'appears in the estate document, and the addendum or supplemental '
                                       'filing needed for anything the document omits.',
                             'example': 'Letter of administration lists the bank shares but omits the '
                                        'dividend warrants, so an addendum is requested before filing, '
                                        'since any letter that does not mention the instruments claimed is '
                                        'not proper [Broadstreet Radio — ykLXSnb1CRE @ 00:11:10]. Claiming '
                                        'the suspended royalties alongside can help cure title and restore '
                                        'pay status [Blue Mesa Minerals — HSmuF8xIaIU @ 00:07:55].'},
                            {'name': 'holder_filing_calendar',
                             'type': 'textarea',
                             'prompt': 'As a holder, list every state where you must report, the report '
                                       'and payment deadline for each, the due diligence letter threshold '
                                       'and timing window, and the person responsible for filing. Include '
                                       'negative reports where a state requires one.',
                             'example': 'Utah: report and payment both due November 1, paid electronically '
                                        'at mycash.utah.gov [Utah Office of State Treasurer — hUiiEXcFE0k '
                                        '@ 00:03:20]. Texas: July 1 deadline, $250 notice floor. South '
                                        'Carolina: letters on items of $50 or more, sent no more than 120 '
                                        'days before filing. Tennessee: negative report filed. '
                                        'Responsible: corporate controller, calendar reviewed quarterly.'},
                            {'name': 'exposure_assessment',
                             'type': 'textarea',
                             'prompt': 'Identify where your unclaimed property exposure hides, including '
                                       'receivable credit balances, voided and stale checks swept into '
                                       'miscellaneous income, and industry property types you have never '
                                       'reported. Estimate the dollar amount and years affected for each '
                                       'area.',
                             'example': 'Accounts receivable credit balances flagged first, the area a '
                                        'former state auditor says drove much company exposure [SimekScott '
                                        'LLC — p0UoXSbya5E @ 00:01:52]. Voided check register shows '
                                        '$18,400 swept to miscellaneous income since 2019; that practice '
                                        'stops, because those items become unclaimed property within three '
                                        'to five years [Friedman LLP — duwB7Y82flc @ 00:27:10].'},
                            {'name': 'exemption_review',
                             'type': 'text',
                             'prompt': 'Before remitting, list every exemption you have reviewed, such as '
                                       'recoupment, business-to-business, and de minimis, with the statute '
                                       'or regulation supporting each. Note your goal of being compliant '
                                       'without being overly compliant, and who signed off on each '
                                       'decision.',
                             'example': 'Healthcare holder reviewed recoupment, business-to-business, and '
                                        'de minimis exemptions out of roughly 100 opportunities Kodiak '
                                        'counts, aiming to be compliant but not overly compliant [Kodiak '
                                        'Solutions — 2BplqmdsUpU @ 00:28:08]. Statutes and actual state '
                                        'practice were studied before the auditor asked, since auditor '
                                        'interpretations often miss what statutes require [COMPUTERSHARE — '
                                        '03CoUEgqdzg @ 00:01:47]. Counsel signed off.'},
                            {'name': 'audit_notice_response',
                             'type': 'textarea',
                             'prompt': 'When an audit notice or Delaware VDA invitation arrives, record '
                                       'the date received, the participating states as listed in each '
                                       "state's own notification, the 90-day decision deadline, and "
                                       'whether you will enter voluntary disclosure or prepare to contest.',
                             'example': 'Delaware VDA invitation received March 3; decision due within 90 '
                                        'days or the file is referred for audit [SimekScott LLC — '
                                        'TGu6R9Pc0-4 @ 00:00:19]. Participating states pulled from each '
                                        "state's notification, not the auditor's list, which may include "
                                        'every contracted state [COMPUTERSHARE — 79d39hagJ6U @ 00:00:40]. '
                                        'Voluntary disclosure chosen for the roughly ten-year look-back '
                                        'and waived penalties.'},
                            {'name': 'penalty_and_acquisition_risk',
                             'type': 'textarea',
                             'prompt': 'Quantify penalty exposure if you fail to file, using the '
                                       "applicable state's daily penalty and percentage-of-value rules, "
                                       'and record who bears unclaimed property responsibility for each '
                                       'period in any pending acquisition or merger purchase agreement. '
                                       'Name the counsel reviewing it.',
                             'example': 'Tennessee willful failure: $1,000 per day up to $25,000, plus 25% '
                                        'of the property value, avoided by upfront disclosure through the '
                                        'CDA program [TNTreasury — KiR-ZUeCE5g @ 00:02:45]. Pending '
                                        'acquisition: escheatment counsel engaged, and the purchase '
                                        'agreement assigns seller responsibility for pre-closing periods '
                                        '[SimekScott LLC — p0UoXSbya5E @ 00:04:59]. Interest and penalty '
                                        'can exceed 50% elsewhere.'}],
                 'completion_gate': 'Do not file a specialty claim or a holder report until the dormancy '
                                    'clock and custodian are confirmed, the estate document names every '
                                    'asset claimed, the amount due comes from the registrar, every request '
                                    'ID is logged, exemptions are reviewed, and audit-state lists come '
                                    'directly from the states.'}]}
