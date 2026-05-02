# 参考文献ポリシー

論文・Tdoc・Chair Notes・仕様書など、調査の一次情報は **必ず Markdown に変換して `references/` に保存する**。
これにより Obsidian のグラフビューで「どのノートがどの一次情報に基づくか」が可視化される。

このポリシーは全スキル・コマンドの上位ルール。`framework/skill-contract.md` から参照される。

---

## 0. 引用の実在検証ポリシー（最優先）

**Tdoc 番号・論文タイトル・著者名・arXiv ID・DOI・仕様番号は記憶から書かない。**
LLM が生成する引用情報は誤り率が高く（先行研究では AI 生成引用の誤り率が約 4 割）、本リポジトリの
Principle 1（一次情報の記録）を機械的に裏切る最大の経路となる。

引用する瞬間に、以下のいずれかで **実在を検証** する:

| 引用対象 | 検証手段 | 確認内容 |
|:---|:---|:---|
| 3GPP Tdoc | `framework/3gpp-ftp-cookbook.md` の手順で 3gpp.org FTP に当該ファイルが存在することを確認 | 番号・タイトル・寄稿者の一致 |
| arXiv 論文 | `https://arxiv.org/abs/<ID>` の解決を確認（WebFetch / curl） | タイトル・第一著者の一致 |
| DOI 付き論文 | `https://doi.org/<DOI>` の解決を確認 | タイトル・第一著者・年の一致 |
| 学術論文（DOI/arXiv なし） | WebSearch で `"<タイトル>" <第一著者>` を検索し1件以上ヒット | タイトル・第一著者・年の一致 |
| 3GPP 仕様書 | 3gpp.org の仕様ページで該当バージョンの存在を確認 | 仕様番号・バージョン・リリース |

**検証できない引用は本文に書かない**。書く必要があるなら以下のマーカーを残す:

```markdown
[要出典: <検索手がかり — 著者名・キーワード・推定タイトル等>]
```

そのうえで Next Steps に「実在確認: <マーカー対象>」を必ず積む。

**検証不要なケース**:

- すでに `references/` に保存済みの一次情報を `[[ファイル名]]` で wikilink する場合 — 保存時に検証済み
- `documents/` の既存ノートを wikilink する場合 — 引用ではなく内部参照
- 一般常識（OFDM、MIMO 等の用語そのもの）

**バッチ化の指針**: 1セッション中に同一引用を複数回参照する場合、初回のみ検証して結果を `references/` のノートに固定する。再検証は不要。

---

## 1. 保存対象

| 種別 | 例 | 変換手順 |
|:---|:---|:---|
| 学術論文（PDF） | arXiv、IEEE Xplore | [tools.md](./tools.md) §2 の `pdftotext -layout` で本文抽出 |
| 3GPP Tdoc（docx） | `R1-2503456.docx` | [tools.md](./tools.md) §1 の `pandoc -t gfm --wrap=none` で変換 |
| 3GPP Chair Notes（docx） | `Chair_Notes_RAN1#124b.docx` | 同上 |
| 仕様書（pdf/docx） | TS 38.211, TR 38.913 | docx があれば pandoc 優先。pdf のみなら `pdftotext -layout` |
| ベンダーホワイトペーパー | Qualcomm/Ericsson PDF | `pdftotext -layout` |
| Web 記事 | ブログ、ニュース | WebFetch / curl で本文取得し markdown 化 |

**保存しないもの**: 二次的な Wikipedia 抜粋、要旨だけしか入手できない情報源、URL のみで本文不要な情報源。

---

## 2. 命名規則

> **原則**: 論文の名前や寄書の番号を**そのまま**ファイル名に使う。日付プレフィックスは付けない（`documents/` の `yymmdd_` ルールは適用しない）。

| 一次情報の種類 | ファイル名の形 | 例 |
|:---|:---|:---|
| 3GPP Tdoc | `<Tdoc番号>.md` | `R1-2503456.md`、`R1-2601750.md` |
| arXiv 論文 | `arXiv-<ID>.md` | `arXiv-2508.08225.md`、`arXiv-2602.08163.md` |
| DOI 付き論文 | `<著者-第一著者>_<年>_<短いタイトル>.md` または `doi-<DOI のスラッシュをハイフンに置換>.md` | `Heath_2024_NearField-MIMO.md`、`doi-10.1109-jsac.2024.123456.md` |
| 3GPP 仕様書 | `<仕様番号>-v<バージョン>.md` | `TS38.211-v18.6.0.md`、`TR38.901-v17.0.0.md` |
| Chair Notes | `Chair-Notes-<会合略号>.md` | `Chair-Notes-RAN1-124bis.md` |
| ホワイトペーパー | `<ベンダー>_<短いタイトル>.md` | `Qualcomm_Making5GNRReality_2016.md` |
| Web 記事 | `<媒体>_<短いタイトル>_<YYYY-MM>.md` | `TheMobileNetwork_6Gmeeting_2025-08.md` |

- ファイル名にスペースは使わない（ハイフン or アンダースコア）
- 日本語タイトルは可だが、3GPP 文書番号や arXiv ID がある場合は番号を優先する
- 同じ文書の複数バージョンは末尾に `-v<番号>` を付けて区別

---

## 3. ファイル構造

各 references ノートは frontmatter + 抽出本文で構成する:

```markdown
---
title: "原文タイトル（言語そのまま）"
type: paper | tdoc | chair-notes | spec | whitepaper | web-article
source_url: https://...
accessed: YYYY-MM-DD
authors: []                  # 任意
year: YYYY                   # 任意
venue: ""                    # 会議・ジャーナル・3GPP 会合名
identifiers:
  arxiv: ""                  # 該当する場合のみ
  doi: ""
  tdoc: ""
  spec: ""
related:                     # documents/ 配下でこのリファレンスを引用しているノート
  - "[[260427_RAN1-124bis-DL-CSI-BM-AIML-調査]]"
---

# 原文タイトル

> 出典: [元 URL](https://...) 、アクセス日 YYYY-MM-DD
> 変換コマンド: `pandoc R1-XXXX.docx -t gfm --wrap=none -o R1-XXXX.md`

[本文抽出結果。pandoc/pdftotext の出力をそのまま貼る。整形はしない（情報の歪曲を避けるため）]
```

**抽出時の禁止事項**:

- 本文を要約して書き換えない（要約は `documents/` 側のノートで行う）
- 表が崩れていても無理に整形しない（読み手が原文に戻る前提）
- 機械翻訳結果を勝手に追加しない（必要なら別ノート `<元ファイル名>_ja.md` を作って併記）

---

## 4. リンクの張り方

- references ノートは **必ず `documents/` 配下のノートから wikilink で参照される** こと
- 引用するときは `documents/yymmdd_topic.md` の本文・脚注で `[[R1-2503456]]` のように張る
- references ノート側の frontmatter `related:` にも引用元 `documents/` ノートを記載し、双方向リンクを保つ
- 1つの references ノートが複数の `documents/` から参照されてよい（むしろ推奨）

---

## 5. 既存運用との関係

- これまで本文中に URL を埋めるだけだった一次情報も、再利用が見込まれるなら references 化する
- 一回読み捨ての URL は references 化せず、引用元ノートの `sources:` に URL だけ残す
- references ノート自体には特許・ライセンスに触れる原文をそのまま含むため、**公開情報の利用範囲を逸脱しない**（[principles.md](./principles.md) #5）。研究目的の引用に留め、改変公開しない
