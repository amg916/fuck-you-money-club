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


class PublishingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from src import ebook_publisher, topic_discovery
        cls.publisher, cls.discovery = ebook_publisher, topic_discovery
        cls.temp = tempfile.TemporaryDirectory()
        cls.state = app_server.AppState(build_fixture(Path(cls.temp.name)))
        cls.book = ebook_publisher.build_full_ebook(cls.state.abridged_list, ['Probate & Heir Research'])

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_topic_parsing_and_expansion(self):
        d = self.discovery
        self.assertEqual(d.parse_topics(' Probate,heirs;probate\n deed '), ['Probate', 'heirs', 'deed'])
        self.assertEqual(d.parse_topics(['Probate', 'Probate', ' ']), ['Probate'])
        self.assertEqual(len(d.expand_topic_queries(['probate'])['queries']), 10)
        with self.assertRaises(ValueError):
            d.parse_topics([3])
        with patch.object(d.os, 'access', return_value=False):
            self.assertEqual(d.expand_topic_queries(['probate'], True)['engine'], 'practitioner_multi_angle')
        import subprocess
        with patch.object(d.os, 'access', return_value=True), patch.object(d.subprocess, 'run', side_effect=subprocess.TimeoutExpired('codex', 1)):
            self.assertEqual(d.expand_topic_queries(['probate'], True)['engine'], 'practitioner_multi_angle')
        with patch.object(d.os, 'access', return_value=True), patch.object(d.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, '["probate expert docket investigation"]')):
            self.assertEqual(d.expand_topic_queries(['probate'], True)['engine'], 'chatgpt_pro_codex+practitioner')

    def test_search_tree_and_filtering(self):
        def renderer(vid, duration):
            return {'videoRenderer': {'videoId': vid, 'title': {'runs': [{'text': 'Probate '}, {'text': 'Walkthrough'}]},
                    'ownerText': {'runs': [{'text': 'Researcher'}]}, 'lengthText': {'simpleText': duration},
                    'viewCountText': {'simpleText': '1,000 views'},
                    'detailedMetadataSnippets': [{'snippetText': {'runs': [{'text': 'Court portal tutorial'}]}}]}}
        tree = {'nested': [renderer(CAPTION_ID, '24:03'), renderer('SHORT00001A', '0:30'),
                           renderer('LIVE000001A', ''), renderer(CAPTION_ID, '24:03'), renderer(STORY_ID, '1:02:03')]}
        def transport(request, timeout):
            payload = json.loads(request.data)
            self.assertEqual(payload['context']['client']['clientVersion'], '2.20250201.00.00')
            self.assertEqual(request.get_method(), 'POST')
            return tree
        videos = self.discovery.search_youtube_query('probate', transport=transport)
        self.assertEqual(len(videos), 2)
        self.assertEqual(videos[0]['length_seconds'], 1443)
        self.assertEqual(videos[1]['length_seconds'], 3723)
        self.assertEqual(videos[0]['author'], 'Researcher')
        self.assertEqual(videos[0]['snippet'], 'Court portal tutorial')
        self.assertEqual(len(self.discovery.search_youtube_query('probate', transport=transport, max_results=1)), 1)

    def test_offline_fallback_and_ingest(self):
        d = self.discovery
        def offline(*args, **kwargs):
            raise OSError('offline')
        out = d.discover_topic_videos('probate', self.state, search_fn=offline)
        self.assertEqual(out['matched_corpus_count'], 2)
        self.assertEqual(out['search_failed_count'], 10)
        self.assertEqual(len(out['video_ids']), 2)
        self.assertTrue(d.discover_topic_videos('unrelated astronomy', self.state, search_fn=offline)['fallback_used'])
        with self.assertRaises(ValueError):
            d.discover_topic_videos('', self.state, search_fn=offline)
        vid = 'NEW0000099A'
        candidate = {'video_id': vid, 'title': 'Probate advanced tutorial', 'length_seconds': 900}
        def ingest(urls):
            self.assertEqual(urls, ['https://www.youtube.com/watch?v=' + vid])
            self.state.abridged_by_id[vid] = dict(self.state.abridged_list[0], video_id=vid)
            return {'ingested_count': 1, 'cached_count': 0, 'failed_count': 0}
        try:
            with patch.object(self.state, 'ingest_urls', side_effect=ingest) as mocked:
                result = d.discover_topic_videos('probate', self.state, search_fn=lambda *a, **kw: [candidate, candidate])
            self.assertEqual(mocked.call_count, 1)
            self.assertEqual(result['ingested_count'], 1)
            self.assertIn(vid, result['video_ids'])
        finally:
            self.state.abridged_by_id.pop(vid, None)

    def test_book_and_marketplace_contracts(self):
        book = self.book
        json.dumps(book)
        self.assertEqual(len(book['chapters']), 5)
        self.assertEqual(len(book['exhibits']), 6)
        self.assertEqual(len(book['mockup_svgs']), 5)
        for chapter in book['chapters']:
            self.assertTrue(chapter['sections'] and chapter['exhibits'] and chapter['checklist'])
        kit = book['marketplace_kit']
        self.assertEqual(len(kit['amazon_kdp']['backend_keywords']), 7)
        self.assertTrue(all(len(k) <= 50 for k in kit['amazon_kdp']['backend_keywords']))
        self.assertEqual(len(kit['etsy']['tags']), 13)
        self.assertTrue(all(len(t) <= 20 for t in kit['etsy']['tags']))
        self.assertLessEqual(len(kit['etsy']['title']), 140)
        self.assertLessEqual(len(kit['ebay']['title']), 80)
        isbn = book['book_spec']['isbn_placeholder']
        self.assertRegex(isbn, r'^978\d{10}$')
        self.assertEqual(sum(int(n)*(1 if i % 2 == 0 else 3) for i, n in enumerate(isbn)) % 10, 0)
        self.assertIn('ISBN-13', book['book_spec']['isbn_status'])
        self.assertEqual(book['publication_notice'], self.publisher.EDITION_SUMMARY)
        self.assertEqual(kit['amazon_kdp']['pricing_recommendation'], 'Kindle eBook: $9.99 | KDP Print Paperback (6x9): $24.99')
        self.assertEqual(kit['ebay']['pricing_recommendation'], 'Buy It Now: $14.99 (Collector Illustrated Playbook + Printable Workbook)')
        self.assertTrue(all(s['status'] == 'Verified Transcript Citation' for s in book['statutes']))
        self.assertTrue(all(p['status'] == 'Primary Operational Portal' for p in book['portals']))
        for exhibit in book['exhibits']:
            self.assertEqual(exhibit['image_provenance'], 'YouTube Frame & Vector Evidence Diagram')
            self.assertIn(' Key Portals & Tools: ', exhibit['caption'])
            self.assertIn('. Statutory & Form Citations: ', exhibit['caption'])
            self.assertNotIn('Editorial reconstruction', exhibit['caption'])
            self.assertIn('VISUAL EVIDENCE EXHIBIT', exhibit['svg_markup'])
        for exhibit in book['exhibits']:
            if exhibit['video_id'] == STORY_ID:
                self.assertEqual(exhibit['timestamp'], 'whole-video reconstruction')
                self.assertNotIn('&t=', exhibit['url'])
        with self.assertRaises(ValueError):
            self.publisher.build_full_ebook([])
        with patch.object(self.state, 'discover_topics', return_value={'video_ids': [CAPTION_ID]}) as discover:
            book = self.state.generate_ebook(topics='probate', discover_first=True)
        discover.assert_called_once()
        self.assertEqual(book['telemetry']['video_count'], 1)
        self.assertIs(self.state.last_ebook, book)
        with self.assertRaises(ValueError):
            self.state.generate_ebook(video_ids=[])
        self.assertEqual(self.state.generate_ebook(max_videos=1)['telemetry']['video_count'], 1)
        self.assertEqual(self.state.generate_ebook(video_ids=[CAPTION_ID, STORY_ID], max_videos=1)['telemetry']['video_count'], 1)
        self.assertEqual(self.state.generate_ebook(video_ids=[CAPTION_ID]*30)['telemetry']['video_count'], 1)

    def test_custom_video_nullable_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            record = {'video_id': 'NULL000001A', 'segments': _segments(),
                      'metadata': {'title': 'Nullable metadata', 'author': None,
                                   'shortDescription': None, 'lengthSeconds': 162}}
            (root / 'custom_videos.json').write_text(json.dumps([record]), encoding='utf-8')
            state = app_server.AppState(root)
            self.assertIn(record['video_id'], state.abridged_by_id)
            meta = state.raw_by_id[record['video_id']]['metadata']
            self.assertEqual(meta['shortDescription'], '')
            self.assertEqual(meta['author'], '')
            self.assertEqual(meta['lengthSeconds'], '162')

    def test_jpeg_svg_and_real_qr_structure(self):
        import base64
        import xml.etree.ElementTree as ET
        p = self.publisher
        for svg in [self.book['cover_svg'], *self.book['mockup_svgs'].values()]:
            ET.fromstring(svg)
        for e in self.book['exhibits']:
            jpeg = base64.b64decode(e['jpeg_base64'])
            self.assertTrue(jpeg.startswith(b'\xff\xd8\xff') and jpeg.endswith(b'\xff\xd9'))
            self.assertEqual(pdf_generator._jpeg_dimensions(jpeg), (480, 272))
            self.assertIn(b'\xff\xc0', jpeg)
            ET.fromstring(e['svg_markup'])
            matrix = e['qr_matrix']
            self.assertEqual(len(matrix), 33)
            self.assertTrue(all(len(row) == 33 and set(row) <= {0, 1} for row in matrix))
            self.assertEqual(matrix[0][:7], [1]*7)
            self.assertEqual(matrix[1][:7], [1, 0, 0, 0, 0, 0, 1])
            self.assertEqual(matrix, p.qr_matrix(e['url']))
        with patch.object(p.urllib.request, 'urlopen', side_effect=OSError('offline')):
            exhibits = p.build_visual_evidence_exhibits(self.state.abridged_list, self.book['book_spec'], True)
        self.assertTrue(all(e['jpeg_bytes'].startswith(b'\xff\xd8') for e in exhibits))
        for candidate in (b'\xff\xd8\xff\xc0\x00\x11\xff\xd9',
                          b'\xff\xd8\xff\xc0\x00\x11\x08\x00\x00\x00\x00\xff\xd9',
                          bytes.fromhex('ffd8ffc00011080001ffd9')):
            with self.subTest(candidate=candidate):
                with patch.object(p.urllib.request, 'urlopen') as urlopen:
                    urlopen.return_value.__enter__.return_value.read.return_value = candidate
                    exhibits = p.build_visual_evidence_exhibits(
                        self.state.abridged_list, self.book['book_spec'], fetch_thumbnails=True)
                self.assertTrue(exhibits)
                for exhibit in exhibits:
                    self.assertNotEqual(exhibit['jpeg_bytes'], candidate)
                    self.assertEqual(pdf_generator._jpeg_dimensions(exhibit['jpeg_bytes']), (480, 272))
                with self.assertRaises(ValueError):
                    pdf_generator._jpeg_dimensions(candidate)

    def test_illustrated_pdf_modes_and_xref(self):
        for mode, box in [('8.5x11', b'[0 0 612 792]'), ('6x9', b'[0 0 432 648]'), ('workbook', b'[0 0 612 792]')]:
            blob = self.publisher.render_ebook_pdf_bytes(self.book, mode)
            for marker in [b'%PDF-1.4', b'/Subtype /Image', b'/Filter /DCTDecode', b'/Subtype /Link',
                           b'/Annots [', b'/S /URI', b'/Im1 Do', b'Page 1 of', box]:
                self.assertIn(marker, blob)
            start = int(re.search(rb'startxref\n(\d+)', blob)[1])
            self.assertEqual(blob[start:start+4], b'xref')
            entries = blob[start:].splitlines()[3:]
            for number, entry in enumerate(entries, 1):
                if entry == b'trailer':
                    break
                offset = int(entry[:10])
                self.assertTrue(blob[offset:].startswith(f'{number} 0 obj'.encode()))
            if mode == '6x9':
                self.assertIn(b'1 0 0 1 58.00', blob)
                self.assertIn(b'1 0 0 1 40.00', blob)
            if mode == 'workbook':
                self.assertIn(b'Finding:', blob)
        with self.assertRaises(ValueError):
            self.publisher.render_ebook_pdf_bytes(self.book, 'bad')

    def test_long_title_fits_6x9_cover(self):
        book = self.publisher.build_full_ebook(
            self.state.abridged_list, custom_title='Research Methods and Field Practice ' * 8)
        with patch.object(pdf_generator, '_text', wraps=pdf_generator._text) as text:
            blob = self.publisher.render_ebook_pdf_bytes(book, '6x9')
        self.assertTrue(blob.startswith(b'%PDF-1.4'))
        calls = [call.args for call in text.call_args_list]
        toc = next(i for i, args in enumerate(calls) if args[2] == 'Table of Contents')
        cover = calls[:toc]
        self.assertEqual(sum(args[4] == 23 for args in cover), 5)
        self.assertLessEqual(sum(args[4] == 11 for args in cover), 3)
        self.assertTrue(all(args[0] == 58 for args in cover))
        self.assertTrue(all(65 + args[4] <= args[1] < 648 for args in cover))
        self.assertTrue(all(a[1] > b[1] for a, b in zip(cover, cover[1:])))
        for label in book['telemetry']:
            self.assertTrue(any(args[2].startswith(label.replace('_', ' ').upper() + ':') for args in cover))

    def test_custom_title_epub_xml_cleaning(self):
        import zipfile
        import xml.etree.ElementTree as ET
        auto_spec = self.publisher.auto_design_book_spec(None, self.state.abridged_list)
        for custom_title in ('\x01', '   '):
            with self.subTest(custom_title=custom_title):
                book = self.publisher.build_full_ebook(
                    self.state.abridged_list, custom_title=custom_title)
                self.assertTrue(book['title'].strip())
                self.assertEqual(book['title'], auto_spec['title'])
                self.assertEqual(book['book_spec']['title'], auto_spec['title'])
                self.assertEqual(book['book_spec']['isbn_placeholder'], auto_spec['isbn_placeholder'])
        book = self.publisher.build_full_ebook(
            self.state.abridged_list, custom_title='Broken' + chr(1) + 'Title')
        self.assertEqual(book['title'], 'BrokenTitle')
        self.assertEqual(book['book_spec']['title'], 'BrokenTitle')
        blob = self.publisher.render_ebook_epub_bytes(book)
        with zipfile.ZipFile(io.BytesIO(blob)) as archive:
            for name in archive.namelist():
                if name.endswith(('.xml', '.opf', '.xhtml', '.ncx', '.svg')):
                    ET.fromstring(archive.read(name))

    def test_epub_structure_xml_manifest_and_links(self):
        import zipfile
        import xml.etree.ElementTree as ET
        import posixpath
        blob = self.publisher.render_ebook_epub_bytes(self.book)
        with zipfile.ZipFile(io.BytesIO(blob)) as archive:
            self.assertEqual(archive.namelist()[0], 'mimetype')
            self.assertEqual(archive.getinfo('mimetype').compress_type, zipfile.ZIP_STORED)
            self.assertEqual(archive.read('mimetype'), b'application/epub+zip')
            self.assertIsNone(archive.testzip())
            opf = ET.fromstring(archive.read('OEBPS/content.opf'))
            self.assertEqual(opf.attrib['version'], '3.0')
            ns = {'o': 'http://www.idpf.org/2007/opf'}
            manifest = opf.find('o:manifest', ns)
            ids = {item.attrib['id'] for item in manifest}
            for item in manifest:
                self.assertIn('OEBPS/' + item.attrib['href'], archive.namelist())
            for item in opf.find('o:spine', ns):
                self.assertIn(item.attrib['idref'], ids)
            for name in archive.namelist():
                if name.endswith(('.xml', '.opf', '.xhtml', '.ncx', '.svg')):
                    root = ET.fromstring(archive.read(name))
                    if name.endswith('.xhtml'):
                        for node in root.iter():
                            for attr in ('src', 'href'):
                                link = node.get(attr)
                                if link and not link.startswith(('http:', 'https:', '#')):
                                    self.assertIn(posixpath.normpath(posixpath.join(posixpath.dirname(name), link)), archive.namelist())
            self.assertIn(b'&amp;t=', archive.read('OEBPS/chapter_3.xhtml'))

    def test_marketplace_bundle(self):
        import zipfile
        blob = self.publisher.render_marketplace_bundle_zip(self.book)
        with zipfile.ZipFile(io.BytesIO(blob)) as archive:
            self.assertIsNone(archive.testzip())
            names = archive.namelist()
            self.assertIn('01-Amazon-KDP/Amazon-Kindle-Edition.epub', names)
            self.assertIn('01-Amazon-KDP/Amazon-KDP-Print-Paperback-6x9.pdf', names)
            self.assertIn('02-Etsy-Digital-Product-Bundle/Printable-Action-Workbook-8.5x11.pdf', names)
            self.assertIn('03-eBay-Listing-Bundle/ebay-listing-template.html', names)
            self.assertIn('04-Source-Manuscript-and-Evidence/manuscript.md', names)
            self.assertEqual(sum('/Mockups/' in n for n in names), 5)
            self.assertNotIn('READ-BEFORE-PUBLISHING.txt', names)
            for name in names:
                if name.endswith('.json'):
                    json.loads(archive.read(name))
                if name.endswith('.pdf'):
                    self.assertIn(b'/Subtype /Image', archive.read(name))


class PublishingServerTest(ServerTest):
    def test_ebook_generate_empty_video_ids(self):
        status, body = self._call('/api/ebook/generate?video_ids=')
        self.assertEqual(status, 400)

    def test_favicon(self):
        status, body = self._call('/favicon.ico', raw=True)
        self.assertEqual(status, 200)
        self.assertIn(b'<svg', body)

    def test_all_publishing_routes_get_and_post(self):
        from src import topic_discovery
        with patch.object(topic_discovery, 'search_youtube_query', return_value=[]):
            for payload, suffix in [({'topics': 'probate', 'auto_ingest': False}, ''), (None, '?topics=probate&auto_ingest=false')]:
                status, data = self._call('/api/topic-discover' + suffix, payload)
                self.assertEqual(status, 200)
                self.assertEqual(len(data['video_ids']), 2)
                self.assertEqual(len(data['videos']), 2)
            for payload, suffix in [({'topics': 'probate', 'discover_first': True}, ''), (None, '?topics=probate')]:
                status, book = self._call('/api/ebook/generate' + suffix, payload)
                self.assertEqual(status, 200)
                self.assertEqual(len(book['chapters']), 5)
        for route, signature in [('pdf', b'%PDF-1.4'), ('epub', b'PK'), ('bundle', b'PK')]:
            for payload in (None, {'video_ids': [CAPTION_ID]}):
                status, data = self._call('/api/ebook/' + route, payload, raw=True)
                self.assertEqual(status, 200)
                self.assertTrue(data.startswith(signature))
        for mode in ('6x9', 'workbook'):
            status, data = self._call('/api/ebook/pdf?trim=' + mode, raw=True)
            self.assertEqual(status, 200)
            self.assertIn(b'/Subtype /Link', data)
        with urllib.request.urlopen(f'http://127.0.0.1:{self.port}/api/ebook/epub') as response:
            self.assertEqual(response.headers['Content-Type'], 'application/epub+zip')
            self.assertIn('illustrated-ebook-kindle.epub', response.headers['Content-Disposition'])

    def test_publishing_invalid_parameters(self):
        for payload in ({'topics': 3}, {'topics': [False]}, {'trim': []}, {'pdf_mode': 'a4'},
                        {'discover_first': 'true'}, {'auto_ingest': 1}, {'use_codex_cli': None},
                        {'max_videos': True}, {'max_videos': 0}, {'max_videos': 101}, {'video_ids': []}):
            self.assertEqual(self._call('/api/ebook/generate', payload)[0], 400)
        self.assertEqual(self._call('/api/topic-discover', {'topics': ''})[0], 400)
        for query in ('max_videos=x', 'auto_ingest=yes', 'trim=invalid'):
            self.assertEqual(self._call('/api/ebook/pdf?' + query)[0], 400)

    def test_studio_controls_and_legacy_ids(self):
        status, body = self._call('/', raw=True)
        self.assertEqual(status, 200)
        for ident in ('ingest-panel', 'tab-library', 'tab-combine', 'tab-agent', 'view-library',
                      'view-combine', 'view-agent', 'tab-ebook', 'view-ebook', 'ebook-body',
                      'ebook-topics-input', 'ebook-topic-presets', 'ebook-discover-youtube',
                      'ebook-use-chatgpt-pro', 'btn-build-autonomous-ebook', 'btn-discover-topics-only',
                      'btn-open-ebook-studio', 'ebook-download-bar', 'btn-download-ebook-bundle',
                      'btn-download-ebook-pdf-digital', 'btn-download-ebook-pdf-kdp',
                      'btn-download-ebook-epub', 'btn-download-ebook-workbook'):
            self.assertEqual(body.count(('id="' + ident + '"').encode()), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
