"""Abridger engine: per-video ProTip/Finite-Details digests, multi-video combination,
and custom prompt-driven Agent Operational Reports. Standard library only."""
from __future__ import annotations

import re

if __package__:
    from .fetch_transcripts import ROOT, fetch_video, Transport, RateGate, atomic_write, patch_existing_corpus
    from .storyboard_fallbacks import apply_storyboard_fallback
    from .report_playbook import DOMAINS, PROCEDURES
    from .build_agent_report import classify, mentions, stamp, windows, load_corpus, EvidenceIndex, tokens
else:  # pragma: no cover - top-level script usage
    from fetch_transcripts import ROOT, fetch_video, Transport, RateGate, atomic_write, patch_existing_corpus
    from storyboard_fallbacks import apply_storyboard_fallback
    from report_playbook import DOMAINS, PROCEDURES
    from build_agent_report import classify, mentions, stamp, windows, load_corpus, EvidenceIndex, tokens

RequestGate = RateGate  # backwards-compatible alias for earlier callers
REEXPORTS = (ROOT, fetch_video, Transport, RateGate, atomic_write, patch_existing_corpus,
             apply_storyboard_fallback, load_corpus, tokens)
OCR_STAMP = "whole-video reconstruction"

TRIGGERS = {"never": 5, "always": 4, "mistake": 5, "secret": 4, "pro tip": 5, "trick": 3, "hack": 3,
            "make sure": 4, "reject": 4, "instead": 2, "important": 3, "first": 2, "careful": 3,
            "don't": 4, "trap": 4, "exact": 3, "hidden": 3, "verify": 4, "rule": 3, "deadline": 5,
            "statute": 5, "percent": 3, "fee": 3, "court": 3, "lien": 4, "heir": 4, "deed": 4}
CATEGORIES = (("never|don't|mistake|trap|reject", "Pitfall / Hard No"),
              ("deadline|statute|court|lien|heir|deed|percent|fee", "Legal / Deadline"),
              ("secret|pro tip|trick|hack|hidden|exact", "Insider Tactic"),
              ("always|make sure|verify|important|rule|careful", "Non-Negotiable Rule"),
              ("first|instead", "Sequence / Alternative"))
VERBS = ("call", "pull", "file", "record", "order", "check", "search", "verify", "skip", "send",
         "sign", "request", "confirm", "open", "close", "negotiate", "offer", "contact", "review")

_URL_RE = re.compile(
    r"(?:youtube\.com/(?:watch\?(?:[^\s\"'<>&]*&)*v=|shorts/|embed/|live/|v/)|youtu\.be/)([A-Za-z0-9_-]{11})(?=$|[?&#/\s])"
    r"|(?<![A-Za-z0-9_\-/?=&.])([A-Za-z0-9_-]{11})(?![A-Za-z0-9_-])")
_STATUTE_RE = re.compile(
    r"(?:(?:Probate|Civil|Family|Estates?|Tax|Property|Business|Health(?:\s*&\s*Safety)?)\s+(?:and\s+\w+\s+)?Code"
    r"\s*(?:Section\s*)?§?\s*[\d.\-]*\d"
    r"|(?:HB|SB|AB|SJR)\s*\d+|Form\s+[A-Z0-9][\w\-/]*|(?:Section|Chapter|Rule|Article)\s+[\d.\-]*\d"
    r"|§\s*[\d.\-]*\d|Table\s+of\s+Heirship|Affidavit\s+of\s+[A-Z]\w+|Declaration\s+of\s+[A-Z]\w+"
    r"|Letters\s+(?:Testamentary|of\s+Administration)|Quiet\s+Title|Summary\s+Administration"
    r"|Transfer\s+on\s+Death\s+Deed|Small\s+Estate\s+Affidavit|Heggstad\s+Petition|Court\s+Order"
    r"|(?:Quitclaim|Warranty|Grant|Interspousal|Trustee'?s?)\s+Deed|UPHPA|RESPA|TILA|HECM|FIRPTA|HIPAA"
    r"|Garn[\s\-]St\.?\s*Germain|Due[\s\-]on[\s\-]Sale(?:\s+Clause)?|[A-Z][a-z]{3,}\s+Act)\b", re.I)
_NUM_RE = re.compile(r"(?:\$\s?[\d,]+(?:\.\d+)?|\b\d+(?:\.\d+)?\s?(?:%|percent)|\b\d+\s+(?:day|week|month|year)s?"
                     r"|\b\d{3}[\-.\s]\d{3}[\-.\s]\d{4}\b|\b\d+(?:\.\d+)?\s*(?:k|million|x)\b)", re.I)


def extract_video_urls(raw_text: str) -> list[tuple[str, str]]:
    """Pull every YouTube video id out of pasted text, deduplicated, in input order."""
    found, seen = [], set()
    for m in _URL_RE.finditer(raw_text or ""):
        vid = m.group(1) or m.group(2)
        if vid and vid not in seen:
            seen.add(vid)
            found.append((vid, f"https://www.youtube.com/watch?v={vid}"))
    return found


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


def _win_parts(w) -> tuple[str, int]:
    if isinstance(w, dict):
        secs = w.get("seconds", w.get("start", w.get("offset", 0)))
        return _clean(w.get("text") or w.get("body") or w.get("content")), int(float(secs or 0))
    if isinstance(w, (list, tuple)) and w:
        secs = w[1] if len(w) > 1 and isinstance(w[1], (int, float)) else 0
        return _clean(w[0]), int(float(secs))
    return _clean(w), 0


def _video_windows(video: dict) -> list[tuple[str, int]]:
    try:
        raw = windows(video, target=75)
    except TypeError:  # pragma: no cover - alternate signature
        raw = windows(video)
    return [p for p in (_win_parts(w) for w in (raw or [])) if p[0]]


def _procedure_steps(domain: str) -> list[str]:
    proc = PROCEDURES.get(domain) or PROCEDURES.get("general") or []
    if isinstance(proc, dict):
        proc = proc.get("steps") or proc.get("rules") or [f"{k}: {v}" for k, v in proc.items()]
    out = []
    for step in proc:
        out.append(_clean(" — ".join(str(x) for x in step) if isinstance(step, (list, tuple)) else step))
    return [s for s in out if s]


def _score(text: str) -> int:
    low = text.lower()
    return sum(weight for trig, weight in TRIGGERS.items() if trig in low)


def _category(text: str) -> str:
    low = text.lower()
    for pattern, label in CATEGORIES:
        if re.search(pattern, low):
            return label
    return "Practitioner Note"


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|(?<=—)\s+", _clean(text)) if len(s.strip()) > 25]


def abridge_video(video: dict) -> dict:
    """Condense one corpus video into executive summary, ProTips, finite details and chapters."""
    meta = video.get("metadata") or {}
    length = int(float(meta.get("lengthSeconds") or video.get("length_seconds") or 0))
    domain = video.get("domain") or classify(video)
    full_text = _clean(video.get("full_text"))
    ocr = video.get("client") == "STORYBOARD_OCR" or (video.get("provenance") or {}).get("time_aligned") is False
    source_mode = "STORYBOARD_OCR" if ocr else "caption"
    url = video.get("url") or f"https://www.youtube.com/watch?v={video.get('video_id')}"
    title = _clean(meta.get("title") or video.get("title") or video.get("video_id"))
    author = _clean(meta.get("author") or video.get("author") or "Unknown operator")
    wins = _video_windows(video)

    def locate(seconds: int) -> tuple[str, str]:
        if source_mode == "STORYBOARD_OCR":
            return OCR_STAMP, url
        return stamp(seconds), f"{url}&t={max(int(seconds), 0)}s"

    ranked = sorted(((_score(t), -i, t, s) for i, (t, s) in enumerate(wins)), reverse=True)
    tips, seen = [], set()
    for sc, _, text, secs in ranked:
        if sc <= 0 or len(tips) >= 7:
            break
        key = re.sub(r"[^a-z0-9]", "", text.lower())[:90]
        if key in seen:
            continue
        seen.add(key)
        ts, link = locate(secs)
        tips.append({"category": _category(text), "tip": text[:460], "timestamp": ts,
                     "seconds": 0 if source_mode == "STORYBOARD_OCR" else int(secs),
                     "link": link, "source_type": source_mode})
    low_all = full_text.lower() + " " + title.lower()
    steps = _procedure_steps(domain)
    matched = [s for s in steps if any(tok in low_all for tok in tokens(s))] or steps
    for step in matched[:3]:
        ts, link = locate(0)
        tips.append({"category": "Finite Expert Rule", "tip": step[:460], "timestamp": ts, "seconds": 0,
                     "link": link, "source_type": f"playbook:{domain}"})
    while len(tips) < 6 and wins:
        text, secs = wins[len(tips) % len(wins)]
        ts, link = locate(secs)
        tips.append({"category": "Practitioner Note", "tip": text[:460], "timestamp": ts,
                     "seconds": 0 if source_mode == "STORYBOARD_OCR" else int(secs),
                     "link": link, "source_type": source_mode})
    tips = tips[:10]

    statutes, seen_s = [], set()
    for m in _STATUTE_RE.finditer(full_text + " " + _clean(meta.get("shortDescription"))):
        val = _clean(m.group(0))
        if val.lower() not in seen_s:
            seen_s.add(val.lower())
            statutes.append(val)
    numbers = []
    for sentence in _sentences(full_text):
        if _NUM_RE.search(sentence) and len(numbers) < 6:
            numbers.append(sentence[:300])
    checklist = [s for s in matched[:6]]
    for text, _ in wins:
        if len(checklist) >= 8:
            break
        low = text.lower()
        if any(re.search(rf"\b{v}\b", low) for v in VERBS):
            checklist.append(text[:260])
    details = {"tools_and_portals": mentions(full_text + "\n" + _clean(meta.get("shortDescription"))),
               "statutes_and_forms": statutes[:25],
               "numbers_thresholds_deadlines": numbers,
               "tactical_checklist": checklist[:8] or ["Review the full transcript; no discrete action verbs detected."]}

    chapters, span = [], len(wins)
    count = min(span, 6, max(4, span // 6 or 4))
    for i in range(count):
        chunk = wins[i * span // count:(i + 1) * span // count] or wins[-1:]
        text = " ".join(t for t, _ in chunk)[:420] if chunk else "—"
        ts, link = locate(chunk[0][1] if chunk else 0)
        chapters.append({"title": f"Part {i + 1}", "timestamp": ts, "link": link, "summary": text})

    lead = (wins[0][0][:220] if wins else "no transcript text available")
    summary = " ".join([
        f"{title} is a {DOMAINS[domain][0]} walkthrough from {author}, running {stamp(length)} across {len(tokens(full_text)):,} transcribed words.",
        f"The operator opens by establishing: {lead}.",
        f"Core takeaway: {tips[0]['tip'][:240] if tips else 'see tactical checklist'}.",
        ("Timing is reconstructed from storyboard OCR, so every cue is whole-video rather than second-accurate."
         if source_mode == "STORYBOARD_OCR" else "Every ProTip below is deep-linked to its exact caption timestamp.")])

    out = {"index": video.get("index"), "video_id": video.get("video_id"), "url": url, "title": title,
           "author": author, "length_seconds": length, "duration": stamp(length),
           "word_count": len(tokens(full_text)), "domain": domain, "domain_name": DOMAINS[domain][0],
           "source_mode": source_mode, "executive_summary": summary, "pro_tips": tips,
           "finite_details": details, "chapters": chapters}
    out["markdown"] = _video_markdown(out)
    return out


def _tip_lines(tips: list[dict], label: bool = False) -> str:
    rows = []
    for i, t in enumerate(tips, 1):
        src = f" · {t['video_title']}" if label and t.get("video_title") else ""
        rows.append(f"{i}. **[{t['category']}]** {t['tip']}\n   - Evidence: [{t['timestamp']}]({t['link']}){src}")
    return "\n".join(rows) or "_None extracted._"


def _bullets(items) -> str:
    return "\n".join(f"- {i}" for i in items) or "_None detected._"


def _video_markdown(v: dict) -> str:
    d = v["finite_details"]
    return "\n".join([
        f"## #{v['index']} — {v['title']}", "",
        f"`{v['domain_name']}` · {v['author']} · {v['duration']} · {v['word_count']:,} words · source `{v['source_mode']}` · [watch]({v['url']})",
        "", "### Abridged Version", "", v["executive_summary"], "",
        f"### ProTips ({len(v['pro_tips'])})", "", _tip_lines(v["pro_tips"]), "",
        "### Finite Details", "", "**Tools & portals**", _bullets(d["tools_and_portals"]), "",
        "**Statutes, codes & forms**", _bullets(d["statutes_and_forms"]), "",
        "**Numbers, thresholds & deadlines**", _bullets(d["numbers_thresholds_deadlines"]), "",
        "**Tactical checklist**",
        "\n".join(f"{i}. {s}" for i, s in enumerate(d["tactical_checklist"], 1)), "",
        "### Chapters", "",
        "\n".join(f"- **{c['title']}** — [{c['timestamp']}]({c['link']}) — {c['summary'][:260]}"
                  for c in v["chapters"]), ""])


def combine_videos(abridged_videos: list[dict],
                   custom_title: str = "Combined Multi-Video ProTip & Finite Details Playbook") -> dict:
    """Synthesize 1..N abridged videos into one deduplicated master playbook."""
    vids = list(abridged_videos or [])
    total_words = sum(v.get("word_count", 0) for v in vids)
    total_secs = sum(v.get("length_seconds", 0) for v in vids)
    counts: dict[str, int] = {}
    for v in vids:
        counts[v.get("domain_name", "Unclassified")] = counts.get(v.get("domain_name", "Unclassified"), 0) + 1
    breakdown = [{"domain_name": k, "video_count": n, "share_pct": round(100.0 * n / max(len(vids), 1), 1)}
                 for k, n in sorted(counts.items(), key=lambda kv: -kv[1])]

    master, seen = [], set()
    for v in vids:
        for t in v.get("pro_tips", []):
            key = re.sub(r"[^a-z0-9]", "", t["tip"].lower())[:90]
            if key in seen:
                continue
            seen.add(key)
            master.append({"video_index": v.get("index"), "video_id": v.get("video_id"),
                           "video_title": v.get("title"), "domain_name": v.get("domain_name"),
                           "category": t["category"], "tip": t["tip"], "timestamp": t["timestamp"],
                           "link": t["link"], "score": _score(t["tip"])})
    master.sort(key=lambda t: -t["score"])

    def merge(key):
        out, seen_v = [], set()
        for v in vids:
            for item in v.get("finite_details", {}).get(key, []):
                low = re.sub(r"\s+", " ", str(item).lower())[:140]
                if low not in seen_v:
                    seen_v.add(low)
                    out.append(item)
        return out

    workflow = merge("tactical_checklist")
    merged = {"tools_and_portals": merge("tools_and_portals"), "statutes_and_forms": merge("statutes_and_forms"),
              "numbers_thresholds_deadlines": merge("numbers_thresholds_deadlines"),
              "unified_workflow_steps": workflow[:40]}
    compact = [{"index": v.get("index"), "video_id": v.get("video_id"), "title": v.get("title"),
                "domain_name": v.get("domain_name"), "duration": v.get("duration"),
                "word_count": v.get("word_count"), "pro_tip_count": len(v.get("pro_tips", [])),
                "source_mode": v.get("source_mode"), "url": v.get("url")} for v in vids]
    out = {"title": custom_title, "video_count": len(vids), "total_words": total_words,
           "total_duration_hours": round(total_secs / 3600.0, 2),
           "total_pro_tips": sum(len(v.get("pro_tips", [])) for v in vids),
           "domain_breakdown": breakdown, "master_pro_tips": master[:120],
           "master_finite_details": merged, "videos": compact}
    out["markdown"] = "\n".join([
        f"# {custom_title}", "", "## Executive Telemetry", "",
        f"- Videos combined: **{out['video_count']}**",
        f"- Transcribed words: **{total_words:,}**",
        f"- Runtime: **{out['total_duration_hours']} h**",
        f"- ProTips extracted: **{out['total_pro_tips']}** (deduplicated to {len(out['master_pro_tips'])})",
        f"- Domains: " + (", ".join(f"{b['domain_name']} ({b['video_count']})" for b in breakdown) or "n/a"), "",
        "## Master ProTips Vault", "", _tip_lines(out["master_pro_tips"], label=True), "",
        "## Master Finite Details Ledger", "", "### Tools & Portals", _bullets(merged["tools_and_portals"]), "",
        "### Statutes, Codes & Forms", _bullets(merged["statutes_and_forms"]), "",
        "### Numbers, Thresholds & Deadlines", _bullets(merged["numbers_thresholds_deadlines"]), "",
        "## Unified Step-by-Step Workflow", "",
        "\n".join(f"{i}. {s}" for i, s in enumerate(merged["unified_workflow_steps"], 1)) or "_None._", "",
        "## Per-Video Abridged Digests", "",
        "\n\n".join(v.get("markdown", "") for v in vids)])
    return out


def build_custom_agent_report(all_videos: list[dict] | None = None,
                              abridged_map: dict[str, dict] | None = None, prompt: str = "",
                              selected_video_ids: list[str] | None = None,
                              index: EvidenceIndex | None = None, *, records=None,
                              video_ids: list[str] | None = None, max_passages=18) -> dict:
    """Rank the corpus against a free-form prompt and emit a custom Agent Operational Report."""
    if isinstance(all_videos, str) and records is not None:
        prompt = all_videos
    pool = list(records if records is not None else (all_videos or []))
    abridged_map = abridged_map or {}
    selected_video_ids = video_ids if video_ids is not None else selected_video_ids
    if selected_video_ids is not None:
        wanted = set(selected_video_ids)
        pool = [v for v in pool if v.get("video_id") in wanted]
    terms = [t for t in tokens(prompt or "") if len(t) > 2]

    def rank(video: dict) -> int:
        if not terms:
            return 1
        hay = (_clean(video.get("full_text")) + " " + _clean((video.get("metadata") or {}).get("title"))).lower()
        return sum(hay.count(t) for t in terms)

    scored = sorted(((rank(v), v) for v in pool), key=lambda p: -p[0])
    matched = [v for sc, v in scored if sc > 0] or [v for _, v in scored]
    matched = matched[:60] if terms else matched

    abridged = []
    for v in matched:
        vid = v.get("video_id")
        abridged.append(abridged_map.get(vid) or abridge_video(v))
    combined = combine_videos(abridged, custom_title="Custom Agent Operational Report")

    passages = []
    by_id = {a['video_id']: a for a in abridged}

    def passage(a, text, secs, score, matched_terms):
        ocr = a['source_mode'] == 'STORYBOARD_OCR'
        return {'video_id': a['video_id'], 'index': a['index'], 'title': a['title'],
                'url': a['url'], 'domain': a['domain'], 'domain_name': a['domain_name'],
                'start': 0 if ocr else secs, 'timestamp': OCR_STAMP if ocr else stamp(secs),
                'timestamp_url': a['url'] if ocr else f"{a['url']}&t={int(secs)}s",
                'score': score, 'matched_terms': list(matched_terms), 'excerpt': text[:400]}

    if index is not None and terms:
        for hit in index.search(prompt, top_k=max_passages, allowed_video_ids=set(by_id)):
            a = by_id.get(hit['video']['video_id'])
            if a is not None:
                passages.append(passage(a, hit['text'], hit['start'], hit['score'], hit['matched_terms']))
    if not passages:
        for a, v in zip(abridged, matched):
            for text, secs in _video_windows(v):
                overlap = [t for t in terms if t in text.lower()]
                hits = sum(text.lower().count(t) for t in terms)
                if hits or not terms:
                    passages.append(passage(a, text, secs, hits, overlap))
        passages.sort(key=lambda p: -p['score'])
    passages = passages[:max_passages]

    procs, seen_d = [], set()
    for a in abridged:
        if a["domain"] not in seen_d:
            seen_d.add(a["domain"])
            procs.append({"domain": a["domain"], "domain_name": a["domain_name"],
                          "steps": _procedure_steps(a["domain"])})
    telemetry = {"videos_scanned": len(pool), "videos_matched": len(matched),
                 "total_words": combined["total_words"], "runtime_hours": combined["total_duration_hours"],
                 "pro_tips": len(combined["master_pro_tips"]), "evidence_passages": len(passages),
                 "domains": combined["domain_breakdown"],
                 "storyboard_only": sum(1 for a in abridged if a["source_mode"] == "STORYBOARD_OCR")}
    subtitle = (f"Prompt-matched intelligence across {len(matched)} of {len(pool)} selected videos"
                if terms else f"Full sweep across {len(matched)} selected videos")
    out = {"title": "Agent Operational Report", "subtitle": subtitle, "prompt": prompt or "(all selected videos)",
           "matched_video_count": len(matched), "total_pro_tips": len(combined["master_pro_tips"]),
           "telemetry": telemetry, "pro_tips": combined["master_pro_tips"],
           "finite_details": combined["master_finite_details"], "evidence_passages": passages,
           "procedures": procs, "videos": combined["videos"]}
    fd = out["finite_details"]
    out["markdown"] = "\n".join([
        "# Agent Operational Report", "", f"_{subtitle}_", "", f"**Prompt:** {out['prompt']}", "",
        "## Executive Telemetry", "",
        f"- Videos scanned: **{telemetry['videos_scanned']}** · matched: **{telemetry['videos_matched']}**",
        f"- Words analyzed: **{telemetry['total_words']:,}** · runtime: **{telemetry['runtime_hours']} h**",
        f"- ProTips: **{telemetry['pro_tips']}** · evidence passages: **{telemetry['evidence_passages']}**",
        f"- Storyboard-OCR sourced videos: **{telemetry['storyboard_only']}**", "",
        "## Master ProTips Vault", "", _tip_lines(out["pro_tips"], label=True), "",
        "## Master Finite Details Ledger", "", "### Tools & Portals", _bullets(fd["tools_and_portals"]), "",
        "### Statutes, Codes & Forms", _bullets(fd["statutes_and_forms"]), "",
        "### Numbers, Thresholds & Deadlines", _bullets(fd["numbers_thresholds_deadlines"]), "",
        "## Unified Step-by-Step Workflow", "",
        "\n".join(f"{i}. {s}" for i, s in enumerate(fd["unified_workflow_steps"], 1)) or "_None._", "",
        "## Playbook Procedures", "",
        "\n".join(f"**{p['domain_name']}**\n" + _bullets(p["steps"]) for p in procs) or "_None._", "",
        "## Evidence Passages", "",
        "\n".join(f"- **#{p['index']} {p['title']}** — [{p['timestamp']}]({p['timestamp_url']}) — {p['excerpt']}"
                  for p in passages) or "_None._", "",
        "## Per-Video Abridged Digests", "",
        "\n\n".join(a.get("markdown", "") for a in abridged)])
    return out
