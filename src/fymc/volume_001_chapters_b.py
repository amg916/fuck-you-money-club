"""Backward-compatible re-export shim for Volume 001 Chapters 7-12 and workbook."""
from __future__ import annotations

from .vol001_q07 import CHAPTER_7
from .vol001_q08 import CHAPTER_8
from .vol001_q09 import CHAPTER_9
from .vol001_q10 import CHAPTER_10
from .vol001_q11 import CHAPTER_11
from .vol001_q12 import CHAPTER_12
from .vol001_workbook import build_volume_001_workbook

CHAPTERS_7_TO_12 = [CHAPTER_7, CHAPTER_8, CHAPTER_9, CHAPTER_10, CHAPTER_11, CHAPTER_12]
