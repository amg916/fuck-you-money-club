"""FYMC platform acceptance tests (Python 3.9+, standard library only).

Run with: python -m unittest tests.test_fymc_platform -v
Imports and server startup are deferred until test execution. Required public
functions are resolved from src.fymc; signature mismatches fail explicitly.
"""
import importlib
import inspect
import io
import json
import pkgutil
from pathlib import Path
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MODULES = {}


def api(name):
    package = importlib.import_module("src.fymc")
    if not MODULES:
        MODULES[package.__name__] = package
        for entry in pkgutil.iter_modules(package.__path__, package.__name__ + "."):
            MODULES[entry.name] = importlib.import_module(entry.name)
    matches = [getattr(module, name) for module in MODULES.values() if hasattr(module, name)]
    if not matches:
        raise AssertionError("Missing FYMC public API: " + name)
    return matches[0]


def call(name, **context):
    """Bind named inputs, never retry a function after a runtime TypeError."""
    function = api(name)
    parameters = inspect.signature(function).parameters
    kwargs = {key: value for key, value in context.items() if key in parameters}
    inspect.signature(function).bind(**kwargs)
    return function(**kwargs)


def text(value):
    return json.dumps(value, ensure_ascii=False, default=str)


def nodes(value):
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from nodes(child)
    elif isinstance(value, (list, tuple)):
        for child in value:
            yield from nodes(child)


def collection(value, *keys):
    if isinstance(value, (list, tuple)):
        return list(value)
    for key in keys:
        if key in value:
            result = value[key]
            return list(result.values()) if isinstance(result, dict) else result
    if isinstance(value, dict) and value and all(isinstance(v, dict) for v in value.values()):
        return list(value.values())
    raise AssertionError("Missing collection: " + ", ".join(keys))


class PlatformTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from src.app_server import AppState

        cls.temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        cls.data_dir = Path(cls.temp.name)
        app_state = AppState(ROOT / "data")
        diagrams = call("build_volume_001_diagrams_data")
        workbook = call("build_volume_001_workbook")
        call("sync_publishing_store", root_dir=cls.data_dir,
             abridged_videos=app_state.abridged_list, raw_videos=app_state.raw_videos)
        pub_state = call("load_publishing_state", root_dir=cls.data_dir)
        cls.context = dict(root=ROOT, workspace_root=ROOT, data_dir=cls.data_dir,
                           store_dir=cls.data_dir, output_dir=cls.data_dir,
                           root_dir=cls.data_dir, abridged_videos=app_state.abridged_list,
                           raw_videos=app_state.raw_videos, diagrams=diagrams,
                           workbook=workbook, volume_meta=pub_state["volume"]["metadata"],
                           state=pub_state)
        cls.candidates = call("build_29_candidate_pipeline")
        cls.scorecard = call("get_flagship_scorecard")
        cls.audit = call("audit_existing_workspace", root_dir=ROOT)
        cls.research = call("build_research_database", **cls.context,
                            audit=cls.audit, workspace_audit=cls.audit)
        cls.manuscript = call("build_volume_001_manuscript", **cls.context,
                              research=cls.research, research_database=cls.research)
        cls.concepts = api("get_all_concepts")()
        cls.context.update(candidates=cls.candidates, scorecard=cls.scorecard,
                           audit=cls.audit, research=cls.research,
                           research_database=cls.research, manuscript=cls.manuscript)

    def render(self, name, concept, **extra):
        identifier = concept.get("id", concept.get("concept_id"))
        context = dict(self.context, concept=concept, concept_id=identifier,
                       design_concept=concept)
        context.update(extra)
        for alias, parameter in (
            ("mode", "viewport_mode"), ("page_number", "chapter_number"), ("format", "fmt")
        ):
            if alias in extra:
                context.setdefault(parameter, extra[alias])
        return call(name, **context)

    def svg(self, value):
        self.assertIsInstance(value, (str, bytes))
        element = ET.fromstring(value)
        self.assertEqual(element.tag, "{http://www.w3.org/2000/svg}svg")

    def test_brand_constants_and_no_trademark_symbols(self):
        package = importlib.import_module("src.fymc")
        constants = {key: value for key, value in vars(package).items()
                     if key.isupper() and isinstance(value, (str, dict, list, tuple))}
        self.assertTrue(constants, "src.fymc must expose brand constants")
        self.assertTrue(any("BRAND" in key for key in constants))
        self.assertNotIn(chr(0x2122), text(constants))
        self.assertNotIn(chr(0x00AE), text(constants))

    def test_candidate_ranking_dimensions_and_profit_uncertainty(self):
        candidates = collection(self.candidates, "candidates", "businesses")
        self.assertEqual(len(candidates), 29)
        self.assertEqual([candidate["rank"] for candidate in candidates], list(range(1, 30)))
        for candidate in candidates:
            with self.subTest(rank=candidate["rank"]):
                dimensions = candidate.get("dimensions", candidate.get("scores"))
                self.assertIsNotNone(dimensions)
                values = list(dimensions.values()) if isinstance(dimensions, dict) else dimensions
                self.assertEqual(len(values), 5)
                scores = [v["score"] if isinstance(v, dict) else v for v in values]
                self.assertEqual(sum(scores), candidate["total_score"])
        serialized = text(self.scorecard).lower()
        for required in ("conservative", "base", "scaled", "owner", "net", "profit", "uncertainty"):
            self.assertIn(required, serialized)
        bands = [v for v in nodes(self.scorecard) if isinstance(v, dict)
                 and (("low" in v and "high" in v) or ("lower" in v and "upper" in v))]
        self.assertTrue(bands, "Scorecard must contain numeric uncertainty bounds")
        for band in bands:
            self.assertLessEqual(band.get("low", band.get("lower")), band.get("high", band.get("upper")))

    def test_research_audit_consensus_and_permissions(self):
        for bucket in ("reusable_foundation", "needs_improvement", "must_redesign"):
            self.assertIn(bucket, text(self.audit))
        self.assertEqual(len(collection(self.research, "topics", "research_topics")), 8)
        self.assertIn("consensus", text(self.research).lower())
        ledger = self.research["permissions_ledger"]
        frames = [row for row in nodes(ledger) if isinstance(row, dict) and "frame" in text(row).lower()]
        self.assertTrue(frames)
        self.assertTrue(any(row.get("commercial_use_allowed") is False
                            or row.get("commercial_use") is False
                            or "non-commercial" in text(row).lower() for row in frames))

    def test_manuscript_diagrams_workbook_and_timestamp_citations(self):
        chapters = collection(self.manuscript, "chapters")
        self.assertEqual(len(chapters), 12)
        for number, chapter in enumerate(chapters, 1):
            self.assertRegex(text(chapter), r"\bQ" + str(number) + r"\b")
            self.assertGreater(len(text(chapter)), 100)
        self.assertEqual(len(collection(call("build_volume_001_diagrams_data"), "diagrams")), 8)
        self.assertEqual(len(collection(call("build_volume_001_workbook"), "worksheets", "sheets")), 6)
        video = {"video_id": "dQw4w9WgXcQ", "title": "Authorized research fixture",
                 "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                 "transcript": [{"text": "Validate demand before buying inventory.", "start": 83, "duration": 5}],
                 "tips": [{"text": "Validate demand first.", "timestamp": 83, "start": 83}],
                 "key_points": [{"text": "Validate demand first.", "timestamp": 83}]}
        cited = call("build_volume_001_manuscript",
                     **dict(self.context, abridged_videos=[video], videos=[video]))
        self.assertRegex(text(cited), r"https://(?:www\.)?(?:youtube\.com/watch\?[^\s\"<>]*[&?]t=83|youtu\.be/[^\s\"<>]*[?&]t=83)")

    def test_concept_identity_and_all_57_svg_documents(self):
        concepts = collection(self.concepts, "concepts")
        self.assertEqual(len(concepts), 3)
        ids = [c.get("id", c.get("concept_id")) for c in concepts]
        self.assertEqual(set(ids), {"concept_a", "concept_b", "concept_c"})
        for field in ("typography", "palette"):
            self.assertEqual(len({text(c[field]) for c in concepts}), 3)
        count = 0
        for concept in concepts:
            self.svg(self.render("render_scorecard_svg", concept))
            count += 1
            for function in ("render_all_diagrams_for_concept", "render_all_concept_mockups"):
                rendered = self.render(function, concept)
                self.assertIsInstance(rendered, dict)
                self.assertEqual(len(rendered), 8 if "diagrams" in function else 10)
                for name, svg in rendered.items():
                    with self.subTest(concept=concept.get("id"), asset=name):
                        self.svg(svg)
                        count += 1
                        if "cover" in name:
                            self.assertLessEqual(svg.upper().count("FUCK"), 1)
                        if "09_series_collection_mockup" in name:
                            for volume in range(1, 6):
                                self.assertIn("%03d" % volume, svg)
            for clean in (False, True):
                cover = self.render("render_cover_or_mockup_svg", concept,
                                    marketplace_clean=clean, mockup_id="01_front_cover",
                                    asset_id="01_front_cover", kind="cover")
                self.svg(cover)
                self.assertLessEqual(cover.upper().count("FUCK"), 0 if clean else 1)
        self.assertEqual(count, 57)

    def test_fourteen_interior_templates_in_three_modes(self):
        templates = api("INTERIOR_TEMPLATES")
        self.assertEqual(len(templates), 14)
        concept = collection(self.concepts, "concepts")[0]
        for index, template in enumerate(templates, 1):
            for mode in ("desktop", "tablet", "print"):
                with self.subTest(template=template, mode=mode):
                    html = self.render("render_interior_page_html", concept, template=template,
                                       template_id=template, page=index, page_number=index,
                                       mode=mode, viewport_mode=mode, chapter_number=index,
                                       show_print_guides=True)
                    self.assertIsInstance(html, str)
                    self.assertIn("<", html)
                    self.assertIn("guide", html.lower())

    def test_publishing_partial_updates_and_approval_guardrails(self):
        with tempfile.TemporaryDirectory() as directory:
            context = dict(self.context, root_dir=Path(directory),
                           data_dir=Path(directory), store_dir=Path(directory))
            call("sync_publishing_store", **context)
            before = call("load_publishing_state", **context)["volume"]
            chapters = collection(before.get("manuscript", before), "chapters")
            target = chapters[0].get("id", chapters[0].get("chapter_id", "Q1"))
            patch = {"chapter_id": target, "content": "Single chapter acceptance edit."}
            call("update_chapter_content", **context, chapter_number=target, patch=patch,
                 **patch, payload=patch, updates=patch)
            after = call("load_publishing_state", **context)["volume"]
            updated = collection(after.get("manuscript", after), "chapters")
            self.assertIn(patch["content"], text(updated[0]))
            self.assertEqual(chapters[1:], updated[1:])
            review = {"graphic_id": "01_front_cover", "status": "reviewed", "notes": "Fixture review"}
            call("update_graphic_review", **context, **review, payload=review, updates=review)
            reviewed = call("load_publishing_state", **context)["volume"]
            self.assertIn("Fixture review", text(reviewed))
            self.assertEqual(updated, collection(reviewed.get("manuscript", reviewed), "chapters"))
            settings = {"approved_concept_id": "concept_a", "public_deploy_approved": True,
                        "paid_sales_approved": True}
            call("update_publishing_settings", **context, patch=settings,
                 settings=settings, payload=settings, updates=settings)
            state = call("load_publishing_state", **context)
            guarded = state.get("settings", state)
            self.assertIsNone(guarded["approved_concept_id"])
            self.assertIs(guarded["public_deploy_approved"], False)
            self.assertIs(guarded["paid_sales_approved"], False)
            signup = {"email": "reader@example.com", "consent": True}
            call("record_newsletter_signup", **context, **signup, payload=signup)
            self.assertIn(signup["email"], text(call("load_publishing_state", **context)))

    def test_pdf_epub_and_full_qa(self):
        concept = collection(self.concepts, "concepts")[0]
        for kind in ("digital_pdf", "print_6x9_pdf", "workbook_pdf"):
            data = self.render("render_fymc_pdf_bytes", concept, fmt=kind,
                               format=kind, export_format=kind, variant=kind)
            self.assertTrue(data.startswith(b"%PDF-"))
            self.assertIn(b"%%EOF", data[-1024:])
            if kind == "print_6x9_pdf":
                self.assertIn(b"/TrimBox", data)
        data = self.render("render_fymc_epub_bytes", concept)
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(archive.namelist()[0], "mimetype")
            self.assertEqual(archive.getinfo("mimetype").compress_type, zipfile.ZIP_STORED)
            self.assertEqual(archive.read("mimetype"), b"application/epub+zip")
            container = ET.fromstring(archive.read("META-INF/container.xml"))
            rootfile = container.find(".//{*}rootfile")
            self.assertIsNotNone(rootfile)
            package = ET.fromstring(archive.read(rootfile.attrib["full-path"]))
            self.assertEqual(package.attrib["version"], "3.0")
            self.assertFalse(any(name.lower().endswith((".jpg", ".jpeg")) for name in archive.namelist()))
        qa = call("run_full_qa_suite", **self.context)
        self.assertIs(qa["overall_pass"], True, text(qa))
        self.assertTrue(any(v == 57 for v in nodes(qa)), "QA must report 57 SVGs")
        self.assertTrue(any(v == 42 for v in nodes(qa)), "QA must report 42 template renders")


class LiveHTTPTests(unittest.TestCase):
    def test_complete_local_http_workflow(self):
        from src.app_server import create_server
        with tempfile.TemporaryDirectory() as directory:
            server = create_server("127.0.0.1", 0, directory)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            base = "http://127.0.0.1:%d" % server.server_address[1]
            def request(path, payload=None):
                body = None if payload is None else json.dumps(payload).encode()
                req = urllib.request.Request(base + path, data=body,
                                             headers={"Content-Type": "application/json"})
                try:
                    with urllib.request.urlopen(req, timeout=60) as response:
                        self.assertEqual(response.status, 200, path)
                        data = response.read()
                        self.assertTrue(data, path)
                        return json.loads(data) if "application/json" in response.headers.get("Content-Type", "") else data
                except urllib.error.HTTPError as error:
                    self.fail("%s: HTTP %s: %s" % (path, error.code, error.read().decode(errors="replace")))
            try:
                for path in ("/", "/studio", "/site"):
                    self.assertIn(b"<html", request(path).lower())
                request("/api/fymc/overview")
                catalog = request("/api/fymc/catalog")
                for key in ("candidates", "businesses"):
                    self.assertEqual(len(catalog[key]), 29)
                request("/api/fymc/research")
                manuscript = request("/api/fymc/manuscript")
                chapters = collection(manuscript.get("manuscript", manuscript), "chapters")
                request("/api/fymc/manuscript/update", {"chapter_id": chapters[0].get("id", "Q1"), "content": "HTTP chapter edit."})
                self.assertIn("HTTP chapter edit.", text(request("/api/fymc/manuscript")))
                for path in ("mockup?concept=a", "diagram?concept=b", "scorecard?concept=c"):
                    self.assertEqual(ET.fromstring(request("/api/fymc/svg/" + path)).tag, "{http://www.w3.org/2000/svg}svg")
                self.assertIn(b"<", request("/api/fymc/preview-page?concept=a&page=1"))
                request("/api/fymc/graphics/review", {"graphic_id": "01_front_cover", "status": "reviewed", "notes": "HTTP review"})
                self.assertTrue(request("/api/fymc/download?concept=a&format=pdf").startswith(b"%PDF-"))
                with zipfile.ZipFile(io.BytesIO(request("/api/fymc/download?concept=b&fmt=epub"))) as archive:
                    self.assertEqual(archive.read("mimetype"), b"application/epub+zip")
                settings = request("/api/fymc/settings", {"approved_concept_id": "concept_a"})
                self.assertIsNone(settings.get("settings", settings)["approved_concept_id"])
                request("/api/fymc/newsletter", {"email": "http-reader@example.com", "consent": True})
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=10)
                self.assertFalse(thread.is_alive(), "HTTP server thread did not stop")


class ExistingRegressionAuditTests:
    def setUp(self):
        from src.fymc.brand_and_catalog import sync_publishing_store, load_publishing_state
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        sync_publishing_store(self.root)
        self.state = load_publishing_state(self.root)
        self.volume = self.root / "publishing/volumes/vol-001-heir-hunting"

    def test_python_settings_cannot_bypass_gates(self):
        from src.fymc.brand_and_catalog import update_publishing_settings
        patch = dict(approved_concept_id="concept_a", public_deploy_approved=True,
                     paid_sales_approved=True, owner_explicit_concept_approval=True,
                     owner_explicit_deploy_approval=True, owner_explicit_sales_approval=True)
        brand_path = self.root / "publishing/brand/brand_system.json"
        brand = json.loads(brand_path.read_text())
        brand["gates"].update(approved_concept_id="concept_a", design_approved_at="yesterday",
                              public_deploy_approved=True, paid_sales_approved=True)
        brand_path.write_text(json.dumps(brand))
        for changes in ({}, patch, {"owner_explicit_concept_approval": True}):
            result = update_publishing_settings(self.root, changes)
            self.assertEqual(set(result["rejected"]), set(changes))
            self.assertTrue(result["design_approval_gate_enforced"])
            gates = result["gates"]
            self.assertIsNone(gates["approved_concept_id"])
            self.assertFalse(gates["public_deploy_approved"])
            self.assertFalse(gates["paid_sales_approved"])
            self.assertEqual(gates["design_approval_status"], "awaiting_owner_approval")
            self.assertNotIn("design_approved_at", gates)

    def test_http_pricing_and_invalid_sections(self):
        from src.app_server import create_server
        server = create_server("127.0.0.1", 0, self.temp.name)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        base = "http://127.0.0.1:%d" % server.server_address[1]
        def request(path, payload=None, method=None):
            req = urllib.request.Request(base + path,
                data=None if payload is None else json.dumps(payload).encode(),
                headers={"Content-Type": "application/json"}, method=method)
            try:
                response = urllib.request.urlopen(req, timeout=60)
            except urllib.error.HTTPError as error:
                response = error
            with response:
                return response.code, json.loads(response.read())
        try:
            self.assertEqual(request("/api/fymc/manuscript")[0], 200)
            paths = list(self.root.rglob("manuscript.json")) + list(self.root.rglob("chapter-01.md"))
            self.assertTrue(paths)
            before = {path: path.read_bytes() for path in paths}
            status, result = request("/api/fymc/manuscript/update", {"chapter_id": "Q1", "sections": 1})
            self.assertEqual(status, 400)
            self.assertEqual(result["error"], "invalid_field_type")
            self.assertEqual(before, {path: path.read_bytes() for path in paths})
            for payload, error in (({"chapter_id": "Q1", "sections": [{"tables": [{"rows": 1}]}]}, "invalid_field_type"),
                                   ({"chapter_id": "Q1", "sections": [{"sop": {"steps": 1}}]}, "invalid_field_type"),
                                   ({"chapter_number": 1.9, "title": "Invalid"}, "invalid_chapter_number"),
                                   ({"chapter_number": float("inf"), "title": "Invalid"}, "invalid_chapter_number")):
                status, result = request("/api/fymc/manuscript/update", payload)
                self.assertEqual(status, 400)
                self.assertEqual(result["error"], error)
                self.assertEqual(before, {path: path.read_bytes() for path in paths})
            from unittest.mock import patch
            from src.fymc.brand_and_catalog import update_chapter_content
            with patch("src.fymc.http_routes.run_full_qa_suite", return_value={"marker": "cached"}) as qa:
                self.assertEqual(request("/api/fymc/qa")[0], 200)
                self.assertEqual(request("/api/fymc/qa")[0], 200)
                self.assertEqual(qa.call_count, 1)
                update_chapter_content(self.root, 1, {"title": "Direct Python edit"})
                self.assertEqual(request("/api/fymc/qa")[0], 200)
                self.assertEqual(qa.call_count, 2)
            brand_path = self.root / "publishing/brand/brand_system.json"
            brand = json.loads(brand_path.read_text())
            brand["gates"]["approved_concept_id"] = "concept_a"
            brand_path.write_text(json.dumps(brand))
            status, overview = request("/api/fymc/overview")
            self.assertEqual(status, 200)
            self.assertIsNone(overview["gates"]["approved_concept_id"])
            for method in ("POST", "PATCH"):
                status, result = request("/api/fymc/settings",
                    {"pricing_hypotheses": {"digital": {"price": 29}}}, method)
                self.assertEqual(status, 200)
                self.assertEqual(result["rejected"], [])
                self.assertIsNone(result["gates"]["approved_concept_id"])
                self.assertFalse(result["gates"]["public_deploy_approved"])
                self.assertFalse(result["gates"]["paid_sales_approved"])
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=10)

    def test_field_validation_and_render_failure_leave_files_unchanged(self):
        from unittest.mock import patch
        from src.fymc.brand_and_catalog import update_chapter_content
        paths = [self.volume / "manuscript.json", self.volume / "chapters/chapter-01.md"]
        before = {path: path.read_bytes() for path in paths}
        invalid = [{key: value} for key in ("title", "subtitle", "executive_summary", "pull_quote", "sections", "action_checklist")
                   for value in (None, 1, True, 1.5)]
        invalid += [{"title": "  "}, {"pull_quote": {"text": 3}}, {"sections": [False]}, {"action_checklist": [3]}]
        for key in ("heading", "title", "name", "epistemic_status", "body", "text", "content", "paragraphs", "bullets", "points", "takeaways", "table", "tables", "sops", "sop", "procedures", "sop_steps", "callouts", "callout", "notes"):
            invalid.append({"sections": [{key: 1}]})
        invalid += [{"sections": [{"table": {"rows": 1}}]}, {"sections": [{"body": [True]}]},
                    {"sections": [{"tables": [1]}]}, {"sections": [{"sop_steps": [False]}]}]
        for changes in invalid:
            with self.subTest(changes=changes):
                result = update_chapter_content(self.root, 1, changes)
                self.assertEqual(result["error"], "invalid_field_type")
                self.assertEqual(result["invalid_fields"], list(changes))
                self.assertEqual(before, {path: path.read_bytes() for path in paths})
        with patch("src.fymc.brand_and_catalog.chapter_to_markdown", side_effect=ValueError("render failed")):
            result = update_chapter_content(self.root, 1, {"title": "Valid title"})
            self.assertEqual(result["error"], "invalid_field_type")
        self.assertEqual(before, {path: path.read_bytes() for path in paths})

    def test_chapter_strings_are_recursively_xml_cleaned(self):
        from src.fymc.brand_and_catalog import update_chapter_content
        dirty = "Before\x00\x08\x0b\x0c\x0e\x1f\ufffe\uffff\ud800\udfffAfter"
        result = update_chapter_content(self.root, 1, {
            "title": dirty, "subtitle": dirty, "executive_summary": dirty,
            "pull_quote": {"text": dirty}, "action_checklist": [dirty, {"action": dirty}],
            "sections": [{"heading": dirty, "paragraphs": [dirty],
                          "sop_steps": [{"title": dirty, "detail": dirty}]}]})
        self.assertTrue(result["ok"])
        self.assertEqual(result["chapter"]["sections"][0]["sop_steps"][0]["detail"], "BeforeAfter")
        self.assertIn("BeforeAfter", Path(result["markdown_path"]).read_text())
        self.assertNotIn("\\u0000", Path(result["manuscript_path"]).read_text())

    def test_epub_diagram_references(self):
        from src.fymc.exporters import render_fymc_epub_bytes
        chapter = self.state["volume"]["manuscript"]["chapters"][1]
        for reference, expected in (("diag-04-jurisdiction-fee-caps", 4), ("diagram_04", 4),
                                    (None, 2), ("", 2)):
            chapter["diagram_id"] = reference
            with zipfile.ZipFile(io.BytesIO(render_fymc_epub_bytes(self.state))) as archive:
                self.assertIn(('images/diag_%02d.svg' % expected).encode(), archive.read("OEBPS/chapter_02.xhtml"))
        chapter.pop("diagram_id")
        with zipfile.ZipFile(io.BytesIO(render_fymc_epub_bytes(self.state))) as archive:
            self.assertIn(b"images/diag_02.svg", archive.read("OEBPS/chapter_02.xhtml"))
        for reference in ("unknown", "diag-00-invalid", "diagram_09", False, "unknown-04-reference", "diag-04-nonexistent"):
            chapter["diagram_id"] = reference
            with self.assertRaisesRegex(ValueError, "Chapter diagram reference must identify diagram 01 through 08"):
                render_fymc_epub_bytes(self.state)

    def test_control_characters_in_epub_and_bundle(self):
        from src.fymc.exporters import render_fymc_epub_bytes, render_fymc_bundle_zip_bytes, _ascii
        self.state["volume"]["metadata"]["title"] = "Safe\x00Title"
        self.state["volume"]["manuscript"]["chapters"][0]["executive_summary"] = "Safe\x00Text\uffff\ud800\udfff"
        self.assertEqual(_ascii("Safe\x00Text\uffff\ud800\udfff"), "SafeText")
        epub = render_fymc_epub_bytes(self.state)
        with zipfile.ZipFile(io.BytesIO(render_fymc_bundle_zip_bytes(self.state))) as bundle:
            self.assertIn("book.epub", bundle.namelist())
        with zipfile.ZipFile(io.BytesIO(epub)) as archive:
            for name in archive.namelist():
                if name.endswith((".xml", ".xhtml", ".opf", ".ncx", ".svg")):
                    ET.fromstring(archive.read(name))
            self.assertIn(b"SafeText", archive.read("OEBPS/chapter_01.xhtml"))

    def test_sync_preserves_source_citations(self):
        from src.fymc.brand_and_catalog import sync_publishing_store
        video = {"video_id": "dQw4w9WgXcQ", "title": "Heir hunting research",
                 "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                 "tips": [{"text": "Validate demand first.", "timestamp": 83, "start": 83, "chapter_number": 1}]}
        sync_publishing_store(self.root, abridged_videos=[video])
        manuscript = json.loads((self.volume / "manuscript.json").read_text())
        citations = [citation for chapter in manuscript["chapters"] for citation in chapter["source_citations"]]
        self.assertTrue(citations)
        self.assertIn("t=83", text(citations))
        video["tips"].append({"text": "Second incremental tip.", "timestamp": 97, "start": 97, "chapter_number": 1})
        sync_publishing_store(self.root, abridged_videos=[video])
        sync_publishing_store(self.root, abridged_videos=[video])
        updated = json.loads((self.volume / "manuscript.json").read_text())
        first = next(ch for ch in updated["chapters"] if any(c.get("text") == "Validate demand first." for c in ch["source_citations"]))
        self.assertEqual(sum(c.get("text") == "Second incremental tip." for c in first["source_citations"]), 1)

    def test_sop_labels_and_details_in_markdown_and_html(self):
        from copy import deepcopy
        from src.fymc.brand_and_catalog import chapter_to_markdown
        from src.fymc.interior_templates import render_interior_page_html
        manuscript = self.state["volume"]["manuscript"]
        chapter = manuscript["chapters"][6]
        steps = [{"step": 1, "title": "Define the question", "action": "Ask the operator.", "detail": "Record the precise research question."}]
        for location in ("section", "sop", "sops", "procedures", "sop_steps", "steps"):
            current = deepcopy(chapter)
            current["sections"] = [{"heading": "Research"}]
            current.pop("steps", None)
            current.pop("sop_steps", None)
            if location == "section":
                current["sections"][0]["sop_steps"] = steps
            elif location in ("sop", "sops", "procedures"):
                current["sections"][0][location] = {"steps": steps}
            else:
                current[location] = steps
            chapters = deepcopy(manuscript["chapters"])
            chapters[6] = current
            markdown = chapter_to_markdown(current)
            page = render_interior_page_html(template_id="step_by_step_sop", concept_id="concept_a",
                manuscript={"chapters": chapters}, scorecard={}, diagrams=[], chapter_number=7)
            self.assertIn("1. Define the question", markdown)
            for rendered in (markdown, page):
                self.assertIn(steps[0]["detail"], rendered)
                self.assertIn(steps[0]["title"], rendered)
            self.assertIn(steps[0]["action"], page)
        from src.fymc.interior_templates import _steps
        self.assertIn("Detail survives", _steps([{"action": "", "detail": "Detail survives"}]))

    def test_partial_initialization_and_markdown_write_rollback(self):
        from unittest.mock import patch
        from src.fymc.brand_and_catalog import load_publishing_state, update_chapter_content
        for path in (self.volume / "manuscript.json", self.volume / "chapters/chapter-12.md"):
            path.unlink()
            recovered = load_publishing_state(self.root)
            self.assertTrue(path.is_file())
            self.assertEqual(recovered["counts"]["chapter_markdown_files"], 12)
        paths = [self.volume / "manuscript.json", self.volume / "chapters/chapter-01.md"]
        before = {p: p.read_bytes() for p in paths}
        with patch("src.fymc.brand_and_catalog._write_text", side_effect=OSError("write failed")):
            with self.assertRaisesRegex(OSError, "write failed"):
                update_chapter_content(self.root, 1, {"title": "Rollback this"})
        self.assertEqual(before, {p: p.read_bytes() for p in paths})

    def test_cross_process_reentrant_lock_and_writers(self):
        import subprocess
        import sys
        from src.fymc.brand_and_catalog import _root_lock, load_publishing_state
        probe = "from pathlib import Path; from src.fymc.brand_and_catalog import _root_lock; import sys; lock=_root_lock(Path(sys.argv[1])); acquired=lock.acquire(False); print(acquired); acquired and lock.release()"
        lock = _root_lock(self.root)
        with lock:
            self.assertTrue(lock.acquire(False))
            lock.release()
            result = subprocess.run([sys.executable, "-c", probe, str(self.root)], cwd=ROOT,
                                    capture_output=True, text=True, timeout=10, check=True)
            self.assertEqual(result.stdout.strip(), "False")
        code = """
import sys, time
from pathlib import Path
from src.fymc.brand_and_catalog import _root_lock, update_chapter_content, record_newsletter_signup
root, number = Path(sys.argv[1]), int(sys.argv[2])
for i in range(8):
    with _root_lock(root):
        time.sleep(.005)
        assert update_chapter_content(root, number, {'title': f'Writer {number} revision {i}'})['ok']
        assert record_newsletter_signup(root, f'writer{number}-{i}@example.com')['ok']
"""
        processes = [subprocess.Popen([sys.executable, "-c", code, str(self.root), str(n)],
                     cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE) for n in (1, 2)]
        try:
            for process in processes:
                out, err = process.communicate(timeout=30)
                self.assertEqual(process.returncode, 0, err.decode())
        finally:
            for process in processes:
                if process.poll() is None:
                    process.kill()
                    process.wait()
        state = load_publishing_state(self.root)
        self.assertEqual(state["counts"]["newsletter_subscribers"], 16)
        for n in (1, 2):
            self.assertEqual(state["volume"]["manuscript"]["chapters"][n - 1]["title"], f"Writer {n} revision 7")

    def test_nested_validation_and_strict_numbers(self):
        from src.fymc.brand_and_catalog import update_chapter_content
        paths = [self.volume / "manuscript.json", self.volume / "chapters/chapter-01.md"]
        before = {p: p.read_bytes() for p in paths}
        malformed = [{"tables": [{"rows": 1}]}, {"table": {"rows": [], "headers": [1]}},
                     {"sop": {"steps": 1}}, {"sops": [{"steps": [{"detail": []}]}]},
                     {"callout": {"body": {}}}, {"callouts": [{"items": [1]}]}]
        for section in malformed:
            self.assertEqual(update_chapter_content(self.root, 1, {"sections": [section]})["error"], "invalid_field_type")
        for number in (True, 1.9, float("inf"), "1.0", "+1", "chapter-1junk"):
            self.assertEqual(update_chapter_content(self.root, number, {"title": "Invalid"})["error"], "invalid_chapter_number")
        self.assertEqual(before, {p: p.read_bytes() for p in paths})

    def test_seeded_gates_and_single_package_art_render(self):
        from unittest.mock import patch
        from src.fymc import exporters
        from src.fymc.brand_and_catalog import load_publishing_state, sync_publishing_store
        path = self.root / "publishing/brand/brand_system.json"
        brand = json.loads(path.read_text())
        brand["gates"].update(approved_concept_id="concept_a", design_approved_at="today",
                              public_deploy_approved=True, paid_sales_approved=True)
        path.write_text(json.dumps(brand))
        loaded = load_publishing_state(self.root)
        self.assertIsNone(loaded["gates"]["approved_concept_id"])
        self.assertIsNone(sync_publishing_store(self.root)["gates"]["approved_concept_id"])
        self.assertNotIn("design_approved_at", json.loads(path.read_text())["gates"])
        loaded["brand_system"]["gates"]["approved_concept_id"] = "concept_a"
        with zipfile.ZipFile(io.BytesIO(exporters.render_fymc_epub_bytes(loaded))) as epub:
            self.assertIn(b"AWAITING OWNER DESIGN APPROVAL", epub.read("OEBPS/cover.xhtml"))
        with patch.object(exporters, "_epub_art", wraps=exporters._epub_art) as render:
            result = exporters.export_concept_package(self.root, loaded)
            self.assertEqual(render.call_count, 1)
        self.assertFalse(json.loads(Path(result["files"]["manifest.json"]).read_text())["approved"])

    def test_export_swap_rollback_and_render_outside_lock(self):
        from unittest.mock import patch
        from src.fymc import exporters
        directory = self.root / "publishing/previews/concept_a"
        directory.mkdir(parents=True)
        (directory / "old.txt").write_text("previous package")
        original = exporters.os.replace
        def replace(source, target):
            if ".stage." in Path(source).name:
                raise OSError("swap failed")
            return original(source, target)
        with patch.object(exporters, "_package_files", return_value={"new.txt": b"new"}), patch.object(exporters.os, "replace", side_effect=replace):
            with self.assertRaisesRegex(OSError, "swap failed"):
                exporters.export_concept_package(self.root, self.state)
        self.assertEqual((directory / "old.txt").read_text(), "previous package")
        self.assertEqual(list(directory.parent.iterdir()), [directory])

    def test_concept_nested_copies(self):
        from src.fymc.design_concepts import get_concept, get_all_concepts
        original = get_concept("concept_a")
        get_concept("concept_a")["palette"]["accent"] = "#000"
        get_all_concepts()["concept_a"]["typography"]["body"] = "changed"
        self.assertEqual(get_concept("concept_a"), original)

    def test_unicode_cover_copy_terminates(self):
        import subprocess
        import sys
        code = ('from src.fymc.cover_and_mockups import render_cover_or_mockup_svg; '
                'print(render_cover_or_mockup_svg("concept_a", "01_front_cover", '
                '{"title": "ß" * 10 + "fuck"}, marketplace_clean=True))')
        result = subprocess.run([sys.executable, "-c", code], cwd=ROOT, capture_output=True,
                                text=True, timeout=10, check=True)
        ET.fromstring(result.stdout)
        self.assertIn("ß" * 10 + "FYMC", result.stdout)
        self.assertNotIn("fuck", result.stdout.lower())

    def test_concurrent_exports_hold_root_lock_through_replacement(self):
        from concurrent.futures import ThreadPoolExecutor
        from unittest.mock import patch
        import hashlib
        from src.fymc import exporters
        from src.fymc.brand_and_catalog import _root_lock
        original_package = exporters._package_files
        render_barrier = threading.Barrier(2)
        original_replace = exporters.os.replace
        def assert_locked():
            with ThreadPoolExecutor(max_workers=1) as pool:
                def probe():
                    lock = _root_lock(self.root)
                    acquired = lock.acquire(blocking=False)
                    if acquired:
                        lock.release()
                    return acquired
                self.assertFalse(pool.submit(probe).result(timeout=5))
        def package(*args):
            render_barrier.wait(timeout=10)
            return original_package(*args)
        def replace(*args):
            assert_locked()
            return original_replace(*args)
        with patch.object(exporters, "_package_files", side_effect=package), patch.object(exporters.os, "replace", side_effect=replace):
            with ThreadPoolExecutor(max_workers=2) as pool:
                futures = [pool.submit(exporters.export_concept_package, self.root, self.state) for _ in range(2)]
                results = [future.result(timeout=60) for future in futures]
        directory = Path(results[-1]["output_dir"])
        manifest = json.loads((directory / "manifest.json").read_text())
        with zipfile.ZipFile(directory / "bundle.zip") as bundle:
            for name, info in manifest["files"].items():
                data = (directory / name).read_bytes()
                self.assertEqual(hashlib.sha256(data).hexdigest(), info["sha256"])
                self.assertEqual(len(data), info["bytes"])
                self.assertEqual(bundle.read(name), data)


class InteriorSchemaTests(unittest.TestCase):
    def setUp(self):
        self.chapter = {
            "chapter_number": 1, "title": "Schema fixture", "subtitle": "A focused pilot",
            "executive_summary": "The executive brief.", "reading_time_minutes": 7,
            "key_metrics": [{"label": "Pilot", "value": "20 records", "context": "Bounded cohort"}],
            "sections": [{
                "heading": "Qualification", "epistemic_status": "operating_framework",
                "paragraphs": ["First paragraph.", "Second paragraph."],
                "table": {"headers": ["Gate", "Evidence"], "rows": [["Identity", "Official record"]]},
                "sop_steps": ["Save the record.", "Check the claimant."],
                "callout": {"title": "Stop rule", "body": "Pause at the budget limit."},
            }],
            "pull_quote": "Evidence before outreach.",
            "action_checklist": ["Approve the pilot."],
            "statutory_citations": [{"title": "Primary authority", "relevance": "Eligibility rules.", "url": "https://example.com/law?a=1&b=2"}],
            "source_citations": [{"timestamp_label": "01:23", "title": "Operator interview", "text": "Verify first.", "url": "https://example.com/video?t=83"}],
        }

    def render(self, template, chapter=None, **kwargs):
        from src.fymc.interior_templates import render_interior_page_html
        options = dict(template_id=template, concept_id="concept_a",
                       manuscript={"chapters": [self.chapter if chapter is None else chapter]},
                       scorecard={}, diagrams=[], chapter_number=1)
        options.update(kwargs)
        return render_interior_page_html(**options)

    def test_structured_sections_and_evidence(self):
        templates = ("executive_summary", "opportunity_overview", "expert_insights",
                     "financial_breakdown", "comparison_table", "case_study_walkthrough",
                     "legal_compliance_notes", "resource_directory", "thirty_day_plan")
        for template in templates:
            with self.subTest(template=template):
                page = self.render(template)
                for fragment in ("<h3>Qualification</h3>", "<p>First paragraph.</p>",
                                 "<p>Second paragraph.</p>", '<aside class="aside">',
                                 "<li>Save the record.</li>", "<td>Official record</td>",
                                 "Pilot: 20 records — Bounded cohort", "01:23",
                                 'href="https://example.com/law?a=1&amp;b=2"',
                                 'href="https://example.com/video?t=83"',
                                 "Reading time: 7 min"):
                    self.assertIn(fragment, page)
                for fragment in ("paragraphs:", "epistemic status:", "sop steps:",
                                 "not legal advice", "not a guarantee of results",
                                 "has not been independently verified by this renderer"):
                    self.assertNotIn(fragment, page)

    def test_opener_sop_and_checklist(self):
        opener = self.render("chapter_opener")
        for fragment in ("A focused pilot", "The executive brief.", "Chapter sections",
                         "<li>Qualification</li>", "<blockquote><p>Evidence before outreach.</p>"):
            self.assertIn(fragment, opener)
        sop = self.render("step_by_step_sop")
        self.assertIn("<h3>Qualification</h3><ol>", sop)
        self.assertEqual(sop.count("<li>Save the record.</li>"), 1)
        self.assertIn("Approve the pilot.", sop)
        checklist = self.render("action_checklist")
        self.assertIn('class="checkbox"', checklist)
        self.assertIn("Approve the pilot.", checklist)
        self.assertIn("Pilot: 20 records — Bounded cohort", checklist)

    def test_flat_fields_override_structured_fallbacks(self):
        cases = [
            ("chapter_opener", {"summary": "Flat brief", "body": "Flat body"}, "Flat brief"),
            ("executive_summary", {"key_takeaways": ["Flat finding"]}, "Flat finding"),
            ("opportunity_overview", {"demand_signals": ["Flat demand"]}, "Flat demand"),
            ("step_by_step_sop", {"steps": [{"title": "Flat step", "action": "Execute", "acceptance_criteria": "Done"}]}, "Flat step"),
            ("expert_insights", {"expert_insights": [{"quote": "Flat quote", "expert": "Reviewer"}]}, "Flat quote"),
            ("financial_breakdown", {"financials": [{"item": "Flat cost", "amount": 0}]}, "Flat cost"),
            ("comparison_table", {"comparison": {"headers": ["Flat header"], "rows": [["Flat option"]]}}, "Flat option"),
            ("case_study_walkthrough", {"case_study": {"summary": "Flat case"}}, "Flat case"),
            ("legal_compliance_notes", {"legal_notes": [{"jurisdiction": "Flat jurisdiction"}]}, "Flat jurisdiction"),
            ("resource_directory", {"resources": [{"name": "Flat resource", "url": "https://example.com/tool"}]}, "Flat resource"),
            ("action_checklist", {"checklist": ["Flat check"]}, "Flat check"),
            ("action_checklist", {"action_items": ["Flat action"]}, "Flat action"),
            ("thirty_day_plan", {"thirty_day_plan": [{"days": "Flat period", "actions": ["Execute"]}]}, "Flat period"),
        ]
        for template, fields, expected in cases:
            with self.subTest(template=template, fields=fields):
                chapter = dict(self.chapter, **fields)
                if template == "chapter_opener":
                    chapter.pop("executive_summary")
                self.assertIn(expected, self.render(template, chapter))
                self.assertIn(expected, self.render(template, {}, manuscript=fields))
        page = self.render("executive_summary", dict(self.chapter, sources=["https://example.com/flat"],
                           editorial_notes="Flat editorial note", verification_status="Reviewed"))
        self.assertIn('href="https://example.com/flat"', page)
        self.assertNotIn("Primary authority", page)
        self.assertIn("Flat editorial note", page)
        self.assertIn("Reviewed", page)

    def test_real_volume_all_templates_concepts_and_modes(self):
        from src.fymc.interior_templates import INTERIOR_TEMPLATES
        from src.fymc.volume_001_manuscript import CHAPTERS_1_TO_6, build_volume_001_diagrams_data
        from src.fymc.volume_001_chapters_b import CHAPTERS_7_TO_12
        from src.fymc.scorecard_engine import get_flagship_scorecard
        chapters = CHAPTERS_1_TO_6 + CHAPTERS_7_TO_12
        for template in INTERIOR_TEMPLATES:
            number = template["default_chapter"]
            for concept in ("concept_a", "concept_b", "concept_c"):
                for mode in ("desktop", "tablet", "print"):
                    with self.subTest(template=template["template_id"], concept=concept, mode=mode):
                        page = self.render(template["template_id"], manuscript={"chapters": chapters},
                                           chapter_number=number, concept_id=concept, viewport_mode=mode,
                                           show_print_guides=True, scorecard=get_flagship_scorecard(),
                                           diagrams=build_volume_001_diagrams_data())
                        self.assertIn(chapters[number - 1]["key_metrics"][0]["label"] + ":", page)
                        self.assertIn("Source register", page)
                        self.assertNotIn("paragraphs:", page)
                        self.assertNotIn(chr(0x2122), page)
                        self.assertNotIn(chr(0x00AE), page)
                        if mode == "print":
                            self.assertIn('class="guide bleed"', page)
                            self.assertIn("6.25in 9.25in", page)

    def test_diagrams_scorecard_and_safe_links(self):
        from src.fymc.volume_001_manuscript import build_volume_001_diagrams_data
        from src.fymc.scorecard_engine import get_flagship_scorecard
        diagram = build_volume_001_diagrams_data()[0]
        page = self.render("research_exhibit", diagrams=[diagram])
        self.assertIn(diagram["caption"], page)
        self.assertIn("Classify (Gate 1) —", page)
        self.assertIn(diagram["assumptions_note"], page)
        self.assertNotIn("Not supplied", page)
        page = self.render("scorecard_page", scorecard=get_flagship_scorecard())
        table = page.split("<caption>Accessible scorecard data</caption>", 1)[1]
        for label in ("Total Score", "Tier", "Confidence &amp; Uncertainty Band", "Dimensions", "Scenarios", "Revenue Potential:"):
            self.assertIn(label, table)
        self.assertIn("Key risks", table)
        self.assertIn("Scoring method &amp; uncertainty", table)
        chapter = dict(self.chapter, source_citations=[{"title": "<script>alert(1)</script>", "url": "javascript:alert(1)"}])
        page = self.render("resource_directory", chapter)
        self.assertNotIn("<script>", page)
        self.assertNotIn('href="javascript:', page)
        self.assertIn("&lt;script&gt;", page)

    def test_validation_and_brand_stripping(self):
        for kwargs in ({"template_id": "bad"}, {"concept_id": "bad"},
                       {"viewport_mode": "bad"}, {"chapter_number": 0},
                       {"chapter_number": True}, {"chapter_number": "1"}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                self.render("chapter_opener", **kwargs)
        for kwargs in ({"manuscript": []}, {"scorecard": []}, {"diagrams": {}}, {"diagrams": [None]}):
            with self.subTest(kwargs=kwargs), self.assertRaises(TypeError):
                self.render("research_exhibit", **kwargs)
        for symbol in (chr(0x2122), chr(0x00AE)):
            page = self.render("chapter_opener", dict(self.chapter, title="Money-to-Manpower Score" + symbol))
            self.assertNotIn(symbol, page)
        source = (ROOT / "src/fymc/interior_templates.py").read_text()
        self.assertNotIn(chr(0x2122), source)
        self.assertNotIn(chr(0x00AE), source)


class RegressionAuditTests(ExistingRegressionAuditTests, unittest.TestCase):
    def setUp(self):
        from src.fymc import brand_and_catalog as store
        self.store = store
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        store.sync_publishing_store(self.root)
        self.state = store.load_publishing_state(self.root)
        self.pub = self.root / 'publishing'
        self.volume = self.pub / 'volumes' / store.VOLUME_SLUG

    def route(self, method, path, body=None):
        from types import SimpleNamespace
        from src.fymc.http_routes import handle_fymc_http
        class Handler:
            def _json(self, payload, status=200):
                return status, payload
        state = SimpleNamespace(lock=threading.RLock(), data_dir=self.root,
                                abridged_list=[], raw_videos=[])
        return handle_fymc_http(Handler(), state, method, path, {}, body)

    def test_01_corrupt_store_refusal_and_http_500(self):
        path = self.pub / 'site/newsletter_signups.json'
        for data in (b'{broken', b'   ', b'"oops"', b'{"subscribers":"not-a-list"}', b'\xff'):
            with self.subTest(data=data):
                path.write_bytes(data)
                with self.assertRaises(self.store.CorruptStoreError):
                    self.store.record_newsletter_signup(self.root, 'reader@example.com')
                self.assertEqual(path.read_bytes(), data)
                status, payload = self.route('GET', '/api/fymc/overview')
                self.assertEqual(status, 500)
                self.assertEqual(payload['error'], 'corrupt_store')
                with self.assertRaises(self.store.CorruptStoreError):
                    self.store.sync_publishing_store(self.root)
                self.assertEqual(path.read_bytes(), data)
        self.store.sync_publishing_store(self.root, force=True)
        self.assertEqual(json.loads(path.read_text()), {'subscribers': []})
        path.unlink()
        path.symlink_to(self.root / 'absent')
        with self.assertRaises(self.store.CorruptStoreError):
            self.store._read_json(path, strict=True)
        missing = self.root / 'missing.json'
        self.assertEqual(self.store._read_json(missing, {'default': True}, strict=True), {'default': True})

    def test_02_fsync_transaction_rollback_and_restart_recovery(self):
        from unittest.mock import patch
        manuscript = self.volume / 'manuscript.json'
        markdown = self.volume / 'chapters/chapter-01.md'
        prior = manuscript.read_bytes(), markdown.read_bytes()
        with patch('src.fymc.brand_and_catalog._write_text', side_effect=OSError('disk failure')):
            with self.assertRaises(OSError):
                self.store.update_chapter_content(self.root, 1, {'title': 'Must roll back'})
        self.assertEqual((manuscript.read_bytes(), markdown.read_bytes()), prior)
        self.assertFalse((self.pub / '.journal.json').exists())
        self.assertFalse((self.pub / '.txn_backup').exists())
        backup = self.pub / '.txn_backup'
        backup.mkdir()
        (backup / 'old.bak').write_bytes(prior[0])
        created = self.pub / 'new.json'
        created.write_text('{}')
        manuscript.write_text('{}')
        self.store._write_json(self.pub / '.journal.json', {'targets': [
            {'path': str(manuscript.relative_to(self.root)), 'existed': True, 'backup': 'old.bak'},
            {'path': str(created.relative_to(self.root)), 'existed': False, 'backup': 'new.bak'}]})
        self.store.load_publishing_state(self.root)
        self.assertEqual(manuscript.read_bytes(), prior[0])
        self.assertFalse(created.exists())
        self.assertFalse(backup.exists())
        with patch('src.fymc.brand_and_catalog.os.fsync', wraps=self.store.os.fsync) as fsync:
            self.store.update_chapter_content(self.root, 1, {'title': 'Durable edit'})
            self.assertGreater(fsync.call_count, 5)
        manifest = json.loads((self.pub / '.commit_manifest.json').read_text())
        import hashlib
        self.assertEqual(manifest['sha256'][str(manuscript.relative_to(self.pub))],
                         hashlib.sha256(manuscript.read_bytes()).hexdigest())
        with self.assertRaises(ValueError):
            self.store._commit_store_transaction(self.root, [(created, {'bad': float('nan')})], [])
        self.assertFalse(created.exists())
        self.assertFalse((self.pub / '.journal.json').exists())

    def test_02_hard_process_exit_recovers_on_next_access(self):
        import subprocess
        import sys
        manuscript = self.volume / 'manuscript.json'
        prior = manuscript.read_bytes()
        script = (
            'import os, signal, sys\n'
            'from pathlib import Path\n'
            'from src.fymc import brand_and_catalog as store\n'
            'def killed_write(*args):\n'
            '    os.kill(os.getpid(), signal.SIGKILL)\n'
            'store._write_text = killed_write\n'
            'store.update_chapter_content(Path(sys.argv[1]), 1, {"title": "Interrupted"})\n'
        )
        result = subprocess.run([sys.executable, '-c', script, str(self.root)],
                                cwd=ROOT, capture_output=True, timeout=30)
        self.assertLess(result.returncode, 0, result.stderr.decode())
        self.assertTrue((self.pub / '.journal.json').exists())
        self.assertNotEqual(manuscript.read_bytes(), prior)
        self.store.load_publishing_state(self.root)
        self.assertEqual(manuscript.read_bytes(), prior)
        self.assertFalse((self.pub / '.journal.json').exists())

    def test_03_workspace_backup_and_symlink_containment(self):
        from src.fymc.research_intelligence import audit_existing_workspace
        from src.fymc.http_routes import _store_revision
        self.assertEqual(audit_existing_workspace(self.root)['backup_details']['backups_dir'],
                         str(self.root / 'backups'))
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / 'external.json'
            target.write_text('{"subscribers": []}')
            link = self.pub / 'site/newsletter_signups.json'
            link.unlink()
            link.symlink_to(target)
            with self.assertRaisesRegex(ValueError, 'escapes workspace root'):
                self.store.record_newsletter_signup(self.root, 'reader@example.com')
            with self.assertRaises(ValueError):
                _store_revision(self.root)
            with self.assertRaises(ValueError):
                audit_existing_workspace(self.root)
            self.assertEqual(target.read_text(), '{"subscribers": []}')
            with self.assertRaises(ValueError):
                self.store._resolve_contained(self.root, self.root / '..' / 'escape')

    def test_04_chapter_revisions_and_editor_inflight_protection(self):
        chapter = self.store.load_publishing_state(self.root)['volume']['manuscript']['chapters'][0]
        revision = chapter['revision']
        self.assertRegex(revision, r'^[0-9a-f]{16}$')
        result = self.store.update_chapter_content(self.root, 1, {'title': 'Revision one'}, revision)
        self.assertTrue(result['ok'])
        self.assertNotEqual(revision, result['chapter']['revision'])
        status, payload = self.route('PATCH', '/api/fymc/manuscript',
                                     {'chapter_number': 1, 'patch': {'title': 'Stale', 'expected_revision': revision}})
        self.assertEqual(status, 409)
        self.assertEqual(payload['error'], 'revision_conflict')
        status, payload = self.route('PATCH', '/api/fymc/manuscript',
                                     {'chapter_number': 1, 'expected_revision': result['chapter']['revision'],
                                      'patch': {'title': 'Revision two'}})
        self.assertEqual(status, 200)
        self.assertNotIn('expected_revision', payload['rejected_fields'])
        editor = (ROOT / 'src/static/studio.html').read_text()
        for marker in ('editSeq++', 'submitSeq=editSeq', 'editSeq===submitSeq',
                       'textarea, #discard-chapter', 'expected_revision:c.revision',
                       'finally {if(!editor.hidden)'):
            self.assertIn(marker, editor)

    def test_05_research_and_manuscript_api_ui_parity(self):
        from unittest.mock import patch
        research = {'topics': [{'title': 'Evidence'}], 'consensus_findings': ['Consensus'],
                    'claims_requiring_verification': ['Verify'], 'permissions_ledger': [],
                    'corpus_metrics': {'videos': 1}, 'coverage': {}, 'schema_version': 2}
        with patch('src.fymc.brand_and_catalog.build_research_database', return_value=research):
            self.store.sync_publishing_store(self.root, abridged_videos=[{'video_id': 'research'}])
        self.store.sync_publishing_store(self.root)
        status, payload = self.route('GET', '/api/fymc/research')
        self.assertEqual(status, 200)
        for key, value in research.items():
            self.assertEqual(payload[key], value)
        self.assertEqual(payload['conflicting_views'], ['Verify'])
        _, payload = self.route('GET', '/api/fymc/manuscript')
        self.assertEqual(payload['chapters'], payload['manuscript']['chapters'])
        self.assertEqual(len(payload['chapters']), 12)
        self.assertIn('state.manuscript?.manuscript ?? state.manuscript',
                      (ROOT / 'src/static/site.html').read_text())

    def test_06_section_alias_content_preserved_across_formats(self):
        from src.fymc.interior_templates import _section_html, _first_table
        from src.fymc.exporters import render_fymc_pdf_bytes, render_fymc_epub_bytes
        section = {'heading': 'Alias section', 'paragraphs': ['ParagraphAlpha'],
                   'body': 'BodyBeta', 'text': ['TextGamma'], 'content': 'ContentDelta',
                   'table': {'headers': ['Cell'], 'rows': [['TableSingular']]},
                   'tables': [{'headers': ['Cell'], 'rows': [['TablePlural']]}],
                   'callout': {'body': 'CalloutSingular', 'items': ['CalloutItem']},
                   'callouts': [{'body': 'CalloutPlural'}], 'notes': ['NotesAlias'],
                   'sop_steps': [{'title': 'StepTitle', 'action': 'StepAction', 'detail': 'StepDetail'}]}
        result = self.store.update_chapter_content(self.root, 1, {'sections': [section]})
        self.assertTrue(result['ok'])
        state = self.store.load_publishing_state(self.root)
        chapter = state['volume']['manuscript']['chapters'][0]
        md = self.store.chapter_to_markdown(chapter)
        html = _section_html(section)
        pdf = render_fymc_pdf_bytes(state).decode('latin-1')
        epub = render_fymc_epub_bytes(state, _art={})
        with zipfile.ZipFile(io.BytesIO(epub)) as archive:
            xhtml = archive.read('OEBPS/chapter_01.xhtml').decode()
        for marker in ('ParagraphAlpha', 'BodyBeta', 'TextGamma', 'ContentDelta',
                       'TableSingular', 'TablePlural', 'CalloutSingular', 'CalloutPlural',
                       'CalloutItem', 'NotesAlias', 'StepTitle', 'StepAction', 'StepDetail'):
            for name, output in [('MD', md), ('HTML', html), ('PDF', pdf), ('EPUB', xhtml)]:
                with self.subTest(marker=marker, format=name):
                    self.assertIn(marker, output)
        self.assertIn('TablePlural', _first_table({'sections': [section]}))
        normalized = self.store._normalize_section({'paragraphs': ['Same'], 'body': 'Same'})
        self.assertEqual(normalized['paragraphs'], ['Same'])

    def test_07_epub_false_zero_and_aligned_table_rows(self):
        from src.fymc.exporters import _markup, _aligned_row_cells, _PDF
        from unittest.mock import patch
        self.assertEqual(_markup(None), '')
        self.assertIn('0', _markup(0))
        self.assertIn('0.0', _markup(0.0))
        self.assertIn('false', _markup(False).lower())
        table = {'headers': ['First Name', 'Score', 'Missing'],
                 'rows': [{'SCORE': 0, 'first_name': 'Ada', 'extra': 'ignore'}]}
        self.assertEqual(_aligned_row_cells(table['rows'][0], table['headers']), ['Ada', 0, ''])
        markup = _markup(table)
        self.assertLess(markup.index('Ada'), markup.index('<p>0</p>'))
        self.assertNotIn('ignore', markup)
        pdf = _PDF('concept_a', 'digital_pdf')
        pdf.new()
        with patch.object(pdf, 'draw') as draw:
            pdf.table(table)
        cells = [call.args[0] for call in draw.call_args_list]
        self.assertEqual(cells[-3:], ['Ada', '0', ''])
        self.assertEqual(_aligned_row_cells({'unrelated': 2}, ['Other']), [2])

    def test_08_huge_funnel_and_nonfinite_geometry(self):
        from src.fymc.diagrams_engine import render_diagram_svg
        from src.fymc.design_concepts import _SVG, get_concept
        from src.fymc.qa_validator import validate_svg_asset
        svg = render_diagram_svg({'chart_type': 'funnel', 'stages': [{'value': 1e308}]})
        self.assertTrue(validate_svg_asset(svg, 'large')['passed'])
        for method, args in [('rect', (0, 0, float('inf'), 1, 'black')),
                             ('line', (0, float('nan'), 1, 1)),
                             ('circle', (0, 0, float('inf'), 'black')),
                             ('text', (float('inf'), 0, 'bad'))]:
            with self.subTest(method=method), self.assertRaises(ValueError):
                getattr(_SVG(100, 100, get_concept('concept_a'), 'Test'), method)(*args)

    def test_09_boundary_inputs_and_clear_graphic_notes(self):
        from src.fymc.research_intelligence import _scan_transcripts, _normalize_video
        from src.fymc.design_concepts import render_scorecard_svg
        directory = self.root / 'transcripts'
        directory.mkdir()
        (directory / 'bad.json').write_text(json.dumps({'metadata': {'lengthSeconds': '1e309'}}))
        self.assertEqual(_scan_transcripts(directory)['total_duration_seconds'], 0)
        self.assertEqual(_normalize_video({'length_seconds': '1e309'}, {})['length_seconds'], 0)
        ET.fromstring(render_scorecard_svg({'scores': {'revenue_potential': 10},
                                           'dimension_max': None, 'score_rationale': None}))
        for value in (-1, True, '5'):
            result = self.store.update_publishing_settings(self.root, {'pricing_hypotheses': {'test': {'price': value}}})
            self.assertIn('pricing_hypotheses.test.price', result['rejected'])
            self.assertNotIn('price', result['pricing_hypotheses']['test'])
        for value in (float('nan'), float('inf')):
            with self.assertRaises(ValueError):
                self.store.update_publishing_settings(self.root, {'pricing_hypotheses': {'test': {'price': value}}})
        self.store.update_graphic_review(self.root, 'cover_front', notes='Keep')
        self.assertEqual(self.store.update_graphic_review(self.root, 'cover_front')['notes'], 'Keep')
        self.assertEqual(self.store.update_graphic_review(self.root, 'cover_front', notes='')['notes'], '')
        self.assertEqual(self.store.update_graphic_review(self.root, 'cover_front', notes=42)['error'], 'invalid_notes')

    def test_10_weak_lock_registry_identity_and_eviction(self):
        import gc
        import weakref
        self.assertIsInstance(self.store._ROOT_LOCKS, weakref.WeakValueDictionary)
        lock = self.store._root_lock(self.root)
        self.assertIs(lock, self.store._root_lock(self.root))
        reference = weakref.ref(lock)
        del lock
        gc.collect()
        self.assertIsNone(reference())
        self.assertNotIn(str(self.root), self.store._ROOT_LOCKS)

    def test_11_appstate_detached_records_and_ingestion_rollback(self):
        from src.app_server import AppState
        from unittest.mock import patch
        state = AppState(self.root / 'data')
        sample = {'video_id': 'old', 'title': 'Sample', 'pro_tips': [{'tip': 'Original'}]}
        state.abridged_list = [sample]
        state.abridged_by_id = {'old': sample}
        for records in (state.search(), state.resolve(None), state.resolve(['old'])):
            records[0]['pro_tips'][0]['tip'] = 'Mutated'
            self.assertEqual(sample['pro_tips'][0]['tip'], 'Original')
        state.abridged_list = []
        state.abridged_by_id = {}
        state.data_dir.mkdir()
        path = state.data_dir / 'custom_videos.json'
        record = {'status': 'ok', 'full_text': 'Some transcript', 'segments': [], 'metadata': {}}
        for prior in (None, b'{"videos": []}\n  '):
            if prior is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(prior)
            with patch('src.app_server.extract_video_urls', return_value=[('new', 'https://example.com')]), \
                 patch('src.app_server.fetch_video', return_value=dict(record)), \
                 patch('src.app_server.abridge_video', return_value={'video_id': 'new'}), \
                 patch.object(state.evidence_index, 'add_record', side_effect=RuntimeError('index failure')):
                result = state.ingest_urls('input')
            self.assertEqual(result['failed_count'], 1)
            self.assertEqual(path.read_bytes() if path.exists() else None, prior)
            self.assertNotIn('new', state.raw_by_id)
            self.assertEqual(state.raw_videos, [])

    def test_12_svg_external_attributes_and_nonfinite_geometry(self):
        from src.fymc.qa_validator import validate_svg_asset
        for attr in ('width="inf"', 'width="-inf"', 'height="infinity"', 'x="nan"',
                     'fill="url(https://evil.example/x)"', 'stroke="url(//evil.example/x)"',
                     'style="@import url(https://evil.example/x)"', 'filter="url(data:text/plain,x)"'):
            with self.subTest(attr=attr):
                svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><rect {attr}/></svg>'
                self.assertFalse(validate_svg_asset(svg, 'malformed')['passed'])

    def test_13_newsletter_and_partial_writers_recover_journal_and_update_manifest(self):
        brand_file = self.pub / 'brand/brand_system.json'
        prior_brand = brand_file.read_bytes()
        orphan = self.pub / 'orphan_crashed.json'
        orphan.write_text('{"stale": true}')
        brand_file.write_text('{"corrupted_mid_crash": true}')
        backup = self.pub / '.txn_backup'
        backup.mkdir(exist_ok=True)
        (backup / '0000.bak').write_bytes(prior_brand)
        self.store._write_json(self.pub / '.journal.json', {'targets': [
            {'path': str(brand_file.relative_to(self.root)), 'existed': True, 'backup': '0000.bak'},
            {'path': str(orphan.relative_to(self.root)), 'existed': False, 'backup': '0001.bak'},
        ]})
        signup = self.store.record_newsletter_signup(self.root, 'ops@example.com', source='unit_test')
        self.assertTrue(signup['ok'])
        self.assertEqual(brand_file.read_bytes(), prior_brand)
        self.assertFalse(orphan.exists())
        self.assertFalse((self.pub / '.journal.json').exists())
        self.assertTrue(self.store.verify_commit_manifest(self.root, strict=True)['passed'])
        review = self.store.update_graphic_review(self.root, 'cover_front', status='approved', notes='Clean plate')
        self.assertEqual(review['status'], 'approved')
        self.assertTrue(self.store.verify_commit_manifest(self.root, strict=True)['passed'])
        settings = self.store.update_publishing_settings(
            self.root,
            {'active_preview_concept': 'concept_b', 'editorial_notes': 'Fact-Checking pass'},
        )
        self.assertEqual(settings['active_preview_concept'], 'concept_b')
        self.assertIn('editorial_notes', settings['applied'])
        self.assertTrue(self.store.verify_commit_manifest(self.root, strict=True)['passed'])

    def test_14_export_hard_crash_recovery_and_manifest_preview_isolation(self):
        import subprocess
        import sys
        from src.fymc.exporters import export_concept_package
        state = self.store.load_publishing_state(self.root)
        export_concept_package(self.root, state, 'concept_a')
        self.assertTrue(self.store.verify_commit_manifest(self.root, strict=True)['passed'])
        preview_dir = self.pub / 'previews/concept_a'
        prior_files = {p.name: p.read_bytes() for p in sorted(preview_dir.iterdir()) if p.is_file()}
        self.assertTrue(prior_files)
        script = (
            'import os, signal, sys\n'
            'from pathlib import Path\n'
            'from src.fymc import brand_and_catalog as store, exporters\n'
            'root = Path(sys.argv[1])\n'
            'state = store.load_publishing_state(root)\n'
            'orig_replace = exporters.os.replace\n'
            'def crash_after_backup(src, dst):\n'
            '    orig_replace(src, dst)\n'
            '    if ".prev." in Path(dst).name:\n'
            '        os.kill(os.getpid(), signal.SIGKILL)\n'
            'exporters.os.replace = crash_after_backup\n'
            'exporters.export_concept_package(root, state, "concept_a")\n'
        )
        result = subprocess.run([sys.executable, '-c', script, str(self.root)],
                                cwd=ROOT, capture_output=True, timeout=60)
        self.assertLess(result.returncode, 0, result.stderr.decode())
        self.assertTrue((self.pub / 'previews/.export_journal_concept_a.json').exists())
        self.assertFalse(preview_dir.exists())
        self.store.load_publishing_state(self.root)
        self.assertTrue(preview_dir.exists())
        restored = {p.name: p.read_bytes() for p in sorted(preview_dir.iterdir()) if p.is_file()}
        self.assertEqual(restored, prior_files)
        leftovers = [p.name for p in (self.pub / 'previews').iterdir()
                     if '.prev.' in p.name or '.stage.' in p.name or p.name.startswith('.export_journal_')]
        self.assertEqual(leftovers, [])
        self.assertTrue(self.store.verify_commit_manifest(self.root, strict=True)['passed'])

    def test_15_strict_manifest_detects_out_of_band_tampering(self):
        loaded = self.store.load_publishing_state(self.root)
        self.assertTrue(loaded['manifest_verified'])
        self.assertTrue(self.store.load_publishing_state(self.root, verify_manifest=True)['manifest_verified'])
        brand_file = self.pub / 'brand/brand_system.json'
        prior = brand_file.read_bytes()
        tampered = json.loads(prior.decode('utf-8'))
        tampered['tagline'] = 'Tampered Out Of Band'
        brand_file.write_text(json.dumps(tampered, indent=2) + '\n', encoding='utf-8')
        self.assertFalse(self.store.load_publishing_state(self.root)['manifest_verified'])
        with self.assertRaises(self.store.CorruptStoreError):
            self.store.load_publishing_state(self.root, verify_manifest=True)
        with self.assertRaises(self.store.CorruptStoreError):
            self.store.verify_commit_manifest(self.root, strict=True)
        brand_file.write_bytes(prior)
        rogue = self.pub / 'rogue_untracked.json'
        rogue.write_text('{"rogue": 1}\n', encoding='utf-8')
        check = self.store.verify_commit_manifest(self.root)
        self.assertFalse(check['passed'])
        self.assertIn('rogue_untracked.json', check['unexpected'])
        with self.assertRaises(self.store.CorruptStoreError):
            self.store.verify_commit_manifest(self.root, strict=True)
        rogue.unlink()
        self.assertTrue(self.store.verify_commit_manifest(self.root, strict=True)['passed'])

    def test_16_appstate_ingest_and_generate_ebook_return_detached_copies(self):
        from src.app_server import AppState
        from unittest.mock import patch
        state = AppState(self.root / 'detached_app_data')
        raw_rec = {
            'status': 'ok',
            'full_text': 'Pro tip: always verify probate docket filings and county surplus ledgers carefully.',
            'segments': [{'start': 12.0, 'duration': 4.0, 'text': 'Pro tip: always verify probate docket filings.'}],
            'metadata': {'title': 'Original Video Title', 'author': 'Court Researcher', 'lengthSeconds': '180'},
        }
        with patch('src.app_server.extract_video_urls', return_value=[('vid00000001', 'https://youtu.be/vid00000001')]), \
             patch('src.app_server.fetch_video', return_value=dict(raw_rec)):
            first = state.ingest_urls('https://youtu.be/vid00000001')
        self.assertEqual(first['results'][0]['status'], 'ok')
        first['results'][0]['video']['title'] = 'Mutated By Caller'
        first['results'][0]['video']['pro_tips'].append({'tip': 'Injected'})
        self.assertEqual(state.abridged_by_id['vid00000001']['title'], 'Original Video Title')
        self.assertNotIn({'tip': 'Injected'}, state.abridged_by_id['vid00000001']['pro_tips'])
        with patch('src.app_server.extract_video_urls', return_value=[('vid00000001', 'https://youtu.be/vid00000001')]):
            second = state.ingest_urls('https://youtu.be/vid00000001')
        self.assertEqual(second['results'][0]['status'], 'cached')
        second['results'][0]['video']['title'] = 'Mutated Cached Copy'
        self.assertEqual(state.abridged_by_id['vid00000001']['title'], 'Original Video Title')
        ebook = state.generate_ebook(title='Playbook Draft')
        self.assertEqual(state.last_ebook, ebook)
        self.assertIsNot(state.last_ebook, ebook)
        orig_caption = state.last_ebook['exhibits'][0]['caption']
        ebook['exhibits'][0]['caption'] = 'Mutated Exhibit Caption'
        self.assertEqual(state.last_ebook['exhibits'][0]['caption'], orig_caption)
        self.assertEqual(state.abridged_by_id['vid00000001']['title'], 'Original Video Title')

    def test_17_tables_bullets_and_citations_across_all_renderers(self):
        from src.fymc.interior_templates import render_interior_page_html
        from src.fymc.exporters import render_fymc_pdf_bytes, render_fymc_epub_bytes
        patch_payload = {
            'sections': [
                {
                    'heading': 'Jurisdictional Caps',
                    'paragraphs': ['Lead analysis paragraph.'],
                    'bullets': ['BulletOne'],
                    'points': ['PointTwo'],
                    'takeaways': ['TakeawayThree'],
                    'table': {
                        'caption': 'Statutory Fee Matrix',
                        'columns': ['State Code', 'Fee Cap', 'Statute Note'],
                        'rows': [{'state_code': 'CA', 'FEE_CAP': '10%', 'statute_note': 'CCP 1582'}],
                    },
                },
                {
                    'heading': 'Secondary Economics',
                    'paragraphs': ['Second section paragraph.'],
                    'table': {
                        'caption': 'Unit Margin Table',
                        'rows': [{'MetricName': 'NetMargin', 'MetricVal': '37.5%'}],
                    },
                },
            ],
            'statutory_citations': [{'statute': 'Cal. Civ. Proc. Code 1582', 'summary': 'Ten percent cap'}],
            'source_citations': [{
                'video_id': 'vid123',
                'timestamp_label': '00:14:22',
                'text': 'Verify docket first',
                'relevance': 'Core probate check',
            }],
        }
        res = self.store.update_chapter_content(self.root, 1, patch_payload)
        self.assertTrue(res['ok'])
        state = self.store.load_publishing_state(self.root)
        manuscript = state['volume']['manuscript']
        chapter = manuscript['chapters'][0]
        md = self.store.chapter_to_markdown(chapter)
        fin_html = render_interior_page_html(
            'financial_breakdown', 'concept_a', manuscript, state['volume']['scorecard'], [], chapter_number=1
        )
        cmp_html = render_interior_page_html(
            'comparison_table', 'concept_b', manuscript, state['volume']['scorecard'], [], chapter_number=1
        )
        pdf = render_fymc_pdf_bytes(state).decode('latin-1')
        epub = render_fymc_epub_bytes(state, _art={})
        with zipfile.ZipFile(io.BytesIO(epub)) as archive:
            xhtml = archive.read('OEBPS/chapter_01.xhtml').decode('utf-8')
        for marker in ('BulletOne', 'PointTwo', 'TakeawayThree', 'Statutory Fee Matrix',
                       'Unit Margin Table', 'CCP 1582', 'NetMargin', '37.5%'):
            for fmt_name, content in [('MD', md), ('FIN_HTML', fin_html), ('CMP_HTML', cmp_html), ('PDF', pdf), ('EPUB', xhtml)]:
                with self.subTest(marker=marker, format=fmt_name):
                    self.assertIn(marker, content)
        self.assertEqual(fin_html.count('CCP 1582'), 1)
        self.assertEqual(cmp_html.count('CCP 1582'), 1)
        for cite_marker in ('Cal. Civ. Proc. Code 1582', 'Ten percent cap',
                            '00:14:22', 'Verify docket first', 'Core probate check'):
            for fmt_name, content in [('MD', md), ('FIN_HTML', fin_html), ('CMP_HTML', cmp_html), ('PDF', pdf), ('EPUB', xhtml)]:
                with self.subTest(cite_marker=cite_marker, format=fmt_name):
                    self.assertIn(cite_marker, content)

    def test_18_word_count_recomputed_on_chapter_update_and_merge(self):
        from src.fymc.volume_001_manuscript import compute_manuscript_word_count
        before = self.store.load_publishing_state(self.root)['volume']['manuscript']
        initial_words = before['total_word_count']
        self.assertEqual(initial_words, compute_manuscript_word_count(before['chapters']))
        extra_paragraph = ' '.join(f'lexicon{i}' for i in range(240))
        chapter_sections = list(before['chapters'][0]['sections']) + [{
            'heading': 'Expanded Verification Notes',
            'paragraphs': [extra_paragraph],
        }]
        updated = self.store.update_chapter_content(self.root, 1, {'sections': chapter_sections})
        self.assertTrue(updated['ok'])
        after = self.store.load_publishing_state(self.root)['volume']['manuscript']
        self.assertEqual(after['total_word_count'], compute_manuscript_word_count(after['chapters']))
        self.assertGreaterEqual(after['total_word_count'] - initial_words, 240)
        self.store.sync_publishing_store(self.root)
        merged = self.store.load_publishing_state(self.root)['volume']['manuscript']
        self.assertEqual(merged['total_word_count'], compute_manuscript_word_count(merged['chapters']))
        self.assertEqual(merged['chapter_count'], len(merged['chapters']))

    def test_19_score_zero_and_alias_precedence_across_cover_plate_and_html(self):
        from src.fymc.scorecard_engine import resolve_score_value
        from src.fymc.cover_and_mockups import render_cover_or_mockup_svg
        from src.fymc.design_concepts import render_scorecard_svg
        from src.fymc.interior_templates import render_interior_page_html
        manuscript = {'title': 'Test Volume', 'chapters': [{'chapter_number': 1, 'title': 'Chapter One'}]}
        cases = [
            ({'total_score': 0}, 0),
            ({'composite_score': 64}, 64),
            ({'money_to_manpower_score': '72 / 100', 'total_score': 87}, 72),
        ]
        for scorecard, expected in cases:
            with self.subTest(scorecard=scorecard):
                self.assertEqual(resolve_score_value(scorecard, default=87), expected)
                cover_svg = render_cover_or_mockup_svg('concept_c', '01_front_cover', {'title': 'Test'}, scorecard)
                plate_a = render_scorecard_svg(scorecard, 'concept_a')
                plate_b = render_scorecard_svg(scorecard, 'concept_b')
                plate_c = render_scorecard_svg(scorecard, 'concept_c')
                page_html = render_interior_page_html('scorecard_page', 'concept_a', manuscript, scorecard, [])
                self.assertIn(f'{expected} / 100', cover_svg)
                self.assertIn(f'>{expected}</tspan>', plate_a)
                self.assertIn('OF 100', plate_a)
                self.assertIn(f'{expected} / 100', plate_b)
                self.assertIn(f'>{expected}</tspan>', plate_c)
                self.assertIn('Composite / 100', plate_c)
                self.assertIn(f'<tr><td>Total Score</td><td>{expected}</td></tr>', page_html)

    def test_20_raw_metadata_backfill_in_normalize_video(self):
        from src.fymc.research_intelligence import _normalize_video
        normalized = _normalize_video(
            {'video_id': 'meta123'},
            {'meta123': {'metadata': {'title': 'Probate Deep Dive', 'author': 'Clerk Insider', 'lengthSeconds': '1845'}}},
        )
        self.assertEqual(normalized['title'], 'Probate Deep Dive')
        self.assertEqual(normalized['author'], 'Clerk Insider')
        self.assertEqual(normalized['length_seconds'], 1845)

    def test_21_astra_round5_hardening_probes(self):
        import os
        from unittest.mock import patch
        from src.fymc.exporters import _PDF, export_concept_package
        from src.fymc.qa_validator import validate_svg_asset
        from src.fymc.scorecard_engine import resolve_score_value

        # 1. Wide 50-column digital & print tables render without hanging.
        wide = {
            'caption': 'Fifty Column Stress Table',
            'headers': [f'C{i}' for i in range(50)],
            'rows': [[f'val{i}' for i in range(50)]],
        }
        for fmt in ('digital_pdf', 'print_6x9_pdf'):
            pdf = _PDF('concept_a', fmt)
            pdf.new('Wide')
            pdf.table(wide)
            rendered = pdf.finish()
            self.assertTrue(rendered.startswith(b'%PDF-1.4'))
            self.assertIn(b'Fifty Column Stress Table', rendered)

        # 2. Post-swap _fsync_dir failure rolls back cleanly without ENOTEMPTY.
        state = self.store.load_publishing_state(self.root)
        export_concept_package(self.root, state, 'concept_a')
        preview_dir = self.pub / 'previews/concept_a'
        marker = preview_dir / 'sentinel.txt'
        marker.write_bytes(b'prior-version')
        orig_replace = os.replace
        swapped = {'done': False}

        def tracked_replace(src, dst):
            orig_replace(src, dst)
            if Path(dst) == preview_dir and '.stage.' in Path(src).name:
                swapped['done'] = True

        orig_fsync = self.store._fsync_dir

        def fail_after_swap(dpath):
            if swapped['done']:
                raise OSError('post-swap directory fsync failure')
            return orig_fsync(dpath)

        with patch('src.fymc.exporters.os.replace', side_effect=tracked_replace), \
             patch('src.fymc.exporters._fsync_dir', side_effect=fail_after_swap):
            with self.assertRaises(OSError):
                export_concept_package(self.root, state, 'concept_a')
        self.assertTrue((preview_dir / 'sentinel.txt').exists())
        self.assertEqual((preview_dir / 'sentinel.txt').read_bytes(), b'prior-version')
        self.assertFalse((self.pub / 'previews/.export_journal_concept_a.json').exists())

        # 3. Malformed export journal with '..' or invalid backup/stage names fails closed.
        bad_journal = self.pub / 'previews/.export_journal_concept_a.json'
        bad_journal.write_text(json.dumps({
            'concept_id': 'concept_a',
            'target': 'concept_a',
            'stage': 'concept_a.stage.bad',
            'backup': '..',
        }), encoding='utf-8')
        with self.assertRaises(self.store.CorruptStoreError):
            self.store._recover_export_journals(self.root)
        self.assertTrue((self.pub / 'brand/brand_system.json').exists())
        bad_journal.unlink()

        # 4. SVG validator blocks relative, file:, and CSS-escaped URLs while allowing internal #id refs.
        ok_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><defs><linearGradient id="g1"/></defs><rect fill="url(#g1)"/></svg>'
        self.assertTrue(validate_svg_asset(ok_svg, 'internal_grad')['passed'])
        for bad_frag in (
            '<use href="external.svg#icon"/>',
            '<rect fill="url(relative.svg#grad)"/>',
            '<rect fill="url(file:///etc/passwd)"/>',
            '<rect style="fill:\\75\\72\\6c(https://evil.example/a)"/>',
            '<style>\\40 import "https://evil.example/x.css";</style>',
            '<feImage href="https://evil.example/a.png"/>',
        ):
            with self.subTest(bad_frag=bad_frag):
                bad_svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10">{bad_frag}</svg>'
                self.assertFalse(validate_svg_asset(bad_svg, 'bad_svg')['passed'])

        # 5. Forked child cannot bypass parent's held _RootLock.
        if hasattr(os, 'fork'):
            lock = self.store._root_lock(self.root)
            with lock:
                rfd, wfd = os.pipe()
                pid = os.fork()
                if pid == 0:
                    try:
                        os.close(rfd)
                        acquired = lock.acquire(blocking=False)
                        os.write(wfd, b'1' if acquired else b'0')
                        os.close(wfd)
                    finally:
                        os._exit(0)
                os.close(wfd)
                child_byte = os.read(rfd, 1)
                os.close(rfd)
                os.waitpid(pid, 0)
                self.assertEqual(child_byte, b'0')

        # 6. Oversized integer scores do not raise OverflowError.
        self.assertEqual(resolve_score_value({'total_score': 10 ** 400}, default=87), 87)
        self.assertEqual(resolve_score_value({'money_to_manpower_score': 10 ** 400, 'score': 75}, default=87), 75)

    def test_22_astra_round6_hardening_probes(self):
        import os
        import shutil
        import threading
        from unittest.mock import patch
        from src.fymc.exporters import export_concept_package
        from src.fymc.qa_validator import validate_svg_asset

        # 1. First-export post-swap OSError removes newly swapped directory and leaves zero journal.
        state = self.store.load_publishing_state(self.root)
        first_dir = self.pub / 'previews/concept_b'
        if first_dir.exists():
            shutil.rmtree(first_dir)
        orig_replace = os.replace
        orig_fsync = self.store._fsync_dir
        swapped = {'done': False}

        def track_first_swap(src, dst):
            res = orig_replace(src, dst)
            if Path(dst) == first_dir:
                swapped['done'] = True
            return res

        def fail_post_first_swap(dpath):
            if swapped['done'] and Path(dpath) == (self.pub / 'previews'):
                swapped['done'] = False
                raise OSError('simulated post-swap fsync failure on first export')
            return orig_fsync(dpath)

        with patch('src.fymc.exporters.os.replace', side_effect=track_first_swap), \
             patch('src.fymc.exporters._fsync_dir', side_effect=fail_post_first_swap):
            with self.assertRaises(OSError):
                export_concept_package(self.root, state, 'concept_b')
        self.assertFalse(first_dir.exists())
        self.assertFalse((self.pub / 'previews/.export_journal_concept_b.json').exists())

        # 2. SVG validator allows XML declaration but blocks xml-stylesheet PI and xml:base bypasses.
        xml_decl_svg = '<?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><rect width="5" height="5"/></svg>'
        self.assertTrue(validate_svg_asset(xml_decl_svg, 'decl_ok')['passed'])
        for bypass_svg in (
            '<?xml-stylesheet type="text/css" href="https://evil.example/a.css"?><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><rect width="5" height="5"/></svg>',
            '<?xml version="1.0" encoding="UTF-8"?><?xml-stylesheet type="text/css" href="https://evil.example/a.css"?><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><rect width="5" height="5"/></svg>',
            '<svg xmlns="http://www.w3.org/2000/svg" xml:base="https://evil.example/" viewBox="0 0 10 10"><use href="#x"/></svg>',
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><g xml:base="https://evil.example/"><use href="#x"/></g></svg>',
        ):
            with self.subTest(bypass_svg=bypass_svg):
                self.assertFalse(validate_svg_asset(bypass_svg, 'bypass_svg')['passed'])

        # 3. Forking while another thread holds _ROOT_LOCKS_GUARD does not deadlock child _root_lock().
        if hasattr(os, 'fork'):
            acquired_guard = threading.Event()
            release_guard = threading.Event()

            def hold_guard():
                with self.store._ROOT_LOCKS_GUARD:
                    acquired_guard.set()
                    release_guard.wait(timeout=10)

            holder = threading.Thread(target=hold_guard, daemon=True)
            holder.start()
            self.assertTrue(acquired_guard.wait(timeout=5))
            rfd, wfd = os.pipe()
            try:
                pid = os.fork()
                if pid == 0:
                    try:
                        os.close(rfd)
                        child_lock = self.store._root_lock(self.root)
                        ok = child_lock.acquire(blocking=False)
                        if ok:
                            child_lock.release()
                        os.write(wfd, b'1' if ok else b'0')
                        os.close(wfd)
                    finally:
                        os._exit(0)
                os.close(wfd)
                wfd = -1
            finally:
                release_guard.set()
                holder.join(timeout=5)
            child_out = os.read(rfd, 1)
            os.close(rfd)
            _, status = os.waitpid(pid, 0)
            self.assertEqual(status, 0)
            self.assertEqual(child_out, b'1')

    def test_23_astra_round7_hardening_probes(self):
        import gc
        import os
        import shutil
        import subprocess
        import sys
        from unittest.mock import patch
        from src.fymc import exporters
        from src.fymc.qa_validator import validate_svg_asset

        # 1. Interrupted post-commit backup cleanup keeps new export intact and sweeps orphan .prev.
        target = self.pub / 'previews/concept_a'
        target.mkdir(parents=True, exist_ok=True)
        (target / 'old_one.txt').write_text('original one', encoding='utf-8')
        (target / 'old_two.txt').write_text('original two', encoding='utf-8')
        real_rmtree = shutil.rmtree

        def partial_cleanup(path, *args, **kwargs):
            p = Path(path)
            if p.name.startswith('concept_a.prev.'):
                (p / 'old_one.txt').unlink(missing_ok=True)
                raise OSError('simulated backup cleanup interruption')
            return real_rmtree(p, *args, **kwargs)

        with patch.object(exporters, '_package_files', return_value={'new.txt': b'complete new export'}), \
             patch.object(exporters.shutil, 'rmtree', side_effect=partial_cleanup):
            with self.assertRaises(OSError):
                exporters.export_concept_package(self.root, {}, 'concept_a')
        self.assertFalse((target.parent / '.export_journal_concept_a.json').exists())
        self.assertEqual(sorted(p.name for p in target.iterdir()), ['bundle.zip', 'new.txt'])
        with self.store._root_lock(self.root):
            self.store._recover_export_journals(self.root)
        self.assertEqual(sorted(p.name for p in target.iterdir()), ['bundle.zip', 'new.txt'])
        self.assertEqual([p.name for p in target.parent.iterdir() if '.prev.' in p.name], [])

        # 2. Valid Unicode internal SVG fragment url(#café) passes while external URLs still fail.
        unicode_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><defs><linearGradient id="caf\u00e9"/></defs><rect fill="url(#caf\u00e9)"/></svg>'
        self.assertTrue(validate_svg_asset(unicode_svg, 'unicode_internal')['passed'])
        self.assertFalse(validate_svg_asset('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><rect fill="url(other.svg#caf\u00e9)"/></svg>', 'ext_unicode')['passed'])

        # 3. Forked child releases inherited lock descriptor immediately so abrupt parent exit never strands flock.
        if hasattr(os, 'fork'):
            script = (
                'import gc, os, sys, time\n'
                'from pathlib import Path\n'
                'from src.fymc import brand_and_catalog as store\n'
                'root = Path(sys.argv[1]).resolve()\n'
                'r_ready, w_ready = os.pipe()\n'
                'r_res, w_res = os.pipe()\n'
                'pid = os.fork()\n'
                'if pid > 0:\n'
                '    os.close(w_ready); os.close(w_res)\n'
                '    os.read(r_ready, 1); os.close(r_ready)\n'
                '    out = os.read(r_res, 1); os.close(r_res)\n'
                '    os.waitpid(pid, 0)\n'
                '    sys.stdout.buffer.write(out)\n'
                '    sys.exit(0)\n'
                'os.close(r_ready); os.close(r_res)\n'
                'lock = store._root_lock(root)\n'
                'assert lock.acquire(blocking=False)\n'
                'gcid = os.fork()\n'
                'if gcid > 0:\n'
                '    os.close(w_ready); os.close(w_res)\n'
                '    os._exit(0)\n'
                'del lock\n'
                'gc.collect()\n'
                'os.write(w_ready, b"r"); os.close(w_ready)\n'
                'deadline = time.monotonic() + 2.0\n'
                'acquired = False\n'
                'while time.monotonic() < deadline and not acquired:\n'
                '    fresh = store._root_lock(root)\n'
                '    acquired = fresh.acquire(blocking=False)\n'
                '    if acquired:\n'
                '        fresh.release()\n'
                '        break\n'
                '    time.sleep(0.02)\n'
                'os.write(w_res, b"1" if acquired else b"0")\n'
                'os.close(w_res)\n'
                'os._exit(0)\n'
            )
            proc = subprocess.run([sys.executable, '-c', script, str(self.root)],
                                  cwd=ROOT, capture_output=True, timeout=15)
            self.assertEqual(proc.returncode, 0, proc.stderr.decode())
            self.assertEqual(proc.stdout, b'1')

    def test_24_astra_round8_hardening_probes(self):
        import os
        import re
        import subprocess
        import sys
        from src.fymc.exporters import _PDF, _width

        # 1. Wide 50- and 100-column PDF tables contain every glyph strictly inside cell boundaries.
        for concept in ('concept_a', 'concept_b', 'concept_c'):
            for mode in ('digital_pdf', 'print_6x9_pdf'):
                for ncols in (50, 100):
                    for header in ('C', 'W', '@', '%', 'WWW'):
                        pdf = _PDF(concept, mode)
                        pdf.new('Wide')
                        draws = []
                        orig_draw = pdf.draw

                        def record(text, x, y, size=10, font=1, _orig=orig_draw, _draws=draws):
                            _draws.append((text, x, y, size, font))
                            _orig(text, x, y, size, font)

                        pdf.draw = record
                        pdf.table({'headers': [header] * ncols, 'rows': [['WM@%'] * ncols]})
                        cw = pdf.usable / ncols
                        for idx, (text, x, y, size, font) in enumerate(draws):
                            if text:
                                right = x + _width(text, pdf.fonts[font], size)
                                boundary = pdf.left + (idx % ncols + 1) * cw
                                self.assertLessEqual(right, boundary + 1e-6, (concept, mode, ncols, header, right, boundary))
                                self.assertLessEqual(round(x, 2) + _width(text, pdf.fonts[font], size), boundary + 1e-6)
                        rendered = pdf.finish()
                        self.assertTrue(rendered.startswith(b'%PDF-1.4'))
                        self.assertIsNone(re.search(rb'\de[-+]\d+\s+Tf', rendered, re.I))

        # 2. Forking concurrently with os.open() inside _RootLock.acquire() never leaks an unregistered fd.
        if hasattr(os, 'fork'):
            script = (
                'import os, sys, threading, time\n'
                'from pathlib import Path\n'
                'from src.fymc import brand_and_catalog as store\n'
                'root = Path(sys.argv[1]).resolve()\n'
                'r_child_alive, w_child_alive = os.pipe()\n'
                'r_hold_child, w_hold_child = os.pipe()\n'
                'parent_pid = os.fork()\n'
                'if parent_pid > 0:\n'
                '    os.close(w_child_alive); os.close(r_hold_child)\n'
                '    assert os.read(r_child_alive, 1) == b"c"\n'
                '    os.close(r_child_alive)\n'
                '    os.waitpid(parent_pid, 0)\n'
                '    contender = store._root_lock(root)\n'
                '    ok = contender.acquire(blocking=False)\n'
                '    if ok:\n'
                '        contender.release()\n'
                '    os.write(w_hold_child, b"x")\n'
                '    os.close(w_hold_child)\n'
                '    sys.stdout.buffer.write(b"1" if ok else b"0")\n'
                '    sys.exit(0)\n'
                'os.close(r_child_alive); os.close(w_hold_child)\n'
                'real_open = os.open\n'
                'entered_open = threading.Event()\n'
                'fork_called = threading.Event()\n'
                'def slow_open(path, flags, mode=0o777):\n'
                '    fd = real_open(path, flags, mode)\n'
                '    entered_open.set()\n'
                '    fork_called.wait(timeout=0.08)\n'
                '    return fd\n'
                'store.os.open = slow_open\n'
                'lock = store._root_lock(root)\n'
                'acquired_evt = threading.Event()\n'
                'def worker():\n'
                '    assert lock.acquire(blocking=True)\n'
                '    acquired_evt.set()\n'
                '    time.sleep(5)\n'
                't = threading.Thread(target=worker, daemon=True)\n'
                't.start()\n'
                'assert entered_open.wait(timeout=2)\n'
                'fork_called.set()\n'
                'cid = os.fork()\n'
                'if cid == 0:\n'
                '    os.write(w_child_alive, b"c")\n'
                '    os.close(w_child_alive)\n'
                '    os.read(r_hold_child, 1)\n'
                '    os.close(r_hold_child)\n'
                '    os._exit(0)\n'
                'os.close(w_child_alive); os.close(r_hold_child)\n'
                'assert acquired_evt.wait(timeout=2)\n'
                'os._exit(0)\n'
            )
            proc = subprocess.run([sys.executable, '-c', script, str(self.root)],
                                  cwd=ROOT, capture_output=True, timeout=15)
            self.assertEqual(proc.returncode, 0, proc.stderr.decode())
            self.assertEqual(proc.stdout, b'1')

    def test_25_astra_round9_hardening_probes(self):
        import io
        import os
        import zipfile
        from src.fymc.exporters import render_fymc_epub_bytes, render_fymc_pdf_bytes
        from src.fymc.interior_templates import render_interior_page_html

        # 1. Deleting a committed file causes load_publishing_state(verify_manifest=True) to fail closed.
        self.store.update_publishing_settings(
            self.root,
            {'pricing_hypotheses': {'digital_edition': {'range_label': '$25-$39', 'test_price_usd': 123.45}}},
        )
        brand_path = self.pub / 'brand/brand_system.json'
        saved_brand = brand_path.read_bytes()
        brand_path.unlink()
        try:
            with self.assertRaises(self.store.CorruptStoreError):
                self.store.load_publishing_state(self.root, verify_manifest=True)
            self.assertFalse(brand_path.exists())
        finally:
            brand_path.write_bytes(saved_brand)
        restored = self.store.load_publishing_state(self.root, verify_manifest=True)
        self.assertEqual(
            restored['brand_system']['pricing_hypotheses']['digital_edition']['test_price_usd'],
            123.45,
        )

        # 2. Retained _RootLock instance across os.fork() stays in _ROOT_LOCKS and re-enters without self-deadlock.
        if hasattr(os, 'fork'):
            retained_lock = self.store._root_lock(self.root)
            rfd, wfd = os.pipe()
            pid = os.fork()
            if pid == 0:
                try:
                    os.close(rfd)
                    with retained_lock:
                        check = self.store.verify_commit_manifest(self.root, strict=True)
                        ok = check['passed'] and (retained_lock is self.store._root_lock(self.root))
                    os.write(wfd, b'1' if ok else b'0')
                    os.close(wfd)
                finally:
                    os._exit(0)
            os.close(wfd)
            child_byte = os.read(rfd, 1)
            os.close(rfd)
            _, status = os.waitpid(pid, 0)
            self.assertEqual(status, 0)
            self.assertEqual(child_byte, b'1')

        # 3. Citation `tip` text is preserved across Markdown, HTML, PDF, and EPUB.
        marker = 'CITETEXTMARKER'
        citation = {
            'title': 'CITETITLEMARKER',
            'tip': marker,
            'timestamp_label': '00:14:22',
            'url': 'https://example.com/?t=862',
            'relevance': 'CITERELEVANCEMARKER',
        }
        res = self.store.update_chapter_content(self.root, 1, {'source_citations': [citation]})
        self.assertTrue(res['ok'])
        state = self.store.load_publishing_state(self.root, verify_manifest=True)
        manuscript = state['volume']['manuscript']
        chapter = manuscript['chapters'][0]
        md = self.store.chapter_to_markdown(chapter)
        html_out = render_interior_page_html(
            'chapter_opener', 'concept_a', manuscript, state['volume']['scorecard'], [], chapter_number=1
        )
        pdf_out = render_fymc_pdf_bytes(state).decode('latin-1')
        with zipfile.ZipFile(io.BytesIO(render_fymc_epub_bytes(state, _art={}))) as book:
            epub_out = book.read('OEBPS/chapter_01.xhtml').decode('utf-8')
        for fmt_name, content in (('Markdown', md), ('HTML', html_out), ('PDF', pdf_out), ('EPUB', epub_out)):
            with self.subTest(fmt_name=fmt_name):
                self.assertIn(marker, content)
                self.assertIn('CITERELEVANCEMARKER', content)

        # 4. SMIL animated links and non-SVG namespace elements are rejected by validate_svg_asset.
        from src.fymc.qa_validator import validate_svg_asset
        for smil_frag in (
            '<a href="https://example.invalid/">link</a>',
            '<a href="#safe"><set attributeName="href" to="https://example.invalid/"/><text x="1" y="5">link</text></a>',
            '<a href="#safe"><animate attributeName="href" values="javascript:alert(1)"/><text x="1" y="5">link</text></a>',
            '<rect width="5" height="5"><set attributeName="fill" to="url(https://example.invalid/x)"/></rect>',
            '<rect width="5" height="5"><animateTransform attributeName="transform" type="scale" from="1" to="2"/></rect>',
            '<use href="#"/>',
            '<style><g/>@import url(javascript:alert(1));</style>',
            '<style><g/>@import url(vbscript:msgbox(1));</style>',
            '<style><g/>@import url(data:text/css,rect%7Bfill:red%7D);</style>',
            '<style><g/>@import url(file:///tmp/a.css);</style>',
            '<style>svg { background-image: image-set("http://127.0.0.1:8765/probe.png" 1x); }</style><rect width="10" height="10"/>',
            '<style>svg { background-image: -webkit-image-set("/probe.png" 1x); }</style><rect width="10" height="10"/>',
            '<rect width="10" height="10" style="mask-image: -webkit-image-set(\'/probe.png\' 1x)"/>',
            '<style>svg { background-image: cross-fade(url(#a), "/probe.png", 50%); }</style><rect width="10" height="10"/>',
            '<style>svg { background-image: image("/probe.png"); }</style><rect width="10" height="10"/>',
            '<style>@font-face { font-family: x; src: local("Arial"); }</style><rect width="10" height="10"/>',
        ):
            with self.subTest(smil_frag=smil_frag):
                bad_svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10">{smil_frag}</svg>'
                self.assertFalse(validate_svg_asset(bad_svg, 'smil_bad')['passed'])

    def test_26_expert_youtube_links_floor_150_200(self) -> None:
        from copy import deepcopy
        import re
        from src.fymc import (
            MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
            MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
            TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        )
        from src.fymc.volume_001_manuscript import build_volume_001_manuscript
        from src.fymc.qa_validator import validate_manuscript_youtube_links

        self.assertEqual(MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK, 150)
        self.assertEqual(MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER, 12)
        self.assertEqual(TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK, "150-200+")

        ms = build_volume_001_manuscript()
        self.assertGreaterEqual(ms["expert_youtube_link_count"], 150)
        self.assertEqual(ms["expert_youtube_link_count"], 180)
        channels = set()
        for ch in ms["chapters"]:
            cites = ch["source_citations"]
            self.assertGreaterEqual(len(cites), 12)
            self.assertEqual(len(cites), 15)
            for c in cites:
                self.assertIn("https://www.youtube.com/watch?v=", c["url"])
                self.assertIn("&t=", c["url"])
                if c.get("channel"):
                    channels.add(c["channel"])
        self.assertEqual(len(channels), 59)

        report = validate_manuscript_youtube_links(ms)
        self.assertTrue(report["passed"], report)
        self.assertEqual(report["unique_links"], 180)

        # Boundary check: 11 links in chapter 1 fails per-chapter floor
        under_chapter = deepcopy(ms)
        under_chapter["chapters"][0]["source_citations"] = under_chapter["chapters"][0]["source_citations"][:11]
        rep_under_ch = validate_manuscript_youtube_links(under_chapter)
        self.assertFalse(rep_under_ch["passed"])
        self.assertTrue(any("Chapter Q1" in issue for issue in rep_under_ch["issues"]))

        # Boundary check: 12 per chapter * 12 = 144 (< 150 per-book floor) fails per-book floor
        under_book = deepcopy(ms)
        for ch in under_book["chapters"]:
            ch["source_citations"] = ch["source_citations"][:12]
        rep_under_book = validate_manuscript_youtube_links(under_book)
        self.assertFalse(rep_under_book["passed"])
        self.assertEqual(rep_under_book["unique_links"], 144)
        self.assertTrue(any("below minimum floor of 150" in issue for issue in rep_under_book["issues"]))

        # Untimestamped URLs, FTP URLs, invalid ports, and non-YouTube URLs are rejected even if timestamp_seconds metadata is present
        from src.fymc import parse_expert_youtube_deep_link
        for bad_u in (
            "https://www.youtube.com/watch?v=1AMk1-SB5ic",
            "ftp://www.youtube.com/watch?v=1AMk1-SB5ic&t=10s",
            "https://www.youtube.com:invalid/watch?v=1AMk1-SB5ic&t=10s",
            "https://www.youtube.com:99999/watch?v=1AMk1-SB5ic&t=10s",
            "https://www.youtube.com:443/watch?v=1AMk1-SB5ic&t=10s",
        ):
            self.assertIsNone(parse_expert_youtube_deep_link(bad_u), bad_u)
        bad_urls_ms = deepcopy(ms)
        for idx, ch in enumerate(bad_urls_ms["chapters"]):
            for c_idx, c in enumerate(ch["source_citations"]):
                c["url"] = (
                    "https://www.youtube.com/watch?v=1AMk1-SB5ic"
                    if c_idx % 3 == 0
                    else (
                        "https://www.youtube.com:invalid/watch?v=1AMk1-SB5ic&t=10s"
                        if c_idx % 3 == 1
                        else "https://www.youtube.com:99999/watch?v=1AMk1-SB5ic&t=10s"
                    )
                )
        rep_bad_urls = validate_manuscript_youtube_links(bad_urls_ms)
        self.assertFalse(rep_bad_urls["passed"])
        self.assertEqual(rep_bad_urls["unique_links"], 0)

        # Updating chapter source_citations updates both manuscript and metadata counts consistently and ignores non-YouTube citations
        non_yt = [{"title": f"Non-YT {i}", "url": f"https://example.com/source-{i}", "text": "Note"} for i in range(20)]
        upd_res = self.store.update_chapter_content(self.root, 1, {"source_citations": non_yt})
        self.assertEqual(upd_res["expert_youtube_link_count"], 165)
        st_after = self.store.load_publishing_state(self.root, verify_manifest=True)
        self.assertEqual(st_after["volume"]["manuscript"]["expert_youtube_link_count"], 165)
        self.assertEqual(st_after["volume"]["metadata"]["expert_youtube_link_count"], 165)

        # Restore full 180 citations and verify clickable links across exported PDF and EPUB editions
        self.store.update_chapter_content(self.root, 1, {"source_citations": ms["chapters"][0]["source_citations"]})
        st_full = self.store.load_publishing_state(self.root, verify_manifest=True)
        self.assertEqual(st_full["volume"]["manuscript"]["expert_youtube_link_count"], 180)
        self.assertEqual(st_full["volume"]["metadata"]["expert_youtube_link_count"], 180)
        from src.fymc.exporters import render_fymc_pdf_bytes, render_fymc_epub_bytes, _wrap_with_links
        from src.fymc.qa_validator import validate_pdf_bytes, validate_epub_bytes
        for mode in ("digital_pdf", "print_6x9_pdf", "workbook_pdf"):
            raw_pdf = render_fymc_pdf_bytes(st_full, "concept_b", mode)
            pdf_rep = validate_pdf_bytes(raw_pdf, mode)
            self.assertTrue(pdf_rep["passed"], pdf_rep)
            self.assertEqual(pdf_rep["youtube_link_count"], 180)
            # Stripping /Annots from pages drops reachable clickable links to 0
            stripped_pdf = re.sub(rb'/Annots\s*\[[^\]]*\]', lambda m: b' ' * len(m.group(0)), raw_pdf)
            self.assertEqual(validate_pdf_bytes(stripped_pdf, mode)["youtube_link_count"], 0)
        epub_rep = validate_epub_bytes(render_fymc_epub_bytes(st_full, "concept_b"))
        self.assertTrue(epub_rep["passed"], epub_rep)
        self.assertEqual(epub_rep["youtube_link_count"], 180)

        # Wrapped long URL preserves full timestamped target on every fragment; two URLs on one line get distinct x-bounds
        long_url = "https://www.youtube.com/watch?v=1AMk1-SB5ic&list=" + ("A" * 90) + "&t=42s"
        wrapped_rows = _wrap_with_links(long_url, "Helvetica", 9, 180)
        self.assertGreater(len(wrapped_rows), 1)
        for frag_line, frag_links in wrapped_rows:
            self.assertEqual(len(frag_links), 1)
            self.assertEqual(frag_links[0][2], long_url)
        two_urls = "https://www.youtube.com/watch?v=1AMk1-SB5ic&t=1s https://www.youtube.com/watch?v=1N1Z99kUvRw&t=303s"
        two_rows = _wrap_with_links(two_urls, "Helvetica", 8, 500)
        self.assertEqual(len(two_rows), 1)
        self.assertEqual(len(two_rows[0][1]), 2)
        self.assertNotEqual(two_rows[0][1][0][:2], two_rows[0][1][1][:2])

        # Uppercase HTTPS:// scheme still produces clickable links in _wrap_with_links and _markup
        from src.fymc.exporters import _markup, _PDF
        upper_url = "HTTPS://www.youtube.com/watch?v=1AMk1-SB5ic&t=12s"
        upper_rows = _wrap_with_links(upper_url, "Helvetica", 9, 400)
        self.assertEqual(len(upper_rows[0][1]), 1)
        self.assertEqual(upper_rows[0][1][0][2], upper_url)
        self.assertIn('<a href="HTTPS://www.youtube.com/watch?v=1AMk1-SB5ic&amp;t=12s">', _markup(upper_url))

        # Alternating print margins update text_x after page break inside paragraph()
        pdf_doc = _PDF("concept_b", "print_6x9_pdf")
        pdf_doc.new("Test")
        pdf_doc.y = 80  # Force mid-paragraph page break between line 1 and line 2
        pdf_doc.paragraph("LineOne\n" + upper_url, size=10, font=1, boxed=False)
        self.assertEqual(len(pdf_doc.pages), 2)
        self.assertEqual(len(pdf_doc.annots[1]), 1)
        self.assertAlmostEqual(pdf_doc.annots[1][0][0], pdf_doc.left, places=2)

    def test_27_asymmetric_and_greyzone_arbitrage_tracks(self):
        from src.fymc.scorecard_engine import (
            TRACK_DEFINITIONS,
            PLAY_DEFINITIONS,
            CANDIDATE_PLAY_MAP,
            get_candidate_track_metadata,
            build_29_candidate_pipeline,
            get_flagship_scorecard,
        )
        self.assertEqual(set(TRACK_DEFINITIONS), {"track_1", "track_2"})
        self.assertEqual(len(PLAY_DEFINITIONS), 49)
        self.assertEqual(
            set(PLAY_DEFINITIONS),
            {
                "public_record_api_intelligence",
                "expired_domain_traffic_arbitrage",
                "programmatic_seo",
                "distressed_asset_recovery",
                "parasitic_seo",
                "high_velocity_affiliate_funnels",
                "viral_distribution_loops",
                "paid_to_organic_media_arbitrage",
                "telegram_channel_signal_scraping",
                "high_velocity_dm_outbound_systems",
                "serp_signal_navboost_engineering",
                "public_filing_trigger_mail_arbitrage",
                "newly_registered_domain_trigger_arbitrage",
                "identity_graph_pixel_arbitrage",
                "competitor_intent_comparison_hijacking",
                "social_to_search_ping_post_arbitrage",
                "chrome_extension_contextual_arbitrage",
                "rank_and_rent_pay_per_call_routing",
                "ego_bait_directory_badge_arbitrage",
                "b2b_class_action_contingency_recovery",
                "arizona_abs_mass_tort_cocounsel",
                "unclaimed_property_escheatment_arbitrage",
                "municipal_code_violation_trigger_arbitrage",
                "freight_detention_audit_contingency",
                "ucc1_expiration_refi_trigger_arbitrage",
                "probate_docket_inheritance_arbitrage",
                "fmcsa_dot_inspection_trigger_arbitrage",
                "ad_library_spend_velocity_arbitrage",
                "saas_technographic_churn_pixel_scraping",
                "sec_edgar_8k_vendor_trigger_arbitrage",
                "patent_trademark_office_action_arbitrage",
                "review_gating_reputation_extortion_funnels",
                "government_rfp_subcontractor_brokerage",
                "hospital_lien_medical_receivables_arbitrage",
                "amazon_asin_hijack_brand_protection_trigger",
                "property_tax_assessment_appeal_contingency",
                "ssl_ada_wcag_compliance_scanner_outbound",
                "typo_squatting_brand_bid_hijacking",
                "reddit_quora_aged_thread_injection",
                "google_maps_gbp_lead_gen_network",
                "expired_chrome_extension_acquisitions",
                "llm_citation_geo_poisoning",
                "youtube_faceless_high_cpc_compilation_arbitrage",
                "newsletter_co_reg_sparkloop_arbitrage",
                "expired_podcast_rss_redirect_arbitrage",
                "coupon_checkout_tab_under_injection",
                "pinterest_flipboard_visual_serp_arbitrage",
                "job_board_xml_feed_programmatic_arbitrage",
                "domain_drop_catch_backlink_parking_arbitrage",
            },
        )
        for play_id, play in PLAY_DEFINITIONS.items():
            self.assertEqual(play["id"], play_id)
            self.assertIn(play["track_id"], TRACK_DEFINITIONS)
            self.assertTrue(play["name"] and play["mechanism"] and play["inputs"] and play["workflow"] and play["metrics"])
            self.assertTrue(play["platform_risks"], play_id)
            for risk in play["platform_risks"]:
                for req_key in ("failure_mode", "trigger", "impact", "detection_metric", "fallback"):
                    self.assertTrue(risk.get(req_key), (play_id, req_key))

        mapped_plays: set[str] = set()
        for cand_num, play_tuple in CANDIDATE_PLAY_MAP.items():
            self.assertTrue(1 <= cand_num <= 29, cand_num)
            self.assertEqual(len(play_tuple), len(set(play_tuple)), cand_num)
            for pid in play_tuple:
                self.assertIn(pid, PLAY_DEFINITIONS)
                mapped_plays.add(pid)
        self.assertEqual(mapped_plays, set(PLAY_DEFINITIONS))

        # Detached copy isolation & overlap verification
        meta_25_a = get_candidate_track_metadata(25)
        meta_25_b = get_candidate_track_metadata(25)
        self.assertEqual(meta_25_a["track_ids"], ["track_1", "track_2"])
        self.assertEqual(len(meta_25_a["plays"]), 22)
        for req_play in (
            "serp_signal_navboost_engineering",
            "newly_registered_domain_trigger_arbitrage",
            "identity_graph_pixel_arbitrage",
            "ego_bait_directory_badge_arbitrage",
            "competitor_intent_comparison_hijacking",
            "rank_and_rent_pay_per_call_routing",
            "llm_citation_geo_poisoning",
            "reddit_quora_aged_thread_injection",
            "domain_drop_catch_backlink_parking_arbitrage",
        ):
            self.assertIn(req_play, [p["id"] for p in meta_25_a["plays"]])
        meta_25_a["plays"][0]["name"] = "Mutated"
        self.assertNotEqual(meta_25_b["plays"][0]["name"], "Mutated")

        meta_18 = get_candidate_track_metadata(18)
        for req_play in (
            "telegram_channel_signal_scraping",
            "high_velocity_dm_outbound_systems",
            "public_filing_trigger_mail_arbitrage",
            "newly_registered_domain_trigger_arbitrage",
            "identity_graph_pixel_arbitrage",
            "social_to_search_ping_post_arbitrage",
            "rank_and_rent_pay_per_call_routing",
            "ego_bait_directory_badge_arbitrage",
            "arizona_abs_mass_tort_cocounsel",
            "municipal_code_violation_trigger_arbitrage",
            "saas_technographic_churn_pixel_scraping",
            "sec_edgar_8k_vendor_trigger_arbitrage",
        ):
            self.assertIn(req_play, [p["id"] for p in meta_18["plays"]])

        meta_21 = get_candidate_track_metadata(21)
        self.assertIn("arizona_abs_mass_tort_cocounsel", [p["id"] for p in meta_21["plays"]])

        meta_5 = get_candidate_track_metadata(5)
        self.assertIn("b2b_class_action_contingency_recovery", [p["id"] for p in meta_5["plays"]])
        self.assertIn("unclaimed_property_escheatment_arbitrage", [p["id"] for p in meta_5["plays"]])
        meta_22 = get_candidate_track_metadata(22)
        self.assertIn("chrome_extension_contextual_arbitrage", [p["id"] for p in meta_22["plays"]])
        self.assertIn("expired_chrome_extension_acquisitions", [p["id"] for p in meta_22["plays"]])

        # Unmapped candidates get empty arrays cleanly
        meta_10 = get_candidate_track_metadata(10)
        self.assertEqual(meta_10, {"track_ids": [], "track_labels": [], "plays": [], "platform_risks": []})

        # Flagship score remains 87 and carries Track 1 metadata
        flagship = get_flagship_scorecard()
        self.assertEqual(flagship["total_score"], 87)
        self.assertEqual(flagship["track_ids"], ["track_1"])
        self.assertEqual(flagship["plays"][0]["id"], "public_record_api_intelligence")

        # Malformed None play/risk entries are filtered out cleanly
        from src.fymc.scorecard_engine import compute_scorecard
        filtered_card = compute_scorecard({**flagship, "plays": [None, flagship["plays"][0]], "platform_risks": [None]})
        self.assertEqual(len(filtered_card["plays"]), 1)
        self.assertEqual(filtered_card["platform_risks"], [])

        # Pipeline of 29 candidates preserves ranks 1..29 and includes both tracks
        pipeline = build_29_candidate_pipeline()
        self.assertEqual(len(pipeline), 29)
        t1_cands = [c["candidate_number"] for c in pipeline if "track_1" in c["track_ids"]]
        t2_cands = [c["candidate_number"] for c in pipeline if "track_2" in c["track_ids"]]
        self.assertEqual(
            sorted(t1_cands),
            [1, 2, 4, 5, 8, 9, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        )
        self.assertEqual(
            sorted(t2_cands),
            [9, 13, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 29],
        )

        # Store & UI HTML include track filters and platform risk sections while preserving persisted brand settings
        state = self.store.load_publishing_state(self.root, verify_manifest=True)
        self.assertEqual(set(state["pipeline_29_candidates"]["editorial_tracks"]), {"track_1", "track_2"})
        repo_state = self.store.load_publishing_state(ROOT, verify_manifest=True)
        self.assertTrue(repo_state["manifest_verified"])
        self.assertEqual(repo_state["brand_system"]["active_preview_concept"], "concept_b")
        self.assertIn("print_paperback", repo_state["brand_system"]["pricing_hypotheses"])
        self.assertEqual(set(repo_state["pipeline_29_candidates"]["editorial_tracks"]), {"track_1", "track_2"})
        self.assertEqual(set(repo_state["pipeline_29_candidates"]["editorial_plays"]), set(PLAY_DEFINITIONS))
        studio_html = (ROOT / "src" / "static" / "studio.html").read_text(encoding="utf-8")
        site_html = (ROOT / "src" / "static" / "site.html").read_text(encoding="utf-8")
        self.assertIn('id="book-track"', studio_html)
        self.assertIn('id="score-tracks-and-risks"', studio_html)
        self.assertIn('id="business-track"', site_html)


if __name__ == "__main__":
    unittest.main()
