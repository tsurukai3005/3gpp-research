# Skill Contract

Every skill (`.claude/skills/*/SKILL.md`) must comply with this contract.

## Common behavioral principles

The following always apply during skill execution. Individual skills should not restate them.

### Global Will (always do)

1. **Record the primary source** — URL + document number + access date (Principle 1)
2. **Be aware of the implementation-constraint gap** — always question the difference between academic ideal assumptions and 3GPP constraints (Principle 2)
3. **Mark uncertain information as `[要確認]`** — also set the `confidence` field (Principle 5)
4. **Leave Next Steps** — write the next actions so they can be executed immediately (Principle 6)
5. **Follow the six principles in `framework/principles.md`** — when a skill-specific rule conflicts with these principles, the principles win
6. **Convert binary documents to text before reading** — `.docx` / `.pptx` / `.odt` / `.rtf` must be converted to Markdown via pandoc; then Read / Grep the generated `.md`. Commands and procedures: see [`framework/tools.md`](./tools.md)
7. **Save primary sources as Markdown under `references/`** — papers, Tdocs, Chair Notes, and specs must have their body extracted and stored. Use the paper title / contribution number / arXiv ID verbatim as the filename. Details: [`framework/references-policy.md`](./references-policy.md)
8. **Always link notes** — embed Obsidian wikilinks (`[[ファイル名]]`) in the body, and express hierarchy via the frontmatter `up` / `related` fields. Orphan notes (with no incoming or outgoing links) are forbidden. Details: [`framework/linking-policy.md`](./linking-policy.md)
9. **Write each note as a finished artifact representing the current best state** — when updating, **replace** old descriptions with new ones (pure information replacement). Do not leave diffs or old versions in the body. If deletion or major rewriting risks losing information, confirm with the user before proceeding.

### Global Will Not (never do)

1. **Do not assert facts without a source** — claims with no primary-source URL must not be written to a file
2. **Do not write thin guesses as definitive** — mark guesses as guesses, and set `confidence: low`
3. **Do not arbitrarily narrow the scope of investigation** — follow the structure imposed by the skill, but actively record unexpected findings
4. **Do not write conversation history, diffs, or revision notes in the note body** — meta-comments such as "ユーザが○○と述べたので", "前回は X と書いたが今回 Y に修正", "ご指摘を反映して", "当初の記述では…だったが" are forbidden. The reader sees only the note body, so editing history belongs in git commit logs; the body must show **only the final result**. The frontmatter `updated` field is for the update date only — do not describe what changed.
5. **Do not handle non-public or NDA-restricted information** — public sources only
6. **Do not draft patent claims or give legal advice** — IP analysis is limited to research and discussion
7. **Do not generate citation information from memory** — document numbers, authors, titles, year, DOI, arXiv ID, and Tdoc numbers must only be written after their existence has been verified against a primary source at the moment of writing. When verification is impossible, leave a `[要出典: <hint>]` marker instead of asserting (see [`framework/references-policy.md`](./references-policy.md) §0). This applies to all skills; an unverified document number is a Principle 1 violation regardless of how plausible it sounds.

## Unified structure of a skill file

```markdown
---
name: スキル名
description: 一行の目的説明
user-invocable: true
---

# スキル名

## モチベーション

このスキルが存在する理由。どんな問いに答えるためのものか。

## 使い方

起動コマンドと引数の説明。

## 入力と前提

- 必須入力: 何が必要か
- 前提条件: 事前に何が存在している必要があるか
- 最低限の情報: これがないと実行できない閾値

## 実行フロー

番号付きの手順。各ステップは:
- 何をするか（動詞で始まる）
- 何を参照するか（ファイルパス）
- 何を出力するか

## 出力

- 形式: チャット / ファイル / 両方
- 保存先: ファイルパスのパターン
- frontmatter: 必須フィールド
- status: 初期値（通常 draft）

## このスキル固有の注意点

Global Will / Will Not に加えて、このスキル特有のルール。

## 関連スキル

このスキルの前後に使うと有効なスキルへのポインタ。
（実行の強制ではなく、参考情報として提示）
```

## Design principles for the execution flow

1. **Make references explicit** — not "read the template" but "read `framework/templates/X.md`"
2. **State the decision criteria** — not "collect information" but "check whether the WI/SI exists in the 3GPP portal; if it does, retrieve the Tdoc list"
3. **Write the branches** — what to do when the information is not found, or when the topic does not exist
4. **Fix the output format** — explicitly specify the file save path pattern and the required frontmatter fields

## File location and naming

### `documents/` — your own research notes (flat)

- Save everything directly under `documents/`. Do not classify into subfolders (revisit later)
- Filename: `yymmdd_<内容スラッグ>.md`
  - `yymmdd` is the **creation date** (last two digits of year + month + day, matching frontmatter `created`). Not the update date.
  - Examples: `260421_NRフレーム構造の発表資料ドラフト.md`、`260427_RAN1-124bis-DL-CSI-BM-AIML-調査.md`
- Slugs may use Japanese. Use a hyphen or underscore in place of a space.
- When creating multiple notes on the same day, distinguish by content slug (do not append a sequential number)

### `references/` — primary sources rendered as Markdown (flat)

- Save Markdown renderings of papers, Tdocs, Chair Notes, and specs directly under `references/`
- Use the **paper title / contribution number / arXiv ID verbatim** as the filename (no `yymmdd_` prefix)
- Details: [`framework/references-policy.md`](./references-policy.md)

## Common frontmatter schema

Every note file must carry the following frontmatter:

```yaml
---
title: "タイトル"
status: draft | reviewed | stable | obsolete
confidence: low | medium | high
created: YYYY-MM-DD
updated: YYYY-MM-DD
axes:
  technology-layer: []   # phy-mimo, phy-coding, higher-layer, cross-layer
  generation: []         # rel-15, rel-16, ..., rel-21
  value: []              # energy-efficiency, coverage, ai-integration, throughput, latency, connectivity, reliability
  market: []             # consumer-xr, b2b-industrial, fwa, ntn, ambient-iot
  adoption-factors: []   # killer-app, standard-convergence, operator-roi, economies-of-scale, backward-compat
  ip: []                 # novelty, inventive-step, spec-mapping
sources: []              # 出典 URL のリスト（references/ にも置いていればそれを `references` に追記）
references: []           # references/ 配下の wikilink リスト（このノートが引用する一次情報）
up: ""                   # 親ノート（wikilink、0または1本）
related: []              # 関連ノートへの wikilink リスト
---
```

- List only the entries that apply under each `axes` key (empty lists are allowed)
- `sources` requires at least one entry (notes without a source must not be created)
- At least one of `up` / `related` must contain at least one link (no orphan notes — see [`linking-policy.md`](./linking-policy.md))
- Each skill may define additional skill-specific fields