# /commit — Commit research notes / 研究ノートのコミット

Analyze changes and generate commits at appropriate granularity.

## Steps

1. Check changes with `git status`, `git diff --staged`, and `git diff`
2. Classify changed files by category:
   - `framework/` → framework changes (axes, lenses, templates, policies, personas)
   - `documents/` → your own research notes (flat, `yymmdd_<slug>.md`)
   - `references/` → primary sources rendered as Markdown (papers, Tdocs, specs)
   - `.claude/` → skill / command changes
   - `CLAUDE.md` / `README.md` / config → docs and configuration
3. Create separate commits per category (fine-grained commits)
4. Run `git log --oneline -10` to confirm recent commit style and stay consistent

## Commit message format

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

A directory name or topic name. Examples: `mimo`, `channel-coding`, `axes`, `personas`, `linking-policy`

### Examples

```
research(mimo): Cell-Free Massive MIMO の初期調査ノートを追加
analysis(channel-coding): GRAND と LDPC の接続メモを作成
reference(ran1-124bis): R1-2503456 を MD 化して references に追加
meeting(ran1-124): FFS 項目の抽出メモを追加
framework(linking-policy): Obsidian wikilink ルールを追加
chore(documents): 週フォルダ廃止に伴うリネーム
```

## Forbidden

- Do not use `git add -A` (prevent unintended file inclusion)
- Do not commit `.env` or credentials
- Do not use `--no-verify`