from __future__ import annotations

def build_volume_001_workbook() -> dict:
    return {'workbook_id': 'wb-001-heir-hunting',
 'volume_id': 'vol-001-heir-hunting',
 'title': 'Heir Hunting — Practitioner Testimony Operator Workbook',
 'subtitle': 'Heir Hunting: Qualify the Case, Trace Every Relationship, Recover the Complete Probate File, '
             'and Build a Cited Evidence Record',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Case Qualification and Documented Family Reconstruction',
                 'purpose': 'Define the research service before extending the search. Separate commercial '
                            'assumptions from established facts, identify relationships that could '
                            'displace wider relatives, and build a family reconstruction whose sources, '
                            'uncertainties, and next searches remain visible.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Begin with a preliminary research hour. Record what the case requires, '
                                  'what you can establish, and which unresolved questions prevent a '
                                  'responsible commitment.',
                                  'Describe the charging arrangement separately from the research '
                                  'objective. Keep practitioner fee examples attached to their particular '
                                  'service and circumstances rather than treating them as interchangeable.',
                                  'Trace documented parent-child relationships through each generation. '
                                  'Preserve separate categories for biological, half, step, foster, and '
                                  'uncertain relationships wherever the evidence requires them.',
                                  'Review existing sources, obituary versions, family photographs, and '
                                  'collateral relatives before repeating searches. Record unsuccessful '
                                  'searches alongside useful discoveries so another researcher can follow '
                                  'the work.',
                                  'Finish by reviewing possible prior kin, the will question, remaining '
                                  'funds, and independent contact verification. Keep the case provisional '
                                  'wherever these checks remain unresolved.'],
                 'fields': [{'name': 'preliminary_hour',
                             'type': 'textarea',
                             'prompt': 'Describe the work you will complete during a preliminary research '
                                       'hour, including the relationship question, records already '
                                       'available, and skills the case demands. Explain which findings '
                                       'would support acceptance and which gaps would require further '
                                       'investigation before commitment.',
                             'example': 'My preliminary hour will review the supplied family information, '
                                        'identify the first unsupported relationship, and list the records '
                                        'needed to investigate it. I will compare those tasks with my '
                                        'research skills before accepting the assignment. Lawson '
                                        'recommends this initial hour to establish whether a case fits the '
                                        'researcher. [The Genealogy Professional Podcast — R5XtgGL0gkQ @ '
                                        '00:34:16]'},
                            {'name': 'service_and_fee_scope',
                             'type': 'textarea',
                             'prompt': 'State the service being offered and the proposed charging '
                                       'arrangement without assuming that every heir search uses the same '
                                       'commercial model. Identify the case circumstances supporting that '
                                       'choice and distinguish research work, recovery expenses, and the '
                                       'event triggering payment.',
                             'example': "I will compare beneficiary contingency, finder's fee contingency, "
                                        'time spent, and fixed fee before describing the proposed '
                                        'arrangement. Fraser and Fraser presents these as different '
                                        'options for different cases. My scope will identify the selected '
                                        "option explicitly rather than importing another practitioner's "
                                        'percentage into every missing-beneficiary assignment I consider '
                                        'taking. [Fraser and Fraser — EPZo6YVIMi4 @ 00:00:03]'},
                            {'name': 'funds_and_case_activity',
                             'type': 'textarea',
                             'prompt': 'Record how you will check whether funds remain and whether other '
                                       'claimants or case activity affect the proposed investigation. '
                                       'Separate confirmed information from assumed estate value, and '
                                       'identify the unresolved financial question that must be answered '
                                       'before extending field pursuit.',
                             'example': 'Before extending the field search, I will check the courthouse '
                                        'information for other claimants and confirmation that the funds '
                                        'remain. John and Char made those checks before continuing their '
                                        'pursuit. My case note will distinguish what the courthouse '
                                        'confirms from any amount or availability that is still only '
                                        'assumed. [Heir Hunters International — A8ywogOJn9I @ 00:02:26]'},
                            {'name': 'independent_contact_verification',
                             'type': 'textarea',
                             'prompt': 'Explain how an inheritance letter or initial approach will be '
                                       'verified independently before personal information or payment is '
                                       'provided. Identify which supplied details remain unverified and '
                                       'describe why an official appearance, reference number, or '
                                       'telephone number cannot complete this check.',
                             'example': "I will not treat the letter's reference number and supplied "
                                        'telephone number as proof of authenticity. I will seek '
                                        'independent contact before sharing personal information or making '
                                        "payment. The verification note will distinguish the letter's "
                                        'claims from the information established through that separate '
                                        'contact, keeping unresolved claims visibly unverified. [Probate '
                                        'TV — le9BUKYDl1A @ 00:01:03]'},
                            {'name': 'prior_kin_review',
                             'type': 'textarea',
                             'prompt': 'Identify any possible nearer relatives whose existence could '
                                       "change the wider family's position, especially unresolved half "
                                       'siblings. Record the evidence examined, the remaining question, '
                                       'and the reason a wider branch must remain provisional until the '
                                       'earlier relationship issue is resolved.',
                             'example': 'I will keep the wider-family conclusion provisional while the '
                                        'half-sibling question remains open. In the Hubbuck investigation, '
                                        'the team needed to rule out half siblings before treating the '
                                        'wider family as entitled. My review will name the unresolved '
                                        'relationship and the evidence still needed, rather than treating '
                                        'contacted cousins as sufficient. [Ancestry — 4F57BlTAWTk @ '
                                        '00:24:14]'},
                            {'name': 'will_search_checkpoint',
                             'type': 'textarea',
                             'prompt': 'Describe the will-search checkpoint for the case, including what '
                                       'will be examined when property access becomes available. Explain '
                                       'how an undiscovered will could change the research direction, and '
                                       'distinguish completed family tracing from an established basis for '
                                       'continuing the assignment.',
                             'example': 'When property access becomes available, I will include a search '
                                        'for a will rather than assuming the family tracing settles the '
                                        "case. Curran's Battersea work was written off after a charity "
                                        'will appeared behind a wardrobe. My checkpoint will keep that '
                                        'possibility separate from progress locating relatives and '
                                        'documenting their relationships. [Boyes Turner — SLqhAWEXEv4 @ '
                                        '00:17:21]'},
                            {'name': 'generation_link_evidence',
                             'type': 'textarea',
                             'prompt': 'Map the proposed descendant route one generation at a time. For '
                                       'each parent-child connection, identify the supporting record and '
                                       'any unresolved detail. Explain where the chain stops being '
                                       'documented so a plausible family tree does not become an '
                                       'unsupported relationship conclusion.',
                             'example': 'I will list each parent-child link separately and attach the '
                                        'record supporting that generation before extending the line. '
                                        'Tanner calls for a valid sourced relationship at every '
                                        'generation. If a link lacks that support, I will mark the break '
                                        'and investigate it rather than allowing later relatives to make '
                                        'the earlier connection appear established. [BYU Library Family '
                                        'History Center — 9Q4qYeK5DTg @ 00:06:44]'},
                            {'name': 'relationship_confirmation_status',
                             'type': 'textarea',
                             'prompt': 'Create a relationship review that distinguishes possible '
                                       'connections from those supported by two sources. Identify the '
                                       'records supporting each conclusion, retain unresolved '
                                       'disagreements, and specify which relationships need another source '
                                       'before they can move beyond a provisional status in the research '
                                       'report.',
                             'example': 'I will mark a relationship supported by only one source as '
                                        'possible and identify the additional evidence needed. PBI marks '
                                        'relationships confirmed when two sources support them. My review '
                                        'will preserve the actual source references beside each status, so '
                                        'the label does not hide the underlying evidence or an unresolved '
                                        'disagreement. [PBI Research Services — rR4YCKGVNmg @ 00:09:45]'},
                            {'name': 'obituary_version_review',
                             'type': 'textarea',
                             'prompt': 'Plan a comparison of every available obituary or death-notice '
                                       'version for the relevant family. Identify differences in named '
                                       'relatives, corrections, and omitted details, and explain how you '
                                       'will preserve both useful leads and negative findings without '
                                       'mistaking repeated text for additional discovery.',
                             'example': 'I will compare the short notice, fuller obituary, corrections, '
                                        'and versions printed by different newspapers rather than stopping '
                                        'at the first result. Cowan shows that repeated entries can '
                                        'contain different information. My comparison will record which '
                                        "version supplies each relative's name and which versions omit it, "
                                        'preserving the distinctions for follow-up. [Ancestry — '
                                        '_q7yAh8Anok @ 00:12:35]'},
                            {'name': 'existing_source_reinspection',
                             'type': 'textarea',
                             'prompt': 'Identify the existing attached records you will reread before '
                                       'starting another search. Describe the names, initials, dates, and '
                                       'places requiring comparison, and explain how a correction will be '
                                       'recorded without silently replacing the earlier reading or '
                                       'treating a new hint as proof.',
                             'example': 'I will reopen the attached census sources and compare the '
                                        'recorded initial before searching again. Tanner corrected Mary V '
                                        'to Mary A from existing sources, after which a death-record hint '
                                        'appeared. My note will retain the original reading, explain the '
                                        'correction, and list the hint as the next record to inspect '
                                        'rather than a completed conclusion. [BYU Library Family History '
                                        'Center — TVIHQUFpkjk @ 00:45:24]'}],
                 'completion_gate': 'Complete all ten fields before advancing. The file must distinguish '
                                    'the proposed service from payment assumptions, identify unresolved '
                                    'will and prior-kin questions, and show a source-backed route through '
                                    'each investigated generation. Funds and contact authenticity must not '
                                    'be presented as verified without the corresponding check. Carry every '
                                    'unresolved relationship into the next research plan.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Probate Discovery, Complete-File Review, and Authority Checks',
                 'purpose': 'Move from a probable death and an index entry to the surviving estate '
                            'records. Preserve the route through courts, collections, images, and '
                            'citations while distinguishing documentary findings from assumptions about '
                            'family relationships, administration, property condition, and transaction '
                            'readiness.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Start with the probable death information, relevant court, and location '
                                  'of surviving records. Establish collection coverage before interpreting '
                                  'a missing name as a meaningful absence.',
                                  'Follow index references into dockets, journals, packets, and separate '
                                  'will books. Browse surrounding images and other record types instead of '
                                  'assuming indexed results represent the complete estate.',
                                  'Preserve the cover sheet and inspect the last filing to orient the '
                                  'review. Build a chronology that allows administration and later '
                                  'proceedings to extend well beyond the death.',
                                  'Record document requests, processing expectations, copy requirements, '
                                  'and research access restrictions separately. A document listing, an '
                                  'abstract, and an actual record image are different research holdings.',
                                  'Review uncertain terminology, guardianship statements, appointment '
                                  'letters, and property questions before drawing conclusions. Keep '
                                  'research completion separate from authority to sell or readiness to '
                                  'authorize paid probate work.'],
                 'fields': [{'name': 'jurisdiction_and_repository',
                             'type': 'textarea',
                             'prompt': 'Record the probable death information, the court to investigate, '
                                       'and the repository holding surviving records. Explain what remains '
                                       'uncertain about jurisdiction or storage, and identify the next '
                                       'inquiry needed before assuming that an online platform contains '
                                       'the complete estate file.',
                             'example': 'I will begin with the death information, identify the relevant '
                                        'court, and determine where the surviving records are stored '
                                        'before choosing a search collection. Tanner makes record location '
                                        'a necessary part of probate discovery. My repository note will '
                                        'separate the court associated with the estate from the place '
                                        'where its surviving records can actually be consulted. [BYU '
                                        'Library Family History Center — oZiYbKNvxJY @ 00:10:43]'},
                            {'name': 'collection_coverage_review',
                             'type': 'textarea',
                             'prompt': "Describe the collection's stated geographical scope, date range, "
                                       'and any known gaps before evaluating a missing result. Explain '
                                       'whether the intended record falls within that coverage and what '
                                       'additional collection or repository must be checked before drawing '
                                       'a conclusion from absence.',
                             'example': 'Before recording a negative result, I will compare the '
                                        "collection's scope and dates with the estate being investigated. "
                                        'Brown warns that record sets are not necessarily complete. If '
                                        'coverage is uncertain, my log will say the search did not locate '
                                        'the record in that collection, rather than asserting that no '
                                        'probate record exists anywhere. [BYU Library Family History '
                                        'Center — Gwcf300h1sA @ 00:34:12]'},
                            {'name': 'index_to_unindexed_records',
                             'type': 'textarea',
                             'prompt': 'Trace an index reference into its underlying document and any '
                                       'referenced docket or journal. Describe how you will navigate the '
                                       'county collection, preserve the starting result, and inspect '
                                       'unindexed material without treating the first search hit as the '
                                       'whole probate record.',
                             'example': 'I will use the breadcrumb above the Ancestry image to inspect '
                                        'other record types within the county collection, then follow '
                                        'references into relevant dockets and journals. The navigation '
                                        'record will preserve the initial hit and the additional '
                                        'collection route, so an indexed entry does not become a '
                                        'substitute for examining the underlying proceedings. [Ancestry — '
                                        'lOmly79G2Tk @ 00:02:41]'},
                            {'name': 'packet_and_will_book',
                             'type': 'textarea',
                             'prompt': 'Specify how you will check both an estate packet and any '
                                       'separately maintained will book. Record which component has '
                                       'actually been examined, what references connect them, and which '
                                       'missing component prevents you from describing the probate search '
                                       'as complete for this case.',
                             'example': 'For the Jackson County arrangement described by the presenter, I '
                                        'will check the estate packet and the separate will book rather '
                                        'than expecting the packet to contain everything. My checklist '
                                        'will identify each component independently and leave the second '
                                        'item open until examined, even when the first already contains '
                                        'useful names and estate information. [Mid-Continent Public '
                                        'Library — uAcku9kesK4 @ 00:32:38]'},
                            {'name': 'copy_request_and_processing',
                             'type': 'textarea',
                             'prompt': 'Distinguish a document listing from a copy already obtained. '
                                       'Record what must be ordered, how it will be supplied, and the '
                                       'processing expectation described by the office, while keeping '
                                       'processing time separate from a promised delivery date or '
                                       'completed record review.',
                             'example': 'I will treat the Delaware County index as a document listing, not '
                                        'as possession of the underlying images. For an order, I will '
                                        'allow for the stated approximately fourteen-day processing period '
                                        'before mailing or emailing. My status will remain requested until '
                                        'the copy arrives, and the processing estimate will not become a '
                                        'guaranteed delivery date. [Rachel Ezzell Berry — hpvnOFjxwaM @ '
                                        '00:07:18]'},
                            {'name': 'image_citation_capture',
                             'type': 'textarea',
                             'prompt': 'Describe the citation information you will preserve when saving or '
                                       "transferring a probate image. Identify the record's location, the "
                                       'saved navigation link, and the destination description so another '
                                       'researcher can return to the image without repeating the entire '
                                       'browsing sequence.',
                             'example': 'When bringing a FamilySearch image into Ancestry, I will copy the '
                                        'Information-tab citation into the image description and preserve '
                                        'the image URL. This keeps the saved image connected to its '
                                        'location. I will retain that route with the document rather than '
                                        'depending on memory or repeating the browsing process during the '
                                        'next review. [Five-minute genealogy — hsFQHg-SMN4 @ 00:03:31]'},
                            {'name': 'file_orientation_and_chronology',
                             'type': 'textarea',
                             'prompt': 'Explain how the cover sheet and last filing will orient your '
                                       'reading of the estate. Record the chronological span you need to '
                                       'investigate and identify any later proceedings that would be '
                                       'missed by stopping near the death date or the initial appointment.',
                             'example': 'I will preserve the cover sheet and read the last filing first to '
                                        'understand where the estate proceedings ended before '
                                        'reconstructing the intervening sequence. Tanner uses those steps '
                                        'to orient the Utah estate review. My chronology will remain open '
                                        'to later filings rather than ending automatically with the death '
                                        'or the first probate document. [BYU Library Family History Center '
                                        '— 07zaZ3sQwi8 @ 00:01:47]'},
                            {'name': 'document_sides_and_completeness',
                             'type': 'textarea',
                             'prompt': 'Identify which petitions and related papers require inspection on '
                                       'both sides. Describe how you will record missing versos, '
                                       'incomplete images, and information discovered outside the first '
                                       'visible page, keeping the distinction between a reviewed image and '
                                       'a fully reviewed document explicit.',
                             'example': 'I will inspect the reverse of each available petition instead of '
                                        'extracting only the first visible page. Finley found additional '
                                        "Chapman information on a petition's reverse. My document "
                                        'checklist will record whether both sides were available and read, '
                                        'so an absent reverse image remains a retrieval question rather '
                                        'than an assumption that nothing follows. [FamilySearch — '
                                        'fCvgh_QabMY @ 00:08:48]'},
                            {'name': 'guardianship_interpretation',
                             'type': 'textarea',
                             'prompt': 'Record exactly what a guardianship document establishes and '
                                       'separate its financial function from assumptions about where a '
                                       'child lived or who raised them. Identify any proposed family '
                                       'narrative that requires additional evidence before it can be '
                                       'included in the research conclusion.',
                             'example': 'I will describe the guardian appointment as a financial matter '
                                        "unless other evidence supports a statement about the child's "
                                        "upbringing. O'Neill's Slough correction identifies the mistake of "
                                        'turning an appointment into a custody story. My conclusion will '
                                        "preserve the document's actual function and leave household or "
                                        'caregiving claims unresolved rather than filling them in. '
                                        '[Five-minute genealogy — 7_oRhXnhlag @ 00:04:06]'},
                            {'name': 'administration_authority_checkpoint',
                             'type': 'textarea',
                             'prompt': 'Describe the appointment letters you must inspect and the '
                                       'administration restrictions requiring clarification before a sale '
                                       "proceeds. Separate the representative's appointment from authority "
                                       'for the proposed transaction, and record any additional order and '
                                       'timing issue that remains unresolved in the file.',
                             'example': 'I will inspect the appointment letters and determine whether '
                                        'dependent administration requires a sale order before treating '
                                        'the transaction as ready. Krit describes an approximately '
                                        'two-week order delay affecting timing. My review will distinguish '
                                        'the appointment already documented from the additional sale '
                                        'authority still needed, rather than assuming one establishes the '
                                        'other in this case. [Texas Probate Real Estate — n8jP0gweIR4 @ '
                                        '00:23:34]'}],
                 'completion_gate': 'Advance only when the court and repository route is recorded, '
                                    'collection limitations are visible, and index entries are separated '
                                    'from documents actually obtained. Preserve citations, document '
                                    'requests, missing pages, and later proceedings. Do not equate a '
                                    'complete family tree with transaction authority. Before authorizing '
                                    'paid probate work, complete the title and property investigation '
                                    'rather than leaving those questions until filings have begun.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Conflict Resolution, Research Logs, and Digital Evidence Control',
                 'purpose': 'Turn competing records into an explicit, reviewable analysis. Separate '
                            'namesakes, retain uncertain relationships, distinguish meaningful absence '
                            'from unsuccessful searching, and preserve citations through timelines, '
                            'transcription, identity comparison, and digital-file checks without allowing '
                            'software output to replace documentary reasoning.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Write the research question and assemble original-image details before '
                                  'choosing a preferred identity. Preserve conflicting spellings, dates, '
                                  'and relationship descriptions instead of smoothing them into agreement.',
                                  'Compare candidates through relatives, chronology, geography, and '
                                  'associated records. Keep provisional relationships visibly provisional '
                                  'and test explanations against evidence that could disprove them.',
                                  'Record every search with its source and result. Distinguish an '
                                  'unsuccessful search from missing information that was expected in an '
                                  'extant, relevant record.',
                                  'Carry citations with facts into comparison tables and timelines. Begin '
                                  'with five or ten research ideas, then revise the plan as easier '
                                  'verification changes the remaining questions.',
                                  'Review what digital processing might alter or discard. Test recognition '
                                  'beyond training pages, retain reviewable identity connections, and '
                                  'investigate unexplained file changes before accepting the resulting '
                                  'evidence package.'],
                 'fields': [{'name': 'namesake_comparison',
                             'type': 'textarea',
                             'prompt': 'Build a comparison of competing people sharing the same name, '
                                       'using spouses, children, locations, and associated records. '
                                       'Explain which details distinguish the candidates and which common '
                                       'characteristics provide little separation, keeping each identity '
                                       'independent until the documentary comparison supports a '
                                       'conclusion.',
                             'example': 'I will keep the Daniel Jones candidates separate and compare '
                                        'their spouses, children, locations, and associated records. Cowen '
                                        'distinguished five men, all of whom were farmers, so occupation '
                                        'alone did not resolve identity. My table will show the family and '
                                        'record associations that separate each candidate rather than '
                                        'merging people because their names and work agree. [Ancestry — '
                                        'K6-4Y6O5bbQ @ 00:23:16]'},
                            {'name': 'original_image_comparison',
                             'type': 'textarea',
                             'prompt': 'Describe how you will collect original-image details from '
                                       'suggested records and arrange them chronologically. Identify the '
                                       'dates, locations, relatives, and wording to compare, and explain '
                                       'how the combined table will expose contradictions that a single '
                                       'attractive search result could leave unnoticed.',
                             'example': 'I will open Suggested Records in separate tabs, arrange them '
                                        'chronologically, and extract the original-image details into one '
                                        'comparison table. Cowen uses this approach to analyze the records '
                                        'together. My table will preserve dates, places, and named '
                                        'associates from each image, making differences visible before I '
                                        'decide whether the records describe one person or competing '
                                        'candidates. [Ancestry — ElrY5ALsx1Y @ 00:11:47]'},
                            {'name': 'provisional_relationship_label',
                             'type': 'textarea',
                             'prompt': 'Identify a relationship currently suggested but not established by '
                                       'the record wording. Preserve the exact description, state the '
                                       'proposed interpretation separately, and explain how your working '
                                       'tree or notes will keep that uncertainty visible until additional '
                                       'evidence supports or contradicts the proposal.',
                             'example': 'I will retain Pearl as a possible spouse rather than converting '
                                        "the draft card's nearest-relative description into a confirmed "
                                        'marriage. Cowen italicized the provisional relationship in the '
                                        "working analysis. My note will preserve the card's wording and "
                                        'the tentative interpretation separately, so later readers can see '
                                        'precisely which part comes from the record and which remains '
                                        'inference. [Ancestry — ElrY5ALsx1Y @ 00:16:54]'},
                            {'name': 'negative_evidence_classification',
                             'type': 'textarea',
                             'prompt': 'Classify an absence as either an unsuccessful search or missing '
                                       'information expected in an extant source. Explain the expectation, '
                                       'the source examined, and the limits of coverage, then state what '
                                       'conclusion the absence can support without treating those two '
                                       'situations as equivalent.',
                             'example': 'If I fail to locate a record, I will log the unsuccessful search '
                                        'without declaring that the event never occurred. If an extant '
                                        'source lacks information expected there, I will explain that '
                                        'expectation separately. Childs distinguishes those situations, so '
                                        'my analysis will preserve the difference rather than using every '
                                        'missing search result as equivalent negative evidence. '
                                        '[FamilySearch — VwfAeN31cTw @ 00:26:51]'},
                            {'name': 'written_conflict_resolution',
                             'type': 'textarea',
                             'prompt': 'Write the competing claims and explain why they disagree, what '
                                       'evidence supports each, and what remains unresolved. State your '
                                       'current conclusion only as strongly as the comparison permits, and '
                                       'identify the next record or question needed if the conflict cannot '
                                       'yet be settled.',
                             'example': 'I will write a conflict note even when the available evidence '
                                        'does not resolve the disagreement. The note will set out the '
                                        'competing statements, the records supporting them, and the '
                                        'remaining question. The practitioner recommends documenting '
                                        'conclusions or the unresolved conflict itself, so uncertainty '
                                        'stays visible rather than disappearing when the family tree is '
                                        'updated later. [FamilySearch — Ep2zENQQZ1k @ 00:17:44]'},
                            {'name': 'first_search_citation',
                             'type': 'textarea',
                             'prompt': 'Describe the citation you will create at the first examination of '
                                       'a source. Identify the record and its retrieval route while the '
                                       'information is available, and explain how the citation will remain '
                                       'attached to extracted facts rather than being reconstructed from '
                                       'memory afterward.',
                             'example': 'I will create the citation when I first search the source, while '
                                        'the record and retrieval details are still visible. The citation '
                                        'will accompany the extracted information in my notes. The '
                                        'practitioner emphasizes doing this immediately because it is '
                                        'easier than reconstructing the source later, especially when '
                                        'several searches contribute to the same relationship question. '
                                        '[FamilySearch — DUAbGD8rVzA @ 00:06:50]'},
                            {'name': 'cited_timeline_transfer',
                             'type': 'textarea',
                             'prompt': 'Explain how facts will move from your research log into a '
                                       'chronology without losing their citations. Identify which dates '
                                       'and statements belong to each source, and describe how conflicting '
                                       'entries will remain separately attributable instead of becoming a '
                                       'single uncited narrative.',
                             'example': 'I will copy the fact and its citation together from the log into '
                                        'the timeline, retaining separate entries where records disagree. '
                                        'Coford insists that citations follow facts during this transfer. '
                                        'My chronology will therefore remain a route back to the evidence, '
                                        'not merely a convenient sequence of dates detached from the '
                                        'documents that supplied them. [FamilySearch — J1h18kFbXKU @ '
                                        '00:12:06]'},
                            {'name': 'identity_merge_review',
                             'type': 'textarea',
                             'prompt': 'Identify what information an identity merge would discard or '
                                       'conceal. Explain whether a reviewable same-as relationship would '
                                       'preserve competing records more clearly, and state which '
                                       'unresolved differences must remain visible before any '
                                       'software-assisted similarity result becomes a decision to combine '
                                       'people.',
                             'example': 'Before combining candidate identities, I will list the '
                                        'information that would disappear or become difficult to review. '
                                        'Tomas keeps same-as relationships available for review or '
                                        'permanent use instead of automatically merging nodes. I will '
                                        'retain that reviewable connection where differences remain, '
                                        'rather than allowing a similarity result to erase distinctions '
                                        'that the research has not resolved. [Neo4j — GMTY78xqGXQ @ '
                                        '00:33:50]'},
                            {'name': 'recognition_validation',
                             'type': 'textarea',
                             'prompt': 'Describe how a newly trained text recognizer will be tested before '
                                       'processing the remaining documents. Identify pages outside the '
                                       'ground-truth set, the comparison you will make against their '
                                       'images, and the unresolved reading problems that should prevent '
                                       'unquestioned use of recognized text.',
                             'example': 'I will test the newly trained recognizer on pages outside the '
                                        'ground-truth set before applying it to all remaining pages. The '
                                        'Transkribus demonstration makes that separate test a checkpoint. '
                                        'My review will compare recognized text with the images and retain '
                                        'unresolved readings, rather than assuming success on training '
                                        'material establishes reliability for every document still '
                                        'awaiting recognition. [Transkribus — bLXMXvhuz6k @ 00:52:56]'},
                            {'name': 'file_change_investigation',
                             'type': 'textarea',
                             'prompt': 'Record how repeated checksum checks will be reviewed and how known '
                                       'operator edits will be distinguished from unexplained changes. '
                                       'Identify the affected file, the change requiring investigation, '
                                       'and why a changed result must be examined rather than '
                                       'automatically dismissed or labeled damage.',
                             'example': 'When the Fixity report identifies a changed file, I will check '
                                        'whether an operator edit explains it before deciding what '
                                        'happened. The tutorial distinguishes expected edits from '
                                        'unexplained changes that could indicate damage. My review note '
                                        'will identify the file and the explanation still needed, keeping '
                                        'the investigation open instead of treating every difference as '
                                        'harmless or corrupt. [ScottishArchivesTV — 1pRY7lpZ7nA @ '
                                        '00:09:27]'}],
                 'completion_gate': 'Complete the comparison and documentation before promoting a '
                                    'candidate to a resolved identity. Namesakes must remain '
                                    'distinguishable, provisional relationships must stay labeled, and '
                                    'every conflict must have a written conclusion or an explicit '
                                    'unresolved question. Citations must survive transfer into timelines. '
                                    'Do not accept an automatic merge, untested recognizer, or unexplained '
                                    'file change as a substitute for reviewing and preserving the '
                                    'underlying evidence.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Deceased-Owner Claim Readiness and Recovery Operations',
                 'purpose': 'Build a claim file that connects the deceased owner, claimant, property, '
                            'required evidence, and applicable filing process. Separate county surplus '
                            'work from state unclaimed-property procedures, then establish practical '
                            'document collection, communication, and follow-up controls.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Choose one claim and identify its jurisdiction and recovery category '
                                  'before selecting forms or estimating compensation.',
                                  'Complete every field with documented facts, outstanding questions, and '
                                  'the next action needed to resolve each gap.',
                                  'Keep Property IDs, Claim IDs, owner identities, and claimant '
                                  'relationships separately labeled throughout the working file.',
                                  'Select the document collection approach appropriate to the claims '
                                  'office rather than imposing one universal submission sequence.',
                                  'Review the completion gate before filing, extending paid research, or '
                                  'treating a contacted claimant as a completed recovery.'],
                 'fields': [{'name': 'owner_identity_and_death_evidence',
                             'type': 'textarea',
                             'prompt': "Record the deceased owner's full name, death date, and death "
                                       'place. Identify the document supporting those details, state '
                                       'whether the death certificate is actually present, and assign the '
                                       'next collection action before treating the claim file as ready.',
                             'example': 'I will mark the death certificate as missing until the document '
                                        'is actually received, not merely requested. Richardson describes '
                                        "Christian's $138,000 claim remaining stalled for over a year "
                                        'because that certificate was absent. My collection checklist will '
                                        'therefore distinguish requested, received, and still outstanding '
                                        'evidence before submission. [Money Making Juggernaut — '
                                        'MVCNlj7HQBQ @ 00:12:31]'},
                            {'name': 'claim_route_and_heirship_form',
                             'type': 'textarea',
                             'prompt': "Identify the claim's state or county route and explain why the "
                                       "selected heirship paperwork fits the deceased owner's "
                                       'circumstances. Record whether a will, trust, other estate plan, or '
                                       "probate requirement changes the proposed use of California's Table "
                                       'of Heirship.',
                             'example': 'For a California heir claim, I will not select the Table of '
                                        'Heirship merely because the owner died. The stated use concerns '
                                        'intestacy without a will, trust, or other estate plan, where '
                                        'probate was not required. Any unanswered condition remains an '
                                        "open routing question. [California State Controller's Office — "
                                        'cMCrrRkehJk @ 00:00:19]'},
                            {'name': 'property_and_claim_identifier_control',
                             'type': 'textarea',
                             'prompt': 'List the identifiers used by the claim process and specify exactly '
                                       "where each belongs. Separate the submission's Claim ID from "
                                       'individual Property IDs, describe any attached property schedule, '
                                       'and record the identifier check required before uploading '
                                       'supporting documents.',
                             'example': 'My California declaration checklist will place the individual '
                                        'Property ID Numbers in Section 5 and use an attached property '
                                        'list when needed. I will keep the Claim ID in a separately '
                                        'labeled entry so it is not substituted for the property '
                                        'identifiers during preparation or review. [California State '
                                        "Controller's Office — 1ahhduhMdd0 @ 00:01:25]"},
                            {'name': 'document_collection_and_return_plan',
                             'type': 'textarea',
                             'prompt': "Create the claimant's document checklist and choose a collection "
                                       'sequence. Explain whether the file will be returned as one '
                                       'complete bundle or submitted with available evidence for examiner '
                                       'follow-up, identifying who collects outstanding items and how '
                                       'their return is tracked.',
                             'example': "When using Church's bundled approach, I will give the notary the "
                                        'client checklist and ask for every listed item to come back '
                                        'together in a FedEx envelope. The return review will compare the '
                                        'contents against that checklist rather than assuming notarization '
                                        'means the supporting file is complete. [Surplus Institute / David '
                                        'Church / Unclaimed Funds — 1AMk1-SB5ic @ 00:00:56]'},
                            {'name': 'address_evidence_and_upload_review',
                             'type': 'textarea',
                             'prompt': 'Identify any missing connection between the owner and an old '
                                       'address, then list the evidence you will pursue. Describe how each '
                                       'upload will be labeled and how the receiving Claim ID will be '
                                       'checked before documents are sent.',
                             'example': 'For an unresolved Ohio address connection, I will consider a BMV '
                                        'transcript, a relevant hospital bill, or a credit report showing '
                                        'address history. I will record which item is being pursued and '
                                        'whether it actually supports the address connection, instead of '
                                        'treating any personal document as sufficient evidence. '
                                        '[ohiocommerce — dFKMkAIKskU @ 00:03:15]'},
                            {'name': 'deadline_notarization_and_queue_notes',
                             'type': 'textarea',
                             'prompt': 'Record the applicable deadline discussion, the receive date shown '
                                       'on the claim form, and any notarization requirement. Distinguish '
                                       "the claim's actual submission requirements from reported "
                                       'processing queues, and identify older guidance that must not '
                                       'control the filing plan.',
                             'example': 'My Ohio timing note will use the February 2026 discussion of HB '
                                        '96, 2036, and the receive date on the form rather than repeat the '
                                        "older forever-holding message. I will leave the claim's operative "
                                        "date unresolved until the form's receive date has been recorded "
                                        'and reviewed. [ohiocommerce — 8nmo4S1v3Co @ 00:09:15]'},
                            {'name': 'county_sales_claims_and_liens',
                             'type': 'textarea',
                             'prompt': 'Document how the county publishes upcoming sales, completed sale '
                                       'results, and claim instructions. Record the checks for an existing '
                                       'claim and liens, then explain whether the remaining surplus '
                                       'supports further pursuit or requires additional investigation '
                                       'before claimant outreach continues.',
                             'example': 'I will add separate entries for existing claims and liens before '
                                        'extending a county surplus pursuit. Richardson identifies both as '
                                        'research beginners often omit. A listed surplus will remain an '
                                        'unqualified opportunity until those checks show whether another '
                                        'claim exists and whether liens reduce or eliminate the amount '
                                        'available. [Money Making Juggernaut — FNbqvZGEzeE @ 00:02:48]'},
                            {'name': 'registration_fee_and_effort_fit',
                             'type': 'textarea',
                             'prompt': 'Identify the operating registration instructions, prescribed '
                                       'agreement materials, and fee arrangement for this specific '
                                       'recovery category. Compare expected research effort with available '
                                       'compensation, and explain why a percentage reported for another '
                                       "jurisdiction or claim type does not establish this file's "
                                       'economics.',
                             'example': "For a Delaware market review, I will record Wilkerson's reported "
                                        '10% commission cap separately from the question of bulk-lead '
                                        'availability. Their evaluation emphasizes that availability, not '
                                        "the percentage alone. I will not import Richardson's separate 25% "
                                        'recovery example into the Delaware worksheet as an available fee '
                                        'assumption. [Surplus Funds 101 — TTfaOSBvLDc @ 00:05:14]'},
                            {'name': 'proof_first_contact_and_response',
                             'type': 'textarea',
                             'prompt': "Write the first contact's objective, the proof you intend to send, "
                                       'and the follow-up action. Distinguish a complaint about your '
                                       'approach from an existing agreement with another investigator, and '
                                       'specify how each response changes the next conversation.',
                             'example': 'My first-call objective will be permission to send proof, not an '
                                        'immediate signature. Richardson explicitly separates that first '
                                        'conversation from closing. I will record whether the person '
                                        'received the proof and what question remains, rather than '
                                        'classify an unfinished initial conversation as a failed recovery '
                                        'or a completed engagement. [Money Making Juggernaut — DMdtmrWAO6c '
                                        '@ 00:07:39]'},
                            {'name': 'notary_coverage_and_follow_up_capacity',
                             'type': 'textarea',
                             'prompt': 'Describe the notary coverage needed for the claim area, including '
                                       'replacement recruitment and current availability. Set a recurring '
                                       'review action and identify how claimant follow-up will continue '
                                       'when an existing notary becomes unavailable or a document return '
                                       'remains incomplete.',
                             'example': 'I will schedule a weekly 15-to-30-minute notary recruitment event '
                                        'with reminders rather than consider the roster permanently '
                                        'finished. The review will keep replacement coverage active while '
                                        'current claims move forward. A scheduled recruitment block will '
                                        "remain separate from the check that a particular claimant's "
                                        'documents have actually returned. [Surplus Funds 101 — '
                                        'Qn63DtrxFts @ 00:02:01]'}],
                 'completion_gate': 'Advance only when the owner and claimant connection is documented, '
                                    'the selected forms fit the claim route, required evidence and '
                                    'identifiers have been checked, and deadlines and outstanding items '
                                    'are explicit. Keep unresolved death evidence, existing claims, liens, '
                                    'registration questions, or document gaps visible rather than calling '
                                    'the recovery ready.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Qualified Probate Leads and Curative-Title Decisions',
                 'purpose': 'Turn probate records and property leads into researched opportunities without '
                            'confusing contact data, family identity, or apparent equity with a closable '
                            'transaction. Establish a bounded sourcing test, respectful outreach, verified '
                            'ownership, and a cure budget before committing further.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Start with a defined research sample and record why each retained '
                                  'property deserves more investigation.',
                                  'Preserve source settings, contact requirements, ownership notes, and '
                                  'exclusions so the qualification process can be reviewed.',
                                  'Keep wrong numbers, unanswered calls, located owners, and willing '
                                  'sellers as distinct outcomes in the contact record.',
                                  'Build the ownership and death timeline before treating an apparent heir '
                                  'or fractional interest as verified.',
                                  'Compare the complete cure burden with the available spread and record '
                                  'an explicit proceed, hold, or reject decision.'],
                 'fields': [{'name': 'lead_source_and_initial_sample',
                             'type': 'textarea',
                             'prompt': 'Choose the initial probate or ownership-problem lead source and '
                                       'define a manageable research sample. Explain what direct '
                                       'collection or purchased data contributes, how candidates will be '
                                       'ranked, and what evidence must emerge before expanding beyond the '
                                       'first sample.',
                             'example': "I will use Fricke's starting structure: assemble 50–100 visibly "
                                        'distressed properties, research an initial subset, and rank the '
                                        'best 10–20. The ranking will identify candidates for deeper '
                                        'ownership investigation rather than imply completed transactions. '
                                        'I will keep address-specific findings with the sample instead of '
                                        'scaling immediately into a larger purchased database. [Courtney '
                                        'Fricke — W-FX20iI9Jk @ 00:20:03]'},
                            {'name': 'historical_search_and_contact_filters',
                             'type': 'textarea',
                             'prompt': 'Record the historical filing window, property availability '
                                       'selection, geographic filters, and required contact fields. '
                                       'Explain how you will preserve contact quality when volume declines '
                                       'and verify the selected year and complete qualifying record set '
                                       'before exporting the search results.',
                             'example': "I will treat Jonathan's reduction from 228 historical Los Angeles "
                                        'cases to 71 Available properties with petitioner phone and email '
                                        'as a qualification example, not a conversion rate. My export '
                                        'notes will preserve those contact requirements and the selected '
                                        'filing window so a later review can explain the retained records. '
                                        '[probatedata — nRRFhMEip8c @ 00:04:43]'},
                            {'name': 'owner_variants_and_address_notes',
                             'type': 'textarea',
                             'prompt': 'List owner-name variants, middle initials, suffixes, and property '
                                       'addresses requiring investigation. Record findings beside the '
                                       'specific address rather than in an undifferentiated lead list, and '
                                       'identify the unresolved ownership condition that makes each '
                                       'candidate worth further research.',
                             'example': 'My screening spreadsheet will retain the property address and the '
                                        'owner-name versions searched, including middle initials and '
                                        "suffixes. Following Fricke's approach, I will keep "
                                        'address-specific research notes alongside that screening work. An '
                                        'unsuccessful search under one spelling will not become a blanket '
                                        'conclusion that the ownership problem cannot be investigated. '
                                        '[Courtney Fricke — W-FX20iI9Jk @ 00:14:16]'},
                            {'name': 'outreach_offer_and_removal_handling',
                             'type': 'textarea',
                             'prompt': 'Describe the service offered in outreach and how the next contact '
                                       "will be chosen from the person's response. Record any request for "
                                       'removal and explain how you will prevent a rejected lead from '
                                       'being pursued indirectly through relatives.',
                             'example': 'If the executor requests removal, I will delete the rejected lead '
                                        'rather than contact relatives to bypass that response. Gross '
                                        "gives that direction in Richard's situation. My outreach record "
                                        'will show that the lead was removed, not quietly reclassified as '
                                        'a family-tracing opportunity for another person to pursue. '
                                        '[Probate Mastery — PDnxvvPI7jU @ 00:28:53]'},
                            {'name': 'telephone_quality_and_provider_tracking',
                             'type': 'textarea',
                             'prompt': 'Record the provider associated with each telephone number and '
                                       'separate verified wrong numbers from unanswered calls. Explain how '
                                       'those outcomes affect the next tracing action, the evaluation of '
                                       'purchased data, and any decision to repeat or change outreach.',
                             'example': 'I will tag each telephone number with its provider in the CRM and '
                                        'reserve the wrong-number label for a verified mismatch. A correct '
                                        'number that does not answer stays in a separate category. This '
                                        'prevents the contact review from treating nonresponse as proof '
                                        'that the data provider identified the wrong person. [Logan '
                                        'Fullmer — dJ-LTFmMsTg @ 00:02:18]'},
                            {'name': 'alternate_address_and_obituary_route',
                             'type': 'textarea',
                             'prompt': "Compare the subject property's address with its separate mailing "
                                       'address and identify the next tracing route. List historical '
                                       'occupants, associates, or obituary questions worth pursuing, and '
                                       'explain how a stalled name search will change into a different '
                                       'research approach.',
                             'example': 'When the property address differs from the mailing address, I '
                                        'will trace the mailing address rather than keep repeating the '
                                        "same owner-name search. Shepard's method uses address research to "
                                        'uncover historical occupants and associates. I will record those '
                                        'connections as tracing leads, not automatically promote an '
                                        'associated person into a verified heir. [Logan Fullmer — '
                                        'zMW-iFWYX9w @ 00:04:13]'},
                            {'name': 'identity_and_vesting_confirmation',
                             'type': 'textarea',
                             'prompt': 'Explain how the located person has been matched to the ownership '
                                       'record beyond sharing a name. Identify the vesting evidence and '
                                       'heirship questions still unresolved, and state what must be '
                                       'confirmed before contracting for a deed or racing toward closing.',
                             'example': 'My decision note will separate a successful locate from '
                                        'confirmation that the person holds the relevant interest. '
                                        "Fullmer's wrong-heir reversal makes exact identity and vesting a "
                                        'checkpoint before closing pressure takes over. Until those '
                                        'questions are resolved, I will describe the person as a candidate '
                                        'connection rather than the verified seller. [Logan Fullmer — '
                                        'zMW-iFWYX9w @ 00:15:42]'},
                            {'name': 'spouse_death_and_interest_timeline',
                             'type': 'textarea',
                             'prompt': 'Build the spouse-and-death timeline for the ownership chain and '
                                       'list every acquired or asserted interest separately. Explain which '
                                       'title findings could reveal missing interests after heir '
                                       'purchases, and identify the evidence needed before claiming that '
                                       'ownership has been assembled.',
                             'example': 'I will rebuild the spouse-and-death sequence even after apparent '
                                        "heir interests have been purchased. Matt's title opening exposed "
                                        'four asserted life estates after the purchases in the ten-heir '
                                        'transaction. My interest schedule will therefore distinguish '
                                        'purchased interests from unresolved assertions instead of '
                                        'assuming a collection of heir deeds settles the entire chain. '
                                        '[Courtney Fricke — nYQaov_liDw @ 00:09:16]'},
                            {'name': 'cure_budget_and_walk_away_test',
                             'type': 'textarea',
                             'prompt': 'Calculate the apparent spread separately from succession costs, '
                                       'co-owner negotiation, occupancy resolution, liabilities, and '
                                       'delay. Explain which amounts remain uncertain and whether '
                                       'compensation still justifies the work, documenting a clear reason '
                                       'to proceed, investigate further, or reject the proposed purchase.',
                             'example': "I will not label Fricke's $15,500 apparent spread as profit: the "
                                        'assumed 25% interest was valued at $22,500 against a $7,000 '
                                        'purchase price before cure costs. My worksheet will leave '
                                        'succession, negotiation, occupancy, liabilities, and delay '
                                        'visible so the arithmetic cannot conceal why the fractional '
                                        'purchase was rejected. [Courtney Fricke — -QzABvCmtVc @ '
                                        '00:03:25]'},
                            {'name': 'locate_scope_deadline_and_outcome',
                             'type': 'textarea',
                             'prompt': 'Define whether the engagement purchases a locate, deeper research, '
                                       'or progress toward a closing. Record any auction deadline and '
                                       "explain how a successfully contacted owner's refusal changes the "
                                       'outcome without erasing the research work or implying a completed '
                                       'transaction.',
                             'example': 'I will budget the locate as a separate deliverable rather than '
                                        'promise a closing from a successful contact. The Bakers describe '
                                        'an owner who was located and contacted but refused. My result '
                                        'entry will preserve both facts: the tracing objective was '
                                        'achieved, while the proposed transaction did not follow from that '
                                        'success. [Logan Fullmer — GK-4kFznJlA @ 00:17:58]'}],
                 'completion_gate': 'Proceed only when search settings and contact quality are recorded, '
                                    'removal requests are honored, the person and ownership interest are '
                                    'verified, and the cure burden has been evaluated separately from the '
                                    'apparent spread. Hold unresolved interest chains or undisclosed '
                                    'deadlines; reject economics that cannot absorb the remaining work.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Ownership, Property Conditions, and Data Verification',
                 'purpose': 'Reconcile family relationships, recorded ownership, property conditions, and '
                            'research-system limitations before relying on a parcel report or authorizing '
                            'curative work. Preserve the distinction between inherited interests, title '
                            "evidence, mortgage questions, and the family's intended use or retention of "
                            'the property.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Begin with the acquisition deed and family tree rather than assuming an '
                                  'assessor entry resolves ownership.',
                                  'Record source coverage, retrieval limitations, refresh information, and '
                                  'unresolved family evidence alongside every important conclusion.',
                                  'Investigate financial and environmental conditions before authorizing '
                                  'probate work that depends on a viable property outcome.',
                                  'Inspect import matches and paid research settings before finishing an '
                                  'import or incurring avoidable viewing charges.',
                                  'Use the final gate to separate verified findings from remaining title, '
                                  'family, servicing, and data questions.'],
                 'fields': [{'name': 'acquisition_deed_and_owner_search',
                             'type': 'textarea',
                             'prompt': 'Identify the acquisition deed and the owner name used for '
                                       'recorded-document searches. Distinguish ownership documents from '
                                       'debt-related documents, list name-search results requiring review, '
                                       'and explain why searching only the property address would leave '
                                       'the lien investigation incomplete.',
                             'example': 'For a foreclosure-related review, I will identify the owner '
                                        "immediately before foreclosure and search that person's name for "
                                        'recorded liens. Richardson explains that the liens are indexed '
                                        "under the individual rather than the property's address. My notes "
                                        'will therefore retain the searched owner name with the documents '
                                        'returned for review. [Money Making Juggernaut — q95klfFm9mE @ '
                                        '00:02:04]'},
                            {'name': 'complete_family_and_missing_branches',
                             'type': 'textarea',
                             'prompt': 'Build the complete family tree, explicitly asking about deceased '
                                       'siblings and their descendants rather than recording only '
                                       'relatives first mentioned. Identify missing branches, supporting '
                                       'documents still needed, and any supposedly sole-heir statement '
                                       'that remains unverified pending broader family inquiry.',
                             'example': 'I will ask about every relative, including deceased siblings and '
                                        'their children, before accepting a sole-sibling description. '
                                        'Nicoletti recounts a supposed sole sibling eventually disclosing '
                                        'thirteen others. My family worksheet will keep the initial '
                                        'statement separate from the expanded tree so the earlier answer '
                                        'cannot silently control the ownership analysis. [Logan Fullmer — '
                                        'onebNbNQSBM @ 00:08:40]'},
                            {'name': 'shared_ownership_and_family_objective',
                             'type': 'textarea',
                             'prompt': "Describe the family's property objective and the shared ownership "
                                       "interests requiring clarification. Separate an owner's inherited "
                                       'interest from a physically assigned portion of land, and record '
                                       'governance or retention questions without assuming the parcel has '
                                       'already been divided.',
                             'example': 'I will not describe ten owners of 100 acres as automatically '
                                        'owning ten separately identified acres each. The FarmersGov '
                                        'explanation rejects pointing to particular sections that way. My '
                                        'worksheet will describe the shared ownership question first and '
                                        'keep any proposed physical allocation separate from what the '
                                        'ownership evidence currently establishes. [FarmersGov — '
                                        'whDzDrFNADQ @ 00:15:11]'},
                            {'name': 'tax_payment_and_mortgage_questions',
                             'type': 'textarea',
                             'prompt': 'Record who receives the tax bill, whether payments are current, '
                                       'and which foreclosure fees remain unresolved. Identify the '
                                       'mortgage type separately, flagging any reverse mortgage before '
                                       'applying ordinary stay-and-pay reasoning or assuming inherited '
                                       'ownership settles the servicing questions.',
                             'example': 'My property review will distinguish the person receiving tax '
                                        'bills from the actual payment status and total fees. Henderson '
                                        'and Hayyatt describe foreclosure fees that can equal or exceed '
                                        'the taxes and disrupt payment plans. I will therefore leave the '
                                        'financial review open until those additional amounts are '
                                        'identified. [Farm Aid — OODJe43FyEs @ 00:21:06]'},
                            {'name': 'environmental_and_financial_authorization',
                             'type': 'textarea',
                             'prompt': "Summarize the property's environmental and financial investigation "
                                       'before authorizing probate filings. Identify unresolved '
                                       'conditions, their potential effect on the transaction, and the '
                                       'decision that must be made before legal work begins on a property '
                                       'whose economics may fail.',
                             'example': 'I will hold probate authorization until the property '
                                        'investigation is complete rather than assume title repair makes '
                                        "the deal viable. Nicoletti's wetlands example involved a reported "
                                        '$50,000 resolution cost disclosed the day after four waterfall '
                                        'probate filings were authorized. My decision record will keep '
                                        'that property risk ahead of filing approval. [Courtney Fricke — '
                                        'pQwwvYbUYrU @ 00:02:00]'},
                            {'name': 'curative_theory_and_underwriting_review',
                             'type': 'textarea',
                             'prompt': 'State the proposed curative theory and the ownership problem it '
                                       'addresses. Record whether the proposed complaint and order have '
                                       'been put in writing for underwriting review, and identify the '
                                       'remaining uncertainty before treating a probate result as an '
                                       'insurable closing.',
                             'example': 'I will put the curative theory and proposed complaint in writing '
                                        'and ask whether the proposed order will satisfy underwriting. '
                                        'Nicoletti warns that underwriting positions or personnel can '
                                        'change. My review will not equate obtaining a court order with a '
                                        'guaranteed insurable closing while that acceptance question '
                                        'remains unresolved. [Logan Fullmer — onebNbNQSBM @ 01:01:51]'},
                            {'name': 'title_history_coverage_and_retrieval',
                             'type': 'textarea',
                             'prompt': "Record the title-chain report's coverage start date and identify "
                                       'older ownership events that fall outside it. List documents '
                                       'requiring separate retrieval, distinguish available report history '
                                       'from the complete chain, and explain how the coverage gap affects '
                                       'your conclusion.',
                             'example': 'Before relying on a Dallas title-chain report, I will record the '
                                        "demonstrated coverage start of February 11, 2012. Seth's example "
                                        'does not establish that earlier ownership events are absent. I '
                                        "will mark earlier events as outside that report's coverage and "
                                        'identify the additional documents needed rather than declare the '
                                        'chain complete. [REtipster — GfyX48eCbRY @ 00:02:42]'},
                            {'name': 'parcel_import_matching_and_refresh',
                             'type': 'textarea',
                             'prompt': 'Describe how the parcel import was matched and record the match '
                                       'results before finishing. Identify unmatched entries and the '
                                       "dataset's refresh information, then explain why a completed upload "
                                       'or visible map does not alone establish that records attached '
                                       'correctly.',
                             'example': 'I will inspect the import match results before clicking Finish '
                                        "Import. Regrid's presenter warns that finishing too early can "
                                        'leave an effectively empty dataset with nothing attached to '
                                        'parcels. My review will record the matching outcome rather than '
                                        'use the fact that a file uploaded as evidence of successful '
                                        'attachment. [Regrid — VAtPDJ1KDjw @ 00:01:29]'},
                            {'name': 'data_access_cost_and_owner_deduplication',
                             'type': 'textarea',
                             'prompt': "Record the dataset's access limits and the action that triggers "
                                       'any additional charge. Explain how you will narrow results before '
                                       'paid viewing and distinguish multiple property holdings from '
                                       'duplicate owner contacts when preparing the final research or '
                                       'outreach list.',
                             'example': "I will treat the portfolio filter's reported $0.25 per-record "
                                        'surcharge as a viewing cost, not merely an export cost. Seth '
                                        'shows 4,108 results and explains that opening the results incurs '
                                        'the additional charge. My research plan will record that cost '
                                        'trigger before I open a broad premium-filter result set. '
                                        '[REtipster — 9RvXCiHUzlo @ 00:03:16]'},
                            {'name': 'certificate_dependency_and_research_exposure',
                             'type': 'textarea',
                             'prompt': 'Identify the outstanding certificate or family fact capable of '
                                       'displacing the current heir group. Separate signed beneficiaries '
                                       'from established entitlement, record the research already '
                                       'committed, and explain what remains provisional until the decisive '
                                       'evidence has been received and examined.',
                             'example': "I will keep Eileen Holmes's possible-child question open until "
                                        "the certificate resolves it, rather than rely on the cousin's "
                                        "recollection. Amy's wider family research could be displaced by a "
                                        'child. My worksheet will therefore distinguish progress finding '
                                        'maternal relatives from confirmation that the wider family is the '
                                        'correct beneficiary group. [Ancestry — ClFseOLAURA @ 00:27:22]'}],
                 'completion_gate': 'Complete this worksheet only when the deed and family evidence, '
                                    'financial and environmental conditions, underwriting questions, and '
                                    'data limitations are explicitly reconciled. Do not substitute signed '
                                    'heirs for settled entitlement, report coverage for a complete chain, '
                                    'or an uploaded file for verified parcel matches. Record every '
                                    'unresolved dependency and the action required before authorization.'}]}
