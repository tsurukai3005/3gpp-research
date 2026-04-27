---
up: "[[README|templates]]"
related:
  - "[[paper-digest]]"
  - "[[gap-analysis]]"
  - "[[../axes/README]]"
---

# テンプレート: トピック新規調査

スキル `/survey-topic` から参照される。

> 親: [[README|templates（テンプレ MoC）]] | 関連: [[paper-digest]] / [[gap-analysis]] / [[../axes/README|6軸]]

## 調査項目

以下の7項目で [トピック名] を調査する。
情報源は `sources.md` の「定番の情報源」を優先し、一次情報の URL を必ず記録する。

### 1. 定義と背景（Why）
- このトピックは何で、なぜ必要とされたか？
- どの技術的課題を解決するために生まれたか？

### 2. 技術要点（What）
- 最小構成（コアアイデア）は何か？
- 主要なアルゴリズム・プロトコルは？

### 3. 実装制約（How）
- 3GPP の仕様にどう落とし込まれるか？
- シグナリング、フレーム構造、リソース割当への影響は？
- ハードウェア実装の制約（チップ面積、消費電力）は？

### 4. 前世代との差分
- 4G/5G と比較して何が新しいか？
- 前世代の何が限界だったか？

### 5. 主要プレイヤー
- 学術（IEEE の主要論文・著者）
- 3GPP（Tdoc 提出企業、Feature Lead）
- 要件定義（NGMN、ITU-R 等の関連文書）

### 6. 未解決課題
- FFS に残されているもの
- 学術でも未解決のもの
- 実装上の懸念事項

### 7. 市場・普及の見込みと知財余地
- どのセグメントで誰が使うか？
- 論文と 3GPP 実装制約のギャップはどこにあるか？

## 出力フォーマット

```yaml
---
title: [トピック名]
axes:
  technology_layer: [...]
  generation: [...]
  value: [...]
  market: [...]
  adoption: [...]
  ip: [...]
status: draft
confidence: low | medium | high
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - url: https://...
    accessed: YYYY-MM-DD
references:
  - "[[arXiv-XXXX.XXXXX]]"   # references/ にある一次情報の wikilink
up: "[[親ノート名]]"           # 0または1本（最も近い親）
related:                       # 兄弟・関連ノートへの wikilink
  - "[[260420_NRフレーム構造とリソースブロックの進化まとめ]]"
---
```

ファイル名は `documents/<yymmdd>_<内容スラッグ>.md`（例: `documents/260427_cell-free-massive-mimo.md`）。サブフォルダ禁止。
