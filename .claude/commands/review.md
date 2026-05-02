# /review — Review research notes / 研究ノートのレビュー

Check the quality of changed notes and produce review comments.

## Usage

```
/review              ← review staged changes (or HEAD~1 if none staged)
/review <file-path>  ← review a specific file
```

## Steps

1. Identify the target:
   - No argument → if `git diff --staged` exists, use it; otherwise use `git diff HEAD~1`
   - Argument given → read the specified file
2. Check against the invariant principles in `framework/principles.md`
3. Review against the five viewpoints below
4. Output the result to chat

## Review viewpoints

### 1. Source completeness (Principle 1)
- Do factual statements carry the URL of a primary source?
- Are document numbers (TS/TR/Tdoc) present?
- Is the access date recorded?

### 2. Implementation-constraint awareness (Principle 2)
- Are the paper's ideal assumptions accepted uncritically?
- Are gaps to 3GPP implementation constraints (DCI bit count, frame structure, sync offset) mentioned?

### 3. Generation comparison (Principle 3)
- Is there a section comparing with previous generations (for survey-topic)?
- Are the lessons of 5G considered?

### 4. Three-layer structure (Principle 4)
- Does it follow Why → What → How?
- Does it dive into technical details prematurely?

### 5. Six-axis coverage
- Are `axes:` in frontmatter recorded appropriately?
- Are applicable axes missing?
- Are `[要確認]` markers used appropriately?

### 6. Link hygiene ([`framework/linking-policy.md`](../../framework/linking-policy.md))
- Does either `up` / `related` (or the body) carry at least one wikilink (`[[...]]`)? (Not an orphan note)
- Are cited primary sources (papers, Tdocs, specs) rendered to Markdown under `references/`?
- Does the filename follow `yymmdd_<slug>.md` (documents) or the original number/title (references) convention?
- Do the cited `[[ファイル名]]` actually exist (no broken links)?

## Output format

```markdown
## レビュー: <ファイル名>

### 良い点
- ...

### 要改善
- [ ] [出典] ... に URL がない
- [ ] [実装制約] ... の論文前提が無批判に採用されている
- [ ] [6軸] 市場軸の記載が欠落している
- [ ] [リンク] 孤立ノート: up / related が空、本文に wikilink もない
- [ ] [references] arXiv 2602.08163 が引用されているが references/ に未保存
- [ ] [命名] yymmdd_ プレフィックスがない

### 提案
- ...
```