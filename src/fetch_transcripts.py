#!/usr/bin/env python3
"""Fetch a timestamped YouTube caption corpus using only the standard library."""
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import gzip
import html
import http.client
import json
import math
import os
from pathlib import Path
import random
import re
import socket
import ssl
import tempfile
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

if __package__:
    from .storyboard_fallbacks import FALLBACKS, apply_storyboard_fallback
else:
    from storyboard_fallbacks import FALLBACKS, apply_storyboard_fallback

ROOT = Path(__file__).resolve().parents[1]
PLAYER_URL = 'https://www.youtube.com/youtubei/v1/player?prettyPrint=false'
CLIENTS = (
    ('IOS', '20.10.4', 'com.google.ios.youtube/20.10.4 (iPhone16,2; U; CPU iOS 17_5_1 like Mac OS X)'),
    ('ANDROID', '20.10.38', 'com.google.android.youtube/20.10.38 (Linux; U; Android 14) gzip'),
)
FIELDS = ('title', 'author', 'channelId', 'lengthSeconds', 'viewCount', 'shortDescription', 'keywords')


def utcnow():
    return datetime.now(timezone.utc).isoformat()


class RateGate:
    """Space requests across all workers and share server-requested cooldowns."""
    def __init__(self, interval=0.3):
        self.interval = interval
        self.next_request = 0.0
        self.lock = threading.Lock()

    def wait(self):
        while True:
            with self.lock:
                delay = self.next_request - time.monotonic()
                if delay <= 0:
                    self.next_request = time.monotonic() + self.interval
                    return
            time.sleep(delay)

    def defer(self, seconds):
        with self.lock:
            self.next_request = max(self.next_request, time.monotonic() + seconds)


def retry_after(value):
    try:
        return max(0.0, float(value))
    except (TypeError, ValueError):
        try:
            return max(0.0, parsedate_to_datetime(value).timestamp() - time.time())
        except (TypeError, ValueError, OverflowError):
            return 0.0


class Transport:
    def __init__(self, attempts=5, timeout=30, interval=0.3):
        self.attempts = attempts
        self.timeout = timeout
        self.gate = RateGate(interval)

    def request(self, url, user_agent, payload=None):
        body = None if payload is None else json.dumps(payload).encode('utf-8')
        headers = {'User-Agent': user_agent, 'Accept-Encoding': 'gzip'}
        if body is not None:
            headers['Content-Type'] = 'application/json'
        for attempt in range(self.attempts):
            self.gate.wait()
            try:
                req = urllib.request.Request(url, data=body, headers=headers)
                with urllib.request.urlopen(req, timeout=self.timeout) as response:
                    content = response.read()
                    if response.headers.get('Content-Encoding') == 'gzip':
                        content = gzip.decompress(content)
                    return content
            except urllib.error.HTTPError as exc:
                retryable = exc.code in (408, 429) or 500 <= exc.code <= 599
                server_delay = retry_after(exc.headers.get('Retry-After'))
                exc.close()
                if not retryable:
                    raise
                if attempt + 1 == self.attempts:
                    delay = max(server_delay, 2 ** attempt + random.uniform(0, 0.5))
                    self.gate.defer(delay)
                    raise
            except (urllib.error.URLError, socket.timeout, ConnectionError,
                    http.client.IncompleteRead, http.client.RemoteDisconnected) as exc:
                reason = getattr(exc, 'reason', exc)
                if isinstance(reason, ssl.SSLCertVerificationError) or attempt + 1 == self.attempts:
                    raise
                server_delay = 0
            delay = max(server_delay, 2 ** attempt + random.uniform(0, 0.5))
            self.gate.defer(delay)
        raise RuntimeError('Request attempts exhausted')


def video_id(url):
    parsed = urllib.parse.urlparse(url)
    values = urllib.parse.parse_qs(parsed.query).get('v', [])
    if parsed.scheme != 'https' or parsed.hostname not in ('www.youtube.com', 'youtube.com') or len(values) != 1 or not re.fullmatch(r'[A-Za-z0-9_-]{11}', values[0]):
        raise ValueError('Invalid YouTube watch URL: ' + url)
    return values[0]


def track_rank(track):
    english = track.get('languageCode', '').lower().split('-')[0] == 'en'
    return (0 if english and track.get('kind') != 'asr' else 1 if english else 2)


def select_track(tracks):
    usable = [track for track in tracks if track.get('baseUrl')]
    return min(usable, key=track_rank) if usable else None


def clean_text(text):
    return ' '.join(html.unescape(text).split())


def parse_captions(content):
    root = ET.fromstring(content)
    tag = lambda node: node.tag.rsplit('}', 1)[-1]
    if tag(root) not in ('transcript', 'timedtext'):
        raise ValueError('Unexpected caption XML root: ' + tag(root))
    segments = []
    for node in root.iter():
        kind = tag(node)
        if kind not in ('text', 'p'):
            continue
        text = clean_text(''.join(node.itertext()))
        if not text:
            continue
        scale = 1000 if kind == 'p' else 1
        start = float(node.get('t' if kind == 'p' else 'start', '0')) / scale
        duration = float(node.get('d' if kind == 'p' else 'dur', '0')) / scale
        if not all(math.isfinite(value) and value >= 0 for value in (start, duration)):
            raise ValueError('Invalid caption timestamp')
        segments.append({'start': start, 'duration': duration, 'text': text})
    segments.sort(key=lambda segment: segment['start'])
    return segments, ' '.join(segment['text'] for segment in segments)


def atomic_write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent,
                                         prefix='.' + path.name, delete=False) as stream:
            temporary = stream.name
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if temporary and os.path.exists(temporary):
            os.unlink(temporary)


def json_text(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def fetch_video(index, url, transport):
    result = {'index': index, 'url': url, 'video_id': video_id(url),
              'status': 'error', 'metadata': {}, 'caption_tracks': [],
              'selected_track': None, 'segments': [], 'full_text': '',
              'attempts': [], 'fetched_at': utcnow()}
    saw_playable = False
    saw_tracks = False
    for name, version, agent in CLIENTS:
        attempt = {'client': name}
        result['attempts'].append(attempt)
        try:
            payload = {'context': {'client': {'clientName': name, 'clientVersion': version,
                                               'hl': 'en', 'gl': 'US'}},
                       'videoId': result['video_id'], 'contentCheckOk': True, 'racyCheckOk': True}
            player = json.loads(transport.request(PLAYER_URL, agent, payload))
            details = player.get('videoDetails', {})
            result['metadata'].update({key: details[key] for key in FIELDS if key in details})
            playability = player.get('playabilityStatus', {})
            attempt['playability'] = playability
            saw_playable |= playability.get('status') == 'OK'
            tracks = player.get('captions', {}).get('playerCaptionsTracklistRenderer', {}).get('captionTracks', [])
            if tracks:
                result['caption_tracks'] = tracks
            track = select_track(tracks)
            if track is None:
                attempt['outcome'] = 'no_caption_tracks'
                continue
            saw_tracks = True
            result['selected_track'] = track
            segments, text = parse_captions(transport.request(track['baseUrl'], agent))
            if not segments:
                raise ValueError('Caption endpoint returned no text segments')
            result.update(status='ok', segments=segments, full_text=text, client=name)
            attempt['outcome'] = 'ok'
            break
        except Exception as exc:
            attempt['outcome'] = 'error'
            attempt['error'] = {'type': type(exc).__name__, 'message': str(exc)}
    if result['status'] != 'ok':
        if saw_tracks or any(a['outcome'] == 'error' for a in result['attempts']):
            result['status'] = 'error'
        else:
            result['status'] = 'no_captions' if saw_playable else 'unavailable'
    if (result['status'] != 'ok' and not saw_tracks
            and any(a['outcome'] == 'no_caption_tracks' for a in result['attempts'])):
        apply_storyboard_fallback(result)
    result['fetched_at'] = utcnow()
    return result


def save_result(result, output):
    stem = f"{result['index']:03d}_{result['video_id']}"
    result['json_path'] = f'transcripts/{stem}.json'
    result['text_path'] = f'transcripts/{stem}.txt'
    atomic_write(output / result['text_path'], result['full_text'] + ('\n' if result['full_text'] else ''))
    atomic_write(output / result['json_path'], json_text(result))
    return {key: value for key, value in result.items() if key not in ('segments', 'full_text', 'caption_tracks')} | {
        'segment_count': len(result['segments']), 'word_count': len(result['full_text'].split())}


def patch_existing_corpus(output=ROOT / 'data'):
    """Repair known captionless records offline; validate before writing anything."""
    output = Path(output)
    manifest = json.loads((output / 'index.json').read_text(encoding='utf-8'))
    prepared = []
    seen = set()
    for item in manifest['items']:
        path = output / 'transcripts' / f"{item['index']:03d}_{item['video_id']}.json"
        result = json.loads(path.read_text(encoding='utf-8'))
        if result['video_id'] != item['video_id'] or result['index'] != item['index']:
            raise ValueError('Manifest identity mismatch: ' + str(path))
        if result['video_id'] in seen:
            raise ValueError('Duplicate video identity')
        seen.add(result['video_id'])
        changed = False
        if result['video_id'] in FALLBACKS and not result.get('full_text', '').strip():
            changed = apply_storyboard_fallback(result)
        if result['status'] != 'ok' or not result.get('full_text', '').strip():
            raise ValueError('Unresolved transcript: ' + str(path))
        prepared.append((item, result, changed))
    items = []
    for item, result, changed in prepared:
        if changed:
            item = save_result(result, output)
        else:
            item = dict(item, status=result['status'],
                        word_count=len(result['full_text'].split()),
                        segment_count=len(result['segments']))
        items.append(item)
    manifest.update(items=items, total=len(items), processed=len(items),
                    counts={'ok': len(items), 'no_captions': 0, 'unavailable': 0, 'error': 0})
    atomic_write(output / 'index.json', json_text(manifest))
    return manifest


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--urls', type=Path, default=ROOT / 'urls.txt')
    parser.add_argument('--output', type=Path, default=ROOT / 'data')
    parser.add_argument('--attempts', type=int, default=5)
    parser.add_argument('--timeout', type=float, default=30)
    parser.add_argument('--interval', type=float, default=0.3, help='Minimum seconds between requests globally')
    args = parser.parse_args(argv)
    if args.attempts < 1 or args.timeout <= 0 or args.interval < 0:
        parser.error('attempts and timeout must be positive; interval must be nonnegative')
    urls = args.urls.read_text(encoding='utf-8').splitlines()
    if not urls:
        parser.error('URL list is empty')
    for url in urls:
        video_id(url)
    transport = Transport(args.attempts, args.timeout, args.interval)
    started = utcnow()
    items = []
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(fetch_video, i, url, transport): (i, url)
                   for i, url in enumerate(urls, 1)}
        for future in as_completed(futures):
            result = future.result()
            items.append(save_result(result, args.output))
            print(f"[{len(items)}/{len(urls)}] {result['index']:03d} {result['video_id']}: {result['status']}", flush=True)
    items.sort(key=lambda item: item['index'])
    counts = {status: sum(item['status'] == status for item in items)
              for status in ('ok', 'no_captions', 'unavailable', 'error')}
    manifest = {'schema_version': 1, 'started_at': started, 'finished_at': utcnow(),
                'total': len(urls), 'processed': len(items), 'counts': counts, 'items': items}
    atomic_write(args.output / 'index.json', json_text(manifest))
    print(json.dumps({'total': len(urls), 'counts': counts}), flush=True)
    return 0 if counts['ok'] == len(urls) else 1


if __name__ == '__main__':
    raise SystemExit(main())
