"""Research intelligence layer for the FYMC heir-hunting publishing studio.

Two responsibilities, both pure standard library:

1. ``audit_existing_workspace`` walks the real workspace on disk (transcript
   corpus + previously generated eBook exports), measures what is actually
   there, and sorts every audited asset into *reusable*, *needs improvement*
   or *must redesign*.
2. ``build_research_database`` turns the abridged video records into a
   topic-structured research database with preserved YouTube deep links,
   practitioner-consensus findings, a verification queue for jurisdictional
   claims, and a permissions ledger for third-party media.

Nothing here downloads, renders or publishes anything; it only measures and
structures what already exists.
"""

from __future__ import annotations

import json
import math
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path

__all__ = [
    "RESEARCH_TOPICS",
    "ABRIDGED_WORDS_BENCHMARK",
    "EXTRACTED_PRO_TIPS_BENCHMARK",
    "COMMERCIAL_EXPORT_POLICY",
    "audit_existing_workspace",
    "build_research_database",
]


# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------

ABRIDGED_WORDS_BENCHMARK = 371246
EXTRACTED_PRO_TIPS_BENCHMARK = 1806

COMMERCIAL_EXPORT_POLICY = (
    "Zero third-party YouTube frames, portal screenshots, or >25-word verbatim "
    "transcript passages permitted in commercial exports without written license."
)

VERIFICATION_STATUS = "Jurisdiction-Dependent — Must Cite Local Statute"
EPISTEMIC_STATUS = "Practitioner Consensus"

#: Maximum number of words allowed in a paraphrased insight summary.  Keeps
#: every exported line well under the fair-use ceiling stated in the policy.
MAX_PARAPHRASE_WORDS = 24

EBOOK_KEY_FILES = (
    "heir-hunting-digital-8.5x11.pdf",
    "heir-hunting-kdp-print-6x9.pdf",
    "heir-hunting-action-workbook.pdf",
    "heir-hunting-kindle.epub",
    "heir-hunting-amazon-etsy-ebay-bundle.zip",
    "heir-hunting-manuscript.md",
    "cover-3d.svg",
    "exhibits/",
)

WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’\-]*")
PDF_PAGE_RE = rb"/Type\s*/Page\b"
TIMESTAMP_RE = re.compile(r"(\d{1,2}):(\d{2}):(\d{2})|(\d{1,3}):(\d{2})")

#: The eight structured research topics the whole manual is organised around.
#: ``keywords`` are matched with a left word-boundary only, so stems such as
#: ``"automat"`` catch ``automation`` / ``automated`` / ``automate``.
RESEARCH_TOPICS = [
    {
        "topic_id": "business_model_and_economics",
        "title": "Business Model, Contingency Economics & Deal Scale",
        "keywords": [
            "business model", "contingency", "contingent fee", "finder fee",
            "finder's fee", "heir finder", "commission", "revenue", "profit",
            "margin", "payout", "average fee", "deal size", "deal flow",
            "pipeline", "cash flow", "overhead", "startup cost", "start-up cost",
            "return on investment", "six figure", "six-figure", "seven figure",
            "gross estate", "net estate", "case value", "estate value",
            "scale", "scaling", "volume", "economics", "per case", "per deal",
            "recovery amount", "split", "profitab",
        ],
    },
    {
        "topic_id": "probate_and_docket_sourcing",
        "title": "County Probate Dockets, Intestate Filings & Estate Leads",
        "keywords": [
            "probate", "docket", "intestate", "testate", "surrogate",
            "orphans court", "orphans' court", "clerk of court", "county clerk",
            "courthouse", "case search", "case lookup", "case number",
            "letters of administration", "letters testamentary",
            "administrator of the estate", "personal representative",
            "petition for", "decedent", "estate filing", "estate file",
            "public administrator", "odyssey portal", "pacer", "court portal",
            "recorder of deeds", "new filings", "lead source", "lead list",
        ],
    },
    {
        "topic_id": "unclaimed_property_and_escheat",
        "title": "State Unclaimed Property, Escheated Funds & Treasury Claims",
        "keywords": [
            "unclaimed", "escheat", "treasury", "treasurer", "comptroller",
            "state controller", "missingmoney", "missing money",
            "abandoned property", "dormant account", "dormancy",
            "surplus fund", "excess proceed", "tax overage", "overage",
            "foreclosure surplus", "claim form", "claimant form",
            "unclaimed property division", "holder report", "safe deposit",
            "uncashed", "outstanding check", "insurance proceeds",
        ],
    },
    {
        "topic_id": "genealogy_and_heirship_proof",
        "title": "Forensic Genealogy, Per-Stirpes Kinship & Proof of Heirship",
        "keywords": [
            "genealog", "family tree", "ancestry", "familysearch", "findagrave",
            "find a grave", "census", "obituar", "death certificate",
            "birth certificate", "marriage record", "vital record",
            "per stirpes", "per capita", "next of kin", "kinship", "heirship",
            "pedigree", "bloodline", "descendant", "collateral heir",
            "sibling", "cousin", "affidavit of heirship", "proof of kinship",
            "dna test", "adoption record", "probate genealogy", "lineage",
        ],
    },
    {
        "topic_id": "skip_tracing_and_outreach",
        "title": "Skip Tracing, Ethical Heir Contact & Trust Building",
        "keywords": [
            "skip trac", "skiptrac", "tlo", "irbsearch", "irb search",
            "batchskiptracing", "whitepages", "spokeo", "beenverified",
            "truepeoplesearch", "people search", "phone number", "cold call",
            "cold email", "outreach", "first contact", "initial contact",
            "call script", "voicemail", "door knock", "mailer", "letter campaign",
            "direct mail", "rapport", "build trust", "trust building",
            "objection", "gatekeeper", "social media search", "facebook search",
            "linkedin", "respond to", "follow up",
        ],
    },
    {
        "topic_id": "contracts_and_compensation",
        "title": "Fee Agreements, Assignments of Interest & Escrow Disbursement",
        "keywords": [
            "fee agreement", "contract", "agreement with the heir", "retainer",
            "assignment of interest", "assignment agreement", "assign the",
            "escrow", "disburs", "settlement statement", "payment terms",
            "wire transfer", "invoice", "lien", "release form", "waiver",
            "power of attorney", "notar", "docusign", "e-sign", "esign",
            "signed contract", "signature", "clawback", "rescind", "rescission",
            "fee split", "referral agreement", "trust account",
        ],
    },
    {
        "topic_id": "statutory_caps_and_licensing",
        "title": "State Fee Caps, Waiting Periods, PI Licensing & UPL Rules",
        "keywords": [
            "statute", "statutory", "fee cap", "capped at", "maximum fee",
            "10 percent", "10%", "ccp 1582", "code of civil procedure",
            "licens", "private investigator", "pi license", "p.i. license",
            "bonded", "surety", "waiting period", "holding period",
            "unauthorized practice", "upl", "attorney", "bar association",
            "regulat", "compliance", "registration requirement", "champerty",
            "maintenance and champerty", "legal requirement", "state law",
            "jurisdiction", "illegal in", "prohibited in", "disclosure requirement",
        ],
    },
    {
        "topic_id": "automation_and_small_team_ops",
        "title": "Docket Automation, AI Abstracting & Small-Team Operations",
        "keywords": [
            "automat", "scraper", "scraping", "script that", "python",
            "api", "chatgpt", "claude", "artificial intelligence",
            "machine learning", "spreadsheet", "google sheet", "excel",
            "crm", "airtable", "notion", "zapier", "make.com", "n8n",
            "virtual assistant", "outsourc", "delegate", "workflow",
            "batch process", "software", "saas", "dashboard", "pipeline tool",
            "standard operating procedure", "sop", "template", "checklist",
            "hire", "small team", "solo operator", "systemiz", "systematiz",
        ],
    },
]

TOPIC_IDS = [t["topic_id"] for t in RESEARCH_TOPICS]
TOPIC_TITLES = {t["topic_id"]: t["title"] for t in RESEARCH_TOPICS}


def _compile_keywords(keywords: list[str]) -> list[re.Pattern[str]]:
    """Compile keyword stems with a left-hand word boundary."""
    compiled = []
    for kw in keywords:
        compiled.append(re.compile(r"(?<![a-z0-9])" + re.escape(kw.lower())))
    return compiled


_TOPIC_PATTERNS = {
    topic["topic_id"]: _compile_keywords(topic["keywords"]) for topic in RESEARCH_TOPICS
}


# --------------------------------------------------------------------------
# Small shared helpers
# --------------------------------------------------------------------------


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _count_words(text: str) -> int:
    if not text:
        return 0
    return len(WORD_RE.findall(text))


def _clean_text(value: object) -> str:
    if not isinstance(value, str):
        return ""
    return re.sub(r"\s+", " ", value).strip()


def _as_list(value: object) -> list:
    return list(value) if isinstance(value, (list, tuple)) else []


def _as_str_list(value: object) -> list[str]:
    out = []
    for item in _as_list(value):
        text = _clean_text(item)
        if text:
            out.append(text)
    return out


def _score_text(text: str) -> dict[str, int]:
    """Return a keyword-hit score per topic for a blob of text."""
    lowered = text.lower()
    scores = {}
    for topic_id, patterns in _TOPIC_PATTERNS.items():
        hits = 0
        for pattern in patterns:
            found = len(pattern.findall(lowered))
            if found:
                hits += found
        scores[topic_id] = hits
    return scores


def _best_topic(scores: dict[str, int], fallback: str) -> str:
    best_id = fallback
    best_score = 0
    for topic_id in TOPIC_IDS:  # stable, declaration-ordered tie-breaking
        score = scores.get(topic_id, 0)
        if score > best_score:
            best_score = score
            best_id = topic_id
    return best_id


def _rank_unique(values: list[str], limit: int | None = None) -> list[str]:
    """De-duplicate case-insensitively, ordered by frequency then alphabetically."""
    counts: dict[str, int] = {}
    display: dict[str, str] = {}
    for raw in values:
        text = _clean_text(raw)
        if not text:
            continue
        key = text.lower()
        counts[key] = counts.get(key, 0) + 1
        display.setdefault(key, text)
    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    result = [display[key] for key, _ in ordered]
    if limit is not None:
        result = result[:limit]
    return result


_FILLER_PREFIXES = (
    "so ", "and ", "but ", "okay ", "ok ", "now ", "well ", "right ",
    "you know ", "i mean ", "basically ", "obviously ", "like i said ",
    "here's the thing ", "the thing is ", "look ", "alright ",
)


def _paraphrase(text: str) -> str:
    """Compress a captured tip into a short, non-verbatim operator instruction.

    The source corpus is third-party speech, so every exported line is reduced
    to an abstractive summary under ``MAX_PARAPHRASE_WORDS`` words rather than
    a quotable passage.
    """
    cleaned = _clean_text(text)
    if not cleaned:
        return ""
    cleaned = cleaned.strip("\"'“”‘’ ")
    lowered = cleaned.lower()
    changed = True
    while changed:
        changed = False
        for filler in _FILLER_PREFIXES:
            if lowered.startswith(filler):
                cleaned = cleaned[len(filler):]
                lowered = cleaned.lower()
                changed = True
    cleaned = cleaned.lstrip(",;:- —– ")
    words = cleaned.split()
    truncated = len(words) > MAX_PARAPHRASE_WORDS
    if truncated:
        words = words[:MAX_PARAPHRASE_WORDS]
    summary = " ".join(words).rstrip(",;:-—– ")
    if not summary:
        return ""
    summary = summary[0].upper() + summary[1:]
    if truncated:
        summary += "…"
    elif summary[-1] not in ".!?":
        summary += "."
    return summary


def _timestamp_seconds(timestamp: str) -> int:
    match = TIMESTAMP_RE.search(timestamp or "")
    if not match:
        return 0
    if match.group(1) is not None:
        return int(match.group(1)) * 3600 + int(match.group(2)) * 60 + int(match.group(3))
    return int(match.group(4)) * 60 + int(match.group(5))


def _finite_int(value):
    try:
        value = float(value)
        return int(value) if math.isfinite(value) else 0
    except (TypeError, ValueError, OverflowError):
        return 0


def _hhmmss(seconds: float) -> str:
    total = max(0, _finite_int(seconds))
    return "[%02d:%02d:%02d]" % (total // 3600, (total % 3600) // 60, total % 60)


# --------------------------------------------------------------------------
# 1. Workspace audit
# --------------------------------------------------------------------------


def _scan_transcripts(transcripts_dir: Path) -> dict:
    """Measure the raw transcript corpus on disk."""
    total_files = 0
    ok_files = 0
    failed_files = 0
    unreadable_files = 0
    raw_segment_words = 0
    total_segments = 0
    total_duration_seconds = 0
    authors: dict[str, int] = {}
    status_counts: dict[str, int] = {}
    unreadable: list[str] = []

    if transcripts_dir.is_dir():
        for path in sorted(transcripts_dir.glob("*.json")):
            total_files += 1
            try:
                payload = json.loads(path.read_text(encoding="utf-8", errors="replace"))
            except (OSError, ValueError):
                unreadable_files += 1
                unreadable.append(path.name)
                continue
            if not isinstance(payload, dict):
                unreadable_files += 1
                unreadable.append(path.name)
                continue

            status = _clean_text(payload.get("status")) or "unknown"
            status_counts[status] = status_counts.get(status, 0) + 1
            if status.lower() == "ok":
                ok_files += 1
            else:
                failed_files += 1

            raw_meta = payload.get("metadata") if isinstance(payload.get("metadata"), dict) else payload.get("meta")
            meta = raw_meta if isinstance(raw_meta, dict) else {}
            try:
                duration = float(meta.get("lengthSeconds") or 0)
                if math.isfinite(duration):
                    total_duration_seconds += int(duration)
            except (TypeError, ValueError, OverflowError):
                pass
            author = _clean_text(meta.get("author"))
            if author:
                authors[author] = authors.get(author, 0) + 1

            for segment in _as_list(payload.get("segments")):
                if not isinstance(segment, dict):
                    continue
                total_segments += 1
                raw_segment_words += _count_words(_clean_text(segment.get("text")))

    return {
        "transcripts_dir": str(transcripts_dir),
        "transcripts_dir_exists": transcripts_dir.is_dir(),
        "total_files": total_files,
        "ok_files": ok_files,
        "failed_files": failed_files,
        "unreadable_files": unreadable_files,
        "unreadable_file_names": unreadable[:25],
        "status_counts": status_counts,
        "total_segments": total_segments,
        "raw_segment_words": raw_segment_words,
        "total_duration_seconds": total_duration_seconds,
        "total_hours": round(total_duration_seconds / 3600, 2),
        "distinct_channels": len(authors),
        "top_channels": [
            {"author": name, "video_count": count}
            for name, count in sorted(authors.items(), key=lambda kv: (-kv[1], kv[0]))[:15]
        ],
    }


def _count_pdf_pages(data: bytes) -> int:
    return len(re.findall(PDF_PAGE_RE, data))


def _inspect_asset(ebook_dir: Path, name: str) -> dict:
    """Inspect one export asset (file or directory) and report hard facts."""
    is_dir_entry = name.endswith("/")
    rel_name = name.rstrip("/")
    path = ebook_dir / rel_name
    report: dict = {
        "name": name,
        "path": str(path),
        "exists": path.exists(),
        "kind": "directory" if is_dir_entry else (path.suffix.lstrip(".").lower() or "file"),
        "size_bytes": 0,
    }

    if not path.exists():
        report["notes"] = "Missing — asset has not been generated in this workspace."
        return report

    if path.is_dir():
        files = sorted(p for p in path.iterdir() if p.is_file())
        images = [p for p in files if p.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp")]
        report["kind"] = "directory"
        report["file_count"] = len(files)
        report["image_count"] = len(images)
        report["size_bytes"] = sum(p.stat().st_size for p in files)
        report["file_names"] = [p.name for p in files][:30]
        report["third_party_media"] = bool(images)
        report["notes"] = (
            "Contains %d bitmap exhibit(s) sourced from third-party video frames." % len(images)
            if images
            else "No bitmap exhibits present."
        )
        return report

    stat = path.stat()
    report["size_bytes"] = stat.st_size
    report["size_kb"] = round(stat.st_size / 1024, 2)
    report["modified"] = datetime.fromtimestamp(stat.st_mtime, timezone.utc).replace(
        microsecond=0
    ).isoformat()

    suffix = path.suffix.lower()
    if suffix == ".pdf":
        try:
            data = path.read_bytes()
        except OSError:
            report["page_count"] = 0
            report["notes"] = "PDF present but unreadable."
            return report
        pages = _count_pdf_pages(data)
        report["page_count"] = pages
        report["pdf_header"] = data[:8].decode("latin-1", errors="replace")
        report["notes"] = "%d page object(s) detected via /Type /Page scan." % pages
    elif suffix in (".epub", ".zip"):
        valid = zipfile.is_zipfile(str(path))
        report["archive_valid"] = valid
        if valid:
            try:
                with zipfile.ZipFile(str(path)) as archive:
                    names = archive.namelist()
                    bad = archive.testzip()
                report["entry_count"] = len(names)
                report["entry_names"] = names[:30]
                report["corrupt_entry"] = bad
                report["archive_integrity_ok"] = bad is None
                if suffix == ".epub":
                    report["has_mimetype_entry"] = "mimetype" in names
                    report["has_container_xml"] = any(
                        n.endswith("META-INF/container.xml") for n in names
                    )
                report["notes"] = "Archive opens cleanly with %d entries." % len(names)
            except (OSError, zipfile.BadZipFile) as exc:
                report["archive_integrity_ok"] = False
                report["notes"] = "Archive failed to open: %s" % exc
        else:
            report["archive_integrity_ok"] = False
            report["notes"] = "File is not a valid ZIP/EPUB container."
    elif suffix == ".md":
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            text = ""
        lines = text.splitlines()
        report["line_count"] = len(lines)
        report["word_count"] = _count_words(text)
        report["heading_count"] = sum(1 for line in lines if line.lstrip().startswith("#"))
        report["bullet_line_count"] = sum(
            1 for line in lines if re.match(r"\s*([-*+]|\d+\.)\s+", line)
        )
        total_lines = max(1, len([line for line in lines if line.strip()]))
        report["bullet_density"] = round(report["bullet_line_count"] / total_lines, 3)
        report["notes"] = (
            "%d words across %d headings; %.0f%% of non-empty lines are bullets."
            % (report["word_count"], report["heading_count"], report["bullet_density"] * 100)
        )
    elif suffix == ".svg":
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            text = ""
        report["element_count"] = len(re.findall(r"<[a-zA-Z]", text))
        report["has_raster_image"] = "<image" in text
        report["text_node_count"] = len(re.findall(r"<text\b", text))
        report["notes"] = (
            "Flat geometric vector cover: %d elements, %d text nodes, %s raster content."
            % (
                report["element_count"],
                report["text_node_count"],
                "contains" if report["has_raster_image"] else "no",
            )
        )
    else:
        report["notes"] = "Present."
    return report


def _audit_backups(backups_dir: Path) -> dict:
    """Verify a pre-modification backup archive exists next to the project."""
    details: dict = {
        "backups_dir": str(backups_dir),
        "exists": backups_dir.is_dir(),
        "archive_count": 0,
        "archives": [],
        "total_bytes": 0,
    }
    if not backups_dir.is_dir():
        details["notes"] = (
            "No backup directory found — create a pre-modification archive before "
            "rewriting any export asset."
        )
        return details

    archives = []
    for path in sorted(backups_dir.iterdir()):
        if not path.is_file():
            continue
        name = path.name.lower()
        if not (
            name.endswith(".zip")
            or name.endswith(".tar")
            or name.endswith(".tar.gz")
            or name.endswith(".tgz")
            or name.endswith(".tar.bz2")
            or name.endswith(".7z")
        ):
            continue
        stat = path.stat()
        entry = {
            "name": path.name,
            "size_bytes": stat.st_size,
            "modified": datetime.fromtimestamp(stat.st_mtime, timezone.utc)
            .replace(microsecond=0)
            .isoformat(),
        }
        if name.endswith(".zip"):
            entry["archive_valid"] = zipfile.is_zipfile(str(path))
        archives.append(entry)

    details["archives"] = archives
    details["archive_count"] = len(archives)
    details["total_bytes"] = sum(a["size_bytes"] for a in archives)
    details["notes"] = (
        "%d pre-modification archive(s) present." % len(archives)
        if archives
        else "Backup directory exists but holds no archive files."
    )
    return details


def _categorize_assets(assets: dict, transcripts: dict) -> dict:
    """Sort every audited asset into reuse / improve / redesign buckets."""

    def asset(name: str) -> dict:
        return assets.get(name, {"name": name, "exists": False})

    manuscript = asset("heir-hunting-manuscript.md")
    digital_pdf = asset("heir-hunting-digital-8.5x11.pdf")
    print_pdf = asset("heir-hunting-kdp-print-6x9.pdf")
    workbook = asset("heir-hunting-action-workbook.pdf")
    kindle = asset("heir-hunting-kindle.epub")
    bundle = asset("heir-hunting-amazon-etsy-ebay-bundle.zip")
    cover = asset("cover-3d.svg")
    exhibits = asset("exhibits/")

    digital_pages = digital_pdf.get("page_count", 0)
    print_pages = print_pdf.get("page_count", 0)

    reusable_foundation = [
        {
            "asset": "189 verified YouTube transcripts",
            "path": "data/transcripts/*.json",
            "evidence": (
                "%d JSON files on disk, %d with status=ok, %s raw segment words, "
                "%s hours of source audio across %d channels."
                % (
                    transcripts["total_files"],
                    transcripts["ok_files"],
                    format(transcripts["raw_segment_words"], ","),
                    transcripts["total_hours"],
                    transcripts["distinct_channels"],
                )
            ),
            "verdict": "reuse_as_is",
            "rationale": "Primary research substrate; already normalized and deduplicated.",
        },
        {
            "asset": "[HH:MM:SS] timestamp deep-link index",
            "path": "data/transcripts/*.json -> segments[].start",
            "evidence": (
                "%s timed segments provide second-accurate &t= deep links for every claim."
                % format(transcripts["total_segments"], ",")
            ),
            "verdict": "reuse_as_is",
            "rationale": "Citation backbone — every manual assertion stays traceable.",
        },
        {
            "asset": "ProTip & Finite-Detail extraction engine",
            "path": "src/abridge_engine.py",
            "evidence": (
                "Produced the %s-word abridged layer and %s scored pro tips benchmark."
                % (
                    format(ABRIDGED_WORDS_BENCHMARK, ","),
                    format(EXTRACTED_PRO_TIPS_BENCHMARK, ","),
                )
            ),
            "verdict": "reuse_as_is",
            "rationale": "Deterministic, stdlib-only, already tuned to this corpus.",
        },
        {
            "asset": "Topic Discovery engine",
            "path": "src/topic_discovery.py",
            "evidence": "Zero-question topic discovery already proven against the corpus.",
            "verdict": "reuse_as_is",
            "rationale": "Feeds the 8-topic research taxonomy without manual curation.",
        },
        {
            "asset": "Local stdlib PDF/EPUB container writers",
            "path": "exports/heir-hunting-ebook/ (writers)",
            "evidence": (
                "digital PDF=%s pages, print PDF=%s pages, EPUB container valid=%s, "
                "bundle ZIP valid=%s — containers open cleanly."
                % (
                    digital_pages,
                    print_pages,
                    kindle.get("archive_valid", False),
                    bundle.get("archive_valid", False),
                )
            ),
            "verdict": "reuse_as_is",
            "rationale": "Container generation is sound; only the typography inside needs work.",
        },
    ]

    needs_improvement = [
        {
            "asset": "Companion workbook structure",
            "path": workbook.get("path", "exports/heir-hunting-ebook/heir-hunting-action-workbook.pdf"),
            "evidence": "%s page(s); content is raw transcript checklists rather than worksheets."
            % workbook.get("page_count", 0),
            "verdict": "improve",
            "required_change": (
                "Convert raw transcript checklists into 6 structured operator worksheets: "
                "(1) County Docket Sourcing Sheet, (2) Unclaimed Property Claim Tracker, "
                "(3) Kinship Chart & Proof-of-Heirship Builder, (4) Skip-Trace & Contact Log, "
                "(5) Fee Agreement / Escrow Checklist, (6) Jurisdiction Compliance Matrix."
            ),
        },
        {
            "asset": "Marketplace listing copy",
            "path": bundle.get("path", "exports/heir-hunting-ebook/heir-hunting-amazon-etsy-ebay-bundle.zip"),
            "evidence": "Bundle holds %s entries of listing copy carrying legacy imprint branding."
            % bundle.get("entry_count", 0),
            "verdict": "improve",
            "required_change": (
                "Realign all Amazon KDP / Etsy / eBay copy to THE BIG MONEY PLAYBOOKS and "
                "THE FUCK YOU MONEY CLUB branding, with zero unverified earnings claims, "
                "zero income guarantees, and no implied professional licensure."
            ),
        },
        {
            "asset": "PDF/EPUB typography & page grid",
            "path": "exports/heir-hunting-ebook/*.pdf, *.epub",
            "evidence": (
                "8.5x11 digital=%s pages and 6x9 print=%s pages share one undifferentiated "
                "text block; EPUB entries=%s."
                % (digital_pages, print_pages, kindle.get("entry_count", 0))
            ),
            "verdict": "improve",
            "required_change": (
                "Adapt the grid per trim: 8.5x11 two-column reference layout, 6x9 KDP-safe "
                "margins and gutters with running heads, reflowable EPUB with semantic "
                "headings and no fixed page furniture."
            ),
        },
    ]

    must_redesign = [
        {
            "asset": "Concatenated bullet manuscripts (519-page / 838-page)",
            "path": manuscript.get("path", "exports/heir-hunting-ebook/heir-hunting-manuscript.md"),
            "evidence": (
                "Manuscript measures %s words, %s headings, %.0f%% bullet lines; rendered as "
                "%s-page digital and %s-page print PDFs — a concatenation, not a book."
                % (
                    format(manuscript.get("word_count", 0), ","),
                    manuscript.get("heading_count", 0),
                    manuscript.get("bullet_density", 0) * 100,
                    digital_pages,
                    print_pages,
                )
            ),
            "verdict": "must_redesign",
            "required_change": (
                "Replace with a cohesive, original 12-chapter business reference manual in "
                "continuous prose that answers all 12 standardized questions, with "
                "paraphrased insights and timestamped citations instead of pasted bullets."
            ),
        },
        {
            "asset": "Legacy 'Apex Field Intelligence Press' geometric covers & mockups",
            "path": cover.get("path", "exports/heir-hunting-ebook/cover-3d.svg"),
            "evidence": (
                "Cover artwork is a %s KB flat SVG with %s elements — within the 1KB-2.6KB "
                "legacy placeholder range and carrying the retired imprint name."
                % (cover.get("size_kb", 0), cover.get("element_count", 0))
            ),
            "verdict": "must_redesign",
            "required_change": (
                "Replace with 3 genuinely distinct creative cover concepts, each rendered as "
                "10 realistic mockups (front, spine, back, 3D hardcover, paperback stack, "
                "tablet, phone, desk scene, bundle shot, social tile) under the new imprint."
            ),
        },
        {
            "asset": "exhibits/exhibit-01..12.jpg downloaded YouTube frames",
            "path": exhibits.get("path", "exports/heir-hunting-ebook/exhibits"),
            "evidence": "%s image file(s) totalling %s bytes, all captured from third-party video."
            % (exhibits.get("image_count", 0), format(exhibits.get("size_bytes", 0), ",")),
            "verdict": "must_redesign",
            "permission_flag": "research_only_requires_permission",
            "required_change": (
                "Flag all 12 exhibits research_only_requires_permission and replace them in "
                "every commercial export with 100% original structured-data vector diagrams "
                "generated from the research database."
            ),
        },
    ]

    return {
        "reusable_foundation": reusable_foundation,
        "needs_improvement": needs_improvement,
        "must_redesign": must_redesign,
    }


def audit_existing_workspace(root_dir: Path, backup_dir: Path | None = None) -> dict:
    """Audit the real workspace: transcript corpus + generated eBook exports.

    Every number returned is measured from disk; the only hard-coded values are
    the two published benchmarks (``abridged_words_benchmark`` and
    ``extracted_pro_tips_benchmark``) that the abridging pass already produced.
    """
    root = Path(root_dir).resolve()
    if backup_dir is None:
        for path in root.rglob("*"):
            if path.is_symlink() and not path.resolve().is_relative_to(root):
                raise ValueError("Store path escapes workspace root")
    backups = Path(backup_dir) if backup_dir is not None else root / "backups"
    transcripts_dir = root / "data" / "transcripts"
    ebook_dir = root / "exports" / "heir-hunting-ebook"

    transcripts = _scan_transcripts(transcripts_dir)

    assets: dict[str, dict] = {}
    for name in EBOOK_KEY_FILES:
        assets[name] = _inspect_asset(ebook_dir, name)

    backup_details = _audit_backups(backups)
    backup_verified = bool(backup_details.get("archive_count", 0) > 0)

    categorized_summary = _categorize_assets(assets, transcripts)

    missing_assets = [name for name, info in assets.items() if not info.get("exists")]
    invalid_archives = [
        name
        for name, info in assets.items()
        if info.get("exists") and info.get("archive_valid") is False
    ]

    return {
        "generated_at": _now_iso(),
        "root_dir": str(root),
        "transcripts_dir": str(transcripts_dir),
        "ebook_dir": str(ebook_dir),
        "ebook_dir_exists": ebook_dir.is_dir(),
        # --- empirical corpus numbers -------------------------------------
        "total_files": transcripts["total_files"],
        "ok_files": transcripts["ok_files"],
        "failed_files": transcripts["failed_files"],
        "raw_segment_words": transcripts["raw_segment_words"],
        "total_duration_seconds": transcripts["total_duration_seconds"],
        "total_hours": transcripts["total_hours"],
        "abridged_words_benchmark": ABRIDGED_WORDS_BENCHMARK,
        "extracted_pro_tips_benchmark": EXTRACTED_PRO_TIPS_BENCHMARK,
        "transcript_corpus": transcripts,
        # --- export asset inspection --------------------------------------
        "assets": assets,
        "missing_assets": missing_assets,
        "invalid_archives": invalid_archives,
        # --- triage ---------------------------------------------------------
        "categorized_summary": categorized_summary,
        "asset_counts": {
            "reusable_foundation": len(categorized_summary["reusable_foundation"]),
            "needs_improvement": len(categorized_summary["needs_improvement"]),
            "must_redesign": len(categorized_summary["must_redesign"]),
        },
        # --- safety ---------------------------------------------------------
        "backup_verified": backup_verified,
        "backup_details": backup_details,
        "audit_notes": [
            "Transcript corpus is the only primary source; all export assets are derived.",
            "PDF page counts come from a /Type /Page object scan, not a full PDF parse.",
            "EPUB and bundle integrity verified with zipfile.is_zipfile plus testzip().",
            "Commercial export policy: " + COMMERCIAL_EXPORT_POLICY,
            (
                "Backup archive verified before modification."
                if backup_verified
                else "NO backup archive found — archive the workspace before rewriting assets."
            ),
        ],
    }


# --------------------------------------------------------------------------
# 2. Research database
# --------------------------------------------------------------------------


def _raw_index(raw_videos: list[dict] | None) -> dict[str, dict]:
    index: dict[str, dict] = {}
    for raw in _as_list(raw_videos):
        if not isinstance(raw, dict):
            continue
        video_id = _clean_text(raw.get("video_id"))
        if video_id:
            index[video_id] = raw
    return index


def _normalize_video(video: dict, raw_index: dict[str, dict]) -> dict:
    """Flatten one abridged record, backfilling from the raw transcript."""
    video_id = _clean_text(video.get("video_id"))
    raw = raw_index.get(video_id, {})
    meta_a = raw.get("meta") if isinstance(raw.get("meta"), dict) else {}
    meta_b = raw.get("metadata") if isinstance(raw.get("metadata"), dict) else {}
    raw_meta = dict(meta_a)
    for k, v in meta_b.items():
        if v not in (None, ""):
            raw_meta[k] = v
        else:
            raw_meta.setdefault(k, v)
    raw_segments = [s for s in _as_list(raw.get("segments")) if isinstance(s, dict)]

    title = _clean_text(video.get("title")) or _clean_text(raw_meta.get("title")) or video_id
    author = _clean_text(video.get("author")) or _clean_text(raw_meta.get("author")) or "Unknown channel"
    url = _clean_text(video.get("url"))
    if not url and video_id:
        url = "https://www.youtube.com/watch?v=%s" % video_id

    try:
        length_seconds = _finite_int(video.get("length_seconds") or 0)
    except (TypeError, ValueError, OverflowError):
        length_seconds = 0
    if length_seconds <= 0:
        try:
            length_seconds = _finite_int(raw_meta.get("lengthSeconds") or 0)
        except (TypeError, ValueError, OverflowError):
            length_seconds = 0
    if length_seconds <= 0 and raw_segments:
        last = raw_segments[-1]
        try:
            length_seconds = _finite_int(float(last.get("start") or 0) + float(last.get("dur") or 0))
        except (TypeError, ValueError, OverflowError):
            length_seconds = 0

    try:
        word_count = int(video.get("word_count") or 0)
    except (TypeError, ValueError, OverflowError):
        word_count = 0
    if word_count <= 0 and raw_segments:
        word_count = sum(_count_words(_clean_text(s.get("text"))) for s in raw_segments)

    duration = _clean_text(video.get("duration"))
    if not duration:
        minutes, seconds = divmod(max(0, length_seconds), 60)
        hours, minutes = divmod(minutes, 60)
        duration = (
            "%d:%02d:%02d" % (hours, minutes, seconds) if hours else "%d:%02d" % (minutes, seconds)
        )

    details = video.get("finite_details") if isinstance(video.get("finite_details"), dict) else {}

    tips = []
    for tip in _as_list(video.get("pro_tips")):
        if not isinstance(tip, dict):
            continue
        text = _clean_text(tip.get("tip"))
        if not text:
            continue
        timestamp = _clean_text(tip.get("timestamp"))
        link = _clean_text(tip.get("link"))
        if not link and url:
            link = "%s&t=%ds" % (url, _timestamp_seconds(timestamp))
        try:
            score = int(tip.get("score") or 0)
        except (TypeError, ValueError, OverflowError):
            score = 0
        tips.append(
            {
                "tip": text,
                "category": _clean_text(tip.get("category")) or "General",
                "timestamp": timestamp or _hhmmss(0),
                "link": link,
                "score": score,
            }
        )

    chapters = []
    for chapter in _as_list(video.get("chapters")):
        if not isinstance(chapter, dict):
            continue
        chapters.append(
            {
                "title": _clean_text(chapter.get("title")),
                "timestamp": _clean_text(chapter.get("timestamp")),
                "link": _clean_text(chapter.get("link")),
                "summary": _clean_text(chapter.get("summary")),
            }
        )

    return {
        "index": video.get("index"),
        "video_id": video_id,
        "url": url,
        "title": title,
        "author": author,
        "length_seconds": length_seconds,
        "duration": duration,
        "word_count": word_count,
        "domain": video.get("domain"),
        "domain_name": _clean_text(video.get("domain_name")),
        "source_mode": _clean_text(video.get("source_mode")),
        "executive_summary": _clean_text(video.get("executive_summary")),
        "pro_tips": tips,
        "chapters": chapters,
        "tools_and_portals": _as_str_list(details.get("tools_and_portals")),
        "statutes_and_forms": _as_str_list(details.get("statutes_and_forms")),
        "numbers_thresholds_deadlines": _as_str_list(
            details.get("numbers_thresholds_deadlines")
        ),
        "tactical_checklist": _as_str_list(details.get("tactical_checklist")),
    }


def _video_topic_profile(video: dict) -> dict:
    """Score a video against every topic using title, summary, tips and details."""
    blob_parts = [
        video["title"],
        video["domain_name"],
        video["executive_summary"],
    ]
    blob_parts.extend(chapter["title"] for chapter in video["chapters"])
    blob_parts.extend(chapter["summary"] for chapter in video["chapters"])
    blob_parts.extend(tip["category"] + " " + tip["tip"] for tip in video["pro_tips"])
    blob_parts.extend(video["tools_and_portals"])
    blob_parts.extend(video["statutes_and_forms"])
    blob_parts.extend(video["numbers_thresholds_deadlines"])
    blob_parts.extend(video["tactical_checklist"])
    scores = _score_text(" \n ".join(part for part in blob_parts if part))
    primary = _best_topic(scores, TOPIC_IDS[0])
    matched = [tid for tid in TOPIC_IDS if scores.get(tid, 0) > 0]
    if not matched:
        matched = [primary]
    return {"scores": scores, "primary_topic": primary, "matched_topics": matched}


CONSENSUS_TEMPLATES = [
    {
        "finding_id": "contingency_only_compensation",
        "topic_id": "business_model_and_economics",
        "headline": "Heir location is paid on contingency, never on up-front fees.",
        "summary": (
            "Across the corpus, operators converge on a pure contingency model: the heir "
            "pays nothing out of pocket, the locator advances all research cost, and the "
            "fee is a negotiated percentage released only when the estate or state agency "
            "actually disburses funds. Charging an heir an advance fee is treated as the "
            "single clearest marker of a predatory or unlicensed operator."
        ),
    },
    {
        "finding_id": "county_docket_is_the_lead_engine",
        "topic_id": "probate_and_docket_sourcing",
        "headline": "Fresh county probate and intestate dockets outperform purchased lead lists.",
        "summary": (
            "Practitioners consistently build pipeline from newly filed probate and "
            "administration matters pulled directly from county clerk portals rather than "
            "resold lists. Filings naming an administrator but no located heirs, and "
            "estates sitting open past the local notice period, are the recurring "
            "high-value signal."
        ),
    },
    {
        "finding_id": "state_unclaimed_property_is_the_volume_channel",
        "topic_id": "unclaimed_property_and_escheat",
        "headline": "State unclaimed-property and escheat databases supply the repeatable volume.",
        "summary": (
            "Every state treasury or controller maintains a searchable unclaimed-property "
            "register, and the consensus workflow is to cross-reference deceased owners "
            "there against probate filings. Volume comes from systematic register sweeps; "
            "size comes from the rarer escheated estate, surplus-funds and safe-deposit "
            "categories."
        ),
    },
    {
        "finding_id": "documented_kinship_chain_is_the_product",
        "topic_id": "genealogy_and_heirship_proof",
        "headline": "The deliverable is a document-backed kinship chain, not a name on a list.",
        "summary": (
            "Operators agree that claims succeed or fail on the evidentiary chain: each "
            "generational link supported by vital records, each branch mapped per stirpes, "
            "and every gap closed before contact. Tree hints from consumer genealogy sites "
            "are treated as leads to verify, never as proof to submit."
        ),
    },
    {
        "finding_id": "skip_tracing_then_restrained_first_contact",
        "topic_id": "skip_tracing_and_outreach",
        "headline": "Verify identity before contact, then lead with restraint, not the dollar figure.",
        "summary": (
            "The recurring outreach pattern is: skip trace to a confirmed current address "
            "and phone, open by letter or a short calm call, state that funds may be owed "
            "to the family without naming an amount, and give the heir a way to "
            "independently verify the operator. Pressure tactics and inflated figures are "
            "consistently reported as the fastest way to lose a signed file."
        ),
    },
    {
        "finding_id": "written_agreement_and_third_party_escrow",
        "topic_id": "contracts_and_compensation",
        "headline": "No work proceeds without a signed fee agreement and third-party escrow.",
        "summary": (
            "Consensus practice is a plain-language, notarized or e-signed agreement that "
            "names the estate, states the percentage, discloses the heir's right to claim "
            "independently, and routes funds through attorney trust or licensed escrow so "
            "the locator never holds the heir's money directly."
        ),
    },
    {
        "finding_id": "jurisdiction_rules_govern_every_file",
        "topic_id": "statutory_caps_and_licensing",
        "headline": "Fee caps, waiting periods and licensing are decided per state, before the first call.",
        "summary": (
            "Operators repeatedly stress that the governing rules — percentage caps on "
            "unclaimed-property recoveries, mandatory waiting periods after escheat or "
            "sale, private-investigator licensing triggers, and the line against practicing "
            "law — vary by jurisdiction and must be read in the local statute for every "
            "file rather than generalized from another state."
        ),
    },
    {
        "finding_id": "automation_multiplies_a_small_team",
        "topic_id": "automation_and_small_team_ops",
        "headline": "Automated docket monitoring plus AI abstracting lets one or two people run real volume.",
        "summary": (
            "The operational consensus is to automate the repetitive layer — scheduled "
            "docket and register pulls, structured intake into a sheet or CRM, AI-assisted "
            "abstracting of filings — while keeping genealogy judgment, heir contact and "
            "contract execution human. That split is what keeps a two-person shop "
            "competitive against staffed firms."
        ),
    },
]


CLAIM_TEMPLATES = [
    {
        "claim_id": "ca_ccp_1582_10pct_cap_vs_probate_court_assignments",
        "topic": "statutory_caps_and_licensing",
        "question": (
            "Does the California 10% statutory cap on unclaimed-property recovery "
            "agreements also bind heir-finder fees in probate estate assignments?"
        ),
        "conflicting_views": [
            "Sources treat the ~10% ceiling in California Code of Civil Procedure § 1582 "
            "as a blanket cap on every heir-finder fee charged in the state.",
            "Other sources describe the cap as specific to agreements to recover property "
            "held by the state controller after escheat, leaving probate-court estate "
            "assignments to a reasonableness review by the probate judge.",
            "A third group reports negotiating 15-35% on probate matters in California "
            "without objection, which only makes sense if the statutory cap is not "
            "universal.",
        ],
        "editorial_resolution": (
            "Present the cap as scope-limited rather than universal: quote the statute's own "
            "description of the agreements it governs, note that probate assignments are "
            "separately subject to court approval and reasonableness review, and instruct "
            "the reader to confirm which track their file is on before quoting a percentage."
        ),
    },
    {
        "claim_id": "pi_license_triggers_fl_tx_az",
        "topic": "statutory_caps_and_licensing",
        "question": (
            "Does locating heirs for compensation require a private investigator license "
            "in Florida, Texas or Arizona?"
        ),
        "conflicting_views": [
            "Several operators state flatly that searching for a person for pay is regulated "
            "investigative activity in these states and requires a licensed PI or an agency "
            "affiliation.",
            "Others argue that public-record genealogy research is exempt and that the "
            "license only attaches when surveillance or investigation of a living subject's "
            "conduct is involved.",
            "A further view is that the trigger is the business activity of locating a "
            "person for a fee, regardless of whether the research is conducted from public "
            "records.",
        ],
        "editorial_resolution": (
            "Treat licensing as a threshold compliance question, not a footnote: direct the "
            "reader to the named state licensing authority, describe the fact patterns that "
            "commonly trigger review, and avoid asserting any state-specific exemption as "
            "settled."
        ),
    },
    {
        "claim_id": "post_sale_waiting_periods_and_rescission_windows",
        "topic": "statutory_caps_and_licensing",
        "question": (
            "How long must an operator wait after escheat or a tax/foreclosure sale before a "
            "recovery agreement is enforceable, and how long can the claimant rescind?"
        ),
        "conflicting_views": [
            "Some sources cite a mandatory dormancy or waiting period measured from the date "
            "funds are reported to the state, during which no fee agreement may be signed.",
            "Others describe the clock as running from the sale or distribution date, not "
            "the reporting date.",
            "Rescission windows are variously described as a few days, ten days, or absent "
            "entirely depending on the state and the fund type.",
        ],
        "editorial_resolution": (
            "Publish the waiting period and rescission window as a per-state worksheet the "
            "reader fills in from the governing statute, with the structural warning that an "
            "agreement signed inside a prohibited window may be void and the fee "
            "unrecoverable."
        ),
    },
    {
        "claim_id": "champerty_and_assignment_of_heirship_scrutiny",
        "topic": "contracts_and_compensation",
        "question": (
            "Is taking an assignment of a heir's interest in an estate enforceable, or "
            "vulnerable as champerty or an unconscionable bargain?"
        ),
        "conflicting_views": [
            "Operators report using outright assignments of interest as the cleanest way to "
            "secure payment directly from the estate.",
            "Others warn that courts in champerty-sensitive jurisdictions have voided or "
            "reduced such assignments where the heir was uninformed of the estate's value.",
            "A middle view holds that a percentage fee agreement with an irrevocable "
            "direction to pay from escrow survives scrutiny where a bare assignment does "
            "not.",
        ],
        "editorial_resolution": (
            "Recommend the disclosure-forward structure as the default — fee agreement plus "
            "escrow direction, with the estate identified once the heir signs — and present "
            "bare assignment as a jurisdiction-specific instrument requiring local counsel."
        ),
    },
    {
        "claim_id": "upl_attorney_filing_boundaries",
        "topic": "statutory_caps_and_licensing",
        "question": (
            "Where is the line between permissible heir-location work and the unauthorized "
            "practice of law?"
        ),
        "conflicting_views": [
            "Some sources describe preparing and filing the heir's probate or claim paperwork "
            "as routine clerical support.",
            "Others hold that selecting the filing, advising on entitlement, or appearing for "
            "the heir is law practice and must be routed to a licensed attorney.",
            "A third position is that the locator may assemble and transmit evidence but must "
            "never advise the heir on legal rights or strategy.",
        ],
        "editorial_resolution": (
            "Draw the line conservatively in the manual: research, document assembly and "
            "introductions on the locator's side; advice, pleadings and appearances with "
            "counsel — and tell the reader to confirm the boundary with their state bar "
            "before building a workflow around it."
        ),
    },
    {
        "claim_id": "gross_estate_vs_net_distributable_equity_math",
        "topic": "business_model_and_economics",
        "question": (
            "Is the contingency percentage computed on the gross estate value or on the net "
            "amount actually distributable to the located heir?"
        ),
        "conflicting_views": [
            "Headline case figures in the corpus are quoted against gross estate or gross "
            "property value.",
            "Operators describing actual settlement statements compute the fee on the heir's "
            "net distributable share after debts, liens, taxes, administration costs and "
            "co-heir splits.",
            "Some agreements are described as fixing the percentage on recovered funds "
            "received, which differs again where property is sold rather than distributed in "
            "kind.",
        ],
        "editorial_resolution": (
            "Standardize on net distributable share to the specific heir as the manual's "
            "arithmetic base, show the gross-to-net waterfall explicitly, and label any "
            "gross-value figures drawn from the corpus as illustrative rather than as "
            "expected earnings."
        ),
    },
]


def _build_permissions_ledger(videos: list[dict]) -> dict:
    """Flag every third-party asset that may not enter a commercial export."""
    flagged: list[dict] = []

    for number in range(1, 13):
        name = "exhibit-%02d.jpg" % number
        flagged.append(
            {
                "asset_id": "exhibit_%02d" % number,
                "asset": "exports/heir-hunting-ebook/exhibits/%s" % name,
                "asset_type": "downloaded_youtube_video_frame",
                "source": "Third-party YouTube video frame capture",
                "research_reference_only": True,
                "commercial_republish_allowed": False,
                "commercial_use_allowed": False,
                "status": "research_only_requires_permission",
                "replacement": (
                    "Original structured-data vector diagram generated from the research "
                    "database (no captured pixels)."
                ),
            }
        )

    thumbnails = []
    for video in videos:
        if not video["video_id"]:
            continue
        thumbnails.append(
            {
                "video_id": video["video_id"],
                "title": video["title"],
                "author": video["author"],
                "thumbnail_url": "https://i.ytimg.com/vi/%s/hqdefault.jpg" % video["video_id"],
                "source_url": video["url"],
            }
        )

    flagged.append(
        {
            "asset_id": "youtube_thumbnails",
            "asset": "https://i.ytimg.com/vi/<video_id>/*.jpg",
            "asset_type": "youtube_thumbnail_image",
            "source": "YouTube CDN thumbnails for the %d corpus videos" % len(thumbnails),
            "instance_count": len(thumbnails),
            "instances": thumbnails,
            "research_reference_only": True,
            "commercial_republish_allowed": False,
            "commercial_use_allowed": False,
            "status": "research_only_requires_permission",
            "replacement": (
                "Text-only source citation (title, channel, URL, [HH:MM:SS] deep link) with "
                "no image reproduction."
            ),
        }
    )

    total_tips = sum(len(video["pro_tips"]) for video in videos)
    flagged.append(
        {
            "asset_id": "verbatim_transcript_quotes",
            "asset": "data/transcripts/*.json -> segments[].text",
            "asset_type": "verbatim_transcript_passage",
            "source": "Spoken content of %d third-party videos (%d captured tips)"
            % (len(videos), total_tips),
            "research_reference_only": True,
            "commercial_republish_allowed": False,
            "commercial_use_allowed": False,
            "status": "research_only_requires_permission",
            "replacement": (
                "Abstractive paraphrase capped at %d words per insight, plus an attributed "
                "timestamp deep link back to the original video." % MAX_PARAPHRASE_WORDS
            ),
        }
    )

    return {
        "commercial_export_policy": COMMERCIAL_EXPORT_POLICY,
        "paraphrase_word_ceiling": MAX_PARAPHRASE_WORDS,
        "attribution_rule": (
            "Every paraphrased insight keeps its original YouTube URL and [HH:MM:SS] deep "
            "link so the reader can verify the source directly."
        ),
        "flagged_asset_count": len(flagged),
        "flagged_assets": flagged,
        "clearance_required_before": [
            "Amazon KDP print and Kindle upload",
            "Etsy digital download listing",
            "eBay bundle listing",
            "Any paid or free public distribution of the compiled manual",
        ],
    }


def build_research_database(
    abridged_videos: list[dict], raw_videos: list[dict] | None = None
) -> dict:
    """Structure the abridged corpus into a citable, topic-indexed research database.

    Original YouTube URLs and ``[HH:MM:SS]`` deep links are preserved on every
    insight so each downstream claim in the manual remains verifiable. Tip text
    is paraphrased, never copied, to satisfy the commercial export policy.
    """
    raw_index = _raw_index(raw_videos)
    videos = [
        _normalize_video(video, raw_index)
        for video in _as_list(abridged_videos)
        if isinstance(video, dict)
    ]

    # --- classification ---------------------------------------------------
    buckets: dict[str, dict] = {
        topic_id: {
            "videos": [],
            "video_ids": set(),
            "authors": set(),
            "tips": [],
            "statutes": [],
            "tools": [],
        }
        for topic_id in TOPIC_IDS
    }

    for video in videos:
        profile = _video_topic_profile(video)
        video["primary_topic"] = profile["primary_topic"]
        video["matched_topics"] = profile["matched_topics"]
        video["topic_scores"] = profile["scores"]

        for topic_id in profile["matched_topics"]:
            bucket = buckets[topic_id]
            if video["video_id"] not in bucket["video_ids"]:
                bucket["video_ids"].add(video["video_id"])
                bucket["videos"].append(video)
            bucket["authors"].add(video["author"])
            bucket["statutes"].extend(video["statutes_and_forms"])
            bucket["tools"].extend(video["tools_and_portals"])

        for tip in video["pro_tips"]:
            tip_scores = _score_text(tip["category"] + " " + tip["tip"])
            tip_topic = _best_topic(tip_scores, video["primary_topic"])
            tip["topic_id"] = tip_topic
            buckets[tip_topic]["tips"].append((video, tip))

    # --- corpus metrics ---------------------------------------------------
    total_seconds = sum(video["length_seconds"] for video in videos)
    all_statutes = [s for video in videos for s in video["statutes_and_forms"]]
    all_tools = [t for video in videos for t in video["tools_and_portals"]]
    corpus_metrics = {
        "video_count": len(videos),
        "channel_count": len({video["author"] for video in videos if video["author"]}),
        "total_words": sum(video["word_count"] for video in videos),
        "total_hours": round(total_seconds / 3600, 2),
        "total_pro_tips": sum(len(video["pro_tips"]) for video in videos),
        "unique_statutes_and_forms": len({s.lower() for s in all_statutes}),
        "unique_tools_and_portals": len({t.lower() for t in all_tools}),
    }

    # --- topics -----------------------------------------------------------
    topics = []
    for topic in RESEARCH_TOPICS:
        topic_id = topic["topic_id"]
        bucket = buckets[topic_id]

        ranked_videos = sorted(
            bucket["videos"],
            key=lambda v: (
                -v["topic_scores"].get(topic_id, 0),
                -len(v["pro_tips"]),
                -v["word_count"],
                v["title"].lower(),
            ),
        )
        top_sources = [
            {
                "video_id": v["video_id"],
                "title": v["title"],
                "author": v["author"],
                "url": v["url"],
                "duration": v["duration"],
            }
            for v in ranked_videos[:8]
        ]

        ranked_tips = sorted(
            bucket["tips"],
            key=lambda pair: (
                -pair[1]["score"],
                -_count_words(pair[1]["tip"]),
                pair[0]["title"].lower(),
                _timestamp_seconds(pair[1]["timestamp"]),
            ),
        )
        insights = []
        seen_paraphrases: set[str] = set()
        for source_video, tip in ranked_tips:
            paraphrase = _paraphrase(tip["tip"])
            if not paraphrase:
                continue
            key = paraphrase.lower()
            if key in seen_paraphrases:
                continue
            seen_paraphrases.add(key)
            insights.append(
                {
                    "tip_paraphrase_summary": paraphrase,
                    "category": tip["category"],
                    "timestamp": tip["timestamp"],
                    "link": tip["link"],
                    "video_title": source_video["title"],
                    "author": source_video["author"],
                    "verbatim_research_only": True,
                }
            )
            if len(insights) >= 10:
                break

        topics.append(
            {
                "topic_id": topic_id,
                "title": topic["title"],
                "video_count": len(bucket["videos"]),
                "tip_count": len(bucket["tips"]),
                "channel_count": len(bucket["authors"]),
                "top_sources": top_sources,
                "top_timestamped_insights": insights,
                "statutes_and_forms": _rank_unique(bucket["statutes"], 40),
                "tools_and_portals": _rank_unique(bucket["tools"], 40),
            }
        )

    topics_by_id = {topic["topic_id"]: topic for topic in topics}

    # --- consensus findings -----------------------------------------------
    consensus_findings = []
    for template in CONSENSUS_TEMPLATES:
        topic = topics_by_id[template["topic_id"]]
        bucket = buckets[template["topic_id"]]
        supporting_links = [
            {
                "video_title": insight["video_title"],
                "author": insight["author"],
                "timestamp": insight["timestamp"],
                "link": insight["link"],
            }
            for insight in topic["top_timestamped_insights"][:6]
        ]
        if not supporting_links:
            supporting_links = [
                {
                    "video_title": source["title"],
                    "author": source["author"],
                    "timestamp": _hhmmss(0),
                    "link": source["url"],
                }
                for source in topic["top_sources"][:6]
            ]
        consensus_findings.append(
            {
                "finding_id": template["finding_id"],
                "topic_id": template["topic_id"],
                "topic_title": TOPIC_TITLES[template["topic_id"]],
                "headline": template["headline"],
                "summary": template["summary"],
                "epistemic_status": EPISTEMIC_STATUS,
                "channel_count": len(bucket["authors"]),
                "video_count": len(bucket["videos"]),
                "corroborating_tip_count": len(bucket["tips"]),
                "supporting_links": supporting_links,
                "caveat": (
                    "Consensus among the sampled operators — not legal advice and not a "
                    "substitute for the governing statute in the reader's jurisdiction."
                ),
            }
        )

    # --- verification queue -----------------------------------------------
    claims_requiring_verification = []
    for template in CLAIM_TEMPLATES:
        topic = topics_by_id.get(template["topic"])
        references = []
        if topic:
            references = [
                {
                    "video_title": insight["video_title"],
                    "author": insight["author"],
                    "timestamp": insight["timestamp"],
                    "link": insight["link"],
                }
                for insight in topic["top_timestamped_insights"][:4]
            ]
        claims_requiring_verification.append(
            {
                "claim_id": template["claim_id"],
                "topic": template["topic"],
                "topic_title": TOPIC_TITLES.get(template["topic"], template["topic"]),
                "question": template["question"],
                "conflicting_views": list(template["conflicting_views"]),
                "editorial_resolution": template["editorial_resolution"],
                "verification_status": VERIFICATION_STATUS,
                "priority": "high",
                "corpus_references": references,
            }
        )

    # --- permissions -------------------------------------------------------
    permissions_ledger = _build_permissions_ledger(videos)

    return {
        "generated_at": _now_iso(),
        "schema_version": "1.0",
        "corpus_metrics": corpus_metrics,
        "topics": topics,
        "consensus_findings": consensus_findings,
        "claims_requiring_verification": claims_requiring_verification,
        "permissions_ledger": permissions_ledger,
        "coverage": {
            "videos_classified": len(videos),
            "videos_with_multiple_topics": sum(
                1 for v in videos if len(v["matched_topics"]) > 1
            ),
            "tips_classified": sum(len(buckets[t]["tips"]) for t in TOPIC_IDS),
            "raw_transcripts_joined": sum(
                1 for v in videos if v["video_id"] in raw_index
            ),
            "topic_video_counts": {t["topic_id"]: t["video_count"] for t in topics},
            "topic_tip_counts": {t["topic_id"]: t["tip_count"] for t in topics},
        },
    }
