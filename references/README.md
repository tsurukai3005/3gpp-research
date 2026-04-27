# references — 一次情報の Markdown 化置き場

論文・3GPP Tdoc・Chair Notes・仕様書・ベンダーホワイトペーパーなど、調査の根拠となる
一次情報を Markdown に変換して置く場所。

## ルール

詳細は [`framework/references-policy.md`](../framework/references-policy.md) を参照。
要点だけ:

- **フラット構造**: 全ファイルを `references/` 直下に置く（サブフォルダなし）
- **命名は原文の番号/タイトルをそのまま**:
  - 3GPP Tdoc → `R1-2503456.md`
  - arXiv 論文 → `arXiv-2508.08225.md`
  - 仕様書 → `TS38.211-v18.6.0.md`
  - Chair Notes → `Chair-Notes-RAN1-124bis.md`
  - ホワイトペーパー → `Qualcomm_Making5GNRReality_2016.md`
- **`yymmdd_` プレフィックスは付けない**（`documents/` の命名規則とは別）

## 変換コマンド

| 元ファイル | 推奨コマンド |
|:---|:---|
| docx | `pandoc input.docx -t gfm --wrap=none --extract-media=./media -o output.md` |
| pdf（論文） | `pdftotext -layout input.pdf output.txt`（拡張子を `.md` にリネームして保存） |
| pdf（仕様書） | docx 版があれば pandoc 優先。なければ `pdftotext -layout` |

詳細は [`framework/tools.md`](../framework/tools.md) を参照。

## frontmatter スキーマ

```yaml
---
title: "原文タイトル（言語そのまま）"
type: paper | tdoc | chair-notes | spec | whitepaper | web-article
source_url: https://...
accessed: YYYY-MM-DD
authors: []
year: YYYY
venue: ""
identifiers:
  arxiv: ""
  doi: ""
  tdoc: ""
  spec: ""
related:                    # documents/ 配下でこのリファレンスを引用しているノート
  - "[[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]]"
---
```

## 引用の作法

- **必ず `documents/` 配下のノートからリンクされる**こと（孤立 references は禁止）
- 引用元 `documents/` ノートの frontmatter `references:` に wikilink を入れる
- このフォルダのノート側にも `related:` で逆方向リンクを保つ（双方向）
- 1つの reference ノートが複数の `documents/` から参照されてよい
