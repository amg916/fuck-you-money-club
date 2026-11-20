"""HTTP adapters for the local FYMC publishing workspace."""
from __future__ import annotations

import hashlib
from pathlib import Path

from . import PUBLISHED_VOLUME_IDS, WORKFLOW_STAGES, resolve_volume_slug
from .brand_and_catalog import (EDITABLE_CHAPTER_FIELDS, VOLUME_SLUG,
                                CorruptStoreError, _resolve_contained,
                                load_publishing_state,
                                record_newsletter_signup, sync_publishing_store,
                                update_chapter_content, update_graphic_review,
                                update_publishing_settings)
from .cover_and_mockups import MOCKUP_SPECS, render_cover_or_mockup_svg
from .design_concepts import get_all_concepts, render_scorecard_svg
from .diagrams_engine import render_diagram_svg
from .exporters import (export_concept_package, render_fymc_bundle_zip_bytes,
                        render_fymc_epub_bytes, render_fymc_pdf_bytes)
from .interior_templates import INTERIOR_TEMPLATES, render_interior_page_html
from .qa_validator import run_full_qa_suite
from .scorecard_engine import build_29_candidate_pipeline

ROOT = Path(__file__).resolve().parent.parent.parent
STATIC_STUDIO = ROOT / "src" / "static" / "studio.html"
STATIC_SITE = ROOT / "src" / "static" / "site.html"
METHODOLOGY = (
    "100-point Money-to-Manpower Score across Revenue Potential (25), "
    "Profit Margin Potential (25), Team Efficiency (20), "
    "Startup Accessibility (15), and Automation Potential (15)"
)


def _store_revision(root_dir):
    publishing = _resolve_contained(root_dir, Path(root_dir).resolve() / "publishing")
    digest = hashlib.sha256()
    for path in sorted(publishing.rglob("*")):
        try:
            _resolve_contained(root_dir, path)
            if not path.is_file():
                continue
            stat = path.stat()
        except FileNotFoundError:
            continue
        digest.update(f"{path.relative_to(publishing)}\0{stat.st_mtime_ns}\0{stat.st_size}\n".encode())
    return digest.hexdigest()


def is_fymc_route(path: str) -> bool:
    return path in ("/studio", "/site") or path.startswith("/api/fymc/")


def _norm_concept(val, default="concept_b"):
    val = default if val is None or val == "" else val
    aliases = {"a": "concept_a", "b": "concept_b", "c": "concept_c",
               "concept_a": "concept_a", "concept_b": "concept_b", "concept_c": "concept_c"}
    if not isinstance(val, str) or val not in aliases:
        raise ValueError("Invalid concept_id")
    return aliases[val]


def _candidates(pub):
    pipeline = pub.get("pipeline_29_candidates", {})
    candidates = pipeline.get("candidates") if isinstance(pipeline, dict) else pipeline
    return candidates if isinstance(candidates, list) and candidates else build_29_candidate_pipeline()


def _candidate_summary(candidate):
    for key in ("description", "summary"):
        if isinstance(candidate.get(key), str) and candidate[key]:
            return candidate[key]
    economics = candidate.get("economics", {})
    return " ".join(str(economics[key]) for key in ("revenue_basis", "estimate_status")
                    if economics.get(key))


def _five_volume_collection(pub):
    metadata = (pub["volumes"]["vol-001-heir-hunting"]["metadata"]
                if "volumes" in pub else pub["volume"]["metadata"])
    volumes = [dict(metadata, status="approved_master")]
    built_map = {
        2: "vol-002-surplus-funds-recovery",
        3: "vol-003-digital-product-empire",
    }
    for number, title in enumerate(("Surplus Funds Recovery", "Digital Product Empire",
                                    "AI-Powered Micro SaaS", "High-Ticket Affiliate Marketing"), 2):
        slug = built_map.get(number)
        if slug and slug in pub.get("volumes", {}):
            volumes.append(dict(pub["volumes"][slug]["metadata"], status="approved_master"))
        else:
            volumes.append({"volume_number": number, "title": title,
                            "status": "proposed", "public_deploy_approved": False,
                            "paid_sales_approved": False})
    return volumes


def _diagrams_list(pub):
    diagrams = pub["volume"].get("diagrams_data", [])
    return diagrams.get("diagrams", []) if isinstance(diagrams, dict) else diagrams


def handle_fymc_http(handler, state, method: str, path: str, query: dict, body: dict | None):
    def q(key):
        value = query.get(key)
        return (value[0] if value else None) if isinstance(value, (list, tuple)) else value

    def text_response(value, content_type):
        return handler._raw(200, value.encode("utf-8"), content_type + "; charset=utf-8")

    def mutation(func, *args):
        with state.lock:
            result = func(root_dir, *args)
            if result.get("ok", True):
                state._fymc_qa_cache = None
            return result

    try:
        if method == "GET" and path in ("/studio", "/site"):
            asset = STATIC_STUDIO if path == "/studio" else STATIC_SITE
            return handler._raw(200, asset.read_bytes(), "text/html; charset=utf-8")
        if not path.startswith("/api/fymc/"):
            return handler._json({"ok": False, "error": "Not found"}, 404)
        if body is None:
            body = {}
        if not isinstance(body, dict):
            raise ValueError("JSON body must be an object")
        raw_vol = q("volume") if q("volume") is not None else (
            q("volume_id") if q("volume_id") is not None else (
                body.get("volume_id") if "volume_id" in body else body.get("volume")))
        vol_slug = resolve_volume_slug(raw_vol)
        root_dir = Path(getattr(state, "fymc_root_dir", None) or (
            ROOT if state.data_dir.resolve() == (ROOT / "data").resolve() else state.data_dir))
        with state.lock:
            root_key = str(root_dir.resolve())
            initialized = getattr(state, "_fymc_initialized_roots", set())
            if root_key not in initialized:
                if not ((root_dir / "publishing" / "brand" / "brand_system.json").is_file()
                        and all((root_dir / "publishing" / "volumes" / slug / "manuscript.json").is_file()
                                for slug in PUBLISHED_VOLUME_IDS)):
                    sync_publishing_store(root_dir, state.abridged_list, state.raw_videos, force=False)
                state._fymc_initialized_roots = initialized | {root_key}
            pub = load_publishing_state(root_dir, volume_id=vol_slug)
        volume = pub["volume"]
        default_concept = pub["brand_system"].get("active_preview_concept", "concept_b")
        if method == "GET" and path == "/api/fymc/overview":
            return handler._json({"ok": True, "brand_system": pub["brand_system"],
                "gates": pub["brand_system"].get("gates", {}), "workflow_stages": WORKFLOW_STAGES,
                "concepts": get_all_concepts(), "mockup_specs": MOCKUP_SPECS,
                "interior_templates": INTERIOR_TEMPLATES,
                "active_volume_id": pub.get("active_volume_id", vol_slug),
                "published_volumes": [pub["volumes"][s]["metadata"] for s in PUBLISHED_VOLUME_IDS
                                      if s in pub.get("volumes", {})],
                "volume": {key: volume[key] for key in (
                    "metadata", "scorecard", "diagrams_data", "graphics_reviews")},
                "counts": pub["counts"],
                "audit_summary": pub["existing_work_audit"].get("summary", pub["existing_work_audit"]),
                "volumes": _five_volume_collection(pub)})
        if method == "GET" and path == "/api/fymc/audit":
            return handler._json({"ok": True, **pub["existing_work_audit"]})
        if method == "GET" and path == "/api/fymc/catalog":
            candidates = _candidates(pub)
            businesses = [{"id": c.get("slug") or str(c.get("candidate_number")),
                "candidate_number": c.get("candidate_number"), "rank": c.get("rank"),
                "name": c.get("title"), "title": c.get("title"), "category": c.get("category"),
                "money_to_manpower_score": c.get("total_score"), "total_score": c.get("total_score"),
                "tier_label": c.get("tier_label"), "description": _candidate_summary(c),
                "methodology": METHODOLOGY + ".", "scorecard": c} for c in candidates]
            return handler._json({"ok": True, "candidates": candidates,
                "pipeline_29_candidates": pub["pipeline_29_candidates"], "businesses": businesses,
                "volumes": _five_volume_collection(pub), "methodology": METHODOLOGY +
                ", separating gross revenue from net owner profit and counting full labor hours."})
        if method == "GET" and path == "/api/fymc/research":
            return handler._json({"ok": True, "research_database": pub["research_database_summary"],
                                  **pub["research_database_summary"]})
        if method == "GET" and path == "/api/fymc/manuscript":
            return handler._json({"ok": True, "manuscript": volume["manuscript"],
                "chapters": volume["manuscript"].get("chapters", []),
                "workbook": volume["workbook"], "diagrams": _diagrams_list(pub),
                "editable_fields": list(EDITABLE_CHAPTER_FIELDS),
                "chapter_markdown": volume["chapter_markdown"]})
        if method in ("POST", "PATCH") and path in (
                "/api/fymc/manuscript", "/api/fymc/manuscript/update"):
            raw_ch = body.get("chapter_number", body.get("chapter_id"))
            if isinstance(raw_ch, bool) or raw_ch is None:
                raise ValueError("invalid_chapter_number")
            patch = body.get("patch", {
                k: v for k, v in body.items()
                if k not in ("chapter_number", "chapter_id", "volume", "volume_id", "expected_revision")
            })
            if not isinstance(patch, dict):
                raise ValueError("patch must be an object")
            res = mutation(lambda r, *a: update_chapter_content(r, *a, volume_id=vol_slug),
                           raw_ch, patch, body.get("expected_revision"))
            if res.get("error") == "revision_conflict":
                return handler._json(res, 409)
            if res.get("error") == "invalid_chapter_number":
                raise ValueError("invalid_chapter_number")
            status = 200 if res["ok"] else (404 if res.get("error") == "chapter_not_found" else 400)
            return handler._json(res, status)
        if method == "GET" and path == "/api/fymc/svg/mockup":
            concept = _norm_concept(q("concept"), default_concept)
            asset = q("asset") or "05_3d_hardcover_mockup"
            clean = str(q("clean") or "0").lower() in ("1", "true", "yes")
            return text_response(render_cover_or_mockup_svg(concept, asset, volume["metadata"],
                volume["scorecard"], marketplace_clean=clean), "image/svg+xml")
        if method == "GET" and path == "/api/fymc/svg/diagram":
            concept = _norm_concept(q("concept"), default_concept)
            diag_id = q("diagram") or "diag-01-end-to-end-workflow"
            diag = next((d for i, d in enumerate(_diagrams_list(pub), 1)
                         if str(diag_id) in (str(d.get("diagram_id")), str(i))), None)
            if diag is None:
                return handler._json({"ok": False, "error": "Unknown diagram"}, 404)
            return text_response(render_diagram_svg(diag, concept), "image/svg+xml")
        if method == "GET" and path == "/api/fymc/svg/scorecard":
            concept = _norm_concept(q("concept"), default_concept)
            selector = q("candidate") or q("candidate_number") or q("business_id") or q("slug")
            target = str(selector or "1")
            cand = next((c for c in _candidates(pub) if target in (
                str(c.get("candidate_number")), str(c.get("slug")), str(c.get("id", "")))), None)
            if cand is None:
                return handler._json({"ok": False, "error": "Unknown candidate"}, 404)
            return text_response(render_scorecard_svg(cand, concept), "image/svg+xml")
        if method == "GET" and path == "/api/fymc/preview-page":
            concept = _norm_concept(q("concept"), default_concept)
            chapter = q("chapter") or q("page")
            ch = int(chapter or 1) if chapter else None
            guides = str(q("guides") or "0").lower() in ("1", "true", "yes")
            return text_response(render_interior_page_html(q("template") or "chapter_opener",
                concept, volume["manuscript"], volume["scorecard"], _diagrams_list(pub),
                chapter_number=ch, viewport_mode=q("viewport") or "desktop",
                show_print_guides=guides), "text/html")
        if method == "POST" and path == "/api/fymc/graphics/review":
            concept = _norm_concept(body.get("concept_id") or body.get("concept"))
            res = mutation(lambda r, *a: update_graphic_review(r, *a, volume_id=vol_slug),
                           str(body.get("graphic_id") or body.get("asset_id") or ""),
                           concept, str(body.get("status") or ""), body.get("notes") if "notes" in body else None)
            return handler._json(res, 200 if res["ok"] else 400)
        if method == "POST" and path == "/api/fymc/export":
            concept = _norm_concept(body.get("concept_id") or body.get("concept"))
            with state.lock:
                res = export_concept_package(root_dir,
                    load_publishing_state(root_dir, volume_id=vol_slug), concept, volume_id=vol_slug)
                state._fymc_qa_cache = None
            return handler._json({"ok": True, **res})
        if method == "GET" and path == "/api/fymc/download":
            concept = _norm_concept(q("concept"), default_concept)
            raw_fmt = (q("fmt") or q("format") or "digital_pdf").lower()
            fmt = {"pdf": "digital_pdf", "digital_pdf": "digital_pdf", "print": "print_6x9_pdf",
                   "print_6x9_pdf": "print_6x9_pdf", "epub": "epub", "workbook": "workbook_pdf",
                   "workbook_pdf": "workbook_pdf", "zip": "bundle_zip", "bundle_zip": "bundle_zip"}.get(raw_fmt)
            if fmt is None:
                raise ValueError("Invalid download format")
            if fmt == "epub":
                data = render_fymc_epub_bytes(pub, concept, volume_id=vol_slug)
                mime, ext = "application/epub+zip", "epub"
            elif fmt == "bundle_zip":
                data = render_fymc_bundle_zip_bytes(pub, concept, volume_id=vol_slug)
                mime, ext = "application/zip", "zip"
            else:
                data = render_fymc_pdf_bytes(pub, concept, fmt, volume_id=vol_slug)
                mime, ext = "application/pdf", "pdf"
            filename_prefix = "fymc" if vol_slug == VOLUME_SLUG else f"fymc-{vol_slug}"
            return handler._raw(200, data, mime, {"Content-Disposition":
                f'attachment; filename="{filename_prefix}-{concept}-{fmt}.{ext}"'})
        if method == "GET" and path == "/api/fymc/qa":
            refresh = str(q("refresh") or "0").lower() in ("1", "true")
            with state.lock:
                cache = getattr(state, "_fymc_qa_cache", None)
                cache_key = (root_key,
                    vol_slug if (q("volume") is not None or q("volume_id") is not None) else "all",
                    _store_revision(root_dir))
                if refresh or cache is None or cache[0] != cache_key:
                    report = run_full_qa_suite(root_dir,
                        load_publishing_state(root_dir, volume_id=vol_slug),
                        volume_id=vol_slug if (q("volume") is not None or q("volume_id") is not None) else None)
                    state._fymc_qa_cache = (cache_key, report)
                else:
                    report = cache[1]
            return handler._json({"ok": True, **report})
        if path == "/api/fymc/settings":
            if method == "GET":
                return handler._json({"ok": True, "brand_system": pub["brand_system"],
                    "pricing_hypotheses": pub["brand_system"].get("pricing_hypotheses", {}),
                    "gates": pub["brand_system"].get("gates", {})})
            if method in ("POST", "PATCH"):
                patch = dict(body)
                patch.pop("owner_explicit_deploy_approval", None)
                patch.pop("owner_explicit_sales_approval", None)
                patch.pop("owner_explicit_concept_approval", None)
                patch.pop("gates", None)
                for key in ("active_preview_concept", "approved_concept_id"):
                    if key in patch and patch[key] is not None:
                        patch[key] = _norm_concept(patch[key])
                res = mutation(update_publishing_settings, patch)
                res["settings"] = res.get("gates", {})
                return handler._json(res, 200 if res["ok"] else 400)
        if method == "POST" and path == "/api/fymc/newsletter":
            email = str(body.get("email") or "").strip()
            tier = str(body.get("tier_interest") or body.get("tier") or "operator_dispatch")
            source = str(body.get("source") or "staging_site")
            res = mutation(record_newsletter_signup, email, tier, source)
            if not res["ok"]:
                return handler._json(res, 400)
            return handler._json({"ok": True, "success": True, "status": "subscribed",
                                  "subscribed": True, **res})
        return handler._json({"ok": False, "error": "Not found"}, 404)
    except CorruptStoreError as exc:
        return handler._json({"ok": False, "error": "corrupt_store", "detail": str(exc)}, 500)
    except ValueError as exc:
        return handler._json({"ok": False, "error": str(exc)}, 400)
