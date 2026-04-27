# 3GPP Research — Claude の行動指針

## プロジェクトの目的

3GPP RAN1（MIMO・チャネルコーディング）の動向を体系的に把握し、
標準必須特許（SEP）のアイデアに繋がる知見をストックする個人プロジェクト。
公開情報のみを扱う。

## フレームワーク

調査・分析・記録の全ての行動は `framework/` のルールパーツに従う。

- **不変原則**: `framework/principles.md`
- **スキル契約**: `framework/skill-contract.md` — 全スキル共通の行動規範・禁止事項・出力スキーマ
- **分析軸（6軸）**: `framework/axes/` — 1軸1ファイル、全トピックに必ず適用
- **分析レンズ**: `framework/lenses/` — 状況に応じて適用するオプショナル視点
- **ペルソナ**: `framework/personas/` — 需要側の多面的モデル
- **問いかけテンプレ**: `framework/templates/` — スキルが参照する定型質問
- **レビューポリシー**: `framework/review-policy.md`
- **情報源リスト**: `framework/sources.md`
- **外部ツール運用**: `framework/tools.md` — pandoc 等の前処理コマンド（docx → md 等）
- **3GPP FTP 操作**: `framework/3gpp-ftp-cookbook.md` — Tdoc/Chair Notes 取得手順

## リポジトリ構造

```
3gpp-research/
├── framework/      ← 調査ルール・分析軸の定義
├── documents/      ← 全メモ（フラット、日付プレフィックス）
├── CLAUDE.md
└── README.md
```

### documents/ の命名規則

- 週ごとのフォルダ: `MM-DD_MM-DD/`（例: `2026-04-21_04-27/`）
- ファイル名: 内容の要約（日付なし、タグなし）
- 目的が混ざったメモも許容する
- 年またぎの場合: `2026-12-29_2027-01-04/`

## スキル一覧

| スキル | 用途 |
|:---|:---|
| `/survey-topic` | トピックを6軸で体系調査し `documents/` に記録 |
| `/analyze-gap` | 学術/3GPP/実装制約のギャップを3バケットで可視化 |
| `/success-pattern` | 過去世代の成功・失敗から6Gの条件を抽出 |
| `/digest-paper` | 論文を読み3GPP実装制約との差分を記録 |
| `/connect-dots` | トピック間の相乗効果・矛盾・組合せ価値を発見 |
| `/demand-reverse` | ペルソナの課題から技術候補を逆引き |
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