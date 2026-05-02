---
name: build-presentation
description: Build a presentation (slide content + speaker script) from a research note in four progressive phases. 研究ノートから発表資料・スライド・原稿を4フェーズで段階構築。
user-invocable: true
---

# build-presentation

## Motivation

When converting research output into a talk, packing in too much information is the
default failure mode and the message stops landing with the audience.
Applying Pyramid Principle / Assertion-Evidence / SCQA systematically produces a
presentation that **delivers what you actually want delivered**.

Send the full detail to papers and notes; on the slide, ruthlessly strip down.

## Usage

```
/build-presentation <source>
/build-presentation <source> --phase <1|2|3|4|review|patch>
/build-presentation <source> --lang <ja|en>
```

- `<source>`: a note under `documents/`, paper memo, or freeform text
- `--phase`: enter at a later phase (default: 1)
- `--lang`: output language (default: ja)

### Mid-flow entry points

| Flag | Use case |
|:---|:---|
| `--phase 2` | Build the tree directly from the source material |
| `--phase 3` | Tree is already done; only ask for story and ordering |
| `--phase 4` | Structure is fixed; only ask for per-slide concretization |
| `--phase review` | Pass an existing deck and evaluate it against the value definition with improvement suggestions |
| `--phase patch` | Edit a specific slide (provide context of surrounding claims) |

**In every case, always confirm the five Phase 1 items first** (audience / what to convey / success definition / ...).
Even with an explicit declaration, if any of the five items are missing, fill those gaps via dialogue before advancing to the requested phase.

## Inputs and prerequisites

- **Required input**: source material for the talk (path of a repo note, plain text, or attached file)
- **Minimum information**: at least 2 of the following (the rest will be filled in Phase 1 dialogue)
  - audience profile
  - purpose of the talk
  - duration
- **Optional (improves quality)**:
  - past similar decks
  - audience-preferred / disliked styles
  - constraints from supervisors or co-presenters
  - differentiation against competing talks at the same venue
- **Cannot proceed when**: source material is empty → first redirect to `/survey-topic` or `/digest-paper`

## Execution flow

### Critical rules

1. **At the end of every phase, stop and obtain user confirmation before advancing.**
   Even on vague approval (e.g. "looks fine") with no concrete change request, re-confirm.
2. **Roll back to a previous phase as soon as a problem is found.**
   Choose to roll back rather than "we're already late, let's keep going". If you notice the takeaway is weak in Phase 3, return to Phase 1.
3. **If an existing artifact file exists** (under `documents/`), read it and continue from there.
4. **Read the source material end-to-end before entering Phase 1.**
   Do not propose structure based on the first few dozen lines or just the frontmatter. State the read range explicitly (e.g. "read lines 1-489 in full, no unread range"). When there are multiple sources, declare this for each one.
5. **Enumerate every major source structure before pruning.**
   List every heading-level unit of the source (this project uses 「主張N」「根拠N.M」「節」 etc.) and **explicitly** label each unit as one of: `adopt` / `prune (with reason)` / `defer (question item)`. Do not invent treatments not present in the source ("save for next time", "move to a separate doc"). If you drop something, declare it as `prune` with a reason in Phase 3.
6. **Track every element of the frontmatter `takeaway` in a coverage table.**
   When `takeaway` contains multiple elements (e.g. A + B + C + D), present a table mapping each element to the slide numbers / claim node IDs that cover it. Drops must be declared with a reason.
7. **Do not invoke renderers (`tools/pptx/build_slides.py`, `/render-tex-slides`, etc.) or external generators before the Phase 1-3 thinking process is confirmed.**
   Renderers only perform a deterministic transform: spec → pptx, or note → tex. Responsibility for the slide structure sits in this skill's process. Only after Phase 4 user confirmation has been obtained batch-by-batch may you assemble the spec and call the renderer.

---

### Progress gates from MD source to slide structure

A phase advances only when its gate is met. Otherwise return to the prior phase.

| Gate | Condition to advance |
|:---|:---|
| **G0 → Phase 1** | Source material has been read end-to-end (read range declared) |
| **G1 → Phase 2** | Explicit user agreement on the five items (audience / prior knowledge / what to convey / success definition / failure definition) |
| **G2 → Phase 3** | Full enumeration of source structure + adopt/prune/defer labels + tree, with explicit user agreement |
| **G3 → Phase 4** | Explicit user agreement on SCQA, ordering, prune reasons, and the takeaway coverage table |
| **G4 → spec/renderer** | Phase 4 user confirmation completed batch-by-batch for every slide |

**Typical gate violations (do not commit)**
- Assemble a slide spec while only part of the source has been read
- Skip Phase 1 confirmation just because frontmatter has `audience` / `takeaway` recorded
- Invent treatments like "next time" / "separate document" without user instruction
- Silently drop part of the major source structure (claims, evidence, ...)
- Skip Phase 1-3 in the name of validating the renderer

---

### Phase 1: Fix the audience and the goal

**Purpose**: define the evaluation axis. If this wobbles, every downstream step wobbles.

1. **Read the source material end-to-end**. With multiple sources, read all of them. Report the read result in one line (e.g. `[[xxx]] 全 489 行 / [[yyy]] 全 120 行 を読了、未読範囲なし`)
2. Bundle unclear points into **at most 2-3 questions** (do not drag out questioning). Even when the frontmatter records `audience` / `takeaway`, ask if anything remains uncertain
3. Fix the following five items:
   - **Primary audience** (with priority when multiple)
   - **Audience prior-knowledge level** (what they know vs. don't know)
   - **What to convey** (the message for the audience; fewer is structurally better, but multiple is acceptable)
   - **Success definition** (what should change in the audience after the talk)
   - **Failure definition** (what would make the value zero)
4. Present the five items and obtain explicit agreement, especially on "what to convey" and "success definition". A vague compromise here wastes every downstream phase, so do not advance with ambiguity

**Phase 1 completion (G1)**: end-to-end read declared, and explicit user agreement on the five items

---

### Phase 2: Build the message tree

**Purpose**: build the logical structure of the talk. Without a tree, slide drafting becomes "a list of things I want to say" and the structure collapses.

1. **Enumerate and label the source structure** (prerequisite for tree construction): list every major heading of the source (「主張N」「根拠N.M」「節」「サブセクション」 etc.) and label each unit as one of the following. Present this as a table to the user.
   - **adopt**: place on the tree
   - **prune**: exclude with reason (low importance / not needed for understanding other nodes; reason will be re-examined in Phase 3)
   - **defer**: needs user judgement. In this case add it to the Phase 1 questions before proceeding
   - Treatments not in the source ("next time", "separate doc") are forbidden. If you drop something, declare it as `prune` with a reason
2. **Decide the tree structure**: based on the Phase 1 "what to convey", decide a sound tree through dialogue
   - One takeaway → one pyramid with that takeaway at the apex
   - Multiple takeaways → multiple pyramids, each with a takeaway at the apex
   - Pyramid shape: apex (takeaway) → claims (2-4) → evidence (cite the corresponding source location)
   - Also state the relationship between pyramids (independent, sequential dependency, contrast, ...)
3. **Surface the prerequisite concepts**: enumerate prior knowledge that is outside the explained section but required for understanding. Do not stop at the source note's scope; verify that every concept the audience needs to understand each claim is present on the tree
4. **Subsection coverage check**: for every subsection of the target section, list whether it is explained. If you intentionally omit one, state the reason
5. MECE check: confirm there is no overlap or gap between sibling nodes
6. Importance ranking: assign each node an importance (high / medium / low) and state the rationale

**Output format** (repeat per pyramid when there are multiple):
```
伝えたいこと A: [文]
├── 主張1: [文] (重要度: 高)
│   ├── 根拠1.1: [資料X p.Y より]
│   └── 根拠1.2: ...
├── 主張2: ... (重要度: 中)
└── 主張3: ... (重要度: 高)

伝えたいこと B: [文]
├── ...

ピラミッド間の関係: A は B の前提知識となる
```

**Confirm with the user explicitly**:
- Is the tree shape (number of pyramids, relationship) sound?
- Is the way claims are split sound?
- Are any important points missing?
- Is the source citation under each evidence correct?
- Is the importance ranking sound?

**Self-question**: does the whole tree express "what to convey" without excess or deficit? (3-5 line report. If a problem is found, propose returning to Phase 1.)

**Phase 2 completion (G2)**: explicit user agreement on the source-structure enumeration + adopt/prune/defer labels + tree (including prerequisite concepts, subsection coverage, MECE, and importance)

---

### Phase 3: Story construction and pruning

**Purpose**: unfold the tree into a time-ordered talk. Eliminate logical leaps and produce a flow where the audience does not get lost.

1. **Write an SCQA introduction**: 1-2 sentences per block
   - Situation: a premise the audience can agree with
   - Complication: a change or problem
   - Question: the question to be asked
   - Answer: your answer (= what to convey; summarize when there are multiple)
2. **Build the takeaway coverage table**: when frontmatter `takeaway` (which should match Phase 1's "what to convey") contains multiple elements, build a table mapping each element to slide numbers / claim node IDs. Declare drops with a reason. If Answer ≠ Q, or if a takeaway element is dropped, return to Phase 1 or Phase 2

   ```
   takeaway 要素 | カバーするスライド | 主張ノード | 備考
   ----------------------------------------------------------
   A: ...        | Slide 4-5         | 主張1, 2.1 |
   B: ...        | Slide 6           | 主張3      |
   C: ...        | (落とす)          | —          | 理由: 重要度低、A の系として包含される
   D: ...        | Slide 7-8         | 主張4, 5   |
   ```

3. **Decide ordering**: decide the order across pyramids and the order of claims inside each pyramid. Decide via dependencies (B is unintelligible without A) and importance
4. **Design transitions**: write connector sentences between claims and between pyramids. Make the audience able to predict "what comes next"
5. **Pruning**: based on the importance ranking and the source-structure labels from Phase 2, finalize the deletion reason for every dropped node. Re-examine all `prune`-labeled items from Phase 2. The temptation to keep a node "because it would be a shame to drop" is strong, so apply a strict bar to the deletion rationale
6. **Time allocation (reference)**: when a duration is fixed, record a rough allocation per claim. The exact time is unknown until rehearsal — treat this as a guideline only

**Output format**:
```
【導入 (SCQA)】
Situation: ...
Complication: ...
Question: ...
Answer: ... (= 伝えたいこと)

【本体の順序】
1. 主張1 (重要度: 高)
   → トランジション: "..."
2. 主張2 (重要度: 中)
   ...

【枝刈り提案】
- 根拠2.3: 削除推奨（理由: 重要度低、他ノードの理解に不要）
- ...

【時間配分（参考）】
- 全体: 約N分（発表時間が決まっている場合）
- 各ブロックの大まかな比重
```

**User confirmation**: ordering and pruning are areas with significant presenter discretion. Treat Claude's suggestion as a starting point, expecting adjustment.

**Self-question**: are there logical leaps? Are high-importance nodes placed appropriately? Do SCQA's Q and A match? Does the takeaway coverage table have zero missing elements, or are missing reasons explicitly stated? (3-5 line report. If a problem is found, propose returning to a previous phase.)

**Phase 3 completion (G3)**: explicit user agreement on SCQA, ordering, prune reasons, and the takeaway coverage table

---

### Phase 4: Concretize slides + script

**Purpose**: expand each node into "1 slide + script". Apply Assertion-Evidence rigorously.

Expand each node in the format below. Present in batches of **3-5 slides** and obtain confirmation (presenting all slides at once degrades quality because the user cannot review thoroughly). Split further for long talks.

```markdown
## Slide N: [1文の主張ヘッドライン]

### 視覚コンテンツ
- [図/グラフ/表の種類と内容]
- [軸、凡例、強調点（矢印・色で示す箇所）]
- [データソース]

### 原稿（推定時間: X秒）
[話し言葉で書く]

### 補足
- トランジション: [次スライドへのつなぎ]
- Q&A予想: [想定質問と回答方針]
- 注記: [削除可能/時間調整ポイントの場合は明示]
```

**Rules to obey**:
- Headline is a **complete sentence** (「○○について」 → 「○○は△△である」)
- One slide = one claim (split if it threatens to become two)
- **Write the script as concise bullet points** (the presenter supplements with spoken phrasing on the spot)
- Visual content is meaningful figures only (do not write decorations)
- Numbers are presented with a comparison reference (limit digit count to the meaningful range)
- **Slide titles are fact-based**. Avoid metaphor and emphatic phrasing. Do not conflate "scope declaration" with "fact assertion"
- **Include the rationale for naming and formula choices in the explanation** (e.g. why "minimum", why "common")
- Always cite the corresponding spec section number

**Anti-AI writing screening (mandatory before user confirmation)**:
Before presenting each batch of 3-5 slides, scan every headline and script line against [`framework/anti-ai-writing.md`](../../../framework/anti-ai-writing.md) §1 patterns (metaphor escapes, vague attribution, adjective inflation, theatrical preambles, unsupported clichés). For every detection, decide explicitly: keep with reason, delete, or replace. Report the count and decisions in 1-3 lines per batch (e.g. `anti-ai 検査: 5件検出 → 3件削除 / 1件数値置換 / 1件保持(理由: ...)`). Do not skip this step.

**Self-question**: does each slide actually prove its headline? Does the whole talk improve the audience's understanding / judgement / action? (3-5 line report. If a problem is found, consult the user without hesitation.)

**Phase 4 completion (G4)**: every slide's content (headline, visual content, script, supplement) has been confirmed by the user batch-by-batch (3-5 at a time), and the anti-ai screening has been applied per batch

---

### After Phase 4: handoff to the renderer

The renderer is invoked only here. The entry point depends on the desired output format:

- **For PPTX output**: [`tools/pptx/build_slides.py`](../../../tools/pptx/build_slides.py) (spec.json → `slides/pptx/<title>.pptx`)
- **For TeX/Beamer/PDF output**: [`/render-tex-slides`](../render-tex-slides/SKILL.md) (note → `slides/tex/<yymmdd>_<slug>/main.pdf`)

The two pipelines are completely separated by output location, template, and naming namespace (PPTX: `tools/pptx/`・`slides/pptx/`; TeX: `framework/templates/slide-tex/`・`slides/tex/`). Do not mix them.

**Pre-call check (re-verify G4 is met)**:
1. Have all gates in Phase 1-4 been passed?
2. Does the takeaway coverage table have no missing elements (or, if any, are they declared with reasons)?
3. Are no `defer` items left in the source-structure labels (adopt/prune/defer)?
4. Has the user given an explicit instruction such as "render to pptx" / "send to the renderer"?

**OK to call**: Phase 4 confirmation completed for every slide and the user said "now build the pptx"
**NOT OK to call**: skipping Phase 1-4 under the guise of tool verification / producing a pptx mid-Phase-4 / writing a spec on your own and building "as a sanity check"

The renderer is responsible for the deterministic spec → pptx transform. **Responsibility for slide-structure quality sits in Phase 1-4.**

---

### Review mode

Invoke with `--phase review`. Pass an existing deck and evaluate against:

1. The "value definition" section
2. Whether each slide satisfies Assertion-Evidence
3. Pruning suggestions
4. SCQA reconstruction proposal (if needed)

### Patch mode

Invoke with `--phase patch`. Edit a specific slide.

1. Receive the target slide along with surrounding-claim context
2. Confirm the five Phase 1 items (retrievable from existing file's frontmatter / metadata)
3. Verify that the edited slide remains consistent with the overall storyline and transitions
4. Present the edit, and report any knock-on effects on neighbouring slides

## Output

- **Format**: chat (interactive, progressive generation) + final file
- **Save location**: `documents/<yymmdd>_<slug>.md` (flat, no subfolders; `yymmdd` is the creation date)
- **Links**: list source notes in frontmatter `source_notes` and in `up:` / `related:` as wikilinks. Embed `[[ソースノート名]]` at first mention in the body ([`framework/linking-policy.md`](../../../framework/linking-policy.md))
- **frontmatter**:

```yaml
---
title: "発表タイトル"
status: draft | reviewed | stable
created: YYYY-MM-DD
updated: YYYY-MM-DD
audience: "聴衆の属性"
takeaway:
  - "伝えたいこと1"
  - "伝えたいこと2（複数の場合）"
duration_min: N
venue: "会議室 / 学会 / オンライン"
format: "口頭発表 / ポスター / ライトニングトーク"
source_notes:
  - "ソースノートへの相対パス"
lang: ja | en
---
```

**Final document structure**:
```markdown
# [発表タイトル]

## メタ情報
- 聴衆 / 目的 / 時間 / 会場 / 形式

## ストーリー概要
(SCQA + 主張順序の圧縮版)

## スライド別内容
### Slide 1: [ヘッドライン]
...

## 想定Q&A
- Q: ... / A: ...

## 削除候補 / 時間調整ポイント
- Slide X: 時間不足時は省略可能（理由）
```

## Skill-specific notes

### Value definition (re-question constantly)

1. **Audience understands what to convey**: they can answer "what was that about?" (fewer takeaways → clearer answer)
2. **Audience's understanding / judgement / action improves over the pre-talk baseline**: not information transfer, but change
3. **Value of the deleted ≥ value of the kept**: "packing too much" kills a talk

**Anything that does not contribute to the three points above is noise.** Judge purely by contribution to these three — not by appeals to form or style.

### Expression rules (apply across all phases)

These apply to every text this skill produces — slide content, script, tree, SCQA, etc.

The tables below are the **canonical reference** for forbidden expressions in this skill.
[`framework/anti-ai-writing.md`](../../../framework/anti-ai-writing.md) provides a Japanese-localized
pattern dictionary plus grep-based self-check commands; consult it during the Phase 4 anti-ai screening.

#### Forbidden expressions

**1. Self-evaluative expressions**: phrases that assert one's own value. Show via results.

| 禁止 | 代替 |
|:---|:---|
| 核心的貢献、画期的、革新的 | 具体的な技術変更を記述する |
| 優れた、卓越した | 数値比較で示す |
| パラダイムシフト | 「アプローチの変更」等、事実を書く |
| 〜を実現する（未実証のまま） | 「〜を目的とする」または実証結果を書く |

**2. Metaphoric / decorative expressions**: describe the technical content directly.

| 禁止 | 代替 |
|:---|:---|
| 橋渡し、鍵を握る、扉を開く、柱となる | 事実を直接記述する |
| 〜を支える、〜の心臓部 | 「〜に必要な」「〜を構成する」 |
| 〜の世界、〜の風景 | 削除 |
| ナビゲートする、駆動する | 「探索する」「計算する」等の動作動詞 |

**3. Vague magnitude / degree expressions**: replace with numbers and concrete comparisons.

| 禁止 | 代替 |
|:---|:---|
| 非常に、極めて、かなり、大幅に | 具体的な数値比較 |
| 飛躍的に、劇的に | 変化量を数値で示す |
| 多くの、少ない、一部の | 具体的な個数・割合 |
| 高い、低い、大きい、小さい | 数値+単位+基準 |
| 約、およそ（範囲なし） | 具体値または明示的な範囲 |

**4. Theatrical connectors / preambles**: drop them and write the fact directly.

| 禁止 | 代替 |
|:---|:---|
| ここで重要なのは、注目すべきは | 削除。事実をそのまま書く |
| 興味深いことに、驚くべきことに | 削除。結果を提示する |
| 言うまでもなく、当然のことながら | 削除。根拠が自明なら書かなくてよい |
| まず理解すべきは | 削除。説明を始める |
| 本スライドでは〜を説明する | 削除。スライドタイトルが内容を示す |

**5. Unsupported evaluations / clichés**: evaluations may only appear with quantitative grounds.

| 禁止 | 代替 |
|:---|:---|
| 効果的、有用、有望 | 何がどう変わるかを具体的に書く |
| 一般的に〜と言われている（出典なし） | 出典を付けるか削除 |
| 近年〜が注目されている（出典なし） | 具体的な時期と出典を示す |
| 広く知られているように | 削除。事実を書く |

**6. Repetition / redundancy**: do not say the same thing in different words.

| 禁止 | 代替 |
|:---|:---|
| 同じ主張を言い換えて複数回書く | 1回で明確に書く |
| 「前述のとおり〜」で再説明する | セクション番号を参照する |
| 「新しく新規な」等の同義反復 | 片方を削除 |

**7. Coined / undefined terms**: use existing terms, or define on first appearance.

| 禁止 | 代替 |
|:---|:---|
| 引用根拠のない専門用語風の造語 | 既存の用語を使う |
| 省略形（初出で未定義） | 初出時に正式名称と定義を提示 |

#### Mandatory rules

1. **Distinguish facts from inferences explicitly**
   - Fact: 「仕様 TS 38.211 §4.3.2 では〜と定義されている」
   - Inference: 「この制約から〜と考えられる」
   - Unverified: 「〜の可能性があるが、確認が必要」
2. **Numbers should be presented with their comparison reference and conditions when possible** (best-effort; omit if it becomes verbose)
   - 「処理量が増加する」 is weaker than 「処理量が O(MK) から O(MK²) に増加する」
   - **Never fabricate numbers without source or basis**. If the concrete number is unknown, it is better to leave 「増加する」 as is.
3. **Use existing definitions for terminology**. If a coined term is required, define it on first appearance
4. **Do not use theatrical phrasing unless the user requests it**
5. **Each sentence must add new information**. Do not write zero-information sentences.

### Frameworks (operational reference)

| Framework | Key idea |
|:---|:---|
| Pyramid Principle | conclusion → claims → evidence; top-down; siblings are MECE |
| Assertion-Evidence | 1 slide = 1 claim (full-sentence headline) + visual evidence |
| Doumont 3 principles | audience fit / max S/N / effective redundancy; no more than 3 in parallel |
| Peyton Jones | narrow the takeaway, examples mandatory, ruthless pruning |
| SCQA | Situation → Complication → Question → Answer |

Reading the originals deepens understanding (Alley and Doumont in particular are practical for engineering presenters):
- Barbara Minto, *The Pyramid Principle* (Pearson)
- Michael Alley, *The Craft of Scientific Presentations* (Springer)
- Jean-luc Doumont, *Trees, Maps, and Theorems* (Principiae)
- Simon Peyton Jones et al., "How to give a good research talk", *SIGPLAN Notices* 28(11), 1993

### External research rules

Run external search only when:
- The latest information not in the supplied source is required for a claim
- Performance numbers of competing methods are needed for comparison
- Industry trend / standardization status confirmation is needed

Constraints: keep it minimal, cite sources, do not conflate guesses with search results.
When time is limited, ask the user before searching.

### Connection to the 3GPP research context

- Notes under `documents/` may be referenced as sources directly
- Apply Principle 1 (source recording) to technical grounds
- The implementation-constraint gap (Principle 2) can be a differentiator for the talk
- Use the note's `axes:` to contextualize for the audience

## How to update this skill

After every actual presentation, jot down the following to improve the skill:

1. **What worked**: which rules paid off
2. **What did not work**: which rules did not fit reality
3. **Rules to add**: new rules derived from this experience
4. **Rules to delete / fix**: rules proven unnecessary

### Next-update candidates (judged in operation)

- Mode switch: research talk vs. internal business talk
- Additional rules for English presentations (phrasing, Q&A handling)
- Time-of-day rules (e.g. early-afternoon slump)

### 更新履歴

- **v1.6 (2026-05-02)**: ソース読了義務・ソース構造の全列挙ラベル付け・takeaway カバレッジ表・レンダラ呼び出し条件を追加。各 Phase に完了条件 (G1-G4) を明示。`MD ソースからスライド構造を決めるまでの進行ゲート` セクションを新設
- **v1.5 (2026-04-21)**: 表現ルールを追加。禁止表現を7カテゴリに分類（自己評価、比喩・装飾、曖昧な量・程度、演出的接続・前置き、根拠のない評価・常套句、繰り返し・冗長、造語・未定義用語）。必須ルールに「各文は新しい情報を追加する」を追加
- **v1.4 (2026-04-21)**: ツリー構造の柔軟化（複数ピラミッド対応）、時間計算を参考情報に格下げ、重要度ベースの枝刈りに変更、比喩表現の排除
- **v1.3 (2026-04-21)**: ユーザーフィードバック反映。Phase 2 に前提概念洗い出しとサブセクション網羅チェックを追加。Phase 4 の原稿形式を箇条書きに変更、タイトルの事実/スコープ区別・命名根拠説明・仕様セクション番号明示を追加。保存先を `documents/` 配下に変更
- **v1.2 (2026-04-21)**: 各フェーズに「目的」と「なぜそうするか」の説明を復元。Phase 2/3 にユーザー確認の具体的チェックリストとアウトプット形式を追加。Phase 4 に分割提示の理由を明記
- **v1.1 (2026-04-21)**: レビュー結果を反映。途中エントリ強化（patch モード追加、Phase 1 前提条件チェック）、フェーズ巻き戻し許可、更新サイクル追加、参考文献追加、frontmatter に venue/format 追加
- **v1.0 (2026-04-21)**: 初版。`docs/presentation-prompt-v1.md` から SKILL.md 形式に変換

## Related skills

- `/survey-topic` — survey the topic that becomes the source of the talk
- `/analyze-gap` — use gap analysis as the rationale for the talk
- `/connect-dots` — use cross-topic links in the storyline
- `/digest-paper` — reference paper memos as material