---
name: trace-evolution
description: From a natural-language topic phrase, follow the RAN1 discussion trajectory across meetings and write the cross-meeting timeline under documents/. 自然言語トピックから RAN1 議論変遷を会合横断で追跡し documents/ にタイムライン生成。
user-invocable: true
---

# trace-evolution

## Motivation

For a specific topic (e.g. CSI compression, Type-II codebook, 6GR PDCCH),
**"when, in which meeting, who claimed what, and what was agreed"** can only be
followed vertically. Reading individual Tdocs / Chair Notes side-by-side per meeting does not surface this.

This skill skewers [`framework/catalog/`](../../../framework/catalog/) and the existing
`references/` Chair Notes across meetings to draw **the cross-meeting genealogy of the discussion** as Markdown.

Why we choose **structured metadata + Markdown→Markdown extraction** over embedding search:

- Discussion continuity can be tracked through structural information: AI-number genealogy, FL nominations, revision pointers, etc.
- Being able to wikilink back to source Tdoc / Chair Notes is more useful for SEP exploration
- For missing source material, **"reporting the gap"** is more valuable than emitting a hallucinated summary

## Usage

```
/trace-evolution <natural-language topic phrase>
/trace-evolution <natural-language topic phrase> --meetings RAN1#124,RAN1#124bis,RAN1#125
/trace-evolution --ai-id <stable AI ID>
/trace-evolution <topic phrase> --from RAN1#123 --to RAN1#125
```

Examples:

- `/trace-evolution CSI 圧縮`
- `/trace-evolution type-II codebook`
- `/trace-evolution 6GR の DL 制御チャネル --meetings RAN1#124bis,RAN1#125`
- `/trace-evolution --ai-id ai_6gr_mimo_dl_pdcck`

## Inputs and prerequisites

- **Required input**: one of
  - A natural-language topic phrase (fuzzy-matched against `aliases` in agenda-items.yaml)
  - `--ai-id <stable ID>` (specify the agenda-items.yaml key directly)
- **Optional**:
  - `--meetings`: comma-separated meeting filter
  - `--from <meeting>` / `--to <meeting>`: range filter
  - `--persona <persona-file>`: evaluate from a persona's perspective
- **Prerequisites**:
  - [`framework/catalog/meetings.yaml`](../../../framework/catalog/meetings.yaml) must exist
  - [`framework/catalog/agenda-items.yaml`](../../../framework/catalog/agenda-items.yaml) must exist
- **Cannot proceed when**: the topic does not match any catalog `aliases` and the user provides no clarification

## Execution flow

### Phase A: topic resolution (natural language → stable AI ID)

1. Read [`framework/skill-contract.md`](../../../framework/skill-contract.md) and [`framework/principles.md`](../../../framework/principles.md), and confirm Global Will / Will Not
2. Read [`framework/catalog/agenda-items.yaml`](../../../framework/catalog/agenda-items.yaml) and fuzzy-match the input topic phrase against:
   - every `aliases` entry
   - the major terms in `title`
3. Branch on match count:
   - **0 hits**: present candidates and ask the user for the closest stable ID. Also propose `aliases` additions to `agenda-items.yaml`
   - **1 hit**: adopt directly
   - **2+ hits**: ask the user "which one to track?" along with scope explanations of the candidates

### Phase B: meeting-range resolution

4. Using the adopted stable AI ID as the key, scan every meeting in [`framework/catalog/meetings.yaml`](../../../framework/catalog/meetings.yaml) and extract those whose `ai_map` contains the key
5. Apply `--meetings` / `--from` / `--to` filters
6. Zero meetings → report to the user "not registered in `ai_map`; catalog extension needed" and propose candidate meetings to add

### Phase C: inspect material availability

7. For each meeting, check the `references/` retrieval state:
   - **Chair Notes**: confirm via Glob whether `references/Chair-Notes-RAN1-<meeting>.md` exists
   - **Individual Tdocs**: among `references/R1-<num>.md`, those whose frontmatter `agenda_item` matches the meeting's AI number (often absent)
8. **Do not fetch missing material**. Instead, list the URLs and retrieval steps in a **"missing material"** section (assemble from [`framework/3gpp-ftp-cookbook.md`](../../../framework/3gpp-ftp-cookbook.md) §2.2)
   - This preserves the "instruction → interpretation → tool" flexibility. Claude decides on the spot whether to curl the file or ask the user to fetch

### Phase D: per-meeting extraction

9. For meetings with available material, extract:
   - **a. Chair Notes section**: extract the section for the AI number (heading search if already pandoc-rendered to md; otherwise use the docx-parsing steps in `framework/3gpp-ftp-cookbook.md` §2.4)
   - **b. Major Tdocs**: from available `references/R1-*.md`, list those for the AI number (FL Summary first)
   - **c. Key phrases**: harvest verbs `noted` / `agreed` / `revised` / `endorsed` / `working assumption`
   - **d. Proposing companies**: where possible, aggregate from the `Source` column of the Tdoc list (skip if not needed)

### Phase E: assemble the timeline

10. Build a cross-meeting timeline in Markdown:
    - **Header summary** (directly under H1):
      - Where the discussion has converged (agreed items)
      - Items still under discussion
      - Major axes of disagreement (company pairs / technical pairs)
      - What to watch in the next meeting
    - **Each meeting = H2 section** (chronological):
      - **i. Snapshot**: number of proposing companies, principal FL
      - **ii. Major issues**: 1-3 line summary
      - **iii. Agreements**: verbatim list of `agreed` / `endorsed` / `working assumption`
      - **iv. Open items**: `noted` / `revised` / FFS (For Further Study) items
      - **v. Cited Tdocs**: list of `[[R1-XXXXXXX]]` wikilinks
    - **Missing-material section**: URLs to retrieve and rough curl commands

### Phase F: save and link

11. Save the note as `documents/<yymmdd>_<topic-slug>_変遷.md`
12. **Always set links** ([`framework/linking-policy.md`](../../../framework/linking-policy.md)):
    - frontmatter `up:` ⇒ the parent note of the WI/SI (if already in `documents/`). If absent, derive from `framework/catalog/work-items.yaml` and place a placeholder in `next:`
    - frontmatter `related:` ⇒ existing per-meeting investigation notes in `documents/`
    - frontmatter `references:` ⇒ wikilink list of cited Chair Notes / Tdocs
    - In the body, embed `[[ファイル名]]` wikilinks at the first mention of each related note / Tdoc
    - Add reverse links from existing `documents/` notes (append the new note to their `related:`)

### Phase G: operational branches

- If catalog `aliases` were thin ⇒ append a **"catalog extension proposal"** section listing aliases to add
- If content might overlap an existing note ⇒ draft into `.tmp/<yymmdd>_<topic-slug>_変遷_draft.md` and show the diff to the user
- If the user adds instructions like "add more company-by-company positions", regenerate accordingly

## Output

- **Format**: file save + chat summary
- **Save location**: `documents/<yymmdd>_<topic-slug>_変遷.md` (flat, no subfolders)
- **frontmatter**: common schema + the following extra fields
  ```yaml
  trace:
    ai_id: "ai_nr_aiml_csi_compression_r19"   # 採用した安定 ID
    meetings_in_scope: ["RAN1#124", "RAN1#124bis", "RAN1#125"]
    completeness:
      chair_notes_obtained: ["RAN1#124bis"]   # 手元にある Chair Notes
      chair_notes_missing: ["RAN1#124", "RAN1#125"]  # 未取得（fetch 候補）
      tdocs_obtained: 0                       # 個別 Tdoc は基本未取得運用
  ```
- **status**: `draft`

## Skill-specific notes

- **Do not fully automate** — when the catalog hit is ambiguous, always confirm with the user
- **Write "missing" honestly when material is missing** — do not fill in by guess (Principle 5).
  Writing agreement items in the absence of Chair Notes is forbidden
- **AI numbers change per meeting; always resolve via `ai_map` in `meetings.yaml`**
- **Do not fetch in this skill** — execute curl steps from `framework/3gpp-ftp-cookbook.md` via the user or a separate task
- **Re-running on the same topic is allowed** — when new meetings appear, prefer incremental append via `--from` over overwrite. Draft diffs in `.tmp/` and confirm with the user
- **Always leave catalog-update proposals** — list any alias gaps, missing `ai_map` entries, or newly discovered meetings observed during the run at the end of the note (catalog grows through use; see `framework/catalog/README.md` §3.1)

## Related skills

- ← `/survey-topic` — basic topic facts (initial survey is a prerequisite for trajectory tracking)
- ↔ `/connect-dots` — horizontal connections (this skill is **vertical depth**, connect-dots is **horizontal combination**)
- → `/analyze-gap` — classify gaps surfaced by the trajectory into academic / 3GPP / implementation
- ↔ `/digest-paper` — drill into individual Tdocs / papers cited in the trajectory