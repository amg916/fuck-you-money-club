import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

from src.fetch_transcripts import (CLIENTS, Transport, fetch_video, main,
                                   parse_captions, patch_existing_corpus, retry_after,
                                   save_result, select_track, video_id)
from src.storyboard_fallbacks import FALLBACKS, apply_storyboard_fallback


class CorpusTests(unittest.TestCase):
    def test_urls(self):
        urls = (Path(__file__).resolve().parents[1] / 'urls.txt').read_text().splitlines()
        self.assertEqual(len(urls), 189)
        self.assertEqual(len(set(map(video_id, urls))), 189)
        self.assertEqual(video_id(urls[0]), '9Q4qYeK5DTg')
        self.assertEqual(video_id(urls[-1]), '2ThZ61aal9k')

    def test_storyboard_fallback(self):
        for identity, (duration, text) in FALLBACKS.items():
            with self.subTest(video_id=identity):
                result = {'video_id': identity, 'status': 'no_captions'}
                self.assertTrue(apply_storyboard_fallback(result))
                self.assertEqual(result['status'], 'ok')
                self.assertEqual(result['client'], 'STORYBOARD_OCR')
                self.assertEqual(result['full_text'], text)
                self.assertIsNone(result['selected_track'])
                self.assertEqual(result['metadata']['lengthSeconds'], str(duration))
                self.assertEqual(result['segments'], [{
                    'start': 0.0, 'duration': float(duration), 'text': text,
                    'timing': 'whole_video_coverage_not_quote_timestamp'}])
                self.assertFalse(result['provenance']['verbatim'])
                self.assertFalse(result['provenance']['time_aligned'])
                result['metadata']['lengthSeconds'] = '999'
                apply_storyboard_fallback(result)
                self.assertEqual(result['metadata']['lengthSeconds'], '999')

    def test_unknown_storyboard_unchanged(self):
        result = {'video_id': 'unknown', 'status': 'error', 'metadata': {}}
        before = json.dumps(result, sort_keys=True)
        self.assertFalse(apply_storyboard_fallback(result))
        self.assertEqual(json.dumps(result, sort_keys=True), before)

    def make_patch_corpus(self, root, invalid=False):
        items = []
        for index, identity in enumerate((next(iter(FALLBACKS)), '9Q4qYeK5DTg'), 1):
            text = '' if index == 1 or invalid else 'Existing captions stay intact.'
            result = {'index': index, 'video_id': identity,
                      'url': 'https://www.youtube.com/watch?v=' + identity,
                      'status': 'ok' if text else 'no_captions',
                      'metadata': {'title': 'Fixture'}, 'client': 'IOS',
                      'full_text': text, 'segments': [
                          {'start': 1.0, 'duration': 2.0, 'text': text}] if text else []}
            items.append(save_result(result, root))
        (root / 'index.json').write_text(json.dumps({'items': items, 'total': 2}))
        return items

    def test_patch_existing_corpus(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            items = self.make_patch_corpus(root)
            existing = root / items[1]['json_path']
            before = existing.read_bytes()
            with patch('src.fetch_transcripts.Transport.request', side_effect=AssertionError('network')):
                manifest = patch_existing_corpus(root)
            self.assertEqual(manifest['counts'], {
                'ok': 2, 'no_captions': 0, 'unavailable': 0, 'error': 0})
            self.assertEqual(manifest['processed'], 2)
            self.assertEqual(manifest['total'], 2)
            self.assertEqual(existing.read_bytes(), before)
            repaired = json.loads((root / items[0]['json_path']).read_text())
            self.assertEqual(repaired['client'], 'STORYBOARD_OCR')
            self.assertEqual(manifest['items'][0]['word_count'], len(repaired['full_text'].split()))
            self.assertEqual(manifest['items'][0]['segment_count'], 1)
            self.assertEqual((root / items[0]['text_path']).read_text(), repaired['full_text'] + '\n')
            snapshot = {p: p.read_bytes() for p in root.rglob('*') if p.is_file()}
            self.assertEqual(patch_existing_corpus(root), manifest)
            self.assertEqual({p: p.read_bytes() for p in snapshot}, snapshot)

    def test_patch_validates_before_writing(self):
        for failure in ('unresolved', 'identity', 'duplicate'):
            with self.subTest(failure=failure), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                items = self.make_patch_corpus(root, invalid=failure == 'unresolved')
                if failure == 'identity':
                    path = root / items[1]['json_path']
                    record = json.loads(path.read_text())
                    record['index'] = 99
                    path.write_text(json.dumps(record))
                elif failure == 'duplicate':
                    (root / 'index.json').write_text(json.dumps({'items': [items[0], items[0]]}))
                snapshot = {p: p.read_bytes() for p in root.rglob('*') if p.is_file()}
                with self.assertRaises(ValueError):
                    patch_existing_corpus(root)
                self.assertEqual({p: p.read_bytes() for p in snapshot}, snapshot)

    def test_standard_xml(self):
        segments, text = parse_captions(b'<transcript><text start="1.25" dur="2.5"> A &amp;amp; B\n C </text></transcript>')
        self.assertEqual(segments, [{'start': 1.25, 'duration': 2.5, 'text': 'A & B C'}])
        self.assertEqual(text, 'A & B C')

    def test_format_three(self):
        segments, text = parse_captions(b'<timedtext format="3"><body><p t="1230" d="450"><s>Hello </s><s>world</s></p><p t="2000" d="0"> &amp; </p></body></timedtext>')
        self.assertEqual(segments[0], {'start': 1.23, 'duration': 0.45, 'text': 'Hello world'})
        self.assertEqual(text, 'Hello world &')

    def test_bad_xml_and_timestamp(self):
        for content in (b'<html/>', b'<transcript><text start="nan">bad</text></transcript>'):
            with self.assertRaises(ValueError):
                parse_captions(content)

    def test_track_preference(self):
        tracks = [{'languageCode': 'fr', 'baseUrl': 'fr'},
                  {'languageCode': 'en', 'kind': 'asr', 'baseUrl': 'auto'},
                  {'languageCode': 'en-GB', 'baseUrl': 'manual'}]
        self.assertEqual(select_track(tracks)['baseUrl'], 'manual')
        self.assertEqual(select_track(tracks[:2])['baseUrl'], 'auto')
        self.assertEqual(select_track(tracks[:1])['baseUrl'], 'fr')
        self.assertIsNone(select_track([]))

    def test_fallback_and_metadata(self):
        class FakeTransport:
            def request(self, url, agent, payload=None):
                if payload:
                    if payload['context']['client']['clientName'] == CLIENTS[0][0]:
                        return b'{"playabilityStatus":{"status":"ERROR"}}'
                    return json.dumps({'videoDetails': {'title': 'Example', 'keywords': ['test']},
                                       'captions': {'playerCaptionsTracklistRenderer': {'captionTracks': [
                                           {'languageCode': 'en', 'baseUrl': 'https://example.com/captions'}]}}}).encode()
                return b'<transcript><text start="0" dur="1">Hello</text></transcript>'
        result = fetch_video(1, 'https://www.youtube.com/watch?v=9Q4qYeK5DTg', FakeTransport())
        self.assertEqual(result['status'], 'ok')
        self.assertEqual(result['client'], 'ANDROID')
        self.assertEqual(result['metadata']['title'], 'Example')

    def test_empty_caption_is_failure(self):
        class FakeTransport:
            def request(self, url, agent, payload=None):
                if payload:
                    return b'{"captions":{"playerCaptionsTracklistRenderer":{"captionTracks":[{"baseUrl":"https://example.com"}]}}}'
                return b'<transcript/>'
        self.assertEqual(fetch_video(1, 'https://www.youtube.com/watch?v=9Q4qYeK5DTg', FakeTransport())['status'], 'error')

    @patch('src.fetch_transcripts.urllib.request.urlopen')
    def test_retry(self, open_url):
        response = unittest.mock.MagicMock()
        response.__enter__.return_value = response
        response.headers = {}
        response.read.return_value = b'ok'
        for code in (429, 500, 503):
            open_url.reset_mock()
            open_url.side_effect = [urllib.error.HTTPError('https://example.com', code, 'retry', {'Retry-After': '0'}, io.BytesIO()), response]
            transport = Transport(attempts=2, interval=0)
            with patch.object(transport.gate, 'defer') as defer:
                self.assertEqual(transport.request('https://example.com', 'test'), b'ok')
                self.assertEqual(open_url.call_count, 2)
                defer.assert_called_once()

    @patch('src.fetch_transcripts.urllib.request.urlopen')
    def test_exhausted_retry_defers_shared_gate(self, open_url):
        for attempts in (1, 2):
            with self.subTest(attempts=attempts):
                errors = [urllib.error.HTTPError(
                    'https://example.com', 429, 'retry',
                    {'Retry-After': '120'}, io.BytesIO()) for _ in range(attempts)]
                open_url.reset_mock()
                open_url.side_effect = errors
                transport = Transport(attempts=attempts, interval=0)
                with patch.object(transport.gate, 'wait'), patch.object(transport.gate, 'defer') as defer:
                    with self.assertRaises(urllib.error.HTTPError) as raised:
                        transport.request('https://example.com', 'test')
                    self.assertIs(raised.exception, errors[-1])
                    self.assertEqual(open_url.call_count, attempts)
                    self.assertEqual(defer.call_args_list, [unittest.mock.call(120.0)] * attempts)

    @patch('src.fetch_transcripts.urllib.request.urlopen')
    def test_permanent_http_error(self, open_url):
        open_url.side_effect = urllib.error.HTTPError('https://example.com', 403, 'forbidden', {}, io.BytesIO())
        with self.assertRaises(urllib.error.HTTPError):
            Transport(interval=0).request('https://example.com', 'test')
        self.assertEqual(open_url.call_count, 1)

    def test_retry_after(self):
        self.assertEqual(retry_after('12'), 12)
        self.assertEqual(retry_after(None), 0)
        self.assertEqual(retry_after('bad'), 0)

    def test_manifest_and_failure_artifacts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            urls = root / 'urls.txt'
            urls.write_text('https://www.youtube.com/watch?v=9Q4qYeK5DTg\n')
            with patch('src.fetch_transcripts.Transport.request', side_effect=OSError('offline')):
                self.assertEqual(main(['--urls', str(urls), '--output', str(root / 'data')]), 1)
            manifest = json.loads((root / 'data/index.json').read_text())
            self.assertEqual(manifest['counts']['error'], 1)
            item = manifest['items'][0]
            self.assertTrue((root / 'data' / item['json_path']).exists())
            self.assertEqual((root / 'data' / item['text_path']).read_text(), '')


if __name__ == '__main__':
    unittest.main()
