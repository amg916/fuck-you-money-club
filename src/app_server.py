#!/usr/bin/env python3
"""Standard-library HTTP server for the ProTip Abridger / Agent Report web app.

Run: python3 -m src.app_server --port 8765
No third-party packages, no credentials, no outbound calls except YouTube ingestion.
"""
from __future__ import annotations

import argparse
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
else:  # pragma: no cover - top-level script usage
    from abridge_engine import (ROOT, Transport, abridge_video, atomic_write,
                                build_custom_agent_report, combine_videos,
                                extract_video_urls, fetch_video)
    from build_agent_report import EvidenceIndex, load_corpus
    from report_playbook import DOMAINS

MAX_BODY_BYTES = 2 * 1024 * 1024


class BadRequestError(ValueError):
    pass


def validate_params(params):
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


class AppState:
    """Thread-safe corpus state: raw records, abridged digests and the evidence index."""

    def __init__(self, data_dir=ROOT / "data"):
        self.data_dir = Path(data_dir)
        self._lock = threading.RLock()
        self.lock = self._lock
        self.raw_videos = self._load_videos()
        self.evidence_index = EvidenceIndex(self.raw_videos)
        self.abridged_list = [abridge_video(v) for v in self.raw_videos]
        self.abridged_by_id = {a["video_id"]: a for a in self.abridged_list}
        self.raw_by_id = {v["video_id"]: v for v in self.raw_videos}

    def _load_videos(self) -> list[dict]:
        videos, known = [], set()
        paths = (sorted((self.data_dir / 'transcripts').glob('*.json')) +
                 sorted((self.data_dir / 'custom').glob('*.json')) +
                 [self.data_dir / 'custom_videos.json'])
        for path in paths:
            try:
                data = json.loads(path.read_text(encoding='utf-8'))
            except (OSError, ValueError):
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
                except (ValueError, TypeError):
                    continue
                record.setdefault('metadata', {})
                record.setdefault('full_text', ' '.join(s['text'] for s in segments))
                record.setdefault('segments', [])
                record['index'] = len(videos) + 1
                record['word_count'] = len(record['full_text'].split())
                try:
                    abridge_video(record)
                except (KeyError, TypeError, ValueError, AttributeError, OverflowError):
                    continue
                videos.append(record)
                known.add(vid)
        return videos

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
                results.append({"video_id": vid, "status": "cached", "video": hit})
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
                        results.append({'video_id': vid, 'status': 'cached', 'video': hit})
                        continue
                    record['video_id'] = vid
                    record['index'] = len(self.raw_videos) + 1
                    record['word_count'] = len(record['full_text'].split())
                    ab = abridge_video(record)
                    self._persist(record)
                    self.evidence_index.add_record(record)
                    self.raw_videos.append(record)
                    self.raw_by_id[vid] = record
                    self.abridged_list.append(ab)
                    self.abridged_by_id[vid] = ab
            except Exception as exc:
                failed += 1
                results.append({'video_id': vid, 'status': 'error', 'error': f'{type(exc).__name__}: {exc}'})
                continue
            ingested += 1
            results.append({"video_id": vid, "status": "ok", "video": ab})
        return {"results": results, "ingested_count": ingested, "cached_count": cached,
                "failed_count": failed, "total_videos": len(self.abridged_list)}

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
            items = list(self.abridged_list)
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
                return list(self.abridged_list)
            return [self.abridged_by_id[v] for v in video_ids if v in self.abridged_by_id]


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

        def do_GET(self):
            parts = urllib.parse.urlsplit(self.path)
            path, query = parts.path.rstrip("/") or "/", urllib.parse.parse_qs(parts.query)
            one = lambda key: (query.get(key) or [None])[0]
            try:
                if path in ("/", "/index.html"):
                    return self._raw(200, STATIC_INDEX.read_bytes(), "text/html; charset=utf-8")
                if path == "/api/health":
                    return self._json(dict(state.totals(), status="ok",
                                           total_videos=len(state.abridged_list)))
                if path == "/api/videos":
                    items = state.search(one("domain"), one("q"))
                    counts = {d: 0 for d in DOMAINS}
                    for v in state.abridged_list:
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
                        params['video_ids'] = params['video_ids'].split(',')
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
            path = urllib.parse.urlsplit(self.path).path.rstrip("/") or "/"
            try:
                payload = self._body()
                validate_params(payload)
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
    print(f"ProTip Abridger on http://{args.host}:{args.port} "
          f"({len(server.state.abridged_list)} videos loaded)", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("shutting down", flush=True)
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
