# スキル契約（Skill Contract）

全てのスキル（`.claude/skills/*/SKILL.md`）はこの契約に従う。

## 共通行動原則

スキル実行時、以下は常に適用される（個別スキルでの再記述は不要）:

### 常に行うこと（Global Will）

1. **一次情報の出典を記録する** — URL + 文書番号 + アクセス日（原則1）
2. **実装制約ギャップを意識する** — 論文の理想仮定と 3GPP の制約差を常に問う（原則2）
3. **不確実な情報は `[要確認]` と明記する** — confidence フィールドも設定する（原則5）
4. **Next Steps を残す** — 次のアクションが即座に実行できる具体性で書く（原則6）
5. **`framework/principles.md` の6原則に従う** — スキル固有ルールが原則と矛盾する場合、原則が優先
6. **バイナリ文書はテキスト化してから読む** — `.docx` / `.pptx` / `.odt` / `.rtf` は pandoc で Markdown 化し、生成した `.md` を Read / Grep する。コマンドと運用は [`framework/tools.md`](./tools.md) を参照
7. **一次情報は `references/` に Markdown 化して保存する** — 論文・Tdoc・Chair Notes・仕様書は本文を抽出して保存。ファイル名は論文タイトル/寄書番号/arXiv ID をそのまま使う。詳細は [`framework/references-policy.md`](./references-policy.md)
8. **ノート間は必ずリンクでつなぐ** — Obsidian wikilink (`[[ファイル名]]`) を本文に埋め、frontmatter `up` / `related` で階層関係を明示する。孤立ノート（被リンクも発リンクも無いノート）は禁止。詳細は [`framework/linking-policy.md`](./linking-policy.md)
9. **ノートは常に「現時点の最良の状態」を表現する完成形として書く** — 更新時は古い記述を新しい記述で **置き換える**（純粋な情報更新）。差分や旧版を本文に残さない。事実の削除・大幅な書き換えで情報が失われる恐れがあるときは、実行前にユーザーに確認する

### 絶対にしないこと（Global Will Not）

1. **出典なしに事実を断定しない** — 一次情報の URL がない主張はファイルに書かない
2. **根拠の薄い推測を確定的に書かない** — 推測は推測と明記し、confidence: low を設定する
3. **調査の範囲を恣意的に狭めない** — スキルが定める構造に沿いつつ、予想外の発見は積極的に記録する
4. **ノート本文に会話の経緯・差分・修正履歴を書かない** — 「ユーザが○○と述べたので」「前回は X と書いたが今回 Y に修正」「ご指摘を反映して」「当初の記述では…だったが」等のメタ記述は禁止。読者はノート本体だけを見るので、編集経緯は git のコミットログに残し、本文は **最終結果だけ** を示す。frontmatter の `updated` フィールドは更新日付の記録のみに用い、変更内容は記述しない
5. **非公開情報・NDA 対象の情報を扱わない** — 公開情報のみ
6. **特許クレームの起草・法的助言をしない** — 知財分析は調査・考察の範囲に留める

## スキルファイルの統一構造

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

## 実行フローの設計原則

1. **参照先を明示する** — 「テンプレートを読む」ではなく「`framework/templates/X.md` を読む」
2. **判断基準を書く** — 「情報を収集する」ではなく「3GPP ポータルで WI/SI の存在を確認し、存在すれば Tdoc リストを取得する」
3. **分岐を書く** — 情報が見つからない場合、トピックが存在しない場合の対処
4. **出力形式を固定する** — ファイル保存のパスパターン、frontmatter の必須フィールドを明記

## ファイルの保存場所と命名

### `documents/` — 自分の調査ノート（フラット）

- すべて `documents/` 直下に保存する。サブフォルダで分類しない（将来見直し）
- ファイル名: `yymmdd_<内容スラッグ>.md`
  - `yymmdd` は **作成日**（frontmatter `created` の年下2桁+月+日）。更新日ではない
  - 例: `260421_NRフレーム構造の発表資料ドラフト.md`、`260427_RAN1-124bis-DL-CSI-BM-AIML-調査.md`
- スラッグは日本語可。スペースの代わりにハイフン or アンダースコア
- 同日に複数作る場合は内容スラッグで区別する（連番は付けない）

### `references/` — 一次情報の Markdown 化（フラット）

- 論文・Tdoc・Chair Notes・仕様書を Markdown 化したものは `references/` 直下に保存
- ファイル名は **論文タイトル・寄書番号・arXiv ID をそのまま使う**（`yymmdd_` を付けない）
- 詳細は [`framework/references-policy.md`](./references-policy.md)

## frontmatter の共通スキーマ

全てのノートファイルは以下の frontmatter を持つ:

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

- `axes` の各項目は該当するもののみ記載（空リストも可）
- `sources` は最低1件必須（出典なしのノートは作成しない）
- `up` / `related` の少なくとも一方に最低1本のリンクを入れる（孤立ノート禁止、[`linking-policy.md`](./linking-policy.md)）
- スキル固有の追加フィールドは各スキルで定義可能