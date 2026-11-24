"""Volume 030 manuscript, 8 vector diagrams, and verbatim practitioner citation loader for Lending & Flash-Funding Arbitrage."""
from __future__ import annotations

from copy import deepcopy

from .vol030_q01 import CHAPTER_1
from .vol030_q02 import CHAPTER_2
from .vol030_q03 import CHAPTER_3
from .vol030_q04 import CHAPTER_4
from .vol030_q05 import CHAPTER_5
from .vol030_q06 import CHAPTER_6
from .vol030_q07 import CHAPTER_7
from .vol030_q08 import CHAPTER_8
from .vol030_q09 import CHAPTER_9
from .vol030_q10 import CHAPTER_10
from .vol030_q11 import CHAPTER_11
from .vol030_q12 import CHAPTER_12
from .vol030_workbook import build_volume_030_workbook
from .vol030_diagrams import (
    VOLUME_030_POSITIONING_ALTERNATIVES,
    VOLUME_030_SUBTITLE,
    build_volume_030_diagrams_data,
)
from .volume_030_citations import BASELINE_EXPERT_CITATIONS_BY_CHAPTER, CHAPTER_KEYWORDS
from .volume_001_manuscript import compute_manuscript_word_count

ALL_VOLUME_030_CHAPTERS = [
    CHAPTER_1,
    CHAPTER_2,
    CHAPTER_3,
    CHAPTER_4,
    CHAPTER_5,
    CHAPTER_6,
    CHAPTER_7,
    CHAPTER_8,
    CHAPTER_9,
    CHAPTER_10,
    CHAPTER_11,
    CHAPTER_12,
]


def build_volume_030_manuscript(abridged_videos: list[dict] | None = None, **kwargs) -> dict:
    """Build Volume 030 strictly from Claude's verbatim-transcript-grounded chapters and exact timestamped citations."""
    from . import (
        MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
        count_manuscript_youtube_links,
    )
    from .scorecard_engine import get_candidate_track_metadata

    chapters = deepcopy(ALL_VOLUME_030_CHAPTERS)
    diagram_ids = {item["diagram_id"][:7]: item["diagram_id"] for item in build_volume_030_diagrams_data()}
    for chapter in chapters:
        number = int(chapter["chapter_number"])
        chapter.setdefault("id", f"Q{number}")
        chapter.setdefault("chapter_id", f"Q{number}")
        reference = str(chapter.get("diagram_id") or "diag-01")
        prefix = reference[:7]
        if prefix not in diagram_ids:
            prefix = "diag-01"
        chapter["diagram_id"] = diagram_ids[prefix]
        if not chapter.get("source_citations"):
            chapter["source_citations"] = deepcopy(BASELINE_EXPERT_CITATIONS_BY_CHAPTER.get(number, []))

    total_words = compute_manuscript_word_count(chapters)
    total_yt_links = count_manuscript_youtube_links(chapters)
    return {
        "volume_id": 'vol-030-lending-and-flash-funding-arbitrage',
        "volume_number": "030",
        "series_title": "THE BIG MONEY PLAYBOOKS",
        "parent_brand": "THE FUCK YOU MONEY CLUB",
        "tagline": "Big Money. Small Teams. No Bullshit.",
        "title": 'LENDING & FLASH-FUNDING ARBITRAGE',
        "subtitle": VOLUME_030_SUBTITLE,
        "content_architecture_layers": [
            {"layer": 1, "title": "Practitioner orientation", "description": "Question-led summaries and practitioner-reported metrics distilled strictly from 192 YouTube transcripts."},
            {"layer": 2, "title": "Verbatim testimony synthesis", "description": "Detailed sections report consensus, street mechanics, disagreements, and failure modes with inline timestamp attribution."},
            {"layer": 3, "title": "Visual testimony maps", "description": "Diagrams and matrices map workflows, funnels, economics, and timelines reported by the cited speakers."},
            {"layer": 4, "title": "Practitioner execution checklists", "description": "SOPs, insider pro-tips, operator gates, and the 6-worksheet workbook trace every example to a named video source."},
            {"layer": 5, "title": "Direct timestamped video links", "description": "Every chapter links directly to the exact [HH:MM:SS] moments in the underlying YouTube transcripts."},
        ],
        "operator_plays": deepcopy(get_candidate_track_metadata(30)["plays"]),
        "min_expert_youtube_links_per_book": MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        "target_expert_youtube_links_per_book": TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        "min_expert_youtube_links_per_chapter": MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
        "expert_youtube_link_count": total_yt_links,
        "positioning_alternatives": deepcopy(VOLUME_030_POSITIONING_ALTERNATIVES),
        "chapters": chapters,
        "chapter_count": len(chapters),
        "total_word_count": total_words,
        "epistemic_note": "Compiled exclusively from attributed English YouTube practitioner transcripts in vol030_lending_and_flash_funding_arbitrage_corpus.json.",
    }
