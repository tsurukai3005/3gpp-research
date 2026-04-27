# framework — 調査フレームワーク

このディレクトリは Claude の行動を規定するルールパーツの集合体。
CLAUDE.md からポインタで参照される。

## 構造

```
framework/
├── principles.md          ← 不変原則（全ての行動の基盤）
├── skill-contract.md      ← スキル契約（全スキル共通の Will / Will Not / 出力スキーマ・命名規則）
├── linking-policy.md      ← Obsidian wikilink ルール（孤立ノート禁止・階層は up/related で表現）
├── references-policy.md   ← 一次情報を references/ に MD 化して保存するルール
├── review-policy.md       ← レビューポリシー（軽量、後から拡張可能）
├── sources.md             ← 情報源リンク集
├── strategy-summary.md    ← 戦略文書の要約
├── tools.md               ← 外部ツール運用ガイド（pandoc 等の前処理コマンド）
├── 3gpp-ftp-cookbook.md   ← 3GPP FTP アクセスの実装ガイド
│
├── axes/                  ← 分析軸（1軸1ファイル）
│   必ず全トピックに適用する独立した座標軸。
│   軸を追加するには新ファイルを置くだけ。
│
├── lenses/                ← 分析レンズ（オプショナル）
│   状況に応じて適用する補助的視点。
│   軸とは異なり、常時適用ではない。
│
├── personas/              ← 需要側ペルソナ（1ペルソナ1ファイル）
│   地域・産業・ステークホルダーの3分類。
│   ペルソナ追加はファイルを置くだけ。
│
└── templates/             ← 問いかけテンプレート（1テンプレ1ファイル）
    スキルから参照される定型質問。
```

## サブフォルダの Map of Content

各サブフォルダには README.md を MoC（Map of Content）として置き、配下のファイルは
frontmatter `up:` でその MoC を親として参照する（[[linking-policy]]）。

- [[axes/README|axes/]]: 6軸の MoC
- [[lenses/README|lenses/]]: 状況依存レンズの MoC
- [[personas/README|personas/]]: 需要側ペルソナの MoC（地域・産業・ステークホルダー）
- [[templates/README|templates/]]: 各スキル用テンプレの MoC

## トップレベル文書

- [[principles]] — 不変原則6か条
- [[skill-contract]] — スキル契約・命名規則・frontmatter スキーマ
- [[linking-policy]] — Obsidian wikilink ルール
- [[references-policy]] — 一次情報の MD 化ルール
- [[review-policy]] — レビュー基準
- [[strategy-summary]] — 戦略文書要約
- [[sources]] — 情報源リスト
- [[tools]] — pandoc / pdftotext 運用
- [[3gpp-ftp-cookbook]] — 3GPP FTP アクセス手順

## 設計原則

- **1概念1ファイル**: 削除・入れ替え・追加が容易
- **上→下の一方向参照**: CLAUDE.md → framework → skills
- **軸とレンズの区別**: 軸=常時ON・直交、レンズ=状況依存ON・横断的
- **サブフォルダは MoC で集約**: 配下ファイルは README.md を `up:` で親として参照し、Obsidian グラフでハブが見える形にする
