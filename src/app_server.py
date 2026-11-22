#!/usr/bin/env python3
"""Standard-library HTTP server for the ProTip Abridger / Agent Report web app.

Run: python3 -m src.app_server --port 8765
No third-party packages, no credentials, no outbound calls except YouTube ingestion.
"""
from __future__ import annotations

import argparse
import copy
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib
import json
import math
from pathlib import Path
import threading
import urllib.parse

if __package__:
    from .abridge_engine import (ROOT, Transport, abridge_video, atomic_write,
                                 build_custom_agent_report, combine_videos,
                                 extract_video_urls, fetch_video)
    from .build_agent_report import EvidenceIndex, load_corpus
    from .report_playbook import DOMAINS
    from .fymc.http_routes import handle_fymc_http, is_fymc_route
else:  # pragma: no cover - top-level script usage
    from abridge_engine import (ROOT, Transport, abridge_video, atomic_write,
                                build_custom_agent_report, combine_videos,
                                extract_video_urls, fetch_video)
    from build_agent_report import EvidenceIndex, load_corpus
    from report_playbook import DOMAINS
    from fymc.http_routes import handle_fymc_http, is_fymc_route

if __package__:
    from .topic_discovery import parse_topics, discover_topic_videos, relevance_score
    from .ebook_publisher import (build_full_ebook, render_ebook_pdf_bytes,
                                  render_ebook_epub_bytes, render_marketplace_bundle_zip)
else:
    from topic_discovery import parse_topics, discover_topic_videos, relevance_score
    from ebook_publisher import (build_full_ebook, render_ebook_pdf_bytes,
                                 render_ebook_epub_bytes, render_marketplace_bundle_zip)

MAX_BODY_BYTES = 2 * 1024 * 1024
EBOOK_ROUTES = {'/api/topic-discover', '/api/ebook/generate', '/api/ebook/pdf',
                '/api/ebook/epub', '/api/ebook/bundle'}


class BadRequestError(ValueError):
    pass


def validate_params(params):
    if 'topics' in params:
        try:
            if params['topics'] is None:
                raise ValueError('topics must be a string or list of strings')
            topics = parse_topics(params['topics'])
            if len(topics) > 10 or any(len(t) > 300 for t in topics):
                raise ValueError('use at most 10 topics, each at most 300 characters')
        except ValueError as exc:
            raise BadRequestError(str(exc)) from exc
    for key in ('trim', 'pdf_mode'):
        if key in params and (not isinstance(params[key], str) or params[key] not in {'8.5x11', '6x9', 'workbook'}):
            raise BadRequestError(f'invalid {key}')
    for key in ('discover_first', 'auto_ingest', 'use_codex_cli'):
        if key in params and type(params[key]) is not bool:
            raise BadRequestError(f'{key} must be a boolean')
    if 'max_videos' in params and (type(params['max_videos']) is not int or not 1 <= params['max_videos'] <= 100):
        raise BadRequestError('max_videos must be an integer between 1 and 100')
    for key in ('prompt', 'title', 'subtitle', 'mode', 'markdown', 'video_id'):
        if key in params and not isinstance(params[key], str):
            raise BadRequestError(f'{key} must be a string')
    if 'mode' in params and params['mode'] not in {'single', 'combine', 'agent', 'markdown'}:
        raise BadRequestError('invalid mode')
    ids = params.get('video_ids')
    if ids is not None and (not isinstance(ids, list) or any(not isinstance(v, str) for v in ids)):
        raise BadRequestError('video_ids must be null or a list of strings')
    for key in ('urls', 'url'):
        if key in params:
            urls = params[key]
            if not isinstance(urls, (list, str)) or (isinstance(urls, list) and any(not isinstance(u, str) for u in urls)):
                raise BadRequestError(f'{key} must be a string or a list of strings')


STATIC_INDEX = ROOT / "src" / "static" / "index.html"
PDF_MODULES = ("pdf_generator", "pdf_export", "pdf_writer", "pdf_report", "markdown_pdf",
               "report_pdf", "abridge_engine", "build_agent_report")


def markdown_to_pdf_bytes(markdown: str, title: str = "ProTip Agent Report", subtitle: str = "") -> bytes:
    """Locate the project's markdown->PDF writer wherever it lives and call it."""
    for name in PDF_MODULES:
        try:
            module = importlib.import_module("." + name, __package__) if __package__ else importlib.import_module(name)
        except ImportError:
            continue
        fn = getattr(module, "markdown_to_pdf_bytes", None)
        if callable(fn):
            try:
                return fn(markdown, title=title, subtitle=subtitle)
            except TypeError:
                return fn(markdown)
    raise RuntimeError("markdown_to_pdf_bytes is not available in this project")


_APPSTATE_CORPUS_CACHE: dict[str, tuple[list[dict], list[dict]]] = {}
_APPSTATE_CORPUS_CACHE_LOCK = threading.Lock()


class AppState:
    """Thread-safe corpus state: raw records, abridged digests and the evidence index."""

    def __init__(self, data_dir=ROOT / "data"):
        self.data_dir = Path(data_dir)
        self._lock = threading.RLock()
        self.lock = self._lock
        self._loaded_corpus = False
        self._raw_videos: list[dict] = []
        self._abridged_list: list[dict] = []
        self._abridged_by_id: dict[str, dict] = {}
        self._raw_by_id: dict[str, dict] = {}
        self._evidence_index: EvidenceIndex | None = None
        self._last_ebook = None

    def _ensure_corpus_loaded(self) -> None:
        if self._loaded_corpus:
            return
        with self._lock:
            if self._loaded_corpus:
                return
            raw_v, abr_v = self._load_videos_and_abridged()
            self._raw_videos = raw_v
            self._abridged_list = abr_v
            self._abridged_by_id = {a["video_id"]: a for a in abr_v}
            self._raw_by_id = {v["video_id"]: v for v in raw_v}
            self._loaded_corpus = True

    @property
    def raw_videos(self) -> list[dict]:
        self._ensure_corpus_loaded()
        return self._raw_videos

    @raw_videos.setter
    def raw_videos(self, value: list[dict]) -> None:
        with self._lock:
            self._raw_videos = value
            self._loaded_corpus = True

    @property
    def abridged_list(self) -> list[dict]:
        self._ensure_corpus_loaded()
        return self._abridged_list

    @abridged_list.setter
    def abridged_list(self, value: list[dict]) -> None:
        with self._lock:
            self._abridged_list = value
            self._loaded_corpus = True

    @property
    def abridged_by_id(self) -> dict[str, dict]:
        self._ensure_corpus_loaded()
        return self._abridged_by_id

    @abridged_by_id.setter
    def abridged_by_id(self, value: dict[str, dict]) -> None:
        with self._lock:
            self._abridged_by_id = value

    @property
    def raw_by_id(self) -> dict[str, dict]:
        self._ensure_corpus_loaded()
        return self._raw_by_id

    @raw_by_id.setter
    def raw_by_id(self, value: dict[str, dict]) -> None:
        with self._lock:
            self._raw_by_id = value

    @property
    def evidence_index(self) -> EvidenceIndex:
        with self._lock:
            if self._evidence_index is None:
                self._evidence_index = EvidenceIndex(self.raw_videos)
            return self._evidence_index

    @evidence_index.setter
    def evidence_index(self, value: EvidenceIndex | None) -> None:
        with self._lock:
            self._evidence_index = value

    @property
    def last_ebook(self):
        with self.lock:
            return copy.deepcopy(self._last_ebook) if self._last_ebook is not None else None

    @last_ebook.setter
    def last_ebook(self, value):
        with self.lock:
            self._last_ebook = copy.deepcopy(value) if value is not None else None

    def _corpus_paths(self) -> list[Path]:
        return (sorted((self.data_dir / 'transcripts').glob('*.json')) +
                sorted((self.data_dir / 'custom').glob('*.json')) +
                [self.data_dir / 'custom_videos.json'])

    def _load_videos(self) -> list[dict]:
        raw_videos, _ = self._load_videos_and_abridged()
        return raw_videos

    def _load_videos_and_abridged(self) -> tuple[list[dict], list[dict]]:
        import hashlib
        paths = self._corpus_paths()
        hasher = hashlib.sha256()
        existing_blobs: list[tuple[Path, bytes]] = []
        for path in paths:
            try:
                raw_bytes = path.read_bytes()
            except OSError:
                continue
            rel = str(path.relative_to(self.data_dir)) if self.data_dir in path.parents else path.name
            hasher.update(rel.encode('utf-8'))
            hasher.update(b'\0')
            hasher.update(hashlib.sha256(raw_bytes).digest())
            existing_blobs.append((path, raw_bytes))
        cache_key = hasher.hexdigest()
        with _APPSTATE_CORPUS_CACHE_LOCK:
            cached = _APPSTATE_CORPUS_CACHE.get(cache_key)
        if cached is not None:
            return copy.deepcopy(cached[0]), copy.deepcopy(cached[1])

        if __package__:
            from .build_agent_report import classify as _classify, mentions as _mentions
        else:
            from build_agent_report import classify as _classify, mentions as _mentions

        videos, abridged_out, known = [], [], set()
        for path, raw_bytes in existing_blobs:
            try:
                data = json.loads(raw_bytes.decode('utf-8'))
            except (UnicodeDecodeError, ValueError):
                continue
            entries = data if isinstance(data, list) else data.get('videos', [data]) if isinstance(data, dict) else []
            if not isinstance(entries, list):
                continue
            for record in entries:
                if not isinstance(record, dict):
                    continue
                vid = record.get('video_id')
                if not isinstance(vid, str) or not vid or vid in known:
                    continue
                if not isinstance(record.get('metadata', {}), dict) or not isinstance(record.get('full_text', ''), str):
                    continue
                segments = record.get('segments', [])
                if not isinstance(segments, list):
                    continue
                try:
                    if any(not isinstance(s, dict) or not isinstance(s.get('text'), str)
                           or not math.isfinite(float(s.get('start', 0))) for s in segments):
                        continue
                except (ValueError, TypeError, OverflowError):
                    continue
                record.setdefault('metadata', {})
                meta = record['metadata']
                for k in ('title', 'author', 'shortDescription', 'lengthSeconds'):
                    if meta.get(k) is None:
                        meta[k] = ''
                    elif not isinstance(meta[k], str):
                        meta[k] = str(meta[k])
                record.setdefault('full_text', ' '.join(s['text'] for s in segments))
                record.setdefault('segments', [])
                record['index'] = len(videos) + 1
                record['word_count'] = len(record['full_text'].split())
                try:
                    record['domain'] = _classify(record)
                    record['tools'] = _mentions(record['full_text'] + '\n' + meta.get('shortDescription', ''))
                    ab = abridge_video(record)
                except (KeyError, TypeError, ValueError, AttributeError, OverflowError):
                    continue
                videos.append(record)
                abridged_out.append(ab)
                known.add(vid)
        with _APPSTATE_CORPUS_CACHE_LOCK:
            if len(_APPSTATE_CORPUS_CACHE) >= 8:
                _APPSTATE_CORPUS_CACHE.pop(next(iter(_APPSTATE_CORPUS_CACHE)))
            _APPSTATE_CORPUS_CACHE[cache_key] = (copy.deepcopy(videos), copy.deepcopy(abridged_out))
        return videos, abridged_out

    def _persist(self, record: dict) -> None:
        atomic_write(self.data_dir / 'custom_videos.json',
                     json.dumps({'videos': self.raw_videos + [record]}, ensure_ascii=False, indent=2) + '\n')

    def ingest_urls(self, raw_input, transport=None) -> dict:
        text = "\n".join(str(x) for x in raw_input) if isinstance(raw_input, (list, tuple, set)) else str(raw_input or "")
        pairs = extract_video_urls(text)
        results, ingested, cached, failed = [], 0, 0, 0
        for vid, url in pairs:
            with self.lock:
                hit = self.abridged_by_id.get(vid)
            if hit:
                cached += 1
                results.append({"video_id": vid, "status": "cached", "video": copy.deepcopy(hit)})
                continue
            try:
                record = fetch_video(len(self.raw_videos) + 1, url,
                                     transport or Transport(attempts=3, timeout=20, interval=0.2))
            except Exception as exc:
                failed += 1
                results.append({"video_id": vid, "status": "error", "error": f"{type(exc).__name__}: {exc}"})
                continue
            if record.get("status") != "ok":
                failed += 1
                results.append({"video_id": vid, "status": record.get("status", "error"),
                                "error": "no usable captions were recovered for this video"})
                continue
            try:
                with self.lock:
                    hit = self.abridged_by_id.get(vid)
                    if hit:
                        cached += 1
                        results.append({'video_id': vid, 'status': 'cached', 'video': copy.deepcopy(hit)})
                        continue
                    record['video_id'] = vid
                    record['index'] = len(self.raw_videos) + 1
                    record['word_count'] = len(record['full_text'].split())
                    ab = abridge_video(record)
                    custom_path = self.data_dir / 'custom_videos.json'
                    prior_bytes = custom_path.read_bytes() if custom_path.exists() else None
                    prior_raw = list(self.raw_videos)
                    prior_abridged = list(self.abridged_list)
                    had_ei = self._evidence_index is not None
                    try:
                        self._persist(record)
                        if had_ei:
                            self._evidence_index.add_record(record)
                        else:
                            if __package__:
                                from .build_agent_report import classify as _classify, mentions as _mentions
                            else:
                                from build_agent_report import classify as _classify, mentions as _mentions
                            record['domain'] = _classify(record)
                            record['tools'] = _mentions(record['full_text'] + '\n' + record.get('metadata', {}).get('shortDescription', ''))
                        self.raw_videos.append(record)
                        self.raw_by_id[vid] = record
                        self.abridged_list.append(ab)
                        self.abridged_by_id[vid] = ab
                    except Exception:
                        if prior_bytes is None:
                            custom_path.unlink(missing_ok=True)
                        else:
                            if __package__:
                                from .fymc.brand_and_catalog import _write_bytes
                            else:
                                from fymc.brand_and_catalog import _write_bytes
                            _write_bytes(custom_path, prior_bytes)
                        self.raw_videos = prior_raw
                        self.abridged_list = prior_abridged
                        self.raw_by_id = {v['video_id']: v for v in prior_raw}
                        self.abridged_by_id = {v['video_id']: v for v in prior_abridged}
                        self._evidence_index = EvidenceIndex(prior_raw) if had_ei else None
                        raise
            except Exception as exc:
                failed += 1
                results.append({'video_id': vid, 'status': 'error', 'error': f'{type(exc).__name__}: {exc}'})
                continue
            ingested += 1
            results.append({"video_id": vid, "status": "ok", "video": copy.deepcopy(ab)})
        return {"results": results, "ingested_count": ingested, "cached_count": cached,
                "failed_count": failed, "total_videos": len(self.abridged_list)}

    def discover_topics(self, topics, max_videos=20, auto_ingest=True, use_codex_cli=False, search_fn=None):
        result = discover_topic_videos(topics, state=self, max_videos=max_videos,
                                      auto_ingest=auto_ingest, use_codex_cli=use_codex_cli, search_fn=search_fn)
        result['videos'] = self.resolve(result['video_ids'])
        return result

    def generate_ebook(self, topics=None, video_ids=None, title=None, discover_first=False,
                       max_videos=20, use_codex_cli=False):
        parsed = parse_topics(topics)
        discovery = None
        if discover_first and parsed:
            discovery = self.discover_topics(parsed, max_videos=max_videos, use_codex_cli=use_codex_cli)
            video_ids = discovery['video_ids']
        if video_ids is not None:
            video_ids = list(dict.fromkeys(video_ids))
        selected = self.resolve(video_ids)
        fallback = False
        if parsed and video_ids is None:
            matched = sorted((v for v in selected if relevance_score(v, parsed)),
                             key=lambda v: -relevance_score(v, parsed))
            fallback = not bool(matched)
            selected = (matched or selected)[:max_videos]
        selected = selected[:max_videos]
        ebook = build_full_ebook(selected, topics=parsed, custom_title=title)
        ebook['topic_fallback_used'] = fallback
        if discovery is not None:
            ebook['discovery'] = copy.deepcopy(discovery)
        with self.lock:
            self.last_ebook = ebook
        return ebook

    def agent_report(self, prompt='', video_ids=None):
        with self._lock:
            return build_custom_agent_report(self.raw_videos, self.abridged_by_id,
                                             prompt=prompt, selected_video_ids=video_ids,
                                             index=self.evidence_index)

    def totals(self, videos=None) -> dict:
        with self.lock:
            items = list(self.abridged_list if videos is None else videos)
        return {"total": len(items),
                "total_words": sum(v.get("word_count", 0) for v in items),
                "total_hours": round(sum(v.get("length_seconds", 0) for v in items) / 3600.0, 2),
                "total_pro_tips": sum(len(v.get("pro_tips", [])) for v in items)}

    def search(self, domain=None, query=None) -> list[dict]:
        with self.lock:
            items = copy.deepcopy(self.abridged_list)
        if domain:
            items = [v for v in items if str(v.get("domain")) == str(domain)]
        q = (query or "").strip().lower()
        if q:
            def hit(v):
                d = v.get("finite_details") or {}
                hay = [v.get("title", ""), v.get("author", ""), v.get("video_id", ""),
                       v.get("domain_name", "")]
                hay += [str(x) for x in d.get("tools_and_portals", [])]
                hay += [str(x) for x in d.get("statutes_and_forms", [])]
                hay += [t.get("tip", "") for t in v.get("pro_tips", [])]
                return any(q in str(x).lower() for x in hay)
            items = [v for v in items if hit(v)]
        return items

    def resolve(self, video_ids) -> list[dict]:
        with self.lock:
            if video_ids in (None, "all") or (isinstance(video_ids, str) and video_ids.lower() == "all"):
                return copy.deepcopy(self.abridged_list)
            return copy.deepcopy([self.abridged_by_id[v] for v in video_ids if v in self.abridged_by_id])


def create_handler(state: AppState):
    class Handler(BaseHTTPRequestHandler):
        server_version = "ProTipAbridger/1.0"
        protocol_version = "HTTP/1.1"
        timeout = 15

        def log_message(self, fmt, *args):  # quieter console
            print(f"[app] {self.address_string()} {fmt % args}", flush=True)

        def _raw(self, status, body, content_type, extra=None):
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            for key, value in (extra or {}).items():
                self.send_header(key, value)
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)

        def _json(self, payload, status=200):
            self._raw(status, json.dumps(payload, ensure_ascii=False).encode("utf-8"),
                      "application/json; charset=utf-8")

        def _body(self):
            try:
                if self.headers.get('Transfer-Encoding'):
                    raise BadRequestError('Transfer-Encoding is not supported')
                lengths = self.headers.get_all('Content-Length', [])
                if len(lengths) > 1:
                    raise BadRequestError('multiple Content-Length headers')
                length = int(self.headers.get('Content-Length') or 0)
                if length < 0 or length > MAX_BODY_BYTES:
                    raise BadRequestError('Content-Length must be between 0 and 2 MB')
                raw = self.rfile.read(length)
                if len(raw) != length:
                    raise BadRequestError('incomplete request body')
                data = json.loads(raw.decode('utf-8'))
                if not isinstance(data, dict):
                    raise BadRequestError('JSON body must be an object')
                return data
            except (ValueError, UnicodeError, OSError) as exc:
                self.close_connection = True
                raise BadRequestError(str(exc)) from exc

        def _pdf(self, params):
            validate_params(params)
            mode = params.get('mode', 'agent')
            ids = params.get("video_ids")
            if isinstance(ids, str):
                ids = [i for i in (p.strip() for p in ids.split(",")) if i]
            title = params.get("title") or "ProTip Agent Report"
            if mode == 'markdown' or 'markdown' in params:
                markdown = params.get('markdown', '')
            elif mode == "single":
                video = state.abridged_by_id.get(str(params.get("video_id") or ""))
                if not video:
                    return self._json({"error": "unknown video_id"}, 404)
                markdown, title = video.get("markdown", ""), video.get("title", title)
            elif mode == "combine":
                selected = state.resolve(ids)
                if not selected:
                    return self._json({"error": "no videos selected"}, 400)
                markdown = combine_videos(selected, title)["markdown"]
            else:
                report = state.agent_report(params.get('prompt', ''), ids)
                markdown = report["markdown"]
            self._raw(200, markdown_to_pdf_bytes(markdown, title, params.get('subtitle', '')), "application/pdf",
                      {"Content-Disposition": 'attachment; filename="protip-agent-report.pdf"'})

        def _ebook(self, path, params):
            validate_params(params)
            try:
                if path == '/api/topic-discover':
                    return self._json(state.discover_topics(params.get('topics'),
                        max_videos=params.get('max_videos', 20), auto_ingest=params.get('auto_ingest', True),
                        use_codex_cli=params.get('use_codex_cli', False)))
                generation_keys = ('topics', 'video_ids', 'title', 'discover_first', 'max_videos', 'use_codex_cli')
                with state.lock:
                    cached_ebook = getattr(state, 'last_ebook', None)
                    ebook = copy.deepcopy(cached_ebook) if cached_ebook is not None else None
                if path == '/api/ebook/generate' or any(k in params for k in generation_keys) or ebook is None:
                    generated = state.generate_ebook(**{k: params[k] for k in generation_keys if k in params})
                    ebook = copy.deepcopy(generated)
                if path == '/api/ebook/generate':
                    return self._json(ebook)
                if path == '/api/ebook/pdf':
                    mode = params.get('pdf_mode', params.get('trim', '8.5x11'))
                    data, mime, filename = render_ebook_pdf_bytes(ebook, mode), 'application/pdf', f'illustrated-ebook-{mode}.pdf'
                elif path == '/api/ebook/epub':
                    data, mime, filename = render_ebook_epub_bytes(ebook), 'application/epub+zip', 'illustrated-ebook-kindle.epub'
                else:
                    data, mime, filename = render_marketplace_bundle_zip(ebook), 'application/zip', 'amazon-etsy-ebay-ebook-bundle.zip'
                return self._raw(200, data, mime, {'Content-Disposition': f'attachment; filename="{filename}"'})
            except ValueError as exc:
                raise BadRequestError(str(exc)) from exc

        def do_GET(self):
            parts = urllib.parse.urlsplit(self.path)
            path, query = parts.path.rstrip("/") or "/", urllib.parse.parse_qs(parts.query, keep_blank_values=True)
            one = lambda key: (query.get(key) or [None])[0]
            try:
                if is_fymc_route(path):
                    return handle_fymc_http(self, state, "GET", path, query, None)
                if path in EBOOK_ROUTES:
                    params = {k: v[0] for k, v in query.items()}
                    for k in ('trim', 'pdf_mode', 'mode', 'video_id'):
                        if params.get(k) == '':
                            del params[k]
                    if 'video_ids' in params:
                        params['video_ids'] = [v for v in params['video_ids'].split(',') if v]
                    for key in ('discover_first', 'auto_ingest', 'use_codex_cli'):
                        if key in params:
                            if params[key].lower() not in ('true', 'false'):
                                raise BadRequestError(f'{key} must be true or false')
                            params[key] = params[key].lower() == 'true'
                    if 'max_videos' in params:
                        try:
                            params['max_videos'] = int(params['max_videos'])
                        except ValueError as exc:
                            raise BadRequestError('max_videos must be an integer') from exc
                    return self._ebook(path, params)
                if path in ("/", "/index.html"):
                    return self._raw(200, STATIC_INDEX.read_bytes(), "text/html; charset=utf-8")
                if path == "/favicon.ico":
                    return self._raw(200, b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#0D1424"/></svg>', "image/svg+xml")
                if path == "/api/health":
                    t = state.totals()
                    return self._json(dict(t, status="ok", total_videos=t["total"]))
                if path == "/api/videos":
                    with state.lock:
                        snapshot = list(state.abridged_list)
                    items = snapshot
                    domain = one("domain")
                    if domain:
                        items = [v for v in items if str(v.get("domain")) == str(domain)]
                    q = (one("q") or "").strip().lower()
                    if q:
                        def hit(v):
                            d = v.get("finite_details") or {}
                            hay = [v.get("title", ""), v.get("author", ""), v.get("video_id", ""),
                                   v.get("domain_name", "")]
                            hay += [str(x) for x in d.get("tools_and_portals", [])]
                            hay += [str(x) for x in d.get("statutes_and_forms", [])]
                            hay += [t.get("tip", "") for t in v.get("pro_tips", [])]
                            return any(q in str(x).lower() for x in hay)
                        items = [v for v in items if hit(v)]
                    counts = {d: 0 for d in DOMAINS}
                    for v in snapshot:
                        if v.get("domain") in counts:
                            counts[v["domain"]] += 1
                    return self._json(dict(state.totals(items),
                                           domains=[{"id": d, "name": DOMAINS[d][0], "count": counts[d]}
                                                    for d in DOMAINS],
                                           videos=[{k: val for k, val in v.items() if k != "markdown"}
                                                   for v in items]))
                if path.startswith("/api/videos/"):
                    vid = urllib.parse.unquote(path[len("/api/videos/"):])
                    video, raw = state.abridged_by_id.get(vid), state.raw_by_id.get(vid)
                    if not video:
                        return self._json({"error": f"unknown video_id: {vid}"}, 404)
                    return self._json(dict(video, segments=(raw or {}).get("segments", []),
                                           full_text=(raw or {}).get("full_text", "")))
                if path == "/api/report/pdf":
                    params = {k: v[0] for k, v in query.items()}
                    if 'video_ids' in params:
                        params['video_ids'] = [v for v in params['video_ids'].split(',') if v]
                    return self._pdf(params)
                return self._json({"error": f"not found: {parts.path}"}, 404)
            except FileNotFoundError as exc:
                return self._json({"error": f"missing asset: {exc}"}, 500)
            except BadRequestError as exc:
                return self._json({'error': str(exc)}, 400)
            except Exception as exc:
                return self._json({"error": f"{type(exc).__name__}: {exc}"}, 500)

        def do_HEAD(self):
            self.do_GET()

        def do_POST(self):
            parts = urllib.parse.urlsplit(self.path)
            path = parts.path.rstrip("/") or "/"
            query = urllib.parse.parse_qs(parts.query, keep_blank_values=True)
            try:
                payload = self._body()
                if is_fymc_route(path):
                    return handle_fymc_http(self, state, "POST", path, query, payload)
                validate_params(payload)
                if path in EBOOK_ROUTES:
                    return self._ebook(path, payload)
                if path == "/api/ingest":
                    urls = payload.get("urls", payload.get("url", ""))
                    if not extract_video_urls("\n".join(str(u) for u in urls)
                                              if isinstance(urls, (list, tuple, set)) else str(urls or "")):
                        return self._json({"error": "no valid YouTube URLs or video IDs found"}, 400)
                    return self._json(state.ingest_urls(urls))
                if path == "/api/combine":
                    ids = payload.get("video_ids")
                    if isinstance(ids, list) and not ids:
                        return self._json({"error": "video_ids was empty; select at least one video"}, 400)
                    selected = state.resolve(ids)
                    if not selected:
                        return self._json({"error": "none of the requested video_ids are loaded"}, 400)
                    return self._json(combine_videos(
                        selected, payload.get("title") or "Combined Multi-Video ProTip & Finite Details Playbook"))
                if path == "/api/agent-report":
                    ids = payload.get("video_ids")
                    return self._json(state.agent_report(payload.get('prompt', ''), ids))
                if path == "/api/report/pdf":
                    return self._pdf(payload)
                return self._json({"error": f"not found: {path}"}, 404)
            except BadRequestError as exc:
                return self._json({'error': str(exc)}, 400)
            except Exception as exc:
                return self._json({"error": f"{type(exc).__name__}: {exc}"}, 500)

        def do_PATCH(self):
            parts = urllib.parse.urlsplit(self.path)
            path = parts.path.rstrip("/") or "/"
            query = urllib.parse.parse_qs(parts.query, keep_blank_values=True)
            try:
                if is_fymc_route(path):
                    return handle_fymc_http(self, state, "PATCH", path, query, self._body())
                self.close_connection = True
                return self._json({"ok": False, "error": f"not found: {path}"}, 404)
            except BadRequestError as exc:
                return self._json({"ok": False, "error": str(exc)}, 400)
            except Exception as exc:
                return self._json({"ok": False, "error": f"{type(exc).__name__}: {exc}"}, 500)

    return Handler


def create_server(host="127.0.0.1", port=8765, data_dir=ROOT / "data", state=None) -> ThreadingHTTPServer:
    state = state or AppState(data_dir)
    server = ThreadingHTTPServer((host, port), create_handler(state))
    server.daemon_threads = True
    server.state = state
    return server


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--data", type=Path, default=ROOT / "data")
    args = parser.parse_args(argv)
    server = create_server(args.host, args.port, args.data)
    print(f"ProTip Abridger & FYMC Studio on http://{args.host}:{args.port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("shutting down", flush=True)
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
