"""Brand system, publishing store, and partial-update helpers for FYMC.

This module owns everything that lives under ``<root>/publishing``:

* the canonical brand + governance configuration (``brand/brand_system.json``),
* the catalog/audit/research snapshots,
* the flagship volume (metadata, scorecard, diagrams, manuscript, workbook,
  graphics reviews, and one Markdown file per chapter),
* the marketing site's newsletter signup store.

Everything is plain stdlib JSON + Markdown on disk so the UI, the exporters and
the tests can all read the same state without a database.  Writes are atomic
(temp file + ``Path.replace``) and partial-update helpers never force a full
rebuild: editing one chapter rewrites exactly one Markdown file, reviewing one
graphic touches exactly one JSON entry.

Governance note (Section 3 Design Approval Gate): ``gates.approved_concept_id``
stays ``None`` until the owner explicitly approves a concept.  ``active_preview_concept``
is a UI preview affordance only and never implies approval.
"""

from __future__ import annotations

import fcntl
import hashlib
import inspect
import math
import shutil
import weakref
import json
import os
import re
import tempfile
import threading
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

from . import (
    PARENT_BRAND,
    BOOK_SERIES,
    BRAND_TAGLINE,
    RATING_SYSTEM_NAME,
    FLAGSHIP_VOLUME_ID,
    VOLUME_002_ID,
    VOLUME_003_ID,
    VOLUME_004_ID,
    VOLUME_005_ID,
    PUBLISHED_VOLUME_IDS,
    OWNER_APPROVED_CONCEPT_ID,
    MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
    TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK,
    MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
    count_manuscript_youtube_links,
    resolve_volume_slug,
    WORKFLOW_STAGES,
)
from .scorecard_engine import (
    TRACK_DEFINITIONS,
    PLAY_DEFINITIONS,
    get_candidate_track_metadata,
    build_29_candidate_pipeline,
    get_flagship_scorecard,
    get_volume_002_scorecard,
    get_volume_003_scorecard,
    get_volume_004_scorecard,
    get_volume_005_scorecard,
    get_volume_scorecard,
    compute_scorecard,
    resolve_score_value,
)
from .volume_registry import get_published_volume_ids, get_volume_spec, load_volume_builders
from .research_intelligence import audit_existing_workspace, build_research_database
from .volume_001_manuscript import (
    build_volume_001_manuscript,
    build_volume_001_diagrams_data,
    build_volume_001_workbook,
    compute_manuscript_word_count,
)
from .volume_002_manuscript import (
    build_volume_002_manuscript,
    build_volume_002_diagrams_data,
)
from .volume_002_chapters_b import build_volume_002_workbook
from .volume_003_manuscript import (
    build_volume_003_manuscript,
    build_volume_003_diagrams_data,
    build_volume_003_workbook,
)
from .volume_004_manuscript import (
    build_volume_004_manuscript,
    build_volume_004_diagrams_data,
    build_volume_004_workbook,
)
from .volume_005_manuscript import (
    build_volume_005_manuscript,
    build_volume_005_diagrams_data,
    build_volume_005_workbook,
)

__all__ = [
    "CorruptStoreError",
    "PUBLISHING_DIRNAME",
    "VOLUME_SLUG",
    "VOLUME_002_SLUG",
    "VOLUME_003_SLUG",
    "VOLUME_004_SLUG",
    "VOLUME_005_SLUG",
    "PUBLISHED_VOLUME_SLUGS",
    "CONCEPT_IDS",
    "CONCEPT_LABELS",
    "COVER_GRAPHIC_IDS",
    "DEFAULT_DIAGRAM_IDS",
    "REVIEW_STATUSES",
    "EDITABLE_CHAPTER_FIELDS",
    "build_default_brand_system",
    "chapter_to_markdown",
    "sync_publishing_store",
    "load_publishing_state",
    "verify_commit_manifest",
    "update_chapter_content",
    "update_graphic_review",
    "update_publishing_settings",
    "record_newsletter_signup",
    "recompute_candidate_scorecard",
]

# --------------------------------------------------------------------------
# Layout constants
# --------------------------------------------------------------------------

PUBLISHING_DIRNAME = "publishing"

# The on-disk folder for the flagship volume is pinned by the publishing spec;
# ``FLAGSHIP_VOLUME_ID`` is carried inside the metadata payload instead.
VOLUME_SLUG = "vol-001-heir-hunting"
VOLUME_002_SLUG = VOLUME_002_ID
VOLUME_003_SLUG = VOLUME_003_ID
VOLUME_004_SLUG = VOLUME_004_ID
VOLUME_005_SLUG = VOLUME_005_ID
PUBLISHED_VOLUME_SLUGS = PUBLISHED_VOLUME_IDS

CONCEPT_IDS = ("concept_a", "concept_b", "concept_c")

CONCEPT_LABELS = {
    "concept_a": "Concept A — Black & Gold Executive",
    "concept_b": "Concept B — Bold Editorial",
    "concept_c": "Concept C — Modern Wealth Intelligence",
}

COVER_GRAPHIC_IDS = (
    "cover_front",
    "cover_back",
    "cover_spine",
    "01_front_cover",
    "02_paperback_wrap",
    "03_hardcover_concept",
    "04_ebook_cover",
    "05_3d_hardcover_mockup",
    "06_paperback_mockup",
    "07_ereader_mockup",
    "08_phone_tablet_mockup",
    "09_series_collection_mockup",
    "10_social_promo_pack",
)

COVER_LABELS = {
    "cover_front": "Front Cover",
    "cover_back": "Back Cover",
    "cover_spine": "Spine",
    "01_front_cover": "Front Cover",
    "02_paperback_wrap": "Paperback Wrap",
    "03_hardcover_concept": "Hardcover Concept",
    "04_ebook_cover": "Ebook Cover",
    "05_3d_hardcover_mockup": "3D Hardcover Mockup",
    "06_paperback_mockup": "Paperback Mockup",
    "07_ereader_mockup": "Ereader Mockup",
    "08_phone_tablet_mockup": "Phone / Tablet Mockup",
    "09_series_collection_mockup": "Series Collection Mockup",
    "10_social_promo_pack": "Social Promo Pack",
}

DEFAULT_DIAGRAM_IDS = (
    "diagram_01_money_to_manpower_matrix",
    "diagram_02_heir_hunting_value_chain",
    "diagram_03_claim_lifecycle_timeline",
    "diagram_04_state_escheatment_landscape",
    "diagram_05_fee_structure_ladder",
    "diagram_06_research_stack_architecture",
    "diagram_07_compliance_gate_flow",
    "diagram_08_scale_economics_curve",
)

REVIEW_STATUSES = frozenset(
    {"approved", "rejected", "changes_requested", "pending_review"}
)

EDITABLE_CHAPTER_FIELDS = (
    "title",
    "subtitle",
    "executive_summary",
    "pull_quote",
    "sections",
    "action_checklist",
    "statutory_citations",
    "source_citations",
)

CHAPTER_COUNT = 12

_COMPLETED_STAGES = (
    "Research",
    "Source Review",
    "Editorial Outline",
    "Manuscript",
    "Fact-Checking",
    "Design",
    "Graphics",
    "Scorecard",
    "Proofreading",
    "Export",
    "Quality Assurance",
)
_AWAITING_APPROVAL_STAGES = ()
_STAGED_PREVIEW_STAGES = (
    "Publication Approval",
)

_EPISTEMIC_BADGES = {
    "verified": "✅ VERIFIED",
    "sourced": "✅ VERIFIED",
    "confirmed": "✅ VERIFIED",
    "estimated": "🧮 ESTIMATED",
    "estimate": "🧮 ESTIMATED",
    "modeled": "🧮 ESTIMATED",
    "inferred": "🧠 INFERRED",
    "inference": "🧠 INFERRED",
    "speculative": "🔭 SPECULATIVE",
    "hypothesis": "🔭 SPECULATIVE",
    "framework": "📐 FRAMEWORK",
    "operator_opinion": "🗣️ OPERATOR VIEW",
}

_EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$")


# --------------------------------------------------------------------------
# Small IO / coercion helpers
# --------------------------------------------------------------------------


_OPEN_LOCK_FDS: set[int] = set()
_LIVE_ROOT_LOCKS: weakref.WeakSet = weakref.WeakSet()
_FORK_FD_GUARD = threading.Lock()


class _RootLock:
    def __init__(self, root):
        self.key = str(Path(root).resolve())
        self.path = _resolve_contained(Path(root), Path(root) / "publishing" / ".fymc.lock")
        self.lock = threading.RLock()
        self.depth = 0
        self.owner = None
        self.fd = None
        self.pid = os.getpid()
        _LIVE_ROOT_LOCKS.add(self)

    def _reset_if_forked(self):
        current_pid = os.getpid()
        if self.pid != current_pid:
            if self.fd is not None:
                fd = self.fd
                self.fd = None
                with _FORK_FD_GUARD:
                    _OPEN_LOCK_FDS.discard(fd)
                    try:
                        os.close(fd)
                    except OSError:
                        pass
            self.lock = threading.RLock()
            self.depth = 0
            self.owner = None
            self.fd = None
            self.pid = current_pid

    def acquire(self, blocking=True):
        self._reset_if_forked()
        if not self.lock.acquire(blocking):
            return False
        try:
            self._reset_if_forked()
            if self.depth == 0:
                self.path.parent.mkdir(parents=True, exist_ok=True)
                flags = os.O_CREAT | os.O_RDWR | getattr(os, "O_CLOEXEC", 0)
                with _FORK_FD_GUARD:
                    fd = os.open(self.path, flags, 0o600)
                    _OPEN_LOCK_FDS.add(fd)
                try:
                    fcntl.flock(fd, fcntl.LOCK_EX | (0 if blocking else fcntl.LOCK_NB))
                except BaseException:
                    with _FORK_FD_GUARD:
                        _OPEN_LOCK_FDS.discard(fd)
                        try:
                            os.close(fd)
                        except OSError:
                            pass
                    raise
                self.fd = fd
                self.pid = os.getpid()
            self.depth += 1
            self.owner = threading.get_ident()
            return True
        except BlockingIOError:
            self.lock.release()
            return False
        except BaseException:
            self.lock.release()
            raise

    def release(self):
        self._reset_if_forked()
        if self.owner != threading.get_ident():
            raise RuntimeError("cannot release un-acquired lock")
        try:
            self.depth -= 1
            if self.depth == 0:
                try:
                    fcntl.flock(self.fd, fcntl.LOCK_UN)
                finally:
                    fd = self.fd
                    self.fd = None
                    self.owner = None
                    if fd is not None:
                        with _FORK_FD_GUARD:
                            _OPEN_LOCK_FDS.discard(fd)
                            os.close(fd)
        finally:
            self.lock.release()

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, *exc):
        self.release()


_ROOT_LOCKS = weakref.WeakValueDictionary()
_ROOT_LOCKS_GUARD = threading.Lock()
_ROOT_LOCKS_PID = os.getpid()


def _before_fork() -> None:
    _FORK_FD_GUARD.acquire()


def _after_fork_parent() -> None:
    if _FORK_FD_GUARD.locked():
        _FORK_FD_GUARD.release()


def _reset_root_locks_after_fork() -> None:
    global _ROOT_LOCKS, _ROOT_LOCKS_GUARD, _ROOT_LOCKS_PID, _FORK_FD_GUARD
    for fd in tuple(_OPEN_LOCK_FDS):
        try:
            os.close(fd)
        except OSError:
            pass
    _OPEN_LOCK_FDS.clear()
    try:
        live = tuple(_LIVE_ROOT_LOCKS)
    except Exception:
        live = ()
    cur_pid = os.getpid()
    _ROOT_LOCKS = weakref.WeakValueDictionary()
    for inst in live:
        inst.fd = None
        inst.depth = 0
        inst.owner = None
        inst.lock = threading.RLock()
        inst.pid = cur_pid
        if getattr(inst, "key", None):
            _ROOT_LOCKS[inst.key] = inst
    _ROOT_LOCKS_GUARD = threading.Lock()
    _FORK_FD_GUARD = threading.Lock()
    _ROOT_LOCKS_PID = cur_pid


if hasattr(os, "register_at_fork"):
    os.register_at_fork(
        before=_before_fork,
        after_in_parent=_after_fork_parent,
        after_in_child=_reset_root_locks_after_fork,
    )


def _root_lock(root_dir: Path) -> _RootLock:
    if _ROOT_LOCKS_PID != os.getpid():
        _reset_root_locks_after_fork()
    key = str(Path(root_dir).resolve())
    with _ROOT_LOCKS_GUARD:
        lock = _ROOT_LOCKS.get(key)
        if lock is None:
            lock = _RootLock(key)
            _ROOT_LOCKS[key] = lock
        return lock


def _now_iso() -> str:
    return (
        datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    )


def _publishing_dir(root_dir: Path) -> Path:
    root = Path(root_dir).resolve()
    return _resolve_contained(root, root / PUBLISHING_DIRNAME)


def _volume_dir(root_dir: Path, volume_id: object = None) -> Path:
    slug = resolve_volume_slug(volume_id)
    return _resolve_contained(root_dir, _publishing_dir(root_dir) / "volumes" / slug)


def _write_json(path: Path, payload: object) -> Path:
    """Atomically write ``payload`` as pretty, stable-ordered JSON."""
    path = _guard_store_path(path)
    serialized = json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=str(path.parent),
            prefix=f".{path.name}.", suffix=".tmp", delete=False,
        ) as tmp:
            tmp_path = Path(tmp.name)
            tmp.write(serialized + "\n")
            tmp.flush()
            os.fsync(tmp.fileno())
        os.replace(tmp_path, path)
        _fsync_dir(path.parent)
    finally:
        if tmp_path is not None:
            tmp_path.unlink(missing_ok=True)
    return path


def _write_text(path: Path, text: str) -> Path:
    path = _guard_store_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=str(path.parent),
            prefix=f".{path.name}.", suffix=".tmp", delete=False,
        ) as tmp:
            tmp_path = Path(tmp.name)
            tmp.write(text)
            tmp.flush()
            os.fsync(tmp.fileno())
        os.replace(tmp_path, path)
        _fsync_dir(path.parent)
    finally:
        if tmp_path is not None:
            tmp_path.unlink(missing_ok=True)
    return path


class CorruptStoreError(RuntimeError):
    """An existing store cannot safely be read or updated."""


def _resolve_contained(root_dir: Path, target: Path) -> Path:
    root = Path(root_dir).resolve()
    target = Path(target)
    if not target.is_absolute():
        target = root / target
    try:
        parts = target.relative_to(root).parts
    except ValueError:
        raise ValueError("Store path escapes workspace root") from None
    current = root
    for part in parts:
        current = current / part
        if not current.resolve().is_relative_to(root):
            raise ValueError("Store path escapes workspace root")
    return target


def _guard_store_path(path: Path) -> Path:
    path = Path(path).absolute()
    for parent in (path, *path.parents):
        if parent.name == PUBLISHING_DIRNAME:
            return _resolve_contained(parent.parent, path)
    return path


def _fsync_dir(dir_path: Path):
    fd = os.open(str(dir_path), os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _read_json(path: Path, default: object = None, *, strict: bool = False) -> object:
    path = _guard_store_path(path)
    if not path.exists() and not path.is_symlink():
        return default
    try:
        raw = path.read_text(encoding="utf-8")
        value = json.loads(raw)
        if strict:
            json.dumps(value, allow_nan=False)
            if not isinstance(value, dict):
                raise ValueError("Expected object")
            schemas = {
                "newsletter_signups.json": {"subscribers": list},
                "manuscript.json": {"chapters": list},
                "graphics_reviews.json": {"reviews": dict},
                "pipeline_29_candidates.json": {"candidates": list},
            }
            for key, kind in schemas.get(path.name, {}).items():
                if not isinstance(value.get(key), kind):
                    raise ValueError("Invalid store schema")
            for key in ("chapters", "subscribers", "candidates"):
                if key in schemas.get(path.name, {}) and any(not isinstance(item, dict) for item in value[key]):
                    raise ValueError("Invalid store record")
        return value
    except (OSError, UnicodeDecodeError, ValueError) as exc:
        if strict:
            raise CorruptStoreError(f"Corrupt or unreadable store file: {path}") from exc
        return default


def _write_bytes(path, data):
    path = _guard_store_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        _fsync_dir(path.parent)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def _recover_single_previews_dir(root: Path, previews_dir: Path):
    if not previews_dir.exists() and not previews_dir.is_symlink():
        return
    if not previews_dir.is_dir():
        raise CorruptStoreError(f"Corrupt previews directory: {previews_dir}")
    dirty = False
    for journal_path in sorted(previews_dir.glob(".export_journal_*.json")):
        _resolve_contained(root, journal_path)
        if ".tmp." in journal_path.name:
            journal_path.unlink(missing_ok=True)
            dirty = True
            continue
        payload = _read_json(journal_path, strict=True)
        target_name = payload.get("target")
        stage_name = payload.get("stage")
        backup_name = payload.get("backup")
        if (target_name not in CONCEPT_IDS
                or not isinstance(stage_name, str) or not stage_name.startswith(target_name + ".stage.")
                or not isinstance(backup_name, str) or not backup_name.startswith(target_name + ".prev.")
                or any(n in {".", ".."} or "/" in n or "\\" in n or Path(n).name != n
                       for n in (target_name, stage_name, backup_name))):
            raise CorruptStoreError(f"Corrupt export journal: {journal_path}")
        target_dir = _resolve_contained(previews_dir, previews_dir / target_name)
        stage_dir = _resolve_contained(previews_dir, previews_dir / stage_name)
        backup_dir = _resolve_contained(previews_dir, previews_dir / backup_name)
        if any(p.resolve() == previews_dir.resolve() for p in (target_dir, stage_dir, backup_dir)):
            raise CorruptStoreError(f"Corrupt export journal: {journal_path}")
        had_existing = bool(payload.get("had_existing", True))
        if not target_dir.exists() and backup_dir.exists():
            os.replace(backup_dir, target_dir)
        elif target_dir.exists() and backup_dir.exists():
            if target_dir.is_dir() and not target_dir.is_symlink():
                shutil.rmtree(target_dir)
            else:
                target_dir.unlink(missing_ok=True)
            os.replace(backup_dir, target_dir)
        elif not had_existing and (target_dir.exists() or target_dir.is_symlink()):
            if target_dir.is_dir() and not target_dir.is_symlink():
                shutil.rmtree(target_dir)
            else:
                target_dir.unlink(missing_ok=True)
        if stage_dir.exists():
            shutil.rmtree(stage_dir)
        journal_path.unlink(missing_ok=True)
        dirty = True
    for entry in sorted(previews_dir.iterdir()):
        _resolve_contained(root, entry)
        if any(entry.name.startswith((cid + ".stage.", cid + ".prev.")) for cid in CONCEPT_IDS):
            if entry.is_dir() and not entry.is_symlink():
                shutil.rmtree(entry)
            else:
                entry.unlink(missing_ok=True)
            dirty = True
        elif entry.name.startswith(".export_journal_") and ".tmp." in entry.name:
            entry.unlink(missing_ok=True)
            dirty = True
    if dirty:
        _fsync_dir(previews_dir)


def _recover_export_journals(root_dir):
    root = Path(root_dir).resolve()
    pub = _resolve_contained(root, root / PUBLISHING_DIRNAME)
    previews_dir = _resolve_contained(root, pub / "previews")
    _recover_single_previews_dir(root, previews_dir)
    if previews_dir.is_dir() and not previews_dir.is_symlink():
        for slug in get_published_volume_ids():
            if slug == VOLUME_SLUG:
                continue
            nested = _resolve_contained(root, previews_dir / slug)
            if nested.exists() or nested.is_symlink():
                _recover_single_previews_dir(root, nested)


def _recover_journal(root_dir):
    root = Path(root_dir).resolve()
    _recover_export_journals(root)
    pub = _resolve_contained(root, root / PUBLISHING_DIRNAME)
    journal = _resolve_contained(root, pub / ".journal.json")
    backup = _resolve_contained(root, pub / ".txn_backup")
    if not journal.exists() and not journal.is_symlink():
        return
    payload = _read_json(journal, strict=True)
    entries = payload.get("targets")
    if not isinstance(entries, list):
        raise CorruptStoreError(f"Corrupt or unreadable store file: {journal}")
    # Validate all recovery paths before restoring any file.
    restored = []
    for entry in entries:
        target = _resolve_contained(root, root / entry["path"])
        source = _resolve_contained(root, backup / entry["backup"])
        restored.append((target, source.read_bytes() if entry["existed"] else None))
    for target, data in restored:
        if data is None:
            target.unlink(missing_ok=True)
            if target.parent.exists():
                _fsync_dir(target.parent)
        else:
            _write_bytes(target, data)
    journal.unlink()
    _fsync_dir(pub)
    shutil.rmtree(backup)
    _fsync_dir(pub)


def _compute_store_digests(root: Path, pub: Path) -> dict[str, str]:
    digests: dict[str, str] = {}
    if not pub.exists() and not pub.is_symlink():
        return digests
    for path in sorted(pub.rglob("*")):
        _resolve_contained(root, path)
        if not path.is_file():
            continue
        rel_parts = path.relative_to(pub).parts
        if not rel_parts or rel_parts[0] == "previews" or any(p.startswith(".") for p in rel_parts):
            continue
        digests[str(path.relative_to(pub))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return digests


def verify_commit_manifest(root_dir: Path, *, strict: bool = False) -> dict:
    """Verify `.commit_manifest.json` digests across `publishing/` (excluding `previews/`)."""
    with _root_lock(root_dir):
        root = Path(root_dir).resolve()
        _recover_journal(root)
        pub = _publishing_dir(root)
        manifest_path = _resolve_contained(root, pub / ".commit_manifest.json")
        manifest = _read_json(manifest_path, None, strict=strict)
        if not isinstance(manifest, dict) or not isinstance(manifest.get("sha256"), dict):
            if strict:
                raise CorruptStoreError(f"Missing or invalid commit manifest: {manifest_path}")
            return {
                "passed": False,
                "scope": "publishing_store_excluding_previews",
                "checked_files": 0,
                "missing": [],
                "unexpected": [],
                "mismatched": [],
            }
        expected = manifest["sha256"]
        if any(not isinstance(k, str) or not isinstance(v, str) for k, v in expected.items()):
            if strict:
                raise CorruptStoreError(f"Invalid digest entries in commit manifest: {manifest_path}")
            return {
                "passed": False,
                "scope": "publishing_store_excluding_previews",
                "checked_files": 0,
                "missing": [],
                "unexpected": [],
                "mismatched": [],
            }
        actual = _compute_store_digests(root, pub)
        missing = sorted(set(expected) - set(actual))
        unexpected = sorted(set(actual) - set(expected))
        mismatched = sorted(k for k in (set(expected) & set(actual)) if expected[k] != actual[k])
        passed = not missing and not unexpected and not mismatched
        if not passed and strict:
            raise CorruptStoreError(
                f"Commit manifest mismatch in {manifest_path}: "
                f"missing={missing}, unexpected={unexpected}, mismatched={mismatched}"
            )
        return {
            "passed": passed,
            "scope": "publishing_store_excluding_previews",
            "checked_files": len(actual),
            "missing": missing,
            "unexpected": unexpected,
            "mismatched": mismatched,
        }


def _commit_store_transaction(root_dir, json_writes: list[tuple[Path, object]],
                              text_writes: list[tuple[Path, str]]):
    root = Path(root_dir).resolve()
    pub = _resolve_contained(root, root / PUBLISHING_DIRNAME)
    journal = _resolve_contained(root, pub / ".journal.json")
    backup = _resolve_contained(root, pub / ".txn_backup")
    manifest = _resolve_contained(root, pub / ".commit_manifest.json")
    targets = []
    for path, payload in json_writes:
        json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False)
        targets.append(_resolve_contained(root, Path(path).absolute()))
    for path, text in text_writes:
        text.encode("utf-8")
        targets.append(_resolve_contained(root, Path(path).absolute()))
    targets.append(manifest)
    if len(set(targets)) != len(targets):
        raise ValueError("Duplicate transaction target")
    with _root_lock(root):
        _recover_journal(root)
        if backup.exists():
            shutil.rmtree(backup)
        backup.mkdir(parents=True)
        entries = []
        for index, path in enumerate(targets):
            existed = path.exists() or path.is_symlink()
            name = f"{index:04d}.bak"
            if existed:
                _write_bytes(backup / name, path.read_bytes())
            entries.append({"path": str(path.relative_to(root)), "existed": existed, "backup": name})
        try:
            _write_json(journal, {"targets": entries})
            for path, payload in json_writes:
                _write_json(path, payload)
            for path, text in text_writes:
                _write_text(path, text)
            digests = _compute_store_digests(root, pub)
            _write_json(manifest, {"scope": "publishing_store_excluding_previews", "sha256": digests})
        except BaseException:
            _recover_journal(root)
            raise
        journal.unlink()
        _fsync_dir(pub)
        shutil.rmtree(backup)
        _fsync_dir(pub)


def _chapter_revision(chapter):
    content = {key: value for key, value in chapter.items() if key not in ("updated_at", "revision")}
    content["sections"] = [_normalize_section(s) for s in content.get("sections", [])]
    return hashlib.sha256(json.dumps(content, sort_keys=True, ensure_ascii=False,
                                    allow_nan=False).encode("utf-8")).hexdigest()[:16]


def _is_signature_error(exc: TypeError, func) -> bool:
    """True when a TypeError came from calling ``func`` with the wrong arity."""
    name = getattr(func, "__name__", "")
    text = str(exc)
    return bool(name) and name in text and "argument" in text


def _invoke(func, *args):
    """Call ``func`` with as many of ``args`` as its signature accepts.

    Sibling builders have evolved their signatures over time (some take the
    workspace root or the video corpora, some take nothing).  Rather than pin
    this module to one revision, try the richest call first and degrade.
    """
    last: TypeError | None = None
    for count in range(len(args), -1, -1):
        try:
            return func(*args[:count])
        except TypeError as exc:
            if not _is_signature_error(exc, func):
                raise
            last = exc
    if last is not None:
        raise last
    return func()


def _as_dict(value: object, key: str) -> dict:
    """Normalize a builder result into a dict payload."""
    if isinstance(value, dict):
        return dict(value)
    if value is None:
        return {}
    if isinstance(value, (list, tuple)):
        return {key: list(value)}
    return {key: value}


def _as_list(value: object, *keys: str) -> list:
    """Normalize a builder result into a list payload."""
    if isinstance(value, list):
        return list(value)
    if isinstance(value, tuple):
        return list(value)
    if isinstance(value, dict):
        for key in keys:
            inner = value.get(key)
            if isinstance(inner, (list, tuple)):
                return list(inner)
        return [value]
    if value is None:
        return []
    return [value]


def _text(value: object) -> str:
    """Flatten a string / list-of-strings / dict body into plain text."""
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, (list, tuple)):
        parts = [_text(item) for item in value]
        return "\n\n".join(part for part in parts if part)
    if isinstance(value, dict):
        for key in ("text", "body", "content", "value", "summary"):
            if key in value:
                return _text(value[key])
        return "\n\n".join(
            "**{0}:** {1}".format(k, _text(v)) for k, v in value.items()
        )
    return str(value)


def _first(mapping: dict, *keys: str, default=None):
    for key in keys:
        if isinstance(mapping, dict) and mapping.get(key) not in (None, "", [], {}):
            return mapping[key]
    return default


def _chapter_number(chapter: dict, fallback: int) -> int:
    raw = _first(chapter, "number", "chapter_number", "chapter", "index", default=fallback)
    try:
        return int(raw)
    except (TypeError, ValueError):
        return fallback


def _chapter_filename(number: int) -> str:
    return "chapter-{0:02d}.md".format(int(number))


def _epistemic_badge(value: object) -> str:
    label = _text(value)
    if not label:
        return ""
    key = label.strip().lower().replace(" ", "_").replace("-", "_")
    return _EPISTEMIC_BADGES.get(key, "🏷️ {0}".format(label.strip().upper()))


def _summarize_payload(payload: object, sample_size: int = 12) -> dict:
    """Build a compact, JSON-safe summary of a potentially huge structure."""
    summary: dict = {"type": type(payload).__name__}
    if isinstance(payload, dict):
        summary["keys"] = sorted(str(k) for k in payload.keys())
        counts: dict = {}
        for key, value in payload.items():
            if isinstance(value, (list, tuple, dict)):
                counts[str(key)] = len(value)
        if counts:
            summary["counts"] = counts
        scalars = {
            str(k): v
            for k, v in payload.items()
            if isinstance(v, (str, int, float, bool)) or v is None
        }
        if scalars:
            summary["values"] = scalars
    elif isinstance(payload, (list, tuple)):
        summary["count"] = len(payload)
        sample = []
        for item in list(payload)[:sample_size]:
            if isinstance(item, dict):
                sample.append(
                    {
                        str(k): item[k]
                        for k in list(item.keys())[:6]
                        if isinstance(item.get(k), (str, int, float, bool))
                    }
                )
            else:
                sample.append(item)
        summary["sample"] = sample
    else:
        summary["value"] = payload
    return summary


# --------------------------------------------------------------------------
# 1. Brand system
# --------------------------------------------------------------------------


def _build_workflow_stages() -> list:
    """Project ``WORKFLOW_STAGES`` into the 12-stage governance board."""
    stages = []
    raw_stages = list(WORKFLOW_STAGES) if WORKFLOW_STAGES else []
    if not raw_stages:
        raw_stages = list(
            _COMPLETED_STAGES + _AWAITING_APPROVAL_STAGES + _STAGED_PREVIEW_STAGES
        )
    for index, raw in enumerate(raw_stages, start=1):
        if isinstance(raw, dict):
            name = str(_first(raw, "name", "stage", "label", default="Stage {0}".format(index)))
        else:
            name = str(raw)
        if name in _COMPLETED_STAGES:
            status = "completed"
        elif name in _AWAITING_APPROVAL_STAGES:
            status = "awaiting_owner_approval"
        else:
            status = "staged_preview"
        stages.append({"order": index, "name": name, "status": status})
    return stages


def _normalize_gates(gates):
    result = dict(gates) if isinstance(gates, dict) else {}
    result.update(
        design_approval_status="approved",
        approved_concept_id=OWNER_APPROVED_CONCEPT_ID,
        public_deploy_approved=False,
        paid_sales_approved=False,
    )
    result.pop("design_approved_at", None)
    return result


def build_default_brand_system() -> dict:
    """Return the canonical brand, pricing-hypothesis and governance config."""
    return {
        "parent_brand": PARENT_BRAND,
        "book_series": BOOK_SERIES,
        "tagline": BRAND_TAGLINE,
        "rating_system": {
            "name": RATING_SYSTEM_NAME,
            "scale": "0-100",
            "trademark_symbol_policy": (
                "No TM or R symbols used pending formal trademark clearance."
            ),
        },
        "cover_profanity_policy": {
            "series_dominant": True,
            "parent_brand_placement": (
                "Subtle single publisher colophon / imprint mark only"
            ),
            "never_repeat_profanity_across_cover": True,
            "marketplace_safe_cover_ready": True,
        },
        "gates": _normalize_gates({}),
        "active_preview_concept": OWNER_APPROVED_CONCEPT_ID,
        "pricing_hypotheses": {
            "digital_playbook": {
                "label": "Digital Playbook Edition (Concept B)",
                "range_label": "$29 Approved ($19–$39 Band)",
                "test_price_usd": 29,
                "includes": [
                    "8.5×11 Executive Digital PDF",
                    "Reflowable EPUB 3.0",
                    "Clickable Source Index",
                ],
                "hypothesis": True,
                "paid_checkout_enabled": False,
                "notes": "8.5x11 Executive Digital PDF + Reflowable EPUB 3.0 + Clickable Source Index (97.1% direct net margin).",
            },
            "print_paperback": {
                "label": "6×9 Print Paperback Edition (Concept B)",
                "range_label": "$34 Approved ($2.99–$4.36 KDP COGS)",
                "test_price_usd": 34,
                "includes": [
                    "6×9 Print Paperback Edition",
                    "14 Editorial Interior Templates",
                    "8 Structured Vector Diagrams",
                ],
                "notes": "Spec B (78pp Standard Color: $2.99 KDP COGS, +$17.41 KDP net, +$28.56 Direct net) & Spec D (280pp Expanded B&W: $4.36 KDP COGS, +$16.04 KDP net, +$27.11 Direct net).",
                "hypothesis": True,
                "paid_checkout_enabled": False,
            },
            "operator_bundle": {
                "label": "Complete Operator Bundle (Print + Digital + Workbook)",
                "range_label": "$79 Approved ($49–$99 Band)",
                "test_price_usd": 79,
                "includes": [
                    "6×9 Print Edition",
                    "Digital PDF + EPUB",
                    "6-Worksheet Operator Companion Workbook",
                ],
                "hypothesis": True,
                "paid_checkout_enabled": False,
                "notes": "6x9 Print Paperback + 8.5x11 Digital PDF + EPUB 3.0 + 6-Worksheet Operator Companion Workbook.",
            },
            "founder_collection": {
                "label": "Multi-Volume Playbook Collection",
                "range_label": "$199–$399",
                "test_price_usd": 249,
                "includes": [
                    "5-Volume Flagship Boxed/Digital Set",
                    "36-Business Money-to-Manpower Atlas",
                    "All Companion Workbooks",
                ],
                "hypothesis": True,
                "paid_checkout_enabled": False,
            },
            "club_membership": {
                "label": "The Fuck You Money Club Charter Membership",
                "range_label": "$290/yr ($39/mo Charter Tier)",
                "test_price_usd": 290,
                "billing_period": "monthly",
                "includes": [
                    "New Playbook Releases",
                    "Live Money-to-Manpower Deal Scorecards",
                    "Research Briefings & Operator Templates",
                ],
                "hypothesis": True,
                "paid_checkout_enabled": False,
                "notes": "All Big Money Playbook releases, live 36-business Money-to-Manpower deal scorecards, and operator templates.",
            },
        },
        "workflow_stages": _build_workflow_stages(),
        "expert_youtube_links_policy": {
            "min_links_per_book": MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
            "target_links_per_book": TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK,
            "min_links_per_chapter": MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
            "require_timestamp_deep_links": True,
            "require_across_all_editions": True,
        },
        "editorial_tracks": deepcopy(TRACK_DEFINITIONS),
        "editorial_notes": (
            "OWNER APPROVED: (1) Concept B — Bold Editorial (#09090B / #FFD400 / #FFFFFF) locked as "
            "Owner-Approved Series Master; (2) Volume 001 — Heir Hunting (87/100) and Volume 002 — "
            "Surplus Funds Recovery (86/100) completed through Quality Assurance with 5-layer FYMC "
            "content architecture; (3) Public deploy and paid checkout remain disabled pending final "
            "Publication Approval."
        ),
    }


# --------------------------------------------------------------------------
# 2. Chapter Markdown rendering
# --------------------------------------------------------------------------


def _render_table(table: object) -> list:
    """Render a table spec into Markdown lines."""
    lines: list = []
    if isinstance(table, str):
        return [table.strip(), ""]
    if not isinstance(table, dict):
        return lines

    title = _text(_first(table, "title", "caption", "name", default=""))
    columns = _first(table, "columns", "headers", "header", default=None)
    rows = _first(table, "rows", "data", "records", default=[]) or []

    if isinstance(rows, dict):
        rows = [rows]

    if not columns:
        keys: list = []
        for row in rows:
            if isinstance(row, dict):
                for key in row.keys():
                    if key not in keys:
                        keys.append(key)
        if keys:
            columns = keys
        elif rows:
            max_cols = max((len(r) if isinstance(r, (list, tuple)) else 1) for r in rows)
            columns = ["Item", "Value"] if max_cols == 2 else [f"Column {i}" for i in range(1, max_cols + 1)]

    columns = [str(col) for col in (columns or [])]
    if title:
        lines.append("**{0}**".format(title))
        lines.append("")
    if not columns:
        return lines

    lines.append("| " + " | ".join(columns) + " |")
    lines.append("| " + " | ".join(["---"] * len(columns)) + " |")
    for row in rows:
        if isinstance(row, dict):
            lower = {str(k).lower(): k for k in row}
            norm_map = {re.sub(r"[^a-z0-9]+", "_", str(k).lower()).strip("_"): k for k in row}
            cells = []
            for col in columns:
                actual = col if col in row else lower.get(col.lower())
                if actual is None:
                    actual = norm_map.get(re.sub(r"[^a-z0-9]+", "_", col.lower()).strip("_"))
                cells.append(_text(row[actual] if actual is not None else "").replace("\n", " "))
        elif isinstance(row, (list, tuple)):
            cells = [_text(cell).replace("\n", " ") for cell in row]
            cells += [""] * (len(columns) - len(cells))
            cells = cells[: len(columns)]
        else:
            cells = [_text(row)] + [""] * (len(columns) - 1)
        lines.append("| " + " | ".join(cell.replace("|", "\\|") for cell in cells) + " |")
    lines.append("")
    source = _text(_first(table, "source", "sources", "note", default=""))
    if source:
        lines.append("_Source: {0}_".format(source))
        lines.append("")
    return lines


def _render_sop(sop: object) -> list:
    lines: list = []
    if isinstance(sop, str):
        return [sop.strip(), ""]
    if not isinstance(sop, dict):
        return lines
    title = _text(_first(sop, "title", "name", default="Standard Operating Procedure"))
    lines.append("**SOP — {0}**".format(title))
    lines.append("")
    purpose = _text(_first(sop, "purpose", "objective", "goal", default=""))
    if purpose:
        lines.append("_Purpose: {0}_".format(purpose))
        lines.append("")
    steps = _first(sop, "steps", "procedure", "actions", default=[]) or []
    if isinstance(steps, (str, dict)):
        steps = [steps]
    for position, step in enumerate(steps, start=1):
        if isinstance(step, dict):
            label = _text(_first(step, "title", "action", "text", "step", default=""))
            detail = _text(_first(step, "detail", "details", "body", "notes", default=""))
            action = _text(_first(step, "action", "description", default=""))
            lines.append("{0}. {1}".format(position, label or detail))
            if action and action != label:
                lines.append("   - {0}".format(action))
            if label and detail:
                lines.append("   - {0}".format(detail.replace("\n", " ")))
        else:
            lines.append("{0}. {1}".format(position, _text(step)))
    lines.append("")
    owner = _text(_first(sop, "owner", "role", default=""))
    cadence = _text(_first(sop, "cadence", "frequency", default=""))
    if owner or cadence:
        meta = " · ".join(
            part
            for part in (
                "Owner: {0}".format(owner) if owner else "",
                "Cadence: {0}".format(cadence) if cadence else "",
            )
            if part
        )
        lines.append("_{0}_".format(meta))
        lines.append("")
    return lines


def _render_callout(callout: object) -> list:
    lines: list = []
    if isinstance(callout, str):
        body = callout.strip()
        if body:
            lines.append("> {0}".format(body.replace("\n", "\n> ")))
            lines.append("")
        return lines
    if not isinstance(callout, dict):
        return lines
    kind = _text(_first(callout, "kind", "type", "variant", default="NOTE")).upper()
    title = _text(_first(callout, "title", "heading", default=""))
    body = _text(_first(callout, "body", "text", "content", default=""))
    header = kind if not title else "{0} — {1}".format(kind, title)
    lines.append("> **{0}**".format(header))
    if body:
        lines.append("> ")
        lines.append("> {0}".format(body.replace("\n", "\n> ")))
    for item in callout.get("items", []):
        lines.append("> - " + _text(item))
    lines.append("")
    return lines


def _render_key_metrics(metrics: object) -> list:
    lines: list = []
    if not metrics:
        return lines
    if isinstance(metrics, dict):
        rows = [
            {"metric": key, "value": value}
            for key, value in metrics.items()
        ]
    else:
        rows = []
        for item in metrics:
            if isinstance(item, dict):
                rows.append(item)
            else:
                rows.append({"metric": _text(item), "value": ""})
    if not rows:
        return lines

    lines.append("### Key Metrics")
    lines.append("")
    lines.append("| Metric | Value | Confidence | Source |")
    lines.append("| --- | --- | --- | --- |")
    for row in rows:
        metric = _text(_first(row, "metric", "name", "label", "kpi", default=""))
        value = _text(_first(row, "value", "amount", "figure", "result", default=""))
        confidence = _text(
            _first(row, "confidence", "epistemic_status", "status", default="")
        )
        badge = _epistemic_badge(confidence) if confidence else ""
        source = _text(_first(row, "source", "citation", "reference", default=""))
        cells = [metric, value, badge, source]
        lines.append(
            "| "
            + " | ".join(cell.replace("\n", " ").replace("|", "\\|") for cell in cells)
            + " |"
        )
    lines.append("")
    return lines


def _normalize_section(section):
    if not isinstance(section, dict):
        return section
    result = dict(section)
    for canonical, aliases in (("paragraphs", ("body", "text", "content")),
                               ("bullets", ("points", "takeaways")),
                               ("tables", ("table",)),
                               ("callouts", ("callout", "notes"))):
        values = []
        for key in (canonical, *aliases):
            value = result.pop(key, None)
            for item in (value if isinstance(value, list) else [value]):
                if item is not None and (not values or values[-1] != item):
                    values.append(item)
        if values:
            result[canonical] = values
    return result


def _render_section(section: object, position: int) -> list:
    section = _normalize_section(section)
    lines: list = []
    if isinstance(section, str):
        lines.append(section.strip())
        lines.append("")
        return lines
    if not isinstance(section, dict):
        return lines

    heading = _text(
        _first(section, "heading", "title", "name", default="Section {0}".format(position))
    )
    badge = _epistemic_badge(
        _first(section, "epistemic_status", "epistemic", "confidence", "status", default="")
    )
    header = "## {0}".format(heading)
    if badge:
        header += "  `{0}`".format(badge)
    lines.append(header)
    lines.append("")

    body = _text(_first(section, "body", "text", "content", "paragraphs", default=""))
    if body:
        lines.append(body)
        lines.append("")

    bullets = _first(section, "bullets", "points", "takeaways", default=[]) or []
    if isinstance(bullets, str):
        bullets = [bullets]
    for bullet in bullets:
        lines.append("- {0}".format(_text(bullet).replace("\n", " ")))
    if bullets:
        lines.append("")

    tables = _first(section, "tables", "table", default=[]) or []
    if isinstance(tables, dict):
        tables = [tables]
    for table in tables:
        lines.extend(_render_table(table))

    sops = _first(section, "sops", "sop", "procedures", default=[]) or []
    if not sops and section.get("sop_steps"):
        lines.extend(_render_sop({"title": "Standard Operating Procedure", "steps": section["sop_steps"]}))
    if isinstance(sops, (dict, str)):
        sops = [sops]
    for sop in sops:
        lines.extend(_render_sop(sop))

    callouts = _first(section, "callouts", "callout", "notes", default=[]) or []
    if isinstance(callouts, (dict, str)):
        callouts = [callouts]
    for callout in callouts:
        lines.extend(_render_callout(callout))

    figure = _first(section, "diagram_id", "figure_id", "graphic_id", default="")
    if figure:
        lines.append("_Figure reference: `{0}`_".format(_text(figure)))
        lines.append("")

    return lines


def _render_citation(citation: object, position: int) -> str:
    if isinstance(citation, str):
        return "{0}. {1}".format(position, citation.strip())
    if not isinstance(citation, dict):
        return "{0}. {1}".format(position, _text(citation))
    title = _text(_first(citation, "title", "video_title", "name", "label", "statute", "authority", default=""))
    channel = _text(_first(citation, "channel", "author", "creator", "publisher", default=""))
    url = _text(_first(citation, "url", "link", "video_url", "source_url", default=""))
    locator = _text(_first(citation, "timestamp_label", "timestamp", "locator", "page", default=""))
    accessed = _text(_first(citation, "accessed", "date", "published", default=""))
    note_parts = []
    for nkey in ("tip", "text", "relevance", "note", "summary", "quote", "excerpt", "description"):
        nval = _text(citation.get(nkey, "")).replace("\n", " ")
        if nval and nval not in note_parts:
            note_parts.append(nval)
    parts = [part for part in (title, channel) if part]
    line = "{0}. {1}".format(position, " — ".join(parts) if parts else "Untitled source")
    if locator:
        line += " @ {0}".format(locator)
    if note_parts:
        line += ": {0}".format(" — ".join(note_parts))
    if url:
        line += " — <{0}>".format(url)
    if accessed:
        line += " (accessed {0})".format(accessed)
    return line


def chapter_to_markdown(chapter: dict) -> str:
    """Render one chapter dict into publication-ready Markdown."""
    chapter = chapter if isinstance(chapter, dict) else {}
    number = _chapter_number(chapter, 0)
    title = _text(_first(chapter, "title", "name", default="Untitled Chapter"))
    subtitle = _text(_first(chapter, "subtitle", "deck", "tagline", default=""))

    lines: list = ["# Chapter {0:02d}: {1}".format(number, title), ""]
    if subtitle:
        lines.append("*{0}*".format(subtitle))
        lines.append("")

    series_line = "{0} · {1}".format(BOOK_SERIES, PARENT_BRAND)
    lines.append("> {0}".format(series_line))
    lines.append("")

    summary = _text(
        _first(chapter, "executive_summary", "summary", "abstract", default="")
    )
    if summary:
        lines.append("## Executive Summary")
        lines.append("")
        lines.append(summary)
        lines.append("")

    lines.extend(
        _render_key_metrics(
            _first(chapter, "key_metrics", "metrics", "kpis", default=[])
        )
    )

    sections = _first(chapter, "sections", "body", "content", default=[]) or []
    if isinstance(sections, (str, dict)):
        sections = [sections]
    for position, section in enumerate(sections, start=1):
        lines.extend(_render_section(section, position))

    steps = chapter.get("sop_steps") or chapter.get("steps")
    if steps:
        lines.extend(_render_sop({"title": "Standard Operating Procedure", "steps": steps}))

    pull_quote = _text(_first(chapter, "pull_quote", "quote", "callout_quote", default=""))
    if pull_quote:
        lines.append("---")
        lines.append("")
        lines.append("> ### “{0}”".format(pull_quote.strip().strip('“”"')))
        lines.append("")

    checklist = _first(
        chapter, "action_checklist", "checklist", "actions", "next_actions", default=[]
    ) or []
    if isinstance(checklist, (str, dict)):
        checklist = [checklist]
    if checklist:
        lines.append("## Action Checklist")
        lines.append("")
        for item in checklist:
            if isinstance(item, dict):
                label = _text(
                    _first(item, "action", "task", "text", "label", "item", default="")
                )
                owner = _text(_first(item, "owner", "role", default=""))
                due = _text(_first(item, "due", "timeline", "when", default=""))
                done = bool(_first(item, "done", "complete", "completed", default=False))
                suffix = " · ".join(
                    part
                    for part in (
                        "Owner: {0}".format(owner) if owner else "",
                        "Due: {0}".format(due) if due else "",
                    )
                    if part
                )
                row = "- [{0}] {1}".format("x" if done else " ", label)
                if suffix:
                    row += " _({0})_".format(suffix)
                lines.append(row)
            else:
                lines.append("- [ ] {0}".format(_text(item).replace("\n", " ")))
        lines.append("")

    statutory = _first(chapter, "statutory_citations", default=[]) or []
    if isinstance(statutory, (str, dict)):
        statutory = [statutory]
    if statutory:
        lines.append("## Statutory & Primary Authorities")
        lines.append("")
        for position, citation in enumerate(statutory, start=1):
            lines.append(_render_citation(citation, position))
        lines.append("")

    citations = _first(
        chapter, "source_citations", "sources", "citations", "references", default=[]
    ) or []
    if isinstance(citations, (str, dict)):
        citations = [citations]
    if citations:
        lines.append("## Sources")
        lines.append("")
        for position, citation in enumerate(citations, start=1):
            lines.append(_render_citation(citation, position))
        lines.append("")

    rendered = "\n".join(lines).rstrip() + "\n"
    # Collapse any runs of blank lines introduced by empty blocks.
    while "\n\n\n" in rendered:
        rendered = rendered.replace("\n\n\n", "\n\n")
    return rendered


# --------------------------------------------------------------------------
# Scorecard helper
# --------------------------------------------------------------------------


def recompute_candidate_scorecard(candidate: dict) -> dict:
    """Re-run the rating engine for one candidate business."""
    return _as_dict(_invoke(compute_scorecard, candidate), "scorecard")


def _flagship_scorecard(pipeline: list) -> dict:
    scorecard = _as_dict(_invoke(get_flagship_scorecard), "scorecard")
    if scorecard:
        return scorecard
    for candidate in pipeline:
        if not isinstance(candidate, dict):
            continue
        identifier = _first(candidate, "id", "slug", "volume_id", "candidate_id", default="")
        rank = _first(candidate, "rank", "position", default=None)
        if identifier == FLAGSHIP_VOLUME_ID or rank in (1, "1"):
            return recompute_candidate_scorecard(candidate)
    if pipeline and isinstance(pipeline[0], dict):
        return recompute_candidate_scorecard(pipeline[0])
    return {}


def _volume_scorecard_for_slug(pipeline: list, volume_slug: str) -> dict:
    spec = get_volume_spec(volume_slug)
    for candidate in pipeline:
        if isinstance(candidate, dict) and candidate.get("candidate_number") == spec["candidate_number"]:
            return recompute_candidate_scorecard(candidate)
    return get_volume_scorecard(volume_slug)


# --------------------------------------------------------------------------
# Graphics review scaffolding
# --------------------------------------------------------------------------


def _diagram_ids(diagrams_data: dict) -> list:
    diagrams = _as_list(
        diagrams_data.get("diagrams", diagrams_data), "diagrams", "items", "figures"
    )
    ids: list = []
    for position, diagram in enumerate(diagrams, start=1):
        if isinstance(diagram, dict):
            identifier = _first(
                diagram, "id", "diagram_id", "slug", "key", default=None
            )
            if identifier:
                ids.append(str(identifier))
                continue
        if position <= len(DEFAULT_DIAGRAM_IDS):
            ids.append(DEFAULT_DIAGRAM_IDS[position - 1])
    # Pad/trim to the mandated 8-diagram program.
    for fallback in DEFAULT_DIAGRAM_IDS:
        if len(ids) >= 8:
            break
        if fallback not in ids:
            ids.append(fallback)
    return ids[:8]


def _diagram_labels(diagrams_data: dict, ids: list) -> dict:
    diagrams = _as_list(
        diagrams_data.get("diagrams", diagrams_data), "diagrams", "items", "figures"
    )
    labels: dict = {}
    for position, identifier in enumerate(ids):
        label = ""
        if position < len(diagrams) and isinstance(diagrams[position], dict):
            label = _text(
                _first(diagrams[position], "title", "label", "name", default="")
            )
        if not label:
            label = identifier.replace("_", " ").title()
        labels[identifier] = label
    return labels


def _build_graphics_reviews(
    diagrams_data: dict,
    existing: dict | None,
    *,
    volume_slug: str = VOLUME_SLUG,
) -> dict:
    existing = existing if isinstance(existing, dict) else {}
    previous = existing.get("reviews") if isinstance(existing.get("reviews"), dict) else {}

    diagram_ids = _diagram_ids(diagrams_data)
    labels = _diagram_labels(diagrams_data, diagram_ids)

    reviews: dict = {}
    ordered: list = []
    for graphic_id in list(COVER_GRAPHIC_IDS) + diagram_ids:
        is_cover = graphic_id in COVER_GRAPHIC_IDS
        label = COVER_LABELS.get(graphic_id) if is_cover else labels.get(graphic_id, graphic_id)
        ordered.append(graphic_id)
        prior_graphic = previous.get(graphic_id, {}) if isinstance(previous, dict) else {}
        per_concept: dict = {}
        for concept_id in CONCEPT_IDS:
            prior = (
                prior_graphic.get(concept_id)
                if isinstance(prior_graphic, dict)
                else None
            )
            entry = {
                "graphic_id": graphic_id,
                "graphic_type": "cover" if is_cover else "diagram",
                "label": label,
                "concept_id": concept_id,
                "concept_label": CONCEPT_LABELS.get(concept_id, concept_id),
                "status": "pending_review",
                "notes": "",
                "reviewed_at": None,
            }
            if isinstance(prior, dict):
                status = prior.get("status")
                if status in REVIEW_STATUSES:
                    entry["status"] = status
                notes = prior.get("notes")
                if isinstance(notes, str):
                    entry["notes"] = notes
                if prior.get("reviewed_at"):
                    entry["reviewed_at"] = prior["reviewed_at"]
            per_concept[concept_id] = entry
        reviews[graphic_id] = per_concept

    return {
        "volume_id": volume_slug,
        "volume_slug": volume_slug,
        "concepts": [
            {"id": concept_id, "label": CONCEPT_LABELS.get(concept_id, concept_id)}
            for concept_id in CONCEPT_IDS
        ],
        "graphic_order": ordered,
        "cover_graphic_ids": list(COVER_GRAPHIC_IDS),
        "diagram_graphic_ids": diagram_ids,
        "allowed_statuses": sorted(REVIEW_STATUSES),
        "reviews": reviews,
        "updated_at": _now_iso(),
    }


# --------------------------------------------------------------------------
# 3. Full store sync
# --------------------------------------------------------------------------


def _merge_brand_system(default: dict, existing: dict | None, force: bool) -> dict:
    merged = dict(default)
    merged["gates"] = _normalize_gates(default.get("gates"))
    if force or not isinstance(existing, dict) or not existing:
        merged["generated_at"] = _now_iso()
        merged["updated_at"] = merged["generated_at"]
        return merged

    for key in ("gates", "pricing_hypotheses", "active_preview_concept"):
        if key in existing and existing[key] not in (None, "", {}, []):
            merged[key] = existing[key]
    if isinstance(existing.get("editorial_notes"), str):
        merged["editorial_notes"] = existing["editorial_notes"]
    # Hard governance invariant: price tiers never silently enable checkout.
    prices = merged.get("pricing_hypotheses")
    if isinstance(prices, dict):
        for tier in prices.values():
            if isinstance(tier, dict):
                tier["hypothesis"] = True
                tier["paid_checkout_enabled"] = False
    merged["gates"] = _normalize_gates(merged.get("gates"))
    merged["generated_at"] = existing.get("generated_at") or _now_iso()
    merged["updated_at"] = _now_iso()
    return merged


def _merge_manuscript(
    fresh: dict,
    existing: dict | None,
    force: bool,
    *,
    volume_slug: str = VOLUME_SLUG,
) -> dict:
    """Keep saved chapter edits, refresh empty citation blocks."""
    if force or not isinstance(existing, dict) or not existing.get("chapters"):
        result = dict(fresh)
        fresh_ch = _as_list(result.get("chapters", []), "chapters")
        result["chapters"] = fresh_ch
        result["chapter_count"] = len(fresh_ch)
        result["total_word_count"] = compute_manuscript_word_count(fresh_ch)
        result.setdefault("volume_id", volume_slug)
        result["updated_at"] = _now_iso()
        return result

    fresh_chapters = _as_list(fresh.get("chapters", fresh), "chapters")
    existing_chapters = _as_list(existing.get("chapters"), "chapters")
    by_number: dict = {}
    for position, chapter in enumerate(fresh_chapters, start=1):
        if isinstance(chapter, dict):
            by_number[_chapter_number(chapter, position)] = chapter

    merged_chapters: list = []
    for position, chapter in enumerate(existing_chapters, start=1):
        if not isinstance(chapter, dict):
            continue
        number = _chapter_number(chapter, position)
        merged = dict(chapter)
        source = by_number.get(number, {})
        citations = list(merged.get("source_citations") or [])
        def citation_key(item):
            return (item.get("url"), item.get("text")) if isinstance(item, dict) else str(item)
        def tip_key(item):
            if isinstance(item, dict) and item.get("source_type") == "video_pro_tip":
                return (item.get("video_id"), item.get("timestamp_seconds"), item.get("text"))
            return None
        seen = {citation_key(item) for item in citations}
        tips = {tip_key(item): i for i, item in enumerate(citations) if tip_key(item) is not None}
        for item in source.get("source_citations", []) or []:
            key = citation_key(item)
            tip = tip_key(item)
            if tip is not None and tip in tips:
                citations[tips[tip]] = item
            elif key not in seen:
                citations.append(item)
                if tip is not None:
                    tips[tip] = len(citations) - 1
            seen.add(key)
        merged["source_citations"] = citations
        for key, value in source.items():
            if key in EDITABLE_CHAPTER_FIELDS:
                continue
            if merged.get(key) in (None, "", [], {}):
                merged[key] = value
        merged_chapters.append(merged)

    # Any brand-new chapters produced by the builder get appended.
    seen = {_chapter_number(ch, i) for i, ch in enumerate(merged_chapters, start=1)}
    for number in sorted(by_number):
        if number not in seen:
            merged_chapters.append(by_number[number])

    merged_chapters.sort(key=lambda ch: _chapter_number(ch, 0))

    result = dict(existing)
    for key, value in fresh.items():
        if key == "chapters":
            continue
        result.setdefault(key, value)
    result["chapters"] = merged_chapters
    result["chapter_count"] = len(merged_chapters)
    result["total_word_count"] = compute_manuscript_word_count(merged_chapters)
    result["min_expert_youtube_links_per_book"] = MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK
    result["target_expert_youtube_links_per_book"] = TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK
    result["min_expert_youtube_links_per_chapter"] = MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER
    result["expert_youtube_link_count"] = count_manuscript_youtube_links(merged_chapters)
    result.setdefault("volume_id", volume_slug)
    result["updated_at"] = _now_iso()
    return result


def _build_volume_metadata(
    scorecard: dict,
    manuscript: dict,
    *,
    volume_slug: str = VOLUME_SLUG,
) -> dict:
    chapters = _as_list(manuscript.get("chapters", manuscript), "chapters")
    yt_count = count_manuscript_youtube_links(chapters)
    spec = get_volume_spec(volume_slug)
    default_title = spec["title"]
    default_subtitle = spec["subtitle"]
    return {
        "volume_id": volume_slug,
        "volume_slug": volume_slug,
        "volume_number": spec["volume_number"],
        "site_ui": deepcopy(spec["site_ui"]),
        "parent_brand": PARENT_BRAND,
        "book_series": BOOK_SERIES,
        "tagline": BRAND_TAGLINE,
        "title": _text(
            _first(manuscript, "title", "book_title", default=default_title)
        )
        or default_title,
        "subtitle": _text(
            _first(
                manuscript,
                "subtitle",
                default=default_subtitle,
            )
        ),
        "chapter_count": len(chapters),
        "total_word_count": manuscript.get("total_word_count", compute_manuscript_word_count(chapters)),
        "expert_youtube_link_count": yt_count,
        "min_expert_youtube_links_required": MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        "target_expert_youtube_links": TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        "min_expert_youtube_links_per_chapter": MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
        "rating_system": RATING_SYSTEM_NAME,
        "composite_score": resolve_score_value(scorecard, default=None),
        "formats": [
            "8.5×11 Executive Digital PDF",
            "6×9 Print Edition",
            "Reflowable EPUB 3.0",
        ],
        "isbn": None,
        "publication_status": "approved_master",
        "public_deploy_approved": False,
        "paid_sales_approved": False,
        "updated_at": _now_iso(),
    }


_VOLUME_BUILDERS_CACHE: dict[tuple, tuple[dict, dict, dict]] = {}
_VOLUME_BUILDERS_CACHE_LOCK = threading.Lock()


def _abridged_fingerprint(abridged: list[dict]) -> tuple[int, str]:
    return (
        len(abridged),
        hashlib.sha256(json.dumps(
            abridged,
            sort_keys=True,
            default=str,
            separators=(",", ":"),
        ).encode("utf-8")).hexdigest()[:24],
    )


def _fresh_volume_builders(
    volume_slug: str,
    abridged: list[dict],
    *,
    _fingerprint: tuple[int, str] | None = None,
) -> tuple[dict, dict, dict]:
    spec = get_volume_spec(volume_slug)
    num = spec["volume_number"]
    source_path = Path(__file__).with_name(f"volume_{num:03d}_manuscript.py")
    fingerprint = _abridged_fingerprint(abridged) if _fingerprint is None else _fingerprint
    key = (spec["volume_id"], fingerprint, source_path.stat().st_mtime_ns)
    with _VOLUME_BUILDERS_CACHE_LOCK:
        if key in _VOLUME_BUILDERS_CACHE:
            return deepcopy(_VOLUME_BUILDERS_CACHE[key])
    diagrams_builder, manuscript_builder, workbook_builder = load_volume_builders(volume_slug)
    result = (
        _as_dict(_invoke(diagrams_builder), "diagrams"),
        _as_dict(_invoke(workbook_builder), "worksheets"),
        _as_dict(_invoke(manuscript_builder, abridged), "chapters"),
    )
    with _VOLUME_BUILDERS_CACHE_LOCK:
        _VOLUME_BUILDERS_CACHE[key] = deepcopy(result)
        while len(_VOLUME_BUILDERS_CACHE) > 96:
            del _VOLUME_BUILDERS_CACHE[next(iter(_VOLUME_BUILDERS_CACHE))]
    return result


def sync_publishing_store(
    root_dir: Path,
    abridged_videos: list[dict] | None = None,
    raw_videos: list[dict] | None = None,
    force: bool = False,
    *,
    only_volumes: tuple[str, ...] | list[str] | set[str] | None = None,
) -> dict:
    """Refresh shared publishing data and all or selected volume files.

    Existing owner-controlled state (gates, pricing hypotheses, preview concept,
    chapter edits, graphics review notes, newsletter subscribers) is preserved
    unless ``force`` is set.
    """
    published_slugs = get_published_volume_ids()
    target_slugs = set(published_slugs) if only_volumes is None else {
        resolve_volume_slug(item) for item in only_volumes
    }
    with _root_lock(root_dir):
        root = Path(root_dir).resolve()
        _recover_journal(root)
        pub = _publishing_dir(root)
        volume = _volume_dir(root, VOLUME_SLUG)
        json_writes = []
        text_writes = []

        def stage_json(path, payload):
            _resolve_contained(root, path)
            if not force:
                _read_json(path, strict=True)
            json_writes.append((path, payload))
            return path

        abridged = list(abridged_videos or [])
        abridged_fp = _abridged_fingerprint(abridged)
        raw = list(raw_videos or [])

        # --- brand -----------------------------------------------------------
        brand_path = pub / "brand" / "brand_system.json"
        existing_brand = _read_json(brand_path, None, strict=not force)
        brand = _merge_brand_system(
            build_default_brand_system(),
            existing_brand if isinstance(existing_brand, dict) else None,
            force,
        )

        # --- audit -----------------------------------------------------------
        audit = _as_dict(_invoke(audit_existing_workspace, root), "audit")
        audit.setdefault("generated_at", _now_iso())
        audit_path = stage_json(pub / "audit" / "existing_work_audit.json", audit)

        # --- catalog ---------------------------------------------------------
        pipeline = _as_list(
            _invoke(build_29_candidate_pipeline), "candidates", "pipeline", "businesses"
        )
        catalog_payload = {
            "parent_brand": PARENT_BRAND,
            "book_series": BOOK_SERIES,
            "rating_system": RATING_SYSTEM_NAME,
            "candidate_count": len(pipeline),
            "flagship_volume_id": FLAGSHIP_VOLUME_ID,
            "published_volume_ids": list(published_slugs),
            "editorial_tracks": deepcopy(TRACK_DEFINITIONS),
            "editorial_plays": deepcopy(PLAY_DEFINITIONS),
            "candidates": pipeline,
            "generated_at": _now_iso(),
        }
        catalog_path = stage_json(
            pub / "catalog" / "pipeline_29_candidates.json", catalog_payload
        )

        # --- research --------------------------------------------------------
        research_db = _invoke(build_research_database, abridged, raw)
        research_summary = {
            "abridged_video_count": len(abridged),
            "raw_video_count": len(raw),
            "summary": _summarize_payload(research_db),
            "generated_at": _now_iso(),
        }
        if isinstance(research_db, dict):
            for key in ("topics", "entities", "themes", "sources", "videos"):
                value = research_db.get(key)
                if isinstance(value, (list, dict)):
                    research_summary.setdefault("counts", {})[key] = len(value)
        if isinstance(research_db, dict):
            for key in ("topics", "consensus_findings", "claims_requiring_verification",
                        "permissions_ledger", "corpus_metrics", "coverage", "schema_version"):
                research_summary[key] = research_db.get(key, [] if key in (
                    "topics", "consensus_findings", "claims_requiring_verification", "permissions_ledger") else {})
            research_summary["conflicting_views"] = research_summary["claims_requiring_verification"]
        research_path = pub / "research" / "research_database_summary.json"
        prior_research = _read_json(research_path, {}, strict=not force)
        prior_research = prior_research if isinstance(prior_research, dict) else {}
        if not force and not abridged and (prior_research.get("topics") or prior_research.get("abridged_video_count", 0) > 0):
            research_summary.update(prior_research)
        stage_json(research_path, research_summary)

        # --- volume payloads (all published volumes) -------------------------
        volume_paths_by_slug: dict[str, dict] = {}
        flagship_chapter_files: list[str] = []
        flagship_graphics_reviews: dict = {}
        flagship_workbook: dict = {}
        builder_kwargs = (
            {"_fingerprint": abridged_fp}
            if "_fingerprint" in inspect.signature(_fresh_volume_builders).parameters
            else {}
        )

        for vol_slug in published_slugs:
            vol_dir = _volume_dir(root, vol_slug)
            vol_chapters_dir = _resolve_contained(root, vol_dir / "chapters")
            if vol_slug not in target_slugs:
                chapter_files = []
                for path in sorted(vol_chapters_dir.glob("chapter-*.md")):
                    _resolve_contained(root, path)
                    chapter_files.append(str(path))
                volume_paths_by_slug[vol_slug] = {
                    "volume_dir": str(vol_dir),
                    **{name: str(vol_dir / (name + ".json")) for name in (
                        "metadata", "scorecard", "diagrams_data", "manuscript",
                        "workbook", "graphics_reviews",
                    )},
                    "chapters": chapter_files,
                }
                if vol_slug == VOLUME_SLUG:
                    flagship_chapter_files = chapter_files
                    flagship_graphics_reviews = _read_json(
                        vol_dir / "graphics_reviews.json", {}, strict=True
                    ) or {}
                    flagship_workbook = _read_json(
                        vol_dir / "workbook.json", {}, strict=True
                    ) or {}
                continue
            vol_scorecard = _volume_scorecard_for_slug(pipeline, vol_slug)
            vol_diagrams_data, vol_workbook, vol_fresh_manuscript = _fresh_volume_builders(
                vol_slug, abridged, **builder_kwargs
            )
            vol_manuscript_path = vol_dir / "manuscript.json"
            existing_manuscript = _read_json(vol_manuscript_path, None, strict=not force)
            vol_manuscript = _merge_manuscript(
                vol_fresh_manuscript,
                existing_manuscript if isinstance(existing_manuscript, dict) else None,
                force,
                volume_slug=vol_slug,
            )
            vol_metadata = _build_volume_metadata(
                vol_scorecard, vol_manuscript, volume_slug=vol_slug
            )
            for chapter in vol_manuscript.get("chapters", []):
                chapter["revision"] = _chapter_revision(chapter)
            stage_json(vol_dir / "metadata.json", vol_metadata)
            stage_json(vol_dir / "scorecard.json", vol_scorecard)
            stage_json(vol_dir / "diagrams_data.json", vol_diagrams_data)
            stage_json(vol_manuscript_path, vol_manuscript)
            stage_json(vol_dir / "workbook.json", vol_workbook)

            vol_reviews_path = vol_dir / "graphics_reviews.json"
            existing_reviews = _read_json(vol_reviews_path, None, strict=not force)
            vol_graphics_reviews = _build_graphics_reviews(
                vol_diagrams_data,
                None if force else (existing_reviews if isinstance(existing_reviews, dict) else None),
                volume_slug=vol_slug,
            )
            stage_json(vol_reviews_path, vol_graphics_reviews)

            chapters = _as_list(vol_manuscript.get("chapters", vol_manuscript), "chapters")
            vol_chapter_files: list[str] = []
            for position, chapter in enumerate(chapters, start=1):
                if not isinstance(chapter, dict):
                    continue
                number = _chapter_number(chapter, position)
                cpath = vol_chapters_dir / _chapter_filename(number)
                text_writes.append((cpath, chapter_to_markdown(chapter)))
                vol_chapter_files.append(str(cpath))

            volume_paths_by_slug[vol_slug] = {
                "volume_dir": str(vol_dir),
                "metadata": str(vol_dir / "metadata.json"),
                "scorecard": str(vol_dir / "scorecard.json"),
                "diagrams_data": str(vol_dir / "diagrams_data.json"),
                "manuscript": str(vol_manuscript_path),
                "workbook": str(vol_dir / "workbook.json"),
                "graphics_reviews": str(vol_reviews_path),
                "chapters": vol_chapter_files,
            }
            if vol_slug == VOLUME_SLUG:
                flagship_chapter_files = vol_chapter_files
                flagship_graphics_reviews = vol_graphics_reviews
                flagship_workbook = vol_workbook

        # --- site ------------------------------------------------------------
        signup_path = pub / "site" / "newsletter_signups.json"
        signups = _read_json(signup_path, None, strict=not force)
        if not isinstance(signups, dict) or not isinstance(signups.get("subscribers"), list):
            signups = {"subscribers": []}
        stage_json(signup_path, signups)
        stage_json(brand_path, brand)
        _commit_store_transaction(root, json_writes, text_writes)
        return {
            "ok": True,
            "forced": bool(force),
            "publishing_dir": str(pub),
            "volume_dir": str(volume),
            "volumes": volume_paths_by_slug,
            "paths": {
                "brand_system": str(brand_path),
                "existing_work_audit": str(audit_path),
                "pipeline_29_candidates": str(catalog_path),
                "research_database_summary": str(research_path),
                "metadata": str(volume / "metadata.json"),
                "scorecard": str(volume / "scorecard.json"),
                "diagrams_data": str(volume / "diagrams_data.json"),
                "manuscript": str(volume / "manuscript.json"),
                "workbook": str(volume / "workbook.json"),
                "graphics_reviews": str(volume / "graphics_reviews.json"),
                "newsletter_signups": str(signup_path),
                "chapters": flagship_chapter_files,
            },
            "counts": {
                "candidates": len(pipeline),
                "published_volumes": len(published_slugs),
                "chapters": len(flagship_chapter_files),
                "diagrams": len(flagship_graphics_reviews.get("diagram_graphic_ids", [])),
                "covers": len(flagship_graphics_reviews.get("cover_graphic_ids", [])),
                "graphics_review_entries": sum(
                    len(entry) for entry in flagship_graphics_reviews.get("reviews", {}).values()
                ),
                "workbook_worksheets": len(
                    _as_list(flagship_workbook.get("worksheets", []), "worksheets")
                ),
                "abridged_videos": len(abridged),
                "raw_videos": len(raw),
                "newsletter_subscribers": len(signups.get("subscribers", [])),
            },
            "gates": brand.get("gates", {}),
            "synced_at": _now_iso(),
        }


# --------------------------------------------------------------------------
# 4. Partial-update helpers
# --------------------------------------------------------------------------


def _ensure_initialized(root_dir: Path) -> None:
    _recover_journal(root_dir)
    pub = _publishing_dir(root_dir)
    required = [
        pub / "brand" / "brand_system.json",
        pub / "catalog" / "pipeline_29_candidates.json",
        pub / "audit" / "existing_work_audit.json",
        pub / "research" / "research_database_summary.json",
        pub / "site" / "newsletter_signups.json",
    ]
    for vol_slug in get_published_volume_ids():
        vol_dir = _volume_dir(root_dir, vol_slug)
        required.extend(
            vol_dir / name
            for name in (
                "manuscript.json",
                "metadata.json",
                "scorecard.json",
                "diagrams_data.json",
                "workbook.json",
                "graphics_reviews.json",
            )
        )
    for path in required:
        _resolve_contained(root_dir, path)
        _read_json(path, strict=True)
    for vol_slug in get_published_volume_ids():
        vol_dir = _volume_dir(root_dir, vol_slug)
        required.extend(
            vol_dir / "chapters" / _chapter_filename(i)
            for i in range(1, CHAPTER_COUNT + 1)
        )
    if not all(path.is_file() for path in required):
        sync_publishing_store(root_dir)


def _load_single_volume_bundle(root: Path, vol_slug: str, read_store) -> dict:
    vol_dir = _volume_dir(root, vol_slug)
    chapters_dir = vol_dir / "chapters"
    chapter_markdown: dict = {}
    if chapters_dir.is_dir():
        for path in sorted(chapters_dir.glob("chapter-*.md")):
            try:
                _resolve_contained(root, path)
                chapter_markdown[path.stem] = path.read_text(encoding="utf-8")
            except OSError:
                continue
    manuscript = read_store(vol_dir / "manuscript.json", {}) or {}
    for chapter in manuscript.get("chapters", []):
        chapter["revision"] = _chapter_revision(chapter)
    scorecard = read_store(vol_dir / "scorecard.json", {}) or {}
    default_cand_num = get_volume_spec(vol_slug)["candidate_number"]
    if isinstance(scorecard, dict) and "track_ids" not in scorecard:
        scorecard.update(
            get_candidate_track_metadata(scorecard.get("candidate_number", default_cand_num))
        )
    return {
        "metadata": read_store(vol_dir / "metadata.json", {}) or {},
        "scorecard": scorecard,
        "diagrams_data": read_store(vol_dir / "diagrams_data.json", {}) or {},
        "manuscript": manuscript,
        "workbook": read_store(vol_dir / "workbook.json", {}) or {},
        "graphics_reviews": read_store(vol_dir / "graphics_reviews.json", {}) or {},
        "chapter_markdown": chapter_markdown,
    }


def load_publishing_state(
    root_dir: Path,
    volume_id: object = None,
    *,
    verify_manifest: bool = False,
) -> dict:
    """Read the entire ``publishing/`` store into one dict (auto-initializing)."""
    active_slug = resolve_volume_slug(volume_id)
    with _root_lock(root_dir):
        root = Path(root_dir)
        if verify_manifest:
            manifest_report = verify_commit_manifest(root, strict=True)
            _ensure_initialized(root)
        else:
            _ensure_initialized(root)
            manifest_report = verify_commit_manifest(root, strict=False)
        pub = _publishing_dir(root)
        active_volume_dir = _volume_dir(root, active_slug)

        signups = _read_json(pub / "site" / "newsletter_signups.json", {"subscribers": []}, strict=True)
        if not isinstance(signups, dict):
            signups = {"subscribers": []}

        def read_store(path, default=None):
            return _read_json(path, default, strict=True)

        volumes_map: dict[str, dict] = {
            slug: _load_single_volume_bundle(root, slug, read_store)
            for slug in get_published_volume_ids()
        }
        active_bundle = volumes_map[active_slug]

        state = {
            "root_dir": str(root),
            "publishing_dir": str(pub),
            "volume_dir": str(active_volume_dir),
            "active_volume_id": active_slug,
            "brand_system": read_store(pub / "brand" / "brand_system.json", {}) or {},
            "existing_work_audit": read_store(pub / "audit" / "existing_work_audit.json", {})
            or {},
            "pipeline_29_candidates": read_store(
                pub / "catalog" / "pipeline_29_candidates.json", {}
            )
            or {},
            "research_database_summary": read_store(
                pub / "research" / "research_database_summary.json", {}
            )
            or {},
            "volumes": volumes_map,
            "volume": active_bundle,
            "newsletter_signups": signups,
            "loaded_at": _now_iso(),
        }
        state["manifest_verified"] = manifest_report["passed"]
        state["brand_system"]["gates"] = _normalize_gates(state["brand_system"].get("gates"))
        state["brand_system"].setdefault("editorial_tracks", deepcopy(TRACK_DEFINITIONS))
        if isinstance(state.get("pipeline_29_candidates"), dict):
            state["pipeline_29_candidates"].setdefault("editorial_tracks", deepcopy(TRACK_DEFINITIONS))
            for cand in _as_list(state["pipeline_29_candidates"].get("candidates", []), "candidates"):
                if isinstance(cand, dict) and "track_ids" not in cand:
                    cand.update(get_candidate_track_metadata(cand.get("candidate_number")))
        state["gates"] = dict(state["brand_system"]["gates"])
        state["settings"] = dict(state["brand_system"].get("gates", {}))
        manuscript = active_bundle["manuscript"]
        chapter_markdown = active_bundle["chapter_markdown"]
        state["counts"] = {
            "published_volumes": len(volumes_map),
            "chapters": len(_as_list(manuscript.get("chapters", []), "chapters")),
            "chapter_markdown_files": len(chapter_markdown),
            "candidates": len(
                _as_list(
                    state["pipeline_29_candidates"].get("candidates", []), "candidates"
                )
            ),
            "newsletter_subscribers": len(signups.get("subscribers", []) or []),
        }
        return state


def _strip_xml_controls(value):
    if isinstance(value, str):
        return "".join(c for c in value if c in "\t\n\r" or
                       0x20 <= ord(c) <= 0xD7FF or 0xE000 <= ord(c) <= 0xFFFD or
                       0x10000 <= ord(c) <= 0x10FFFF)
    if isinstance(value, list):
        return [_strip_xml_controls(item) for item in value]
    if isinstance(value, dict):
        return {_strip_xml_controls(key): _strip_xml_controls(item) for key, item in value.items()}
    return value


def _valid_chapter_field(key, value):
    def string_list(item):
        return isinstance(item, str) or (isinstance(item, list) and all(isinstance(v, str) for v in item))

    def records(item, validator):
        return all(validator(v) for v in (item if isinstance(item, list) else [item]))

    def table(item):
        return (isinstance(item, dict) and isinstance(item.get("rows"), list)
                and all(name not in item or (isinstance(item[name], list)
                        and all(isinstance(v, str) for v in item[name]))
                        for name in ("headers", "columns")))

    def sop(item):
        if isinstance(item, str):
            return True
        if not isinstance(item, dict):
            return False
        for name in ("step", "title", "action", "description", "text", "detail",
                     "details", "body", "notes"):
            if name in item and (not isinstance(item[name], (str, int)) or isinstance(item[name], bool)):
                return False
        return all(name not in item or records(item[name], sop)
                   for name in ("steps", "procedure", "actions"))

    def callout(item):
        if isinstance(item, str):
            return True
        return (isinstance(item, dict)
                and all(name not in item or isinstance(item[name], str)
                        for name in ("title", "heading", "body", "text", "content", "kind", "type", "variant"))
                and ("items" not in item or (isinstance(item["items"], list)
                     and all(isinstance(v, str) for v in item["items"]))))

    def section(item):
        if isinstance(item, str):
            return True
        if not isinstance(item, dict):
            return False
        for name, field in item.items():
            if name in ("heading", "title", "name", "epistemic_status"):
                if not isinstance(field, str):
                    return False
            elif name in ("body", "text", "content", "paragraphs", "bullets", "points", "takeaways"):
                if not string_list(field):
                    return False
            elif name in ("table", "tables"):
                if not records(field, table):
                    return False
            elif name in ("sops", "sop", "procedures", "sop_steps"):
                if not records(field, sop):
                    return False
            elif name in ("callouts", "callout", "notes"):
                if not records(field, callout):
                    return False
        return True

    if key in ("title", "subtitle", "executive_summary"):
        return isinstance(value, str) and (key != "title" or bool(_strip_xml_controls(value).strip()))
    if key == "pull_quote":
        return isinstance(value, str) or (isinstance(value, dict) and all(isinstance(v, str) for v in value.values()))
    if key == "sections":
        return isinstance(value, list) and all(section(item) for item in value)
    if key == "action_checklist":
        return isinstance(value, list) and all(isinstance(item, (str, dict)) for item in value)
    if key in ("statutory_citations", "source_citations"):
        return isinstance(value, list) and all(
            isinstance(item, str) or (
                isinstance(item, dict)
                and all(
                    isinstance(k, str)
                    and (v is None or isinstance(v, (str, int, float)))
                    and not isinstance(v, bool)
                    and (not isinstance(v, float) or math.isfinite(v))
                    for k, v in item.items()
                )
            )
            for item in value
        )
    return False


def update_chapter_content(root_dir: Path, chapter_number: int | str, patch=None,
                           expected_revision: str | None = None,
                           *,
                           volume_id: object = None) -> dict:
    """Patch one chapter in ``manuscript.json`` and rewrite only its Markdown."""
    vol_slug = resolve_volume_slug(volume_id)
    with _root_lock(root_dir):
        root = Path(root_dir)
        _ensure_initialized(root)
        volume = _volume_dir(root, vol_slug)
        manuscript_path = volume / "manuscript.json"

        manuscript = _read_json(manuscript_path, {}, strict=True)
        if not isinstance(manuscript, dict):
            manuscript = {}
        chapters = _as_list(manuscript.get("chapters", []), "chapters")

        try:
            if isinstance(chapter_number, (bool, float)):
                raise ValueError("invalid_chapter_number")
            raw_number = chapter_number
            if isinstance(chapter_number, str):
                match = re.fullmatch(r"^(?:q|ch(?:apter)?[-_]?)?(\d+)$", chapter_number.strip(), re.I)
                if not match:
                    raise ValueError("invalid_chapter_number")
                raw_number = match.group(1)
            target_number = int(raw_number)
        except (TypeError, ValueError):
            return {
                "ok": False,
                "error": "invalid_chapter_number",
                "chapter_number": chapter_number,
            }

        if isinstance(patch, dict) and "content" in patch:
            patch = dict(patch)
            content = patch.pop("content")
            patch.setdefault("executive_summary", content)

        if not isinstance(patch, dict) or not patch:
            return {"ok": False, "error": "empty_patch", "chapter_number": target_number}

        patch = dict(patch)
        patch_revision = patch.pop("expected_revision", None)
        if expected_revision is None:
            expected_revision = patch_revision
        rejected = [key for key in patch if key not in EDITABLE_CHAPTER_FIELDS]
        applied = {key: value for key, value in patch.items() if key in EDITABLE_CHAPTER_FIELDS}
        if not applied:
            return {
                "ok": False,
                "error": "no_editable_fields",
                "chapter_number": target_number,
                "editable_fields": list(EDITABLE_CHAPTER_FIELDS),
                "rejected_fields": rejected,
            }

        invalid_fields = [key for key, value in applied.items()
                          if not _valid_chapter_field(key, value)]
        if invalid_fields:
            return {"ok": False, "error": "invalid_field_type",
                    "chapter_number": target_number, "invalid_fields": invalid_fields}
        applied = _strip_xml_controls(applied)

        index = None
        for position, chapter in enumerate(chapters):
            if isinstance(chapter, dict) and _chapter_number(chapter, position + 1) == target_number:
                index = position
                break
        if index is None:
            return {
                "ok": False,
                "error": "chapter_not_found",
                "chapter_number": target_number,
                "available": [
                    _chapter_number(ch, i + 1)
                    for i, ch in enumerate(chapters)
                    if isinstance(ch, dict)
                ],
            }

        current_rev = _chapter_revision(chapters[index])
        if expected_revision is not None and expected_revision != current_rev:
            return {"ok": False, "error": "revision_conflict", "chapter_number": target_number,
                    "expected_revision": expected_revision, "current_revision": current_rev}
        updated = dict(chapters[index])
        updated.update(applied)
        if "sections" in applied:
            updated["sections"] = [_normalize_section(s) for s in applied["sections"]]
        updated["updated_at"] = _now_iso()
        updated["revision"] = _chapter_revision(updated)
        try:
            rendered_md = chapter_to_markdown(updated)
        except (TypeError, ValueError):
            return {"ok": False, "error": "invalid_field_type",
                    "chapter_number": target_number, "invalid_fields": list(applied)}
        chapters[index] = updated

        manuscript["chapters"] = chapters
        manuscript["chapter_count"] = len(chapters)
        manuscript["total_word_count"] = compute_manuscript_word_count(chapters)
        manuscript["expert_youtube_link_count"] = count_manuscript_youtube_links(chapters)
        manuscript["updated_at"] = _now_iso()
        markdown_path = volume / "chapters" / _chapter_filename(target_number)
        json_writes = [(manuscript_path, manuscript)]
        metadata_path = volume / "metadata.json"
        if "source_citations" in applied and metadata_path.is_file():
            metadata = _read_json(metadata_path, {}, strict=True)
            if isinstance(metadata, dict):
                metadata = dict(metadata)
                metadata["expert_youtube_link_count"] = manuscript["expert_youtube_link_count"]
                metadata["updated_at"] = manuscript["updated_at"]
                json_writes.append((metadata_path, metadata))
        _commit_store_transaction(root, json_writes,
                                  [(markdown_path, rendered_md)])

        return {
            "ok": True,
            "chapter_number": target_number,
            "updated_fields": sorted(applied.keys()),
            "rejected_fields": rejected,
            "manuscript_path": str(manuscript_path),
            "markdown_path": str(markdown_path),
            "chapter": updated,
            "expert_youtube_link_count": manuscript["expert_youtube_link_count"],
            "updated_at": manuscript["updated_at"],
        }


def update_graphic_review(
    root_dir: Path,
    graphic_id: str,
    concept_id: str = "concept_a",
    status: str = "pending_review",
    notes: str | None = None,
    *,
    volume_id: object = None,
) -> dict:
    """Record one cover/diagram review without touching any other state."""
    vol_slug = resolve_volume_slug(volume_id)
    with _root_lock(root_dir):
        root = Path(root_dir)
        _ensure_initialized(root)
        vol_dir = _volume_dir(root, vol_slug)
        reviews_path = vol_dir / "graphics_reviews.json"

        status = {"reviewed": "approved", "pending": "pending_review"}.get(status, status)
        if status not in REVIEW_STATUSES:
            return {
                "ok": False,
                "error": "invalid_status",
                "status": status,
                "allowed_statuses": sorted(REVIEW_STATUSES),
            }

        payload = _read_json(reviews_path, None, strict=True)
        if not isinstance(payload, dict) or not isinstance(payload.get("reviews"), dict):
            diagrams_data = _read_json(vol_dir / "diagrams_data.json", {}) or {}
            payload = _build_graphics_reviews(
                diagrams_data if isinstance(diagrams_data, dict) else {},
                None,
                volume_slug=vol_slug,
            )

        reviews = payload["reviews"]
        graphic = reviews.get(graphic_id)
        is_cover = graphic_id in COVER_GRAPHIC_IDS
        is_diagram = graphic_id in DEFAULT_DIAGRAM_IDS or bool(
            re.fullmatch(r"(?:diag-0[1-8]-[a-z0-9]+(?:-[a-z0-9]+)*|diagram_0[1-8]_[a-z0-9]+(?:_[a-z0-9]+)*)", graphic_id)
        )
        if not isinstance(graphic, dict) and (is_cover or is_diagram):
            graphic = {
                identifier: {
                    "graphic_id": graphic_id,
                    "graphic_type": "cover" if is_cover else "diagram",
                    "label": COVER_LABELS.get(graphic_id, graphic_id),
                    "concept_id": identifier,
                    "concept_label": CONCEPT_LABELS[identifier],
                    "status": "pending_review",
                    "notes": "",
                    "reviewed_at": None,
                }
                for identifier in CONCEPT_IDS
            }
            reviews[graphic_id] = graphic
            for key in ("graphic_order", "cover_graphic_ids" if is_cover else "diagram_graphic_ids"):
                identifiers = payload.setdefault(key, [])
                if graphic_id not in identifiers:
                    identifiers.append(graphic_id)
        if not isinstance(graphic, dict):
            return {
                "ok": False,
                "error": "unknown_graphic_id",
                "graphic_id": graphic_id,
                "known_graphic_ids": sorted(reviews.keys()),
            }

        entry = graphic.get(concept_id)
        if not isinstance(entry, dict):
            return {
                "ok": False,
                "error": "unknown_concept_id",
                "graphic_id": graphic_id,
                "concept_id": concept_id,
                "known_concept_ids": sorted(graphic.keys()),
            }

        timestamp = _now_iso()
        entry = dict(entry)
        entry["status"] = status
        if notes is not None:
            if not isinstance(notes, str):
                return {"ok": False, "error": "invalid_notes"}
            entry["notes"] = _strip_xml_controls(notes)
        entry.setdefault("notes", "")
        entry["reviewed_at"] = timestamp
        graphic[concept_id] = entry
        reviews[graphic_id] = graphic
        payload["reviews"] = reviews
        payload["updated_at"] = timestamp

        _commit_store_transaction(root, [(reviews_path, payload)], [])

        status_counts: dict = {key: 0 for key in sorted(REVIEW_STATUSES)}
        for per_concept in reviews.values():
            if not isinstance(per_concept, dict):
                continue
            for item in per_concept.values():
                if isinstance(item, dict) and item.get("status") in status_counts:
                    status_counts[item["status"]] += 1

        return {
            "ok": True,
            "graphic_id": graphic_id,
            "concept_id": concept_id,
            "status": status,
            "notes": entry["notes"],
            "reviewed_at": timestamp,
            "path": str(reviews_path),
            "status_counts": status_counts,
            "review": entry,
        }


def update_publishing_settings(root_dir: Path, patch: dict) -> dict:
    """Update pricing hypotheses, preview concept, or editorial notes.

    Section 3 Design Approval Gate: ``gates.approved_concept_id`` is forced back
    to ``None``. Dictionary flags cannot approve design, deployment, or sales.
    Selecting a preview concept is never an approval.
    """
    with _root_lock(root_dir):
        root = Path(root_dir)
        _ensure_initialized(root)
        brand_path = _publishing_dir(root) / "brand" / "brand_system.json"

        brand = _read_json(brand_path, None, strict=True)
        if not isinstance(brand, dict) or not brand:
            brand = build_default_brand_system()

        if not isinstance(patch, dict):
            patch = {}

        gates = brand.get("gates")
        if not isinstance(gates, dict):
            gates = dict(build_default_brand_system()["gates"])
        gates = dict(gates)

        applied: list = []
        rejected: list = []

        # -- pricing hypotheses (deep merge per tier) -------------------------
        pricing_patch = patch.get("pricing_hypotheses")
        if isinstance(pricing_patch, dict):
            pricing = brand.get("pricing_hypotheses")
            if not isinstance(pricing, dict):
                pricing = dict(build_default_brand_system()["pricing_hypotheses"])
            else:
                pricing = {
                    key: (dict(value) if isinstance(value, dict) else value)
                    for key, value in pricing.items()
                }
            for tier_id, tier_patch in pricing_patch.items():
                if not isinstance(tier_patch, dict):
                    rejected.append("pricing_hypotheses.{0}".format(tier_id))
                    continue
                tier = pricing.get(tier_id)
                tier = dict(tier) if isinstance(tier, dict) else {}
                for key, value in tier_patch.items():
                    # Checkout stays disabled: these are price tests, not products.
                    if key in ("hypothesis", "paid_checkout_enabled"):
                        rejected.append("pricing_hypotheses.{0}.{1}".format(tier_id, key))
                        continue
                    if key in ("price", "test_price_usd", "min_price_usd", "max_price_usd", "amount"):
                        if isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0:
                            rejected.append(f"pricing_hypotheses.{tier_id}.{key}")
                            continue
                        if isinstance(value, float) and not math.isfinite(value):
                            raise ValueError("Price must be finite")
                    if key in ("label", "range_label", "notes", "currency") and not isinstance(value, str):
                        rejected.append(f"pricing_hypotheses.{tier_id}.{key}")
                        continue
                    tier[key] = value
                tier["hypothesis"] = True
                tier["paid_checkout_enabled"] = False
                pricing[tier_id] = tier
                applied.append("pricing_hypotheses.{0}".format(tier_id))
            brand["pricing_hypotheses"] = pricing
        elif "pricing_hypotheses" in patch:
            rejected.append("pricing_hypotheses")

        # -- preview concept (UI only) ----------------------------------------
        if "active_preview_concept" in patch:
            concept = patch["active_preview_concept"]
            if isinstance(concept, str) and concept in CONCEPT_IDS:
                brand["active_preview_concept"] = concept
                applied.append("active_preview_concept")
            else:
                rejected.append("active_preview_concept")

        # -- editorial notes ---------------------------------------------------
        for key in ("editorial_notes", "notes"):
            if key in patch:
                value = patch[key]
                if isinstance(value, str):
                    brand["editorial_notes"] = value
                    applied.append("editorial_notes")
                else:
                    rejected.append(key)
                break

        for key in (
            "approved_concept_id", "public_deploy_approved", "paid_sales_approved",
            "owner_explicit_concept_approval", "owner_explicit_deploy_approval",
            "owner_explicit_sales_approval",
        ):
            if key in patch:
                rejected.append(key)
        gates = _normalize_gates(gates)

        brand["gates"] = gates
        brand["updated_at"] = _now_iso()
        _commit_store_transaction(root, [(brand_path, brand)], [])

        return {
            "ok": True,
            "applied": applied,
            "rejected": rejected,
            "path": str(brand_path),
            "gates": gates,
            "settings": dict(gates),
            "active_preview_concept": brand.get("active_preview_concept"),
            "pricing_hypotheses": brand.get("pricing_hypotheses", {}),
            "design_approval_gate_enforced": True,
            "updated_at": brand["updated_at"],
        }


def record_newsletter_signup(
    root_dir: Path,
    email: str,
    tier_interest: str = "",
    source: str = "site",
) -> dict:
    """Validate and append a newsletter subscriber (case-insensitive dedupe)."""
    with _root_lock(root_dir):
        root = Path(root_dir).resolve()
        _recover_journal(root)
        pub = _publishing_dir(root)
        signup_path = _resolve_contained(root, pub / "site" / "newsletter_signups.json")

        candidate = (email or "").strip() if isinstance(email, str) else ""
        if not candidate or not _EMAIL_RE.match(candidate):
            return {"ok": False, "error": "invalid_email", "email": email}

        payload = _read_json(signup_path, None, strict=True)
        if not isinstance(payload, dict) or not isinstance(payload.get("subscribers"), list):
            payload = {"subscribers": []}

        subscribers = payload["subscribers"]
        normalized = candidate.lower()
        timestamp = _now_iso()

        for position, existing in enumerate(subscribers):
            if not isinstance(existing, dict):
                continue
            existing_email = existing.get("email")
            if isinstance(existing_email, str) and existing_email.strip().lower() == normalized:
                updated = dict(existing)
                if tier_interest:
                    updated["tier_interest"] = tier_interest
                if source:
                    updated["source"] = source
                updated["last_seen_at"] = timestamp
                subscribers[position] = updated
                payload["subscribers"] = subscribers
                payload["updated_at"] = timestamp
                _commit_store_transaction(root, [(signup_path, payload)], [])
                return {
                    "ok": True,
                    "duplicate": True,
                    "email": existing_email,
                    "subscriber": updated,
                    "subscriber_count": len(subscribers),
                    "path": str(signup_path),
                }

        subscriber = {
            "email": candidate,
            "email_normalized": normalized,
            "tier_interest": tier_interest or "",
            "source": source or "site",
            "signed_up_at": timestamp,
            "last_seen_at": timestamp,
            "marketing_consent": True,
            "paid_sales_approved": False,
        }
        subscribers.append(subscriber)
        payload["subscribers"] = subscribers
        payload["updated_at"] = timestamp
        _commit_store_transaction(root, [(signup_path, payload)], [])

        return {
            "ok": True,
            "duplicate": False,
            "email": candidate,
            "subscriber": subscriber,
            "subscriber_count": len(subscribers),
            "path": str(signup_path),
        }
