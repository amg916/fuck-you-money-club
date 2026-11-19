#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[verify-fymc] Checking embedded JS syntax in studio.html and site.html..."
python3 -X utf8 - <<'PY'
import re, subprocess, tempfile
from pathlib import Path

for rel in ("src/static/studio.html", "src/static/site.html"):
    html = Path(rel).read_text(encoding="utf-8")
    scripts = re.findall(r"<script\b[^>]*>(.*?)</script>", html, flags=re.S | re.I)
    assert scripts, f"No <script> block in {rel}"
    for idx, js in enumerate(scripts, 1):
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=True) as tmp:
            tmp.write(js)
            tmp.flush()
            subprocess.run(["node", "--check", tmp.name], check=True)
print("Embedded JS syntax OK.")
PY

echo "[verify-fymc] Verifying on-disk commit manifest..."
python3 -X utf8 -c '
from pathlib import Path
from src.fymc.brand_and_catalog import verify_commit_manifest
res = verify_commit_manifest(Path(".").resolve(), strict=True)
assert res["passed"] is True, res
print("Commit manifest verified:", res["checked_files"], "files")
'

echo "[verify-fymc] Running full unittest suite..."
python3 -m unittest discover -s tests -v
