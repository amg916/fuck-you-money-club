from __future__ import annotations

from .vol001_q07_08 import CHAPTERS_7_TO_8
from .vol001_q09_10 import CHAPTERS_9_TO_10
from .vol001_q11_12 import CHAPTERS_11_TO_12, build_volume_001_workbook


CHAPTERS_7_TO_12 = CHAPTERS_7_TO_8 + CHAPTERS_9_TO_10 + CHAPTERS_11_TO_12

__all__ = ["CHAPTERS_7_TO_12", "build_volume_001_workbook"]
