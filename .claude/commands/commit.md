# /commit — 研究ノートのコミット

変更内容を分析し、適切な粒度でコミットを生成する。

## 手順

1. `git status` と `git diff --staged` および `git diff` で変更内容を確認する
2. 変更ファイルをカテゴリ別に分類する:
   - `framework/` → フレームワーク変更（軸・レンズ・テンプレ・ポリシー・ペルソナ）
   - `documents/` → 自分の調査ノート（フラット、`yymmdd_<slug>.md`）
   - `references/` → 一次情報の MD 化（論文・Tdoc・仕様書）
   - `.claude/` → スキル・コマンド変更
   - `CLAUDE.md` / `README.md` / 設定 → ドキュメント・設定
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
| `research` | トピック調査・論文ダイジェストの追加（documents/） |
| `analysis` | ギャップ分析・考察・接続メモ（documents/） |
| `reference` | 一次情報の MD 化追加・更新（references/） |
| `meeting` | 会合関連メモ（documents/） |
| `framework` | 軸・レンズ・ペルソナ・ポリシー・テンプレの変更 |
| `docs` | README・CLAUDE.md・その他ドキュメントの更新 |
| `chore` | 構造整理・リネーム・設定変更 |

### scope

ディレクトリまたはトピック名。例: `mimo`, `channel-coding`, `axes`, `personas`, `linking-policy`

### 例

```
research(mimo): Cell-Free Massive MIMO の初期調査ノートを追加
analysis(channel-coding): GRAND と LDPC の接続メモを作成
reference(ran1-124bis): R1-2503456 を MD 化して references に追加
meeting(ran1-124): FFS 項目の抽出メモを追加
framework(linking-policy): Obsidian wikilink ルールを追加
chore(documents): 週フォルダ廃止に伴うリネーム
```

## 禁止事項

- `git add -A` は使わない（意図しないファイルの混入を防ぐ）
- `.env` やクレデンシャル系ファイルをコミットしない
- `--no-verify` は使わない
