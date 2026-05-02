# /status — Overview of all research notes / 研究ノート全体の状態確認

List status / confidence for every note, and surface staleness, unreviewed entries, and link-hygiene problems.

## Steps

0. **Run KB Lint first**: execute `python tools/kb_lint.py --root . --report tools/kb_lint_report.md` and parse the JSON output. Use the lint result as the authoritative source for the four mechanical checks (orphan notes / broken wikilinks / documents without primary source / missing required frontmatter). Do not duplicate this check by hand.
1. Flat-scan every `.md` file (excluding README.md) under `documents/` and `references/`
2. Extract `status`, `confidence`, `updated`, `up`, `related` from each frontmatter
3. Read each body to count `[[...]]` wikilinks; cross-reference with the lint result for broken links and orphan notes
4. Output the listing in the format below, with the "要注意" section populated from the lint result

## Output format

```markdown
## 研究ノート ステータス一覧（YYYY-MM-DD 時点）

### 要注意
| ファイル | status | confidence | 最終更新 | リンク数 | 備考 |
|:---|:---|:---|:---|:---|:---|
| 260101_xxx.md | draft | low | 2026-01-15 | 0 | 孤立ノート / 3ヶ月以上未更新 |

### documents/（自分の調査ノート）
| ファイル | status | confidence | 最終更新 | up | リンク数 |
|:---|:---|:---|:---|:---|:---|
| 260421_xxx.md | reviewed | medium | 2026-04-21 | [[260420_yyy]] | 4 |

### references/（一次情報）
| ファイル | type | accessed | 被リンク数 |
|:---|:---|:---|:---|
| arXiv-2508.08225.md | paper | 2026-04-21 | 2 |

### 統計
- 全ノート数: documents N / references M
- draft: N / reviewed: N / stable: N / obsolete: N
- confidence low: N / medium: N / high: N
- 3ヶ月以上未更新: N
- 孤立ノート: N（kb_lint）
- リンク切れ: N（kb_lint）
- 一次情報未紐付け documents: N（kb_lint）
- frontmatter 必須フィールド欠損: N（kb_lint）
```

## "Needs attention" criteria

- `status: draft` and `updated` is over 30 days old
- `status: reviewed` and `updated` is over 90 days old
- `confidence: low` for over 60 days
- frontmatter is missing `status` or `axes`
- **Orphan note** (`up` and `related` both empty, zero body wikilinks, zero inbound links)
- **Broken link** (a `[[...]]` in body or frontmatter does not point to a real file)
- A note that no `references/` entry cites and whose `sources` are external URLs only (consider rendering to references)