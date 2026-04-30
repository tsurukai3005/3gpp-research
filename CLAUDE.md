# 3GPP Research — Claude の行動指針

## プロジェクトの目的

3GPP RAN1（MIMO・チャネルコーディング）の動向を体系的に把握し、
標準必須特許（SEP）のアイデアに繋がる知見をストックする個人プロジェクト。
公開情報のみを扱う。

## フレームワーク

調査・分析・記録の全ての行動は `framework/` のルールパーツに従う。

- **不変原則**: `framework/principles.md`
- **スキル契約**: `framework/skill-contract.md` — 全スキル共通の行動規範・禁止事項・出力スキーマ・命名規則
- **リンクポリシー**: `framework/linking-policy.md` — Obsidian wikilink、孤立ノート禁止、階層は `up`/`related` で表現
- **参考文献ポリシー**: `framework/references-policy.md` — 一次情報を `references/` に MD 化する命名・保存規則
- **分析軸（6軸）**: `framework/axes/` — 1軸1ファイル、全トピックに必ず適用
- **分析レンズ**: `framework/lenses/` — 状況に応じて適用するオプショナル視点
- **ペルソナ**: `framework/personas/` — 需要側の多面的モデル
- **問いかけテンプレ**: `framework/templates/` — スキルが参照する定型質問
- **メタデータカタログ**: `framework/catalog/` — RAN1 会合・アジェンダ・WI/SI の YAML カタログ（自然言語 → 安定 ID 解決の参照元）
- **レビューポリシー**: `framework/review-policy.md`
- **情報源リスト**: `framework/sources.md`
- **外部ツール運用**: `framework/tools.md` — pandoc 等の前処理コマンド（docx → md 等）
- **3GPP FTP 操作**: `framework/3gpp-ftp-cookbook.md` — Tdoc/Chair Notes 取得手順

## リポジトリ構造

```
3gpp-research/
├── framework/      ← 調査ルール・分析軸の定義
├── documents/      ← 自分の調査ノート（フラット、yymmdd_ プレフィックス）
├── references/     ← 一次情報（論文・Tdoc・仕様書）の MD 化（フラット、原文の番号/タイトル名）
├── CLAUDE.md
└── README.md
```

### documents/ の命名規則

- 全ファイルは `documents/` 直下に置く（フォルダ分けは保留）
- ファイル名: `yymmdd_<内容スラッグ>.md`
  - `yymmdd` は **作成日**（frontmatter `created` の年下2桁+月+日）
  - 例: `260421_NRフレーム構造の発表資料ドラフト.md`
- 同日に複数作る場合は内容スラッグで区別
- ノート間は **必ず Obsidian wikilink** (`[[ファイル名]]`) でつなぐ。孤立ノート禁止
- 階層は frontmatter の `up`（親ノート、0または1本）と `related`（兄弟、複数）で表現

### references/ の命名規則

- 論文・Tdoc・Chair Notes・仕様書を Markdown 化したものを保存
- ファイル名は **論文タイトル・寄書番号・arXiv ID をそのまま**（`yymmdd_` を付けない）
  - 例: `R1-2601750.md`、`arXiv-2508.08225.md`、`TS38.211-v18.6.0.md`、`Chair-Notes-RAN1-124bis.md`
- 詳細は `framework/references-policy.md`

## スキル一覧

| スキル | 用途 |
|:---|:---|
| `/survey-topic` | トピックを6軸で体系調査し `documents/` に記録 |
| `/analyze-gap` | 学術/3GPP/実装制約のギャップを3バケットで可視化 |
| `/success-pattern` | 過去世代の成功・失敗から6Gの条件を抽出 |
| `/digest-paper` | 論文を読み3GPP実装制約との差分を記録 |
| `/connect-dots` | トピック間の相乗効果・矛盾・組合せ価値を発見 |
| `/demand-reverse` | ペルソナの課題から技術候補を逆引き |
| `/trace-evolution` | 自然言語のトピック語から RAN1 議論変遷を縦に追い、会合横断のタイムラインを生成 |
| `/build-presentation` | 研究ノートから発表資料を4フェーズで段階構築 |

## コマンド一覧

| コマンド | 用途 |
|:---|:---|
| `/commit` | 変更をカテゴリ別に分類し、適切な粒度でコミット |
| `/review` | 研究ノートを不変原則・6軸の観点でレビュー |
| `/create-issue` | 研究タスクを GitHub Issue として登録 |
| `/weekly-summary` | 今週の研究活動サマリーと Next Steps 集約 |
| `/pr-template` | PR の説明文を自動生成 |
| `/status` | 全ノートの status/confidence 一覧と要注意ファイル |