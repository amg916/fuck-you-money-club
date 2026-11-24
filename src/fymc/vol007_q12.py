from __future__ import annotations

CHAPTER_12 = {'id': 'Q12',
 'chapter_id': 'Q12',
 'chapter_number': 12,
 'question_number': 12,
 'slug': 'vol007-q12-holder-reporting-compliance-audit-risk',
 'question_prompt': 'How do holders manage reporting obligations, compliance exposure, and audit risks in '
                    'the programs and industries covered?',
 'kicker': 'Q12 / THE BIG MONEY PLAYBOOKS',
 'title': 'Holder Reporting, Compliance, and Audit Risk',
 'subtitle': 'Texas and Utah reporting, Tennessee negative reports, KUPS reporting technology, '
             'exposure-assessment mistakes, audit preparation and litigation, Delaware VDA invitations, '
             'enforcement penalties, and healthcare trends',
 'layout_template': 'action_worksheet_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'State examiners in Utah, Tennessee, South Carolina and Texas agree with advisors at '
                      'SimekScott, Friedman, Kodiak and Clarus on what triggers audits: non-filing, '
                      'missing industry property types, and M&A. They also agree that receivable credit '
                      'balances are where the real exposure hides. The mechanics run on hard numbers. '
                      'Tennessee penalizes willful failure at $1,000 a day up to $25,000 plus 25 percent '
                      'of the property value. South Carolina requires letters on items of $50 or more, '
                      'sent no more than 120 days before filing. Texas sets a $250 notice floor and a July '
                      '1 deadline. Delaware gives VDA invitees 90 days before referring them to audit. '
                      'Voluntary disclosure cuts the look-back to about ten years and waives penalties. '
                      'The split is about posture: examiners say most holders just need training, while '
                      'attorney Jennifer Borden urges holders to fight auditor overreach, even into '
                      'litigation.',
 'key_metrics': [{'label': 'Tennessee willful failure penalty',
                  'metric': 'Tennessee willful failure penalty',
                  'value': '$1,000 per day up to $25,000, plus 25% of the property value',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Penalty for willful failure to meet holder duties. Negligent failure runs '
                             '$200 per day with a $5,000 maximum.',
                  'source': 'TNTreasury ([KiR-ZUeCE5g @ 00:02:45])'},
                 {'label': 'Holder non-filing rate estimated by states',
                  'metric': 'Holder non-filing rate estimated by states',
                  'value': '65% to 90% of companies that should file are not filing',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Tom Quarry's framing of why states are pushing enforcement and hiring "
                             'contingency-fee auditors.',
                  'source': 'Friedman LLP ([duwB7Y82flc @ 00:02:38])'},
                 {'label': 'State claim rate on remitted property',
                  'metric': 'State claim rate on remitted property',
                  'value': 'Roughly 5% to 10% claimed; 90% to 95% kept by states',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Kodiak's explanation for why states treat unclaimed property as a revenue "
                             'generator and are stepping up enforcement.',
                  'source': 'Kodiak Solutions ([2BplqmdsUpU @ 00:11:04])'},
                 {'label': 'KUPS processing throughput',
                  'metric': 'KUPS processing throughput',
                  'value': '3.5 million records and 350,000 due diligence letters per hour',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Keane's stated platform capacity, with a 14-point data validation check and "
                             'two-point USPS address verification.',
                  'source': 'Keane Unclaimed Property ([UP88bQoP2JU @ 00:01:30])'}],
 'sections': [{'heading': '1. The Practitioner Consensus',
               'paragraphs': ['State examiners and private advisors name the same three audit triggers. '
                              'Clarus Partners starts with failure to file by a company with no filing '
                              'history. Next come incomplete filings that leave out a property type '
                              'endemic to the industry: a manufacturer that remits payables and payroll '
                              'but skips receivables, an oil and gas company with no royalties, a retailer '
                              'that files without gift cards [po0e86TAQwA @ 00:00:20]. The auditor in the '
                              'ucproput Utah and Idaho audit-issues session describes the same flags from '
                              'the state side of the table. Not reporting raises a red flag. Omitted '
                              'property raises a red flag. A merger or reorg raises a red flag because '
                              'records usually get lost [3B5mPVcKPDE @ 00:08:16]. TNTreasury adds '
                              'whistleblower complaints, randomly selected samples, and multi-state audits '
                              "to the list [KiR-ZUeCE5g @ 00:00:21]. Kodiak's Melinda Hyde draws on the "
                              "firm's roughly 250 healthcare assessments and describes states mining their "
                              'own databases. A holder that filed three years ago and then went quiet gets '
                              'an inquiry asking whether it dissolved or was acquired. An unbroken filing '
                              'history therefore works as a defense in its own right [2BplqmdsUpU @ '
                              '00:19:39]. The same examiner adds a reality check on intent: most '
                              'businesses simply do not know what they are doing, need training, and run '
                              'smoothly once shown how. Outright fraud is very rare.',
                              'The second point of agreement is that the money that sinks companies is not '
                              'in the check register. Lori, the unclaimed property principal at '
                              'SimekScott, says clients treat payroll and accounts payable checks as the '
                              'low-hanging fruit but miss how large accounts receivable credits can be '
                              '[p0UoXSbya5E @ 00:01:18]. Managing principal Matt Bauer previously worked '
                              'the state side as an auditor. Bauer says receivables drove a lot of '
                              'exposure and caught controllers and CFOs off guard, because their teams '
                              'chase debits and ignore customers sitting in a credit balance. The ucproput '
                              'auditor puts it bluntly: companies get paid way too much, park the '
                              'overpayment in receivables, and let it sit there. After three years it has '
                              'to go to the state [3B5mPVcKPDE @ 00:00:45]. In healthcare, Melinda Hyde of '
                              'Kodiak calls active patient-account credit balances one of the largest '
                              'sources of unclaimed property. No uncashed check is involved, and the state '
                              'does not care whether a refund was ever processed [2BplqmdsUpU @ 00:20:36]. '
                              "Friedman's Alan Goldenberg and Tom Quarry warn that holders who sweep these "
                              'credits into income get whipsawed. The tax is already paid, there is no '
                              'statute of limitations, and there is no amended-return refund. The full '
                              'amount is still owed to the state when an auditor finds it [duwB7Y82flc @ '
                              '00:15:54].',
                              'Third, every source that addresses past-due liability points the same way: '
                              'disclose before you are found. Tennessee runs a Compliance Disclosure '
                              'Agreement for holders not currently under audit. The holder submits a '
                              'Reporting Method worksheet and its current written procedures, then comes '
                              'into compliance within a set period. It avoids both the audit and the '
                              'penalty fees, and the division never physically reviews its records '
                              "[KiR-ZUeCE5g @ 00:01:55]. South Carolina's Daniel Hanley describes the same "
                              "lever: the treasurer's voluntary disclosure program accepts past-due "
                              'property without assessing interest or penalties [D-PMjgNe-7s @ 00:18:20]. '
                              "Friedman's Alan Goldenberg spells out the trade. An audit can reach back to "
                              'the beginning of the business, while voluntary disclosure typically caps '
                              'the look-back at about ten years and waives penalties. Some states also '
                              'waive the due diligence requirement, provided the holder follows it going '
                              'forward [duwB7Y82flc @ 00:41:49]. Clarus Partners puts the stakes in '
                              'percentages: audit interest and penalty can exceed 50 percent of the '
                              'liability owed in some states. It names VDAs and amnesty programs as the '
                              'way to waive them [po0e86TAQwA @ 00:01:40]. Underneath all of it sits one '
                              'shared prerequisite: written procedures. Tennessee requires them for entry, '
                              'and Friedman notes that some states will not admit a holder to voluntary '
                              'disclosure without an unclaimed property manual in place.'],
               'table': {'caption': 'Where examiners and advisors line up on holder audit risk',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Takeaway',
                                     'Expert Source'],
                         'rows': [['No filing history invites an audit',
                                   'A company that has never filed unclaimed property reports is the first '
                                   'risk factor states screen for',
                                   'Start a filing history now and keep it unbroken every single year',
                                   'Clarus Partners ([po0e86TAQwA @ 00:00:20])'],
                                  ['Missing industry property types are red flags',
                                   'Remitting payables and payroll while skipping receivables, royalties, '
                                   'or gift cards signals an incomplete report',
                                   'Benchmark your filed property types against what your industry '
                                   'normally generates',
                                   'Clarus Partners ([po0e86TAQwA @ 00:00:36])'],
                                  ['Receivable credits are the hidden exposure',
                                   'A former state auditor says receivable credits caught controllers and '
                                   'CFOs off guard because teams chase debits',
                                   'Age every customer credit balance and test it against dormancy before '
                                   'year end',
                                   'SimekScott LLC ([p0UoXSbya5E @ 00:01:52])'],
                                  ['Acquirers inherit historical liability',
                                   'Unclaimed property is not covered by the catch-all tax provision and '
                                   'must be carved out specifically',
                                   'Name unclaimed property and responsible periods explicitly in every '
                                   'purchase agreement',
                                   'SimekScott LLC ([p0UoXSbya5E @ 00:04:14])'],
                                  ['Reporting gaps generate state inquiries',
                                   'States flag holders who filed once and then went silent, asking '
                                   'whether they dissolved or were acquired',
                                   'File every year so you can pull a consecutive history the moment a '
                                   'notice lands',
                                   'Kodiak Solutions ([2BplqmdsUpU @ 00:19:39])'],
                                  ['Upfront disclosure avoids penalties',
                                   'Penalties are avoided when a holder discloses through the Compliance '
                                   'Disclosure Agreement before any audit starts',
                                   'Enter voluntary disclosure before an audit notice arrives, because '
                                   'eligibility ends once you are under audit',
                                   'TNTreasury ([KiR-ZUeCE5g @ 00:02:45])'],
                                  ['Find non-compliance before the auditors do',
                                   'You do not know what you do not know, so an internal review should '
                                   'precede the audit',
                                   'Run a self-review starting with corporate structure, incorporation '
                                   'states, and acquisitions',
                                   'COMPUTERSHARE ([79d39hagJ6U @ 00:01:12])']]}},
              {'heading': '2. Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The annual cycle follows the same five steps everywhere, but the dates and '
                              "thresholds are set state by state. Utah's State Treasurer walks holders "
                              'through review, due diligence, report preparation, NAUPA-format filing, and '
                              'payment. Most property goes dormant at three years and payroll at one. Due '
                              'diligence letters go out between May 1 and September 1, and the report and '
                              'payment are both due by November 1 [hUiiEXcFE0k @ 00:01:48]. Texas runs '
                              'earlier. Reports and payments are due July 1, and due diligence notices go '
                              'out by mail or email 60 days before the due date, but only for property '
                              "valued above $250 [WZH47JEDcEI @ 00:02:37]. South Carolina's Daniel Hanley "
                              'sets the letter floor at $50 and allows letters no more than 120 days '
                              'before filing. In the worked example, an October 15 filing means letters '
                              'can go out no earlier than June 17. With the recommended 30-day response '
                              'window, September 15 is the latest send date [D-PMjgNe-7s @ 00:11:40]. '
                              "Friedman's Alan Goldenberg puts the general window at 60 to 120 days before "
                              'the reporting date and lays out the deadlines. Most states use November 1, '
                              'Maryland uses October 31, and a few use May 1. California and Puerto Rico '
                              'use a two-step process in which a preliminary report comes six or seven '
                              'months before the final one [duwB7Y82flc @ 00:33:41].',
                              "The filing format is fixed: states take the NAUPA electronic layout. Utah's "
                              'treasurer points holders to two third-party vendors, HRS Pro and UP '
                              'Exchange. Small filers can instead key in owners manually on the state '
                              'portal [hUiiEXcFE0k @ 00:02:43]. Texas opens its free manual online tool to '
                              'reports with 30 properties or less. It warns that property codes determine '
                              'the abandonment period, so choosing the right code is the most '
                              'consequential data-entry decision in the report [WZH47JEDcEI @ 00:02:57]. '
                              'South Carolina refuses paper, CD, or USB and requires encrypted or '
                              'password-protected electronic files. It describes UP Exchange and HRS Pro '
                              'as free: sign up, download the NAUPA-formatted Excel template, build the '
                              'report, and upload it [D-PMjgNe-7s @ 00:15:18]. At enterprise scale, '
                              "Keane's pitch for KUPS is throughput. The platform runs a 14-point data "
                              'validation check and two-point USPS address verification. It processes 3.5 '
                              'million records and 350,000 due diligence letters per hour inside one '
                              'repository that holds historical data [UP88bQoP2JU @ 00:01:30]. Deloitte '
                              'runs the same job through its Intella platform. It uses proprietary '
                              'workflows to calculate dormancy and exposure and lets payees respond '
                              'electronically to raise response rates. Kodiak pitches a Turbo Tax model '
                              'for unclaimed property and claims its exemption finds often more than cover '
                              'the total cost of compliance.',
                              "The penalty schedule is the number that gets executives' attention. "
                              'Tennessee charges $200 per day, up to $5,000, for negligent failure to '
                              'report, deliver, or remit. Willful failure costs $1,000 per day, up to '
                              '$25,000, plus 25 percent of the property value [KiR-ZUeCE5g @ 00:02:45]. In '
                              'South Carolina, penalties for a holder that simply refuses to report range '
                              'from 25 percent of the property value to a $10,000 fine. However, a written '
                              'extension request filed before November 1 waives late penalties and '
                              'interest if the report arrives before the extension expires [D-PMjgNe-7s @ '
                              "00:18:36]. Delaware's VDA invitations come with a hard clock. Matt Bauer of "
                              'SimekScott says a recipient must decide within the first 90 days, and '
                              'declining means referral to the Department of Finance for an audit '
                              '[TGu6R9Pc0-4 @ 00:00:19]. The audit math is where the real damage happens. '
                              "Friedman's Tom Quarry describes contingency-fee auditors paid a percentage "
                              "of what they find, look-backs of 15 to 20 years, and Delaware's estimation "
                              'fraction. The auditor takes the error rate from years with records and '
                              'applies it to revenue from years without them. Alan Goldenberg warns that '
                              "this inflates the liability, because today's larger business gets projected "
                              'onto its smaller past [duwB7Y82flc @ 00:29:42]. Kodiak adds that '
                              'auto-assessed interest of 10 to 12 percent a year can push penalty and '
                              'interest past the original principal.'],
               'table': {'caption': 'Hard numbers holders work to, by mechanic',
                         'headers': ['Mechanic',
                                     'Exact Number or Rule',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Utah annual reporting calendar',
                                   'Three-year dormancy, one-year payroll, letters May 1 to September 1, '
                                   'report and pay by November 1',
                                   'Schedule the letter run backward so the report and payment both clear '
                                   'November 1',
                                   'Utah Office of State Treasurer ([hUiiEXcFE0k @ 00:03:20])'],
                                  ['Texas due diligence threshold',
                                   'Mail or email notice 60 days before the July 1 due date for property '
                                   'valued above $250',
                                   'Skip notices on items of $250 or less and calendar the 60-day mark '
                                   'from July 1',
                                   'txcomptroller ([WZH47JEDcEI @ 00:02:37])'],
                                  ['South Carolina letter window',
                                   'Written notice on property of $50 or more, sent no more than 120 days '
                                   'before filing',
                                   'Send at least 30 days before filing so owners have the full response '
                                   'window',
                                   'SC REALTORS ([D-PMjgNe-7s @ 00:10:30])'],
                                  ['Incidental out-of-state property',
                                   'Fewer than 10 accounts totaling less than $1,000 accepted for owners '
                                   'in other states',
                                   'Fold tiny out-of-state balances into the home report after checking '
                                   'the reciprocity matrix',
                                   'SC REALTORS ([D-PMjgNe-7s @ 00:14:04])'],
                                  ['Enterprise processing capacity',
                                   '3.5 million records and 350,000 due diligence letters per hour with '
                                   '14-point validation',
                                   'Outsource high-volume filings to platforms with USPS address '
                                   'verification built in',
                                   'Keane Unclaimed Property ([UP88bQoP2JU @ 00:01:30])'],
                                  ['Tennessee penalty ladder',
                                   'Negligent $200 per day to $5,000; willful $1,000 per day to $25,000 '
                                   'plus 25 percent',
                                   'Price the cost of staying silent against the cost of a Compliance '
                                   'Disclosure Agreement',
                                   'TNTreasury ([KiR-ZUeCE5g @ 00:02:45])'],
                                  ['Delaware VDA invitation clock',
                                   'Decide within 90 days of the invitation or be referred to the '
                                   'Department of Finance for audit',
                                   'Review the Secretary of State sample work plan immediately to judge '
                                   'whether staff can handle the project',
                                   'SimekScott LLC ([TGu6R9Pc0-4 @ 00:00:19])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Moves the advisors use to shrink the bill',
                           'body': 'Four tactics practitioners use to control audit scope, push back on '
                                   'auditor interpretations, and avoid over-reporting.',
                           'items': ["Get the list of participating states directly from each state's "
                                     "notification. Pam Wentz warns that the auditor's list may include "
                                     'every state the firm contracts with, not just the states that '
                                     'actually signed on [COMPUTERSHARE — 79d39hagJ6U @ 00:00:40].',
                                     'Learn the statutes, regulations, and actual state practice before '
                                     'the auditor asks. Jennifer Borden says auditor interpretations often '
                                     'do not line up with what the statutes require, and holders are no '
                                     'longer afraid to say no, even if it leads to litigation '
                                     '[COMPUTERSHARE — 03CoUEgqdzg @ 00:01:47].',
                                     'Hunt for exemptions before remitting. Kodiak counts about 100 '
                                     'healthcare exemption opportunities, including recoupment, '
                                     'business-to-business, and de minimis, and aims to be compliant but '
                                     'not overly compliant [Kodiak Solutions — 2BplqmdsUpU @ 00:28:08].',
                                     'When calling a state about where to send property, give a scenario '
                                     'instead of a yes-or-no question. States sometimes agree to send '
                                     'property where the owner is most likely to look, but scale the '
                                     'effort to the amount: a $75 check does not justify the work a '
                                     '$75,000 check does [ucproput — 3B5mPVcKPDE @ 00:11:13].']},
               'sop_steps': [{'step': 1,
                              'title': 'Map the entity footprint',
                              'action': 'Start the internal review with corporate structure, incorporation '
                                        'states, operating entities, and acquisition history.',
                              'detail': 'Pam Wentz calls corporate structure the single factor with the '
                                        'greatest effect on liability and the key to limiting an audit '
                                        '[COMPUTERSHARE — 79d39hagJ6U @ 00:01:28]. Melinda Hyde adds that '
                                        'you should pull the org chart to capture physician practices, '
                                        'urgent care, surgery centers, imaging, and health plans [Kodiak '
                                        'Solutions — 2BplqmdsUpU @ 00:23:41].'},
                             {'step': 2,
                              'title': 'Scrub the ledgers',
                              'action': 'Review the general ledger, trial balances, voided check register, '
                                        'aged receivable credits, and ERP tolerance write-off settings.',
                              'detail': 'Matt Bauer flags ERPs set to write off differences within $10, '
                                        'which can quietly build into unclaimed credits [SimekScott LLC — '
                                        'p0UoXSbya5E @ 00:02:40]. Friedman reviews voided checks picked up '
                                        'into miscellaneous income, which typically become reportable '
                                        'within three to five years [Friedman LLP — duwB7Y82flc @ '
                                        '00:27:10].'},
                             {'step': 3,
                              'title': 'Run due diligence inside the window',
                              'action': "Send owner letters inside the state's window, give owners a "
                                        '30-day response deadline, and document any owner activity that '
                                        'stops the dormancy clock.',
                              'detail': 'South Carolina requires letters no more than 120 days before '
                                        'filing and recommends allowing at least 30 days for a response '
                                        '[SC REALTORS — D-PMjgNe-7s @ 00:11:40]. A signed W-9 or a '
                                        'change-of-address notice counts as proof of owner awareness, '
                                        'while automatic drafts and interest postings do not [ucproput — '
                                        '3B5mPVcKPDE @ 00:06:07].'},
                             {'step': 4,
                              'title': 'File, pay, and archive',
                              'action': 'Submit a NAUPA-format report with the correct property codes, '
                                        'make one payment per report, and retain the records.',
                              'detail': 'Texas requires electronic submission, payment by July 1, and '
                                        'retention of unclaimed property records for 10 years for later '
                                        'claims or audits [txcomptroller — WZH47JEDcEI @ 00:04:25].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split in holder defense is whether to fold early or fight. '
                              'Jennifer Borden, an attorney with Wharton Consulting Group speaking on '
                              'COMPUTERSHARE, argues the era of holders acquiescing to whatever states and '
                              "auditors demanded is over: with litigation now on the books, 'people aren't "
                              "afraid to fight,' and if an auditor position does not feel right, Borden "
                              'would say no even if that leads to litigation [03CoUEgqdzg @ 00:01:47]. The '
                              'opposite playbook is the voluntary on-ramp. Friedman LLP pitches voluntary '
                              'disclosure as the escape hatch: a look-back typically limited to about ten '
                              'years, waived penalties, and in some states a waived due diligence '
                              'requirement, versus an audit that can reach back to the beginning of the '
                              'business [duwB7Y82flc @ 00:41:49]. Tennessee sells the same trade through '
                              'its Compliance Disclosure Agreement, where the holder submits a proposal of '
                              'Reporting Method worksheet and the division never physically reviews the '
                              "company's unclaimed property records [KiR-ZUeCE5g @ 00:02:20]. The view "
                              'from the Utah audit desk undercuts the adversarial framing entirely: that '
                              'auditor reports most businesses simply do not know what they are doing, '
                              "want to do what's right, and run smoothly as soon as they are trained, with "
                              'real fraud very rarely found [3B5mPVcKPDE @ 00:07:56]. The choice is '
                              'litigated finality versus a negotiated, capped exposure window.',
                              'Practitioners split on how much a holder can lean on reciprocity to '
                              'shortcut multi-state filing. The ucproput Utah and Idaho presenters frame '
                              'reciprocity as a holder benefit, with Utah forwarding property to all 50 '
                              'states plus Puerto Rico and moving over 1 million dollars to other states '
                              'in one calendar year, yet they flag the catch that a state lacking '
                              'priority, Idaho included, cannot indemnify the holder for funds turned over '
                              'to it [3B5mPVcKPDE @ 00:04:01]. Friedman LLP is blunter: clients routinely '
                              'ask to lump everything into one state report and clear the books in a '
                              'single shot, and for the most part states do not allow it, with voluntary '
                              'disclosure clients who try to dump everything into their state of '
                              'incorporation finding it often does not work [duwB7Y82flc @ 00:35:52]. '
                              'South Carolina auditor Daniel Hanley stakes out the narrow middle ground of '
                              'incidental property, fewer than 10 accounts totaling less than $1,000, '
                              'which most states including South Carolina will accept with an out-of-state '
                              'address [D-PMjgNe-7s @ 00:13:46]. Kodiak Solutions shows what ignoring the '
                              'split looks like: a three-hospital Indianapolis-area system reporting every '
                              'vendor check and patient refund to Indiana when reports are likely due to '
                              'dozens of states [2BplqmdsUpU @ 00:16:36]. On this point the practitioners '
                              'treat reciprocity as a small-balance convenience, not a filing strategy.',
                              'The deepest philosophical split is over how much to report at all. Kodiak '
                              'Solutions vice president Jason tells healthcare holders the goal is to be '
                              "'compliant but not overly compliant,' pointing to about 100 healthcare "
                              'exemption opportunities, including an exemption where a payer that never '
                              'recoups its payment leaves the provider owing neither a refund nor a '
                              'report, plus business-to-business and de minimis exemptions that often more '
                              'than cover the total costs of compliance [2BplqmdsUpU @ 00:28:08]. South '
                              "Carolina's program pushes the opposite direction: all property must be "
                              'reported regardless of amount, and reported accounts cannot be reduced by '
                              'fees or service charges unless the act specifically allows it [D-PMjgNe-7s '
                              '@ 00:16:31]. Idaho sits in between as the only state exempting property '
                              'valued at $50 or less, yet holders who skip reporting must keep those '
                              'balances on their records indefinitely because the owner may claim at any '
                              'time, so the ucproput presenter calls reporting anyway advantageous '
                              '[3B5mPVcKPDE @ 00:01:23]. The same tension shows up in negative reporting. '
                              'Tennessee says negative reports are not required but positions a voluntary '
                              'negative report, filed only through ReportItTN after due diligence turns up '
                              'nothing, as one way holders can avoid an audit [KiR-ZUeCE5g @ 00:00:45], '
                              'while South Carolina generally skips negative reporting except after an '
                              'approved extension.'],
               'table': {'caption': 'Competing holder playbooks reported side by side by practitioners',
                         'headers': ['Decision Point For The Holder',
                                     'Playbook A As Taught',
                                     'Playbook B As Taught',
                                     'Expert Source'],
                         'rows': [['Audit posture when auditor positions look wrong',
                                   'Refuse positions that do not match statutes, even if that leads to '
                                   'litigation',
                                   'Enter a voluntary disclosure for a roughly ten-year look-back and '
                                   'waived penalties',
                                   'COMPUTERSHARE ([03CoUEgqdzg @ 00:01:47]); Friedman LLP ([duwB7Y82flc @ '
                                   '00:41:49])'],
                                  ['How to handle property owed to other states',
                                   'Rely on Utah reciprocity, which forwards property to all 50 states '
                                   'plus Puerto Rico',
                                   'File each priority state separately because most states reject one '
                                   'lumped report',
                                   'ucproput ([3B5mPVcKPDE @ 00:04:20]); Friedman LLP ([duwB7Y82flc @ '
                                   '00:35:52])'],
                                  ['How aggressively to shrink the reportable balance',
                                   'Harvest statutory exemptions to stay compliant but not overly '
                                   'compliant',
                                   'Report all property regardless of amount with no unauthorized fee '
                                   'reductions',
                                   'Kodiak Solutions ([2BplqmdsUpU @ 00:28:08]); SC REALTORS ([D-PMjgNe-7s '
                                   '@ 00:16:31])'],
                                  ['When and above what value to send due diligence',
                                   'South Carolina: written notice for $50 or more, no more than 120 days '
                                   'before filing',
                                   'Texas: mail or email notice 60 days before the due date for property '
                                   'over $250',
                                   'SC REALTORS ([D-PMjgNe-7s @ 00:10:30]); txcomptroller ([WZH47JEDcEI @ '
                                   '00:02:37])'],
                                  ['Who builds and maintains the annual holder report',
                                   'Outsource to a consultant tracking 54 sets of regulations or a '
                                   'platform processing 3.5 million records per hour',
                                   'Small filers key reports manually online; Texas allows manual entry '
                                   'for 30 properties or less',
                                   'COMPUTERSHARE ([K64AFLANH3A @ 00:00:49]); Keane Unclaimed Property '
                                   '([UP88bQoP2JU @ 00:01:30]); txcomptroller ([WZH47JEDcEI @ 00:02:57])'],
                                  ['How much money states actually keep each year',
                                   'Friedman measures a breakage rate close to sixty percent of fiscal '
                                   '2015 collections',
                                   'Kodiak puts state claim rates at only around 5 to 10 percent on '
                                   'average',
                                   'Friedman LLP ([duwB7Y82flc @ 00:03:24]); Kodiak Solutions '
                                   '([2BplqmdsUpU @ 00:11:04])'],
                                  ['Where to send property with an ambiguous owner address',
                                   'Apply sourcing priority rules strictly because each state statute has '
                                   'the final say',
                                   'Call the state with scenario context and ask where the owner most '
                                   'likely looks',
                                   'PwC US ([yjxm_QOITBY @ 00:00:57]); ucproput ([3B5mPVcKPDE @ '
                                   '00:10:40])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive firsthand misses are property types holders never think '
                              "to look for. SimekScott's Matt Bauer, drawing on time on the state side as "
                              'an auditor, reports that accounts receivable credits drove a lot of '
                              'exposure and caught controllers and CFOs off guard because receivables '
                              'teams spend their time chasing debits, not customers sitting in a credit '
                              'balance [p0UoXSbya5E @ 00:01:52]. Bauer adds the tolerance trap: an ERP set '
                              'to write off transactions within a $10 differential, positive or negative, '
                              'can quietly generate unclaimed property as credits written off outpace '
                              'debits for a customer [p0UoXSbya5E @ 00:02:40]. Kodiak Solutions executive '
                              'director Melinda Hyde sees the healthcare version, where one of the largest '
                              'sources of property never touches accounts payable at all: active patient '
                              'credit balances where no refund was ever processed, which the state treats '
                              'as property the holder is holding that is not theirs [2BplqmdsUpU @ '
                              '00:20:36]. The Friedman LLP presenters describe walking into major '
                              'companies fifteen years ago that claimed they had none because they took it '
                              'into income, then lay out the whipsaw: tax was already paid on that income, '
                              'the funds still must be remitted on audit, and there is no way to amend the '
                              'return for a refund [duwB7Y82flc @ 00:15:54].',
                              'Once an audit lands, the record-retention gap becomes the loss engine. '
                              'Friedman LLP reports contingency-fee auditors looking for records that go '
                              'back 20 years, a five-year dormancy period plus fifteen years of look-back, '
                              'and when records are gone the holder falls into an estimation fraction '
                              'built from known years and applied to earlier revenue [duwB7Y82flc @ '
                              "00:51:02]. Because businesses grow year over year, applying today's ratios "
                              'to twenty years ago can produce a large liability that voluntary disclosure '
                              'would have avoided. Kodiak Solutions confirms state audits generally reach '
                              'back 15 years, far beyond most retention policies, with contingency-fee '
                              'auditors incentivized to look underneath every nook and cranny [2BplqmdsUpU '
                              '@ 00:12:17]. Pam Wentz on COMPUTERSHARE warns these are not typical audits: '
                              'they last longer, the auditors do not play by typical rules, and the '
                              'participating-state list must come directly from the states, because an '
                              'auditor list may include every state it has a contract with rather than the '
                              'ones that signed on [79d39hagJ6U @ 00:00:40]. Jennifer Borden adds that in '
                              'the last couple of years auditor interpretations have not always lined up '
                              'with what statutes actually require, so holders must know the statutes, '
                              'regulations, and state practice before the exam starts [03CoUEgqdzg @ '
                              '00:01:01].',
                              'The penalty math punishes delay. Tennessee sets negligent failure to '
                              'report, deliver, or remit at $200 per day capped at $5,000, and willful '
                              'failure at $1,000 per day up to $25,000 plus 25% of the value of the '
                              'property the holder had a duty to report [KiR-ZUeCE5g @ 00:02:45]. Kodiak '
                              'Solutions reports states increasingly auto-assess penalties plus 10% to 12% '
                              'annual interest on past-due amounts, and that penalty and interest often '
                              'grow larger than the original principal value of the property [2BplqmdsUpU '
                              '@ 00:12:50]. M&A is the second blind spot. Clarus Partners warns that stock '
                              'acquisitions, or asset transactions where liability was retained, create '
                              "successor liability reaching back to the target's date of incorporation, "
                              'and that these issues are generally missed in merger and acquisition due '
                              "diligence [po0e86TAQwA @ 00:01:08]. SimekScott's principals add that a "
                              'catch-all tax provision does not cover it; unclaimed property has to be '
                              'specifically carved out in the purchase agreement, even asset deals can '
                              'carry receivables with embedded property, and because VDAs and audits can '
                              'take more than a year just to gather records, there is never enough time in '
                              'deal diligence to size the real exposure [p0UoXSbya5E @ 00:04:30].'],
               'table': {'caption': 'Firsthand failure modes and their economic hit as reported by '
                                    'practitioners',
                         'headers': ['Failure Mode Observed In The Field',
                                     'What Went Wrong Firsthand',
                                     'Economic Hit Or Operational Bottleneck',
                                     'Expert Source'],
                         'rows': [['Accounts receivable credit balances never reviewed',
                                   'Receivables teams chase debits and ignore customers sitting in credit '
                                   'balances',
                                   'Drove a lot of audit exposure and blindsided controllers and CFOs',
                                   'SimekScott LLC ([p0UoXSbya5E @ 00:01:52])'],
                                  ['ERP tolerance write-off policy left unchecked',
                                   'System auto-writes off transactions within a $10 differential either '
                                   'direction',
                                   'Credits written off beyond debits accumulate into unreported unclaimed '
                                   'property',
                                   'SimekScott LLC ([p0UoXSbya5E @ 00:02:40])'],
                                  ['Stale checks and credits taken into income',
                                   'Major companies claimed zero property because stale items went to '
                                   'income',
                                   'Tax already paid, funds still remitted on audit, no amended return '
                                   'refund',
                                   'Friedman LLP ([duwB7Y82flc @ 00:16:15])'],
                                  ['Every property reported to one home state',
                                   'Three-hospital system sent every vendor check and patient refund to '
                                   'Indiana',
                                   'Reports were likely due to dozens of states across 54 jurisdictions',
                                   'Kodiak Solutions ([2BplqmdsUpU @ 00:16:36])'],
                                  ['Filing history with gaps between annual reports',
                                   'Holder filed once, then went silent for three years running',
                                   'State database flags possible dissolution or acquisition and generates '
                                   'audit notices',
                                   'Kodiak Solutions ([2BplqmdsUpU @ 00:19:39])'],
                                  ['Payroll outsourced to a third-party administrator',
                                   'Holder assumes the administrator files and remits uncashed payroll '
                                   'checks',
                                   'Holder stays responsible unless it confirms the third party actually '
                                   'remits',
                                   'Friedman LLP ([duwB7Y82flc @ 00:31:01])'],
                                  ['Reissued checks treated as brand new items',
                                   'Holder ages a reissued check from the reissue date instead of original',
                                   'Dormancy runs from the original issue date, so reports land late',
                                   'SC REALTORS ([D-PMjgNe-7s @ 00:08:06])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Stop Points Before Exposure Compounds',
                           'body': 'Each of these checks comes straight from a practitioner who watched '
                                   'holders lose money, time, or leverage by skipping it.',
                           'items': ['When an audit notice arrives, pull the participating-state list from '
                                     "the states' own notifications and never from the auditor, whose list "
                                     'may include every state it has a contract with [COMPUTERSHARE — '
                                     '79d39hagJ6U @ 00:00:40].',
                                     'Before any acquisition closes, loop in counsel with an escheatment '
                                     'specialty and delineate in the purchase agreement who is responsible '
                                     'for unclaimed property and for what periods [SimekScott LLC — '
                                     'p0UoXSbya5E @ 00:04:59].',
                                     'Review the voided check register and stop sweeping voided or stale '
                                     'items into miscellaneous income, because those items become '
                                     'unclaimed property within three to five years [Friedman LLP — '
                                     'duwB7Y82flc @ 00:27:10].',
                                     'If a Delaware VDA invitation arrives, decide within the first 90 '
                                     'days, because declining means referral to the Department of Finance '
                                     'for an unclaimed property audit [SimekScott LLC — TGu6R9Pc0-4 @ '
                                     '00:00:19].']}}],
 'pull_quote': '"If you fail to plan you can plan to fail... I want to know any issues before the auditors '
               'do." — Jennifer Borden, COMPUTERSHARE (03CoUEgqdzg @ 00:00:42).',
 'diagram_id': 'diag-08',
 'action_checklist': ['Test your existing internal controls and make sure staff know what to review across '
                      'payroll accounts, accounts receivable, accounts payable, and bank reconciliations '
                      '[ucproput — 3B5mPVcKPDE @ 00:00:25].',
                      "Send due diligence letters to each owner's last known address, or by email where "
                      'the owner consented, between May 1st and September 1st for Utah filings [Utah '
                      'Office of State Treasurer — hUiiEXcFE0k @ 00:01:31].',
                      'Build the report in the NAUPA format using free holder software such as UP Exchange '
                      'or HRS Pro, then upload directly or attach it to an email [SC REALTORS — '
                      'D-PMjgNe-7s @ 00:15:18].',
                      'Pull an org chart and confirm every entity, including physician practices, urgent '
                      'care, surgery centers, imaging, and health plans, plus every disbursement account, '
                      'is captured in the review [Kodiak Solutions — 2BplqmdsUpU @ 00:24:01].',
                      'Run an internal review before any audit starts, beginning with corporate structure, '
                      'incorporation states, and mergers or acquisitions that drive liability '
                      '[COMPUTERSHARE — 79d39hagJ6U @ 00:01:12].',
                      'If past-due property exists and no audit is underway, apply for the Tennessee CDA '
                      'with a proposal of Reporting Method worksheet and current written procedures '
                      '[TNTreasury — KiR-ZUeCE5g @ 00:01:55].'],
 'statutory_citations': [{'title': 'Friedman LLP — Unclaimed Property: Avoiding Penalties From Increased '
                                   'State Enforcement | FULL Webinar [00:41:49]',
                          'url': 'https://www.youtube.com/watch?v=duwB7Y82flc&t=2509s',
                          'relevance': 'Primary practitioner testimony on voluntary disclosure look-back '
                                       'limits, estimation fractions, and contingency-fee audit exposure.'},
                         {'title': 'TNTreasury — Unclaimed Property in Tennessee: Understanding Audits, '
                                   'Compliance, and Negative Reports [00:02:45]',
                          'url': 'https://www.youtube.com/watch?v=KiR-ZUeCE5g&t=165s',
                          'relevance': 'Primary practitioner testimony on CDA penalty avoidance and '
                                       'negligent versus willful penalty schedules.'},
                         {'title': 'SimekScott LLC — SALT: Top 5 Mistakes Companies Make Evaluating Their '
                                   'Unclaimed Property Exposure. [00:01:52]',
                          'url': 'https://www.youtube.com/watch?v=p0UoXSbya5E&t=112s',
                          'relevance': 'Primary practitioner testimony on accounts receivable credits, '
                                       'tolerance write-offs, and M&A carve-outs from a former state '
                                       'auditor.'},
                         {'title': 'ucproput — (3 of 4) Utah Unclaimed Property Audit Issues [00:07:35]',
                          'url': 'https://www.youtube.com/watch?v=3B5mPVcKPDE&t=455s',
                          'relevance': 'Primary practitioner testimony on audit triggers, reciprocity '
                                       'indemnification limits, and record retention from the state audit '
                                       'side.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'hUiiEXcFE0k',
                       'title': 'Unclaimed Property Reporting Overview',
                       'channel': 'Utah Office of State Treasurer',
                       'author': 'Utah Office of State Treasurer',
                       'text': 'The most convenient way is to pay electronically on the website '
                               'mycash.utah.gov, and please note that both reports and payment are due by '
                               'November 1st.',
                       'tip': 'The most convenient way is to pay electronically on the website '
                              'mycash.utah.gov, and please note that both reports and payment are due by '
                              'November 1st.',
                       'timestamp': 200,
                       'timestamp_seconds': 200,
                       'timestamp_label': '[00:03:20]',
                       'url': 'https://www.youtube.com/watch?v=hUiiEXcFE0k&t=200s',
                       'markdown': '[00:03:20](https://www.youtube.com/watch?v=hUiiEXcFE0k&t=200s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KiR-ZUeCE5g',
                       'title': 'Unclaimed Property in Tennessee: Understanding Audits, Compliance, and '
                                'Negative Reports',
                       'channel': 'TNTreasury',
                       'author': 'TNTreasury',
                       'text': 'Penalties are avoided when a holder discloses unclaimed property upfront '
                               'through the CDA program.',
                       'tip': 'Penalties are avoided when a holder discloses unclaimed property upfront '
                              'through the CDA program.',
                       'timestamp': 165,
                       'timestamp_seconds': 165,
                       'timestamp_label': '[00:02:45]',
                       'url': 'https://www.youtube.com/watch?v=KiR-ZUeCE5g&t=165s',
                       'markdown': '[00:02:45](https://www.youtube.com/watch?v=KiR-ZUeCE5g&t=165s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UP88bQoP2JU',
                       'title': 'Keane Unclaimed Property System (KUPS)',
                       'channel': 'Keane Unclaimed Property',
                       'author': 'Keane Unclaimed Property',
                       'text': 'KUPS can process 3.5 million records and 350,000 due-diligence letters per '
                               'hour.',
                       'tip': 'KUPS can process 3.5 million records and 350,000 due-diligence letters per '
                              'hour.',
                       'timestamp': 90,
                       'timestamp_seconds': 90,
                       'timestamp_label': '[00:01:30]',
                       'url': 'https://www.youtube.com/watch?v=UP88bQoP2JU&t=90s',
                       'markdown': '[00:01:30](https://www.youtube.com/watch?v=UP88bQoP2JU&t=90s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'K64AFLANH3A',
                       'title': 'Unclaimed Property Regulation',
                       'channel': 'COMPUTERSHARE',
                       'author': 'COMPUTERSHARE',
                       'text': 'It would be great if we could come up with a single regulation so that we '
                               'can follow it and put our energy towards that instead of towards keeping '
                               'up with 54 sets of regulations.',
                       'tip': 'It would be great if we could come up with a single regulation so that we '
                              'can follow it and put our energy towards that instead of towards keeping up '
                              'with 54 sets of regulations.',
                       'timestamp': 28,
                       'timestamp_seconds': 28,
                       'timestamp_label': '[00:00:28]',
                       'url': 'https://www.youtube.com/watch?v=K64AFLANH3A&t=28s',
                       'markdown': '[00:00:28](https://www.youtube.com/watch?v=K64AFLANH3A&t=28s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '79d39hagJ6U',
                       'title': 'Preparing for an unclaimed property audit',
                       'channel': 'COMPUTERSHARE',
                       'author': 'COMPUTERSHARE',
                       'text': "You're going to want to get a list of the participating states, and it's "
                               'very important that that list comes directly from the states; do not rely '
                               'on a list from the auditors.',
                       'tip': "You're going to want to get a list of the participating states, and it's "
                              'very important that that list comes directly from the states; do not rely '
                              'on a list from the auditors.',
                       'timestamp': 40,
                       'timestamp_seconds': 40,
                       'timestamp_label': '[00:00:40]',
                       'url': 'https://www.youtube.com/watch?v=79d39hagJ6U&t=40s',
                       'markdown': '[00:00:40](https://www.youtube.com/watch?v=79d39hagJ6U&t=40s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'po0e86TAQwA',
                       'title': 'Mitigating Unclaimed Property Risk: Best Practices for Compliance',
                       'channel': 'Clarus Partners',
                       'author': 'Clarus Partners',
                       'text': 'These factors matter because they lead to audits, and audits include the '
                               'addition of interest and penalty which in some states could be greater '
                               'than 50% of the liability owed.',
                       'tip': 'These factors matter because they lead to audits, and audits include the '
                              'addition of interest and penalty which in some states could be greater than '
                              '50% of the liability owed.',
                       'timestamp': 85,
                       'timestamp_seconds': 85,
                       'timestamp_label': '[00:01:25]',
                       'url': 'https://www.youtube.com/watch?v=po0e86TAQwA&t=85s',
                       'markdown': '[00:01:25](https://www.youtube.com/watch?v=po0e86TAQwA&t=85s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'p0UoXSbya5E',
                       'title': 'SALT: Top 5 Mistakes Companies Make Evaluating Their Unclaimed Property '
                                'Exposure.',
                       'channel': 'SimekScott LLC',
                       'author': 'SimekScott LLC',
                       'text': 'As my time on the other side of this issue on the state side as an '
                               'auditor, the accounts receivable area certainly did drive a lot of '
                               'exposure for companies.',
                       'tip': 'As my time on the other side of this issue on the state side as an auditor, '
                              'the accounts receivable area certainly did drive a lot of exposure for '
                              'companies.',
                       'timestamp': 112,
                       'timestamp_seconds': 112,
                       'timestamp_label': '[00:01:52]',
                       'url': 'https://www.youtube.com/watch?v=p0UoXSbya5E&t=112s',
                       'markdown': '[00:01:52](https://www.youtube.com/watch?v=p0UoXSbya5E&t=112s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '03CoUEgqdzg',
                       'title': 'Litigation and unclaimed property audits',
                       'channel': 'COMPUTERSHARE',
                       'author': 'COMPUTERSHARE',
                       'text': "Now with all the litigation we've had, people aren't afraid to fight, so "
                               "if something doesn't feel right I would not be afraid to say no even if "
                               'that may lead to litigation.',
                       'tip': "Now with all the litigation we've had, people aren't afraid to fight, so if "
                              "something doesn't feel right I would not be afraid to say no even if that "
                              'may lead to litigation.',
                       'timestamp': 107,
                       'timestamp_seconds': 107,
                       'timestamp_label': '[00:01:47]',
                       'url': 'https://www.youtube.com/watch?v=03CoUEgqdzg&t=107s',
                       'markdown': '[00:01:47](https://www.youtube.com/watch?v=03CoUEgqdzg&t=107s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UC28yxW8Pls',
                       'title': 'Unclaimed Property',
                       'channel': 'Deloitte US',
                       'author': 'Deloitte US',
                       'text': 'Managing your unclaimed property compliance risks is as important now as '
                               'ever as states may ramp up audit efforts in the face of economic '
                               'uncertainties.',
                       'tip': 'Managing your unclaimed property compliance risks is as important now as '
                              'ever as states may ramp up audit efforts in the face of economic '
                              'uncertainties.',
                       'timestamp': 21,
                       'timestamp_seconds': 21,
                       'timestamp_label': '[00:00:21]',
                       'url': 'https://www.youtube.com/watch?v=UC28yxW8Pls&t=21s',
                       'markdown': '[00:00:21](https://www.youtube.com/watch?v=UC28yxW8Pls&t=21s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yjxm_QOITBY',
                       'title': 'Abandoned and Unclaimed Property Quarterly - April 2024',
                       'channel': 'PwC US',
                       'author': 'PwC US',
                       'text': 'One common pitfall is dealing with incomplete addresses, which can lead to '
                               'premature escheatment.',
                       'tip': 'One common pitfall is dealing with incomplete addresses, which can lead to '
                              'premature escheatment.',
                       'timestamp': 23,
                       'timestamp_seconds': 23,
                       'timestamp_label': '[00:00:23]',
                       'url': 'https://www.youtube.com/watch?v=yjxm_QOITBY&t=23s',
                       'markdown': '[00:00:23](https://www.youtube.com/watch?v=yjxm_QOITBY&t=23s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3B5mPVcKPDE',
                       'title': '(3 of 4) Utah Unclaimed Property Audit Issues',
                       'channel': 'ucproput',
                       'author': 'ucproput',
                       'text': 'What I have found out on audits is that most businesses do not know what '
                               'they are doing, that they need training, and most of them want to do '
                               "what's right.",
                       'tip': 'What I have found out on audits is that most businesses do not know what '
                              "they are doing, that they need training, and most of them want to do what's "
                              'right.',
                       'timestamp': 476,
                       'timestamp_seconds': 476,
                       'timestamp_label': '[00:07:56]',
                       'url': 'https://www.youtube.com/watch?v=3B5mPVcKPDE&t=476s',
                       'markdown': '[00:07:56](https://www.youtube.com/watch?v=3B5mPVcKPDE&t=476s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'D-PMjgNe-7s',
                       'title': 'SCR Webinar: Unclaimed Property Program Overview',
                       'channel': 'SC REALTORS',
                       'author': 'SC REALTORS',
                       'text': 'To ease the reporting burden most states including South Carolina will '
                               'accept incidental property with a last known address in another state.',
                       'tip': 'To ease the reporting burden most states including South Carolina will '
                              'accept incidental property with a last known address in another state.',
                       'timestamp': 826,
                       'timestamp_seconds': 826,
                       'timestamp_label': '[00:13:46]',
                       'url': 'https://www.youtube.com/watch?v=D-PMjgNe-7s&t=826s',
                       'markdown': '[00:13:46](https://www.youtube.com/watch?v=D-PMjgNe-7s&t=826s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TGu6R9Pc0-4',
                       'title': 'Delaware Unclaimed Property VDA Invitations - April 11 2025',
                       'channel': 'SimekScott LLC',
                       'author': 'SimekScott LLC',
                       'text': 'You have to take action within the first 90 days, and if you decide not to '
                               'participate, you will be referred to the Department of Finance for an '
                               'unclaimed property audit.',
                       'tip': 'You have to take action within the first 90 days, and if you decide not to '
                              'participate, you will be referred to the Department of Finance for an '
                              'unclaimed property audit.',
                       'timestamp': 19,
                       'timestamp_seconds': 19,
                       'timestamp_label': '[00:00:19]',
                       'url': 'https://www.youtube.com/watch?v=TGu6R9Pc0-4&t=19s',
                       'markdown': '[00:00:19](https://www.youtube.com/watch?v=TGu6R9Pc0-4&t=19s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'duwB7Y82flc',
                       'title': 'Unclaimed Property: Avoiding Penalties From Increased State Enforcement | '
                                'FULL Webinar',
                       'channel': 'Friedman LLP',
                       'author': 'Friedman LLP',
                       'text': 'The benefit is that there is a limited look-back period; unclaimed '
                               'property audits can go back to the beginning of the business operation, '
                               'but voluntary disclosures are typically limited to about ten years.',
                       'tip': 'The benefit is that there is a limited look-back period; unclaimed property '
                              'audits can go back to the beginning of the business operation, but '
                              'voluntary disclosures are typically limited to about ten years.',
                       'timestamp': 2509,
                       'timestamp_seconds': 2509,
                       'timestamp_label': '[00:41:49]',
                       'url': 'https://www.youtube.com/watch?v=duwB7Y82flc&t=2509s',
                       'markdown': '[00:41:49](https://www.youtube.com/watch?v=duwB7Y82flc&t=2509s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'duwB7Y82flc',
                       'title': 'Unclaimed Property: Avoiding Penalties From Increased State Enforcement | '
                                'FULL Webinar',
                       'channel': 'Friedman LLP',
                       'author': 'Friedman LLP',
                       'text': 'Third-party auditors operating on a contingency basis are very aggressive, '
                               "and I've seen situations where they will look for records that go back 20 "
                               'years.',
                       'tip': 'Third-party auditors operating on a contingency basis are very aggressive, '
                              "and I've seen situations where they will look for records that go back 20 "
                              'years.',
                       'timestamp': 3062,
                       'timestamp_seconds': 3062,
                       'timestamp_label': '[00:51:02]',
                       'url': 'https://www.youtube.com/watch?v=duwB7Y82flc&t=3062s',
                       'markdown': '[00:51:02](https://www.youtube.com/watch?v=duwB7Y82flc&t=3062s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2BplqmdsUpU',
                       'title': '5 healthcare unclaimed property compliance trends you need to know',
                       'channel': 'Kodiak Solutions',
                       'author': 'Kodiak Solutions',
                       'text': 'What we like to say is we want you to be compliant but not overly '
                               'compliant.',
                       'tip': 'What we like to say is we want you to be compliant but not overly '
                              'compliant.',
                       'timestamp': 1688,
                       'timestamp_seconds': 1688,
                       'timestamp_label': '[00:28:08]',
                       'url': 'https://www.youtube.com/watch?v=2BplqmdsUpU&t=1688s',
                       'markdown': '[00:28:08](https://www.youtube.com/watch?v=2BplqmdsUpU&t=1688s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WZH47JEDcEI',
                       'title': 'Unclaimed Property: Holder Reporting - General',
                       'channel': 'txcomptroller',
                       'author': 'txcomptroller',
                       'text': 'Businesses must mail or email a due diligence notice 60 days before the '
                               'due date to all owners of unclaimed property valued at more than $250.',
                       'tip': 'Businesses must mail or email a due diligence notice 60 days before the due '
                              'date to all owners of unclaimed property valued at more than $250.',
                       'timestamp': 157,
                       'timestamp_seconds': 157,
                       'timestamp_label': '[00:02:37]',
                       'url': 'https://www.youtube.com/watch?v=WZH47JEDcEI&t=157s',
                       'markdown': '[00:02:37](https://www.youtube.com/watch?v=WZH47JEDcEI&t=157s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'}]}
