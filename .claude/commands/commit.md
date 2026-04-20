# /commit — 研究ノートのコミット

変更内容を分析し、適切な粒度でコミットを生成する。

## 手順

1. `git status` と `git diff --staged` および `git diff` で変更内容を確認する
2. 変更ファイルをカテゴリ別に分類する:
   - `00_framework/` → フレームワーク変更
   - `10_topics/` → トピック追加・更新
   - `20_history/` → 世代分析
   - `30_meetings/` → 会合メモ
   - `40_ideas/` → アイデア・考察
   - `50_sources/` → 文献メモ
   - `.claude/` → スキル・コマンド変更
3. カテゴリごとに個別のコミットを作成する（細粒度コミット）
4. `git log --oneline -10` で直近のコミットスタイルを確認し、一貫性を保つ

## コミットメッセージ形式

```
<type>(<scope>): <日本語の説明>

<変更の背景・理由（任意）>
```

### type

| type | 用途 |
|:---|:---|
| `research` | トピック調査・論文メモの追加 |
| `analysis` | ギャップ分析・考察・接続メモ |
| `meeting` | 会合メモの追加・更新 |
| `framework` | 軸・レンズ・ペルソナ・テンプレの変更 |
| `docs` | README・その他ドキュメントの更新 |
| `chore` | 構造整理・リネーム・設定変更 |

### scope

ディレクトリまたはトピック名。例: `mimo`, `channel-coding`, `axes`, `personas`

### 例

```
research(mimo): Cell-Free Massive MIMO の初期調査ノートを追加
analysis(channel-coding): GRAND と LDPC の接続メモを作成
meeting(ran1-124): FFS 項目の抽出メモを追加
framework(personas): インド地域ペルソナを追加
```

## 禁止事項

- `git add -A` は使わない（意図しないファイルの混入を防ぐ）
- `.env` やクレデンシャル系ファイルをコミットしない
- `--no-verify` は使わない
