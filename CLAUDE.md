# 3GPP Research — Claude の行動指針

## プロジェクトの目的

3GPP RAN1（MIMO・チャネルコーディング）の動向を体系的に把握し、
標準必須特許（SEP）のアイデアに繋がる知見をストックする個人プロジェクト。
公開情報のみを扱う。

## フレームワーク

調査・分析・記録の全ての行動は `00_framework/` のルールパーツに従う。

- **不変原則**: `00_framework/principles.md`
- **分析軸（6軸）**: `00_framework/axes/` — 1軸1ファイル、全トピックに必ず適用
- **分析レンズ**: `00_framework/lenses/` — 状況に応じて適用するオプショナル視点
- **ペルソナ**: `00_framework/personas/` — 需要側の多面的モデル
- **問いかけテンプレ**: `00_framework/templates/` — スキルが参照する定型質問
- **レビューポリシー**: `00_framework/review-policy.md`
- **情報源リスト**: `00_framework/sources.md`

## スキル一覧

| スキル | 用途 |
|:---|:---|
| `/survey-topic` | トピックを6軸で体系調査し `10_topics/` に記録 |
| `/analyze-gap` | 学術/3GPP/実装制約のギャップを3バケットで可視化 |
| `/success-pattern` | 過去世代の成功・失敗から6Gの条件を抽出 |
| `/digest-paper` | 論文を読み3GPP実装制約との差分を記録 |
| `/connect-dots` | トピック間の相乗効果・矛盾・組合せ価値を発見 |
| `/demand-reverse` | ペルソナの課題から技術候補を逆引き |

## コマンド一覧

| コマンド | 用途 |
|:---|:---|
| `/commit` | 変更をカテゴリ別に分類し、適切な粒度でコミット |
| `/review` | 研究ノートを不変原則・6軸の観点でレビュー |
| `/create-issue` | 研究タスクを GitHub Issue として登録 |
| `/weekly-summary` | 今週の研究活動サマリーと Next Steps 集約 |
| `/pr-template` | PR の説明文を自動生成 |
| `/status` | 全ノートの status/confidence 一覧と要注意ファイル |

## リポジトリ構造

| ディレクトリ | 役割 |
|:---|:---|
| `00_framework/` | 調査ルールの定義（メタ情報） |
| `10_topics/` | トピック別知識ベース（時系列を超えた概念整理） |
| `20_history/` | 過去世代の分析（普及要因の学び） |
| `30_meetings/` | 会合ごとのスナップショット（時点情報） |
| `40_ideas/` | アイデア・考察メモ |
| `50_sources/` | 読んだ文献のメモ |
