from __future__ import annotations

CHAPTER_9 = {'id': 'Q9',
 'chapter_id': 'Q9',
 'chapter_number': 9,
 'question_number': 9,
 'slug': 'clear-permissions-and-address-infringement',
 'question_prompt': 'How do I distinguish permitted use from infringement, obtain image permissions and '
                    'understand the options for enforcing IP rights?',
 'kicker': 'Q9 / THE BIG MONEY PLAYBOOKS',
 'title': 'Clear Permissions and Address Infringement',
 'subtitle': 'Patent infringement, defenses and design-arounds; unauthorized sellers, compulsory '
             'licensing, photography ownership, image licenses, registration and fair use',
 'layout_template': 'tool_resource_directory',
 'reading_time_minutes': 15,
 'executive_summary': 'Photographers, IP litigators and patent analysts converge on one rule: without '
                      'written permission or a license there is no right to use, and only the claims '
                      "define a patent. Matthew Anderson says photographers keep copyright in '90 some "
                      "percent' of client jobs. freeCodeCamp and DesignLab route users to CC0, Pixabay, "
                      "Unsplash and CCSearch. Barbara Aboagye's ScienceDirect 'get rights and content' "
                      'flow cleared a journal figure at a zero-fee quote. The ASMP speaker at B&H '
                      'registers about 1,500 images for $35 with roughly six-week turnaround, because '
                      'registering before infringement unlocks statutory damages of $750 to $150,000 per '
                      'work, a range Visme repeats. Torys LLP warns that platforms remove listings but '
                      'rarely do more, which turns cross-border enforcement into whack-a-mole. LawShelf '
                      'puts willful patent infringement at up to 3x damages. Speakers split on how far '
                      'fair use can be trusted versus simply creating original content.',
 'key_metrics': [{'label': 'Statutory damages per registered work',
                  'metric': 'Statutory damages per registered work',
                  'value': '$750 minimum, up to $150,000 per work',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Penalty range Visme cites for infringing a work registered with the US '
                             'Copyright Office; the B&H ASMP speaker gives the same $750 to $150,000 '
                             'per-infringement range.',
                  'source': 'Visme ([ShCyD9TYhLY @ 00:00:18])'},
                 {'label': 'Batch copyright registration cost and turnaround',
                  'metric': 'Batch copyright registration cost and turnaround',
                  'value': 'About 1,500 images for $35; about 6 weeks, or about $700 to expedite',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Registration economics from the ASMP speaker: fill out the form, pay, and '
                             'send a deposit, which can be 600-pixel JPEGs.',
                  'source': 'B&H Photo Video Pro Audio ([74bQUodJbWY @ 01:16:43])'},
                 {'label': 'Share of client jobs where photographer keeps copyright',
                  'metric': 'Share of client jobs where photographer keeps copyright',
                  'value': "'90 some percent' of cases",
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Anderson's estimate of how often the photographer, not the paying client, "
                             'retains copyright; clients cannot pass images to third parties, contests or '
                             'editorials.',
                  'source': 'Matthew Anderson ([manKMR61ho0 @ 00:02:57])'},
                 {'label': 'Willful patent infringement multiplier',
                  'metric': 'Willful patent infringement multiplier',
                  'value': 'Up to 3x damages',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "LawShelf's remedies breakdown: at least a reasonable royalty "
                             '(Georgia-Pacific factors) or lost profits, enhanced up to 3x for '
                             "willfulness, with attorney's fees in exceptional cases.",
                  'source': 'LawShelf ([WtxlYb996kI @ 00:14:33])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Across the photo-licensing and image-reuse camp, the baseline is identical: '
                              'nothing found online is free by default. freeCodeCamp Concepts states every '
                              "image starts at 'all rights reserved' and lists only three lawful ways in: "
                              'written permission, a purchased license, or narrow, transformative fair use '
                              'such as commentary, review or parody [grui-CD6Uck @ 00:00:18]. Visme '
                              'hammers the same point, telling creators to stop copy-pasting from Google '
                              "Images into projects because 'permission is the key word here' [ShCyD9TYhLY "
                              '@ 00:01:33]. Matthew Anderson frames his master test as a single question, '
                              'whether there is clear written permission from the original photographer. '
                              "He calls the belief that anything on social media is usable '100 wrong' and "
                              'adds that a missing watermark does not mean free [manKMR61ho0 @ 00:06:31]. '
                              'On the commissioning side, Anderson says that unless a contract explicitly '
                              'transfers copyright, the paying client does not own the images. The client '
                              'holds a license for social, website, blog and promotional use and cannot '
                              'hand the files to other companies, even companies willing to pay '
                              '[-267ABEXf8o @ 00:00:41]. The same logic covers subjects inside a frame: '
                              'owning the product in a photo confers no rights in the photo itself. '
                              'Coca-Cola cannot use a kitchen shot that shows its can, and Delta needs '
                              'permission for an image featuring its faucet.',
                              'On the patent side, every speaker who walks through an infringement '
                              'analysis lands on the same rule: only the claims matter. Dylan Adams of '
                              'Patents Demystified says protection is defined by the claims, not the '
                              'drawings or description. The comparison runs element by element against an '
                              'actual product, and the plaintiff must prove every element of at least one '
                              'claim [9hTMXJtONtM @ 00:07:59]. CIONCA IP demonstrates this with building '
                              'blocks. A claim where two of three elements match and one part is swapped '
                              '(a bearing in place of a gear) is not infringed. A claim missing one of '
                              'four elements is not infringed. A claim with every element present is '
                              'infringed, and one infringed claim means the patent is infringed '
                              '[kRlS4inO95k @ 00:05:25]. Patent Insanity builds its whole design-around '
                              'method on the same foundation, telling engineering teams to analyse the '
                              'claims only and map every limitation of each claim onto their own product '
                              '[Jwz-iMwUtCU @ 00:01:17]. Patent Attorney Worldwide reduces it to a thesis '
                              "that claim quality decides everything: 'A badly written claim can make an "
                              "amazing invention totally worthless' [D-Am1gpuzaw @ 00:04:56]. The "
                              'prohibited acts are consistent across these speakers: making, using, '
                              "selling and importing, with encouraging someone else's infringement "
                              'creating liability too.',
                              'The third point of agreement is that rights only pay off when they are set '
                              'up for enforcement before trouble starts. Torys LLP opens its '
                              'unauthorized-seller playbook by mapping where you hold rights, where the '
                              'infringing activity happens and who the infringer is, because IP rights are '
                              'jurisdictional. A Canadian patent can still be asserted against a foreign '
                              'vendor that is selling into Canada [ijF0IyvjXXg @ 00:00:36]. Adams agrees '
                              'that protection is territorial and expressly reaches importing [9hTMXJtONtM '
                              "@ 00:06:55]. In copyright, the ASMP speaker at B&H is blunt: 'you must "
                              "register before an infringement to have the full protection of copyright.' "
                              'Registration is required before suing in federal court, and it unlocks '
                              'statutory damages, attorney fees and real payment leverage when chasing an '
                              'infringer [74bQUodJbWY @ 01:19:44]. Derek Fahey makes the same case. '
                              'Copyright exists the moment a work is fixed, but registration is what opens '
                              'access to statutory, enhanced damages. He also warns that a design patent '
                              'must be filed within one year of first U.S. disclosure, or the rights are '
                              'lost [nLSthuXQCL4 @ 00:01:10]. The shared message for operators is that '
                              'unregistered, unmapped or late-filed rights leave an owner chasing '
                              'infringers with almost no leverage, however strong the underlying work or '
                              'invention is.'],
               'table': {'caption': 'Consensus rules every operator should lock in before using or '
                                    'enforcing IP',
                         'headers': ['Consensus Principle',
                                     'What Practitioners Say',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Default image status is all rights reserved',
                                   'Every image starts locked; lawful use needs written permission, a '
                                   'purchased license, or fair use',
                                   'Treat every unlabeled online image as unusable until a license route '
                                   'is documented',
                                   'freeCodeCamp Concepts ([grui-CD6Uck @ 00:00:18])'],
                                  ['Paying client does not own commissioned photos',
                                   'Without an explicit written transfer, the client only licenses social, '
                                   'website, blog and promotional use',
                                   'Write the copyright transfer or exact usage scope into the contract '
                                   'before the shoot',
                                   'Matthew Anderson ([-267ABEXf8o @ 00:00:41])'],
                                  ['Social media posts and unwatermarked images are not free',
                                   "Anderson calls 'anything on social media is usable' 100 wrong; no "
                                   'watermark changes nothing',
                                   'Get clear written permission from the original photographer for every '
                                   'reposted image',
                                   'Matthew Anderson ([manKMR61ho0 @ 00:06:31])'],
                                  ['Permission is the key word for copyrighted photos',
                                   'Copy-pasting from Google Images risks a hefty fine or, even worse, a '
                                   'lawsuit',
                                   'Replace ad-hoc image grabs with licensed, Creative Commons, public '
                                   'domain or self-made assets',
                                   'Visme ([ShCyD9TYhLY @ 00:01:33])'],
                                  ['Only patent claims define the protected territory',
                                   'Drawings and description do not count; compare the actual product '
                                   'element by element',
                                   'Run every infringement or clearance check against the issued claims, '
                                   'never the specification',
                                   'Patents Demystified ([9hTMXJtONtM @ 00:07:59])'],
                                  ['All elements of one claim must be present',
                                   'A claim missing one element is not infringed; one fully matched claim '
                                   'infringes the patent',
                                   'Find a single claim where every element maps before sending any demand '
                                   'letter',
                                   'CIONCA IP ([kRlS4inO95k @ 00:06:11])'],
                                  ['IP rights are jurisdictional and must be mapped',
                                   'First map where rights exist, where the infringement happens and who '
                                   'the infringer is',
                                   'Build a rights-versus-activity map for each country before targeting '
                                   'any foreign seller',
                                   'Torys LLP ([ijF0IyvjXXg @ 00:00:36])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['To clear a figure from a research paper, Barbara Aboagye walks through a '
                              'concrete workflow. Grab the DOI or title and Google it, then on '
                              "ScienceDirect click 'get rights and content' [SK5CqQ61CYI @ 00:00:41]. From "
                              'there she selects the reuse type (journal, magazine or thesis), selects '
                              'academic and confirms the publisher. In her example, Cement and Concrete '
                              'Research routes to Elsevier. She specifies a figure, the number of figures, '
                              'electronic format, not author and not translating. She then picks a '
                              'currency to reveal the fee, which shows as free, paid or special case. Her '
                              'quote came back at zero, though it is flagged as an estimate that may '
                              'change [SK5CqQ61CYI @ 00:03:00]. She finishes by entering a reference '
                              'number, identifying the figure, entering her name and accepting the terms, '
                              'then printing the license and submitting it to the journal. For zero-fee '
                              'sourcing, freeCodeCamp Concepts points to search-engine license filters, '
                              'Pixabay and Unsplash, and notes that public domain and CC0 works carry no '
                              "restrictions [grui-CD6Uck @ 00:01:30]. DesignLab UW-Madison calls CC0 'our "
                              "best friend' because commercial use is allowed without permission, and "
                              'sends users to CCSearch filters. DesignLab also warns that Creative Commons '
                              'licenses combine Attribution, Non-commercial, Non-derivative and Share '
                              'Alike terms, so read the full combination before publishing [mGWJAAFhtRk @ '
                              '00:01:00].',
                              'The ASMP speaker at B&H lays out the registration routine: fill out the '
                              'form, pay and send a deposit, and deposits can be 600-pixel JPEGs '
                              '[74bQUodJbWY @ 01:16:43]. Separate published from unpublished work, lean '
                              'toward treating work as published, and register before delivering to '
                              'clients. There is a 3-month window after publication [74bQUodJbWY @ '
                              '01:20:24]. The numbers quoted are roughly 1,500 images for $35 and about 6 '
                              "weeks of turnaround, or about $700 to expedite. The same speaker's "
                              'monitoring and proof stack includes the free PLUS Registry, metadata '
                              'practice via dpBestflow, TinEye, Google Images, PicScout, PhotoShelter and '
                              'DMCA takedown letters modeled on Plagiarism Today. The payoff is the '
                              'damages range. Visme puts infringement of a registered work at a minimum of '
                              '$750 and up to $150,000 per work [ShCyD9TYhLY @ 00:00:18], which matches '
                              'the $750-to-$150,000-per-infringement figure from the B&H speaker. Anderson '
                              "prices the infringer's downside at 'hundreds if not thousands… tens of "
                              "thousands.' He stresses that taking the image down afterward does not cure "
                              'the infringement, and that getting defensive or ignoring the claim '
                              'backfires [manKMR61ho0 @ 00:11:29]. He prices his own licenses by scope, '
                              'comparing a 15-employee software license with an enterprise one, and a '
                              'roughly $1 personal song purchase with a national TV ad.',
                              'Against marketplace sellers, Torys LLP says platforms will usually claim '
                              'they are not the seller. On notice, they either forward the complaint to '
                              "the vendor or remove the listing under their terms, but are 'unlikely to do "
                              "much more' [ijF0IyvjXXg @ 00:01:20]. Trademark claims move faster than "
                              'patent claims because the platform is arguably advertising and proof is '
                              'often just the registration. To unmask the real seller, start with the '
                              'platform itself, then use corporate searches, domain name lookups or an '
                              'investigator [ijF0IyvjXXg @ 00:05:39]. For US patent litigation, LawShelf '
                              'maps the sequence. After TC Heartland (2017), venue is limited to the state '
                              'of incorporation, or to where acts of infringement occurred plus a regular '
                              'and established place of business. Next come claim charts setting each '
                              'element against the evidence, then Markman hearings, up to 10 depositions '
                              'per party, a jury trial and a Federal Circuit appeal [WtxlYb996kI @ '
                              '00:06:01]. Remedies start at a reasonable royalty under the Georgia-Pacific '
                              'factors or lost profits, run up to 3x for willful infringement, and add '
                              "attorney's fees in exceptional cases. On defense, Patent Attorney Worldwide "
                              'says the strongest move is invalidity through a prior-art validity search '
                              "covering papers, old products or 'even a YouTube video' [D-Am1gpuzaw @ "
                              '00:03:41].'],
               'table': {'caption': 'Street-level tools, workflows and numbers for clearing and enforcing '
                                    'IP',
                         'headers': ['Mechanic or Tool',
                                     'Exact Steps or Numbers',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [["ScienceDirect 'get rights and content' permission request",
                                   'DOI or title, reuse type, academic, figure count, electronic format, '
                                   'currency fee quote',
                                   'Clear journal figures, then print the license for the journal '
                                   'submission',
                                   'Barbara “Financial Tidbitter” Aboagye ([SK5CqQ61CYI @ 00:01:03])'],
                                  ['Batch copyright registration with a JPEG deposit',
                                   'About 1,500 images for $35, roughly 6 weeks, about $700 to expedite',
                                   'Register batches before client delivery to lock in statutory damages '
                                   'and fee recovery',
                                   'B&H Photo Video Pro Audio ([74bQUodJbWY @ 01:16:43])'],
                                  ['Statutory damages range for registered works',
                                   '$750 minimum, up to $150,000 for each registered work infringed',
                                   'Use the range as payment leverage when demanding license fees from '
                                   'infringers',
                                   'Visme ([ShCyD9TYhLY @ 00:00:38])'],
                                  ['Free-source license filters and CC0 databases',
                                   'Search-engine license filters, Pixabay, Unsplash, CCSearch and '
                                   'DesignLab databases',
                                   'Pull commercial-safe visuals with zero permission requests when the '
                                   'work is CC0',
                                   'DesignLab UW-Madison ([mGWJAAFhtRk @ 00:01:19])'],
                                  ['Image monitoring and registry stack',
                                   'Free PLUS Registry, TinEye, Google Images, PicScout, PhotoShelter, '
                                   'dpBestflow metadata',
                                   'Track where your images appear online and back up DMCA takedown '
                                   'letters',
                                   'B&H Photo Video Pro Audio ([74bQUodJbWY @ 00:38:48])'],
                                  ['Platform notice against an unauthorized online seller',
                                   'Notice gets the listing removed or forwarded; a trademark registration '
                                   'is often enough proof',
                                   'Lead with trademark claims, then unmask the seller through platform, '
                                   'corporate and domain searches',
                                   'Torys LLP ([ijF0IyvjXXg @ 00:05:39])'],
                                  ['Patent damages ladder in US litigation',
                                   'Reasonable royalty via Georgia-Pacific or lost profits; up to 3x for '
                                   'willful infringement',
                                   'Size the claim and push willfulness evidence, such as evidence of '
                                   'copying, during discovery',
                                   'LawShelf ([WtxlYb996kI @ 00:14:33])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Moves the practitioners use to turn rights into leverage',
                           'body': 'Small timing and scoping decisions decide whether an owner collects or '
                                   'walks away empty-handed.',
                           'items': ['Register before you deliver files to a client, because registration '
                                     'has to come before the infringement to unlock full protection, '
                                     'statutory damages and attorney fees [B&H Photo Video Pro Audio — '
                                     '74bQUodJbWY @ 01:19:44]',
                                     'If you are caught using an image, pulling it down does not cure the '
                                     'infringement; do not get defensive or ignore the claim, since costs '
                                     'can run into the tens of thousands [Matthew Anderson — manKMR61ho0 @ '
                                     '00:11:29]',
                                     'For music, cap any clip at 10 to 15 seconds and never use the whole '
                                     'song; the better play is to skip copyrighted songs and use '
                                     'royalty-free sound [DesignLab UW-Madison — mGWJAAFhtRk @ 00:02:58]',
                                     'When designing around a patent, clear every independent claim, '
                                     'including method claims, since patents usually carry at least three; '
                                     'clearing them all also covers the dependent claims [Patent Insanity '
                                     '— Jwz-iMwUtCU @ 00:07:47]']},
               'sop_steps': [{'step': 1,
                              'title': 'Map rights, territory and target',
                              'action': 'List where you hold rights, where the infringing activity '
                                        'happens, and who the true seller is.',
                              'detail': 'Treat IP as jurisdictional, assert local rights against foreign '
                                        'vendors selling into your market, and identify the seller through '
                                        'the platform, corporate searches, domain lookups or an '
                                        'investigator [Torys LLP — ijF0IyvjXXg @ 00:00:36].'},
                             {'step': 2,
                              'title': 'Classify the asset and pick a license route',
                              'action': 'Decide whether the use is commercial, non-commercial or fair use, '
                                        'then choose permission, a paid license, CC or public domain.',
                              'detail': 'Monetized social media, blogs, brochures and newsletters count as '
                                        'commercial use, while classrooms and nonprofits count as '
                                        'non-commercial; fair use is unclear and ultimately decided in '
                                        'court [Visme — ShCyD9TYhLY @ 00:04:27].'},
                             {'step': 3,
                              'title': 'Request and document permission',
                              'action': "Run the publisher's rights request, confirm the fee quote, and "
                                        'keep the issued license on file.',
                              'detail': "Use ScienceDirect's 'get rights and content', specify the figure, "
                                        'format and reuse type, accept the terms, then print the license '
                                        'and submit it to the journal [Barbara “Financial Tidbitter” '
                                        'Aboagye — SK5CqQ61CYI @ 00:04:52].'},
                             {'step': 4,
                              'title': 'Register, monitor and enforce',
                              'action': 'Register work in batches, monitor where it appears with '
                                        'reverse-image tools, and send DMCA letters or license demands.',
                              'detail': 'Registration is required before suing in federal court and '
                                        'unlocks statutory damages, attorney fees and payment leverage; '
                                        'about 1,500 images can be registered for $35 [B&H Photo Video Pro '
                                        'Audio — 74bQUodJbWY @ 01:12:41].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['On stopping an unauthorized seller, the practitioners split between the '
                              'platform lever and the courtroom lever. Torys LLP works the notice route: a '
                              'platform served with a complaint may forward it to the vendor or pull the '
                              'listing, but it is “unlikely to do much more,” and trademark claims move '
                              'faster than patent claims because the platform is “arguably advertising” '
                              'and proof is often just the registration [ijF0IyvjXXg @ 00:05:39]. LawShelf '
                              'maps the heavy alternative: federal court or the ITC, venue limited after '
                              'TC Heartland (2017), claim charts, a Markman hearing, up to 10 depositions '
                              'per party, a jury trial and a Federal Circuit appeal that can take years, '
                              'by which point the technology may be outdated [WtxlYb996kI @ 00:07:35]. '
                              'CIONCA IP frames the endgame as a fork rather than a shutdown: once a '
                              'single claim reads on the product, the owner can recover damages or '
                              'negotiate a license carrying a royalty fee [kRlS4inO95k @ 00:06:11]. The '
                              'Alliance for Patient Access pushes the licensing branch hardest, arguing '
                              'that voluntary licensing, where patent holders partner with other companies '
                              'and share manufacturing expertise, beats regulator-forced compulsory '
                              'licensing that lets copies in before the patent expires [5RtieTL1OqM @ '
                              '00:01:55]. The operator choice is speed and low cost on the platform side '
                              'versus leverage and years of exposure in court.',
                              'Accused infringers get conflicting advice on where to fight. Patent '
                              'Attorney Worldwide calls invalidity the strongest move, running a validity '
                              'search for prior art that can be papers, old products, or “even a YouTube '
                              'video” [D-Am1gpuzaw @ 00:03:41]. LawShelf adds the price of that route: '
                              'non-infringement is proven by a preponderance, but invalidity demands clear '
                              'and convincing evidence, and claim construction strategy flips depending on '
                              'the fight, with the patentee pushing narrow constructions when validity is '
                              'at risk and the accused infringer pushing broad ones [WtxlYb996kI @ '
                              '00:12:05]. Patent Insanity skips the courtroom and teaches designing '
                              'around: read only the claims, drop an unnecessary limitation, or substitute '
                              'something else, but warns that if the substitute performs the same function '
                              '“you may have a problem,” and that courts may differ on equivalence, so '
                              '“proceed cautiously” [Jwz-iMwUtCU @ 00:04:53]. Sinorbit Academy shows why '
                              'that warning bites across borders: the UK line ran from literalism through '
                              'Catnik, where 6 to 8 degrees off vertical still infringed, to Kirin-Amgen '
                              'rejecting a doctrine of equivalence, then Actavis v Lilly (2017) bringing a '
                              'two-stage test that needs yes/yes/no answers, while revocation stays open '
                              'to any person without standing as the “knockout blow” [-uT7bPngmNc @ '
                              '00:54:16].',
                              'On copyright clearance, the split is between leaning on fair use and '
                              'refusing to touch it. freeCodeCamp Concepts lists fair use as one of three '
                              'lawful routes alongside written permission and a purchased license, limited '
                              'to transformative uses such as commentary, review, or parody [grui-CD6Uck @ '
                              '00:00:18]. Visme stretches it to educational, research, or personal use '
                              'like a phone background or an office presentation, then hedges that it is '
                              "“still not 100% clear what is fair use and what isn't and ultimately can "
                              'only be decided in the courtroom,” and that profiting combined with bad '
                              'faith is likely not fair use [ShCyD9TYhLY @ 00:05:17]. DesignLab UW-Madison '
                              'draws a hard line on music, capping a Taylor Swift clip at 10 to 15 seconds '
                              'and saying it is best to avoid copyrighted songs altogether, steering '
                              'creators instead to CC0, “our best friend,” and royalty-free sound '
                              '[mGWJAAFhtRk @ 00:03:17]. The B&H Photo Video ASMP speaker kills the '
                              'percentage shortcut outright: there is no safe percentage, and fair use is '
                              'a defense you can only claim after actually infringing on a work '
                              "[74bQUodJbWY @ 00:20:18]. Visme's closing play is the zero-risk alternative "
                              'that sidesteps the entire argument: create your own content.'],
               'table': {'caption': 'Competing playbooks for enforcement, defense, and clearance',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Stopping an unauthorized online seller fast',
                                   'Serve platform notice; trademark claims move fastest on registration '
                                   'proof',
                                   'File federal suit with claim charts, Markman hearing, depositions, '
                                   'jury trial',
                                   'Torys LLP ([ijF0IyvjXXg @ 00:05:39]); LawShelf ([WtxlYb996kI @ '
                                   '00:02:36])'],
                                  ['Monetizing a proven patent infringement against a product',
                                   'Recover damages once any single claim reads on the product',
                                   'Negotiate a license with a royalty fee instead of litigating',
                                   'CIONCA IP ([kRlS4inO95k @ 00:06:11])'],
                                  ['Sharing patented technology with other manufacturers abroad',
                                   'Voluntary licensing partnerships that share manufacturing expertise '
                                   'and know-how',
                                   'Regulator-forced compulsory licensing that lets copies in before '
                                   'patent expiry',
                                   'Alliance for Patient Access ([5RtieTL1OqM @ 00:01:55])'],
                                  ['Best defense when accused of patent infringement',
                                   'Attack validity with a prior art search, even YouTube videos',
                                   'Argue non-infringement at the lower preponderance burden of proof',
                                   'Patent Attorney Worldwide ([D-Am1gpuzaw @ 00:03:41]); LawShelf '
                                   '([WtxlYb996kI @ 00:12:05])'],
                                  ['Handling equivalence exposure when designing around a claim',
                                   'Eliminate an unnecessary limitation so nothing performs that claimed '
                                   'function',
                                   'Replace the element, accepting risk if it performs the same function',
                                   'Patent Insanity ([Jwz-iMwUtCU @ 00:02:20])'],
                                  ['Using third-party images, clips, and music in content',
                                   'Rely on limited, transformative fair use for commentary, review, '
                                   'parody',
                                   'Avoid fair use entirely; use CC0, free stock, or own content',
                                   'freeCodeCamp Concepts ([grui-CD6Uck @ 00:00:18]); Visme ([ShCyD9TYhLY '
                                   '@ 00:06:10])'],
                                  ['Protecting a decorative design such as a wallpaper pattern',
                                   'Design patent: no copying proof needed, but file within one year',
                                   'Copyright: exists on fixation, register later to unlock statutory '
                                   'damages',
                                   'Derek Fahey, Esq. ([nLSthuXQCL4 @ 00:01:27])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The enforcement traps start with jurisdiction and resale. Torys LLP warns '
                              'that a foreign vendor with no Canadian presence is hard to enforce against, '
                              'and that knocking one listing down usually just pushes the seller to '
                              'another platform: “it can become a bit of a game of whack-a-mole to try to '
                              'stop a foreign vendor” [ijF0IyvjXXg @ 00:02:09]. The same team flags two '
                              'dead ends that burn budget: exhaustion means the first authorized sale ends '
                              "the patentee's control unless limits were “clearly and unambiguously "
                              'expressed” to the purchaser, and reselling genuine trademarked gray goods '
                              'is not infringement at all, so only counterfeits support passing off and '
                              'depreciation of goodwill claims [ijF0IyvjXXg @ 00:04:08]. LawShelf adds the '
                              'remedy trap for non-practicing owners: non-competitors and NPEs are '
                              'generally denied injunctions, leaving a reasonable royalty under the '
                              'Georgia-Pacific factors or lost profits, with up to 3x damages reserved for '
                              "willful infringement and attorney's fees only in exceptional cases "
                              '[WtxlYb996kI @ 00:14:33]. Patents Demystified (Dylan Adams) closes another '
                              'hole that sinks software claims: server-side features create '
                              '“discoverability issues,” and the plaintiff still has to prove every '
                              'element of at least one claim against the actual product, so a hunch about '
                              'hidden code does not get a case off the ground [9hTMXJtONtM @ 00:08:42].',
                              'Timing kills more claims than bad facts. Derek Fahey, Esq. warns that a '
                              'design patent must be filed within one year of first U.S. disclosure or the '
                              'rights are lost, while copyright exists on fixation but only registration '
                              'opens statutory, “enhanced” damages [nLSthuXQCL4 @ 00:00:33]. The B&H Photo '
                              'Video ASMP speaker makes the sequencing explicit: “you must register before '
                              'an infringement to have the full protection of copyright,” with a 3-month '
                              'window after publication, registration required before suing in federal '
                              'court, and statutory damages plus attorney fees acting as payment leverage '
                              '[74bQUodJbWY @ 01:19:44]. The economics check is lopsided in the '
                              "registrant's favor: roughly 1,500 images for $35, deposits as 600-pixel "
                              'JPEGs, about 6 weeks turnaround or about $700 to expedite, set against '
                              'damages of $750 to $150,000 per infringement. Visme runs the same numbers '
                              'from the user side, warning that a copy and paste “that took you 15 '
                              'seconds” can end up “costing you your paycheck Mortgage business or worse,” '
                              'at minimum $750 and up to $150,000 per registered work [ShCyD9TYhLY @ '
                              '00:00:38]. Sinorbit Academy notes the UK twist: intention is irrelevant to '
                              'liability under Proctor v Bennis, but objective innocence can limit damages '
                              'under s.62, and s.69 lets damages reach back to publication [-uT7bPngmNc @ '
                              '00:09:16].',
                              'The image-licensing failures are mostly ownership myths. Matthew Anderson '
                              'states the default bluntly: “unless it has been explicitly written in a '
                              'contract or agreement that copyright ownership has been transferred to you '
                              'by default you do not own the images,” so a client licensed for social, '
                              'website, and blog use cannot hand files to another company even if that '
                              'company would pay [-267ABEXf8o @ 00:00:41]. In Photo Licensing 101 he lists '
                              'the myths that trigger claims: “anything on social media is usable” is “100 '
                              'wrong,” no watermark does not mean free, the brand in the frame gets no '
                              'rights, and taking an image down afterward does not cure the infringement, '
                              'with costs running hundreds if not thousands to tens of thousands, so never '
                              'get defensive or ignore the claim [manKMR61ho0 @ 00:11:29]. Visme adds that '
                              'an Instagram photo is not public domain and that embedding a tweet on a '
                              'website or using it in ads risks trouble, even though retweeting to your '
                              'own feed is fine [ShCyD9TYhLY @ 00:05:53]. On the permission side, Barbara '
                              '“Financial Tidbitter” Aboagye shows the Elsevier fee quote came back at '
                              'zero but is only an estimate that may change, so the printed license, not '
                              'the quote, is what goes to the journal [SK5CqQ61CYI @ 00:03:00].'],
               'table': {'caption': 'Firsthand traps, mechanisms, and the operator check for each',
                         'headers': ['Trap', 'Mechanism Reported', 'Operator Check', 'Expert Source'],
                         'rows': [['Whack-a-mole against foreign platform sellers with no local presence',
                                   'Seller relaunches on another platform after each takedown notice lands',
                                   'Map rights, infringing activity, and the true seller before sending '
                                   'notices',
                                   'Torys LLP ([ijF0IyvjXXg @ 00:02:09])'],
                                  ['Chasing resellers of genuine branded or patented goods',
                                   'Exhaustion and gray goods rules mean genuine resale is not '
                                   'infringement',
                                   'Express any resale limits clearly and unambiguously in the terms of '
                                   'sale',
                                   'Torys LLP ([ijF0IyvjXXg @ 00:02:44])'],
                                  ['Missing the design patent filing window after launch',
                                   'Rights are lost one year after first U.S. disclosure of the design',
                                   'Calendar the one-year deadline from the first public disclosure date',
                                   'Derek Fahey, Esq. ([nLSthuXQCL4 @ 00:00:33])'],
                                  ['Registering copyright only after the infringement has happened',
                                   'Late registration forfeits statutory damages, attorney fees, and '
                                   'payment leverage',
                                   'Register before client delivery; batch roughly 1,500 images for $35',
                                   'B&H Photo Video Pro Audio ([74bQUodJbWY @ 01:12:41])'],
                                  ['Assuming the paying client owns commissioned photos outright',
                                   'Without written transfer, the photographer keeps copyright in most '
                                   'cases',
                                   'Check for clear written permission from the original photographer '
                                   'first',
                                   'Matthew Anderson ([manKMR61ho0 @ 00:02:57])'],
                                  ['Taking an infringing image down and ignoring the claim letter',
                                   'Removal does not cure infringement; costs can reach tens of thousands',
                                   'Respond promptly rather than ignoring the claim or getting defensive',
                                   'Matthew Anderson ([manKMR61ho0 @ 00:11:29])'],
                                  ['Designing around a claim with a functional substitute part',
                                   'A replaced element performing the same function may still be '
                                   'equivalent',
                                   'Clear every independent claim, including method claims, before launch',
                                   'Patent Insanity ([Jwz-iMwUtCU @ 00:05:14])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before you enforce or publish',
                           'body': 'Every item below is a pitfall the practitioners hit or watched clients '
                                   'hit. Clear all four before sending a notice, launching a '
                                   'design-around, or publishing third-party imagery.',
                           'items': ['Confirm the true seller through the platform, corporate searches, '
                                     'domain name lookups, or an investigator before filing anything '
                                     '[Torys LLP — ijF0IyvjXXg @ 00:06:35].',
                                     'Clear every independent claim, including method claims, since '
                                     'patents usually carry at least three independent claims [Patent '
                                     'Insanity — Jwz-iMwUtCU @ 00:07:47].',
                                     'Register images before delivering to clients and inside the 3-month '
                                     'window after publication [B&H Photo Video Pro Audio — 74bQUodJbWY @ '
                                     '01:20:24].',
                                     'Hold clear written permission or a purchased license before using '
                                     'any image; a missing watermark does not mean free [Matthew Anderson '
                                     '— manKMR61ho0 @ 00:10:02].']}}],
 'pull_quote': '“A badly written claim can make an amazing invention totally worthless.” — Patent Attorney '
               'Worldwide (D-Am1gpuzaw @ 00:04:56).',
 'diagram_id': 'diag-05',
 'action_checklist': ['Map where you hold rights, where the infringing activity occurs, and who the '
                      'infringer is before sending any notice [Torys LLP — ijF0IyvjXXg @ 00:00:36].',
                      'Lead platform complaints with trademark registrations, since platforms act faster '
                      'when their liability is clear [Torys LLP — ijF0IyvjXXg @ 00:05:39].',
                      'Build claim charts that set each claim element against the evidence before '
                      'litigating [LawShelf — WtxlYb996kI @ 00:02:36].',
                      'When accused, run a validity search for prior art covering papers, old products, '
                      'and YouTube videos [Patent Attorney Worldwide — D-Am1gpuzaw @ 00:04:11].',
                      'Request reuse rights through the ScienceDirect “get rights and content” flow, then '
                      'print the license and submit it to the journal [Barbara “Financial Tidbitter” '
                      'Aboagye — SK5CqQ61CYI @ 00:04:52].',
                      'Filter for CC0 and Creative Commons images with CCSearch and give attribution '
                      'verbally or on the page [DesignLab UW-Madison — mGWJAAFhtRk @ 00:01:19].'],
 'statutory_citations': [{'title': 'Torys LLP — Ask an IP litigator: #5 - How do I stop an unauthorized '
                                   'seller? [00:05:39]',
                          'url': 'https://www.youtube.com/watch?v=ijF0IyvjXXg&t=339s',
                          'relevance': 'Primary practitioner testimony on platform takedowns, trademark '
                                       'versus patent leverage, and whack-a-mole enforcement.'},
                         {'title': 'LawShelf — Patent Infringement Litigation: Module 5 of 5 [00:14:33]',
                          'url': 'https://www.youtube.com/watch?v=WtxlYb996kI&t=873s',
                          'relevance': 'Primary practitioner testimony on royalty and lost-profit '
                                       'remedies, NPE injunction denials, and willful damages.'},
                         {'title': 'B&H Photo Video Pro Audio — Registration Counts: How to Copyright Your '
                                   'Images [01:12:41]',
                          'url': 'https://www.youtube.com/watch?v=74bQUodJbWY&t=4361s',
                          'relevance': 'Primary practitioner testimony on registration timing, statutory '
                                       'damages, attorney fees, and registration costs.'},
                         {'title': 'Matthew Anderson — Photo Licensing 101 - The Basics Explained '
                                   '[00:11:29]',
                          'url': 'https://www.youtube.com/watch?v=manKMR61ho0&t=689s',
                          'relevance': 'Primary practitioner testimony on client ownership myths and the '
                                       'cost of image infringement claims.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'ijF0IyvjXXg',
                       'title': 'Ask an IP litigator: #5 - How do I stop an unauthorized seller?',
                       'channel': 'Torys LLP',
                       'author': 'Torys LLP',
                       'text': "You have to keep in mind that there's probably another platform that the "
                               'seller can use to promote your product, and unfortunately it can become a '
                               'bit of a game of whack-a-mole to try to stop a foreign vendor.',
                       'tip': "You have to keep in mind that there's probably another platform that the "
                              'seller can use to promote your product, and unfortunately it can become a '
                              'bit of a game of whack-a-mole to try to stop a foreign vendor.',
                       'timestamp': 129,
                       'timestamp_seconds': 129,
                       'timestamp_label': '[00:02:09]',
                       'url': 'https://www.youtube.com/watch?v=ijF0IyvjXXg&t=129s',
                       'markdown': '[00:02:09](https://www.youtube.com/watch?v=ijF0IyvjXXg&t=129s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ijF0IyvjXXg',
                       'title': 'Ask an IP litigator: #5 - How do I stop an unauthorized seller?',
                       'channel': 'Torys LLP',
                       'author': 'Torys LLP',
                       'text': 'Well, it sounds like the platform is usually the best source for '
                               'determining who the true seller is.',
                       'tip': 'Well, it sounds like the platform is usually the best source for '
                              'determining who the true seller is.',
                       'timestamp': 381,
                       'timestamp_seconds': 381,
                       'timestamp_label': '[00:06:21]',
                       'url': 'https://www.youtube.com/watch?v=ijF0IyvjXXg&t=381s',
                       'markdown': '[00:06:21](https://www.youtube.com/watch?v=ijF0IyvjXXg&t=381s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WtxlYb996kI',
                       'title': 'Patent Infringement Litigation: Module 5 of 5',
                       'channel': 'LawShelf',
                       'author': 'LawShelf',
                       'text': 'Willful infringement allows up to three times damages, and exceptional '
                               "cases allow attorney's fees.",
                       'tip': 'Willful infringement allows up to three times damages, and exceptional '
                              "cases allow attorney's fees.",
                       'timestamp': 873,
                       'timestamp_seconds': 873,
                       'timestamp_label': '[00:14:33]',
                       'url': 'https://www.youtube.com/watch?v=WtxlYb996kI&t=873s',
                       'markdown': '[00:14:33](https://www.youtube.com/watch?v=WtxlYb996kI&t=873s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nLSthuXQCL4',
                       'title': 'What is the difference between design patent infringement and Copyright '
                                'infringement?',
                       'channel': 'Derek Fahey, Esq.',
                       'author': 'Derek Fahey, Esq.',
                       'text': 'A design patent must be filed within one year of first U.S. disclosure or '
                               'the rights are lost.',
                       'tip': 'A design patent must be filed within one year of first U.S. disclosure or '
                              'the rights are lost.',
                       'timestamp': 33,
                       'timestamp_seconds': 33,
                       'timestamp_label': '[00:00:33]',
                       'url': 'https://www.youtube.com/watch?v=nLSthuXQCL4&t=33s',
                       'markdown': '[00:00:33](https://www.youtube.com/watch?v=nLSthuXQCL4&t=33s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'D-Am1gpuzaw',
                       'title': 'Patent Infringement Explained: Types, Lawsuits & Legal Remedies (Complete '
                                'Guide)',
                       'channel': 'Patent Attorney Worldwide',
                       'author': 'Patent Attorney Worldwide',
                       'text': 'A badly written claim can make an amazing invention totally worthless.',
                       'tip': 'A badly written claim can make an amazing invention totally worthless.',
                       'timestamp': 296,
                       'timestamp_seconds': 296,
                       'timestamp_label': '[00:04:56]',
                       'url': 'https://www.youtube.com/watch?v=D-Am1gpuzaw&t=296s',
                       'markdown': '[00:04:56](https://www.youtube.com/watch?v=D-Am1gpuzaw&t=296s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-uT7bPngmNc',
                       'title': 'TOPIC 18    Patent Infringement and Defences - Intellectual Property Law '
                                '- UoL',
                       'channel': 'Sinorbit Academy',
                       'author': 'Sinorbit Academy',
                       'text': 'Displaying the product at an exhibition, for instance, has been held to '
                               'count as an offer to dispose.',
                       'tip': 'Displaying the product at an exhibition, for instance, has been held to '
                              'count as an offer to dispose.',
                       'timestamp': 909,
                       'timestamp_seconds': 909,
                       'timestamp_label': '[00:15:09]',
                       'url': 'https://www.youtube.com/watch?v=-uT7bPngmNc&t=909s',
                       'markdown': '[00:15:09](https://www.youtube.com/watch?v=-uT7bPngmNc&t=909s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Jwz-iMwUtCU',
                       'title': 'Designing Around Patents - How to avoid patent infringement',
                       'channel': 'Patent Insanity',
                       'author': 'Patent Insanity',
                       'text': 'Courts may differ on equivalence, so proceed cautiously.',
                       'tip': 'Courts may differ on equivalence, so proceed cautiously.',
                       'timestamp': 293,
                       'timestamp_seconds': 293,
                       'timestamp_label': '[00:04:53]',
                       'url': 'https://www.youtube.com/watch?v=Jwz-iMwUtCU&t=293s',
                       'markdown': '[00:04:53](https://www.youtube.com/watch?v=Jwz-iMwUtCU&t=293s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kRlS4inO95k',
                       'title': 'Patent Infringement - Visually and Simply Explained',
                       'channel': 'CIONCA IP',
                       'author': 'CIONCA IP',
                       'text': 'Because not all the elements of the patented claim are found in the '
                               'accused product, this claim is not infringed by this product.',
                       'tip': 'Because not all the elements of the patented claim are found in the accused '
                              'product, this claim is not infringed by this product.',
                       'timestamp': 234,
                       'timestamp_seconds': 234,
                       'timestamp_label': '[00:03:54]',
                       'url': 'https://www.youtube.com/watch?v=kRlS4inO95k&t=234s',
                       'markdown': '[00:03:54](https://www.youtube.com/watch?v=kRlS4inO95k&t=234s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5RtieTL1OqM',
                       'title': 'Understanding Compulsory Licensing',
                       'channel': 'Alliance for Patient Access',
                       'author': 'Alliance for Patient Access',
                       'text': 'Voluntary licensing lets patent holders partner with other companies and '
                               'share their manufacturing expertise.',
                       'tip': 'Voluntary licensing lets patent holders partner with other companies and '
                              'share their manufacturing expertise.',
                       'timestamp': 115,
                       'timestamp_seconds': 115,
                       'timestamp_label': '[00:01:55]',
                       'url': 'https://www.youtube.com/watch?v=5RtieTL1OqM&t=115s',
                       'markdown': '[00:01:55](https://www.youtube.com/watch?v=5RtieTL1OqM&t=115s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9hTMXJtONtM',
                       'title': 'Mastering Patentability And Infringement Concepts Made EASY',
                       'channel': 'Patents Demystified',
                       'author': 'Patents Demystified',
                       'text': 'One important thing to understand about infringement is a patent cannot '
                               "infringe on somebody else's patent.",
                       'tip': 'One important thing to understand about infringement is a patent cannot '
                              "infringe on somebody else's patent.",
                       'timestamp': 429,
                       'timestamp_seconds': 429,
                       'timestamp_label': '[00:07:09]',
                       'url': 'https://www.youtube.com/watch?v=9hTMXJtONtM&t=429s',
                       'markdown': '[00:07:09](https://www.youtube.com/watch?v=9hTMXJtONtM&t=429s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-267ABEXf8o',
                       'title': 'Do You Own the Photos? - Photography Copyright/Licensing Simplified & '
                                'Explained!',
                       'channel': 'Matthew Anderson',
                       'author': 'Matthew Anderson',
                       'text': 'Well, unless it has been explicitly written in a contract or agreement '
                               'that copyright ownership has been transferred to you, by default you do '
                               'not own the images.',
                       'tip': 'Well, unless it has been explicitly written in a contract or agreement that '
                              'copyright ownership has been transferred to you, by default you do not own '
                              'the images.',
                       'timestamp': 41,
                       'timestamp_seconds': 41,
                       'timestamp_label': '[00:00:41]',
                       'url': 'https://www.youtube.com/watch?v=-267ABEXf8o&t=41s',
                       'markdown': '[00:00:41](https://www.youtube.com/watch?v=-267ABEXf8o&t=41s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'grui-CD6Uck',
                       'title': 'What are the different types of image licenses and how do they work?',
                       'channel': 'freeCodeCamp Concepts',
                       'author': 'freeCodeCamp Concepts',
                       'text': 'You can use an image lawfully with written permission, a purchased '
                               'license, or limited and transformative fair use.',
                       'tip': 'You can use an image lawfully with written permission, a purchased license, '
                              'or limited and transformative fair use.',
                       'timestamp': 18,
                       'timestamp_seconds': 18,
                       'timestamp_label': '[00:00:18]',
                       'url': 'https://www.youtube.com/watch?v=grui-CD6Uck&t=18s',
                       'markdown': '[00:00:18](https://www.youtube.com/watch?v=grui-CD6Uck&t=18s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mGWJAAFhtRk',
                       'title': 'Copyright and Fair Use for Images, Videos, and Audio - Basics',
                       'channel': 'DesignLab UW-Madison',
                       'author': 'DesignLab UW-Madison',
                       'text': 'The music industry is typically much stricter on Fair Use, so it is best '
                               'to avoid using copyrighted songs altogether.',
                       'tip': 'The music industry is typically much stricter on Fair Use, so it is best to '
                              'avoid using copyrighted songs altogether.',
                       'timestamp': 197,
                       'timestamp_seconds': 197,
                       'timestamp_label': '[00:03:17]',
                       'url': 'https://www.youtube.com/watch?v=mGWJAAFhtRk&t=197s',
                       'markdown': '[00:03:17](https://www.youtube.com/watch?v=mGWJAAFhtRk&t=197s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'manKMR61ho0',
                       'title': 'Photo Licensing 101 - The Basics Explained',
                       'channel': 'Matthew Anderson',
                       'author': 'Matthew Anderson',
                       'text': "Photography is our livelihood, we just can't pay our bills with photo "
                               'credit or exposure bucks.',
                       'tip': "Photography is our livelihood, we just can't pay our bills with photo "
                              'credit or exposure bucks.',
                       'timestamp': 443,
                       'timestamp_seconds': 443,
                       'timestamp_label': '[00:07:23]',
                       'url': 'https://www.youtube.com/watch?v=manKMR61ho0&t=443s',
                       'markdown': '[00:07:23](https://www.youtube.com/watch?v=manKMR61ho0&t=443s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SK5CqQ61CYI',
                       'title': 'How to Request Copyright Permission to Reuse an Image | Can You Use '
                                'Images From Research Papers?',
                       'channel': 'Barbara “Financial Tidbitter” Aboagye',
                       'author': 'Barbara “Financial Tidbitter” Aboagye',
                       'text': 'The fee shown is an estimate and may change, and in this example the quote '
                               'came back as zero.',
                       'tip': 'The fee shown is an estimate and may change, and in this example the quote '
                              'came back as zero.',
                       'timestamp': 180,
                       'timestamp_seconds': 180,
                       'timestamp_label': '[00:03:00]',
                       'url': 'https://www.youtube.com/watch?v=SK5CqQ61CYI&t=180s',
                       'markdown': '[00:03:00](https://www.youtube.com/watch?v=SK5CqQ61CYI&t=180s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '74bQUodJbWY',
                       'title': 'Registration Counts: How to Copyright Your Images',
                       'channel': 'B&H Photo Video Pro Audio',
                       'author': 'B&H Photo Video Pro Audio',
                       'text': 'You must register before an infringement to have the full protection of '
                               'copyright.',
                       'tip': 'You must register before an infringement to have the full protection of '
                              'copyright.',
                       'timestamp': 4784,
                       'timestamp_seconds': 4784,
                       'timestamp_label': '[01:19:44]',
                       'url': 'https://www.youtube.com/watch?v=74bQUodJbWY&t=4784s',
                       'markdown': '[01:19:44](https://www.youtube.com/watch?v=74bQUodJbWY&t=4784s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '74bQUodJbWY',
                       'title': 'Registration Counts: How to Copyright Your Images',
                       'channel': 'B&H Photo Video Pro Audio',
                       'author': 'B&H Photo Video Pro Audio',
                       'text': 'Because fair use is really a defense of infringement, that means that you '
                               "can't claim fair use without actually infringing on a work.",
                       'tip': 'Because fair use is really a defense of infringement, that means that you '
                              "can't claim fair use without actually infringing on a work.",
                       'timestamp': 1012,
                       'timestamp_seconds': 1012,
                       'timestamp_label': '[00:16:52]',
                       'url': 'https://www.youtube.com/watch?v=74bQUodJbWY&t=1012s',
                       'markdown': '[00:16:52](https://www.youtube.com/watch?v=74bQUodJbWY&t=1012s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ShCyD9TYhLY',
                       'title': 'How to LEGALLY Use a Copyrighted Photo',
                       'channel': 'Visme',
                       'author': 'Visme',
                       'text': "Copyright infringement shouldn't be shrugged off.",
                       'tip': "Copyright infringement shouldn't be shrugged off.",
                       'timestamp': 370,
                       'timestamp_seconds': 370,
                       'timestamp_label': '[00:06:10]',
                       'url': 'https://www.youtube.com/watch?v=ShCyD9TYhLY&t=370s',
                       'markdown': '[00:06:10](https://www.youtube.com/watch?v=ShCyD9TYhLY&t=370s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'}]}
