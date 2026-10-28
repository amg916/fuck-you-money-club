import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from src.build_agent_report import (EvidenceIndex, generate, load_corpus, mentions,
                                     stamp, windows)
from src.fetch_transcripts import ROOT, fetch_video, patch_existing_corpus
from src.storyboard_fallbacks import FALLBACKS, apply_storyboard_fallback


class FallbackTests(unittest.TestCase):
    def test_known_missing_tracks(self):
        class Transport:
            def request(self, *args, **kwargs):
                return b'{"playabilityStatus":{"status":"OK"}}'
        for identity in FALLBACKS:
            result = fetch_video(1, 'https://www.youtube.com/watch?v=' + identity, Transport())
            self.assertEqual(result['status'], 'ok')
            self.assertEqual(result['client'], 'STORYBOARD_OCR')
            self.assertTrue(result['full_text'])
            self.assertFalse(result['provenance']['verbatim'])
            self.assertFalse(result['provenance']['time_aligned'])

    def test_network_failure_does_not_trigger_fallback(self):
        class Transport:
            def request(self, *args, **kwargs):
                raise OSError('offline')
        result = fetch_video(82, 'https://www.youtube.com/watch?v=bsbWDqAXsrE', Transport())
        self.assertEqual(result['status'], 'error')
        self.assertFalse(result['full_text'])

    def test_unknown_not_reconstructed(self):
        result = {'video_id': '9Q4qYeK5DTg'}
        self.assertFalse(apply_storyboard_fallback(result))
        self.assertEqual(result, {'video_id': '9Q4qYeK5DTg'})

    def test_real_captions_take_precedence(self):
        class Transport:
            def request(self, url, agent, payload=None):
                if payload:
                    return b'{"captions":{"playerCaptionsTracklistRenderer":{"captionTracks":[{"baseUrl":"https://example.com/captions"}]}}}'
                return b'<transcript><text start="1" dur="2">Actual captions</text></transcript>'
        result = fetch_video(82, 'https://www.youtube.com/watch?v=bsbWDqAXsrE', Transport())
        self.assertEqual(result['full_text'], 'Actual captions')
        self.assertNotEqual(result['client'], 'STORYBOARD_OCR')


class OrderingTests(unittest.TestCase):
    def test_case_variant_mentions(self):
        self.assertEqual(
            mentions('https://probatemastery.com https://ProbateMastery.com'),
            ['https://ProbateMastery.com', 'https://probatemastery.com'])

    def test_cross_seed_determinism(self):
        script = '''
import json
from src.build_agent_report import EvidenceIndex, build_manual, build_compendium, mentions
text = 'claim deadline https://probatemastery.com https://ProbateMastery.com'
video = {
    'index': 1, 'video_id': 'fixture', 'url': 'https://example.com',
    'metadata': {'title': 'Claim deadline'}, 'full_text': text,
    'segments': [{'start': 0, 'duration': 1, 'text': text}],
    'word_count': len(text.split()), 'digest': 'fixture',
}
index = EvidenceIndex([video])
print(json.dumps([mentions(text), build_manual(index), build_compendium(index)]))
'''
        outputs = [subprocess.check_output(
            [sys.executable, '-c', script], cwd=ROOT,
            env=dict(os.environ, PYTHONHASHSEED=str(seed)), text=True)
            for seed in (1, 2, 42, 123)]
        for output in outputs[1:]:
            self.assertEqual(output, outputs[0])


class ReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory()
        cls.root = Path(cls.temporary.name)
        cls.data = cls.root / 'data'
        shutil.copytree(ROOT / 'data', cls.data)
        patch_existing_corpus(cls.data)
        cls.videos = load_corpus(cls.data)
        cls.paths = generate(cls.data, cls.root, repair=False)
        cls.manual, cls.compendium = [p.read_text(encoding='utf-8') for p in cls.paths]

    @classmethod
    def tearDownClass(cls):
        cls.temporary.cleanup()

    def test_all_189_nonempty(self):
        self.assertEqual(len(self.videos), 189)
        for video in self.videos:
            self.assertEqual(video['status'], 'ok')
            self.assertTrue(video['full_text'].strip())
            self.assertTrue(video['segments'])

    def test_all_ids_urls_and_headings(self):
        for video in self.videos:
            self.assertIn(video['video_id'], self.compendium)
            self.assertIn(video['url'], self.compendium)
            self.assertIn('## [%03d]' % video['index'], self.compendium)
            self.assertIn('[%03d]' % video['index'], self.manual)

    def test_domains_and_depth(self):
        for domain in range(1, 9):
            self.assertIn('## Domain %d:' % domain, self.manual)
        self.assertGreaterEqual(len(self.manual.splitlines()), 1200)
        self.assertNotIn('\x00', self.manual + self.compendium)

    def test_idempotent_patch(self):
        before = (self.data / 'index.json').read_bytes()
        patch_existing_corpus(self.data)
        self.assertEqual(before, (self.data / 'index.json').read_bytes())

    def test_deterministic_reports(self):
        paths = generate(self.data, self.root / 'second', repair=False)
        self.assertEqual(self.manual, paths[0].read_text(encoding='utf-8'))
        self.assertEqual(self.compendium, paths[1].read_text(encoding='utf-8'))

    def test_every_segment_consumed(self):
        for video in self.videos:
            self.assertEqual(' '.join(w['text'] for w in windows(video)),
                             ' '.join(s['text'] for s in video['segments']))

    def test_invalid_manifest_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            (path / 'index.json').write_text(json.dumps({'items': []}))
            with self.assertRaises(ValueError):
                load_corpus(path)

    def test_reconstruction_has_no_fabricated_quote_timestamp(self):
        for identity in FALLBACKS:
            video = next(v for v in self.videos if v['video_id'] == identity)
            self.assertFalse(video['provenance']['time_aligned'])
        self.assertIn('no quote timestamp', self.compendium)
        for index in (82, 112, 179):
            for report in (self.manual, self.compendium):
                self.assertNotIn(f'[{index:03d}] 00:00:00', report)

    def test_tools_and_timestamps(self):
        self.assertEqual(stamp(3661.5), '01:01:01')
        found = mentions('Use Regrid and Neo4j at https://example.com/records.')
        self.assertIn('Regrid', found)
        self.assertIn('Neo4j', found)
        self.assertIn('https://example.com/records', found)


if __name__ == '__main__':
    unittest.main()
