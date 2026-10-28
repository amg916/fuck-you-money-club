# YouTube Transcript Corpus & Reports

Completed corpus and deterministic report builders for the 189 ordered videos in
`urls.txt`. The tools use only the Python 3.9+ standard library: no pip
installation, API key, external model, or third-party runtime is required.

## Completed corpus

- **189/189 records have status `ok`.**
- **186 XML caption tracks + 3 storyboard/description reconstructions.**
- **814,088 words** across the corpus.
- **79.95 hours** of video duration.

The three reconstructions are user-supplied storyboard/description summaries,
not verbatim captions or independently re-OCRed transcripts. They are explicitly
marked `client: STORYBOARD_OCR`, with provenance identifying them as non-verbatim
and not time-aligned. Each uses one whole-video coverage segment; its start time
is not a quote timestamp. `ok` therefore means usable corpus text, not that all
189 videos have caption tracks.

## Generated reports

- [ADVANCED_AGENT_HOW_TO_REPORT.md](ADVANCED_AGENT_HOW_TO_REPORT.md): an
  eight-domain operational manual with corpus evidence, procedures, decision
  matrices, a tool/portal/database candidate directory, and a complete source
  register.
- [VIDEO_BY_VIDEO_COMPENDIUM.md](VIDEO_BY_VIDEO_COMPENDIUM.md): individual video
  analyses in original corpus order, with metadata, domain classification,
  extractive passages, and source references. Reconstruction passages are
  distinguished from timestamped caption evidence.

The reports are deterministic local synthesis, not external-model output.
Heuristic domain assignments and tool mentions are research aids, not evidence
of endorsement or independently verified current legal/API behavior.

## Report builders

- `src/build_agent_report.py` validates and loads the corpus, indexes evidence,
  and generates both reports. By default it also repairs known reconstruction
  records in the existing corpus before building.
- `src/report_playbook.py` supplies the editorial operational procedures used by
  the agent report builder; corpus matching attaches citations. It is a supporting
  module, not a separate command-line builder.
- `src/build_compendium.py` is a standalone extractive compendium builder with
  heuristic domain classification, metadata, ranked passages, and a table of
  contents. It validates manifest/record identities before writing its output.

From the repository root, rebuild both reports from the completed corpus without
repairing or modifying the source data:

```sh
python3 src/build_agent_report.py --no-repair
```

Options: `--data PATH` selects the corpus directory; `--output PATH` selects the
output directory for both Markdown reports. Omit `--no-repair` to enable the
known-record repair step.

To build only the standalone compendium:

```sh
python3 src/build_compendium.py
```

Its `--data PATH` selects the corpus directory and `--output PATH` selects the
output **file** (default: `VIDEO_BY_VIDEO_COMPENDIUM.md`). The standalone builder
and the combined report builder use different compendium renderers and overwrite
the same default destination; choose the builder for the desired presentation.
Default paths resolve relative to the repository, regardless of working directory.

## Fetcher

`src/fetch_transcripts.py` retrieves metadata and captions.
`src/storyboard_fallbacks.py` holds the three known user-supplied reconstructions
and applies their explicit provenance and whole-video timing markers. Real
captions take precedence; unknown videos and network failures do not receive
invented fallback text.

The completed corpus is already in `data/`; fetching again is not required to
build the reports. To refetch all videos:

```sh
python3 src/fetch_transcripts.py
```

Optional arguments: `--urls PATH`, `--output PATH`, `--attempts 5`, `--timeout 30`,
and `--interval 0.3` (global minimum request spacing in seconds). Eight worker
threads share request pacing and retry cooldown. Transient HTTP 429/5xx and
connection errors receive up to five attempts with exponential backoff, jitter,
and Retry-After support. This reduces rate-limit pressure but cannot guarantee
that YouTube will not block or throttle requests.

Each video tries the IOS client first, then ANDROID if the first client cannot
provide a usable transcript. The fetcher preserves available videoDetails and
captionTracks, prefers manual English captions over automatic English, and falls
back to another language only when no English track is available. Both standard
transcript XML and timedtext format 3 are supported. Caption timestamps and
durations are stored in seconds; text is HTML-unescaped and whitespace-normalized.

### Corpus files and statuses

- `data/transcripts/001_<video_id>.json` through `189_<video_id>.json`: metadata,
  caption tracks, selected track, segments, full text, retrieval diagnostics,
  and reconstruction provenance where applicable.
- Matching `.txt` files contain the clean full text. Unresolved results have
  empty text files, not invented transcript text.
- `data/index.json`: ordered per-video metadata and status, paths, segment/word
  counts, and aggregate counts, written after all results have been saved.

Possible statuses are `ok`, `no_captions` (playable without caption tracks and
without an applicable reconstruction), `unavailable` (neither client reported
playable video or tracks), and `error` (network, parsing, empty-caption, or other
retrieval failure). Client diagnostics distinguish underlying causes; a blocked
client is not proof that a video has been deleted.

Files are replaced atomically individually. A fetch rerun retrieves every URL
again and replaces its outputs; it does not resume or reuse cached successes.
Run only one fetch process per output directory. A filesystem failure aborts the
process rather than falsely reporting a saved output. Exit status is zero only
when every URL has usable corpus text; otherwise it is one. A nonzero exit still
leaves diagnostic files for processed videos, barring a filesystem/process failure.

## Unit tests and verification

The **32-test unit test suite** spans `tests/test_fetch_transcripts.py`,
`tests/test_build_agent_report.py`, and `tests/test_build_compendium.py`. Run it
from the repository root:

```sh
python3 -m unittest discover -s tests -v
```

Coverage includes URL count/uniqueness, both XML formats, normalization, timestamp
validation, track preference, client fallback, metadata, empty captions, HTTP
retries and permanent failures, manifest/error artifacts, reconstruction
provenance and precedence, safe/idempotent corpus repair, all 189 nonempty
records, report completeness and determinism, evidence consumption, domain
classification, and reconstruction handling without fabricated quote timestamps.
Network behavior is tested using mock transport; report tests also exercise the
local completed corpus.

After any refetch, verify `total == processed == 189`, `counts.ok == 189`, and
status counts summing to 189 in `data/index.json`. Every listed JSON/TXT file
must exist, and every `ok` record must have nonempty segments and full text.
Recheck source types, word totals, and duration against the completed-corpus
figures above if upstream captions or metadata change.
