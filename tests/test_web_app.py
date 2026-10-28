#!/usr/bin/env python3
"""Unit tests for the abridger engine, PDF writer and the stdlib HTTP app server."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import threading
import unittest
import urllib.error
import urllib.request

ROOT_DIR = Path(__file__).resolve().parents[1]
for _p in (str(ROOT_DIR), str(ROOT_DIR / "src")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from src import abridge_engine, app_server, pdf_generator
from unittest.mock import patch
from concurrent.futures import ThreadPoolExecutor
import copy
import io
import re
import time

CAPTION_ID, STORY_ID = "VID0000001A", "STORY00002B"
LINES = [
    "Never skip the verification step because the county deadline is strict and the statute controls.",
    "Always pull the recorded deed and verify the heir chain before you file the small estate affidavit.",
    "Pro tip: search FamilySearch and Ancestry first, then order the SS-5 form from the state archive.",
    "The filing fee is $435 and you have 30 days to request the court order under Probate Code 13101.",
    "Make sure you contact the holder, confirm the lien payoff, and review the quitclaim deed closely.",
]


def _segments(count=18):
    segments, start = [], 0.0
    for i in range(count):
        segments.append({"start": start, "duration": 9.0, "text": LINES[i % len(LINES)]})
        start += 9.0
    return segments


def build_fixture(root: Path) -> Path:
    (root / "transcripts").mkdir(parents=True, exist_ok=True)
    items = []
    for index, (vid, client) in enumerate(((CAPTION_ID, "web"), (STORY_ID, "STORYBOARD_OCR")), 1):
        segments = _segments()
        full_text = " ".join(s["text"] for s in segments)
        record = {"index": index, "video_id": vid, "status": "ok", "client": client,
                  "url": f"https://www.youtube.com/watch?v={vid}",
                  "full_text": full_text, "segments": segments,
                  "metadata": {"title": f"Probate Heir Deed Research Walkthrough {index}",
                               "author": "Field Operator", "lengthSeconds": str(len(segments) * 9),
                               "shortDescription": "Uses FamilySearch, PACER and Table of Heirship."}}
        if client == "STORYBOARD_OCR":
            record["provenance"] = {"time_aligned": False}
        base = root / "transcripts" / f"{index:03d}_{vid}"
        base.with_suffix(".json").write_text(json.dumps(record), encoding="utf-8")
        base.with_suffix(".txt").write_text(full_text + "\n", encoding="utf-8")
        items.append({"index": index, "video_id": vid, "url": record["url"]})
    (root / "index.json").write_text(json.dumps({"items": items, "counts": {"ok": len(items)}}),
                                     encoding="utf-8")
    return root


class ExtractUrlsTest(unittest.TestCase):
    def test_all_url_shapes_and_dedup(self):
        text = ("https://www.youtube.com/watch?v=aaaaaaaaaaa\n"
                "https://youtu.be/bbbbbbbbbbb\n"
                "https://www.youtube.com/shorts/ccccccccccc\n"
                "ddddddddddd\n"
                "https://www.youtube.com/watch?v=aaaaaaaaaaa\n")
        found = abridge_engine.extract_video_urls(text)
        self.assertEqual([vid for vid, _ in found],
                         ["a" * 11, "b" * 11, "c" * 11, "d" * 11])
        self.assertEqual(found[0][1], "https://www.youtube.com/watch?v=" + "a" * 11)
        self.assertEqual(abridge_engine.extract_video_urls(""), [])
        self.assertEqual(abridge_engine.extract_video_urls("hello world"), [])


class AbridgeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp())
        build_fixture(cls.tmp)
        cls.records = app_server.load_corpus(cls.tmp, expected=2)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_caption_record(self):
        out = abridge_engine.abridge_video(self.records[0])
        self.assertEqual(out["source_mode"], "caption")
        self.assertTrue(out["pro_tips"] and out["chapters"])
        self.assertTrue(out["finite_details"]["tactical_checklist"])
        self.assertIn("FamilySearch", out["finite_details"]["tools_and_portals"])
        self.assertTrue(out["finite_details"]["statutes_and_forms"])
        self.assertTrue(any(t["timestamp"].count(":") == 2 for t in out["pro_tips"]))
        self.assertIn("ProTips", out["markdown"])

    def test_storyboard_record(self):
        out = abridge_engine.abridge_video(self.records[1])
        self.assertEqual(out["source_mode"], "STORYBOARD_OCR")
        stamps = [t["timestamp"] for t in out["pro_tips"]] + [c["timestamp"] for c in out["chapters"]]
        self.assertTrue(stamps)
        self.assertTrue(all(s == "whole-video reconstruction" for s in stamps))
        self.assertNotIn("00:00:00", stamps)
        self.assertTrue(all(t["seconds"] == 0 for t in out["pro_tips"]))

    def test_combine_and_agent_report(self):
        abridged = [abridge_engine.abridge_video(r) for r in self.records]
        combined = abridge_engine.combine_videos(abridged, "My Playbook")
        self.assertEqual(combined["title"], "My Playbook")
        self.assertEqual(combined["video_count"], 2)
        self.assertTrue(combined["master_pro_tips"])
        self.assertIn("Master ProTips Vault", combined["markdown"])
        report = abridge_engine.build_custom_agent_report(
            self.records, {a["video_id"]: a for a in abridged}, prompt="deadline deed heir")
        self.assertEqual(report["title"], "Agent Operational Report")
        self.assertEqual(report["telemetry"]["videos_scanned"], 2)
        self.assertTrue(report["pro_tips"] and report["markdown"].startswith("# Agent"))


class PdfTest(unittest.TestCase):
    def _check(self, blob):
        self.assertTrue(blob.startswith(b"%PDF-1.4"))
        for marker in (b"xref", b"trailer", b"/Type /Font", b"/Helvetica-Bold", b"/Courier"):
            self.assertIn(marker, blob)
        self.assertTrue(blob.rstrip().endswith(b"%%EOF"))

    def test_render_pdf_bytes(self):
        blob = pdf_generator.render_pdf_bytes(
            "Report (A) \\ B", "Subtitle line",
            [("Videos", "2"), {"label": "ProTips", "value": 14}],
            [{"heading": "Section", "level": 2, "body": ["Prose."],
              "bullets": ["first", "second"], "pro_tips": ["never skip verification"],
              "code": ["| a | b |"]}])
        self._check(blob)
        self.assertIn(b"Report \\(A\\) \\\\ B", blob)
        self.assertIn(b"Page 1 of", blob)

    def test_markdown_pagination(self):
        markdown = "# Agent Report\n\n_Lede line_\n\n## Vault\n\n" + "\n".join(
            f"- Bullet {i} with enough wording to wrap across the full printable page width."
            for i in range(150))
        blob = pdf_generator.markdown_to_pdf_bytes(markdown, telemetry=["Videos: 2"])
        self._check(blob)
        self.assertGreaterEqual(blob.count(b"/Type /Page "), 2)
        self.assertIn(b"Page 2 of", blob)
        self.assertIn(b"Agent Report", blob)


class ServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp())
        build_fixture(cls.tmp)
        cls.server = app_server.create_server("127.0.0.1", 0, cls.tmp)
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def _call(self, path, payload=None, raw=False):
        url = f"http://127.0.0.1:{self.port}{path}"
        data = json.dumps(payload).encode("utf-8") if payload is not None else None
        request = urllib.request.Request(url, data=data,
                                        headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                body = response.read()
                return response.status, (body if raw else json.loads(body.decode("utf-8")))
        except urllib.error.HTTPError as exc:
            return exc.code, json.loads(exc.read().decode("utf-8"))

    def test_app_state(self):
        state = self.server.state
        self.assertEqual(len(state.abridged_list), 2)
        self.assertEqual(set(state.abridged_by_id), {CAPTION_ID, STORY_ID})
        self.assertEqual(state.totals()["total"], 2)
        self.assertEqual(len(state.resolve("all")), 2)
        self.assertEqual([v["video_id"] for v in state.resolve([STORY_ID])], [STORY_ID])
        self.assertTrue(state.search(query="familysearch"))
        self.assertEqual(state.search(query="zzzznotpresent"), [])

    def test_read_endpoints(self):
        status, health = self._call("/api/health")
        self.assertEqual((status, health["status"], health["total_videos"]), (200, "ok", 2))
        status, listing = self._call("/api/videos")
        self.assertEqual(status, 200)
        self.assertEqual(len(listing["videos"]), 2)
        self.assertTrue(listing["domains"])
        self.assertNotIn("markdown", listing["videos"][0])
        status, detail = self._call(f"/api/videos/{CAPTION_ID}")
        self.assertEqual((status, detail["video_id"]), (200, CAPTION_ID))
        self.assertTrue(detail["segments"] and detail["full_text"])
        self.assertEqual(self._call("/api/videos/nope")[0], 404)

    def test_write_endpoints(self):
        status, body = self._call("/api/ingest", {"urls": "hello world"})
        self.assertEqual(status, 400)
        self.assertIn("no valid YouTube", body["error"])
        status, body = self._call("/api/ingest",
                                  {"urls": [f"https://www.youtube.com/watch?v={CAPTION_ID}"]})
        self.assertEqual((status, body["cached_count"], body["ingested_count"]), (200, 1, 0))
        status, body = self._call("/api/combine", {"title": "Combo"})
        self.assertEqual((status, body["video_count"], body["title"]), (200, 2, "Combo"))
        self.assertEqual(self._call("/api/combine", {"video_ids": []})[0], 400)
        status, body = self._call("/api/agent-report", {"prompt": "heir deed deadline"})
        self.assertEqual(status, 200)
        self.assertTrue(body["markdown"] and body["telemetry"]["videos_matched"] >= 1)

    def test_pdf_endpoints(self):
        status, blob = self._call(f"/api/report/pdf?mode=single&video_id={CAPTION_ID}", raw=True)
        self.assertEqual(status, 200)
        self.assertTrue(blob.startswith(b"%PDF-1.4") and blob.rstrip().endswith(b"%%EOF"))
        status, blob = self._call("/api/report/pdf",
                                  {"mode": "combine", "video_ids": [CAPTION_ID, STORY_ID]}, raw=True)
        self.assertEqual(status, 200)
        self.assertIn(b"xref", blob)
        status, blob = self._call("/api/report/pdf",
                                  {"markdown": "# Custom\n\n- one\n- two\n", "title": "Custom"},
                                  raw=True)
        self.assertEqual(status, 200)
        self.assertIn(b"trailer", blob)
        self.assertEqual(self._call("/api/report/pdf?mode=single&video_id=nope")[0], 404)


class AuditRegressionTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = build_fixture(Path(self.temp.name))
        self.state = app_server.AppState(self.root)

    def test_url_boundaries(self):
        for prefix in ('https://youtube.com/watch?v=', 'https://youtu.be/',
                       'https://youtube.com/embed/', 'https://youtube.com/shorts/',
                       'https://youtube.com/v/', ''):
            with self.subTest(prefix=prefix):
                self.assertEqual(abridge_engine.extract_video_urls(prefix + 'a' * 12), [])
                self.assertEqual(len(abridge_engine.extract_video_urls(prefix + 'a' * 11)), 1)

    def test_short_chapters(self):
        for count in range(4):
            wins = [('Unique chapter ' + str(i), i * 75) for i in range(count)]
            with patch.object(abridge_engine, '_video_windows', return_value=wins):
                chapters = abridge_engine.abridge_video(self.state.raw_videos[0])['chapters']
            self.assertEqual(len(chapters), count)
            self.assertEqual([c['timestamp'] for c in chapters],
                             [abridge_engine.stamp(i * 75) for i in range(count)])

    def test_index_scope_and_sanitized_passages(self):
        for ids, expected in ((None, 2), ([], 0), ([CAPTION_ID], 1), (['missing'], 0)):
            report = abridge_engine.build_custom_agent_report(
                'deed deadline', records=self.state.raw_videos, video_ids=ids,
                index=self.state.evidence_index, max_passages=3)
            self.assertEqual(report['matched_video_count'], expected)
            self.assertLessEqual(len(report['evidence_passages']), 3)
            json.dumps(report)
            self.assertNotIn('#None', report['markdown'])
            for p in report['evidence_passages']:
                self.assertEqual(set(p), {'video_id', 'index', 'title', 'url', 'domain',
                                         'domain_name', 'start', 'timestamp', 'timestamp_url',
                                         'score', 'matched_terms', 'excerpt'})
                if ids is not None:
                    self.assertIn(p['video_id'], ids)
        self.assertEqual(self.state.evidence_index.search('deed', allowed_video_ids=[]), [])

    def test_concurrent_ingestion_and_live_index(self):
        record = copy.deepcopy(self.state.raw_videos[0])
        vid = 'NEW0000001A'
        record.update(video_id=vid, url='https://www.youtube.com/watch?v=' + vid)
        barrier = threading.Barrier(2)
        def fetch(*args):
            barrier.wait(timeout=5)
            return copy.deepcopy(record)
        with patch.object(app_server, 'fetch_video', side_effect=fetch):
            with ThreadPoolExecutor(max_workers=2) as pool:
                results = list(pool.map(self.state.ingest_urls, [vid, vid]))
        self.assertEqual(sum(r['ingested_count'] for r in results), 1)
        self.assertEqual(sum(r['cached_count'] for r in results), 1)
        self.assertEqual(len(self.state.raw_videos), 3)
        self.assertIn('## #3', self.state.abridged_by_id[vid]['markdown'])
        self.assertTrue(self.state.evidence_index.search('deed', allowed_video_ids=[vid]))
        self.assertEqual(len(app_server.AppState(self.root).raw_videos), 3)

    def test_storage_failure_is_not_success(self):
        record = copy.deepcopy(self.state.raw_videos[0])
        with patch.object(app_server, 'fetch_video', return_value=record), \
                patch.object(app_server, 'atomic_write', side_effect=OSError('disk full')):
            result = self.state.ingest_urls('NEW0000002A')
        self.assertEqual((result['ingested_count'], result['failed_count']), (0, 1))
        self.assertEqual(len(self.state.raw_videos), 2)

    def test_load_malformed_and_custom_shapes(self):
        (self.root / 'transcripts' / 'bad.json').write_text('[null, 3]')
        record = copy.deepcopy(self.state.raw_videos[0])
        record['video_id'] = 'NEW0000003A'
        for data in ([None, 3, {}, record], {'videos': [False, record]}):
            (self.root / 'custom_videos.json').write_text(json.dumps(data))
            self.assertEqual(len(app_server.AppState(self.root).raw_videos), 3)

    def test_pdf_info_is_indirect(self):
        blob = pdf_generator.markdown_to_pdf_bytes('# Test\n\nbody')
        match = re.search(rb'/Info (\d+) 0 R', blob)
        self.assertIsNotNone(match)
        self.assertIn(match[1] + b' 0 obj\n<< /Title', blob)
        self.assertIn(b'/CreationDate (D:', blob)

    def test_code_order_indentation_and_long_lines(self):
        code = '    ' + 'x' * 250
        table = '| ' + 'y' * 250 + ' |'
        blocks = pdf_generator._markdown_blocks('before prose\n```\n' + code + '\n```\nafter prose\n\n' + table)
        self.assertEqual(blocks[0]['body'], ['before prose'])
        self.assertEqual(blocks[1]['code'], [code])
        self.assertEqual(blocks[2]['body'], ['after prose'])
        self.assertEqual(blocks[3]['code'], [table])
        lines = pdf_generator.wrap(code, 8.6, 480, mono=True)
        self.assertGreater(len(lines), 1)
        self.assertEqual(''.join(lines), code)
        self.assertTrue(lines[0].startswith('    '))

    def test_linear_wrap_and_font_widths(self):
        durations = []
        for _ in range(5):
            start = time.perf_counter()
            lines = pdf_generator.wrap('W' * 2000, 10, 500)
            durations.append(time.perf_counter() - start)
        self.assertEqual(''.join(lines), 'W' * 2000)
        self.assertLess(min(durations), 0.005)
        self.assertAlmostEqual(pdf_generator.text_width('ABmw', 10, font='F2'), 31.11)
        self.assertEqual(pdf_generator.text_width('ABmw', 10, font='F3'), 24)
        for line in pdf_generator.wrap('Wm' * 38, 22, pdf_generator.BODY_W, font='bold'):
            self.assertLessEqual(pdf_generator.text_width(line, 22, font='bold'), pdf_generator.BODY_W)

    def test_bad_bodies(self):
        handler_type = app_server.create_handler(self.state)
        self.assertEqual(handler_type.timeout, 15)
        for raw, length in ((b'{', '1'), (b'[]', '2'), (b'null', '4'), (b'\xff', '1'),
                            (b'{}', '-1'), (b'{}', '3'), (b'', str(app_server.MAX_BODY_BYTES + 1)),
                            (b'', 'nope')):
            handler = handler_type.__new__(handler_type)
            from email.message import Message
            handler.headers = Message()
            handler.headers['Content-Length'] = length
            handler.rfile = io.BytesIO(raw)
            with self.assertRaises(app_server.BadRequestError):
                handler._body()


class InvalidRequestTest(ServerTest):
    def test_wrong_types_are_400(self):
        cases = [('/api/ingest', {'urls': 3}), ('/api/ingest', {'urls': [3]}),
                 ('/api/combine', {'video_ids': 'all'}), ('/api/combine', {'video_ids': [3]}),
                 ('/api/combine', {'title': {}}), ('/api/agent-report', {'prompt': []}),
                 ('/api/agent-report', {'video_ids': False}), ('/api/report/pdf', {'mode': []}),
                 ('/api/report/pdf', {'mode': 'wrong'}), ('/api/report/pdf', {'subtitle': 4})]
        for path, payload in cases:
            with self.subTest(path=path, payload=payload):
                self.assertEqual(self._call(path, payload)[0], 400)
        status, report = self._call('/api/agent-report', {'prompt': 'deed', 'video_ids': []})
        self.assertEqual((status, report['matched_video_count']), (200, 0))

    def test_malformed_json_returns_400(self):
        for body in (b'{', b'[]', b'null', b'\xff'):
            request = urllib.request.Request(f'http://127.0.0.1:{self.port}/api/combine', data=body)
            with self.assertRaises(urllib.error.HTTPError) as caught:
                urllib.request.urlopen(request, timeout=5)
            self.assertEqual(caught.exception.code, 400)
            caught.exception.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
