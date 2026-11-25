from __future__ import annotations

def build_volume_048_workbook() -> dict:
    return {'workbook_id': 'wb-048-qui-tam-sec-and-irs-whistleblower-analytics',
 'volume_id': 'vol-048-qui-tam-sec-and-irs-whistleblower-analytics',
 'title': 'Data-Mined Qui Tam, SEC & IRS Whistleblower Analytics — Practitioner Testimony Operator '
          'Workbook',
 'subtitle': 'A field workbook for screening, building, and sealing qui tam cases, from materiality and '
             'relator share through intervention odds, data-mined enforcement, billing fraud red flags, '
             'and Stark and Anti-Kickback referral exposure',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Qui Tam Case Viability and Relator Intake Screen',
                 'purpose': 'Test whether a suspected fraud satisfies the False Claims Act engine of '
                            'falsity, materiality, knowledge, and federal money. Then size the damages, '
                            'measure relator exposure, and lock down silence and disclosure sequencing '
                            'before counsel files a sealed complaint under the first-to-file rule.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Complete every field in writing before the first call with '
                                  'whistleblower counsel, and keep the worksheet itself off shared '
                                  'devices, cloud summaries, and AI tools.',
                                  'Answer the government-money and materiality fields first; if no federal '
                                  'agency lost money or the defect is cosmetic, stop and reassess the '
                                  'theory.',
                                  'Write damages as pre-trebling figures with the arithmetic shown, then '
                                  'apply treble damages and per-claim penalties on a separate line.',
                                  'Be blunt in the dirty-hands and silence fields, because counsel can '
                                  'only protect an award share and original-source status against facts it '
                                  'knows.',
                                  'Date every entry, and update the limitations and disclosure fields '
                                  'whenever new conduct, documents, or contacts emerge.'],
                 'fields': [{'name': 'federal_money_link',
                             'type': 'text',
                             'prompt': 'Identify the specific federal dollar connected to the suspected '
                                       'lie. Name the paying program, the agency that lost the money, and '
                                       'how each claim, invoice, or certification moved from the defendant '
                                       'to that payer during the period you observed.',
                             'example': 'A cardiology group bills Medicare and Medi-Cal for monitoring '
                                        'never performed. Medi-Cal is 50% federal money, so a parallel '
                                        'California count rides alongside the federal one [Beverly Hills '
                                        'Bar Association — yN7NRjwYKFs @ 00:12:13]. Without government '
                                        'money and an identifiable agency that lost it, there is no '
                                        'traditional False Claims Act case [Tony Munter Attorney at Law — '
                                        'IX4WhZTmPRI @ 00:01:46].'},
                            {'name': 'materiality_test',
                             'type': 'textarea',
                             'prompt': 'Describe why the payer would refuse to pay if it knew the truth. '
                                       'Separate defects that go to the essence of the bargain from '
                                       'cosmetic deviations, and record any evidence that the payer '
                                       'previously paid despite knowing about the problem.',
                             'example': 'Out-of-spec military parts pass the materiality test because the '
                                        'government would refuse to pay for them; wrong-color parts do not '
                                        '[Justia — HocnawRgrAA @ 00:23:01]. Record here whether the '
                                        'deviation affects performance or merely appearance, and note that '
                                        'per-claim penalties stack on top of treble damages once '
                                        'materiality holds [Justia — HocnawRgrAA @ 00:23:57].'},
                            {'name': 'knowledge_standard',
                             'type': 'textarea',
                             'prompt': 'State what the defendant knew and how you can show it. Note '
                                       'whether the evidence points to actual knowledge, deliberate '
                                       'indifference, or reckless disregard, and list the specific emails, '
                                       "meetings, or instructions that reveal the decision-makers' state "
                                       'of mind.',
                             'example': 'The statute does not require intent to defraud; reckless '
                                        'disregard and deliberate indifference are enough [Beverly Hills '
                                        'Bar Association — yN7NRjwYKFs @ 00:31:35]. Example entry: the '
                                        'billing manager was told twice in writing that incident-to claims '
                                        'lacked physician presence and kept submitting them. Practitioners '
                                        'still split on how demanding the knowledge standard should be, so '
                                        'plead the strongest documents first.'},
                            {'name': 'damages_estimate',
                             'type': 'textarea',
                             'prompt': 'Estimate actual damages before trebling, then multiply by three '
                                       'and add per-claim penalties. Show the number of claims, the '
                                       'average claim value, your arithmetic, and the documents behind '
                                       'each figure so counsel can test whether the case clears intake '
                                       'thresholds.',
                             'example': 'Brown, LLC generally looks for $10 million in actual damages '
                                        'before trebling, applied on a sliding scale against proof '
                                        'strength and solvency [Brown, LLC - A Premier Whistleblower Law '
                                        'Firm — Hb6Ogl9Fm8I @ 00:02:58]. Do not self-reject a smaller '
                                        'number; state it, explain the math, and show the proof [Brown, '
                                        'LLC - A Premier Whistleblower Law Firm — Hb6Ogl9Fm8I @ '
                                        '00:04:01].'},
                            {'name': 'limitations_window',
                             'type': 'text',
                             'prompt': 'Map the full ten-year window of conduct you can document. Record '
                                       'the earliest and latest dates of the scheme, when your employment '
                                       'ended, and whether the conduct continued afterward, so damages '
                                       'accrued during the seal period are not left out.',
                             'example': 'Hamilton and Newman always plead 10 years, because damages keep '
                                        'accruing after the relator leaves and while the case sits under '
                                        'seal [Justia — HocnawRgrAA @ 00:27:22]. That matters: the seal '
                                        'runs 60 days on paper but about 2.5 years in practice, and DOJ '
                                        'averages about 11 months to decide intervention [Phillips & Cohen '
                                        'LLP — 5-ptDaAQkvI @ 00:37:27].'},
                            {'name': 'relator_profile_and_share',
                             'type': 'text',
                             'prompt': 'Classify yourself as an insider with documents or an outsider '
                                       'working from public data. Explain the source of your knowledge, '
                                       'the realistic award percentage for that profile, and any facts '
                                       'that could move the share toward the top of the range.',
                             'example': 'Insiders can collect 15 to 30 percent of whatever the government '
                                        'recovers by settlement or judgment [Justia — HocnawRgrAA @ '
                                        '00:05:11], while PPP data-mining outsiders are paid about 10 '
                                        'percent [Justia — HocnawRgrAA @ 00:32:07]. Brown, LLC also '
                                        'scrutinizes outsider cases built from ProPublica PPP records '
                                        'harder than insider cases, so document firsthand knowledge '
                                        'wherever it exists.'},
                            {'name': 'dirty_hands_audit',
                             'type': 'textarea',
                             'prompt': 'Measure your own involvement honestly before moving forward. '
                                       'Describe what you did, what you knew and when, whether you '
                                       'received any money from the scheme, and how long you waited after '
                                       'learning of it before seeking counsel.',
                             'example': 'Masterminding, profiting, or delaying the report drastically '
                                        'reduces the award, so think about how dirty your hands are before '
                                        'starting [Brown, LLC - A Premier Whistleblower Law Firm — '
                                        '3ugChIElhkM @ 00:10:00]. Follow the dough on any bonus you '
                                        'received, and remember that blowing the whistle does not grant '
                                        'immunity [Brown, LLC - A Premier Whistleblower Law Firm — '
                                        'CZeUV80NaAA @ 00:05:24].'},
                            {'name': 'silence_log',
                             'type': 'textarea',
                             'prompt': 'List every person you have told about the fraud, every post you '
                                       'have written, and every outside contact you plan. Flag any press, '
                                       'social media, or comment-section activity and any co-worker who '
                                       'could become a rival filer.',
                             'example': 'Do not go to the newspaper or the press; going public can blow '
                                        'original-source status [Levin Papantonio — xH5IpDAiP5c @ '
                                        '00:00:36]. Before approaching a former biller as a collaborator, '
                                        'have the complaint nearly finished, because a co-worker who '
                                        'refuses can turn around and file first [Brown, LLC - A Premier '
                                        'Whistleblower Law Firm — 3ugChIElhkM @ 00:04:54].'},
                            {'name': 'lawful_access_inventory',
                             'type': 'textarea',
                             'prompt': 'Inventory each piece of evidence and explain how you lawfully '
                                       'accessed it in your normal role. Note whether you photographed or '
                                       'copied it, where originals remain, and whether any summary or AI '
                                       'tool has touched the material.',
                             'example': 'Take pictures of documents rather than walking out with them '
                                        '[Beverly Hills Bar Association — yN7NRjwYKFs @ 00:36:16]. The '
                                        'government will ask how you knew and whether access was lawful '
                                        '[Brown, LLC - A Premier Whistleblower Law Firm — 39Q-yYGWPVg @ '
                                        '00:03:55]. Do not run documents through AI or draft a summary '
                                        'before calling counsel [Stephen Teller - Teller Law — SiATzxJHy2Y '
                                        '@ 00:06:42].'},
                            {'name': 'disclosure_sequencing',
                             'type': 'textarea',
                             'prompt': 'Plan the order of your government contacts. Record when the '
                                       'written disclosure statement with all material evidence will be '
                                       'served, when the sealed complaint will be filed, and which '
                                       'civil-frauds AUSA or attorney will receive the initial outreach.',
                             'example': 'Serve the written disclosure statement with all material evidence '
                                        'before filing the complaint to protect original-source status '
                                        '[Phillips & Cohen LLP — 5-ptDaAQkvI @ 00:18:37]. Front-load the '
                                        'pleading with evidence, and once counsel is ready, pick up the '
                                        'phone or email an AUSA in civil frauds [Beverly Hills Bar '
                                        'Association — yN7NRjwYKFs @ 01:21:07]. Then file first.'}],
                 'completion_gate': 'Gate passes only when a named federal payer and agency are '
                                    'identified, materiality is tied to a payment-refusal defect, '
                                    'pre-trebling damages are calculated with proof, every piece of '
                                    'evidence shows lawful access, no public disclosure has occurred, and '
                                    'the written disclosure statement is scheduled ahead of the sealed '
                                    'filing.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Seal Period, Intervention, and Data-Mined Enforcement Tracker',
                 'purpose': 'Manage the qui tam lifecycle from sealed filing through intervention, '
                            'declination, or dismissal, while stress-testing data-mined theories against '
                            "Rule 9(b), the FOCUS initiative's demand for correlations tied to falsity and "
                            'scienter, and the alternative explanations that have killed algorithmic '
                            'complaints.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Run the privilege screen and targeted-evidence check before any '
                                  'document leaves your hands for government investigators.',
                                  'Track seal dates on a calendar with six-month extension reminders, and '
                                  'log every request to disclose while the seal holds.',
                                  'Score intervention odds against the 21 to 24 percent baseline, and '
                                  'prepare a declination budget regardless of the score.',
                                  'For any claims-data theory, pair each statistical outlier with a '
                                  'document that shows falsity and knowledge.',
                                  'Keep all case facts out of AI tools, and require human review on any '
                                  'analysis before it is shared.'],
                 'fields': [{'name': 'privilege_screen',
                             'type': 'textarea',
                             'prompt': 'Identify every document or recording that involved an attorney in '
                                       'any way. Describe how each item will be segregated, who serves as '
                                       'outside ethics counsel, and the date the screen was completed '
                                       'before anything reaches the government.',
                             'example': 'Segregate attorney-involved materials and route them to outside '
                                        'ethics counsel before DOJ sees them [ABA Criminal Justice Section '
                                        "— JN4iipJiHZM @ 00:06:51]. A lawyer's name on a document does not "
                                        'by itself make it privileged [ABA Criminal Justice Section — '
                                        'JN4iipJiHZM @ 00:05:11], so log each item, the attorney involved, '
                                        'and the screening decision.'},
                            {'name': 'targeted_evidence_check',
                             'type': 'textarea',
                             'prompt': 'For each document you hold, confirm it is something you normally '
                                       'access and that it targets the fraud directly. Describe anything '
                                       'you deliberately left behind and where the government could '
                                       'subpoena it instead of you taking it.',
                             'example': 'The Cafasso relator grabbed an 11 GB folder and the case ended in '
                                        'a $300,000 fee award [ABA Criminal Justice Section — JN4iipJiHZM '
                                        '@ 00:11:12]. Do not rummage; the CFAA criminalizes unauthorized '
                                        'access, so tell the government where documents sit and let it '
                                        'subpoena them [ABA Criminal Justice Section — JN4iipJiHZM @ '
                                        '00:09:12].'},
                            {'name': 'severance_and_release_review',
                             'type': 'textarea',
                             'prompt': 'List every severance agreement, exit form, or release you have '
                                       'been offered. Quote any clause that waives whistleblower rights or '
                                       'releases False Claims Act claims, and record the advice counsel '
                                       'gave before you signed or declined anything.',
                             'example': 'Percival was offered $42,000 in severance with a fine-print '
                                        "waiver of whistleblower rights, and their lawyer's advice was "
                                        "'don't sign anything' [Whistleblower Heroes — FopC1sCa2y8 @ "
                                        '00:33:04]. McGuireWoods notes an employer cannot require an '
                                        'employee to release False Claims Act claims [McGuireWoods LLP — '
                                        'J3hHvouRce8 @ 00:54:51], so flag any such clause immediately.'},
                            {'name': 'seal_calendar',
                             'type': 'text',
                             'prompt': 'Build a calendar for the seal period. Record the filing date, the '
                                       'statutory deadline, each six-month extension request, and the '
                                       'people who must not learn of the case, including co-workers, '
                                       'insurers, buyers, and members of the press.',
                             'example': 'Hamilton has never seen a seal shorter than 120 days, and one ran '
                                        'about five years [Against The Fraud — H0ay64A0XXA @ 00:09:43]. '
                                        'The 60-day statutory window is not much time to evaluate a '
                                        'multi-billion dollar fraud [ABA Criminal Justice Section — '
                                        'kcNFrNC2BIg @ 00:46:46]. A seal breach is not an automatic '
                                        'dismissal, but avoid one.'},
                            {'name': 'intervention_odds',
                             'type': 'textarea',
                             'prompt': 'Estimate the likelihood the government will intervene and explain '
                                       'why. Describe the evidence package you will deliver, including '
                                       'draft subpoenas and organizational charts, and note how '
                                       'intervention or declination would change the expected settlement '
                                       'value and your share.',
                             'example': 'DOJ intervenes in only 21 to 24 percent of qui tam cases '
                                        '[McGuireWoods LLP — J3hHvouRce8 @ 00:09:07], yet it recovers '
                                        'about 90 percent of its money from that slice [McGuireWoods LLP — '
                                        'JXEl43HAAuo @ 00:16:24]. Hand investigators boxed fruit: '
                                        'organized evidence, draft subpoenas, and org charts that make '
                                        'joining the case easy.'},
                            {'name': 'declination_plan',
                             'type': 'textarea',
                             'prompt': 'Describe how you will proceed if the government declines. Note '
                                       'whether counsel will litigate the case alone, the litigation '
                                       'budget you can support, and the evidence suggesting the '
                                       'declination reflects resource cost rather than a judgment on the '
                                       'merits.',
                             'example': 'A declination is not a pass: $2.3 billion of FY2025 qui tam '
                                        'settlements came out of declined cases [Foley & Lardner LLP — '
                                        'J1-aE0W1Eu8 @ 00:07:51]. Aerojet Rocketdyne settled for $9M after '
                                        'DOJ declined and summary judgment was denied [Thompson Coburn LLP '
                                        '— CNlX3Qfdluw @ 00:31:43]. Budget for expense, because these '
                                        'cases can be very expensive.'},
                            {'name': 'dismissal_risk',
                             'type': 'textarea',
                             'prompt': 'Assess the risk that the government moves to dismiss the case '
                                       'outright. Identify which Granston memo category a defendant might '
                                       'invoke, the counterarguments available, and any facts showing the '
                                       'case serves program interests rather than burdening the '
                                       'government.',
                             'example': 'DOJ qui tam dismissals climbed from about 6 per year to about 25 '
                                        'last year [Husch Blackwell — XAVzMsuvKNE @ 00:00:18]. Defendants '
                                        'who ask DOJ to dismiss fit the request into a Granston memo '
                                        "category, because simply arguing 'we're right' fails [Husch "
                                        'Blackwell — XAVzMsuvKNE @ 00:05:18]. Prepare a response for each '
                                        'category.'},
                            {'name': 'data_correlation_pleading',
                             'type': 'textarea',
                             'prompt': 'If the case rests on claims-data analysis, describe the '
                                       'statistical pattern and tie it to a specific false statement and '
                                       'to scienter. Explain how the complaint pleads particular claims '
                                       'with enough detail to survive an early Rule 9(b) challenge.',
                             'example': 'Data miners have driven more than 45 percent of qui tams since '
                                        'FY2024 [Epstein Becker Green — rxUll524o5w @ 00:16:24], and the '
                                        'FOCUS initiative demands correlations tethered to falsity and '
                                        'scienter. Correlation does not equate to causation [HB Litigation '
                                        'News — mNX2NY20ks0 @ 00:16:16], so pair each outlier with a '
                                        'document showing someone knew.'},
                            {'name': 'alternative_explanation_check',
                             'type': 'textarea',
                             'prompt': 'List every innocent explanation a defendant could offer for the '
                                       'pattern you found. For each one, record the evidence that rules it '
                                       'out, and note any corrective action the defendant took that could '
                                       'undercut the knowledge element.',
                             'example': "Integra's DRG suits died in the Fifth and Ninth Circuits because "
                                        'an obvious alternative explanation existed [Analysis Group — '
                                        'y9nEr_YUXBY @ 00:29:43]. Providers who self-mine their claims '
                                        'data and take corrective action undercut the scienter a '
                                        'data-mining relator needs [HB Litigation News — mNX2NY20ks0 @ '
                                        '00:29:13], so check for remediation before filing.'},
                            {'name': 'ai_and_channel_discipline',
                             'type': 'textarea',
                             'prompt': 'Document how case facts are kept out of AI tools and unprivileged '
                                       'channels. Record which searches you ran, who reviews any '
                                       'analytical output before it reaches investigators, and how drafts '
                                       'are stored to avoid later subpoena or discovery problems.',
                             'example': 'Hamilton warns that AI is not privileged, can be subpoenaed, and '
                                        'gives wrong legal answers, while an ordinary Google search is '
                                        'fine [Against The Fraud — H0ay64A0XXA @ 00:26:51]. On the defense '
                                        'side, relying on an AI tool alone is not a defense, so put human '
                                        'review on every output headed to the government [Seyfarth Shaw '
                                        'LLP — QLVKZRh_ArE @ 00:46:37].'}],
                 'completion_gate': 'Gate passes only when privileged materials are segregated with ethics '
                                    'counsel, every document is targeted and normally accessed, no waiver '
                                    'has been signed, the seal calendar is current, a declination plan '
                                    'exists, Granston categories are answered, and each data correlation '
                                    'is tied to falsity and scienter.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Billing Fraud and Referral Arrangement Exposure Map',
                 'purpose': 'Separate systemic Medicare and Medicaid billing fraud from individual benefit '
                            'misuse, document scienter through emails and scrub language, and map the '
                            'Stark and Anti-Kickback remuneration flows, fair market value, referral-data '
                            'firewalls, and lease and value-based monitoring that turn referral '
                            'arrangements into False Claims Act triggers.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Describe the scheme in concrete operational terms: who bills, which '
                                  'codes or items, how many claims, and through which entities.',
                                  'Quote messages and scripts verbatim with dates and senders, because '
                                  'paraphrase weakens the knowledge showing.',
                                  'Treat any remuneration flowing in either direction as reportable, '
                                  'including free services, call coverage, space, or staff.',
                                  'Record personal involvement and internal reports honestly so counsel '
                                  'can weigh exposure and retaliation risk.',
                                  'Collect only records you are lawfully entitled to access, and call '
                                  'whistleblower counsel before pulling anything further.'],
                 'fields': [{'name': 'scheme_classification',
                             'type': 'text',
                             'prompt': 'Describe the scheme and classify it as systemic provider billing '
                                       'fraud or individual benefit misuse. Name the billing entity, the '
                                       'codes or items involved, the approximate claim volume, and whether '
                                       'the conduct runs like an assembly line across multiple '
                                       'participants.',
                             'example': 'Reports about a neighbor wrongly receiving benefits often go '
                                        'directly to the government [Brown, LLC - A Premier Whistleblower '
                                        'Law Firm — nDO81fwnTqg @ 00:01:07]. Systemic schemes look '
                                        'different: call centers selling signed prescriptions, signers '
                                        'paid $12 to $15 per file, and labs billing $463 million. Record '
                                        'which pattern fits your facts.'},
                            {'name': 'scienter_communications',
                             'type': 'textarea',
                             'prompt': 'List the emails, texts, and internal messages that show the '
                                       'defendant knew the claims were false or recklessly disregarded the '
                                       'truth. Note who wrote each message, who received it, the date, and '
                                       'the billing decision it influenced.',
                             'example': 'Insiders win because the government already holds the claims data '
                                        'but lacks state of mind, and emails are the top proof. When a '
                                        'billing employee raises a question and the owner shuts it down '
                                        'instead of explaining, Teller treats that as a clue something is '
                                        'wrong [Stephen Teller - Teller Law — 0w534uBbqVQ @ 00:09:55]. Log '
                                        'every such exchange.'},
                            {'name': 'medical_necessity_theory',
                             'type': 'textarea',
                             'prompt': 'If your concern involves medical necessity, describe the objective '
                                       'standard the claims failed rather than a clinical disagreement. '
                                       'Note the documentation, coverage rule, or physician-presence '
                                       'requirement involved, and whether a second clinician would reach '
                                       'the same conclusion from the records.',
                             'example': "A nurse who simply disagrees with a doctor's opinion on necessity "
                                        'has a tough case to make [Stephen Teller - Teller Law — '
                                        '0w534uBbqVQ @ 00:04:39]. A cleaner theory is incident-to billing: '
                                        'services by a nurse practitioner or PA billed at 100 percent '
                                        'instead of 85 percent without the required physician presence '
                                        '[Chapman Law Group: Health Care Attorneys — 4cRTBx7ikiY @ '
                                        '00:03:41].'},
                            {'name': 'scrub_language_log',
                             'type': 'textarea',
                             'prompt': 'Record any coded language, scripts, or warnings designed to keep '
                                       'claims from being flagged. Quote the exact words used, identify '
                                       'who supplied them, and explain how the instructions shaped '
                                       'ordering volume, patient contact, or claim submission timing.',
                             'example': 'In the Joyner chain, the file supplier told providers not to '
                                        'order too many tests at once to avoid being flagged, called '
                                        'approval plug and play, and banned no-no words like free and '
                                        'Medicare [Money vs. The System — QrUTZJlJrbQ @ 00:11:27]. '
                                        'Pushback against a patient who asks to stop shipments is another '
                                        'tell [James Hoyer, P.A. — whq5-7zwAGE @ 00:00:16].'},
                            {'name': 'internal_reporting_decision',
                             'type': 'textarea',
                             'prompt': 'Decide whether to raise the issue internally before contacting the '
                                       'government, and explain the reasoning. Record any prior hotline '
                                       'reports, supervisor conversations, or compliance tickets, and note '
                                       'the retaliation risk and remedies discussed with counsel before '
                                       'escalating.',
                             'example': 'Brown says internal reporting often results in termination, even '
                                        'though retaliation remedies include lost wages, damages, attorney '
                                        'fees, and costs [Brown, LLC - A Premier Whistleblower Law Firm — '
                                        'faQOCnnY-QI @ 00:07:53]. If retaliation follows, settle that '
                                        'claim carefully, because it can settle the False Claims Act case '
                                        'out from under the government [Stephen Teller - Teller Law — '
                                        'SiATzxJHy2Y @ 00:06:26].'},
                            {'name': 'personal_exposure',
                             'type': 'textarea',
                             'prompt': 'Describe any personal role you played in the billing process. Note '
                                       'whether you signed documents, handed over a Medicare number, '
                                       'received payments, or delayed reporting, and record the timeline '
                                       'counsel needs to evaluate whether you could be viewed as '
                                       'implicated.',
                             'example': 'If you signed, profited, or handed over a Medicare number, assume '
                                        'personal exposure; the government may view a reporter who '
                                        'profited as implicated [Brown, LLC - A Premier Whistleblower Law '
                                        'Firm — 7two8gR6AAY @ 00:00:35]. Delay compounds it: only the '
                                        'first filer has rights [Brown, LLC - A Premier Whistleblower Law '
                                        'Firm — faQOCnnY-QI @ 00:09:35].'},
                            {'name': 'remuneration_flow',
                             'type': 'textarea',
                             'prompt': 'Trace everything of value moving between referral sources and the '
                                       'entity billing the program, in either direction. Identify the '
                                       'payer, the recipient, the form of remuneration, its market value, '
                                       'and the referrals that coincided with each payment or benefit.',
                             'example': 'Catholic Medical Center gave a referring cardiologist free call '
                                        'coverage that other cardiologists were paid $10,000 per weekend '
                                        'to provide, and settled for $3.8 million [KLGatesLaw — '
                                        'MMcEwUD0PNo @ 00:12:18]. Both the pitcher who gives the '
                                        'remuneration and the catcher who receives it are liable [Group '
                                        'Practice with Neal Goldstein — gIyVCP3OhyM @ 00:03:46].'},
                            {'name': 'fair_market_value_review',
                             'type': 'textarea',
                             'prompt': 'Evaluate whether each physician arrangement falls within fair '
                                       'market value and makes commercial sense without referrals. Note '
                                       'any appraisal obtained, who engaged the appraiser, where the '
                                       'payment sits within the range, and any written statement '
                                       'suggesting improper purpose.',
                             'example': 'Alyssa James says FMV is a range where the high and low ends are '
                                        'equally compliant, and engaging appraisers through counsel '
                                        'preserves privilege [Dallas-Fort Worth Hospital Council — '
                                        '_1_drZryqm4 @ 00:36:13]. Watch the paper trail: 800 pages of good '
                                        'purposes can be undone by one sentence in a board comment, email, '
                                        'or text [Dallas-Fort Worth Hospital Council — _1_drZryqm4 @ '
                                        '00:07:29].'},
                            {'name': 'referral_data_firewall',
                             'type': 'textarea',
                             'prompt': 'Describe where referral, technical-fee, or revenue data is tracked '
                                       'and who can see it. Record whether anyone setting physician '
                                       'compensation reviews those reports, and document the firewall, '
                                       'deletion policy, or access controls that separate the data from '
                                       'pay decisions.',
                             'example': 'Wheeling Hospital paid physicians a percentage of net revenue '
                                        'tracked in physician impact reports and settled for $50 million, '
                                        'with $10 million to a former-executive relator [KLGatesLaw — '
                                        'MMcEwUD0PNo @ 00:06:05]. The lesson: either do not keep '
                                        'spreadsheets tracking referrals against pay, or wall them off '
                                        'from compensation decisions [KLGatesLaw — MMcEwUD0PNo @ '
                                        '00:08:56].'},
                            {'name': 'lease_and_value_based_monitoring',
                             'type': 'textarea',
                             'prompt': 'Inventory every lease, service agreement, and value-based '
                                       'arrangement involving referral sources. Record signature dates '
                                       'against occupancy or start dates, any changes made by email only, '
                                       'the written amendments on file, and the next scheduled monitoring '
                                       'review date.',
                             'example': 'No physician moves into space before signature, and schedule '
                                        'drift or escalator changes need a written amendment, not an email '
                                        '[Dallas-Fort Worth Hospital Council — _1_drZryqm4 @ 00:33:55]. '
                                        'For value-based arrangements, calendar at least annual '
                                        'monitoring; an ineffective activity gets 30 days to wind down or '
                                        '90 days to modify [Holland & Hart LLP — wODno0XW8l4 @ '
                                        '00:57:26].'}],
                 'completion_gate': 'Gate passes only when the scheme is classified as systemic provider '
                                    'fraud, scienter rests on dated communications, remuneration flows are '
                                    'traced with market values, referral data access is documented, '
                                    'personal exposure is disclosed to counsel, and no record was pulled '
                                    'beyond lawful access.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Contractor Cyber-Fraud and Customs Evasion Case Builder',
                 'purpose': 'Convert a contractor cyber-compliance gap, a customs evasion pattern, or a '
                            'relief-loan concealment into a documented False Claims Act theory with '
                            'defensible exposure math, a defendant chain, and a realistic view of seal '
                            'length, relator share, and collectability.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Work only from records you normally access in your job; photograph or '
                                  'note document locations rather than removing files, and let counsel '
                                  'decide what reaches the government.',
                                  'Answer the cyber fields first if your facts involve NIST 800-171, SPRS, '
                                  'or incident reporting, then move to the customs and relief-loan fields '
                                  'if import or loan data is involved.',
                                  'Use the practitioner penalty figures as ranges, since quoted per-claim '
                                  'amounts vary from about $11,665 to $28,619, and show every '
                                  'multiplication step.',
                                  'Keep every answer under seal discipline: no co-worker, competitor, or '
                                  'press contact while the seal holds, because the average seal runs about '
                                  '18 months.',
                                  'Leave a field blank rather than guessing, and mark any secondhand fact '
                                  'clearly, because a case resting on secondhand happy-hour gossip was '
                                  'dismissed.'],
                 'fields': [{'name': 'cyber_theory_selection',
                             'type': 'textarea',
                             'prompt': 'Identify which of the three cyber-fraud theories your facts '
                                       'support: deficient cyber products or services, misrepresented '
                                       'controls such as NIST 800-171 and SPRS certifications, or late '
                                       'incident reporting. Explain why the gap became a knowing false '
                                       'claim once an invoice went out.',
                             'example': 'Misrepresented controls theory. The contractor posted an SPRS '
                                        'score claiming full NIST 800-171 implementation while the '
                                        "security officer's own gap list showed open items, then kept "
                                        "invoicing. Since DOJ's October 2021 Civil Cyber-Fraud Initiative, "
                                        'that gap is a knowing false claim, not a fixable defect; Aerojet '
                                        'Rocketdyne settled for $9M after DOJ declined [Thompson Coburn '
                                        'LLP — CNlX3Qfdluw @ 00:31:43].'},
                            {'name': 'per_claim_exposure_math',
                             'type': 'textarea',
                             'prompt': 'Count the invoices or claims tied to the false certification, then '
                                       'apply treble damages and the per-claim penalty range. Record which '
                                       'penalty figures practitioners quoted, since figures differ, and '
                                       'note whether losses must be shown for the number to grow.',
                             'example': 'Forty monthly invoices under one contract. At the July 2025 range '
                                        'of $14,308 to $28,619 per claim, penalties alone run $572,320 to '
                                        '$1,144,760 before trebling [UAP Legion — Y9DOny35SW0 @ 00:03:15]. '
                                        'Jones Day warns that number can grow quite exponentially even '
                                        'when the government has not shown any losses at all [Jones Day — '
                                        'ah8GhXnbe-8 @ 00:02:39].'},
                            {'name': 'knowledge_standard_defense_map',
                             'type': 'textarea',
                             'prompt': 'Anticipate the defense theme on knowledge. Write down the facts '
                                       'showing the conduct went beyond innocent mistake, mere error, or '
                                       'negligence, and list who raised the issue internally, when, and '
                                       'what response, if any, management gave.',
                             'example': "Expect the two-step defense Bracker describes: we didn't do "
                                        "anything wrong, and if we did we didn't mean to [ClearanceJobs — "
                                        'j_QEFJG-ON4 @ 00:19:04]. Counter it with dated emails from the '
                                        'security officer flagging the open controls and the unchanged '
                                        'certification that followed, because civil FCA knowledge excludes '
                                        'innocent mistake, mere error, or negligence [Thompson Coburn LLP '
                                        '— CNlX3Qfdluw @ 00:12:55].'},
                            {'name': 'contracting_officer_notice_log',
                             'type': 'textarea',
                             'prompt': 'Log every SPRS score change and material contract change, the date '
                                       'it occurred, and whether it reached the contracting officer or '
                                       'stopped at the project manager. Note the format used, such as an '
                                       'email or a formal letter.',
                             'example': 'March: SPRS score revised downward after an internal assessment; '
                                        'notice sent only to the project manager, so it is re-sent to the '
                                        'contracting officer. Minor changes go by email; an organizational '
                                        'conflict of interest goes by formal letter [CMMC LaunchPad — '
                                        'GkIQylusGaw @ 00:09:44]. The safest, most compliant approach will '
                                        'always be open and transparent communication [CMMC LaunchPad — '
                                        'GkIQylusGaw @ 00:11:15].'},
                            {'name': 'cid_response_clock',
                             'type': 'text',
                             'prompt': 'Record the date any subpoena or civil investigative demand '
                                       'arrived, its 30-day or 14-day return date, the litigation hold '
                                       'issued, the date counsel was called, and any date-range narrowing '
                                       'you negotiated down with the government in writing.',
                             'example': 'CID received; return date calendared on its 30-day clock, because '
                                        'ignoring it triggers a public motion to compel [Cape Endeavors, '
                                        'Inc. — -2BTi30xXrA @ 00:14:47]. Document destruction halted the '
                                        'same day and counsel called without panic [PilieroMazza PLLC — '
                                        'ZyG_Zu7OvIg @ 00:44:22]. Date range pushed down hard, as when a '
                                        'demand reaching back to 2006 was narrowed to 2009-2013 '
                                        '[WilliamsMullen — NdqYGSN5BYc @ 00:57:16].'},
                            {'name': 'customs_entry_attack_surface',
                             'type': 'textarea',
                             'prompt': 'Walk each suspect import entry through CBP Form 7501: country of '
                                       'origin, HTS code, product description, and declared value. Name '
                                       'the scheme you suspect, such as dual invoicing, misclassification, '
                                       'transshipment, sham substantial transformation, omitted assists, '
                                       'or de minimis structuring.',
                             'example': 'Origin line declares a third country, but the goods were only '
                                        'repackaged there after leaving the tariffed source. Legitimate '
                                        'substantial transformation can change origin, but simple '
                                        'repackaging does not [Shipping Solutions — EIHwzCe4zZM @ '
                                        '00:03:09]. A cosmetic or superficial change does not qualify as a '
                                        'substantive change [Brown, LLC - A Premier Whistleblower Law Firm '
                                        '— XXtgvEhkvo4 @ 00:01:38]. Section 301 tariff: 25%.'},
                            {'name': 'raw_data_public_disclosure_check',
                             'type': 'textarea',
                             'prompt': 'If your case is built by mining import or loan records rather than '
                                       'insider knowledge, describe the raw data source, the analysis you '
                                       'performed on it yourself, and why the result is not a public '
                                       'disclosure that bars the claim.',
                             'example': 'Raw, unanalyzed import data matched shipments against declared '
                                        'origin; the relator built the comparison personally. Raw import '
                                        'data is generally not treated as a public disclosure, so '
                                        'self-analysis keeps the case clear of the bar [Tycko & Zavareei '
                                        'LLP — A2nRu5da_9k @ 00:17:20]. Price the award realistically: for '
                                        'PPP data-mining outsiders the government pays about 10%, not '
                                        '15-30% [Justia — HocnawRgrAA @ 00:32:07].'},
                            {'name': 'customs_liability_and_award_projection',
                             'type': 'textarea',
                             'prompt': 'Estimate evaded duty, the number of shipments, and the resulting '
                                       'liability once damages and per-shipment penalties apply. Then '
                                       'project the realistic relator share, the expected seal length, and '
                                       'the time to resolution for a customs case.',
                             'example': 'Benchmark: $2M evaded across 25 shipments becomes about $6.5M in '
                                        'liability [Tycko & Zavareei LLP — A2nRu5da_9k @ 00:25:04]. '
                                        'Relator share: plan near 17%, since above 20% is hard to get '
                                        '[Stephen Teller - Teller Law — QNzd1e6e8UE @ 00:12:30]. Seal: '
                                        'about 18 months against a 60-day clock, with resolution in 2.5 to '
                                        '3 years [Tycko & Zavareei LLP — A2nRu5da_9k @ 00:20:33].'},
                            {'name': 'ppp_grant_state_lane',
                             'type': 'textarea',
                             'prompt': 'For relief-loan, grant, or state matters, identify the specific '
                                       'concealment or charging problem, the federal or state program that '
                                       'lost money, and whether a parallel state False Claims Act count '
                                       'could pay a larger relator share.',
                             'example': 'Borrower concealed affiliates to slip under the 500-employee or '
                                        '$10M PPP cap, the viable relief-loan pattern [Brown, LLC - A '
                                        'Premier Whistleblower Law Firm — 5fDm1yVZ4cM @ 00:03:09]. Where '
                                        'state money is involved, a parallel California count matters: '
                                        'non-intervened relators can reach up to 50%, versus 25-30% '
                                        'federally [Husch Blackwell — _n3NJXxKz_8 @ 00:03:13].'},
                            {'name': 'defendant_chain_and_collectability',
                             'type': 'textarea',
                             'prompt': 'List every potential defendant in the chain, including the '
                                       'importer of record, overseas suppliers, downstream retailers, and '
                                       'owners. For each, note available insurance and whether the policy '
                                       'is likely to fund the treble portion of any recovery.',
                             'example': 'Defendants: importer of record, its overseas supplier, the '
                                        'downstream retailer, and the two owners, since the whole chain '
                                        'can be named [Tycko & Zavareei LLP — A2nRu5da_9k @ 00:44:46]. '
                                        'Collectability: the importer carries D&O coverage, but D&O '
                                        'insurance often excludes treble damages, so the policy may not '
                                        'fund the treble portion [PilieroMazza PLLC — eIBPl3LNUXQ @ '
                                        '00:41:04].'}],
                 'completion_gate': 'Do not advance to Worksheet 5 until every field cites at least one '
                                    'practitioner source, the liability math shows each multiplication '
                                    'step, the contracting officer log is current, and the defendant chain '
                                    'includes a collectability note for each party named.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'SEC, CFTC, and AML Bounty Filing Control Sheet',
                 'purpose': 'Lock down the procedural steps that decide whether a securities, derivatives, '
                            'or anti-money-laundering tip ever pays: original information, the TCR route, '
                            'the 120-day clock, anonymity through counsel, evidence packaging, ongoing '
                            'assistance, and the self-policed award claim.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Fill in the TCR and 120-day fields before anything else, because '
                                  'procedural failures carry no rewards and no exceptions.',
                                  'If you need anonymity, retain whistleblower counsel before submitting '
                                  'anything; both the SEC and CFTC routes tie anonymous filing to '
                                  'representation by an attorney.',
                                  'Hold back any document that may be attorney-client privileged until '
                                  'counsel sets up segregation or a taint process.',
                                  'Record every contact with agency staff the same day it happens, '
                                  'including what was requested and what you supplied.',
                                  'Set a recurring calendar reminder to check notices of covered action, '
                                  'because the agency may resolve the matter without notifying you.'],
                 'fields': [{'name': 'original_information_threshold',
                             'type': 'textarea',
                             'prompt': 'Describe the original information you hold, how you came to know '
                                       'it, and why it is voluntary. Estimate whether resulting sanctions '
                                       'could exceed $1 million, the floor that unlocks a 10 to 30 percent '
                                       'award, and which agency program applies.',
                             'example': 'Internal records showing malfeasance inside a regulated financial '
                                        'company, seen firsthand in the normal course of the job and not '
                                        'yet known to any agency. Sanctions likely clear $1 million, and '
                                        'the SEC and CFTC programs pay up to 30% on tips leading to '
                                        'monetary sanctions above that line [Zuckerman Whistleblower Law '
                                        'Firm — mq-TIQ4Y8ps @ 00:00:30].'},
                            {'name': 'tcr_filing_route',
                             'type': 'text',
                             'prompt': 'Record the date and channel of your Form TCR filing and confirm it '
                                       'went to the SEC itself. If you are already cooperating with DOJ, a '
                                       'U.S. attorney, or the FBI, note when that began relative to the '
                                       'TCR.',
                             'example': 'TCR filed through counsel the same week FBI interviews began, not '
                                        'after. Years of cooperation without a TCR may leave the claim too '
                                        'late [Brown, LLC - A Premier Whistleblower Law Firm — b9I9BCtPjzw '
                                        '@ 00:01:14]. A letter or hotline call is not a tip; fail the '
                                        'procedural rules and there are no rewards, no exceptions [Mahany '
                                        'Law — BueLAsaxhHM @ 00:03:40].'},
                            {'name': 'internal_report_120_day_clock',
                             'type': 'text',
                             'prompt': 'If you already reported to a hotline, supervisor, compliance '
                                       'department, or another agency, enter that date and the 120-day '
                                       'deadline for delivering the same information to the SEC. Explain '
                                       'how you will meet it before it expires.',
                             'example': 'Hotline report made on day one; SEC submission calendared well '
                                        'inside 120 days to keep eligibility and Dodd-Frank retaliation '
                                        'coverage [Parnham and Associates — 8tuRViP_j4Y @ 00:02:57]. The '
                                        'window works across agencies too: the SEC highlighted a $2.2 '
                                        'million award to a whistleblower who first reported elsewhere '
                                        '[Wiley Rein LLP — lzz_1rNcrwk @ 00:06:35].'},
                            {'name': 'internal_vs_sec_first_decision',
                             'type': 'textarea',
                             'prompt': 'Weigh reporting internally first against going to the SEC first. '
                                       'Record the plus factor internal reporting can earn, the '
                                       'termination risk that compliance lines carry, and the retaliation '
                                       'protection you would lose by reporting only internally.',
                             'example': 'Internal reporting is not required and counts as a plus factor '
                                        'for a higher award [Whistleblower Network News — wsT0MJ2Q9Gg @ '
                                        '00:32:21]. But Dodd-Frank protects an internal disclosure only '
                                        'where the person also reported to the SEC [Zuckerman '
                                        'Whistleblower Law Firm — EG1qQyQJKzg @ 00:01:25]. Decision: SEC '
                                        'first through counsel, internal report afterward only with '
                                        "employment counsel's sign-off."},
                            {'name': 'anonymity_and_identity_risk',
                             'type': 'textarea',
                             'prompt': 'State whether you need anonymity and, if so, which attorney will '
                                       'file on your behalf. Then describe the circumstances, such as '
                                       'court proceedings or a criminal referral, under which your name '
                                       'could still have to surface.',
                             'example': 'Anonymity required; counsel files the CFTC submission, since that '
                                        'program ties anonymity to legal representation [Whistleblowers '
                                        'International — nGZvKSKSh-Y @ 00:02:56]. Identity risk priced in: '
                                        'if the case goes to court or turns criminal, the name may have to '
                                        'surface [Wiley Rein LLP — lzz_1rNcrwk @ 00:04:01].'},
                            {'name': 'evidence_package_and_privilege_screen',
                             'type': 'textarea',
                             'prompt': 'List the documents you will deliver, why each matters, and how '
                                       "they make the agency's job easier. Flag anything potentially "
                                       'attorney-client privileged and describe how it will be held back '
                                       'until segregation or a taint process exists.',
                             'example': 'Twelve key documents with a one-page index, not terabytes; the '
                                        'government wants the good material, and privileged items are held '
                                        'back until segregation is set up, because they can taint the '
                                        'whole investigative team [Fraud in America — R3h4J-EAtro @ '
                                        '00:31:26]. Well-packaged information plus substantial assistance '
                                        'is what rises to the top of thousands of tips [Wiley Rein LLP — '
                                        'lzz_1rNcrwk @ 00:13:52].'},
                            {'name': 'ongoing_assistance_log',
                             'type': 'textarea',
                             'prompt': 'Track every follow-up contact with agency staff after the initial '
                                       'tip: date, request, what you supplied, and whether it filled a gap '
                                       "the company's own self-disclosure left out. Ongoing, extensive, "
                                       'and timely assistance can drive award size.',
                             'example': 'Third follow-up call: staff asked about senior leadership '
                                        'knowledge; supplied the meeting calendar and two emails. In a $37 '
                                        'million SEC award, ongoing, extensive and timely assistance '
                                        "exposed the full context the company's self-disclosure left out "
                                        '[Compliance Podcast Network — bFRmUwE-_F4 @ 00:14:00]. Showing '
                                        'senior leadership knew is what tipsters most often leave out '
                                        '[Fraud in America — R3h4J-EAtro @ 00:14:54].'},
                            {'name': 'notice_of_covered_action_monitor',
                             'type': 'textarea',
                             'prompt': 'Set a recurring schedule for checking posted notices of covered '
                                       'action and related actions by other agencies. Record each check '
                                       'date, any matching posting, and the date your award claim was '
                                       'filed within the required window.',
                             'example': 'Monthly check of SEC postings; the SEC may settle off a tip '
                                        'without telling the tipster, and missing the timely claim has led '
                                        'to countless denials [Brown, LLC - A Premier Whistleblower Law '
                                        'Firm — 0_sJP-wJPRc @ 00:02:25]. Related actions count: another '
                                        "agency's action on the same information can pay 10 to 30% of its "
                                        'sanctions [Foundation Digital Media — dyn9ni2HPDU @ 00:00:23].'},
                            {'name': 'retaliation_clock_selection',
                             'type': 'textarea',
                             'prompt': 'Record the date of any adverse employment action and compare the '
                                       'Sarbanes-Oxley 180-day filing deadline with the Dodd-Frank window '
                                       'of up to six years. Note whether your report reached the SEC '
                                       'directly, which Dodd-Frank damages and coverage require.',
                             'example': 'Demotion dated in the log. SOX allows 180 days; Dodd-Frank allows '
                                        'up to six years and potentially double damages, but only if the '
                                        'concern reached the SEC directly, not just a manager or '
                                        'compliance department [Garrison, Levin-Epstein, Fitzgerald & '
                                        'Pirrotti — ft81gWsFd2M @ 00:01:46]. Dated timeline written before '
                                        'any complaint [Garrison, Levin-Epstein, Fitzgerald & Pirrotti — '
                                        'ft81gWsFd2M @ 00:02:17].'},
                            {'name': 'aml_and_newer_bounty_lanes',
                             'type': 'textarea',
                             'prompt': 'If the conduct involves money laundering, sanctions, derivatives, '
                                       'or corporate crime, identify which program fits: CFTC, FinCEN AML, '
                                       "DOJ's corporate pilot, or Treasury's flat-reward portal. Note the "
                                       'award structure and any confidentiality concerns practitioners '
                                       'raised about each lane.',
                             'example': 'Bank sanctions failures fit the FinCEN AML lane. Point the agency '
                                        'at data banks already self-report, since it often lacks only the '
                                        'key showing where to look [Fraud in America — R3h4J-EAtro @ '
                                        '00:14:54]. FinCEN proposed a maximum-award presumption at $15 '
                                        'million versus $5 million at the SEC [Fraud in America — '
                                        'R3h4J-EAtro @ 00:12:18]. Practitioners flag confidentiality and '
                                        'bankruptcy loopholes.'}],
                 'completion_gate': 'Do not advance to Worksheet 6 until the TCR date, any internal-report '
                                    'date with its 120-day deadline, the retaliation filing clock, and the '
                                    'covered-action monitoring schedule are all entered and confirmed with '
                                    'counsel.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'IRS Form 211 Claim Builder and Signal-Versus-Noise Filter',
                 'purpose': 'Build an IRS award claim that clears the liability floor, survives '
                            'eligibility screening, and stands out in a crowded review queue, while '
                            'separating genuine detection and reporting practice from acronym collisions '
                            'and tax-protester narratives that lead nowhere.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Calculate tax liability, not income, for the threshold field; a large '
                                  'unreported-income figure can still fall short of $2 million in '
                                  'liability.',
                                  'Submit your strongest evidence with the original filing; do not hold '
                                  'documents back waiting for the IRS to call.',
                                  'Identify yourself on the claim; anonymous submissions are not eligible '
                                  'for an award, though the IRS protects claimant confidentiality.',
                                  'Keep case facts out of AI tools, which are not privileged and can be '
                                  'subpoenaed; a general search is fine.',
                                  'Treat any online claim about Form 211 or the FCA acronym as noise until '
                                  'it passes the acronym and label test in the final field.'],
                 'fields': [{'name': 'form_211_route_confirmation',
                             'type': 'text',
                             'prompt': 'Confirm you are filing Form 211, not Form 3949-A or another '
                                       'information-only report. Record the filing date, the claimant name '
                                       'you will sign under, and why anonymous submission is not an option '
                                       'for an award under this program.',
                             'example': 'Form 211 selected; Form 3949-A rejected because it looks '
                                        'strikingly similar but carries no award, a common but devastating '
                                        'mistake [Law Minded — sNHauc7rutQ @ 00:06:08]. Claimant '
                                        'identified by name, since IRS tips cannot be submitted '
                                        'anonymously, though confidentiality is protected [The Anti-Fraud '
                                        'Coalition — fQss6bE5tKc @ 00:00:17]. Anonymous complaints are a '
                                        'historic dead end [Boston 25 News — mfEL3LienPQ @ 00:01:18].'},
                            {'name': 'threshold_liability_math',
                             'type': 'textarea',
                             'prompt': 'Calculate the tax, penalties, interest, and additions in dispute, '
                                       'not the unreported income, and show it exceeds $2 million. For an '
                                       'individual target, confirm gross income above $200,000 in at least '
                                       'one year at issue, and cite the supporting records.',
                             'example': 'Unreported income of $5 million at a roughly 50% effective rate '
                                        'yields about $2.5 million in liability, clearing the floor; $2 '
                                        'million of income would yield only $1 million and fail [Brown, '
                                        'LLC - A Premier Whistleblower Law Firm — tQIkb01vCTw @ 00:01:37]. '
                                        'Floor confirmed: over $2 million in dispute and over $200,000 '
                                        'individual income [The Anti-Fraud Coalition — fQss6bE5tKc @ '
                                        '00:01:27].'},
                            {'name': 'collection_potential_and_size',
                             'type': 'textarea',
                             'prompt': 'Explain why the IRS will realistically collect if it acts, naming '
                                       'reachable assets or ongoing income. State where the claim sits '
                                       'against the practitioner sweet spot and the likely collection '
                                       'level below which the IRS rarely moves.',
                             'example': 'Target holds domestic operating businesses with steady income, so '
                                        "collection potential exists; without it, don't do it [Former IRS "
                                        'Agent Representation   4.2M Views — 41ejxu80Qtg @ 00:04:23]. '
                                        'Estimated collection near $20 million sits inside the $10 million '
                                        'to $50 million simple-evasion sweet spot that Green and Skarlatos '
                                        'favor over billion-dollar claims that never paid.'},
                            {'name': 'narrative_memo_and_appendices',
                             'type': 'textarea',
                             'prompt': 'Outline the narrative memo that tells the story of the '
                                       'noncompliance, then list the appendices: enabling parties, '
                                       'witnesses, and documents. Describe any supporting documents you do '
                                       'not hold but know exist, and where the IRS can find them.',
                             'example': 'Memo: four pages tracing the scheme year by year. Appendix A: '
                                        'enabling accountant; Appendix B: two witnesses; Appendix C: '
                                        'documents held. Unheld records are described with their location '
                                        '[Teach Me! Personal Finance — WA3dtUQT9f8 @ 00:02:46]. The killer '
                                        'email goes in on day one, since the IRS really only looks once '
                                        '[Kohn Kohn & Colapinto — O45E7FrG_mM @ 00:09:24].'},
                            {'name': 'eligibility_strike_out',
                             'type': 'textarea',
                             'prompt': 'Screen yourself for disqualifiers: current or former Treasury '
                                       'employment, facts learned through official duties or a federal '
                                       'contract, information obtained from an ineligible insider, or '
                                       'knowledge gained as an attorney or accountant that needs resolving '
                                       'before filing.',
                             'example': 'No Treasury employment, no federal contract role, and no '
                                        'IRS-employee friend as a source, so no strike-out applies [Teach '
                                        'Me! Personal Finance — WA3dtUQT9f8 @ 00:05:58]. The claimant kept '
                                        "the target's books as an outside accountant, so that issue is "
                                        'resolved with counsel before filing to avoid a three-to-five-year '
                                        'taint process [Brown, LLC - A Premier Whistleblower Law Firm — '
                                        'tQIkb01vCTw @ 00:05:48].'},
                            {'name': 'tax_owed_theory',
                             'type': 'textarea',
                             'prompt': 'State plainly why the target owes tax, identifying the years, the '
                                       'income or deductions at issue, and the red flags observed. '
                                       'Separate what proves tax owed from any fraud evidence, which helps '
                                       'but is not required.',
                             'example': 'Theory: owner expensed personal costs through the company in '
                                        'three years, booked as round-number entries such as $5,000 '
                                        'monthly consulting. Showing fraud is a nice bonus, but all that '
                                        'is needed is that the person owes tax [Kohn Kohn & Colapinto — '
                                        'O45E7FrG_mM @ 00:17:40]. Round-number expenses are the biggest '
                                        'audit red flag [The Brad Weisman Show — _ehHXyRo6fI @ 00:18:13].'},
                            {'name': 'timeline_and_payment_expectations',
                             'type': 'textarea',
                             'prompt': "Set realistic expectations for the claim's lifecycle: the review "
                                       'queue, examination, appeals, and collection. Record that no award '
                                       'pays until the target exhausts every appeal, and plan for mostly '
                                       'vague yearly status updates in the meantime.',
                             'example': 'Plan for about 10 years to a paid claim [Brown, LLC - A Premier '
                                        'Whistleblower Law Firm — tQIkb01vCTw @ 00:07:20]; awards issue '
                                        'only after the taxpayer exhausts all appeal rights [Logan Allec — '
                                        'i4GnKgGXiMw @ 00:01:04]. The Whistleblower Office faces about '
                                        '1,000 claims a month against 32 reviewers [Where IRS Problems Get '
                                        'Solved — ruRW_hNSDYk @ 00:07:31].'},
                            {'name': 'internal_data_detection_program',
                             'type': 'textarea',
                             'prompt': 'Describe the data-driven tests you run on bank feeds and payroll '
                                       'exports, how often, and who reviews results. Confirm payroll '
                                       'exports to Excel and that owners are named on every business bank '
                                       'account before relying on any hotline.',
                             'example': 'Monthly macros run against the operating bank feed, reviewed by '
                                        'the controller; payroll provider confirmed to export to Excel, or '
                                        'it gets replaced [Workman Forensics — 4CnIVLSoe2o @ 00:11:12]. '
                                        'Hotline-only shops are already behind, because tips arrive late '
                                        'and the reporter may have been part of the scam [Workman '
                                        'Forensics — 4CnIVLSoe2o @ 00:04:12]. Data plus a hotline is '
                                        'gold.'},
                            {'name': 'hotline_intake_and_investigation_design',
                             'type': 'textarea',
                             'prompt': 'Design the hotline intake and investigation path: intake channels '
                                       'beyond mail and fax, a good-faith certification checkbox, whether '
                                       'a written policy exists before any 990 disclosure, and whether '
                                       'outside investigators replace in-house HR to limit bias.',
                             'example': 'Web intake added with a good-faith certification checkbox [GRF '
                                        'CPAs & Advisors — bPsS_B4v7Dw @ 00:45:14]. The 990 whistleblower '
                                        'box stays unchecked until the written policy is adopted, since a '
                                        'false yes creates liability [GRF CPAs & Advisors — bPsS_B4v7Dw @ '
                                        '00:17:14]. Investigations go to outside investigators, because HR '
                                        'is there for the corporation [Koegle Law Group — nM5JZ33rgDk @ '
                                        '00:00:45].'},
                            {'name': 'noise_filter_and_acronym_check',
                             'type': 'textarea',
                             'prompt': 'Before acting on any whistleblower claim found online, test it: '
                                       'does FCA mean the False Claims Act or the UK Financial Conduct '
                                       'Authority, and does the IRS whistleblower label describe a real '
                                       'Form 211 claim or a tax-protester theory?',
                             'example': 'Rejected: advice urging filers to file Form 211 in court as '
                                        'evidence and send it to the Treasury [SovereignProductions369 — '
                                        'Q2EMaQHpNPM @ 00:00:21]. That is not an award claim. Against '
                                        "no-file narratives stands Sherry Peel Jackson's four-year "
                                        'sentence for willful failure to file. Separately, a UK FCA '
                                        'reference meant the Financial Conduct Authority.'}],
                 'completion_gate': 'The worksheet is complete only when liability math clears $2 million, '
                                    'the eligibility screen shows no strike-out, collection potential is '
                                    'documented, the narrative memo and three appendices are outlined, and '
                                    'every online claim relied on has passed the noise filter.'}]}
