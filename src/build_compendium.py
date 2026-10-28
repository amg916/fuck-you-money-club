#!/usr/bin/env python3
"""Build a deterministic, extractive video compendium; no network or dependencies."""
import argparse
from collections import Counter
import html
import json
from pathlib import Path
import re

if __package__:
    from .fetch_transcripts import atomic_write
else:
    from fetch_transcripts import atomic_write

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = (
    'Forensic Genealogy, Descendancy & GPS Proof Standard',
    'Probate Court Procedures, Wills, Intestacy & Estate Administration',
    'Vital Records, Death Certificates, SSDI & Obituary Mining',
    'State Unclaimed Property & Tax/Foreclosure Surplus Funds Recovery',
    'Curative Title, Tangled/Heirs Property Resolution & Probate Real Estate',
    'Skip Tracing, Title Search, GIS/Parcel APIs (Regrid/DataTree), HTR/OCR & Graph Entity Resolution',
)
# Each vocabulary doubles as classification evidence and a mention dictionary.
VOCABULARY = (
    'forensic genealogy|descendancy|descendants|genealogy|genealogical|ancestors|family history|'
    'Genealogical Proof Standard|GPS proof|reasonably exhaustive research|proof argument|'
    'FamilySearch|Family Search|Ancestry|MyHeritage|WikiTree|Geni|RootsMagic|Legacy Family Tree|'
    'Findmypast|GEDmatch|DNA Painter|GEDCOM|Board for Certification of Genealogists|'
    'Evidence Explained|FAN club|cluster research|census|National Archives|NARA|'
    'Fold3|Allen County Public Library|Daughters of the American Revolution',
    'probate|probate court|will|wills|intestacy|intestate|estate administration|executor|'
    'personal representative|letters testamentary|letters of administration|petition for probate|'
    'small estate affidavit|affidavit of heirship|Uniform Probate Code|UPC|'
    'notice to creditors|inventory and appraisal|final accounting|beneficiary|beneficiaries|'
    'estate tax|Form 706|Form 1041|DE-111|DE-150|DE-160|DE-310|trust administration|'
    'surrogate court|register of wills|clerk of court|testate|distribution decree',
    'vital records|death certificate|death certificates|SSDI|Social Security Death Index|'
    'obituary|obituaries|birth certificate|marriage certificate|death records|'
    'Find a Grave|FindAGrave|BillionGraves|Newspapers.com|NewspaperArchive|'
    'GenealogyBank|Legacy.com|Chronicling America|ProQuest|SS-5|SSA|'
    'Social Security Administration|National Death Index|VitalChek|burial records|'
    'cemetery records|funeral home|death notice|vital statistics',
    'unclaimed property|surplus funds|surplus proceeds|excess proceeds|excess funds|'
    'tax sale|tax deed|tax foreclosure|foreclosure surplus|escheat|escheated|'
    'ClaimIt.ca.gov|MissingMoney.com|Missing Money|unclaimed.org|NAUPA|'
    'state controller|state treasurer|claim form|eClaim|claimant relationship|'
    'Property ID|investigator agreement|holder reporting|claim cart|'
    'California Unclaimed Property Law|Florida Statute 45.032|Florida Statute 45.033',
    'curative title|tangled title|heirs property|heirs’ property|heirs\' property|'
    'quiet title|partition action|partition sale|probate real estate|cloud on title|'
    'title defect|quitclaim deed|warranty deed|transfer on death deed|Lady Bird deed|'
    'Uniform Partition of Heirs Property Act|UPHPA|adverse possession|'
    'marketable title|chain of title|tenants in common|joint tenancy|life estate|'
    'real estate investor|inherited property|inherited house|deed correction',
    'skip tracing|skip trace|title search|GIS|parcel|parcels|Regrid|DataTree|'
    'HTR|OCR|entity resolution|knowledge graph|graph database|Neo4j|'
    'Transkribus|Tesseract|handwritten text recognition|optical character recognition|'
    'ArcGIS|QGIS|GeoJSON|Shapefile|GeoPackage|APN|assessor|recorder|'
    'LexisNexis|Accurint|TLOxp|TransUnion|BeenVerified|BatchSkipTracing|'
    'PropStream|LandGlide|NETR Online|NETROnline|PropertyRadar|OpenRefine|'
    'REST API|parcel API|county GIS|Data Dictionary|File Geodatabase|KML',
)


def pattern(term):
    return re.compile(r'(?<!\w)' + re.escape(term).replace(r'\ ', r'\s+') + r'(?!\w)', re.I)


TERMS = tuple(tuple((term, pattern(term)) for term in group.split('|')) for group in VOCABULARY)
ACTION = re.compile(r'\b(search|find|file|request|verify|compare|identify|record|check|'
                    r'obtain|submit|upload|download|select|click|document|petition|'
                    r'prove|trace|contact|must|required|first|next)\b', re.I)
NOISE = re.compile(r'https?://|subscribe|like and share|sponsor|welcome back', re.I)


def clean(text):
    return ' '.join(html.unescape(str(text or '')).split())


def md(text):
    text = clean(text).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return re.sub(r'([\\`*_{}\[\]|])', r'\\\1', text)


def clip(text, limit=420):
    text = clean(text)
    return text if len(text) <= limit else text[:limit].rsplit(' ', 1)[0] + ' …'


def mentions(text):
    return list(dict.fromkeys(term for group in TERMS for term, regex in group if regex.search(text)))


def classify(record):
    meta = record['metadata']
    fields = ((meta.get('title', ''), 9), (' '.join(meta.get('keywords') or []), 5),
              (meta.get('author', ''), 3), (meta.get('shortDescription', ''), 2),
              (record['full_text'], 1))
    scores = [sum(weight * sum(bool(regex.search(text)) for _, regex in group)
                  for text, weight in fields) for group in TERMS]
    return max(range(len(DOMAINS)), key=lambda i: scores[i])


def signal(text, terms):
    return (3 * len(ACTION.findall(text)) + 2 * sum(regex.search(text) is not None for regex in terms)
            - 8 * len(NOISE.findall(text)))


def representative(candidates, terms, count=3):
    """Choose high-signal text across coverage thirds, avoiding duplicate text."""
    chosen, seen = [], set()
    candidates = [(i, clean(text)) for i, text in candidates if clean(text)]
    for part in range(count):
        pool = candidates[len(candidates) * part // count:len(candidates) * (part + 1) // count]
        ranked = sorted(pool, key=lambda pair: (-signal(pair[1], terms), pair[0]))
        for item in ranked:
            if item[1].casefold() not in seen:
                chosen.append(item)
                seen.add(item[1].casefold())
                break
    return sorted(chosen)


def sentences(text):
    # Unpunctuated automatic captions need bounded windows instead of one giant sentence.
    for sentence in re.split(r'(?<=[.!?])\s+|\n+', text):
        words = sentence.split()
        for start in range(0, len(words), 65):
            yield ' '.join(words[start:start + 65])


def render(record, domain):
    meta, segments = record['metadata'], record['segments']
    title = meta.get('title') or record['video_id']
    text = record['full_text']
    found = mentions(title + ' ' + text)
    terms = [pattern(term) for term in found]
    duration = int(meta.get('lengthSeconds') or max(
        (s['start'] + s['duration'] for s in segments), default=0))
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    lines = [f'<a id="video-{record["index"]:03d}"></a>',
             f'### [#{record["index"]:03d}] {md(title)} ({record["video_id"]})', '',
             f'- **URL:** {record["url"]}', f'- **Channel:** {md(meta.get("author", "Unknown"))}',
             f'- **Duration:** {hours:02d}:{minutes:02d}:{seconds:02d} ({duration} seconds)',
             f'- **Word Count:** {len(text.split()):,}', f'- **Segment Count:** {len(segments):,}',
             f'- **Transcript Source:** {md(record.get("client", "Unknown"))}',
             f'- **Assigned Operational Domain:** {domain + 1}. {DOMAINS[domain]}', '',
             '#### Automated Tactical Extraction', '', '**Core Topic & Summary**', '',
             f'Focus: {md(title)}. Operational category: {DOMAINS[domain]}.']
    description = [s for s in sentences(meta.get('shortDescription', '')) if not NOISE.search(s)]
    if description:
        lines.append('Description context: ' + md(clip(description[0], 300)))
    keywords = meta.get('keywords') or []
    if keywords:
        lines.append('Keywords: ' + md(clip(', '.join(keywords[:10]), 240)))
    for _, excerpt in representative(enumerate(sentences(text)), terms, 2):
        lines.append('- Procedural extract: ' + md(clip(excerpt)))
    lines.extend(['', '**Tools, Portals, Statutes & Forms Mentioned**', '',
                  '; '.join(md(term) for term in found) or 'No dictionary matches.', '',
                  '**Key Timestamped Excerpts**', ''])
    whole = any(s.get('timing') == 'whole_video_coverage_not_quote_timestamp' for s in segments)
    if whole:
        lines.append('Storyboard/description reconstruction; not verbatim or time-aligned.\n')
        candidates = list(enumerate(sentences(' '.join(s['text'] for s in segments))))
    else:
        candidates = [(i, s['text']) for i, s in enumerate(segments)]
    excerpts = representative(candidates, terms)
    for index, excerpt in excerpts:
        seconds = int(segments[index]['start']) if not whole else 0
        stamp = 'whole-video' if whole else f'{seconds // 60:02d}:{seconds % 60:02d}'
        lines.append(f'- [{stamp}] {md(clip(excerpt))}')
    if len(excerpts) < 3:
        lines.append(f'Only {len(excerpts)} distinct excerpts available.')
    return '\n'.join(lines) + '\n'


def build(data, output):
    manifest = json.loads((data / 'index.json').read_text(encoding='utf-8'))
    items = sorted(manifest['items'], key=lambda item: item['index'])
    if [item['index'] for item in items] != list(range(1, len(items) + 1)):
        raise ValueError('Manifest indices must be unique and contiguous from 001')
    sections, rows, counts, seen = [], [], Counter(), set()
    for item in items:
        record = json.loads((data / item['json_path']).read_text(encoding='utf-8'))
        if (record['index'], record['video_id']) != (item['index'], item['video_id']):
            raise ValueError('Manifest/transcript identity mismatch')
        if record['video_id'] in seen or record['status'] != 'ok' or not record['full_text'].strip():
            raise ValueError('Duplicate identity or unresolved transcript')
        seen.add(record['video_id'])
        domain = classify(record)
        counts[domain] += 1
        sections.append(render(record, domain))
        title = md(record['metadata'].get('title') or record['video_id'])
        rows.append(f'| [{item["index"]:03d}](#video-{item["index"]:03d}) | {title} | {domain + 1} |')
    intro = ['# Video-by-Video Compendium', '', f'{len(items)} videos in original index order.', '',
             'Deterministic extractive synthesis: metadata context and ranked transcript passages. '
             'Domains are heuristic; dictionary matches indicate mentions, not endorsements. '
             'Caption windows may be sentence fragments; ellipses indicate truncation.', '',
             '## Domain Breakdown', '']
    intro.extend(f'- **{i + 1}. {name}:** {counts[i]} videos' for i, name in enumerate(DOMAINS))
    intro.extend(['', '## Summary Table of Contents', '', '| Video | Title | Domain |',
                  '| --- | --- | --- |', *rows, '', '## Video-by-Video Analysis', ''])
    atomic_write(output, '\n'.join(intro) + '\n' + '\n'.join(sections))
    return len(items)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=ROOT / 'data')
    parser.add_argument('--output', type=Path, default=ROOT / 'VIDEO_BY_VIDEO_COMPENDIUM.md')
    args = parser.parse_args(argv)
    print(f'Built {build(args.data, args.output)} video sections: {args.output}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
