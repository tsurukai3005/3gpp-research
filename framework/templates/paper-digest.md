---
up: "[[README|templates]]"
related:
  - "[[survey-topic]]"
  - "[[gap-analysis]]"
  - "[[../references-policy]]"
  - "[[../tools]]"
---

# テンプレート: 論文読解

スキル `/digest-paper` から参照される。

> 親: [[README|templates（テンプレ MoC）]] | 関連: [[survey-topic]] / [[gap-analysis]] / [[../references-policy|references-policy]] / [[../tools|pandoc/pdftotext 運用]]

## 抽出項目

### メタ情報
- 著者 / 年 / 会議 or ジャーナル / DOI or arXiv ID

### 主張（Contribution）
- 3-5点で要約

### 前提仮定
以下を明示的に抽出する:
- チャネルモデル（AWGN? Rayleigh? 3GPP channel model?）
- SNR 範囲
- アンテナ構成（送信/受信アンテナ数）
- CSI の仮定（完全 CSI? 量子化 CSI?）
- 計算複雑性の評価有無
- シミュレーション環境の詳細

### 3GPP 実装時のギャップ（最重要セクション）

前提仮定 vs NR 仕様の制約の差を言語化する。

| 論文の前提 | 3GPP の現実 | ギャップ |
|:---|:---|:---|
| (例) 完全 CSI | 限られた PUCCH リソース | CSI 量子化誤差への耐性が未検証 |
| (例) 単一セル | マルチセル干渉 | 干渉下での性能が不明 |

### 関連トピック
- `documents/` のどのノートに紐づくか

### Next Steps
- この論文を踏まえて次に調べるべきこと

## 出力ファイル

論文ダイジェスト（自分の整理）と原文 MD を別ファイルに分けて保存する:

| ファイル | パス | 内容 |
|:---|:---|:---|
| 原文 MD | `references/<論文番号 or arXiv-ID or 著者-年-タイトル>.md` | pandoc/pdftotext 出力をそのまま、論文タイトル・寄書番号・arXiv ID をファイル名に |
| ダイジェスト | `documents/<yymmdd>_<first-author>_<slug>.md` | メタ情報・主張・前提仮定・ギャップテーブル・Next Steps |

ダイジェストの frontmatter には `references: ["[[<原文ファイル名>]]"]` を必ず入れ、本文中でも `[[<原文ファイル名>]]` で参照する。
関連する `documents/` 既存ノートには `up:` または `related:` で wikilink を張る（孤立ノート禁止）。
