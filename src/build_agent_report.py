#!/usr/bin/env python3
"""Build offline, source-linked operational reports using Python's standard library.

Run: python3 -m src.build_agent_report
Editorial procedures are explicitly separated from extractive transcript evidence.
No external AI, APIs, credentials, or third-party packages are required.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path
import re

if __package__:
    from .fetch_transcripts import ROOT, atomic_write, patch_existing_corpus
    from .report_playbook import DOMAINS, PROCEDURES
else:
    from fetch_transcripts import ROOT, atomic_write, patch_existing_corpus
    from report_playbook import DOMAINS, PROCEDURES

STOP = set('the a an of and or to in on for with is are was were be been it that this those these you your we our they their i my he she his her have has had can will would should could from as at by not but if then than so do does did about into what how when where who which all any some more also just very there here'.split())
TOOLS = (
    'FamilySearch', 'Ancestry', 'FindAGrave', 'Find a Grave', 'SSDI', 'SS-5',
    'Transkribus', 'AWS Textract', 'Textract', 'ClaimIt.ca.gov', 'Table of Heirship',
    'Small Estate', '13101', 'HB 96', 'Pennsylvania Treasury', 'UPHPA',
    'Uniform Partition', 'RESPA', 'TILA', 'Garn', 'TLOxp', 'TLO', 'idiCORE',
    'Accurint', 'PropStream', 'DataTree', 'TaxSource', 'Regrid', 'ArcGIS',
    'Neo4j', 'Fixity Pro', 'ProbateData', 'Deal Finder', 'Newspapers.com',
    'GenealogyBank', 'Chronicling America', 'BillionGraves', 'MyHeritage',
    'Google', 'Bing', 'Facebook', 'LinkedIn', 'LexisNexis', 'PACER',
    'Excel', 'CSV', 'GeoJSON', 'Shapefile', 'GeoPackage', 'KML', 'GPKG', 'GDB',
)
ACTION = re.compile(r'\b(search|check|find|verify|record|request|compare|look|click|select|upload|download|file|contact|read|identify|follow|use|obtain|review|trace|document)\b', re.I)
SIGNAL = re.compile(r'\b(must|need|important|because|first|step|deadline|required|cannot|always|never|example|however|instead)\b', re.I)
URL = re.compile(r'https?://[^\s<>"\]]+')


def tokens(text):
    return [w for w in re.findall(r'[a-z0-9]+', text.lower()) if len(w) > 2 and w not in STOP]


def stamp(seconds):
    seconds = max(0, int(float(seconds)))
    hours, rem = divmod(seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


def safe(text):
    return re.sub(r'\s+', ' ', str(text)).replace('|', '\\|').replace('<', '&lt;').replace('>', '&gt;').replace('[', '\\[').replace(']', '\\]')


def load_corpus(data, expected=189):
    data = Path(data)
    manifest = json.loads((data / 'index.json').read_text(encoding='utf-8'))
    items = sorted(manifest['items'], key=lambda x: x['index'])
    if len(items) != expected or [x['index'] for x in items] != list(range(1, expected + 1)):
        raise ValueError('Corpus must have consecutive unique indices 1 through ' + str(expected))
    videos, ids = [], set()
    for item in items:
        path = data / 'transcripts' / f"{item['index']:03d}_{item['video_id']}.json"
        video = json.loads(path.read_text(encoding='utf-8'))
        if any(video.get(k) != item.get(k) for k in ('index', 'video_id', 'url')):
            raise ValueError('Manifest mismatch: ' + str(path))
        if video['video_id'] in ids:
            raise ValueError('Duplicate video ID')
        ids.add(video['video_id'])
        if video.get('status') != 'ok' or not video.get('full_text', '').strip() or not video.get('segments'):
            raise ValueError('Missing transcript: ' + str(path))
        if video['url'] != 'https://www.youtube.com/watch?v=' + video['video_id']:
            raise ValueError('Unexpected video URL')
        previous = -1
        for segment in video['segments']:
            start, duration = float(segment['start']), float(segment['duration'])
            if not math.isfinite(start) or not math.isfinite(duration) or start < previous or duration < 0 or not segment['text'].strip():
                raise ValueError('Invalid segment: ' + str(path))
            previous = start
        text_path = path.with_suffix('.txt')
        if text_path.read_text(encoding='utf-8').strip() != video['full_text'].strip():
            raise ValueError('JSON/text mismatch: ' + str(path))
        video['word_count'] = len(video['full_text'].split())
        video['digest'] = hashlib.sha256(video['full_text'].encode()).hexdigest()
        videos.append(video)
    if manifest.get('counts', {}).get('ok') != expected:
        raise ValueError('Manifest counts are stale')
    return videos


def windows(video, target=95):
    """Read every segment into non-overlapping, contiguous evidence windows."""
    result, parts, count, start = [], [], 0, 0
    for segment in video['segments']:
        if not parts:
            start = segment['start']
        parts.append(segment['text'])
        count += len(segment['text'].split())
        if count >= target:
            result.append({'start': start, 'text': ' '.join(parts)})
            parts, count = [], 0
    if parts:
        result.append({'start': start, 'text': ' '.join(parts)})
    return result


def classify(video):
    title = Counter(tokens(video['metadata'].get('title', '')))
    body = Counter(tokens(video['full_text']))
    scores = {}
    for domain, (_, terms) in DOMAINS.items():
        scores[domain] = sum(10 * title[t] + math.log1p(body[t]) for t in tokens(terms))
    return max(scores, key=scores.get)


def mentions(text):
    found = set()
    for tool in TOOLS:
        if re.search(r'(?<!\w)' + re.escape(tool) + r'(?!\w)', text, re.I):
            found.add(tool)
    found.update(url.rstrip('.,);') for url in URL.findall(text))
    found.update(m.group(0) for m in re.finditer(r'\b(?:[A-Z][a-z]+\s+){0,3}(?:Code|Act|Statute)\s*(?:§\s*)?\d+(?:\.\d+)*', text))
    return sorted(found, key=lambda s: (s.casefold(), s))


class EvidenceIndex:
    def __init__(self, videos):
        self.videos = []
        self.rows = []
        self.by_video = defaultdict(list)
        self.postings = defaultdict(set)
        self.video_ids = set()
        for video in videos:
            self.add_record(video)

    def add_record(self, video):
        if video['video_id'] in self.video_ids:
            return
        video['domain'] = classify(video)
        video['tools'] = mentions(video['full_text'] + '\n' + video['metadata'].get('shortDescription', ''))
        rows = [dict(window, video=video, terms=Counter(tokens(window['text'])))
                for window in windows(video)]
        for row in rows:
            idx = len(self.rows)
            self.rows.append(row)
            self.by_video[video['index']].append(row)
            for word in row['terms']:
                self.postings[word].add(idx)
        self.videos.append(video)
        self.video_ids.add(video['video_id'])

    def search(self, text, top_k=18, allowed_video_ids=None):
        allowed = None if allowed_video_ids is None else set(allowed_video_ids)
        query = set(tokens(text))
        hits = []
        for row in self.rows:
            if allowed is not None and row['video']['video_id'] not in allowed:
                continue
            overlap = sorted(query & row['terms'].keys())
            if overlap:
                hits.append(dict(row, score=sum(row['terms'][w] for w in overlap),
                                 matched_terms=overlap))
        return sorted(hits, key=lambda row: -row['score'])[:max(0, top_k)]

    def query(self, text, limit=4, domain=None):
        query = set(tokens(text))
        candidates = set()
        for word in query:
            candidates.update(self.postings.get(word, ()))
        ranked = []
        for idx in sorted(candidates):
            row = self.rows[idx]
            overlap = sorted(query & row['terms'].keys())
            if len(overlap) < min(2, len(query)):
                continue
            score = math.fsum(math.log(1 + len(self.rows) / (1 + len(self.postings[w]))) * (1 + math.log(row['terms'][w])) for w in overlap)
            if domain == row['video']['domain']:
                score *= 1.15
            ranked.append((score, idx))
        chosen, seen = [], set()
        for _, idx in sorted(ranked, key=lambda x: (-x[0], x[1])):
            row = self.rows[idx]
            identity = row['video']['index']
            if identity not in seen:
                chosen.append(row)
                seen.add(identity)
            if len(chosen) >= limit:
                break
        return chosen

    def highlights(self, video, limit=6):
        rows = self.by_video[video['index']]
        title_terms = set(tokens(video['metadata'].get('title', '')))
        ranked = sorted(enumerate(rows), key=lambda pair: (-sum(pair[1]['terms'][t] for t in title_terms) - 2 * len(SIGNAL.findall(pair[1]['text'])) - len(ACTION.findall(pair[1]['text'])), pair[0]))
        selected = []
        for idx, row in ranked:
            if all(abs(idx - previous) > 1 for previous, _ in selected) or len(rows) <= 2:
                selected.append((idx, row))
            if len(selected) >= limit:
                break
        return [row for _, row in sorted(selected)]


def evidence(row):
    video = row['video']
    label = f"[{video['index']:03d}]"
    if video.get('client') == 'STORYBOARD_OCR':
        return f"{label} — supplied storyboard/description reconstruction; no quote timestamp: {safe(row['text'])}"
    at = stamp(row['start'])
    link = video['url'] + '&t=' + str(int(row['start'])) + 's'
    return f'{label} [{at}]({link}) — “{safe(row["text"])}”'


def build_compendium(index):
    lines = ['# Video-by-Video Tactical Compendium', '',
             '## Method and provenance', '',
             'Every full transcript and segment is scanned. Summaries below are extractive: selected contiguous caption passages, not invented paraphrases. Captions may contain recognition errors. Editorial action prompts identify work to perform on the quoted evidence; they are not additional speaker claims.',
             'The three STORYBOARD_OCR entries are user-supplied non-verbatim reconstructions with whole-video coverage, not independently recovered captions or timestamped quotations.',
             'Tool matches combine transcript and description and are labeled by source. The directory is an automatically extracted candidate inventory, not a guarantee of every implicit or misspelled reference.', '']
    for video in index.videos:
        n = video['index']
        metadata = video['metadata']
        rows = index.highlights(video)
        lines += [f'## [{n:03d}] {safe(metadata.get("title", "Untitled"))}', '',
                  f'- Video Index: #{n:03d}', f'- Video ID: `{video["video_id"]}`',
                  f'- Full URL: {video["url"]}', f'- Title: {safe(metadata.get("title", ""))}',
                  f'- Channel/Author: {safe(metadata.get("author", "Not supplied"))}',
                  f'- Duration: {stamp(metadata.get("lengthSeconds", 0))} ({metadata.get("lengthSeconds", 0)} seconds)',
                  f'- Word Count: {video["word_count"]:,}',
                  f'- Assigned Domain: {video["domain"]} — {DOMAINS[video["domain"]][0]}',
                  f'- Source mode: {video.get("client", "caption")}; SHA-256: `{video["digest"]}`', '',
                  '### Executive Summary & Core Methodology', '',
                  'Extractive overview of the video’s most instruction-rich passages:', '']
        for row in rows[:3]:
            lines.append('- ' + evidence(row))
        lines += ['', '### Key Tactical Steps / Actionable Takeaways', '',
                  'Apply these evidence-review operations to the source passages (editorial prompts):']
        for row in rows:
            verbs = sorted(set(word.lower() for word in ACTION.findall(row['text'])))
            lines.append('- Inspect the passage at ' + ('whole-video coverage' if video.get('client') == 'STORYBOARD_OCR' else stamp(row['start'])) + '; extract the ' + (', '.join(verbs[:7]) if verbs else 'research') + ' operations, their prerequisites, exceptions and resulting evidence. Preserve any dates or amounts as speaker claims until checked against the original record.')
        lines += ['', '### Specific Tools, Portals, Statutes, Forms, or Databases Mentioned', '']
        transcript_tools = set(mentions(video['full_text']))
        if not video['tools']:
            lines.append('- No named reference detected by the extractor; inspect the full transcript for unrecognized names.')
        for tool in video['tools']:
            source = 'transcript/reconstruction' if tool in transcript_tools else 'metadata description only'
            lines.append(f'- {safe(tool)} — {source}')
        lines += ['', '### High-Signal Transcript Highlights / Key Quotes', '']
        lines.extend('- ' + evidence(row) for row in rows)
        lines += ['', '### Full-coverage chapter map', '',
                  'All contiguous transcript windows appear below, ensuring later sections and low-key passages are not excluded by highlight ranking. Each entry is an extract, not a paraphrased claim.', '']
        lines.extend('- ' + evidence(row) for row in index.by_video[n])
        lines.append('')
    return '\n'.join(lines) + '\n'


def build_manual(index):
    videos = index.videos
    words = sum(v['word_count'] for v in videos)
    seconds = sum(float(v['metadata'].get('lengthSeconds', 0)) for v in videos)
    lines = ['# Advanced Agent How-To Operational Manual & System Playbook', '',
             '## Executive Overview & Corpus Telemetry', '',
             f'- Videos: {len(videos)}; non-empty successful records: {len(videos)}.',
             f'- Corpus words: {words:,}; video duration: {seconds / 3600:.2f} hours.',
             f'- Caption records: {sum(v.get("client") != "STORYBOARD_OCR" for v in videos)}; supplied storyboard/description reconstructions: {sum(v.get("client") == "STORYBOARD_OCR" for v in videos)}.',
             '- Six core operational domains connect genealogy, probate, vital-record evidence, recovery, curative title, and skip tracing/title search. Domain 7 supplies the data infrastructure; Domain 8 supplies orchestration.', '',
             '### End-to-end architecture', '',
             'Lead → immutable source capture → identity resolution → death/domicile anchor → genealogical proof → estate authority → asset/title/lien verification → net-value underwriting → claim or acquisition packet → adjudication/closing → distribution → preservation.', '',
             '### Evidence contract', '',
             'Operational procedures are editorial synthesis, not quotations or legal determinations. Related evidence below each procedure is retrieved by lexical relevance from the entire corpus; retrieval establishes a research lead, not entailment of every procedural sentence. Read the cited excerpt before relying on it. A missing exact rule is explicitly unresolved.',
             'Video statements are dated source claims. Current statute text, court orders and official program instructions govern concrete filings. Numeric thresholds, fees, limitation periods and state-specific deadlines are not invented when absent. This report is generated offline and does not verify current law or live API contracts.',
             'All caption excerpts are contiguous source text and may contain ASR errors. STORYBOARD_OCR entries are non-verbatim supplied reconstructions; no fabricated quote timestamps are assigned.', '',
             '### Shared case and evidence schema', '',
             '```text',
             'Case(case_id, jurisdiction, objective, owner_entity_id, asset_id, stage, next_action)',
             'Assertion(assertion_id, subject_id, predicate, value, valid_from, valid_to, confidence)',
             'Source(source_id, video_id, segment_start, record_locator, retrieved_at, sha256)',
             'Support(assertion_id, source_id, source_type, informant, independence_group)',
             'Authority(case_id, representative, capacity, instrument, effective_date, limitations)',
             'Interest(parcel_id, owner_id, numerator, denominator, vesting, instrument_id)',
             'Lien(asset_id, creditor, amount_as_of, priority_basis, release_or_survival_evidence)',
             'Task(case_id, prerequisite_ids, assignee, due_date, status, evidence_required)',
             '```', '',
             'Unknown is a first-class value, not zero. Preserve competing assertions. Canonical identity changes must be reversible; statutory rules must carry jurisdiction and effective-date ranges.', '']
    for domain, (title, _) in DOMAINS.items():
        lines += [f'## Domain {domain}: {title}', '']
        domain_videos = [v for v in videos if v['domain'] == domain]
        lines.append('Primary video assignments: ' + (', '.join(f'[{v["index"]:03d}]' for v in domain_videos) or 'Cross-domain sources; see evidence below.'))
        lines.append('')
        for number, (name, inputs, operations, artifact) in enumerate(PROCEDURES[domain], 1):
            steps = operations.split('|')
            related = index.query(name + ' ' + inputs + ' ' + operations, domain=domain)
            lines += [f'### {domain}.{number} {name}', '', f'**Input:** {inputs}.',
                      f'**Output:** {artifact}.', '', '**Ordered procedure (editorial synthesis):**', '']
            lines.extend(f'{i}. {step}' for i, step in enumerate(steps, 1))
            lines += ['', '**Execution and acceptance contract:**', '',
                      f'- Persist `{artifact}` under the case identifier with an immutable source manifest.',
                      '- Attach supporting record identifiers to each decisive assertion; distinguish source facts from analyst conclusions.',
                      '- Log conflicting evidence and the specific next retrieval needed to resolve it.',
                      '- Mark completion only when inputs, authority, output and unresolved exceptions are explicit.', '',
                      '**Related corpus evidence — inspect for scope and exceptions:**', '']
            lines.extend('- ' + evidence(row) for row in related)
            if not related:
                lines.append('- No matching passage found; this procedure is editorial guidance without established corpus support.')
            lines.append('')
        lines += ['### Domain evidence workbench', '',
                  'The following source-specific evidence cards expose primary assigned videos without treating lexical matches as verified legal rules.', '']
        for video in domain_videos:
            lines += [f'#### [{video["index"]:03d}] {safe(video["metadata"].get("title", ""))}', '',
                      f'- Source: {video["url"]}',
                      '- Agent task: extract the demonstrated method, identify its jurisdiction/date and compare its prerequisites with the case.',
                      '- Acceptance: cite the original record or official instruction for any dispositive name, fraction, deadline, amount or legal conclusion.']
            lines.extend('- ' + evidence(row) for row in index.highlights(video, 2))
            lines.append('')
    lines += ['## State-specific recovery research matrix', '',
              '| Jurisdiction | Required operational fields | Corpus evidence leads |',
              '|---|---|---|']
    for state in ('California', 'Ohio HB 96', 'Pennsylvania Treasury', 'Michigan', 'Delaware', 'New Mexico'):
        rows = index.query(state + ' investigator registration fee claim deadline', 3)
        refs = ', '.join(
            f'[{r["video"]["index"]:03d}] (whole-video reconstruction)'
            if r['video'].get('client') == 'STORYBOARD_OCR'
            or r['video'].get('provenance', {}).get('time_aligned') is False
            else f'[{r["video"]["index"]:03d}] {stamp(r["start"])}'
            for r in rows)
        lines.append(f'| {state} | Registration; fee/contract restrictions; claim authority; steps; exact deadline; effective date. Not established solely by retrieval. | {refs or "No evidence located"} |')
    lines += ['', '## Decision matrices', '',
              '| Condition | Route | Required output |', '|---|---|---|',
              '| Owner alive, identity matched | Direct owner claim | Ownership/address evidence |',
              '| Owner deceased, representative appointed | Estate representative route | Valid appointment and asset entitlement |',
              '| Owner deceased, no administration | Evaluate jurisdiction-specific successor procedure | Eligibility and complete heirship proof |',
              '| Property pre-escheat notice | Holder route | Holder confirmation and notice deadline |',
              '| Recorded lien conflicts with surplus schedule | Reconcile both verification methods | Priority/order/payoff evidence |',
              '| Fractional parcel interest only | TIC acquisition analysis | Cap table and control/exit assessment |',
              '| Conflicting identities | Keep entities separate | Discriminating source retrieval |',
              '| Missing numeric rule | Retrieve official rule | Jurisdiction/date-specific authority |', '',
              '## Master Tool / Portal / Statute / Database Candidate Directory', '',
              'Automatically detected names and URLs from every transcript and metadata description. This is a candidate inventory: ASR misspellings, unnamed references and ambiguous short names require source review. Each video’s entry distinguishes transcript from description mentions.', '']
    directory = defaultdict(list)
    for video in videos:
        for tool in video['tools']:
            directory[tool].append(video['index'])
    for tool in sorted(directory, key=lambda s: (s.casefold(), s)):
        lines.append('- **' + safe(tool) + '** — ' + ', '.join(f'[{n:03d}]' for n in directory[tool]))
    lines += ['', '## Complete source register', '']
    for video in videos:
        lines.append(f'- [{video["index"]:03d}] {safe(video["metadata"].get("title", ""))} — {video["url"]} — {video["word_count"]:,} words — Domain {video["domain"]}.')
    lines += ['', '## Reproducibility and known limits', '',
              '- The generator scans every full_text and every segment; the companion compendium includes every contiguous segment window, not merely ranked highlights.',
              '- Classification and retrieval are deterministic lexical heuristics. Editorial procedures provide a structured operating model; they do not imply every detail was stated by every cited video.',
              '- No external model, network call or third-party package is used. Current legal/API verification and independent storyboard OCR are not performed.',
              '- Corpus SHA-256 fingerprints are listed per video in the compendium. Rebuild from the same source files to reproduce the documents.', '']
    return '\n'.join(lines) + '\n'


def generate(data=ROOT / 'data', output=ROOT, repair=True, expected=189):
    data, output = Path(data), Path(output)
    if repair:
        patch_existing_corpus(data)
    index = EvidenceIndex(load_corpus(data, expected))
    manual = build_manual(index)
    compendium = build_compendium(index)
    if any(f'## Domain {n}:' not in manual for n in range(1, 9)):
        raise ValueError('Missing operational domain')
    for video in index.videos:
        if video['video_id'] not in compendium or video['url'] not in compendium:
            raise ValueError('Incomplete compendium')
    paths = (output / 'ADVANCED_AGENT_HOW_TO_REPORT.md', output / 'VIDEO_BY_VIDEO_COMPENDIUM.md')
    for path, text in zip(paths, (manual, compendium)):
        atomic_write(path, text)
    return paths


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=ROOT / 'data')
    parser.add_argument('--output', type=Path, default=ROOT)
    parser.add_argument('--no-repair', action='store_true')
    args = parser.parse_args(argv)
    for path in generate(args.data, args.output, not args.no_repair):
        print(path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
