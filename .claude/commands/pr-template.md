# /pr-template — Generate a PR description / PR 説明文の生成

Analyze the branch's changes and generate a PR description.

## Usage

```
/pr-template              ← summarize the current branch
/pr-template <PR number>  ← generate the description for an existing PR
```

## Steps

1. Identify the target:
   - No argument → use `git diff main...HEAD` to capture all changes on the current branch
   - PR number given → use `gh pr diff <number>` to capture the diff
2. Classify changed files by category
3. Generate the description from the template below
4. Output the result to chat

## Output template

```markdown
## 概要

[1-3 文で変更の目的を説明]

## 変更内容

### フレームワーク変更（framework/）
- ...

### スキル・コマンド（.claude/）
- ...

### 自分の調査ノート（documents/）
- ...

### 参考文献の MD 化（references/）
- ...

### ドキュメント・設定（CLAUDE.md / README.md / .obsidian / 設定）
- ...

## 該当する軸

[この PR で主に扱った軸を列挙]

## レビュー観点

- [ ] 出典の URL は記録されているか
- [ ] 一次情報は references/ に MD 化されているか
- [ ] 論文の理想仮定と 3GPP 実装制約の差が意識されているか
- [ ] 前世代との対比が含まれているか
- [ ] frontmatter の axes が適切に記録されているか
- [ ] frontmatter の up / related / references にリンクが入っているか（孤立ノートが生まれていないか）
- [ ] ファイル名は yymmdd_<slug>.md（documents/）または原文の番号/タイトル（references/）に従っているか
```