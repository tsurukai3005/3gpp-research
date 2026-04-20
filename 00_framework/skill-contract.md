# スキル契約（Skill Contract）

全てのスキル（`.claude/skills/*/SKILL.md`）はこの契約に従う。

## 共通行動原則

スキル実行時、以下は常に適用される（個別スキルでの再記述は不要）:

### 常に行うこと（Global Will）

1. **一次情報の出典を記録する** — URL + 文書番号 + アクセス日（原則1）
2. **実装制約ギャップを意識する** — 論文の理想仮定と 3GPP の制約差を常に問う（原則2）
3. **不確実な情報は `[要確認]` と明記する** — confidence フィールドも設定する（原則5）
4. **Next Steps を残す** — 次のアクションが即座に実行できる具体性で書く（原則6）
5. **`00_framework/principles.md` の6原則に従う** — スキル固有ルールが原則と矛盾する場合、原則が優先

### 絶対にしないこと（Global Will Not）

1. **出典なしに事実を断定しない** — 一次情報の URL がない主張はファイルに書かない
2. **根拠の薄い推測を確定的に書かない** — 推測は推測と明記し、confidence: low を設定する
3. **調査の範囲を恣意的に狭めない** — スキルが定める構造に沿いつつ、予想外の発見は積極的に記録する
4. **既存ノートを無断で上書きしない** — 更新時は差分を明示し、元の記述は保持する
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

1. **参照先を明示する** — 「テンプレートを読む」ではなく「`00_framework/templates/X.md` を読む」
2. **判断基準を書く** — 「情報を収集する」ではなく「3GPP ポータルで WI/SI の存在を確認し、存在すれば Tdoc リストを取得する」
3. **分岐を書く** — 情報が見つからない場合、トピックが存在しない場合の対処
4. **出力形式を固定する** — ファイル保存のパスパターン、frontmatter の必須フィールドを明記

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
sources: []              # URL のリスト
related: []              # 関連ノートへの相対パス
---
```

- `axes` の各項目は該当するもののみ記載（空リストも可）
- `sources` は最低1件必須（出典なしのノートは作成しない）
- スキル固有の追加フィールドは各スキルで定義可能