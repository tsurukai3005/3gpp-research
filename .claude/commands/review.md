# /review — Review research notes / 研究ノートのレビュー

Check the quality of changed notes and produce a structured PASS/FAIL/PARTIAL/SKIP report.

## Usage

```
/review              ← review staged changes (or HEAD~1 if none staged)
/review <file-path>  ← review a specific file
```

## Steps

1. **Identify the target**:
   - No argument → if `git diff --staged` exists, use it; otherwise use `git diff HEAD~1`
   - Argument given → read the specified file
2. **Run KB Lint** for the target file: `python tools/kb_lint.py --root .` and extract issues that touch the target file (broken links, orphan, unsourced, missing frontmatter)
3. Read `framework/principles.md`, `framework/skill-contract.md`, `framework/references-policy.md`, `framework/linking-policy.md`
4. Score each viewpoint below as **PASS / FAIL / PARTIAL / SKIP** with a one-line reason
5. Output the report in the format below

## Scoring vocabulary

- **PASS**: the viewpoint is satisfied
- **FAIL**: the viewpoint is violated; this blocks promotion to `reviewed`
- **PARTIAL**: machine cannot decide; human judgement required, or the viewpoint is partially met
- **SKIP**: not applicable to this note's type (e.g. citation verification on a meta note)

## Review viewpoints

| # | Viewpoint | Source | How to decide |
|:---|:---|:---|:---|
| 1 | Wikilinks (orphan / broken) | [`framework/linking-policy.md`](../../framework/linking-policy.md) | KB Lint result for this file. PASS if 0 broken + not orphan |
| 2 | Frontmatter required fields | [`framework/skill-contract.md`](../../framework/skill-contract.md) | KB Lint result. PASS if `status` / `confidence` / `created` / `sources or references` present |
| 3 | Citation verification (§0) | [`framework/references-policy.md`](../../framework/references-policy.md) §0 | PASS if every Tdoc / arXiv / DOI / spec number cited has a `references/` entry or a `[要出典]` marker; PARTIAL if cannot verify; SKIP for meta notes |
| 4 | Claim-Evidence pairing | [`framework/templates/claim-evidence-block.md`](../../framework/templates/claim-evidence-block.md) | For paper digests: PASS if every Claim has Evidence/Method/Limitation/Project relevance; PARTIAL if some incomplete; SKIP for non-digest notes |
| 5 | Source completeness (Principle 1) | [`framework/principles.md`](../../framework/principles.md) #1 | Do factual statements carry primary-source URLs? TS/TR/Tdoc numbers explicit? Access date present? |
| 6 | Implementation-constraint awareness (Principle 2) | [`framework/principles.md`](../../framework/principles.md) #2 | Are paper assumptions accepted uncritically? Are 3GPP gap items mentioned? PARTIAL/SKIP allowed for pure-spec notes |
| 7 | Six-axis coverage | [`framework/skill-contract.md`](../../framework/skill-contract.md) frontmatter | Are `axes:` populated with at least the obvious ones? Is `[要確認]` used for low-confidence items? |
| 8 | Three-layer structure (Why / What / How) | [`framework/principles.md`](../../framework/principles.md) #4 | Does it follow the three layers? Or dive into details prematurely? |

## Output format

```markdown
## REVIEW REPORT: <ファイル名>

| # | Viewpoint                                  | Result   | Detail |
|:--|:-------------------------------------------|:---------|:-------|
| 1 | Wikilinks (orphan / broken)                | PASS     | 0 broken, 3 outbound links |
| 2 | Frontmatter required fields                | FAIL     | `confidence` missing |
| 3 | Citation verification (§0)                 | PARTIAL  | R1-2503456 not in references/ — verify before promotion |
| 4 | Claim-Evidence pairing                     | SKIP     | not a paper digest |
| 5 | Source completeness (Principle 1)          | PASS     | TS/Tdoc numbers and access dates present |
| 6 | Implementation-constraint awareness (P2)   | PARTIAL  | gap table exists but no signaling-overhead column |
| 7 | Six-axis coverage                          | PASS     | technology-layer, generation, value populated |
| 8 | Three-layer structure (Why/What/How)       | PASS     |  |

**Overall**: NOT READY (1 FAIL, 2 PARTIAL)

### Blocking issues (must fix)
1. [Frontmatter] `confidence` field is missing — add `confidence: medium` (or appropriate level)

### Non-blocking suggestions
- [Citation §0] R1-2503456 が本文で引用されているが `references/R1-2503456.md` 未作成。一次情報を pandoc で MD 化して保存
- [P2] ギャップテーブルに「signaling overhead」列を追加すると `digest-paper` 標準に揃う
```

**Overall verdict** is one of:

- **READY FOR REVIEWED**: all viewpoints PASS or SKIP
- **NOT READY**: at least one FAIL → list as Blocking issues
- **NEEDS HUMAN JUDGEMENT**: only PARTIAL/PASS/SKIP, no FAIL → user decides whether to promote
