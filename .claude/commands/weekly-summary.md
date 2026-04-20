# /weekly-summary — 週次研究サマリー

今週の研究活動を振り返り、サマリーを生成する。

## 手順

1. `git log --since="1 week ago" --oneline --all` で今週のコミットを取得する
2. 変更されたファイルを `git log --since="1 week ago" --name-only --all` で取得する
3. 以下の構造でサマリーを生成する
4. 結果をチャットに出力する（保存は任意）

## サマリー構造

```markdown
## 週次研究サマリー: YYYY-MM-DD 〜 YYYY-MM-DD

### 新規追加
- [ファイル名](パス): 概要1行

### 更新
- [ファイル名](パス): 何を更新したか

### トピック別進捗

| トピック | status 変化 | confidence 変化 | メモ |
|:---|:---|:---|:---|
| ... | draft → reviewed | low → medium | ... |

### 今週の発見・気づき
- [自由記述: git diff から読み取れる知見の変化]

### 来週の Next Steps
- [各ノートの Next Steps セクションから集約]

### 統計
- 新規ファイル数: N
- 更新ファイル数: N
- コミット数: N
```

## Next Steps の集約

各ノートの `## Next Steps` セクションから未完了（`- [ ]`）の項目を
自動的に収集し、「来週の Next Steps」にまとめる。
これにより、散在する TODO が1箇所で確認できる。
