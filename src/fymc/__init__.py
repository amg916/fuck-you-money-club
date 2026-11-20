"""Brand constants for the FYMC publishing pipeline."""

from __future__ import annotations

import re
from urllib.parse import parse_qs, urlparse

PARENT_BRAND = "THE FUCK YOU MONEY CLUB"
BOOK_SERIES = "THE BIG MONEY PLAYBOOKS"
BRAND_TAGLINE = "Big Money. Small Teams. No Bullshit."
RATING_SYSTEM_NAME = "Money-to-Manpower Score"
FLAGSHIP_VOLUME_ID = "vol-001-heir-hunting"
VOLUME_002_ID = "vol-002-surplus-funds-recovery"
VOLUME_003_ID = "vol-003-digital-product-empire"
VOLUME_004_ID = "vol-004-ai-powered-micro-saas"
PUBLISHED_VOLUME_IDS = (FLAGSHIP_VOLUME_ID, VOLUME_002_ID, VOLUME_003_ID, VOLUME_004_ID)
OWNER_APPROVED_CONCEPT_ID = "concept_b"
MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK = 150
TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK = "150-200+"
MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER = 12


def resolve_volume_slug(volume_id: object = None) -> str:
    """Resolve supported volume aliases without coercing other value types."""
    if volume_id is None:
        return FLAGSHIP_VOLUME_ID
    if isinstance(volume_id, bool):
        raise ValueError("Invalid volume_id")
    if isinstance(volume_id, int):
        if volume_id == 1:
            return FLAGSHIP_VOLUME_ID
        if volume_id == 2:
            return VOLUME_002_ID
        if volume_id == 3:
            return VOLUME_003_ID
        if volume_id == 4:
            return VOLUME_004_ID
    elif isinstance(volume_id, str):
        if volume_id in {"", "1", "001", "vol-001", FLAGSHIP_VOLUME_ID, "heir-hunting"}:
            return FLAGSHIP_VOLUME_ID
        if volume_id in {"2", "002", "vol-002", VOLUME_002_ID, "surplus-funds-recovery"}:
            return VOLUME_002_ID
        if volume_id in {"3", "003", "vol-003", VOLUME_003_ID, "digital-product-empire"}:
            return VOLUME_003_ID
        if volume_id in {"4", "004", "vol-004", VOLUME_004_ID, "ai-powered-micro-saas"}:
            return VOLUME_004_ID
    raise ValueError("Invalid volume_id")


def parse_expert_youtube_deep_link(url: object) -> tuple[str, int] | None:
    """Return ``(video_id, timestamp_seconds)`` iff ``url`` is a valid HTTP(S) YouTube deep link with ``t`` in the URL."""
    if not isinstance(url, str):
        return None
    raw = url.strip()
    if not raw or any(ch.isspace() for ch in raw):
        return None
    try:
        parsed = urlparse(raw)
        port = parsed.port
    except ValueError:
        return None
    if (
        parsed.scheme.lower() not in {"http", "https"}
        or parsed.username
        or parsed.password
        or port is not None
        or ":" in (parsed.netloc or "")
    ):
        return None
    host = (parsed.hostname or "").lower()
    qs = parse_qs(parsed.query, keep_blank_values=True)
    vid = ""
    if host in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
        if parsed.path == "/watch":
            v_vals = qs.get("v", [])
            if len(v_vals) != 1:
                return None
            vid = v_vals[0]
        else:
            m = re.fullmatch(r"/(?:shorts|live|embed)/([A-Za-z0-9_-]{11})", parsed.path)
            if not m:
                return None
            vid = m.group(1)
    elif host == "youtu.be":
        m = re.fullmatch(r"/([A-Za-z0-9_-]{11})", parsed.path)
        if not m or "v" in qs:
            return None
        vid = m.group(1)
    else:
        return None
    if not re.fullmatch(r"[A-Za-z0-9_-]{11}", vid):
        return None
    t_vals = qs.get("t", [])
    if len(t_vals) != 1:
        return None
    raw_t = str(t_vals[0]).strip()
    if not re.fullmatch(r"\d+[sS]?", raw_t):
        return None
    t_sec = int(raw_t.rstrip("sS"))
    if t_sec < 0:
        return None
    return (vid, t_sec)


def count_manuscript_youtube_links(chapters: object) -> int:
    """Count unique valid ``(video_id, timestamp_seconds)`` YouTube deep links across chapters."""
    if not isinstance(chapters, list):
        return 0
    seen: set[tuple[str, int]] = set()
    for ch in chapters:
        if not isinstance(ch, dict):
            continue
        cites = ch.get("source_citations")
        if not isinstance(cites, list):
            continue
        for cite in cites:
            if not isinstance(cite, dict):
                continue
            parsed = parse_expert_youtube_deep_link(cite.get("url"))
            if parsed is None:
                continue
            vid, t_sec = parsed
            if cite.get("video_id") not in (None, "", vid):
                continue
            ts = cite.get("timestamp_seconds", cite.get("timestamp"))
            if ts is not None and (isinstance(ts, bool) or not isinstance(ts, int) or ts != t_sec):
                continue
            seen.add(parsed)
    return len(seen)


WORKFLOW_STAGES = [
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
    "Publication Approval",
]
