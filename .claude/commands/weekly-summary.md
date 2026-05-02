# /weekly-summary — Weekly research summary / 週次研究サマリー

Look back over this week's research activity and generate a summary.

## Steps

1. Get this week's commits with `git log --since="1 week ago" --oneline --all`
2. Get changed files with `git log --since="1 week ago" --name-only --all`
3. Build the summary in the structure below
4. Output the result to chat (saving is optional)

## Summary structure

```markdown
## 週次研究サマリー: YYYY-MM-DD 〜 YYYY-MM-DD

### 新規追加
- [[<ファイル名>]]: 概要1行（documents/ または references/）

### 更新
- [[<ファイル名>]]: 何を更新したか

### トピック別進捗

| トピック | status 変化 | confidence 変化 | メモ |
|:---|:---|:---|:---|
| ... | draft → reviewed | low → medium | ... |

### 今週の発見・気づき
- [自由記述: git diff から読み取れる知見の変化]

### 来週の Next Steps
- [各ノートの Next Steps セクションから集約]

### 統計
- 新規ファイル数: documents N / references M
- 更新ファイル数: N
- コミット数: N
```

## Aggregating Next Steps

Automatically collect unchecked items (`- [ ]`) from each note's `## Next Steps` section and gather them under "来週の Next Steps". This puts scattered TODOs in a single place.