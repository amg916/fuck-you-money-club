"""Backward-compatible re-export shim for Volume 002 Chapters 11-12."""
from __future__ import annotations

from .vol002_q11 import CHAPTER_11
from .vol002_q12 import CHAPTER_12

from .vol002_workbook import build_volume_002_workbook

CHAPTERS_11_TO_12 = [CHAPTER_11, CHAPTER_12]
