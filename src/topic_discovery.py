"""Bounded, dependency-free YouTube practitioner discovery with offline corpus fallback."""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import urllib.request

CODEX_PATH = shutil.which('codex') or ('/Users/macbookpro/.local/bin/codex' if os.access('/Users/macbookpro/.local/bin/codex', os.X_OK) else '/Applications/ChatGPT.app/Contents/Resources/codex')


def parse_topics(raw_topics) -> list[str]:
    if raw_topics is None:
        return []
    values = [raw_topics] if isinstance(raw_topics, str) else raw_topics
    if not isinstance(values, list) or any(not isinstance(v, str) for v in values):
        raise ValueError('topics must be a string or list of strings')
    out, seen = [], set()
    for value in values:
        for topic in re.split(r'[\n;,]+', value):
            topic = topic.strip()
            if topic and topic.casefold() not in seen:
                seen.add(topic.casefold())
                out.append(topic)
    return out


def expand_topic_queries(topics: list[str], use_codex_cli=False, codex_timeout=25) -> dict:
    topics = parse_topics(topics)
    suffixes = ['step by step walkthrough tutorial', 'county court portal records search how to',
                'forms affidavit statute filing checklist', 'advanced pro tips mistakes traps to avoid',
                'real case study example', 'complete masterclass training guide']
    domains = [({'probate', 'estate', 'heir'}, ['small estate affidavit statutory thresholds', 'heirship probate docket workflow', 'executor inventory distribution audit', 'estate jurisdiction deadlines']),
               ({'surplus', 'unclaimed', 'funds'}, ['unclaimed property holder claim proof', 'surplus funds priority lien research', 'recovery fee limits assignment rules', 'treasurer disbursement audit']),
               ({'title', 'lien', 'deed'}, ['chain of title recorder index', 'lien release payoff verification', 'quiet title service requirements', 'deed legal description exceptions']),
               ({'tracing', 'genealogy'}, ['genealogy source citation proof standard', 'skip tracing identity disambiguation', 'heir family tree vital records', 'privacy consent research limits']),
               ({'tax', 'foreclosure'}, ['tax sale redemption deadline', 'foreclosure surplus claim priority', 'auction title due diligence', 'county notice service audit'])]
    queries = []
    for topic in topics:
        tokens = set(re.findall(r'\w+', topic.lower()))
        extra = next((items for keys, items in domains if keys & tokens),
                     ['expert methodology evidence validation', 'professional tools workflow demonstration',
                      'quality control checklist primary sources', 'troubleshooting edge cases decision tree'])
        queries.extend(f'{topic} {s}' for s in suffixes + extra)
    engine = 'practitioner_multi_angle'
    if use_codex_cli and os.access(CODEX_PATH, os.X_OK):
        try:
            result = subprocess.run([CODEX_PATH, 'exec', '--ephemeral', '--skip-git-repo-check',
                                     'Generate 10 high-signal YouTube search queries for deep expert tutorials on: '
                                     + '; '.join(topics) + '. Output only a JSON array of strings.'],
                                    capture_output=True, text=True, timeout=codex_timeout, check=True)
            text = result.stdout.strip()
            match = re.search(r'\[.*\]', text, re.S)
            additions = json.loads(match.group(0)) if match else []
            if isinstance(additions, list):
                additions = [q.strip() for q in additions if isinstance(q, str) and 3 < len(q) < 300][:10]
                if additions:
                    queries.extend(additions)
                    engine = 'chatgpt_pro_codex+practitioner'
        except (OSError, subprocess.SubprocessError, ValueError):
            pass
    return {'topics': topics, 'queries': list(dict.fromkeys(queries)), 'engine': engine}


def _text(value):
    if not isinstance(value, dict):
        return ''
    return value.get('simpleText') or ''.join(r.get('text', '') for r in value.get('runs', []))


def search_youtube_query(query: str, transport=None, max_results=15) -> list[dict]:
    """transport, when supplied, is a callable(request, timeout=...) returning JSON or a response."""
    payload = {'context': {'client': {'clientName': 'WEB', 'clientVersion': '2.20250201.00.00',
                                       'hl': 'en', 'gl': 'US'}}, 'query': query}
    request = urllib.request.Request('https://www.youtube.com/youtubei/v1/search?prettyPrint=false',
                                     data=json.dumps(payload).encode(),
                                     headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'})
    response = (transport or urllib.request.urlopen)(request, timeout=8)
    if isinstance(response, dict):
        tree = response
    else:
        try:
            tree = json.loads(response.read(8 * 1024 * 1024))
        finally:
            response.close()
    results, seen = [], set()
    stack = [tree]
    while stack and len(results) < max_results:
        node = stack.pop()
        if isinstance(node, list):
            stack.extend(reversed(node))
        elif isinstance(node, dict):
            video = node.get('videoRenderer')
            if isinstance(video, dict):
                vid = video.get('videoId', '')
                duration = _text(video.get('lengthText'))
                if not re.fullmatch(r'[\w-]{11}', vid, re.ASCII) or vid in seen or not duration:
                    continue
                try:
                    seconds = 0
                    for part in duration.split(':'):
                        seconds = seconds * 60 + int(part)
                except ValueError:
                    continue
                if seconds < 45:
                    continue
                seen.add(vid)
                snippets = ' '.join(_text(s.get('snippetText')) for s in video.get('detailedMetadataSnippets', []))
                results.append({'video_id': vid, 'url': f'https://www.youtube.com/watch?v={vid}',
                                'title': _text(video.get('title')), 'author': _text(video.get('ownerText') or video.get('longBylineText')),
                                'duration': duration, 'length_seconds': seconds,
                                'view_count_text': _text(video.get('viewCountText')),
                                'snippet': snippets or _text(video.get('descriptionSnippet')),
                                'thumbnail_url': f'https://i.ytimg.com/vi/{vid}/hqdefault.jpg', 'matched_query': query})
            else:
                stack.extend(reversed(list(node.values())))
    return results


def relevance_score(video, topics):
    tokens = {t for t in re.findall(r'\w+', ' '.join(topics).lower()) if len(t) > 2}
    title = str(video.get('title', '')).lower()
    body = json.dumps({k: video.get(k, '') for k in ('snippet', 'domain_name', 'domain',
                       'executive_summary', 'finite_details', 'pro_tips')}, ensure_ascii=False).lower()
    hits = sum(4 * (t in title) + (t in body) for t in tokens)
    if not hits:
        return 0
    signals = sum(s in title + body for s in ('tutorial', 'walkthrough', 'step by step', 'checklist', 'case study', 'portal'))
    return hits + signals + (2 if 300 <= int(video.get('length_seconds') or 0) <= 3600 else 0)


def discover_topic_videos(topics, state=None, transport=None, max_videos=24, auto_ingest=True,
                          use_codex_cli=False, search_fn=None) -> dict:
    topic_list = parse_topics(topics)
    if not topic_list:
        raise ValueError('at least one topic is required')
    if type(max_videos) is not int or not 1 <= max_videos <= 100:
        raise ValueError('max_videos must be between 1 and 100')
    expansion = expand_topic_queries(topic_list, use_codex_cli=use_codex_cli)
    corpus = state.resolve(None) if state is not None else []
    known = {v['video_id'] for v in corpus}
    candidates, errors = {}, []
    for query in expansion['queries']:
        try:
            videos = (search_fn or search_youtube_query)(query, transport=transport, max_results=15)
            for video in videos:
                vid = video.get('video_id', '')
                if re.fullmatch(r'[\w-]{11}', vid, re.ASCII):
                    candidate = dict(video, url=f'https://www.youtube.com/watch?v={vid}')
                    candidate['relevance_score'] = relevance_score(candidate, topic_list)
                    candidates.setdefault(vid, candidate)
        except Exception as exc:
            errors.append({'query': query, 'error': f'{type(exc).__name__}: {exc}'})
    matched = [v for v in corpus if relevance_score(v, topic_list)]
    for video in matched:
        candidates[video['video_id']] = dict(video, relevance_score=relevance_score(video, topic_list))
    selected = sorted(candidates.values(), key=lambda v: (-v['relevance_score'], v['video_id']))[:max_videos]
    external = [v for v in selected if v['video_id'] not in known]
    ingest = {'ingested_count': 0, 'cached_count': 0, 'failed_count': 0}
    if auto_ingest and state is not None and external:
        ingest = state.ingest_urls([v['url'] for v in external])
    ready_set = set(state.abridged_by_id) if state is not None else set()
    ready = [v['video_id'] for v in selected if v['video_id'] in ready_set]
    fallback = not ready and bool(corpus)
    if fallback:
        ready = [v['video_id'] for v in corpus[:max_videos]]
    return {'topics': topic_list, 'queries_executed': expansion['queries'], 'engine': expansion['engine'],
            'discovered_count': len(selected), 'ingested_count': ingest['ingested_count'],
            'cached_count': sum(v['video_id'] in known for v in selected) + ingest['cached_count'],
            'failed_count': ingest['failed_count'], 'search_failed_count': len(errors), 'search_errors': errors,
            'matched_corpus_count': len(matched), 'discovered_videos': selected, 'video_ids': ready,
            'fallback_used': fallback,
            'research_summary': f"Searched {len(expansion['queries'])} queries; {len(selected)} candidates; {len(ready)} sources ready. "
                                + ('No selected sources ready; using existing corpus as an explicitly unverified topic fallback.' if fallback
                                   else 'Search relevance is not independent verification of source claims.')}
