# Advanced Agent How-To Operational Manual & System Playbook

## Executive Overview & Corpus Telemetry

- Videos: 189; non-empty successful records: 189.
- Corpus words: 814,088; video duration: 79.95 hours.
- Caption records: 186; supplied storyboard/description reconstructions: 3.
- Six core operational domains connect genealogy, probate, vital-record evidence, recovery, curative title, and skip tracing/title search. Domain 7 supplies the data infrastructure; Domain 8 supplies orchestration.

### End-to-end architecture

Lead → immutable source capture → identity resolution → death/domicile anchor → genealogical proof → estate authority → asset/title/lien verification → net-value underwriting → claim or acquisition packet → adjudication/closing → distribution → preservation.

### Evidence contract

Operational procedures are editorial synthesis, not quotations or legal determinations. Related evidence below each procedure is retrieved by lexical relevance from the entire corpus; retrieval establishes a research lead, not entailment of every procedural sentence. Read the cited excerpt before relying on it. A missing exact rule is explicitly unresolved.
Video statements are dated source claims. Current statute text, court orders and official program instructions govern concrete filings. Numeric thresholds, fees, limitation periods and state-specific deadlines are not invented when absent. This report is generated offline and does not verify current law or live API contracts.
All caption excerpts are contiguous source text and may contain ASR errors. STORYBOARD_OCR entries are non-verbatim supplied reconstructions; no fabricated quote timestamps are assigned.

### Shared case and evidence schema

```text
Case(case_id, jurisdiction, objective, owner_entity_id, asset_id, stage, next_action)
Assertion(assertion_id, subject_id, predicate, value, valid_from, valid_to, confidence)
Source(source_id, video_id, segment_start, record_locator, retrieved_at, sha256)
Support(assertion_id, source_id, source_type, informant, independence_group)
Authority(case_id, representative, capacity, instrument, effective_date, limitations)
Interest(parcel_id, owner_id, numerator, denominator, vesting, instrument_id)
Lien(asset_id, creditor, amount_as_of, priority_basis, release_or_survival_evidence)
Task(case_id, prerequisite_ids, assignee, due_date, status, evidence_required)
```

Unknown is a first-class value, not zero. Preserve competing assertions. Canonical identity changes must be reversible; statutory rules must carry jurisdiction and effective-date ranges.

## Domain 1: Advanced Forensic Genealogy, Descendancy Research & Genealogical Proof Standard

Primary video assignments: [001], [002], [003], [004], [005], [015], [016], [017], [026], [027], [028], [029], [030], [031], [032], [033], [034], [035], [036], [037], [038], [051], [061], [066], [070], [076]

### 1.1 Forward descendancy versus reverse genealogy

**Input:** known ancestor and bounded research question.
**Output:** generation-by-generation lineage ledger.

**Ordered procedure (editorial synthesis):**

1. Start reverse research with the subject and prove each parent-child link independently.
2. For descendancy, enumerate every child of the anchor couple before following grandchildren.
3. Expand one generation at a time with a queue; mark unresolved branches instead of silently dropping them.
4. Record spouses, adopted relationships, half relationships and dates separately from biological links.
5. Stop a branch only with a documented death/no-issue conclusion or an explicit unresolved status.

**Execution and acceptance contract:**

- Persist `generation-by-generation lineage ledger` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [027] [00:01:13](https://www.youtube.com/watch?v=_q7yAh8Anok&t=73s) — “also including information about siblings your parents siblings your grandparents siblings and so on anytime you do that it's going to help you go back another Generation Um so for example your grandfather's death certificate might not list his mother's made name but his sister's death certificate might and so that's why it's always really important to trace siblings as well now that's traditional ancestry research you work your way back a generation at a time in descendancy research you pick an ancestor and you trace all of that ancestor's descendants so um their children their grandchildren”
- [028] [00:00:10](https://www.youtube.com/watch?v=rKKDh07PmVc&t=10s) — “Hi everyone, Christa Cowan here with another episode of the barefoot genealogologist. Today we are talking about post 1940 descendancy research. Now let's start first with the concept of descendancy research. Ancestry research is where you try to identify your parents and your grandparents and your great-grandparents and so on back through time. Always looking for kind of that pedigree view of a family. Descendancy research is where you pick a particular ancestor and identify all of their children and their grandchildren and their great-grandchildren and so on down to the current day. Now, here in the United”
- [026] [00:12:13](https://www.youtube.com/watch?v=TVIHQUFpkjk&t=733s) — “ancestors descendants well we define descendants in a lot of different ways and the this is another reason why the the descendants II research has turned out to be a challenge a greater challenge than doing ancestral research back through your ancestral lines first of all you have relationships that are biological so those are the the fundamental biological relationships where a child has one parent one father and one mother and that's natural and no matter how many different whatever you want to call it alternative marriage arrangements or lifestyles that we have out there the reality as far as we have”
- [031] [00:09:22](https://www.youtube.com/watch?v=VbgMCP7bKcs&t=562s) — “it's not that important to resolve and know the exact date of birth um go ahead and give a brief explanation um in your software or in your report wherever you keep track of your family history and then move on so now let's move on to some more complex conflicting evidence we can come across in our research the first is relationships just like today our ancestors families often included complex relationships of many types including biological relationships adopted and that could be formally adopted or informally illegitimacy half relationships step relationships and remarriages so we”

### 1.2 Collateral lines and brickwalls

**Input:** unresolved parentage or migration.
**Output:** hypothesis table with exclusion evidence.

**Ordered procedure (editorial synthesis):**

1. Build a sibling set from censuses, probate distributions and household records.
2. Track witnesses, neighbors, sponsors and executors as an associates cluster.
3. Search each sibling in the destination jurisdiction and compare origin locations.
4. Test the proposed relationship against contradictory ages, occupations and simultaneous residences.
5. Write competing hypotheses and the next record that could discriminate them.

**Execution and acceptance contract:**

- Persist `hypothesis table with exclusion evidence` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [036] [00:31:00](https://www.youtube.com/watch?v=FPaiNw1Z1b0&t=1860s) — “newspapers and obituaries for marriage and maiden names biographies censuses cemeteries Church records and family Bibles family histories land and property records the military newspapers nobility listings personal correspondents probate records school records and vital records for OCC occupations you'd be talking about business directories that list company officials and employees the censuses city directories a crisscross civil registration court records immigration military newspapers obituaries and probate records for parents children and other family members most of these are exactly the same but you also have biographies land and property records the Naturalization and citizenship”
- [066] [00:25:51](https://www.youtube.com/watch?v=MMe67JLgS08&t=1551s) — “the word under place or the the search under place is Germany and it when I hit update it brought up two different record groups immigration and migration a history with two records it also brought brought up Germany migration with one record and if you'll notice if you click on the drop down arrow next to um next to the record field collection field it will give you the specific items in the library that you can access and then I just really quickly went through or went back to my original place because I wanted to”
- [033] [00:25:24](https://www.youtube.com/watch?v=JIUMf1OHaY0&t=1524s) — “And I know he lived for a good long time because he's my grandpa, so I would not have been here without him. So doing this is what we call correlating evidence uh so this this standard of researching teaches us that we can never rely on evidence from one record alone we need to find evidence in multiple records and compare them against one another. Do they say the same thing? Does each record have different information? And then if they differ you need to decide and determine the credibility of each of the”
- [038] [00:41:20](https://www.youtube.com/watch?v=VwfAeN31cTw&t=2480s) — “supporting this negative evidence that james had died after 1801 and when we searched the probate records of all of the county where the older james and his children had lived we find no record of this older james in any of those counties including saratoga where galway is so though again the absence negatively supports the conclusion that james died in saratoga county after he was no longer able to appear to in church the second use of negative evidence is to help us eliminate competing hypotheses a process of elimination here's another example from bill”

### 1.3 GPS and conflicting evidence

**Input:** all competing assertions about one event.
**Output:** proof argument and source matrix.

**Ordered procedure (editorial synthesis):**

1. Define reasonably exhaustive research by jurisdiction, period and surviving record classes.
2. Cite repository, collection, volume, page/image, record identifier and access date.
3. Separate original versus derivative source from primary versus secondary information and direct versus indirect evidence.
4. Assess each informant’s opportunity to know; do not decide by majority vote among copied trees.
5. Resolve conflicting dates with event proximity, independent corroboration and calendar context.
6. Write a reasoned conclusion preserving unresolved contradictions.

**Execution and acceptance contract:**

- Persist `proof argument and source matrix` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [035] [00:11:51](https://www.youtube.com/watch?v=7Jn_XMUozo0&t=711s) — “start to get into discussions about analyzing sources. Here's some of those words: primary, a primary document versus a secondary source or document, evidence as a as a term that's used about information that you obtain from historical records, original versus derivative, an original document versus a derivative document, sort of the same as primary versus secondary, but these are different terms that are used. Sometimes you'll hear that you need to consider whether or not this is correct beyond a reasonable doubt or clear if this evidence is clear and convincing or whether it is based on a”
- [030] [00:18:47](https://www.youtube.com/watch?v=tljNDoj74TI&t=1127s) — “So in the same document, the wife has given primary and secondary information and there are 3 different informants so we can look at each piece of information separately and determine which one answers our research question and then whether or not that was primary secondary information. All right, moving on to that 3rd column, the last column, evidence. Evidence is how we use information items so evidence does not exist without a research question. It has to apply or answer a research question. Evidence can be direct. Indirect or negative. So direct evidence answers a research question directly.”
- [036] [00:04:07](https://www.youtube.com/watch?v=FPaiNw1Z1b0&t=247s) — “proof statement is subject to being re-examined when new evidence arises this next slide talks about the different types of evidence direct evidence this refers to the source of information example if the birth information came from a birth certificate then it would be direct evidence indirect evidence this is information that requires corroboration it provides enough detail to enable you to form a hypothesis and when combined with other evidence will allow you to reach a reasonably reliable conclusion an example of this there are three of them you can't find a birth certificate for your grandfather but you”
- [031] [00:00:03](https://www.youtube.com/watch?v=VbgMCP7bKcs&t=3s) — “\[Music\] hello my name is melissa finley and this is the presentation called dueling dates and fact fights resolving evidence conflicts part one the fourth element of the genealogical proof standard created by the board for certification of genealogists states that we must make a resolution of conflicting evidence to reach a sound conclusion in our genealogical research but what is conflicting evidence the law dictionary website provides this definition conflicting evidence is evidence that is taken from different sources that contradict each other in this class part one of two of dueling dates and fact fights”

### 1.4 Same name, different person

**Input:** candidate identities.
**Output:** identity resolution decision.

**Ordered procedure (editorial synthesis):**

1. Normalize names but retain exact spellings and aliases.
2. Compare time intervals, addresses, spouses, children, occupations and associates.
3. Reject impossible overlapping life histories; permit uncertain dates as intervals.
4. Require independent discriminators beyond a shared name before merging.
5. Keep a reversible merge ledger with provenance and rejected candidates.

**Execution and acceptance contract:**

- Persist `identity resolution decision` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [001] [00:43:34](https://www.youtube.com/watch?v=9Q4qYeK5DTg&t=2614s) — “get married and watch out for the same name same person trap now I got into one of these that was just absolutely complicated basically what happened was that I found a person and in England and it turned out that I kept coming up with different wives names I kept coming up with different children's names they weren't they were all the wise name were exactly the same except the children all were always weren't the same and I kept working on it finally it occurred to me that I was probably dealing with two different people here”
- [030] [00:06:16](https://www.youtube.com/watch?v=tljNDoj74TI&t=376s) — “independent information this probably all came from the same purpose for the same from the same person for the same purpose. All right. Now moving on, if we take that same death certificate and we add in a World War 2 draft and my grandfather's birth certificate. Then these are independent sources because they were all created at different times for different purposes by different people. I'm gonna grab a drink really quick. Sorry, much better. OK. Now, another thing that I want to drill into your head. Is that the quality of a source is more important than the quantity.”
- [036] [00:31:00](https://www.youtube.com/watch?v=FPaiNw1Z1b0&t=1860s) — “newspapers and obituaries for marriage and maiden names biographies censuses cemeteries Church records and family Bibles family histories land and property records the military newspapers nobility listings personal correspondents probate records school records and vital records for OCC occupations you'd be talking about business directories that list company officials and employees the censuses city directories a crisscross civil registration court records immigration military newspapers obituaries and probate records for parents children and other family members most of these are exactly the same but you also have biographies land and property records the Naturalization and citizenship”
- [090] [00:07:35](https://www.youtube.com/watch?v=MVCNlj7HQBQ&t=455s) — “you get this part right, the county has no real reason to reject your claim. But unfortunately, this is where the little stuff sinks people. They send a plain photocopy of the deed and they get rejected. Or, they send an ID where the name doesn't quite match the actual name on the deed. And that gets rejected. Or, they pull up a claim form that they saved 6 months ago, not knowing that the county quietly changed their entire protocol. And that will eventually get you rejected. None of these feel like a big mistake, but the county does not”

### 1.5 Indirect and negative evidence

**Input:** missing or indirect record.
**Output:** negative-search log.

**Ordered procedure (editorial synthesis):**

1. Document the record’s coverage and whether the person should have appeared.
2. Distinguish a failed keyword query from an inspected complete record set.
3. Combine independent indirect assertions into a written logical chain.
4. Treat destroyed records and incomplete indexes as absence of evidence, not negative proof.
5. Record alternative explanations and a falsification search.

**Execution and acceptance contract:**

- Persist `negative-search log` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [038] [00:27:47](https://www.youtube.com/watch?v=VwfAeN31cTw&t=1667s) — “assemblage to strengthen the case about the identity of josiah's daughter's mother mary leonard before we look at more examples of negative evidence let's look at what negative evidence is not more misconceptions that some of you might need to unlearn and this is in your syllabus material so the absence of records is not negative evidence an unproductive search that yields no genealogical genealogically useful information is not negative evidence and direct or indirect evidence of a non-relationship is not negative evidence let's look at some examples of not negative evidence the absence of information an absence”
- [033] [00:22:31](https://www.youtube.com/watch?v=JIUMf1OHaY0&t=1351s) — “So negative evidence is the absence of information that you would expect to find in the record. So a really good example of this is a census record. If a person wasn't listed on the record that you think should have been there, that's negative evidence that perhaps that person. Died Moved somewhere else, was living elsewhere, got old enough to get married and leave the household. So that's negative evidence that you can use in your research when you're trying to decide and learn the story of your ancestors. Now you have to be really careful when you're making assumptions about negative evidence”
- [030] [00:11:32](https://www.youtube.com/watch?v=tljNDoj74TI&t=692s) — “We have information that can be primary, secondary, or indeterminable or unknown, and we have evidence which is direct, indirect, or negative. We're gonna talk about each of these in detail. All right, so first off, we start with the source. Your source is the container. This is what holds the information. So this can be an original record, derivative record or authored work. Sources are published, they're unpublished they're artifacts, photographs, registers, websites, anything where we get information, but they are not things like finding aids or indexes or search engines that help us find”
- [127] [00:01:29](https://www.youtube.com/watch?v=W0wjEVX_Jxw&t=89s) — “faster way to make sure you've got the coverage you need to protect you and no more lengthy policies either. Once you're set up, you're billed monthly and prorated \[music\] by the day for however long your policy is active. It's powered by MSI, the third largest independent MGA with 1.5 million customers and more than \[music\] $1 billion in cumulative premiums written. Get set up today in about 2 minutes at myinvestorinsurance.com/fuel. Welcome back to another episode of The Real Estate Pro Show. I'm your host, Isa Hanna, and today I have a treat. I have”

### 1.6 Kinship degree and distribution

**Input:** proved common ancestor and descent paths.
**Output:** kinship chart plus jurisdiction-specific share worksheet.

**Ordered procedure (editorial synthesis):**

1. Count parent-child edges from each person to the nearest shared ancestor.
2. For collateral cousins with depths a and b at least two: cousin degree=min(a,b)-1; removal=abs(a-b).
3. Depths 2/2 yield first cousins; 3/3 second cousins; 4/4 third cousins; 2/3 first cousins once removed.
4. Handle ancestors, siblings, half relationships and pedigree collapse explicitly rather than forcing the cousin formula.
5. Compute per stirpes and per capita shares only under the applicable jurisdiction’s actual representation rule; do not infer the statutory variant from the label.
6. Use rational fractions and verify distributions sum to one after spouse and other priority interests.

**Execution and acceptance contract:**

- Persist `kinship chart plus jurisdiction-specific share worksheet` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [026] [00:20:47](https://www.youtube.com/watch?v=TVIHQUFpkjk&t=1247s) — “than one person who was a descendant of who we could prove was a cousin in a sense because of DNA testing and then we traced that cousins ancestry back and it turns out that we both have a common ancestor the same name and that common ancestor is then identified in other words we've been able to indicate which of the common ancestors of the people with the same name as a common ancestor are the right one so this comes to be it becomes one of the of the other tools that we have is doing this descendency”
- [028] [00:04:07](https://www.youtube.com/watch?v=rKKDh07PmVc&t=247s) — “fourth cousins might be so that you can invite them to be tested to help prove those connections. Now, I don't know about you, I know all of my first cousins personally. Um, I know most of my second cousins. Uh, that's because both of my parents have maintained fairly close relationships with their first cousins and so it is only natural that I know uh many of their children. But we start getting to that third cousin range and most of us don't know a lot about those people. And so descendency research helps us figure”
- [008] [00:04:13](https://www.youtube.com/watch?v=rR4YCKGVNmg&t=253s) — “three years I've been with the holding company uh for PBI for over 10 years um Benny search is a product that we've had for almost 10 years now but with a heavier emphasis within the last five years as more and more clients have asked for this product um we've built out a robust processing system to handle Benny search that we refined and continue to refined uh to this day with the with the goal of finding at least one first degree relative first degree relative being a parent a child a spouse or a sibling”
- [027] [00:01:55](https://www.youtube.com/watch?v=_q7yAh8Anok&t=115s) — “their great-grandchildren and so on in this case you know you are one of those people in that line so for example this is a uh let's see a paternal um father's looks like a paternal grandmother's line that gets you up to this common ancestor here and so you have these um other people included so you're tracing not just the siblings of your ancestor but you're also tracing their children as well and so you end up with lots of second and third and fourth cousins now there are a lot of reasons why would want to do”

### 1.7 DNA plus paper trail

**Input:** authorized match data and documented pedigree.
**Output:** DNA hypothesis worksheet.

**Ordered procedure (editorial synthesis):**

1. Use DNA as evidence of a relationship hypothesis, not an automatic legal heir determination.
2. Cluster matches and compare plausible shared ancestors with documentary branches.
3. Account for endogamy, pedigree collapse, half relationships and multiple shared lines.
4. Track test type and uncertainty; avoid treating shared centimorgans as a unique relationship.
5. Resolve the documentary lineage independently before adding an heir to a distribution schedule.

**Execution and acceptance contract:**

- Persist `DNA hypothesis worksheet` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [031] [00:09:22](https://www.youtube.com/watch?v=VbgMCP7bKcs&t=562s) — “it's not that important to resolve and know the exact date of birth um go ahead and give a brief explanation um in your software or in your report wherever you keep track of your family history and then move on so now let's move on to some more complex conflicting evidence we can come across in our research the first is relationships just like today our ancestors families often included complex relationships of many types including biological relationships adopted and that could be formally adopted or informally illegitimacy half relationships step relationships and remarriages so we”
- [021] [00:02:31](https://www.youtube.com/watch?v=KpQQ3n37XXM&t=151s) — “attack it from different fronts until something cracks first i started with a research log to identify him and others of his same surname in texas i started with a record type category research log two i made a data list of men of that surname living in texas registered to vote in 1867 and i compared it with censuses from 1860 through 1880 and tax lists i started a pedigree of autosomal dna matches and their comparative relationships i have a spreadsheet of autosomal dna matches with url links and color-coded to the leads method”
- [032] [00:13:56](https://www.youtube.com/watch?v=Ep2zENQQZ1k&t=836s) — “sense now another strategy that you should use in order to resolve conflicting evidence is to compare and contrast until you can create a hypothesis or a proof argument to resolve the conflict so in this case we have mrs donahue i like this donahue family they have a lot of conflicts for me to resolve um i wanted to find out her time her date of death and i found i looked in a kentucky death index which should have been kept during the time period in which she died kentucky was a little sporadic about”
- [038] [00:30:36](https://www.youtube.com/watch?v=VwfAeN31cTw&t=1836s) — “but it says nothing about maddie and her siblings that we can use genealogically descendants of julia greenfield do not appear in my dna match list i'm related to many people who do not appear in my dna match list this is just another absence that provides no useful genealogical information we can use negative evidence in two ways we'll start with uh the first use which is to establish aged status death or removal and let's start with a simpler example this evidence is from research by william lichman it's cited on the slide and also your”

### 1.8 Unindexed FamilySearch images

**Input:** place, date and record class.
**Output:** image-level citations and research log.

**Ordered procedure (editorial synthesis):**

1. Search the Catalog by historical jurisdiction rather than only by surname.
2. Inspect collection descriptions, coverage, access restrictions and film/image group identifiers.
3. Locate internal indexes and navigate volume/page sequences in image-only collections.
4. Capture the image identifier, stable link, volume, page and neighboring context.
5. Transcribe critical names literally and preserve uncertain characters.

**Execution and acceptance contract:**

- Persist `image-level citations and research log` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [066] [00:15:01](https://www.youtube.com/watch?v=MMe67JLgS08&t=901s) — “search you can make in the catalog for example I'll show you later about my search for migrant workers that's something that you know we can't often find just by looking for names and places of ancestors then you'll notice at the bottom well it's kind of the middle of this but the bottom of the area it says search for call number film fish group number Etc Image Group number and those are handy when you you may have looked at a record say previous to This urrent research session and you you would have noticed that a certain film”
- [006] [00:03:32](https://www.youtube.com/watch?v=lOmly79G2Tk&t=212s) — “docket volume four and five. I'm interested in docket 5. So I'm going to go ahead and click on this. It takes me to the very first page of that particular set of images. What I need to do is use the film strip navigation at the bottom or use the page selection and navigate to that page. Now remember I was interested in docket 5 page 231. So using a combination of the page selection and the filmrip navigation I can navigate ahead to the page I'm interested in. Using the combination of the filmrip”
- [058] [00:23:46](https://www.youtube.com/watch?v=bcOlApV2Fng&t=1426s) — “an example of an index page I've got some names and then some page numbers okay so I can jump to any one of those images then using this film strip and and keep in mind that the image number in this case I'm on image number 50 does is not the same as the page number so here I'm on page 20 and 21 of the book but I'm on image 50 and so what that tells me is that I've got two pages per image and so for example if I'm looking for image 56 I'm going to want to jump”
- [054] [00:25:02](https://www.youtube.com/watch?v=Gwcf300h1sA&t=1502s) — “catalog again for film 17355 I found it on the same page where the index film was listed once again we scroll through the film and find another image 576 after that page I find that there is another index listing Thomas Maris and showing that his will is found on page 508 so there is an index right before the wills I scroll through the film once again and here on page 508 at the top and the will for Thomas Maris here is an enlarged image of the will here is the transcription of the”

### Domain evidence workbench

The following source-specific evidence cards expose primary assigned videos without treating lexical matches as verified legal rules.

#### [001] Finding Your Ancestors' Descendants - James Tanner (26 Feb 2023)

- Source: https://www.youtube.com/watch?v=9Q4qYeK5DTg
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [001] [00:00:00](https://www.youtube.com/watch?v=9Q4qYeK5DTg&t=0s) — “welcome to this Sunday's virtual class in the Brigham Young University's family history library at Provo Utah today's class is finding your ancestors descendants our presenters James Tanner we appreciate his preparation and willingness to share his knowledge on this subject we'll now turn the time over to James well we are going to go about look about finding your ancestors descendants and this particular presentation is going to be based primarily on familysearch.org it is one of the few programs that I'm aware of that will show you all your descendants from back to whatever living”
- [001] [00:35:05](https://www.youtube.com/watch?v=9Q4qYeK5DTg&t=2105s) — “getting all their descendants so now here's some way to start the first one you start is with people who who have few or no sources and how do you know that well family search tells you that so if you click on there it'll tell you if I clicked on this Mary Bryan in 1817 and she has one source another way that that happens is uh through some other things that we'll look here here so what are the other things that I would look here I don't necessarily need to do all these people”

#### [002] What Do I Enter Into My Family Tree? Resolving Conflicting Evidence \| Ancestry

- Source: https://www.youtube.com/watch?v=ElrY5ALsx1Y
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [002] [00:09:24](https://www.youtube.com/watch?v=ElrY5ALsx1Y&t=564s) — “need to do more research first so um I'm a big fan you can see up here across the top of my web browser I'm a big fan of tabs um I use extra tabs a lot and so um first of all what I did was I've actually looked at the record itself never rely solely on this index page for your information always if there is an original record attached always view that original record because sometimes oftentimes there's additional information there's more context there's um there's more information there's more accurate information so I'm going to”
- [002] [00:33:05](https://www.youtube.com/watch?v=ElrY5ALsx1Y&t=1985s) — “accurate information maybe you need to bookmark those records um and contact a County Courthouse maybe you need to go look in a newspaper or contact a local library maybe there's more information that you need before you can make the decision about whether or not all these records are for your person and then whether you DET when you decide what to put into your tree um about them in order to help you move to the next step so for us and John Wright the next step of course is going to be to trace him”

#### [003] When Paper Trails Meet DNA: The Full Conversation with Professor Turi King and Neil Fraser

- Source: https://www.youtube.com/watch?v=LZWYe4jFvZM
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [003] [00:06:36](https://www.youtube.com/watch?v=LZWYe4jFvZM&t=396s) — “&gt;&gt; Okay. Okay. It's like \[laughter\] no. No. So, I I mean um my kind of first in probably the the first time it was ever kind of used in a in a genealogy case was actually DNA fingerprinting when it was first invented. So this is professor Sir Alec Jeff back in 1984 uh discovers that you can uh use DNA to identify individuals and close relatives. And when people think of DNA fingerprinting the first thing they think of is uh the police shows and um usually that they take a DNA sample and it pops out about”
- [003] [00:38:19](https://www.youtube.com/watch?v=LZWYe4jFvZM&t=2299s) — “policies saying they would never give out that DNA to law enforcement unless they were ordered to by a court. Um they did. It caught someone who absolutely should have been locked up. That case may never happen today because that data is now fully locked up and fully locked away. So you can't do it. So &gt;&gt; you heard it here first. We're defending murderers &gt;&gt; because you can. So you can use Jed match and you can use family tree DNA. You can you apply because I'm I'm working on cases now. So this is”

#### [004] HeirSearch \| Consanguinity Chart Walk-Through

- Source: https://www.youtube.com/watch?v=aOXjjN53MT8
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [004] [00:00:47](https://www.youtube.com/watch?v=aOXjjN53MT8&t=47s) — “consanguinity chart this chart outlines the relation between a decedent and their family members each box on the chart has a generational title and a number representing the degrees of consanguinity or relationship to begin reading the chart place the decedent let's call him john smith in the blank box the first step is determining if john has a living spouse and lineal descendants this is established by following the line directly below him to identify his children grandchildren and great-grandchildren if john smith has no living spouse or lineal descendants we move on to the next level of the”
- [004] [00:02:03](https://www.youtube.com/watch?v=aOXjjN53MT8&t=123s) — “we call this a level two search as it begins with his grandparents who are two degrees of consanguinity away his aunts uncles and first cousins on both the paternal and maternal sides of the family are included in this search as well as his first cousins one time two times or three times removed when state law requires the higher we go up the consanguinity chart the further back we go into the decedent's genealogy and the more complex the family tree becomes each level up the chart requires that the previous level of search has proven”

#### [005] TGP - 13 Leslie Lawson - Forensic Genealogist

- Source: https://www.youtube.com/watch?v=R5XtgGL0gkQ
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [005] [00:15:10](https://www.youtube.com/watch?v=R5XtgGL0gkQ&t=910s) — “tough do you ever feel like that or did it come easier to you I've always enjoyed genealogy and I never felt it was too hard but it always was where am I gonna get another client I need more clients I need more business rolling in and when the economy tanked my business went down because here where I live it's very expensive to file a probate and I knew many people were having to choose between paying for food that month or paying the rent that month versus paying for a probate so”
- [005] [00:21:39](https://www.youtube.com/watch?v=R5XtgGL0gkQ&t=1299s) — “client would be you know what would the end result be most of my clients are attorneys across the United States they honestly don't have any idea what we need so usually my response to them is send me everything you have I want a copy of every will every vital record document I need to know what you know and then I can recreate these family groups some attorneys try to help me by telling me oh you don't need that well yes I need all the documents I need to know everything you know because they don't”

#### [015] Crafting Source Citations in Your Ancestry Tree \| Ancestry

- Source: https://www.youtube.com/watch?v=7M3XZfN7814
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [015] [00:10:23](https://www.youtube.com/watch?v=7M3XZfN7814&t=623s) — “citations helps me to analyze the the sources that I'm using so that I come to better conclus conclusions about who's in my tree about the information and that all helps ensure that I'm climbing my own tree and not somebody else's that I haven't just attached some record that has nothing to do with my person so creating this Source um is is an important step now the repository here at the bottom of this Source form is also important so this is where you're going to list I'm going to use a book as an example again because it's”
- [015] [00:23:18](https://www.youtube.com/watch?v=7M3XZfN7814&t=1398s) — “my tree that still need to be cleaned up and I find that as I go back and revisit or redo some of those citations I discover new evidence that I miss the first time around because I wasn't as meticulous in crafting those citations as I am now so so don't be too intimidated by it just jump in and get started and you'll find that you'll um get better at as as time goes by if you have questions about how to craft Source citations um one of the things I would encourage you to do if you if you can is”

#### [016] Peeling Back the Layers: Citing Sources from Online Materials, Part 1

- Source: https://www.youtube.com/watch?v=DUAbGD8rVzA
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [016] [00:00:01](https://www.youtube.com/watch?v=DUAbGD8rVzA&t=1s) — “hello and welcome to peeling back the layers citing sources from online materials part one my name is diana elder and you can reach me at diana familylocket.com or find more about me on my website familylocket.com the content of this video as well as the thoughts views and opinions expressed herein belongs solely to the creator and do not necessarily reflect the views of family search international and roots tech as we talk about source citations today let's stop for a minute and just think about where source citations fit into our entire genealogy research”
- [016] [00:10:01](https://www.youtube.com/watch?v=DUAbGD8rVzA&t=601s) — “reproduction of the source and i'll show you some examples of that so how do we go about creating a source citation well step number one is simply to understand the source we need to know what we're citing it's not enough just to look at a record and to try to write something up really quickly we need to make sure we thoroughly understand what it is we're trying to create a sort a citation for so we're going to use the example of the world war one draft registration card for dot keras and this is found on”

#### [017] Peeling Back the Layers: Citing Sources From Online Materials, Part 2

- Source: https://www.youtube.com/watch?v=KtpN2Ws9PA4
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [017] [00:00:01](https://www.youtube.com/watch?v=KtpN2Ws9PA4&t=1s) — “welcome to peeling back the layers citing sources from online materials part two my name is diana elder i'm an accredited genealogist and you can find more about me on the familylocket.com of this video as well as the thoughts views and opinions expressed herein belongs solely to the creator and do not necessarily reflect the views of family search international and roots tech as i mentioned in part one of this series source citations falls in the genealogy research process as a critical part and as we have created an objective for our research”
- [017] [00:15:51](https://www.youtube.com/watch?v=KtpN2Ws9PA4&t=951s) — “archives again there's no need to be repetitive if we've got the basic information in one of the layers then we don't need to add it to the other layer let's stop and think about punctuation punctuation is really important in our citations and you may get confused you may think why do i need to bother this is just one step i don't want to worry about but it's really pretty simple and once you get used to it you get the hang of it and it becomes second nature so let's just go through these and i'm”

#### [026] Basic Series: Part 3 - Beginning Descendancy Research - James Tanner

- Source: https://www.youtube.com/watch?v=TVIHQUFpkjk
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [026] [00:07:54](https://www.youtube.com/watch?v=TVIHQUFpkjk&t=474s) — “connections but that in those days of mainly paper-based genealogy doing genuinely doing death-sentence research involved a tremendous effort and a lot of work first of all descendancy worked only with near relatives if you started off into trying to find the descendants of your of your ancestors that got to be extremely complex the the main reason was because you it was you knew for example let's let's gonna kind of IgG tell you how this works if you if you knew your your father for example some people don't but let's assume you do and”
- [026] [00:51:52](https://www.youtube.com/watch?v=TVIHQUFpkjk&t=3112s) — “family history guide that I mentioned the FH guide calm has detailed step-by-step instructions on how to do descendancy research so you get into the descendents each section of the family history guide for the Family Search program and it will show you step-by-step take you through the projects and the goals and the choices that will let you progress and understand how to do this very very just exactly what I just did in showing how to find a family on them in the program okay so there are videos and handouts that are connected to the family history”

#### [027] Descendancy Research \| Ancestry

- Source: https://www.youtube.com/watch?v=_q7yAh8Anok
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [027] [00:20:14](https://www.youtube.com/watch?v=_q7yAh8Anok&t=1214s) — “still need to go look for um a death record for her possibly a cemetery record if I can locate that maybe an obituary in a local newspaper there in New Jersey so lots of different things I need to locate her marriage record lots of Records still missing here and I can tell that just at a glance because I have made notes about every record I've found as well as just attaching that record it's just a quick add a glance way to tell what I've discovered what I haven't what I still need to look for”
- [027] [00:21:09](https://www.youtube.com/watch?v=_q7yAh8Anok&t=1269s) — “search over and over sometimes and you think this is so familiar I think I've looked through all of these search results before um but if you keep notes of those negative findings it'll help you a little bit now one of the unique things about um a descendency research as compared to ancestry research when you're doing ancestry research you know you're always looking for two parents no matter what you're always looking for a father and a mother uh and that make that's a little comforting because you know there's information or hope there's”

#### [028] Post-1940 Descendancy Research \| Ancestry

- Source: https://www.youtube.com/watch?v=rKKDh07PmVc
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [028] [00:00:10](https://www.youtube.com/watch?v=rKKDh07PmVc&t=10s) — “Hi everyone, Christa Cowan here with another episode of the barefoot genealogologist. Today we are talking about post 1940 descendancy research. Now let's start first with the concept of descendancy research. Ancestry research is where you try to identify your parents and your grandparents and your great-grandparents and so on back through time. Always looking for kind of that pedigree view of a family. Descendancy research is where you pick a particular ancestor and identify all of their children and their grandchildren and their great-grandchildren and so on down to the current day. Now, here in the United”
- [028] [00:10:28](https://www.youtube.com/watch?v=rKKDh07PmVc&t=628s) — “introductory information about why we do descendency research, where to start doing that descendency research, what exactly that means. So let's talk about um that post 1940 wall and where we go. Now, of course, the first thing you want to do is make sure that you have all the information solid up to 1940. So, from whatever ancestor down to the 1940 census, make sure you've collected all that information and all those census records and use other records as well. Uh, however, once you get past 1940, there are various privacy laws that come into play. Now, the federal”

#### [029] Tracing Descendants: An Essential Strategy to Solve Your Brickwall

- Source: https://www.youtube.com/watch?v=FA43rRoIJV8
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [029] [00:11:51](https://www.youtube.com/watch?v=FA43rRoIJV8&t=711s) — “didn't have any children she became the ultimate relative i want because she in her will identified members of the family that i had never had any idea existed and then helped me to make a connection for the kingsley family so it's worth spending some time to trace that particular descendant on that particular part of the family let's look at another example where tracing descendants is absolutely key so this individual is william h you might remember the shoops because you saw that tree of john w shoop in the beginning and i mentioned”
- [029] [00:16:09](https://www.youtube.com/watch?v=FA43rRoIJV8&t=969s) — “children including john w shoop so just to recap william h never married he never had any children and yet through researching him and finding another sister and then tracing the descendants of that sister i was able to find a copy of a document that is likely the only place where that family's vital events are recorded on one piece of paper it's an absolute treasure in something that helped to solve a huge brick wall in the family but again would never have been able to be found had i not spent some time working”

#### [030] Analyzing Evidence: A Research Game Changer

- Source: https://www.youtube.com/watch?v=tljNDoj74TI
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [030] [00:04:47](https://www.youtube.com/watch?v=tljNDoj74TI&t=287s) — “So finding the original is important and when we're doing research in databases such as ancestry or Find My Past, quite often the digital image of the original will be attached so it's really easy to just click on that image and look at it and read it. Sometimes we have to take extra steps. We have to go find the original, but it's always worth the effort, so make sure that you're making that effort. All right, finally, you need to find as many independent sources as you can. And I want to explain independent sources a little bit better.”
- [030] [00:12:20](https://www.youtube.com/watch?v=tljNDoj74TI&t=740s) — “that information. Now a record documents an action or an event. So an original record is not based on any prior records. This is the first time something has been written down. A derivative record is copies or it's created from the prior record, so this is gonna include things like transcriptions, abstractions, translations or databases where we get our information. Now the more times that something is copied, the more chances there are to introduce error so that's why we want to always look for the original because the original is the first time it was written down and sometimes after it's been copied those”

#### [031] Dueling Dates and Fact Fights: Resolving Evidence Conflicts, Part 1

- Source: https://www.youtube.com/watch?v=VbgMCP7bKcs
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [031] [00:00:03](https://www.youtube.com/watch?v=VbgMCP7bKcs&t=3s) — “\[Music\] hello my name is melissa finley and this is the presentation called dueling dates and fact fights resolving evidence conflicts part one the fourth element of the genealogical proof standard created by the board for certification of genealogists states that we must make a resolution of conflicting evidence to reach a sound conclusion in our genealogical research but what is conflicting evidence the law dictionary website provides this definition conflicting evidence is evidence that is taken from different sources that contradict each other in this class part one of two of dueling dates and fact fights”
- [031] [00:10:08](https://www.youtube.com/watch?v=VbgMCP7bKcs&t=608s) — “sometimes come up with conflicting evidence because we don't yet understand the true nature of the relationship between two people so we need to analyze more or find more evidence to figure out what the nature of their relationship is let's talk for a minute about the historic use of the terms senior and junior for the most part today they are used to denote a parent-child relationship however historically this was not always the case often men of the same name in a community would use these terms to distinguish between themselves so the older one would say he was william”

#### [032] Dueling Dates and Fact Fights: Resolving Evidence Conflicts, Part 2

- Source: https://www.youtube.com/watch?v=Ep2zENQQZ1k
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [032] [00:00:07](https://www.youtube.com/watch?v=Ep2zENQQZ1k&t=7s) — “\[Music\] hi i'm melissa finley welcome to part two of dueling dates and fact fights resolving evidence conflicts in part one of this presentation we discuss that the fourth element of the genealogical proof standard is the resolution of conflicting evidence we defined conflicting evidence as evidence from different sources that contradict each other and we discussed where and why we might find conflicting evidence in our research now let's discuss some solutions and examples to resolve evidence conflicts first and foremost check your assumptions we all go into our research with certain assumptions and it might cause us to skip a key”
- [032] [00:17:14](https://www.youtube.com/watch?v=Ep2zENQQZ1k&t=1034s) — “20th and then the cause of death on the register was psoas abscess while the article said era syphilis so which one was it and then of course we have the fact that her first name was never stated in either record she was just donahue and then mrs donohue and no first name but i i thought that you know i think i can resolve these conflicts by really just comparing and contrasting and writing it up and that is my last strategy for you i think every time that you have conflicting evidence”

#### [033] Extracting Evidence: Strategies for Analyzing Genealogical Sources

- Source: https://www.youtube.com/watch?v=JIUMf1OHaY0
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [033] [00:08:11](https://www.youtube.com/watch?v=JIUMf1OHaY0&t=491s) — “time of the event, but we don't always get that. In fact, quite often we don't have that ideal situation. So we can use what's called indirect evidence from records and correlate that with other records to come to our conclusions. Uh, in genealogical terms you might hear these questions referred to as questions about the source, questions about the information or the informant for the info for the record, and the evidence we're talking about direct or indirect evidence. So if you see those terms, that's what those are referring to. As we are doing our evidence analysis, we need to make sure that we are always guided by a”
- [033] [00:25:24](https://www.youtube.com/watch?v=JIUMf1OHaY0&t=1524s) — “And I know he lived for a good long time because he's my grandpa, so I would not have been here without him. So doing this is what we call correlating evidence uh so this this standard of researching teaches us that we can never rely on evidence from one record alone we need to find evidence in multiple records and compare them against one another. Do they say the same thing? Does each record have different information? And then if they differ you need to decide and determine the credibility of each of the”

#### [034] From Questionable to Credible: Analyzing and Verifying Genealogical Sources

- Source: https://www.youtube.com/watch?v=R50W1KDrRPw
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [034] [00:02:27](https://www.youtube.com/watch?v=R50W1KDrRPw&t=147s) — “the people who assembled these had. And then how many of you have found a find a grave memorial that has information that you've never seen before? So what do you do when you see one of these types of questionable sources? Well, I want to outline for you the steps I take to verify these sources when I come across them. There are three high level steps to my To my process, I critique the source. I organize the information. And then I verify the evidence. The first step in turning a questionable source into credible evidence is to critique”
- [034] [00:04:52](https://www.youtube.com/watch?v=R50W1KDrRPw&t=292s) — “Step three is to verify the evidence. I like to sort information items into these three verification buckets based on the anticipated level of difficulty. Bucket one. These are items that are easy to verify or include straightforward action items, for example, contacting a cemetery or a church record office. Bucket two. These are harder to verify items. They may require researching records that are in less accessible archives. And bucket three. These includes items that are conjecture or are nearly impossible to verify. For example, set somebody's motivation. So the process is simple. I execute bucket one.”

#### [035] How to Analyze Genealogical Sources - James Tanner

- Source: https://www.youtube.com/watch?v=7Jn_XMUozo0
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [035] [00:22:35](https://www.youtube.com/watch?v=7Jn_XMUozo0&t=1355s) — “this to genealogy? You're using case method when you look at thousands of records and documents. So the first time you pick up a document or see a uh US federal census record or a census record from any other country or any other document out there, whether it's a uh parish register from uh Latin America or a a tax record from some country around the world or a census record of of whatever type, or birth certificate, a death certificate, any kind of historical record, um a history history of a county where”
- [035] [00:38:06](https://www.youtube.com/watch?v=7Jn_XMUozo0&t=2286s) — “look at a new document like this, anything that you haven't looked at previously, if you're going to analyze that document, you need to learn about it. You need to learn where it came from, who created it, why they created it, how long during what period of time it was created. Uh and um how accurate it could possibly be. How much accuracy was there? And what was required and what what actually happened in in um in real practice when they started gathering census information. Well, in the United States federal census, for example, one thing you'll”

#### [036] Recognizing Inaccurate and Misleading Genealogical Records, Citations, and Sources

- Source: https://www.youtube.com/watch?v=FPaiNw1Z1b0
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [036] [00:02:16](https://www.youtube.com/watch?v=FPaiNw1Z1b0&t=136s) — “source does contain some errors don't ignore it compare it to more sources closer to the event trusting only one source or focusing only on items that fit your assumptions or expectations may lead to errors misinterpretation Andor faulty conclusions and this would also include eyewitness accounts found in official records you should always question the reliability of the informant in testimony and the informant is always going to be the key to the accuracy of the information there are three important genealogical definitions that you really need to be aware of evidence constitutes facts used to reach conclusions about”
- [036] [00:05:48](https://www.youtube.com/watch?v=FPaiNw1Z1b0&t=348s) — “this that I run into a lot a young child is not listed with a family on a sensus living individual is not named in the will of a supposed parent when all the other children are finally a surviving spouse is not listed in the will or obituary when it comes to the concept of proof it's a four-step process number one the reliability of sources must always be established number two the statements made by family members Associates and neighbors cannot always be taken at face value for a variety of reasons number three official records often”

#### [037] Same Name - Different Man \| Ancestry

- Source: https://www.youtube.com/watch?v=K6-4Y6O5bbQ
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [037] [00:01:15](https://www.youtube.com/watch?v=K6-4Y6O5bbQ&t=75s) — “just some basic strategies that you can use first of all to discover if there are others with the same name and second of all to sort them out so that you make sure that you're attaching the right person to the right life events and to the right family members okay let's go ahead and dive in let's talk first about um how uh you know if there is more than one person with the same name now this is going to um be all about the genealogical proof standard if you're not familiar with that the very first”
- [037] [00:19:10](https://www.youtube.com/watch?v=K6-4Y6O5bbQ&t=1150s) — “it looks like at first glance oh look it's a husband and a wife and a bunch of children because they all have the same last name except one of the kids because it's a child of a sister um they all have the same last name they're all about the right age to be but it's not you know further investigation showed that this was actually a or an aunt and uncle with some nieces and nephews working the family farm so don't assume from 1850 1860 and 1870 just because you have children in a household that those”

#### [038] Using Indirect and Negative Evidence to Prove Unrecorded Events

- Source: https://www.youtube.com/watch?v=VwfAeN31cTw
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [038] [00:02:06](https://www.youtube.com/watch?v=VwfAeN31cTw&t=126s) — “is wrong is possible only after you've assembled evidence from thorough research resolve conflicts within the assembled evidence and use that assemblage to support a conclusion well why are genealogical evidence concepts especially indirect and negative evidence important to us genealogists the simple answer is that when we use indirect and negative evidence we can break through genealogical brick walls that's because brick walls most often occur when direct evidence is absent or scarce and the researcher does not understand or consider what indirect and negative evidence have to offer what information has to offer indirectly”
- [038] [00:27:47](https://www.youtube.com/watch?v=VwfAeN31cTw&t=1667s) — “assemblage to strengthen the case about the identity of josiah's daughter's mother mary leonard before we look at more examples of negative evidence let's look at what negative evidence is not more misconceptions that some of you might need to unlearn and this is in your syllabus material so the absence of records is not negative evidence an unproductive search that yields no genealogical genealogically useful information is not negative evidence and direct or indirect evidence of a non-relationship is not negative evidence let's look at some examples of not negative evidence the absence of information an absence”

#### [051] Unraveling Forensic Genealogy With Juli Whittaker

- Source: https://www.youtube.com/watch?v=u2HltZJ1FrM
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [051] [00:00:34](https://www.youtube.com/watch?v=u2HltZJ1FrM&t=34s) — “&gt;&gt; \[laughter\] &gt;&gt; Oh, god. Just once. Just once. Well, you Hey, you need to step up. You need to get that first word in and start talking, or you're going to get the hey, baby. We're here with Julie Witker, who is a forensic genealogist, and I'm going to be learning how to pronounce multisyllabic words, as well \[laughter\] as finding out what forensic genealogy is doing, and Kathleen's going to dig deeper and ask the questions that I don't even know I should ask. Kathleen, you know Julie, yes? I do know Julie. Julie, how did we”
- [051] [00:15:39](https://www.youtube.com/watch?v=u2HltZJ1FrM&t=939s) — “instead of being certified there, I decided to be a licensed private investigator only on that the forensic side. I don't do surveillance and peeking your trees and find out who \[laughter\] your husband's have having an affair with. I don't \[clears throat\] care about all of that, but I do need the the very important documents and records. So, I just wanted to make sure that I was clear with our audience because I do want to put a plug back into the Council for the Advancement of Forensic Genealogy. You mentioned an internship program. How do listeners get”

#### [061] U.S. Probate Records for Genealogy \| Midwest Genealogy Center

- Source: https://www.youtube.com/watch?v=uAcku9kesK4
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [061] [00:00:30](https://www.youtube.com/watch?v=uAcku9kesK4&t=30s) — “Good afternoon. And welcome to Midwest Genealogy Center's US Probate Records for Genealogy. Uh first a few things, you should have received an email uh for those that are watching hybrid. Um it will include uh the outline for the class as well as um your number to get in. Uh and within 24 hours you will also be getting an email that uh has our marketing evaluation sheet. Please fill that out and return it. Please mute your um audio and your video. Um also please hold your questions to the end of class.”
- [061] [00:46:50](https://www.youtube.com/watch?v=uAcku9kesK4&t=2810s) — “FamilySearch is completely digitized. They also have uh where you can search for a name. You can also uh on some of them you can search the administrative papers, the inventories, and the indexes. It just depends. Uh you can also use search engines to find online databases for specific uh counties and states. And various printed probate indexes of records. You might look at our catalog. We have a lot of indexes up there on probate, including Jackson County. Um and before we get any further, we have our upcoming spring seminar, Branches and Bites.”

#### [066] FamilySearch Catalog: Digging Deeper – Christine Moss Pack (26 September 2024)

- Source: https://www.youtube.com/watch?v=MMe67JLgS08
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [066] [00:03:00](https://www.youtube.com/watch?v=MMe67JLgS08&t=180s) — “uh a spot in our yard to put an aquaponics Pond or a greenhouse so but I thought it would fit right in with our topic of family search catalog digging deeper my objective is to increase your desire and love for research by digging deeper into the family search catalog as we seek to find our people I say our people because I'm fond of them I know you probably are too and just as a kind of overviewer outline I will be basically contrasting the difference between searching from the main records page through family search versus”
- [066] [00:05:34](https://www.youtube.com/watch?v=MMe67JLgS08&t=334s) — “over in this presentation so what does it look like with family search well if we go to the family search page and we click select the search menu you'll see that records is the first option on that menu and that takes you to this search historical records page that you see behind it with a with a basic um ability to type in names and a place and maybe a date and then family search will then um show us results for all of those different for for our relative and different records that they have in”

#### [070] Marriage Records for Family History: Where to find them on Ancestry.com & FamilySearch.org

- Source: https://www.youtube.com/watch?v=JYf7R5lhBlU
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [070] [00:04:35](https://www.youtube.com/watch?v=JYf7R5lhBlU&t=275s) — “certificates marriage registries there are quite a few different and it's just a part of the list but there are quite a few different types of marriage records that you can find now where can you find them I suggest you start with family search familysearch says that they have marriage records dating back to 1570 on up into about 1950 now ancestry has a great deal of marriage records as well and I highly suggest you start with the locality as I'm always professing you want to start with the location what you're searching”
- [070] [00:05:42](https://www.youtube.com/watch?v=JYf7R5lhBlU&t=342s) — “similar you can drill into the Family Search wiki in through the map and again look for by locality first now that's not the same you don't want to search by surname because you could get a different set of results so make sure that you search both ways first by location and then by surname if you don't find what you're looking for one of the things that you want to keep in mind about marriage records there's a lot of times they the civil records are usually held at the county level at”

#### [076] Why Research Death Records First + Ancestry Updates

- Source: https://www.youtube.com/watch?v=F5XFoUx37Ko
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [076] [00:06:53](https://www.youtube.com/watch?v=F5XFoUx37Ko&t=413s) — “researching death records first for a couple reasons one is there is a ton of death records probably more than any other category or vinyl record set or grouping and so we're gonna kind of we're gonna kind of dig into that here right now let me jump over to my slides so death records you know obviously there is death certificates and death registries that's kind of a no-brainer and a lot of people will be looking at those and they'll just ingest them really quick and I want my point with death certificates”
- [076] [00:34:18](https://www.youtube.com/watch?v=F5XFoUx37Ko&t=2058s) — “societies in the state and at the local level in the county level if there is one for the area which you're researching it can get a little expensive if you're joining you know 20 different genealogical societies so think about that research question decide what is your most important important research question that you're tackling right now and then go join that genealogical society and they will also be very grateful because they need that support while you're there volunteer look at children's death records that is also another place where you might find the”

## Domain 2: Probate Court Procedures, Wills, Intestacy & Estate File Extraction

Primary video assignments: [006], [007], [010], [011], [012], [013], [014], [025], [039], [040], [041], [042], [043], [044], [046], [047], [049], [052], [054], [056], [057], [058], [059], [060], [062], [063], [064], [065], [067], [081], [121], [124], [133], [136], [137], [145], [149], [151], [152], [153], [156], [157], [164], [166], [169], [174], [184], [188]

### 2.1 Testate and intestate routing

**Input:** death, domicile, assets and possible will.
**Output:** estate route decision.

**Ordered procedure (editorial synthesis):**

1. Locate the original will, codicils and any admission order; a found will is not necessarily an admitted will.
2. Identify domicile probate and any ancillary real-property proceedings.
3. Distinguish devisees under a valid will from intestate heirs and nonprobate beneficiaries.
4. Search prior administrations and reopened proceedings before opening a duplicate matter.
5. Build a jurisdiction/date-specific succession rule table.

**Execution and acceptance contract:**

- Persist `estate route decision` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [010] [00:11:38](https://www.youtube.com/watch?v=oZiYbKNvxJY&t=698s) — “other entity records birth before and for a time period after the death of the ancestor you can really find that the probate actions could be filed up two years after the date of death sometimes the heirs simply did not take any action to probate the estate until some events as the sale of the real property required a probate and that could have happened years after the person actually died so my rule of course is that you look for probate records from the date of death until the present but that's a”
- [059] [00:01:37](https://www.youtube.com/watch?v=0c5trJYJTyQ&t=97s) — “words in probate is intestate or testate if you died with a will it's a testate probate meaning that you provided the information on what you wanted to have happen with your stuff and if you died without a will it's considered intestate and a lot of people think if there wasn't a will there's no records but that's not true if somebody died intestate without a will there's still a lot of things that can be found so when the colonies were formed the laws were based on english law because that's where basically most”
- [046] [00:00:52](https://www.youtube.com/watch?v=U6LsR1gr0oA&t=52s) — “situations with children being born out of wedlock children prior to marriage family members being at odds with one another family members being arrain all of those things create complications when there is a probate Administration involved because any missing people of a particular decedent or deceased person must be found in order for that probate to proceed the court appointed administrator or executive is responsible for identifying and locating any missing Heirs of a probate Administration or any missing beneficiaries of a will or a trust the probate code mandates that the personal representative use due diligence that”
- [139] [00:04:46](https://www.youtube.com/watch?v=59C1meISvlc&t=286s) — “concerned your grandmother or your parents still own the house it's still in their name it's not in you and your siblings names and there are a lot of issues that can come with that owning property is aage property and we're going to go through some of the issues but let's lay a little bit of the groundwork first uh next slide in taste intestate succession order intestate succession order that would be what happens when a person dies without a will that's what happens when a person dies intestate without a testament that's what that word means”

### 2.2 Probate lifecycle

**Input:** case docket and jurisdiction.
**Output:** dated event ledger and missing-document queue.

**Ordered procedure (editorial synthesis):**

1. Extract petition, notice, service and hearing events with filed and effective dates.
2. Verify Letters Testamentary or Letters of Administration, representative identity and limitations.
3. Capture bond, waivers, inventory and appraisement.
4. Track creditor notice, filing deadlines, allowed claims and payment priority from actual rules.
5. Reconcile interim/final accounting, sale orders and distributions.
6. Use the final decree and receipts to close the chain; do not substitute a petition for an adjudication.

**Execution and acceptance contract:**

- Persist `dated event ledger and missing-document queue` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [014] [00:15:20](https://www.youtube.com/watch?v=07zaZ3sQwi8&t=920s) — “for distribution and notice of the petition for final accounting and this is the order for the hearing on the final accounting so you know final is kind of a relative term here I could go on for some considerable period of time before there is a final final document this is the case here in the Haws case because here is a supplemental decree on distribution in this case they're asking for changes in the way that the final distribution is handled possibly this can possibly occur because in a case like this where it stretched on for 33”
- [064] [00:14:27](https://www.youtube.com/watch?v=t_t1v7TPbFA&t=867s) — “filed that the order is responding to. Right. Um we also have sale bill a lot of stuff I'll just kind of say you need proof of what's done with any assets. Final distributions this is what we also call a final accounting showing here's the assets here's what we did with them here's all the people who made claims whether we paid them or not. The judge has to eventually approve the entire accounting to close out the estate. So if you did something you're not supposed to as a hammer or in this case”
- [059] [00:20:15](https://www.youtube.com/watch?v=0c5trJYJTyQ&t=1215s) — “people that purchase stuff in an estate so that can be very very helpful let me go to one more here we have new york new york they have a ton of probate records they have 32 different probate things some of these are books that people have written and you can click on them and take a look at them some of them are the court records the decrees on accounting administrator bonds estate orders index of wills inventories letters of petitions and administrations letters of collections letters testamentary miscellaneous orders miscellaneous probate records orders admitting wills”
- [156] [01:24:10](https://www.youtube.com/watch?v=7xCfSyqYEys&t=5050s) — “name. And uh we were talking about probate. And uh this guy tried to tell me that when you have real estate part of probate, you're not allowed nationwide, you're not allowed to sell that real estate until you close probate and you do your final uh final accounting. and that was a real estate professional that probably should know better. Um, if a real estate professional that should probably know better thinks that, what do you think your client that's never been in probate before and didn't even know that the word probate existed before they had to”

### 2.3 Archaic wills and historic rights

**Input:** will image and law applicable at execution/death.
**Output:** clause-by-clause disposition map.

**Ordered procedure (editorial synthesis):**

1. Transcribe exactly before normalizing archaic terms; keep illegible spans marked.
2. Separate bequests, devises, residue, life interests, remainder interests and executor appointments.
3. Resolve pronouns and repeated names using witnesses and family context.
4. Check dower, curtesy, coverture and married women’s property statutes for the location and historical date.
5. For pre-1858 England and Wales, identify the ecclesiastical probate jurisdiction; do not generalize that cutoff to every country.

**Execution and acceptance contract:**

- Persist `clause-by-clause disposition map` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [054] [00:03:48](https://www.youtube.com/watch?v=Gwcf300h1sA&t=228s) — “these is using cousin or Kinsman as a cat allall for various relatives up until 1858 probate in England and Wales was administered by over 300 Church of England ecclesiastical courts they are often the only record for the time period before Census records where all members of a family might be listed they were recorded much earlier than birth marriage and death registration as well as baptism marriage and burial information and can fill in other information lacking in Parish registers they can give Vital Information such as occupations land owned and localities that the individual”
- [058] [00:19:40](https://www.youtube.com/watch?v=bcOlApV2Fng&t=1180s) — “often so don't just assume because you know they died in 1894 that the probate should be in 1895 or 1896 and be done keep keep a little bit of an open mind about that another thing to be aware of is that women had probate records too every state had had different laws throughout time about women's property rights um and those laws varied based on a lot of different things um were they single were they married were they widowed were they divorced did they own the property before they got married um”
- [061] [00:40:27](https://www.youtube.com/watch?v=uAcku9kesK4&t=2427s) — “and listed them. It's very interesting, and it's very interesting who had dower rights. Dower rights in Missouri don't exist anymore. They um went out in 1955. And then again in 2017, the legislature made sure we had no dower rights here or curtesy, which is the husband's dower rights. Generally, they didn't have much of that. It would be if for some reason, say the father-in-law put a hold on the estate such that only his daughter could inherit. He could go back on that if his wife died and ask for dower rights.”
- [025] [00:06:45](https://www.youtube.com/watch?v=BAgypTLrbR4&t=405s) — “women but um what did happen was that law had what was called her dower rights so any property that in which she may have had an interest during her life she obtained an interest upon her husband's death now let's give you a scenario that how this could end up in court and how you might know find out what the woman's maiden name was uh so the woman uh so the husband during the lifetime of the of of H as his lifetime and while he was married to the to the woman with the”

### 2.4 Guardianship and minor heirs

**Input:** minor or incapacitated beneficiary.
**Output:** authority matrix.

**Ordered procedure (editorial synthesis):**

1. Identify guardianship/conservatorship separately from estate administration.
2. Read appointment orders for powers, bond and sale/distribution restrictions.
3. Do not treat a guardian’s personal signature as authority to sell a minor’s interest.
4. Track age-of-majority and successor fiduciary events.
5. Reconcile funds with court approval and final accounting.

**Execution and acceptance contract:**

- Persist `authority matrix` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [156] [00:32:41](https://www.youtube.com/watch?v=7xCfSyqYEys&t=1961s) — “when you don't have full authority or when the heirs are minors. When heirs are minors, you almost never have full authority. Um or represent that like and basically if the heirs are minors and and there's not an adult that's the named representative. Um normally you have to go through the court for approval on certain things or um all the heirs are um deemed incapacitated mentally or unfit mentally. All right? And we're talking about all the heirs. And I'm not saying if there's two adults and one minor, you have to do”
- [060] [00:06:08](https://www.youtube.com/watch?v=fCvgh_QabMY&t=368s) — “quite a few years to get all the different parts complete so one of the first dated pieces in this packet which by the way has over a dozen pages is a guardian bond mordecai smith is giving a bond to the court saying that he's bound in a certain amount of money to do his job responsibly for these minor children and this was produced in court in 1775 and he is going to be the guardian for the property of john sally and olive bassett those are the minor heirs of john bassett”
- [041] [00:04:33](https://www.youtube.com/watch?v=pGyFJ46jwTE&t=273s) — “tend to be family, friends, associates and neighbors of the deceased. Sometimes you’ll get a relationship for a single person, but that’s about it. Letters of administration state that a given individual is the estate’s administrator, and can transact on behalf of the estate until it is settled. If there are minor children, the administrator may keep showing up in court until the youngest child reaches the age of majority. Bonds are a financial guarantee that the administrator and or guardian won’t embezzle from the estate. If a court later found the administrator guilty of financial malfeasance, the administrator and”
- [064] [00:13:10](https://www.youtube.com/watch?v=t_t1v7TPbFA&t=790s) — “you to actually give an inventory, which then goes to a final accounting as well. I'll talk about in a second. You do have appraisals and stuff. You can't just sell somebody's house for a dollar. If you are an executor or an administrator personal representative of the estate um you you actually have a duty to the estate itself to make sure that you're basically getting top dollar for anything that's being sold and managing all the funds and property in a proper manner. Orders um the order from the court can be any”

### 2.5 Unindexed probate packets

**Input:** court, decedent variants and death interval.
**Output:** packet completeness checklist.

**Ordered procedure (editorial synthesis):**

1. Search docket/index variants, then petition numbers and estate numbers.
2. Request the complete packet, not only the will.
3. Follow minute books, order books, inventories and loose-paper references.
4. Record gaps in page numbering and request missing exhibits.
5. Cross-check docket events against documents actually received.

**Execution and acceptance contract:**

- Persist `packet completeness checklist` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [063] [00:06:17](https://www.youtube.com/watch?v=Xzst9ZSC1M0&t=377s) — “are recorded only in the probate court minute books a probate court minute book is just that as as the probate court judge deals with this particular probate he writes or his clerk writes the minutes and it's generally a short mr. Jones was here and this happened and that happened but it's in the minute book so when you do your research don't forget to check the court minute books these petitions are filed with the original estate papers it could be the only place that all heirs are named these original estate papers are”
- [056] [00:16:16](https://www.youtube.com/watch?v=Gv4Mibtn8CM&t=976s) — “records office there's other places to look to some genealogy societies historical societies and other groups have transcribed probate records and they've placed them in books in quarterlies or journals most probate records whether in packet or book form can be found through an index either in the courthouse or online but be sure to look beyond the index in those probate books look at the index and then check to see where that record has been placed find the book number and the page number and go find it many are browsable online some”
- [006] [00:01:40](https://www.youtube.com/watch?v=lOmly79G2Tk&t=100s) — “result when I clicked on that image that took me directly to will record volume 3 and 4 page 313. And this is the copy of the will of George Seaffort of Senica County. It's giving me wonderful information, but are there other records in the ancestry pro probate collection that aren't showing up in the index? Remember that first record that we saw? That very first record that we saw for George Seaffort listed not only his will being in will book four page 313 but also docket 5 page 231 and probate journal 8 page 15. Are”
- [060] [00:05:29](https://www.youtube.com/watch?v=fCvgh_QabMY&t=329s) — “see exactly the value of probate records and sometimes we find them in tidy probate packets including all the different parts that went through the court but often we only find it in bits and pieces and we'll go over both kinds of examples so first i want to look at the wills and estates papers from the north carolina estate files collection on family search this happens to be the packet for john bassett and it was dated 1785 although as you'll see as we go through this probate went through the court for”

### 2.6 HTR and OCR extraction

**Input:** scanned probate images.
**Output:** page-linked extraction with confidence flags.

**Ordered procedure (editorial synthesis):**

1. Preserve originals and create checksum-addressed working copies.
2. Deskew and split pages without destroying marginal notes or endorsements.
3. Use Transkribus for handwriting or AWS Textract for supported OCR/layout workflows only where available; this generator calls neither service.
4. Retain page geometry, confidence and raw transcription alongside normalized fields.
5. Manually verify names, amounts, dates, fractions and dispositive language against images.
6. Version corrected text and record who or what made each correction.

**Execution and acceptance contract:**

- Persist `page-linked extraction with confidence flags` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [174] [00:38:43](https://www.youtube.com/watch?v=bLXMXvhuz6k&t=2323s) — “the fields and the baselines drawn hopefully correctly. Else, you can also pre um recognize only the fields and only your baselines and using a baseline model to only recognize the layout um first and then type in all your text in the editor. Um whatever of course works best for your material where you're fastest, but it will of course take away some time from correcting if you use um pre-trained models. And after having corrected the text, um you save it as ground truth. And ground truth is a um term that's used in”
- [169] [00:16:55](https://www.youtube.com/watch?v=wXbImDeCCsY&t=1015s) — “your aws account might be please go and check now so this is the default amazon extract dashboard so here in the left hand side that you see is a sample document where you can see there is printer text as well hand written text and on the right hand side we will see how the output would look like so for example if i click on the raw text you can see like all the fields has been extracted and given to you and if i click on one thing like the corresponding field is highlighted”
- [023] [00:04:02](https://www.youtube.com/watch?v=DjxOkXDU2cY&t=242s) — “permission for access to these files except for vinyl records copies usually cost $1.00 per page and higher if the copy needs to be certified some courthouses offer self-service copiers while others require that all coffees must be made by clerks each state mandates the fees for copies of vital records be prepared to pay $5 to $20 for each certified document often clerks require that copies be made 15 to 45 minutes before closing time we're almost out of time this is intended as an overview of what you can find at a County Courthouse especially Ana County”
- [015] [00:14:15](https://www.youtube.com/watch?v=7M3XZfN7814&t=855s) — “put the volume number or the film number or whatever additional detail is going to get us to that particular record we're going to enter a date here if that's significant we're going to enter the transcription of the text if you would like to now I actually I personally do this a little bit differently rather than putting the transcription of the text into my source citation I actually put it into my notes for the person and I do that so that I create a narrative and so that I have all my um citation transcriptions in one”

### Domain evidence workbench

The following source-specific evidence cards expose primary assigned videos without treating lexical matches as verified legal rules.

#### [006] Finding Probate Records That Aren't Indexed \| Ancestry

- Source: https://www.youtube.com/watch?v=lOmly79G2Tk
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [006] [00:00:01](https://www.youtube.com/watch?v=lOmly79G2Tk&t=1s) — “Welcome to this episode of Five Minute Find, where we show you things on ancestry.com in 5 minutes or less. In this episode, finding probate records that aren't indexed. I recently did a search in the Ohio probate records for George Seaffort in Sakica County and got three results. When I clicked to view the image for the first result, I found that it was his entry in the general index to wills. We have George Seaffort and his will is in will book 4, page 313. There's also a reference to records of George”
- [006] [00:01:40](https://www.youtube.com/watch?v=lOmly79G2Tk&t=100s) — “result when I clicked on that image that took me directly to will record volume 3 and 4 page 313. And this is the copy of the will of George Seaffort of Senica County. It's giving me wonderful information, but are there other records in the ancestry pro probate collection that aren't showing up in the index? Remember that first record that we saw? That very first record that we saw for George Seaffort listed not only his will being in will book four page 313 but also docket 5 page 231 and probate journal 8 page 15. Are”

#### [007] Targeted Genealogical Research: Probate Example

- Source: https://www.youtube.com/watch?v=10DuXkEoTRA
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [007] [00:00:00](https://www.youtube.com/watch?v=10DuXkEoTRA&t=0s) — “Hey everybody. In this episode, I am going to do some what I'm calling targeted research. This is when I am specifically going after a type of record for a specific person. I am focused. I'm laser focused on what I'm doing. So, this was recorded a few months ago back when um Family Search, full text search was in a different location than it is now. Now, all you have to do is click on the search button and find it. But I'm using multiple platforms here. I'm targeted. I'm going after some probate uh records. The video”
- [007] [00:08:12](https://www.youtube.com/watch?v=10DuXkEoTRA&t=492s) — “fact and I had just dialed in 1884 because he had died in 1884 when I did the search. Remember from the full text search I just did 1884. So it might be smart to, you know, go forward and and search several years. So, what I need to do is I'm going to take this whole hyperlink and I'm going to copy that into my research notes and make some notes about this. Actually, we'll transcribe this in a separate document and then take some notes about it into my research notes. Now, we don't want to”

#### [010] Probate Part 6 "Finding Probate Documents" by James Tanner

- Source: https://www.youtube.com/watch?v=oZiYbKNvxJY
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [010] [00:01:36](https://www.youtube.com/watch?v=oZiYbKNvxJY&t=96s) — “preserved in order to provide future insurance that the land can be cleared of any title claims the first question you need to answer in finding a probate file is the jurisdiction this word means the type of case handled by a particular cord and that may be divided either by the district county or the nature of the claim or controversy so for example finding out which of the courts within the particular jurisdiction a particular area had jurisdiction over the probate action is one of the challenges currently it's fairly simple you would need to sent to look up the”
- [010] [00:12:14](https://www.youtube.com/watch?v=oZiYbKNvxJY&t=734s) — “little excessive at least until the possibility of finding after years and years is not not available so important to check with the following other areas be sure and check the court where the probate action may have been filed at the time of the decedent but in addition to that you need to check adjoining counties and cords so almost always possible that the probate was filed in an adjoining County for whatever reason perhaps the probate judge was a relative of the deceased or a friend or even an enemy and they may have been required to”

#### [011] Probate Part 2, Wills by James Tanner

- Source: https://www.youtube.com/watch?v=CyAfgfoF-eo
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [011] [00:02:32](https://www.youtube.com/watch?v=CyAfgfoF-eo&t=152s) — “before that time about the death and the families of the ancestors must come from some other source usually church records the church records are rather limited compared to the amount of information that can be available in a probate record salsa it's also important to understand that probate law is different from differ from state to state the first step is to identify the place where the probate records are archived this can take some considerable detective work on the part of a genealogical researcher the reason is that the lot the older the records are”
- [011] [00:08:02](https://www.youtube.com/watch?v=CyAfgfoF-eo&t=482s) — “the estate for for handling the probate in the uniform probate code States the attorneys are required to submit a bill for their time itemized in a bill to the court for approval before any payment can be made it's important to understand the probate may be necessary either with or without a will the will is kind of an artifact of transferring the property but is not the purpose for having probate probate is the orderly transfer property from one from a deceased person to that deceased person's heirs or assigns if a probate happens with the will it's”

#### [012] Probate Part 3, "Wording of Wills" by James Tanner

- Source: https://www.youtube.com/watch?v=7120UjJPqZM
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [012] [00:03:43](https://www.youtube.com/watch?v=7120UjJPqZM&t=223s) — “the will so the courts have to decide if the new what the new language means and how it relates to previous rulings and how it will affect the law in the future of course wills use language that may be unfamiliar these are not the words you'd have on your grade school spelling test you may have to work slowly at first understand what's being said in the will very important to focus on each word if you don't know the meaning of the word look it up you may need to use a”
- [012] [00:05:03](https://www.youtube.com/watch?v=7120UjJPqZM&t=303s) — “of the wheel is broken each will is broken down into some common provisions the important thing to understand that these particular provisions are necessary and required for a valid will the first is a statement of the identity of the testator testator is the person making the will next is a statement of the testator's intent to make a will this is called testamentary intent and that and the person making a whale has to clearly state they want to dispose of their property upon their demise or upon their death next is a statement setting”

#### [013] Probate Part 5, " What are Probate Procedures" by James Tanner

- Source: https://www.youtube.com/watch?v=Xe2NEfqDwTQ
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [013] [00:03:05](https://www.youtube.com/watch?v=Xe2NEfqDwTQ&t=185s) — “now probate law in the United States is based upon English common law a common law arises out of the cumulative decisions of the courts over hundreds of years and the probate law in the United States also includes legislature made statutes and court made decisions so the court decisions are persuasive to the court however the court must follow the law established by the legislature in statutes most of the time when people say something is for example against the law they mean that there is a statute prohibiting the action however that does”
- [013] [00:06:51](https://www.youtube.com/watch?v=Xe2NEfqDwTQ&t=411s) — “states of america the united states began enacting it's the Legislature's begin enacting their own set of laws there's also a need to know some of the procedures of the court so now we need to know the difference between the law as it is and the procedures so what our probate procedures first of all we understand that laws are made by the legislature rules are made by administrative agencies so for example here the United States legislature would pass a law and then an administrative agency such as the IRS or the any of the”

#### [014] Probate Part 7, "Example of a Probate File" by James Tanner

- Source: https://www.youtube.com/watch?v=07zaZ3sQwi8
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [014] [00:00:43](https://www.youtube.com/watch?v=07zaZ3sQwi8&t=43s) — “simple probate file first we'll do an overview of the file this particular file came from the Utah probate records from 1851 to 1961 which are hosted on the familysearch.org historical record collections it concerns Kayla Paz who died on the 20 November of 20 in November of 1871 and it's interesting to see that the last probate document in the case file was filed on the fourteenth of October 1904 nearly 33 years later this is the first this is actually one of the last documents in the probate file there are 62 pages of”
- [014] [00:03:03](https://www.youtube.com/watch?v=07zaZ3sQwi8&t=183s) — “with the wife's estate finally after 33 years the state was distributed and closed both Caleb and his wife died intestate that means they died without a will the first document in the file is a cover sheet this is something that you may have a tendency to disregard thinking is just a little document that you have to go through but this is an important document because it tells exactly which court the probate was filed in in this case it's the 4th district court in utah county and utah it also gives the name of the deceased”

#### [025] The Anatomy of a Court Case for Genealogists - James Tanner

- Source: https://www.youtube.com/watch?v=BAgypTLrbR4
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [025] [00:22:41](https://www.youtube.com/watch?v=BAgypTLrbR4&t=1361s) — “pending before the court that needed to be decided uh something that needed to be decided by the court so or the judge in this case court and judge in this context are synonymous so we we would all go down to court well they want to go my client would say oh you're going to court can I come and am I supposed to be there and I said well you you don't need to be there but I always told people that they were welcome to come to court if they wanted to well we would go to court uh we'd go”
- [025] [00:59:21](https://www.youtube.com/watch?v=BAgypTLrbR4&t=3561s) — “been lost if there's an appeal but good news there's always more records so we just keep looking and looking because we find it now on appeals we have two kinds of courts courts of appeal versus courts that are not of or courts of record that are are courts that are not of record uh courts of record the appeals courts write out their decisions and uh publish them courts not of record uh all of the information goes into the court file but it's never publicly U published or recorded and so the court of appeal records are”

#### [039] Finding probate records by browsing through images on FamilySearch.org

- Source: https://www.youtube.com/watch?v=hsFQHg-SMN4
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [039] [00:00:00](https://www.youtube.com/watch?v=hsFQHg-SMN4&t=0s) — “Probate documents can be goldmines for genealogical research, few documents are both digitized and indexed, so expect to put in some real effort to find these. In this video, I’ll cover how to find things in digitized probate records once you find the repository. I’ve covered finding the repository in a previous video. Short version: Not every death results in a probate record. Start with digitally indexed repositories, but…. Expect to browse through hand-written indices in digitized court records, and fourth, always include the source citation to make it easier to find those records again.”
- [039] [00:01:20](https://www.youtube.com/watch?v=hsFQHg-SMN4&t=80s) — “index. That’s when it’s time to start browsing through images. I prefer doing this on FamilySearch.org because the site just feels well suited to browsing. You’ll need to create a free account, but after that, just search in the catalog for the county you need. let’s look at Lancaster Cty, Pennsylvania for sources where the author is something like “Pennsylvania. Orphan’s Court” rather than a person’s name. When you see a person's name, it means it's a book. When it's the orphan's court, it means it's the actual court records We’re looking for Jacob Slough of Lancaster county who died around 1750.”

#### [040] Finding repositories for probate records

- Source: https://www.youtube.com/watch?v=A437gHrrk2s
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [040] [00:00:43](https://www.youtube.com/watch?v=A437gHrrk2s&t=43s) — “To get started, U.S. records are stored chronologically at the county level. You’ll need a rough idea when your ancestor died, and where. Death certificates, Find-a-grave, even census records can help. The where can be tricky, though: county boundaries changed, especially in frontier areas, such as Ohio in the early 1800s or Pennsylvania in the 1700s. Court records remain in the original county courthouse. For example, if your ancestor died in Gettysburg, Pennsylvania in 1799, you would find a probate record in York County. If they died a year later, however, you would find the record in Adams County, which was”
- [040] [00:02:02](https://www.youtube.com/watch?v=A437gHrrk2s&t=122s) — “index. The next step is to check the probate inventory on FamilySearch.org. Some probate records are digitized, though not indexed. But many aren’t, which means you need to go old school. I’m a big fan of the library at this stage. If you’re lucky, like me, you live close to a city with a great genealogy section. If you don’t, inter-library loans can bring great libraries to your local branch. Let’s take a glance at Family Search’s probate information for Highland County, Ohio. See those books with authors? You’ll often find a handful of books published in the last 20 to 50 years that have indices”

#### [041] Primary sources: Intestate probate documents

- Source: https://www.youtube.com/watch?v=pGyFJ46jwTE
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [041] [00:00:00](https://www.youtube.com/watch?v=pGyFJ46jwTE&t=0s) — “Probate documents are one of the best primary source documents, but they’re also one of the most complicated, partly because of the dizzying array of different document types, such as: 1) Probate proceedings. 2) Bonds, letters of administration, letters testamentary, and other administrativa. 3) Inventories & bills of sale. 4) Guardianship. I’m Mike O’Neill, and I’m going to give you an overview of different probate documents in five minutes. If you want to dig deeper, I recommend spending some time at “Bob’s Genealogy Cabinet” at genfiles.com. In this video, I’m going to focus on intestate proceedings, where there’s no valid will.”
- [041] [00:03:13](https://www.youtube.com/watch?v=pGyFJ46jwTE&t=193s) — “If you’re lucky, you’ll find pre-built explanations. Bob’s Genealogy Filing Cabinet is a pretty good one. But it may come down to finding an old book on worldcat and requesting it via inter-library loan. I’ve actually got a case study video that hinged on how Virginia’s intestate laws treated children born out of wedlock. Without a copy of the law, I could only speculate. Intestate probate proceedings are going to follow some boilerplate conventions, the most important of which is that children will almost always be listed in birth order. One common exception is if the first-born son has special legal rights: in this case,”

#### [042] Primary Sources: testate probate documents

- Source: https://www.youtube.com/watch?v=NYz_-ZkJbBE
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [042] [00:00:00](https://www.youtube.com/watch?v=NYz_-ZkJbBE&t=0s) — “Probate documents are one of the best primary source documents, but they’re also one of the most complicated, partly because of the dizzying array of different document types, such as: 1) Wills. 2) Bonds, letters of administration, letters testamentary, and other administrativa. 3) Inventories. 4) Probate proceedings. 5) Settlement. 6) Guardianship. I’m Mike O’Neill, and I’m going to give you an overview of different probate documents in five minutes. If you want to dig deeper, I recommend spending some time at “Bob’s Genealogy Cabinet” at genfiles.com. In this video, I’m going to focus on testate proceedings where a person made out a will.”
- [042] [00:03:59](https://www.youtube.com/watch?v=NYz_-ZkJbBE&t=239s) — “The actual court handling probate proceedings will vary state to state, and that can make it difficult to find. I’ll cover hints for this in another video. The final document type you may encounter is an estate settlement. In my experience, this is the rarest type of document to find, and is typically part of probate proceedings. But it is worth calling out because of its potential high genealogical value. If the will explicitly lists out all familial relationships, the settlement won’t matter much. If the decedent didn’t map out familial relationships, perhaps by saying “I leave”

#### [043] Primary Sources: Understanding guardianship in probate proceedings

- Source: https://www.youtube.com/watch?v=7_oRhXnhlag
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [043] [00:01:17](https://www.youtube.com/watch?v=7_oRhXnhlag&t=77s) — “You’ve got the message. Guardianship was about finances, not about raising a child. Of course, I have a few things to add, along with an example of how to misinterpret guardianship. First, pay close attention to when the courts assign guardians. Many courts will note in the record that a child was below or above a certain age. For probate proceedings taking place over many years, you can get very accurate estimates of when some of the children were born. Now why do probate courts do this? Typically, children had different rights depending on their age.”
- [043] [00:03:26](https://www.youtube.com/watch?v=7_oRhXnhlag&t=206s) — “from your parents or via an apprenticeship. For example, in colonial Pennsylvania, apprenticeship was such an important educational path that a 1713 law granted the courts the explicit power to place a minor orphan into an apprenticeship or other form of employment upon the request of a guardian. Now why is that important? If you see a probate document where a child was handed off into an apprenticeship you might think there's a wicked stepfather thing going on. That wasn't the case at all. That's how you got educated. Let's look at an example of how to misinterpret guardianship.”

#### [044] Probate case study: Illegitimacy and conflicting surnames

- Source: https://www.youtube.com/watch?v=YNOLd8LZB48
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [044] [00:00:38](https://www.youtube.com/watch?v=YNOLd8LZB48&t=38s) — “birthplace in Virginia. The consensus was that Julia’s maiden name was Huggins. As always, I assumed good intent when looking at secondary and tertiary sources—that is, other people’s research—and I found a March 1835 probate proceeding in Highland County, Ohio for a William Huggins who named two daughters, July Chew & Thirza Hancher, as well as a son Doctor Benjamin Franklin M. Huggins. Fun fact: Doctor wasn’t a title, it was actually the poor guy’s first name. What a mouthful. Anyway, the probate file noted that William owned land in Frederick County, Virginia. Julia and Thomas spent most of their lives in Highland County, Ohio and in Indiana, but”
- [044] [00:04:08](https://www.youtube.com/watch?v=YNOLd8LZB48&t=248s) — “George P. Chrisman in 1837 in Highland County, Ohio. Then I looked back at William Huggins’ will. It actually named a Wm. Minser in relation to some debts, and lo and behold, Brad Minser’s tree listed William Minser as son of Rebecca Hancher Minser. This has to be all the same family, but there’s no explanation to why Thirza and Julia appear with the wrong maiden name. Or why they would appear in the probate proceeding of a Rebecca Minser receiving shares in her estate equal to Rebecca’s kids. So I went back to my principles: always read the original.”

#### [046] What If An Heir or Beneficary is Missing? How to Find a Missing Heir?

- Source: https://www.youtube.com/watch?v=U6LsR1gr0oA
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [046] [00:01:58](https://www.youtube.com/watch?v=U6LsR1gr0oA&t=118s) — “means that they have to use every effort humanly possible to find the missing Heir or beneficiary the California probate courts are reluctant to close a probate Administration unless they are convinced that the personal representative has used every effort possible to find the missing air or beneficiary the following are common methods used to to identify and to locate a missing Heir or beneficiary the personal representative should speak to friends and other family members of the deceased person to determine if they know anything about additional children or offsprings or issues as they're called in the legal”
- [046] [00:04:51](https://www.youtube.com/watch?v=U6LsR1gr0oA&t=291s) — “intestate secession it is critical that the personal representative keep extreme detailed records of every single effort they've made in order to find that missing Heir or beneficiary because ultimately what you're going to need to do is demonstrate to the probate court all of your due diligence involved in finding that missing Heir or beneficiary so ultimately what happens if you cannot find that missing Heir or beneficiary if the Probate Judge is completely convinced that you have exhausted every single effort to find that missing eror when they are convinced of that they”

#### [047] Daniel Curran Finders International - Todays Wills & Probate Podcast

- Source: https://www.youtube.com/watch?v=AKvEFJHf5K0
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [047] [00:00:00](https://www.youtube.com/watch?v=AKvEFJHf5K0&t=0s) — “you're listening to the today's wills and probate podcast one of the leading sources of information for the Wilson probate sector don't forget to subscribe and sign up to our free newsletter at today's wills and probate dot Co dot UK and follow us on LinkedIn and Twitter hello and welcome to the first today's Wilson probate podcast of 2023 it's a new year I have a new guest somebody's we have not had on the podcast before my thanks to Danny Curran founder and MD of finders International for joining thank you for coming on the”
- [047] [00:27:30](https://www.youtube.com/watch?v=AKvEFJHf5K0&t=1650s) — “joining and thank you for sharing your Insight no it's a pleasure and if ever the surname Opie comes up in a family tree don't contact me for goodness sake yeah you don't want the money the today's Wilson probate podcast is available on your preferred podcast provider it's also available on today's wasn't probate dot Co dot UK my thanks to Danny thank you for listening and we'll see you again soon you're listening to the today's wills and probate podcast one of the leading sources of information for the Wilson probate sector don't forget to subscribe”

#### [049] Probate Detectives

- Source: https://www.youtube.com/watch?v=SLqhAWEXEv4
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [049] [00:04:20](https://www.youtube.com/watch?v=SLqhAWEXEv4&t=260s) — “document divorces as well as marriages so you can find you know we've had cases where people have uh forgotten to get divorced when they when they get married a second time um and of course that means that the the second marriage is uh technically not allowed and the first the Widow from the first marriage or the widower from the first marriage then becomes involved going on from that you're looking at siblings they're usually intes spouse issue parents siblings when you get to um extended family the last category that we allow in England and”
- [049] [00:07:12](https://www.youtube.com/watch?v=SLqhAWEXEv4&t=432s) — “England she would didn't trust anyone never spoke to anyone ever again she became a total recluse so this one big event had this other kind of knock on effect that you would never read about because it wasn't the main story but to hear these as I say the story behind that was was quite incredible recently I think uh I saw you on TV um I think you were on good morning on ITV with um Holly Willoughby and Philip skolfield and and there there was a one of the beneficiaries that you'd found was on that program but”

#### [052] How to Spot a Fake Probate Letter \| 3 Steps to Avoid Scams

- Source: https://www.youtube.com/watch?v=le9BUKYDl1A
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [052] [00:00:00](https://www.youtube.com/watch?v=le9BUKYDl1A&t=0s) — “Think a probate letter is genuine because it has a HMCTS number on it? Think again. Scammers can make letters look very official. They may \[music\] use a deceased person's real details, an actual case reference number, and even a spoof telephone number that appears \[music\] legitimate. Look at these two letters. Exact same information, but one is for 11,000 and one is for 110 million. And this is how easy it is for scammers to alter information. Here are some steps you should take \[music\] to check if a probate letter is genuine. Step one, check the sender and details”
- [052] [00:01:08](https://www.youtube.com/watch?v=le9BUKYDl1A&t=68s) — “&gt;&gt; \[music\] &gt;&gt; to properly verify the letter, visit gov.uk's probate service. Contact them independently to confirm whether \[music\] the letter is genuine. Never use the contact details provided in a suspicious letter. And remember, never make a payment or give personal information until you've independently verified the letter. Still unsure if a probate letter is genuine? Don't take any chances. Contact Fraser and Fraser for expert guidance and peace of mind, &gt;&gt; \[music\] &gt;&gt; completely free of charge.”

#### [054] Finding Wills in England and Wales Online, Part 3: Ecclesiastical Probate Courts, pre-1858 (3-24)

- Source: https://www.youtube.com/watch?v=Gwcf300h1sA
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [054] [00:00:08](https://www.youtube.com/watch?v=Gwcf300h1sA&t=8s) — “hello and welcome to this Vu family history Library webinar which is the third webinar in this third part series talking about finding England and Wales Wills online if you weren't here for the first and second webinars in the first webinar we covered finding Wills online for the prerogative Court of Canterbury and the prerogative Court of York and finding principal probate registry Wills post 1857 in webinar 2 should you wish to see those you can find them at BYU family history Library click classes and webinars and choose Sunday virtual classes where you”
- [054] [00:04:34](https://www.youtube.com/watch?v=Gwcf300h1sA&t=274s) — “is associated with every county has their own way of dealing with the probate courts and the index is associated with those courts there is no cookie cutter way to approach these the first thing you need to establish when searching for pre 1858 probate records is the court in which the will was probated once you've figured out the court you will need to check to see if there is an index if you can find an index online that is the most ideal often the index is at the beginning or at the end of the volumes”

#### [056] Analyzing Probate Records: Finding Our Ancestor's Stories

- Source: https://www.youtube.com/watch?v=Gv4Mibtn8CM
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [056] [00:15:30](https://www.youtube.com/watch?v=Gv4Mibtn8CM&t=930s) — “can be found in archives and courthouses and many have been digitized and can be found online so where can you find probate records check online first ancestry family search and some state and county archives have digitized and placed probate records online and it's a continual commitment for them to do so check locally check home sources who in your family may have some original records i have my grandmother's will check the local courthouse and the state and county archives also see if there's a special records office in some places these records are handed off to a”
- [056] [00:17:51](https://www.youtube.com/watch?v=Gv4Mibtn8CM&t=1071s) — “all may be mentioned in probate packages as property has to be distributed and sold to pay debts you just never know what you might find so do you have any questions if you do please feel free to contact me at sheri carolinagirlgeneology.com well thank you so much for joining me for analyzing probate records finding clues to your ancestors stories remember even when there's not a will there's still a way to find out information about your ancestors so i hope that you will start looking for probate packages and see what goodies that you can find”

#### [057] Discovering Your Ancestors Using Probate Records- James Tanner

- Source: https://www.youtube.com/watch?v=Yt91gmZt8sE
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [057] [00:18:37](https://www.youtube.com/watch?v=Yt91gmZt8sE&t=1117s) — “who were copying the records decided to add their own versions of the seals so these were kind of interesting things that happened okay so what are we going to see when we open up a probate file first of all a probate file isn't a document like a birth certificate or a or a death certificate it isn't something that you see oh there's the probate it's one document a probate file may contain hundreds i would say up to thousands of documents in one file and so that would make that that's another reason that makes them extremely”
- [057] [00:37:55](https://www.youtube.com/watch?v=Yt91gmZt8sE&t=2275s) — “uniform probate code just as i started law school back in 1972 the uniform probate code was starting to be be adopted by certain states within the united states in arizona where i went to law school is was one of the first and so we studied the uniform probate code and i never had to study the old corporate code because arizona was one of the few now it was anticipated that all of the states would eventually accept uniform probate code that has never happened and so you have uniform probate code upc”

#### [058] Getting Started With Probate Records \| Ancestry

- Source: https://www.youtube.com/watch?v=bcOlApV2Fng
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [058] [00:03:39](https://www.youtube.com/watch?v=bcOlApV2Fng&t=219s) — “those databases are by State okay another thing to know is that every County within that state has different records available for different time periods so for example just because the state of Indiana just because the database states that they started keeping records in 17 98 does not mean that every single county has records back to that particular date okay every county is going to have a different date range within that same time period so that's important to understand also it's important to understand that some counties have suffered devastating effects of Courthouse fires or”
- [058] [00:11:56](https://www.youtube.com/watch?v=bcOlApV2Fng&t=716s) — “is going to come up when I do a search so in this case I just put put in the surname Smith into the California wheels and probates Records database specifically and you're going to notice there's 1,75 records that came up and as I scroll through them there are a few things that I notice one for example I have someone who has a surname but no given name listed again that could be because the given name wasn't actually on the record it could be because it was illegible on the record whatever the case may be um”

#### [059] How to Find Wills and Probate Records for Free and What They Can Tell Us

- Source: https://www.youtube.com/watch?v=0c5trJYJTyQ
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [059] [00:01:09](https://www.youtube.com/watch?v=0c5trJYJTyQ&t=69s) — “repetitious so let's get started all right so probates first of all they are more than wills a lot of times we think of probate records as only wills and that's not true so you want to be sure that you're looking at all probate records we're going to talk today about different types of probate records what you can find and where you can find them all right there's a few things that you need to understand about the law in order for you to understand wills and probate records first of all one of the big”
- [059] [00:13:09](https://www.youtube.com/watch?v=0c5trJYJTyQ&t=789s) — “ancestry has quite a lot of these land records and some of their records are actually referencing documents that are in microfilm at family search and i kind of talked about how i prefer family search when i'm looking at deeds because i don't know i just can find them better but on wills and probate records sometimes the opposite is true sometimes i find them easier on ancestry but i do always want to go over to family search and make sure i'm not missing a record set because ancestry might have some of”

#### [060] Records Analysis: Level up Your Probate Skills

- Source: https://www.youtube.com/watch?v=fCvgh_QabMY
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [060] [00:00:07](https://www.youtube.com/watch?v=fCvgh_QabMY&t=7s) — “hi i'm melissa finley welcome to this presentation entitled records analysis level up your probate skills when we talk about probate let's talk about what is the purpose the purpose of probate is to administer all the legalities of a deceased person's estate probate is a multi-step court process and even though i'm going to specifically talk about the united states process this process is very similar in many countries around the world so i'm a united states expert but this might apply at least in some instances where you are researching so this multi-step court process”
- [060] [00:15:21](https://www.youtube.com/watch?v=fCvgh_QabMY&t=921s) — “not be and you have to find bits and pieces here and there in the records of the county that you're looking at but what if you can't find anything you can't find any parts of the probate because the records have been destroyed or because um you just can't find your ancestor in those are there any other alternative records that can find us the same kind of information we're looking for in probate um no will know probate file what can we do well we can go look at deed records and just generic court records so let's”

#### [062] Understanding Wills, Probate, Estate Records, and Women's Rights for Genealogy

- Source: https://www.youtube.com/watch?v=jydLZrDuzCM
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [062] [00:05:46](https://www.youtube.com/watch?v=jydLZrDuzCM&t=346s) — “country in the midwest okay so she wasn't an heir of her husband she didn't inherit from him she could only get her d until the married women's property acts start getting passed and they start replacing da with actual inheritance and what time frame would that be the earliest married women's property Act was passed in 1839 I think it always surprises people to think about where it was passed because every time I ask that of a group people are saying oh it must have been New York or it must have been massach”
- [062] [00:16:51](https://www.youtube.com/watch?v=jydLZrDuzCM&t=1011s) — “that um and and there are going to be differences over time where it's much more common to see widows named and given bequests towards the end of the 19th century than it would be before then when you may not even find the Widow named in the will because after all she's gonna get D yeah so we need to kind of take those those factors into consideration one of the things that I'm always uh professing is is to look at the witnesses because I can't tell you how many genealogical problems I have”

#### [063] Using Land and Probate Records in Family History Research Laurie Bradshaw

- Source: https://www.youtube.com/watch?v=Xzst9ZSC1M0
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [063] [00:07:07](https://www.youtube.com/watch?v=Xzst9ZSC1M0&t=427s) — “extremely important because a file begins to be created as soon as the probate starts and you can find a lot of information in that file that case file if there has been any challenge to the probate or if there have been any concerns about any of the heirs you can find out how long it took to find brother Daniel and where was he and if that should be your some states not all and remember not all states because it isn't a federal law so it's not across the nation but there are some states”
- [063] [00:39:01](https://www.youtube.com/watch?v=Xzst9ZSC1M0&t=2341s) — “that you might try amazon.com and you might be able to get one for a good price the probate records at the family history library catalog is very simple to use when you're looking for probate you always go for the place name and we're going to look for place names in a state hopefully we'll know the county you're going to find out as you look at that how they file and how they house their probate records do they put them in a box a basement do they put them in Superior Court what do”

#### [064] What Happens After Death: Finding and Using Probate Records

- Source: https://www.youtube.com/watch?v=t_t1v7TPbFA
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [064] [00:01:46](https://www.youtube.com/watch?v=t_t1v7TPbFA&t=106s) — “answer on. So, now, there's some important terms here. We we're going to toss around probate. So, the probate is a we're Latin. most literally it it's a proving. So, it's typically associated with proving the contents of a will, proving the validity of a will. You're taking it there to the judge and saying, "Hey, this is what the guy wanted done. This is what the lady wanted done. We need to distribute assets and everything accordingly on their death." Now, probate courts though don't just handle uh deceased person's assets, okay? So, they uh can also handle uh”
- [064] [00:35:27](https://www.youtube.com/watch?v=t_t1v7TPbFA&t=2127s) — “times it'll just then they'll get uh letters of administration on that. Um so, they're administering the will or the estate. Uh personal representative is usually when you aren't probating a will, but you need an estate open for someone. Uh one example of that is uh I always need a personal representative appointed uh when unfortunately uh there has been a death and I represent a surviving family member. Um I have to get a uh estate open and appoint a surviving family member as a personal representative so that then they can make a claim against the person who”

#### [065] What’s in a Probate Record and How to Use it for Genealogical Research– James Tanner (10 Sep 2023)

- Source: https://www.youtube.com/watch?v=TBB8OPPFSsM
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [065] [00:00:11](https://www.youtube.com/watch?v=TBB8OPPFSsM&t=11s) — “well hello this is James Tanner and I'm here again from the BYU family history library to talk about probate records and how to use the probate records in genealogical research and I guess I'll need one couple of things of introduction I've spent almost 41 years doing genealogical research and a lot of that has involved res Research into probate cases they're extremely helpful in finding families and the second part of that is that I was a trial attorney in Arizona for 39 years and spent a lot of time in the probate”
- [065] [00:23:59](https://www.youtube.com/watch?v=TBB8OPPFSsM&t=1439s) — “any records for the African Americans back behind 1860 they simply do not know that there are records which primarily end up being probate records and it may reveal unknown family relationships you may find out who is related to who and that may be a surprise and also may be the only record of the ancestors death It's Not Unusual that you can't find any other evidence of the dis of the ancestors death you might because you found a probate record then be able to find a cemetery record or a cemetery marker”

#### [067] Find More Wills and Probate Records for Using Both Ancestry and FamilySearch Together

- Source: https://www.youtube.com/watch?v=zIOhXZZxDDM
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [067] [00:00:00](https://www.youtube.com/watch?v=zIOhXZZxDDM&t=0s) — “welcome everybody to another episode on genealogy TV today we are talking about wills and probate packages there is a lot to find I'm finding that I can find additional records by using a combination of both ancestry and family search I'm going to show you how you can research these records for your ancestors both on uh family search and on Ancestry by using that combination together it's it's pretty incredible so here's what we're going to do first if this is your first time here my name is Connie Knox I am a lifelong genealogist”
- [067] [00:04:20](https://www.youtube.com/watch?v=zIOhXZZxDDM&t=260s) — “discourage you because I promise you there's more records to find besides that one County so if we hit record count this is a state level there's 1.2 million records there is a state level uh record set here so the county really is irrelevant we don't have to drill into the county in fact I'm not even sure I need this at this point because this whole record set is what we're drilling into so I'm going to rightclick and I'm going to open in a new tab and then I'm going to come into”

#### [081] Declaration Under Probate Code 13101 Tutorial

- Source: https://www.youtube.com/watch?v=1ahhduhMdd0
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [081] [00:00:00](https://www.youtube.com/watch?v=1ahhduhMdd0&t=0s) — “Welcome to this tutorial on how to complete the Declaration Under Probate Code Section 13101 Form located on the California State Controller's Unclaimed Property Website. To navigate to the Declaration Under Probate form from the State Controller's Office website, click on Unclaimed Property. Next, click the link for Claim Filing Instructions and Forms. Lastly, scroll down to the bottom of the page, and click the link for the Declaration Under Probate Code 13101 form. The Declaration Under Probate Form is used for Heir claims, as a way to declare that no Probate was required for an estate, or that the Administrator”
- [081] [00:02:30](https://www.youtube.com/watch?v=1ahhduhMdd0&t=150s) — “for the claimant. Fill in the name of the person or the name of the trust entitled to the decedent's property, whichever is applicable. Finally, the claimant's signature, printed name, and date the claimant makes this declaration is required at the bottom of the form. By signing this form, you declare the statements made on this form are true under penalty of perjury. A notary is not required on this form. If you have any questions, please contact the State Controller's Office by phone at 800-992-4647. Our Call Center is available 8 a.m. to 5 p.m. Pacific Time, Monday through Friday, excluding”

#### [121] Probate Data and Property Lookups: Live Real Estate Coaching with Probate Mastery

- Source: https://www.youtube.com/watch?v=TA4mtGUeNo8
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [121] [00:00:00](https://www.youtube.com/watch?v=TA4mtGUeNo8&t=0s) — “Hey, good afternoon. This is bill gross. I am the host today for our weekly probate mastery community call. We get together every Tuesday, even those that come after our holiday, Tuesdays at noon, Pacific time, 3:00 PM Eastern time, and they're recorded and shortly posted on YouTube and then that's pretty editable. And so we're here to talk about all things, probate, real estate. I'll share with you for those who don't know me. I took Chad's probate mastery program three years. And two months ago. I've been a real estate awhile, but I had to really realize”
- [121] [00:00:58](https://www.youtube.com/watch?v=TA4mtGUeNo8&t=58s) — “I tell them that one, it may not get you a certified in your state. I'm in California. There's another program. They may go through the details of California. But in terms of learning the come from the value proposition you need to create to be successful real estate, there's nothing better than Probate mastery. I participate because I need to keep my head in the game and I need to connect, I think, in real estate, whether you're investor a real estate agent, it's important to connect with people we're in the meet, the people business.”

#### [124] I got free probate leads from the courthouse! Plus SOI and referral marketing \| Podcast Episode 85

- Source: https://www.youtube.com/watch?v=1BlzkVdGPAo
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [124] [00:15:24](https://www.youtube.com/watch?v=1BlzkVdGPAo&t=924s) — “going through probate, get in contact with me, your Certified Probate Expert! Well, I'll tell you what also, if you Google search Pinal county courthouse, you're gonna find pictures of the courthouse. Yeah. You can just throw any like whatever your county is, whatever your courthouse is, put that in there for the familiarity, right? People will stop scrolling as they're going through their Facebook timelines because they see a picture of something. In most counties, the courthouse is somewhat iconic. Like in LA, the, Stanley mosque courthouse is somewhat recognizable. Movies and TV and things like that.”
- [124] [00:31:01](https://www.youtube.com/watch?v=1BlzkVdGPAo&t=1861s) — “I said, you know, probate referee would charge 1% of the value. So it was $454. He said, great. I emailed and he paid me. So I made $454 yesterday. You know, I basically did the BPO and an invoice. So, when people ask is my business, how much of business probate? I'd say, you know, half of it is probate listings where the disclosures probate, yes. But all of it's because of my probate marketing, I met that attorney in court. I guess three and a half or four years ago, just walking down the aisleway we had met socially, I'd met him.”

#### [133] How to JV a probate deal with the estate as your partner \| Probate Investing \| Chad Corbett Probate

- Source: https://www.youtube.com/watch?v=coUYfNbBvq0
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [133] [00:07:04](https://www.youtube.com/watch?v=coUYfNbBvq0&t=424s) — “I'd have to find out, Chad Corbett: ...but the title hasn't transferred, otherwise the note would be paid, right? Probate. Probate is still open. Otherwise I couldn't have transferred title and satisfied the note. Christie: I think probate is still open. I didn't find them through the normal way of sending letters cause they filed for probate. It was a referral. So I'm, I'd have to look to see how long . Chad Corbett: Well, this is a fun one. So normally what we do is we establish an as-is value, like a basis value for the asset that gets that's on the side of the”
- [133] [00:11:12](https://www.youtube.com/watch?v=coUYfNbBvq0&t=672s) — “the land trust, does that mean essentially title would be run at that time to determine if there are any other liens that I don't know about, for example? Chad Corbett: Yep. Christie: Okay. Chad Corbett: That's why I'm suggesting that because we want to have clear general warranty deed proof out. The only lien we hope that comes up is that one first mortgage four for 60,000 bucks. If that's the case, then take it subject to, into the land trust. And again, if it's on their side of the deal, they're responsible for debt service.”

#### [136] The Probate Mistake New Real Estate Investors Make (Florida Attorney Case Study)

- Source: https://www.youtube.com/watch?v=pQwwvYbUYrU
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [136] [00:00:00](https://www.youtube.com/watch?v=pQwwvYbUYrU&t=0s) — “Let's jump into that real story. Tell me about a probate case that looks simple at first and then it turned into a complete mess cuz well, we like talking about the messy side of real estate here. &gt;&gt; Yeah, well first of all Courtney, happy to be on this podcast with you and you know, this this world of probate so fascinating, so vast. There's a lot to learn, lot to know and it's in our great state of Florida, it's amazing here. So, I'll tell you this the the story that I have for you on this was a deal that was”
- [136] [00:04:54](https://www.youtube.com/watch?v=pQwwvYbUYrU&t=294s) — “all these other things? And so, powerful lesson there, Al, because for investors, as they're looking at these deals, just because probate needs to get done, and therefore you know that solution, you shouldn't be jumping the gun too soon to start the legal process until you're ready to make that decision. You've taken that calculated analysis step first. You said, "This is a deal we want to start the process." Man, that's a rough one. &gt;&gt; Oh, and and there was one recently, too, where we were in the about to get everything going with probate, and then”

#### [137] Calling probates, probate marketing, and selling probate property: Live probate class w/ Bill Gross

- Source: https://www.youtube.com/watch?v=PDnxvvPI7jU
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [137] [00:11:22](https://www.youtube.com/watch?v=PDnxvvPI7jU&t=682s) — “Yeah. I hear this question regularly. No, am I calling too soon or I don't want to call too soon. And I would say that question only comes from somebody who's not making phone calls. You guys, once you start calling the probate leads, I've gotten one person say it was too soon out of one because by definition, that person was comfortable enough for whatever word you wanna use enough to fill the paperwork, file it, pay for it. Maybe get an attorney and start the process. Because they, because they've got something they need to”
- [137] [00:26:58](https://www.youtube.com/watch?v=PDnxvvPI7jU&t=1618s) — “have you been in that house? Geez, you must have an awful lot of memories there and a lot of things that you've collected over the years, and then I wait for them to answer. And that's usually, yeah. What are you going to do with all of the things that have accumulated? Do you want to just keep it, or do you think maybe an estate sale would help you? And then that's how I approached the real estate. I don't really go right for the real estate ever, especially when I first, my first conversation, because”

#### [145] Affidavits of Heirship and Other Texas Probate Pitfalls \| TPRE Podcast Ep 3

- Source: https://www.youtube.com/watch?v=n8jP0gweIR4
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [145] [00:03:19](https://www.youtube.com/watch?v=n8jP0gweIR4&t=199s) — “a um like they're concerned about something and actually they should maybe be concerned about something else. Tell me a little bit about that. &gt;&gt; Well, when they when they come in, the first thing I do is what's in the estate and that will determine there's because in in Texas, there's various ways you can do things. You can probate the will as immune of title, which is a very short, brief type of probate, and it's usually to transfer real estate. And if all they have is just the house, then that's really all we need to do. If”
- [145] [00:21:30](https://www.youtube.com/watch?v=n8jP0gweIR4&t=1290s) — “and like they think that 5 hours and a lunch is like now they've got they've got it down. They know what's going on, right? which is interesting because it shows you, you know, there's a lot of wisdom in in um in the Texas licensing law, by the way, that has new real estate agents be under a broker because it's like, you know, there is some like apprenticeship or mentoring you need because you're dealing with high value assets. You're dealing with very serious issues and you can really do damage if you don't know what you're doing. But in”

#### [149] DelcoPA ROW \| Searching for Probated Estates Online

- Source: https://www.youtube.com/watch?v=hpvnOFjxwaM
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [149] [00:00:00](https://www.youtube.com/watch?v=hpvnOFjxwaM&t=0s) — “welcome to the delaware county register of wills online records search i'm rachel ezell berry the register of wills the purpose of this video is teaching you about searching for probated estates online let's get started first want to discuss some features of the online records search service our entire office is very excited to finally be able to offer this free service to the public because this service is free you do not need an account and you do not need to pay to use it the service is also much faster than the”
- [149] [00:01:36](https://www.youtube.com/watch?v=hpvnOFjxwaM&t=96s) — “need a copy or a certified copy of any probate or estate document you must still order it from our office and wait to receive it when using our new online records search the first thing you want to do is click the log in as guest button you do not need a guest account you do not need a name and password logging in as guest will give you access to our system the first screen you'll see involves our disclaimer if you feel satisfied with the disclaimer you can click accept to continue”

#### [151] Pre Probate Leads vs Probate Leads: How do you market to them and why cold calling isn't the best

- Source: https://www.youtube.com/watch?v=4Z6pgZnoWi4
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [151] [00:02:53](https://www.youtube.com/watch?v=4Z6pgZnoWi4&t=173s) — “the new system launches? So I'm no longer associated with all the leads I support them. You know, Jim and Tim are still good friends of mine, but I wanted to move in the direction of this uh, and not, not be chasing leads and the logistics and all that. So I believe that there's a very specific way to work pre probate or leads that are before the probate filing. I always felt comfortable with probate. And what I've found in pulling data is there's a median of 68 days. If you look at the entire file across the country,”
- [151] [00:03:52](https://www.youtube.com/watch?v=4Z6pgZnoWi4&t=232s) — “In pre probate, if you're calling off of death records or scraped obituaries or wherever you might be getting that data, you don't know who the decision makers are. You don't know through a skip trace if you're even getting the right Jane Doe. You don't know if you're calling a minor. You could be calling a 12 year old with a cell phone that happened that, you know, you don't know this stuff. So. I do not believe in direct marketing, in outbound direct mail and cold calling pre-probate lists. I just don't. And I probably never will because I think you have a”

#### [152] Sub-to strategy for probate investing \| Probate foreclosures \| Probate real estate marketing tips

- Source: https://www.youtube.com/watch?v=AAF69oF79DU
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [152] [00:04:25](https://www.youtube.com/watch?v=AAF69oF79DU&t=265s) — “Ideally, if it was held as tenants in the entirety with rights of survivorship, then you had a transfer on death and that will be easy to transfer from stepmother to father. And then she'll have to probate the father's estate to get the property in her name. Tenants in common or some other form of title. You may have probate step mom's estate to get it to dad's estate and then probate that estate. So what her attorney has told her is that there was rights of survivorship. That's where I got that from, but she hasn't heard”
- [152] [00:46:40](https://www.youtube.com/watch?v=AAF69oF79DU&t=2800s) — “messaging that really fits this line of work. I guess two questions I would have would be people who are in probate. Do they even go online to look for probate related resources or do they just have people reach out to them? Is it even productive to try to engineer a website so that they find. It's very difficult. If you look at search volume, like you can use tools like SEM rush there's virtually zero search traffic for probate services, probate information. You're stepping into a blue ocean niche. People don't know it exists.”

#### [153] Hyperlocal real estate marketing at probate court & How to buy a probate property as a sub2 deal

- Source: https://www.youtube.com/watch?v=Odf2VQ3AZsg
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [153] [00:02:48](https://www.youtube.com/watch?v=Odf2VQ3AZsg&t=168s) — “loophole, which solidified, which creates a strong relationship or solidifies an existing relationship. Three you're putting something valuable. It's an actual valuable piece of your marketing that lands in the hands of the family. Like they've been talked to by the probate clerk, the probate attorney. They may have read a book or done some goo but they don't fully have their head wrapped around the probate process either. So it's unlikely anyone else was handed them like a, a literally step by step list. One of the things we're actually working on providing for you guys as a piece of software that does that.”
- [153] [00:11:47](https://www.youtube.com/watch?v=Odf2VQ3AZsg&t=707s) — “We would, I mean, if, if somebody passed away yesterday, they got the letter, they petitioned the court and got the letters of testamentary. Today. We can sell that house. We can go to a purchase agreement. And even to closing this week, we don't need court approval. We don't need anything. We just need to connect chain of title and make sure we can convey title clearly and sell it in Florida is kind of an, a good example of that, that next level of complexity and Florida, you can put the house on the market.”

#### [156] Probate Process for Real Estate Agents & Investors: 12 Steps From Filing to Sale

- Source: https://www.youtube.com/watch?v=7xCfSyqYEys
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [156] [00:59:34](https://www.youtube.com/watch?v=7xCfSyqYEys&t=3574s) — “frequently people apply for probate and then they don't list their assets. Okay? But there comes a point normally in the first couple of months where they have to give their full list of inventory and they have to put real estate on it if it's in the estate. Just because it's not on their list of inventory does not mean that there's no real estate. Really important. Just because it's not on their list doesn't mean there's no real estate. Uh that real estate might be passing outside of probate. And if it is, they might still need to sell. But”
- [156] [01:17:08](https://www.youtube.com/watch?v=7xCfSyqYEys&t=4628s) — “a trust. It could be a survivable asset. In other words, being transferred to a family member without going through probate. So, I don't want anyone making the mistake of going, "Bruce, only 20% or 30% of my list has real estate." Not true. there's real estate hidden all the time. We use probate as sort of our our our first point of reference to recognize that they're going through a process. They have assets. Even if it's not even if real estate's not on there, there may still be a real estate need and frequently is still a real estate”

#### [157] All The Leads Probate Mastermind #447

- Source: https://www.youtube.com/watch?v=xumwh2SPKv4
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [157] [00:02:29](https://www.youtube.com/watch?v=xumwh2SPKv4&t=149s) — “if you're shy or you are in uh Facebook live or YouTube live watching the stream uh you can chat your questions in we'll be monitoring those and they'll come over to the coaches to help answer those questions but we are here for you guys um this call is hosted by all the leads so if you don't know who all the leads is all the leads provides probate leads pre-probate leads divorce leads a list management system CRM that you can use marketing resources like letters websites pretty much anything around that life transition Niche that you may”
- [157] [00:10:31](https://www.youtube.com/watch?v=xumwh2SPKv4&t=631s) — “times you need dates and times and addresses and names that you sent letters to you need you need to show details because that's going to be your ammunition and I probably wouldn't wait six months because property taxes need to be paid the grass needs to be cut um this product this asset is going to start reducing in value and eventually somebody is going to foreclose and it's probably going to be the county so you're probably going to be dealing with the county and the judge is a state or a county official who”

#### [164] Getting started with Transkribus

- Source: https://www.youtube.com/watch?v=TE9fOzkibiE
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [164] [00:00:00](https://www.youtube.com/watch?v=TE9fOzkibiE&t=0s) — “greetings historians and digital archists Welcome to our getting started tutorial on transcribers today you'll learn how to harness this platform to digitize and transcribe historical documents and unlock the written past but what does that mean practically start by creating a free account navigate to app. transcribers doeu sign up and verify your email address once inside you see a dashboard tailored for historical document Management in the transcriber desk which is your central Hub to start working with transcribers let's now have a look on how you can navigate in transcribers in the top navigation you will find the”
- [164] [00:02:16](https://www.youtube.com/watch?v=TE9fOzkibiE&t=136s) — “your texts to upload click upload document transcribers accepts various formats such as jpegs pngs or PDFs but recommends 300 DPI jpegs for op recognition with your documents uploaded it's time for handwritten text recognition the so-called HTR transcribers offers a range of public models for different languages and time periods choose one that matches your document's characteristics for immediate text recognition without any sort of training if the public models don't suit your needs transcribers empowers you to train a custom model this might require require more effort but it is invaluable for specialized”

#### [166] How to Find the Best Probate Leads First

- Source: https://www.youtube.com/watch?v=AZazHyPY6xU
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [166] [00:00:00](https://www.youtube.com/watch?v=AZazHyPY6xU&t=0s) — “Most probate professionals don't need more leads. \[music\] They need a faster way to identify the right ones. In this walkthrough, Jonathan shows how to rank opportunities \[music\] as A, B, and C leads, narrow hundreds of cases without sacrificing quality, use zip codes and historical data, and uncover high priority outofstate petitioners. &gt;&gt; Let me point you to the main thing that you should be of interest to you, and that's this market status tablet right here available. So you have three types of of cases here. Um let's say we were in traditional sales uh sales environment,”
- [166] [00:02:49](https://www.youtube.com/watch?v=AZazHyPY6xU&t=169s) — “first. Hit search again. And that took us some 464 down to 282. All right, we're still not Let's say we want to limit it to 100. So I go back to modify filter again. And let's say this time I only want cases with phone numbers and email address. So, I go down here and to the petitioner filters and I select phone number yes and email yes. So, both must be true for them to show up. If I just pick one or the other, you'll probably get more results, but I like to be picky from the”

#### [169] AWS What’s Next Ft. Amazon Textract for Handwriting

- Source: https://www.youtube.com/watch?v=wXbImDeCCsY
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [169] [00:16:55](https://www.youtube.com/watch?v=wXbImDeCCsY&t=1015s) — “your aws account might be please go and check now so this is the default amazon extract dashboard so here in the left hand side that you see is a sample document where you can see there is printer text as well hand written text and on the right hand side we will see how the output would look like so for example if i click on the raw text you can see like all the fields has been extracted and given to you and if i click on one thing like the corresponding field is highlighted”
- [169] [00:20:31](https://www.youtube.com/watch?v=wXbImDeCCsY&t=1231s) — “the cells also because how a human being would read a table right amazon extract can deliver the same result for you as well now i i can't wait to play with this because i love testing these quarter cases i'm gonna i think i'm next time i use this i'm gonna go in there and draw a table in one of the fields and see if it reads it as a table rob's going to draw a table inside of the name field and and see see what it does he's going to he's going to try to break it”

#### [174] Transkribus Webinar for Beginners (English)

- Source: https://www.youtube.com/watch?v=bLXMXvhuz6k
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [174] [00:30:49](https://www.youtube.com/watch?v=bLXMXvhuz6k&t=1849s) — “information. Again, names, places, or anything else, keywords that you want to look for within the transcriptions that you created. Once you've recognized and corrected and maybe even searched through all your transcriptions, the next step, or well, it's an optional step, is exporting your transcriptions. So, exporting can make a lot of sense if you want to use the text outside of Transkribus, for example, to include it in a publication, share it with colleagues who don't use Transkribus. And to export it, you can select the document or single pages, and then click”
- [174] [00:33:59](https://www.youtube.com/watch?v=bLXMXvhuz6k&t=2039s) — “version history, and you can select a different version, click on compare with current version. Here, this there's not much to compare. Let's maybe see here. And there we can see a lot of differences. So, this is one way how you can compare the results of two different models. What you can do as well is use a layout model first. So, for example, a baseline model like this one, like the Universal Lines model, to first recognize the structure, and then in the second step apply the text recognition model. Uh what you can also try is adjust the”

#### [184] How to Find Old Probate Leads

- Source: https://www.youtube.com/watch?v=nRRFhMEip8c
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [184] [00:00:00](https://www.youtube.com/watch?v=nRRFhMEip8c&t=0s) — “One of David's best probate deals came from a lead that never responded for 5 years. Then she called and the opportunity involved two houses. Jonathan shows how historical prospecting helps you find older probate cases that still haven't listed or sold, filter them down, and build a pipeline most agents overlook. &gt;&gt; So then the question is, well, why do I need probate data and then to log in? Why do I need access to your platform? Because of historical prospecting. So, what is historical prospecting? Historical prospecting is basically going back in time and looking for cases”
- [184] [00:03:45](https://www.youtube.com/watch?v=nRRFhMEip8c&t=225s) — “that. We just want to go back to first we select the year. We go back to 2024. Then we select November of 2024. And we don't select December 1st, 2025 cuz that would give us like 13 months worth of stuff. We need a window, right? We just need a window of time. So, what we do here is we go to 2024 December 30 Well, let's do November. Cuz that's what I said I was going to do. So, November and I have LA County. All right. Now, I do a search. First”

#### [188] Scraping Data--Probate--Public Notice

- Source: https://www.youtube.com/watch?v=sX_SYXDaDeA
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [188] [00:00:37](https://www.youtube.com/watch?v=sX_SYXDaDeA&t=37s) — “keyword that we're searching we're not excluding anything and then I recommend going on county by county so these are the five counties that I search for and the reason I do that is because when I input it into the spreadsheet here I can just make Adams County and just drag that down and then go on to the next one but you can do whatever you want so I've got Adams County pulled up here and these are the ads example the ads that we're looking for so we're looking for probate data so it always has public”
- [188] [00:01:49](https://www.youtube.com/watch?v=sX_SYXDaDeA&t=109s) — “lead so a state of this person here and so on so once you have the ad pull up there's really there's only a few data points that were after after the case number right we're after the estate of that person obviously and the most important data is the PRS first and last name the PRS address mailing address which is all broken down now I know that you can just copy and paste the whole formulas in or the pop you paste the whole address in there and break it out formulas it doesn't always”

## Domain 3: Vital Records, Death Certificates, SSDI & Obituary Mining

Primary video assignments: [022], [024], [069], [071], [072], [073], [074], [075], [150], [159]

### 3.1 Death-first research

**Input:** subject identity and estimated death interval.
**Output:** death identity anchor.

**Ordered procedure (editorial synthesis):**

1. Search death evidence first to bound the life timeline and locate the final jurisdiction.
2. Compare residence, place of death, place of burial and probate venue rather than assuming they match.
3. Use the informant and funeral home to generate family leads.
4. Move backward to marriage and birth only after stabilizing the death identity.
5. Record whether the certificate is original, amended, index-only or a later abstract.

**Execution and acceptance contract:**

- Persist `death identity anchor` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [074] [00:01:29](https://www.youtube.com/watch?v=6TDebNoMsvQ&t=89s) — “could find find even if you have a death certificate so in this example you see that they've listed the place of burial the Masonic Cemetery of Cedar Bayou and the funeral home The Undertaker Tri City's funeral home and they even have the address of the funeral home 400 401 West Pierce Street now in this death certificate you see that they were buried in Glennwood semetery and they gives you the date of burial and then the Undertaker which is a little bit more difficult to read but you have their address so I could go into a city directory and”
- [071] [00:02:49](https://www.youtube.com/watch?v=5sxGnXLZO6A&t=169s) — “Same as the research wiki on family search. So what do you do if you don't have a death certificate? Because as family history researchers, we really do want to be looking at our ancestors from birth to death because that way we have the completeness of their life. It gives us the social history, context of their life, what occurred in their life. And so we really do need to start and to end their life for completeness of our research. So if you don't have a death certificate, you do need to think about the situations that occur around”
- [075] [00:04:44](https://www.youtube.com/watch?v=RM0PcAQiipM&t=284s) — “sometimes you're going to be finding a death record and so it is a little bit different it doesn't look like a death certificate it may list the cause of death it may provide you some other information but they weren't quite the same now another place that I frequently go to get death certificates is family search family search has multiple death records but this shows you the California County birth and death records between 1800 and 1994. and here is an example of a death certificate that was from that database now this death certificate looks a”
- [015] [00:01:51](https://www.youtube.com/watch?v=7M3XZfN7814&t=111s) — “I should be doing a reasonably exhaustive search which means that sometimes I have to go elsewhere for records sometimes because it's all that the state or archive has provided ancestry only has an index of a particular record and so I have to actually write away to the state or get on their website and order a copy of the original marriage certificate or the original death certificate uh because they haven't allowed those to be placed online a lot of times I do a lot of newspaper research and so I use the”

### 3.2 Death certificate extraction

**Input:** certificate image.
**Output:** field-level death record table.

**Ordered procedure (editorial synthesis):**

1. Extract every field including informant name, relationship and address.
2. Capture burial place/date, undertaker, funeral home and disposition method.
3. Record cause and duration of illness as contextual clues, not identity proof alone.
4. Separate medical certifier knowledge from informant-supplied parentage.
5. Link each assertion to the page and field; preserve unknown and blank distinctly.

**Execution and acceptance contract:**

- Persist `field-level death record table` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [074] [00:01:29](https://www.youtube.com/watch?v=6TDebNoMsvQ&t=89s) — “could find find even if you have a death certificate so in this example you see that they've listed the place of burial the Masonic Cemetery of Cedar Bayou and the funeral home The Undertaker Tri City's funeral home and they even have the address of the funeral home 400 401 West Pierce Street now in this death certificate you see that they were buried in Glennwood semetery and they gives you the date of burial and then the Undertaker which is a little bit more difficult to read but you have their address so I could go into a city directory and”
- [030] [00:18:03](https://www.youtube.com/watch?v=tljNDoj74TI&t=1083s) — “informant on a document as well. So just as an example, we're gonna take my grandfather's death certificate. On this death certificate there are 3 informants. All 3 of these informants give us primary information but for different things. The wife gives primary information of his death date and his parents' names because she knew the parents. The doctor gives primary information of the cause of death. The funeral director gives primary information of where the burial took place. Now there's also secondary information in this, and we've already talked about it. This is his birth date and this was given by his wife.”
- [071] [00:00:05](https://www.youtube.com/watch?v=5sxGnXLZO6A&t=5s) — “Hello, everyone. Welcome to Rootstech presentation. No death certificate. What name? By Helen Smith. In Australia. We're quite lucky because civil registration start dates were quite early. Certainly some of the, um. Amount of information on. Tasmanian and South Australian certificates is not as complete as we would like because they were working on copying the English system, which had fairly limited information on the certificates. The death certificate is going to give you the date of death, the cause of death. Place of death and the name and age and occupation of the person as known by the informant.”
- [033] [00:09:30](https://www.youtube.com/watch?v=JIUMf1OHaY0&t=570s) — “Illinois, and her parents were Morris Phelps and Laura Clark Phelps, and she married a man named Amaa Mason Lyman on the 16th of January 1846 in Navo, Hancock County, Illinois. Let's look at a source that will help us answer this research question. So we are going to look and see when and how was this source created so this is a death certificate when someone dies, the law requires a medical professional to certify the date of death and the time and cause of death, and then the undertaker or the funeral home director will help a family member fill out the”

### 3.3 SSDI and SS-5

**Input:** death identity and Social Security clues.
**Output:** SSDI/SS-5 evidence comparison.

**Ordered procedure (editorial synthesis):**

1. Search SSDI variants and compare dates with primary death records.
2. Distinguish death-index data from the original SS-5 application.
3. Evaluate lawful access and availability before requesting an application.
4. Use application parent names and birth details as assertions requiring corroboration.
5. Do not publish full sensitive identifiers in derived reports.

**Execution and acceptance contract:**

- Persist `SSDI/SS-5 evidence comparison` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [072] [00:03:02](https://www.youtube.com/watch?v=Af6QVCj8Rcg&t=182s) — “Social Security application we do not have those on ancestry.com but you may order them for a fee from the Social Security Administration to see instructions on how to do this click on request copy of original application on the left this page walks you through the steps and the information you need to write a letter to the Social Security Administration to get a copy of the ss5 so when you look at this Social Security death index make sure that you record and understand all five pieces that you might be looking at name birth”
- [069] [01:00:38](https://www.youtube.com/watch?v=70ya-VPbkBc&t=3638s) — “died so there is a legal requirement in the United States for the mortuaries and anyone else recording a death to report that to the Social Security Administration who then creates a list called the Social Security Death Index or SSDI and there's been a lot of controversy lately because of privacy issues with the SSDI and some now it's not nearly as easily to obtain this information as it used to be what happens if the person is lost at sea or someplace else well then you get into shipping records and then you get into”
- [032] [00:08:33](https://www.youtube.com/watch?v=Ep2zENQQZ1k&t=513s) — “so this would have given them birth dates around 1895 and 1898. however when we look at other records from their life um bessie was born on the 6th of june 1900 and this is verified by the 1910 census by a delayed birth certificate filled out in the 1940s and by the social security death index and sydney was born on the 16th of august 1897 and this is verified in some of the records from his life the 1900 census his world war one draft registration and the social security death index so why is there conflicting”
- [076] [00:12:09](https://www.youtube.com/watch?v=F5XFoUx37Ko&t=729s) — “folks there as well so that is what I'm talking about with funeral and burial records Social Security Death Index is another source of death information and so it's it's really kind of cool if you can get the actual Social Security records you know it's an index right so that's just indexing something to more records so dig deeper if you can now there are privacy laws and so in some cases I think it's with the Social Security Death Index I think they fall under the same seventy-two your Privacy Act but if you can get a hold of the”

### 3.4 No certificate fallback ladder

**Input:** documented failed civil death search.
**Output:** bounded death interval with fallback citations.

**Ordered procedure (editorial synthesis):**

1. Search burial registers, cemetery sexton records and grave ownership.
2. Search applicable mortality schedules and coroner/inquest records.
3. Search church burial registers and funeral home files.
4. Search probate petitions, inventories and guardianship records.
5. Compare tax cessation, deed transitions and census disappearance without treating any one as a death date.
6. Bound the death interval between last-known-alive and first independently recorded death evidence.

**Execution and acceptance contract:**

- Persist `bounded death interval with fallback citations` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [074] [00:01:29](https://www.youtube.com/watch?v=6TDebNoMsvQ&t=89s) — “could find find even if you have a death certificate so in this example you see that they've listed the place of burial the Masonic Cemetery of Cedar Bayou and the funeral home The Undertaker Tri City's funeral home and they even have the address of the funeral home 400 401 West Pierce Street now in this death certificate you see that they were buried in Glennwood semetery and they gives you the date of burial and then the Undertaker which is a little bit more difficult to read but you have their address so I could go into a city directory and”
- [071] [00:03:32](https://www.youtube.com/watch?v=5sxGnXLZO6A&t=212s) — “a death to be able to determine other potential records that you may have. So this is a mind map I did using Kaggle and just thinking about deaths and places where deaths could actually be mentioned. So you've got the civil registration, you've got funeral directors records, you've got perhaps hospital records, inquest records, police records. Um, you've gotten potentially an obituary. There's a funeral director who's involved. There's actually a cemetery where the body's been placed, maybe a crematorium in later, um, in the more modern time frames. You might find that you don't actually have a date of death,”
- [069] [00:38:11](https://www.youtube.com/watch?v=70ya-VPbkBc&t=2291s) — “for burial by the way tells almost as much information total information is as would be found on it on a death certificate and in addition it tells more information that is on the news on most death certificates because it tells the location of the burial and it also tale tells the day of the burial sometimes that's noted on the death certificate but not always and so this is kind of an important that this permit for it open the grave tells exactly where the grave was located which once again is important especially if the grave is not”
- [015] [00:19:15](https://www.youtube.com/watch?v=7M3XZfN7814&t=1155s) — “certificate yes it contains information about the death date in place but it also is a piece of evidence for gender and it's a piece of evidence for name and it's a piece of evidence for birth date in place it might be a piece of evidence for parents' names and birthplaces for spouse's names and birthplaces for the burial date and location okay so a death certificate is a source it is not just an image and that Source pertains to a lot of facts not just the obvious fact of a death certificate and this is true of a lot of”

### 3.5 Marriage and obituary chaining

**Input:** names across multiple records.
**Output:** surname alias graph and obituary family table.

**Ordered procedure (editorial synthesis):**

1. Build a dated surname timeline from marriages, divorces and remarriages.
2. Search maiden names, prior married names, initials and spouse names.
3. Extract survivors, predeceased relatives, residences, funeral details and relationship wording from obituaries.
4. Check newspaper issue date, edition, page and image; OCR search failures require browsing.
5. Do not equate omitted relatives with disinheritance or proof of no relationship.

**Execution and acceptance contract:**

- Persist `surname alias graph and obituary family table` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [049] [00:04:20](https://www.youtube.com/watch?v=SLqhAWEXEv4&t=260s) — “document divorces as well as marriages so you can find you know we've had cases where people have uh forgotten to get divorced when they when they get married a second time um and of course that means that the the second marriage is uh technically not allowed and the first the Widow from the first marriage or the widower from the first marriage then becomes involved going on from that you're looking at siblings they're usually intes spouse issue parents siblings when you get to um extended family the last category that we allow in England and”
- [024] [00:10:37](https://www.youtube.com/watch?v=1Ptl1u6wRoY&t=637s) — “now when we're talking about digital newspapers we're talking about newspapers not the paper but the paper has had a an image made through a scanner that has transferred that the photograph the image of that newspaper page onto a uh into a file format that can be read by a computer and then searched most of the larger digital newspaper websites have what have have used what is called optical character recognition or OCR to read through all of the articles in the newspaper and make the text available online for to be searched by their”
- [139] [00:53:27](https://www.youtube.com/watch?v=59C1meISvlc&t=3207s) — “records to see this person's obituary the the owner of record to see their obituary did this person have children and then that's when we start building the family tree did this person have children now we're going to try and find this person's obituary did this person have children then we're going to look in the parish records of marriages divorces child support things like that we're going to build a family tree out from there it can be very arduous depending on how long ago it was but it is a thing that's possible uh another”
- [150] [00:06:13](https://www.youtube.com/watch?v=yFnDG9Lf6kc&t=373s) — “what we do have in our files after clicking on the blue hyperlink you'll see a search details page that will provide information regarding marriage info applicant 1 info and applicant 2 info if you'd like to navigate on the different tabs to see what's available click the different tabs and scroll down to see that information information that's included includes the name of your officiant if you had one the date of marriage and information about each person that applied for the marriage license if you determine that indeed we do have your marriage license in our records and”

### Domain evidence workbench

The following source-specific evidence cards expose primary assigned videos without treating lexical matches as verified legal rules.

#### [022] Courthouse Records: One-Stop Shopping for Family Secrets

- Source: https://www.youtube.com/watch?v=PuaqkDhOYh8
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [022] [00:01:23](https://www.youtube.com/watch?v=PuaqkDhOYh8&t=83s) — “with here's the example our first number one is the example of using courthouse documents uh this is mabel claire powers and we are going to research her best kept secrets here is um her certificate of death her real name was patricia marie um her last name was powers when she was born you can see right away that she is her name is actually not patricia uh that is one of the fun mysteries we get to research but let's take a look right here this is the date of birth that we were given on”
- [022] [00:10:30](https://www.youtube.com/watch?v=PuaqkDhOYh8&t=630s) — “amazing amount of genealogical information in this grouping then we have civil court and criminal court records those also can be hard to fund they're not always kept in the older the older cases are not always kept in the courthouses any longer but we just put on our sleuth cap and we can find out um one way or another where some of these might have gone if in fact they've still been retained road records tax records corners records records and naturalizations i actually just saw my first corners records a couple of years ago and”

#### [024] Online Digital Newspaper Sources - James Tanner

- Source: https://www.youtube.com/watch?v=1Ptl1u6wRoY
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [024] [00:05:43](https://www.youtube.com/watch?v=1Ptl1u6wRoY&t=343s) — “search all day on the internet on Google for the for your ancestors name and he may be in a thousand newspaper articles but they would never show up online so we need to uh to understand there's that that you really do have to go to each of these websites and do a search with their search engine on their website in order to see if they have the information that you need uh next big point is free versus subscription um we all like free it sounds good um there are some very very large free”
- [024] [00:34:51](https://www.youtube.com/watch?v=1Ptl1u6wRoY&t=2091s) — “regardless we know I understand we're talking about online digital newspapers but um eventually you run out of the of the digital newspapers you may go through every every page that's online for for some specific County or whatever and it still is a good idea to always either contact directly or go to the place and start asking in museums and local libraries about their newspaper collections because because these are very very local newspapers may only still be sitting in in a pile of paper someplace in a in a storage room or on a”

#### [069] Digging Deep into Death Records - James Tanner

- Source: https://www.youtube.com/watch?v=70ya-VPbkBc
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [069] [00:02:22](https://www.youtube.com/watch?v=70ya-VPbkBc&t=142s) — “digging deep into death records and learn a little bit about the different kinds of records that accompany the death process and I guess if you were to look at most of the source citations that are that are put into family to online family trees and generally what people know about and look for are in regard to death records are just two things first of all tombstones also called grave markers also called gravestones and death certificates but is that all and the question and the answer to that question of course is”
- [069] [01:02:38](https://www.youtube.com/watch?v=70ya-VPbkBc&t=3758s) — “there is always more places to look you're never gonna run out of places to look for stuff you think you're done you think you've looked everywhere you are wrong you just have no idea where does how many records there could be I have I have been through this process with grave records and it is always every time I go back through this process I always find another class of records that I didn't know existed so it just keeps going it's just incredible how much information that you can find if you're persistent and if you're willing”

#### [071] No Death Certificate?

- Source: https://www.youtube.com/watch?v=5sxGnXLZO6A
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [071] [00:00:05](https://www.youtube.com/watch?v=5sxGnXLZO6A&t=5s) — “Hello, everyone. Welcome to Rootstech presentation. No death certificate. What name? By Helen Smith. In Australia. We're quite lucky because civil registration start dates were quite early. Certainly some of the, um. Amount of information on. Tasmanian and South Australian certificates is not as complete as we would like because they were working on copying the English system, which had fairly limited information on the certificates. The death certificate is going to give you the date of death, the cause of death. Place of death and the name and age and occupation of the person as known by the informant.”
- [071] [00:02:49](https://www.youtube.com/watch?v=5sxGnXLZO6A&t=169s) — “Same as the research wiki on family search. So what do you do if you don't have a death certificate? Because as family history researchers, we really do want to be looking at our ancestors from birth to death because that way we have the completeness of their life. It gives us the social history, context of their life, what occurred in their life. And so we really do need to start and to end their life for completeness of our research. So if you don't have a death certificate, you do need to think about the situations that occur around”

#### [072] Social Security Death Index: Uncovering Hidden Clues \| Ancestry

- Source: https://www.youtube.com/watch?v=Af6QVCj8Rcg
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [072] [00:00:02](https://www.youtube.com/watch?v=Af6QVCj8Rcg&t=2s) — “hello this is five minute find where we show you something you might have missed on ancestry.com in 5 minutes or less this is Anne Mitchell and today I'm going to show you something you might have missed in the Social Security death index let's start with the basics on every Social Security death index entry you'll find the name birth date death date place and year the social security number was issued but what you may have missed is in the last residence or last benefit let's start with the most basic Social Security death index entry this”
- [072] [00:03:02](https://www.youtube.com/watch?v=Af6QVCj8Rcg&t=182s) — “Social Security application we do not have those on ancestry.com but you may order them for a fee from the Social Security Administration to see instructions on how to do this click on request copy of original application on the left this page walks you through the steps and the information you need to write a letter to the Social Security Administration to get a copy of the ss5 so when you look at this Social Security death index make sure that you record and understand all five pieces that you might be looking at name birth”

#### [073] Sourcing Your Vitals - Citations for Birth, Marriage and Death Records \| Ancestry

- Source: https://www.youtube.com/watch?v=ih5iilWPvjI
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [073] [00:01:14](https://www.youtube.com/watch?v=ih5iilWPvjI&t=74s) — “will find you use these a lot and being able to evaluate Vital Records is really really important and Vital Records um are usually what we we call Birth marriage and death records right these are the big event records so let's step back a second maybe not all of you have been in some of my source classes so why do you site your sources why is this important why not just attach things and go merrily along your way because you need to be able to find the source again if you need”
- [073] [00:11:45](https://www.youtube.com/watch?v=ih5iilWPvjI&t=705s) — “because it's important to me when I'm evaluating one you Source because you want to find two you do it because you want to evaluate so it's North Carolina State Board of Health Bureau of Vital Statistics SS uh North Carolina death certificates blah blah blah microfilm s123 North Carolina State archives in North Carolina so when I write out the citation it would look like North Carolina State Board of Health database name database and images ancestry.com publication details and entry for James Thomas Payne died 19 May 1934 and you can stop there”

#### [074] What death records are you missing?

- Source: https://www.youtube.com/watch?v=6TDebNoMsvQ
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [074] [00:00:00](https://www.youtube.com/watch?v=6TDebNoMsvQ&t=0s) — “death records it's all about death yes I'm wearing black so what death records have you overlooked what death records may exist that you're not thinking about or that may help you figure out somebody's death if you don't already know it I'm Amy cross and today we're going to talk about this and more records that pertain to death and how you can find them for your family members I'm here to help you take your genealogy to the next level so let's go death certificates at least in the United States really didn't start until”
- [074] [00:07:15](https://www.youtube.com/watch?v=6TDebNoMsvQ&t=435s) — “records that maybe you haven't found that may pertain to your family member they might be in the Social Security death index in the United States and so you definitely want to check that because that can lead you to further records and then you also want to look at more mortality schedules if you haven't been able to find the death date of your ancestor and in the United States we have Federal mortality schedules in 1850 1860 1870 1880 and 1885 most of those are available on Ancestry and family search okay what are”

#### [075] Where Can You Get a Death Certificate (& what information is in it)

- Source: https://www.youtube.com/watch?v=RM0PcAQiipM
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [075] [00:00:55](https://www.youtube.com/watch?v=RM0PcAQiipM&t=55s) — “death certificate is a really valuable record but there's a couple of things that you need to keep in mind about it and it's a matter of when was it created and by whom was it created and so the information that you find in a death certificate can kind of be spotty sometimes and it's not always right so let's talk talk about what you'll find in a death certificate here is an example of a death certificate from Texas so this death certificate was in Fort Worth Tarrant County Texas it was for a woman Tenny Alexander”
- [075] [00:04:44](https://www.youtube.com/watch?v=RM0PcAQiipM&t=284s) — “sometimes you're going to be finding a death record and so it is a little bit different it doesn't look like a death certificate it may list the cause of death it may provide you some other information but they weren't quite the same now another place that I frequently go to get death certificates is family search family search has multiple death records but this shows you the California County birth and death records between 1800 and 1994. and here is an example of a death certificate that was from that database now this death certificate looks a”

#### [150] DelcoPA ROW \| Searching for the Existence of Marriage Records Online

- Source: https://www.youtube.com/watch?v=yFnDG9Lf6kc
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [150] [00:00:01](https://www.youtube.com/watch?v=yFnDG9Lf6kc&t=1s) — “welcome to the delaware county register of wills online records search i'm rachel lee zelberry the register of wills the topic of this video is searching for the existence of marriage records online at the end of this video you should feel comfortable navigating our online records search to determine if your marriage record exists in our online records let's get started first i want to briefly discuss some features of the online records search service that we're so excited to finally offer the public first of all this service is free you don't need an account”
- [150] [00:02:38](https://www.youtube.com/watch?v=yFnDG9Lf6kc&t=158s) — “services screen you want to look to the left-hand pane under what would you like to do today and you want to look for the search public records option please click that option you should now proceed to a screen that gives you an option with different search types in order to search your marriage record online you want to look on the left hand pane under search types and i recommend selecting marriage names in order to search for your marriage record you want to type in information under the specific criteria heading in order to search for your”

#### [159] TRAINING Using Successor in Interest to Save the Family Home

- Source: https://www.youtube.com/watch?v=JsPL1vXcgCI
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [159] [00:08:42](https://www.youtube.com/watch?v=JsPL1vXcgCI&t=522s) — “to file probate does this person who's sitting in my office wanting to try to save this home do they need a probate petition and the answer is it depends and sometimes lenders or servicers will say you have to go file probate and that seems to be kind of a gut reaction an immediate assumption that oh yes if there's been a death you absolutely have to file probate and that's not always true there are a few circumstances in which the air that has inherited the house might not need to file probate so we”
- [159] [00:39:53](https://www.youtube.com/watch?v=JsPL1vXcgCI&t=2393s) — “have to file probate because probate is costly and time consuming and i'll just put in a plug because that it was a great question to bring that up because there's lots behind it that when you're working with borrowers not because somebody has died and they're coming in sort of in a distressed situation but when it's earlier you can really help them be proactive a lot of the problems that all of us deal with in these situations are because there hasn't been sort of advanced planning and laying it out and trying to create an easier”

## Domain 4: State Unclaimed Property & Tax/Mortgage Foreclosure Surplus Funds Recovery

Primary video assignments: [077], [078], [080], [082], [083], [084], [086], [087], [088], [089], [090], [091], [092], [093], [094], [096], [097], [098], [099], [100], [102], [104], [105], [106], [108], [109], [110], [111], [113], [114], [115], [155]

### 4.1 Unclaimed property versus surplus

**Input:** candidate asset.
**Output:** asset-specific recovery route.

**Ordered procedure (editorial synthesis):**

1. Classify state-held intangible property separately from county tax-sale and mortgage-sale proceeds.
2. Identify custodian, property/case identifier, claimant and governing jurisdiction.
3. Verify the asset is still held and not already paid or assigned.
4. Construct the right-to-claim chain from original owner through estate and successors.
5. Estimate net recovery after actual priority claims, costs and permissible fees.

**Execution and acceptance contract:**

- Persist `asset-specific recovery route` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [086] [00:00:00](https://www.youtube.com/watch?v=4-lZwuXtY6Y&t=0s) — “This is a case study for an Amador County, California tax sale surplus funds. We were able to get $25,898 on this claim. As you can see here, we got paid directly from the county. All right? Company's name is Prestige Family Assets Group. And we assist individuals filing for surplus funds due to non-payment in taxes or mortgage. In the event of this foreclosure, if the property sells for more than what was owed, that is going to result in a surplus. We were able to identify the surplus, identify who's actually entitled, assist them on”
- [094] [00:02:46](https://www.youtube.com/watch?v=TTMtgtc31k4&t=166s) — “identifiers like names addresses and other personal information number two contacting potential claimants okay we call this skip tracing or Outreach Once A match is identified unclaimed property investigators contact the potential claimants through mail phone calls or emails they inform the claimants about the existence of unclaimed funds or property and offer their services to assist in the recovery process that's number two okay number three verification and documentation okay verification unclaimed property investigators help claim it verify and identify the right to the unclaimed property this may involve Gathering necessary documents such as”
- [084] [00:00:00](https://www.youtube.com/watch?v=MiiGrCZZAZk&t=0s) — “Hey, what's up, YouTube? Welcome back to my page, Money Making Juggernaut. I'm your host, Eric Richardson, the number one educator in the asset recovery business. Today, I'm going to provide a case study. Just got paid out on a $210,000 claim. This was in the state of California on a mortgage foreclosure, which is non-judicial. For those of you who do non-judicial, so you have to basically be a foreclosure consultant, or you have to go through a law firm to have the claim filed. Also, mortgage foreclosures being non-judicial, you're going through a”
- [082] — supplied storyboard/description reconstruction; no quote timestamp: Controller Malia M. Cohen introduces ClaimIt.ca.gov and explains California Unclaimed Property Law. After three years of dormancy, covered property can include bank accounts, stocks, uncashed checks, insurance benefits, wages and safe deposit box contents. Real estate is excluded. Search by Last or Business Name, First Name and City or ZIP, or by Property ID. Active escheated properties have a +CLAIM button. Pre-escheat Notice properties have an INFO button showing holder contact information and a June 1 transfer deadline; an owner can contact the holder directly before transfer. Add multiple properties to the Claim Cart. Select the Claimant Relationship: Myself; Business Officer/Dissolving/LLC/Sole Prop; Heir; Heir-Trust; Heir-Will; Heir-Court Appointed Rep; Heir-Final Decree Distribution; Holder Reimbursement; Government Agency; or Bankruptcy Trustee. Complete the three-step eClaim form. Step 1 collects contact information, SSN and date of birth. Step 2 is an electronic signature under penalty of perjury. Step 3 presents a claim summary with Claim ID and a confirmation email within 24 hours. Upload verification documents through Upload Claim Documentation, with up to five files per batch in PDF, JPG or JPEG format, each between 1 KB and 15 MB. Document types include ID, SSN, Proof of Reported Address, Death Certificate, Trust/Will/Probate Decree and Investigator Agreement. Check status at ClaimIt.ca.gov or call 1-800-992-4647.

### 4.2 Deceased-owner claim packet

**Input:** owner death and candidate heirs.
**Output:** complete deceased-owner claim packet.

**Ordered procedure (editorial synthesis):**

1. Match the owner to the reported name/address using independent records.
2. Obtain death evidence and representative appointment or applicable successor procedure.
3. Locate will, distribution order and trust documents where relevant.
4. Construct an heirship table including deceased intermediate heirs and their successors.
5. Reconcile claimant identity, capacity, shares and supporting documents before submission.
6. Record claim ID, requested supplements, deadlines and payment disposition.

**Execution and acceptance contract:**

- Persist `complete deceased-owner claim packet` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [082] — supplied storyboard/description reconstruction; no quote timestamp: Controller Malia M. Cohen introduces ClaimIt.ca.gov and explains California Unclaimed Property Law. After three years of dormancy, covered property can include bank accounts, stocks, uncashed checks, insurance benefits, wages and safe deposit box contents. Real estate is excluded. Search by Last or Business Name, First Name and City or ZIP, or by Property ID. Active escheated properties have a +CLAIM button. Pre-escheat Notice properties have an INFO button showing holder contact information and a June 1 transfer deadline; an owner can contact the holder directly before transfer. Add multiple properties to the Claim Cart. Select the Claimant Relationship: Myself; Business Officer/Dissolving/LLC/Sole Prop; Heir; Heir-Trust; Heir-Will; Heir-Court Appointed Rep; Heir-Final Decree Distribution; Holder Reimbursement; Government Agency; or Bankruptcy Trustee. Complete the three-step eClaim form. Step 1 collects contact information, SSN and date of birth. Step 2 is an electronic signature under penalty of perjury. Step 3 presents a claim summary with Claim ID and a confirmation email within 24 hours. Upload verification documents through Upload Claim Documentation, with up to five files per batch in PDF, JPG or JPEG format, each between 1 KB and 15 MB. Document types include ID, SSN, Proof of Reported Address, Death Certificate, Trust/Will/Probate Decree and Investigator Agreement. Check status at ClaimIt.ca.gov or call 1-800-992-4647.
- [083] [00:02:03](https://www.youtube.com/watch?v=cMCrrRkehJk&t=123s) — “Next, list the birthdate and date of death for each child, if known. In section 3, list all of the grandchildren of the deceased owner, whether living or deceased. Be sure to include their parent's name in this section under Parent's Name. Next, list the birthdate and date of death for each grandchild, if known. Section 4 list the name of the parents of the deceased owner, including their date of birth and their date of death, if applicable. In section 5 you will list the names of all siblings of the deceased owner, whether they”
- [094] [00:03:37](https://www.youtube.com/watch?v=TTMtgtc31k4&t=217s) — “identification proof of address legal documents or any other relevant records to help them tie them to that claim now there's the claim filing process so once you have all the supporting documents you know you're dealing with the right person you got to file a claim okay so filing claims they assist in preparing and submitting the required forms and documents ment ation to the appropriate state unclaimed property office okay now as far as compensation goes okay there's a few different ways that we can get paid as investigators when we're working deals and the very”
- [110] [00:10:11](https://www.youtube.com/watch?v=GrE0UUh_3BI&t=611s) — “you can see um the information exactly what we will need from you in order to prove that you are the rightful owner so owner is if you're the you're the owner of the claim joint owner it's you and someone else owns that claim if you're a guardian you're claiming on behalf of someone an heir if you're claiming on behalf of a deceased person trust business government and international claims we have claim instructions right there that you can click on that go into detail more if you have any questions so if you find your name uh on”

### 4.3 California search and pre-escheat

**Input:** California owner variants.
**Output:** search history and property ledger.

**Ordered procedure (editorial synthesis):**

1. Use ClaimIt.ca.gov; omit middle initial on initial search and use at least three last-name characters.
2. Try partial city and first names, nicknames, prior addresses and reporting typos.
3. Inspect +CLAIM escheated entries separately from INFO holder notices.
4. For a notice, capture holder contact and the displayed June 1 transfer deadline; contact the holder directly where appropriate.
5. Preserve Property IDs and search variants; do not confuse unclaimed money with real estate.

**Execution and acceptance contract:**

- Persist `search history and property ledger` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [082] — supplied storyboard/description reconstruction; no quote timestamp: Controller Malia M. Cohen introduces ClaimIt.ca.gov and explains California Unclaimed Property Law. After three years of dormancy, covered property can include bank accounts, stocks, uncashed checks, insurance benefits, wages and safe deposit box contents. Real estate is excluded. Search by Last or Business Name, First Name and City or ZIP, or by Property ID. Active escheated properties have a +CLAIM button. Pre-escheat Notice properties have an INFO button showing holder contact information and a June 1 transfer deadline; an owner can contact the holder directly before transfer. Add multiple properties to the Claim Cart. Select the Claimant Relationship: Myself; Business Officer/Dissolving/LLC/Sole Prop; Heir; Heir-Trust; Heir-Will; Heir-Court Appointed Rep; Heir-Final Decree Distribution; Holder Reimbursement; Government Agency; or Bankruptcy Trustee. Complete the three-step eClaim form. Step 1 collects contact information, SSN and date of birth. Step 2 is an electronic signature under penalty of perjury. Step 3 presents a claim summary with Claim ID and a confirmation email within 24 hours. Upload verification documents through Upload Claim Documentation, with up to five files per batch in PDF, JPG or JPEG format, each between 1 KB and 15 MB. Document types include ID, SSN, Proof of Reported Address, Death Certificate, Trust/Will/Probate Decree and Investigator Agreement. Check status at ClaimIt.ca.gov or call 1-800-992-4647.
- [112] — supplied storyboard/description reconstruction; no quote timestamp: The California State Controller's Office explains Property ID searching on ClaimIt.ca.gov. Do not use a middle initial on the initial search. The example John P Sullivan returns 73 matches while John Sullivan returns more than 500 because holders often omit middle initials. Last Name requires at least three characters. Narrow results with cities where the person lived or received mail. Holder reporting errors in names, streets, cities or ZIP codes can explain undelivered payments. Try partial city names, such as Gold for Gold River, common name misspellings, partial first names and nicknames, such as WIL for William or Will. Inspect results for former addresses, P.O. boxes and family members. Click Add beside a Property ID to add it to the Claims Cart, then Claim Properties in My Cart or Continue Search. File using eClaim or a paper mail-in form when complex heir documentation is required. Record the Property ID before calling (800) 992-4647.
- [092] [00:03:39](https://www.youtube.com/watch?v=ijLtjR0tTd8&t=219s) — “next page. Probably something like get your unclaimed property. And it says search for unclaimed property. Let's go ahead and read some of the text that's on the upper left. It says to begin your search, enter your last name or the name of your business. To better refine your results, you may also enter your first name. Exact name matches will be shown first property for individuals with similar names to the name you entered will \[music\] follow. Says this is a free and secured service provided by California unclaimed property to claim your lost funds. Once you found the”
- [111] [00:00:45](https://www.youtube.com/watch?v=eRjGqaIOHWI&t=45s) — “means no paper claim form is required and it will significantly cut down the amount of time it takes for you to receive your money you can also speed up the process by selecting to receive your funds by direct deposit also known as AC okay now let's get started type your last name or company name in the designated text box you must type a minimum of two characters into the text box to further narrow your search you may also type your first name or initial your ZIP code address or city in each designated text box by”

### 4.4 California eClaim and upload

**Input:** matched California property IDs.
**Output:** submission receipt and upload manifest.

**Ordered procedure (editorial synthesis):**

1. Select the actual claimant relationship: Myself; Business Officer/Dissolving/LLC/Sole Prop; Heir; Heir-Trust; Heir-Will; Heir-Court Appointed Rep; Heir-Final Decree Distribution; Holder Reimbursement; Government Agency; Bankruptcy Trustee.
2. Treat these as supplied UI labels, not invented machine/API codes.
3. Complete contact information, SSN/DOB, then electronic signature, then claim summary.
4. Retain Claim ID and monitor the stated 24-hour confirmation email.
5. Upload at most five files per batch, PDF/JPG/JPEG, 1 KB–15 MB each, using the corresponding document categories.
6. Check status at ClaimIt.ca.gov or 1-800-992-4647 with Property ID and Claim ID available.

**Execution and acceptance contract:**

- Persist `submission receipt and upload manifest` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [082] — supplied storyboard/description reconstruction; no quote timestamp: Controller Malia M. Cohen introduces ClaimIt.ca.gov and explains California Unclaimed Property Law. After three years of dormancy, covered property can include bank accounts, stocks, uncashed checks, insurance benefits, wages and safe deposit box contents. Real estate is excluded. Search by Last or Business Name, First Name and City or ZIP, or by Property ID. Active escheated properties have a +CLAIM button. Pre-escheat Notice properties have an INFO button showing holder contact information and a June 1 transfer deadline; an owner can contact the holder directly before transfer. Add multiple properties to the Claim Cart. Select the Claimant Relationship: Myself; Business Officer/Dissolving/LLC/Sole Prop; Heir; Heir-Trust; Heir-Will; Heir-Court Appointed Rep; Heir-Final Decree Distribution; Holder Reimbursement; Government Agency; or Bankruptcy Trustee. Complete the three-step eClaim form. Step 1 collects contact information, SSN and date of birth. Step 2 is an electronic signature under penalty of perjury. Step 3 presents a claim summary with Claim ID and a confirmation email within 24 hours. Upload verification documents through Upload Claim Documentation, with up to five files per batch in PDF, JPG or JPEG format, each between 1 KB and 15 MB. Document types include ID, SSN, Proof of Reported Address, Death Certificate, Trust/Will/Probate Decree and Investigator Agreement. Check status at ClaimIt.ca.gov or call 1-800-992-4647.
- [092] [00:11:04](https://www.youtube.com/watch?v=ijLtjR0tTd8&t=664s) — “well, air court appointed representative, air final decree beneficiary, air interstate, interstate holder reimbursement, government agency, and bankruptcy trustee. \[music\] And so when you're ready to choose what you need to choose, go a hit that file claim button at the below and we will continue to the next slide. On the following screen, you're going to enter your contact information. Now on the top of the screen, it should default to individual, but for some reason, if it isn't, you're going to choose individual and then continue with the last name. Or if you're business, obviously choose”
- [112] — supplied storyboard/description reconstruction; no quote timestamp: The California State Controller's Office explains Property ID searching on ClaimIt.ca.gov. Do not use a middle initial on the initial search. The example John P Sullivan returns 73 matches while John Sullivan returns more than 500 because holders often omit middle initials. Last Name requires at least three characters. Narrow results with cities where the person lived or received mail. Holder reporting errors in names, streets, cities or ZIP codes can explain undelivered payments. Try partial city names, such as Gold for Gold River, common name misspellings, partial first names and nicknames, such as WIL for William or Will. Inspect results for former addresses, P.O. boxes and family members. Click Add beside a Property ID to add it to the Claims Cart, then Claim Properties in My Cart or Continue Search. File using eClaim or a paper mail-in form when complex heir documentation is required. Record the Property ID before calling (800) 992-4647.
- [081] [00:02:30](https://www.youtube.com/watch?v=1ahhduhMdd0&t=150s) — “for the claimant. Fill in the name of the person or the name of the trust entitled to the decedent's property, whichever is applicable. Finally, the claimant's signature, printed name, and date the claimant makes this declaration is required at the bottom of the form. By signing this form, you declare the statements made on this form are true under penalty of perjury. A notary is not required on this form. If you have any questions, please contact the State Controller's Office by phone at 800-992-4647. Our Call Center is available 8 a.m. to 5 p.m. Pacific Time, Monday through Friday, excluding”

### 4.5 California small estate and heirship

**Input:** decedent dates, assets and proposed § 13101 declaration.
**Output:** dated eligibility worksheet and completed heirship schedule.

**Ordered procedure (editorial synthesis):**

1. Read the applicable California Probate Code §§ 13100–13116 provisions and current SCO instructions together.
2. Check the waiting period, applicable date-dependent value threshold, eligible asset classes and valuation exclusions; do not hardcode a timeless dollar amount.
3. Establish whether administration is pending or completed and whether any required representative consent exists.
4. Use the official SCO Table of Heirship; list spouse, descendants and other relevant classes including predeceased links, not only the claimant.
5. Attach the actual chain of death, marriage, birth, will and court records supporting entitlement.
6. Distinguish collection authority from a determination of real-property title.

**Execution and acceptance contract:**

- Persist `dated eligibility worksheet and completed heirship schedule` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [081] [00:00:00](https://www.youtube.com/watch?v=1ahhduhMdd0&t=0s) — “Welcome to this tutorial on how to complete the Declaration Under Probate Code Section 13101 Form located on the California State Controller's Unclaimed Property Website. To navigate to the Declaration Under Probate form from the State Controller's Office website, click on Unclaimed Property. Next, click the link for Claim Filing Instructions and Forms. Lastly, scroll down to the bottom of the page, and click the link for the Declaration Under Probate Code 13101 form. The Declaration Under Probate Form is used for Heir claims, as a way to declare that no Probate was required for an estate, or that the Administrator”
- [083] [00:00:00](https://www.youtube.com/watch?v=cMCrrRkehJk&t=0s) — “Welcome to this tutorial on how to complete the Table of Heirship Form located on the California State Controller's Unclaimed Property Website. To navigate to the Table of Heirship form from the State Controller's Office website, click on Unclaimed Property. Next, click the link for Claim Filing Instructions and Forms. Lastly, scroll down to the bottom of the page, and click the link for the Table of Heirship form. The Table of Heirship Form is used for Heir claims, where the owner passed intestate, with no Will, Trust, or other Estate Plan, and Probate was”
- [082] — supplied storyboard/description reconstruction; no quote timestamp: Controller Malia M. Cohen introduces ClaimIt.ca.gov and explains California Unclaimed Property Law. After three years of dormancy, covered property can include bank accounts, stocks, uncashed checks, insurance benefits, wages and safe deposit box contents. Real estate is excluded. Search by Last or Business Name, First Name and City or ZIP, or by Property ID. Active escheated properties have a +CLAIM button. Pre-escheat Notice properties have an INFO button showing holder contact information and a June 1 transfer deadline; an owner can contact the holder directly before transfer. Add multiple properties to the Claim Cart. Select the Claimant Relationship: Myself; Business Officer/Dissolving/LLC/Sole Prop; Heir; Heir-Trust; Heir-Will; Heir-Court Appointed Rep; Heir-Final Decree Distribution; Holder Reimbursement; Government Agency; or Bankruptcy Trustee. Complete the three-step eClaim form. Step 1 collects contact information, SSN and date of birth. Step 2 is an electronic signature under penalty of perjury. Step 3 presents a claim summary with Claim ID and a confirmation email within 24 hours. Upload verification documents through Upload Claim Documentation, with up to five files per batch in PDF, JPG or JPEG format, each between 1 KB and 15 MB. Document types include ID, SSN, Proof of Reported Address, Death Certificate, Trust/Will/Probate Decree and Investigator Agreement. Check status at ClaimIt.ca.gov or call 1-800-992-4647.
- [010] [00:11:38](https://www.youtube.com/watch?v=oZiYbKNvxJY&t=698s) — “other entity records birth before and for a time period after the death of the ancestor you can really find that the probate actions could be filed up two years after the date of death sometimes the heirs simply did not take any action to probate the estate until some events as the sale of the real property required a probate and that could have happened years after the person actually died so my rule of course is that you look for probate records from the date of death until the present but that's a”

### 4.6 State locator rules and Ohio HB 96

**Input:** state and claim type.
**Output:** state-by-state dated rule matrix.

**Ordered procedure (editorial synthesis):**

1. Maintain separate California, Ohio, Pennsylvania Treasury, Michigan, Delaware and New Mexico rule records.
2. Extract registration, contract timing, fee cap, required disclosures and filing authority with exact source and effective date.
3. For Ohio HB 96, identify each of the three claimed steps and the precise deadline language in the corpus evidence; do not infer dates from the bill number.
4. Compare video-era instructions with the current official program before operational use.
5. Mark any absent numeric limit or deadline as not established, never fill it with a nationwide default.

**Execution and acceptance contract:**

- Persist `state-by-state dated rule matrix` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [082] — supplied storyboard/description reconstruction; no quote timestamp: Controller Malia M. Cohen introduces ClaimIt.ca.gov and explains California Unclaimed Property Law. After three years of dormancy, covered property can include bank accounts, stocks, uncashed checks, insurance benefits, wages and safe deposit box contents. Real estate is excluded. Search by Last or Business Name, First Name and City or ZIP, or by Property ID. Active escheated properties have a +CLAIM button. Pre-escheat Notice properties have an INFO button showing holder contact information and a June 1 transfer deadline; an owner can contact the holder directly before transfer. Add multiple properties to the Claim Cart. Select the Claimant Relationship: Myself; Business Officer/Dissolving/LLC/Sole Prop; Heir; Heir-Trust; Heir-Will; Heir-Court Appointed Rep; Heir-Final Decree Distribution; Holder Reimbursement; Government Agency; or Bankruptcy Trustee. Complete the three-step eClaim form. Step 1 collects contact information, SSN and date of birth. Step 2 is an electronic signature under penalty of perjury. Step 3 presents a claim summary with Claim ID and a confirmation email within 24 hours. Upload verification documents through Upload Claim Documentation, with up to five files per batch in PDF, JPG or JPEG format, each between 1 KB and 15 MB. Document types include ID, SSN, Proof of Reported Address, Death Certificate, Trust/Will/Probate Decree and Investigator Agreement. Check status at ClaimIt.ca.gov or call 1-800-992-4647.
- [098] [00:02:09](https://www.youtube.com/watch?v=_8vyoTSh7Rs&t=129s) — “I'm gonna show you guys how to register to work on claim funds, and the state of California... The first thing you'd wanna do... From a Google search bar, just type in California unclaimed property. 0:02:22.6 S2: Now, if you wanted to work in Delaware is put in Delaware on claim property or New York, whatever it might be. But Google's pretty good, you guys... They're pretty good at predicting exactly what you want, and so this is the correct website right here, just do... So CDOT gov, it right here. Okay, now what doesn't matter if you're trying to register for the State”
- [097] [00:04:50](https://www.youtube.com/watch?v=Fn04U_Yfuzg&t=290s) — “um first name last name you don't have to put middle name date of birth email address confirm the email address phone number social security number tax id county address cities state and zip code once that's filled out simply press the next button this is the three step form so enter the claim info uh preview the claim then you go to claim summary and then you submit once you finish right so that's how you would um enter a clean um in the state of michigan if you have worked lived in the state of michigan if you”
- [090] [00:05:22](https://www.youtube.com/watch?v=MVCNlj7HQBQ&t=322s) — “you the authority to act. First, your signed contingency agreement, all right? That's the deal with your client that spells out your fees and protects both of you. You know your state's fees cap before you write a number, very important, because if your fee is too high, the entire agreement can get thrown out. Next, you need one of the two things, either an assignment of interest where the owner hands their claim fully over to you, or a limited power of attorney, which lets you act for them without taking the claim over.”

### 4.7 Two-method lien verification

**Input:** surplus case and property legal description.
**Output:** lien priority and net proceeds reconciliation.

**Ordered procedure (editorial synthesis):**

1. Method 1: reconstruct the recorded encumbrance chain using recorder grantor/grantee, mortgage, assignment, release and judgment indexes.
2. Match every instrument to the legal description and relevant owner aliases; obtain payoff/release evidence rather than assuming a lien vanished.
3. Method 2: inspect the foreclosure/tax-sale court or custodian file, sale confirmation, distribution order, creditor claims and current held-balance statement.
4. Reconcile recorded interests against adjudicated priority, notice, redemption and surviving claims.
5. Treat disagreement between methods as an unresolved net-proceeds issue; gross surplus is not claimant net recovery.

**Execution and acceptance contract:**

- Persist `lien priority and net proceeds reconciliation` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [082] — supplied storyboard/description reconstruction; no quote timestamp: Controller Malia M. Cohen introduces ClaimIt.ca.gov and explains California Unclaimed Property Law. After three years of dormancy, covered property can include bank accounts, stocks, uncashed checks, insurance benefits, wages and safe deposit box contents. Real estate is excluded. Search by Last or Business Name, First Name and City or ZIP, or by Property ID. Active escheated properties have a +CLAIM button. Pre-escheat Notice properties have an INFO button showing holder contact information and a June 1 transfer deadline; an owner can contact the holder directly before transfer. Add multiple properties to the Claim Cart. Select the Claimant Relationship: Myself; Business Officer/Dissolving/LLC/Sole Prop; Heir; Heir-Trust; Heir-Will; Heir-Court Appointed Rep; Heir-Final Decree Distribution; Holder Reimbursement; Government Agency; or Bankruptcy Trustee. Complete the three-step eClaim form. Step 1 collects contact information, SSN and date of birth. Step 2 is an electronic signature under penalty of perjury. Step 3 presents a claim summary with Claim ID and a confirmation email within 24 hours. Upload verification documents through Upload Claim Documentation, with up to five files per batch in PDF, JPG or JPEG format, each between 1 KB and 15 MB. Document types include ID, SSN, Proof of Reported Address, Death Certificate, Trust/Will/Probate Decree and Investigator Agreement. Check status at ClaimIt.ca.gov or call 1-800-992-4647.
- [131] [00:08:26](https://www.youtube.com/watch?v=sf2hUucsNZ8&t=506s) — “unreleased mortgage. Plenty of times people get sent the the um satisfaction for their mortgage in the mail, but then they don't go bring it to the court the the public records at the county clerk to then release the mortgage. And so, that's very common to have an unreleased mortgage that's still is a question mark and you have to figure out what's going on, whether it's an active mortgage that needs a payoff or like that release that's just sitting in a file, it could be something like that. It could be a judgment or a lien.”
- [160] [00:02:39](https://www.youtube.com/watch?v=TWPIHeWyybg&t=159s) — “current date now when it comes to liens there are two different types of liens that can be recorded on a title you have what's called a recorded lien and an unrecorded lien now an example of a recorded lien can be a mortgage an example of an unrecorded lien can be let's say a mechanics lien where you had a contractor do some work on a property but they weren't paid for that particular job so they decided to slap a lien on the property a mechanics lien on that property to cloud the title”
- [152] [00:33:54](https://www.youtube.com/watch?v=AAF69oF79DU&t=2034s) — “Any short sale agents on Oahu, they'll hand you one, but when you meet with the family, have them sign the authorization to release, and you may need to connect that chain of title with a death certificate showing that the borrower's deceased and the authorization to release was signed by the heirs and the line of succession. Then you can talk to them and order your own payoff statement and, know that the real numbers. Yeah, it makes sense. Okay. So get that, get the auditory release, perhaps have the heir the immediate family rights, somebody signed.”

### 4.8 Recovery operations

**Input:** qualified claim and projected economics.
**Output:** operations queue, contract register and quality scorecard.

**Ordered procedure (editorial synthesis):**

1. Recruit notaries by county/coverage, verify commissioning and document-handling capability, and maintain backup availability.
2. Separate notarial identity work from legal advice and estate authority decisions.
3. Use jurisdiction-specific contingency/investigator contracts; record fee basis, expenses, cancellation and assignment terms.
4. Open calls with identity, purpose and a verifiable callback route; ask whether the person wants the asset details before discussing sensitive information.
5. Treat an objection as a question to answer and a complaint as an issue to log and resolve; honor cancellation and contact preferences.
6. Give VAs bounded research tasks and source-quality checks, not authority to invent heirs or signatures.
7. Compare free official portals against paid research tools using retrieval quality and total cost per resolved case.

**Execution and acceptance contract:**

- Persist `operations queue, contract register and quality scorecard` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [082] — supplied storyboard/description reconstruction; no quote timestamp: Controller Malia M. Cohen introduces ClaimIt.ca.gov and explains California Unclaimed Property Law. After three years of dormancy, covered property can include bank accounts, stocks, uncashed checks, insurance benefits, wages and safe deposit box contents. Real estate is excluded. Search by Last or Business Name, First Name and City or ZIP, or by Property ID. Active escheated properties have a +CLAIM button. Pre-escheat Notice properties have an INFO button showing holder contact information and a June 1 transfer deadline; an owner can contact the holder directly before transfer. Add multiple properties to the Claim Cart. Select the Claimant Relationship: Myself; Business Officer/Dissolving/LLC/Sole Prop; Heir; Heir-Trust; Heir-Will; Heir-Court Appointed Rep; Heir-Final Decree Distribution; Holder Reimbursement; Government Agency; or Bankruptcy Trustee. Complete the three-step eClaim form. Step 1 collects contact information, SSN and date of birth. Step 2 is an electronic signature under penalty of perjury. Step 3 presents a claim summary with Claim ID and a confirmation email within 24 hours. Upload verification documents through Upload Claim Documentation, with up to five files per batch in PDF, JPG or JPEG format, each between 1 KB and 15 MB. Document types include ID, SSN, Proof of Reported Address, Death Certificate, Trust/Will/Probate Decree and Investigator Agreement. Check status at ClaimIt.ca.gov or call 1-800-992-4647.
- [094] [00:04:13](https://www.youtube.com/watch?v=TTMtgtc31k4&t=253s) — “first one is going to be a contingency fee this is going to be probably 99% of the time how you're going to get paid a contingency fee is unclaimed property investigators work on a contingency fee basis meaning they only get paid if they successfully recover the unclaimed fund fund for the claim it the fee typically is a percentage of the recovered amount which can range from 10 to 40% depending on the complexity and the size of the claim now you guys I will tell you there are some states out there that don't have a state commission”
- [020] [00:02:50](https://www.youtube.com/watch?v=J1h18kFbXKU&t=170s) — “evidence and what all of this means a research log is a working document for you it's as i said before in part one it's your brain on paper and i'm saying it again you're making calculations in writing right here the only wrong way is to not record your searches now to introduce the record type research log it's one of my favorites to use when we use the record type research log it's simply that we take notes by category of record type because it operates as a checklist of resources we like in any research log we document”
- [104] [00:05:57](https://www.youtube.com/watch?v=t4w_wFimZ9A&t=357s) — “0:05:58.2 S1: So second time they bring it up, you address it slightly, and then you move back onto the conversation on the third time, if somebody brings up a complaint three times, it's not a complaint, surreal objection, and that's something that you need to tackle and resolve for that person in their head, otherwise that probably is gonna be a buying hurdle for them saying yes to letting them have a mobile notary come or their house and sign contracts with them. Okay. 0:06:25.7 S2: So when that third time comes, address the issue completely until”

### Domain evidence workbench

The following source-specific evidence cards expose primary assigned videos without treating lexical matches as verified legal rules.

#### [077] How To Work Deceased Claims - Step-By-Step (Surplus Funds Recovery)

- Source: https://www.youtube.com/watch?v=l8J2d1WwudY
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [077] [00:04:46](https://www.youtube.com/watch?v=l8J2d1WwudY&t=286s) — “might see living will or trust. So if you have case parties they'll be identifying them as that and then also you might see an existing surplus funds list. All right so why does this matter? Step one, we need to verify that the person is deceased so that we can know that hey, we're now looking to target the heirs, the family members. We are not looking to target somebody who has passed away. All right, so step one, plain and simple, the foundation of working deceased claims, you have to know if somebody's deceased or not.”
- [077] [00:25:29](https://www.youtube.com/watch?v=l8J2d1WwudY&t=1529s) — “sometimes even $50, but you can obtain a death certificate. In some scenarios, you might need their social. So, um, some of the heirs may not know this. You can use the SSA form 711 and you can request to obtain the social security number for the deceased individual. All right? So, you can request that as the heir. So there are some forms and documents that are going to require the deceased individual's social. So that's why you'll need that. All right. So it's very important to note that these are essential so that we can establish the”

#### [078] ✅ 💰 CALIFORNIA Unclaimed Property Investigations - Tips from a Licensed Private Investigator!

- Source: https://www.youtube.com/watch?v=nI1xm6ZA2qo
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [078] [00:00:00](https://www.youtube.com/watch?v=nI1xm6ZA2qo&t=0s) — “let's talk about unclaimed property investigations in the state of California when there is no activity on an account or there is no contact with the owner for more than three years typically the business corporation or financial institution or even an insurance company that holds that money has to send that money to the state of California the state of California has to make reasonable attempts of locating the owner and that usually fails and that's where you come in you can go to the state controllers office for the state of California and check their beta”
- [078] [00:04:43](https://www.youtube.com/watch?v=nI1xm6ZA2qo&t=283s) — “would locate the owner and then write a letter saying Who I am and I'm saying is my contact information but that cost money that cost postage and I'm not too sure spending money on those databases to find these people is even worth the effort because they're gonna get a whole there any of this letter or you might call them if you're able to find them and it's going to be it might be kind of awkward because if you show up to my door you know with one of these unclaimed property investigations and”

#### [080] Unclaimed Funds: Lead Sourcing Masterclass

- Source: https://www.youtube.com/watch?v=h4Qz3EvAAnw
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [080] [00:00:56](https://www.youtube.com/watch?v=h4Qz3EvAAnw&t=56s) — “there's going to be a link in the description of this video. You click on that, you put your email in, it gets automatically sent to you. So, go grab it. But without going any longer, let's just get right into the content, you guys. So, for starters, let's talk about what a lead is. Okay, a lead, also known as a claimant, aka the people that we help, is an individual or entity identified as having unclaimed funds or assets. These data files represent potential clients who need assistance in recovering their lost or abandoned”
- [080] [00:06:51](https://www.youtube.com/watch?v=h4Qz3EvAAnw&t=411s) — “1 to 3 weeks, but there are also some states that allow you to download the leads directly from the State Department website 247, like the California website. You could literally pause this video right now, go to the unclaimed funds website for California, and then just download them and get them right now. But most states aren't like that. Okay. Now, what do you do after you have the data? You got to skip trace it so you can call it. Okay. Now, whether you obtain bulk leads or manual search leads, the data will need to be sorted,”

#### [082] How to Claim Your Property for the California State Controller's Office

- Source: https://www.youtube.com/watch?v=bsbWDqAXsrE
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [082] — supplied storyboard/description reconstruction; no quote timestamp: Controller Malia M. Cohen introduces ClaimIt.ca.gov and explains California Unclaimed Property Law. After three years of dormancy, covered property can include bank accounts, stocks, uncashed checks, insurance benefits, wages and safe deposit box contents. Real estate is excluded. Search by Last or Business Name, First Name and City or ZIP, or by Property ID. Active escheated properties have a +CLAIM button. Pre-escheat Notice properties have an INFO button showing holder contact information and a June 1 transfer deadline; an owner can contact the holder directly before transfer. Add multiple properties to the Claim Cart. Select the Claimant Relationship: Myself; Business Officer/Dissolving/LLC/Sole Prop; Heir; Heir-Trust; Heir-Will; Heir-Court Appointed Rep; Heir-Final Decree Distribution; Holder Reimbursement; Government Agency; or Bankruptcy Trustee. Complete the three-step eClaim form. Step 1 collects contact information, SSN and date of birth. Step 2 is an electronic signature under penalty of perjury. Step 3 presents a claim summary with Claim ID and a confirmation email within 24 hours. Upload verification documents through Upload Claim Documentation, with up to five files per batch in PDF, JPG or JPEG format, each between 1 KB and 15 MB. Document types include ID, SSN, Proof of Reported Address, Death Certificate, Trust/Will/Probate Decree and Investigator Agreement. Check status at ClaimIt.ca.gov or call 1-800-992-4647.

#### [083] Table of Heirship Tutorial

- Source: https://www.youtube.com/watch?v=cMCrrRkehJk
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [083] [00:00:00](https://www.youtube.com/watch?v=cMCrrRkehJk&t=0s) — “Welcome to this tutorial on how to complete the Table of Heirship Form located on the California State Controller's Unclaimed Property Website. To navigate to the Table of Heirship form from the State Controller's Office website, click on Unclaimed Property. Next, click the link for Claim Filing Instructions and Forms. Lastly, scroll down to the bottom of the page, and click the link for the Table of Heirship form. The Table of Heirship Form is used for Heir claims, where the owner passed intestate, with no Will, Trust, or other Estate Plan, and Probate was”
- [083] [00:03:22](https://www.youtube.com/watch?v=cMCrrRkehJk&t=202s) — “a second Table of Heirship Form to add the additional names. At the bottom of the form, print your name in the first box, and sign in the second box. In signing this form, you declare the information provided on this form is true under penalty of perjury. A notary is not required on this form. If you have any questions, please contact the State Controller's Office by phone at 800-992-4647. Our Call Center is available 8 a.m. to 5 p.m. Pacific Time, Monday through Friday, excluding state holidays. The California State Controller's team is committed to helping rightful owners receive”

#### [084] $200,000 California Foreclosure Heir Claim Case Study

- Source: https://www.youtube.com/watch?v=MiiGrCZZAZk
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [084] [00:00:00](https://www.youtube.com/watch?v=MiiGrCZZAZk&t=0s) — “Hey, what's up, YouTube? Welcome back to my page, Money Making Juggernaut. I'm your host, Eric Richardson, the number one educator in the asset recovery business. Today, I'm going to provide a case study. Just got paid out on a $210,000 claim. This was in the state of California on a mortgage foreclosure, which is non-judicial. For those of you who do non-judicial, so you have to basically be a foreclosure consultant, or you have to go through a law firm to have the claim filed. Also, mortgage foreclosures being non-judicial, you're going through a”
- [084] [00:01:15](https://www.youtube.com/watch?v=MiiGrCZZAZk&t=75s) — “guys know, that is the industry. All right? This isn't a get-rich-quick scheme. It does take time, but it's well worth it. I mean, 25% of 210,000, that's over $50,000. So, it's well worth the wait. Now, on this case, this was a beautiful home in the state of California. All right? This was in Contra Costa. And this took 9 months for us to recover. And the reason is, in California, opening a probate does take some time. All right? We reached out to the client. We informed them that there was a surplus. We asked them if they had a”

#### [086] Amador county Tax Sale Surplus Funds Case Study

- Source: https://www.youtube.com/watch?v=4-lZwuXtY6Y
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [086] [00:00:00](https://www.youtube.com/watch?v=4-lZwuXtY6Y&t=0s) — “This is a case study for an Amador County, California tax sale surplus funds. We were able to get $25,898 on this claim. As you can see here, we got paid directly from the county. All right? Company's name is Prestige Family Assets Group. And we assist individuals filing for surplus funds due to non-payment in taxes or mortgage. In the event of this foreclosure, if the property sells for more than what was owed, that is going to result in a surplus. We were able to identify the surplus, identify who's actually entitled, assist them on”
- [086] [00:03:19](https://www.youtube.com/watch?v=4-lZwuXtY6Y&t=199s) — “contact the county. After that, we had to follow up with the county, all right? So, on this one, since we didn't have to wait a full year because a lot of time already elapsed, we only had to wait, I mean, we ended up They They actually cut the check while we're following up. I mean, we ended up receiving the check. I think it was like September 13th, and they cut that check like August 28th. And we were able to file I think that was like late June. So, we didn't have to wait a long time. A lot”

#### [087] How To Become a Surplus Funds Expert FOR 1 COUNTY (Asset Recovery Business)

- Source: https://www.youtube.com/watch?v=FNbqvZGEzeE
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [087] [00:00:23](https://www.youtube.com/watch?v=FNbqvZGEzeE&t=23s) — “is it is very important for you to become an expert in the county that you wish to work surplus funds I mean think about it these people are trusting you to file a claim for them in the county that they have no idea about so why would they trust somebody who has no idea about it in this video you're going to learn exactly how to become an expert when it comes to being an expert in a county your first step is going to be understanding their sales information we should know when they are having their”
- [087] [00:01:48](https://www.youtube.com/watch?v=FNbqvZGEzeE&t=108s) — “entitled to Surplus a great way to show them is that the property sold for a higher amount so once we get that first step done we've established how and when the counties are having their sales we now now want to see if they have claim instructions check to see what is required for a successful claim do they need a copy of the deed do they need a copy of the driver's license do they need a utility bill these are all items that you should check and see exactly what's necessary now to find this the”

#### [088] How to start a Surplus Funds Recovery Business in 2026 (for beginners)

- Source: https://www.youtube.com/watch?v=suJSu-vn6yI
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [088] [00:00:00](https://www.youtube.com/watch?v=suJSu-vn6yI&t=0s) — “In this updated 2026 video, I'll show you how to start a surplus funds recovery business in 2026, even if you're a complete beginner. Starting a surplus funds business in 2026 is easier than it has ever been, and I know that because I've been doing this business since 2018, and I've recovered over 100 million in surplus funds. And the process that I've built has allowed me to become a multimillionaire using the same system that I'm going to walk you through. I've updated the system to what is currently happening in the market,”
- [088] [00:01:04](https://www.youtube.com/watch?v=suJSu-vn6yI&t=64s) — “end of this, you'll have everything that you need to launch your own surplus funds recovery business and get to your first $10,000 check, or even $100,000 check. Before we talk about how this business is built, you need to understand what surplus funds actually are. Because if you can't explain this simply to a client within 30 seconds, you're not going to even close any deals. Here's the simple version. When a homeowner falls behind on their property taxes or they default on their mortgage, the county or the bank has the right to”

#### [089] Surplus Funds Recovery Cold Calling - STEP-BY-STEP SCRIPT

- Source: https://www.youtube.com/watch?v=DMdtmrWAO6c
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [089] [00:10:20](https://www.youtube.com/watch?v=DMdtmrWAO6c&t=620s) — “your mouth could ever say. And before I show you that, really quickly, if you want help starting your surplus funds recovery business, you should consider joining the surplus funds profit system. My signature program where my team and I, we're going to help people just like you close surplus funds deals. Even if you are a complete beginner, you get daily surplus funds list with fully skip trace leads so that the numbers are ready to call. Step one is basically done for you. You get weekly live training calls, an attorney network ready to work with you on a contingency”
- [089] [00:17:18](https://www.youtube.com/watch?v=DMdtmrWAO6c&t=1038s) — “to give you very specific sales advice. All right. Now, this is very good if you are a beginner. But here's the thing. Code calling is only one piece of this puzzle. You still need to know where these leads came from in the first place, how to research the leans on a property, and how to actually file the claim and get paid. So, watch this next video. All right. This is a full 45minute surplus funds master class and it walks you through the entire business step by step from pulling your very”

#### [090] Surplus Funds Recovery: COMPLETE Document List (2026 UPDATE)

- Source: https://www.youtube.com/watch?v=MVCNlj7HQBQ
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [090] [00:03:16](https://www.youtube.com/watch?v=MVCNlj7HQBQ&t=196s) — “all the research. But in 2026, you can go to ChatGPT or Gemini and type in anything you want the AI to do for your research. For example, I went to Gemini \[snorts\] and I typed in, "What kind of documents do I need to file a tax overage surplus claim in Alachua County?" And guess what? A surplus funds recovery agent helping out a client to recover these funds, it gives me all the details. They gave me a complete list, and they provided the source so that I know that this came directly from the”
- [090] [00:08:42](https://www.youtube.com/watch?v=MVCNlj7HQBQ&t=522s) — “connects the two names. It's called an attestation of identity. You need the county's claim form. You need to make sure that it's the same claim form that is accurate. You might also need a W-9 because almost every county in America wants one before they actually cut the check. You'll need the case number. You'll need the sale date. You'll need the sale amount because that's the anchor. Everything else attaches to that information. And you need proof that the surplus even exists. And to prove that you need a simple notice of surplus”

#### [091] Surplus Funds: Owner Died - STILL CLAIM!

- Source: https://www.youtube.com/watch?v=1N1Z99kUvRw
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [091] [00:03:34](https://www.youtube.com/watch?v=1N1Z99kUvRw&t=214s) — “survivorship first so with joint tenants with the right survivorship the number one factor is the date of death guys here's an example Barry and Elizabeth Hurley bought the home January 1st 1998 as joint tenants with the right survivorship you see a lot of that Barry dies March the 1st 2023 his ownership would transfer at that point no need for a state no need for probate the deed said husband and wife literally Elizabeth could walk down to the court with a death certificate and prove that she's a sole owner of the property”
- [091] [00:04:40](https://www.youtube.com/watch?v=1N1Z99kUvRw&t=280s) — “because of the rights of survivorship did not kick in until after the property was lost so it didn't happen is the transfer of his portion to her didn't happen very important you understand it date of death is everything if the property was foreclosed on March 2nd Barry's ownership passed to Elizabeth the day before when he died at his death so Elizabeth since it passed completely to her the day before the foreclosure she gets all the Surplus you don't have to worry about probate or estate big deal now here's where it gets wacky”

#### [092] CA Unclaimed Property - Are you missing out? - Tutorial

- Source: https://www.youtube.com/watch?v=ijLtjR0tTd8
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [092] [00:01:54](https://www.youtube.com/watch?v=ijLtjR0tTd8&t=114s) — “forwarding address. In some cases, \[music\] the owner dies with the heirs who have to have with the heirs who have no knowledge of the property. What efforts are made to find property owners. California law requires all holders, corporations, businesses, associations, financial institutions, and insurance companies of unclaimed property to attempt to contact owners before reporting their property to the state controllers's office. Holders are required to send a notice to the owner's last known address informing them that the property will be transferred to to the state controllers's office for safekeeping if the owner does not”
- [092] [00:03:39](https://www.youtube.com/watch?v=ijLtjR0tTd8&t=219s) — “next page. Probably something like get your unclaimed property. And it says search for unclaimed property. Let's go ahead and read some of the text that's on the upper left. It says to begin your search, enter your last name or the name of your business. To better refine your results, you may also enter your first name. Exact name matches will be shown first property for individuals with similar names to the name you entered will \[music\] follow. Says this is a free and secured service provided by California unclaimed property to claim your lost funds. Once you found the”

#### [093] California Unclaimed Funds: What You Need To Know To Be A Property Investigator #unclaimedassets

- Source: https://www.youtube.com/watch?v=xAiBXreoVY0
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [093] [00:00:01](https://www.youtube.com/watch?v=xAiBXreoVY0&t=1s) — “Unclaimed funds California, here's what you need to know. As of 2024, there is 13 billion dollars in unclaimed funds that are sitting at the state level. There's also 76 million active accounts, which means you will never ever ever run out of deals to chase. The state has a 10% commission cap. They also offer you pre-drafted work agreements, so you don't have to ever worry about getting signed or looked over by an attorney. The state also gives you leads. You can literally go download them right now. So, it makes it really easy for you to skip trace”
- [093] [00:00:41](https://www.youtube.com/watch?v=xAiBXreoVY0&t=41s) — “them in bulk, upload them into an auto dialer, and start calling everybody in town. But, that's what you need to know for the state of California. I also have a little freebie for you. It's sitting in the comment section. Go check it out.”

#### [094] How To Become An Unclaimed Property Investigator

- Source: https://www.youtube.com/watch?v=TTMtgtc31k4
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [094] [00:01:24](https://www.youtube.com/watch?v=TTMtgtc31k4&t=84s) — “you're an unclaimed property investigator so let's get into it the very first thing is what is an unclaimed funds property investigator okay a recovery agent also known as a property investigator or Hef finder is a professional or a company that specializes in helping individuals or entities locate and recover unclaimed funds or property these agents play a critical role in reuniting rightful owners with their unclaimed assets often for a fee or percentage of the recovered amount so here's a detailed overview of how the whole process works number one research and identification we got to go”
- [094] [00:02:46](https://www.youtube.com/watch?v=TTMtgtc31k4&t=166s) — “identifiers like names addresses and other personal information number two contacting potential claimants okay we call this skip tracing or Outreach Once A match is identified unclaimed property investigators contact the potential claimants through mail phone calls or emails they inform the claimants about the existence of unclaimed funds or property and offer their services to assist in the recovery process that's number two okay number three verification and documentation okay verification unclaimed property investigators help claim it verify and identify the right to the unclaimed property this may involve Gathering necessary documents such as”

#### [096] Mastering Unclaimed Funds Contracts: A Complete Beginners Guide

- Source: https://www.youtube.com/watch?v=_RTcaTMOwlY
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [096] [00:04:27](https://www.youtube.com/watch?v=_RTcaTMOwlY&t=267s) — “drafted this agreement and like I had to have this eight-page document." And he's like, "No, all you need are the legally binding aspects of an agreement." And so I've gone and done all the hard work, you guys. For most of the states that you're going to work in that don't give you an agreement that they've pre-drafted. If they give you any agreements at all or offer them that they've pre-drafted, don't use something like this. Okay, always do exactly what the state department's outline and what they give you. But there are a lot of the states”
- [096] [00:11:30](https://www.youtube.com/watch?v=_RTcaTMOwlY&t=690s) — “to cut you a check to or they're going to cut the claimant a check and then you're probably going to be invoicing them. All right, so it's important that you get the right address because last thing you want to do is add any more time to being able to invoice them um so you can get paid. You know, you don't want them to send the check to an old address or the incorrect address. You know, you want to make sure that's right. And you know, when these claimants, when they do when they're in”

#### [097] Michigan Unclaimed Property - This is How You Make an Unclaimed Property Claim

- Source: https://www.youtube.com/watch?v=Fn04U_Yfuzg
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [097] [00:00:02](https://www.youtube.com/watch?v=Fn04U_Yfuzg&t=2s) — “hello everyone and welcome to another video from forgottenloot.org and in this video we're going to look at michigan we're going to see how we can um file or claim unclaimed property from michigan now uh we're on the michigan website and as we can see over 400 million dollars has been paid out in the last five years um to citizens of the great states of michigan um if you have worked up lived or have family members friends that live uh reside in michigan then please share this information with them um don't forget to share forgottle.org”
- [097] [00:04:50](https://www.youtube.com/watch?v=Fn04U_Yfuzg&t=290s) — “um first name last name you don't have to put middle name date of birth email address confirm the email address phone number social security number tax id county address cities state and zip code once that's filled out simply press the next button this is the three step form so enter the claim info uh preview the claim then you go to claim summary and then you submit once you finish right so that's how you would um enter a clean um in the state of michigan if you have worked lived in the state of michigan if you”

#### [098] State Funds California: Registration Process & Requirements To Work Unclaimed Funds.

- Source: https://www.youtube.com/watch?v=_8vyoTSh7Rs
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [098] [00:02:09](https://www.youtube.com/watch?v=_8vyoTSh7Rs&t=129s) — “I'm gonna show you guys how to register to work on claim funds, and the state of California... The first thing you'd wanna do... From a Google search bar, just type in California unclaimed property. 0:02:22.6 S2: Now, if you wanted to work in Delaware is put in Delaware on claim property or New York, whatever it might be. But Google's pretty good, you guys... They're pretty good at predicting exactly what you want, and so this is the correct website right here, just do... So CDOT gov, it right here. Okay, now what doesn't matter if you're trying to register for the State”
- [098] [00:03:29](https://www.youtube.com/watch?v=_8vyoTSh7Rs&t=209s) — “0:03:30.6 S1: Okay, so unclaimed property. Let's go down here for this. Okay. 0:03:35.9 S2: Hangover, handbook and forms. Now, it doesn't matter if you're in the state of California or wherever, they are probably gonna have some instructions on what you need to do now, they might not have a handbook, but there will probably be a link or a tab on the website that you can click on, they'll give you all that information you need, now you guys, if it's not on the very first page, right when you hit the main website,”

#### [099] State Funds Tutorial Delaware: Registering As A Property Locator For The State Of Delaware.

- Source: https://www.youtube.com/watch?v=TTfaOSBvLDc
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [099] [00:02:01](https://www.youtube.com/watch?v=TTfaOSBvLDc&t=121s) — “one of the big cheat codes is just go to the NAPA org website, from there, there'll be a site map, you can click on any Stein USA, and it'll take you right to the UN claim funds department website. 0:02:14.7 S1: So if you guys are brand new and you guys might not want to be working in Delaware, but somewhere else, that's the very first step, second step is figuring out... They have an investigator handbook, the State of Delaware gives you a lot of information. Okay, so right here, you guys... And this is just a very quick search I did on the website”
- [099] [00:11:24](https://www.youtube.com/watch?v=TTfaOSBvLDc&t=684s) — “0:11:26.0 S2: Now, I do have a couple of links down here, the very first one is the process for how to submit a claim, and... So that's gonna take you through step-by step exactly what you need to do in the state of Delaware to submit a completed claim package. 0:11:42.8 S1: Now, I know a lot of the deals that you guys are chasing after, sometimes they involve dead people, and a lot of the states you're gonna have to require... Will require thus certificate. And so down here is the website for the state of Delaware,”

#### [100] State Funds Tutorial New Mexico: How To Register As A Property Locator In The State Of New Mexico.

- Source: https://www.youtube.com/watch?v=6yIKsJMj6Gk
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [100] [00:00:00](https://www.youtube.com/watch?v=6yIKsJMj6Gk&t=0s) — “0:00:00.0 S2: Hope you're doing well. My name is David Wilkerson, and this is surplus funds 101. In today's video and in estate funds tutorial, I'm gonna be sharing with you guys everything you need to know about New Mexico, everybody always wants to know, How do I register for a state? How do I call the state departments? How do I know where to work? How much am I gonna get paid? When am I gonna get paid? So on and so forth. And in this video, I'm gonna share it all with you. Before I get into that though, I”
- [100] [00:01:34](https://www.youtube.com/watch?v=6yIKsJMj6Gk&t=94s) — “Okay, now for all you guys that are brand new, they're still kind of unclear about how you'd even go find the website to get the information from here is a little tick sheet, rapallo on what to do is the very first thing. You just go to Google search, and 0:01:50.1 S1: In that search bar, you type the State's name followed by unclaimed funds, so you are researching Mississippi, it would be Mississippi on claim funds, and usually the very first two or three things are gonna pop up is gonna be the state website or the website that you're looking for.”

#### [102] State Funds Tutorial Virtual Assistants: Top 3 Hiring Mistakes While Growing Your Surplus Business

- Source: https://www.youtube.com/watch?v=ASO1JUOWTjA
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [102] [00:00:00](https://www.youtube.com/watch?v=ASO1JUOWTjA&t=0s) — “0:00:00.0 S1: My name is David Wilkerson, and this is surplus funds 101. In today's state fund tutorial, I'm gonna be sharing with you guys some virtual assistant hiring mistakes. Okay, I have a few virtual assistants right now that help me out, and my gosh, it has been a blessing, the weight that has been lifted off my shoulders, it's been great, but throughout that process of hiring virtual assistance have fired a few of them and I've learned a few things, and now that I have a coaching program and other people are starting”
- [102] [00:01:56](https://www.youtube.com/watch?v=ASO1JUOWTjA&t=116s) — “okay, they go out and they get all excited about going and hiring a virtual assistant, they either go to online jobs, Ph dot com, or some regroup in a Facebook area, and they hire their very first virtual assistant. Doesn't work out for him. And so here are some of the things that they don't do that I do. 0:02:15.9 S1: That has really, really helped out. But one of the things is they don't require the virtual assistants to send in a video sample of them reading the script, so they make a job post looking for virtual assistants to help them with their unclaimed funds business”

#### [104] State Funds Tutorial: Cold Calling Objections vs. Complaints. Surplus Funds 101

- Source: https://www.youtube.com/watch?v=t4w_wFimZ9A
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [104] [00:05:24](https://www.youtube.com/watch?v=t4w_wFimZ9A&t=324s) — “the very first time, so many complaints... You kindly ignore it. 0:05:29.4 S2: Complaints come out subconsciously from people all the time. Again, I encourage you guys to just pay attention to the conversations you have and just listen to all the compliance and negativity that people say without them even really putting a strong emotional value on it, so the very first thing is you just kinda ignore it. They bring it up a second time, mildly, address the issue and then side step it, and then turn back into the conversation that you originally happen with them.”
- [104] [00:07:10](https://www.youtube.com/watch?v=t4w_wFimZ9A&t=430s) — “clearing objections and complaints before they come up... Okay, one of the best things you can do as a sales person, if you think or if you know that there's three or four different objections that are always gonna get brought up in a conversation or during a presentation, you be the one to bring them up and you have pre-canned ways to overcome all those things. 0:07:34.4 S2: So bring up all the objections that client has and resolve all of those potential issues that might stall a deal 0:07:43.3 S1: Guy, this is how you're gonna wanna start clearing objections,”

#### [105] State Funds Tutorial: How To Make Cold Calls If You Have A Full Time Job.

- Source: https://www.youtube.com/watch?v=JmuqGo9wYkg
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [105] [00:00:30](https://www.youtube.com/watch?v=JmuqGo9wYkg&t=30s) — “30 minutes to go get my kid then i got another hour commute to get back home i cook dinner and then i gotta do all this other stuff and my kids need my my time my kids need mom time and that's completely valid you know that's a very very legitimate excuse you know i remember when i was getting started in the high ticket consulting world you know aka asset recovery again big chunks of money up front you know i was super busy the only time that i had was saturdays and”
- [105] [00:03:02](https://www.youtube.com/watch?v=JmuqGo9wYkg&t=182s) — “you guys know that you have to prospect you know you have to make phone calls and so it doesn't matter what your schedule is like just make your calls around your schedule it's okay to start off small and not go take over the world right out of the gates you know but just make a couple phone calls every single day and just keep at it you know it's okay to go slow but it's not okay to not do anything okay but with that being said you guys go out there and crush it”

#### [106] State Funds Tutorial: What To Do When A Deal Cancels While Working Your State Funds Business.

- Source: https://www.youtube.com/watch?v=foMCyYJ4LgY
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [106] [00:00:00](https://www.youtube.com/watch?v=foMCyYJ4LgY&t=0s) — “0:00:00.5 S1: And this is surplus funds 101. In today's video, I'm gonna talk to you guys about something new, but wants to think about or talk about its cancellations, and you know it's something that you guys can't get around, you if you've been doing this business for a long time or been in any sort of high volume sales, you would probably be the first person to raise your hand say, Oh yeah, you know, cancellations are part of the business, and so you guys... Cancellations or something, you guys can't get around, and it's not always”
- [106] [00:01:01](https://www.youtube.com/watch?v=foMCyYJ4LgY&t=61s) — “it. 0:01:02.0 S1: And if you guys haven't gone and gotten my free any course, there's a link in the description, you guys can click it, it's an instant access product, and you just can learn in training right away. I know a lot of you guys are brand new. You guys might not know what to say, who to talk to or what to do first, so this is gonna give you the exact step-by-step system on exactly what you need to do in order to go and get your very first deal done right. Now that being said, let's get to the content. Okay, so the”

#### [108] Unclaimed Funds Tutorial: Cold Calling Basics For Your Unclaimed Funds Business. state funds.

- Source: https://www.youtube.com/watch?v=XHOqG0CY1KA
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [108] [00:13:28](https://www.youtube.com/watch?v=XHOqG0CY1KA&t=808s) — “really hone in on one thing what i would suggest is pick one niche either state funds surplus funds tax bankruptcy and then just do it in one state and then crush it i mean there is so much money in all the municipalities nationwide to where you will always have work to be done but that just makes it really easy especially when you're brand new you know you want to keep it as simple as possible while you're learning and another thing is quality conversations will always outweigh quantity you know the people that you”
- [108] [00:14:28](https://www.youtube.com/watch?v=XHOqG0CY1KA&t=868s) — “first phone call but after doing this for a while i know what to expect what i'm trying to get is this you guys don't give up on leads after the very first follow-up you know some people you gotta call them a dozen times some people you gotta call them for six months you know it seems like the more follow-up that's involved with a certain leader account the bigger the payday is but regardless guess follow-up is crucial follow-up and just asking for the business but other than that you guys when it comes to”

#### [109] Unclaimed Funds: How to Get Your Client's Documents in Order⚡️Unclaimed fund Client Document finding

- Source: https://www.youtube.com/watch?v=1AMk1-SB5ic
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [109] [00:00:25](https://www.youtube.com/watch?v=1AMk1-SB5ic&t=25s) — “get me what you need what I found is that I had 20 documents and I started getting these papers in some would be mail some would be email and it's like oh this one goes here as a complete and I had this checklist and it was it was chaos what I do now is I send a checklist of everything I need from my client that really helps out let's say I need five items I need a contingency agreement I need an assignment of Interest I need a power of attorney I”
- [109] [00:01:10](https://www.youtube.com/watch?v=1AMk1-SB5ic&t=70s) — “and you get it mailed to you and you have all the documentation you need if my client is missing a documentation but they'll give me most of what they have I'll go and I'll take that but I try not to do that because what ends up happening is I have a hard time getting that back in the system it's like a broken system and you're trying to get it back in cuz it's it's incomplete I'm not saying don't do do it I'm just saying don't make it a habit try to get”

#### [110] Claiming your Unclaimed Funds

- Source: https://www.youtube.com/watch?v=GrE0UUh_3BI
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [110] [00:06:15](https://www.youtube.com/watch?v=GrE0UUh_3BI&t=375s) — “money today so in unclaimed funds we have uh last year in 2023 we processed 40 we paid out 43,000 claims and we returned over $139 $130 Million last year and so for today we're going to go over what exactly is unclaimed funds the three easy steps to claim them the timeline and how you can look up the status of your claim so most people wonder what are unclaimed funds unclaimed funds are lost or forgotten monies and inactive accounts uh businesses are required to report those to the uh division of unclaimed funds every year and we keep”
- [110] [00:07:52](https://www.youtube.com/watch?v=GrE0UUh_3BI&t=472s) — “providing us with the right information to verify you are the rightful owner and then step three is just to send us your claim it's that easy so when you go to our uh our site um at unclaimed funds or missingmoney.com or you can go through uh unclaimed funds uh.com and find uh and search for uh your missing money but the first step is missing money that site is legit uh we we back that site several States you can actually search for money uh through I think at least 30 to 40 different”

#### [111] How To File a Claim - PA Treasury Unclaimed Property Tutorial

- Source: https://www.youtube.com/watch?v=eRjGqaIOHWI
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [111] [00:00:03](https://www.youtube.com/watch?v=eRjGqaIOHWI&t=3s) — “hello everyone in this video I'll cover the process of filing an online claim via our website here's the main screen for our site first go to patreasury.gov and click programs on the menu bar then click unclaim property on the drop- down menu then select start your search next click the search now button displayed here the green gives you an idea of how far you are in the claim submission process the online process for finding unclaimed property is simple plus if you file online your claim may be eligible for our automated approval process that”
- [111] [00:05:59](https://www.youtube.com/watch?v=eRjGqaIOHWI&t=359s) — “presented with the ability to generate a PDF of your claim form then a paper claim form is required you can fill it out sign and upload the claim form online you'll receive an email of the claim form as a PDF along with a list of two options to either upload a completed claim form to our website or print and mail the claim form to our PO Box however if no PDF is presented that's good news it likely means that no paper claim form is required for the claim to check the status of the claim”

#### [113] Ohio Unclaimed Funds: How to Claim Your Cash in 3 Steps (HB 96 Deadline Explained) Webinar 2-5-2026

- Source: https://www.youtube.com/watch?v=8nmo4S1v3Co
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [113] [00:14:57](https://www.youtube.com/watch?v=8nmo4S1v3Co&t=897s) — “the ones who get approved quicker and sooner rather than having to wait longer for us to review everything um that you've sent us. And so you if you've been wondering what are the steps to claim my money, it is three steps. So just like with Maryanne and Fred, the first step is to search your name to see if you have any funds. You'll generate a claim form and then that claim form you'll have required documents to review and then you submit those documents to us on our website. On the next screen I'm going to show you a”
- [113] [00:18:33](https://www.youtube.com/watch?v=8nmo4S1v3Co&t=1113s) — “And you'll fill out this check box and do an electronic signature to submit that form. And on the next screen, so once you submit that form, congratulations. You've completed the first step to claiming your funds. So you are not finished. You will still need to review those required documents on your claim form and provide them to us. And on the next screen, Marlene will kick us off in walking you through steps two and three and showing you how to check the status of your claim. &gt;&gt; Hello, I'm Marlene Chuks, the deputy”

#### [114] Watch our Demo on How to Claim Your Ohio Unclaimed Funds

- Source: https://www.youtube.com/watch?v=o1cc3hUtIv4
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [114] [00:09:39](https://www.youtube.com/watch?v=o1cc3hUtIv4&t=579s) — “to submit your claim. So, here are some things you're definitely going to need. You're going to need an unexpired government ID. You're going to need a social security card and you're going to need proof of either you had a business relationship with the person the business that sent us the funds or you're going to need proof of the address that reported. So those are things that we're going to actually always always need. So, let's just say we got our claim form and you've sent you sent in all the correct information and we're going to go back”
- [114] [00:11:11](https://www.youtube.com/watch?v=o1cc3hUtIv4&t=671s) — “in your claim ID number here and double check that you put the correct number in um when you're searching for your claim. And I need to go back and get my claim ID number. Or you can scroll. You can scroll down. So there's also when you get your claim, if you have your documentation, you can take a picture with your phone. You can scan it in and you can upload your documents. Right? So up here it says upload claim documentation. Click click on upload. It's very important your claim ID number. At the top, it'll say please”

#### [115] What Documentation is Needed for Unclaimed Funds

- Source: https://www.youtube.com/watch?v=dFKMkAIKskU
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [115] [00:04:35](https://www.youtube.com/watch?v=dFKMkAIKskU&t=275s) — “terms of ourselves we need the same information and you would you would need to First identify that your loved one actually own the property they actually own These funds that are here with us so the same documentation would be needed in terms of proof of business relationship with the company or proof of the last reported address um we will need some additional documentation and that would include maybe a death certificate uh and we need to verify that you are the next of can and that usually requires that you go to”
- [115] [00:07:58](https://www.youtube.com/watch?v=dFKMkAIKskU&t=478s) — “the mail within 14 business days from the time we process from the time we gather everything they will get that check in the mail um and then if they can even check on that they can say you know has that check gone out and we can give them that information so that they can be looking for that check in the \[Music\] mail there is always money out there you never know you never know someone could have left you something that you didn't even know about so please continue to check there's always money there we have”

#### [155] 🚨 Probate Property Headed to Foreclosure Auction… Is It Worth Pursuing?

- Source: https://www.youtube.com/watch?v=T2gvkByDlFU
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [155] [00:00:40](https://www.youtube.com/watch?v=T2gvkByDlFU&t=40s) — “of the traditional ready to go um sort of the probate. So, I just wanted to get maybe some ideas, your approach, how you might approach um something that's in probate, but then also up for auction. &gt;&gt; You say for auction, do you mean because it's foreclosure or do you &gt;&gt; Yeah, foreclosure foreclosure auction. &gt;&gt; Yeah. So, you know, I think the the we get paid to solve problems. You solve bigger problems, you make more money. And so, the fact that it's in foreclosure wouldn't cause me to back off. I think I would want to”
- [155] [00:01:39](https://www.youtube.com/watch?v=T2gvkByDlFU&t=99s) — “done. So, again, I I don't know the laws in Michigan, but I would say that it sounds like there's an opportunity there cuz people have a problem. And if you spend some time and design a solution, then you get paid. If that makes sense. &gt;&gt; Yeah, um it does, right? It's just maybe it's a limiting belief that I have, but yeah, I would always just skip over those cuz I'm always looking for the PRs right that &gt;&gt; I would like to hear the sound of the gunfire. If there's a problem there,”

## Domain 5: Curative Title Investing, Tangled/Heirs’ Property Resolution & Probate Real Estate Acquisition

Primary video assignments: [045], [053], [095], [117], [119], [120], [122], [125], [126], [128], [129], [130], [131], [134], [135], [138], [139], [140], [141], [142], [143], [144], [154], [158], [185]

### 5.1 Curative lead sourcing

**Input:** geographic buy box.
**Output:** ranked curative lead list.

**Ordered procedure (editorial synthesis):**

1. Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates.
2. Separate pre-probate from filed estates and foreclosure-auction probate leads.
3. Match APN to legal description and deceased owner before outreach.
4. Label the title defect: missing probate, fractional ownership, unreleased lien, defective deed or boundary issue.
5. Prioritize by curability, equity, cooperation and evidence quality rather than discount alone.

**Execution and acceptance contract:**

- Persist `ranked curative lead list` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [185] [00:03:51](https://www.youtube.com/watch?v=W0bwM9N_98Y&t=231s) — “hi i'm an investor we're looking to buy real estate right so don't go after the list itself just know that we do have it the great source of new leads for you but let's not actually talk to them about that type of lead uh when you're actually talking to them that's just my only disclosure but that's the difference between a probate and pre-probate deceased owners um our new list got you okay so so what we have on property are the pre-probates not probates okay and absolutely yeah essentially it's um before they go through that probate”
- [131] [00:15:42](https://www.youtube.com/watch?v=sf2hUucsNZ8&t=942s) — “that's essentially what a quick claim a a quick, quiet title action does. That allows a court to determine ownership when there's uncertainty, confusion, or that those competing claims, right? There's different people who were saying, "No, this is my situation." Or this is what I believe. And they're competing towards having that ownership claim. Quiet title actions commonly arise in situations involving tax sale properties. That's probably one of the most common ones that I see. Could be defective or fraudulent deeds, boundary disputes, adverse possession claims, missing or unknown owners, and breaks in the chain of title.”
- [126] [00:00:00](https://www.youtube.com/watch?v=U_Eh790rq3o&t=0s) — “I wonder how many deals are sitting dead in wholesaler CRM right now that are aren't actually debt. Maybe the seller wanted to sell. There was equity. The numbers worked. Then somebody discovered a probate problem, missing error. Maybe an old lean popped up out of somewhere where the payoff was a lot more than the property's worth or they couldn't even find that creditor anymore. Maybe there's some tax lean issues, some other title issue, and the wholesaler moved on to the next league because that's just taking too long, and I like to make a”
- [154] [01:09:10](https://www.youtube.com/watch?v=Dutmzc9gb30&t=4150s) — “you can go and you can talk to, so you can solve a deal and learn. Like, it's great to learn from that JV opportunity because you're just going to keep up picking up more. Um and then, of course, like being able to target the right lead sources for a lot of these, right? There's a lot of ways that people get into this, whether it's tax delinquent properties, pre-foreclosures, absentees, uh code violations. Being able to kind of know where to go, where to start, of being able to pick this up really starts at that lead base of of”

### 5.2 Underwriting and walk-away

**Input:** ARV comparables and defect inventory.
**Output:** base/downside underwriting model.

**Ordered procedure (editorial synthesis):**

1. Estimate ARV from comparable closed sales with explicit condition/location adjustments.
2. Compute maximum acquisition budget = conservative resale value minus repairs, selling/holding costs, lien payoffs, curative legal costs, target profit and contingency.
3. Add heir buyouts and time-dependent financing/carrying costs without double-counting consideration.
4. Run delayed-probate and adverse-lien scenarios; use sensitivity ranges rather than a single optimistic closing date.
5. Walk away if authority cannot be established, necessary interests cannot be obtained, insurability has no credible path, or downside net value is negative.

**Execution and acceptance contract:**

- Persist `base/downside underwriting model` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [132] [00:04:47](https://www.youtube.com/watch?v=FgFrlIpbscs&t=287s) — “know how fast can you get in touch with these people, right? And it's not going to be your scale your your sales skill, things like that. It's just going to be a matter of price then, right? Remember back in the day, wholesaling was 70% the ARV minus repairs, and then all of a sudden the really competitive markets it went up to like 80, 90% with the hedge funds. They were paying over 100% of ARV. So what I don't want you to do is I want to challenge this mindset. I don't want you”
- [187] [00:18:49](https://www.youtube.com/watch?v=ntT8V0gnpAs&t=1129s) — “And just based on these comparables I'm seeing, I would anticipate that a reasonable fair market value would probably be about 5,000 bucks for this one right here. And then property taxes, I'm gonna assume that I'm not paying any back due property taxes. However if I was, I would put that number in here. For purchase closing costs, just as a general rule of thumb, if I'm closing a deal myself in house, I'll usually put like 200 bucks in here. If I'm closing with a title company, I'll put 500 bucks. If I'm closing with an attorney I'll put 1,000 bucks.”
- [158] [00:25:41](https://www.youtube.com/watch?v=ME2xl7cczH8&t=1541s) — “have an heir that's living in the property and their state laws are such that they can't take advantage of Homestead credits that's adding uh costs and complications for them to be able to reside in and um continue to use the property additionally um there is a disproportional amount of airs property that is lost to uh tax sales over time and so this is certainly something our industry has been looking into in terms of advocating for for some reforms to help airs um in this area next if I may add sorry go ahead yeah no go ahead if I”
- [144] [00:56:36](https://www.youtube.com/watch?v=TP6n8TBsCGs&t=3396s) — “Excuse me. We're going to talk about the most common legal structures for holding land. And we're not going to do a deep dive into these, just introducing you to terms so you have some familiarity with them and understand that these are options that for holding heirs' property land, right? So let's talk about trusts first. Sometimes creating a single entity that owns the land in which each family member effectively owns an interest can be a more secure way of owning the property and transferring it to future generations. So rather than each family member owning a share of the land directly, what they own is a share in the entity that owns the land.”

### 5.3 Ten-heir fractional consolidation

**Input:** proved owners and rational shares.
**Output:** fractional-interest cap table.

**Ordered procedure (editorial synthesis):**

1. Build a tenancy-in-common cap table and verify shares sum to one.
2. Track each interest’s chain, encumbrances, spouse rights and transfer authority separately.
3. Price partial interests for lack of control and transaction costs; buying one share does not acquire the whole parcel.
4. Model consensual consolidation before litigated partition.
5. Obtain title review of each deed and updated ownership after each acquisition.

**Execution and acceptance contract:**

- Persist `fractional-interest cap table` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [144] [00:16:07](https://www.youtube.com/watch?v=TP6n8TBsCGs&t=967s) — “It contains legal protections for heirs property landowners that are designed to address the devastating effects of partition sales while balancing the interests of all owners of the property. In order for a partition action to be governed by the UPHPA, the property in question must constitute heirs property as defined under the UPHPA. So this is very specific in the model law that it applies only to heirs property. And the next few slides gives us more detail here. I do want to note here, when you see on here a mention of co-tenant, that the co-tenant is defined as a person having a fractional interest, a fractional ownership interest in the property.”
- [131] [00:06:05](https://www.youtube.com/watch?v=sf2hUucsNZ8&t=365s) — “renting it out. Good for you, Mary. 20 years later, Mary decides she wants to sell her rental property. But the problem is no probate was ever opened. The deed was never recorded transferring ownership from John, her dad, to Mary, his daughter, his heir. Mary may have acted like the owner for 20 years, but the chain of proper chain of title was never properly updated. Now you've got a title problem to solve before the property can be sold. And so that right there, that is one of the most common breaks in the chain of”
- [142] [00:12:21](https://www.youtube.com/watch?v=OODJe43FyEs&t=741s) — “form of ownership where uh multiple people have what's called an undivided interest in the property and in the land. meaning that though \[clears throat\] each person might have their own percentage ownership or fractional ownership, they still have rights to use and occupy the whole thing. Um so what that just as an example you know if one person owns let's say a 3% undivided interest in 100 acres that doesn't mean that they own 3 acres. It means they own 3% of 100 acres and they have the right to access and use”
- [138] [00:17:39](https://www.youtube.com/watch?v=whDzDrFNADQ&t=1059s) — “can buy them out. Or, as really want to buy them out, and if so great, they pay their portion they buy their shares, but the thing is the land still and tenancy in common. So now, you still have heir property you just have heir property, with eight owners, instead of 10 owners. So, at that point, you know you've gotten rid of the owners you've kept the land in the family. But you may not have fix the situation because eventually those eight people are going to pass away their. heirs their children grandchildren whatever are going to inherit the land and then you”

### 5.4 Curative instrument decision tree

**Input:** jurisdiction and title defect.
**Output:** counsel/title-approved curative route.

**Ordered procedure (editorial synthesis):**

1. Use an affidavit of heirship only where law and title underwriting accept it; distinguish evidence of heirship from a conveyance.
2. For Texas, examine statutory evidentiary treatment, recording history and applicable waiting periods rather than declaring any affidavit instantly marketable.
3. Compare summary administration eligibility with formal administration powers and costs.
4. Use quiet title to adjudicate competing title claims with correct parties and service.
5. Evaluate partition and applicable UPHPA coverage, appraisal, cotenant buyout and partition-in-kind preference before planning a forced sale.

**Execution and acceptance contract:**

- Persist `counsel/title-approved curative route` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [139] [00:42:25](https://www.youtube.com/watch?v=59C1meISvlc&t=2545s) — “independent appraisal of property assuming sole ownership of the fee simple estate so buyout provision we talked about the buyout provision uh partition preference this is a big one that we talked about earlier the idea that in theory and law in Louisiana we have a preference for partition and kind but in practice we have a we have a preference for partition partition and sell what this would do is this would codify in law the actual re and Rec codify I guess you'd have to say that we're going to have a preference for”
- [131] [00:15:42](https://www.youtube.com/watch?v=sf2hUucsNZ8&t=942s) — “that's essentially what a quick claim a a quick, quiet title action does. That allows a court to determine ownership when there's uncertainty, confusion, or that those competing claims, right? There's different people who were saying, "No, this is my situation." Or this is what I believe. And they're competing towards having that ownership claim. Quiet title actions commonly arise in situations involving tax sale properties. That's probably one of the most common ones that I see. Could be defective or fraudulent deeds, boundary disputes, adverse possession claims, missing or unknown owners, and breaks in the chain of title.”
- [144] [00:19:27](https://www.youtube.com/watch?v=TP6n8TBsCGs&t=1167s) — “So there's a lot more information and notice under the UPHPA. Now for the independent appraisal requirements of the UPHPA, obviously it's possible that the co-tenants maybe could all agree on the value of the property. But if all co-tenants do not agree on the value of the property, then under the UPHPA, the court will order a disinterested licensed real estate appraiser to determine the fair market value of the property. And that way the property is less likely to be sold at a discount. The right of first refusal or buyout provision under the UPHPA allows a co-tenant who did not request a partition by sale to purchase the property, right?”
- [135] [00:16:13](https://www.youtube.com/watch?v=onebNbNQSBM&t=973s) — “affidavit of heirship from him. You need a probate from him. There's also another issue up the chain they didn't even run up. Title report. And you're over here like, all right, let's look at your deal, but they brought it for a probate. And I'm like, uh how can everybody in Florida go to you for this? Because that's a curative &gt;&gt; It sounds like you've expanded &gt;&gt; Yeah. &gt;&gt; into more of the curative work, which is nice cuz you can have additional projects like the quiet title and the some some of the other stuff.”

### 5.5 Encumbered family home and estate JV

**Input:** loan, successor relationship and estate powers.
**Output:** financing and authority map.

**Ordered procedure (editorial synthesis):**

1. Identify confirmed successor-in-interest procedures under applicable RESPA/TILA servicing rules.
2. Separate servicing recognition from personal assumption of the mortgage debt.
3. Evaluate the specific Garn–St Germain protected transfer exception; not every investor purchase is protected.
4. For Subject-To probate acquisitions, model due-on-sale, insurance, servicing, default and authorization issues explicitly.
5. For estate JVs, verify representative powers, court approvals, conflicts, compensation and distribution waterfall.
6. Document who owns title, who owes the debt and who bears losses at every stage.

**Execution and acceptance contract:**

- Persist `financing and authority map` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [158] [00:50:26](https://www.youtube.com/watch?v=ME2xl7cczH8&t=3026s) — “transfers and said these are the people that are successors in interest and it makes sense right because the lender cannot accelerate the loan based on the transfer in these cases and so we need to let these people get information about the mortgage and deal with the mortgage next slide please so in order to have the protections of the respa and Tila rules and get things like periodic statements and the right to dispute errors and apply for loan modifications you do have to be a confirmed successor in interest and and you are confirmed once a serer”
- [159] [00:34:24](https://www.youtube.com/watch?v=JsPL1vXcgCI&t=2064s) — “wrong and the lender will tell you this is not an assumable mortgage they will tell you that this is not an assumable mortgage what they mean by that is this mortgage has a due on sale clause in it and what you say to them is i know there's a due on sale clause and under the garden st germain act you may not exercise that due on sale clause because this is a family transfer and it's an exempt transfer under the garden stature main act so just be aware that the lender will”
- [082] — supplied storyboard/description reconstruction; no quote timestamp: Controller Malia M. Cohen introduces ClaimIt.ca.gov and explains California Unclaimed Property Law. After three years of dormancy, covered property can include bank accounts, stocks, uncashed checks, insurance benefits, wages and safe deposit box contents. Real estate is excluded. Search by Last or Business Name, First Name and City or ZIP, or by Property ID. Active escheated properties have a +CLAIM button. Pre-escheat Notice properties have an INFO button showing holder contact information and a June 1 transfer deadline; an owner can contact the holder directly before transfer. Add multiple properties to the Claim Cart. Select the Claimant Relationship: Myself; Business Officer/Dissolving/LLC/Sole Prop; Heir; Heir-Trust; Heir-Will; Heir-Court Appointed Rep; Heir-Final Decree Distribution; Holder Reimbursement; Government Agency; or Bankruptcy Trustee. Complete the three-step eClaim form. Step 1 collects contact information, SSN and date of birth. Step 2 is an electronic signature under penalty of perjury. Step 3 presents a claim summary with Claim ID and a confirmation email within 24 hours. Upload verification documents through Upload Claim Documentation, with up to five files per batch in PDF, JPG or JPEG format, each between 1 KB and 15 MB. Document types include ID, SSN, Proof of Reported Address, Death Certificate, Trust/Will/Probate Decree and Investigator Agreement. Check status at ClaimIt.ca.gov or call 1-800-992-4647.
- [046] [00:01:58](https://www.youtube.com/watch?v=U6LsR1gr0oA&t=118s) — “means that they have to use every effort humanly possible to find the missing Heir or beneficiary the California probate courts are reluctant to close a probate Administration unless they are convinced that the personal representative has used every effort possible to find the missing air or beneficiary the following are common methods used to to identify and to locate a missing Heir or beneficiary the personal representative should speak to friends and other family members of the deceased person to determine if they know anything about additional children or offsprings or issues as they're called in the legal”

### Domain evidence workbench

The following source-specific evidence cards expose primary assigned videos without treating lexical matches as verified legal rules.

#### [045] Locating Heirs

- Source: https://www.youtube.com/watch?v=X-Q-bm1y9no
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [045] [00:00:15](https://www.youtube.com/watch?v=X-Q-bm1y9no&t=15s) — “hi and welcome to hullen Hull TV I'm Dana O'Brien and I'm joined by founding partner Ian Hull and managing partner Susanna poit monag at hullen Hall LLP an Innovative Law Firm that practices exclusively in aate trust and capacity litigation here at hullen Hull TV we're exploring the issues around estate planning that affect you Ian and Susanna an executive's duties include locating all heirs who may be entitled to share in the estate what's the best place to start Susanna when we're looking to locate areas what we're really talking about is trying to find those”
- [045] [00:02:23](https://www.youtube.com/watch?v=X-Q-bm1y9no&t=143s) — “then at that point you may have done your your reasonable efforts to locate someone and what happens Ian if an executive isn't satisfied that they've found all missing airs what's the next option well you can uh go to court and get some assistance from the court and the steps that suzanna's talked about we can document them fully and identify this the self-help remedies that you've sought identify the researcher and the researcher will typically file a report in respect of what efforts they've taken even that though the court is going to”

#### [053] Unclaimed Estates & Abandoned Properties in Spain - tracing Heirs Worldwide

- Source: https://www.youtube.com/watch?v=ywaYY4cPtAY
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [053] [00:09:55](https://www.youtube.com/watch?v=ywaYY4cPtAY&t=595s) — “got at least one in the case at the minute where it seems like Sophie, I don't know, property in Nigeria keeps coming up every day on one particular case. We would always investigate it. But and and what what comes first, Ryan? Does the the heir come first or does the property come first? I mean, how does it get to you? I mean, any notification that someone's passed away comes to us first. So that could be in all the various methods that I um explained earlier. But also we are conscious especially if Finders is going to conduct the work speculatively. We are”
- [053] [00:20:13](https://www.youtube.com/watch?v=ywaYY4cPtAY&t=1213s) — “that they need to be instructing dual qualified solicitors like you guys. Um, and then there may be the need for some genealogy at some point to prove who you know the relatives are and to look for missing beneficiaries. But the most important thing is to get your stake in on that property. And I just wondered talking about the restrictions on accessing wills. I was thinking if you're even the most proactive neighbour of someone that's passed away and you want to find out if they left a will um you know you can't just um kind of make your own enquiries because it's”

#### [095] How to Build a Nationwide Notary Team (Step-by-Step)

- Source: https://www.youtube.com/watch?v=Qn63DtrxFts
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [095] [00:00:02](https://www.youtube.com/watch?v=Qn63DtrxFts&t=2s) — “One of the questions that I get on a pretty regular basis is, "Hey Dave, how do I build my notary dream team?" Okay. So, today I wanted to create a short little video and give you some tricks and tips and pointers and things that you can apply to your business to start seeing better results right away. Okay. So, today I'm using Las Vegas as the example and let's just say that you took your leads and you got them all organized and you pulled all the zip codes for all the little cities that”
- [095] [00:03:30](https://www.youtube.com/watch?v=Qn63DtrxFts&t=210s) — “obviously, I'm not going to go and hire any Joe Schmo. I'm going to go and I'm going to take them through my interview process. And if you guys need help with some interview questions, in my contract library, I have my notary interview script and that's um that's going to be in a link in the description. And so, if you guys want that, you guys can take it. But, it's really really easy um when you really look at it and you always want to be recruiting new new notaries. Have everything quadrant it off and you'll be”

#### [117] How I Actually Find Curative Title Leads

- Source: https://www.youtube.com/watch?v=W5g3Gia5jX4
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [117] [00:00:01](https://www.youtube.com/watch?v=W5g3Gia5jX4&t=1s) — “The longer I invest in real estate, the less I believe in some magic list where you'll find all of your deals. And the more I start to believe in this concept of really mastery and understanding real estate, understanding the process, and well, how humans mess it up. And cuz ultimately that's where we make our money, right? In the mess tied to real estate. So, a lot of folks have been saying, "Courtney, I can't I don't know how to find these curative title issues or these ownership issues uh to be able to do a curative title”
- [117] [00:21:18](https://www.youtube.com/watch?v=W5g3Gia5jX4&t=1278s) — “department, I wanted that data she was talking about. And so then I made a FOIA request for it. It could look like you being hyper local with your public records and figuring out patterns. Maybe it's how something gets indexed that you say, "Hey, when this gets indexed, this, you know, instrument type leads me to, you know, often be able to find title issues or ownership issues because of this." Um it could be, you know, a niche search um that no again no one else runs, something that you come stumble across and you say, "Hey,”

#### [119] How to Get Your First Curative Title Deal: A Step-by-Step Guide

- Source: https://www.youtube.com/watch?v=W-FX20iI9Jk
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [119] [00:00:00](https://www.youtube.com/watch?v=W-FX20iI9Jk&t=0s) — “If you want to get your first curative title deal, stop looking for the perfect list and stop worrying about knowing everything, especially the legal stuff before you get started. I want to walk you through in this episode a step-by-step process you can actually follow so you can start building that skill set that makes money in curype. So before we get started, my name is Courtney Fricky. I've been investing for 12 13 years at this point. And since 2017, we're in 20 26 now. So, uh, nine years ago, I started doing curative”
- [119] [00:14:30](https://www.youtube.com/watch?v=W-FX20iI9Jk&t=870s) — “presume vacancy, right? Or maybe it was very obviously occupied. Um, that's important. That's an important factor for me. And then I want to look at the the current owner of record. So that's going to be again the tax assessor site. I want to look up, you know, who owns 123 Main Street. So, I'm going to put their first and last name. And maybe it's more than one person, you know, but it's also important to know, is it an individual? Is it like an LLC? Is it a trust? And then I want you to have some”

#### [120] How to Underwrite a Curative Title Deal (And Know When to Walk Away)

- Source: https://www.youtube.com/watch?v=-QzABvCmtVc
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [120] [00:00:54](https://www.youtube.com/watch?v=-QzABvCmtVc&t=54s) — “side. I'm talking foreclosures, inherited properties, and that means complicated ownership, and title issues. Now, let's go ahead and jump in to the deal. But before we do, today's conversation is important because one of the first steps in learning how to do the curative title deals is to learn how to spot the problems like the title issues and the ownership issues. But the second part of it is knowing which ones are worth solving. Now, let's get into it. This came to me by email. Hey Courtney, I have a deal in Louisiana. I”
- [120] [00:04:01](https://www.youtube.com/watch?v=-QzABvCmtVc&t=241s) — “versus the ARV fixed up because again, we're not underwriting for a flip. So, if you do all the work to resolve the title and ownership issues, what is it worth then that day? The minute you stop resolving that title issue and it's all done, before you did any other work, what would it be worth? What could you offload it for? And I want you to think in that number and train yourself when you're looking at these deals to run that number because again, we're not underwriting for a flip. Sure, you could”

#### [122] How to Find Heirs for a Florida Probate Property

- Source: https://www.youtube.com/watch?v=RmtbOq_vtuU
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [122] [00:01:29](https://www.youtube.com/watch?v=RmtbOq_vtuU&t=89s) — “heirs? You know, who might be the family members? Right? This is John Doe who owns the house. But how do I know if John Doe actually ever produced any children, fell in love, got married, you know, um things like that? &gt;&gt; I think one of the valuable resources if you have the time to do this is going to pull a death certificate could lead to a lot of uh resources for you because on death certificates, first of all, you can order a death certificate in Florida if you're over 18 and you could order”
- [122] [00:02:57](https://www.youtube.com/watch?v=RmtbOq_vtuU&t=177s) — “there that people can tap into that are more on the free side. And then if you need to go to more paid sources like some of the skip tracing, you can. But these are the first steps some people will take out there to be able to find it. And I think the obituaries for some people has been a big one because it'll it'll lead to other people that will lead to other people. Exactly. And a reminder here to anyone that obituaries are not fact checked. So there could be things in there that are wrong. For”

#### [125] Curative Title + Creative Finance: The Combo Most Investors Miss

- Source: https://www.youtube.com/watch?v=DcB4tJku4-A
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [125] [00:22:09](https://www.youtube.com/watch?v=DcB4tJku4-A&t=1329s) — “for example aren't in your buy box to get what you need to then be able to get what you want, which may be for example something in your buy box. Right. &gt;&gt; Right. Um there is so like for example I was talking with people uh you know recently at a curative event and I was saying hey like don't be afraid to take down some of these curative deals. Don't take your profit immediately in the sense of a sale right like to where you're getting a lump amount. Turn them into rentals and they might be shitty”
- [125] [00:24:50](https://www.youtube.com/watch?v=DcB4tJku4-A&t=1490s) — “just need more tools. I need more expertise. And I I just, you know, having financial friends has just been a a godsend to, you know, been very blessed because I had I had the ability to meet these, you know, teachers and mentors and put it all together. &gt;&gt; Yeah. And and and this why it's like important to talk through the fact that none of this stuff is new, not even curative, right? &gt;&gt; Yeah, you're right. &gt;&gt; It's been around for a long time. &gt;&gt; Um creative as well, right? &gt;&gt; Yep. And so what we're talking about”

#### [126] How Wholesalers Can Turn Title Problems Into Profitable Curative Deals

- Source: https://www.youtube.com/watch?v=U_Eh790rq3o
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [126] [00:05:30](https://www.youtube.com/watch?v=U_Eh790rq3o&t=330s) — “with owners and then you had to go find them again because at this point they had you know or you had to to address that. So there's ultimately is understanding. So for anyone who's like, "Hey, well, what's the difference between just working distressed property because distress doesn't equal curative, right? Because ultimately there needs to be something that's stopping it from being able to be sold with insurable and marketable title. So with that being said, with that being said, Steve, um, do you think you've done any deals over the years that you know how to solve”
- [126] [00:09:38](https://www.youtube.com/watch?v=U_Eh790rq3o&t=578s) — “know? Walk me through. &gt;&gt; I think I think they need to know what's possible. So, I think they need to have a basic understanding of like how these issues can be solved, but yes, they don't need the full deep legal understanding. uh and they need who to know, right? So, I think it's it's a bit of how and what's possible, but then it's who like who do I call, who should I speak to, who can do these things, you know what I mean? Like, you're going to need a good succession lawyer. You're”

#### [128] Curative Title Explained: How Investors Make Money When Deals Can’t Close

- Source: https://www.youtube.com/watch?v=GH5TN_iIdMs
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [128] [00:02:42](https://www.youtube.com/watch?v=GH5TN_iIdMs&t=162s) — “curative title. &gt;&gt; Um what when people when you talk about it, how do you define it? &gt;&gt; I've been thinking about this a lot lately and kind of the iteration that I've arrived at now is that there's actually in real estate there's two values. There's value of something that can't get title insurance and something that can because the the the industry standard is when you buy a piece of real estate or property, it needs to come along with title insurance because that title insurance is protecting you and saying, "Yeah, this this is clear.”
- [128] [00:25:42](https://www.youtube.com/watch?v=GH5TN_iIdMs&t=1542s) — “hey this thing has a very reduced value in the marketplace because of something that's wrong with the documentation because that's basically what title is, right? So although it it it wasn't a title issue per se, it was it was a document issue where the it was a seller carryback note that was so poorly drafted that if and that this you know this per note holder wanted to liquidate it and the gap between the value of where it was when I enter the picture and where we ended was about $200,000. Right. significant because the paper was”

#### [129] Curative Title for Wholesalers: How He Turned a Dead Lead Into a Deal

- Source: https://www.youtube.com/watch?v=2agNOU2taXA
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [129] [00:26:04](https://www.youtube.com/watch?v=2agNOU2taXA&t=1564s) — “because because I I I could have not but like I value the relationship cuz like so again the relationship matters and caring about them matters. It's not just hey go do free work for me. I care that they get paid. I care that they get more business. So you know that it flows both ways. &gt;&gt; Well and I I always relate it to like an ATM. You can't always be taking withdrawals. you you've got a deposit as well. Were there any costs that were unknown in in the transaction for you?”
- [129] [00:29:49](https://www.youtube.com/watch?v=2agNOU2taXA&t=1789s) — “buyer louisiana.com and you can always find us at homebyiana.com as well but we we we don't post deals publicly. We don't do that. Uh we you know we acquire some deals ourselves. We do wholesale and assign deals but it's all we don't list them on our website. There's nothing public about it. You need to reach out and need to be trusted and be on our in our in our network. &gt;&gt; Goes back to what we talked about. You got to build relationships, right? &gt;&gt; And so, look, this is why I love deals”

#### [130] How a Curative Title Investor Finds & Solves Deals Others Can't

- Source: https://www.youtube.com/watch?v=5LDDkiUTmXI
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [130] [00:00:00](https://www.youtube.com/watch?v=5LDDkiUTmXI&t=0s) — “Curative title deals don't always have to die because there's a title problem that can't be solved. Sometimes they die because the deal stops moving. People stop working them. An heir stops answering. You can't find somebody. Your research hits a dead end. You've called, texted, mailed, skip traced, built out a family tree, hired a private investigator even, and nothing is working. Most inve- investors eventually label that person as unreachable, and they kind of move on. But my guest today has built a big part of his curative operation around a different question.”
- [130] [00:31:59](https://www.youtube.com/watch?v=5LDDkiUTmXI&t=1919s) — “moving? What else could, you know, help me solve it? What haven't we tried? Or maybe, you know, is it who do we need to talk to?" &gt;&gt; Yeah. &gt;&gt; But, you still need to ask, "Is this an opportunity worth solving?" like we talked about. And that's a skill that goes beyond like that's a huge skill set in the cure of title space. So, Carl, I appreciate you coming back on and giving us a look behind the scenes of how you actually work through these problems. Guys, if this is your uh first time”

#### [131] 5 Curative Title Terms Every Investor Should Understand

- Source: https://www.youtube.com/watch?v=sf2hUucsNZ8
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [131] [00:02:01](https://www.youtube.com/watch?v=sf2hUucsNZ8&t=121s) — “actually sell the property. And this is really important. Just because someone name appears on the the tax assessor's website, maybe at the county or parish level, doesn't mean they own fee simple title. Just because they're living in the property doesn't mean they they own fee simple title, either. And just because they're paying on the taxes doesn't mean they own fee simple title, either. Real estate is full of situations where the decision maker and the occupant are not the same person. You know, the people who are you are talking to, it's”
- [131] [00:04:20](https://www.youtube.com/watch?v=sf2hUucsNZ8&t=260s) — “to the next runner. And the chain of title is the baton. You should be able to follow every handoff from start to finish. But if the baton gets dropped, lost, or handed to the wrong person, you've got a problem. So, let's kind of pull this to where the curative issues show up. These Many of these title issues exist because something interrupted that chain of title. So, common examples might include something like an estate, you know, someone died and their estate was never probated. It could be that a deed was never”

#### [134] Differentiating Yourself From The Competition: How To HASHTAG Your ELEVATOR PITCH \| #10

- Source: https://www.youtube.com/watch?v=OrEz4Qk-EZ0
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [134] [00:07:31](https://www.youtube.com/watch?v=OrEz4Qk-EZ0&t=451s) — “local law enforcement and say, listen, we're trying to do a federal search. I mean he could be in jail. And if that PI didn't do a thorough job, I would want to know what he did. What was his exhaustive effort if it was in fact exhaustive, because if he was, if he's on the wrong side of Perino's principle, maybe they didn't get into the federal database and search penal records and he could be in a prison somewhere. If he didn't search nationally for death certificates, he might not be alive. Now at first scrutinized the PI work that you've”
- [134] [00:33:34](https://www.youtube.com/watch?v=OrEz4Qk-EZ0&t=2014s) — “I used on all of my flips. I sold it. I re uh, literally ran the guy out of money, but his balance sheet. Exploded. I ran him out of cash because he was like, I have never, he's we go through three or four realtors a year because they just won't freaking do the work and never bring us the right deals. He's I've never met anyone. Like you, you ran me out of money in three months. I'm like, great. How can we make more? Let me help you scale your contracting business.”

#### [135] Curative Title Explained by a Florida Probate Attorney

- Source: https://www.youtube.com/watch?v=onebNbNQSBM
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [135] [00:02:34](https://www.youtube.com/watch?v=onebNbNQSBM&t=154s) — “talking to. &gt;&gt; How do they know How do they know how to do that? &gt;&gt; Well, one, you can get with the probate attorney, right? And then the other side of it, too, is learning from people like me and people like you in your Texas market and experts that are out there because at the end of the day, a lot of this comes from the statutes. The statutes tell us who's first in line, who's next, and who's after that. Um we just simplify it and make it easy on like who you need to find. But you need”
- [135] [00:16:13](https://www.youtube.com/watch?v=onebNbNQSBM&t=973s) — “affidavit of heirship from him. You need a probate from him. There's also another issue up the chain they didn't even run up. Title report. And you're over here like, all right, let's look at your deal, but they brought it for a probate. And I'm like, uh how can everybody in Florida go to you for this? Because that's a curative &gt;&gt; It sounds like you've expanded &gt;&gt; Yeah. &gt;&gt; into more of the curative work, which is nice cuz you can have additional projects like the quiet title and the some some of the other stuff.”

#### [138] USDA FSA Resources for Heirs: Join FSA as we talk with the Experts (Episode 1-Full Version)

- Source: https://www.youtube.com/watch?v=whDzDrFNADQ
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [138] [00:02:31](https://www.youtube.com/watch?v=whDzDrFNADQ&t=151s) — “opportunity to sit down with the USDA farm service agency, just to provide some guidance as we're looking for this. heirs property program just to roll out, not only the heirs property relending program but also. The different aspects as we talked about the county offices as well, a certified mediation program, we know that a lot of heirs have questions like where to start you know what are some things that. They need to do when they first have found out that they have heirs property. And things of those nature FSA has partnered with different organizations, as well as heirs”
- [138] [00:06:39](https://www.youtube.com/watch?v=whDzDrFNADQ&t=399s) — “up to very unique things so you always end up with a unique problem it's never going to look the same one situation to the next. So that's usually why it's important to have an attorney involved because there's not really a cookie cutter way of doing this. Who does this is going to vary widely depending upon what state you're in some states do have resources that are available to help owners of heir property. some of it with some of the legal work other states, the options may be more limited. Generally, though you're going to be looking for an attorney that's had a little bit of”

#### [139] Law Talks: Heirs' Property 1-21-2025

- Source: https://www.youtube.com/watch?v=59C1meISvlc
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [139] [00:00:51](https://www.youtube.com/watch?v=59C1meISvlc&t=51s) — “again we're here to talk about airs property today with Jonathan Reynolds before getting started I need to go over a few important reminders first first this presentation is being live streamed questions will be taken at the end if time permits permits and answered live if you're watching at a library you may ask or submit your question to the library staff if you're watching via Zoom please submit questions in the Q&A section if you're watching via Facebook please submit questions in the comment section please note that the comments are public and accessible by anyone”
- [139] [01:01:15](https://www.youtube.com/watch?v=59C1meISvlc&t=3675s) — “they are concerned we're trying to develop a program specifically dealing with trust because I'm starting to see if that's what the people want to hear about maybe if you check in again with me 6 months from now I'll be doing one on trust or we'll have someone someone else on law talks doing one own trust okay let's see um another question will I still need a will about my property if I have a Special Needs Trust uh the the simple the simple answer is yes most people will still need a will even if their property is in”

#### [140] Heirs' Property with Jonathan Reynolds of Louisiana Appleseed

- Source: https://www.youtube.com/watch?v=JPgk0Y7ZzuY
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [140] [00:17:45](https://www.youtube.com/watch?v=JPgk0Y7ZzuY&t=1065s) — “actually seen it work but uh in theory when you own this property just because you live on the property just because you're the person taking care of the property just because you're the person paying taxes on the property does not give you the right to exclude your other co-owners uh the reason why I put that after the assessor slide is because that's a one of the major questions that people like to ask and I'm just getting that out of the way right now challenges to heirs Property Owners reasons that you might not want to own a”
- [140] [00:29:44](https://www.youtube.com/watch?v=JPgk0Y7ZzuY&t=1784s) — “relatives so very important to keep track of the library also has archival records uh civil and criminal court records uh and these are very relevant 1920 1926 1931 and the Civil records uh information that you can find uh divorces adoptions adoptions are very important that's a thing we always have to check for when we're doing this kind of thing uh child support notices give you information and the person's mailing address uh criminal records have things that don't necessarily seem relevant at the beginning of your search like date of birth is always relevant Parish of”

#### [141] Heirs' Property 101

- Source: https://www.youtube.com/watch?v=DG4Uhckk-fU
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [141] [00:04:44](https://www.youtube.com/watch?v=DG4Uhckk-fU&t=284s) — “being an asset for the neighbors and community. Right? That's our focus at community progress and it's important and critical work. But this property and so many other vacant abandoned interior interiorated properties like it across the country uh in rural in suburban in urban spaces. It it also though has a history, right? And it's one that we need to understand both in our efforts to address what it has become and to identify what might be done to prevent it from becoming this way in the first place. Right? So along that line, we're”
- [141] [00:16:13](https://www.youtube.com/watch?v=DG4Uhckk-fU&t=973s) — “expensive. Uh it's time consuming and all of those groups need continue to need resources, uh attention and support. Um and so, you know, there's also a lot of great research out there that's been done by a whole lot of other organizations. um the housing and property rights center at Boston College Law, the initiative on land, housing and property rights at Boston College Law, uh academics all over the country, USDA, um national consumer law center, right? So lot of folks and what we all need to continue to do and a lot of these folks”

#### [142] Heirs' Property Training (Webinar from DBAN)

- Source: https://www.youtube.com/watch?v=OODJe43FyEs
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [142] [00:36:54](https://www.youtube.com/watch?v=OODJe43FyEs&t=2214s) — “Annette said that there's back and forth. there's there's a need to find pretty complete information. I think that's one of the reasons that it's so important not to rush the process uh because and to really spend that time uh developing relationship with the the person and the family that you're talking with because they are very personal conversations um you know about someone may come to you and say well I know all the owners of the property and it's uh these six people over here uh because that is how they understand it uh but it's important and”
- [142] [01:02:12](https://www.youtube.com/watch?v=OODJe43FyEs&t=3732s) — “property and the person they appoint to be that kind of face in the world. That that document though would be filed in the register of deeds office. Um, because it it relates to land. um it would have to be filed and then anybody that goes through to look for the title history of this particular piece of property um would see it there um that oh we need to go talk to Mary Henderson when we're looking at this particular piece of property because all these folks that are on this document have”

#### [143] Preserving Homeownership: A Guide to Heirs Property for Housing Counselors

- Source: https://www.youtube.com/watch?v=VFSnbIIfy-M
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [143] [00:01:31](https://www.youtube.com/watch?v=VFSnbIIfy-M&t=91s) — “can go to the next slide. My work has been around uh how do we think about this uh notion of housing counseling and estate planning as a potential onramp for home ownership. Um given the price of new construction, we think that this notion of encouraging um the legal transfer of housing is a way quiet way for folks to be able to enter the formal housing market. Here's why that's important. Because you see on your screen sort of the heir's property challenge. On the left is what it is. And I won't read this to you, but on the”
- [143] [00:16:35](https://www.youtube.com/watch?v=VFSnbIIfy-M&t=995s) — “you do have those educational resources at your fingertips, you're able to keep your property in good repair or be able to take advantage of resources that may be out there. Homeownership readiness and faith-based missiondriven affordable housing development is also one of the programmatic areas that we focus on. Next slide, please. We all know that he's property is a silent threat. So, LIS has uplifted this body of work. The project program objectives for list heirs property programs increase awareness and causes of heirs property through community education. If we don't know what heir's property”

#### [144] Resolving Heirs' Property

- Source: https://www.youtube.com/watch?v=TP6n8TBsCGs
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [144] [00:09:12](https://www.youtube.com/watch?v=TP6n8TBsCGs&t=552s) — “Heirs property owners can't use the land as collateral to get low interest loans to start a business, for example, or to pay for schooling. And this limits the ability of owners of heirs property to build wealth that can be passed down from generation to generation. Heirs property owners have what's called dead capital, right? Dead capital is an economic term and it's related to property that's informally held. is not legally recognized and cannot be exchanged for financial capital. So these heirs property owners, they have all of the burdens that come with the ownership right, but none of the benefits of the property.”
- [144] [00:33:40](https://www.youtube.com/watch?v=TP6n8TBsCGs&t=2020s) — “However, owners of heirs' properties They might, right? They might decide that no change is necessary. And that's an option, right? So here are some important things that families must consider in deciding whether to change the way that the heirs property is held. They have to consider resolving the fact, or they will be considering the fact that resolving heirs property, like I said, does take time, takes a little time, takes effort, energy, money. to identify all potential heirs, get a unanimous agreement on what to do and hire a lawyer and change the legal status of the property.”

#### [154] Florida Probate Explained: What Happens When Someone Dies Owning Real Estate?

- Source: https://www.youtube.com/watch?v=Dutmzc9gb30
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [154] [00:00:35](https://www.youtube.com/watch?v=Dutmzc9gb30&t=35s) — “estate attorney. He specializes in probate and other things. This is not going to be legal advice. These will be uh for your education. I'm saying the disclaimer for you. But let's jump into that uh real story. Tell me about a probate case that looked simple at first, and then it turned into a complete mess. Cuz well, we like talking about the messy side of real estate here. &gt;&gt; Yeah. Well, first of all, Courtney, happy to be on this podcast with you. And you know, this this world of probate is so fascinating, so vast. There's a”
- [154] [00:11:35](https://www.youtube.com/watch?v=Dutmzc9gb30&t=695s) — “to talk through some more case studies as well. So, let's start off talking through some probate fundamentals. So, with the big picture first of all, let's start with that. When someone dies owning real estate in Florida, what actually happens to ownership in the property? So, you know, if Jane Doe owns a property today in Florida and she passes away, what what happens tomorrow? Who owns it tomorrow? &gt;&gt; Well, when we start with that, the first thing that we're ever doing with any probate deal is you got to start with the deed. You got to start with the”

#### [158] Successor in Interest and Tangled Title

- Source: https://www.youtube.com/watch?v=ME2xl7cczH8
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [158] [00:18:03](https://www.youtube.com/watch?v=ME2xl7cczH8&t=1083s) — “you have a situation where you were forcing people out of their home because perhaps an unscrupulous air or just we just don't get along and so I'm going to go ahead and force it um I always say from an underwriting standpoint I never want to get involved in neighbor disputes and I don't want to get involved in family disputes because those seem to be the costliest and take the longest to resolve because because the the it's not just about the law and the facts it's about you will you can never really reach a great resolution”
- [158] [00:59:31](https://www.youtube.com/watch?v=ME2xl7cczH8&t=3571s) — “that you need to be aware of and I know people are needing to go to the HUD meeting this is going to be recorded So you'll see it later no need to apologize we we totally understand um so really important and I would just say as an aside that um it's always really important to know what kind of loan somebody has this should be um absolutely one of the first things that you look into when you're helping someone whether it's a successor issue or other mortgage delinquency or trying to get half assistance any of these”

#### [185] Probates List on Propstream Wholesale Real Estate

- Source: https://www.youtube.com/watch?v=W0bwM9N_98Y
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [185] [00:04:29](https://www.youtube.com/watch?v=W0bwM9N_98Y&t=269s) — “process um okay and i mean to in one i guess one degree you're getting you're getting them before they go to probate because a lot of people still get probates right and so you're kind of one step ahead when you're getting the pre-probates um but yeah i like that you know because it can be a sensitive topic just like other lists like whether it's a divorce list or even bankruptcy or inheritance you know it's something that we have to you know care about and you know look at it like it's our own family”
- [185] [00:09:00](https://www.youtube.com/watch?v=W0bwM9N_98Y&t=540s) — “right and so the first way to get to this list is it's under the quick list choices so to repeat all you have to do is hit clear all search your market go into the filter choose the pre-probate list and you can hit close and stop there or just like we just did a few moments ago add some more additional filters to it so that's the first avenue the other way to get to the pre-probate list is in the ownership info you can go into the ownership info and we have a filter here that says”

## Domain 6: Ex-FBI & Curative Skip Tracing + DIY Title Search & Hidden Lien Discovery

Primary video assignments: [079], [085], [112], [116], [118], [123], [127], [132], [146], [147], [148], [160], [161], [162], [167], [168]

### 6.1 Ex-FBI and curative skip-trace chain

**Input:** identity anchor and legitimate research purpose.
**Output:** verified locator record with provenance.

**Ordered procedure (editorial synthesis):**

1. Begin with an evidence-based identity profile: age range, known residences, associates and chronology, not speculative psychological labels.
2. Chain obituaries to funeral registries, FindAGrave and probate dockets.
3. Compare accessible voter, vehicle or utility sources only within actual access permissions; no restricted database bypass.
4. Cross-check social profiles, public address history and voluntarily supplied relative/neighbor leads.
5. Compare TLOxp, idiCORE, Accurint, PropStream and free records without treating broker aggregation as independent corroboration.
6. Record false positives and stop repeated contact with the wrong person.

**Execution and acceptance contract:**

- Persist `verified locator record with provenance` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [151] [00:06:50](https://www.youtube.com/watch?v=4Z6pgZnoWi4&t=410s) — “originates, so when somebody passes away, the funeral home will notify the social security. Social security keeps the death database and for a long time that had a lid on it. It was only accessible to government entities and nonprofits. Loopholes have been found and people are including that data in data sets using it for skip trace and append processes. However, we all know how good what's your best skip trace percentage. Like maybe 60%. Like when you skip trace as far as accuracy. It's not science, it's more art. You're making calculated guesses who the right John DOE is.”
- [123] [00:04:02](https://www.youtube.com/watch?v=zMW-iFWYX9w&t=242s) — “going to be on there. The the parents might even be on there. &gt;&gt; So then you'll trace the by the PO box then by instead of by the person that way. &gt;&gt; Yeah, and and that's what I tell everybody. When you're researching a property and you're already stuck, you have to see skip indicator, right? If the subject property is different than the mailing address on the CAD, skip trace the mailing address. &gt;&gt; Yeah. &gt;&gt; So you don't want to skip trace an individual's name cuz you're only going to get one hit.”
- [038] [00:11:28](https://www.youtube.com/watch?v=VwfAeN31cTw&t=688s) — “that connection is evidence evidence links the material we use in the present to see what happened in the past in the burton example the fact was the identity of the woman who bore zervaya and lydia the information came from church probate and town records the evidence is the meaning we obtained by assembling those infrared information items from s4 sources this means that evidence exists in your mind evidence can change as you think about information you found you can't be sure of the labels until you've assembled the evidence to support a hypothesis”
- [036] [00:15:53](https://www.youtube.com/watch?v=FPaiNw1Z1b0&t=953s) — “proven track record for success for uncovering some of these errors this section is going to cover that most errors are uncovered by taking the time to compare and contrast independent sources that provide evidence answering the same research questions and the steps that I am going to talk about now are considered critical in this analysis process number one view any uncorroborated records or testimony with skep ticism no matter how much you may think the person is telling the truth if they don't have something to back it up you need to be careful number two search”

### 6.2 DIY chain of title

**Input:** parcel and current recorded owner.
**Output:** instrument-by-instrument title chain.

**Ordered procedure (editorial synthesis):**

1. Retrieve the current vesting deed and copy the full legal description.
2. Search backward through grantee indexes to each acquisition, then grantor indexes forward for conveyances and encumbrances.
3. Resolve metes-and-bounds, lot-and-block and rectangular survey descriptions; street address alone is insufficient.
4. Track recording and execution dates, instrument numbers, exceptions and missing links.
5. Distinguish joint tenancy survivorship, tenancy in common, life estate and enhanced life estate/Lady Bird deeds under local law.
6. Reconcile the chain with probate and death records, not only assessor ownership.

**Execution and acceptance contract:**

- Persist `instrument-by-instrument title chain` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [144] [00:55:13](https://www.youtube.com/watch?v=TP6n8TBsCGs&t=3313s) — “Also, you'll learn about the type of interest that you might have in the property if it's shared, because your interest might be limited, right, by the form of the deed to you if you hold title by Joint tenancy with right of survivorship, that's one way to hold title, right? Typically we see that for husbands and wives, right, or married couples. And that joint tenancy with right of survivorship, that vests title in the survivor as between the joint tenants, right? So if one dies, their right, the right of survivorship passes to the living owner.”
- [167] [00:07:27](https://www.youtube.com/watch?v=aUiod-Jy68U&t=447s) — “the name of the grantee and the grant tour and the address and how the grantees were holding title together. And we could scroll down here and see that full legal description, just like the report told us right up here at the very top, which again was not included in that property detail report. And honestly, this probably wouldn't be included anywhere else online that would normally be free because it was just a whole lot of information here. And in order to get the full unabridged legal description, you would have to either look at that most recent deed”
- [116] [00:01:44](https://www.youtube.com/watch?v=EDl18zX1-F0&t=104s) — “looking for is an accurate listing of the grantor, who relinquished the title, and the grantee, whoever took possession of it. Another method of looking up the same information is to go to the advanced search option down here at the bottom of the record search page. You can search for deed and again select the option with those parentheses, then enter your last name and first name here. You are able to purchase a copy of any document from your search by adding the appropriate entry to your shopping cart. Please note, only images from records”
- [091] [00:03:34](https://www.youtube.com/watch?v=1N1Z99kUvRw&t=214s) — “survivorship first so with joint tenants with the right survivorship the number one factor is the date of death guys here's an example Barry and Elizabeth Hurley bought the home January 1st 1998 as joint tenants with the right survivorship you see a lot of that Barry dies March the 1st 2023 his ownership would transfer at that point no need for a state no need for probate the deed said husband and wife literally Elizabeth could walk down to the court with a death certificate and prove that she's a sole owner of the property”

### 6.3 Hidden lien discovery

**Input:** title chain and owner aliases.
**Output:** hidden-lien register and payoff evidence.

**Ordered procedure (editorial synthesis):**

1. Search municipal code enforcement, utilities and special assessments outside ordinary mortgage indexes.
2. Evaluate Medicaid estate recovery claims and the applicable estate/recovery scope.
3. Search federal/state tax liens and applicable release, expiry and priority records.
4. Check child support, alimony and judgment liens against the relevant owners.
5. Evaluate HOA/condominium super-priority rules and mechanics liens with statutory timing.
6. Obtain written current balances and determine whether each interest survives the sale or attaches to proceeds.

**Execution and acceptance contract:**

- Persist `hidden-lien register and payoff evidence` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [160] [00:02:39](https://www.youtube.com/watch?v=TWPIHeWyybg&t=159s) — “current date now when it comes to liens there are two different types of liens that can be recorded on a title you have what's called a recorded lien and an unrecorded lien now an example of a recorded lien can be a mortgage an example of an unrecorded lien can be let's say a mechanics lien where you had a contractor do some work on a property but they weren't paid for that particular job so they decided to slap a lien on the property a mechanics lien on that property to cloud the title”
- [161] [00:05:32](https://www.youtube.com/watch?v=xtdWFaJY8Xc&t=332s) — “Is the mortgage gonna leave the property? Yes, the mortgage and the deed of trust are gonna be wiped out by the county. The point is, you need to check on these things if you're gonna be a good buyer at the auction. All right. This research can be done at the county records. Maybe there was a bankruptcy involved. Maybe there's a child support lien against the property. Maybe there's a divorce judgment against the property. You need to find out about those financial judgments before you head off to the auction. All right. Now the county records are the public records.”
- [146] [00:11:45](https://www.youtube.com/watch?v=lKsfBAioCYU&t=705s) — “successful in getting the the partial release of IRS liens from the property. They will do that if the lien is not huge or if you're not a a big criminal, you means the owner. Um I mean, they'll they'll probably release it or you'll pay $10,000 on a million dollar IRS lien. Now, people are afraid of it. They shouldn't. It's actually very attractive. A lot of a lot of folks don't know the theory on which liens can be negotiated. So, that's pretty powerful tool to have. &gt;&gt; When it comes to the federal stuff, I”
- [162] [00:00:27](https://www.youtube.com/watch?v=z6h2w5h7oTQ&t=27s) — “or otherwise they might hinder your success in the curative title world. Now, I want to be very clear that curative is not just wholesaling harder deals. That's something that I want to be very clear about. There is some difference here. So, sure, you might be dealing with things like probate and tax sale auctions. Maybe you've got owners who are fighting, or people who don't even think they're an owner. Maybe you have some title issues, whether it's a broken chain title, you know, you've got a messed up property description. Maybe you have some complex liens or”

### Domain evidence workbench

The following source-specific evidence cards expose primary assigned videos without treating lexical matches as verified legal rules.

#### [079] How To Find family members of a deceased person!

- Source: https://www.youtube.com/watch?v=eiQ53kxE6ZA
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [079] [00:00:25](https://www.youtube.com/watch?v=eiQ53kxE6ZA&t=25s) — “going to go over about a five-step system with you that I do. First of all, when I run the skip tracing, the red D means that they're deceased. The first thing I do is I try the numbers on there just to see if a family member has kept the numbers. I've had numerous times where I've called I called a few months ago and there was a son that was deceased and his dad was taking the phone calls, knew nothing about the unclaimed property that his son had. or there was a time when I called and a”
- [079] [00:03:29](https://www.youtube.com/watch?v=eiQ53kxE6ZA&t=209s) — “I got his son's name in his city. I could then go ahead and look and find his son cuz not all relatives are always listed with the accounts. Then I go through and I look at the associates. Now the associates are people who they've apparently done business with. But sometimes it works, sometimes it doesn't. What I'll do is I'll just same thing. This David Church trying to reach John Smith. John, did you know X and X who lived at this address? I have you down as a possible contact. And then”

#### [085] 2 Ways To Check If There's a Lien On a Property (For Surplus Funds Recovery)

- Source: https://www.youtube.com/watch?v=q95klfFm9mE
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [085] [00:00:22](https://www.youtube.com/watch?v=q95klfFm9mE&t=22s) — “of people want to know how in the world do I check to see if there's leans you understand that leans can actually take over your ser because a lean is in first position first priority to the Surplus so if you're working on a claim you want to make sure that if there's a lean first of all you want to be aware of it then we want to understand do they actually have the rights towards the claim and what their time duration is so for starters to actually locate if there is a lean on the property I'm going to”
- [085] [00:02:12](https://www.youtube.com/watch?v=q95klfFm9mE&t=132s) — “name if they have a lean it's going to be recorded under their name and then it will show the asset in which the lean is held to it's not going to be under the property's address going to be under the owner's name so the first step is figuring out who that previous owner is prior to the Foreclosure searching their name in the county recorder's office you're also going to be able to find the D document you're going to be able to check and see if there's any leans you're going to get the book and page”

#### [112] How to Search for a Property ID

- Source: https://www.youtube.com/watch?v=ZX-Ttx_4Ezo
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [112] — supplied storyboard/description reconstruction; no quote timestamp: The California State Controller's Office explains Property ID searching on ClaimIt.ca.gov. Do not use a middle initial on the initial search. The example John P Sullivan returns 73 matches while John Sullivan returns more than 500 because holders often omit middle initials. Last Name requires at least three characters. Narrow results with cities where the person lived or received mail. Holder reporting errors in names, streets, cities or ZIP codes can explain undelivered payments. Try partial city names, such as Gold for Gold River, common name misspellings, partial first names and nicknames, such as WIL for William or Will. Inspect results for former addresses, P.O. boxes and family members. Click Add beside a Property ID to add it to the Claims Cart, then Claim Properties in My Cart or Continue Search. File using eClaim or a paper mail-in form when complex heir documentation is required. Record the Property ID before calling (800) 992-4647.

#### [116] Quick tip: How to do an Online Title Search

- Source: https://www.youtube.com/watch?v=EDl18zX1-F0
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [116] [00:00:36](https://www.youtube.com/watch?v=EDl18zX1-F0&t=36s) — “The simplest way to access the document search function is by clicking on this graphic depicting books, which says begin your recorded document search. That will take you to this official record search portal. One way to conduct a title search is by clicking the top button, which says name search. From there, you can enter the property owner's name, but be sure to follow the format of last name, then first name with no comma, then click search. Keep in mind, the more information you include here, the tighter the search will be. So, don't include a middle name”
- [116] [00:01:44](https://www.youtube.com/watch?v=EDl18zX1-F0&t=104s) — “looking for is an accurate listing of the grantor, who relinquished the title, and the grantee, whoever took possession of it. Another method of looking up the same information is to go to the advanced search option down here at the bottom of the record search page. You can search for deed and again select the option with those parentheses, then enter your last name and first name here. You are able to purchase a copy of any document from your search by adding the appropriate entry to your shopping cart. Please note, only images from records”

#### [118] Skip Tracing for Curative Title: Find Owners Others Can't

- Source: https://www.youtube.com/watch?v=dJ-LTFmMsTg
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [118] [00:14:05](https://www.youtube.com/watch?v=dJ-LTFmMsTg&t=845s) — “want to find the person associated with this. The first thing I would do is look immediately for that person. Then I would dump their information to Google, see if anything else came up. &gt;&gt; Yep. &gt;&gt; And then I would look at a relative, which would be a child, a sibling, or a parent. Sometimes they're easy to find, sometimes they're not. Um then I would look to neighbors. And then if I I would also go to social media and look through that, see if I could find them and find other people”
- [118] [00:52:35](https://www.youtube.com/watch?v=dJ-LTFmMsTg&t=3155s) — “sounds really fascinating to say that you did a deal that had 10 owners or 15 owners. But, they also it's important to remember that I need to get this deal to cycle. I need to get it these sellers paid. I need to close my problems out. I need to resell it, make some money. And if I'm doing one or two deals at a time, I need one to close every 30 days. I got bills to pay, you know, things like that. And people miss it, and I hear them say, "Well, I got”

#### [123] Curative Title Research: How She Finds Missing Owners

- Source: https://www.youtube.com/watch?v=zMW-iFWYX9w
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [123] [00:04:45](https://www.youtube.com/watch?v=zMW-iFWYX9w&t=285s) — “right, I'm going to skip trace, I don't know, Aaron Rodgers. You can put it in there. You go you put the name in the first field. Aaron first name or last name last name first, whatever. Put them in. You hit the button and see what happens. Well, hold on a minute. First hit the First do it that way. See what you get. Just I would glance it. Second, I'd go back and put the subject address in. Glance it. Then you say, okay, hold on a minute. There was a mailing address that”
- [123] [00:29:26](https://www.youtube.com/watch?v=zMW-iFWYX9w&t=1766s) — “there are those ones that are kind of hairy and you're like oh, I need I'm going to need some random affidavit signed besides the affidavit of heirship, right? But it's just that helps me understand like from the underwriter's perspective why they need it. &gt;&gt; Yeah. &gt;&gt; Right? And it's I love learning that because it's just another layer of education, you know? &gt;&gt; With you being like a breakthrough specialist and going to find the last people and helping connect the dots, there's a big piece of this that's the title abstracting and examining and”

#### [127] How to Buy Distressed Properties With Title Problems for Pennies on the Dollar \| Logan Fullmer

- Source: https://www.youtube.com/watch?v=W0wjEVX_Jxw
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [127] [00:02:29](https://www.youtube.com/watch?v=W0wjEVX_Jxw&t=149s) — “work. I buy property for pennies on the dollar because they have title issues. We buy without title insurance, solve those issues, then go sell them for what they're really worth. That took me 6 or 7 years to build. So, I'd find partners that were young guys and I'd train them and they were young and hungry. They shouldn't have the capital or experience. So, I built businesses with each of them. Once they were up and running good, I would say, "Let's start a company." So, let's start an LLC. I'll capitalize it. You”
- [127] [00:19:42](https://www.youtube.com/watch?v=W0wjEVX_Jxw&t=1182s) — “nothing to do on a Saturday? Don't buy a hamburger and buy that. There you go. &gt;&gt; And if yeah, you guys want to learn how to acquire these distressed properties, buy the guy or listen to the guy who literally wrote a book on it. Uh go follow those socials because this is one of the experts. This is one of the top guys in the country at acquiring these type of properties, resolving these type of defects. A lot you can learn from him. Uh and if you're watching this show for a reason, you all either want to be”

#### [132] How to Find Curative Title Deals Nobody Else Is Chasing

- Source: https://www.youtube.com/watch?v=FgFrlIpbscs
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [132] [00:00:01](https://www.youtube.com/watch?v=FgFrlIpbscs&t=1s) — “I've said it before, but I'll say it again that I have made a lot of money in real estate, especially curative title deals where I'm solving title and ownership problems by being curious. And look, every time I say that, I always find someone who's like rolling their eyes. You can tell they just I don't know, they get defeated. And I've been told that, "Hey, that is vague." And I've even watched people say that to other folks who talk about this skill set. And so, let me break it down for you and show you how this is”
- [132] [00:01:32](https://www.youtube.com/watch?v=FgFrlIpbscs&t=92s) — “I want to talk about something that not only could you use right now for the deals you're working, you could think back on deals you've already done, but then it's a skill set that as you move forward, I hope you apply it. And then you can find other types of leads with a whole lot less competition. So, ultimately, what we're starting to see right now. So, most of my uh curative deals have been in Louisiana and Mississippi. That's my um first market. That's where I've been doing I started doing curative deals”

#### [146] Title Search Explained: The Hidden Liens Investors Miss

- Source: https://www.youtube.com/watch?v=lKsfBAioCYU
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [146] [00:04:39](https://www.youtube.com/watch?v=lKsfBAioCYU&t=279s) — “accompanying the report. You don't need to be a title expert. You need You don't need to to look anywhere, but you know, a highlighted areas of the search, which is abstract. Um and we wanted to standardize it across United States because the data doesn't look the same in Louisiana versus Puerto Rico in Spanish versus Hawaii, um etc., right? So, we wanted to make sure that we provide to our investor clients a standard data reports, which will highlight what's wrong with title, right? And the more hair we find, the more discount you can count on when”
- [146] [00:10:13](https://www.youtube.com/watch?v=lKsfBAioCYU&t=613s) — “survive. So, you really need to know the theory on what options or what solutions you have on the table. But uh yeah, one thing to to completely be aware of, you know, &gt;&gt; \[clears throat\] &gt;&gt; all the liens, right? There's probably 20 types of liens that you need to know as real estate investor and you need to to verify those liens attached to the property or the person. If they're attached to the to the person that lives in the property right now, you don't care. Right? You don't care. Civil judgments,”

#### [147] How Ex-FBI Agents Skip Trace Anyone for Real Estate Deals

- Source: https://www.youtube.com/watch?v=GK-4kFznJlA
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [147] [01:00:24](https://www.youtube.com/watch?v=GK-4kFznJlA&t=3624s) — “and so you can do some some good work from the outside but it's it may be that face-to-face they needed that or they may need a a female to be making the call versus a male or may need an emissary to you know just just keep pushing. You till you find that button that's going to work with that person. &gt;&gt; The persistence part of it. When folks are trying to get these deals done and they're calling people to ask about others I find they get confused and they always try to find or I notice people a”
- [147] [01:03:30](https://www.youtube.com/watch?v=GK-4kFznJlA&t=3810s) — “today. I mean, if the budget's big enough, yeah, you can find him, but you'd have to camp out for weeks. &gt;&gt; canvas a lot. You got to work it. &gt;&gt; so that's our kind of our motto is always, you know, like Alec Baldwin said in Glengarry Glen Ross, always be closing. &gt;&gt; Oh, yeah. &gt;&gt; Always be developing sources. And we have so many and so many different industries. It's it's it's kind of funny. We have it like card catalog because you just don't don't know what you're going to need to know.”

#### [148] How Matt Solved a 10 Heir Title Nightmare (A Curative Title Case Study)

- Source: https://www.youtube.com/watch?v=nYQaov_liDw
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [148] [00:04:07](https://www.youtube.com/watch?v=nYQaov_liDw&t=247s) — “the second or I guess like the third life estate we ended up buying her uh life estate for $500. And then the last life estate it was the mother of the great-grandson. And she was just &gt;&gt; things along. &gt;&gt; Exactly. Exactly. So, that's what title said. But, she actually didn't have a life estate because the her husband predeceased the original decedent. So, when he died, he never had ownership. But, when So, so title was saying that she was a she had a life estate, but that's actually not true because husband”
- [148] [00:10:13](https://www.youtube.com/watch?v=nYQaov_liDw&t=613s) — “that case, the son he died and had one kid. I would buy the interest from the kid and then I would buy a deed from the mom and then that would clear title. And again, this is all Texas by the way. &gt;&gt; Yeah, cuz it's really important to talk about this per state. In In Louisiana, we call this something different, but we're weird in Louisiana for everything else. So um So but life estates are really important because that as you said is not an owner, but is a decision-maker and you”

#### [160] How To Do A Property Title Search

- Source: https://www.youtube.com/watch?v=TWPIHeWyybg
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [160] [00:01:31](https://www.youtube.com/watch?v=TWPIHeWyybg&t=91s) — “title well in layman's terms a property title is a bundle of rights and a piece of property we're gonna leave it at that because that's exactly what it is we don't want to over complicate this so when you're purchasing real estate and you're taking title to a property or rather before you take title to a property what you want to do is what's called a title search so what exactly is a title search well in its simplest form a title search is the process of retrieving the history of a piece”
- [160] [00:04:43](https://www.youtube.com/watch?v=TWPIHeWyybg&t=283s) — “cost you somewhere between 100 and 150 dollars based on the company that you're using and the reason you would want to use a preliminary title search is to get some information on the property before you actually purchase that property without doing a full-blown title search on that particular property and by doing that preliminary title search it can prevent you from purchasing a property that will give you headaches on the other side now another thing you want to keep in mind is any property that you purchase you want to get what's called title”

#### [161] How To Do A Title Search On A Property Yourself Before You Bid At Tax Sale Auctions

- Source: https://www.youtube.com/watch?v=xtdWFaJY8Xc
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [161] [00:01:38](https://www.youtube.com/watch?v=xtdWFaJY8Xc&t=98s) — “that work at title companies as abstracters, or title searchers, or something like that. All right. You don't have to get that good at this, but you need to learn to do basic research before you bid at a tax defaulted auction. Now usually the people that work at title companies have training in this, so they're gonna be expert, and can get it done quickly. But you're gonna have to look at many properties at tax defaulted auction. At least, look at the list before you buy the property. So you need to get some basics, and learn how to do it.”
- [161] [00:10:34](https://www.youtube.com/watch?v=xtdWFaJY8Xc&t=634s) — “I don't know what could have happened to that property. But you need to have boots on the ground and check, and make sure you know what you're buying. The other mistake people make is they don't look at the property, and when they're looking at the property, they don't look at the neighborhood. You've gotta look at the neighborhood, because you're gonna want to sell the property. If the neighborhood isn't good, you're gonna have trouble selling the property. So you want to know before you start bidding, how high to bid. So you need to get a good look at the neighborhood.”

#### [162] Before You Go From Wholesaling to Curative Title, Watch This

- Source: https://www.youtube.com/watch?v=z6h2w5h7oTQ
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [162] [00:08:38](https://www.youtube.com/watch?v=z6h2w5h7oTQ&t=518s) — “Honestly, you shouldn't even be spending thousands of dollars every month generating leads. Like that's crazy. And a lot of that money will go towards though instead the support that your deals will need. So for example, you may need support to help with the research, building out the profile, what I call a profile or others call a fact pattern, on the property. What's going on, right? Basically the title search stuff. Hey, what's going on? Maybe it's goes towards genealogists who say, "Hey, someone's has died. We need to build out who their”
- [162] [00:20:48](https://www.youtube.com/watch?v=z6h2w5h7oTQ&t=1248s) — “actually get my first curative title deal?" That's exactly where I want you to go next. See, I have a video where I'll put out on how to get your first curative title deal. It In that episode, I walk you through where you should start, what kinds of opportunities I would look for, and how to start pulling this into practice without trying to tackle the most complex title problems you can find on day one. So, go watch that episode. It's a literal step-by-step guide. So, I'm going to see you on that next one, and I'll see you”

#### [167] DataTree Hacks: Find Full Legal Descriptions and Title Vesting Information

- Source: https://www.youtube.com/watch?v=aUiod-Jy68U
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [167] [00:01:05](https://www.youtube.com/watch?v=aUiod-Jy68U&t=65s) — “you're going to need the legal description and the name of the owner who is selling that property. And one way you can get that is right here in DataTree. So all you have to do is find the property and question that you're working with, and DataTree gives you several useful ways to do this. You could search by the owner name or the address of the property or the APN or even a document number. In this case, I'm just going to find a random property in, I don't know, New York, let's go with that. And we'll pick the first”
- [167] [00:07:00](https://www.youtube.com/watch?v=aUiod-Jy68U&t=420s) — “were holding title together. This is another very important thing that might not be evident without doing an actual title search, to see how it was written on the most recent deed. And speaking of that title search, there's actually a separate video I have on how to do a title search through DataTree. It's actually pretty easy, but in this case with this particular report, we can scroll down. It shows us the actual recorded deed from the most recent transaction. And we can see all the relevant information that that first page told us about”

#### [168] DataTree Hacks: How to Do Title Research and Hire Abstractor Services

- Source: https://www.youtube.com/watch?v=GfyX48eCbRY
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [168] [00:00:38](https://www.youtube.com/watch?v=GfyX48eCbRY&t=38s) — “For example, if I go over here to, I don't know, Texas we'll go check out Dallas County. We can see what they've got there. And when we scroll down, when it comes to looking at the title history of a property, the things that we're looking for are the title chain and lean report in Transaction History Full. This is the kind of information that a title researcher would be doing at a title company. They may not use DataTree specifically, but just as a first pass, this would tell them most of what they need to know.”
- [168] [00:05:05](https://www.youtube.com/watch?v=GfyX48eCbRY&t=305s) — “then you might not even want to go down this road because there can be a lot of little hidden issues that a title specialist knows exactly what to look for and how to find, but somebody who has never done this before, and doesn't know what they're doing, doesn't even know what they're looking for and or when it's a problem. So you sort of have to take into account your own experience and comfort with doing title searching. But if you are at all confident in what you're doing, this can just be a super convenient way”

## Domain 7: Real Estate Data APIs, GIS Parcel Platforms & Neo4j Knowledge Graph Entity Resolution

Primary video assignments: [163], [165], [170], [171], [172], [173], [175], [176], [177], [178], [179], [180], [181], [182], [183], [186], [189]

### 7.1 DataTree property intelligence

**Input:** parcel and jurisdiction.
**Output:** document-backed property intelligence packet.

**Ordered procedure (editorial synthesis):**

1. Retrieve full legal description and vesting documents, not just the summary owner label.
2. Use TaxSource property tax verification reports where available and reconcile with the taxing authority.
3. Search nationwide owner variants and mailing addresses for portfolio candidates.
4. Resolve LLCs, trusts and similarly named owners before aggregating holdings.
5. Hire a local abstractor when images/index coverage is incomplete; specify date range and requested instruments.

**Execution and acceptance contract:**

- Persist `document-backed property intelligence packet` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [179] — supplied storyboard/description reconstruction; no quote timestamp: Regrid demonstrates self-service acquisition of statewide standardized parcel data at store.regrid.com, covering more than 155 million US parcels. Select a state, such as Ohio with approximately 5.29 million parcels across 88 counties. Inspect the County Coverage Report spreadsheet and Parcel Schema / Data Dictionary. Fields and tier distinctions include APN, owner name, mailing address, situs address, land use, valuation, building footprints and secondary addresses, across Standard and Premium offerings. Add a statewide dataset to the cart, complete checkout under the Data License Agreement and download the full state bundle or individual county files. Available formats include CSV, GeoJSON, Shapefile (SHP), File Geodatabase (GDB), GeoPackage (GPKG) and KML. Support is available at parcels@regrid.com. This reconstruction combines the visual screen tutorial and video description; it is not a verbatim audio transcript.
- [167] [00:01:57](https://www.youtube.com/watch?v=aUiod-Jy68U&t=117s) — “Go ahead and place the order. And what happens here is DataTree extracts the legal description from the latest full value deed in the vesting, from the latest transfer document, which is then sent to DataTree's keying staff for review and verification. And the time it takes to get these reports back is usually anywhere from 30 minutes to two hours. So it's not going to happen instantaneously, but it should happen relatively quickly. And if you're trying to do this for like a bunch of properties, say if you're a title company, and you've got a huge list that you need this information for, you can do a batch order as well,”
- [187] [00:07:04](https://www.youtube.com/watch?v=ntT8V0gnpAs&t=424s) — “I've actually already ordered it for this property, so I'm just gonna go ahead and click on that, and show you what it looks like. And this is pretty much it. We see again the name of the owner. We see the owner's mailing address. We can see the full legal description of the property, which is really helpful when we want to put that in our purchase agreement, or our deed. You can see again the parcel number. Another super helpful thing, especially when it comes to vacant land, is the coordinates of the property.”
- [082] — supplied storyboard/description reconstruction; no quote timestamp: Controller Malia M. Cohen introduces ClaimIt.ca.gov and explains California Unclaimed Property Law. After three years of dormancy, covered property can include bank accounts, stocks, uncashed checks, insurance benefits, wages and safe deposit box contents. Real estate is excluded. Search by Last or Business Name, First Name and City or ZIP, or by Property ID. Active escheated properties have a +CLAIM button. Pre-escheat Notice properties have an INFO button showing holder contact information and a June 1 transfer deadline; an owner can contact the holder directly before transfer. Add multiple properties to the Claim Cart. Select the Claimant Relationship: Myself; Business Officer/Dissolving/LLC/Sole Prop; Heir; Heir-Trust; Heir-Will; Heir-Court Appointed Rep; Heir-Final Decree Distribution; Holder Reimbursement; Government Agency; or Bankruptcy Trustee. Complete the three-step eClaim form. Step 1 collects contact information, SSN and date of birth. Step 2 is an electronic signature under penalty of perjury. Step 3 presents a claim summary with Claim ID and a confirmation email within 24 hours. Upload verification documents through Upload Claim Documentation, with up to five files per batch in PDF, JPG or JPEG format, each between 1 KB and 15 MB. Document types include ID, SSN, Proof of Reported Address, Death Certificate, Trust/Will/Probate Decree and Investigator Agreement. Check status at ClaimIt.ca.gov or call 1-800-992-4647.

### 7.2 Regrid acquisition and import

**Input:** spatial scope and licensed dataset.
**Output:** versioned parcel dataset and import error log.

**Ordered procedure (editorial synthesis):**

1. Choose state/county coverage and inspect County Coverage Report plus Parcel Schema/Data Dictionary.
2. Check APN, owner, mailing/situs addresses, land use, valuation and Standard/Premium field coverage.
3. Acquire CSV, GeoJSON, SHP, GDB, GPKG or KML according to downstream needs.
4. For imports, validate encoding, headers, geometry, CRS, coordinate order and stable parcel keys.
5. Test a small sample before a full import; quarantine invalid geometry and unmatched IDs.
6. Record license, release date and source county freshness separately.

**Execution and acceptance contract:**

- Persist `versioned parcel dataset and import error log` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [179] — supplied storyboard/description reconstruction; no quote timestamp: Regrid demonstrates self-service acquisition of statewide standardized parcel data at store.regrid.com, covering more than 155 million US parcels. Select a state, such as Ohio with approximately 5.29 million parcels across 88 counties. Inspect the County Coverage Report spreadsheet and Parcel Schema / Data Dictionary. Fields and tier distinctions include APN, owner name, mailing address, situs address, land use, valuation, building footprints and secondary addresses, across Standard and Premium offerings. Add a statewide dataset to the cart, complete checkout under the Data License Agreement and download the full state bundle or individual county files. Available formats include CSV, GeoJSON, Shapefile (SHP), File Geodatabase (GDB), GeoPackage (GPKG) and KML. Support is available at parcels@regrid.com. This reconstruction combines the visual screen tutorial and video description; it is not a verbatim audio transcript.
- [177] [00:09:35](https://www.youtube.com/watch?v=EToN9mWFZWc&t=575s) — “readable a description of what that field is so if there's a particular field you're looking at check out the standardized schema the data dictionary for the standardized schema and then you can check on the coverage report our coverage for that place we also try to keep these as machine readable as possible so if you're integrating this into a workflow you can add your own automated checks and your own queries on top of this we do one thing I do want to note is that we we have this skin standard schema 105 different columns”
- [173] [00:00:02](https://www.youtube.com/watch?v=X-_cLY3_96Y&t=2s) — “welcome to regrid this will be a quick video demoing our new regrid feature service an esri compatible solution that deploys our nationwide land parcel data straight into your esri environment for enterprises centered on esri technologies regrid feature service is compatible with esri arcgis pro on the desktop app configuration tools and javascript api development environments simply integrate with our url for full parcel geometries and associated attributes in regrid's parcel records schema here we're going to quickly demo loading our premium parcel data into arcgis online you can do the same to configure”
- [178] [00:00:01](https://www.youtube.com/watch?v=6nMKiCCsK60&t=1s) — “welcome to the regrid property app today we're going to be talking about importing data that you have into regrid the first thing to cover here is that regrid only supports data that can be tied to individual properties so that means you're going to need an address a parcel number or a latl coordinate to match what you have to our properties census data or other aggregate data isn't going to work here so let's say that you do have some property level data that you want to import for example you know you've got a list of properties”

### 7.3 Spatial filtering and API integration

**Input:** parcel dataset and selection criteria.
**Output:** reproducible GIS/API query manifest.

**Ordered procedure (editorial synthesis):**

1. Combine attribute predicates with explicit spatial predicates such as intersects or within.
2. Use a spatial index and bounding-box prefilter before exact geometry tests in a suitable GIS runtime.
3. For ArcGIS Feature Services, inspect layer metadata, field types, CRS, limits and pagination support.
4. Use Regrid API Sandbox documentation for the actual current endpoint and authentication; do not invent endpoint paths.
5. Handle rate limits, bounded retries, pagination, caching and source-update timestamps.
6. Validate known parcels and empty-result cases before bulk ingestion.

**Execution and acceptance contract:**

- Persist `reproducible GIS/API query manifest` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [179] — supplied storyboard/description reconstruction; no quote timestamp: Regrid demonstrates self-service acquisition of statewide standardized parcel data at store.regrid.com, covering more than 155 million US parcels. Select a state, such as Ohio with approximately 5.29 million parcels across 88 counties. Inspect the County Coverage Report spreadsheet and Parcel Schema / Data Dictionary. Fields and tier distinctions include APN, owner name, mailing address, situs address, land use, valuation, building footprints and secondary addresses, across Standard and Premium offerings. Add a statewide dataset to the cart, complete checkout under the Data License Agreement and download the full state bundle or individual county files. Available formats include CSV, GeoJSON, Shapefile (SHP), File Geodatabase (GDB), GeoPackage (GPKG) and KML. Support is available at parcels@regrid.com. This reconstruction combines the visual screen tutorial and video description; it is not a verbatim audio transcript.
- [173] [00:00:02](https://www.youtube.com/watch?v=X-_cLY3_96Y&t=2s) — “welcome to regrid this will be a quick video demoing our new regrid feature service an esri compatible solution that deploys our nationwide land parcel data straight into your esri environment for enterprises centered on esri technologies regrid feature service is compatible with esri arcgis pro on the desktop app configuration tools and javascript api development environments simply integrate with our url for full parcel geometries and associated attributes in regrid's parcel records schema here we're going to quickly demo loading our premium parcel data into arcgis online you can do the same to configure”
- [165] [00:07:08](https://www.youtube.com/watch?v=RVakKAvFa_M&t=428s) — “this endpoint is structured but I have included sample use cases for you to try on how to use this endpoint so for example if you're looking for all the owners of a specific the owner who owns you know several Parcels within a certain area County zip code State Etc uh you can use this endpoint I used um our County which is a geoid also known as the fips code and the owner name I'm looking for all the 7-Elevens in Dallas County um I already pre-loaded and said that this result should turn 232.”
- [177] [00:17:45](https://www.youtube.com/watch?v=EToN9mWFZWc&t=1065s) — “last month into my database or other system and we're happy to provide specific code examples or walkthrough parts of that so that is that's how we deliver the bulk data to clients I'm happy to answer any questions about that it's by SFTP you'll get your own login password and in this metadata table to help process it in bulk or of course you can always use it by hand we also have a parcel API we have once you sign up we'll share a support document for that there's a couple of different endpoints that we”

### 7.4 Lead APIs and public docket ingestion

**Input:** county list and date window.
**Output:** auditable ingestion batch.

**Ordered procedure (editorial synthesis):**

1. Evaluate Deal Finder APIs, PropStream probate lists and ProbateData new/old leads against official case records.
2. Separate filing date, death date, sale date and ingestion date.
3. For public notices/dockets, record request parameters, retrieval time and stable document URL.
4. Use incremental checkpoints, deduplication and bounded backoff; preserve raw responses.
5. Detect schema changes and empty pages before accepting a run as complete.

**Execution and acceptance contract:**

- Persist `auditable ingestion batch` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [071] [00:09:46](https://www.youtube.com/watch?v=5sxGnXLZO6A&t=586s) — “so you can know that the death had to occur on or before that date. Obviously, prior to refrigeration, people didn't tend to leave bodies out for too long. So generally it's close to the time of burial, although sometimes you've got situations where the ground is frozen. So in those instances it may be longer. So consider the time of year. Newspapers, of course, are always a wonderful extra resource. Funeral notices, death notices, probate notices. Maybe there's a notice of the accident where someone was killed. Maybe. And then you also get legal notices.”
- [010] [00:11:38](https://www.youtube.com/watch?v=oZiYbKNvxJY&t=698s) — “other entity records birth before and for a time period after the death of the ancestor you can really find that the probate actions could be filed up two years after the date of death sometimes the heirs simply did not take any action to probate the estate until some events as the sale of the real property required a probate and that could have happened years after the person actually died so my rule of course is that you look for probate records from the date of death until the present but that's a”
- [171] [00:15:01](https://www.youtube.com/watch?v=NtfeEhpvcuk&t=901s) — “take a considerable amount of time while we need a a resolution that is able to keep our um to keep our resolution results up to date and it's quick enough because usually data changes over time and in small increments so we need for this reason a process that is able to um address all the changes happening the data almost in a real time and this is the process that we call incremental uh resolution that essentially works by identifying only the portion of the graphs that are affected by some changes according to um I mean compared to the”
- [017] [00:11:33](https://www.youtube.com/watch?v=KtpN2Ws9PA4&t=693s) — “collection it's indexed i could simply put in the name of doc harris and i could find it again really quickly as could anyone else now let's think about another scenario where perhaps you have found a source on a website and you don't know if that website will be around very long or if they will maybe rearrange their records and in that case you might want to have the complete url which as i mentioned before you could use on the internet archive wayback machine you'd put in the complete url and the”

### 7.5 Neo4j entity resolution

**Input:** normalized observations and citations.
**Output:** provenance-aware knowledge graph.

**Ordered procedure (editorial synthesis):**

1. Model Person, DeceasedOwner role, Heir role, Parcel, Address, ProbateCase, UnclaimedProperty and SourceCitation.
2. Use explicit relationships such as PARENT_OF, RESIDED_AT, OWNS, SUBJECT_OF and SUPPORTED_BY with validity intervals.
3. Keep assertions separate from canonical entities so conflicting facts can coexist.
4. Block candidates using jurisdiction, normalized name and address tokens before expensive similarity work.
5. Combine exact identifier matches, Cypher neighborhood evidence and optional vector candidates; semantic similarity alone never authorizes a merge.
6. Represent merge confidence, reviewer decision and reversible redirects.
7. Use unique jurisdiction-qualified identifiers, parameterized Cypher and idempotent MERGE operations.

**Execution and acceptance contract:**

- Persist `provenance-aware knowledge graph` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [171] [00:10:58](https://www.youtube.com/watch?v=NtfeEhpvcuk&t=658s) — “s data now at the end of this process we will have our uh similarity added into the graph so that among possible matches we create this similarity relationship with the similarity value then we perform the resolution phase that employs Community detection algorithms to identify Community subn likely to represent the same entity in our approach we are using we and we can use two different algorithms from the new 4J graph data science Library the first one is weekly connected component or WCC that offers a broad resolution value uh resolution level in the sense that this algorithm”
- [163] [00:01:55](https://www.youtube.com/watch?v=GMTY78xqGXQ&t=115s) — “the same user if we have notes of our offices in different locations if they have the same address we're going to consider them the same same office um beyond that we have semantic similarity which is going to be very familiar to anybody who's worked with rag so just Vector embeddings of node properties and then running semantic similarity on those vectors so if we have a node with a name company node with a name Tesla in the industry of autonomous vehicles that's going to be similar as a another one with the”
- [176] [00:00:09](https://www.youtube.com/watch?v=y5XZp-4n_uc&t=9s) — “Hey guys, it’s Seth here. In this video, I want to really quickly show you one of the most basic and useful things you can do in DataTree. Let's say you're trying to find a person and any real estate they own. And the same thing goes for a business entity in any real estate that that entity owns. But all the information you have is the name. You don't have a property address. You don't have a mailing address. You don't have a parcel number. You don't have anything else, just a name. Preferably you know what state and county that person or busines is in”
- [134] [00:08:28](https://www.youtube.com/watch?v=OrEz4Qk-EZ0&t=508s) — “Who else has something to troubleshoot? Who's here for their first time. Yeah, this is I don't, I'm not a first timer, but I actually want to set up a separate entity LLC for the branded name that I'm operating under. So I just wanted to know how I should go about setting that up. I know you've talked I've never heard anybody break down the way that you've broken it down to really protect yourself and keep keep entities separate. Now I do have a parent real estate company that I take all of my income.”

### 7.6 Digital preservation

**Input:** source documents and exports.
**Output:** fixity manifest and restore log.

**Ordered procedure (editorial synthesis):**

1. Hash every original with SHA-256 and store a manifest with byte size, origin and retrieval date.
2. Keep immutable originals separate from OCR, normalized extracts and reports.
3. Use Fixity Pro or an equivalent checksum workflow to compare scheduled inventories.
4. Investigate missing or changed files and restore from independently stored copies.
5. Test restores and preserve format/software metadata for long-term readability.

**Execution and acceptance contract:**

- Persist `fixity manifest and restore log` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [170] [00:00:07](https://www.youtube.com/watch?v=1pRY7lpZ7nA&t=7s) — “welcome welcome to this fixity Pro how to guide this tutorial will show you how to use fixity Pro to check your digital collections for any errors or changes that could make them inaccessible you can then take action as needed to ensure your files remain readable as long as possible fixity Pro is a file Integrity checking tool developed by AVP it is free to access for the first 30 days and then you have the option to pay $4.99 per month or £50 a year using fixity Pro takes a guess work out of preserving your digital files and”
- [016] [00:09:21](https://www.youtube.com/watch?v=DUAbGD8rVzA&t=561s) — “know how to do citations for online material a layered citation is the term coined by elizabeth shown mills and it describes digital sources that contain digital images of original records so we're going to have layers to our citations we're going to have a physical source citation and we're going to have a digital source citation and so these will be two separate parts and we can show that they are separate with the semicolon separating the two sections sometimes we might want to have even a third section especially if we're referencing an original microfilm”
- [019] [00:09:01](https://www.youtube.com/watch?v=PfqiDmLnMIg&t=541s) — “searched why you searched for this and what you found this is the most basic and straightforward way to put together a research log and the most commonly used enter things that you searched in the order that you search them you can do each with bullet points or in a table and with any research log you talk it out put in your theories your plans any conflicts in every document with citations now that doesn't mean you need to put in the documents i keep a folder with i keep a separate digital folder with copies of the”
- [018] [00:19:36](https://www.youtube.com/watch?v=FxQgurvv3_g&t=1176s) — “all the way through it so let's just see all those kind of recapitulate so first of all you want to click on all available information about the source from the webpage understand the jurisdictions of the locality use a template to fill in the citation elements for both the physical and digital layers and then assemble your citation keep your physical and digital parts together separate each part with a semicolon and don't be repetitive each layer does not have to have every single piece remember citation is an art not a science when you have the tools that you need”

### Domain evidence workbench

The following source-specific evidence cards expose primary assigned videos without treating lexical matches as verified legal rules.

#### [163] Neo4j Live: Entity Resolution and Deduplication with Neo4j and GenAI

- Source: https://www.youtube.com/watch?v=GMTY78xqGXQ
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [163] [00:00:00](https://www.youtube.com/watch?v=GMTY78xqGXQ&t=0s) — “jump into a little couple of slides first uh some of this we touched already in the intro chat but yeah we're going to just talk briefly about What entity resolution actually is what is the problem and why is it important a quick overview of some of the methods that are available in neo4j for solving the issue and then finally the practical application so entity resolution it's determining whether or not two representations of an entity actually refer to the same entity so again as we mentioned before if I was going to”
- [163] [00:22:21](https://www.youtube.com/watch?v=GMTY78xqGXQ&t=1341s) — “create the same as relationships and now we can see that now these two nodes are in fact tagged as as being the same and so with that in place the last thing we need to do is we just need to merge the nodes that have the same as relationship in this way uh matching matching finding the node pairs that have the relationship uh we're going to delete the same as relationship right after that because we don't need it anymore and we don't need it to be cluttering our graph uh Beyond this step and then”

#### [165] Quick Start Regrid's Interactive API Sandbox Guide

- Source: https://www.youtube.com/watch?v=RVakKAvFa_M
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [165] [00:00:03](https://www.youtube.com/watch?v=RVakKAvFa_M&t=3s) — “this demo for the interactive API sandbox on the support center page this is where you can find the information about the interactive API sandbox helpful links about our products that are within the sandbox the ability for yourself to get an API token this is for a trial token and the information that's included for the trial is right below it if you already have your own token already you can definitely jump into the interactive API sandbox so let's get started with getting a token I'm going to go ahead and sign up for an account”
- [165] [00:02:02](https://www.youtube.com/watch?v=RVakKAvFa_M&t=122s) — “history and check out the history that you did with using your token I'll definitely show you another way later on in this video so let's go ahead and take our token just copy it to our clipboard and we're going to navigate into the interactive API sandbox all right so I just want to let you know that as an admin I have a little bit of a different view but you will be landing on this page with getting started with a regret interactive API sandbox that gives you a lot of information on what is included”

#### [170] Getting Started with Digital Preservation: Fixity Pro

- Source: https://www.youtube.com/watch?v=1pRY7lpZ7nA
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [170] [00:00:48](https://www.youtube.com/watch?v=1pRY7lpZ7nA&t=48s) — “in this tutorial we will cover how to set up and run the program and how to read your reports so let's get started double click the icon to open fixity Pro it will take some time to load but when it opens the program will look like this the first time you use the program you need to change some settings so for now click cancel in the new project box first you need to tell fixity Pro where you want it to store the reports that it will create to do this click”
- [170] [00:07:12](https://www.youtube.com/watch?v=1pRY7lpZ7nA&t=432s) — “files that were scanned so let's talk about this a bit more fixity Pro works by scanning your files and allocating each one a unique reference number called a checkm the first time you run a scan all files are confirmed as new files as fixity pro has never seen them before however if we go back to fixity Pro and we run the scan again the report will go to the same location we can see that the status of all files has now changed to confirmed this is because fixity pro has compared the files with the data from”

#### [171] NODES 2024 - Beyond the Silos Achieving Data Harmony With Graph Based ER

- Source: https://www.youtube.com/watch?v=NtfeEhpvcuk
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [171] [00:04:05](https://www.youtube.com/watch?v=NtfeEhpvcuk&t=245s) — “of information that they leverage in the graph and the first type of rules is of course the the ones that depend on nod attributes here in in this picture there is an example that is the same social security number this is a rule of type node attribute because it is using the social security number that is indeed an attribute of our person nodes that we are supposed in to resolve in this case now these rules are very easy to manage but usually they are not enough because the problem I mean the problem”
- [171] [00:19:03](https://www.youtube.com/watch?v=NtfeEhpvcuk&t=1143s) — “Consolidated attributes so which one which option to prefer depends of course on the use cases and the requirements for instance if you are working in a street Access Control scenario you should prefer you can prefer the first option the attribute option or the hyperlink because allows us allows you to uh check the information check the resolution of your node without disclosing information about other Nots that you cannot you you do not have privileges to see while if you need to um Traverse essentially these these resolution results in your queries because for instance you want to merge”

#### [172] Exporting Regrid Data to ArcGIS - Regrid Property App (Web)

- Source: https://www.youtube.com/watch?v=EVN-9bqTEtM
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [172] [00:00:03](https://www.youtube.com/watch?v=EVN-9bqTEtM&t=3s) — “welcome to the regrid mapping platform today we're going to quickly discuss how you can export data that you have created in our regrid system as a file that you can open in arc products specifically arc desktop so here i'm looking at a project in which i have some bookmarks saved so we'll use that as the sample data in this example generally speaking we allow for only spreadsheet exports but there are certain edge cases where you can export data that you have created as a spatial file those two are basically where you have bookmarked or surveyed to”
- [172] [00:01:21](https://www.youtube.com/watch?v=EVN-9bqTEtM&t=81s) — “side here we go and you will also get an email notification clicking download downloads those files into a zipped folder i can then open that folder i'll want to extract it into a regular folder and you can see here that shapefiles come in a multi-file setup so what i'll do is i'll select all and now i'm going to tab over to my blank arc project and i'll simply click and drag all of those files into the left hand contents pane closing this out you can see that the bookmarks show up”

#### [173] Feature Service Product Demo

- Source: https://www.youtube.com/watch?v=X-_cLY3_96Y
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [173] [00:00:36](https://www.youtube.com/watch?v=X-_cLY3_96Y&t=36s) — “web apps hosted on agol the first and key step is to use our token and url to link the feature service to the arcgis online environment so to do that you go to content on the top left new item and from here you'll click url and here you'll paste in the url as well as the token that you got when you have access to that from the regrid team this will automatically uh select the arcgis server web service as the type which is correct we'll hit next you'll be prompted to set a title for”
- [173] [00:04:06](https://www.youtube.com/watch?v=X-_cLY3_96Y&t=246s) — “and then you would say save as and you're going to want to save this as a map so i'm going to call this regrid feature service demo map save it now that this has been saved i can go into our content page again from here you'll see both the feature layer that we added initially and then the web map that we just saved a second ago and from here you can click create app instant apps and then you'll be able to select from any of the multitudes of apps that are available here”

#### [175] DataTree Hacks: How to Find Portfolio Owners With Multiple Properties

- Source: https://www.youtube.com/watch?v=9RvXCiHUzlo
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [175] [00:00:09](https://www.youtube.com/watch?v=9RvXCiHUzlo&t=9s) — “Hey, what's going on? It’s Seth here from retipser.com. In this video, I'm going to show you two quick tricks for finding property owners who own multiple properties. Sometimes people refer to these as portfolio owners, and there's a number of different reasons why you might want to be aware of this when somebody owns multiple properties or to intentionally seek out property owners who own multiple properties. I know as a real estate investor, sometimes this can be a great source for motivated sellers or people who just have real estate to sell. Just being able to find”
- [175] [00:01:35](https://www.youtube.com/watch?v=9RvXCiHUzlo&t=95s) — “not just in that one state or that one county, but everywhere that they own under that name. And then you can go ahead and click on any one of these and do more research from there. But let's say you're trying to pull a list of property owners, whether it's for marketing purposes or direct mail or anything like that. And you want to find only the people who own multiple properties. Well, we would go up here to advance search and go through the usual steps. And by the way, if you've never been in DataTree and you have no idea how to filter a list like this,”

#### [176] DataTree Hacks: How to Search and Find Property Owners Nationwide

- Source: https://www.youtube.com/watch?v=y5XZp-4n_uc
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [176] [00:01:57](https://www.youtube.com/watch?v=y5XZp-4n_uc&t=117s) — “but we know that there's somewhere in California and we can see how many results show up this way. And in this case, it looks like it helped a lot to be able to add that first name in there. Because even though we're looking at the entire state of California, it narrows it down to 117 results now. And the really cool thing about DataTree, and there's not very many data services. In fact, I don't really know of any of the ones that allow you to do this is that you can search through the entire country at once, if you want to.”
- [176] [00:04:07](https://www.youtube.com/watch?v=y5XZp-4n_uc&t=247s) — “why we're searching for this information in the first place, there's a lot of different types of people that use DataTree for all sorts of different reasons. But again, the main point of this video is just to show you how easy it is to find into a person and the real estate they own on a nationwide basis. All you need to know is the name under which they own their real estate, be it their first and last name and or the name of their spouse, or the name of whatever entity they own that owns their real estate.”

#### [177] Regrid Parcel Data - Overview & Coverage

- Source: https://www.youtube.com/watch?v=EToN9mWFZWc
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [177] [00:00:45](https://www.youtube.com/watch?v=EToN9mWFZWc&t=45s) — “Matt today Blake is also here from the languor team but he you know typical glitches as always he's not able to hear us on on this webinar so let's get started this is exciting today we're just gonna talk about landed parcel data and just go through like an overview of what the parcel data is what our coverage is like what what sort of attribution we have how we deliver data etc and at the end we would like to open it up up to all of you who've joined us live right now for any questions so yeah”
- [177] [00:03:25](https://www.youtube.com/watch?v=EToN9mWFZWc&t=205s) — “primary property and parcel data collector for over a year close to 2 to 3 years now we work with counties directly and we obtain parcel boundaries the shape files the data and the taxes of the data that comes along with it now if those of you worked in this industry or have worked with this kind of data before you know that the data differs from County to County it's very disparate it's not standardized so our amazing team here which includes the two people that you will hear now Matt and Blake um they”

#### [178] Import Your Own Property Data - Regrid Property App (Web)

- Source: https://www.youtube.com/watch?v=6nMKiCCsK60
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [178] [00:00:01](https://www.youtube.com/watch?v=6nMKiCCsK60&t=1s) — “welcome to the regrid property app today we're going to be talking about importing data that you have into regrid the first thing to cover here is that regrid only supports data that can be tied to individual properties so that means you're going to need an address a parcel number or a latl coordinate to match what you have to our properties census data or other aggregate data isn't going to work here so let's say that you do have some property level data that you want to import for example you know you've got a list of properties”
- [178] [00:01:16](https://www.youtube.com/watch?v=6nMKiCCsK60&t=76s) — “work a little bit better so you've got your data set here next step is to bring it actually into the import setup so I'm going to go to the import tool here select a file click on the file that I want want to open uh you'll see the progress bars working away here um and what you see up at the top is just a preview of the file itself so the number of Records here uh the file name as well as the field names for each of the columns uh that's been pulled from the”

#### [179] Parcel data by the state on the Regrid Data Store \| Demo

- Source: https://www.youtube.com/watch?v=MdSAG5LMn4I
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [179] — supplied storyboard/description reconstruction; no quote timestamp: Regrid demonstrates self-service acquisition of statewide standardized parcel data at store.regrid.com, covering more than 155 million US parcels. Select a state, such as Ohio with approximately 5.29 million parcels across 88 counties. Inspect the County Coverage Report spreadsheet and Parcel Schema / Data Dictionary. Fields and tier distinctions include APN, owner name, mailing address, situs address, land use, valuation, building footprints and secondary addresses, across Standard and Premium offerings. Add a statewide dataset to the cart, complete checkout under the Data License Agreement and download the full state bundle or individual county files. Available formats include CSV, GeoJSON, Shapefile (SHP), File Geodatabase (GDB), GeoPackage (GPKG) and KML. Support is available at parcels@regrid.com. This reconstruction combines the visual screen tutorial and video description; it is not a verbatim audio transcript.

#### [180] Using Datasets - Regrid Property App (Web)

- Source: https://www.youtube.com/watch?v=-s07juX_8jE
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [180] [00:00:03](https://www.youtube.com/watch?v=-s07juX_8jE&t=3s) — “welcome to the regrid mapping platform today we're covering how to use data sets a data set simply put is any data that you have imported that you've created with a survey or a bookmark or which is publicly available on our platform it's basically just a collection of data into one file if you're in a project you can add data sets to the project by simply clicking data sets on the left hand side as i have selected here and then finding a data set of interest let's say that we're interested in one”
- [180] [00:01:02](https://www.youtube.com/watch?v=-s07juX_8jE&t=62s) — “and surveys and imported data that you have and if you'd like to delete any of these things you can click on the data set name and then scroll to the bottom where you will find a delete data set option”

#### [181] Regrid Mapping Platform - Filter Data

- Source: https://www.youtube.com/watch?v=cKYlwRY3aVw
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [181] [00:00:04](https://www.youtube.com/watch?v=cKYlwRY3aVw&t=4s) — “welcome to the regrid mapping platform today we'll be covering the filter tool filtering is the best way to find just properties that interest you by characteristics in our data for example you could use a filter to narrow down to just residential properties properties that are vacant or anything else that we have data for at the parcel level as with most of our mapping tools to get started we recommend you first create a project you can do this by clicking on the project drop down and then new project or you can open up a project that you”
- [181] [00:02:09](https://www.youtube.com/watch?v=cKYlwRY3aVw&t=129s) — “to look for a specific name for example let's look at this with owner if i click on it we can see the top examples but if i start typing the results will be refined to just ones that include that phrase so for example if i'm interested in various cities ownership here typing in city will bring up just those and if i then want to choose that to use as my filter i can click on the result you see it sort of enters into the box here and then when i click load on map”

#### [182] Troubleshooting Data Import - Regrid Property App (Web)

- Source: https://www.youtube.com/watch?v=VAtPDJ1KDjw
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [182] [00:00:03](https://www.youtube.com/watch?v=VAtPDJ1KDjw&t=3s) — “welcome to the regrid mapping platform today we're going to be talking about troubleshooting a spreadsheet import that you're attempting so starting at the most general level it's important to note that what regrid does in its importer is work with parcel level data meaning not census data you know not larger geographies but something that can be tied to specific properties this is a lot of the data that you may see floating around especially in open data portals so it's not a big deal but it's important to note that you need to get”
- [182] [00:01:09](https://www.youtube.com/watch?v=VAtPDJ1KDjw&t=69s) — “excel you can save it as a csv it's worth uh if you have an excel file we can accept excel files but if you're seeing issues it's often worth saving as a csv and trying that way just to reduce the number of variables so that's the first thing that you can try secondly you'll note that when you click import and you see the progress bars go through and you get to tested there is a finish import button however don't click that until you actually see what the match rate and sort of how the import is going it”

#### [183] Quick Start - The Regrid Property App (Web)

- Source: https://www.youtube.com/watch?v=1Wm_NPEagT8
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [183] [00:00:00](https://www.youtube.com/watch?v=1Wm_NPEagT8&t=0s) — “welcome to the regrid mapping platform today we're going to do a quick start guide that should get you right into our data and able to see and use our tools so first things first you're going to want to go to app. rd.com plans and choose a plan uh starter will get you able to browse around for free um but to use most of the tools and other things we're going to be talking about in this video you'll want to be a pro or a team subscriber once you have that all set up”
- [183] [00:04:18](https://www.youtube.com/watch?v=1Wm_NPEagT8&t=258s) — “rundown uh remember you can always get back to your dashboard if you'd like uh from the top left uh you can also have a quick link to your billing there um you can sign in and out from here if you're signed out uh you can do that and then one final note is that if you're a paying Pro or team subscriber uh your credentials will also work on our companion mobile app so if you search regrid mobile app or regrid property app in the app store for Android or Apple uh you can download it”

#### [186] Best Real Estate Data APIs for Building a Deal Finder App

- Source: https://www.youtube.com/watch?v=NMsRlUhQbUI
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [186] [00:00:00](https://www.youtube.com/watch?v=NMsRlUhQbUI&t=0s) — “I'm a real estate investor that wants to leverage AI in my investing. Specifically, I want to build a tool that searches for active listings in my market and automatically sends me the best deal every day. Sounds nice, right? But there's just one problem. I need data. And it turns out that getting real estate data, particularly for onmarket listings, is not an easy task. Especially if you want nationwide coverage and you don't have a real estate license or direct access to an MLS. But just because something's difficult doesn't mean it's impossible.”
- [186] [00:04:50](https://www.youtube.com/watch?v=NMsRlUhQbUI&t=290s) — “bother me cuz I'm not a commercial real estate investor. So, it's decided for my first version of building an onmarket AI enabled deal finding app, I'm going to move forward using rentcast data. So, let's recap. I started with dozens of options for real estate data, but I first eliminated consumer websites like Zillow and Redfin because scraping them is a major legal liability and likely not going to work out in the long term. I also eliminated MLS dependent platforms that required too much red tape, licensing, and bureaucracy. And lastly, I filtered down the remaining”

#### [189] DataTree Hacks: TaxSource Reports and Property Tax Verification

- Source: https://www.youtube.com/watch?v=2ThZ61aal9k
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [189] [00:00:09](https://www.youtube.com/watch?v=2ThZ61aal9k&t=9s) — “Hey guys, what's going on? It’s Seth here. In this video, I'm going to show you a few tricks you can use in DataTree to check on a properties tax status. And what I mean by that is finding out how much the annual property tax bill is for that property when that tax bill is due each year, whether or not it's paid current, and if it's not paid current, how far delinquent it is. And you can do this nationwide in DataTree. And there's a little pricing sheet right here that explains how much it costs. So in most states you are able”
- [189] [00:01:05](https://www.youtube.com/watch?v=2ThZ61aal9k&t=65s) — “And what we have to do is go over here to property data reports, and right here, where we see tax source report that's what we're going to click on. So we're going to click that and then click order. And it's going to take just a few seconds for this to pop up and I'll show you what we can see here. All right. So here it is. So we can see a lot of the basic inform about the property and the tax agency that collects the tax bills. And right here, we can see when the tax bills are due each year. It looks like there's”

## Domain 8: Autonomous Agent SOPs, Decision Matrices & Master Tool/Database Directory

Primary video assignments: [008], [009], [018], [019], [020], [021], [023], [048], [050], [055], [068], [101], [103], [107], [187]

### 8.1 End-to-end autonomous case SOP

**Input:** lead and research objective.
**Output:** case dossier with evidence and next action.

**Ordered procedure (editorial synthesis):**

1. Ingest raw evidence and assign immutable source IDs.
2. Resolve owner identity, death and domicile.
3. Prove heir relationships and determine estate authority.
4. Resolve parcel/asset identity, title, liens and custodian.
5. Calculate net recovery or acquisition economics.
6. Prepare the specific filing/curative packet with source-linked fields.
7. Track submission, supplements, adjudication, payment and closure as distinct states.

**Execution and acceptance contract:**

- Persist `case dossier with evidence and next action` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [031] [00:09:22](https://www.youtube.com/watch?v=VbgMCP7bKcs&t=562s) — “it's not that important to resolve and know the exact date of birth um go ahead and give a brief explanation um in your software or in your report wherever you keep track of your family history and then move on so now let's move on to some more complex conflicting evidence we can come across in our research the first is relationships just like today our ancestors families often included complex relationships of many types including biological relationships adopted and that could be formally adopted or informally illegitimacy half relationships step relationships and remarriages so we”
- [107] [00:08:35](https://www.youtube.com/watch?v=Gk0D4wVEXmc&t=515s) — “niche or the industry that you're in, like asset recovery, you're unclaimed funds, this is gonna make you look really slick when you are emailing a potential claim it... You wanna sign and you need to send them some documents to prove there is an account out there that you can recover for them. 0:08:52.6 S1: Okay, now this is something you guys... I like using Google, but any email provider out there, you can do that for free. So if you're with the Aha, you can do it at Yahoo, you just be like, Oh no, north star asset recovery, Yahoo dot com. There's an example...”
- [015] [00:13:46](https://www.youtube.com/watch?v=7M3XZfN7814&t=826s) — “able to take all of that evidence and resolve it and come to a conclusion and your conclusion is going to be the best that you can come to at the time with the evidence that you have been able to to loc to identify so the purpose of the source citation again is to help you just like the creating the source to help you analyze that information again much like the source the only thing that's required in this field is some kind of a title um so in this case we're going to”
- [179] — supplied storyboard/description reconstruction; no quote timestamp: Regrid demonstrates self-service acquisition of statewide standardized parcel data at store.regrid.com, covering more than 155 million US parcels. Select a state, such as Ohio with approximately 5.29 million parcels across 88 counties. Inspect the County Coverage Report spreadsheet and Parcel Schema / Data Dictionary. Fields and tier distinctions include APN, owner name, mailing address, situs address, land use, valuation, building footprints and secondary addresses, across Standard and Premium offerings. Add a statewide dataset to the cart, complete checkout under the Data License Agreement and download the full state bundle or individual county files. Available formats include CSV, GeoJSON, Shapefile (SHP), File Geodatabase (GDB), GeoPackage (GPKG) and KML. Support is available at parcels@regrid.com. This reconstruction combines the visual screen tutorial and video description; it is not a verbatim audio transcript.

### 8.2 Decision gates and exception queue

**Input:** case dossier.
**Output:** decision log and exceptions.

**Ordered procedure (editorial synthesis):**

1. Gate identity on discriminating evidence, not name similarity.
2. Gate heirship on proven links and documented unresolved branches.
3. Gate authority on actual appointments, orders or eligible successor procedure.
4. Gate economics on net proceeds and downside costs.
5. Send missing evidence, conflicting orders and uncertain legal rules to a specific exception queue with owner and due date.
6. Never convert unknown into false or zero merely to complete a workflow.

**Execution and acceptance contract:**

- Persist `decision log and exceptions` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [035] [00:13:18](https://www.youtube.com/watch?v=7Jn_XMUozo0&t=798s) — “and these were the methodologies used by attorneys to take matters to court and to present cases before before various agencies and courts and things. Okay, so these rules of civil procedure and criminal procedure both contained uh a sections called the rules of evidence. And the rules of evidence were very specific about how evidence is presented in court and considered by a judge. And those terms that we see and that I see here in front of us uh that I put up on the screen are specifically defined in uh the rules of evidence and”
- [013] [00:08:58](https://www.youtube.com/watch?v=Xe2NEfqDwTQ&t=538s) — “started practicing law now more than 40 years ago the whole book of rules of civil procedure was approximately half an inch thick by the time I finished it was closer to 2 inches thick so the rules of procedure have become much more complex and more difficult to learn and surprisingly the Rules of Civil Procedure not the law is it can be often determined who wins or loses in the case many times the cases are won or lost in the procedures not in the the actual trial of the case now how do we”
- [149] [00:02:37](https://www.youtube.com/watch?v=hpvnOFjxwaM&t=157s) — “probated in delaware county we're going to focus on the search types case names option the specific criteria that corresponds to the case names option involves name type name options name death date and filing date for purposes of this video i'm going to focus on searching by name but of course you can use any of the specific criteria that you think would be most helpful to you when searching for name make sure to search last name first the way that our system is set up is you would need to search for smith john if the decedent's name”
- [031] [00:00:03](https://www.youtube.com/watch?v=VbgMCP7bKcs&t=3s) — “\[Music\] hello my name is melissa finley and this is the presentation called dueling dates and fact fights resolving evidence conflicts part one the fourth element of the genealogical proof standard created by the board for certification of genealogists states that we must make a resolution of conflicting evidence to reach a sound conclusion in our genealogical research but what is conflicting evidence the law dictionary website provides this definition conflicting evidence is evidence that is taken from different sources that contradict each other in this class part one of two of dueling dates and fact fights”

### 8.3 Research quality and tool selection

**Input:** research tasks and available tools.
**Output:** research log and tool capability matrix.

**Ordered procedure (editorial synthesis):**

1. Prefer official source images over commercial summaries when resolving decisive facts.
2. Compare retrieval coverage, freshness, cost and citation quality for every tool.
3. Log successful and negative queries with exact variants and date ranges.
4. Deduplicate copied-source assertions before measuring corroboration.
5. Require reproducible citations and record the limits of automated extraction.

**Execution and acceptance contract:**

- Persist `research log and tool capability matrix` under the case identifier with an immutable source manifest.
- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.
- Log conflicting evidence and the specific next retrieval needed to resolve it.
- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.

**Related corpus evidence — inspect for scope and exceptions:**

- [018] [00:01:13](https://www.youtube.com/watch?v=FxQgurvv3_g&t=73s) — “question and then we come to source citations and research logs so we want to make sure that as we are searching our plan doing our planned research that we have a research log where we are keeping track of where we've been and what we've looked at and the source citation is key because this is where we write exactly what we found or what we didn't find in a source citation and i want to make a note that sometimes we have negative source citations if we have browse an entire micro film on family search and”
- [020] [00:11:30](https://www.youtube.com/watch?v=J1h18kFbXKU&t=690s) — “document that says that the event happened who was involved do you have fan club and how does it affect the research compare with other people in the locations and definitely compare with historic maps how is this important to the research question let's look at a sample of a timeline put together with elements of my research log and data lists on the whitman's in albany saratoga and schenectady counties and see what kind of connections we can find note that my facts in my timeline never go naked in fact i've got more source citations here”
- [019] [00:17:50](https://www.youtube.com/watch?v=PfqiDmLnMIg&t=1070s) — “we can continue our research but this is the example here is a straightforward case it doesn't need more complex treatment for its research log so a summary of style one the log by date searched log by date searched is a diary of research they're all a diary of research no matter what style of log you use the negative positive searches without result they all go in there because no matter what you're doing if you can't find it you can't use it and i don't know how many times if i've just gotten excited”
- [016] [00:01:16](https://www.youtube.com/watch?v=DUAbGD8rVzA&t=76s) — “i use a research log and i create a source citation for each source that i search that goes right into my research log and then when i'm ready to write my conclusions i have a source citation ready to go for my research log and i can write up an entire report about what i've found for that research objective so now that you have an idea of what a research process could look like whether you use that or not let's talk about why you even need to cite your sources and here are some of my favorite reasons”

### Domain evidence workbench

The following source-specific evidence cards expose primary assigned videos without treating lexical matches as verified legal rules.

#### [008] New Techniques to Find Missing Beneficiaries - PBI Research Services BeneSearch Webinar

- Source: https://www.youtube.com/watch?v=rR4YCKGVNmg
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [008] [00:21:15](https://www.youtube.com/watch?v=rR4YCKGVNmg&t=1275s) — “regard to your census file and a big part of that is our service census solution which will not just find missing participants or you know deceased participants or pensioners within your plan but will also keep your beneficiaries up to date on a continual basis available via ad hoc also available in some of our ongoing Services mainly um Serta census um you know who do you contact well there's a couple ways you can do this uh one is you have my contact information here certainly feel free to contact attack me I can push you in the right”
- [008] [00:24:51](https://www.youtube.com/watch?v=rR4YCKGVNmg&t=1491s) — “participant date of birth that really helps us identify uh deceased participants information pull in and find obituary text so we can provide that in the in the report if you are missing any of that information PPI certainly has a ways and other services that we provide to pull in that missing information so let's say that you have the name and address but you're missing the social security number we have services that can provide any part of those those missing data points that you have you just contact us and we can walk you uh on how to start those”

#### [009] A Guide To Our Fee Options • Fraser and Fraser

- Source: https://www.youtube.com/watch?v=EPZo6YVIMi4
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [009] [00:01:47](https://www.youtube.com/watch?v=EPZo6YVIMi4&t=107s) — “beneficiaries this is irrespective of whether or not there are already some known beneficiaries to the estate or trust we would always recommend this fee option for cases whereby somewhere is already known as the contingency nature of this protects them from research fees which may not actually yield results here the personal representative agrees with fraser and fraser to be paid a share of the entitlement of each air that we trace typically a lower fee is charged than that of the beneficiary contingency option because the fee is agreed prior to research commencing we usually expect”
- [009] [00:03:32](https://www.youtube.com/watch?v=EPZo6YVIMi4&t=212s) — “locate the beneficiary's thought it may also be that the research will turn out to be more expensive than we've originally thought we will therefore discuss that with you and you must be prepared for the fact that the budget may have to increase he will however have control of any budget increases along the way proceeding under the time spent option provides no guarantees about time scales and therefore you may wish to consider a fixed fee option instead under the fixed fee the budget is usually larger than that on the time spent basis under the guarantee that the”

#### [018] Peeling Back the Layers: Citing Sources From Online Materials, Part 3

- Source: https://www.youtube.com/watch?v=FxQgurvv3_g
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [018] [00:00:01](https://www.youtube.com/watch?v=FxQgurvv3_g&t=1s) — “welcome to peeling back the layers citing sources from online materials part three my name is diana elder i'm an accredited genealogist and you can find me at familylocket.com the content of this video as well as the thoughts views and opinions expressed herein belongs solely to the creator and do not necessarily reflect the views of family search international and roots tech in part one and part 2 of this series i talked about the genealogy research process and where source citations fit and so let's just review that again when we do a project or when we are”
- [018] [00:02:57](https://www.youtube.com/watch?v=FxQgurvv3_g&t=177s) — “and there are billions of wonderful records that are digitized and available for us to use for free now remember step two that we create our citation by answering the five questions the who what where is when and where in and because we're doing layered citations we'll be answering these for both layers but we don't always need to duplicate information so sometimes one layer can answer the question of who and we don't need to duplicate it in the other layer and we'll look at some examples of that we're going to start with looking at a”

#### [019] Research Logs: A Variety of Styles to Suit Your Project, Part 1

- Source: https://www.youtube.com/watch?v=PfqiDmLnMIg
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [019] [00:00:01](https://www.youtube.com/watch?v=PfqiDmLnMIg&t=1s) — “\[Music\] welcome to research logs a variety of styles to suit your project this is part one of three i'm rebecca whitman coford certified genealogist and certified genealogical lecturer in this three-part series we will explore three research log style varieties first date searched style second the record category style and last the plan and log style as we go we'll also discuss the value of research logs part one will focus on the basic style that any research log can start with the date research style in each part i will also introduce a”
- [019] [00:14:30](https://www.youtube.com/watch?v=PfqiDmLnMIg&t=870s) — “card under irwin with an i a porter and i found that on fold three so what do i do next with that this looked like a long card of a military service record and so i went to family search wiki because if i don't know what something is my first instinct is to find out more about that record where do i find the record what does the record mean what can the record do for my research and one of my favorite things to do is to go to family search wiki to find out”

#### [020] Research Logs: A Variety of Styles to Suit Your Project, Part 2

- Source: https://www.youtube.com/watch?v=J1h18kFbXKU
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [020] [00:00:01](https://www.youtube.com/watch?v=J1h18kFbXKU&t=1s) — “\[Music\] welcome to research logs a variety of styles to suit your project this is part two of three i am rebecca whitman coford certified genealogist and certified genealogical lecturer in this three-part series we will explore three research log style varieties first the date search style second the record category style and last the plan and log style as we go we'll also discuss the value of research logs in this part 2 we will focus on the record category style in each part i'll also introduce a complementary organizational technique to work with”
- [020] [00:02:50](https://www.youtube.com/watch?v=J1h18kFbXKU&t=170s) — “evidence and what all of this means a research log is a working document for you it's as i said before in part one it's your brain on paper and i'm saying it again you're making calculations in writing right here the only wrong way is to not record your searches now to introduce the record type research log it's one of my favorites to use when we use the record type research log it's simply that we take notes by category of record type because it operates as a checklist of resources we like in any research log we document”

#### [021] Research Logs: A Variety of Styles to Suit Your Project, Part 3

- Source: https://www.youtube.com/watch?v=KpQQ3n37XXM
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [021] [00:00:01](https://www.youtube.com/watch?v=KpQQ3n37XXM&t=1s) — “\[Music\] welcome to research logs a variety of styles to suit your project this is part three of three i'm rebecca whitman-covert certified genealogist and certified genealogical lecturer in this three-part series we explore three research log style varieties first date search style second the record category style and last the plan and log style as we go we discuss the value of research logs part 3 focuses on the research plan and log style in parts i introduce a complementary organizational technique to work with any of the research log styles for more effective analysis”
- [021] [00:05:16](https://www.youtube.com/watch?v=KpQQ3n37XXM&t=316s) — “sharing my findings but for analysis and reaching conclusions in a sound way this is exactly how i felt when i started to really find value in research logs so here's an idea even if you're already keeping research logs or you want to start really getting your your teeth into a good project revitalize an old project by rewriting or restarting your research log in a different style so let's talk about research plans planning research starts with identifying a research question sometimes we have to research mid-project goals to a main question i'll give you”

#### [023] GenealogyMagazine, Episode 1: Courthouse Research

- Source: https://www.youtube.com/watch?v=DjxOkXDU2cY
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [023] [00:01:43](https://www.youtube.com/watch?v=DjxOkXDU2cY&t=103s) — “uncle's name on a list of confirmed soldiers with the notation he'd been killed at Fort Donelson which confirmed a family story in the basement of an Alabama courthouse I came across a newspaper collection dating back to the 1880s and this is how I found an obituary for my three-times great-grandmother that alone is enough to make a genealogist do a happy dance before you rush off to the courthouse be prepared you never know what lurks behind these doors in my experience I have found most clerks are nice but not always get out get out come back maybe”
- [023] [00:03:14](https://www.youtube.com/watch?v=DjxOkXDU2cY&t=194s) — “days and hours Virginie illogical inquiries Oh before you go make a list of documents that you would like to find have the records in microfilm check familysearch.org to see what's been filmed and digitized by the LDS have any of these records been transcribed for publication in books periodicals or online databases transcriptions and abstracts are extremely helpful but think of them as guides to records not substitutes the District Clerk's office has criminal records as well as civil suits which is where you'll find divorced cases these documents are usually stored in vaults so you'll need”

#### [048] NALP webinar, May 2024 - what is it like working in the Probate Research Industry

- Source: https://www.youtube.com/watch?v=zz_ksXmJqyI
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [048] [00:03:04](https://www.youtube.com/watch?v=zz_ksXmJqyI&t=184s) — “involve um so probate is the administration and the transfer of assets previously owned by a deceased person then we combine that with the research so probate research overall is assisting estate administrators and others in the probate industry just to trace and approve the claims of rightful heirs um when I joined in the industry and I think largely is still called probate gen energy on occasion so then again we're just linking the probate side of it to the genealogy side of it I think probably your question is quite apt because more and more we're having”
- [048] [00:19:18](https://www.youtube.com/watch?v=zz_ksXmJqyI&t=1158s) — “trace someone or a different way to do research in however many countries there is overseas that you need to do research in so you never stop learning you work on cases B similar to like how a lawyer would work on a Case when they're conducting the administration so you do get that sense of satisfaction from opening a case working on it as a team so teamwork and then closing a case out and ultimately the beneficiaries receiving their inheritance so yeah super rewarding really good job for dinner parties when you're speaking to”

#### [050] TGP 19 - Eileen O'Duill - Probate Research

- Source: https://www.youtube.com/watch?v=7v_UB7hKgKg
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [050] [00:30:10](https://www.youtube.com/watch?v=7v_UB7hKgKg&t=1810s) — “were you talking about okay yeah I will put a link to that into the show notes so people will be able to find that I hear they're terrific do you have a productivity tool or an app like Dropbox that you love and can share with the audience I do use Dropbox and I like it but I don't use it as much as I perhaps should I should develop more use of it do you have any other tools that you use for productivity long hours of hard work that's productivity okay seeing up late because”
- [050] [00:36:54](https://www.youtube.com/watch?v=7v_UB7hKgKg&t=2214s) — “I want you to do for this action item is determine if you have the right equipment there is a little upfront cost with being a public speaker and you need to have certain equipment because not every place that you go will have the equipment necessary to make a presentation most presentations today are done using a laptop and presenting some kind of PowerPoint or keynote presentation PowerPoint being the Windows product keynote being I believe the Mac product so at the very minimum you really do need to of a laptop you don't always have to”

#### [055] Part One • 10 Steps To Building Your Own Family Tree • Fraser and Fraser

- Source: https://www.youtube.com/watch?v=MdFDiQQXD3M
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [055] [00:00:06](https://www.youtube.com/watch?v=MdFDiQQXD3M&t=6s) — “thanks to the internet it's never been easier to trace your family tree however it's quite a daunting task setting off and knowing what's correct where to look in this series of films we're going to try and give you a few hints to tell you how to get started and how to build your very own family tree get the biggest piece of paper you can find and jot down all you know about your family in the form of the family tree it's best to look online for a template and the best thing is to put”
- [055] [00:01:55](https://www.youtube.com/watch?v=MdFDiQQXD3M&t=115s) — “the first thing you're going to want to decide when you're mapping out your findings is whether you're going to draw it out on a family tree with pen and paper the old fashioned the cheaper way or as we would advise get yourself a good family history piece of software and that means that every time you need to change your family tree you can make the changes to the software and they'll change the outline of the tree for you means you won't be crossing out and rubbing things out all the time makes”

#### [068] How to Link Unindexed Images to FS by Ann Tanner 10 minutes

- Source: https://www.youtube.com/watch?v=zTQCnGBnAvc
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [068] [00:02:23](https://www.youtube.com/watch?v=zTQCnGBnAvc&t=143s) — “record is now available on Family Search and I would like to attach this original digitized copy of this original record to this person so everybody can see it now I've already done the research so I'm not going to tell you how to do research that's up to you but I'm going to show you the process and how you can access these records first of all we're going to go to search it's one of the tabs across the top and we're going to search the catalog okay catalog she was born in Sweden so we'll”
- [068] [00:07:12](https://www.youtube.com/watch?v=zTQCnGBnAvc&t=432s) — “really enjoy seeing as this one was a delight to research I'm going to go ahead and attach this now to family tree okay the source is already in here it gives us that what is in this record I'm going to say birth and christening record and we'll use the patronymic Anders daughter Hall showing her parents then we are going to select a person and again this is so easy and elegant and this is a very new feature of Family Search so we select Amanda Matilda I check her ID number to make sure I've”

#### [101] State Funds Tutorial Top 4 Tech Tools Needed For Your State Funds Business

- Source: https://www.youtube.com/watch?v=ApkuK7OOL9w
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [101] [00:02:19](https://www.youtube.com/watch?v=ApkuK7OOL9w&t=139s) — “there looking at these crms you guys they don't you don't need to spend money on them and they don't need to be super fancy they seem to be able to do the basic functions of what a CRM can do now because this is so important I want to go a little bit more in depth about why crms are so important and just the daily workflow on how you can use it so number one while you're speaking to somebody on the phone you take manual notes of the conversation with a pen and”
- [101] [00:03:18](https://www.youtube.com/watch?v=ApkuK7OOL9w&t=198s) — “to get really good at following up with people okay following up with people that's the goal of this business because most of the money is made and the follow-up now I know that some of the advanced people listening to this they're going to say no David you're wrong what you need to do is have an automation trigger on your auto dealer that pushes a lead information in your CRM and yes that's true that's how I run my business but I know a lot of you guys are going through YouTube University you”

#### [103] State Funds Tutorial: 5 Tech Tools For Your State Funds Business

- Source: https://www.youtube.com/watch?v=ES6y4iF-bBM
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [103] [00:00:00](https://www.youtube.com/watch?v=ES6y4iF-bBM&t=0s) — “0:00:00.0 S1: My name is David Wilkerson, and this is surplus funds 101. And today, I'm gonna be talking to you guys about the five tech tools you need to run your state funds business. If you guys are just getting started, you're probably wondering where do I start, what do I need today in this video, I'm gonna cover all that for you before I do, I wanted to first start off by saying thanks to all the people who like the video, subscribe to the channel, if you guys haven't done that, go do that now. On this channel, I share with”
- [103] [00:00:54](https://www.youtube.com/watch?v=ES6y4iF-bBM&t=54s) — “0:00:55.0 S2: You just go click on the link below and it's an instant download... Non-instant download, I'm sorry, in syntax and you can happen start watching videos and training right away with that being said, here are my top five tech tools, when you're just getting started to run your state funds business, the 0:01:13.1 S1: Very first thing you guys is a CRM stands for customer relationship software for you guys that are brand new. 0:01:21.0 S2: Pretty much all this does is it keeps track and it manages all the people that”

#### [107] Surplus Funds 101 Tutorial: Top 4 FREE Software Platforms For Your State Funds Business

- Source: https://www.youtube.com/watch?v=Gk0D4wVEXmc
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [107] [00:03:41](https://www.youtube.com/watch?v=Gk0D4wVEXmc&t=221s) — “0:03:41.4 S1: You take the phone home and you never end up using it, like you paid for something that she didn't really need, and so you really have to understand from start to finish, everything that's included in a successful transaction and all of the different key features they're gonna facilitate that without having to over-pay for anything... Okay, so those are my three things. But the very first thing you guys are gonna need is the CRM... HubSpot or Salesforce is what I've found to be the easiest for most people. I use HubSpot,”
- [107] [00:08:35](https://www.youtube.com/watch?v=Gk0D4wVEXmc&t=515s) — “niche or the industry that you're in, like asset recovery, you're unclaimed funds, this is gonna make you look really slick when you are emailing a potential claim it... You wanna sign and you need to send them some documents to prove there is an account out there that you can recover for them. 0:08:52.6 S1: Okay, now this is something you guys... I like using Google, but any email provider out there, you can do that for free. So if you're with the Aha, you can do it at Yahoo, you just be like, Oh no, north star asset recovery, Yahoo dot com. There's an example...”

#### [187] The Fastest Way to Research Any Property in the United States

- Source: https://www.youtube.com/watch?v=ntT8V0gnpAs
- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.
- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.
- [187] [00:03:10](https://www.youtube.com/watch?v=ntT8V0gnpAs&t=190s) — “I'll go here and click on Florida because that's where this property is at. And then this is in Putnam County, Florida. Now I'll actually say more often than not when I'm starting this process, the information that I do have is the owner's name, not necessarily the parcel number. And usually it's pretty easy to find it that way. However, the parcel number is a more precise way of finding it, because there's pretty much only one parcel in the entire county with that number. Whereas sometimes you'll find that an owner may own like a bunch of different properties”
- [187] [00:06:14](https://www.youtube.com/watch?v=ntT8V0gnpAs&t=374s) — “outstanding loans or mortgages, or leans on the property. Which is certainly helpful, however you also gotta keep in mind with a lot of vacant lots, there are no mortgages on them because most banks won't lend on them in the first place. So usually that's not gonna be an issue anyway. However, if you did want to click the Total View Report, it would give you that information. It also tells you a lot of other interesting stuff like market trends, and comparables, and prior listing history. Which frankly I would find to be a lot more helpful”

## State-specific recovery research matrix

| Jurisdiction | Required operational fields | Corpus evidence leads |
|---|---|---|
| California | Registration; fee/contract restrictions; claim authority; steps; exact deadline; effective date. Not established solely by retrieval. | [082] (whole-video reconstruction), [094] 00:04:13, [130] 00:29:54 |
| Ohio HB 96 | Registration; fee/contract restrictions; claim authority; steps; exact deadline; effective date. Not established solely by retrieval. | [082] (whole-video reconstruction), [094] 00:04:13, [130] 00:29:54 |
| Pennsylvania Treasury | Registration; fee/contract restrictions; claim authority; steps; exact deadline; effective date. Not established solely by retrieval. | [082] (whole-video reconstruction), [094] 00:04:13, [111] 00:05:19 |
| Michigan | Registration; fee/contract restrictions; claim authority; steps; exact deadline; effective date. Not established solely by retrieval. | [082] (whole-video reconstruction), [097] 00:00:02, [094] 00:04:13 |
| Delaware | Registration; fee/contract restrictions; claim authority; steps; exact deadline; effective date. Not established solely by retrieval. | [082] (whole-video reconstruction), [099] 00:02:01, [094] 00:04:13 |
| New Mexico | Registration; fee/contract restrictions; claim authority; steps; exact deadline; effective date. Not established solely by retrieval. | [100] 00:06:35, [082] (whole-video reconstruction), [069] 00:41:59 |

## Decision matrices

| Condition | Route | Required output |
|---|---|---|
| Owner alive, identity matched | Direct owner claim | Ownership/address evidence |
| Owner deceased, representative appointed | Estate representative route | Valid appointment and asset entitlement |
| Owner deceased, no administration | Evaluate jurisdiction-specific successor procedure | Eligibility and complete heirship proof |
| Property pre-escheat notice | Holder route | Holder confirmation and notice deadline |
| Recorded lien conflicts with surplus schedule | Reconcile both verification methods | Priority/order/payoff evidence |
| Fractional parcel interest only | TIC acquisition analysis | Cap table and control/exit assessment |
| Conflicting identities | Keep entities separate | Discriminating source retrieval |
| Missing numeric rule | Retrieve official rule | Jurisdiction/date-specific authority |

## Master Tool / Portal / Statute / Database Candidate Directory

Automatically detected names and URLs from every transcript and metadata description. This is a candidate inventory: ASR misspellings, unnamed references and ambiguous short names require source review. Each video’s entry distinguishes transcript from description mentions.

- **13101** — [081]
- **Ancestry** — [001], [002], [003], [005], [006], [007], [011], [015], [016], [017], [018], [019], [020], [021], [022], [024], [025], [026], [027], [028], [029], [030], [031], [032], [033], [036], [037], [039], [040], [047], [048], [050], [054], [055], [056], [057], [058], [059], [060], [061], [062], [063], [064], [065], [067], [069], [070], [072], [073], [074], [075], [076], [077], [079], [123], [140], [144]
- **ArcGIS** — [172], [173]
- **Bing** — [027]
- **Chronicling America** — [007], [024], [067], [069], [071], [076]
- **ClaimIt.ca.gov** — [082], [092], [112]
- **CSV** — [177], [178], [179], [181], [182], [184]
- **DataTree** — [088], [167], [168], [175], [176], [187], [189]
- **Declaration Under Probate Code 13101** — [081]
- **Excel** — [008], [119], [124], [137], [146], [178], [182], [185]
- **Facebook** — [002], [004], [005], [006], [007], [015], [016], [017], [018], [019], [020], [021], [022], [027], [028], [029], [031], [032], [035], [037], [047], [048], [050], [051], [056], [058], [059], [060], [062], [066], [067], [070], [072], [073], [074], [075], [077], [084], [085], [086], [087], [088], [089], [090], [102], [108], [109], [113], [114], [117], [118], [119], [120], [121], [122], [123], [124], [125], [126], [127], [128], [129], [130], [131], [132], [133], [134], [135], [136], [137], [139], [145], [147], [148], [151], [152], [153], [154], [155], [156], [157], [158], [160], [162], [168], [174], [187]
- **FamilySearch** — [001], [007], [011], [014], [016], [017], [018], [019], [020], [021], [022], [023], [024], [025], [026], [029], [031], [032], [033], [034], [039], [040], [056], [057], [059], [060], [061], [062], [063], [064], [065], [066], [067], [068], [070], [071], [074], [075], [076]
- **Find a Grave** — [019], [034], [038], [059], [074], [075], [076], [140], [158]
- **FindAGrave** — [139], [140]
- **Fixity Pro** — [170]
- **Garn** — [158], [159]
- **GDB** — [179]
- **GeoJSON** — [165], [179]
- **GeoPackage** — [179]
- **Google** — [005], [015], [022], [024], [025], [027], [035], [037], [045], [050], [057], [061], [063], [067], [073], [075], [077], [080], [085], [087], [088], [095], [096], [098], [100], [101], [103], [107], [108], [118], [119], [123], [124], [127], [134], [137], [139], [143], [145], [147], [152], [156], [157], [158], [163], [177], [183], [187], [189]
- **GPKG** — [179]
- **HB 96** — [113]
- **http://bit.ly/2O3zS75** — [169]
- **http://bit.ly/316g9t4** — [169]
- **http://coaching.dpasummit.com** — [118], [123], [135], [146], [147]
- **http://creativecommons.org/licenses/by/3.0/** — [062], [076]
- **http://creativecommons.org/licenses/by/3.0/➡🔴🔴** — [070]
- **http://delcode.delaware.gov/title12/c011/sc02/index.html** — [099]
- **http://eepurl.com/dJpXAQ** — [070], [076]
- **http://eepurl.com/dJtBOo** — [076]
- **http://familysearch.me/facebook** — [016], [017], [018], [019], [020], [021], [022], [029], [031], [032], [056], [060]
- **http://familysearch.me/home** — [016], [017], [018], [019], [020], [021], [022], [029], [031], [032], [056], [060]
- **http://familysearch.me/instagram** — [016], [017], [018], [019], [020], [021], [022], [029], [031], [032], [056], [060]
- **http://familysearch.me/RootsTech** — [016], [017], [018], [019], [020], [021], [022], [029], [031], [032], [056], [060]
- **http://familysearch.me/twitter** — [016], [017], [018], [019], [020], [021], [022], [029], [031], [032], [056], [060]
- **http://familysearch.me/youtube** — [016], [017], [018], [019], [020], [021], [022], [029], [031], [032], [056], [060]
- **http://familysearch.me/youtubeeurope** — [016], [017], [018], [019], [020], [021], [022], [029], [031], [032], [056], [060]
- **http://familysearch.me/youtubeportuguese** — [016], [017], [018], [019], [020], [021], [022], [029], [031], [032], [056], [060]
- **http://familysearch.me/youtubespanish** — [016], [017], [018], [019], [020], [021], [022], [029], [031], [032], [056], [060]
- **http://genealogysstar.blogspot.com/2014/07/online-digital-newspaper-collections-by.html** — [024]
- **http://newspaperarchive.com/** — [024]
- **http://reieducationacademy.com/earnings-disclosures** — [160]
- **http://trove.nla.gov.au/** — [024]
- **http://www.ancestry.com/s89299/t38352/rd.ashx** — [028]
- **http://www.ancestry.com/s89365/t38352/rd.ashx** — [006]
- **http://www.ancestry.com/s89386/t38352/rd.ashx** — [058]
- **http://www.ancestry.com/s89392/t38352/rd.ashx** — [015]
- **http://www.ancestry.com/s89585/t38352/rd.ashx** — [027]
- **http://www.ancestry.com/s89589/t38352/rd.ashx** — [037]
- **http://www.ancestry.com/s89613/t38352/rd.ashx** — [002]
- **http://www.ancestry.com/s89715/t38352/rd.ashx** — [072]
- **http://www.ancestry.com/s89770/t38352/rd.ashx** — [073]
- **http://www.anrdoezrs.net/click-9110145-13783401** — [076]
- **http://www.britishnewspaperarchive.co.uk/** — [024]
- **http://www.dpbolvw.net/click-9110145-13783399** — [076]
- **http://www.heirsireland.com/** — [050]
- **http://www.investorfuel.com/apply** — [127]
- **http://www.investorfuel.com/club** — [127]
- **http://www.investorfuel.com/retreat** — [127]
- **http://www.investormachine.com** — [127]
- **http://www.TheGenealogyProfessional.com/leslie-lawson** — [005]
- **http://www.thegenealogyprofessional.com/leslie-lawson/** — [005]
- **http://www.tkqlhce.com/click-9110145-13783399** — [076]
- **http://www.tkqlhce.com/click-9110145-13783400** — [076]
- **http://www.youtube.com/c/jamelgibbs** — [160]
- **http://www.youtube.com/channel/UCsc0AQkAh_2cQmxqwD6VWRw?sub_confirmation=1** — [002], [006], [015], [027], [028], [037], [058], [072], [073]
- **https://amzn.to/2BiLjBz** — [070], [076]
- **https://amzn.to/2BllDEv** — [070], [076]
- **https://amzn.to/2GmPgIM** — [070], [076]
- **https://amzn.to/2MPHMiL** — [070], [076]
- **https://amzn.to/2TtI6WR** — [070], [076]
- **https://amzn.to/2TtSNsE** — [070], [076]
- **https://amzn.to/2WFGbAM** — [070], [076]
- **https://amzn.to/35KUHOe** — [169]
- **https://amzn.to/3eRKUIU** — [169]
- **https://amzn.to/3XFq31U** — [092]
- **https://ancestryaimee.com** — [059], [074], [075]
- **https://app.regrid.com** — [181]
- **https://app.regrid.com/** — [178]
- **https://app.regrid.com/plans** — [183]
- **https://app.regrid.com/profile/api** — [165]
- **https://book.dpasummit.com/free-book-page?el=Book_In_Descrip_YT&htrafficsource=youtube&hcategory=Book_Funnel_Organic** — [118], [123], [135], [146], [147]
- **https://book.dpasummit.com/free-book?el=Link_in_Bio&htrafficsource=Instagram&hcategory=Book_Funnel_Organic&utm_source=ig&utm_medium=social&utm_content=bio_link** — [127]
- **https://calendar.app.google/fanRW59j4meifPyR6** — [156]
- **https://calendly.com/surplusfunds101/surplusfunds101freecoachingcall** — [095]
- **https://cash.app/$etmmediagroup** — [092]
- **https://claimit.ca.gov/** — [092]
- **https://communityprogress.org/community-progress-webinars/** — [141]
- **https://communityprogress.org/newsletter-signup/** — [141]
- **https://courses.magnumopusproject.com/checkout-page** — [124]
- **https://courses.magnumopusproject.com/earn** — [124]
- **https://courses.magnumopusproject.com/marketing-analysis** — [124]
- **https://courses.probatemastery.com/Close-2-Probate-Deals-Every-Month** — [155]
- **https://courses.probatemastery.com/offers/cQhonGt7/checkout** — [156]
- **https://creativecommons.org/licenses/by/4.0/** — [007], [067]
- **https://dealmachine.app.link/bizmatthew** — [185]
- **https://dev.neo4j.com/auradb** — [171]
- **https://dev.neo4j.com/graphrag** — [171]
- **https://dev.neo4j.com/KGBuilder** — [171]
- **https://dev.neo4j.com/learngraph** — [171]
- **https://estateprofessionalsmastermind.buzzsprout.com/share** — [155], [156]
- **https://excesselite.com** — [077], [084], [085], [086], [087], [088], [089], [090]
- **https://facebook.com/groups/estateprofessionalsmastermind** — [121], [124], [133], [134], [137], [152]
- **https://familyhistory.lib.byu.edu/0000018f-a74b-d08a-abaf-bfff074e0001/finding-your-ancestors-descendants-james-tanner-26-feb-2023-pdf** — [001]
- **https://familyhistory.lib.byu.edu/all-webinars/basic-series-part-3-beginning-descendancy-research** — [026]
- **https://familyhistory.lib.byu.edu/all-webinars/digging-deep-into-death-records** — [069]
- **https://familyhistory.lib.byu.edu/all-webinars/familysearch-catalog-digging-deeper** — [066]
- **https://familyhistory.lib.byu.edu/all-webinars/how-to-analyze-genealogical-sources** — [035]
- **https://familyhistory.lib.byu.edu/all-webinars/introduction-to-the-familysearch-app-gallery** — [024]
- **https://familyhistory.lib.byu.edu/all-webinars/the-anatomy-of-a-court-case-for-genealogists** — [025]
- **https://familyhistory.lib.byu.edu/virtual-classes/discovering-your-ancestors-using-probate-records** — [057]
- **https://familyhistory.lib.byu.edu/virtual-classes/finding-wills-in-england-and-wales-online-part-3-ecclesiastical-probate-courts-pre-1858** — [054]
- **https://familyhistory.lib.byu.edu/virtual-classes/finding-your-ancestors-descendants** — [001]
- **https://familyhistory.lib.byu.edu/virtual-classes/whats-in-a-probate-record-and-how-to-use-it-for-genealogical-research** — [065]
- **https://farmaid.org/DBAN** — [142]
- **https://forgottenloot.org** — [097]
- **https://freemusicarchive.org/music/Broke_For_Free/Something_EP/Broke_For_Free_-_Something_EP_-_05_Something_Elated** — [059], [074], [075]
- **https://genealogysafari.com/** — [051]
- **https://genealogytv.org/** — [007], [062], [067], [070], [076]
- **https://genealogytv.org/about-genealogy-tv-academy/** — [067]
- **https://genealogytv.org/academy/** — [007]
- **https://genealogytv.org/coaching-options/** — [062]
- **https://genealogytv.org/handouts/** — [007], [062], [067]
- **https://genealogytv.org/product/handout-for-find-more-wills-and-probate-records-for-using-both-ancestry-and-familysearch-together/** — [067]
- **https://genealogytv.org/product/handout-for-targeted-genealogical-research-probate-example/** — [007]
- **https://go.investorfuel.com/find-your-first-deal-5-day-challenge** — [127]
- **https://go.investorfuel.com/triple-your-profits** — [127]
- **https://graphstuff.fm/episodes/rag-databases-with-johannes-jolkkonen-when-to-choose-a-graph-database-vs-alternative-vector-or-relational-stores** — [163]
- **https://heirsearch.com/** — [004]
- **https://heirsearch.com/joinourcommunity/** — [004]
- **https://homebuyerlouisiana.com/about-us/stephen-keighery/** — [126], [129]
- **https://ident.familysearch.org/identity/login/?state=https://www.familysearch.org/search/full-text** — [067]
- **https://instagram.com/courtneyfricke** — [117], [119], [120], [122], [125], [126], [128], [129], [130], [131], [132], [148], [162]
- **https://instagram.com/courtneyfricke⁠** — [136], [154]
- **https://investorfuel.com/blog/buying-property-with-title-defects/** — [127]
- **https://investorfuel.com/coachingwithmike** — [127]
- **https://learn.surplusfundsprofitsystem.com/** — [084]
- **https://linktr.ee/hittinthebricks** — [051]
- **https://linktr.ee/jamelgibbs** — [160]
- **https://mailchi.mp/a0862c6473aa/genealogytvnewsletter** — [007], [062], [067]
- **https://my.investorfuel.com/if-lm-optin-acquisitions-guide** — [127]
- **https://my.investorfuel.com/mm-lm-coo-hiring-guide** — [127]
- **https://my.investorfuel.com/mm-lm-ea-hiring-guide** — [127]
- **https://my.investorfuel.com/mm-lm-fuel5** — [127]
- **https://my.investorfuel.com/rehab** — [127]
- **https://myinvestorinsurance.com/** — [127]
- **https://ncancestry.com/** — [070], [076]
- **https://neo4j.com/docs/graph-data-science/current/algorithms/node-similarity/** — [163]
- **https://neo4j.com/docs/graph-data-science/current/machine-learning/node-embeddings/fastrp/** — [163]
- **https://open.spotify.com/show/4bMc6mM0X5gUrczWw5lN7H?si=576425854aab4a2b** — [127]
- **https://patreon.com/aimeecross** — [075]
- **https://podcasts.apple.com/us/podcast/investor-fuel-real-estate-investing-show/id943707421** — [127]
- **https://prf.hn/click/camref:1101l4aFW/creativeref:1011l28282** — [070], [076]
- **https://prf.hn/click/camref:1101l4aFW/creativeref:1011l28781** — [062], [070]
- **https://prf.hn/click/camref:1101l4aFW/creativeref:1011l33765** — [070]
- **https://prf.hn/click/camref:1101l4aFW/creativeref:1100l28566** — [070]
- **https://probatedata.com/** — [166]
- **https://ProbateMastery.com** — [134], [151]
- **https://probatemastery.com** — [121], [124], [134], [137], [153], [155], [156]
- **https://probatemastery.com/7-things-to-do-at-probate-court-besides-pull-probate-lead-lists/** — [153]
- **https://probatemastery.com/a-professional-guide-to-probate-for-bighearted-real-estate-agents-and-investors/** — [137]
- **https://probatemastery.com/calling-probate-leads-find-missing-life-insurance-policies-probate-marketing-strategy** — [137]
- **https://probatemastery.com/discovery-call/** — [155]
- **https://probatemastery.com/earn-attorney-referrals-now-course-pricing/** — [155], [156]
- **https://probatemastery.com/ep67-probate-data-and-property-lookups** — [121]
- **https://probatemastery.com/estateexec-probate-software-for-executors/** — [124]
- **https://probatemastery.com/finding-contractors-who-deliver-real-estate-vendors/** — [152]
- **https://probatemastery.com/get-probate-leads-from-courthouse** — [124]
- **https://probatemastery.com/how-to-find-affordable-probate-leads-a-quick-guide-for-real-estate-professionals/** — [133], [152]
- **https://probatemastery.com/how-to-find-cash-buyers-for-real-estate-deals-build-buyers-list/** — [153]
- **https://probatemastery.com/how-to-jv-a-deal-in-probate-live-probate-real-estate-training-chad-corbett/** — [133], [137], [152], [153]
- **https://probatemastery.com/hyperlocal-real-estate-marketing-how-to-buy-probate-property-sub2** — [153]
- **https://probatemastery.com/probate-for-investors-guide/** — [124]
- **https://probatemastery.com/probate-mastery-group-training-10** — [134]
- **https://probatemastery.com/probate-real-estate-leads-companies-reviewed-online/** — [153]
- **https://probatemastery.com/probate-training-course-for-real-estate-agents-investors/** — [133], [137], [152]
- **https://probatemastery.com/probatesuccess/** — [134]
- **https://probatemastery.com/reviews** — [133], [137], [152]
- **https://probatemastery.com/sub-to-deals-in-probate-real-estate-plus-optimizing-your-probate-marketing-strategy/** — [152]
- **https://probateweekly.com** — [137]
- **https://regrid.com/feature-service** — [172], [173]
- **https://regrid.com/saas** — [181]
- **https://reiplusai.com/** — [186]
- **https://reparationsnowdoc.com/** — [092]
- **https://retipster.com/category/due-diligence/?utm_source=youtube&utm_medium=social&utm_campaign=blog&utm_content=9RvXCiHUzlo** — [175]
- **https://retipster.com/datatree** — [167]
- **https://retipster.com/datatree-hacks/?utm_source=youtube&utm_medium=social&utm_campaign=blog&utm_content=2ThZ61aal9k** — [189]
- **https://retipster.com/datatree-hacks/?utm_source=youtube&utm_medium=social&utm_campaign=blog&utm_content=9RvXCiHUzlo** — [175]
- **https://retipster.com/datatree-hacks/?utm_source=youtube&utm_medium=social&utm_campaign=blog&utm_content=aUiod-Jy68U** — [167]
- **https://retipster.com/datatree-hacks/?utm_source=youtube&utm_medium=social&utm_campaign=blog&utm_content=GfyX48eCbRY** — [168]
- **https://retipster.com/datatree-hacks/?utm_source=youtube&utm_medium=social&utm_campaign=blog&utm_content=y5XZp-4n_uc** — [176]
- **https://retipster.com/facebook** — [168], [187]
- **https://retipster.com/facebookgroup** — [168], [187]
- **https://retipster.com/follow/?utm_source=youtube&utm_medium=social&utm_campaign=blog&utm_content=2ThZ61aal9k** — [189]
- **https://retipster.com/follow/?utm_source=youtube&utm_medium=social&utm_campaign=blog&utm_content=y5XZp-4n_uc** — [176]
- **https://retipster.com/follow/?utm_source=youtube&utm_medium=social&utm_campaign=terms&utm_content=aUiod-Jy68U** — [167]
- **https://retipster.com/forum** — [168], [187]
- **https://retipster.com/go/datatree/yt-2ThZ61aal9k** — [189]
- **https://retipster.com/go/datatree/yt-9RvXCiHUzlo** — [175]
- **https://retipster.com/go/datatree/yt-aUiod-Jy68U** — [167]
- **https://retipster.com/go/datatree/yt-GfyX48eCbRY** — [168]
- **https://retipster.com/go/datatree/yt-ntT8V0gnpAs** — [187]
- **https://retipster.com/go/datatree/yt-y5XZp-4n_uc** — [176]
- **https://retipster.com/instagram** — [168], [187]
- **https://retipster.com/linkedin** — [168], [187]
- **https://retipster.com/perc-test/?utm_source=youtube&utm_medium=social&utm_campaign=blog&utm_content=ntT8V0gnpAs** — [187]
- **https://retipster.com/pinterest** — [168], [187]
- **https://retipster.com/propertyresearch/?utm_source=youtube&utm_medium=social&utm_campaign=blog&utm_content=ntT8V0gnpAs** — [187]
- **https://retipster.com/terms/legal-description/?utm_source=youtube&utm_medium=social&utm_campaign=terms&utm_content=aUiod-Jy68U** — [167]
- **https://retipster.com/tiktok** — [168], [187]
- **https://retipster.com/twitter** — [168], [187]
- **https://retipster.com/wetlands/?utm_source=youtube&utm_medium=social&utm_campaign=blog&utm_content=ntT8V0gnpAs** — [187]
- **https://retipster.com/youtube** — [168], [187]
- **https://static.libnet.info/frontend-images/pdfs/acpl/Genealogy/Handout_What_Happens_After_Death_Finding_and_Using_Probate_Records.pdf** — [064]
- **https://static.libnet.info/frontend-images/pdfs/acpl/Genealogy/Recognizing_Inaccurate_and_Misleading_Genealogical_Records__Citations__and_Sources_2024_Program_Version.pdf** — [036]
- **https://static.libnet.info/frontend-images/pdfs/acpl/Genealogy/Recognizing_Inaccurate_and_Misleading_Genealogical_Records_Citations_and_Sources_2024_HANDOUT.pdf** — [036]
- **https://surplusfundsriches.net** — [091]
- **https://tedthomas.com/ytl-31069/** — [161]
- **https://texasprobaterealestate.com/wp-content/uploads/2026/05/tpre-cpn.pdf** — [145]
- **https://texasprobaterealestate.com/wp-content/uploads/2026/05/tpre-iabs.pdf** — [145]
- **https://tiktok.com/@courtney.fricke** — [117], [119], [120], [122], [125], [126], [128], [129], [130], [131], [132], [148], [162]
- **https://tiktok.com/@courtney.fricke⁠** — [136], [154]
- **https://tinyurl.com/AimeesCrew** — [074]
- **https://todayswillsandprobate.co.uk/the-finders-international-story/** — [047]
- **https://trial.propstreampro.com/bizmatthew/** — [185]
- **https://tubitv.com/movies/100005110/reparations-now** — [092]
- **https://twitter.com/Ancestry** — [002], [006], [015], [027], [028], [037], [058], [072], [073]
- **https://twitter.com/heirsearch** — [004]
- **https://twitter.com/itsjamelgibbs** — [160]
- **https://unclaimedproperty.delaware.gov/app/claim/how-to-search** — [099]
- **https://unclaimedproperty.delaware.gov/app/freedom-information-act** — [099]
- **https://unclaimedproperty.delaware.gov/docs/DE%20OUP%20POA%20Form%20-%20Fillable%20PDF.pdf** — [099]
- **https://unclaimedproperty.delaware.gov/docs/Escheat%20Holder%20Reporting%20Handbook_Rewrite_022018.pdf** — [099]
- **https://unclaimedproperty.michigan.gov/** — [097]
- **https://web.datatree.com/home/geocoverage** — [167], [168]
- **https://welcome.retipster.com/?utm_source=youtube&utm_medium=social&utm_campaign=blog&utm_content=9RvXCiHUzlo** — [175]
- **https://www.amazon.com/shop/aimeecross-genealogyhints** — [074]
- **https://www.amazon.com/shop/genealogytv** — [007], [062], [067]
- **https://www.ancestry.com/** — [002], [006], [015], [027], [028], [037], [058], [072], [073]
- **https://www.ancestry.com/cs/alwaysremember** — [076]
- **https://www.ancestry.com/search/categories/36/** — [059]
- **https://www.anrdoezrs.net/click-9110145-11504323** — [062]
- **https://www.batchskiptracing.com?fpr=bizmatthew** — [185]
- **https://www.bizmatthew.com/wholesale-course** — [185]
- **https://www.bizmatthew.com/wholesalecontracts** — [185]
- **https://www.blackburnromey.com/** — [064]
- **https://www.boyesturner.com** — [049]
- **https://www.boyesturner.com/get-in-touch** — [049]
- **https://www.buzzsprout.com/2110726/fan_mail/new** — [051]
- **https://www.claimit.ca.gov** — [082]
- **https://www.dhss.delaware.gov/dhss/dph/ss/vitalstats.html** — [099]
- **https://www.dpaa.mil/** — [051]
- **https://www.elephind.com/** — [024]
- **https://www.etmmediagroupstore.com/** — [092]
- **https://www.eventbrite.com/e/get-probate-cash-tickets-411579925637** — [124]
- **https://www.facebook.com/aimeecross2** — [074], [075]
- **https://www.facebook.com/Ancestry/** — [002], [006], [015], [027], [028], [037], [058], [072], [073]
- **https://www.facebook.com/courtneyfricke19/** — [117], [119], [120], [122], [125], [126], [128], [129], [130], [131], [132], [148], [162]
- **https://www.facebook.com/courtneyfricke19/⁠** — [136], [154]
- **https://www.facebook.com/ellis.s.jose** — [125], [128]
- **https://www.facebook.com/Genealogytv/** — [007], [062], [067], [070]
- **https://www.facebook.com/groups/1430538711907026** — [148]
- **https://www.facebook.com/groups/770825015084618** — [109]
- **https://www.facebook.com/groups/assetrecovery** — [077], [084], [085], [086], [087], [088], [089], [090]
- **https://www.facebook.com/groups/curativetitle** — [120], [122], [126], [129], [130], [132], [162]
- **https://www.facebook.com/groups/ProbateMastery** — [124]
- **https://www.facebook.com/HeirSearchBetterWay/** — [004]
- **https://www.facebook.com/ProbateMastery/** — [155], [156]
- **https://www.facebook.com/realmikehambright** — [127]
- **https://www.facebook.com/stephen.keighery** — [126], [129]
- **https://www.facebook.com/thejamelgibbs/** — [160]
- **https://www.familysearch.org/wiki/en/Death_Records** — [076]
- **https://www.findersinternational.co.uk** — [053]
- **https://www.forensicgenealogists.org/** — [051]
- **https://www.fraserandfraser.co.uk/contact/** — [052]
- **https://www.instagram.com/ancestry** — [002], [006], [015], [027], [028], [037], [058], [072], [073]
- **https://www.instagram.com/ancestryaimee/** — [074], [075]
- **https://www.instagram.com/coachbrucehill/** — [155], [156]
- **https://www.instagram.com/deedclear/** — [125], [128]
- **https://www.instagram.com/erizzyy** — [084], [088], [089], [090]
- **https://www.instagram.com/erizzyy/** — [077], [085], [086], [087]
- **https://www.instagram.com/jamelgibbs/** — [160]
- **https://www.instagram.com/logan_fullmer** — [118], [123], [135], [146], [147]
- **https://www.instagram.com/logan_fullmer/?hl=en** — [127]
- **https://www.instagram.com/realmikehambright/** — [127]
- **https://www.instagram.com/stephenkeighery/** — [126], [129]
- **https://www.instagram.com/thedavidwilkerson** — [093], [095], [098], [099], [100], [101], [102], [103], [104], [105], [106], [107], [108]
- **https://www.legacytree.com/genealogytv** — [067]
- **https://www.legalgenealogist.com/2012/01/25/the-ties-that-bond/** — [070]
- **https://www.legalgenealogist.com/2013/08/01/a-matter-of-consideration/** — [059]
- **https://www.linkedin.com/company/heirsearch/** — [004]
- **https://www.linkedin.com/in/danielcurran-finders/** — [047]
- **https://www.linkedin.com/in/jamelgibbs** — [160]
- **https://www.linkedin.com/in/mikehambright** — [127]
- **https://www.linkedin.com/in/stephenkeighery/** — [126], [129]
- **https://www.loganfullmer.com/** — [118], [123], [135], [146], [147]
- **https://www.moneymakingjug.com/inquiry** — [077], [085], [086], [087], [088], [089], [090]
- **https://www.myheritage.com/** — [024]
- **https://www.myheritage.com/complete-genealogy-package?keyword=partners&utm_source=partner_genealogytv&utm_medium=partner&utm_campaign=genealogytv_march20&tr_funnel=Complete** — [067]
- **https://www.myheritage.com/dna?utm_source=partner_naturalintelligence&utm_medium=partner&utm_campaign=genealogytv_july19&tr_funnel=mhdna** — [076]
- **https://www.mylawyerinspain.com** — [053]
- **https://www.mymcpl.org/genealogy** — [061]
- **https://www.patreasury.gov/unclaimed-property/** — [111]
- **https://www.patreon.com/aimeecross** — [074], [075]
- **https://www.patreon.com/GenealogyTV** — [007], [062], [067], [070], [076]
- **https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2B8FCAGJRN36U&source=url** — [070], [076]
- **https://www.pbinfo.com/benesearch-beneficiary-research/** — [008]
- **https://www.perryeatonlaw.com/** — [145]
- **https://www.sco.ca.gov** — [082]
- **https://www.sco.ca.gov/Files-UPD/guide_investigator_handbook.pdf** — [098]
- **https://www.sco.ca.gov/upd_form_investigator.html** — [098]
- **https://www.skool.com/dirtytitlegoldmine/about?ref=5df750735b234076b6a76b2bf0382a82** — [125], [128]
- **https://www.surplusfunds101.com** — [098]
- **https://www.surplusfunds101.com/contractlibrary** — [101], [103], [104], [105]
- **https://www.surplusfunds101.com/freecallingscript** — [080], [093], [094], [095], [096], [098], [099], [100], [101], [102], [103], [104], [105], [106], [107], [108]
- **https://www.surplusfunds101.com/signaturecourse** — [101], [104]
- **https://www.tax.newmexico.gov/individuals/what-is-unclaimed-property/locators/** — [100]
- **https://www.tax.newmexico.gov/wp-content/uploads/sites/5/2020/10/rpd-41343.pdf** — [100]
- **https://www.texasprobaterealestate.com** — [145]
- **https://www.TheGenealogyProfessional.com/eileen-oduill** — [050]
- **https://www.thegenealogyprofessional.com/eileen-oduill/** — [050]
- **https://www.thoughtco.com/marriage-records-types-4077752** — [070]
- **https://www.tiktok.com/@jamelgibbs** — [160]
- **https://www.tiktok.com/@loganfullmer_?is_from_webapp=1&sender_device=pc** — [118], [123], [135], [146], [147]
- **https://www.tiktok.com/@stephenkeighery** — [126], [129]
- **https://www.twitter.com/Curran_Finders** — [047]
- **https://www.yourdnaguide.com/ref/6/** — [067]
- **https://www.youtube.com/@courtneyfricke** — [117], [119], [120], [122], [126], [129], [130], [131], [132], [136], [148], [154], [162]
- **https://www.youtube.com/@GenealogyTV/community** — [007], [067]
- **https://www.youtube.com/@GenealogyTV/join** — [007], [067]
- **https://www.youtube.com/@HTBKRB** — [051]
- **https://www.youtube.com/@investorfuel** — [127]
- **https://www.youtube.com/@loganfullmer** — [118], [123], [135], [146], [147]
- **https://www.youtube.com/@LouisianaRealEstateTalks** — [120], [122], [126], [129], [130]
- **https://www.youtube.com/@realestateinprobate** — [155], [156]
- **https://www.youtube.com/@UCBFQ_43MCI9tJ8tB6m9q92g** — [126], [129]
- **https://www.youtube.com/@UCfZlfkGpNzcMuDh6NX7xVpQ** — [125], [128]
- **https://www.youtube.com/c/billgrossexp/videos** — [137]
- **https://www.youtube.com/channel/UC_Xc7ATShOd-8odaTDhO7GA/join** — [075]
- **https://www.youtube.com/channel/UCcvpi8XvOScBogIxmarmADw/playlists** — [070], [076]
- **https://www.youtube.com/channel/UCcvpi8XvOScBogIxmarmADw/Subscribe** — [007], [062], [067]
- **https://www.youtube.com/channel/UCVQtE-vfBzIkRIRsIA4Vs7A/join** — [092]
- **https://www.youtube.com/channel/UCwOIg2lTv7ifY_AEitw7L-g** — [062], [070], [076]
- **https://www.youtube.com/genealogytv/?sub_confirmation=1** — [070], [076]
- **https://www.youtube.com/GenealogyTV/Community** — [062]
- **https://www.youtube.com/genealogytv/join** — [062]
- **https://www.youtube.com/jamelgibbs?sub_confirmation=1** — [160]
- **https://www.youtube.com/playlist?list=PL0YMOhafrSa5HeooRyMBeiGxKwsOw44JA** — [185]
- **https://www.youtube.com/playlist?list=PL0YMOhafrSa6b0mtMytUj2KdI05jiD7xi** — [185]
- **https://www.youtube.com/playlist?list=PL_t1CjX04xMsUc4TcAH_uyYDMPzzU6xRy** — [117], [119], [125], [131], [132], [148], [162]
- **https://www.youtube.com/playlist?list=PL_t1CjX04xMsUc4TcAH_uyYDMPzzU6xRy⁠** — [136], [154]
- **https://www.youtube.com/playlist?list=PL_t1CjX04xMtBIyWGIO5Mvi2FDn2f436N** — [117], [119], [125], [131], [132], [148], [162]
- **https://www.youtube.com/playlist?list=PL_t1CjX04xMtBIyWGIO5Mvi2FDn2f436N⁠** — [136], [154]
- **https://www.youtube.com/playlist?list=PL_t1CjX04xMtnNcKPG5LvTh-1m2QVIrY4** — [117], [119], [125], [131], [148]
- **https://www.youtube.com/playlist?list=PL_t1CjX04xMtnNcKPG5LvTh-1m2QVIrY4⁠** — [136], [154]
- **https://www.youtube.com/playlist?list=PL_t1CjX04xMvxWaWZ6RTzx_Bmfe2Cx2xH** — [117], [125], [131]
- **https://www.youtube.com/playlist?list=PLiMXWjHlj5RQn9sWPHtwMdaQQ84RRykAw** — [070], [076]
- **https://www.youtube.com/playlist?list=PLiMXWjHlj5RR12Cc859K76dLKP14t8sAo** — [070], [076]
- **https://www.youtube.com/surplusfunds101** — [080], [093], [095], [096], [098], [099], [100], [101], [102], [103], [104], [105], [106], [107], [108]
- **https://www.youtube.com/user/AncestryCom** — [002], [006], [015], [027], [028], [037], [058], [072], [073]
- **https://www.youtube.com/user/BillGrossC21** — [152]
- **https://www.zeffy.com/en-US/donation-form/93401f2b-8f39-4fd6-ad49-70396eae0ec5** — [051]
- **https://x.com/courtneyfricke** — [117], [119], [120], [122], [125], [126], [128], [129], [130], [131], [132], [148], [162]
- **https://x.com/courtneyfricke⁠** — [136], [154]
- **https://x.com/stephenkeighery** — [126], [129]
- **https://youtu.be/-D6c1fVU3LQ&list=UULFcvpi8XvOScBogIxmarmADw** — [067]
- **https://youtu.be/0BtnonBZ0RI** — [062]
- **https://youtu.be/1lrFNBWKwzo&list=UULFcvpi8XvOScBogIxmarmADw** — [067]
- **https://youtu.be/3cmj5kGm2Xw** — [016], [017], [018], [019], [020], [021], [022], [029], [031], [032], [056], [060]
- **https://youtu.be/BGeeqQb-TQk** — [062]
- **https://youtu.be/D1GHEPQEZUo** — [062]
- **https://youtu.be/DUAbGD8rVzA** — [017], [018]
- **https://youtu.be/Dutmzc9gb30** — [122], [136]
- **https://youtu.be/eRHmplbcT6A** — [062]
- **https://youtu.be/FxQgurvv3_g** — [016], [017]
- **https://youtu.be/jydLZrDuzCM&list=UULFcvpi8XvOScBogIxmarmADw** — [007]
- **https://youtu.be/KtpN2Ws9PA4** — [016], [018]
- **https://youtu.be/O9Qpz6dI9zg** — [163]
- **https://youtu.be/pfFIY36eo88&list=UULFcvpi8XvOScBogIxmarmADw** — [067]
- **https://youtu.be/VWma15_Lc3M** — [059]
- **https://youtu.be/X8NNeexlV8E** — [059]
- **https://youtu.be/yN_ss-zaRvk&list=UULFcvpi8XvOScBogIxmarmADw** — [067]
- **https://youtu.be/zIOhXZZxDDM&list=UULFcvpi8XvOScBogIxmarmADw** — [007]
- **https://youtube.com/playlist?list=PLnm7vznxHH_cDXKlVbtZtZ3et2etxoLne** — [061]
- **https://youtube.com/playlist?list=PLq34PBZ-WZXE0UwJry7DuiNqwxnCnYjvV** — [093], [095], [096], [098], [099], [100], [101], [102], [103], [104], [105], [106], [107], [108]
- **https://youtube.com/playlist?list=PLq34PBZ-WZXE0UwJry7DuiNqwxnCnYjvVn** — [080]
- **KML** — [179]
- **LinkedIn** — [004], [005], [047], [051], [121], [122], [126], [127], [129], [136], [146], [154], [160], [168], [174], [187]
- **MyHeritage** — [007], [016], [024], [059], [065], [067], [074], [075], [076], [144]
- **Neo4j** — [163], [171]
- **Newspapers.com** — [007], [015], [024], [028], [062], [067], [123], [140]
- **Ohio Revised Code 169** — [110]
- **PACER** — [147]
- **Pennsylvania Treasury** — [111]
- **ProbateData** — [166], [184]
- **PropStream** — [118], [151], [185]
- **Regrid** — [165], [172], [173], [177], [178], [179], [180], [181], [182], [183]
- **RESPA** — [158], [159]
- **Shapefile** — [172], [179]
- **Small Estate** — [077], [156]
- **SS-5** — [062]
- **SSDI** — [062], [069]
- **Table of Heirship** — [083]
- **TaxSource** — [189]
- **Textract** — [169]
- **TILA** — [158], [159]
- **TLO** — [118]
- **Transkribus** — [164], [174]
- **Uniform Partition** — [138], [139], [142], [144], [158]
- **UPHPA** — [144]

## Complete source register

- [001] Finding Your Ancestors' Descendants - James Tanner (26 Feb 2023) — https://www.youtube.com/watch?v=9Q4qYeK5DTg — 7,012 words — Domain 1.
- [002] What Do I Enter Into My Family Tree? Resolving Conflicting Evidence \| Ancestry — https://www.youtube.com/watch?v=ElrY5ALsx1Y — 5,885 words — Domain 1.
- [003] When Paper Trails Meet DNA: The Full Conversation with Professor Turi King and Neil Fraser — https://www.youtube.com/watch?v=LZWYe4jFvZM — 10,696 words — Domain 1.
- [004] HeirSearch \| Consanguinity Chart Walk-Through — https://www.youtube.com/watch?v=aOXjjN53MT8 — 469 words — Domain 1.
- [005] TGP - 13 Leslie Lawson - Forensic Genealogist — https://www.youtube.com/watch?v=R5XtgGL0gkQ — 9,138 words — Domain 1.
- [006] Finding Probate Records That Aren't Indexed \| Ancestry — https://www.youtube.com/watch?v=lOmly79G2Tk — 756 words — Domain 2.
- [007] Targeted Genealogical Research: Probate Example — https://www.youtube.com/watch?v=10DuXkEoTRA — 1,733 words — Domain 2.
- [008] New Techniques to Find Missing Beneficiaries - PBI Research Services BeneSearch Webinar — https://www.youtube.com/watch?v=rR4YCKGVNmg — 4,854 words — Domain 8.
- [009] A Guide To Our Fee Options • Fraser and Fraser — https://www.youtube.com/watch?v=EPZo6YVIMi4 — 922 words — Domain 8.
- [010] Probate Part 6 "Finding Probate Documents" by James Tanner — https://www.youtube.com/watch?v=oZiYbKNvxJY — 2,115 words — Domain 2.
- [011] Probate Part 2, Wills by James Tanner — https://www.youtube.com/watch?v=CyAfgfoF-eo — 1,980 words — Domain 2.
- [012] Probate Part 3, "Wording of Wills" by James Tanner — https://www.youtube.com/watch?v=7120UjJPqZM — 1,086 words — Domain 2.
- [013] Probate Part 5, " What are Probate Procedures" by James Tanner — https://www.youtube.com/watch?v=Xe2NEfqDwTQ — 1,809 words — Domain 2.
- [014] Probate Part 7, "Example of a Probate File" by James Tanner — https://www.youtube.com/watch?v=07zaZ3sQwi8 — 2,237 words — Domain 2.
- [015] Crafting Source Citations in Your Ancestry Tree \| Ancestry — https://www.youtube.com/watch?v=7M3XZfN7814 — 4,695 words — Domain 1.
- [016] Peeling Back the Layers: Citing Sources from Online Materials, Part 1 — https://www.youtube.com/watch?v=DUAbGD8rVzA — 2,577 words — Domain 1.
- [017] Peeling Back the Layers: Citing Sources From Online Materials, Part 2 — https://www.youtube.com/watch?v=KtpN2Ws9PA4 — 3,172 words — Domain 1.
- [018] Peeling Back the Layers: Citing Sources From Online Materials, Part 3 — https://www.youtube.com/watch?v=FxQgurvv3_g — 3,360 words — Domain 8.
- [019] Research Logs: A Variety of Styles to Suit Your Project, Part 1 — https://www.youtube.com/watch?v=PfqiDmLnMIg — 2,717 words — Domain 8.
- [020] Research Logs: A Variety of Styles to Suit Your Project, Part 2 — https://www.youtube.com/watch?v=J1h18kFbXKU — 2,578 words — Domain 8.
- [021] Research Logs: A Variety of Styles to Suit Your Project, Part 3 — https://www.youtube.com/watch?v=KpQQ3n37XXM — 2,931 words — Domain 8.
- [022] Courthouse Records: One-Stop Shopping for Family Secrets — https://www.youtube.com/watch?v=PuaqkDhOYh8 — 3,191 words — Domain 3.
- [023] GenealogyMagazine, Episode 1: Courthouse Research — https://www.youtube.com/watch?v=DjxOkXDU2cY — 614 words — Domain 8.
- [024] Online Digital Newspaper Sources - James Tanner — https://www.youtube.com/watch?v=1Ptl1u6wRoY — 6,484 words — Domain 3.
- [025] The Anatomy of a Court Case for Genealogists - James Tanner — https://www.youtube.com/watch?v=BAgypTLrbR4 — 10,310 words — Domain 2.
- [026] Basic Series: Part 3 - Beginning Descendancy Research - James Tanner — https://www.youtube.com/watch?v=TVIHQUFpkjk — 7,822 words — Domain 1.
- [027] Descendancy Research \| Ancestry — https://www.youtube.com/watch?v=_q7yAh8Anok — 5,562 words — Domain 1.
- [028] Post-1940 Descendancy Research \| Ancestry — https://www.youtube.com/watch?v=rKKDh07PmVc — 5,584 words — Domain 1.
- [029] Tracing Descendants: An Essential Strategy to Solve Your Brickwall — https://www.youtube.com/watch?v=FA43rRoIJV8 — 3,396 words — Domain 1.
- [030] Analyzing Evidence: A Research Game Changer — https://www.youtube.com/watch?v=tljNDoj74TI — 7,573 words — Domain 1.
- [031] Dueling Dates and Fact Fights: Resolving Evidence Conflicts, Part 1 — https://www.youtube.com/watch?v=VbgMCP7bKcs — 2,126 words — Domain 1.
- [032] Dueling Dates and Fact Fights: Resolving Evidence Conflicts, Part 2 — https://www.youtube.com/watch?v=Ep2zENQQZ1k — 2,947 words — Domain 1.
- [033] Extracting Evidence: Strategies for Analyzing Genealogical Sources — https://www.youtube.com/watch?v=JIUMf1OHaY0 — 10,052 words — Domain 1.
- [034] From Questionable to Credible: Analyzing and Verifying Genealogical Sources — https://www.youtube.com/watch?v=R50W1KDrRPw — 2,518 words — Domain 1.
- [035] How to Analyze Genealogical Sources - James Tanner — https://www.youtube.com/watch?v=7Jn_XMUozo0 — 8,961 words — Domain 1.
- [036] Recognizing Inaccurate and Misleading Genealogical Records, Citations, and Sources — https://www.youtube.com/watch?v=FPaiNw1Z1b0 — 6,051 words — Domain 1.
- [037] Same Name - Different Man \| Ancestry — https://www.youtube.com/watch?v=K6-4Y6O5bbQ — 4,909 words — Domain 1.
- [038] Using Indirect and Negative Evidence to Prove Unrecorded Events — https://www.youtube.com/watch?v=VwfAeN31cTw — 4,884 words — Domain 1.
- [039] Finding probate records by browsing through images on FamilySearch.org — https://www.youtube.com/watch?v=hsFQHg-SMN4 — 646 words — Domain 2.
- [040] Finding repositories for probate records — https://www.youtube.com/watch?v=A437gHrrk2s — 971 words — Domain 2.
- [041] Primary sources: Intestate probate documents — https://www.youtube.com/watch?v=pGyFJ46jwTE — 925 words — Domain 2.
- [042] Primary Sources: testate probate documents — https://www.youtube.com/watch?v=NYz_-ZkJbBE — 890 words — Domain 2.
- [043] Primary Sources: Understanding guardianship in probate proceedings — https://www.youtube.com/watch?v=7_oRhXnhlag — 712 words — Domain 2.
- [044] Probate case study: Illegitimacy and conflicting surnames — https://www.youtube.com/watch?v=YNOLd8LZB48 — 898 words — Domain 2.
- [045] Locating Heirs — https://www.youtube.com/watch?v=X-Q-bm1y9no — 628 words — Domain 5.
- [046] What If An Heir or Beneficary is Missing? How to Find a Missing Heir? — https://www.youtube.com/watch?v=U6LsR1gr0oA — 870 words — Domain 2.
- [047] Daniel Curran Finders International - Todays Wills & Probate Podcast — https://www.youtube.com/watch?v=AKvEFJHf5K0 — 4,930 words — Domain 2.
- [048] NALP webinar, May 2024 - what is it like working in the Probate Research Industry — https://www.youtube.com/watch?v=zz_ksXmJqyI — 6,198 words — Domain 8.
- [049] Probate Detectives — https://www.youtube.com/watch?v=SLqhAWEXEv4 — 3,953 words — Domain 2.
- [050] TGP 19 - Eileen O'Duill - Probate Research — https://www.youtube.com/watch?v=7v_UB7hKgKg — 7,085 words — Domain 8.
- [051] Unraveling Forensic Genealogy With Juli Whittaker — https://www.youtube.com/watch?v=u2HltZJ1FrM — 5,233 words — Domain 1.
- [052] How to Spot a Fake Probate Letter \| 3 Steps to Avoid Scams — https://www.youtube.com/watch?v=le9BUKYDl1A — 276 words — Domain 2.
- [053] Unclaimed Estates & Abandoned Properties in Spain - tracing Heirs Worldwide — https://www.youtube.com/watch?v=ywaYY4cPtAY — 6,995 words — Domain 5.
- [054] Finding Wills in England and Wales Online, Part 3: Ecclesiastical Probate Courts, pre-1858 (3-24) — https://www.youtube.com/watch?v=Gwcf300h1sA — 4,778 words — Domain 2.
- [055] Part One • 10 Steps To Building Your Own Family Tree • Fraser and Fraser — https://www.youtube.com/watch?v=MdFDiQQXD3M — 446 words — Domain 8.
- [056] Analyzing Probate Records: Finding Our Ancestor's Stories — https://www.youtube.com/watch?v=Gv4Mibtn8CM — 2,497 words — Domain 2.
- [057] Discovering Your Ancestors Using Probate Records- James Tanner — https://www.youtube.com/watch?v=Yt91gmZt8sE — 8,377 words — Domain 2.
- [058] Getting Started With Probate Records \| Ancestry — https://www.youtube.com/watch?v=bcOlApV2Fng — 4,777 words — Domain 2.
- [059] How to Find Wills and Probate Records for Free and What They Can Tell Us — https://www.youtube.com/watch?v=0c5trJYJTyQ — 4,019 words — Domain 2.
- [060] Records Analysis: Level up Your Probate Skills — https://www.youtube.com/watch?v=fCvgh_QabMY — 3,217 words — Domain 2.
- [061] U.S. Probate Records for Genealogy \| Midwest Genealogy Center — https://www.youtube.com/watch?v=uAcku9kesK4 — 5,014 words — Domain 1.
- [062] Understanding Wills, Probate, Estate Records, and Women's Rights for Genealogy — https://www.youtube.com/watch?v=jydLZrDuzCM — 3,345 words — Domain 2.
- [063] Using Land and Probate Records in Family History Research Laurie Bradshaw — https://www.youtube.com/watch?v=Xzst9ZSC1M0 — 7,884 words — Domain 2.
- [064] What Happens After Death: Finding and Using Probate Records — https://www.youtube.com/watch?v=t_t1v7TPbFA — 9,309 words — Domain 2.
- [065] What’s in a Probate Record and How to Use it for Genealogical Research– James Tanner (10 Sep 2023) — https://www.youtube.com/watch?v=TBB8OPPFSsM — 7,599 words — Domain 2.
- [066] FamilySearch Catalog: Digging Deeper – Christine Moss Pack (26 September 2024) — https://www.youtube.com/watch?v=MMe67JLgS08 — 5,162 words — Domain 1.
- [067] Find More Wills and Probate Records for Using Both Ancestry and FamilySearch Together — https://www.youtube.com/watch?v=zIOhXZZxDDM — 2,797 words — Domain 2.
- [068] How to Link Unindexed Images to FS by Ann Tanner 10 minutes — https://www.youtube.com/watch?v=zTQCnGBnAvc — 1,149 words — Domain 8.
- [069] Digging Deep into Death Records - James Tanner — https://www.youtube.com/watch?v=70ya-VPbkBc — 9,355 words — Domain 3.
- [070] Marriage Records for Family History: Where to find them on Ancestry.com & FamilySearch.org — https://www.youtube.com/watch?v=JYf7R5lhBlU — 1,739 words — Domain 1.
- [071] No Death Certificate? — https://www.youtube.com/watch?v=5sxGnXLZO6A — 2,751 words — Domain 3.
- [072] Social Security Death Index: Uncovering Hidden Clues \| Ancestry — https://www.youtube.com/watch?v=Af6QVCj8Rcg — 536 words — Domain 3.
- [073] Sourcing Your Vitals - Citations for Birth, Marriage and Death Records \| Ancestry — https://www.youtube.com/watch?v=ih5iilWPvjI — 4,188 words — Domain 3.
- [074] What death records are you missing? — https://www.youtube.com/watch?v=6TDebNoMsvQ — 2,028 words — Domain 3.
- [075] Where Can You Get a Death Certificate (& what information is in it) — https://www.youtube.com/watch?v=RM0PcAQiipM — 1,782 words — Domain 3.
- [076] Why Research Death Records First + Ancestry Updates — https://www.youtube.com/watch?v=F5XFoUx37Ko — 6,641 words — Domain 1.
- [077] How To Work Deceased Claims - Step-By-Step (Surplus Funds Recovery) — https://www.youtube.com/watch?v=l8J2d1WwudY — 4,774 words — Domain 4.
- [078] ✅ 💰 CALIFORNIA Unclaimed Property Investigations - Tips from a Licensed Private Investigator! — https://www.youtube.com/watch?v=nI1xm6ZA2qo — 1,464 words — Domain 4.
- [079] How To Find family members of a deceased person! — https://www.youtube.com/watch?v=eiQ53kxE6ZA — 1,351 words — Domain 6.
- [080] Unclaimed Funds: Lead Sourcing Masterclass — https://www.youtube.com/watch?v=h4Qz3EvAAnw — 1,443 words — Domain 4.
- [081] Declaration Under Probate Code 13101 Tutorial — https://www.youtube.com/watch?v=1ahhduhMdd0 — 545 words — Domain 2.
- [082] How to Claim Your Property for the California State Controller's Office — https://www.youtube.com/watch?v=bsbWDqAXsrE — 209 words — Domain 4.
- [083] Table of Heirship Tutorial — https://www.youtube.com/watch?v=cMCrrRkehJk — 627 words — Domain 4.
- [084] $200,000 California Foreclosure Heir Claim Case Study — https://www.youtube.com/watch?v=MiiGrCZZAZk — 1,143 words — Domain 4.
- [085] 2 Ways To Check If There's a Lien On a Property (For Surplus Funds Recovery) — https://www.youtube.com/watch?v=q95klfFm9mE — 1,032 words — Domain 6.
- [086] Amador county Tax Sale Surplus Funds Case Study — https://www.youtube.com/watch?v=4-lZwuXtY6Y — 953 words — Domain 4.
- [087] How To Become a Surplus Funds Expert FOR 1 COUNTY (Asset Recovery Business) — https://www.youtube.com/watch?v=FNbqvZGEzeE — 1,139 words — Domain 4.
- [088] How to start a Surplus Funds Recovery Business in 2026 (for beginners) — https://www.youtube.com/watch?v=suJSu-vn6yI — 2,155 words — Domain 4.
- [089] Surplus Funds Recovery Cold Calling - STEP-BY-STEP SCRIPT — https://www.youtube.com/watch?v=DMdtmrWAO6c — 3,237 words — Domain 4.
- [090] Surplus Funds Recovery: COMPLETE Document List (2026 UPDATE) — https://www.youtube.com/watch?v=MVCNlj7HQBQ — 2,523 words — Domain 4.
- [091] Surplus Funds: Owner Died - STILL CLAIM! — https://www.youtube.com/watch?v=1N1Z99kUvRw — 1,293 words — Domain 4.
- [092] CA Unclaimed Property - Are you missing out? - Tutorial — https://www.youtube.com/watch?v=ijLtjR0tTd8 — 3,040 words — Domain 4.
- [093] California Unclaimed Funds: What You Need To Know To Be A Property Investigator #unclaimedassets — https://www.youtube.com/watch?v=xAiBXreoVY0 — 146 words — Domain 4.
- [094] How To Become An Unclaimed Property Investigator — https://www.youtube.com/watch?v=TTMtgtc31k4 — 1,075 words — Domain 4.
- [095] How to Build a Nationwide Notary Team (Step-by-Step) — https://www.youtube.com/watch?v=Qn63DtrxFts — 853 words — Domain 5.
- [096] Mastering Unclaimed Funds Contracts: A Complete Beginners Guide — https://www.youtube.com/watch?v=_RTcaTMOwlY — 3,317 words — Domain 4.
- [097] Michigan Unclaimed Property - This is How You Make an Unclaimed Property Claim — https://www.youtube.com/watch?v=Fn04U_Yfuzg — 793 words — Domain 4.
- [098] State Funds California: Registration Process & Requirements To Work Unclaimed Funds. — https://www.youtube.com/watch?v=_8vyoTSh7Rs — 2,061 words — Domain 4.
- [099] State Funds Tutorial Delaware: Registering As A Property Locator For The State Of Delaware. — https://www.youtube.com/watch?v=TTfaOSBvLDc — 2,366 words — Domain 4.
- [100] State Funds Tutorial New Mexico: How To Register As A Property Locator In The State Of New Mexico. — https://www.youtube.com/watch?v=6yIKsJMj6Gk — 1,517 words — Domain 4.
- [101] State Funds Tutorial Top 4 Tech Tools Needed For Your State Funds Business — https://www.youtube.com/watch?v=ApkuK7OOL9w — 1,459 words — Domain 8.
- [102] State Funds Tutorial Virtual Assistants: Top 3 Hiring Mistakes While Growing Your Surplus Business — https://www.youtube.com/watch?v=ASO1JUOWTjA — 2,238 words — Domain 4.
- [103] State Funds Tutorial: 5 Tech Tools For Your State Funds Business — https://www.youtube.com/watch?v=ES6y4iF-bBM — 1,483 words — Domain 8.
- [104] State Funds Tutorial: Cold Calling Objections vs. Complaints. Surplus Funds 101 — https://www.youtube.com/watch?v=t4w_wFimZ9A — 1,821 words — Domain 4.
- [105] State Funds Tutorial: How To Make Cold Calls If You Have A Full Time Job. — https://www.youtube.com/watch?v=JmuqGo9wYkg — 693 words — Domain 4.
- [106] State Funds Tutorial: What To Do When A Deal Cancels While Working Your State Funds Business. — https://www.youtube.com/watch?v=foMCyYJ4LgY — 1,778 words — Domain 4.
- [107] Surplus Funds 101 Tutorial: Top 4 FREE Software Platforms For Your State Funds Business — https://www.youtube.com/watch?v=Gk0D4wVEXmc — 2,040 words — Domain 8.
- [108] Unclaimed Funds Tutorial: Cold Calling Basics For Your Unclaimed Funds Business. state funds. — https://www.youtube.com/watch?v=XHOqG0CY1KA — 3,021 words — Domain 4.
- [109] Unclaimed Funds: How to Get Your Client's Documents in Order⚡️Unclaimed fund Client Document finding — https://www.youtube.com/watch?v=1AMk1-SB5ic — 1,362 words — Domain 4.
- [110] Claiming your Unclaimed Funds — https://www.youtube.com/watch?v=GrE0UUh_3BI — 7,106 words — Domain 4.
- [111] How To File a Claim - PA Treasury Unclaimed Property Tutorial — https://www.youtube.com/watch?v=eRjGqaIOHWI — 1,157 words — Domain 4.
- [112] How to Search for a Property ID — https://www.youtube.com/watch?v=ZX-Ttx_4Ezo — 153 words — Domain 6.
- [113] Ohio Unclaimed Funds: How to Claim Your Cash in 3 Steps (HB 96 Deadline Explained) Webinar 2-5-2026 — https://www.youtube.com/watch?v=8nmo4S1v3Co — 3,983 words — Domain 4.
- [114] Watch our Demo on How to Claim Your Ohio Unclaimed Funds — https://www.youtube.com/watch?v=o1cc3hUtIv4 — 1,660 words — Domain 4.
- [115] What Documentation is Needed for Unclaimed Funds — https://www.youtube.com/watch?v=dFKMkAIKskU — 1,539 words — Domain 4.
- [116] Quick tip: How to do an Online Title Search — https://www.youtube.com/watch?v=EDl18zX1-F0 — 519 words — Domain 6.
- [117] How I Actually Find Curative Title Leads — https://www.youtube.com/watch?v=W5g3Gia5jX4 — 4,564 words — Domain 5.
- [118] Skip Tracing for Curative Title: Find Owners Others Can't — https://www.youtube.com/watch?v=dJ-LTFmMsTg — 11,806 words — Domain 6.
- [119] How to Get Your First Curative Title Deal: A Step-by-Step Guide — https://www.youtube.com/watch?v=W-FX20iI9Jk — 7,666 words — Domain 5.
- [120] How to Underwrite a Curative Title Deal (And Know When to Walk Away) — https://www.youtube.com/watch?v=-QzABvCmtVc — 2,016 words — Domain 5.
- [121] Probate Data and Property Lookups: Live Real Estate Coaching with Probate Mastery — https://www.youtube.com/watch?v=TA4mtGUeNo8 — 9,164 words — Domain 2.
- [122] How to Find Heirs for a Florida Probate Property — https://www.youtube.com/watch?v=RmtbOq_vtuU — 1,448 words — Domain 5.
- [123] Curative Title Research: How She Finds Missing Owners — https://www.youtube.com/watch?v=zMW-iFWYX9w — 14,281 words — Domain 6.
- [124] I got free probate leads from the courthouse! Plus SOI and referral marketing \| Podcast Episode 85 — https://www.youtube.com/watch?v=1BlzkVdGPAo — 8,167 words — Domain 2.
- [125] Curative Title + Creative Finance: The Combo Most Investors Miss — https://www.youtube.com/watch?v=DcB4tJku4-A — 8,824 words — Domain 5.
- [126] How Wholesalers Can Turn Title Problems Into Profitable Curative Deals — https://www.youtube.com/watch?v=U_Eh790rq3o — 5,956 words — Domain 5.
- [127] How to Buy Distressed Properties With Title Problems for Pennies on the Dollar \| Logan Fullmer — https://www.youtube.com/watch?v=W0wjEVX_Jxw — 4,871 words — Domain 6.
- [128] Curative Title Explained: How Investors Make Money When Deals Can’t Close — https://www.youtube.com/watch?v=GH5TN_iIdMs — 7,542 words — Domain 5.
- [129] Curative Title for Wholesalers: How He Turned a Dead Lead Into a Deal — https://www.youtube.com/watch?v=2agNOU2taXA — 6,794 words — Domain 5.
- [130] How a Curative Title Investor Finds & Solves Deals Others Can't — https://www.youtube.com/watch?v=5LDDkiUTmXI — 6,443 words — Domain 5.
- [131] 5 Curative Title Terms Every Investor Should Understand — https://www.youtube.com/watch?v=sf2hUucsNZ8 — 3,581 words — Domain 5.
- [132] How to Find Curative Title Deals Nobody Else Is Chasing — https://www.youtube.com/watch?v=FgFrlIpbscs — 3,365 words — Domain 6.
- [133] How to JV a probate deal with the estate as your partner \| Probate Investing \| Chad Corbett Probate — https://www.youtube.com/watch?v=coUYfNbBvq0 — 5,171 words — Domain 2.
- [134] Differentiating Yourself From The Competition: How To HASHTAG Your ELEVATOR PITCH \| #10 — https://www.youtube.com/watch?v=OrEz4Qk-EZ0 — 14,924 words — Domain 5.
- [135] Curative Title Explained by a Florida Probate Attorney — https://www.youtube.com/watch?v=onebNbNQSBM — 16,877 words — Domain 5.
- [136] The Probate Mistake New Real Estate Investors Make (Florida Attorney Case Study) — https://www.youtube.com/watch?v=pQwwvYbUYrU — 1,294 words — Domain 2.
- [137] Calling probates, probate marketing, and selling probate property: Live probate class w/ Bill Gross — https://www.youtube.com/watch?v=PDnxvvPI7jU — 9,692 words — Domain 2.
- [138] USDA FSA Resources for Heirs: Join FSA as we talk with the Experts (Episode 1-Full Version) — https://www.youtube.com/watch?v=whDzDrFNADQ — 3,997 words — Domain 5.
- [139] Law Talks: Heirs' Property 1-21-2025 — https://www.youtube.com/watch?v=59C1meISvlc — 13,290 words — Domain 5.
- [140] Heirs' Property with Jonathan Reynolds of Louisiana Appleseed — https://www.youtube.com/watch?v=JPgk0Y7ZzuY — 9,669 words — Domain 5.
- [141] Heirs' Property 101 — https://www.youtube.com/watch?v=DG4Uhckk-fU — 9,504 words — Domain 5.
- [142] Heirs' Property Training (Webinar from DBAN) — https://www.youtube.com/watch?v=OODJe43FyEs — 12,506 words — Domain 5.
- [143] Preserving Homeownership: A Guide to Heirs Property for Housing Counselors — https://www.youtube.com/watch?v=VFSnbIIfy-M — 8,090 words — Domain 5.
- [144] Resolving Heirs' Property — https://www.youtube.com/watch?v=TP6n8TBsCGs — 10,123 words — Domain 5.
- [145] Affidavits of Heirship and Other Texas Probate Pitfalls \| TPRE Podcast Ep 3 — https://www.youtube.com/watch?v=n8jP0gweIR4 — 8,918 words — Domain 2.
- [146] Title Search Explained: The Hidden Liens Investors Miss — https://www.youtube.com/watch?v=lKsfBAioCYU — 8,950 words — Domain 6.
- [147] How Ex-FBI Agents Skip Trace Anyone for Real Estate Deals — https://www.youtube.com/watch?v=GK-4kFznJlA — 18,978 words — Domain 6.
- [148] How Matt Solved a 10 Heir Title Nightmare (A Curative Title Case Study) — https://www.youtube.com/watch?v=nYQaov_liDw — 2,638 words — Domain 6.
- [149] DelcoPA ROW \| Searching for Probated Estates Online — https://www.youtube.com/watch?v=hpvnOFjxwaM — 1,482 words — Domain 2.
- [150] DelcoPA ROW \| Searching for the Existence of Marriage Records Online — https://www.youtube.com/watch?v=yFnDG9Lf6kc — 1,492 words — Domain 3.
- [151] Pre Probate Leads vs Probate Leads: How do you market to them and why cold calling isn't the best — https://www.youtube.com/watch?v=4Z6pgZnoWi4 — 2,143 words — Domain 2.
- [152] Sub-to strategy for probate investing \| Probate foreclosures \| Probate real estate marketing tips — https://www.youtube.com/watch?v=AAF69oF79DU — 11,146 words — Domain 2.
- [153] Hyperlocal real estate marketing at probate court & How to buy a probate property as a sub2 deal — https://www.youtube.com/watch?v=Odf2VQ3AZsg — 8,670 words — Domain 2.
- [154] Florida Probate Explained: What Happens When Someone Dies Owning Real Estate? — https://www.youtube.com/watch?v=Dutmzc9gb30 — 13,618 words — Domain 5.
- [155] 🚨 Probate Property Headed to Foreclosure Auction… Is It Worth Pursuing? — https://www.youtube.com/watch?v=T2gvkByDlFU — 698 words — Domain 4.
- [156] Probate Process for Real Estate Agents & Investors: 12 Steps From Filing to Sale — https://www.youtube.com/watch?v=7xCfSyqYEys — 18,743 words — Domain 2.
- [157] All The Leads Probate Mastermind #447 — https://www.youtube.com/watch?v=xumwh2SPKv4 — 10,661 words — Domain 2.
- [158] Successor in Interest and Tangled Title — https://www.youtube.com/watch?v=ME2xl7cczH8 — 18,801 words — Domain 5.
- [159] TRAINING Using Successor in Interest to Save the Family Home — https://www.youtube.com/watch?v=JsPL1vXcgCI — 14,347 words — Domain 3.
- [160] How To Do A Property Title Search — https://www.youtube.com/watch?v=TWPIHeWyybg — 4,502 words — Domain 6.
- [161] How To Do A Title Search On A Property Yourself Before You Bid At Tax Sale Auctions — https://www.youtube.com/watch?v=xtdWFaJY8Xc — 2,233 words — Domain 6.
- [162] Before You Go From Wholesaling to Curative Title, Watch This — https://www.youtube.com/watch?v=z6h2w5h7oTQ — 4,019 words — Domain 6.
- [163] Neo4j Live: Entity Resolution and Deduplication with Neo4j and GenAI — https://www.youtube.com/watch?v=GMTY78xqGXQ — 7,177 words — Domain 7.
- [164] Getting started with Transkribus — https://www.youtube.com/watch?v=TE9fOzkibiE — 534 words — Domain 2.
- [165] Quick Start Regrid's Interactive API Sandbox Guide — https://www.youtube.com/watch?v=RVakKAvFa_M — 1,826 words — Domain 7.
- [166] How to Find the Best Probate Leads First — https://www.youtube.com/watch?v=AZazHyPY6xU — 1,669 words — Domain 2.
- [167] DataTree Hacks: Find Full Legal Descriptions and Title Vesting Information — https://www.youtube.com/watch?v=aUiod-Jy68U — 1,909 words — Domain 6.
- [168] DataTree Hacks: How to Do Title Research and Hire Abstractor Services — https://www.youtube.com/watch?v=GfyX48eCbRY — 1,416 words — Domain 6.
- [169] AWS What’s Next Ft. Amazon Textract for Handwriting — https://www.youtube.com/watch?v=wXbImDeCCsY — 3,952 words — Domain 2.
- [170] Getting Started with Digital Preservation: Fixity Pro — https://www.youtube.com/watch?v=1pRY7lpZ7nA — 1,099 words — Domain 7.
- [171] NODES 2024 - Beyond the Silos Achieving Data Harmony With Graph Based ER — https://www.youtube.com/watch?v=NtfeEhpvcuk — 4,518 words — Domain 7.
- [172] Exporting Regrid Data to ArcGIS - Regrid Property App (Web) — https://www.youtube.com/watch?v=EVN-9bqTEtM — 372 words — Domain 7.
- [173] Feature Service Product Demo — https://www.youtube.com/watch?v=X-_cLY3_96Y — 1,028 words — Domain 7.
- [174] Transkribus Webinar for Beginners (English) — https://www.youtube.com/watch?v=bLXMXvhuz6k — 9,406 words — Domain 2.
- [175] DataTree Hacks: How to Find Portfolio Owners With Multiple Properties — https://www.youtube.com/watch?v=9RvXCiHUzlo — 1,105 words — Domain 7.
- [176] DataTree Hacks: How to Search and Find Property Owners Nationwide — https://www.youtube.com/watch?v=y5XZp-4n_uc — 1,235 words — Domain 7.
- [177] Regrid Parcel Data - Overview & Coverage — https://www.youtube.com/watch?v=EToN9mWFZWc — 5,954 words — Domain 7.
- [178] Import Your Own Property Data - Regrid Property App (Web) — https://www.youtube.com/watch?v=6nMKiCCsK60 — 846 words — Domain 7.
- [179] Parcel data by the state on the Regrid Data Store \| Demo — https://www.youtube.com/watch?v=MdSAG5LMn4I — 129 words — Domain 7.
- [180] Using Datasets - Regrid Property App (Web) — https://www.youtube.com/watch?v=-s07juX_8jE — 239 words — Domain 7.
- [181] Regrid Mapping Platform - Filter Data — https://www.youtube.com/watch?v=cKYlwRY3aVw — 728 words — Domain 7.
- [182] Troubleshooting Data Import - Regrid Property App (Web) — https://www.youtube.com/watch?v=VAtPDJ1KDjw — 2,037 words — Domain 7.
- [183] Quick Start - The Regrid Property App (Web) — https://www.youtube.com/watch?v=1Wm_NPEagT8 — 1,021 words — Domain 7.
- [184] How to Find Old Probate Leads — https://www.youtube.com/watch?v=nRRFhMEip8c — 1,584 words — Domain 2.
- [185] Probates List on Propstream Wholesale Real Estate — https://www.youtube.com/watch?v=W0bwM9N_98Y — 3,642 words — Domain 5.
- [186] Best Real Estate Data APIs for Building a Deal Finder App — https://www.youtube.com/watch?v=NMsRlUhQbUI — 1,095 words — Domain 7.
- [187] The Fastest Way to Research Any Property in the United States — https://www.youtube.com/watch?v=ntT8V0gnpAs — 5,995 words — Domain 8.
- [188] Scraping Data--Probate--Public Notice — https://www.youtube.com/watch?v=sX_SYXDaDeA — 781 words — Domain 2.
- [189] DataTree Hacks: TaxSource Reports and Property Tax Verification — https://www.youtube.com/watch?v=2ThZ61aal9k — 1,753 words — Domain 7.

## Reproducibility and known limits

- The generator scans every full_text and every segment; the companion compendium includes every contiguous segment window, not merely ranked highlights.
- Classification and retrieval are deterministic lexical heuristics. Editorial procedures provide a structured operating model; they do not imply every detail was stated by every cited video.
- No external model, network call or third-party package is used. Current legal/API verification and independent storyboard OCR are not performed.
- Corpus SHA-256 fingerprints are listed per video in the compendium. Rebuild from the same source files to reproduce the documents.

