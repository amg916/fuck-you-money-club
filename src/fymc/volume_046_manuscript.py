"""Volume 046 manuscript, 8 vector diagrams, and citation merger for Mass-Tort Case Acquisition, HITECH Record Triage & Law-Firm MSOs."""
from __future__ import annotations

from copy import deepcopy

from .vol046_q01 import CHAPTER_1
from .vol046_q02 import CHAPTER_2
from .vol046_q03 import CHAPTER_3
from .vol046_q04 import CHAPTER_4
from .vol046_q05 import CHAPTER_5
from .vol046_q06 import CHAPTER_6
from .vol046_q07 import CHAPTER_7
from .vol046_q08 import CHAPTER_8
from .vol046_q09 import CHAPTER_9
from .vol046_q10 import CHAPTER_10
from .vol046_q11 import CHAPTER_11
from .vol046_q12 import CHAPTER_12
from .vol046_workbook import build_volume_046_workbook
from .vol046_diagrams import (
    VOLUME_046_POSITIONING_ALTERNATIVES,
    VOLUME_046_SUBTITLE,
    build_volume_046_diagrams_data,
)
from .volume_046_citations import BASELINE_EXPERT_CITATIONS_BY_CHAPTER, CHAPTER_KEYWORDS
from .volume_001_manuscript import compute_manuscript_word_count

ALL_VOLUME_046_CHAPTERS = [
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


def build_volume_046_manuscript(abridged_videos: list[dict] | None = None) -> dict:
    """Build isolated Volume 046 chapter records with attributed, sentence-clean commentary."""
    import math
    import re
    from urllib.parse import parse_qs, urlparse

    from . import (
        MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
        count_manuscript_youtube_links,
    )
    from .scorecard_engine import get_candidate_track_metadata

    chapters = deepcopy(ALL_VOLUME_046_CHAPTERS)
    diagram_ids = {item["diagram_id"][:7]: item["diagram_id"] for item in build_volume_046_diagrams_data()}
    for chapter in chapters:
        chapter.setdefault("id", f"Q{chapter['chapter_number']}")
        chapter.setdefault("chapter_id", f"Q{chapter['chapter_number']}")
        reference = str(chapter.get("diagram_id") or "diag-01")
        prefix = reference[:7]
        if prefix not in diagram_ids:
            prefix = "diag-01"
        chapter["diagram_id"] = diagram_ids[prefix]
        chapter["source_citations"] = []

    def seconds_of(value):
        if value is None or isinstance(value, bool):
            return None
        try:
            if isinstance(value, str) and ":" in value:
                parts = value.strip().strip("[]").split(":")
                if len(parts) not in (2, 3):
                    return None
                parts = [float(part) for part in parts]
                if any(not math.isfinite(part) or part < 0 for part in parts):
                    return None
                if any(part >= 60 for part in parts[1:]):
                    return None
                seconds = sum(part * 60 ** index for index, part in enumerate(reversed(parts)))
            else:
                seconds = float(value)
            return int(seconds) if math.isfinite(seconds) and seconds >= 0 else None
        except (ValueError, TypeError, OverflowError):
            return None

    _domain_allow_re = re.compile('\\b(mass\\s+tort|multidistrict\\s+litigation|\\bmdl\\b|plaintiff\\s+intake|case\\s+acquisition|signed\\s+retainer|law\\s+firm\\s+mso|management\\s+services\\s+organization|alternative\\s+business\\s+structure|arizona\\s+abs|aba\\s+rule\\s+5\\.4|hitech\\s+act|medical\\s+record\\s+retrieval|litigation\\s+finance|personal\\s+injury\\s+marketing|legal\\s+lead|legal\\s+intake|litify|filevine|bellwether)\\b', re.IGNORECASE)
    _off_domain_deny_re = re.compile('\\b(minecraft|fortnite|roblox|valorant|gta\\s+rp|sims\\s+4|cooking|knitting|makeup|mukbang|asmr)\\b', re.IGNORECASE)
    _dangling_tail = {
        "a", "about", "after", "although", "am", "an", "and", "any", "are", "as", "at",
        "be", "because", "been", "before", "being", "between", "both", "but", "by", "can",
        "could", "did", "do", "does", "doing", "during", "each", "either", "for", "from",
        "get", "getting", "go", "going", "had", "has", "have", "having", "he", "her", "his",
        "how", "i", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its",
        "just", "like", "make", "many", "may", "might", "more", "most", "much", "must", "my",
        "need", "no", "nor", "not", "of", "on", "onto", "or", "other", "our", "over", "put",
        "really", "same", "say", "saying", "see", "she", "should", "since", "so", "some",
        "still", "such", "than", "that", "that's", "the", "their", "them", "then", "there",
        "these", "they", "they're", "this", "those", "though", "through", "to", "too",
        "under", "unless", "until", "up", "upon", "very", "want", "was", "we", "we'll",
        "we're", "were", "what", "when", "where", "whether", "which", "while", "who", "whom",
        "whose", "why", "will", "with", "within", "without", "would", "you", "you'll",
        "you're", "your",
    }

    def polish_excerpt(raw_text: str) -> str:
        cleaned = re.sub(r"\s+", " ", str(raw_text or "")).replace("\u2122", "").replace("\u00ae", "").replace('!"', "!'").strip()
        if not cleaned:
            return ""
        if (
            "|" not in cleaned
            and not re.search(r"\b\d+:\d{2}(?::\d{2})?(?:\.\d+)?\s*S\d+\b", cleaned)
            and re.search(r'[.!?]["\'\)\]]*$', cleaned)
        ):
            return cleaned.replace('!"', "!'")
        cleaned = re.sub(r"\b\d+:\d{2}(?::\d{2})?(?:\.\d+)?\s*S\d+\b", "", cleaned).strip()
        if "|" in cleaned:
            parts = [p.strip() for p in cleaned.split("|") if p.strip()]
            cleaned = parts[0] if parts and len(parts[0]) >= 50 else ". ".join(parts)
        was_char_clipped = len(raw_text or "") in range(215, 226) or len(raw_text or "") >= 455
        if was_char_clipped and not re.search(r'[.!?]["\'\)\]]*$', cleaned):
            cleaned = re.sub(r"\s+\S+$", "", cleaned).strip()
        matches = list(re.finditer(r'[.!?]["\'\)\]]*(?=\s|$)', cleaned))
        if matches and matches[-1].end() >= 55:
            cleaned = cleaned[: matches[-1].end()].strip()
        if not re.search(r'[.!?]["\'\)\]]*$', cleaned):
            tokens_list = cleaned.split()
            while len(tokens_list) > 6:
                last_word = re.sub(r"^[^A-Za-z0-9']+|[^A-Za-z0-9']+$", "", tokens_list[-1]).lower()
                if not last_word or (not any(ch.isdigit() for ch in last_word) and (last_word in _dangling_tail or len(last_word) <= 1)):
                    tokens_list.pop()
                else:
                    break
            cleaned = " ".join(tokens_list).rstrip(",;:- ")
            if cleaned and cleaned[-1] not in ".!?":
                cleaned += "."
        if cleaned and cleaned[0].isalpha() and cleaned[0].islower():
            cleaned = cleaned[0].upper() + cleaned[1:]
        return cleaned

    valid_videos = [video for video in (abridged_videos or []) if isinstance(video, dict)]
    large_corpus = len(valid_videos) > 20
    for video in valid_videos:
        if large_corpus:
            meta_obj = video.get("metadata") or {}
            haystack = " ".join(
                str(x or "")
                for x in (
                    video.get("title"),
                    video.get("channel"),
                    video.get("channel_title"),
                    video.get("author"),
                    meta_obj.get("title"),
                    meta_obj.get("channel_title"),
                    meta_obj.get("author"),
                )
            ).lower()
            source_corpus = str(video.get("source_corpus") or meta_obj.get("source_corpus") or "").lower()
            if _off_domain_deny_re.search(haystack) or "fuck" in haystack:
                continue
            if source_corpus != 'vol046_mass_tort_intake_hitech_triage_and_law_firm_msos':
                continue
        video_id = str(video.get("video_id") or "")
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
            try:
                parsed = urlparse(str(video.get("url") or video.get("video_url") or ""))
                host = (parsed.hostname or "").lower()
                if host in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
                    video_id = parse_qs(parsed.query).get("v", [""])[0]
                    if not video_id and parsed.path.startswith(("/shorts/", "/embed/", "/live/")):
                        video_id = parsed.path.split("/")[2]
                elif host == "youtu.be":
                    video_id = parsed.path.strip("/").split("/")[0]
            except ValueError:
                continue
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
            continue
        tips = []
        for key in ("pro_tips", "tips", "key_points"):
            items = video.get(key)
            if isinstance(items, list):
                tips.extend(items)
        for tip in tips:
            if not isinstance(tip, dict):
                continue
            raw_tip_text = str(tip.get("text") or tip.get("tip") or tip.get("summary") or "").strip()
            if large_corpus and (_off_domain_deny_re.search(raw_tip_text) or "fuck" in raw_tip_text.lower()):
                continue
            text = polish_excerpt(raw_tip_text) if large_corpus else raw_tip_text
            seconds = None
            for key in ("timestamp", "start", "start_seconds", "timestamp_seconds"):
                seconds = seconds_of(tip.get(key))
                if seconds is not None:
                    break
            if not text or seconds is None:
                continue
            explicit = tip.get("chapter_number", tip.get("question_number"))
            if explicit is not None:
                explicit = str(explicit).upper().removeprefix("Q")
            tokens = set(re.findall(r"[a-z0-9]+", text.lower()))
            scores = []
            for chapter in chapters:
                number = chapter["chapter_number"]
                chapter_tokens = set(re.findall(r"[a-z0-9]+", str(chapter.get("title", "")).lower()))
                chapter_tokens -= {"the", "a", "an", "is", "to", "of", "and", "in", "for", "what", "how", "your", "with", "who", "why", "where"}
                scores.append((len(tokens & (set(CHAPTER_KEYWORDS.get(number, set())) | chapter_tokens)), number))
            best_score = max((score for score, number in scores), default=0)
            targets = (
                {number for score, number in scores if str(number) == explicit}
                if explicit is not None
                else {number for score, number in scores if score == best_score and score > 0}
            )
            label = f"{seconds // 3600:02d}:{seconds % 3600 // 60:02d}:{seconds % 60:02d}"
            url = f"https://www.youtube.com/watch?v={video_id}&t={seconds}s"
            channel_name = str(
                video.get("channel")
                or video.get("channel_title")
                or video.get("author")
                or (video.get("metadata") or {}).get("author")
                or "Independent Practitioner"
            ).replace("\u2122", "").replace("\u00ae", "").replace('!"', "!'").strip()
            citation = dict(
                source_type="video_pro_tip",
                video_id=video_id,
                title=str(video.get("title") or (video.get("metadata") or {}).get("title") or video_id).replace("\u2122", "").replace("\u00ae", "").replace('!"', "!'"),
                channel=channel_name,
                author=channel_name,
                text=text,
                tip=text,
                timestamp=seconds,
                timestamp_seconds=seconds,
                timestamp_label=f"[{label}]",
                url=url,
                markdown=f"[{label}]({url})",
                epistemic_status="attributed_practitioner_claim",
                relevance="Matched source commentary; not independent verification or legal authority.",
            )
            for chapter in chapters:
                if chapter["chapter_number"] in targets:
                    existing = chapter["source_citations"]
                    if not any(item["url"] == url and item["text"] == text for item in existing):
                        existing.append(deepcopy(citation))

    cap_per_chapter = 18 if large_corpus else None
    used_book_videos = {
        str(base_cit.get("video_id") or "")
        for ch_list in BASELINE_EXPERT_CITATIONS_BY_CHAPTER.values()
        for base_cit in ch_list
        if base_cit.get("video_id")
    }
    for chapter in chapters:
        number = chapter["chapter_number"]
        existing = chapter["source_citations"]
        baseline = BASELINE_EXPERT_CITATIONS_BY_CHAPTER.get(number, [])
        baseline_prepared = []
        for base_cit in baseline:
            cloned = deepcopy(base_cit)
            if cloned.get("author") and not cloned.get("channel"):
                cloned["channel"] = str(cloned["author"]).replace("\u2122", "").replace("\u00ae", "").replace('!"', "!'")
            if cloned.get("channel"):
                cloned["channel"] = str(cloned["channel"]).replace("\u2122", "").replace("\u00ae", "").replace('!"', "!'")
            if cloned.get("title"):
                cloned["title"] = str(cloned["title"]).replace("\u2122", "").replace("\u00ae", "").replace('!"', "!'")
            polished_base = polish_excerpt(str(cloned.get("text") or cloned.get("tip") or ""))
            if polished_base:
                cloned["text"] = polished_base.replace('!"', "!'")
                cloned["tip"] = polished_base.replace('!"', "!'")
            baseline_prepared.append(cloned)
        base_urls = {item.get("url") for item in baseline_prepared}
        non_base_raw = [item for item in existing if item.get("url") not in base_urls]
        needed = None if cap_per_chapter is None else max(0, cap_per_chapter - len(baseline_prepared))
        fresh_vid_items = []
        repeat_vid_items = []
        seen_candidate_vids: set[str] = set()
        for item in non_base_raw:
            ivid = str(item.get("video_id") or "")
            if ivid and ivid not in used_book_videos and ivid not in seen_candidate_vids:
                seen_candidate_vids.add(ivid)
                fresh_vid_items.append(item)
            else:
                repeat_vid_items.append(item)
        non_base = fresh_vid_items + repeat_vid_items
        chosen_extra = non_base if needed is None else non_base[:needed]
        for item in chosen_extra:
            ivid = str(item.get("video_id") or "")
            if ivid:
                used_book_videos.add(ivid)
        chapter["source_citations"] = baseline_prepared + chosen_extra

    total_words = compute_manuscript_word_count(chapters)
    total_yt_links = count_manuscript_youtube_links(chapters)
    return {
        "volume_id": 'vol-046-mass-tort-intake-hitech-triage-and-law-firm-msos',
        "volume_number": '046',
        "series_title": "THE BIG MONEY PLAYBOOKS",
        "parent_brand": "THE FUCK YOU MONEY CLUB",
        "tagline": "Big Money. Small Teams. No Bullshit.",
        "title": 'MASS-TORT CASE ACQUISITION, HITECH RECORD TRIAGE & LAW-FIRM MSOS',
        "subtitle": VOLUME_046_SUBTITLE,
        "content_architecture_layers": [
            {"layer": 1, "title": "Executive orientation", "description": "Question-led summaries and key metrics establish revenue boundaries, net margins, and working-capital float."},
            {"layer": 2, "title": "Operator-grade analysis", "description": "Detailed sections separate statutory rules, execution architectures, cohort unit models, and practitioner claims."},
            {"layer": 3, "title": "Visual decision support", "description": "Diagrams and matrices expose conversion funnels, margin waterfalls, payment rails, and risk guardrails."},
            {"layer": 4, "title": "Execution tools", "description": "SOPs, insider callouts, chapter checklists, and the 6-worksheet companion workbook turn research into execution."},
            {"layer": 5, "title": "Source evidence", "description": "Statutory/regulatory citations and attributed timestamped commentary distinguish primary rules from practitioner perspective."},
        ],
        "operator_plays": deepcopy(get_candidate_track_metadata(46)["plays"]),
        "min_expert_youtube_links_per_book": MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        "target_expert_youtube_links_per_book": TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        "min_expert_youtube_links_per_chapter": MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
        "expert_youtube_link_count": total_yt_links,
        "positioning_alternatives": deepcopy(VOLUME_046_POSITIONING_ALTERNATIVES),
        "chapters": chapters,
        "chapter_count": len(chapters),
        "total_word_count": total_words,
        "epistemic_note": "Educational and research material grounded in documented public authorities and attributed practitioner sources; verify jurisdiction-specific licensing, tax, and contracting rules independently.",
    }
