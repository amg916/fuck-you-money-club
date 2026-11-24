from __future__ import annotations

CHAPTER_3 = {'id': 'Q3',
 'chapter_id': 'Q3',
 'chapter_number': 3,
 'question_number': 3,
 'slug': 'servicing-remanufacturing-third-party-biomed-business',
 'question_prompt': 'What rules govern third-party servicing, remanufacturing, and reprocessing, and how '
                    'is the independent biomed service business changing?',
 'kicker': 'Q3 / THE BIG MONEY PLAYBOOKS',
 'title': 'Servicing, Remanufacturing, and the Third-Party Biomed Business',
 'subtitle': 'FDA servicing vs. remanufacturing updates, the Medical Device Servicing Collaborative '
             'Community, ISO 13485 servicing clauses, low-quality remanufactured parts and total cost of '
             'ownership, reprocessing validation and labeling, starting a biomed business, private-equity '
             'consolidation, eQMS for equipment companies, UDI/GUDID device identification, and CBET and '
             'lab career paths',
 'layout_template': 'financial_analysis',
 'reading_time_minutes': 15,
 'executive_summary': 'Third-party servicing already carries most of the installed base. A TechNation FDA '
                      'webinar panelist states that the majority of devices are serviced by someone other '
                      "than the OEM, and Wang's data shows 6 maintenance-linked incidents across about 10 "
                      'million devices. Operators agree the edge comes from people, parts, and paperwork: '
                      'trained techs, OEM-spec parts, and service reports routed into CAPA. On the street, '
                      'Jason of Bright Idea Dental Repair launched on $8,000 of test gear, priced at $150 '
                      'and then $175 an hour, and sells $200-a-month PM memberships targeting $4k a month '
                      'per tech. Summit Imaging shows how knockoff parts running at 60% of OEM performance '
                      'inflate total cost of ownership through downtime. Practitioners split on QMS '
                      'mandates costing $50k to $200k, on CBET value, on contract underbidding ahead of '
                      'private-equity sales, and on how hard to fight OEMs for access.',
 'key_metrics': [{'label': 'Maintenance-Linked Incident Rate',
                  'metric': 'Maintenance-Linked Incident Rate',
                  'value': '6 of ~500 incidents across ~10M devices (6.5 Sigma)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Wang's incident analysis presented on the TechNation FDA webinar to show "
                             'that maintenance, including third-party maintenance, drives almost no device '
                             'incidents',
                  'source': 'TechNation TV ([C3pxzDnP6HM @ 00:42:32])'},
                 {'label': 'Dental Service Rate Card',
                  'metric': 'Dental Service Rate Card',
                  'value': '$175/hr regular, $225/hr after hours, $75 travel beyond 30 minutes',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Jason's current Bright Idea Dental Repair pricing, billed on four lines: "
                             'labor, parts, travel, and shipping',
                  'source': 'Better Biomed Channel ([YXLWY7VHfxM @ 00:35:36])'},
                 {'label': 'ISO 13485 Implementation Cost',
                  'metric': 'ISO 13485 Implementation Cost',
                  'value': '$50,000 to $200,000 over 12 to 24 months',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Dave of TKA's estimate of what a mandated ISO 13485 quality system would "
                             "cost independent servicers, enough to ruin 'garage' ISOs",
                  'source': 'TechNation TV ([kmzmXxn2MBE @ 00:31:12])'},
                 {'label': 'In-House Clinical Engineering Savings',
                  'metric': 'In-House Clinical Engineering Savings',
                  'value': '42% to 75%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Savings Summit Imaging reports hearing from facilities that build in-house '
                             'clinical engineering instead of outsourcing service',
                  'source': 'TechNation TV ([7d4lxsuW9Xs @ 00:10:03])'}],
 'sections': [{'id': 1,
               'title': 'The Practitioner Consensus',
               'paragraphs': ['Every serious operator starts from one baseline: the OEM is not doing most '
                              'of the work. Crawford of Block told a TechNation FDA webinar, which drew '
                              'over 390 concurrent attendees, that the majority of medical devices in the '
                              'marketplace are being serviced by someone other than the original '
                              'manufacturer [C3pxzDnP6HM @ 00:21:33]. Dave Franco of TK/Technology '
                              'Associates, an independent service organization, has 35 years in the field. '
                              'Franco reports that there was no evidence that non-OEM servicing was lower '
                              'quality or less safe [lSIrqUmOamc @ 00:22:16]. Wang brought hard numbers to '
                              'the same webinar: roughly 500 incidents, only 6 traced to maintenance, '
                              'across about 10 million devices, which is a 6.5 Sigma result. Wang also '
                              'cited a set of 1,500 responses with 12 adverse events and none from '
                              'maintenance [C3pxzDnP6HM @ 00:42:32]. Scott Carson, a 30-year veteran who '
                              "helped build eBay's healthcare marketplace, adds the economic case. Carson "
                              'argues that most servicing is already done by third parties and that '
                              "without resale 'we probably wouldn't be able to afford health care.' The "
                              'bright line everyone respects is remanufacturing. Servicing cannot change '
                              'intended use. Remanufacturing significantly changes performance, safety, or '
                              "intended use and falls outside the servicing community's scope entirely. "
                              'Independents protect their model by keeping repairs inside servicing '
                              '[lSIrqUmOamc @ 00:11:38].',
                              'Ask practitioners what separates good service from bad, and the answer is '
                              'not the logo on the truck. Tamore told the FDA webinar that there is no '
                              'disparity between OEM and third-party work when staff are trained and parts '
                              'are OEM-spec, and another panelist put it plainly: the common denominator '
                              'is people [C3pxzDnP6HM @ 00:50:31]. Franco breaks safe servicing into five '
                              'components: skill sets, resources, parts, tools, and location. Franco '
                              'insists that it should not matter where your paycheck comes from, and that '
                              'neither a 100% OEM nor a 100% non-OEM market can work [lSIrqUmOamc @ '
                              '00:46:29]. Aaron Snider of Quality Systems Explained lays out the floor for '
                              'any servicer. Personnel must be trained to the servicing procedures and '
                              "must understand the customer's requirements. Procedures, testing, and "
                              'controls must be defined wherever a reusable device degrades over time, and '
                              'Snider notes that a device requiring installation likely requires servicing '
                              'too [ohnyLE9h6ok @ 00:01:10]. Larry Nolen of Summit Imaging closes the loop '
                              'on parts, arguing that quality is what actually delivers the lowest '
                              'long-term total cost of ownership and the best patient care [7d4lxsuW9Xs @ '
                              '01:09:53]. The shared playbook is blunt: hire or train competent techs, '
                              'source parts you can defend, and document every job.',
                              'The third consensus point is paperwork, because the record is what a '
                              'servicer actually hands an auditor. Snider says every service report must '
                              'be reviewed to decide whether it is a complaint and whether that complaint '
                              'is reportable. Each record carries the device name, lot number, services '
                              'done, performer, date, and related test records, and reports flow into CAPA '
                              "for tracking and trending [ohnyLE9h6ok @ 00:01:30]. Matrix One's QMS "
                              'walkthrough repeats the same requirement: servicing records must include '
                              'the device, the date, who serviced it, the service performed, and any test '
                              'and inspection data [URXL-ymHf4w @ 00:01:18]. Noak framed the CMMS as an '
                              'extension of the OEM device file [C3pxzDnP6HM @ 00:11:06]. Unique device '
                              'identifiers tighten the trail. Jonathan Bratz recalls that in their own '
                              'distributor practice, proprietary item numbers made recalls difficult, '
                              'which is the exact problem a single harmonized global UDI is meant to fix '
                              '[fB0ZiAL0q20 @ 00:02:27]. Snider describes what working well looks like: '
                              'servicing procedures in the device master record, trained in-house '
                              'servicers, and compliant records. The failure picture is the inverse: no '
                              'procedures or no DMR link, untrained personnel, and records that are lost, '
                              'destroyed, or unavailable. A final check confirms that records point back '
                              'to the device history record.'],
               'table': {'caption': 'Where the practitioners line up on third-party servicing fundamentals',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Third parties already service most of the installed base',
                                   'The majority of devices in the market are serviced by someone other '
                                   'than the OEM',
                                   'Position the business as the default service channel rather than the '
                                   'exception',
                                   'TechNation TV ([C3pxzDnP6HM @ 00:21:33])'],
                                  ['Non-OEM servicing has a defensible safety record',
                                   'About 500 incidents, only 6 from maintenance, across roughly 10 '
                                   'million devices at 6.5 Sigma',
                                   'Cite maintenance-incident data when hospitals or OEMs question '
                                   'third-party safety',
                                   'TechNation TV ([C3pxzDnP6HM @ 00:42:32])'],
                                  ['Servicing and remanufacturing are separate businesses',
                                   'Remanufacturing significantly changes performance, safety, or intended '
                                   'use; servicing never changes intended use',
                                   'Keep every repair inside servicing scope to avoid becoming a '
                                   'manufacturer',
                                   'TechNation TV ([lSIrqUmOamc @ 00:11:38])'],
                                  ['Training and parts quality decide service outcomes',
                                   'There is no disparity between OEM and third-party work with trained '
                                   'staff and OEM-spec parts',
                                   'Invest in technician training and defensible parts sourcing before '
                                   'spending on marketing',
                                   'TechNation TV ([C3pxzDnP6HM @ 00:50:31])'],
                                  ['Service reports feed the quality system directly',
                                   'Every report is reviewed for complaint and reportability status, then '
                                   'tracked and trended in CAPA',
                                   'Build a complaint-review step into every closed work order',
                                   'Quality Systems Explained ([ohnyLE9h6ok @ 00:01:30])'],
                                  ['Equipment lives far longer than the original sale',
                                   'Products stay in the channel for 15 to 25 years after the first sale',
                                   'Plan service, parts, and resale revenue around multi-decade device '
                                   'lifecycles',
                                   'Greenlight Guru ([l108Vrz9wLo @ 00:25:42])'],
                                  ['Quality parts lower total cost of ownership',
                                   'Quality delivers the lowest long-term total cost of ownership and the '
                                   'best patient care',
                                   'Sell quality on the downtime and TCO math, not on sticker price',
                                   'TechNation TV ([7d4lxsuW9Xs @ 01:09:53])']]}},
              {'id': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Jason of Bright Idea Dental Repair, a former USAF biomed, built the '
                              'clearest launch template. Side work began at $50 an hour, until a dentist '
                              'reported a major supplier billing $75 for travel plus $150 per half hour. '
                              'Jason countered with no travel charge at $150 an hour, and the dentist said '
                              "'deal' [YXLWY7VHfxM @ 00:02:56]. The launch rode on a 'three-legged stool': "
                              'Guard pay with health insurance, the GI Bill, and the business itself. '
                              'Jason pulled $8,000 from savings for test equipment and started under the '
                              'name JnD Medical Maintenance [YXLWY7VHfxM @ 00:05:49]. Michigan red tape '
                              'was minimal. An LLC cost about $50, and x-ray installs required the 2579 '
                              'form, mailed to the FDA and copied to the state, while Ohio requires '
                              'training. Insurance was the real wall, because water-damage liability '
                              "scared carriers off. Coverage started at 'a couple grand a year' and now "
                              'runs through McCready [YXLWY7VHfxM @ 00:12:30]. Jason would start '
                              "dental-only today, arguing that private-sector biomed has 'not enough "
                              "pain.' By contrast, water-based dental delivery units, autoclaves, suction, "
                              'and compressors all need service. Staying lean matters. Dave of TKA warns '
                              'that a mandated ISO 13485 system would cost $50k to $200k and take 12 to 24 '
                              "months, which is enough to ruin 'garage' ISOs [kmzmXxn2MBE @ 00:31:12].",
                              "Jason's current rate card is $175 an hour regular, $225 after hours, and "
                              '$75 travel for any customer more than 30 minutes out. Invoices carry four '
                              'lines: labor, parts, travel, and shipping, and Michigan taxes both parts '
                              'and shipping [YXLWY7VHfxM @ 00:35:36]. Recurring revenue comes from a PM '
                              'membership: $200 a month buys 2 hours plus a 25-point inspection. Seven '
                              'offices are enrolled, and the target is 20 offices per tech, or $4k a month '
                              'per tech, with a 5-gallon parts bucket staged for each customer '
                              '[YXLWY7VHfxM @ 00:46:29]. Prospecting is pure street work. Jason runs a '
                              "Yelp 'dentist' map search as a 'treasure map' and walks in for "
                              'informational interviews, which once got Jason hired twice in 3 hours for '
                              '$450. Business cards go out paired with 3D-printed earrings, and one '
                              'dentist bought 25 sets at $5 each. Free 10-to-15-minute fixes double as '
                              'recon [YXLWY7VHfxM @ 00:26:46]. The back office runs on FreedomVoice for '
                              'the call tree, QuickBooks Online, a separate bank account, ServiceFusion '
                              'work orders, per-tech expense cards, and site photos as timestamps. Owners '
                              'tend to stall near $300k a year. Jason broke through by adding a part-time '
                              'autoclave bench tech and now runs 6 people from a 6,000 sq ft warehouse on '
                              "4x10 shifts. Dave of TKA's blunt counsel on OEM access is to 'just buy a PM "
                              "only contract from every manufacturer' [kmzmXxn2MBE @ 00:54:28].",
                              'Parts are where margins get made or destroyed. Summit Imaging reports '
                              'facilities hearing of 42% to 75% savings from building in-house clinical '
                              'engineering. Those savings come from diagnosing on site, getting parts the '
                              'next morning, keeping downtime inside business hours, and supporting techs '
                              'remotely by phone, text, FaceTime, Skype, and YouTube [7d4lxsuW9Xs @ '
                              '00:10:03]. The catch is part quality. Knockoff IU22/IE33 video cards run at '
                              '60% of OEM performance and lock up with no error code. They also ship with '
                              'the exact same serial number across a couple thousand units [7d4lxsuW9Xs @ '
                              "00:30:14]. Summit's rule is to compare warranty and DOA rates normalized to "
                              'the warranty term, because 2.5% at 90 days is not 2.5% at 2 years. Summit '
                              'also says to watch for failures right after warranty ends and to demand '
                              'complete assemblies. For the quality system, Matrix One quotes published '
                              'QMS software pricing starting at 10,000 euros a year. Teams go live in 2 to '
                              '6 weeks, with migration support off paper, Word, SharePoint, or Google '
                              'Workspace [URXL-ymHf4w @ 00:03:57]. For credentials, Michelle, a BMET '
                              'serving Alaska village clinics, describes the CBET as 165 questions in 3 '
                              'hours, all from memory, with roughly a 60% first-time pass rate. The prep '
                              'stack was the AAMI online course, ChatGPT to explain wrong answers, and '
                              'subject-sorted YouTube playlists [UatkfSp7sHs @ 00:01:19].'],
               'table': {'caption': 'Street-level tools, prices, and unit economics for a third-party '
                                    'biomed shop',
                         'headers': ['Mechanic',
                                     'Exact Numbers or Tool',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Launch capital for core test equipment',
                                   '$8,000 pulled from savings to start under the name JnD Medical '
                                   'Maintenance',
                                   'Fund the core test gear before chasing the first paying contracts',
                                   'Better Biomed Channel ([YXLWY7VHfxM @ 00:05:49])'],
                                  ['Undercutting incumbent supplier service pricing',
                                   '$150 per hour with no travel versus $75 travel plus $150 per half hour',
                                   "Win dentists by quoting directly against their current supplier's "
                                   'rates',
                                   'Better Biomed Channel ([YXLWY7VHfxM @ 00:02:56])'],
                                  ['PM membership as recurring revenue',
                                   '$200 per month buys 2 hours and a 25-point inspection',
                                   'Target 20 offices per tech for $4k in monthly revenue per tech',
                                   'Better Biomed Channel ([YXLWY7VHfxM @ 00:46:29])'],
                                  ['Field service and billing software stack',
                                   'ServiceFusion work orders plus QuickBooks Online for invoicing and tax '
                                   'reports',
                                   'Run dispatch and billing, and use on-site photos as job timestamps',
                                   'Better Biomed Channel ([YXLWY7VHfxM @ 00:47:34])'],
                                  ['Quality management system software',
                                   'Matrix One pricing starts at 10,000 euros yearly, with teams live in 2 '
                                   'to 6 weeks',
                                   'Replace paper, Word, and SharePoint once a team reaches 20 or more '
                                   'people',
                                   'Matrix One ([URXL-ymHf4w @ 00:03:57])'],
                                  ['Device identifier lookup and data pulls',
                                   'AccessGUDID searches by brand, company, DI, or category and shows a '
                                   'maximum of 1000 results',
                                   'Download the full release plus daily or weekly XML updates for a '
                                   'complete dataset',
                                   'National Library of Medicine ([iWPkoBanBfY @ 00:01:12])'],
                                  ['Benchmarking parts warranties',
                                   'Summit gives a standard 6-month warranty and normalizes DOA rates to '
                                   'the warranty term',
                                   'Reject suppliers whose failures cluster right after the warranty ends',
                                   'TechNation TV ([7d4lxsuW9Xs @ 00:14:22])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'How the veterans actually work the angles',
                           'body': 'These moves come straight from operators who have fought OEMs for '
                                   'access, built shops from savings, and torn down knockoff parts on the '
                                   'bench [TechNation TV — lSIrqUmOamc @ 00:28:02].',
                           'items': ['Do not ask OEMs specifically for software keys, because they will '
                                     'circumvent narrow wins. Ask open-endedly for tools, information, '
                                     'support, and training instead [TechNation TV — lSIrqUmOamc @ '
                                     '00:28:02].',
                                     'Build the shop so it can run without the owner, using a part-time '
                                     'autoclave bench tech to break the ceiling near $300k a year [Better '
                                     'Biomed Channel — YXLWY7VHfxM @ 00:16:13].',
                                     'When FDA requests information, answer with detail rather than '
                                     'opinion, and use the confidential-submission path for sensitive data '
                                     '[TechNation TV — C3pxzDnP6HM @ 00:08:20].',
                                     'Vet remanufactured-part suppliers with site visits and references, '
                                     'require IPC soldering certification, and check their certificates on '
                                     'ISO boards [TechNation TV — 7d4lxsuW9Xs @ 00:59:23].']},
               'sop_steps': [{'step': 1,
                              'title': 'Stand up the entity, bank account, and insurance',
                              'action': 'Form the LLC, open a separate business bank account, and secure '
                                        'liability coverage before the first job.',
                              'detail': 'Jason formed a Michigan LLC for about $50 and found coverage hard '
                                        "to get because of water-damage liability. Insurance started at 'a "
                                        "couple grand a year,' and any 1099 contractors need their own "
                                        'insurance [Better Biomed Channel — YXLWY7VHfxM @ 00:12:30].'},
                             {'step': 2,
                              'title': 'Build the service-record spine',
                              'action': 'Template every work order with the required fields and add a '
                                        'complaint-review step that feeds CAPA.',
                              'detail': 'Capture device name, lot number, services done, performer, date, '
                                        'and related test records. Review every report for complaint and '
                                        'reportability status [Quality Systems Explained — ohnyLE9h6ok @ '
                                        '00:01:30].'},
                             {'step': 3,
                              'title': 'Publish the rate card and PM membership',
                              'action': 'Set regular, after-hours, and travel rates, then sell a monthly '
                                        'PM membership.',
                              'detail': 'Charge $175/hr regular, $225 after hours, and $75 travel beyond '
                                        '30 minutes, billed across labor, parts, travel, and shipping. '
                                        'Pair this with a $200/month PM membership that includes 2 hours '
                                        'and a 25-point inspection [Better Biomed Channel — YXLWY7VHfxM @ '
                                        '00:35:36].'},
                             {'step': 4,
                              'title': 'Verify identifiers and vet parts suppliers',
                              'action': 'Look up device records in AccessGUDID, then qualify every parts '
                                        'vendor on quality evidence rather than price.',
                              'detail': 'Search AccessGUDID by brand, company, DI, or category [National '
                                        'Library of Medicine — iWPkoBanBfY @ 00:01:12]. Then demand '
                                        'full-scope ISO certification, retained records, IPC soldering '
                                        'certification, and site visits from suppliers [TechNation TV — '
                                        '7d4lxsuW9Xs @ 00:59:23].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The loudest split in the third-party biomed business is whether non-OEM '
                              'servicing is a real safety problem or a market-share grab dressed up as '
                              'one. Dave Franco of TK/Technology Associates traces OEM pushes from 1996 to '
                              '2006 to 2016, when MITA reframed the fight as safety, and states that '
                              "“there was no evidence to say that there wasn't less quality or less safe "
                              'servicing of medical equipment by non-oem representation” [lSIrqUmOamc @ '
                              '00:22:16]. On the FDA webinar panel, Wang stacked the numbers: roughly 500 '
                              'incidents, 6 tied to maintenance, across about 10 million devices at 6.5 '
                              'Sigma [C3pxzDnP6HM @ 00:42:32]. Tamore argued there is no disparity between '
                              'OEM and third-party work when staff are trained and parts are OEM-spec, '
                              'calling people the common denominator [C3pxzDnP6HM @ 00:50:31]. Summit '
                              'Imaging pushes from a different flank: the risk is less about who turns the '
                              'wrench and more about what goes into the box. Their bench found knockoff '
                              'IU22/IE33 video cards running at 60 percent of OEM performance, locking up '
                              'with no error code, and carrying the exact same serial number across a '
                              'couple thousand units [7d4lxsuW9Xs @ 00:30:14]. The operator read is that '
                              'the independent camp wins the labor argument on the data its members '
                              'present, while the remanufactured-parts supply chain is where the safety '
                              'case can still be lost.',
                              'The second fault line is how much regulation the independent channel should '
                              "invite. Scott Carson, who helped build eBay's healthcare marketplace and "
                              'founded U.S. Medical, calls regulators “flat-footed,” says Alibaba '
                              'counterfeits are almost epidemic, and states flatly, “I think we need more '
                              'regulation and we need it fast” [l108Vrz9wLo @ 00:30:28]. Franco takes the '
                              'opposite posture and agrees that careless regulation would raise service '
                              'costs “dramatically” [lSIrqUmOamc @ 00:16:19]. The cost math behind that '
                              'fear is concrete: Franco puts an ISO 13485 build somewhere between $50,000 '
                              'and $200,000 and 12 to 24 months, a bill that could ruin the “garage” ISOs, '
                              'which is why the QMS workstream moved toward defining tenets instead of '
                              'mandating one platform [kmzmXxn2MBE @ 00:31:12]. Matrix One frames the '
                              'manufacturer-side reality: since 2 February 2026, 21 CFR Part 820 is the '
                              'Quality Management System Regulation, 820.10 requires compliance with ISO '
                              '13485, and their software starts from 10,000 euros a year with teams live '
                              'in 2 to 6 weeks [URXL-ymHf4w @ 00:00:37]. The playbook splits accordingly: '
                              "a lean independent shop rides the KPI-and-tenets track Franco's committee "
                              'is building, while any operation drifting toward remanufacturing or '
                              'labeling budgets for a full quality system and the tooling that produces '
                              'audit evidence.',
                              'Practitioners also split on where an independent should plant its flag. '
                              'Jason of Bright Idea Dental Repair says that if starting over, they would '
                              'go dental-only, because private-sector biomed equipment has “not enough '
                              'pain,” while water-based dental gear such as delivery units, autoclaves, '
                              'suction and compressors constantly needs service [YXLWY7VHfxM @ 00:06:51]. '
                              'Summit Imaging pitches the hospital side instead: build in-house clinical '
                              'engineering, diagnose on site, get next-morning parts, keep downtime inside '
                              'business hours, and capture the 42 to 75 percent savings customers report '
                              'against outsourced service [7d4lxsuW9Xs @ 00:10:03]. Carson bets on neither '
                              'a shop nor a department but a marketplace, stacking eight trust enablers '
                              'including 1,000-plus owned pre-owned devices, 10,000-plus hand pieces and '
                              "parts, and 750 technicians and trainers on an “Uber and Angie's” model "
                              'aimed at growing, cash-based aesthetics [l108Vrz9wLo @ 00:35:09]. Franco '
                              'refuses the purity test on every side: across skill sets, resources, parts, '
                              "tools and location, “it shouldn't matter where your paycheck comes from,” "
                              'and neither a 100 percent OEM nor a 100 percent non-OEM model can work '
                              '[lSIrqUmOamc @ 00:46:29]. The real choice is niche depth in dental and '
                              'autoclaves, hospital-embedded savings on imaging, or platform aggregation '
                              "across pre-owned inventory, and each speaker's numbers hold inside their "
                              'own lane.'],
               'table': {'caption': 'Contested Questions in Third-Party Servicing and the Competing '
                                    'Playbooks',
                         'headers': ['Contested Question',
                                     'Position A (Practitioner View)',
                                     'Position B (Counter-View)',
                                     'Expert Source'],
                         'rows': [['Does non-OEM servicing actually create more safety incidents in the '
                                   'field?',
                                   'Wang cites roughly 500 incidents, only 6 from maintenance, across '
                                   'about 10 million devices at 6.5 Sigma.',
                                   'Summit finds knockoff video cards at 60 percent of OEM performance '
                                   'with identical serial numbers across thousands.',
                                   'TechNation TV ([C3pxzDnP6HM @ 00:42:32]); TechNation TV ([7d4lxsuW9Xs '
                                   '@ 00:30:14])'],
                                  ['How fast should regulators move on the used and resale channel?',
                                   'Carson says regulators are flat-footed and states that more regulation '
                                   'is needed and needed fast.',
                                   'Franco agrees careless regulation would raise service costs '
                                   'dramatically for hospitals and independent service organizations.',
                                   'Greenlight Guru ([l108Vrz9wLo @ 00:30:28]); TechNation TV '
                                   '([lSIrqUmOamc @ 00:16:19])'],
                                  ['Should every independent shop carry a full ISO 13485 quality system?',
                                   'Franco prices ISO 13485 at $50k to $200k over 12 to 24 months, enough '
                                   'to ruin garage ISOs.',
                                   'Matrix One says 820.10 now requires ISO 13485 compliance, with '
                                   'software starting from 10,000 euros yearly.',
                                   'TechNation TV ([kmzmXxn2MBE @ 00:31:12]); Matrix One ([URXL-ymHf4w @ '
                                   '00:00:37])'],
                                  ['Is the CBET certification worth the study time for a working tech?',
                                   'Michelle does not think certification is necessary or that it makes '
                                   'someone a good tech.',
                                   'Michelle still calls it the emerging industry standard and says take '
                                   'it when the employer pays.',
                                   'Traveling Alaskan Biomed Tech ([UatkfSp7sHs @ 00:04:02]); Traveling '
                                   'Alaskan Biomed Tech ([UatkfSp7sHs @ 00:04:40])'],
                                  ['Are OEMs cooperating with third parties on parts, manuals and service '
                                   'information?',
                                   'Crawford of Block Imaging calls OEM cooperation on x-ray equipment '
                                   'relatively high in practice.',
                                   'Doug reports more OEMs refusing to provide parts and manuals to '
                                   'independent servicers over time.',
                                   'TechNation TV ([C3pxzDnP6HM @ 00:21:17]); TechNation TV ([C3pxzDnP6HM '
                                   '@ 01:24:21])'],
                                  ['How many Class I devices escape UDI through the GMP exemption route?',
                                   'Bratz cites 527 GMP-exempt Class I product codes and more than 60 '
                                   'GUDID attributes to report.',
                                   'LexisNexis says only about 15 to 20 Class I products are GMP-exempt, '
                                   'with 57 attributes reported.',
                                   'Medical Device Academy ([fB0ZiAL0q20 @ 00:08:50]); LexisNexis Life '
                                   'Sciences Solutions ([nxzxvwNJELg @ 00:04:52])'],
                                  ['How many quantitative markers should a cleaning validation study '
                                   'actually use?',
                                   'FDA reviewers state that a total of two quantitative methods such as '
                                   'protein, TOC or hemoglobin suffices.',
                                   'Pentax questioned dropping from three markers to two and the 6 to 10 '
                                   'cycle norm; FDA deferred.',
                                   'Medical and Health Tips (MHT) ([8VMkq0EoUD4 @ 01:12:01]); Medical and '
                                   'Health Tips (MHT) ([8VMkq0EoUD4 @ 01:13:08])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failures in the independent channel show up inside the '
                              "parts bin. Summit Imaging's Larry Nolen and Carl Ravel tell operators to "
                              'normalize warranty and DOA rates to term, because 2.5 percent at 90 days is '
                              'not 2.5 percent at two years, to watch for failures landing right after '
                              'warranty ends, and to reject computers that ship without video cards or '
                              'with reused hard drives [7d4lxsuW9Xs @ 00:14:22]. Their teardown of '
                              'remanufactured cable lines found about 30 frayed lines, and because OEMs do '
                              'not release specs, any “OEM spec” claim on those assemblies is a guess '
                              '[7d4lxsuW9Xs @ 00:36:57]. The deepest trap is the whole-probe swap, where '
                              'an OEM body, can and serial number are refitted around remanufactured '
                              "crystal and lines; Summit's verdict is blunt: “I've never seen a 510 K for "
                              'a whole probe swap” [7d4lxsuW9Xs @ 00:55:33]. Information gaps compound the '
                              'parts risk: on the FDA webinar, panelists reported that Olympus did not '
                              'notify IMS of the TJF-Q180 recall, and that more OEMs are refusing to '
                              'provide parts and manuals [C3pxzDnP6HM @ 01:14:29]. An independent running '
                              'on untested parts and missing recall notices pays twice, first in an extra '
                              'day of downtime chasing diagnostic doubt, then in the misdiagnosis and '
                              'seal-failure liability Summit flags for drop-out sectors and TEE probes.',
                              'On the business side, the traps are pricing and ownership structure. Better '
                              'Biomed Channel relays hearsay, openly hedged with “from what I heard,” that '
                              'a large third-party repair company won a multi-million-dollar hospital '
                              "contract by bidding about half the prior vendor's price, when that prior "
                              'vendor was already barely in the black or in the red [UQh0OoupetI @ '
                              '00:00:25]. The theory: the underbid is a loss leader that pads the books '
                              'and inflates valuation ahead of a reported $660 million sale to a North '
                              'Carolina buyer, so the sellers exit before contractually obligated losses '
                              'arrive, leaving the investment firm and the working techs to absorb the '
                              'damage [UQh0OoupetI @ 00:01:43]. Jason of Bright Idea Dental Repair names '
                              'the solo-owner trap: owners hit a ceiling around $300,000 a year, and “the '
                              'business needs to be able to run without you,” which they broke by adding a '
                              'part-time autoclave bench tech [YXLWY7VHfxM @ 00:16:58]. Insurance is the '
                              'other silent killer: water-damage liability made carriers hard to find, '
                              'premiums started at “a couple grand a year,” and 1099 contractors must '
                              'carry their own coverage [YXLWY7VHfxM @ 00:12:30]. Jason also notes that '
                              'big suppliers treat service as a loss leader and flex rates to each '
                              "customer's supply spend, which is exactly the gap their $150-an-hour, "
                              'no-travel opening offer exploited.',
                              'The paperwork failures are quieter, but they surface the moment a complaint '
                              'or audit lands. Aaron Snider of Quality Systems Explained lists what broken '
                              'servicing looks like: no procedures or no link to the device master record, '
                              'untrained personnel, and records that are lost, destroyed, or unavailable '
                              '[ohnyLE9h6ok @ 00:02:22]. The fix runs through every service report, each '
                              'one reviewed to decide whether it is a complaint and whether that complaint '
                              'is reportable, with device name, lot number, services done, performer, date '
                              'and related test records captured and fed into CAPA for tracking and '
                              'trending [ohnyLE9h6ok @ 00:01:30]. For any shop that relabels or acts as '
                              'the labeler, Jonathan Bratz of Medical Device Academy found the business '
                              'software changes “the most time-consuming and costly aspect” of rolling out '
                              'UDI, and warns that customers now demand UDI on a publish-or-perish basis '
                              '[fB0ZiAL0q20 @ 00:26:31]. LexisNexis Life Sciences Solutions adds the '
                              'maintenance trap: a new version, a new model, or a changed label value '
                              'needs a GUDID update before distribution, with only a 10-day grace period '
                              'for attributes that do not appear on the label [nxzxvwNJELg @ 00:06:17]. '
                              "Snider's bonus audit questions close the loop: is servicing required, is it "
                              'done in-house or at the customer site, and where are the records kept, '
                              'pointing back to the device history record.'],
               'table': {'caption': 'Firsthand Failure Modes and Their Economic Hit on Independent '
                                    'Servicers',
                         'headers': ['Failure Mode',
                                     'What Went Wrong in the Field',
                                     'Economic or Operational Hit',
                                     'Expert Source'],
                         'rows': [['Knockoff remanufactured video cards installed in IU22 and IE33 '
                                   'ultrasound systems.',
                                   'Cards ran at 60 percent of OEM performance, locked up with no error '
                                   'code, shared one serial.',
                                   'Untraceable faults drive geometric user anger and push facilities '
                                   'toward unnecessary capital replacement purchases.',
                                   'TechNation TV ([7d4lxsuW9Xs @ 00:30:14])'],
                                  ['Untested or incomplete replacement parts shipped from low-quality '
                                   'remanufacturing suppliers.',
                                   'Computers arrived without video cards or with reused hard drives; '
                                   'compatibility assumed rather than guaranteed.',
                                   'Diagnostic doubt adds an extra day of downtime, cancelling patients '
                                   'and losing scan revenue.',
                                   'TechNation TV ([7d4lxsuW9Xs @ 00:22:53])'],
                                  ['Underbidding a multi-million-dollar hospital contract at roughly half '
                                   "the incumbent's price.",
                                   'Reportedly used as a loss leader to inflate valuation before a $660 '
                                   'million sale.',
                                   'Investment firm absorbs contract losses, and quality and biomed life '
                                   'are likely to worsen.',
                                   'Better Biomed Channel ([UQh0OoupetI @ 00:02:29])'],
                                  ['Solo owner doing every service call personally with no bench support '
                                   'behind them.',
                                   'Owners stall around $300,000 a year because the business cannot run '
                                   'without them.',
                                   'Jason broke the ceiling with a part-time autoclave bench tech, growing '
                                   'to six people.',
                                   'Better Biomed Channel ([YXLWY7VHfxM @ 00:16:58])'],
                                  ['Sending 1099 contractors into dental offices with water-based '
                                   'equipment and no own coverage.',
                                   'Water-damage liability made insurers hard to find for dental equipment '
                                   'service work.',
                                   'Premiums start at a couple grand yearly, and contractors must carry '
                                   'their own insurance.',
                                   'Better Biomed Channel ([YXLWY7VHfxM @ 00:18:38])'],
                                  ['Servicing without procedures, device master record links, or retained '
                                   'service records.',
                                   'Untrained personnel and records lost, destroyed, or unavailable when '
                                   'auditors or customers ask.',
                                   'No traceable path back to the device history record when a complaint '
                                   'becomes reportable.',
                                   'Quality Systems Explained ([ohnyLE9h6ok @ 00:02:22])'],
                                  ['Relying on OEMs to share recalls, parts and manuals with independent '
                                   'servicers.',
                                   'Olympus did not notify IMS of the TJF-Q180 recall, and more OEMs '
                                   'refuse manuals.',
                                   'Independents work blind on recalled devices and lose access to parts '
                                   'needed for repairs.',
                                   'TechNation TV ([C3pxzDnP6HM @ 01:14:29])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Checks Before Taking the Job, the Part, or the Contract',
                           'body': 'Each check below comes straight from a loss, reversal, or audit '
                                   'failure practitioners reported firsthand; clear all four before '
                                   'committing labor, parts, or a signature.',
                           'items': ['Before installing any remanufactured board, cable or probe, vet the '
                                     'supplier for full-scope ISO 13485 (not just brokering), retained '
                                     'records, IPC soldering certification and risk management, then '
                                     'verify certificates on ISO boards and make a site visit [TechNation '
                                     'TV — 7d4lxsuW9Xs @ 00:59:23].',
                                     'Before bidding against an incumbent, check whether a rival quoting '
                                     'about half the prior price is padding the books for a sale; '
                                     'contracts priced below cost leave the eventual owner and the techs '
                                     'absorbing the losses [Better Biomed Channel — UQh0OoupetI @ '
                                     '00:01:21].',
                                     'Before sending any 1099 contractor on site, confirm they carry their '
                                     'own insurance, because water-damage liability already makes '
                                     'dental-service coverage hard to place [Better Biomed Channel — '
                                     'YXLWY7VHfxM @ 00:18:38].',
                                     'Before closing any work order, review the service report for '
                                     'complaint status and reportability, and capture device name, lot '
                                     'number, services done, performer, date and related test records '
                                     '[Quality Systems Explained — ohnyLE9h6ok @ 00:01:30].']}}],
 'pull_quote': "“I've never seen a 510 K for a whole probe swap.” — TechNation TV (7d4lxsuW9Xs @ 00:55:33)",
 'diagram_id': 'diag-03',
 'action_checklist': ["Normalize every parts supplier's warranty and DOA rate to the warranty term, demand "
                      'complete assemblies, and track failures that land right after warranty expires '
                      '[TechNation TV — 7d4lxsuW9Xs @ 00:14:22].',
                      'Run a Yelp “dentist” map search as a treasure map, then walk in for informational '
                      'interviews and offer free 10 to 15 minute fixes as recon [Better Biomed Channel — '
                      'YXLWY7VHfxM @ 00:26:46].',
                      'Set rates at $175 an hour regular, $225 after hours, and $75 travel for customers '
                      'beyond 30 minutes, billing labor, parts, travel and shipping as separate lines '
                      '[Better Biomed Channel — YXLWY7VHfxM @ 00:35:36].',
                      'Sell a $200-a-month PM membership covering 2 hours plus a 25-point inspection, '
                      'targeting 20 offices per tech, or $4k a month per tech [Better Biomed Channel — '
                      'YXLWY7VHfxM @ 00:46:29].',
                      'Pull device identifiers from AccessGUDID by brand, company, DI or category, filter '
                      'by GMDN term or product code name, and download the full XML release plus daily or '
                      'weekly updates when the 1,000-result display cap is too small [National Library of '
                      'Medicine — iWPkoBanBfY @ 00:01:12].',
                      'When pressing OEMs for access, ask open-endedly for tools, information, support and '
                      'training instead of narrowly for software keys that OEMs will circumvent '
                      '[TechNation TV — lSIrqUmOamc @ 00:28:02].'],
 'statutory_citations': [{'title': 'TechNation TV — How Low Quality Remanufactured Parts Inside Medical '
                                   'Devices Increase Total Cost Of Ownership [00:55:33]',
                          'url': 'https://www.youtube.com/watch?v=7d4lxsuW9Xs&t=3333s',
                          'relevance': 'Primary practitioner testimony on whole-probe swaps, knockoff '
                                       'video cards, and supplier vetting for remanufactured parts.'},
                         {'title': 'TechNation TV — Special FDA Webinar for Medical Equipment Sales and '
                                   'Service Industry [00:42:32]',
                          'url': 'https://www.youtube.com/watch?v=C3pxzDnP6HM&t=2552s',
                          'relevance': 'Primary practitioner testimony on incident data, OEM cooperation, '
                                       'and parts and manual refusals in third-party servicing.'},
                         {'title': 'Better Biomed Channel — Starting Your Own Biomed Business! [00:16:58]',
                          'url': 'https://www.youtube.com/watch?v=YXLWY7VHfxM&t=1018s',
                          'relevance': 'Primary practitioner testimony on launching, pricing, insuring, '
                                       'and scaling an independent dental biomed repair business.'},
                         {'title': 'Quality Systems Explained — Servicing 820.200 & ISO 13485 § 7.5.4, 8.4 '
                                   '(Executive Series #52) [00:02:22]',
                          'url': 'https://www.youtube.com/watch?v=ohnyLE9h6ok&t=142s',
                          'relevance': 'Primary practitioner testimony on servicing records, complaint '
                                       'review, and what failing servicing programs look like.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'ohnyLE9h6ok',
                       'title': 'Servicing 820.200 & ISO 13485 § 7.5.4, 8.4 (Executive Series #52)',
                       'channel': 'Quality Systems Explained',
                       'author': 'Quality Systems Explained',
                       'text': 'servicing Personnel have to be trained to the servicing procedures and '
                               "they also have to understand the customer's requirements.",
                       'tip': 'servicing Personnel have to be trained to the servicing procedures and they '
                              "also have to understand the customer's requirements.",
                       'timestamp': 70,
                       'timestamp_seconds': 70,
                       'timestamp_label': '[00:01:10]',
                       'url': 'https://www.youtube.com/watch?v=ohnyLE9h6ok&t=70s',
                       'markdown': '[00:01:10](https://www.youtube.com/watch?v=ohnyLE9h6ok&t=70s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lSIrqUmOamc',
                       'title': 'Updates to Servicing & Remanufacturing Through the Medical Device '
                                'Servicing Collaborative Community',
                       'channel': 'TechNation TV',
                       'author': 'TechNation TV',
                       'text': "i've worked with about six different states around the country successful "
                               'in each of those so far in terms of making sure that we would still have '
                               'access and the ability to work on a medical equipment.',
                       'tip': "i've worked with about six different states around the country successful "
                              'in each of those so far in terms of making sure that we would still have '
                              'access and the ability to work on a medical equipment.',
                       'timestamp': 3422,
                       'timestamp_seconds': 3422,
                       'timestamp_label': '[00:57:02]',
                       'url': 'https://www.youtube.com/watch?v=lSIrqUmOamc&t=3422s',
                       'markdown': '[00:57:02](https://www.youtube.com/watch?v=lSIrqUmOamc&t=3422s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'W-lVX6x4V2U',
                       'title': 'Biomedical Science vs. Medicine | 6 Key Differences | Atousa',
                       'channel': 'Doctor Atousa',
                       'author': 'Doctor Atousa',
                       'text': 'so in biomedical science typically you will finish in three years whereas '
                               'in medicine you will finish in five.',
                       'tip': 'so in biomedical science typically you will finish in three years whereas '
                              'in medicine you will finish in five.',
                       'timestamp': 431,
                       'timestamp_seconds': 431,
                       'timestamp_label': '[00:07:11]',
                       'url': 'https://www.youtube.com/watch?v=W-lVX6x4V2U&t=431s',
                       'markdown': '[00:07:11](https://www.youtube.com/watch?v=W-lVX6x4V2U&t=431s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'l108Vrz9wLo',
                       'title': 'The Future of Reprocessed Used Medical Equipment',
                       'channel': 'Greenlight Guru',
                       'author': 'Greenlight Guru',
                       'text': 'any manufacturer will tell you that sales and marketing roughly is 40 to '
                               '50 percent of the sales cost of a product.',
                       'tip': 'any manufacturer will tell you that sales and marketing roughly is 40 to 50 '
                              'percent of the sales cost of a product.',
                       'timestamp': 516,
                       'timestamp_seconds': 516,
                       'timestamp_label': '[00:08:36]',
                       'url': 'https://www.youtube.com/watch?v=l108Vrz9wLo&t=516s',
                       'markdown': '[00:08:36](https://www.youtube.com/watch?v=l108Vrz9wLo&t=516s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8VMkq0EoUD4',
                       'title': 'FDA Reprocessing Medical Devices: Validation Methods and '
                                'Labeling.#MedicalDeviceReprocessing',
                       'channel': 'Medical and Health Tips (MHT)',
                       'author': 'Medical and Health Tips (MHT)',
                       'text': 'if it cannot be cleaned it cannot be disinfected or sterilized.',
                       'tip': 'if it cannot be cleaned it cannot be disinfected or sterilized.',
                       'timestamp': 918,
                       'timestamp_seconds': 918,
                       'timestamp_label': '[00:15:18]',
                       'url': 'https://www.youtube.com/watch?v=8VMkq0EoUD4&t=918s',
                       'markdown': '[00:15:18](https://www.youtube.com/watch?v=8VMkq0EoUD4&t=918s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UatkfSp7sHs',
                       'title': 'CBET Exam: What to Study, Tips, and My Results',
                       'channel': 'Traveling Alaskan Biomed Tech',
                       'author': 'Traveling Alaskan Biomed Tech',
                       'text': 'So, if your company is willing to pay for it like mine was, take advantage '
                               'of it and get it done.',
                       'tip': 'So, if your company is willing to pay for it like mine was, take advantage '
                              'of it and get it done.',
                       'timestamp': 280,
                       'timestamp_seconds': 280,
                       'timestamp_label': '[00:04:40]',
                       'url': 'https://www.youtube.com/watch?v=UatkfSp7sHs&t=280s',
                       'markdown': '[00:04:40](https://www.youtube.com/watch?v=UatkfSp7sHs&t=280s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UQh0OoupetI',
                       'title': 'Another Biomedical Repair company sold to private equity?',
                       'channel': 'Better Biomed Channel',
                       'author': 'Better Biomed Channel',
                       'text': 'So what they do is they underbid a contract to secure the contract, which '
                               'increases the valuation of their own company.',
                       'tip': 'So what they do is they underbid a contract to secure the contract, which '
                              'increases the valuation of their own company.',
                       'timestamp': 103,
                       'timestamp_seconds': 103,
                       'timestamp_label': '[00:01:43]',
                       'url': 'https://www.youtube.com/watch?v=UQh0OoupetI&t=103s',
                       'markdown': '[00:01:43](https://www.youtube.com/watch?v=UQh0OoupetI&t=103s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'D3YTNIGYcxQ',
                       'title': 'Apprenticeships Case Study 5- Pathology',
                       'channel': 'norfolknhs',
                       'author': 'norfolknhs',
                       'text': 'certain ones require to be Frozen and some need to be spun down straight '
                               'away.',
                       'tip': 'certain ones require to be Frozen and some need to be spun down straight '
                              'away.',
                       'timestamp': 109,
                       'timestamp_seconds': 109,
                       'timestamp_label': '[00:01:49]',
                       'url': 'https://www.youtube.com/watch?v=D3YTNIGYcxQ&t=109s',
                       'markdown': '[00:01:49](https://www.youtube.com/watch?v=D3YTNIGYcxQ&t=109s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'C3pxzDnP6HM',
                       'title': 'Special FDA Webinar for Medical Equipment Sales and Service Industry',
                       'channel': 'TechNation TV',
                       'author': 'TechNation TV',
                       'text': 'the majority of medical devices today uh in this Marketplace are being '
                               'serviced by someone other than the original manufacturer.',
                       'tip': 'the majority of medical devices today uh in this Marketplace are being '
                              'serviced by someone other than the original manufacturer.',
                       'timestamp': 1293,
                       'timestamp_seconds': 1293,
                       'timestamp_label': '[00:21:33]',
                       'url': 'https://www.youtube.com/watch?v=C3pxzDnP6HM&t=1293s',
                       'markdown': '[00:21:33](https://www.youtube.com/watch?v=C3pxzDnP6HM&t=1293s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'URXL-ymHf4w',
                       'title': 'QMS Software for Medical Electrical Equipment Companies | Matrix Quality',
                       'channel': 'Matrix One',
                       'author': 'Matrix One',
                       'text': 'Servicing records must include the device, the date, who serviced it, the '
                               'service performed and any test and inspection data.',
                       'tip': 'Servicing records must include the device, the date, who serviced it, the '
                              'service performed and any test and inspection data.',
                       'timestamp': 78,
                       'timestamp_seconds': 78,
                       'timestamp_label': '[00:01:18]',
                       'url': 'https://www.youtube.com/watch?v=URXL-ymHf4w&t=78s',
                       'markdown': '[00:01:18](https://www.youtube.com/watch?v=URXL-ymHf4w&t=78s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iWPkoBanBfY',
                       'title': 'AccessGUDID: Search and Download',
                       'channel': 'National Library of Medicine',
                       'author': 'National Library of Medicine',
                       'text': 'The site displays a maximum of 1000 results.',
                       'tip': 'The site displays a maximum of 1000 results.',
                       'timestamp': 72,
                       'timestamp_seconds': 72,
                       'timestamp_label': '[00:01:12]',
                       'url': 'https://www.youtube.com/watch?v=iWPkoBanBfY&t=72s',
                       'markdown': '[00:01:12](https://www.youtube.com/watch?v=iWPkoBanBfY&t=72s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YXLWY7VHfxM',
                       'title': 'Starting Your Own Biomed Business!',
                       'channel': 'Better Biomed Channel',
                       'author': 'Better Biomed Channel',
                       'text': 'the business needs to be able to run without you.',
                       'tip': 'the business needs to be able to run without you.',
                       'timestamp': 973,
                       'timestamp_seconds': 973,
                       'timestamp_label': '[00:16:13]',
                       'url': 'https://www.youtube.com/watch?v=YXLWY7VHfxM&t=973s',
                       'markdown': '[00:16:13](https://www.youtube.com/watch?v=YXLWY7VHfxM&t=973s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kmzmXxn2MBE',
                       'title': 'Medical Device Servicing Community FDA Industry Updates',
                       'channel': 'TechNation TV',
                       'author': 'TechNation TV',
                       'text': "depending on who you are and what you have for resources it's going to be "
                               'somewhere between $50 and $200,000.',
                       'tip': "depending on who you are and what you have for resources it's going to be "
                              'somewhere between $50 and $200,000.',
                       'timestamp': 1872,
                       'timestamp_seconds': 1872,
                       'timestamp_label': '[00:31:12]',
                       'url': 'https://www.youtube.com/watch?v=kmzmXxn2MBE&t=1872s',
                       'markdown': '[00:31:12](https://www.youtube.com/watch?v=kmzmXxn2MBE&t=1872s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7d4lxsuW9Xs',
                       'title': 'How Low Quality Remanufactured Parts Inside Medical Devices Increase '
                                'Total Cost Of Ownership',
                       'channel': 'TechNation TV',
                       'author': 'TechNation TV',
                       'text': "I've never seen a 510 K for a whole probe swap.",
                       'tip': "I've never seen a 510 K for a whole probe swap.",
                       'timestamp': 3333,
                       'timestamp_seconds': 3333,
                       'timestamp_label': '[00:55:33]',
                       'url': 'https://www.youtube.com/watch?v=7d4lxsuW9Xs&t=3333s',
                       'markdown': '[00:55:33](https://www.youtube.com/watch?v=7d4lxsuW9Xs&t=3333s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fB0ZiAL0q20',
                       'title': 'FDA UDI Regulation’s Impact on Medical Device Labelers Webinar',
                       'channel': 'Medical Device Academy',
                       'author': 'Medical Device Academy',
                       'text': 'I found the change is needed in our business software to be the most '
                               'time-consuming and costly aspect of implementing G tins.',
                       'tip': 'I found the change is needed in our business software to be the most '
                              'time-consuming and costly aspect of implementing G tins.',
                       'timestamp': 1591,
                       'timestamp_seconds': 1591,
                       'timestamp_label': '[00:26:31]',
                       'url': 'https://www.youtube.com/watch?v=fB0ZiAL0q20&t=1591s',
                       'markdown': '[00:26:31](https://www.youtube.com/watch?v=fB0ZiAL0q20&t=1591s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nxzxvwNJELg',
                       'title': 'US FDA Class I UDI Requirements and Exceptions',
                       'channel': 'LexisNexis Life Sciences Solutions',
                       'author': 'LexisNexis Life Sciences Solutions',
                       'text': "if there's an attribute that is not on the label then you have a grace "
                               'period of 10 days after your distribution to make sure that the good id '
                               'database is updated.',
                       'tip': "if there's an attribute that is not on the label then you have a grace "
                              'period of 10 days after your distribution to make sure that the good id '
                              'database is updated.',
                       'timestamp': 377,
                       'timestamp_seconds': 377,
                       'timestamp_label': '[00:06:17]',
                       'url': 'https://www.youtube.com/watch?v=nxzxvwNJELg&t=377s',
                       'markdown': '[00:06:17](https://www.youtube.com/watch?v=nxzxvwNJELg&t=377s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7d4lxsuW9Xs',
                       'title': 'How Low Quality Remanufactured Parts Inside Medical Devices Increase '
                                'Total Cost Of Ownership',
                       'channel': 'TechNation TV',
                       'author': 'TechNation TV',
                       'text': 'this remanufactured card only performs to 60 percent of the performance of '
                               'the OEM card a significant difference.',
                       'tip': 'this remanufactured card only performs to 60 percent of the performance of '
                              'the OEM card a significant difference.',
                       'timestamp': 1814,
                       'timestamp_seconds': 1814,
                       'timestamp_label': '[00:30:14]',
                       'url': 'https://www.youtube.com/watch?v=7d4lxsuW9Xs&t=1814s',
                       'markdown': '[00:30:14](https://www.youtube.com/watch?v=7d4lxsuW9Xs&t=1814s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YXLWY7VHfxM',
                       'title': 'Starting Your Own Biomed Business!',
                       'channel': 'Better Biomed Channel',
                       'author': 'Better Biomed Channel',
                       'text': "got an after hours rate of 225 and then i've got a travel rate of 75 "
                               'dollars for any customer outside of 30 minutes.',
                       'tip': "got an after hours rate of 225 and then i've got a travel rate of 75 "
                              'dollars for any customer outside of 30 minutes.',
                       'timestamp': 2136,
                       'timestamp_seconds': 2136,
                       'timestamp_label': '[00:35:36]',
                       'url': 'https://www.youtube.com/watch?v=YXLWY7VHfxM&t=2136s',
                       'markdown': '[00:35:36](https://www.youtube.com/watch?v=YXLWY7VHfxM&t=2136s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'}]}
