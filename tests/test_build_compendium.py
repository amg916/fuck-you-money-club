import json
from pathlib import Path
import tempfile
import unittest

from src.build_compendium import build, classify, md, mentions, render


class CompendiumTests(unittest.TestCase):
    def record(self):
        return {'index': 1, 'video_id': 'example', 'status': 'ok', 'client': 'IOS',
                'url': 'https://www.youtube.com/watch?v=example',
                'metadata': {'title': 'Regrid parcel API tutorial', 'author': 'Regrid',
                             'lengthSeconds': '3661', 'keywords': ['GIS'],
                             'shortDescription': 'Download parcel data.'},
                'full_text': 'Select a parcel. Download GeoJSON. Check the APN.',
                'segments': [{'start': i * 65, 'duration': 5, 'text': text}
                             for i, text in enumerate(('Select a parcel.', 'Download GeoJSON.',
                                                       'Check the APN.'))]}

    def test_classification_and_mentions(self):
        self.assertEqual(classify(self.record()), 5)
        self.assertIn('GeoJSON', mentions(self.record()['full_text']))
        self.assertNotIn('will', mentions('willing'))
        self.assertNotIn('GIS', mentions('registration'))

    def test_render_metadata_and_timestamps(self):
        result = render(self.record(), 5)
        for expected in ('### [#001]', '01:01:01 (3661 seconds)', '[00:00]',
                         '[01:05]', '[02:10]', '**Word Count:** 8', '**Segment Count:** 3'):
            self.assertIn(expected, result)
        self.assertEqual(md('A|B <tag>'), 'A\\|B &lt;tag&gt;')

    def test_storyboard_has_no_quote_timestamps(self):
        record = self.record()
        record['client'] = 'STORYBOARD_OCR'
        record['segments'] = [{'start': 0, 'duration': 3661, 'text': record['full_text'],
                               'timing': 'whole_video_coverage_not_quote_timestamp'}]
        result = render(record, 5)
        self.assertEqual(result.count('[whole-video]'), 3)
        self.assertNotIn('[00:00]', result)
        self.assertIn('not verbatim or time-aligned', result)

    def test_build_and_identity_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            record = self.record()
            (root / 'video.json').write_text(json.dumps(record))
            manifest = {'items': [{'index': 1, 'video_id': 'example', 'json_path': 'video.json'}]}
            (root / 'index.json').write_text(json.dumps(manifest))
            output = root / 'report.md'
            self.assertEqual(build(root, output), 1)
            before = output.read_bytes()
            self.assertIn(b'[001](#video-001)', before)
            build(root, output)
            self.assertEqual(output.read_bytes(), before)
            record['video_id'] = 'mismatch'
            (root / 'video.json').write_text(json.dumps(record))
            with self.assertRaises(ValueError):
                build(root, output)
            self.assertEqual(output.read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
