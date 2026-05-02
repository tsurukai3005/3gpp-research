---
name: render-tex-slides
description: Render a research note (documents/<note>.md) into Beamer/Metropolis slides and build the PDF via latexmk. 研究ノートから Beamer/Metropolis スライドを生成し latexmk で PDF までビルド。
user-invocable: true
---

# render-tex-slides

## Motivation

Convert the output of `/build-presentation` Phase 4 (Markdown shaped as
`## Slide N: <headline>`) into TeX/Beamer + PDF in **a way that coexists with manual edits**.

Whereas the PPTX pipeline ([`tools/pptx/build_slides.py`](../../../tools/pptx/build_slides.py))
performs a deterministic transform from a structured spec JSON to pptx, this skill
prioritizes **keeping LaTeX flexibility while ensuring re-runs do not overwrite hand-edited slides**.

The two pipelines are completely separated by output location, template, and preset namespace:

| Pipeline | Templates | Output | Skill / tool |
|:---|:---|:---|:---|
| TeX | `framework/templates/slide-tex/` | `slides/tex/<yymmdd>_<slug>/` | `/render-tex-slides` (this skill) |
| PPTX | `tools/pptx/styles/` `tools/pptx/styles-meta/` | `slides/pptx/<title>.pptx` | `tools/pptx/build_slides.py` |

## Usage

```
/render-tex-slides <documents/path.md>
/render-tex-slides <documents/path.md> --preset <name>
/render-tex-slides <documents/path.md> --slide <id|N>
/render-tex-slides <documents/path.md> --no-build
/render-tex-slides <documents/path.md> --dry-run
/render-tex-slides <documents/path.md> --rebuild-manifest
```

| Flag | Default | Use |
|:---|:---|:---|
| `--preset <name>` | `tex.ja-aspect43-9pt` | Preset selector. The value matches `name` in `framework/templates/slide-tex/presets/*.yaml` |
| `--slide <id\|N>` | — | Re-render a single slide. `id` is the stem of `parts/<id>.tex`; `N` is the 1-origin index in the manifest |
| `--no-build` | False | Suppress automatic `latexmk`. Generate only |
| `--dry-run` | False | Print to chat what would change; do not touch files |
| `--rebuild-manifest` | False | Discard the existing `manifest.yaml` and regenerate. Slides with `source: manual` are re-listed as protected |

## Inputs and prerequisites

- **Required input**: `documents/<note>.md`. The output of `/build-presentation` Phase 4, or an equivalently-shaped note (see §"Source-note read spec" below)
- **Environment prerequisites**: `lualatex --version` and `latexmk --version` must be runnable on PATH. Details: [`framework/tools.md`](../../../framework/tools.md) §"3. lualatex / latexmk"
- **Templates**: [`framework/templates/slide-tex/`](../../../framework/templates/slide-tex/) must exist (bundled in the repo)
- **Cannot proceed when**:
  - Source has zero `## Slide N: <headline>` sections → fail and redirect to `/build-presentation --phase 4`
  - `lualatex` is not found → quote the install steps from `framework/tools.md` and stop

## Execution flow

### 1. Environment prerequisite check

1. Run `lualatex --version` and `latexmk --version` via Bash. Treat any output to stderr/stdout as success
2. On failure, quote a single block from the relevant section of `framework/tools.md` to chat and stop here

### 2. Decide the output directory

Derive the output location from the source note path:

- Source: `documents/<yymmdd>_<slug>.md`
- Output: `slides/tex/<yymmdd>_<slug>/`
  - `<yymmdd>` is the last two digits of year + month + day from the source frontmatter `created` (YYYY-MM-DD)
  - `<slug>` is what remains after stripping `<yymmdd>_` and the extension from the source filename
- Reuse an existing directory; otherwise create it

### 3. Expand the skeleton (only on first run or with --rebuild-manifest)

Copy [`framework/templates/slide-tex/skeleton/`](../../../framework/templates/slide-tex/skeleton/) to the output directory:

- `main.tex.template` → `<output>/main.tex` (placeholders left unsubstituted; later steps Edit them)
- `latexmkrc` → `<output>/latexmkrc` (as-is)
- `.gitignore` → `<output>/.gitignore` (as-is)
- Create `<output>/parts/` and `<output>/figures/` directories

### 4. Read and parse the source note

Read `documents/<note>.md` end-to-end and interpret in this order:

1. **frontmatter**: extract `title`, `audience`, `takeaway`, `duration_min`, `source_notes`, `venue`, `format`
2. **Split body by `## Slide N: <headline>`**. Extract N and headline
3. Optional meta sections inside each slide:
   - `### 視覚コンテンツ` → image references (`![alt](path)`) and figure caption
   - `### 原稿` (may include an estimated-time note) → speaker script. Aggregate into `<output>/原稿.md`
   - `### 補足` → transitions, anticipated Q&A, notes. Merge into the speaker script
   - `### スライド種別` → explicit `type:` (takes precedence when present)
4. **Body**: extract text, bullet lists, and Markdown tables
5. **Images**: convert `![alt](path)` to `\includegraphics[width=<width>\linewidth]{<basename>}`. Normalize the path to a relative reference under `<output>/figures/`. Even if the file is missing, only warn (do not fail the build)

### 5. Decide the slide type

If `### スライド種別` is explicit, use it. Otherwise auto-detect with this priority:

| Condition | Template |
|:---|:---|
| Slide 1 | `title` |
| headline contains 「目次」 or 「Agenda」 | `agenda` |
| Body contains a Markdown table (`\| ... \| ... \|` header + alignment row) | `table` |
| Image references only and body ≤ 50 chars | `image-with-caption` |
| `\begin{equation}`-style math dominates (≥ 50% of body lines are math) | `equation-focus` |
| `### 左 \| ### 右` or explicit `\|\|\|` separator | `two-column` |
| Last slide with headline 「Q&A」 or 「Thank you」 | `qa` |
| Otherwise | `plain` |

### 6. Generate / reconcile manifest.yaml

Branch on whether `<output>/manifest.yaml` exists:

- **Missing, or `--rebuild-manifest`** → generate a manifest listing every source slide with `source: generated`
- **Existing** → read it; if the source has changed in the count or order of `## Slide N`, update by these rules:
  - id present in manifest but missing from source → deletion candidate. Confirm in chat before removing (`--dry-run` only warns)
  - id present in source but missing from manifest → append at the end with `source: generated`
  - Order changes are treated as user actions; the manifest takes precedence

manifest `source` values:

| Value | Behavior |
|:---|:---|
| `generated` | Overwrite `parts/<id>.tex` from the source note on every run |
| `manual` | Skill never overwrites. `from_section` is also ignored |
| `frozen` | Keep the existing `parts/<id>.tex`. Do not regenerate even if the source updates. Record the freeze date in `frozen_at:` |

Minimum manifest schema:

```yaml
preset: tex.ja-aspect43-9pt
metadata:
  title: "発表タイトル"
  subtitle: ""
  author: "発表者氏名"
  institute: "所属"
  date: "2026-05-15"
slides:
  - id: 01_title
    source: generated
    type: title
    from_section: null
  - id: 02_agenda
    source: generated
    type: agenda
    from_section: "## Slide 2: 目次"
  - id: 03_<headline-slug>
    source: generated
    type: plain
    from_section: "## Slide 3: ..."
```

`id` follows `<NN>_<headline_slug>` (NN is two-digit zero-padded; headline_slug is an ASCII-ified headline or a sequence number). Slides with `source: manual` may use `from_section: null`.

### 7. Generate parts/<id>.tex

For each manifest entry **only when `source: generated`**:

1. Read `framework/templates/slide-tex/slide-parts/<type>.tex.template`
2. Parse the body of the matching `from_section` and fill the `<<NAME>>` placeholders
3. Write to `<output>/parts/<id>.tex`

Slides with `source: manual` / `source: frozen` must **never be rewritten** (do not even Read the file — root-cause prevention of accidental overwrite).

#### Table conversion (`type: table`)

Convert source Markdown tables to booktabs by these rules:

| Markdown | LaTeX |
|:---|:---|
| `:---` | `l` (left aligned) |
| `---:` | `r` (right aligned) |
| `:---:` | `c` (centered) |
| `**text**` | `\textbf{text}` |
| `*text*` | `\emph{text}` |
| `` `code` `` | `\texttt{code}` |
| Escaped `\|` | `|` |

Example:

```markdown
| 手法 | 性能 | 備考 |
|:---|---:|:---:|
| MMSE | 1.40 | 従来 |
| DU-MMSE | **1.61** | 提案 |
```

→ after template expansion:

```latex
\begin{frame}{<headline>}
\centering
\begin{tabular}{lrc}
\toprule
手法 & 性能 & 備考 \\
\midrule
MMSE & 1.40 & 従来 \\
DU-MMSE & \textbf{1.61} & 提案 \\
\bottomrule
\end{tabular}
\end{frame}
```

### 8. Assemble main.tex

Update the skeleton's `main.tex` as follows:

- Read `skeleton.*` from the preset YAML and substitute `<<ASPECT_RATIO>>` `<<BASE_FONT_SIZE>>` `<<JA_FONT_PRESET>>` `<<LATIN_SANS_FONT>>` `<<LATIN_MONO_FONT>>`
- Substitute `<<TITLE>>` `<<SUBTITLE>>` `<<AUTHOR>>` `<<INSTITUTE>>` `<<DATE>>` from `manifest.yaml.metadata`
- Expand `<<SLIDE_INPUTS>>` into `\input{parts/<id>}` lines, one per slide, in manifest order

### 9. Automatic build

When `--no-build` is not given, run inside the output directory:

```bash
cd <output>
latexmk -lualatex -interaction=nonstopmode -halt-on-error -file-line-error
```

- On success: report the absolute path of the produced PDF in chat as a single line (`<output>/main.pdf`)
- On failure: extract the first `! ` line from the build log (`.latex-cache/main.log`) plus 3 lines of context, and present it. Do not present the full log
- In either case, files under `.latex-cache/` are git-untracked (covered by the bundled `.gitignore`)

### 10. Report

Present the following as a single block in chat:

```
出力先: slides/tex/<yymmdd>_<slug>/
manifest: <変更なし | 新規生成 | N 件追加 / M 件更新>
parts: <X 件 generated / Y 件 manual 保護 / Z 件 frozen 保護>
ビルド: <成功: <絶対パス> | 失敗: <抽出ログ> | 抑制(--no-build)>
画像未配置警告: [<相対パス>, ...] （無ければ省略）
```

## Output

- **Format**: a set of files (chat receives only the report)
- **Save location**: directly under `slides/tex/<yymmdd>_<slug>/`
  - `main.tex`, `latexmkrc`, `.gitignore`, `manifest.yaml`, `parts/*.tex`, `figures/` (may be empty), `原稿.md` (optional)
  - `main.pdf` is **git-untracked** (excluded by `.gitignore`)
- **frontmatter**: the output files are `.tex` / `.yaml` so Obsidian frontmatter is not needed. The source note's frontmatter is not modified

## Skill-specific notes

1. **manifest.yaml is the single source of truth**. Never overwrite `source: manual` / `frozen`. Regeneration, reordering, and insertion all go through the manifest
2. **Placeholders are fixed to `<<NAME>>`**. Mustache is rejected because it collides with brace `{}` in the body
3. **Protect hand-written slides**: only Read-then-rewrite `parts/<id>.tex` when `source: generated`. For `manual` / `frozen`, do not even Read it (root-cause prevention of accidental overwrite)
4. **Do not stop because images are missing**: failure to resolve `\graphicspath{{figures/}}` is a warning. The presenter places the figures locally and rebuilds
5. **Do not mix with the PPTX pipeline**: output location, templates, presets, and skill names are all separated. When PPTX is needed, invoke `tools/pptx/build_slides.py` after Phase 4 of `/build-presentation`
6. **Do not skip the thinking process**: when the source note lacks `## Slide N` structure, run `/build-presentation --phase 4` first instead of this skill
7. **`/review` scope**: this skill and its templates are in scope for `/review`. Generated artifacts under `slides/tex/**` are out of scope

## Related skills

- Upstream: [`/build-presentation`](../build-presentation/SKILL.md) — generate the source note (`## Slide N` structure) in Phase 4
- Parallel: `tools/pptx/build_slides.py` — alternative path when an equivalent PPTX output is required
- Reference: [`framework/templates/slide-tex/README.md`](../../../framework/templates/slide-tex/README.md) — template and placeholder conventions
- Reference: [`framework/tools.md`](../../../framework/tools.md) — install steps for `lualatex` / `latexmk` / fonts