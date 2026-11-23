"""Brand constants for the FYMC publishing pipeline."""

from __future__ import annotations

import re
from urllib.parse import parse_qs, urlparse

from .volume_registry import (
    ALL_VOLUME_SPECS,
    get_published_volume_ids,
    resolve_registered_volume_slug,
)

PARENT_BRAND = "THE FUCK YOU MONEY CLUB"
BOOK_SERIES = "THE BIG MONEY PLAYBOOKS"
BRAND_TAGLINE = "Big Money. Small Teams. No Bullshit."
RATING_SYSTEM_NAME = "Money-to-Manpower Score"
FLAGSHIP_VOLUME_ID = "vol-001-heir-hunting"
VOLUME_002_ID = "vol-002-surplus-funds-recovery"
VOLUME_003_ID = "vol-003-digital-product-empire"
VOLUME_004_ID = "vol-004-ai-powered-micro-saas"
VOLUME_005_ID = "vol-005-high-ticket-affiliate-marketing"
VOLUME_006_ID = ALL_VOLUME_SPECS[6]["volume_id"]
VOLUME_007_ID = ALL_VOLUME_SPECS[7]["volume_id"]
VOLUME_008_ID = ALL_VOLUME_SPECS[8]["volume_id"]
VOLUME_009_ID = ALL_VOLUME_SPECS[9]["volume_id"]
VOLUME_010_ID = ALL_VOLUME_SPECS[10]["volume_id"]
VOLUME_011_ID = ALL_VOLUME_SPECS[11]["volume_id"]
VOLUME_012_ID = ALL_VOLUME_SPECS[12]["volume_id"]
VOLUME_013_ID = ALL_VOLUME_SPECS[13]["volume_id"]
VOLUME_014_ID = ALL_VOLUME_SPECS[14]["volume_id"]
VOLUME_015_ID = ALL_VOLUME_SPECS[15]["volume_id"]
VOLUME_016_ID = ALL_VOLUME_SPECS[16]["volume_id"]
VOLUME_017_ID = ALL_VOLUME_SPECS[17]["volume_id"]
VOLUME_018_ID = ALL_VOLUME_SPECS[18]["volume_id"]
VOLUME_019_ID = ALL_VOLUME_SPECS[19]["volume_id"]
VOLUME_020_ID = ALL_VOLUME_SPECS[20]["volume_id"]
VOLUME_021_ID = ALL_VOLUME_SPECS[21]["volume_id"]
VOLUME_022_ID = ALL_VOLUME_SPECS[22]["volume_id"]
VOLUME_023_ID = ALL_VOLUME_SPECS[23]["volume_id"]
VOLUME_024_ID = ALL_VOLUME_SPECS[24]["volume_id"]
VOLUME_025_ID = ALL_VOLUME_SPECS[25]["volume_id"]
VOLUME_026_ID = ALL_VOLUME_SPECS[26]["volume_id"]
VOLUME_027_ID = ALL_VOLUME_SPECS[27]["volume_id"]
VOLUME_028_ID = ALL_VOLUME_SPECS[28]["volume_id"]
VOLUME_029_ID = ALL_VOLUME_SPECS[29]["volume_id"]
VOLUME_030_ID = ALL_VOLUME_SPECS.get(30, {"volume_id": "vol-030-lending-and-flash-funding-arbitrage"})["volume_id"]
VOLUME_031_ID = ALL_VOLUME_SPECS.get(31, {"volume_id": "vol-031"})["volume_id"]
VOLUME_032_ID = ALL_VOLUME_SPECS.get(32, {"volume_id": "vol-032"})["volume_id"]
VOLUME_033_ID = ALL_VOLUME_SPECS.get(33, {"volume_id": "vol-033"})["volume_id"]
VOLUME_034_ID = ALL_VOLUME_SPECS.get(34, {"volume_id": "vol-034"})["volume_id"]
VOLUME_035_ID = ALL_VOLUME_SPECS.get(35, {"volume_id": "vol-035"})["volume_id"]
VOLUME_036_ID = ALL_VOLUME_SPECS.get(36, {"volume_id": "vol-036"})["volume_id"]
VOLUME_037_ID = ALL_VOLUME_SPECS.get(37, {"volume_id": "vol-037-saas-discount-and-gpo-arbitrage"})["volume_id"]
VOLUME_038_ID = ALL_VOLUME_SPECS.get(38, {"volume_id": "vol-038-contingent-bill-audit-and-tax-credit-recovery"})["volume_id"]
VOLUME_039_ID = ALL_VOLUME_SPECS.get(39, {"volume_id": "vol-039-inbound-pay-per-call-and-ping-post-arbitrage"})["volume_id"]
VOLUME_040_ID = ALL_VOLUME_SPECS.get(40, {"volume_id": "vol-040-self-funded-erisa-pbm-and-workers-comp-arbitrage"})["volume_id"]
VOLUME_041_ID = ALL_VOLUME_SPECS.get(41, {"volume_id": "vol-041-buying-group-card-rebate-and-ticket-allocation-arbitrage"})["volume_id"]
VOLUME_042_ID = ALL_VOLUME_SPECS.get(42, {"volume_id": "vol-042-cell-tower-billboard-and-ios-lease-arbitrage"})["volume_id"]
PUBLISHED_VOLUME_IDS = get_published_volume_ids()
OWNER_APPROVED_CONCEPT_ID = "concept_b"
MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK = 150
TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK = "150-200+"
MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER = 12


def resolve_volume_slug(volume_id: object = None) -> str:
    """Resolve supported volume aliases without coercing other value types."""
    return resolve_registered_volume_slug(volume_id, allow_unpublished=False)


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
