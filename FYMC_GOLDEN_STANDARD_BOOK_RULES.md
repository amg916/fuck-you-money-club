# THE BIG MONEY PLAYBOOKS — GOLDEN STANDARD BOOK RULES (VOLUMES 001–049)

> **Publisher:** The Fuck You Money Club · **Series:** *The Big Money Playbooks*
> **Governing Mandate:** Zero AI inner-looking/personal knowledge, zero code-generated prose, 100% Claude Opus authoring strictly from full verbatim English YouTube practitioner transcripts.

---

## 1. Zero Inner-Looking / Personal AI Knowledge & Zero Code-Written Prose
- **100% Claude Opus Authoring:** Every chapter (`volNNN_q01.py`..`volNNN_q12.py`), diagram specification (`volNNN_diagrams.py`), companion workbook (`volNNN_workbook.py`), and UI summary (`volNNN_ui.json`) is authored by **Claude Opus** reading the **full, unedited, word-for-word timestamped YouTube transcripts** directly via `stdin`.
- **Data Plumbing Only for Code:** Python scripts are strictly limited to transcript harvesting, English-language filtering, closed-world `VIDEO_ID`/timestamp verification, and deterministic rendering into PDF, EPUB 3.0, SVG, and Bundle ZIPs.
- **Closed-World Lock:** Neither Antigravity nor Claude may reach into internal AI memory, deduce unstated steps, invent financial figures/benchmarks, or pull outside `.gov` / `U.S.C.` / `CFR` statutes. Laws, regulations, software tools, conversion rates, or dollar amounts appear **only** when a practitioner literally states them in the transcript, attributed directly to that speaker and timestamp.

## 2. Zero Censorship, Preaching, or White-Hat Lecturing
- Report grey-hat, unconventional, and aggressive street-level tactics (CTR/IP click networks, parasite SEO, skip-tracing angles, buying-group float, presale ticket setups, surplus recovery outreach, etc.) **unfiltered and accurately as practitioners teach and test them**, paired honestly with any failures, reversals, or pushback other practitioners report.
- Hard-ban preachy AI disclaimers and filler (`"not legal advice"`, `"not financial advice"`, `"unproven hypothesis"`, `"consult an attorney"`, `"not a guarantee"`, `"compliance gate"`, `"approval gate"`).

## 3. Corpus Quality Gate Before Writing (`192` Strictly English Practitioner Videos per Book)
- Every volume (`001`–`049`) is backed by a verified corpus of **`192` distinct, 100%-English (`en*`) YouTube practitioner transcripts** (`>= 200` spoken words and valid caption timestamps each), partitioned **bijectively (`16` unique transcripts per chapter across `Q01–Q12`, zero duplicates, zero omissions)**.
- Non-English caption tracks and off-topic/short noise clips are purged before planning. If any video is swapped during pre-flight, the chapter's title and subtitle are regenerated *after* the swap so headings never promise a sub-topic absent from the chapter's `16` transcripts.

## 4. Bottom-Up Chapter Architecture (Built Around What Practitioners Actually Teach)
- Before writing a book, Claude reads the `192`-video catalog for that volume and groups the `192` videos (`16` per chapter) around the **12 real operational pillars** taught by those practitioners—ensuring street-specific sub-tactics receive dedicated chapters rather than getting buried in generic templates.

## 5. "Consensus First, Then Street Mechanics, Then Disagreements" Chapter Structure
Every chapter's `4` deep sections synthesize the `16` transcripts into crisp operator intelligence:
1. **The Practitioner Consensus:** What multiple independent operators agree works and why.
2. **Exact Street Mechanics, Tools & Numbers:** Step-by-step setups, software, scripts, pricing, conversion rates, and unit economics reported by the speakers.
3. **Where Practitioners Disagree (Real Tradeoffs):** Side-by-side comparison where operators contradict each other on methods, costs, or sustainability.
4. **Firsthand Failure Modes & Warnings:** Real mistakes, reversals, account bans, or losses experienced firsthand by the speakers.

## 6. Zero "Fourth-Wall / Meta-Transcript" Academic Language
- Never break the fourth wall with phrases such as *"in the supplied transcript"*, *"this corpus does not contain"*, *"the chapter preserves"*, *"the heading organizes"*, or *"in the provided recording"*.
- Write directly as an authoritative operator field dossier reporting what named practitioners demonstrated, measured, and argued. Simply omit sub-topics nobody in the `192` transcripts covered rather than writing meta-commentary about missing transcript coverage.

## 7. 100% Machine-Verified `[Channel — VIDEO_ID @ HH:MM:SS]` Traceability (Zero Blank Cells)
- **Body Paragraphs:** Every paragraph in `sections[].paragraphs` cites `2–4` specific speakers with `[VIDEO_ID @ HH:MM:SS]`.
- **Data Tables:** Every table (`4` per chapter) ends with an `Expert Source` column, and every row cites `Channel ([VIDEO_ID @ HH:MM:SS])` with zero `"TBD"`, `"Unknown"`, or `"N/A"` placeholders.
- **Key Metrics:** Every `key_metrics` entry populates `label`/`metric`, `value`, `confidence` (`"attributed_practitioner_claim"`), `context`, and `source` (`"Channel [VIDEO_ID @ HH:MM:SS]"`) so both PDF cards and Markdown tables render with **zero blank cells**.
- **SOPs, Callouts, Checklists & Workbooks:** Every `sop_steps` item (`4/ch`), `INSIDER PRO-TIPS` item (`4/ch`), `OPERATOR GATE` item (`4/ch`), `action_checklist` item (`6/ch`), and Companion Workbook field example (`60/book`) cites a verified corpus `VIDEO_ID` + timestamp within that video's actual runtime.
- **Clickable Deep Links:** Every chapter includes `3–4` anchor video deep links in `statutory_citations` and `16+` unique `https://www.youtube.com/watch?v=<VIDEO_ID>&t=<SEC>s` deep links in `source_citations` (`192+` per book).

## 8. Uniform `10/10` Production Density, Visuals & Workbook Floor
- **Chapters (`12/book`):** `2,100–2,650` prose words/chapter (`~60,000–66,000+` total words/book), `4` data tables/chapter (`>= 6.0` avg words/cell), `4`-step `SOP`, `4` `INSIDER PRO-TIPS`, `4` `OPERATOR GATE` checks, `1` attributed `Pull Quote`, and `6` `Action Checklist` items.
- **Diagrams (`8/book`):** `diag_01`–`diag_08` rendered and SVG-validated across Concepts A, B, and C using strictly practitioner-reported stages and figures.
- **Companion Workbook (`6` worksheets / `60` fields / `>= 5,500` words):** Printable execution worksheets whose `60` worked examples trace `100%` to real practitioner cases from the book.
- **Retail & Typography Hygiene:** Zero `™`/`®` symbols, zero `NaN`/`undefined`/`i.ytimg.com` artifacts, and spoken profanity sanitized to `[expletive]` inside body text so retail PDF gates pass cleanly.

## 9. Automated Hard-Gate Rejection Before Landing
- Every authored module must pass automated AST + Closed-World Verification (`100%` attribution across paragraphs, tables, callouts, and workbook fields; `0` outside `.gov`/`U.S.C.`/`CFR` strings; `0` fourth-wall meta-phrases; `100%` valid video duration bounds; SVG validation; PDF/EPUB/ZIP export checks; and `run_full_qa_suite` `overall_pass=True`) before landing in `src/fymc/` and `publishing/`.

## 10. Numerical Wave Rollout & End-to-End Verification (`Vol. 001` – `Vol. 049`)
- Execute across `8` numerical waves of `6` volumes each (`W1: 001–006`, `W2: 007–009 & 011–013`, `W3: 014–019`, `W4: 020–025`, `W5: 026–031`, `W6: 032–037`, `W7: 038–043`, `W8: 044–049`) plus `Vol. 010` Golden-Standard retro-polish (Rules 6 & 7), committing and verifying `.commit_manifest.json` (`887` files) after each wave, followed by full `unittest`, **Codex Astra 6** `TECHNICAL PASS`, and **Codex Luna 6.0** `LIVE BROWSER PASS`.
