from __future__ import annotations

def build_volume_046_workbook() -> dict:
    return {'workbook_id': 'wb-046-mass-tort-intake-hitech-triage-and-law-firm-msos',
 'volume_id': 'vol-046-mass-tort-intake-hitech-triage-and-law-firm-msos',
 'title': 'Mass-Tort Case Acquisition, HITECH Record Triage & Law-Firm MSOs — Practitioner Testimony '
          'Operator Workbook',
 'subtitle': 'Choosing the Payout Vehicle, Underwriting the Tort, Proving Every File, and Pricing Every '
             'Signed Case Before the Money Moves',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Vehicle Selection and MDL Readiness Map',
                 'purpose': 'Decide whether each harm belongs in a class action or an MDL, confirm the '
                            'docket can clear the consolidation threshold, fund leadership work, and '
                            'harden every file against bellwether selection, sworn fact sheets, Daubert '
                            'rulings, and distribution failures before committing capital.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Start by classifying the harm: small uniform monetary losses spread '
                                  'across many people point to a class action, while serious injury and '
                                  'death claims point to an MDL where each plaintiff keeps an individual '
                                  'lawsuit.',
                                  'Fill in the case counts and venue fields before any marketing budget is '
                                  'approved, because the panel threshold and venue choice shape every '
                                  'later cost assumption.',
                                  'Confirm leadership or co-counsel funding in writing, since '
                                  'common-benefit document review, depositions, and experts are paid out '
                                  'of pocket through a common fund.',
                                  'Audit each file as if it will be pulled into the bellwether pool '
                                  'tomorrow, checking sworn fact sheet accuracy and any activity that '
                                  'contradicts the claimed injury.',
                                  'Close the worksheet by pricing the inventory against a global Daubert '
                                  'loss and writing a distribution plan that keeps settlement money from '
                                  'sitting in uncashed checks.'],
                 'fields': [{'name': 'vehicle_classification',
                             'type': 'text',
                             'prompt': 'Classify the target harm as a class action, mass tort, or MDL '
                                       'candidate. State whether damages are small and uniform across many '
                                       'people or serious and individualized, and name the payout vehicle '
                                       'you will pursue for this docket.',
                             'example': 'Serious injury and death claims belong in an MDL where each '
                                        'plaintiff keeps an individual lawsuit, attorney and verdict, '
                                        'while small uniform harms fit a class action: one million people '
                                        'overcharged three dollars netted the phone company three million '
                                        'dollars, and nobody files over three dollars [The Brandi Law Firm '
                                        '— luVb2J9MsQk @ 00:01:26]. Our docket is individualized injury, '
                                        'so MDL.'},
                            {'name': 'jpml_threshold_count',
                             'type': 'text',
                             'prompt': 'Record the number of filed cases you can currently document and '
                                       'the number of additional cases you reasonably expect nationwide. '
                                       'Compare both figures against the consolidation threshold '
                                       'practitioners cite and note whether a petition could realistically '
                                       'be denied.',
                             'example': 'Searcy Law looks for at least 20 to 50 cases with an expectation '
                                        'of hundreds and hundreds of additional cases, if not thousands, '
                                        'and notes some MDLs form on fewer than 20 while some petitions '
                                        'are denied [Searcy Law Video — yIQ0NYXRsmQ @ 00:01:12]. Our '
                                        'count: 34 filed, roughly 600 more expected, so petition-ready.'},
                            {'name': 'venue_risk_note',
                             'type': 'textarea',
                             'prompt': 'Describe the venue you hope the panel selects and the fallback '
                                       'locations you could live with. Explain how your docket plan '
                                       'survives if the panel ignores oral argument, chooses a district '
                                       'with one filed case, or picks a location nobody requested.',
                             'example': 'Never bank on venue from oral argument: the panel has judges it '
                                        'likes to give cases to, sometimes picks a location where only one '
                                        'case was filed, and has sent MDLs to places nobody requested '
                                        '[Searcy Law Video — yIQ0NYXRsmQ @ 00:01:43]. Our budget assumes '
                                        'any district, so travel and local filing costs are reserved '
                                        'before argument.'},
                            {'name': 'leadership_funding_check',
                             'type': 'textarea',
                             'prompt': 'Name the co-counsel or leadership firm that will fund '
                                       'common-benefit work, and state the dollar commitment you can '
                                       'contribute. Identify which document review, deposition, and expert '
                                       'costs the common fund will carry versus costs your firm absorbs '
                                       'alone.',
                             'example': 'MDL leadership finances document review, depositions, and experts '
                                        'out of pocket through a common fund, so funding is confirmed '
                                        'before committing [Searcy Law Video — yIQ0NYXRsmQ @ 00:04:07]. '
                                        'Leadership runs an executive committee of 4-5 under lead or '
                                        'co-lead counsel, with a steering committee of 2-3 up to 20 in '
                                        'bigger litigations [Searcy Law Video — yIQ0NYXRsmQ @ 00:03:21].'},
                            {'name': 'bellwether_exposure',
                             'type': 'textarea',
                             'prompt': 'List the files in your inventory most likely to be pulled into a '
                                       'bellwether pool and rate each as strong, average, or weak. Explain '
                                       'how a weak file selected for trial could drag down the settlement '
                                       'matrix for every client.',
                             'example': 'Dolman Law Group describes a pool of 50 to 100 claims, maybe a '
                                        'few more, pulled from thousands of names to pick representative '
                                        'bellwether trials that feed the settlement matrix [Dolman Law '
                                        'Group — qGQGuFYFCF8 @ 00:00:33]. In testosterone, about 600 '
                                        'pooled cases became 100 randomized, 32 in core discovery, and 8 '
                                        'tried [The Federalist Society — vk0M8TfTG9g @ 00:35:27].'},
                            {'name': 'records_frontload_plan',
                             'type': 'textarea',
                             'prompt': 'Describe how you will gather pharmacy records, proof of income, '
                                       'and critical medical records before any plaintiff fact sheet is '
                                       'due. Name who orders records, the target turnaround, and which '
                                       'proof is mandatory before a file enters the inventory.',
                             'example': "By the time defendants get medical authorizations, Lyon's firm "
                                        'has already gathered most of the critical medical records that '
                                        'substantiate the case [Attorney Joseph Lyon — nUl1KZ2z_es @ '
                                        '00:02:45]. Seeger now requires a pharmacy record and proof of '
                                        'income up front, because collecting medical records across an '
                                        'inventory can run tens of millions [The Federalist Society — '
                                        'vk0M8TfTG9g @ 00:56:39].'},
                            {'name': 'fact_sheet_calendar',
                             'type': 'text',
                             'prompt': 'Enter the plaintiff fact sheet deadline for every client in the '
                                       'current inventory and the staff member responsible. Note that fact '
                                       'sheets are sworn, then describe the internal review step that '
                                       'catches inaccurate answers before signature.',
                             'example': 'Fact sheets are sworn with perjury exposure and late filings can '
                                        'lead to dismissal, so every deadline is calendared [LawShelf — '
                                        'sozfq7mjvKE @ 00:12:39]. Our entry: 212 clients, deadlines '
                                        'staggered across three months, a paralegal owner per batch, and '
                                        'an attorney read-through comparing each answer against gathered '
                                        'records before the client signs.'},
                            {'name': 'trial_readiness_audit',
                             'type': 'textarea',
                             'prompt': 'Audit each file for disability or injury claims that could '
                                       'collapse under trial selection or trial-readiness certification. '
                                       'Record any social media, photos, or activities that contradict the '
                                       'claimed injury, and decide whether the file stays, is downgraded, '
                                       'or is dropped.',
                             'example': 'A wood-chopping video and a speedboat trophy shrank one inventory '
                                        'once trial-readiness certification hit [The Federalist Society — '
                                        'vk0M8TfTG9g @ 00:52:08]. Our audit flags a back-injury client '
                                        'posting gym photos and a disability claimant shown on a fishing '
                                        'trip; both are downgraded pending attorney review, and any file '
                                        'that cannot survive trial selection is dropped before the '
                                        'bellwether pool forms.'},
                            {'name': 'expert_match_daubert',
                             'type': 'textarea',
                             'prompt': 'Identify the general causation expert for this docket and confirm '
                                       'the expertise matches the exact product and method at issue. '
                                       'Estimate how a global Daubert ruling against causation would '
                                       'affect every file, and price the inventory against that outcome.',
                             'example': 'A global ruling on whether the drug can cause the disease can '
                                        'dismiss the litigation as a whole [Attorney Joseph Lyon — '
                                        'nUl1KZ2z_es @ 00:04:42]. A forklift expert was excluded for '
                                        'lacking forklift-specific expertise [McGuireWoods LLP — '
                                        'tBtb3Kmq3ZA @ 00:18:39]. Before deposition we run Westlaw Expert '
                                        'Evaluator and PubMed and ask what facts would change the opinion '
                                        '[McGuireWoods LLP — tBtb3Kmq3ZA @ 00:35:31].'},
                            {'name': 'distribution_plan',
                             'type': 'textarea',
                             'prompt': 'Explain how settlement funds will reach each claimant once a '
                                       'global resolution is signed. Describe how you will maintain '
                                       'current addresses, confirm payment delivery, and follow up on '
                                       'uncashed checks so money does not sit unclaimed after '
                                       'distribution.',
                             'example': 'The overdraft MDL left about 80 million dollars in uncashed '
                                        'checks, so distributions must be structured to actually reach '
                                        'claimants [Upchurch Watson White & Max Mediation Group — '
                                        '10ygaMXLKfM @ 00:33:40]. Vioxx settled for $4.85B with about '
                                        'one-third going to fees under retainers [The Federalist Society — '
                                        'vk0M8TfTG9g @ 00:17:07]. Our plan: quarterly address refresh and '
                                        'confirmed-receipt calls on every payment.'}],
                 'completion_gate': 'Do not commit marketing or workup dollars until the payout vehicle is '
                                    'named, the filed and expected case counts clear the cited 20 to 50 '
                                    'case range, leadership funding is confirmed in writing, every fact '
                                    'sheet deadline has an owner, and the inventory has been priced '
                                    'against a global Daubert loss.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Tort Selection and Device Docket Underwriting Scorecard',
                 'purpose': 'Underwrite a tort before buying into it by locating its lifecycle stage, '
                            'testing science and numerosity, discounting purchase economics for fake '
                            'claims and attrition, filtering weak files, and proving product identity and '
                            'injury on every device and pharma file.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Locate the tort on its lifecycle first, because timing beats raw case '
                                  'strength and entry cost rises at every stage from triggering event '
                                  'through settlement.',
                                  'Run the six underwriting gates in order: legal viability, science, '
                                  'numerosity, defendant, venue, and stage, and stop the scorecard at the '
                                  'first gate the tort fails.',
                                  'Discount every quoted return multiple for fake claims and attrition, '
                                  'and price belly-to-belly verification into the acquisition budget '
                                  'rather than treating it as optional overhead.',
                                  'For every device file, secure the original implant surgical report '
                                  'naming the exact product, the documented complication, and any revision '
                                  'or removal surgery before records are purged.',
                                  'Finish by underwriting against a realistic per-case value and an '
                                  'administration timeline of up to 2 to 3 years, then decide between paid '
                                  'acquisition and accepting only files that arrive on their own.'],
                 'fields': [{'name': 'lifecycle_stage',
                             'type': 'text',
                             'prompt': 'Identify the current lifecycle stage of the target tort: '
                                       'triggering event, emerging phase, discovery, Daubert, or '
                                       'settlement. Explain how entry cost has moved since the triggering '
                                       'event and whether the window still justifies acquisition spend '
                                       'today for your firm.',
                             'example': 'Joe Fantini maps a 6-9 month emerging phase and 1-2 years of '
                                        'discovery before Daubert and settlement, with entry cost rising '
                                        'like a stock price at each stage. Power rankings put hair relaxer '
                                        'at 6-9 months and Bard PowerPort almost gone. The panel usually '
                                        'needs more than 25 filed cases before consolidation [LexHive '
                                        'Podcast (Formerly- The Legal Growth Lab) — jn6XvG1gC9w @ '
                                        '00:20:19].'},
                            {'name': 'science_gate',
                             'type': 'textarea',
                             'prompt': 'Summarize the scientific support behind the tort, including the '
                                       'number of studies and subjects. State whether the science clears '
                                       'the underwriting gate, and record which experts you consulted '
                                       'before the MDL forms and what internal documents revealed.',
                             'example': 'The underwriting screen runs six gates: legal viability, science '
                                        'of 2-3 studies with 100+ subjects, numerosity, defendant, venue '
                                        'and stage. Fleming, Nolen & Jez advise talking to experts before '
                                        'the MDL forms, because the internal documents reshape the case '
                                        'like peeling an onion [Fleming, Nolen & Jez — YHzG4RIk3g8 @ '
                                        '00:01:45]. Our tort shows three studies, so the gate is cleared.'},
                            {'name': 'numerosity_math',
                             'type': 'text',
                             'prompt': 'Estimate the injured population behind the tort and apply the '
                                       'share of viable claimants who actually come forward. Show the math '
                                       'that converts that population into a realistic filed-case count '
                                       'and compare it to the consolidation threshold.',
                             'example': 'Only 8-10% of viable claimants come forward, so a 10,000-plus '
                                        'case tort needs roughly 100,000 injured people behind it [LexHive '
                                        'Podcast (Formerly- The Legal Growth Lab) — jn6XvG1gC9w @ '
                                        '00:21:30]. Fantini projected GLP-1s past 10,000 cases, then '
                                        'doubted they would cross it. Our working estimate: 40,000 injured '
                                        'times 9% equals about 3,600 filed cases, far above the 25-case '
                                        'panel floor.'},
                            {'name': 'lead_economics',
                             'type': 'textarea',
                             'prompt': 'Record the quoted lead or case purchase price, the typical payout '
                                       'range, and the projected return multiple. Then discount the '
                                       'projection for fake claims and attrition, explaining what '
                                       'verification cost you are pricing into every purchased file.',
                             'example': 'Buyers quote $5,000 leads against $50K-$250K typical payouts, and '
                                        'purchased cases returned 2x-10x the purchase price over the past '
                                        '5 years [Profit with Law (Moshe Amsel) — tjuCUb5CKVY @ 00:19:40]. '
                                        'Ron Lasorsa found over 20% fake claims in a 15,000-case mesh '
                                        'docket sourced from Indian call centers on a $50M loan [Moore '
                                        'Injury Funding — hZFw0Dvtfuk @ 00:10:18].'},
                            {'name': 'verification_protocol',
                             'type': 'textarea',
                             'prompt': 'Describe the verification steps every purchased or '
                                       'marketer-sourced file passes before money moves, including '
                                       'diagnosis confirmation, notary contact, and rejection windows. '
                                       'Name who performs each step within your firm and what specific '
                                       'result kills the file before workup begins.',
                             'example': 'Belly-to-belly verification with mobile notaries is expensive, '
                                        'but it is less expensive than sanctions or bankruptcy [Moore '
                                        'Injury Funding — hZFw0Dvtfuk @ 00:16:51]. On any medical tort, a '
                                        'medical record confirming the diagnosis is pulled before the lead '
                                        'is accepted, and the 14-day rejection window stays open on every '
                                        'marketer batch [Profit with Law (Moshe Amsel) — tjuCUb5CKVY @ '
                                        '00:31:05].'},
                            {'name': 'weak_case_filter',
                             'type': 'textarea',
                             'prompt': 'List the files you are declining to file into the MDL and the '
                                       'reason for each. Explain how a weak case could become a defense '
                                       'bellwether as the pool narrows, and note any statute of '
                                       'limitations risk disclosed to clients.',
                             'example': 'Weak cases filed into an MDL can become defense bellwethers when '
                                        'the pool is cut from 50 to 30 to 10 [LexHive Podcast (Formerly- '
                                        'The Legal Growth Lab) — jn6XvG1gC9w @ 00:18:12]. Each client '
                                        'receives a letter or certification disclosing possible statute of '
                                        'limitations risk before the file is worked up [On The Docket with '
                                        'Napoli Shkolnik — p519y7c1was @ 00:29:45].'},
                            {'name': 'liability_theory',
                             'type': 'textarea',
                             'prompt': 'State the liability theory for the docket, whether a known product '
                                       'defect, failure to warn, or another theory. If failure to warn '
                                       'applies, explain how you will prove the prescribing doctor would '
                                       'not have prescribed the product with a better warning.',
                             'example': 'The duty to warn runs to the doctor, and the plaintiff must prove '
                                        'the doctor would not have prescribed with a better warning '
                                        '[Justinian & Associates PLLC — _YA0HVm1udc @ 00:08:56]. Stewart & '
                                        "Stewart's aggressive pursuit of a pressure cooker explosion "
                                        'uncovered a seal issue the manufacturer knew about, turning one '
                                        'burn case into a pattern [Stewart & Stewart Attorneys — '
                                        '4iH4c_z7Iw0 @ 00:00:47].'},
                            {'name': 'device_product_id',
                             'type': 'textarea',
                             'prompt': 'For each device or implant file, record the exact product named in '
                                       'the original implant surgical report, the documented complication, '
                                       'and any revision or removal surgery. Note the date records were '
                                       'requested relative to the provider purge window.',
                             'example': 'Secure the original implant surgical report naming the mesh '
                                        'product before records hit the typical 7-to-10-year purge window '
                                        '[Lawsuit Tracker — orLyLTC8fiA @ 00:01:52]. Covidien files are '
                                        'bucketed by product: resorbable collagen-barrier ventral '
                                        'products, ProGrip inguinal with microgrips persisting about 18 '
                                        'months, and bare polyester; discovery showed barrier coating '
                                        'lasting 7 days or less [Jon and Marc — IPkB5-wL-oY @ 00:10:41].'},
                            {'name': 'lone_pine_readiness',
                             'type': 'textarea',
                             'prompt': 'Confirm each Bard hernia mesh or similar file carries immediate '
                                       'proof of use and specific injury evidence. Describe how you will '
                                       'produce a case-specific expert report soon after filing, and '
                                       'identify files that would fail a Lone Pine style order.',
                             'example': 'Lone Pine style docket control now dismisses padded Bard '
                                        'inventory with prejudice, so any file lacking immediate proof of '
                                        'use and specific injury evidence is rejected [Mohr Marketing — '
                                        'agO8HeUx95E @ 00:00:40]. In Bard, a case-specific expert report '
                                        'must be filed pretty soon after the lawsuit [Cut to the Chase '
                                        'Network — JlBWnsNpbyc @ 00:17:25]. Our review rejected 14 files '
                                        'missing operative notes.'},
                            {'name': 'settlement_value_underwrite',
                             'type': 'textarea',
                             'prompt': 'Record the per-case value benchmark you are underwriting against, '
                                       'the expected administration timeline after settlement, and the '
                                       'staff time needed to manage clients. Explain whether paid '
                                       'acquisition is justified or files should only be accepted when '
                                       'they arrive on their own.',
                             'example': "Abbott's NEC inventory deal implied about $80,000 per case, "
                                        'roughly $175 million for about 2,000 cases, so acquisition is '
                                        'underwritten against expensive leads and attrition once records '
                                        'surface [Jon and Marc — 2lQbSEVsxgE @ 00:04:28]. Bard '
                                        'administration can take up to 2 to 3 years, and clients need to '
                                        'be managed on that process [Jon and Marc — IPkB5-wL-oY @ '
                                        '00:04:37].'}],
                 'completion_gate': "Do not buy a single lead until the tort's lifecycle stage is named, "
                                    'the science and numerosity gates are cleared, return projections are '
                                    'discounted for fake claims and attrition, every device file names its '
                                    'exact product from the implant report, and a per-case value benchmark '
                                    'is written down.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Toxic Docket Proof and Acquisition Cost Ledger',
                 'purpose': 'Paper every toxic-exposure and emerging-docket file to the standard '
                            'defendants and administrators demand, protect participation thresholds and '
                            'opt-out rights, budget the settlement-to-funds lag, and measure every lead '
                            'source on cost per retained, settlement-ready case.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Treat proof of injury and proof of exposure as two separate '
                                  'requirements, and do not count a file in the inventory until both are '
                                  'documented from records and work or residency history.',
                                  'Log every deficiency round and fact sheet deadline as it arrives, '
                                  'because filing deadlines and deficiency rounds are the real gatekeepers '
                                  'before any toxic docket pays.',
                                  'Keep client contact data current at all times so participation '
                                  'thresholds near 95% can be reached and opt-outs can be executed with '
                                  'wet signatures and ID inside the window.',
                                  'Budget cash flow on at least a year and a half from settlement to first '
                                  'funds, paid in rolling tranches, before scaling new acquisition on any '
                                  'docket.',
                                  'Measure every vendor and channel on cost per retained, settlement-ready '
                                  'case, not cost per sign, and hold judgment on new vendors until intake '
                                  'confirms clients are reachable.'],
                 'fields': [{'name': 'exposure_proof',
                             'type': 'textarea',
                             'prompt': 'For each toxic-exposure file, document proof of injury from '
                                       'medical records across providers and years, and proof of exposure '
                                       'through work history or residency. Record the identifier used to '
                                       'map residency, such as a water system ID or ZIP code.',
                             'example': 'PFAS files need proof of injury from medical records ordered '
                                        'across providers and years, plus exposure via firefighter work '
                                        'history or residency mapped by PWSID or ZIP code [King Law — '
                                        'aOm5hBG6t9s @ 00:03:52]. It is not enough for someone to simply '
                                        'believe they were exposed or generally know they suffer from a '
                                        'PFAS-associated condition [Napoli Shkolnik — S1VC15_WonY @ '
                                        '00:01:44].'},
                            {'name': 'deficiency_tracker',
                             'type': 'textarea',
                             'prompt': 'Log each deficiency round received from defense counsel, the '
                                       'number of files cited, and the cure deadline. Explain how '
                                       'plaintiff fact sheets and filing deadlines are monitored so no '
                                       'file is scrubbed for qualification or dual-representation '
                                       'problems.',
                             'example': 'King Law has been through four rounds of deficiencies and '
                                        'anticipates another round from defense in the near future [King '
                                        'Law — aOm5hBG6t9s @ 00:04:28]. The AFFF filing deadline drew '
                                        '131,000 cases against 60,000-70,000 expected, the judge postponed '
                                        'the first trial, and the docket was scrubbed toward 80,000-90,000 '
                                        'after dual-rep and qualification problems [Cut to the Chase '
                                        'Network — -H3O5pPP-XA @ 00:07:28].'},
                            {'name': 'participation_threshold',
                             'type': 'textarea',
                             'prompt': 'Record your current reachable-client percentage against any '
                                       'settlement participation threshold, such as 95%. List clients who '
                                       'have moved or died, the estate representatives needed, and the '
                                       'steps you will take to refresh contact data now before enrollment '
                                       'closes.',
                             'example': 'Talc firms are chasing moved and deceased claimants to reach a '
                                        '95% threshold, and excluded clients face an uphill fight [Jon and '
                                        'Marc — NHmq2W3F_do @ 00:05:45]. Aylstock Witkin Kreis & Overholtz '
                                        'reconnected with 20-30% of signed clients after every other '
                                        'channel had failed [Kayse AI — kjUaKK45Ahg @ 00:01:00]. Our '
                                        'status: 91% reachable, 11 estates pending.'},
                            {'name': 'opt_out_mechanics',
                             'type': 'textarea',
                             'prompt': 'If a class settlement threatens to sweep in your clients, describe '
                                       'your opt-out process. Specify the signature format required, the '
                                       'identification collected, the deadline window, and who confirms '
                                       'each opt-out is complete before the file is swept into the class.',
                             'example': 'Roundup opt-outs run on original wet signatures, not DocuSign, '
                                        'with ID inside the 90-day window, or the file is swept into the '
                                        'class [Jon and Marc — 3Qxw8dtCCns @ 00:07:40]. Census data puts '
                                        'the Roundup class average near $70,000, about $40,000 '
                                        'residential, across 10 tiers from $165,000 to $10,000 [Cut to the '
                                        'Chase Network — IHvCfh-WJ6E @ 00:01:34].'},
                            {'name': 'emerging_tort_grading',
                             'type': 'textarea',
                             'prompt': 'Grade each emerging-docket file, such as hair relaxer, rideshare, '
                                       'or spinal cord stimulator, against the specific proofs that docket '
                                       'requires. Record duration of use, documented brand or '
                                       'manufacturer, diagnosis in the charts, and the correct MDL '
                                       'routing.',
                             'example': 'Hair relaxer files are graded on many years of use, a documented '
                                        'brand, and a uterine, ovarian or endometrial diagnosis in the '
                                        'charts [Salenger, Sack, Kimmel & Bavaro, LLP — ch5IVo6DOos @ '
                                        '00:05:33]. Spinal cord stimulator files need the product ID, '
                                        'implant sticker log and operative report to route the case to the '
                                        'correct MDL [Jon and Marc — NHmq2W3F_do @ 00:03:22].'},
                            {'name': 'cash_flow_timeline',
                             'type': 'textarea',
                             'prompt': 'Project the months from settlement announcement to first funds for '
                                       'each active docket, and the tranche schedule you expect. Explain '
                                       'how payroll, advertising, and capital costs will be covered during '
                                       'that lag without forcing premature or discounted client '
                                       'resolutions.',
                             'example': 'Budget at least a year and a half from settlement to first funds, '
                                        'paid in rolling tranches after releases and proof clear [Michael '
                                        'Stanisci — _qBek9AFPiI @ 00:00:35]. AFFF resolved for about $7.35 '
                                        'billion covering 115,000 to 120,000 claims across six injuries '
                                        '[Jon and Marc — 08ES8nUZRYk @ 00:00:39], and first funds are '
                                        'expected in the second half of 2028.'},
                            {'name': 'cost_per_retained_case',
                             'type': 'textarea',
                             'prompt': 'Calculate cost per retained, settlement-ready case for each lead '
                                       'source, not cost per signed retainer. Record raw lead price, '
                                       'conversion rate to retainer, measured attrition, and the resulting '
                                       'true cost so sources can be compared head to head.',
                             'example': 'Attrition of 20-40% is normal, about 30% from 2020 to 2024, and '
                                        'one source fell out at twice the rate of another, so cost per '
                                        'retained case is the true measure [Case Works — My_I0OLHPXc @ '
                                        '00:03:23]. Typical raw-lead-to-retainer conversion runs 3-4% '
                                        '[Advanced Affiliate — Tt2FvNxVuCs @ 00:14:53]. Signed cases range '
                                        'from $300 to six grand [Blue Sky Legal — n9AQhSIMkNg @ '
                                        '00:00:00].'},
                            {'name': 'lead_hygiene_filters',
                             'type': 'textarea',
                             'prompt': 'Describe the automated and human filters every lead passes before '
                                       'reaching workup, including contact congruence checks, TrustedForm '
                                       'certificates, and disqualifying criteria. Explain how filters are '
                                       'tuned so they cut bad leads without inflating cost per lead with '
                                       'no conversion lift.',
                             'example': 'Email/phone congruence checks and TrustedForm run on every lead '
                                        'before workup, because workup is the largest cost in the chain '
                                        'and bad leads should die before it [Case Works — My_I0OLHPXc @ '
                                        '00:06:57]. John Casto found that adding a DQ filter doubled CPL '
                                        'with no conversion lift [Advanced Affiliate — Tt2FvNxVuCs @ '
                                        '00:14:53]. AI does not make a bad lead good.'},
                            {'name': 'vendor_compliance',
                             'type': 'textarea',
                             'prompt': 'For every lead vendor, record proof that the consumer initiated '
                                       "contact, the vendor's generation process, and its true cost to "
                                       'generate. Note the reachability and information-response results '
                                       'intake observed over the first few months before judging the '
                                       'vendor.',
                             'example': 'Before buying, require proof the consumer initiated contact and '
                                        "know the vendor's generation process and true cost to generate, "
                                        'since the firm carries the solicitation exposure [Ron Lasorsa — '
                                        'mmpH5piuvUk @ 00:00:49]. Unreachable clients and refusals to '
                                        'answer basic information requests were the fraud tell a few '
                                        'months in [Tort Experts — AyY5OoT74DQ @ 00:21:03].'},
                            {'name': 'channel_scaling_plan',
                             'type': 'textarea',
                             'prompt': 'Choose the acquisition channels you will scale, such as paid '
                                       'social, SMS, or search, and set the spend controls for each. '
                                       'Record the trailing conversion window you will use and how returns '
                                       'landing past the rejection window are budgeted.',
                             'example': "Scale on today's CPL plus the trailing seven-to-14-day conversion "
                                        'rate and cost per retainer, and budget for returns landing past '
                                        'the 14-day window [Advanced Affiliate — Tt2FvNxVuCs @ 00:18:41]. '
                                        'Paid social runs on bid caps and cost caps across multiple ad '
                                        'accounts [Advanced Affiliate — Tt2FvNxVuCs @ 00:35:02]. SMS runs '
                                        'at $3-4 EPC [OfferVault — dlxuHtoqmYw @ 00:10:18].'}],
                 'completion_gate': 'Do not scale spend on any docket until every counted file carries '
                                    'documented injury and exposure proof, deficiency rounds are logged '
                                    'with cure deadlines, reachable-client percentage is measured against '
                                    'the participation threshold, a settlement-to-funds lag of at least a '
                                    'year and a half is budgeted, and every source is priced on cost per '
                                    'retained case.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Intake Speed, Conversion & Case-Management Stack Audit',
                 'purpose': 'Locate every point where signed-case revenue leaks between the first ring and '
                            'the retained file, then lock intake, retainer tracking, vendor scoring, and '
                            'Filevine or Litify automation into one controlled system of record that '
                            'survives mass-tort volume.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Pull one full week of call logs, recordings, and CRM timestamps before '
                                  'answering any field, so every answer reflects measured performance '
                                  'rather than memory or vendor claims.',
                                  'Record speed-to-contact in minutes and seconds, broken out by mass '
                                  'tort, class action, and assigned attorney, because attorney workup was '
                                  'the hidden slowdown on one audited desk.',
                                  'Freeze any new ad spend until every intake call is recorded and the '
                                  'desk has been audited end to end against the ring, hold, and callback '
                                  'standards set here.',
                                  'Score every lead vendor on cost per retained case rather than cost per '
                                  'sign, and compare sources head to head using daily CRM reports instead '
                                  'of monthly summaries.',
                                  'Treat every automation recipe as a deadline risk: fence it, test it '
                                  'against a single project ID, add error handling, and notify users '
                                  'before it touches live matters.'],
                 'fields': [{'name': 'callback_speed_ladder',
                             'type': 'textarea',
                             'prompt': 'Map your current lead-response timeline from form submission to '
                                       'first outbound dial, and state the target window you will enforce. '
                                       'Name the staffing coverage, overflow route, and redial cadence '
                                       "that guarantee contact before the injured caller's interest decays "
                                       'measurably.',
                             'example': 'Target outbound contact inside 1 to 3 minutes, since injured '
                                        'callers show a 5x drop within 5 minutes [Alert Communications — '
                                        'PJEVefyQCxA @ 00:23:15]. Missing a 60-second callback cuts '
                                        'conversion by over 70% [Saad Khan | AI Automation — ZkN7hMCBwmQ @ '
                                        '00:00:34]. Redials at varied times lift contact to 75% to 80%.'},
                            {'name': 'overflow_ring_cap',
                             'type': 'text',
                             'prompt': 'Document the ring limit, maximum hold time, and the exact point at '
                                       'which unanswered calls roll to a recorded message or overflow '
                                       'center. Explain how you will audit hold times weekly and who owns '
                                       'correcting any breach of the cap.',
                             'example': 'Pickup is capped at three rings and holds at 15 seconds, after '
                                        'which calls roll to a recorded message and an overflow center '
                                        '[Alert Communications — PJEVefyQCxA @ 00:21:02]. One firm was '
                                        'running six-minute holds. Alert also adjusts floor staffing every '
                                        '15 minutes, so the weekly review compares hold logs against those '
                                        'staffing intervals.'},
                            {'name': 'auto_reject_filters',
                             'type': 'textarea',
                             'prompt': 'List every hard disqualifier your system will apply automatically '
                                       'before paid intake staff touch a lead, including jurisdiction, '
                                       'exposure duration, and date windows. Estimate the labor dollars '
                                       'currently wasted processing leads that these filters would have '
                                       'rejected at the door.',
                             'example': 'Auto-reject on jurisdiction, 30-day exposure, and the 1953-1987 '
                                        'window before any paid staff member opens the file. One firm '
                                        'burned $24,000 processing 800 rejected leads [Saad Khan | AI '
                                        'Automation — ZkN7hMCBwmQ @ 00:01:27]. That works out to $30 per '
                                        'rejected lead, which becomes the baseline savings figure for the '
                                        'filter build.'},
                            {'name': 'tort_questionnaire_design',
                             'type': 'textarea',
                             'prompt': 'Describe the tort-specific qualification questionnaire your intake '
                                       'team will run, including which fields are mandatory before the '
                                       'record can advance. Note how you will prevent page clutter that '
                                       'slows specialists, and how the questionnaire grows as criteria for '
                                       'the docket tighten.',
                             'example': 'Questionnaires grew from 4 to 50 questions as tort criteria '
                                        'matured. Fields in the Litify highlights panel are set to '
                                        'required, and banners are limited because too many banners slow '
                                        'the intake page [Litify — 5eCAkl3wUBg @ 00:23:03]. Every intake '
                                        'then ends in one of three exits: open a matter, turn it down, or '
                                        'refer it through the LRN.'},
                            {'name': 'retainer_packet_tracking',
                             'type': 'text',
                             'prompt': 'Explain how retainers are delivered and signed, whether '
                                       'e-signature happens while the caller remains on the line, and how '
                                       'each outstanding packet is tracked until returned. Identify who '
                                       'chases unsigned packets and the follow-up schedule they use.',
                             'example': 'Retainers are e-signed while the caller is still on the line '
                                        'whenever possible. Any packet that goes out unsigned is logged '
                                        'and tracked, because packet tracking alone adds about 15% to '
                                        'conversion [Alert Communications — PJEVefyQCxA @ 00:41:10]. On a '
                                        'floor converting 140 of 200 qualified leads, that lift compounds '
                                        'across every vendor batch.'},
                            {'name': 'vendor_ratio_scorecard',
                             'type': 'textarea',
                             'prompt': 'Build a head-to-head vendor scorecard that pushes every lead into '
                                       'the CRM with daily reporting. Specify the ratio you track for each '
                                       'source, the threshold that triggers a spend cut, and how intake '
                                       'call recordings feed the comparison.',
                             'example': 'Every lead lands in the CRM with a daily report, and vendors are '
                                        'compared head to head; Alert contrasts a vendor at 12:1 with one '
                                        'at 6:1 [Alert Communications — PJEVefyQCxA @ 00:48:26]. New ad '
                                        'spend stays frozen until every call is recorded and audited, '
                                        'since one $30,000 Facebook run ended as a 100% loss.'},
                            {'name': 'ai_agent_vs_human',
                             'type': 'textarea',
                             'prompt': 'Compare the cost and coverage of an AI voice intake agent against '
                                       'round-the-clock human answering for your expected call volume. '
                                       'State which channel handles after-hours calls, which handles '
                                       'qualified escalations, and how you will measure lost conversions '
                                       'on each.',
                             'example': 'The AI voice agent prices at $1 per minute at 1,000 minutes or '
                                        'less, against $2 to $5 per minute for traditional call centers '
                                        "[Legal Lead Sharks Podcast | K'Lee Terrazas — e67Bx9d5FBc @ "
                                        '00:00:46]. Alert counters that converting qualified leads '
                                        'requires lively response 24/7/365, so both channels are '
                                        'benchmarked on the same 70% qualified-conversion target.'},
                            {'name': 'client_journey_comms',
                             'type': 'textarea',
                             'prompt': 'Design the post-signing client journey that sets expectations '
                                       'about MDL timing, shared costs, and individual case status. Name '
                                       'the channels used to reach signed clients, the cadence of updates, '
                                       'and the recovery method for clients who stop responding.',
                             'example': 'An intentional client journey sets expectations so there are no '
                                        'surprises [Chaffin Luhana LLP Injury Lawyers — 5cou1UWhrYw @ '
                                        '00:00:02]. Updates run on a fixed schedule. For lost clients, '
                                        'Aylstock Witkin Kreis & Overholtz reached a 20-30% connection '
                                        'rate after every other channel had failed [Kayse AI — kjUaKK45Ahg '
                                        '@ 00:01:00].'},
                            {'name': 'automation_fencing',
                             'type': 'textarea',
                             'prompt': 'Describe how each new Filevine or Litify automation recipe will be '
                                       'fenced, tested, and released. Include trigger conditions, the test '
                                       'project used, error-handling steps, and the answer to what happens '
                                       'if the automation fails against a filing deadline.',
                             'example': 'Trigger conditions sit on section and field selectors, the API '
                                        'user is excluded, and runs are limited to a single test project '
                                        'ID until proven [Vineskills — YtXAzduQ3PE @ 00:24:15]. Without '
                                        'that fence, one expected item becomes ten thousand. Each recipe '
                                        'also carries an error-handling step, or the assigned user gets '
                                        'spammed with error messages.'},
                            {'name': 'zapier_task_budget',
                             'type': 'text',
                             'prompt': 'Forecast monthly automation task volume for your case count and '
                                       'price it against your connector plan. Identify loops and on-save '
                                       'triggers that inflate task usage, and state whether bulk creates '
                                       'or deletes will ever run in the live environment.',
                             'example': 'About $30 a month covers 750 tasks, roughly 250 cases at 2-3 '
                                        'tasks per case [Vineskills — oNoHY7832hw @ 00:31:13]. High-volume '
                                        'mass-tort clients run closer to a million tasks, near $3,300 a '
                                        'month, so loops get replaced with code blocks. Bulk creates and '
                                        'deletes stay out of live unless an expert builds them.'}],
                 'completion_gate': 'Do not release new ad spend until every intake call is recorded, the '
                                    'three-ring and 15-second hold caps are verified in logs, auto-reject '
                                    'filters are live, retainer packets are tracked to return, and every '
                                    'automation recipe has passed a single test project ID with error '
                                    'handling attached.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'HITECH Record Retrieval, AI Review & Docket Funding Readiness',
                 'purpose': 'Convert medical-record control into a cost advantage, verify every '
                            'AI-assisted chart review against source pages, map the settlement-to-check '
                            'path, and size litigation funding to the real per-case workup burn rather '
                            'than the advertising pitch.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Gather three recent provider invoices for medical records, including at '
                                  'least one digital delivery, so the fee and turnaround fields rest on '
                                  'actual quotes from your own docket.',
                                  'Run a commingled-patient and missing-H&P check on a sample of record '
                                  'sets before filling the quality-control fields, and log how many pages '
                                  'belonged to other patients.',
                                  'Ask every AI, lien, and claims vendor in writing who owns them and what '
                                  'their model trains on, and attach the answers before scoring any '
                                  'vendor.',
                                  'Build the docket valuation by injury subtype, with fee splits, '
                                  'expenses, and surgery dates captured beyond intake, before contacting a '
                                  'single litigation funder.',
                                  'Bring transactional counsel into the funding review before any term '
                                  'sheet turns into a contract, and record every unusual clause flagged '
                                  'during that review.'],
                 'fields': [{'name': 'hitech_digital_request',
                             'type': 'textarea',
                             'prompt': 'Draft your standard electronic medical record request process, '
                                       'including who signs the request, where delivery is directed, and '
                                       'the fee you will accept. Explain how you will respond when a '
                                       'provider attempts per-page billing on digital copies.',
                             'example': 'The request is written by the patient, not the attorney, but '
                                        'directs delivery of records to the firm [The Nomberg Law Firm — '
                                        '_9ZPWIgPW14 @ 00:04:16]. The federal cap on digital copies is '
                                        '$6.50 regardless of page volume, so any 75-cent-per-page digital '
                                        'charge is rejected [The New York Injury & Malpractice Law Firm, '
                                        'P.C. — uJITvDxd4jA @ 00:00:39].'},
                            {'name': 'turnaround_cost_model',
                             'type': 'textarea',
                             'prompt': 'Model the cost and turnaround difference between paper and digital '
                                       'record retrieval for a typical file in your docket. Include page '
                                       'counts, per-page pricing you have been quoted, the digital '
                                       'alternative, and the waiting time each route adds to workup.',
                             'example': 'Two thousand pages arrive in 24 hours on a CD, versus 75 cents a '
                                        'page, about $1,500, and months of waiting [The New York Injury & '
                                        'Malpractice Law Firm, P.C. — JdDeicrkI-o @ 00:03:17]. A 3,000 to '
                                        '5,000 page file billed on paper turns into thousands of dollars, '
                                        'so requests go through records custodians for 24-hour '
                                        'turnaround.'},
                            {'name': 'record_integrity_check',
                             'type': 'textarea',
                             'prompt': 'Define the quality-control check every incoming record set must '
                                       'pass before attorney or nurse review. Address commingled patient '
                                       'pages, missing history and physical documents, illegible '
                                       'handwriting, and the feedback loop you will use with hospitals '
                                       'that repeat errors.',
                             'example': 'At least 2% of every project file carries commingled patients '
                                        'from scanning errors, fixed with NPIs plus OCR and actionable '
                                        'feedback to hospitals [CERIS Health — Coka2u38__k @ 00:25:57]. '
                                        'Every set also gets a missing-H&P check. A five percent error '
                                        'rate on billions is gigantic dollars, so human checks stay in the '
                                        'workflow.'},
                            {'name': 'ai_chart_review_controls',
                             'type': 'textarea',
                             'prompt': 'Specify which AI chart-review tool you will deploy, the record '
                                       'volumes it will process, and the human verification step applied '
                                       'to every output. Describe how you will measure throughput gains '
                                       'against labor-only review on a sample of mass-tort files.',
                             'example': 'Pattern Data reliably sees 7 to 10x better throughput from its '
                                        'litigation lens versus labor-only review [The LegalTech Fund — '
                                        '_HuCGlH6Wyw @ 00:13:03]. Tor Herman Law runs Supio across a '
                                        '43,000-page NICU chart and 86 depositions. Every AI output is '
                                        'still fact-checked against source pages, because blurred records '
                                        'and handwriting can fail OCR [LawNext — Yq68SC86WTQ @ 00:20:26].'},
                            {'name': 'ai_vendor_data_security',
                             'type': 'textarea',
                             'prompt': 'List the questions every AI, lien, or claims vendor must answer '
                                       'before receiving claimant health data. Cover ownership of the '
                                       'vendor, what its language model trains on, where documents are '
                                       'stored, and the disqualifying answers that end the evaluation.',
                             'example': "Every lien or claims vendor is asked 'Who owns you' before any "
                                        'claimant health data changes hands [The Law Firm Brand Builders — '
                                        '73xfuxsKsEM @ 00:24:19]. Every AI vendor is asked what its LLM '
                                        'trains on, and any vendor that trains on user prompts is rejected '
                                        '[Milestone — 1O2RKMH06LU @ 00:29:03]. Client documents stay out '
                                        'of open tools.'},
                            {'name': 'settlement_clearance_liens',
                             'type': 'textarea',
                             'prompt': 'Map the settlement administration path from global deal to '
                                       'claimant checks, including the qualified settlement fund, lien '
                                       'resolution, and estate issues. Identify the lien types you expect '
                                       'to be the long poles and the realistic clearance timeline you will '
                                       'tell clients.',
                             'example': 'Archer generally clears 90% of funds within 10 to 14 months, with '
                                        'VA liens as the long poles [Jon and Marc — 8CBO3CgHLvA @ '
                                        '00:22:02]. Distributions are structured so money actually reaches '
                                        'claimants, since the overdraft MDL left about 80 million dollars '
                                        'in uncashed checks [Upchurch Watson White & Max Mediation Group — '
                                        '10ygaMXLKfM @ 00:33:40].'},
                            {'name': 'workup_capital_sizing',
                             'type': 'text',
                             'prompt': 'Calculate the full per-case workup cost for your docket, including '
                                       'filing fees, record orders, and nurse review, then multiply by '
                                       'your client count. Compare that real burn against the facility '
                                       'size you plan to request from funders.',
                             'example': 'Workup runs about $3,000 per case, covering $400-500 filing fees, '
                                        'medical record orders, and nurse review, so 10,000 clients need '
                                        'roughly $30 million [Slarskey LLC — gdDT2WSKYs0 @ 00:10:38]. The '
                                        'facility is sized to that burn, not the advertising pitch. Rocade '
                                        'writes $10 million to $50 million facilities with a $10 million '
                                        'minimum.'},
                            {'name': 'injury_subtype_valuation',
                             'type': 'textarea',
                             'prompt': 'Replace any per-plaintiff settlement average with a valuation '
                                       'built by injury subtype. Describe which data points beyond intake '
                                       'you will capture, such as fee splits, expenses, and surgery dates, '
                                       'and the quality-control process keeping that data reliable.',
                             'example': 'Every case is valued by injury subtype rather than a settlement '
                                        'average; Rocade modeled three 3M grids in 2020 [The Heart of Law '
                                        'Podcast — Zz1HlCrfQPY @ 00:28:47]. Fee splits, expenses, and '
                                        'surgery dates are captured beyond intake with QC and SOPs in '
                                        'place. Funders underwrite this way because, in their words, data '
                                        'is everything.'},
                            {'name': 'funder_selection_terms',
                             'type': 'textarea',
                             'prompt': 'Profile each funder you will approach, including fund vintage, '
                                       'investment-period status, pricing structure, and recourse terms. '
                                       'Flag any contract clauses that grant unusual control or rights, '
                                       'and note whether repayment depends on case outcomes or functions '
                                       'as a loan.',
                             'example': 'Approach funders right after a fund two closes, and confirm they '
                                        'are still inside the investment period [Slarskey LLC — '
                                        'gdDT2WSKYs0 @ 00:19:28]. Strip clauses such as attorney-in-fact '
                                        'rights on a material risk of bankruptcy. Portfolio pricing runs '
                                        "around a 20% interest rate, paid from the lawyers' slice rather "
                                        "than the plaintiff's [Bloomberg Law — D9nqJXMXzRI @ 00:06:01]."},
                            {'name': 'deal_ratio_and_selectivity',
                             'type': 'text',
                             'prompt': 'Test your funding request against the value-to-commitment ratio '
                                       'and selectivity rates commercial funders apply. State your '
                                       'expected resolution value, the commitment requested, and why your '
                                       'docket belongs in the small share of deals that survive '
                                       'underwriting.',
                             'example': 'A $10 million commitment against a $100 million expected '
                                        'resolution fits the 10x metric [ResTech Solutions — fTOe5KR6QSE @ '
                                        '00:13:12]. Only 5-10% of submitted deals survive underwriting on '
                                        'merits, claim holder, and counsel [TownCenter Partners Litigation '
                                        'Finance — 5XWpCPDxugc @ 00:02:00]. Capital is raised only when '
                                        'reinvestment returns exceed its cost.'}],
                 'completion_gate': 'Do not request funding until per-page digital billing is refused in '
                                    'writing, every record set passes the commingled-patient check, every '
                                    'AI output is verified against source pages, the docket is valued by '
                                    'injury subtype, and the facility request matches the full per-case '
                                    'workup burn.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Law-Firm MSO, Outside Capital & Arizona ABS Structuring',
                 'purpose': 'Design a management services organization or ABS path that brings in outside '
                            'capital without surrendering professional judgment, pricing the services fee '
                            'correctly, benchmarking valuation multiples, and walling client files, intake '
                            'control, and settlement authority off from investors.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['List every non-lawyer asset and function before drafting the MSO '
                                  'carve-out, then mark which items legally must stay inside the law firm '
                                  'under attorney control.',
                                  'Confirm the services fee is flat monthly or cost-plus with a fair '
                                  'margin, and reject any draft that ties compensation to a percentage of '
                                  'revenue or profits.',
                                  'Benchmark every buyer or investor offer against 6-8x market profit '
                                  'multiples, and document the walk-away point before the first '
                                  'negotiation call takes place.',
                                  'Write the capital deployment plan before closing, including '
                                  'reinvestment targets, so equity partners cannot push the incoming money '
                                  'out as compensation.',
                                  'For any Arizona ABS track, appoint a dedicated compliance lawyer with '
                                  'management experience and confirm an Arizona-admitted lawyer personally '
                                  'handles intake and client communication.'],
                 'fields': [{'name': 'mso_asset_carveout',
                             'type': 'textarea',
                             'prompt': 'Inventory the non-lawyer staff, equipment, intellectual property, '
                                       'and brand assets that would move into a management services '
                                       'organization. Separately list everything that must remain inside '
                                       'the law firm, including lawyers, engagement letters, trust '
                                       'accounts, and settlement authority.',
                             'example': 'Non-lawyer staff, equipment, IP and founder likeness spin into a '
                                        'Delaware LLC MSO that leases them back to the firm. Lawyers, '
                                        'engagement letters, trust accounts, hiring, case selection and '
                                        'settlement stay inside the firm. The MSO fee is fixed monthly or '
                                        'cost-plus, validated by a third-party fairness opinion [Confido '
                                        'Legal — 5TjsKzLtyc4 @ 00:23:21].'},
                            {'name': 'mso_fee_structure',
                             'type': 'text',
                             'prompt': 'Set the management services fee structure, choosing between a flat '
                                       'monthly amount and cost-plus with a stated markup. Explain how you '
                                       'will document fairness, how often you will re-price the fee, and '
                                       'why no percentage of revenue appears anywhere.',
                             'example': 'Cost-plus markups typically run 10-15% [Confido Legal — '
                                        '5TjsKzLtyc4 @ 00:25:36]. The fee is re-priced forward-looking '
                                        'only, with the fairness analysis refreshed each time on an annual '
                                        "cadence. Any compensation model that's a percentage of a law "
                                        "firm's revenue is a no-go [Holt Law: For Healthcare Businesses — "
                                        'DNk78wbKy5s @ 00:02:51].'},
                            {'name': 'valuation_multiple_benchmark',
                             'type': 'text',
                             'prompt': 'Benchmark any acquisition or MSO investment offer against market '
                                       'profit multiples for law firms and comparable '
                                       'professional-services deals. Record the offer multiple, the '
                                       'benchmark you will cite, and the walk-away point where the offer '
                                       'is considered light.',
                             'example': 'Shelton benchmarks law-firm offers at 6-8x profit in the market, '
                                        'so a 4x offer reads as light [Ten Golden Rules Internet Marketing '
                                        'for Law Firms — I4F5OYZQJuU @ 00:27:11]. Law firms trade at 4-8x '
                                        'EBITDA while accounting MSO deals sit near 15x. Joe Prencipe '
                                        'pitches buying in at 5x to roll up PI firms running 35% margins.'},
                            {'name': 'control_red_flags',
                             'type': 'textarea',
                             'prompt': 'List the deal terms that would let outside capital control the '
                                       'firm, including intake control, hiring, case selection, and '
                                       'settlement decisions. Describe how majority and minority rights '
                                       'will be contracted up front to keep professional judgment with the '
                                       'lawyers.',
                             'example': "Walk from any buyer whose pitch is 'Once we control client "
                                        "intake, then we control the firm' [Ten Golden Rules Internet "
                                        'Marketing for Law Firms — I4F5OYZQJuU @ 00:28:35]. Majority and '
                                        'minority rights are contracted up front, with hiring, firing, '
                                        'case selection and settlement kept inside the firm, recalling the '
                                        'UnitedLex improper-control finding [Jon and Marc — U2xFBBUm_IU @ '
                                        '00:17:08].'},
                            {'name': 'mso_contract_traps',
                             'type': 'textarea',
                             'prompt': 'Review the proposed management services agreement carefully for '
                                       'restrictive covenants and any personal exposure. Identify '
                                       'non-competes, lawyer or client non-solicits, personal guarantees '
                                       'for unpaid fees, and the replacement language you will demand for '
                                       'each before signing.',
                             'example': 'Strip non-competes, lawyer or client non-solicits, and personal '
                                        'liability for unpaid MSO fees, converting unpaid fees into '
                                        'deferred fees [Confido Legal — 5TjsKzLtyc4 @ 00:42:21]. Frederick '
                                        'Shelton turned down over 60 of 70-plus PE-backed MSOs, about 90%, '
                                        'on behalf of law-firm clients [Ten Golden Rules Internet '
                                        'Marketing for Law Firms — I4F5OYZQJuU @ 00:06:17].'},
                            {'name': 'capital_deployment_plan',
                             'type': 'textarea',
                             'prompt': 'Write the capital deployment plan that will govern any outside '
                                       'money before closing. Specify the reinvestment targets, the '
                                       'expected returns compared with the cost of capital, and the '
                                       'safeguards preventing equity partners from distributing proceeds '
                                       'as compensation.',
                             'example': 'If the money comes in without a plan, there is tremendous '
                                        'pressure from equity partners to pay it out in compensation '
                                        "[Mattern LLC — 8wwcTCIWOXM @ 00:39:23]. There's no magic "
                                        'structure that makes the capital cheaper [Brown Rudnick LLP — '
                                        'QpKDhqASBqM @ 00:43:22]. Capital is raised only when reinvestment '
                                        'returns exceed its cost.'},
                            {'name': 'portfolio_funding_contract',
                             'type': 'textarea',
                             'prompt': 'Evaluate any portfolio funding contract by demanding worked payout '
                                       'examples at multiple outcomes. Describe how the waterfall behaves '
                                       'on a low-but-positive result, the multiple the funder targets, and '
                                       'whether the portfolio is genuinely diversified across torts and '
                                       'stages.',
                             'example': 'The contract carries worked payout examples at different '
                                        'outcomes, because a $7M verdict on a $100M case is the problem '
                                        'scenario [TALKSONLAW — 1kAfGIkF10g @ 00:55:54]. One funder shoots '
                                        'for 1.5 times to secure the deal, with a recent file at 1.54 [Alt '
                                        'Funds Network — FQLjhMdShl0 @ 00:21:40]. Litigation funding is a '
                                        'slow burn at best.'},
                            {'name': 'funding_market_positioning',
                             'type': 'text',
                             'prompt': 'Describe how you will position the firm in a concentrated funding '
                                       'market where few commercial funders dominate. Explain the speed, '
                                       'reliability, and control commitments you will seek, and how '
                                       'current commitment volumes and acceptance rates shape your pitch.',
                             'example': 'With only about 10 commercial funders and repeat business '
                                        'dominating, deals are won at step two on speed, reliability and '
                                        'lack of control [The National Law Review — 9teRv9eFpEc @ '
                                        '00:32:40]. In 2025, 39 funders committed $2.8B across 346 deals. '
                                        'Burford funds only 6-8% of cases reviewed, at mid-20s IRRs '
                                        '[TALKSONLAW — 1kAfGIkF10g @ 00:22:54].'},
                            {'name': 'arizona_abs_compliance',
                             'type': 'textarea',
                             'prompt': 'If pursuing an Arizona alternative business structure, outline the '
                                       'ownership split, the compliance lawyer you will appoint, and the '
                                       'approval timeline you are budgeting. Confirm how an '
                                       'Arizona-admitted lawyer will personally handle intake, record '
                                       'review, and client communication.',
                             'example': 'Non-lawyers may own 100% under a compliance lawyer and 10% '
                                        'disclosure. Approval ran about 4 months and has grown to 6-8 '
                                        'months for 100-1,000 page applications [Law Leaders — Tvn12qG9i5s '
                                        '@ 00:12:25]. An empty Arizona office funneling cases elsewhere is '
                                        'not allowed, so an Arizona-admitted lawyer personally handles '
                                        'intake [The Heart of Law Podcast — poe1CAsUc4U @ 00:36:28].'},
                            {'name': 'staff_upl_and_data_walls',
                             'type': 'textarea',
                             'prompt': 'Describe the unauthorized-practice training every non-attorney '
                                       'staff member will complete and the data walls separating investors '
                                       'from client files. Specify which information outside owners may '
                                       'see, who may quote fees or timelines, and how compliance oversight '
                                       'is staffed.',
                             'example': 'Every staff member gets UPL training; a receptionist never '
                                        "guesses a timeline like '30 days,' and only attorneys quote fees "
                                        '[LegalTechLIVE — ajveDNkk7dg @ 00:37:53]. Outside investors see '
                                        'only revenue and cost data. The compliance lawyer has management '
                                        'experience and is not spread across five to seven firms [The '
                                        'Heart of Law Podcast — OdPOa3osKC0 @ 00:19:39].'}],
                 'completion_gate': 'Do not sign any MSO, investment, or ABS document until the fee is '
                                    'flat monthly or cost-plus with a fairness opinion, restrictive '
                                    'covenants and personal fee liability are stripped, hiring, case '
                                    'selection, and settlement stay inside the firm, and a written capital '
                                    'deployment plan exists.'}]}
